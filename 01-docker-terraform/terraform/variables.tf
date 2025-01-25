variable "credentials" {
  description = "My Credentials"
  default     = "~/.gc/dataeng.json"
}


variable "project" {
  description = "Project"
  default     = "dataeng-course-project"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default     = "northamerica-northeast1"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default     = "US"
}

variable "bq_dataset_name" {
  description = "bigquery_name"
  #Update the below to what you want your dataset to be called
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "storage_bucket"
  #Update the below to a unique bucket name
  default     = "terraform-demo-terra-bucket-472948274"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}