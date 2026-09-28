terraform {
  required_version = ">= 1.5.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.20.0"
    }
  }
}

provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
}

# 1. Enable Required Google Cloud APIs
resource "google_project_service" "enabled_services" {
  for_each = toset([
    "run.googleapis.com",
    "firestore.googleapis.com",
    "bigquery.googleapis.com",
    "storage.googleapis.com",
    "artifactregistry.googleapis.com",
    "cloudbuild.googleapis.com",
    "generativelanguage.googleapis.com"
  ])

  project            = var.gcp_project_id
  service            = each.key
  disable_on_destroy = false
}

# 2. Google Artifact Registry for Docker Images
resource "google_artifact_registry_repository" "kisan_repo" {
  depends_on    = [google_project_service.enabled_services]
  project       = var.gcp_project_id
  location      = var.gcp_region
  repository_id = "kisan-ai-repo"
  description   = "Docker repository for KisanDr AI crop health microservices"
  format        = "DOCKER"
}

# 3. Google Cloud Storage Bucket for Leaf Photos
resource "google_storage_bucket" "leaf_bucket" {
  depends_on                  = [google_project_service.enabled_services]
  name                        = "${var.gcp_project_id}-leaf-archive"
  location                    = var.gcp_region
  force_destroy               = true
  uniform_bucket_level_access = true

  lifecycle_rule {
    condition {
      age = 90
    }
    action {
      type = "Delete"
    }
  }
}

# 4. Google Cloud Firestore NoSQL Database
resource "google_firestore_database" "kisan_database" {
  depends_on  = [google_project_service.enabled_services]
  project     = var.gcp_project_id
  name        = "(default)"
  location_id = var.gcp_region
  type        = "FIRESTORE_NATIVE"
}

# 5. Google BigQuery Dataset & Telemetry Table
resource "google_bigquery_dataset" "analytics_dataset" {
  depends_on                 = [google_project_service.enabled_services]
  dataset_id                 = "kisan_ai_analytics"
  friendly_name              = "KisanDr AI Epidemic Telemetry"
  description                = "Regional crop disease outbreak logs and epidemic risk warehouse"
  location                   = var.gcp_region
  delete_contents_on_destroy = true
}

resource "google_bigquery_table" "disease_telemetry_table" {
  dataset_id          = google_bigquery_dataset.analytics_dataset.dataset_id
  table_id            = "disease_telemetry"
  deletion_protection = false

  time_partitioning {
    type  = "DAY"
    field = "timestamp"
  }

  schema = <<EOF
[
  {"name": "event_id", "type": "STRING", "mode": "REQUIRED"},
  {"name": "timestamp", "type": "TIMESTAMP", "mode": "REQUIRED"},
  {"name": "crop", "type": "STRING", "mode": "REQUIRED"},
  {"name": "disease_id", "type": "STRING", "mode": "REQUIRED"},
  {"name": "disease_name", "type": "STRING", "mode": "NULLABLE"},
  {"name": "confidence", "type": "FLOAT", "mode": "NULLABLE"},
  {"name": "severity_stage", "type": "STRING", "mode": "NULLABLE"},
  {"name": "affected_area_pct", "type": "FLOAT", "mode": "NULLABLE"},
  {"name": "language", "type": "STRING", "mode": "NULLABLE"},
  {"name": "weather_risk", "type": "STRING", "mode": "NULLABLE"}
]
EOF
}

# 6. Google Cloud Run Service (Serverless Autoscaling Container)
resource "google_cloud_run_v2_service" "kisan_service" {
  depends_on = [
    google_project_service.enabled_services,
    google_artifact_registry_repository.kisan_repo
  ]
  name     = "kisan-dr-ai-service"
  location = var.gcp_region
  ingress  = "INGRESS_TRAFFIC_ALL"

  template {
    scaling {
      min_instance_count = 0
      max_instance_count = 10
    }

    containers {
      image = var.container_image

      resources {
        limits = {
          cpu    = "1000m"
          memory = "1Gi"
        }
      }

      ports {
        container_port = 8000
      }

      env {
        name  = "GOOGLE_CLOUD_PROJECT"
        value = var.gcp_project_id
      }
      env {
        name  = "GEMINI_MODEL"
        value = "gemini-1.5-flash"
      }
      env {
        name  = "GEMINI_API_KEY"
        value = var.gemini_api_key
      }
      env {
        name  = "GCS_LEAF_BUCKET"
        value = google_storage_bucket.leaf_bucket.name
      }
    }
  }
}

# Public unauthenticated access for farmers
resource "google_cloud_run_v2_service_iam_member" "public_access" {
  project  = var.gcp_project_id
  location = var.gcp_region
  name     = google_cloud_run_v2_service.kisan_service.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
