# Security group for the EKS Cluster
resource "aws_security_group" "cluster_sg" {
  name = "cluster_sg"
  description = "Security Group for managing EKS Node Groups"
  vpc_id = module.vpc.vpc_id

  tags = {
    name = "${var.company_name}-${var.company_lob}-eks-cluster-sg"
  }
}

resource "aws_vpc_security_group_ingress_rule" "allow_tls_ipv4_eks_cluster" {
  security_group_id = aws_security_group.cluster_sg.id
  cidr_ipv4         = module.vpc.vpc_cidr_block
  from_port         = 443
  ip_protocol       = "tcp"
  to_port           = 443
}

resource "aws_vpc_security_group_egress_rule" "allow_all_traffic_ipv4_eks_cluster" {
  security_group_id = aws_security_group.cluster_sg.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1"
}

# Security group for the cluster worker node group
resource "aws_security_group" "node_sg" {
  name = "node_sg"
  description = "Security Group for managing EKS Node Groups"
  vpc_id = module.vpc.vpc_id

  tags = {
    name = "${var.company_name}-${var.company_lob}-worker-node-sg"
  }
}

resource "aws_vpc_security_group_ingress_rule" "allow_tls_ipv4_worker_node" {
  security_group_id = aws_security_group.node_sg.id
  cidr_ipv4         = module.vpc.vpc_cidr_block
  from_port         = 443
  ip_protocol       = "tcp"
  to_port           = 443
}

resource "aws_vpc_security_group_egress_rule" "allow_all_traffic_ipv4_worker_node" {
  security_group_id = aws_security_group.node_sg.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1" # semantically equivalent to all ports
}