"""
Google gRPC Plant Pathology Microservice.
Implements the high-performance RPC endpoints defined in proto/plant_pathology.proto.
Designed for distributed microservices running on Google Kubernetes Engine (GKE)
or Google Compute Engine clusters.
"""

import sys
import os
import concurrent.futures
from typing import Dict, Any

try:
    import grpc
    HAS_GRPC = True
except ImportError:
    HAS_GRPC = False

from app.ml_engine import classifier
from app.disease_db import get_disease_info, CROP_DISEASES
from app.translations import get_localized_disease_profile
from app.weather_service import calculate_epidemic_risk
from app.shops_service import find_agro_shops
from app.chatbot import answer_farmer_query
from app.feedback_service import add_feedback

class PlantPathologyRPCServer:
    """
    gRPC Server handling distributed RPC requests for diagnosis, shop lookup, and chat.
    Conforms to kisandr.v1.PlantPathologyService.
    """

    def __init__(self, port: int = 50051):
        self.port = port
        self.server = None

    def handle_diagnose(self, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """Handles leaf diagnosis via gRPC."""
        img_bytes = request_data.get("image_data", b"")
        target_crop = request_data.get("target_crop", "auto")
        lang = request_data.get("language", "en")

        diagnosis = classifier.classify_leaf(img_bytes, target_crop=target_crop)
        d_id = diagnosis["disease_id"]
        base_info = diagnosis["disease_profile"]
        localized = get_localized_disease_profile(d_id, lang, base_info)

        weather = calculate_epidemic_risk(
            temp_c=request_data.get("ambient_temp_c", 26.0),
            humidity_pct=request_data.get("relative_humidity_pct", 84.0),
            rainfall_mm=request_data.get("rainfall_mm", 2.0)
        )

        return {
            "status": "success",
            "event_id": f"grpc-{d_id}",
            "crop": base_info.get("crop", "Unknown"),
            "disease_id": d_id,
            "disease_name": base_info.get("disease_name", "Unknown"),
            "disease_name_localized": localized.get("disease_name_localized", ""),
            "pathogen": base_info.get("pathogen", ""),
            "pathogen_type": base_info.get("pathogen_type", ""),
            "confidence": diagnosis["confidence"],
            "severity_stage": diagnosis["severity_stage"],
            "urgency": diagnosis["urgency"],
            "affected_area_pct": diagnosis["affected_area_pct"],
            "organic_remedies": localized.get("organic_remedy_localized", []),
            "chemical_treatments": localized.get("chemical_remedy_localized", []),
            "preventive_practices": localized.get("preventive_practices_localized", []),
            "weather_risk_level": weather.get("risk_level", "Moderate"),
            "voice_summary": localized.get("voice_summary", "")
        }

    def handle_locate_shops(self, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """Handles pesticide shop lookup via gRPC."""
        loc = request_data.get("query_location", "Melur")
        crop = request_data.get("crop")
        d_id = request_data.get("disease_id")
        return find_agro_shops(query_location=loc, crop=crop, disease_id=d_id)

    def handle_consult_assistant(self, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """Handles agronomy assistant inquiries via gRPC."""
        msg = request_data.get("message", "")
        lang = request_data.get("language", "en")
        crop = request_data.get("crop")
        d_id = request_data.get("disease_id")
        return answer_farmer_query(message=msg, lang=lang, crop=crop, disease_id=d_id)

    def start(self):
        """Starts the gRPC server worker pool."""
        if not HAS_GRPC:
            print("[gRPC] grpcio library not installed; running in RPC simulation mode.")
            return

        self.server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
        # Note: In production with generated stubs, register servicer:
        # kisandr_v1_pb2_grpc.add_PlantPathologyServiceServicer_to_server(self, self.server)
        self.server.add_insecure_port(f"[::]:{self.port}")
        self.server.start()
        print(f"[gRPC] PlantPathologyService running on port {self.port}")

# Global RPC server instance
grpc_service = PlantPathologyRPCServer()
