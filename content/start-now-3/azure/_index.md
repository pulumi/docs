---
title: Get Started with Pulumi and Azure
meta_desc: Deploy your first Azure resources with Pulumi in 5 simple steps
type: page
layout: cloud-integrated
no_on_this_page: true

cloud_name: Azure
subtitle: Deploy your first Azure resources in 6 simple steps
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

## Check Prerequisites

Ensure you have the language runtime for your chosen language:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}
**Required:** [Node.js](https://nodejs.org/) version 14 or later

Check your version:

```bash
node --version
```

{{% /choosable %}}

{{% choosable language python %}}
**Required:** [Python](https://www.python.org/) 3.8 or later

Check your version:

```bash
python3 --version
```

{{% /choosable %}}

{{% choosable language go %}}
**Required:** [Go](https://golang.org/) 1.20 or later

Check your version:

```bash
go version
```

{{% /choosable %}}

{{% choosable language csharp %}}
**Required:** [.NET](https://dotnet.microsoft.com/) 6.0 or later

Check your version:

```bash
dotnet --version
```

{{% /choosable %}}

{{% choosable language java %}}
**Required:**

- [Java](https://www.oracle.com/java/) 11 or later
- [Maven](https://maven.apache.org/) 3.6.1 or later

Check your versions:

```bash
java --version
mvn --version
```

{{% /choosable %}}

{{% choosable language yaml %}}
No additional language runtime required - YAML is built into Pulumi!
{{% /choosable %}}

## Configure Azure Access

Configure your Azure credentials:

```bash
az login
```

Or use a service principal:

```bash
export ARM_CLIENT_ID=<YOUR_CLIENT_ID>
export ARM_CLIENT_SECRET=<YOUR_CLIENT_SECRET>
export ARM_TENANT_ID=<YOUR_TENANT_ID>
export ARM_SUBSCRIPTION_ID=<YOUR_SUBSCRIPTION_ID>
```

## Create Your First Project

Choose your preferred language:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

```bash
mkdir quickstart && cd quickstart
pulumi new azure-typescript
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
mkdir quickstart && cd quickstart
pulumi new azure-python
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
mkdir quickstart && cd quickstart
pulumi new azure-go
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
mkdir quickstart && cd quickstart
pulumi new azure-csharp
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
mkdir quickstart && cd quickstart
pulumi new azure-java
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
mkdir quickstart && cd quickstart
pulumi new azure-yaml
```

{{% /choosable %}}

## Deploy Your Infrastructure

The template creates a Resource Group and StorageV2 Storage Account. Deploy it with:

```bash
pulumi up
```

This command:

1. Shows a preview of the Resource Group and Storage Account to be created
2. Asks for your confirmation
3. Creates your Resource Group and StorageV2 Storage Account in Azure
4. Saves the state in Pulumi Cloud

## 🎉 Congratulations!

You've just deployed your first infrastructure with Pulumi!

### What's Next?

- **[Complete Azure Tutorial →](/docs/iac/get-started/azure/)**
  Learn how to build and deploy applications on Azure

- **[Browse Examples →](https://github.com/pulumi/examples#azure)**
  Explore production-ready Azure examples

- **[Join the Community →](https://slack.pulumi.com)**
  Get help and share with 10,000+ developers

### Quick Tips

- Run `pulumi stack` to see your current stack details
- Run `pulumi destroy` to delete your Resource Group and Storage Account
- Run `pulumi config set` to configure stack settings
- View your deployments at [app.pulumi.com](https://app.pulumi.com)
