# -*- coding: utf-8 -*-
"""
pages/4_Emergency_Safety.py
Before / during / after flooding guidance. General emergency preparedness.
"""

import streamlit as st

st.set_page_config(
    page_title="Emergency & Safety · Urban Flood Risk AI",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.markdown("## 🚨 Emergency & Safety")
    st.markdown("---")
    st.caption(
        "This page provides general flood safety guidance. "
        "Always follow your local authority's official instructions."
    )

st.markdown("""
<h2 style="color:#1c2b3a;font-weight:800;margin-bottom:4px;">🚨 Emergency & Safety Guide</h2>
<p style="color:#6b7c93;margin-top:0;">General flood preparedness and response guidance for urban residents.</p>
""", unsafe_allow_html=True)

st.warning(
    "⚠️ **This page provides general preparedness information only.** "
    "It does not replace official emergency services, government flood warnings, "
    "or instructions from local civil authorities. In an emergency, always follow "
    "official guidance and contact emergency services."
)

st.divider()

# ----------------------------------------------------------
# Phases
# ----------------------------------------------------------
tab_before, tab_during, tab_after, tab_general = st.tabs([
    "🟡 Before Flooding",
    "🔴 During Flooding",
    "🟢 After Flooding",
    "📋 General Preparedness",
])

with tab_before:
    st.markdown("### 🟡 Before a Flood Event")
    st.markdown("*Actions to take when flood risk is elevated or heavy rain is forecast.*")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **🏠 At Home**
        - Move valuable documents, electronics, and important items to higher floors or shelves.
        - Identify and clear blockages around drains, gutters, and downpipes.
        - Know your nearest evacuation route and safe shelter location.
        - Prepare an emergency kit (see General Preparedness tab).
        - Charge mobile phones and keep a power bank ready.

        **🚗 Vehicles**
        - Avoid parking in low-lying areas, underpasses, or flood-prone zones.
        - Fill your fuel tank in case evacuation is needed.
        - Keep essential items (torch, first aid, water) in your vehicle.
        """)

    with col2:
        st.markdown("""
        **📡 Stay Informed**
        - Register for local flood alerts from your city's disaster management authority.
        - Monitor IMD (India Meteorological Department) forecasts.
        - Follow official social media channels of your municipal corporation.
        - Know the local emergency helpline numbers.

        **🏢 Community**
        - Check on elderly or vulnerable neighbours.
        - Share flood risk information with family members.
        - Know where the nearest elevated shelter or relief camp is located.
        """)

with tab_during:
    st.markdown("### 🔴 During a Flood Event")
    st.markdown("*Immediate actions when flooding is occurring.*")

    st.error(
        "🚨 **If you are in immediate danger, call emergency services immediately.**  \n"
        "National Disaster Response Force (NDRF) helpline: **011-24363260**  \n"
        "National Emergency Number: **112**"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **🚶 Movement**
        - Do not attempt to walk through moving floodwater — even 15 cm can knock you down.
        - Never drive through flooded roads or underpasses.
        - Avoid bridges over fast-flowing streams.
        - Move to higher ground immediately if instructed by authorities.

        **⚡ Utilities**
        - Turn off electricity at the mains if water enters your home.
        - Do not use electrical appliances in wet conditions.
        - Avoid contact with floodwater — it may be contaminated.
        """)

    with col2:
        st.markdown("""
        **📞 Communication**
        - Keep your phone charged and on. Use SMS or messaging apps to conserve battery.
        - Inform family members of your location.
        - Do not spread unverified information — rely on official sources only.

        **🏠 If sheltering in place**
        - Move to the highest floor of your building.
        - Signal for help from a window if needed.
        - Do not attempt to cross flooded areas to leave unless instructed.
        """)

with tab_after:
    st.markdown("### 🟢 After a Flood Event")
    st.markdown("*Steps to take once floodwaters begin to recede.*")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **🏠 Returning Home**
        - Wait for official confirmation that it is safe to return.
        - Do not enter a building if structural damage is suspected.
        - Check for gas leaks before restoring electricity.
        - Document damage with photographs for insurance purposes.

        **💧 Water & Food Safety**
        - Do not consume tap water until local authorities confirm it is safe.
        - Discard any food that may have come into contact with floodwater.
        - Use bottled or boiled water for drinking, cooking, and cleaning.
        """)

    with col2:
        st.markdown("""
        **🧹 Clean-up**
        - Wear protective clothing (boots, gloves, mask) when cleaning flood-affected areas.
        - Disinfect all surfaces that came into contact with floodwater.
        - Remove waterlogged materials promptly to prevent mould growth.
        - Report blocked drains or damaged infrastructure to your municipality.

        **🧠 Mental Health**
        - Flooding can be traumatic. Seek support if needed.
        - iCall (TISS): 9152987821
        - Vandrevala Foundation: 1860-2662-345
        """)

with tab_general:
    st.markdown("### 📋 General Emergency Preparedness")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **🎒 Emergency Kit — Essential Items**
        - Drinking water (minimum 3 litres per person per day for 3 days)
        - Non-perishable food for 3 days
        - Torch and spare batteries
        - First aid kit and essential medicines
        - Copies of important documents (Aadhaar, insurance, bank details)
        - Mobile phone with emergency numbers saved
        - Cash in small denominations
        - Whistle (to signal for help)
        - Waterproof bags for valuables
        """)

    with col2:
        st.markdown("""
        **📞 Key Emergency Contacts (India)**
        - National Emergency: **112**
        - NDRF Helpline: **011-24363260**
        - Fire: **101**
        - Ambulance: **102**
        - Police: **100**
        - IMD Weather Alerts: [mausam.imd.gov.in](https://mausam.imd.gov.in)
        - NDMA: [ndma.gov.in](https://ndma.gov.in)

        **📲 Official Alert Sources**
        - [Sachet Portal](https://sachet.ndma.gov.in) — NDMA alerts
        - [IMD](https://mausam.imd.gov.in) — Weather forecasts
        - Your city's municipal corporation social media
        """)

    st.info(
        "This tool is intended to support preparedness awareness. It does not provide "
        "real-time emergency alerts. For official flood warnings, always refer to IMD, "
        "NDMA, and your local city administration."
    )

st.divider()
st.caption("Urban Flood Risk AI · SDG 11 + SDG 13 · General guidance only — follow official local authority instructions")
