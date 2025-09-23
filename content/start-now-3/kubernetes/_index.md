---
title: Get Started with Pulumi and Kubernetes
meta_desc: Deploy your first Kubernetes applications with Pulumi in 5 simple steps
type: page
layout: cloud-integrated
no_on_this_page: true

cloud_name: Kubernetes
subtitle: Deploy your first Kubernetes applications in 5 simple steps
---

## Sign up for Pulumi Cloud (Free)

Start with Pulumi Cloud for free - manage state, encrypt secrets, and track deployment history.

<a href="https://app.pulumi.com/signup" class="btn-primary btn-lg">Create Free Account</a>

## Install Pulumi CLI

Choose your operating system:

{{< chooser os "macos,linux,windows" >}}
{{% choosable os macos %}}
```bash
brew install pulumi/tap/pulumi
```
{{% /choosable %}}
{{% choosable os linux %}}
```bash
curl -fsSL https://get.pulumi.com | sh
```
{{% /choosable %}}
{{% choosable os windows %}}
```powershell
choco install pulumi
```
Or download the [installer](https://github.com/pulumi/pulumi/releases)
{{% /choosable %}}
{{< /chooser >}}

## Configure Kubernetes Access

Configure kubectl to connect to your cluster:

```bash
kubectl cluster-info
```

Pulumi uses the same configuration as kubectl from `~/.kube/config`.

## Create Your First Project

Choose your preferred language:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}
```bash
mkdir quickstart && cd quickstart
pulumi new kubernetes-typescript
```
{{% /choosable %}}

{{% choosable language python %}}
```bash
mkdir quickstart && cd quickstart
pulumi new kubernetes-python
```
{{% /choosable %}}

{{% choosable language go %}}
```bash
mkdir quickstart && cd quickstart
pulumi new kubernetes-go
```
{{% /choosable %}}

{{% choosable language csharp %}}
```bash
mkdir quickstart && cd quickstart
pulumi new kubernetes-csharp
```
{{% /choosable %}}

{{% choosable language java %}}
```bash
mkdir quickstart && cd quickstart
pulumi new kubernetes-java
```
{{% /choosable %}}

{{% choosable language yaml %}}
```bash
mkdir quickstart && cd quickstart
pulumi new kubernetes-yaml
```
{{% /choosable %}}

## Deploy Your Infrastructure

The template creates a simple Kubernetes deployment. Deploy it with:

```bash
pulumi up
```

This command:
1. Shows a preview of the Kubernetes resources to be created
2. Asks for your confirmation
3. Creates your deployment in the Kubernetes cluster
4. Saves the state in Pulumi Cloud

## 🎉 Congratulations!

You've just deployed your first infrastructure with Pulumi! 

### What's Next?

- **[Complete Kubernetes Tutorial →](/docs/iac/get-started/kubernetes/)**  
  Learn how to deploy and manage applications on Kubernetes
  
- **[Browse Examples →](https://github.com/pulumi/examples#kubernetes)**  
  Explore production-ready Kubernetes examples
  
- **[Join the Community →](https://slack.pulumi.com)**  
  Get help and share with 10,000+ developers

### Quick Tips

- Run `pulumi stack` to see your current stack details
- Run `pulumi destroy` to remove your Kubernetes deployment
- Run `pulumi config set` to configure stack settings
- View your deployments at [app.pulumi.com](https://app.pulumi.com)