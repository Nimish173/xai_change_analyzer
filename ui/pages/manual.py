# ui/pages/manual.py

import streamlit as st

from services.api import analyze_change
from utils.helpers import get_risk_color
from components.components import render_risk_bar, render_issues, render_breakdown

def show_manual_page():
    st.subheader("Manual Change Analysis")

    description = st.text_area("Enter Change Description")

    col1, col2 = st.columns(2)

    with col1:
        has_code_change = st.checkbox("Code Change Included?")
        performance_test_status = st.selectbox(
            "Performance Test Status",
            ["done", "waived", "not_done"]
        )

    with col2:
        has_rollback_plan = st.checkbox("Rollback Plan Available?")
        approver_role = st.selectbox(
            "Approver Role",
            ["L1", "L2", "L3", "L4", "SLT"]
        )

    if st.button("Analyze Change"):

        if not description.strip():
            st.warning("Please enter change description")
            return

        payload = {
            "description": description,
            "has_code_change": has_code_change,
            "has_rollback_plan": has_rollback_plan,
            "performance_test_status": performance_test_status,
            "approver_role": approver_role,
            "skip_ai": False
        }

        with st.spinner("Analyzing change... 🔍"):
            result = analyze_change(payload)

        if "error" in result:
            st.error(result["error"])
            return

        st.success("Analysis Complete ✅")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Summary")
            st.info(result.get("summary"))

        with col2:
            risk = result.get("risk_level", "LOW")
            score = result.get("risk_score", 0)
            color = get_risk_color(risk)

            st.markdown(f"<h3 style='color:{color};'>{risk}</h3>", unsafe_allow_html=True)
            render_risk_bar(score, risk)

        st.markdown("---")
        render_issues(result.get("issues", []))

        st.markdown("---")
        breakdown = sorted(
            result.get("breakdown", []),
            key=lambda x: x["points"],
            reverse=True
        )
        render_breakdown(breakdown)

        st.markdown("---")
        st.subheader("🔍 Similar Past Changes")

        similar_cases = result.get("similar_cases", [])

        if similar_cases:
            for case in similar_cases:
                with st.expander(f"📝 {case['description'][:80]}"):
                    st.write(f"⚠️ Risk: {case['risk']}")
                    st.write(f"❗ Issues: {case['issues']}")
                    st.write(f"📊 Match Score: {round(case['score'] * 100, 2)}%")
        else:
            st.info("No similar past changes found")

        if breakdown:
            top_issue = breakdown[0]
            st.markdown("---")
            st.error(
                f"🔥 Fix this first: {top_issue['rule']} (+{top_issue['points']} impact)"
            )