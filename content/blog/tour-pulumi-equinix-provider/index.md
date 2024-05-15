---
title: "A Tour of the Pulumi Equinix Provider"
date: 2023-06-28
meta_desc: Learn to use the capabilities of the Pulumi Equinix Provider, including how to deploy Kubernetes on Equinix Metal.
meta_image: tour-equinix-provider.png
authors:
    - josh-kodroff
    - oscar-cobles
tags:
    - equinix
    - kubernetes
---

Equinix recently released their self-maintained, fully-supported Pulumi provider, available in the [Pulumi Registry](https://www.pulumi.com/registry/packages/equinix/). In this post, you'll get an overview of the Equinix resources the provider can manage and we'll show you how to deploy a Kubernetes cluster and associated workloads on Equinix Metal.

<!--more-->

{{% notes type="info" %}}
Join Pulumi and Equinix on September 13, 2023, for a live workshop: [Deploying a Kubernetes Cluster on Equinix Metal](https://www.pulumi.com/resources/deploying-a-kubernetes-cluster-on-equinix-metal/).
{{% /notes %}}

## Introducing the Equinix Provider

The Equinix provider can manage resources for:

- [Equinix Metal](https://www.equinix.com/products/digital-infrastructure-services/equinix-metal), which provides high-performance, bare-metal compute resources.
- [Equinix Fabric](https://www.equinix.com/products/digital-infrastructure-services/equinix-fabric), which provides software-defined networking that enables low-latency connections between private networks; select service providers like Salesforce, AWS, Azure, and more; and Equinix Metal devices.
- [Equinix Network Edge](https://www.equinix.com/products/digital-infrastructure-services/network-edge), which enables organizations to deploy virtual network functions (VNFs) (like virtual firewall devices) in a centralized point, greatly simplifying network traffic management for multi- and hybrid cloud scenarios.

Detailed documentation for the Equinix provider can be found in the [Pulumi Registry](https://www.pulumi.com/registry/) along with 130+ (at the time of writing) other providers that can be used to manage cloud and SaaS resources.

## Creating a Kubernetes cluster on Equinix Metal

In order to demonstrate the power and utility of Pulumi and the Equinix provider, Equinix Labs has produced a codebase that [creates a Kubernetes cluster on Equinix Metal](https://github.com/equinix-labs/pulumi-equinix-kubernetes-cluster/). The codebase is available in both [TypeScript](https://github.com/equinix-labs/pulumi-equinix-kubernetes-cluster/tree/main/nodejs) and [Python](https://github.com/equinix-labs/pulumi-equinix-kubernetes-cluster/tree/main/python).

{{% notes type="info" %}}
For an overview of how Pulumi works along with a guided tour of the codebase and deploying a workload onto the Kubernetes cluster, check out [Pulumi's presentation at Equinix Demo Day 2023](https://youtu.be/-siv1ga0l_o). (Pulumi's presentation begins at 3:30:00 below, or click the preceding link to jump directly to Pulumi's presentation on YouTube.):

{{< youtube "-siv1ga0l_o?t=12576&rel=0" >}}
{{% /notes %}}

The codebase gives an excellent example of one of Pulumi's most compelling features: the ability to manage and orchestrate many different kinds of resources in real programming languages with a single tool. In addition to the Equinix provider which is used to manage the bare metal compute resources, the codebase also uses the following providers:

1. [Cloud-init](https://www.pulumi.com/registry/packages/cloudinit/), to run initialization scripts that install the necessary services to run Kubernetes on the bare metal instances once they are spun up. Much of this work is accomplished via [Kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/). For an even deeper dive on the services installed on the control plane and worker nodes respectively, see [Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way).
1. [TLS](https://www.pulumi.com/registry/packages/tls/), to manage cryptographic resources that allow nodes to join the cluster.
1. [Command](https://www.pulumi.com/registry/packages/command/), which is used to synchronize cluster joining operations and to read the kubeconfig from the control plane.
1. [Random](https://www.pulumi.com/registry/packages/random/), which is used to generate a token for nodes to join the control plane.

Before running the Pulumi program, ensure you've [configured your Equinix credentials](https://www.pulumi.com/registry/packages/equinix/installation-configuration/#credentials). Additionally, if you wish to customize specific aspects of the deployment, you can set the template [configuration values](https://github.com/equinix-labs/pulumi-equinix-kubernetes-cluster/#configuration-variables). Once that's done, execute the following commands to deploy the cluster:

{{% chooser language "typescript,python" / %}}

{{% choosable language typescript %}}

```bash
cd nodejs
npm i
pulumi up
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
cd python
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pulumi up
```

{{% /choosable %}}

After executing the commands, the process will require approximately 5 minutes to finish, resulting in a fully operational cluster. From there, you can write the cluster's Kubeconfig to a file and set it as your default file:

```bash
pulumi stack output kubeconfig --show-secrets > kubeconfig.yml
export KUBECONFIG=kubeconfig.yml
```

Now you can run commands against your cluster with `kubectl` (or the excellent [K9s](https://k9scli.io/) if you prefer a more GUI-like experience)! For example, to show all running pods:

```bash
kubectl get pods --all-namespaces
```

## Deploying a workload with the Pulumi Kubernetes provider

Now that your cluster is provisioned, you can deploy a workload (or any other Kubernetes or Helm resource) using the [Pulumi Kubernetes provider](https://www.pulumi.com/registry/packages/kubernetes/). In order to deploy Kubernetes resources to your cluster, you need to first declare an explicit provider. The explicit provider is needed because you are _creating the cluster and deploying workloads to that cluster in the same Pulumi program_. (For more details on default and explicit providers, see [Resource providers](https://www.pulumi.com/docs/concepts/resources/providers/).) Configure the provider to use the [Kubeconfig](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) of your newly created cluster:

{{% chooser language "typescript,python" / %}}

{{% choosable language typescript %}}

```typescript
const k8sProvider = new k8s.Provider("k8s-provider", {
    kubeconfig: kubeconfig,
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
k8s_provider = k8s.Provider(
    "k8s-provider",
    kubeconfig=kubeconfig
)
```

{{% /choosable %}}

You can then add resources to the cluster by specifying your explicit provider as a [resource option](https://www.pulumi.com/docs/concepts/options/):

{{% chooser language "typescript,python" / %}}

{{% choosable language typescript %}}

```typescript
const nginxDeployment = new k8s.apps.v1.Deployment("nginx-deployment", {
    metadata: {
        // ...
    },
    spec: {
        // ...
    },
}, { provider: k8sProvider });
```

{{% /choosable %}}

{{% choosable language python %}}

```python
deployment = k8s.apps.v1.Deployment(
    "nginx-deployment",
    metadata={
        # ...
    },
    spec={
        # ...
    },
    opts=pulumi.ResourceOptions(
        provider=k8s_provider
    )
)
```

{{% /choosable %}}

## Adding storage

Our cluster as configured will not be able to run stateful workloads due to the lack of a [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/) from which [PersistentVolumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) can be provisioned. Popular storage options for bare-metal/edge Kubernetes clusters include [Portworx](https://www.purestorage.com/products/cloud-native-applications/portworx.html), [Longhorn](https://longhorn.io/), [Rook](https://rook.io/), or (for non-production scenarios as data loss is likely if a node goes down) [NFS](https://kubernetes.io/docs/concepts/storage/storage-classes/#nfs).

## Conclusion

The Pulumi Equinix provider offers developers an intuitive and efficient way to interact with Equinix resources. By combining the power of Pulumi's infrastructure-as-code tooling and ecosystem along with the utility of Equinix's service offerings, you can create and manage networking and bare metal compute resources using a single tool, freeing practitioners from manual configuration so they can focus on value-driving innovation.
