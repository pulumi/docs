---
title_tag: Configure OpenID Connect for AWS with Pulumi Deployments | OIDC
meta_desc: This page describes how to configure OIDC token exchange in AWS for use with Pulumi Deployments
title: AWS
h1: Configuring OpenID Connect for AWS with Pulumi Deployments
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  deployments:
    name: AWS
    parent: deployments-guides-oidc
    weight: 1
    identifier: deployments-guides-oidc-aws
aliases:
  - /docs/administration/access-identity/oidc/provider/aws/
  - /docs/guides/oidc/provider/aws
  - /docs/intro/deployments/oidc/provider/aws/
  - /docs/pulumi-cloud/access-management/oidc/provider/aws/
  - /docs/pulumi-cloud/deployments/oidc/aws/
  - /docs/deployments/deployments/oidc/aws/
  - /docs/pulumi-cloud/deployments/oidc/provider/aws/
  - /docs/pulumi-cloud/oidc/aws/
  - /docs/pulumi-cloud/oidc/provider/aws/
---

{{< esc-recommendation >}}

This document outlines the steps required to configure Pulumi Deployments to use OpenID Connect to authenticate with AWS. OIDC in AWS uses a web identity provider to assume an IAM role. Access to the IAM role is authorized using a trust policy that validates the contents of the OIDC token issued by Pulumi Cloud.

Configuring OIDC for AWS involves two sides:

1. **AWS** — register Pulumi Cloud as an OIDC identity provider and create an IAM role that trusts it. You can do this in the [AWS console](#using-the-aws-console) or [programmatically](#using-infrastructure-as-code).
1. **Pulumi Deployments** — enable the AWS OIDC integration for your stack so that each deployment exchanges its OIDC token for credentials from that role. You can do this in the [Pulumi Cloud console](#using-the-pulumi-cloud-console) or [programmatically with the Pulumi Service provider](#using-infrastructure-as-code-1).

## Configure AWS

{{% notes type="info" %}}
Deployments must authenticate against an OIDC provider in **each** AWS account it deploys to, and AWS allows only **one** OIDC provider per URL in an account. Register the `https://api.pulumi.com/oidc` provider once per account. If it already exists — for example, because you also use it with [Pulumi ESC](/docs/esc/guides/configuring-oidc/aws/) or configured Deployments OIDC previously — don't create a second one. Instead, add only an IAM role that trusts the existing provider, and confirm your Pulumi organization is listed among the provider's audiences (adding one if needed, as described [below](#using-infrastructure-as-code)).
{{% /notes %}}

### Using the AWS console

#### Create the identity provider

1. In the navigation pane of the [IAM console](https://console.aws.amazon.com/iam/), choose **Identity providers**, and then choose **Add provider**.
1. In the **Provider type** section, click the radio button next to **OpenID Connect**.
1. For the **Provider URL**, provide the following URL: `https://api.pulumi.com/oidc`
1. For the **Audience** field, enter the name of your Pulumi organization. Then select **Add provider**.

{{% notes type="info" %}}
The audience must exactly match your Pulumi organization name, which is always lowercase (the value shown in the Pulumi Console URL, `app.pulumi.com/<org>`). AWS compares the token's `aud` claim using a case-sensitive `StringEquals` condition — on both the provider's registered audience and the role's trust policy — so entering it with different casing (for example, a capitalized display name) causes the credential exchange to fail with no obvious error.
{{% /notes %}}

#### Configure the IAM role and trust policy

Once you have created the identity provider, you will see a notification at the top of your screen prompting you to assign an IAM role.

1. Select the **Assign role** button.
1. Select the **Create a new role** option, then select **Next**.
1. On the IAM **Create role** page, ensure the **Web identity** radio button is selected.
1. In the **Web identity** section:
    * Select `api.pulumi.com/oidc` under **Identity provider**.
    * Select the name of your Pulumi organization under **Audience**. Then select **Next**.
1. On the **Add permissions** page, select the permissions that you want to grant to your Pulumi deployments. Then select **Next**.
1. Provide a name and optional description for the IAM role. Then select **Create role**.

Make a note of the IAM role's ARN; it will be necessary to enable OIDC for your deployment.

{{% notes type="info" %}}
When choosing permissions on the **Add permissions** step above, keep in mind that many Pulumi programs create IAM roles, policies, or instance profiles (e.g., for Lambda, ECS, or EKS), which require IAM permissions. While `AdministratorAccess` is the simplest policy that covers all services including IAM, it is broader than most workloads need. For better security, consider one of these alternatives:

* **PowerUserAccess + IAMFullAccess** — provides broad service access with IAM permissions but excludes AWS Organizations management.
* **Custom least-privilege policy** — scoped to only the AWS services and IAM actions your Pulumi program uses (e.g., `ec2:*`, `s3:*`, `iam:CreateRole`, `iam:AttachRolePolicy`, `iam:PassRole`).
* **Permissions boundary** — use a broader role policy but attach an [IAM permissions boundary](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) to cap the privileges of any IAM entities that Pulumi creates, preventing privilege escalation.

You can also further constrain the assumed role session using the **Policy ARNs** field in the Pulumi Deployments OIDC configuration.
{{% /notes %}}

##### Restricting role assumption to Pulumi Cloud scopes

The following restricts to any deployment in your organization:

```json
"Condition": {
  "StringEquals": {
    "api.pulumi.com/oidc:aud": "<your-org-name>"
  },
  "StringLike": {
    "api.pulumi.com/oidc:sub": "pulumi:deploy:org:<your-org-name>:*"
  }
}
```

The following restricts to any stack within a specific project:

```json
"Condition": {
  "StringEquals": {
    "api.pulumi.com/oidc:aud": "<your-org-name>"
  },
  "StringLike": {
    "api.pulumi.com/oidc:sub": "pulumi:deploy:org:<your-org-name>:project:<your-project-name>:*"
  }
}
```

The subject claim also includes the stack name and operation, so you can restrict further. See the [full subject format and custom claims](/docs/deployments/guides/oidc/#custom-claims) for details.

### Using infrastructure as code

You can register the identity provider and create the IAM role with a Pulumi program instead of the console. The following example uses TypeScript and the [AWS provider](/registry/packages/aws/); the same resources are available in every Pulumi language.

```typescript
import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

const org = "<your-org-name>";

// Register Pulumi Cloud as an OIDC identity provider. The audience (clientIdLists)
// is your Pulumi organization name.
const provider = new aws.iam.OpenIdConnectProvider("pulumi-deployments-oidc", {
    url: "https://api.pulumi.com/oidc",
    clientIdLists: [org],
});

// Create the IAM role that deployments will assume, trusting the provider above.
const role = new aws.iam.Role("pulumi-deployments-oidc", {
    assumeRolePolicy: pulumi.jsonStringify({
        Version: "2012-10-17",
        Statement: [{
            Effect: "Allow",
            Principal: { Federated: provider.arn },
            Action: "sts:AssumeRoleWithWebIdentity",
            Condition: {
                StringEquals: { "api.pulumi.com/oidc:aud": org },
                StringLike: { "api.pulumi.com/oidc:sub": `pulumi:deploy:org:${org}:*` },
            },
        }],
    }),
});

// Attach the permissions your deployments need. Scope this down for production.
new aws.iam.RolePolicyAttachment("pulumi-deployments-oidc", {
    role: role.name,
    policyArn: "arn:aws:iam::aws:policy/AdministratorAccess",
});

export const roleArn = role.arn;
```

{{% notes type="warning" %}}
AWS allows only **one** OIDC identity provider per URL per account, and there is no standalone resource for managing a provider's audiences. If `https://api.pulumi.com/oidc` is already registered in your account — for example, because you also use it with [Pulumi ESC](/docs/esc/guides/configuring-oidc/aws/) — recreating it with Pulumi will conflict. To add your organization as an additional audience on the existing provider, use the AWS CLI:

```bash
aws iam add-client-id-to-open-id-connect-provider \
  --open-id-connect-provider-arn arn:aws:iam::<account-id>:oidc-provider/api.pulumi.com/oidc \
  --client-id <your-org-name>
```

{{% /notes %}}

## Configure Pulumi Deployments

### Using the Pulumi Cloud console

1. Navigate to your stack in the Pulumi Console.
1. Open the stack's "Settings" tab.
1. Choose the "Deploy" panel.
1. Under the "OpenID Connect" header, toggle "Enable AWS Integration".
1. Enter the ARN of the IAM role created above in the "Role ARN" field.
1. Enter a name for the assumed role session in the "Session Name" field. See [Session name](#session-name) for the supported template variables.
1. If you would like to use additional policies to further constrain the session's capabilities, enter the policies' ARNs separated by commas in the "Policy ARNs" field.
1. If you would like to constrain the duration of the assumed role session, enter a duration in the form "XhYmZs" in the "Session Duration" field.
1. Select the "Save deployment configuration" button.

### Using infrastructure as code

You can manage the same deployment settings in source control with the [`pulumiservice.DeploymentSettings`](/registry/packages/pulumiservice/api-docs/deploymentsettings/) resource (the OIDC configuration is set under `operationContext.oidc.aws`). Deployment settings can also be configured via the [REST API](/docs/deployments/deployments/api/#patchsettings).

```typescript
import * as pulumiservice from "@pulumi/pulumiservice";

new pulumiservice.DeploymentSettings("deployment-settings", {
    organization: "<your-org-name>",
    project: "<your-project-name>",
    stack: "<your-stack-name>",
    operationContext: {
        oidc: {
            aws: {
                roleARN: "<your-oidc-iam-role-arn>",
                sessionName: "pulumi-deployments",
                // Optional: further constrain the session.
                // policyARNs: ["arn:aws:iam::aws:policy/ReadOnlyAccess"],
                // duration: "1h",
            },
        },
    },
});
```

With this configuration, each deployment of this stack will attempt to exchange the deployment's OIDC token for AWS credentials using the specified IAM role prior to running any pre-commands or Pulumi operations. The fetched credentials are published in the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` environment variables. The raw OIDC token is also available for advanced scenarios in the `PULUMI_OIDC_TOKEN` environment variable and the `/mnt/pulumi/pulumi.oidc` file.

## Session name

The session name becomes the [`RoleSessionName`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) on the AWS STS `AssumeRoleWithWebIdentity` call and surfaces in every subsequent CloudTrail event as the last segment of the assumed-role principal ARN, so a templated session name makes each API call traceable to a specific Pulumi deployment.

### Template variables

The session name supports `${var}` placeholders that Pulumi substitutes when the deployment runs:

1. `${organization.name}`: Pulumi organization name.
1. `${project.name}`: Pulumi project name.
1. `${stack.name}`: Pulumi stack name.
1. `${deployment.operation}`: operation type (for example, `update`, `preview`, or `destroy`).
1. `${deployment.version}`: deployment version number.
1. `${deployment.id}`: deployment UUID.

A literal value with no `${...}` placeholders is passed through unchanged.

### Length and truncation

AWS caps `RoleSessionName` at 64 characters. If a rendered template would exceed that limit, Pulumi trims the truncatable name variables (`${organization.name}`, `${project.name}`, `${stack.name}`) from the end until the result fits. The protected variables (`${deployment.operation}`, `${deployment.version}`, `${deployment.id}`) are never trimmed, so each deployment remains identifiable.

For example, given the template:

```
${organization.name}-${project.name}-${stack.name}-${deployment.id}
```

with `organization.name = "pulumi-local"`, `project.name = "test-nocode-rtct-3"`, `stack.name = "dev"`, and `deployment.id = "806bf21f-444f-4825-a80c-afd12cd2526a"`, the full-length result would be 72 characters. Pulumi caps the three name variables to fit the budget while preserving the deployment UUID:

```
pulumi-loca-test-nocode-dev-806bf21f-444f-4825-a80c-afd12cd2526a
```

The result is exactly 64 characters: `${organization.name}` and `${project.name}` are each capped to 11 characters, `${stack.name}` is 3 characters and fits as-is, and the deployment UUID is preserved in full.
