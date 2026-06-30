---
title: "Pulumi IAM Expands: Manage Access at Scale with Tags, Roles, and Teams"
allow_long_title: true
date: 2026-03-19T10:30:00-07:00
draft: false
meta_desc: "Pulumi IAM introduces tag-based access control and role assignments for teams and users, enabling least-privilege access management at scale."
meta_image: meta.png
feature_image: feature.png
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
category: product
---

Since the launch of [Pulumi IAM](/blog/pulumi-cloud-iam-launch/) with [custom roles](/docs/administration/access-identity/rbac/roles/) and scoped [access tokens](/docs/administration/access-identity/access-tokens/), organizations have been using fine-grained permissions to secure their automation and CI/CD pipelines. As teams scale to hundreds or thousands of stacks, environments, and accounts, the next challenge is applying those permissions efficiently.

Today, we're introducing three new capabilities to help you manage permissions more dynamically at scale: **tag-based access control**, **team role assignments**, and **user role assignments**.

<!--more-->

## Why tag-based access control?

With custom roles, you can define granular permissions using [fine-grained scopes](/docs/administration/access-identity/rbac/scopes). However, applying those roles still requires selecting individual stacks, environments, or accounts one by one. For organizations managing a large number of Pulumi entities, this means either granting overly broad access or spending significant time on manual configuration. Tag-based access control solves this problem.

## What's new?

### Tag-based access control

You can now create rules within a custom role that dynamically grant permissions based on entity tags. This works across IaC stacks, ESC environments, and Insights accounts. For example, when a new stack is created and tagged `env:prod`, anyone with a role containing a matching tag-based rule automatically gets the right permissions. No manual assignment required.

A single role can include multiple tag-based rules, and they are evaluated with **OR** logic. If an entity matches any of the rules, the permissions are granted. Within a single rule, you can combine multiple key-value conditions with implicit **AND** logic for precise targeting. For example, a rule with conditions `env:prod` and `team:payments` ensures access is granted only to production resources owned by the payments team.

### Team role assignments

Custom roles can now be assigned directly to [teams](/docs/administration/access-identity/rbac/teams) within your Pulumi organization. When an engineer joins a team, whether manually or via [SCIM provisioning](/docs/pulumi-cloud/access-management/scim/), they automatically inherit the permissions defined in the team's assigned roles.

Teams support both **inline permissions** (ad-hoc access to specific stacks, environments, or accounts) and **role-based permissions** simultaneously. You can assign **multiple roles** to a single team, giving you full flexibility to compose access from reusable building blocks while retaining the ability to grant one-off access where needed. If you have existing workflows built around ad-hoc assignments to teams, those continue to work exactly as before. You can adopt roles incrementally or mix both approaches on the same team.

{{% notes type="info" %}}
Team admins (or users with the `team:update` scope) can continue to manage their team's inline permissions as they do today. However, assigning organization-level custom roles to a team requires additional permissions: `role:read` and `role:update`.
{{% /notes %}}

### User role assignments

Custom roles can also be assigned directly to individual organization members. This is useful for users whose responsibilities span multiple teams or require permissions beyond the existing org-level `Admin`, `Member`, and `Billing Manager` [roles](/docs/administration/access-identity/rbac/roles).

### How permissions work together

Permissions in Pulumi IAM are **additive**. A user receives the union of all permissions granted to them, including permissions from roles assigned directly to them as a user and permissions from roles assigned to any team they belong to. A user on both the "SRE" and "Security" teams inherits permissions from both team roles, plus any role assigned to them individually.

## How to get started

Configuring tag-based access control and role assignments is done through the Pulumi Cloud console and REST API.

### 1. Create a custom role with tag-based rules

In Pulumi Cloud, navigate to **Settings** > **Access Management** > **Roles** and create a new custom role. In the role configuration, add tag-based rules that define which entities the role should apply to.

For example, to create a role that grants write access to all production stacks:

1. Click **Create custom role** and give it a descriptive name (e.g., "Production Deployer")
1. Add a permission set (e.g., Stack Write) to the role
1. Under entity selection, choose **Tag-based rule**
1. Set the condition: tag key `env` equals `prod`
1. Save the role

### 2. Assign the role to a team

Go to **Settings** > **Access Management** > **Teams**, select a team, and assign your custom role. All team members immediately inherit the defined permissions.

### 3. Assign a role to an individual user

For users with unique access requirements, go to **Settings** > **Access Management** > **Members**, select a user, and assign a custom role directly.

{{< video title="Custom roles with tag-based access control" src="abac-demo.mp4" controls="true" autoplay="true" loop="true" >}}

## Enforce tagging standards with Pulumi Policy

Tag-based access control relies on consistent tagging. If a stack is missing a tag or has an incorrect value, permissions won't be applied as expected. [Pulumi Policy](/docs/insights/policy/) closes this gap by letting you enforce tagging standards as a [preventative policy group](/docs/insights/policy/policy-groups/), so any `pulumi up` on a stack with missing or invalid tags is blocked before deployment. This ensures your tag-based RBAC rules always grant the correct permissions. Policy enforces the standard, RBAC enforces the access.

To learn how to write policies that validate stack tags, see [Using stack tags in policies](/docs/insights/policy/policy-packs/authoring/#using-stack-tags-in-policies).

{{% notes type="info" %}}
Pulumi Policy currently supports tag enforcement for IaC stacks. For ESC environments and Insights accounts, tags are managed through the Pulumi Cloud console or REST API.
{{% /notes %}}

## Availability

Tag-based access control, team role assignments, and user role assignments are available today for customers on the **Pulumi Enterprise** and **Pulumi Business Critical** plans. Check out our [pricing page](/pricing/) for more details on editions and what's included.

## Conclusion

With custom roles providing fine-grained permissions, tag-based rules enabling dynamic access policies, and the ability to assign roles directly to teams and users, Pulumi IAM now provides everything you need to implement automated, least-privilege access control at scale. We're excited to see how you leverage these new capabilities to secure and streamline your cloud operations.

Explore the [IAM documentation](/docs/administration/access-identity/rbac) to get started, and share your feedback in our [GitHub repository](https://github.com/pulumi/pulumi-cloud-requests/issues).

## Learn more

- [RBAC overview](/docs/administration/access-identity/rbac)
- [Roles](/docs/administration/access-identity/rbac/roles)
- [Permission sets](/docs/administration/access-identity/rbac/permission-sets)
- [Teams](/docs/administration/access-identity/rbac/teams)
- [Scopes](/docs/administration/access-identity/rbac/scopes)
- [Pulumi IAM launch blog](/blog/pulumi-cloud-iam-launch/)
- [Pulumi IAM for self-hosted](/blog/pulumi-cloud-iam-self-hosted/)
