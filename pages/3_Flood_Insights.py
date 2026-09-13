# -*- coding: utf-8 -*-
"""
pages/3_Flood_Insights.py
Visual breakdown of risk factor contributions using Streamlit charts.
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from flood_utils import calculate_scores, RISK_COLOR, RISK_BG

st.set_page_config(
    page_title="Flood Insights · Urban Flood Risk AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.markdown("## 📈 Flood Insights")
    st.markdown("---")
    st.caption("Visual breakdown of risk factors and their contributions.")

st.markdown("""
<h2 style="color:#1c2b3a;font-weight:800;margin-bottom:4px;">📈 Flood Risk Insights</h2>
<p style="color:#6b7c93;margin-top:0;">Visual analysis of how each factor contributes to the overall flood risk score.</p>
""", unsafe_allow_html=True)
st.divider()

# ----------------------------------------------------------
# Input — pre-fill from session state if available
# ----------------------------------------------------------
prior = st.session_state.get("assessment", {})

with st.expander("🔧 Adjust Inputs", expanded=not bool(prior)):
    col1, col2 = st.columns(2)
    with col1:
        location = st.text_input("Location", value=prior.get("location", "Mumbai"))
        rainfall = st.number_input(
            "Rainfall (mm)", min_value=0.0, max_value=500.0,
            value=float(prior.get("rainfall", 100.0)), step=1.0
        )
    with col2:
        d_opts = ["Good", "Moderate", "Poor"]
        drainage = st.selectbox(
            "Drainage Condition", d_opts,
            index=d_opts.index(prior.get("drainage", "Moderate"))
        )
        a_opts = ["Normal", "Low-lying"]
        area_type = st.selectbox(
            "Area Type", a_opts,
            index=a_opts.index(prior.get("area_type", "Normal"))
        )
    f_opts = ["No", "Yes"]
    previous_flooding = st.selectbox(
        "Previous Flooding", f_opts,
        index=f_opts.index(prior.get("previous_flooding", "No"))
    )
    recalc = st.button("📊 Update Insights", type="primary", use_container_width=True)

# Use session state if no new button press
if recalc or prior:
    rs, ds, as_, hs, risk_score, risk = calculate_scores(
        rainfall, drainage, area_type, previous_flooding
    )
else:
    # Show placeholder
    st.markdown("""
    <div style="background:#f0f4f9;border-radius:10px;padding:32px;text-align:center;color:#6b7c93;">
      <div style="font-size:2rem;margin-bottom:8px;">📈</div>
      <div style="font-weight:600;">Expand the inputs above and press Update Insights</div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

color = RISK_COLOR[risk]
bg    = RISK_BG[risk]

# ----------------------------------------------------------
# Summary row
# ----------------------------------------------------------
st.markdown(f"""
<div style="background:{bg};border-left:6px solid {color};
            border-radius:8px;padding:14px 20px;margin:16px 0;">
  <span style="font-size:1.1rem;font-weight:800;color:{color};">
    {{"HIGH":"🔴","MEDIUM":"🟡","LOW":"🟢"}}[risk] {location} — {risk} RISK &nbsp;·&nbsp; Score: {risk_score}/10
  </span>
</div>
""".replace('{{"HIGH":"🔴","MEDIUM":"🟡","LOW":"🟢"}}[risk]',
            {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}[risk]),
    unsafe_allow_html=True,
)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Score", f"{risk_score}/10")
m2.metric("Risk Level", risk)
m3.metric("Max Possible", "10")
m4.metric("Score %", f"{risk_score * 10}%")

st.divider()

# ----------------------------------------------------------
# Bar chart — factor contributions
# ----------------------------------------------------------
st.markdown("### 📊 Factor Contribution Breakdown")

try:
    import pandas as pd

    factors_df = pd.DataFrame({
        "Factor": ["🌧️ Rainfall", "🚰 Drainage", "🏘️ Area Type", "🌊 Flood History"],
        "Score":  [rs, ds, as_, hs],
        "Max":    [3, 3, 2, 2],
    })
    factors_df["% of Max"] = (factors_df["Score"] / factors_df["Max"] * 100).round(1)

    st.bar_chart(
        factors_df.set_index("Factor")["Score"],
        color=color,
        use_container_width=True,
        height=280,
    )

    st.dataframe(
        factors_df[["Factor", "Score", "Max", "% of Max"]],
        use_container_width=True,
        hide_index=True,
    )

except ImportError:
    # pandas not available — fall back to metrics
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🌧️ Rainfall", f"{rs}/3")
    c2.metric("🚰 Drainage", f"{ds}/3")
    c3.metric("🏘️ Area Type", f"{as_}/2")
    c4.metric("🌊 Flood History", f"{hs}/2")

st.divider()

# ----------------------------------------------------------
# Condition insights
# ----------------------------------------------------------
st.markdown("### 🔍 Condition Insights")

col_l, col_r = st.columns(2)

with col_l:
    st.markdown("**🌧️ Rainfall Analysis**")
    if rainfall >= 150:
        st.error(f"Extreme: {rainfall} mm — Well above safe drainage thresholds.")
    elif rainfall >= 75:
        st.warning(f"Elevated: {rainfall} mm — May stress drainage systems.")
    else:
        st.success(f"Moderate: {rainfall} mm — Below typical stress threshold.")

    st.markdown("**🏘️ Area Type**")
    if area_type == "Low-lying":
        st.warning("Low-lying terrain — Water accumulates and drains slowly in this area.")
    else:
        st.success("Normal terrain — Not classified as a water accumulation zone.")

with col_r:
    st.markdown("**🚰 Drainage Condition**")
    if drainage == "Poor":
        st.error("Poor — Drainage infrastructure is significantly limited.")
    elif drainage == "Moderate":
        st.warning("Moderate — Drainage may become overwhelmed under heavy rain.")
    else:
        st.success("Good — Drainage infrastructure is functioning well.")

    st.markdown("**🌊 Flooding History**")
    if previous_flooding == "Yes":
        st.warning("Flooding previously reported — This area has a known vulnerability record.")
    else:
        st.success("No prior flooding reported — No historical vulnerability on record.")

st.divider()

# ----------------------------------------------------------
# Score scale reference
# ----------------------------------------------------------
st.markdown("### 📏 Risk Score Reference")

ref_cols = st.columns(3)
with ref_cols[0]:
    st.markdown(
        '<div style="background:#eafaf1;border:2px solid #27ae60;border-radius:8px;'
        'padding:14px;text-align:center;">'
        '<div style="font-weight:700;color:#27ae60;font-size:1rem;">🟢 LOW</div>'
        '<div style="color:#1c2b3a;font-size:1.4rem;font-weight:800;">1–4</div>'
        '<div style="color:#6b7c93;font-size:0.8rem;">out of 10</div>'
        '</div>',
        unsafe_allow_html=True,
    )
with ref_cols[1]:
    st.markdown(
        '<div style="background:#fef3e2;border:2px solid #e67e22;border-radius:8px;'
        'padding:14px;text-align:center;">'
        '<div style="font-weight:700;color:#e67e22;font-size:1rem;">🟡 MEDIUM</div>'
        '<div style="color:#1c2b3a;font-size:1.4rem;font-weight:800;">5–7</div>'
        '<div style="color:#6b7c93;font-size:0.8rem;">out of 10</div>'
        '</div>',
        unsafe_allow_html=True,
    )
with ref_cols[2]:
    st.markdown(
        '<div style="background:#fdecea;border:2px solid #c0392b;border-radius:8px;'
        'padding:14px;text-align:center;">'
        '<div style="font-weight:700;color:#c0392b;font-size:1rem;">🔴 HIGH</div>'
        '<div style="color:#1c2b3a;font-size:1.4rem;font-weight:800;">8–10</div>'
        '<div style="color:#6b7c93;font-size:0.8rem;">out of 10</div>'
        '</div>',
        unsafe_allow_html=True,
    )

st.divider()
st.caption("Urban Flood Risk AI · SDG 11 + SDG 13")
