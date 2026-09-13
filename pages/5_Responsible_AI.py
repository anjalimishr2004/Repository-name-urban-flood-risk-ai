# -*- coding: utf-8 -*-
"""
pages/5_Responsible_AI.py
Transparency, privacy, human oversight, model limitations, AI disclaimers.
"""

import streamlit as st

st.set_page_config(
    page_title="Responsible AI · Urban Flood Risk AI",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.markdown("## ⚖️ Responsible AI")
    st.markdown("---")
    st.caption(
        "Transparency, privacy, human oversight, and model limitation disclosures."
    )

st.markdown("""
<h2 style="color:#1c2b3a;font-weight:800;margin-bottom:4px;">⚖️ Responsible AI</h2>
<p style="color:#6b7c93;margin-top:0;">
  Our commitment to transparent, fair, and safe use of AI in flood risk assessment.
</p>
""", unsafe_allow_html=True)

st.divider()

# ----------------------------------------------------------
# Principles
# ----------------------------------------------------------
principles = [
    {
        "icon": "🔍",
        "title": "Transparency",
        "color": "#1a6fc4",
        "bg": "#eef2f7",
        "body": (
            "The flood risk score is calculated using a fully rule-based formula. "
            "Every input factor and its exact contribution to the score is shown "
            "explicitly in the Risk Assessment output. There is no hidden weighting, "
            "black-box model, or opaque process involved in the scoring. "
            "The source code for this project is available for inspection.\n\n"
            "When IBM watsonx.ai is used to generate recommendations, the source "
            "(IBM watsonx.ai — Granite foundation model) is clearly labelled in the UI."
        ),
    },
    {
        "icon": "🔒",
        "title": "Privacy",
        "color": "#27ae60",
        "bg": "#eafaf1",
        "body": (
            "This prototype does not collect, store, log, or transmit any personally "
            "identifiable information. The location name entered by the user is used "
            "only for display and for constructing the prompt sent to IBM watsonx.ai. "
            "No user data is retained between sessions. No analytics, cookies, or "
            "tracking are enabled."
        ),
    },
    {
        "icon": "👤",
        "title": "Human Oversight",
        "color": "#8e44ad",
        "bg": "#f5eef8",
        "body": (
            "This tool is explicitly a **decision-support aid**, not a decision-making "
            "system. All flood risk assessments and AI-generated recommendations must "
            "be reviewed and validated by a qualified human before any action is taken. "
            "The tool does not replace official flood warning systems, emergency "
            "services, local government advisories, or civil defence authorities. "
            "In any emergency situation, the instructions of official local authorities "
            "take absolute precedence over any output from this tool."
        ),
    },
    {
        "icon": "⚠️",
        "title": "Avoiding Misleading Predictions",
        "color": "#e67e22",
        "bg": "#fef3e2",
        "body": (
            "The risk score is a **simplified rule-based estimate**, not a "
            "scientifically validated flood prediction model. It does not incorporate "
            "real-time hydrological data, satellite imagery, river levels, soil "
            "saturation, or urban drainage network capacity. "
            "A **LOW** score does not guarantee that flooding will not occur. "
            "A **HIGH** score does not guarantee that flooding will occur. "
            "This tool should never be used as the sole basis for emergency "
            "decisions, evacuation orders, or public safety communications."
        ),
    },
    {
        "icon": "⚖️",
        "title": "Fairness",
        "color": "#c0392b",
        "bg": "#fdecea",
        "body": (
            "The same scoring rules are applied uniformly to all inputs, regardless "
            "of location. However, the model does not account for hyperlocal factors "
            "such as proximity to rivers or coastlines, soil permeability, underground "
            "drainage network capacity, urban heat island effects, or population density. "
            "Results should always be interpreted alongside local knowledge and expert "
            "judgment."
        ),
    },
    {
        "icon": "🤖",
        "title": "AI-Generated Recommendation Disclaimer",
        "color": "#1a6fc4",
        "bg": "#eef2f7",
        "body": (
            "When IBM watsonx.ai (Granite) is used to generate flood preparedness "
            "recommendations, the output is produced by a large language model and "
            "may contain inaccuracies, omissions, or context-specific errors. "
            "AI-generated recommendations are labelled clearly in the interface. "
            "Users must verify all AI-generated content against official guidance "
            "from local authorities, IMD, NDMA, and other relevant agencies before "
            "acting on it. IBM watsonx.ai is used here as an assistive tool, not as "
            "an authoritative emergency information source."
        ),
    },
]

for p in principles:
    st.markdown(
        f'<div style="background:{p["bg"]};border-left:5px solid {p["color"]};'
        f'border-radius:8px;padding:18px 22px;margin-bottom:14px;">'
        f'<div style="font-size:1rem;font-weight:700;color:{p["color"]};margin-bottom:6px;">'
        f'{p["icon"]} {p["title"]}</div>'
        f'<div style="color:#1c2b3a;font-size:0.9rem;line-height:1.65;">'
        + p["body"].replace("\n\n", "<br><br>") +
        f'</div></div>',
        unsafe_allow_html=True,
    )

st.divider()

# ----------------------------------------------------------
# SDG alignment
# ----------------------------------------------------------
st.markdown("### 🌐 SDG Alignment")

sdg_c1, sdg_c2 = st.columns(2)

with sdg_c1:
    st.markdown(
        '<div style="background:#eef2f7;border-radius:8px;padding:18px 22px;">'
        '<div style="font-weight:700;color:#1a6fc4;font-size:1rem;margin-bottom:6px;">'
        '🎯 SDG 11 — Sustainable Cities and Communities (Primary)</div>'
        '<div style="color:#4a5568;font-size:0.88rem;line-height:1.6;">'
        'This project directly supports SDG 11 by providing a decision-support tool '
        'that helps urban residents and planners understand and prepare for flood risk, '
        'contributing to safer and more resilient cities.'
        '</div></div>',
        unsafe_allow_html=True,
    )

with sdg_c2:
    st.markdown(
        '<div style="background:#eef2f7;border-radius:8px;padding:18px 22px;">'
        '<div style="font-weight:700;color:#1a6fc4;font-size:1rem;margin-bottom:6px;">'
        '🌍 SDG 13 — Climate Action (Secondary)</div>'
        '<div style="color:#4a5568;font-size:0.88rem;line-height:1.6;">'
        'Urban flooding is a direct consequence of changing precipitation patterns '
        'driven by climate change. This tool supports climate adaptation by enabling '
        'informed preparedness at the community level.'
        '</div></div>',
        unsafe_allow_html=True,
    )

st.divider()

# ----------------------------------------------------------
# IBM BOB
# ----------------------------------------------------------


st.divider()
st.caption("Urban Flood Risk AI · AI for Sustainability · SDG 11 + SDG 13")
