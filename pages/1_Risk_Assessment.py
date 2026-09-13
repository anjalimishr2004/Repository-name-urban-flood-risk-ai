# -*- coding: utf-8 -*-
"""
pages/1_Risk_Assessment.py
Flood risk input form, scoring, risk explanation, and rule-based recommendations.
"""

import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from flood_utils import calculate_scores, risk_badge, RISK_COLOR, RISK_BG

st.set_page_config(
    page_title="Risk Assessment · Urban Flood Risk AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------
with st.sidebar:
    st.markdown("## 📊 Risk Assessment")
    st.markdown("---")
    st.caption("Fill in the area details below and press **Assess**.")

# ----------------------------------------------------------
# Page header
# ----------------------------------------------------------
st.markdown("""
<h2 style="color:#1c2b3a;font-weight:800;margin-bottom:4px;">📊 Flood Risk Assessment</h2>
<p style="color:#6b7c93;margin-top:0;">Enter location conditions to calculate a flood risk score and level.</p>
""", unsafe_allow_html=True)
st.divider()

# ----------------------------------------------------------
# Input form
# ----------------------------------------------------------
with st.form("risk_form"):
    st.markdown("### 📍 Area Information")

    col_a, col_b = st.columns(2)

    with col_a:
        location = st.text_input("Location / City", value="Mumbai")
        rainfall = st.number_input(
            "Rainfall (mm)", min_value=0.0, max_value=500.0, value=100.0, step=1.0
        )

    with col_b:
        drainage = st.selectbox("Drainage Condition", ["Good", "Moderate", "Poor"])
        area_type = st.selectbox("Area Type", ["Normal", "Low-lying"])

    previous_flooding = st.selectbox("Previous Flooding Reported?", ["No", "Yes"])

    submitted = st.form_submit_button(
        "🔍 Assess Flood Risk", use_container_width=True, type="primary"
    )

# ----------------------------------------------------------
# Results
# ----------------------------------------------------------
if submitted:
    rs, ds, as_, hs, risk_score, risk = calculate_scores(
        rainfall, drainage, area_type, previous_flooding
    )

    # Save to session state so AI Preparedness page can use it
    st.session_state["assessment"] = {
        "location": location,
        "rainfall": rainfall,
        "drainage": drainage,
        "area_type": area_type,
        "previous_flooding": previous_flooding,
        "rainfall_score": rs,
        "drainage_score": ds,
        "area_score": as_,
        "history_score": hs,
        "risk_score": risk_score,
        "risk": risk,
    }

    st.divider()

    # --- Risk banner ---
    color  = RISK_COLOR[risk]
    bg     = RISK_BG[risk]
    icon   = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}[risk]
    label  = {"HIGH": "HIGH FLOOD RISK", "MEDIUM": "MEDIUM FLOOD RISK", "LOW": "LOW FLOOD RISK"}[risk]

    st.markdown(
        f'<div style="background:{bg};border-left:6px solid {color};'
        f'border-radius:8px;padding:18px 22px;margin-bottom:16px;">'
        f'<span style="font-size:1.3rem;font-weight:800;color:{color};">'
        f'{icon} {label} — {location}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.caption(
        "⚠️ Rule-based estimate only. LOW risk ≠ no flood possible. "
        "HIGH risk ≠ flooding certain. Always follow official advisories."
    )

    # --- Score metrics ---
    m1, m2, m3 = st.columns(3)
    m1.metric("Risk Score", f"{risk_score} / 10")
    m2.metric("Risk Level", risk)
    m3.metric("Location", location)

    st.divider()

    # --- Factor breakdown ---
    st.markdown("### ⚠️ Risk Factor Breakdown")

    f1, f2, f3, f4 = st.columns(4)
    f1.metric("🌧️ Rainfall", f"+{rs}", help="Score contribution from rainfall")
    f2.metric("🚰 Drainage", f"+{ds}", help="Score contribution from drainage condition")
    f3.metric("🏘️ Area Type", f"+{as_}", help="Score contribution from terrain")
    f4.metric("🌊 Flood History", f"+{hs}", help="Score contribution from previous flooding")

    st.divider()

    # --- Risk explanation ---
    st.markdown("### 🧠 Risk Analysis")

    if risk == "HIGH":
        factors = []
        if rainfall >= 150:
            factors.append(f"very heavy rainfall ({rainfall} mm) likely to exceed drainage capacity")
        elif rainfall >= 75:
            factors.append(f"moderate-to-high rainfall ({rainfall} mm)")
        if drainage == "Poor":
            factors.append("poor drainage infrastructure that cannot move excess water effectively")
        elif drainage == "Moderate":
            factors.append("moderate drainage that may become overwhelmed under sustained rain")
        if area_type == "Low-lying":
            factors.append("low-lying terrain where water naturally accumulates and drains slowly")
        if previous_flooding == "Yes":
            factors.append("a documented history of flooding indicating structural vulnerability")

        if factors:
            st.info(
                f"**{location}** has received a **HIGH** risk rating because multiple serious "
                f"risk factors are present simultaneously: {'; '.join(factors)}. "
                f"When these conditions coincide, the likelihood of surface water flooding, "
                f"waterlogging, or drainage overflow increases significantly."
            )
        else:
            st.info(f"**{location}** received a HIGH rating based on the combined factor score.")

    elif risk == "MEDIUM":
        factors = []
        factors.append(f"rainfall of {rainfall} mm")
        if drainage in ("Poor", "Moderate"):
            factors.append(f"{drainage.lower()} drainage capacity")
        if area_type == "Low-lying":
            factors.append("low-lying terrain")
        if previous_flooding == "Yes":
            factors.append("prior flooding events")

        st.warning(
            f"**{location}** has a **MEDIUM** risk rating. The following factors combine "
            f"to create conditions where localised waterlogging is possible: "
            f"{'; '.join(factors)}. Conditions may worsen if rainfall increases."
        )

    else:
        reasons = []
        if rainfall < 75:
            reasons.append(f"rainfall ({rainfall} mm) is below the threshold where drainage systems typically struggle")
        if drainage == "Good":
            reasons.append("drainage infrastructure is rated as good")
        if area_type == "Normal":
            reasons.append("the area is not low-lying")
        if previous_flooding == "No":
            reasons.append("no reported history of flooding")

        st.success(
            f"**{location}** has a **LOW** risk rating. "
            + (f"Favourable conditions include: {'; '.join(reasons)}." if reasons else "")
            + " The current combination does not suggest an elevated flood risk."
        )

    st.divider()

    # --- Rule-based recommendations ---
    st.markdown("### 🛡️ Rule-Based Recommended Actions")

    recs = [
        "Monitor official weather and emergency advisories from local authorities.",
        "Keep basic emergency contacts and information accessible.",
    ]
    if rainfall >= 150:
        recs.append("**Extreme rainfall:** Avoid flooded roads, underpasses, and low-water crossings.")
    elif rainfall >= 75:
        recs.append("**Elevated rainfall:** Stay alert for rapidly changing water levels in streets.")
    if drainage == "Poor":
        recs.append("**Poor drainage:** Inspect and clear blocked drains, gutters, and storm outlets.")
    elif drainage == "Moderate":
        recs.append("**Moderate drainage:** Check for partially blocked drains before heavy rain.")
    if area_type == "Low-lying":
        recs.append("**Low-lying area:** Avoid parking vehicles in low-lying zones during heavy rain.")
    if previous_flooding == "Yes":
        recs.append("**Flood history:** Ensure household emergency supplies and important documents are ready.")
    if risk == "HIGH":
        recs.append("**High risk:** Avoid unnecessary travel through vulnerable or low-lying areas.")

    for rec in recs:
        st.write(f"- {rec}")

    st.markdown("<br>", unsafe_allow_html=True)
    st.info(
        "💡 For AI-generated recommendations specific to these conditions, "
        "open the **AI Preparedness** page in the sidebar."
    )

else:
    # Placeholder state
    st.markdown("""
    <div style="background:#f0f4f9;border-radius:10px;padding:32px;text-align:center;color:#6b7c93;">
      <div style="font-size:2rem;margin-bottom:8px;">📍</div>
      <div style="font-weight:600;margin-bottom:6px;">Enter area details above and press Assess</div>
      <div style="font-size:0.88rem;">
        Results including risk score, explanation, and recommendations will appear here.
      </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.divider()
st.caption("Urban Flood Risk AI · SDG 11 + SDG 13")
