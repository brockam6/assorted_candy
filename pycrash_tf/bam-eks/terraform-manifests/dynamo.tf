/*Uncomment this to use remote backend after running apply once 
 - Initial run will create this dynamo DB table and S3 bucket
 - Run 'terraform init' to reinitialize the backend
 - Remote backend is now configured */

# resource "aws_dynamodb_table" "backend-db" {
#   name             = "eks-generic"
#   hash_key         = "LockID"
#   billing_mode     = "PAY_PER_REQUEST"
#   stream_enabled   = true
#   stream_view_type = "NEW_AND_OLD_IMAGES"

#   attribute {
#     name = "LockID"
#     type = "S"
#   }
# }