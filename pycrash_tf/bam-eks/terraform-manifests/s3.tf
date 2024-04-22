/*Uncomment this to use remote backend after running apply once 
 - Initial run will create this dynamo DB table and S3 bucket
 - Run 'terraform init' to reinitialize the backend
 - Remote backend is now configured */

# resource "aws_s3_bucket" "backend-bucket" {
#     bucket = "eks-generic-infra-bucket"
#     force_destroy = false
#     object_lock_enabled = true

#     tags = {
#         Name = "S3 Remote Terraform State Store"
#     }
# }