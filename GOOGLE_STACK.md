# KisanDr AI – Google-Oriented Technology Stack & Architecture Guide

This document details how **KisanDr AI** is engineered strictly around **Google-oriented technologies and best practices**, fulfilling enterprise-grade standards across AI/ML, Cloud Infrastructure, Distributed Systems, Data Warehousing, and Frontend Engineering.

---

## 🏛️ Technology Alignment Matrix

| Category | Google Technology Integrated | Implementation in KisanDr AI |
| :--- | :--- | :--- |
| **AI / Multimodal Vision** | **Google Gemini 1.5 Flash / Pro** | `app/google_ai_engine.py`: Multimodal zero-shot plant pathology lesion inspection, pathogen etiology, and multilingual conversational agronomy via official `google-generativeai` SDK. |
| **Deep Learning & Edge AI** | **TensorFlow & TensorFlow Lite (TFLite)** | `app/tf_model.py`: MobileNetV3 / EfficientNet architecture trained on 38 botanical classes. Post-training INT8 quantization for Android and Google Coral Edge TPUs (`scripts/export_tflite.py`). |
| **NoSQL Database** | **Google Cloud Firestore** | `app/gcp_datastore.py`: Real-time document persistence for farmer consultations, community satisfaction ratings, and pesticide shop inventories with offline fallback resilience. |
| **SQL Data Warehouse** | **Google BigQuery** | `app/gcp_datastore.py`: Telemetry streaming (`kisan_ai_analytics.disease_telemetry`) with partitioned timestamp queries for tracking regional disease waves and pathogen outbreaks. |
| **Object Storage** | **Google Cloud Storage (GCS)** | `app/gcp_datastore.py`: Secure bucket storage (`gs://kisan-dr-ai-leaf-archive`) for infected leaf diagnostics with signed URLs. |
| **Serverless Compute** | **Google Cloud Run** | `cloudbuild.yaml` & `terraform/main.tf`: Auto-scaling container deployment (0 to 10 instances) in `asia-south1` (Mumbai) with low latency for Indian farmers. |
| **Container Orchestration**| **Google Kubernetes Engine (GKE)** | `k8s/deployment.yaml`, `k8s/service.yaml`, `k8s/hpa.yaml`, `k8s/ingress.yaml`: Multi-pod deployment with Horizontal Pod Autoscaling and Google-managed SSL. |
| **Distributed Systems** | **Google RPC (gRPC) & Protocol Buffers** | `proto/plant_pathology.proto` & `app/grpc_service.py`: High-throughput binary RPC protocol on port 50051 for low-latency inter-service communication. |
| **High-Throughput Backend** | **Go (Golang)** | `services/telemetry-service/main.go`: Concurrent telemetry ingestion microservice streaming field sensor events to BigQuery. |
| **DevOps & CI/CD** | **Google Cloud Build** | `cloudbuild.yaml`: Automated pipeline executing unit tests, building container images, pushing to Google Artifact Registry, and deploying to Cloud Run. |
| **Infrastructure as Code** | **Terraform for GCP** | `terraform/main.tf`: Declarative provisioning of Cloud Run, Firestore, BigQuery datasets, GCS buckets, and Artifact Registry. |
| **Frontend & Geo-Spatial** | **Google Material 3 & Google Maps** | `static/index.html`: Google Material Design 3 tokens, Google Sans typography, and Google Maps API route navigation to nearby pesticide shops (Melur, Madurai, etc.). |

---

## 🔬 1. AI/ML Architecture: Google Gemini + TensorFlow Fusion

KisanDr AI uses a **hybrid dual-engine AI pipeline**:

```
           +---------------------------------------+
           |       Farmer Uploads Leaf Photo       |
           +---------------------------------------+
                              |
                +-------------+-------------+
                |                           |
                v                           v
  +---------------------------+   +---------------------------+
  |    Google Gemini 1.5      |   |   Google TensorFlow Lite  |
  |  Multimodal Vision Engine |   |  MobileNetV3 (Edge INT8)  |
  +---------------------------+   +---------------------------+
  | - Lesion necrosis analysis|   | - 224x224 input tensor    |
  | - Fungal hyphae detection |   | - 38 pathology classes    |
  | - Organic & chemical cure |   | - Sub-50ms edge latency   |
  | - Multilingual reasoning  |   | - Offline Android device  |
  +---------------------------+   +---------------------------+
                \                           /
                 \                         /
                  v                       v
           +---------------------------------------+
           |       Consensus Clinical Engine       |
           |   (Confidence score, stage code,      |
           |     advisory, weather spray window)   |
           +---------------------------------------+
```

1. **Google Gemini 1.5 Multimodal Vision (`app/google_ai_engine.py`)**:
   - Inspects fine-grained botanical features (chlorotic halos, concentric target spots, powdery mycelium).
   - Generates structured JSON adhering to clinical plant pathology taxonomies.
2. **Google TensorFlow Lite Pipeline (`app/tf_model.py`)**:
   - Lightweight neural network running locally or at the edge.
   - Quantized into INT8 using TensorFlow Model Optimization Toolkit (`scripts/export_tflite.py`) for low-power smartphones used by rural farmers.

---

## 🗄️ 2. Google Cloud Data Architecture: Firestore & BigQuery

```
                                +-----------------------------+
                                |  FastAPI / gRPC Controller  |
                                +-----------------------------+
                                       |              |
                       +---------------+              +---------------+
                       |                                              |
                       v                                              v
      +----------------------------------+          +----------------------------------+
      |      Google Cloud Firestore      |          |          Google BigQuery         |
      |          (NoSQL Store)           |          |        (SQL Data Warehouse)      |
      +----------------------------------+          +----------------------------------+
      | - Collections:                   |          | - Dataset: kisan_ai_analytics    |
      |   * leaf_diagnoses               |          | - Table: disease_telemetry       |
      |   * farmer_feedback              |          | - Day-partitioned event log      |
      |   * pesticide_shops              |          | - Epidemiological spread SQL     |
      | - Millisecond document access    |          | - Outbreak risk forecasting      |
      +----------------------------------+          +----------------------------------+
```

### BigQuery SQL Example:
```sql
SELECT 
    crop, 
    disease_id, 
    COUNT(*) as outbreak_count, 
    AVG(confidence) as avg_model_confidence,
    AVG(affected_area_pct) as avg_damage_pct
FROM `kisan-dr-ai-project.kisan_ai_analytics.disease_telemetry`
WHERE timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 14 DAY)
GROUP BY crop, disease_id
ORDER BY outbreak_count DESC
LIMIT 10;
```

---

## 🚀 3. Google Cloud DevOps & Deployment

### A. Google Cloud Run (Recommended for Zero-Ops Serverless)
To build and deploy using **Google Cloud Build**:
```bash
# Submit build to Google Cloud Build
gcloud builds submit --config=cloudbuild.yaml .
```
This triggers:
1. Automated unit test execution (`python -m unittest`).
2. Docker container build and push to **Google Artifact Registry**: `asia-south1-docker.pkg.dev/$PROJECT_ID/kisan-ai-repo/kisan-dr-ai`.
3. Deployment to **Google Cloud Run** with autoscaling from 0 to 10 instances.

### B. Infrastructure as Code via Terraform
Provision all GCP resources (Cloud Run, Firestore, BigQuery, GCS, Artifact Registry) in a single command:
```bash
cd terraform
terraform init
terraform plan -var="gcp_project_id=YOUR_PROJECT_ID"
terraform apply -var="gcp_project_id=YOUR_PROJECT_ID"
```

### C. Google Kubernetes Engine (GKE)
Deploy to a GKE cluster:
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml
kubectl apply -f k8s/ingress.yaml
```

---

## 🔌 4. Distributed Systems: Google gRPC & Protocol Buffers

Defined in `proto/plant_pathology.proto`:
- `rpc DiagnoseLeaf (DiagnoseLeafRequest) returns (DiagnoseLeafResponse)`
- `rpc LocateShops (LocateShopsRequest) returns (LocateShopsResponse)`
- `rpc ConsultAssistant (ChatConsultRequest) returns (ChatConsultResponse)`
- `rpc SubmitFeedback (FeedbackSubmissionRequest) returns (FeedbackSubmissionResponse)`

Server implementation provided in `app/grpc_service.py` running concurrently with the REST API.

---

## 🗺️ 5. Geo-Spatial Integration: Google Maps

The pesticide and bio-fertilizer shop locator (`app/shops_service.py`) provides:
- Direct Google Maps routing links (`https://www.google.com/maps/dir/?api=1&destination=...`) for shops in Melur, Madurai, and all nationwide locations.
- Live Google Maps search hub integration.
- Instant WhatsApp stock check button to confirm medicine availability before traveling.
