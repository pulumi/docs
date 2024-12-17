---
title_tag: Before You Begin | Pulumi Insights
title: Before you begin
h1: "Pulumi Insights: Before you begin"
meta_desc: This page provides an overview on how to get started with Pulumi Insights Accounts.
menu:
  insights:
    parent: insights-get-started
    identifier: insights-get-started-begin
    weight: 2
---

## Before you begin

Before you get started using Pulumi Insights, let's run through a few prerequisites and quick steps to ensure you ready to create your first Insights account and scan.

- Ensure you’re an admin of your Pulumi organization.
- Verify you have permissions to create credentials in the provider account you want to scan.
- Use a **Team**, **Enterprise**, or **Business Critical** edition of Pulumi. [Start a free trial](https://app.pulumi.com/?create-organization).

## Create an ESC Environment

Pulumi Insights Account Discovery requires read-only access to your cloud accounts and is granted by [creating an ESC environment](/docs/esc/get-started/create-environment/) that when opened, produces valid credentials to use the corresponding Pulumi provider.

{{% notes "info" %}}
Account Discovery uses Pulumi ESC to manage the credentials needed to find and read infrastructure resources. This approach follows enterprise best practices for managing application secrets.
{{% /notes %}}

To create an environment, [sign into the Pulumi cloud](https://app.pulumi.com/) console and navigate to **Pulumi ESC** and select **Environments** in the left-hand menu.

Next, click **Create Environment** and enter a name for the project and environment, such as `insights-discovery-project` and `insights-environment` and then click **Create**.

Leave the default environment definition for now, and you will return to finish configuring ESC after you create the required credentials within the provider account.

## Create and configure cloud credentials with ESC

{{% chooser cloud "aws,azure,oracle,kubernetes" %}}

{{% choosable cloud aws %}}

Configure Pulumi Insights to use OpenID Connect to authenticate with AWS.
For a more detailed step-by-step guide, including screenshots see the [Configuring OpenID Connect for AWS](/docs/pulumi-cloud/access-management/oidc/provider/aws/) Pulumi documentation.

1. Log in to the [AWS Management Console](https://console.aws.amazon.com/iam/).
2. Go to the **Roles** section and create a new role.
3. Select the **Web identity** trusted entity type and choose `api.pulumi.com/oidc` as your identity provider.
4. Select the name of your Pulumi organization under **Audience**.
5. Filter to the `ReadOnlyAccess` policy name.
6. Click **Create**.

This will set up a **trust relationship** to allow Pulumi Cloud to assume the role using the following trust policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Principal": {
                "Federated": "arn:aws:iam::<ACCOUNT_ID>:oidc-provider/api.pulumi.com/oidc"
            },
            "Condition": {
                "StringEquals": {
                    "api.pulumi.com/oidc:aud": [
                        "pulumi"
                    ]
                }
            }
        }
    ]
}
```

Next, return to Pulumi ESC and use the following ESC configuration to provide the required credentials:

```yaml

values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: arn:aws:iam::<YOUR_AWS_IAM_ID>:role/insights-discovery-1
          sessionName: esc-${context.pulumi.user.login}
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}
```

{{% /choosable %}}

{{% choosable cloud azure %}}

Configure Pulumi Insights to use OpenID Connect to authenticate with Azure. For a more detailed step-by-step guide, including screenshots see the [Configuring OpenID Connect for Azure](docs/pulumi-cloud/access-management/oidc/provider/azure/) Pulumi documentation.

1. Create a Service Principal in Azure, then generate the following values:
   - **clientId** (also called **appId** in the Azure UI)
   - **tenantId**
   - **subscriptionId**
   - **clientSecret** (also called **password** in the Azure UI)

Next, return to Pulumi ESC and use the following ESC configuration to provide the required credentials:

```yaml
values:
  azure:
    fn::open::azure-login:
      clientId: <YOUR_CLIENT_ID>
      tenantId: <YOUR_TENANT_ID>
      subscriptionId: <YOUR_SUBSCRIPTION_ID>
      clientSecret:
        'fn::secret': <INSERT_CLIENT_SECRET_HERE>
  environmentVariables:
    ARM_CLIENT_ID: ${azure.clientId}
    AZURE_CLIENT_ID: ${azure.clientId}
    ARM_TENANT_ID: ${azure.tenantId}
    AZURE_TENANT_ID: ${azure.tenantId}
    ARM_SUBSCRIPTION_ID: ${azure.subscriptionId}
    ARM_CLIENT_SECRET: ${azure.clientSecret}
    AZURE_CLIENT_SECRET: ${azure.clientSecret}
```

{{< notes type="info" >}}
  For more details on configuring Azure credentials with ESC, refer to [ESC Azure provider documentation](/docs/pulumi-cloud/access-management/oidc/provider/azure/).
{{< /notes >}}

{{% /choosable %}}

{{% choosable cloud oracle %}}

1. Set up API Key authentication by providing the following credentials:

- **OCI_TENANCY_OCID**: OCID of the tenancy. To get the value, see [Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five).
- **OCI_USER_OCID**: The OCID of the user calling the API. See [Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five).
- **OCI_PRIVATE_KEY_PASSWORD**: (Optional) Passphrase used for the key, if it's encrypted.
- **OCI_FINGERPRINT**: Fingerprint for the key pair being used. See [How to Get the Key's Fingerprint](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#four).
- **OCI_REGION**: The OCI region where your resources are located. See [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).
- **OCI_PRIVATE_KEY_PATH**: The private key is required to be listed as an ESC file. To create a private key and integrate it with ESC, see [How to Generate an API Signing Key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#two) and [how to upload the public key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#three)

Next, return to Pulumi ESC and use the following ESC configuration to provide the required credentials:

```yaml
values:
  environmentVariables:
    OCI_FINGERPRINT: "25:ad:34:****************:cd:05:05:08:02:a7"
    OCI_REGION: "us-phoenix-1"
    OCI_TENANCY_OCID: "ocid1.tenancy.oc1..tenancyidnumbers"
    OCI_USER_OCID: "user_ocid"
  files:
    OCI_PRIVATE_KEY_PATH: "<PRIVATE_KEY_CONTENT>"
```

{{% /choosable %}}

{{% choosable cloud kubernetes %}}

By default, the Kubernetes scanner uses **kubeconfig** for authentication. You can provide the contents of the kubeconfig file using a file-based environment variable. The authenticated user must have **`get`** and **`list`** permissions at the cluster scope to discover all resources.

An example ESC configuration would look like:

```yaml
values:
  files:
    KUBECONFIG: <INSERT_KUBECONFIG_CONTENTS>  # Provide the kubeconfig contents here
```

This configuration projects the kubeconfig file contents to a temporary file that the ESC scanner uses for authentication.
{{< notes type="warning" >}}
  The scanner agent does not have access to external binaries (e.g., `aws`, `gcloud`), so kubeconfig files relying on [client-go credential plugins](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#client-go-credential-plugins) are not supported. We recommend creating a service account with the necessary cluster-scoped permissions (**`get`** and **`list`**) and using its token for authentication.
{{< /notes >}}

For a detailed guide on configuring ESC credentials for Insights with Kubernetes see the [following documentation](/docs/pulumi-cloud/insights/accounts/#kubernetes-k8s).

{{% /choosable %}}

{{% /chooser %}}

Next, you'll create a Pulumi insights account used for scanning provider resources.

{{< get-started-stepper >}}
