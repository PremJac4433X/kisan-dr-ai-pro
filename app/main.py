"""
KisanDr AI: Agricultural Intelligence Crop Disease Detection & Multilingual Advisory Backend.
FastAPI Application serving REST endpoints, AI vision diagnostics, and localized advisory.
"""

import os
import io
import urllib.parse
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Query
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from app.disease_db import CROP_DISEASES, CROPS_LIST, CROPS_CATALOG, get_disease_info
from app.translations import LANGUAGES, UI_STRINGS, get_localized_disease_profile, get_ui_labels
from app.ml_engine import classifier
from app.weather_service import calculate_epidemic_risk

app = FastAPI(
    title="KisanDr AI – Intelligent Crop Health & Multilingual Advisory Platform",
    description="Empowering smallholder farmers with early disease diagnosis and regional advisory.",
    version="1.0.0"
)

# Enable CORS for cross-origin or mobile web wrappers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Mount static folder
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    """Serves the farmer-friendly responsive web application."""
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse("<h1>KisanDr AI Backend Running</h1>")

@app.get("/health")
async def health_check():
    """Deployment and container health check endpoint."""
    return {
        "status": "healthy",
        "service": "KisanDr AI Crop Diagnostic Service",
        "supported_crops_count": len(CROPS_LIST),
        "supported_diseases_count": len(CROP_DISEASES),
        "supported_languages": list(LANGUAGES.keys())
    }

@app.get("/api/crops")
async def get_crops():
    """Returns the catalog of supported crops categorized by type."""
    return {"crops": CROPS_LIST, "catalog": CROPS_CATALOG}

@app.get("/api/languages")
async def get_languages():
    """Returns the list of supported regional languages with voice codes."""
    return {"languages": LANGUAGES}

@app.get("/api/ui-labels")
async def get_labels(lang: str = Query("hi")):
    """Returns localized interface labels."""
    return {"labels": get_ui_labels(lang), "lang": lang}

@app.get("/api/weather-risk")
async def get_weather_risk(
    temp_c: float = Query(25.0, description="Temperature in Celsius"),
    humidity_pct: float = Query(82.0, description="Relative humidity percentage"),
    rainfall_mm: float = Query(3.5, description="Rainfall in mm")
):
    """Calculates fungal spore and pathogen transmission risk."""
    return calculate_epidemic_risk(temp_c, humidity_pct, rainfall_mm)

@app.post("/api/diagnose")
async def diagnose_crop_disease(
    file: Optional[UploadFile] = File(None),
    sample_name: Optional[str] = Form(None),
    target_crop: Optional[str] = Form("auto"),
    lang: str = Form("hi"),
    temp_c: Optional[float] = Form(26.0),
    humidity_pct: Optional[float] = Form(84.0),
    rainfall_mm: Optional[float] = Form(2.0)
):
    """
    Main diagnostic endpoint:
    - Accepts an uploaded leaf image OR a pre-loaded sample leaf identifier
    - Classifies disease, detects early stage indicators
    - Returns localized advisory in chosen language (Hindi, Telugu, Tamil, Marathi, Punjabi, Gujarati, Kannada, Bengali, English)
    - Returns text-to-speech audio script and WhatsApp sharing payload
    """
    image_bytes = None

    if file and file.filename:
        image_bytes = await file.read()
    elif sample_name:
        sample_path = os.path.join(STATIC_DIR, "samples", f"{sample_name}.jpg")
        if not os.path.exists(sample_path):
            sample_path = os.path.join(STATIC_DIR, "samples", f"{sample_name}")
        if os.path.exists(sample_path):
            with open(sample_path, "rb") as f:
                image_bytes = f.read()
        else:
            raise HTTPException(status_code=404, detail=f"Sample '{sample_name}' not found")
    else:
        # Fallback to default sample leaf
        default_sample = os.path.join(STATIC_DIR, "samples", "tomato_early_blight.jpg")
        if os.path.exists(default_sample):
            with open(default_sample, "rb") as f:
                image_bytes = f.read()
        else:
            raise HTTPException(status_code=400, detail="Please upload a crop leaf image or select a sample")

    if not image_bytes:
        raise HTTPException(status_code=400, detail="Invalid image data")

    # Run AI Vision classification
    diagnosis = classifier.classify_leaf(image_bytes, target_crop=target_crop, sample_hint=sample_name)
    disease_id = diagnosis["disease_id"]
    base_info = diagnosis["disease_profile"]

    # Localize advisory
    localized = get_localized_disease_profile(disease_id, lang, base_info)

    # Weather epidemic risk analysis
    weather_risk = calculate_epidemic_risk(
        temp_c=temp_c or 26.0,
        humidity_pct=humidity_pct or 84.0,
        rainfall_mm=rainfall_mm or 2.0
    )

    # WhatsApp share text formatted for farmers and Krishi Vigyan Kendra (KVK) officers
    crop_name = base_info.get("crop", "Crop")
    disease_name_loc = localized.get("disease_name_localized", base_info.get("disease_name"))
    top_organic = localized.get("organic_remedy_localized", ["N/A"])[0]
    top_chemical = localized.get("chemical_remedy_localized", ["N/A"])[0]

    share_text = (
        f"🌿 *KisanDr AI Crop Health Advisory*\n"
        f"Crop: *{crop_name}*\n"
        f"Diagnosed Issue: *{disease_name_loc}*\n"
        f"Stage: *{diagnosis['severity_stage']}* (Confidence: {diagnosis['confidence']}%)\n\n"
        f"🌱 *Biological Remedy:*\n{top_organic}\n\n"
        f"🧪 *Chemical Treatment:*\n{top_chemical}\n\n"
        f"🌤️ *Weather Risk:* {weather_risk['risk_level']}\n"
        f"Shared via KisanDr AI – Empowering Farmers"
    )

    whatsapp_url = f"https://api.whatsapp.com/send?text={urllib.parse.quote(share_text)}"

    return {
        "status": "success",
        "diagnosis": {
            "disease_id": disease_id,
            "crop": crop_name,
            "crop_scientific": base_info.get("crop_scientific", ""),
            "disease_name_en": base_info.get("disease_name", ""),
            "disease_name_localized": disease_name_loc,
            "pathogen": base_info.get("pathogen", ""),
            "pathogen_type": base_info.get("pathogen_type", ""),
            "confidence": diagnosis["confidence"],
            "severity_stage": diagnosis["severity_stage"],
            "stage_code": diagnosis["stage_code"],
            "urgency": diagnosis["urgency"],
            "affected_area_pct": diagnosis["affected_area_pct"],
            "summary_localized": localized.get("summary_localized", ""),
            "voice_summary": localized.get("voice_summary", ""),
            "voice_code": localized.get("voice_code", "en-IN"),
            "features_detected": diagnosis["features_detected"],
            "top_candidates": diagnosis["top_candidates"]
        },
        "advisory": {
            "organic_remedies": localized.get("organic_remedy_localized", []),
            "chemical_treatments": localized.get("chemical_remedy_localized", []),
            "preventive_practices": localized.get("preventive_practices_localized", []),
            "early_stage_indicators": base_info.get("early_stage_indicators", []),
            "favorable_conditions": base_info.get("spread_favorable_conditions", "")
        },
        "weather_risk": weather_risk,
        "actions": {
            "whatsapp_share_url": whatsapp_url,
            "share_text": share_text
        },
        "language": {
            "code": lang,
            "name": LANGUAGES.get(lang, {}).get("name", "Hindi"),
            "native": LANGUAGES.get(lang, {}).get("native", "हिन्दी")
        }
    }

@app.get("/api/disease/{disease_id}")
async def get_disease_detail(disease_id: str, lang: str = Query("hi")):
    """Fetch complete encyclopedia detail for a specific crop disease."""
    if disease_id not in CROP_DISEASES:
        raise HTTPException(status_code=404, detail="Disease ID not found")
    base_info = CROP_DISEASES[disease_id]
    localized = get_localized_disease_profile(disease_id, lang, base_info)
    return {
        "disease_id": disease_id,
        "base_info": base_info,
        "localized": localized
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
