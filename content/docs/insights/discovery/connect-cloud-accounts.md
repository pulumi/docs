---
title: Connect Cloud Accounts
title_tag: Connect Cloud Accounts | Discovery & Governance
h1: Connect Cloud Accounts
meta_desc: Use the Connect cloud accounts wizard to onboard AWS, Azure, and Google Cloud accounts to Pulumi in bulk with OIDC authentication.
menu:
  insights:
    name: Connect Cloud Accounts
    parent: insights-discovery
    weight: 15
pulumi_cloud_feature: insights-discovery
---

The **Connect cloud accounts** wizard onboards one or more cloud accounts to Pulumi in a single guided flow. It discovers the accounts in your AWS organization, Azure tenant, or Google Cloud organization, then sets up everything each account needs: short-lived credentials based on OpenID Connect (OIDC), a [Pulumi ESC (Environments, Secrets, and Configuration)](/docs/esc/) environment, a scheduled discovery scan, and an optional policy pack. With the recommended authentication options, no long-lived cloud secrets are stored in Pulumi Cloud.

The wizard supports bulk discovery for AWS, Microsoft Azure, and Google Cloud. Kubernetes and Oracle Cloud accounts connect through an existing ESC environment instead; for those providers, or to set up a single account manually, see [Create and manage cloud accounts](/docs/insights/discovery/accounts/).

## Prerequisites

- You must have permission in your Pulumi organization to connect cloud accounts and create ESC environments. Organization admins have these permissions by default. Members without them see a screen asking them to contact an organization admin.
- You need administrative access to the cloud organization you are connecting: the ability to authorize applications and create IAM resources in AWS, grant admin consent in Microsoft Entra ID, or grant organization-level roles in Google Cloud. The access each provider flow requests is described in [Step 2: Authenticate](#step-2-authenticate).

{{% notes type="info" %}}
Resource scans and policy evaluations consume workflow minutes and can incur charges beyond your plan's included allowance. See [Pulumi pricing](/pricing/) for details.
{{% /notes %}}

## Start the wizard

You can open the wizard from two places in the Pulumi Cloud console:

- Navigate to **Management** > **Accounts** and select **Connect cloud accounts**.
- On the home dashboard, select the **Connect cloud accounts** task on the **Get to know Pulumi** card.

The wizard opens as a panel and walks you through the onboarding steps.

## Step 1: Choose a cloud provider

Select the provider you want to connect: AWS, Microsoft Azure, or Google Cloud. Kubernetes and Oracle Cloud are also listed, but they connect through an existing ESC environment rather than the bulk discovery flow.

![The Connect cloud accounts wizard showing the cloud provider selection step with AWS, Azure, Google Cloud, Kubernetes, and Oracle Cloud options](/docs/insights/assets/connect-cloud-accounts-provider.png)

## Step 2: Authenticate

Each provider offers a recommended browser-based sign-in that uses OIDC, plus alternatives: static credentials, an existing ESC environment that already has credentials configured, or the Pulumi CLI.

{{% chooser cloud "aws,azure,gcp" %}}

{{% choosable cloud aws %}}

**Connect using IAM Identity Center (SSO)** is the recommended option. Provide your organization's **SSO start URL** (for example, `https://d-xxxxxxxxxx.awsapps.com/start`) and its **Region**. You can find both in the settings summary of your organization's IAM Identity Center instance. When you continue, AWS opens an authorization page in a new window; confirm that the verification code shown matches the one in the wizard, then approve the request. The wizard then lists every AWS account you can access in your organization. Authentication doesn't create anything in your accounts; the wizard creates the IAM role in each account later, after you select accounts and choose an access level.

![The authentication step for AWS showing the IAM Identity Center option selected with SSO start URL and region fields](/docs/insights/assets/connect-cloud-accounts-authentication.png)

Alternatively, you can connect using:

- **Static credentials**: an access key ID, secret access key, and region for an IAM principal that has the `organizations:ListAccounts`, `organizations:DescribeOrganization`, `sts:GetCallerIdentity`, and `iam:GetUser` permissions.
- **Existing ESC credentials**: an ESC environment that already has AWS credentials configured. See [configuring OIDC for AWS](/docs/esc/guides/configuring-oidc/aws/).
- **Pulumi CLI**: instructions for connecting from the command line.

{{% /choosable %}}

{{% choosable cloud azure %}}

**Connect using OpenID Connect (OIDC)** is the recommended option. Pulumi uses workload identity federation with Microsoft Entra ID, so no client secrets are stored. Provide your **Tenant ID (Directory ID)**, which you can find under **Microsoft Entra ID** > **Properties** in the Azure portal. When you continue, Microsoft consent pages open asking you to grant Pulumi:

- Microsoft Graph permissions to create and manage the app registration Pulumi uses (`Application.ReadWrite.All`, `ServicePrincipalEndpoint.ReadWrite.All`, and `User.Read`)
- Access to Azure Resource Manager on your behalf, used to discover your subscriptions

Consent doesn't grant any roles on your subscriptions. The wizard assigns the **Reader** or **Contributor** role on each subscription later, after you select subscriptions and choose an access level.

After you grant consent, the wizard lists the subscriptions in your tenant, including subscriptions you can reach through a role assignment on a management group. If your subscriptions are organized under management groups, see [Azure management groups](#azure-management-groups).

Alternatively, you can connect using:

- **Client secret**: a tenant ID, client ID, client secret, and subscription ID for an existing app registration.
- **Existing ESC credentials**: an ESC environment that already has Azure credentials configured. See [configuring OIDC for Azure](/docs/esc/guides/configuring-oidc/azure/).
- **Pulumi CLI**: instructions for connecting from the command line.

{{% /choosable %}}

{{% choosable cloud gcp %}}

**Connect using Workload Identity Federation** is the recommended option. Pulumi federates directly with Google Cloud, so no service account keys are stored. When you continue, a Google consent page opens asking you to grant Pulumi OAuth scopes for read-only access to your cloud resources, IAM, and service management (`cloud-platform.read-only`, `iam`, and `service.management`). The wizard uses this access to discover your projects.

Consent doesn't grant any roles on your projects. The wizard grants the **Viewer** or **Editor** role in each project later, after you select projects and choose an access level.

You can optionally enter your numeric **Organization ID** to restrict discovery to a single Google Cloud organization, including projects under its folders. Find it in the Google Cloud console under **IAM & Admin** > **Settings**; it is distinct from the project ID, project number, and location ID. Leave it blank to list every project you can access.

Alternatively, you can connect using:

- **Service account key**: a service account key in JSON format.
- **Existing ESC credentials**: an ESC environment that already has Google Cloud credentials configured. See [configuring OIDC for Google Cloud](/docs/esc/guides/configuring-oidc/gcp/).
- **Pulumi CLI**: instructions for connecting from the command line.

{{% /choosable %}}

{{% /chooser %}}

## Step 3: Select accounts and an access level

### Choose accounts

The wizard shows how many accounts, subscriptions, or projects it discovered and pre-selects everything that isn't already connected. Select **Edit selected accounts** (the label matches the provider: accounts, subscriptions, or projects) to open the picker, where you can search, select all, or toggle individual accounts. Accounts that are already connected appear with an **Already onboarded** badge and can't be selected again. You must select at least one account to continue.

![The account picker showing discovered AWS accounts with checkboxes, a search box, and a select all option](/docs/insights/assets/connect-cloud-accounts-picker.png)

### Choose an access level

The access level determines which permissions Pulumi receives in each account:

- **Build & Manage (read and write)**: the default. Enables [Pulumi Neo](/docs/ai/), infrastructure as code, deployments, and policies that remediate issues automatically (Enterprise+ edition). Grants `AdministratorAccess` in AWS, **Contributor** in Azure, or **Editor** in Google Cloud.
- **Discovery & Policy (read-only)**: limited to discovery scanning and inventory. Pulumi can't modify your infrastructure. Grants `ReadOnlyAccess` in AWS, **Reader** in Azure, or **Viewer** in Google Cloud.

Select **Change access level** to switch the default, or set a different level for individual accounts under **Per account access**. If your security review requires it, start with read-only access; you can raise access for specific accounts later.

![The accounts step showing the selected accounts summary, the Build and Manage access level card, and per account access controls](/docs/insights/assets/connect-cloud-accounts-access-level.png)

## Step 4: Configure discovery and policy

These settings apply to every account you're connecting. You can adjust each account's scanning and policy settings after setup from its **Manage** tab.

![The discovery step showing the scanning toggle, scan frequency dropdown, AWS partition selector, scan regions selector, and policy pack settings](/docs/insights/assets/connect-cloud-accounts-discovery.png)

### Scan schedule

Scheduled scans are enabled by default and run every 24 hours. You can switch to a 12-hour schedule, or turn scanning off and enable it later from the **Accounts** page.

### AWS partition (AWS only)

For AWS, choose the partition your accounts run in. The default is AWS Standard, and alternative partitions such as AWS GovCloud (US) and AWS China are also available.

### Scan regions (AWS only)

For AWS, choose the regions to scan. The defaults are `us-east-1`, `us-east-2`, `us-west-2`, and `eu-west-1`, and at least one region is required. Global services such as IAM, Route 53, and CloudFront are always scanned regardless of region selection.

### Policy pack

Policy evaluation is enabled by default, and the pack depends on your organization's edition. The Essentials and Pro editions apply the Pulumi Best Practices pack for your provider. The Enterprise+ edition applies a provider-specific compliance pack by default (the CIS AWS Foundations Benchmark, CIS Microsoft Azure Foundations Benchmark, or CIS Google Cloud Platform Foundations Benchmark), and for AWS or Google Cloud, you can choose NIST 800-53 instead. You can also turn policy off. See [pre-built policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for what each pack checks, and [Pricing](/pricing/) for edition availability.

When you're done, select **Next**. The wizard then creates the resources described in [What the wizard creates](#what-the-wizard-creates) and connects each selected account.

## Step 5: Review the summary

After setup completes, the summary shows:

- The ESC environments the wizard created, grouped by access level
- The state of discovery scanning, including the regions being scanned for AWS
- The policy pack applied, if any
- Suggested next steps, such as viewing discovered resources, reviewing policy findings, asking Pulumi Neo about your infrastructure, or importing resources into Pulumi IaC

If some accounts couldn't be connected, the summary lists each failed account with the error it hit so you can fix the cause and retry. See [Troubleshooting](#troubleshooting).

![The summary step showing setup complete with discovery running, the policy pack applied, and the list of created ESC environments](/docs/insights/assets/connect-cloud-accounts-summary.png)

## What the wizard creates

The recommended flows authenticate with OIDC and workload identity federation, so Pulumi Cloud does not store long-lived cloud secrets. The wizard automates the same setup described in the manual OIDC guides for [AWS](/docs/esc/guides/configuring-oidc/aws/), [Azure](/docs/esc/guides/configuring-oidc/azure/), and [Google Cloud](/docs/esc/guides/configuring-oidc/gcp/).

### In your cloud provider

- **AWS**: in each selected account, an IAM OIDC identity provider for Pulumi Cloud and an IAM role named `pulumi-esc-oidc-<your Pulumi organization>-<policy>-role`, where `<policy>` is the managed policy attached to the role: `AdministratorAccess` or `ReadOnlyAccess`, depending on the access level.
- **Azure**: one app registration with a federated identity credential and service principal, shared across the tenant, plus a **Contributor** or **Reader** role assignment on each selected subscription.
- **Google Cloud**: in each selected project, a workload identity pool and provider, and a service account named `pulumi-oidc` with the **Editor** or **Viewer** role.

### In Pulumi Cloud

- ESC environments in a project named `discover`. AWS and Google Cloud get one environment per account or project, named `discover/<name>-<accountId>-env`. Azure gets one shared environment per tenant, named `discover/azure-<tenantId>-env`, which every subscription's cloud account references.
- A cloud account in Pulumi for each selected provider account, subscription, or project, named after the provider account it represents.
- The scan schedule and, if enabled, the policy pack you chose.

## Azure management groups

Pulumi models each Azure subscription as its own cloud account. No management-group-level account exists, and a single cloud account can't scan more than one subscription. What is shared across your tenant is the *identity*: the wizard creates one app registration, one federated identity credential, and one service principal for the whole tenant, plus one ESC environment (`discover/azure-<tenantId>-env`) that every subscription's cloud account references. Connecting 40 subscriptions produces 40 cloud accounts, but still only one app registration and one set of credentials.

If your subscriptions are organized under management groups, you have two options.

### Let the wizard assign roles per subscription

This is the default flow. The wizard assigns the **Reader** or **Contributor** role at the scope of each subscription you select, so you need permission to create role assignments on those subscriptions — the **Owner** or **User Access Administrator** role, either assigned directly or inherited from a management group.

The wizard doesn't detect access that the service principal already inherits from a management group. If you have already granted the service principal Pulumi uses a role at management-group scope, the wizard adds a subscription-scoped assignment anyway, which is redundant but harmless.

### Grant the role yourself at management-group scope

If your organization prefers to manage RBAC centrally, assign **Reader** or **Contributor** to a service principal once at management-group scope, then connect subscriptions with **Connect using existing ESC credentials** so that Pulumi doesn't create role assignments. Set up the app registration and ESC environment as described in [Create and manage cloud accounts](/docs/insights/discovery/accounts/#azure) and [Configuring OpenID Connect for Azure](/docs/esc/guides/configuring-oidc/azure/).

Because the environment carries the subscription ID, this path takes one ESC environment and one wizard run per subscription. Reuse a single app registration across those environments rather than creating one per subscription. Each environment needs its own federated identity credential, because the subject identifier includes the environment path, and Azure limits an app registration to 20 federated identity credentials. If you are onboarding more subscriptions than that, use the wizard's OIDC flow, which shares a single environment and credential across the tenant.

## Troubleshooting

### Some accounts failed to connect

When setup is partially complete, the summary lists each failed account with the error returned by Pulumi. Fix the underlying issue and run the wizard again. Accounts that connected successfully are recognized and skipped. Or set up the remaining accounts manually by following [Create and manage cloud accounts](/docs/insights/discovery/accounts/).

### AWS IAM role creation is denied

If you don't have permission to create the IAM trust role in an AWS account, ask an AWS administrator in your organization to run the wizard, or choose **Connect using existing ESC credentials** on the authentication step to use an ESC environment with credentials that were set up ahead of time.

### You don't have permission to connect accounts

Connecting a cloud account creates an ESC environment and a trust role in your cloud provider, which requires elevated permissions in Pulumi Cloud. Ask an organization admin to run the connection flow on your behalf, or to grant your role permission to connect accounts. Once an account has been connected, you can view its scanned resources, run policy reports, and create stacks against the ESC environments shared with you.

## Next steps

- [Search your discovered resources](/docs/insights/discovery/search/)
- [Review policy findings](/docs/insights/policy/policy-findings/)
- [Import discovered resources into Pulumi IaC](/docs/insights/discovery/visual-import/)

## Learn more

- [Get started with Discovery](/docs/insights/discovery/get-started/)
- [Pulumi ESC](/docs/esc/)
