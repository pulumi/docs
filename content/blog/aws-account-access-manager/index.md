---
title: "Scale-up your team’s use of AWS Account Access Manager with Pulumi Infrastructure as Code"
allow_long_title: true
linktitle: "Manage AWS Account Access Manager with Pulumi"
date: 2026-09-22
draft: true
meta_desc: "Account access manager is fully supported in Pulumi. Define the IAM roles, applications, and entitlements behind workforce access as code, in any language."
authors:
    - tatiana-cooke
tags:
    - aws
    - iam
    - security
    - infrastructure-as-code
category: product
---

{{% notes type="warning" %}}
**Reviewer notes (delete before submission)**

- **Format:** Modeled on the APN post "How to strengthen cloud security with Pulumi ESC and AWS Secrets Manager" (problem → solution → walkthrough → customer example → conclusion → Partner Spotlight), with the direct launch-announcement opening of the Cloud Control provider post. ~1,400 words.
- **Customer example is anonymized.** It draws on the Nubank / AWS sync (Sep 15). Naming Nubank requires written approval from Nubank and AWS; the swap-in text is in the customer section. Nothing from the call about their internal tooling or their Java SDK dependency appears by name.
- **Co-authors TBD:** Suggest asking Laura Aray (AWS SA, Identity Center / AAM) and Diego Rocha (AWS SA, Security) to co-author. Their involvement also gets us into the launch partner page.
- **To verify before submission:** (1) the minimum pulumi-aws and aws-native versions that include `accountaccess` (placeholders marked **vX.Y.Z**); (2) whether our Partner tier and Competency wording is still current; (3) Run the code samples end to end against a sandbox org. They're built from the registry docs but haven't been executed.
- **Decision for you:** The draft leads with the Java example for the entitlement because JVM teams were the specific ask. If the AWS editors want TypeScript only, drop the Java block. Don't add more languages, because it makes the post too long.
{{% /notes %}}

*By Tatiana Cooke, VP of Product – Pulumi*

*By [AWS co-author], [Title] – AWS*

*By [AWS co-author], [Title] – AWS*

> **Pulumi** — AWS Partner · [Connect with Pulumi]

[XXX], AWS Identity and Access Management (IAM) launched **Account Access Manager**, which lets administrators assign IAM roles to workforce users and groups in AWS IAM Identity Center. Account access manager combines Identity Center's single federation point and user awareness with the flexibility of IAM roles.

Today, as part of our partner launch enablement we're pleased to share that account access manager is fully supported in Pulumi. You can manage account access manager applications and entitlements with the Pulumi AWS provider and the Pulumi AWS Cloud Control provider (AWS Native). Both work in every Pulumi language: TypeScript, Python, Go, C#, Java, HCL, and YAML. Teams that already manage their AWS organization with Pulumi can adopt account access manager in the same stacks, languages, and review workflows they use today. If you’re not using Pulumi today, this post demonstrates how usage of IaC can help you adopt new AWS services and securely scale them out to your organization faster.

In this post, we explain where account access manager fits alongside permission sets. We walk through defining roles, applications, and entitlements as code, and we describe how one financial services customer is using this pattern to move its workforce access to IAM Identity Center.

## The challenge: flexible roles vs. centralized access

Until now, organizations managing human access across many AWS accounts have had to choose between two approaches.

**IAM Identity Center permission sets** provide a single sign-on experience and centralized user awareness. Identity Center provisions a permission set into each account as a uniform role. That works well for baseline access, such as read-only or administrator access that looks the same everywhere. But many enterprises need roles that differ from account to account. These roles carry account-specific policies, tags for attribute-based access control (ABAC), custom trust policies, or role paths that encode team and environment. As organizations add accounts, teams, and specialized roles, some of them run into the scaling limits of the permission set model.

**Per-account IAM roles with direct federation** give complete control over each role. The cost is fragmentation: identity-provider configuration in every account, no single portal for users, and no central view of who can reach what.

Account access manager removes this tradeoff. You keep your own IAM roles, with their policies, tags, paths, and trust conditions. You assign those roles to Identity Center users and groups from one place. Users sign in once, see the accounts and roles assigned to them in the account access portal, and get CLI credentials with `aws login`.

## Why manage account access manager with infrastructure as code

Account access manager moves more of your access model into IAM roles that you own. AWS provisions permission sets automatically, but account access manager roles have to be created by you, either by hand or with infrastructure as code. At enterprise scale, three things matter:

- **The role and the assignment belong together.** An entitlement is only useful if the role it points to exists and has the right trust policy. Defining both in the same Pulumi program means they're created, updated, and destroyed as a unit, so you don't leave orphaned roles or assignments behind.
- **Access changes should go through review.** A new entitlement is a new path into a production account. Through `pulumi preview`, pull requests, and policy as code, access changes get the same review and audit trail as other infrastructure changes.
- **Programming languages make it simple.** Mapping groups to roles across dozens or hundreds of accounts is a data-transformation problem. General-purpose languages let you express it with loops, functions, and shared components instead of hand-maintained lists.

## How it works in Pulumi

The account access manager API (`account-access`) centers on two resources. Both are available in the Pulumi AWS provider under the `aws.accountaccess` module:

| Resource | Purpose |
|---|---|
| `aws.accountaccess.Application` | Binds account access manager to your IAM Identity Center organization instance. It's the parent container for all entitlements. You can have one per Identity Center instance. |
| `aws.accountaccess.Entitlement` | Grants an Identity Center user or group the ability to assume a specific IAM role in a target account. |

The same resources are available in the AWS Cloud Control provider (`aws-native.accountaccess`), which generates its resources directly from the AWS CloudFormation registry.

### Prerequisites

- An **organization instance** of IAM Identity Center, enabled in your AWS Organizations management account (account instances aren't supported)
- Trusted access for account access manager in AWS Organizations:

```bash
aws organizations enable-aws-service-access \
  --service-principal account-access.amazonaws.com
```

- Pulumi CLI and Pulumi AWS provider **vX.Y.Z** or later

### Step 1: Create the account access manager application

First, look up your Identity Center instance and create the application in the same Region:

```typescript
import * as aws from "@pulumi/aws";

const identityCenter = aws.ssoadmin.getInstancesOutput({});

const accessApp = new aws.accountaccess.Application("workforce-access", {
    identitySource: {
        identityCenter: {
            instanceArn: identityCenter.arns[0],
        },
    },
    tags: { "managed-by": "pulumi" },
});
```

### Step 2: Define a role that account access manager can assume

Roles used with account access manager must trust the `account-access.amazonaws.com` service principal for `sts:AssumeRole`, `sts:SetContext`, and `sts:TagSession`. `sts:TagSession` is required for credential retrieval to succeed. Because this is your own IAM role, you can use a path to group roles by team and apply tags that drive ABAC policies:

```typescript
// Provider for a workload account in the organization
const paymentsProd = new aws.Provider("payments-prod", {
    assumeRoles: [{ roleArn: "arn:aws:iam::111122223333:role/PlatformAutomation" }],
});

const deployerRole = new aws.iam.Role("payments-deployer", {
    path: "/workforce/payments/",
    assumeRolePolicy: JSON.stringify({
        Version: "2012-10-17",
        Statement: [{
            Effect: "Allow",
            Principal: { Service: "account-access.amazonaws.com" },
            Action: ["sts:AssumeRole", "sts:SetContext", "sts:TagSession"],
        }],
    }),
    tags: {
        team: "payments",
        environment: "prod",
    },
}, { provider: paymentsProd });

new aws.iam.RolePolicyAttachment("payments-deployer-policy", {
    role: deployerRole.name,
    policyArn: "arn:aws:iam::aws:policy/PowerUserAccess",
}, { provider: paymentsProd });
```

### Step 3: Assign the role to an Identity Center group

Next, look up the Identity Center group and create an entitlement that connects it to the role:

```typescript
const paymentsEngineers = aws.identitystore.getGroupOutput({
    identityStoreId: identityCenter.identityStoreIds[0],
    alternateIdentifier: {
        uniqueAttribute: {
            attributePath: "DisplayName",
            attributeValue: "payments-engineers",
        },
    },
});

new aws.accountaccess.Entitlement("payments-engineers-deployer", {
    applicationArn: accessApp.arn,
    entitlement: {
        principalRole: {
            principal: {
                identityCenter: { groupId: paymentsEngineers.groupId },
            },
            roleArn: deployerRole.arn,
        },
    },
});
```

Many enterprise platform teams build on the JVM. Here's the same entitlement in Java:

```java
var entitlement = new Entitlement("payments-engineers-deployer", EntitlementArgs.builder()
    .applicationArn(accessApp.arn())
    .entitlement(EntitlementEntitlementArgs.builder()
        .principalRole(EntitlementEntitlementPrincipalRoleArgs.builder()
            .principal(EntitlementEntitlementPrincipalRolePrincipalArgs.builder()
                .identityCenter(EntitlementEntitlementPrincipalRolePrincipalIdentityCenterArgs.builder()
                    .groupId(paymentsEngineers.applyValue(g -> g.groupId()))
                    .build())
                .build())
            .roleArn(deployerRole.arn())
            .build())
        .build())
    .build());
```

Run `pulumi up`. After the update completes, members of `payments-engineers` see the payments production account in their account access portal. They can get credentials from the command line with `aws login`.

### Step 4: Scale the pattern across the organization

In practice, you'll define the access model once and generate entitlements from it. Entitlements are immutable, so Pulumi replaces an entitlement when its role or principal changes, and the preview shows that replacement before anything happens:

```typescript
const accessModel = [
    { group: "payments-engineers", roles: [paymentsDeployerProd, paymentsReadOnlyStaging] },
    { group: "sre-oncall",          roles: [breakGlassProd, observabilityAllAccounts] },
];

for (const { group, roles } of accessModel) {
    const g = lookupGroup(group);
    for (const role of roles) {
        new aws.accountaccess.Entitlement(`${group}-${role.name}`, {
            applicationArn: accessApp.arn,
            entitlement: {
                principalRole: {
                    principal: { identityCenter: { groupId: g.groupId } },
                    roleArn: role.arn,
                },
            },
        });
    }
}
```

If you already created application or entitlements through the API or console, bring them under management with `pulumi import`:

```bash
pulumi import aws:accountaccess/entitlement:Entitlement payments-engineers-deployer \
  arn:aws:account-access:us-east-1:123456789012:application/aam-0123456789abcdef,ent-0123456789abcdef
```

### Enforce guardrails with policy as code

Because access is now defined in code, you can check it before it's deployed. With Pulumi Policies, platform teams can require that every role referenced by an entitlement includes `sts:TagSession` in its trust policy. Pulumi [provides AWS Best Practices policies](https://www.pulumi.com/docs/reference/pre-built-policy-packs/pulumi-best-practices/aws/) to help customers manage this type of logic using policy as code. They can also require that production roles sit under an approved path, or block direct user assignments in favor of groups. Violations surface in `pulumi preview` and in pull requests before any access is granted.

## Customer example: moving workforce access to IAM Identity Center at a leading digital bank

{{% notes type="warning" %}}
Anonymized pending approval. If Nubank approves, replace "a leading digital bank in Latin America" with "Nubank" and add a quote from its cloud IAM team.
{{% /notes %}}

A leading digital bank in Latin America uses Pulumi to provision IAM and identity resources across a large AWS organization. The bank's cloud IAM team is moving its workforce from per-account IAM roles to IAM Identity Center. As it planned the migration, it worked with AWS to adopt account access manager rather than permission sets. The bank's access model depends on roles tailored to each account, and at its scale it was running into the limits of permission sets.

The team already managed Identity Center account assignments for permission sets in Pulumi stacks. For account access manager, it initially called the new public API directly from internal tooling. But the team wanted assignments between Identity Center groups and IAM roles to be managed in the same Pulumi stacks as the roles themselves. That way, the full lifecycle, including clean teardown when a team or account is retired, is handled by the same program that created them.

With native `accountaccess` resources in the Pulumi AWS provider, the team can manage roles and entitlements together, in the JVM language its platform tooling already uses, through its existing review and deployment workflow.

## Conclusion

Account access manager gives AWS customers a way to keep the flexibility of their own IAM roles while centralizing workforce access through IAM Identity Center. It also moves more of the access model into resources that customers create and own. Managing those roles and entitlements with Pulumi means access changes are versioned, reviewed, and deployed together, in the language your team already uses.

To get started:

- Read [Account access manager](https://docs.aws.amazon.com/IAM/latest/UserGuide/account-access-manager.html) in the AWS IAM User Guide.
- Explore the [aws.accountaccess.Application](https://www.pulumi.com/registry/packages/aws/api-docs/accountaccess/application/) and [aws.accountaccess.Entitlement](https://www.pulumi.com/registry/packages/aws/api-docs/accountaccess/entitlement/) resources in the Pulumi Registry.
- Try Pulumi for free at [pulumi.com](https://www.pulumi.com), and file feedback or feature requests in the [pulumi-aws GitHub repository](https://github.com/pulumi/pulumi-aws).

---

### Pulumi – AWS Partner Spotlight

**Pulumi is an AWS Advanced Technology Partner and AWS Competency Partner** that makes it easy for platform engineering teams to automate, secure, and manage any cloud deployment with infrastructure as code, centralized secrets management, policy enforcement, and analytics capabilities.

[Contact Pulumi] | [Partner Overview] | [AWS Marketplace]

---

### About the authors

**Tatiana Cooke** is VP of Product at Pulumi, where she leads product management, design, content engineering, and data engineering. She previously worked at AWS and Samsara, and focuses on infrastructure as code, platform engineering, and agentic infrastructure.

**[AWS co-author]** — [bio]

**[AWS co-author]** — [bio]
