import streamlit as st


def apply_global_styles():
    st.markdown("""
    <style>

    /* -------- MAIN BUTTONS (SAFE) -------- */
    div.stButton > button[kind="secondary"] {
        height: 160px;
        font-size: 18px;
        font-weight: 600;
        border-radius: 14px;
        border: 1px solid #e5e7eb;
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        border-color: #2563eb;
        color: #2563eb;
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    }

    /* -------- BACK BUTTON -------- */
    button[kind="secondary"] {
        height: 34px !important;
        font-size: 13px !important;
    }

    /* -------- CENTER TEXT -------- */
    .center-text {
        text-align: center;
        margin-bottom: 10px;
    }

    /* -------- PAGE SPACING -------- */
    .block-container {
        padding-top: 2rem;
        padding-left: 6rem;
        padding-right: 6rem;
    }

    /* -------- CUSTOM CARD BUTTON -------- */
    .custom-card {
        width: 100%;
        height: 160px;
        border-radius: 14px;
        border: 1px solid #e5e7eb;
        background: inherit;
        display: flex;
        align-items: center;
        gap: 15px;
        padding: 20px;
        cursor: pointer;
        transition: all 0.25s ease;
    }

    .custom-card:hover {
        border-color: #2563eb;
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15); /* slightly stronger for dark */
    }

    .btn-icon {
        width: 50px;
        height: 50px;
    }

    .btn-title {
        font-size: 18px;
        font-weight: 600;
        color: inherit;
    }

    .btn-sub {
        font-size: 13px;
        color: #6b7280;
    }

    .custom-card:hover .btn-title {
        color: #2563eb;
    }

    .custom-card:hover .btn-icon {
        transform: scale(1.05);
    }

    a {
        display: block;
    }

    /* -------- FIX FILE UPLOADER (DARK MODE SAFE) -------- */
    section[data-testid="stFileUploader"] * {
        color: inherit !important;
    }

    section[data-testid="stFileUploader"] button {
        background: transparent !important;
        color: inherit !important;
        border: 1px solid #e5e7eb;
    }

    section[data-testid="stFileUploader"] button:hover {
        border-color: #2563eb;
        color: #2563eb;
    }
                
    /* -------- HEADER -------- */
    .app-title {
        font-size: 42px;
        font-weight: 700;
        background: linear-gradient(90deg, #2563eb, #7c3aed);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
        text-align: center;
    }
                
    .app-title {
        animation: fadeIn 0.6s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-8px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .app-subtitle {
        font-size: 15px;
        color: #9ca3af;
        text-align: center;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)