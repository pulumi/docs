---
title: "Pulumi IAM Expands: Manage Access at Scale with Tags, Roles, and Teams"
allow_long_title: true
date: 2026-02-25T00:00:00-08:00
draft: false
meta_desc: "Pulumi IAM introduces tag-based access control and role assignments for teams and users, enabling least-privilege access management at scale."
meta_image: "meta.png"
authors:
  - devon-grove
  - davide-massarenti
  - casey-huang
  - arun-loganathan
tags:
  - iam
  - rbac
  - security
  - features
  - pulumi-cloud
---

Since the launch of [Pulumi IAM](/blog/pulumi-cloud-iam-launch/) with [Custom Roles](/docs/administration/access-identity/rbac/roles) and scoped Access Tokens, organizations have been using fine-grained permissions to secure their automation and CI/CD pipelines. As teams scale to hundreds or thousands of stacks, environments, and accounts, the next challenge is applying those permissions efficiently. Today, we're excited to announce three powerful new capabilities in Pulumi IAM: **Tag-Based Access Control**, **Team Role Assignments**, and **User Role Assignments**. Together, these features enable you to automate and manage permissions at scale, ensuring security keeps pace with the speed of your cloud development.

<!--more-->

## Why tag-based access control?

With Custom Roles, you can define granular permissions using [fine-grained scopes](/docs/administration/access-identity/rbac/scopes). However, applying those roles still required selecting individual stacks, environments, or accounts one by one. For organizations managing a large number of Pulumi entities, this means either granting overly broad access or spending significant time on manual configuration.

Tag-based access control solves this. You can now define rules within a Custom Role that grant permissions based on tags applied to your Pulumi entities. Instead of selecting individual resources, you define a rule like "grant access to all entities where tag `environment` equals `prod`." Permissions are then automatically managed as entities are created and tagged.

## What's New?

### Tag-based access control

You can now create rules within a Custom Role that dynamically grant permissions based on entity tags. This works across IaC stacks, ESC environments, and Insights accounts. For example, when a new stack is created and tagged `env:prod`, anyone with a role containing a matching tag-based rule automatically gets the right permissions. No manual assignment required.

A single role can include multiple tag-based rules, and they are evaluated with **OR** logic. If an entity matches any of the rules, the permissions are granted. Within a single rule, you can combine multiple key-value conditions with implicit **AND** logic for precise targeting. For example, a rule with conditions `env:prod` and `team:payments` ensures access is granted only to production resources owned by the payments team.

### Team role assignments

Custom Roles can now be assigned directly to [teams](/docs/administration/access-identity/rbac/teams) within your Pulumi organization. When an engineer joins a team, whether manually or via [SCIM provisioning](/docs/pulumi-cloud/access-management/scim/), they automatically inherit the permissions defined in the team's assigned roles.

Teams support both **inline permissions** (ad-hoc access to specific stacks, environments, or accounts) and **role-based permissions** simultaneously. You can assign **multiple roles** to a single team, giving you full flexibility to compose access from reusable building blocks while retaining the ability to grant one-off access where needed. If you have existing workflows built around ad-hoc assignments to teams, those continue to work exactly as before. You can adopt roles incrementally or mix both approaches on the same team.

### User role assignments

Custom Roles can also be assigned directly to individual organization members. This provides a way to grant specific permissions to users whose responsibilities span multiple teams or require a unique set of entitlements, going beyond the existing org-level `admin`, `member`, and `billing manager` [roles](/docs/administration/access-identity/rbac/roles).

### How permissions work together

Permissions in Pulumi IAM are **additive**. A user receives the union of all permissions granted to them, including permissions from roles assigned directly to them as a user and permissions from roles assigned to any team they belong to. A user on both the "SRE" and "Security" teams inherits permissions from both team roles, plus any role assigned to them individually.

## How to Get Started

Configuring tag-based access control and role assignments is done through the Pulumi Cloud console and REST API.

### 1. Create a custom role with tag-based rules

Navigate to **Settings** > **Access Management** > **Roles** and create a new Custom Role. In the role configuration, add tag-based rules that define which entities the role should apply to.

For example, to create a role that grants Stack Write access to all production stacks:

1. Click **Create custom role** and give it a descriptive name (e.g., "Production Deployer")
1. Add a permission set (e.g., Stack Write) to the role
1. Under entity selection, choose **Tag-based rule**
1. Set the condition: tag key `env` equals `prod`
1. Save the role

### 2. Assign the role to a team

Go to **Settings** > **Access Management** > **Teams**, select a team, and assign your Custom Role. All team members immediately inherit the defined permissions.

### 3. Assign a role to an individual user

For users with unique access requirements, go to **Settings** > **Access Management** > **Members**, select a user, and assign a Custom Role directly.

**<span style="color:red">Placeholder: add a video on Custom Roles</span>**

## Automate Governance with Pulumi Policy

Tag-based access control works well on its own, but it becomes even more powerful when combined with [Pulumi Policy](/docs/insights/policy/). You can write a policy that enforces tagging standards on all resources and then set it up as a [preventative policy group](/docs/insights/policy/policy-groups/) so that any `pulumi up` without the required tags is blocked before deployment.

Here's a simple example of a policy that requires all AWS resources to have an `env` and `team` tag:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
new PolicyPack("required-tags", {
    policies: [
        {
            name: "require-env-and-team-tags",
            description: "All AWS resources must have 'env' and 'team' tags.",
            enforcementLevel: "mandatory",
            validateResource: (args, reportViolation) => {
                if (args.type.startsWith("aws:")) {
                    const tags = args.props.tags;
                    if (!tags || !tags["env"] || !tags["team"]) {
                        reportViolation("Resource must include 'env' and 'team' tags.");
                    }
                }
            },
        },
    ],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
def require_tags(args, report_violation):
    if args.resource_type.startswith("aws:"):
        tags = args.props.get("tags", {})
        if not tags or "env" not in tags or "team" not in tags:
            report_violation(
                "Resource must include 'env' and 'team' tags."
            )

PolicyPack(
    "required-tags",
    policies=[
        ResourceValidationPolicy(
            name="require-env-and-team-tags",
            description="All AWS resources must have 'env' and 'team' tags.",
            enforcement_level=EnforcementLevel.MANDATORY,
            validate=require_tags,
        ),
    ],
)
```

{{% /choosable %}}

Add this policy pack to a [preventative policy group](/docs/insights/policy/policy-groups/) and once tagging is guaranteed by policy, your tag-based RBAC rules reliably grant the correct permissions. Policy enforces the standard, RBAC enforces the access.

{{% notes type="info" %}}
Pulumi Policy currently supports tag enforcement for IaC stacks. For ESC environments and Insights accounts, tags are managed through the Pulumi Cloud console or REST API.
{{% /notes %}}

## Availability

Tag-Based Access Control, Team Role Assignments, and User Role Assignments are available today for customers on the **Pulumi Enterprise** and **Pulumi Business Critical** plans. Check out our [pricing page](/pricing/) for more details on editions and what's included.

## Conclusion

With Custom Roles providing fine-grained permissions, tag-based rules enabling dynamic access policies, and the ability to assign roles directly to teams and users, Pulumi IAM now provides everything you need to implement automated, least-privilege access control at scale. We're excited to see how you leverage these new capabilities to secure and streamline your cloud operations.

Explore the [IAM documentation](/docs/administration/access-identity/rbac) to get started. We welcome your feedback in our [GitHub repository](https://github.com/pulumi/pulumi-cloud-requests/issues).

## Learn More

- [RBAC overview](/docs/administration/access-identity/rbac)
- [Roles](/docs/administration/access-identity/rbac/roles)
- [Permission sets](/docs/administration/access-identity/rbac/permission-sets)
- [Teams](/docs/administration/access-identity/rbac/teams)
- [Scopes](/docs/administration/access-identity/rbac/scopes)
- [Pulumi IAM launch blog](/blog/pulumi-cloud-iam-launch/)
- [Pulumi IAM for self-hosted](/blog/pulumi-cloud-iam-self-hosted/)
