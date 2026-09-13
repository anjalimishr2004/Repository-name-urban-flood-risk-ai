# -*- coding: utf-8 -*-
"""
pages/2_AI_Preparedness.py
AI-powered flood preparedness recommendations page.
"""
import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from flood_utils import get_gemini_recommendations, calculate_scores

st.set_page_config(
    page_title="AI Preparedness · Urban Flood Risk AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.markdown("## 🤖 AI Preparedness")
    st.markdown("---")
    st.caption("Run a Risk Assessment first to pre-fill the inputs below.")

# ----------------------------------------------------------
# Page header
# ----------------------------------------------------------
st.markdown("""
<h2 style="color:#1c2b3a;font-weight:800;margin-bottom:4px;">🤖 AI Preparedness Recommendations</h2>
<p style="color:#6b7c93;margin-top:0;">AI-generated flood preparedness guidance for your location and conditions.</p>
""", unsafe_allow_html=True)

st.divider()

# ----------------------------------------------------------
# Input — pre-fill from session state if available
# ----------------------------------------------------------
prior = st.session_state.get("assessment", {})

st.markdown("### 📍 Assessment Inputs")
st.caption(
    "These fields are pre-filled from your last Risk Assessment. "
    "You can also edit them directly here."
)

col1, col2 = st.columns(2)
with col1:
    location = st.text_input("Location / City", value=prior.get("location", "Mumbai"))
    rainfall = st.number_input(
        "Rainfall (mm)", min_value=0.0, max_value=500.0,
        value=float(prior.get("rainfall", 100.0)), step=1.0
    )
with col2:
    drainage_opts = ["Good", "Moderate", "Poor"]
    drainage_default = prior.get("drainage", "Moderate")
    drainage = st.selectbox(
        "Drainage Condition", drainage_opts,
        index=drainage_opts.index(drainage_default)
    )
    area_opts = ["Normal", "Low-lying"]
    area_default = prior.get("area_type", "Normal")
    area_type = st.selectbox(
        "Area Type", area_opts,
        index=area_opts.index(area_default)
    )

flood_opts = ["No", "Yes"]
flood_default = prior.get("previous_flooding", "No")
previous_flooding = st.selectbox(
    "Previous Flooding Reported?", flood_opts,
    index=flood_opts.index(flood_default)
)

st.markdown("<br>", unsafe_allow_html=True)
run_ai = st.button(
    "🤖 Generate AI Recommendations", use_container_width=True, type="primary"
)

# ----------------------------------------------------------
# AI generation
# ----------------------------------------------------------
if run_ai:
    _, _, _, _, risk_score, risk = calculate_scores(
        rainfall, drainage, area_type, previous_flooding
    )

    st.divider()
    st.markdown(f"**Location:** {location} &nbsp;|&nbsp; **Risk Level:** {risk} &nbsp;|&nbsp; **Score:** {risk_score}/10")
    st.divider()

    st.markdown("### 💡 AI-Generated Flood Preparedness Recommendations")

    with st.spinner("Generating AI recommendations — please wait…"):
        ai_recs = get_gemini_recommendations(
            location=location,
            risk_score=risk_score,
            risk=risk,
            rainfall=rainfall,
            drainage=drainage,
            area_type=area_type,
            previous_flooding=previous_flooding,
        )

    if ai_recs:
        st.success("✅ AI recommendations generated successfully")
        st.markdown("<br>", unsafe_allow_html=True)

        for i, line in enumerate(ai_recs, 1):
            st.markdown(
                f'<div style="background:#f0f4f9;border-left:4px solid #1a6fc4;'
                f'border-radius:6px;padding:12px 18px;margin-bottom:10px;">'
                f'<span style="color:#1a6fc4;font-weight:700;">{i}.</span> '
                f'<span style="color:#1c2b3a;">{line}</span>'
                f'</div>',
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)
        st.caption(
            "⚠️ AI-generated content. These recommendations should be verified against "
            "official local authority advisories before acting on them. "
            "This is a decision-support tool, not an emergency management system."
        )

    else:
        st.markdown(
            '<div style="background:#fff8e1;border-left:4px solid #f39c12;'
            'border-radius:6px;padding:16px 20px;">'
            '<strong style="color:#e67e22;">AI recommendations are currently unavailable.</strong><br>'
            '<span style="color:#6b7c93;font-size:0.9rem;">'
            'The AI service may be temporarily unreachable. '
            'The rule-based recommendations on the '
            '<strong>Risk Assessment</strong> page remain fully active.'
            '</span></div>',
            unsafe_allow_html=True,
        )

else:
    st.markdown("""
    <div style="background:#f0f4f9;border-radius:10px;padding:32px;text-align:center;color:#6b7c93;">
      <div style="font-size:2rem;margin-bottom:8px;">🤖</div>
      <div style="font-weight:600;margin-bottom:6px;">Press the button above to generate AI recommendations</div>
      <div style="font-size:0.88rem;">The AI will analyse the location conditions and generate practical preparedness advice.</div>
    </div>
    """, unsafe_allow_html=True)


        
st.divider()
st.caption("Urban Flood Risk AI · SDG 11 + SDG 13")
