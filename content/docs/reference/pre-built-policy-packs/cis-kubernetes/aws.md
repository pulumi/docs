---
title: "AWS (EKS)"
meta_desc: Complete list of CIS Kubernetes Benchmark compliance policies for AWS EKS.
h1: "CIS Kubernetes - AWS (EKS)"
menu:
  reference:
    identifier: reference-pre-built-policy-packs-cis-kubernetes-aws
    parent: reference-pre-built-policy-packs-cis-kubernetes
    weight: 1
---

This page lists all 27 policies in the **CIS Kubernetes** pack for **AWS (EKS)**.

| Policy Name | Description | Framework Reference | Framework Specification |
| ----- | ----- | ----- | ----- |
| eks-cluster-audit-logging-enabled | Ensure EKS clusters have audit logging enabled to track all API server requests. | 2.1 | Enable audit logs for EKS clusters to track all API server requests and administrative actions. |
| eks-cluster-cloudwatch-logs-enabled | Ensure EKS clusters have CloudWatch Logs enabled for centralized log management. | 2.1 | Enable audit logs for EKS clusters to track all API server requests and administrative actions. |
| eks-node-group-launch-template-required | Ensure EKS node groups use launch templates for consistent configuration. | 3.1-3.2 | Ensure kubelet configuration follows security best practices including proper authentication, authorization, and file permissions. |
| eks-launch-template-kubelet-config | Ensure EKS launch templates have secure kubelet configuration. | 3.1-3.2 | Ensure kubelet configuration follows security best practices including proper authentication, authorization, and file permissions. |
| eks-cluster-access-manager-enabled | Ensure EKS clusters have access manager enabled for centralized access control. | 4.1 | Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Implement proper RBAC controls. |
| eks-iam-authenticator-enabled | Ensure EKS clusters use IAM authenticator for secure authentication. | 4.1 | Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Implement proper RBAC controls. |
| k8s-cluster-admin-role-binding-minimized | Minimize the use of cluster-admin role bindings in Kubernetes. | 4.1 | Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Implement proper RBAC controls. |
| k8s-rbac-secret-access-minimized | Minimize access to secrets in Kubernetes RBAC policies. | 4.1 | Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Implement proper RBAC controls. |
| k8s-rbac-wildcard-use-minimized | Minimize the use of wildcards in Kubernetes RBAC policies. | 4.1 | Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Implement proper RBAC controls. |
| k8s-rbac-create-pods-minimized | Minimize the ability to create pods in Kubernetes RBAC policies. | 4.1 | Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Implement proper RBAC controls. |
| k8s-rbac-bind-impersonate-escalate-minimized | Minimize bind, impersonate, and escalate permissions in Kubernetes RBAC policies. | 4.1 | Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Implement proper RBAC controls. |
| k8s-default-service-accounts-not-used | Ensure default service accounts are not actively used in Kubernetes. | 4.1 | Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Implement proper RBAC controls. |
| k8s-service-account-token-mounted-minimized | Minimize automatic mounting of service account tokens in Kubernetes. | 4.1 | Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Implement proper RBAC controls. |
| k8s-pod-security-privileged-containers-minimized | Minimize the admission of privileged containers in Kubernetes. | 4.2 | Implement and manage a firewall on servers. Minimize the admission of privileged containers and containers with dangerous capabilities. |
| k8s-pod-security-host-pid-minimized | Minimize the admission of containers with hostPID in Kubernetes. | 4.2 | Implement and manage a firewall on servers. Minimize the admission of privileged containers and containers with dangerous capabilities. |
| k8s-pod-security-host-ipc-minimized | Minimize the admission of containers with hostIPC in Kubernetes. | 4.2 | Implement and manage a firewall on servers. Minimize the admission of privileged containers and containers with dangerous capabilities. |
| k8s-pod-security-host-network-minimized | Minimize the admission of containers with hostNetwork in Kubernetes. | 4.2 | Implement and manage a firewall on servers. Minimize the admission of privileged containers and containers with dangerous capabilities. |
| k8s-pod-security-allow-privilege-escalation-minimized | Minimize the admission of containers with allowPrivilegeEscalation in Kubernetes. | 4.2 | Implement and manage a firewall on servers. Minimize the admission of privileged containers and containers with dangerous capabilities. |
| k8s-secrets-as-files-not-env-vars | Prefer using secrets as files over secrets as environment variables in Kubernetes. | 4.4-4.5 | Prefer using secrets as files over secrets as environment variables. Ensure default namespace is not used for workloads. |
| k8s-default-namespace-not-used | Ensure the default namespace is not used for workloads in Kubernetes. | 4.4-4.5 | Prefer using secrets as files over secrets as environment variables. Ensure default namespace is not used for workloads. |
| eks-ecr-image-scanning-enabled | Ensure Amazon ECR image scanning is enabled for vulnerability detection. | 5.1 | Ensure Image Vulnerability Scanning using Amazon ECR image scanning. Minimize user access to Amazon ECR. |
| eks-ecr-private-repository | Ensure ECR repositories are private to minimize unauthorized access. | 5.1 | Ensure Image Vulnerability Scanning using Amazon ECR image scanning. Minimize user access to Amazon ECR. |
| eks-service-accounts-iam-role-binding | Prefer using dedicated EKS Service Accounts with IAM role bindings. | 5.2-5.3 | Prefer using dedicated EKS Service Accounts. Ensure Kubernetes Secrets are encrypted using Customer Master Keys (CMKs) managed in AWS KMS. |
| eks-secrets-encryption-kms-enabled | Ensure Kubernetes Secrets are encrypted using KMS Customer Master Keys. | 5.2-5.3 | Prefer using dedicated EKS Service Accounts. Ensure Kubernetes Secrets are encrypted using Customer Master Keys (CMKs) managed in AWS KMS. |
| eks-node-group-iam-role-minimal-policy | Ensure EKS node group IAM roles follow the principle of least privilege. | 5.2-5.3 | Prefer using dedicated EKS Service Accounts. Ensure Kubernetes Secrets are encrypted using Customer Master Keys (CMKs) managed in AWS KMS. |
| eks-cluster-endpoint-restrict-public-access | Restrict access to the EKS control plane endpoint. | 5.4 | Restrict Access to the Control Plane Endpoint. Ensure Network Policy is Enabled and set as appropriate. Encrypt traffic to HTTPS load balancers with TLS certificates. |
| eks-network-policy-enabled | Ensure Network Policy is enabled and configured appropriately in EKS. | 5.4 | Restrict Access to the Control Plane Endpoint. Ensure Network Policy is Enabled and set as appropriate. Encrypt traffic to HTTPS load balancers with TLS certificates. |
| eks-load-balancer-tls-encryption | Encrypt traffic to HTTPS load balancers with TLS certificates. | 5.4 | Restrict Access to the Control Plane Endpoint. Ensure Network Policy is Enabled and set as appropriate. Encrypt traffic to HTTPS load balancers with TLS certificates. |
