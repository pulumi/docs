---
title: "Azure Native 3.8: Unified Credentials and Private Clouds"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-09-02T15:42:22-07:00

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: |
    Pulumi Azure Native v3.8 delivers new credential modes (based on DefaultAzureCredential)
    and private cloud support (based on ARM_METADATA_HOSTNAME).

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - eron-wright

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - azure-native
    - azure
    - features
    - releases

# The social copy used to promote this post on Twitter and Linkedin. These
# properties do not actually create the post and have no effect on the
# generated blog page. They are here strictly for reference.

# Here are some examples of posts we have made in the past for inspiration:
# https://www.linkedin.com/feed/update/urn:li:activity:7171191945841561601
# https://www.linkedin.com/feed/update/urn:li:activity:7169021002394296320
# https://www.linkedin.com/feed/update/urn:li:activity:7155606616455737345
# https://twitter.com/PulumiCorp/status/1763265391042654623
# https://twitter.com/PulumiCorp/status/1762900472489185492
# https://twitter.com/PulumiCorp/status/1755637618631405655

social:
    twitter:
    linkedin:

---

Today we're excited to announce Azure Native Provider v3.8, featuring several enhancements that simplify authentication
and extend support to private Azure environments. These updates make it easier than ever to manage Azure infrastructure across diverse deployment scenarios.

<!--more-->

## "DefaultAzureCredential" for Simplified Authentication Across Environments

The highlight of this release is a new authentication mode based on [DefaultAzureCredential][doc1],
a feature of the Azure SDK that unifies authentication-related settings across deployment environments.

[doc1]: https://learn.microsoft.com/en-us/azure/developer/go/sdk/authentication/credential-chains#defaultazurecredential-overview

### What's New

`DefaultAzureCredential` automatically discovers and uses the best available authentication method for your environment,
eliminating the need for an environment-specific configuration. It follows the Azure SDK's standard credential chain:

| Order | Credential                | Description                                                                                                      |
|-------|---------------------------|------------------------------------------------------------------------------------------------------------------|
| 1     | [Environment][o1]         | Reads environment variables (e.g., `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`) to authenticate as a service principal. |
| 2     | [Workload Identity][o2]   | For workloads deployed on an Azure Kubernetes Service (AKS) cluster.                                             |
| 3     | [Managed Identity][o3]    | For apps deployed to an Azure compute resource (e.g., Azure Virtual Machines) or App hosting platform.           |
| 4     | [Azure CLI][o4]           | For local development using Azure CLI's `az login` command.                                                      |
| 5     | [Azure Developer CLI][o5] | For local development using Azure Developer CLI's `azd auth login` command.                                      |

[o1]: https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/azidentity#EnvironmentCredential
[o2]: https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview?tabs=go
[o3]: https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview
[o4]: https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest
[o5]: https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/overview?tabs=windows

### Real-World Benefits

This means your Pulumi programs can now run seamlessly across:

- Local development machines using Azure CLI credentials
- CI/CD pipelines with service principals via environment variables
- Azure Kubernetes Service with Workload Identity
- Azure VMs and App Services with Managed Identity

All without changing a single line of configuration code.

### Getting Started

Enable DefaultAzureCredential using Pulumi configuration:

```bash
pulumi config set azure-native:useDefaultAzureCredential true
pulumi config set azure-native:subscriptionId <your-subscription-id>
```

Note that `subscriptionId` is a required configuration setting in this (and most) authentication modes; it ensures your resources are deployed to the correct Azure subscription.

## Private Azure Cloud Support

This release brings improved support for [Azure private clouds][docprivatecloud].
A private cloud is a dedicated cloud computing environment used by a single organization.

The provider can now automatically discover, and configure itself for, any Azure cloud based on
the `ARM_METADATA_HOSTNAME` environment variable. Note that this takes precedence over the `ARM_ENVIRONMENT` variable.

[docprivatecloud]: https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-private-cloud

### How To Use

The provider can query the Azure metadata service to automatically configure itself for your specific Azure environment:

```bash
# Using environment variable
export ARM_METADATA_HOSTNAME=management.azure.example

# Or via Pulumi configuration
pulumi config set azure-native:metadataHost management.azure.example
```

The provider expects the `2022-09-01` metadata schema, which resembles:

```json
{
  "authentication": {
    "loginEndpoint": "https://login.microsoftonline.com",
    "audiences": [
      "https://management.core.windows.net/",
      "https://management.azure.com/"
    ]
  },
  "name": "AzureCloud",
  "suffixes": {
    "keyVaultDns": "vault.azure.net",
    "storage": "core.windows.net"
  },
  "resourceManager": "https://management.azure.com/",
  "microsoftGraphResourceId": "https://graph.microsoft.com/"
}
```

The provider automatically retrieves the correct endpoints for authentication, resource management, and other services.

## Disabling Instance Discovery

Also in this release is a new setting that determines whether or not instance discovery is performed when attempting to authenticate,
for Pulumi programs authenticating in disconnected clouds or private clouds.

It determines whether the provider requests Microsoft Entra instance metadata from the login endpoint (https://login.microsoftonline.com) before authenticating.
Enabling will completely disable both instance discovery and authority validation. As a result, it is crucial to ensure that the configured authority host is valid and trustworthy.

### How To Use

The provider can be configured to disable instance discovery:

```bash
# Using environment variable
export ARM_DISABLE_INSTANCE_DISCOVERY=true

# Or via Pulumi configuration
pulumi config set azure-native:disableInstanceDiscovery true
```

## Conclusion

Azure Native Provider v3.8 represents our commitment to making Azure infrastructure management work seamlessly across all deployment scenarios,
from local development to production, from public cloud to private cloud.

Have questions or feedback? [Open an issue on GitHub](https://github.com/pulumi/pulumi-azure-native/issues)
or join the conversation in our [Community Slack](https://slack.pulumi.com/) (#azure channel).
