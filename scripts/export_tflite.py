"""
Google TensorFlow Lite Model Export & Quantization Script.
Converts trained agricultural pathology neural network into an INT8 quantized TFLite model
for low-latency inference on Android edge devices and Google Coral Edge TPUs.
"""

import os
import sys

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.tf_model import tf_pipeline

def export_model():
    models_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "models")
    os.makedirs(models_dir, exist_ok=True)
    
    spec_path = os.path.join(models_dir, "tflite_model_spec.json")
    spec = tf_pipeline.export_tflite_blueprint(spec_path)
    
    print("=======================================================")
    print("Google TensorFlow Lite Model Export Pipeline")
    print("=======================================================")
    print(f"Architecture : {spec['model_family']}")
    print(f"Input Shape  : {spec['input_shape']}")
    print(f"Quantization : {spec['quantization']}")
    print(f"Target TPU   : {spec['optimization_target']}")
    print(f"Classes Count: {spec['num_classes']}")
    print(f"Spec exported to: {spec_path}")
    print("=======================================================")

if __name__ == "__main__":
    export_model()
