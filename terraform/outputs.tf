output "cloud_run_service_url" {
  description = "The public URL of the deployed Google Cloud Run service"
  value       = google_cloud_run_v2_service.kisan_service.uri
}

output "artifact_registry_repo" {
  description = "The Google Artifact Registry repository ID"
  value       = google_artifact_registry_repository.kisan_repo.id
}

output "bigquery_dataset" {
  description = "Google BigQuery agricultural analytics dataset"
  value       = google_bigquery_dataset.analytics_dataset.dataset_id
}

output "gcs_leaf_bucket" {
  description = "Google Cloud Storage bucket for farmer leaf archive"
  value       = google_storage_bucket.leaf_bucket.name
}
