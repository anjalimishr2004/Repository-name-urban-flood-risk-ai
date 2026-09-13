# -*- coding: utf-8 -*-

import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Urban Flood Risk AI",
    page_icon="🌧️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# BACKGROUND IMAGE
# ---------------------------------------------------------

image_path = Path("flood_city.jpg")

if image_path.exists():
    image_base64 = base64.b64encode(
        image_path.read_bytes()
    ).decode()
else:
    image_base64 = ""

# ---------------------------------------------------------
# DESIGN / CSS
# ---------------------------------------------------------

st.markdown(
    f"""
    <style>

    /* Main page background */
    [data-testid="stAppViewContainer"] {{
        background:
            linear-gradient(
                rgba(5, 20, 32, 0.62),
                rgba(5, 20, 32, 0.72)
            ),
            url("data:image/jpeg;base64,{image_base64}")
            center center / cover fixed no-repeat !important;
    }}

    [data-testid="stMain"] {{
        background: transparent !important;
    }}

    .block-container {{
        background: transparent !important;
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
    }}

    /* Top header */
    [data-testid="stHeader"] {{
        background: transparent !important;
    }}

    /* Sidebar */
    [data-testid="stSidebar"] {{
        background: rgba(12, 30, 45, 0.97) !important;
    }}

    [data-testid="stSidebar"] * {{
        color: #f4f8fb !important;
    }}

    /* Main text */
    [data-testid="stAppViewContainer"] h1,
    [data-testid="stAppViewContainer"] h2,
    [data-testid="stAppViewContainer"] h3 {{
        color: white !important;
        font-weight: 800 !important;
    }}

    [data-testid="stAppViewContainer"] p,
    [data-testid="stAppViewContainer"] label,
    [data-testid="stAppViewContainer"] .stCaption {{
        color: #f2f6f9 !important;
    }}

    /* Glass cards */
    [data-testid="stVerticalBlockBorderWrapper"] {{
        background: rgba(255, 255, 255, 0.17) !important;
        border: 1px solid rgba(255, 255, 255, 0.38) !important;
        border-radius: 18px !important;
        box-shadow: 0 8px 28px rgba(0, 0, 0, 0.25) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
    }}

    [data-testid="stVerticalBlockBorderWrapper"] p,
    [data-testid="stVerticalBlockBorderWrapper"] h1,
    [data-testid="stVerticalBlockBorderWrapper"] h2,
    [data-testid="stVerticalBlockBorderWrapper"] h3 {{
        color: white !important;
    }}

    /* Buttons */
    .stButton > button,
    .stButton > button p,
    .stButton > button span {{
        background: rgba(255, 255, 255, 0.96) !important;
        color: #17324a !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 800 !important;
        min-height: 44px !important;
        opacity: 1 !important;
    }}

    .stButton > button:hover,
    .stButton > button:hover p,
    .stButton > button:hover span {{
        background: white !important;
        color: #0b5fa5 !important;
    }}

    /* Divider */
    hr {{
        border-color: rgba(255, 255, 255, 0.25) !important;
    }}

    /* Select/input boxes if present */
    [data-testid="stTextInput"] input,
    [data-testid="stNumberInput"] input {{
        background: rgba(255, 255, 255, 0.92) !important;
        color: #172536 !important;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:
    st.title("🌧️ Urban Flood Risk AI")

    st.caption(
        "AI-assisted urban flood risk assessment "
        "and preparedness"
    )

    st.divider()

    st.write("🎯 **SDG 11** · Sustainable Cities")
    st.write("🌍 **SDG 13** · Climate Action")

    st.divider()

    st.caption(
        "Use the navigation menu to explore the application."
    )

# ---------------------------------------------------------
# HOME HERO
# ---------------------------------------------------------

st.title("🌧️ Urban Flood Risk AI")

st.markdown(
    "### AI-powered flood risk assessment and preparedness"
)

st.write(
    "Helping urban communities understand flood risk, "
    "prepare for extreme rainfall, and build safer "
    "and more resilient cities."
)

st.caption(
    "AI FOR SUSTAINABILITY • 1M1B INTERNSHIP PROJECT"
)

st.divider()

# ---------------------------------------------------------
# EXPLORE APPLICATION
# ---------------------------------------------------------

st.markdown("## 🚀 Explore the Application")

st.write(
    "Choose a module below to assess risk, prepare for floods, "
    "explore insights, and learn about responsible AI."
)

st.write("")

# ---------------------------------------------------------
# ROW 1
# ---------------------------------------------------------

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    with st.container(border=True):
        st.markdown("### 🌊 Risk Assessment")
        st.write(
            "Assess urban flood risk using rainfall, "
            "drainage, area type, and previous flooding."
        )

        if st.button(
            "Open Risk Assessment →",
            key="risk_button",
            use_container_width=True,
        ):
            st.switch_page("pages/1_Risk_Assessment.py")


with col2:
    with st.container(border=True):
        st.markdown("### 🤖 AI Preparedness")
        st.write(
            "Generate practical AI-powered flood "
            "preparedness recommendations."
        )

        if st.button(
            "Open AI Preparedness →",
            key="ai_button",
            use_container_width=True,
        ):
            st.switch_page("pages/2_AI_Preparedness.py")


with col3:
    with st.container(border=True):
        st.markdown("### 📊 Flood Insights")
        st.write(
            "Explore rainfall, flood risk patterns, "
            "and useful urban flood insights."
        )

        if st.button(
            "Open Flood Insights →",
            key="insights_button",
            use_container_width=True,
        ):
            st.switch_page("pages/3_Flood_Insights.py")

# ---------------------------------------------------------
# ROW 2
# ---------------------------------------------------------

st.write("")

col4, col5, col6 = st.columns(3, gap="medium")

with col4:
    with st.container(border=True):
        st.markdown("### 🚨 Emergency & Safety")
        st.write(
            "Access important flood safety guidance "
            "and emergency preparedness information."
        )

        if st.button(
            "Open Emergency & Safety →",
            key="emergency_button",
            use_container_width=True,
        ):
            st.switch_page("pages/4_Emergency_Safety.py")


with col5:
    with st.container(border=True):
        st.markdown("### 🛡️ Responsible AI")
        st.write(
            "Understand transparency, privacy, "
            "limitations, and responsible AI use."
        )

        if st.button(
            "Open Responsible AI →",
            key="responsible_button",
            use_container_width=True,
        ):
            st.switch_page("pages/5_Responsible_AI.py")

with col6:
    with st.container(border=True):
        st.markdown("### 🌍 Sustainability")
        st.write(
            "Supporting safer, more resilient, and "
            "climate-ready urban communities."
        )

        st.button(
            "SDG 11 + SDG 13",
            key="sdg_button",
            use_container_width=True,
        )

# ---------------------------------------------------------
# SDG SECTION
# ---------------------------------------------------------

st.write("")
st.divider()

st.markdown("## 🌱 Sustainability Goals")

sdg1, sdg2 = st.columns(2, gap="medium")

with sdg1:
    with st.container(border=True):
        st.markdown("### 🎯 SDG 11 — Sustainable Cities")
        st.write(
            "Promoting safer, inclusive, resilient, "
            "and sustainable urban communities."
        )

with sdg2:
    with st.container(border=True):
        st.markdown("### 🌍 SDG 13 — Climate Action")
        st.write(
            "Supporting climate preparedness and "
            "community resilience against extreme weather."
        )

st.write("")
st.caption(
    "Urban Flood Risk AI · AI for Sustainability · SDG 11 + SDG 13"
)