---
title: "Azure Native 3.8: Unified Credentials and Private Clouds"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-09-04T12:00:00-07:00

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
and extend support to private Azure environments. These updates make it easier than ever to manage Azure infrastructure
using credentials provided by the hosting environment, such as in Azure Kubernetes Service (AKS), Azure VM, and Azure Cloud Shell.

<!--more-->

## Simplified Authentication Across Environments

The highlight of this release is a new authentication mode based on [DefaultAzureCredential][doc1],
a feature of the Azure SDK that unifies authentication-related settings across deployment environments.

[doc1]: https://learn.microsoft.com/en-us/azure/developer/go/sdk/authentication/credential-chains#defaultazurecredential-overview

### What's New

`DefaultAzureCredential` automatically discovers and uses the best available authentication method for your environment,
eliminating the need for an environment-specific configuration. It follows the Azure SDK's standard credential chain:

| Order | Credential                | Description                                                                                                      |
|-------|---------------------------|------------------------------------------------------------------------------------------------------------------|
| 1     | [Environment][o1]         | Reads environment variables (e.g., `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`) to authenticate as a service principal. |
| 2     | [Workload Identity][o2]   | For programs run on an Azure Kubernetes Service (AKS) cluster.                                             |
| 3     | [Managed Identity][o3]    | For programs deployed to an Azure compute resource (e.g., Azure Virtual Machines) or App hosting platform.       |
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

Also in this release is a new setting, `disableInstanceDiscovery`, to determine whether the provider requests
Microsoft Entra instance metadata from the login endpoint (https://login.microsoftonline.com) before authenticating.
This setting is for Pulumi programs authenticating in disconnected clouds or private clouds.

Setting `disableInstanceDiscovery` to `true` will completely disable both instance discovery and authority validation.
Please ensure that the configured authority host is valid and trustworthy.

### How To Use

The provider can be configured to disable instance discovery:

```bash
# Using environment variable
export ARM_DISABLE_INSTANCE_DISCOVERY=true

# Or via Pulumi configuration
pulumi config set azure-native:disableInstanceDiscovery true
```

## Authentication in AKS with Workload Identity

For programs run in a pod on an Azure Kubernetes Service (AKS) cluster, DefaultAzureCredential automatically uses the
workload identity of the pod's service account. This workload identity could then be granted roles in Azure to deploy stack resources.

{{% notes type="info" %}}

Ensure that the application pods using workload identity include the label `azure.workload.identity/use: "true"` in the pod spec.

{{% /notes %}}

### Walkthough

Let's use [Pulumi Kubernetes Operator (PKO)][pko1] to demonstrate a use case where you'd run Pulumi deployment operations in a pod
and could benefit from workload identity.

The operator allocates a dedicated pod for each Pulumi stack under its management, to serve as the execution environment for stack operations.
Each stack may use the same or a different service account. With AKS, that service account has a _workload identity_ that providers
may use to authenticate to Azure cloud and even to Pulumi cloud.

[pko1]: https://www.pulumi.com/docs/iac/using-pulumi/continuous-delivery/pulumi-kubernetes-operator/

#### Create an AKS Cluster

Please follow the steps in ["Deploy and configure workload identity on an Azure Kubernetes Service (AKS) cluster"][aks1]
to create an AKS cluster, managed identity, and Kubernetes service account.  Those steps are:

1. [Create an AKS cluster](https://learn.microsoft.com/en-us/azure/aks/workload-identity-deploy-cluster#create-an-aks-cluster)
2. [Retrieve the OIDC issuer URL](https://learn.microsoft.com/en-us/azure/aks/workload-identity-deploy-cluster#retrieve-the-oidc-issuer-url)
3. [Create a managed identity](https://learn.microsoft.com/en-us/azure/aks/workload-identity-deploy-cluster#create-a-managed-identity)
4. [Create a Kubernetes service account](https://learn.microsoft.com/en-us/azure/aks/workload-identity-deploy-cluster#create-a-kubernetes-service-account)
5. [Create the federated identity credential](https://learn.microsoft.com/en-us/azure/aks/workload-identity-deploy-cluster#create-the-federated-identity-credential)

You now have an Azure managed identity and associated Kubernetes service account that DefaultAzureCredential can use to authenticate to Azure cloud.

Take note of the `clientId` that represents the managed identity:

```shell
az identity show --name "${USER_ASSIGNED_IDENTITY_NAME}" --resource-group "${RESOURCE_GROUP}" --query clientId
"c2bbe0f5-6349-480a-9f6f-3a5cb3e4ecf9"
```

[aks1]: https://learn.microsoft.com/en-us/azure/aks/workload-identity-deploy-cluster

#### Install the Pulumi Kubernetes Operator

Install the operator into the `pulumi-kubernetes-operator` namespace:

```shell
kubectl apply -f https://raw.githubusercontent.com/pulumi/pulumi-kubernetes-operator/refs/tags/v2.0.0/deploy/quickstart/install.yaml
```

#### Configure a Pulumi Cloud Access Token

By default, the operator uses Pulumi Cloud as the state backend for your stacks.
Please create a `Secret` containing a Pulumi access token to be used to authenticate to Pulumi Cloud. Follow [these instructions][doctokens] to create a personal, organization, or team access token.

```shell
kubectl create secret generic -n ${SERVICE_ACCOUNT_NAMESPACE} pulumi-api-secret --from-literal=accessToken=${PULUMI_ACCESS_TOKEN}
```

[doctokens]: https://www.pulumi.com/docs/pulumi-cloud/access-management/access-tokens/

#### Update the Kubernetes Service Account

To use the service account that was created earlier, we need to grant it the `system:auth-delegator` role:

```shell
cat <<EOF | kubectl apply -f -
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: "${SERVICE_ACCOUNT_NAMESPACE}-${SERVICE_ACCOUNT_NAME}:system:auth-delegator"
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:auth-delegator
subjects:
- kind: ServiceAccount
  name: "${SERVICE_ACCOUNT_NAME}"
  namespace: "${SERVICE_ACCOUNT_NAMESPACE}"
EOF
```

#### Define an Example Program

Let's define a simple Pulumi program that uses Azure Native 3.8 and calls the ["getClientConfig"][azdoc1] function to
access the current identity of the provider.

[azdoc1]: https://www.pulumi.com/registry/packages/azure-native/api-docs/authorization/getclientconfig/

```shell
cat <<"EOF" | kubectl apply -n ${SERVICE_ACCOUNT_NAMESPACE} -f -
apiVersion: pulumi.com/v1
kind: Program
metadata:
  name: sample-workload-identity
program:
  variables:
    clientConfig:
      fn::invoke:
        function: azure-native:authorization:getClientConfig
    clientToken:
      fn::secret:
        fn::invoke:
          function: azure-native:authorization:getClientToken
  outputs:
    clientConfig: ${clientConfig}
    clientToken: ${clientToken}
EOF
```

#### Run the Program using Workload Identity

Create a Stack object to run the Pulumi program using your service account and with `azure-native:useDefaultAzureCredential` enabled.

```shell
cat <<EOF | kubectl apply -f -
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: sample-workload-identity
  namespace: "${SERVICE_ACCOUNT_NAMESPACE}"
spec:
  programRef:
    name: sample-workload-identity
  stack: sample-workload-identity
  envRefs:
    PULUMI_ACCESS_TOKEN:
      type: Secret
      secret:
        name: pulumi-api-secret
        key: accessToken
  serviceAccountName: "${SERVICE_ACCOUNT_NAME}"
  config:
    azure-native:useDefaultAzureCredential: "true"
    azure-native:subscriptionId: "${SUBSCRIPTION}"
  workspaceTemplate:
    spec:
      podTemplate:
        metadata:
          labels:
            azure.workload.identity/use: "true"
EOF
```

Checking the stack outputs, we see a `clientId` matching that of the managed identity!

```shell
kubectl get stack/sample-workload-identity -oyaml
```

```yaml
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: sample-workload-identity
  namespace: default
status:
  conditions:
  - lastTransitionTime: "2025-09-04T23:32:11Z"
    message: the stack has been processed and is up to date
    reason: ProcessingCompleted
    status: "True"
    type: Ready
  outputs:
    clientConfig:
      clientId: c2bbe0f5-6349-480a-9f6f-3a5cb3e4ecf9
      objectId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
      subscriptionId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
      tenantId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    clientToken: '[secret]'
```

## Conclusion

Azure Native Provider v3.8 represents our commitment to making Azure infrastructure management work seamlessly across all deployment scenarios,
from local development to production, from public cloud to private cloud.

Have questions or feedback? [Open an issue on GitHub](https://github.com/pulumi/pulumi-azure-native/issues)
or join the conversation in our [Community Slack](https://slack.pulumi.com/) (#azure channel).
