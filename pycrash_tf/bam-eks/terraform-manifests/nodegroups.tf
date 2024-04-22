resource "aws_eks_node_group" "game-group" {
  cluster_name    = aws_eks_cluster.primary_cluster.name
  node_group_name = "game-group"
  node_role_arn   = aws_iam_role.game_group.arn
  subnet_ids      = aws_subnet.private[*].id

  scaling_config {
    desired_size = 1
    max_size     = 2
    min_size     = 1
  }

  update_config {
    max_unavailable = 1
  }

  # Ensure that IAM Role permissions are created before and deleted after EKS Node Group handling.
  # Otherwise, EKS will not be able to properly delete EC2 Instances and Elastic Network Interfaces.
  depends_on = [
    aws_iam_role_policy_attachment.game_group-AmazonEKSWorkerNodePolicy,
    aws_iam_role_policy_attachment.game_group-AmazonEKS_CNI_Policy,
    aws_iam_role_policy_attachment.game_group-AmazonEC2ContainerRegistryReadOnly,
  ]
}