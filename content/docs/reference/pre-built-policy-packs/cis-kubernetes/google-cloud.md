---
title: "Google Cloud (GKE)"
meta_desc: Complete list of CIS Kubernetes Benchmark compliance policies for Google Cloud GKE.
h1: "CIS Kubernetes - Google Cloud (GKE)"
menu:
  reference:
    identifier: reference-pre-built-policy-packs-cis-kubernetes-google-cloud
    parent: reference-pre-built-policy-packs-cis-kubernetes
    weight: 3
---

This page lists all 50 policies in the **CIS Kubernetes** pack for **Google Cloud (GKE)**.

| Policy Name | Description | Framework Reference | Framework Specification |
| ----- | ----- | ----- | ----- |
| k8s-cluster-admin-role-binding-minimized | Minimize the use of cluster-admin role bindings in Kubernetes. | 4.1 | Implement proper RBAC controls to restrict system group bindings and minimize permissions. |
| k8s-rbac-secret-access-minimized | Minimize access to secrets in Kubernetes RBAC policies. | 4.1 | Implement proper RBAC controls to restrict system group bindings and minimize permissions. |
| k8s-rbac-wildcard-use-minimized | Minimize the use of wildcards in Kubernetes RBAC policies. | 4.1 | Implement proper RBAC controls to restrict system group bindings and minimize permissions. |
| k8s-default-service-accounts-not-used | Ensure default service accounts are not actively used in Kubernetes. | 4.1 | Implement proper RBAC controls to restrict system group bindings and minimize permissions. |
| k8s-service-account-token-mounted-minimized | Minimize automatic mounting of service account tokens in Kubernetes. | 4.1 | Implement proper RBAC controls to restrict system group bindings and minimize permissions. |
| k8s-rbac-system-masters-group-avoided | Avoid use of system:masters group in Kubernetes RBAC. | 4.1 | Implement proper RBAC controls to restrict system group bindings and minimize permissions. |
| k8s-rbac-bind-impersonate-escalate-minimized | Minimize bind, impersonate, and escalate permissions in Kubernetes RBAC policies. | 4.1 | Implement proper RBAC controls to restrict system group bindings and minimize permissions. |
| k8s-rbac-system-anonymous-bindings-minimized | Minimize bindings to system:anonymous in Kubernetes RBAC. | 4.1 | Implement proper RBAC controls to restrict system group bindings and minimize permissions. |
| k8s-rbac-system-unauthenticated-bindings-minimized | Minimize bindings to system:unauthenticated in Kubernetes RBAC. | 4.1 | Implement proper RBAC controls to restrict system group bindings and minimize permissions. |
| k8s-rbac-system-authenticated-bindings-minimized | Minimize bindings to system:authenticated in Kubernetes RBAC. | 4.1 | Implement proper RBAC controls to restrict system group bindings and minimize permissions. |
| k8s-pod-security-privileged-containers-minimized | Minimize the admission of privileged containers in Kubernetes. | 4.2 | Enforce Pod Security Standard Baseline profile to prevent privileged containers and host namespace access. |
| k8s-pod-security-host-pid-minimized | Minimize the admission of containers with hostPID in Kubernetes. | 4.2 | Enforce Pod Security Standard Baseline profile to prevent privileged containers and host namespace access. |
| k8s-pod-security-host-ipc-minimized | Minimize the admission of containers with hostIPC in Kubernetes. | 4.2 | Enforce Pod Security Standard Baseline profile to prevent privileged containers and host namespace access. |
| k8s-pod-security-host-network-minimized | Minimize the admission of containers with hostNetwork in Kubernetes. | 4.2 | Enforce Pod Security Standard Baseline profile to prevent privileged containers and host namespace access. |
| k8s-pod-security-allow-privilege-escalation-minimized | Minimize the admission of containers with allowPrivilegeEscalation in Kubernetes. | 4.2 | Enforce Pod Security Standard Baseline profile to prevent privileged containers and host namespace access. |
| gke-network-policy-enabled | Ensure Network Policy is enabled in GKE clusters. | 4.3 | Use network policies to isolate traffic and restrict network access between pods. |
| gke-binary-authorization-enabled | Ensure Binary Authorization is enabled for GKE clusters. | 4.5 | Ensure only trusted container images can be deployed. |
| k8s-seccomp-runtime-default-required | Apply RuntimeDefault seccomp profile to all workloads. | 4.6 | Apply RuntimeDefault seccomp profile to all workloads and ensure default namespace is not used. |
| k8s-default-namespace-not-used | Ensure the default namespace is not used for workloads in Kubernetes. | 4.6 | Apply RuntimeDefault seccomp profile to all workloads and ensure default namespace is not used. |
| gke-container-registry-iam-minimized | Minimize IAM access to Google Container Registry. | 5.1 | Ensure IAM controls and trusted image sources. |
| gke-container-registry-read-only-cluster-access | Ensure GKE clusters have read-only access to Container Registry. | 5.1 | Ensure IAM controls and trusted image sources. |
| k8s-trusted-images-only | Ensure only trusted container images are used. | 5.1 | Ensure IAM controls and trusted image sources. |
| gke-not-using-default-service-account | Ensure GKE nodes do not use the default service account. | 5.2 | Use dedicated service accounts with Workload Identity for GKE nodes. |
| gke-workload-identity-enabled | Ensure Workload Identity is enabled for GKE clusters. | 5.2 | Use dedicated service accounts with Workload Identity for GKE nodes. |
| gke-secrets-encryption-kms-enabled | Ensure Kubernetes Secrets are encrypted using Cloud KMS. | 5.3 | Encrypt Kubernetes secrets using Cloud KMS customer-managed keys. |
| gke-metadata-server-enabled | Ensure GKE Metadata Server is enabled. | 5.4 | Use GKE Metadata Server and Workload Identity for workload authentication. |
| gke-cos-containerd-node-image | Ensure GKE nodes use Container-Optimized OS with containerd. | 5.5 | Ensure nodes use COS with containerd, auto-repair, auto-upgrade, release channels, and Shielded Nodes. |
| gke-node-auto-repair-enabled | Ensure node auto-repair is enabled for GKE node pools. | 5.5 | Ensure nodes use COS with containerd, auto-repair, auto-upgrade, release channels, and Shielded Nodes. |
| gke-node-auto-upgrade-enabled | Ensure node auto-upgrade is enabled for GKE node pools. | 5.5 | Ensure nodes use COS with containerd, auto-repair, auto-upgrade, release channels, and Shielded Nodes. |
| gke-release-channel-enabled | Ensure GKE clusters use a release channel. | 5.5 | Ensure nodes use COS with containerd, auto-repair, auto-upgrade, release channels, and Shielded Nodes. |
| gke-shielded-nodes-enabled | Ensure Shielded Nodes are enabled for GKE clusters. | 5.5 | Ensure nodes use COS with containerd, auto-repair, auto-upgrade, release channels, and Shielded Nodes. |
| gke-shielded-nodes-integrity-monitoring | Ensure integrity monitoring is enabled for Shielded Nodes. | 5.5 | Ensure nodes use COS with containerd, auto-repair, auto-upgrade, release channels, and Shielded Nodes. |
| gke-shielded-nodes-secure-boot | Ensure Secure Boot is enabled for Shielded Nodes. | 5.5 | Ensure nodes use COS with containerd, auto-repair, auto-upgrade, release channels, and Shielded Nodes. |
| gke-vpc-flow-logs-intranode-visibility | Ensure intranode visibility and VPC flow logs are enabled. | 5.6 | Configure VPC-native clusters, private endpoints/nodes, authorized networks, and intranode visibility. |
| gke-vpc-native-cluster-required | Ensure GKE clusters are VPC-native. | 5.6 | Configure VPC-native clusters, private endpoints/nodes, authorized networks, and intranode visibility. |
| gke-control-plane-authorized-networks-enabled | Ensure authorized networks are enabled for the control plane. | 5.6 | Configure VPC-native clusters, private endpoints/nodes, authorized networks, and intranode visibility. |
| gke-private-endpoint-enabled | Ensure GKE clusters use private endpoints. | 5.6 | Configure VPC-native clusters, private endpoints/nodes, authorized networks, and intranode visibility. |
| gke-private-nodes-enabled | Ensure GKE clusters use private nodes. | 5.6 | Configure VPC-native clusters, private endpoints/nodes, authorized networks, and intranode visibility. |
| gke-worker-node-firewall-configured | Ensure firewall rules are configured for worker nodes. | 5.6 | Configure VPC-native clusters, private endpoints/nodes, authorized networks, and intranode visibility. |
| gke-google-managed-ssl-certificates | Use Google-managed SSL certificates for load balancers. | 5.6 | Configure VPC-native clusters, private endpoints/nodes, authorized networks, and intranode visibility. |
| gke-logging-monitoring-enabled | Ensure Cloud Logging and Cloud Monitoring are enabled for GKE. | 5.7 | Enable Cloud Logging, Cloud Monitoring, and auditd logging. |
| gke-linux-auditd-logging-enabled | Ensure Linux auditd logging is enabled for GKE nodes. | 5.7 | Enable Cloud Logging, Cloud Monitoring, and auditd logging. |
| gke-client-certificate-auth-disabled | Ensure client certificate authentication is disabled. | 5.8 | Disable client certificate authentication, enable Google Groups for RBAC, and disable legacy ABAC. |
| gke-google-groups-rbac-enabled | Enable Google Groups for RBAC in GKE. | 5.8 | Disable client certificate authentication, enable Google Groups for RBAC, and disable legacy ABAC. |
| gke-legacy-abac-disabled | Ensure legacy ABAC is disabled in GKE clusters. | 5.8 | Disable client certificate authentication, enable Google Groups for RBAC, and disable legacy ABAC. |
| gke-cmek-persistent-disks | Use customer-managed encryption keys for persistent disks. | 5.9 | Use customer-managed encryption keys (CMEK) for persistent and boot disks. |
| gke-cmek-boot-disks | Use customer-managed encryption keys for boot disks. | 5.9 | Use customer-managed encryption keys (CMEK) for persistent and boot disks. |
| gke-web-ui-disabled | Ensure the Kubernetes Dashboard (Web UI) is disabled. | 5.10 | Disable Kubernetes Dashboard, avoid alpha clusters, and enable security posture. |
| gke-alpha-clusters-not-production | Ensure alpha clusters are not used in production. | 5.10 | Disable Kubernetes Dashboard, avoid alpha clusters, and enable security posture. |
| gke-security-posture-enabled | Ensure GKE Security Posture is enabled. | 5.10 | Disable Kubernetes Dashboard, avoid alpha clusters, and enable security posture. |
