---
title: "Azure (AKS)"
meta_desc: Complete list of CIS Kubernetes Benchmark compliance policies for Azure AKS.
h1: "CIS Kubernetes - Azure (AKS)"
menu:
  reference:
    identifier: reference-pre-built-policy-packs-cis-kubernetes-azure
    parent: reference-pre-built-policy-packs-cis-kubernetes
    weight: 2
---

This page lists all 30 policies in the **CIS Kubernetes** pack for **Azure (AKS)**.

| Policy Name | Description | Framework Reference | Framework Specification |
| ----- | ----- | ----- | ----- |
| aks-cluster-audit-logging-enabled | Ensure AKS clusters have audit logging enabled to track all API server requests. | 2.1 | Enable audit logs for AKS clusters to track all API server requests and administrative actions. |
| k8s-cluster-admin-role-binding-minimized | Minimize the use of cluster-admin role bindings in Kubernetes. | 4.1 | Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Implement proper RBAC controls. |
| k8s-rbac-secret-access-minimized | Minimize access to secrets in Kubernetes RBAC policies. | 4.1 | Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Implement proper RBAC controls. |
| k8s-rbac-wildcard-use-minimized | Minimize the use of wildcards in Kubernetes RBAC policies. | 4.1 | Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Implement proper RBAC controls. |
| k8s-rbac-create-pods-minimized | Minimize the ability to create pods in Kubernetes RBAC policies. | 4.1 | Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Implement proper RBAC controls. |
| k8s-default-service-accounts-not-used | Ensure default service accounts are not actively used in Kubernetes. | 4.1 | Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Implement proper RBAC controls. |
| k8s-service-account-token-mounted-minimized | Minimize automatic mounting of service account tokens in Kubernetes. | 4.1 | Restrict administrator privileges to dedicated administrator accounts on enterprise assets. Implement proper RBAC controls. |
| k8s-pod-security-privileged-containers-minimized | Minimize the admission of privileged containers in Kubernetes. | 4.2 | Minimize the admission of privileged containers and containers with dangerous capabilities. |
| k8s-pod-security-host-pid-minimized | Minimize the admission of containers with hostPID in Kubernetes. | 4.2 | Minimize the admission of privileged containers and containers with dangerous capabilities. |
| k8s-pod-security-host-ipc-minimized | Minimize the admission of containers with hostIPC in Kubernetes. | 4.2 | Minimize the admission of privileged containers and containers with dangerous capabilities. |
| k8s-pod-security-host-network-minimized | Minimize the admission of containers with hostNetwork in Kubernetes. | 4.2 | Minimize the admission of privileged containers and containers with dangerous capabilities. |
| k8s-pod-security-allow-privilege-escalation-minimized | Minimize the admission of containers with allowPrivilegeEscalation in Kubernetes. | 4.2 | Minimize the admission of privileged containers and containers with dangerous capabilities. |
| k8s-namespaces-network-policies-defined | Ensure that all Namespaces have Network Policies defined. | 4.4 | Ensure that all Namespaces have Network Policies defined. |
| k8s-secrets-as-files-not-env-vars | Prefer using secrets as files over secrets as environment variables in Kubernetes. | 4.5-4.6 | Prefer using secrets as files over secrets as environment variables. Ensure default namespace is not used for workloads. Apply security context to pods and containers. |
| k8s-resource-namespace-boundaries | Ensure resources are deployed within appropriate namespace boundaries. | 4.5-4.6 | Prefer using secrets as files over secrets as environment variables. Ensure default namespace is not used for workloads. Apply security context to pods and containers. |
| k8s-pod-security-context-applied | Ensure security context is applied to pods and containers. | 4.5-4.6 | Prefer using secrets as files over secrets as environment variables. Ensure default namespace is not used for workloads. Apply security context to pods and containers. |
| k8s-default-namespace-not-used | Ensure the default namespace is not used for workloads in Kubernetes. | 4.5-4.6 | Prefer using secrets as files over secrets as environment variables. Ensure default namespace is not used for workloads. Apply security context to pods and containers. |
| aks-defender-container-scanning-enabled | Ensure Image Vulnerability Scanning using Microsoft Defender for Cloud is enabled. | 5.1 | Ensure Image Vulnerability Scanning using Microsoft Defender for Cloud (MDC). Minimize user access to Azure Container Registry (ACR). |
| acr-user-access-minimized | Minimize user access to Azure Container Registry (ACR). | 5.1 | Ensure Image Vulnerability Scanning using Microsoft Defender for Cloud (MDC). Minimize user access to Azure Container Registry (ACR). |
| aks-acr-readonly-access | Ensure AKS clusters have read-only access to ACR. | 5.1 | Ensure Image Vulnerability Scanning using Microsoft Defender for Cloud (MDC). Minimize user access to Azure Container Registry (ACR). |
| aks-approved-registries-only | Ensure AKS clusters only pull images from approved registries. | 5.1 | Ensure Image Vulnerability Scanning using Microsoft Defender for Cloud (MDC). Minimize user access to Azure Container Registry (ACR). |
| aks-dedicated-service-accounts | Prefer using dedicated AKS Service Accounts. | 5.2 | Prefer using dedicated AKS Service Accounts. |
| aks-secrets-encryption-enabled | Ensure Kubernetes Secrets are encrypted in AKS. | 5.3 | Ensure Kubernetes Secrets are encrypted. |
| aks-cluster-endpoint-restrict-public-access | Restrict access to the AKS control plane endpoint. | 5.4 | Restrict Access to the Control Plane Endpoint. Ensure clusters are created with Private Endpoints and Private Nodes. Enable Network Policy. Encrypt traffic to HTTPS load balancers. |
| aks-private-endpoint-enabled | Ensure AKS clusters are created with Private Endpoints. | 5.4 | Restrict Access to the Control Plane Endpoint. Ensure clusters are created with Private Endpoints and Private Nodes. Enable Network Policy. Encrypt traffic to HTTPS load balancers. |
| aks-private-nodes-enabled | Ensure AKS clusters are created with Private Nodes. | 5.4 | Restrict Access to the Control Plane Endpoint. Ensure clusters are created with Private Endpoints and Private Nodes. Enable Network Policy. Encrypt traffic to HTTPS load balancers. |
| aks-network-policy-enabled | Ensure Network Policy is enabled and configured appropriately in AKS. | 5.4 | Restrict Access to the Control Plane Endpoint. Ensure clusters are created with Private Endpoints and Private Nodes. Enable Network Policy. Encrypt traffic to HTTPS load balancers. |
| aks-load-balancer-tls-encryption | Encrypt traffic to HTTPS load balancers with TLS certificates. | 5.4 | Restrict Access to the Control Plane Endpoint. Ensure clusters are created with Private Endpoints and Private Nodes. Enable Network Policy. Encrypt traffic to HTTPS load balancers. |
| aks-azure-ad-integration-enabled | Manage Kubernetes RBAC users with Azure AD. | 5.5 | Manage Kubernetes RBAC users with Azure AD. Use Azure RBAC for Kubernetes Authorization. |
| aks-azure-rbac-enabled | Use Azure RBAC for Kubernetes Authorization. | 5.5 | Manage Kubernetes RBAC users with Azure AD. Use Azure RBAC for Kubernetes Authorization. |
