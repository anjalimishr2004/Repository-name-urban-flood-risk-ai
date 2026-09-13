# -*- coding: utf-8 -*-
"""
flood_utils.py
Shared utilities: scoring logic, Gemini AI helper, UI helpers.
"""

import streamlit as st


# ----------------------------------------------------------
# SCORING
# ----------------------------------------------------------

def calculate_scores(rainfall, drainage, area_type, previous_flooding):
    """Return risk component scores and overall risk."""

    if rainfall >= 150:
        rainfall_score = 3
    elif rainfall >= 75:
        rainfall_score = 2
    else:
        rainfall_score = 1

    if drainage == "Poor":
        drainage_score = 3
    elif drainage == "Moderate":
        drainage_score = 2
    else:
        drainage_score = 1

    area_score = 2 if area_type == "Low-lying" else 0
    history_score = 2 if previous_flooding == "Yes" else 0

    risk_score = (
        rainfall_score
        + drainage_score
        + area_score
        + history_score
    )

    if risk_score >= 8:
        risk = "HIGH"
    elif risk_score >= 5:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return (
        rainfall_score,
        drainage_score,
        area_score,
        history_score,
        risk_score,
        risk,
    )


# ----------------------------------------------------------
# RISK COLOUR HELPERS
# ----------------------------------------------------------

RISK_COLOR = {
    "HIGH": "#c0392b",
    "MEDIUM": "#e67e22",
    "LOW": "#27ae60",
}

RISK_BG = {
    "HIGH": "#fdecea",
    "MEDIUM": "#fef3e2",
    "LOW": "#eafaf1",
}


def risk_badge(risk: str) -> str:
    """Return an HTML badge string for the risk level."""

    icon = {
        "HIGH": "🔴",
        "MEDIUM": "🟡",
        "LOW": "🟢",
    }[risk]

    color = RISK_COLOR[risk]
    bg = RISK_BG[risk]

    return (
        f'<span style="background:{bg};color:{color};'
        f'padding:4px 14px;border-radius:20px;'
        f'font-weight:700;font-size:1rem;">'
        f'{icon} {risk} RISK</span>'
    )


# ----------------------------------------------------------
# GEMINI AI RECOMMENDATIONS
# ----------------------------------------------------------

def get_gemini_recommendations(
    location,
    risk_score,
    risk,
    rainfall,
    drainage,
    area_type,
    previous_flooding,
):
    """
    Generate flood preparedness recommendations using Gemini.

    Tries multiple Gemini models automatically.
    If one model fails, the next model is tried.

    Returns:
        list[str] containing 4 recommendations,
        or None if all AI models fail.
    """

    try:
        from google import genai

        # --------------------------------------------------
        # Load API key
        # --------------------------------------------------

        api_key = st.secrets["GEMINI_API_KEY"]

        # --------------------------------------------------
        # Gemini client
        # --------------------------------------------------

        client = genai.Client(api_key=api_key)

        # --------------------------------------------------
        # Prompt
        # --------------------------------------------------

        prompt = f"""
You are an urban flood preparedness expert advising residents
of Indian cities.

Location: {location}
Flood risk level: {risk}
Risk score: {risk_score}/10
Rainfall: {rainfall} mm
Drainage condition: {drainage}
Area type: {area_type}
Previous flooding reported: {previous_flooding}

Give exactly 4 practical flood-preparedness recommendations.

Rules:
- Give exactly 4 recommendations.
- Each recommendation must be one clear sentence.
- Keep them practical and easy for residents to follow.
- Focus on preparedness before or during heavy rainfall.
- Do not give dangerous instructions.
- Do not invent government schemes or emergency numbers.
- Do not include explanations before or after the recommendations.
- Number them 1 to 4.
"""

        # --------------------------------------------------
        # Model fallback list
        # --------------------------------------------------

        models = [
            "gemini-3.8-flash",
            "gemini-3.7-flash",
            "gemini-3.6-flash",
        ]

        response = None
        last_error = None

        # --------------------------------------------------
        # Try models one by one
        # --------------------------------------------------

        for model_name in models:
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                )

                if response is not None and response.text:
                    break

            except Exception as e:
                last_error = e
                response = None
                continue

        # --------------------------------------------------
        # All models failed
        # --------------------------------------------------

        if response is None or not response.text:
            if last_error:
                st.error(
                    f"Gemini AI request failed: "
                    f"{type(last_error).__name__}: {str(last_error)}"
                )
            return None

        text = response.text.strip()

        if not text:
            return None

        # --------------------------------------------------
        # Clean response
        # --------------------------------------------------

        lines = []

        for line in text.splitlines():
            line = line.strip()

            if not line:
                continue

            cleaned = line

            # Remove numbering:
            # 1. recommendation
            # 1) recommendation

            if len(cleaned) >= 3:
                if cleaned[0].isdigit() and cleaned[1] in [".", ")"]:
                    cleaned = cleaned[2:].strip()

            # Remove bullet points

            if cleaned.startswith("-"):
                cleaned = cleaned[1:].strip()

            if cleaned.startswith("•"):
                cleaned = cleaned[1:].strip()

            if cleaned:
                lines.append(cleaned)

        # --------------------------------------------------
        # Keep first 4 recommendations
        # --------------------------------------------------

        recommendations = lines[:4]

        if len(recommendations) < 4:
            return None

        return recommendations

    except KeyError:
        st.warning(
            "Gemini API configuration is incomplete. "
            "Please check the Streamlit secrets configuration."
        )
        return None

    except Exception as e:
        st.error(
            f"Gemini AI request failed: "
            f"{type(e).__name__}: {str(e)}"
        )
        return None