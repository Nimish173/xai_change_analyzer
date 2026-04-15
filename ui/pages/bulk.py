# ui/pages/bulk.py

import streamlit as st
import pandas as pd

from services.api import analyze_change
from utils.helpers import to_bool, get_value


def show_bulk_page():
    st.subheader("Bulk Analysis")

    uploaded_file = st.file_uploader("Upload Change Request Excel", type=["xlsx"])

    if not uploaded_file:
        return

    try:
        df = pd.read_excel(uploaded_file)

        st.success("Excel uploaded successfully ✅")
        st.info(f"Total rows detected: {len(df)}")
        st.write("Detected columns:", df.columns.tolist())

        if not any(col in df.columns for col in ["Description", "description", "Desc"]):
            st.warning("⚠️ No Description column found")

        if st.button("Run Bulk Analysis"):

            results = []

            with st.spinner("Analyzing all change requests... 🔍"):

                for _, row in df.iterrows():

                    payload = {
                        "description": get_value(row, ["Description", "description", "Desc"]),
                        "has_code_change": to_bool(get_value(row, ["Code Change", "code"])),
                        "has_rollback_plan": to_bool(get_value(row, ["Rollback", "rollback"])),
                        "performance_test_status": get_value(row, ["Performance", "performance"]).lower() or "done",
                        "approver_role": get_value(row, ["Approver", "approver"]).upper() or "L1",
                        "skip_ai": True
                    }

                    if not payload["description"]:
                        results.append({
                            "Description": "MISSING DESCRIPTION",
                            "Risk": "SKIPPED",
                            "Score": "-"
                        })
                        continue

                    res = analyze_change(payload)

                    if "error" in res:
                        results.append({
                            "Description": payload["description"][:60],
                            "Risk": "FAILED",
                            "Score": "-"
                        })
                    else:
                        results.append({
                            "Description": payload["description"][:60],
                            "Risk": res.get("risk_level", "UNKNOWN"),
                            "Score": res.get("risk_score", "-")
                        })

            df_result = pd.DataFrame(results)

            def color_risk(val):
                if val == "CRITICAL":
                    return "color: darkred"
                elif val == "HIGH":
                    return "color: red"
                elif val == "MEDIUM":
                    return "color: orange"
                elif val == "LOW":
                    return "color: green"
                return ""

            st.dataframe(df_result.style.map(color_risk, subset=["Risk"]))

    except Exception as e:
        st.error(f"Error reading Excel: {e}")