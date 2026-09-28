"""
Google AI Engine: Gemini 1.5 Multimodal Vision & Agronomy Advisory.
Powered by Google Generative AI (Gemini 1.5 Flash / Pro).
Analyzes diseased leaf pathology imagery and provides conversational agronomy.
"""

import os
import io
import json
import base64
from typing import Dict, Any, Optional, List
from PIL import Image

try:
    import google.generativeai as genai
    HAS_GOOGLE_GENAI = True
except ImportError:
    HAS_GOOGLE_GENAI = False

from app.disease_db import CROP_DISEASES, get_disease_info

class GoogleAIEngine:
    """
    Multimodal Plant Pathology Diagnostic Engine powered by Google Gemini 1.5.
    Combines visual leaf inspection with agricultural domain heuristics.
    """

    def __init__(self):
        self.api_key = os.environ.get("GEMINI_API_KEY", "")
        self.model_name = os.environ.get("GEMINI_MODEL", "gemini-1.5-flash")
        self._initialized = False

        if HAS_GOOGLE_GENAI and self.api_key:
            try:
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel(self.model_name)
                self._initialized = True
            except Exception as e:
                print(f"[Google AI Engine] Initialization notice: {e}")
                self._initialized = False

    @property
    def is_available(self) -> bool:
        return self._initialized and bool(self.api_key)

    def diagnose_multimodal(
        self,
        image_bytes: bytes,
        crop_hint: Optional[str] = None,
        lang: str = "en"
    ) -> Optional[Dict[str, Any]]:
        """
        Submits image to Google Gemini 1.5 Flash Vision for botanical pathology diagnosis.
        Returns structured clinical diagnosis with severity, pathogen, and cure protocols.
        """
        if not self.is_available:
            return None

        try:
            pil_img = Image.open(io.BytesIO(image_bytes))
            
            prompt = f"""
You are an expert plant pathologist and agronomist at the Google Agricultural AI Center.
Analyze this leaf photograph carefully.
Crop context (if provided): {crop_hint or 'Detect automatically'}.
Target Language: {lang}.

Return a STRICT JSON object with these EXACT keys:
{{
  "crop": "Crop name (e.g. Tomato, Rice, Potato)",
  "disease_name": "Standard English disease name or 'Healthy'",
  "disease_id": "lowercase_underscore_id (e.g. tomato_early_blight, rice_blast, tomato_healthy)",
  "confidence": 95.5,
  "severity_stage": "Early Stage (High Curability) | Moderate Stage | Severe | Optimal Plant Vigor",
  "stage_code": "early | moderate | severe | healthy",
  "urgency": "Action window recommendation",
  "affected_area_pct": 12.0,
  "pathogen": "Causative biological pathogen name",
  "pathogen_type": "Fungal | Bacterial | Viral | Nutrient Deficiency | Pest | Healthy",
  "organic_remedies": ["remedy 1", "remedy 2"],
  "chemical_treatments": ["treatment 1", "treatment 2"],
  "preventive_practices": ["practice 1", "practice 2"],
  "explanation": "Concise clinical observation of lesions, halos, or chlorosis observed."
}}
Output ONLY valid JSON without markdown wrapping.
"""
            response = self.model.generate_content([prompt, pil_img])
            text = response.text.strip()
            
            # Clean possible markdown formatting
            if text.startswith("```json"):
                text = text[7:]
            if text.startswith("```"):
                text = text[3:]
            if text.endswith("```"):
                text = text[:-3]
            text = text.strip()

            data = json.loads(text)
            return data
        except Exception as e:
            print(f"[Google AI Engine] Gemini Vision inference error: {e}")
            return None

    def ask_agronomist_gemini(
        self,
        query: str,
        lang: str = "en",
        crop_context: Optional[str] = None,
        disease_context: Optional[str] = None,
        history: Optional[List[Dict[str, str]]] = None
    ) -> Optional[str]:
        """
        Consults Google Gemini for farmer conversational advice in regional languages.
        """
        if not self.is_available:
            return None

        try:
            lang_names = {
                "en": "English", "hi": "Hindi (हिन्दी)", "te": "Telugu (తెలుగు)",
                "ta": "Tamil (தமிழ்)", "kn": "Kannada (ಕನ್ನಡ)", "mr": "Marathi (मराठी)",
                "bn": "Bengali (বাংলা)", "gu": "Gujarati (ગુજરાતી)", "pa": "Punjabi (ਪੰਜਾਬੀ)"
            }
            target_lang_str = lang_names.get(lang, "English")

            system_context = f"""You are KisanDr AI Agronomist, powered by Google Gemini.
You advise Indian smallholder farmers with practical, safe, organic and chemical crop protection advice.
Language: Respond entirely and naturally in {target_lang_str}.
Keep your advice clear, encouraging, bullet-pointed, with exact spray dosages (ml or g per liter of water) and safety precautions.
Crop context: {crop_context or 'General farming'}
Disease context: {disease_context or 'General inquiry'}
"""
            chat = self.model.start_chat()
            response = chat.send_message(f"{system_context}\n\nFarmer Query: {query}")
            return response.text.strip()
        except Exception as e:
            print(f"[Google AI Engine] Gemini Chat error: {e}")
            return None

# Global Google AI Engine singleton
google_ai = GoogleAIEngine()
