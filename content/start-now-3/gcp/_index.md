---
title: Get Started with Pulumi and Google Cloud
meta_desc: Deploy your first Google Cloud resources with Pulumi in 5 simple steps
type: page
layout: cloud-integrated
no_on_this_page: true

cloud_name: Google Cloud
subtitle: Deploy your first Google Cloud resources in 5 simple steps
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

## Configure Google Cloud Access

Configure your Google Cloud credentials:

```bash
gcloud auth application-default login
```

Or use a service account:
```bash
export GOOGLE_CREDENTIALS=/path/to/service-account-key.json
```

## Create Your First Project

Choose your preferred language:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}
```bash
mkdir quickstart && cd quickstart
pulumi new gcp-typescript
```
{{% /choosable %}}

{{% choosable language python %}}
```bash
mkdir quickstart && cd quickstart
pulumi new gcp-python
```
{{% /choosable %}}

{{% choosable language go %}}
```bash
mkdir quickstart && cd quickstart
pulumi new gcp-go
```
{{% /choosable %}}

{{% choosable language csharp %}}
```bash
mkdir quickstart && cd quickstart
pulumi new gcp-csharp
```
{{% /choosable %}}

{{% choosable language java %}}
```bash
mkdir quickstart && cd quickstart
pulumi new gcp-java
```
{{% /choosable %}}

{{% choosable language yaml %}}
```bash
mkdir quickstart && cd quickstart
pulumi new gcp-yaml
```
{{% /choosable %}}

## Deploy Your Infrastructure

The template creates a Google Cloud Storage bucket. Deploy it with:

```bash
pulumi up
```

This command:
1. Shows a preview of the Cloud Storage bucket to be created
2. Asks for your confirmation
3. Creates your Cloud Storage bucket in Google Cloud (US region)
4. Saves the state in Pulumi Cloud

## 🎉 Congratulations!

You've just deployed your first infrastructure with Pulumi! 

### What's Next?

- **[Complete Google Cloud Tutorial →](/docs/iac/get-started/gcp/)**  
  Learn how to build and deploy applications on Google Cloud
  
- **[Browse Examples →](https://github.com/pulumi/examples#gcp)**  
  Explore production-ready Google Cloud examples
  
- **[Join the Community →](https://slack.pulumi.com)**  
  Get help and share with 10,000+ developers

### Quick Tips

- Run `pulumi stack` to see your current stack details
- Run `pulumi destroy` to delete your Cloud Storage bucket
- Run `pulumi config set` to configure stack settings
- View your deployments at [app.pulumi.com](https://app.pulumi.com)