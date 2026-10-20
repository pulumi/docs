---
title: "Scale your team's use of AWS IAM account access manager with Pulumi"
date: 2026-10-14
draft: false
meta_desc: "Manage AWS IAM account access manager (AAM) as code with Pulumi: define IAM roles, applications, and entitlements across your AWS organization in one program."
feature_image: feature.png
authors:
    - tatiana-cooke
tags:
    - aws
    - iam
    - security
    - infrastructure-as-code
category: product
schema_type: auto

social:
    twitter: |
        AWS access used to mean a tradeoff: IAM Identity Center permission sets are centralized but give every account the same role; per-account IAM roles are flexible but fragmented.

        AWS's account access manager ends it. Here's how to manage it as code.
    linkedin: |
        Teams managing human access across dozens of AWS accounts have had two options, and neither was great.

        IAM Identity Center permission sets give you one sign-on and a central view — but every account gets the same uniform role. Per-account IAM roles give you full control over policies, tags, paths, and trust conditions — but you lose the single portal and any central view of who can reach what.

        In September, AWS shipped account access manager (AAM) to remove that tradeoff: keep your own IAM roles, and assign them to IAM Identity Center users and groups from one place.

        You can now manage all of it as code with Pulumi — the roles and the assignments together, in the same stacks and languages your team already uses. One financial services customer is using it to move its entire workforce onto IAM Identity Center.

        Here's what that looks like.
    bluesky: |
        Managing AWS access has meant picking one: centralized permission sets that make every account identical, or per-account IAM roles that fragment everything.

        AWS's account access manager drops that tradeoff, and you can run it as code with Pulumi. Here's how.
---

In September 2026, AWS launched **AWS IAM account access manager (AAM)**, which lets administrators assign IAM roles to workforce users and groups in AWS IAM Identity Center. AAM combines IAM Identity Center's single federation point and user awareness with the flexibility of IAM roles.

<!--more-->

Today, as part of our partner launch enablement, we're pleased to share that you can manage AAM as code with Pulumi. The `accountaccess` resources ship in the Pulumi AWS provider (v7.45.0 and later) and in the Pulumi AWS Cloud Control provider, AWS Native (v1.75.0 and later), with SDKs generated for every Pulumi language: TypeScript, Python, Go, C#, Java, HCL, and YAML. Teams that already manage their AWS organization with Pulumi can adopt AAM in the same stacks, languages, and review workflows they use today. If you're not using Pulumi today, this post demonstrates how infrastructure as code can help you adopt new AWS services and securely scale them out to your organization faster.

In this post, we explain where AAM fits alongside permission sets. We walk through defining roles, applications, and entitlements as code, and we describe how one financial services customer is using this pattern to move its workforce access to IAM Identity Center.

## The challenge: flexible roles vs. centralized access

Until now, organizations managing human access across many AWS accounts have had to choose between two approaches.

**IAM Identity Center permission sets** provide a single sign-on experience and centralized user awareness. IAM Identity Center provisions a permission set into each account as a uniform role. That works well for baseline access, such as read-only or administrator access that looks the same everywhere. But many enterprises need roles that differ from account to account. These roles carry account-specific policies, tags for attribute-based access control (ABAC), custom trust policies, or role paths that encode team and environment. As organizations add accounts, teams, and specialized roles, some of them run into the scaling limits of the permission set model.

**Per-account IAM roles with direct federation** give complete control over each role. The cost is fragmentation: identity-provider configuration in every account, no single portal for users, and no central view of who can reach what.

AAM removes this tradeoff. You keep your own IAM roles, with their policies, tags, paths, and trust conditions. You assign those roles to IAM Identity Center users and groups from one place. Users sign in once, see the accounts and roles assigned to them in the account access portal, and get CLI credentials with `aws login`.

## Why manage AAM with infrastructure as code

AAM moves more of your access model into IAM roles that you own. AWS provisions permission sets automatically, but AAM roles have to be created by you, either by hand or with infrastructure as code. At enterprise scale, three things matter:

- **The role and the assignment belong together.** An entitlement is only useful if the role it points to exists and has the right trust policy. Defining both in the same Pulumi program means they're created, updated, and destroyed as a unit, so you don't leave orphaned roles or assignments behind.
- **Access changes should go through review.** A new entitlement is a new path into a production account. Through `pulumi preview`, pull requests, and policy as code, access changes get the same review and audit trail as other infrastructure changes.
- **Programming languages handle the scale.** Mapping groups to roles across dozens or hundreds of accounts is a data-transformation problem. General-purpose languages let you express it with loops, functions, and shared components instead of hand-maintained lists.

## How it works in Pulumi

The AAM API (`account-access`) centers on two resources. Both are available in the Pulumi AWS provider under the `aws.accountaccess` module:

| Resource | Purpose |
|----------|---------|
| `aws.accountaccess.Application` | Binds AAM to your IAM Identity Center organization instance. It's the parent container for all entitlements. You can have one per IAM Identity Center instance. |
| `aws.accountaccess.Entitlement` | Grants an IAM Identity Center user or group the ability to assume a specific IAM role in a target account. |

The same resources are available in the AWS Cloud Control provider (`aws-native.accountaccess`), which generates its resources directly from the AWS CloudFormation registry.

### Prerequisites

- An **organization instance** of IAM Identity Center, enabled in your AWS Organizations management account (account instances aren't supported)
- Trusted access for AAM in AWS Organizations:

```bash
aws organizations enable-aws-service-access \
  --service-principal account-access.amazonaws.com
```

- Pulumi CLI, and Pulumi AWS provider v7.45.0 or later (or Pulumi AWS Native v1.75.0 or later)

### Step 1: Create the AAM application

First, look up your IAM Identity Center instance and create the application in the same Region:

```typescript
import * as pulumi from "@pulumi/pulumi";
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

### Step 2: Define a role that AAM can assume

Roles used with AAM must trust the `account-access.amazonaws.com` service principal for `sts:AssumeRole` and `sts:SetContext`. Add `sts:TagSession` only if you want identity-provider attributes such as group membership or cost center to propagate as principal tags on the session; role assumption succeeds without it. AWS also recommends scoping the trust with `aws:SourceAccount` and `aws:SourceArn` conditions, so that only your AAM application can assume the role. Because this is your own IAM role, you can use a path to group roles by team and apply tags that drive ABAC policies:

```typescript
// Provider for a workload account in the organization
const paymentsProd = new aws.Provider("payments-prod", {
    assumeRoles: [{ roleArn: "arn:aws:iam::111122223333:role/PlatformAutomation" }],
});

const deployerRole = new aws.iam.Role("payments-deployer", {
    path: "/workforce/payments/",
    assumeRolePolicy: pulumi.jsonStringify({
        Version: "2012-10-17",
        Statement: [{
            Sid: "AccountAccessManagerTrust",
            Effect: "Allow",
            Principal: { Service: "account-access.amazonaws.com" },
            // sts:TagSession is optional. Include it only if policies in the target
            // account read principal tags (aws:PrincipalTag/<key>).
            Action: ["sts:AssumeRole", "sts:SetContext", "sts:TagSession"],
            Condition: {
                StringEquals: {
                    // The account where the AAM application lives.
                    "aws:SourceAccount": aws.getCallerIdentityOutput({}).accountId,
                    "aws:SourceArn": accessApp.arn,
                },
            },
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

### Step 3: Assign the role to an IAM Identity Center group

Next, look up the IAM Identity Center group and create an entitlement that connects it to the role:

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
const lookupGroup = (displayName: string) => aws.identitystore.getGroupOutput({
    identityStoreId: identityCenter.identityStoreIds[0],
    alternateIdentifier: {
        uniqueAttribute: { attributePath: "DisplayName", attributeValue: displayName },
    },
});

// Role keys are plain strings, so Pulumi resource names stay stable and readable.
const accessModel = [
    { group: "payments-engineers", roles: { "deployer-prod": paymentsDeployerProd, "readonly-staging": paymentsReadOnlyStaging } },
    { group: "sre-oncall", roles: { "break-glass-prod": breakGlassProd, "observability": observabilityAllAccounts } },
];

for (const { group, roles } of accessModel) {
    const g = lookupGroup(group);
    for (const [roleName, role] of Object.entries(roles)) {
        new aws.accountaccess.Entitlement(`${group}-${roleName}`, {
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

If you already created an application or entitlements through the API or console, bring them under management with `pulumi import`:

```bash
pulumi import aws:accountaccess/entitlement:Entitlement payments-engineers-deployer \
  arn:aws:account-access:us-east-1:123456789012:application/aam-0123456789abcdef,ent-0123456789abcdef
```

### Enforce guardrails with policy as code

Because access is now defined in code, you can check it before it's deployed. With a custom Pulumi policy pack, platform teams can require that every role referenced by an entitlement scopes its trust policy with `aws:SourceAccount` and `aws:SourceArn`, that production roles sit under an approved path, or that entitlements name groups rather than individual users. Pulumi also ships [pre-built AWS Best Practices policies](/docs/reference/pre-built-policy-packs/pulumi-best-practices/aws/) for common IAM and security checks. Violations surface in `pulumi preview` and in pull requests before any access is granted.

## Customer example: moving workforce access to IAM Identity Center at a leading digital bank

A leading digital bank uses Pulumi to provision IAM and identity resources across a large AWS organization. The bank's cloud IAM team is moving its workforce from per-account IAM roles to IAM Identity Center. As it planned the migration, it worked with AWS to adopt AAM rather than permission sets. Their access model depends on roles tailored to each account, and at its scale it was hitting the limits of permission sets.

The team already managed IAM Identity Center account assignments for permission sets in Pulumi stacks. For AAM, it initially called the new public API directly from internal tooling. But the team wanted assignments between IAM Identity Center groups and IAM roles to be managed in the same Pulumi stacks as the roles themselves. That way, the full lifecycle, including clean teardown when a team or account is retired, is handled by the same program that created them.

With native `accountaccess` resources in the Pulumi AWS provider, the team can manage roles and entitlements together, in the JVM language its platform tooling already uses, through its existing review and deployment workflow.

## Conclusion

AAM gives AWS customers a way to keep the flexibility of their own IAM roles while centralizing workforce access through IAM Identity Center. It also moves more of the access model into resources that customers create and own. Managing those roles and entitlements with Pulumi means access changes are versioned, reviewed, and deployed together, in the language your team already uses.

To get started:

- Read [Account access manager](https://docs.aws.amazon.com/IAM/latest/UserGuide/account-access-manager.html) in the AWS IAM User Guide.
- Explore the [aws.accountaccess.Application](/registry/packages/aws/api-docs/accountaccess/application/) and [aws.accountaccess.Entitlement](/registry/packages/aws/api-docs/accountaccess/entitlement/) resources in the Pulumi Registry.
- Try Pulumi for free at [pulumi.com](/), and file feedback or feature requests in the [pulumi-aws GitHub repository](https://github.com/pulumi/pulumi-aws).
