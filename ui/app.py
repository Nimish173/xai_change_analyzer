import streamlit as st

from pages.manual import show_manual_page
from pages.bulk import show_bulk_page
from components.styles import apply_global_styles

st.set_page_config(page_title="AI Change Analyzer", layout="wide")

# Apply styles
apply_global_styles()

# ---------------- STATE ---------------- #
if "page" not in st.session_state:
    st.session_state.page = "dashboard"

# ---------------- URL ROUTING (READ) ---------------- #
query_params = st.query_params

if "page" in query_params:
    st.session_state.page = query_params["page"]

# ---------------- HEADER ---------------- #
st.markdown("""
<div style="text-align:center;">
    <h1 class="app-title">AI Change Analyzer</h1>
    <p class="app-subtitle">Smart analysis for safer deployments 🚀</p>
</div>
""", unsafe_allow_html=True)

# Back button
col1, col2 = st.columns([8, 1])
with col2:
    if st.session_state.page != "dashboard":
        if st.button("Back"):
            st.session_state.page = "dashboard"
            st.query_params.clear()
            st.rerun()

st.markdown("---")

# ---------------- DASHBOARD ---------------- #
if st.session_state.page == "dashboard":

    st.markdown('<div class="center-text">', unsafe_allow_html=True)

    st.subheader("Select Mode")
    st.caption("Choose how you want to analyze your change request")

    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # -------- MANUAL CARD --------
    with col1:
        st.markdown(f"""
            <a href="?page=manual" style="text-decoration: none;">
                <div class="custom-card">
                    <img src="https://cdn-icons-png.flaticon.com/512/5623/5623395.png" class="btn-icon"/>
                    <div>
                        <div class="btn-title">Manual Analysis</div>
                        <div class="btn-sub">Analyze a single change</div>
                    </div>
                </div>
            </a>
        """, unsafe_allow_html=True)

    # -------- BULK CARD --------
    with col2:
        st.markdown(f"""
            <a href="?page=bulk" style="text-decoration: none;">
                <div class="custom-card">
                    <img src="https://cdn-icons-png.flaticon.com/512/4856/4856667.png" class="btn-icon"/>
                    <div>
                        <div class="btn-title">Bulk Analysis</div>
                        <div class="btn-sub">Upload and process multiple</div>
                    </div>
                </div>
            </a>
        """, unsafe_allow_html=True)

# ---------------- ROUTING ---------------- #
elif st.session_state.page == "manual":
    show_manual_page()

elif st.session_state.page == "bulk":
    show_bulk_page()