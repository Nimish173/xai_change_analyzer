# ui/pages/dashboard.py

import streamlit as st


def card(title, description, color, key):
    clicked = st.markdown(
        f"""
        <div style="
            padding:30px;
            border-radius:16px;
            background: {color};
            color:white;
            cursor:pointer;
            transition:0.25s;
            box-shadow:0 4px 14px rgba(0,0,0,0.12);
        ">
            <h3 style="margin-bottom:10px;">{title}</h3>
            <p style="font-size:16px;">{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Invisible button over card (hack for click)
    return st.button("", key=key)


def show_dashboard():
    st.markdown("## Welcome 👋")
    st.markdown("### Choose your analysis mode")

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if card(
            "✍️ Manual Analysis",
            "Analyze a single change with AI insights",
            "linear-gradient(135deg, #667eea, #764ba2)",
            "manual_card"
        ):
            st.session_state.page = "manual"
            st.rerun()

    with col2:
        if card(
            "📄 Bulk Analysis",
            "Upload Excel and process multiple changes",
            "linear-gradient(135deg, #11998e, #38ef7d)",
            "bulk_card"
        ):
            st.session_state.page = "bulk"
            st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ---------------- FEATURE CARDS ---------------- #
    st.markdown("### Platform Capabilities")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("🤖 AI Risk Prediction")

    with c2:
        st.info("📊 Smart Risk Scoring")

    with c3:
        st.warning("🔍 Similar Change Detection")