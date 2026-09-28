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
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

from app.disease_db import CROP_DISEASES, CROPS_LIST, CROPS_CATALOG, get_disease_info
from app.translations import LANGUAGES, UI_STRINGS, get_localized_disease_profile, get_ui_labels
from app.ml_engine import classifier
from app.weather_service import calculate_epidemic_risk
from app.chatbot import answer_farmer_query
from app.feedback_service import add_feedback, get_all_feedback
from app.shops_service import find_agro_shops

app = FastAPI(
    title="KisanDr AI – Intelligent Crop Health & Multilingual Advisory Platform",
    description="Empowering smallholder farmers with early disease diagnosis and regional advisory.",
    version="1.0.0"
)

# Startup hook to generate sample images if missing
@app.on_event("startup")
async def ensure_sample_images():
    samples_dir = os.path.join(STATIC_DIR, "samples")
    if not os.path.exists(samples_dir) or not os.listdir(samples_dir):
        try:
            from app.create_samples import create_sample_leaves
            create_sample_leaves(samples_dir)
        except Exception as e:
            print(f"Sample generation notice: {e}")

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
async def get_labels(lang: str = Query("en")):
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
    lang: str = Form("en"),
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

    # Record consultation event to Google Cloud Firestore & BigQuery telemetry
    event_id = "local-diag"
    try:
        from app.gcp_datastore import gcp_datastore
        event_id = gcp_datastore.record_diagnosis_event({
            "crop": crop_name,
            "disease_id": disease_id,
            "disease_name": base_info.get("disease_name", ""),
            "confidence": diagnosis["confidence"],
            "severity_stage": diagnosis["severity_stage"],
            "affected_area_pct": diagnosis["affected_area_pct"],
            "lang": lang,
            "weather_risk": weather_risk
        })
    except Exception as e:
        print(f"Datastore notice: {e}")

    return {
        "status": "success",
        "event_id": event_id,
        "google_stack": diagnosis.get("google_stack", {
            "ai_vision_engine": "Google Gemini 1.5 Flash Multimodal Vision",
            "edge_nn_framework": "Google TensorFlow Lite (MobileNetV3)",
            "cloud_platform": "Google Cloud Run & GKE",
            "telemetry_warehouse": "Google BigQuery & Firestore"
        }),
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
async def get_disease_detail(disease_id: str, lang: str = Query("en")):
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

# -------------------------------------------------------------
# Agri-Chatbot & Farmer Assistant Endpoints
# -------------------------------------------------------------

class ChatMessageRequest(BaseModel):
    message: str = Field(..., description="Farmer question or query")
    lang: str = Field("en", description="Language code (en, hi, te, ta, kn, mr, bn, gu, pa)")
    crop: Optional[str] = Field(None, description="Optional target crop context")
    disease_id: Optional[str] = Field(None, description="Optional diagnosed disease context")
    history: Optional[List[Dict[str, str]]] = Field(default_factory=list, description="Chat conversation history")

@app.post("/api/chat")
async def chat_with_agri_expert(req: ChatMessageRequest):
    """
    Intelligent Agricultural Chatbot endpoint.
    Answers farming, disease management, and organic spray questions in real-time.
    """
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Query message cannot be empty")
    
    response = answer_farmer_query(
        message=req.message,
        lang=req.lang,
        crop=req.crop,
        disease_id=req.disease_id,
        history=req.history
    )
    return response

# -------------------------------------------------------------
# Farmer Satisfaction & Comment System Endpoints
# -------------------------------------------------------------

class FeedbackRequest(BaseModel):
    farmer_name: Optional[str] = Field("Farmer", description="Farmer name")
    location: Optional[str] = Field("India", description="Village or district")
    crop: Optional[str] = Field("General", description="Crop concerned")
    disease: Optional[str] = Field("General Health", description="Disease or diagnosis diagnosed")
    satisfaction: str = Field("satisfied", description="Satisfaction status: satisfied, neutral, unsatisfied")
    rating: int = Field(5, ge=1, le=5, description="Star rating from 1 to 5")
    comment: str = Field(..., description="Farmer review, observation, or comment")

@app.post("/api/feedback")
async def submit_farmer_feedback(req: FeedbackRequest):
    """
    Record farmer satisfaction rating and experience comment.
    """
    if not req.comment.strip():
        raise HTTPException(status_code=400, detail="Feedback comment cannot be empty")
    
    entry = add_feedback(
        farmer_name=req.farmer_name or "Farmer",
        location=req.location or "India",
        crop=req.crop or "General",
        disease=req.disease or "General Health",
        satisfaction=req.satisfaction,
        rating=req.rating,
        comment=req.comment
    )
    return {"status": "success", "message": "Feedback submitted successfully! / आपकी समीक्षा सफलतापूर्वक दर्ज कर ली गई है।", "entry": entry}

@app.get("/api/feedback")
async def get_farmer_feedback(limit: int = Query(20, ge=1, le=100)):
    """
    Get community farmer satisfaction metrics and recent testimonials.
    """
    return get_all_feedback(limit=limit)

# -------------------------------------------------------------
# Agro-Chemical & Pesticide Shop Locator Endpoints
# -------------------------------------------------------------

@app.get("/api/shops")
async def get_nearby_pesticide_shops(
    location: str = Query("Melur", description="City, town, district, or address (e.g. Melur, Madurai, Karnal)"),
    crop: Optional[str] = Query(None, description="Crop name"),
    disease_id: Optional[str] = Query(None, description="Disease ID for cure matching"),
    disease_name: Optional[str] = Query(None, description="Disease name")
):
    """
    Finds nearest licensed fertilizer and pesticide shops stocking remedies to cure crop disease.
    Supports Melur, Madurai, and all towns/addresses nationwide.
    """
    remedies = []
    if disease_id and disease_id in CROP_DISEASES:
        d = CROP_DISEASES[disease_id]
        remedies = (d.get("chemical_remedy", [])[:2]) + (d.get("organic_remedy", [])[:2])

    result = find_agro_shops(
        query_location=location,
        crop=crop,
        disease_id=disease_id,
        disease_name=disease_name,
        recommended_meds=remedies if remedies else None
    )
    return result

# -------------------------------------------------------------
# Google Cloud Platform BigQuery Telemetry & Stack Insights
# -------------------------------------------------------------

@app.get("/api/analytics/trends")
async def get_regional_epidemic_trends(crop: Optional[str] = Query(None)):
    """
    Returns regional epidemic risk telemetry powered by Google BigQuery.
    """
    from app.gcp_datastore import gcp_datastore
    trends = gcp_datastore.query_epidemic_trends(crop=crop)
    return {
        "status": "success",
        "warehouse": "Google BigQuery",
        "dataset": "kisan_ai_analytics.disease_telemetry",
        "trends": trends
    }

@app.get("/api/google-stack")
async def get_google_stack_status():
    """
    Returns live status of all Google-oriented technologies integrated in KisanDr AI.
    """
    from app.google_ai_engine import google_ai
    from app.gcp_datastore import gcp_datastore
    return {
        "ai_vision": {
            "technology": "Google Gemini 1.5 Flash / Pro Vision",
            "active": google_ai.is_available,
            "role": "Multimodal Plant Pathology & Advisory"
        },
        "neural_network": {
            "technology": "Google TensorFlow / TensorFlow Lite",
            "architecture": "MobileNetV3-Large Edge Classifier",
            "role": "On-Device & Cloud Neural Classification"
        },
        "database": {
            "technology": "Google Cloud Firestore (NoSQL)",
            "connected": bool(gcp_datastore.firestore_client),
            "role": "Consultation records, feedback, and shop catalog"
        },
        "analytics": {
            "technology": "Google BigQuery (SQL Data Warehouse)",
            "connected": bool(gcp_datastore.bigquery_client),
            "role": "Real-time epidemiological outbreak monitoring"
        },
        "cloud_compute": {
            "technology": "Google Cloud Run & GKE (Google Kubernetes Engine)",
            "orchestration": "Kubernetes + Docker + Terraform IaC",
            "role": "Serverless and microservice autoscaling deployment"
        },
        "distributed_rpc": {
            "technology": "gRPC & Protocol Buffers",
            "definition": "proto/plant_pathology.proto",
            "role": "High-throughput inter-service communication"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
