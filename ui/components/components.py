# ui/components/components.py

import streamlit as st


def render_risk_bar(score, risk_level):
    if risk_level == "LOW":
        color = "green"
    elif risk_level == "MEDIUM":
        color = "orange"
    else:
        color = "red"

    st.progress(score / 100)

    st.markdown(
        f"<h3 style='color:{color}; text-align:center;'>{score} / 100</h3>",
        unsafe_allow_html=True
    )


def render_issues(issues):
    if issues:
        for issue in issues:
            st.error(issue)
    else:
        st.success("No major issues found")


def render_breakdown(breakdown):
    if breakdown:
        st.subheader("Score Breakdown")

        total = 0
        for item in breakdown:
            reason = item.get("reason", "")
            st.warning(f"+{item['points']} → {item['rule']}")

            if reason:
                st.caption(reason)

            total += item["points"]

        st.markdown("---")
        st.success(f"Total Score: {total}")
    else:
        st.info("No risk contributions. Score is minimal.")