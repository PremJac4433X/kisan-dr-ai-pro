"""
Automated Integration and Unit Test Suite for KisanDr AI.
Tests diagnostic pipeline, multilingual response generation, and API health.
"""

import os
import sys
import unittest
from fastapi.testclient import TestClient

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app
from app.disease_db import CROP_DISEASES, CROPS_LIST
from app.translations import LANGUAGES, get_localized_disease_profile
from app.weather_service import calculate_epidemic_risk

client = TestClient(app)

class TestAgriCureAI(unittest.TestCase):

    def test_health_check(self):
        """Verify health check endpoint returns 200 and supported counts."""
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "healthy")
        self.assertGreater(data["supported_crops_count"], 5)
        self.assertGreater(data["supported_diseases_count"], 15)

    def test_get_crops(self):
        """Verify crops catalog is populated."""
        response = client.get("/api/crops")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue("crops" in data)
        self.assertGreaterEqual(len(data["crops"]), 9)

    def test_get_languages(self):
        """Verify regional language catalog includes all 9 Indian languages."""
        response = client.get("/api/languages")
        self.assertEqual(response.status_code, 200)
        langs = response.json()["languages"]
        for code in ["hi", "te", "ta", "kn", "mr", "bn", "gu", "pa", "en"]:
            self.assertIn(code, langs)
            self.assertIn("voice_code", langs[code])

    def test_weather_risk_assessment(self):
        """Verify weather epidemic index calculations under high humidity."""
        risk = calculate_epidemic_risk(temp_c=25.0, humidity_pct=92.0, rainfall_mm=6.0)
        self.assertIn("risk_level", risk)
        self.assertEqual(risk["risk_level"], "High Alert")
        self.assertIn("optimal spray", risk["spray_window"].lower())

    def test_diagnosis_endpoint_sample_hindi(self):
        """Test disease diagnosis with sample tomato leaf in Hindi."""
        response = client.post(
            "/api/diagnose",
            data={
                "sample_name": "tomato_early_blight",
                "target_crop": "tomato",
                "lang": "hi"
            }
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        diag = data["diagnosis"]
        self.assertIn("Tomato", diag["crop"])
        self.assertIn("अर्ली ब्लाइट", diag["disease_name_localized"])
        self.assertGreaterEqual(diag["confidence"], 80.0)
        self.assertTrue(len(data["advisory"]["organic_remedies"]) > 0)
        self.assertTrue(len(data["advisory"]["chemical_treatments"]) > 0)
        self.assertIn("whatsapp", data["actions"]["whatsapp_share_url"])

    def test_diagnosis_endpoint_sample_telugu(self):
        """Test disease diagnosis in Telugu."""
        response = client.post(
            "/api/diagnose",
            data={
                "sample_name": "rice_blast",
                "target_crop": "rice",
                "lang": "te"
            }
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        diag = data["diagnosis"]
        self.assertIn("రైస్", diag["disease_name_localized"])
        self.assertEqual(diag["voice_code"], "te-IN")

    def test_all_nine_regional_languages(self):
        """Test diagnostic advisory localized for all 9 supported regional languages."""
        test_languages = ["hi", "te", "ta", "kn", "mr", "bn", "gu", "pa", "en"]
        for lang in test_languages:
            response = client.post(
                "/api/diagnose",
                data={
                    "sample_name": "tomato_early_blight",
                    "target_crop": "tomato",
                    "lang": lang
                }
            )
            self.assertEqual(response.status_code, 200)
            data = response.json()
            diag = data["diagnosis"]
            adv = data["advisory"]
            self.assertIn("voice_summary", diag)
            self.assertTrue(len(diag["voice_summary"]) > 10)
            self.assertTrue(len(adv["organic_remedies"]) > 0)
            self.assertTrue(len(adv["chemical_treatments"]) > 0)
            self.assertEqual(data["language"]["code"], lang)

    def test_disease_detail_endpoint(self):
        """Test encyclopedia retrieval for apple scab."""
        response = client.get("/api/disease/apple_scab?lang=hi")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["disease_id"], "apple_scab")
        self.assertEqual(data["base_info"]["crop"], "Apple")

    def test_expanded_fruits_and_vegetables(self):
        """Test detail and pathology for expanded fruit and vegetable datasets."""
        test_diseases = [
            ("mango_anthracnose", "Mango"),
            ("banana_sigatoka", "Banana"),
            ("citrus_canker", "Citrus (Lemon / Orange)"),
            ("eggplant_phomopsis_blight", "Brinjal / Eggplant"),
            ("onion_purple_blotch", "Onion & Garlic"),
            ("okra_yellow_vein_mosaic", "Okra / Bhindi"),
            ("sugarcane_red_rot", "Sugarcane"),
            ("groundnut_tikka_leaf_spot", "Groundnut / Peanut"),
            ("chickpea_ascochyta_blight", "Chickpea / Gram"),
            ("tea_blister_blight", "Tea")
        ]
        for disease_id, expected_crop in test_diseases:
            response = client.get(f"/api/disease/{disease_id}?lang=te")
            self.assertEqual(response.status_code, 200, f"Failed for {disease_id}")
            data = response.json()
            self.assertEqual(data["base_info"]["crop"], expected_crop)
            self.assertGreater(len(data["base_info"]["organic_remedy"]), 0)
            self.assertGreater(len(data["base_info"]["chemical_remedy"]), 0)
            self.assertIn("voice_summary", data["localized"])

    def test_categorized_crops_catalog(self):
        """Test /api/crops returns all 4 agricultural sectors."""
        response = client.get("/api/crops")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("catalog", data)
        catalog = data["catalog"]
        categories = [cat["category"] for cat in catalog]
        self.assertIn("Vegetables", categories)
        self.assertIn("Fruits", categories)
        self.assertIn("Cereals & Grains", categories)
        self.assertIn("Cash Crops & Pulses", categories)
        self.assertGreaterEqual(len(data["crops"]), 25)

    def test_chatbot_endpoint(self):
        """Test agricultural chatbot response in Hindi and English."""
        # Query 1: Neem spray question in Hindi
        res = client.post("/api/chat", json={
            "message": "नीम का स्प्रे कैसे तैयार करें?",
            "lang": "hi"
        })
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertIn("reply", data)
        self.assertIn("नीम", data["reply"])
        self.assertGreater(len(data.get("suggestions", [])), 0)

        # Query 2: Rain spray guidelines in English
        res_en = client.post("/api/chat", json={
            "message": "Can I spray in rainy season?",
            "lang": "en"
        })
        self.assertEqual(res_en.status_code, 200)
        self.assertIn("Monsoon", res_en.json()["reply"])

    def test_feedback_system(self):
        """Test submitting farmer satisfaction and retrieving community feedback."""
        # 1. Submit review
        post_res = client.post("/api/feedback", json={
            "farmer_name": "Kisan Harish",
            "location": "Varanasi, UP",
            "crop": "Tomato",
            "disease": "Early Blight",
            "satisfaction": "satisfied",
            "rating": 5,
            "comment": "ट्राइकोडर्मा और तांबे के छिड़काव से फसल पूरी तरह स्वस्थ हो गई।"
        })
        self.assertEqual(post_res.status_code, 200)
        self.assertEqual(post_res.json()["status"], "success")

        # 2. Retrieve feedback
        get_res = client.get("/api/feedback")
        self.assertEqual(get_res.status_code, 200)
        feed_data = get_res.json()
        self.assertIn("satisfaction_rate_percent", feed_data)
        self.assertIn("reviews", feed_data)
        self.assertEqual(feed_data["reviews"][0]["farmer_name"], "Kisan Harish")

    def test_shops_search_melur(self):
        """Test searching shops in Melur returns curated agro stores with remedies."""
        res = client.get("/api/shops?location=Melur&disease_id=tomato_early_blight&crop=Tomato")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["status"], "success")
        self.assertGreaterEqual(data["total_shops"], 2)
        melur_names = [s["name"] for s in data["shops"]]
        self.assertTrue(any("Meenakshi" in name or "Melur" in name for name in melur_names))
        # Verify directions and WhatsApp links are formed
        first_shop = data["shops"][0]
        self.assertIn("google_maps_url", first_shop)
        self.assertIn("whatsapp_url", first_shop)
        self.assertIn("remedies_in_stock", first_shop)

    def test_shops_search_dynamic_address(self):
        """Test searching any custom village or town address."""
        res = client.get("/api/shops?location=Usilampatti")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertGreaterEqual(data["total_shops"], 1)
        self.assertIn("Usilampatti", data["shops"][0]["address"])

    def test_google_stack_status(self):
        """Verify /api/google-stack reports all integrated Google technologies."""
        res = client.get("/api/google-stack")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertIn("ai_vision", data)
        self.assertIn("Gemini", data["ai_vision"]["technology"])
        self.assertIn("neural_network", data)
        self.assertIn("TensorFlow", data["neural_network"]["technology"])
        self.assertIn("database", data)
        self.assertIn("Firestore", data["database"]["technology"])
        self.assertIn("analytics", data)
        self.assertIn("BigQuery", data["analytics"]["technology"])

    def test_bigquery_analytics_trends(self):
        """Verify /api/analytics/trends returns epidemic outbreak telemetry."""
        res = client.get("/api/analytics/trends")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["status"], "success")
        self.assertIn("warehouse", data)
        self.assertEqual(data["warehouse"], "Google BigQuery")
        self.assertGreater(len(data["trends"]), 0)

    def test_diagnosis_returns_google_metadata(self):
        """Verify diagnosis payload contains event_id and google_stack metadata."""
        res = client.post(
            "/api/diagnose",
            data={"sample_name": "tomato_early_blight", "target_crop": "tomato", "lang": "en"}
        )
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertIn("event_id", data)
        self.assertIn("google_stack", data)
        self.assertIn("Gemini", data["google_stack"]["ai_vision_engine"])
        self.assertIn("TensorFlow", data["google_stack"]["edge_nn_framework"])

if __name__ == "__main__":
    unittest.main()
