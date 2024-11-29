---
title_tag: Create and manage insights accounts
meta_desc: This page describes how to create insights accounts for scanning provider account resources to use within Pulumi Cloud.
title: Accounts
h1: Create and manage insights accounts
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Accounts
    parent: pulumi-cloud-insights
    weight: 3
    identifier: pulumi-cloud-insights-accounts
  pulumicloud:
    parent: insights
    weight: 3
---

This document outlines the steps required to create and manage a Pulumi insights account used for scanning provider resources.

## Prerequisites

* You must be an admin of your Pulumi organization.
* permissions required to create credentials within the provider account you want to scan

## Account creation

1. After logging into the Pulumi Cloud Console, navigate to the **Accounts** tab.  
    ![Accounts tab](../account-left-tab-button.png)

2. On this page, click the **Create Account** button to access the account creation screen.  
    ![Create accounts button](../create-accounts-button.png)  
    ![Accounts creation screen](../accounts-creation-screen.png)

3. Select your provider.
{{< notes type="info" >}}  
  Currently, Pulumi supports AWS, Azure, Oracle Cloud, and Kubernetes as providers for insights accounts.  
{{< /notes >}}

4. Select or create an ESC environment that has the correct credentials to scan the selected provider.  
{{< notes type="info" >}}  
  See below for details on how to set up the ESC environment for each provider.  
{{< /notes >}}

5. Enter a unique name for the account. The name cannot contain a `/`.
{{< notes type="info" >}}  
  Pulumi automatically names child accounts using `/`. For more information, see **Account Hierarchies** below.  
{{< /notes >}}
6. Add any provider-specific configuration, such as the regions to scan for AWS.
    ![Account configuration tab for AWS](../account-configuration-aws.png)

7. Choose whether to enable scheduled scans or run them manually.
    ![Accounts scheduled scans](../accounts-scheduled-scan.png)  
{{< notes type="info" >}}  
  When scheduled scans are enabled, Pulumi automatically scans the account every 24 hours.  
{{< /notes >}}

## Account hierarchies

Account hierarchies allow you to organize and manage insights accounts in a structured way. Currently, child accounts can only be created automatically by Pulumi and is only done so in the case of AWS regions. In the future, this feature will be expanded to support creating custom hierarchies, providing more flexibility for structuring accounts, such as for organizing Kubernetes clusters within an Azure subscripiton.

### How child accounts work

Pulumi automatically creates child accounts when applicable. For instance, in AWS, each selected region becomes a child account under the main parent account. These child accounts represent the scanned resources in each region. For Kubernetes, Pulumi will soon allow the automatic creation of child accounts for scanned clusters (e.g., EKS).

For example:

* Parent account: `my-aws-account`  
* Child account (region): `my-aws-account/us-east-1`  
* Sub-child account (K8s cluster): `my-aws-account/us-east-1/my-cluster`

If you scan or delete the `my-aws-account` insights account, Pulumi applies this action to all child accounts. However, you can still scan or delete `my-aws-account/us-east-1` without affecting other children of `my-aws-account` and future scans of `my-aws-account` will no longer include `us-east-1` unless it is updated.

Key benefits of child accounts include:

* **Flexible hierarchy**: You can create custom account structures for organization and aggregation.  
* **Cascade actions**: Performing actions (e.g., scanning or deletion) on a parent account propagates to all its children.  
* **Granular control**: Actions can also target specific child accounts, affecting only them and their children.  
* **Configuration inheritance**: Child accounts can inherit ESC credentials and other configurations from their parent account.

## Resources

All scanned resources are displayed on the **Resources** page in Pulumi Cloud.  

### Viewing resources in the grid

* **Grid structure**:  
  * **Project column**: Displays the ultimate parent account name.  
  * **Stack/Account column**: Displays the full child account path. For example:  
    * **Project**: `my-aws-account`  
    * **Stack/Account**: `us-east-1/my-cluster`

![Resources page](../account-resource-list-page.png)

* **Resource navigation**: Click on a resource's name to view its **Resource Details** page. This page includes:  
  * **Resource history**: Pulumi tracks and displays all versions of a resource, with changes based on property updates.  
  * **Properties**: View detailed properties for each resource version.  
  * **References**: See edges (relationships) to other resources in the same account.

![Resource details page](../account-resource-detail-page.png)

## Configure ESC credentials

### AWS

The AWS scanner for Pulumi Cloud requires access to the AWS account you want to scan. Use an ESC environment to generate credentials dynamically. Follow these steps:

1. **Create an IAM role** with the appropriate trust policy for Pulumi Cloud:

    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Federated": "arn:aws:iam::<ACCOUNT_ID>:oidc-provider/api.pulumi.com/oidc"
                },
                "Action": "sts:AssumeRoleWithWebIdentity",
                "Condition": {
                    "StringEquals": {
                        "api.pulumi.com/oidc:aud": "aws:pulumi"
                    }
                }
            }
        ]
    }
    ```

2. **Assign permissions**: Give that IAM role the right permissions to allow Pulumi access to scan resources. Use the `ReadOnlyAccess` managed policy for quick setup.  
{{< notes type="info" >}}  
  Learn more about the [AWS ReadOnlyAccess policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ReadOnlyAccess.html).  
{{< /notes >}}

3. **Create an ESC environment**: Configure it to assume the role via OIDC. See [ESC AWS provider documentation](/docs/pulumi-cloud/access-management/oidc/provider/aws/).

4. **Assign the ESC environment**: Link the ESC environment to your insights account during account creation.

### Azure

The Azure scanner for Pulumi Cloud requires access to your Azure account. This access can be granted by creating an ESC environment that, when opened, produces valid credentials to use the Pulumi Azure provider. Below are the steps to configure Azure credentials.

1. Create a Service Principal in Azure, then generate the following values:
   * **clientId** (also called **appId** in the Azure UI)
   * **tenantId**
   * **subscriptionId**
   * **clientSecret** (also called **password** in the Azure UI)

2. Use the following ESC configuration to provide the required credentials:

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

1. Once the ESC environment is set up with the proper credentials, assign it to your insights account during the account creation phase.

### OCI

The OCI scanner for Pulumi Cloud requires access to your Oracle Cloud account. This access can be granted by creating an ESC environment that, when opened, produces valid credentials to use the Pulumi OCI provider. Below are the steps to configure OCI credentials.

1. Set up API Key authentication by providing the following credentials:

* OCI_TENANCY_OCID: OCID of the tenancy. To get the value, see [Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five).
* OCI_USER_OCID: The OCID of the user calling the API. See [Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five).
* OCI_PRIVATE_KEY_PASSWORD: (Optional) Passphrase used for the key, if it's encrypted.
* OCI_FINGERPRINT: Fingerprint for the key pair being used. See [How to Get the Key's Fingerprint](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#four).
* OCI_REGION: The OCI region where your resources are located. See [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).
* OCI_PRIVATE_KEY_PATH: The private key is required to be listed as an ESC file. To create a private key and integrate it with ESC, see [How to Generate an API Signing Key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#two) and [how to upload the public key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#three)
Use the following ESC configuration to provide the required credentials:

```yaml
values:
  environmentVariables:
    OCI_FINGERPRINT: "25:ad:34:89:e0:36:78:33:61:bf:cd:05:05:08:02:a7"
    OCI_REGION: "us-phoenix-1"
    OCI_TENANCY_OCID: "ocid1.tenancy.oc1..tenancyidnumbers"
    OCI_USER_OCID: "user_ocid"
  files:
    OCI_PRIVATE_KEY: "PRIVATE_KEY_CONTENT"
```

Once the ESC environment is set up with the proper credentials, assign it to your insights account during the account creation phase.
{{< notes type="info" >}}
  The OCI scanner supports both API Key and token-based authentication, though token-based authentication has not been tested yet.
{{< /notes >}}

### Kubernetes (K8s)

Details for setting up ESC credentials for Kubernetes are coming soon.
