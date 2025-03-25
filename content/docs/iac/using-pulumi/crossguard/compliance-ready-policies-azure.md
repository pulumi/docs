---
title_tag: "Compliance Ready Policies (Azure) | CrossGuard"
meta_desc: This page contains the list of Compliance Ready Policies for Azure.
title: Compliance Ready Azure Policies
h1: List of Compliance Ready Policies for Azure
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    name: Azure Policies
    parent: iac-using-pulumi-policy-compliance
    weight: 4
aliases:
  - /docs/using-pulumi/crossguard/compliance-ready-policies-azure/
  - /docs/iac/packages-and-automation/crossguard/compliance-ready-policies-azure/
search:
  keywords:
    - azure
    - ready
    - policies
    - compute
    - kubernetescluster
    - compliance
    - manageddisk
---

There's a total of 3 Compliance Ready Policies for the Azure provider.

All those policies are available in the `@pulumi/azure-compliance-policies` package.

Please refer to our [Documentation](../compliance-ready-policies/#manual-installation) for more details.

## compute

### LinuxVirtualMachine

#### azure-compute-linuxvirtualmachine-disallow-password-authentication

Policy name: `azure-compute-linuxvirtualmachine-disallow-password-authentication`

Code path: `azure.compute.LinuxVirtualMachine.disallowPasswordAuthentication`

Authentication to Linux machines should require SSH keys.

Service: Compute

Resource: LinuxVirtualMachine

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: authentication, security

Link: <https://docs.microsoft.com/azure/virtual-machines/linux/create-ssh-keys-detailed>

### ManagedDisk

#### azure-compute-manageddisk-disallow-unencrypted-managed-disk

Policy name: `azure-compute-manageddisk-disallow-unencrypted-managed-disk`

Code path: `azure.compute.ManagedDisk.disallowUnencryptedManagedDisk`

Checks that Disks are encrypted.

Service: Compute

Resource: ManagedDisk

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: encryption, storage

Link: <https://docs.microsoft.com/azure/virtual-machines/linux/disk-encryption-overview>

## containerservice

### KubernetesCluster

#### azure-containerservice-kubernetescluster-configure-network-policy

Policy name: `azure-containerservice-kubernetescluster-configure-network-policy`

Code path: `azure.containerservice.KubernetesCluster.configureNetworkPolicy`

Checks AKS cluster has Network Policy configured.

Service: Containerservice

Resource: KubernetesCluster

Associated metadata for this policy:

Severity: <span style='background-color: #F4D8A5;'>high</span>

Frameworks: iso27001, pcidss

Topics: kubernetes, network

Link: <https://kubernetes.io/docs/concepts/services-networking/network-policies/>
