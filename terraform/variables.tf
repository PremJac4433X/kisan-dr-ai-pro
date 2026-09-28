variable "gcp_project_id" {
  description = "The Google Cloud Platform project ID"
  type        = string
  default     = "kisan-dr-ai-project"
}

variable "gcp_region" {
  description = "Google Cloud primary region"
  type        = string
  default     = "asia-south1" # Mumbai, India
}

variable "container_image" {
  description = "Docker container image URI in Google Artifact Registry"
  type        = string
  default     = "asia-south1-docker.pkg.dev/kisan-dr-ai-project/kisan-ai-repo/kisan-dr-ai:latest"
}

variable "gemini_api_key" {
  description = "Google AI Studio Gemini API Key"
  type        = string
  sensitive   = true
  default     = ""
}
