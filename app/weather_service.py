"""
Micro-service for Agricultural Weather & Epidemic Risk Assessment.
Calculates fungal spore germination indices, bacterial spread probability,
and optimal chemical spraying windows based on micro-climate metrics.
"""

from typing import Dict, Any

def calculate_epidemic_risk(temp_c: float = 24.5, humidity_pct: float = 85.0, rainfall_mm: float = 4.2) -> Dict[str, Any]:
    """
    Calculate disease transmission risk based on temperature, relative humidity, and precipitation.
    Epidemiological parameters:
    - Fungi (Alternaria, Phytophthora, Puccinia): Thrives at 18-28°C and RH > 80%
    - Bacteria (Xanthomonas): Thrives at 25-32°C with wind-driven rain
    """
    risk_score = 0
    factors = []
    
    # Humidity factor
    if humidity_pct >= 85:
        risk_score += 45
        factors.append("High relative humidity (>85%) facilitates rapid fungal spore germination")
    elif humidity_pct >= 70:
        risk_score += 25
        factors.append("Moderate humidity (70-84%) sustains leaf wetness")
    else:
        risk_score += 10
        factors.append("Low ambient humidity retards fungal colonization")
        
    # Temperature factor
    if 18 <= temp_c <= 28:
        risk_score += 35
        factors.append(f"Temperature of {temp_c}°C falls precisely in optimal fungal growth range (18-28°C)")
    elif 29 <= temp_c <= 34:
        risk_score += 25
        factors.append(f"Warm temperature of {temp_c}°C favors bacterial multiplication")
    else:
        risk_score += 10
        
    # Rainfall / Leaf wetness
    if rainfall_mm > 5.0:
        risk_score += 20
        factors.append("Active rain accelerates splash dissemination of soil-borne pathogens")
    elif rainfall_mm > 0:
        risk_score += 15
        factors.append("Light rain / dew prolongs canopy wetness")
    
    # Severity assessment
    if risk_score >= 75:
        risk_level = "High Alert"
        color = "red"
        advice = "High epidemic outbreak risk. Apply prophylactic organic/fungicidal protective barrier immediately before rains."
    elif risk_score >= 50:
        risk_level = "Moderate Warning"
        color = "amber"
        advice = "Conditions favorable for disease spread. Scout lower crop canopy closely and prepare spray equipment."
    else:
        risk_level = "Low Risk"
        color = "green"
        advice = "Microclimate is relatively dry; low immediate transmission risk. Maintain standard cultural practices."

    # Spraying window advisory
    spray_window = "Optimal Spray Time: 04:00 PM – 06:30 PM (Cool canopy, minimal wind drift, avoid scorching sun)."
    if rainfall_mm > 10.0:
        spray_window = "Postpone chemical spraying: High rainfall will wash off active ingredients. Wait for clear skies."

    return {
        "risk_level": risk_level,
        "risk_score": min(risk_score, 100),
        "color": color,
        "temperature_c": temp_c,
        "humidity_pct": humidity_pct,
        "rainfall_mm": rainfall_mm,
        "contributing_factors": factors,
        "general_advice": advice,
        "spray_window": spray_window
    }
