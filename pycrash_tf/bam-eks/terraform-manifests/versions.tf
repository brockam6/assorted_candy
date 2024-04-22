terraform {
  required_version = ">= 1.7"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.30"
    }
  }
  
  /*Uncomment this to use remote backend after running apply once 
    - Initial run will create this dynamoo DB table and S3 bucket
    - Run 'terraform init' to reinitialize the backend
    - Remote backend is now configured */

#   backend "s3" {
#     bucket = "eks-generic-infra-bucket"
#     key    = "dev/eks-cluster/terraform.tfstate"
#     region = "us-west-2" 
 
#     # For State Locking
#     dynamodb_table = "eks-generic"    
#   }  
}

provider "aws" {
  region = var.region
  profile = "personal"
}