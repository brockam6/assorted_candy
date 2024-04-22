locals {
  owners = var.company_lob
  environment = var.env
  name = "${var.company_name}-${var.company_lob}"
  common_tags = {
    owners = local.owners
    environment = local.environment
  }
  eks_cluster_name = "${local.name}-${var.cluster_name}"  
} 