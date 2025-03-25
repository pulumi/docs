---
title_tag: "Tips for Writing Policy Packs | CrossGuard"
meta_desc: This page contains best practices for writing policy packs in Pulumi.
title: Best practices
h1: Policy pack best practices
weight: 5
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    name: Best practices
    parent: iac-using-pulumi-policy
    weight: 5
aliases:
  - /docs/guides/crossguard/best-practices/
  - /docs/using-pulumi/crossguard/best-practices/
  - /docs/iac/packages-and-automation/crossguard/best-practices/
search:
  keywords:
    - contains
    - rds
    - practices
    - best
    - policy
    - writing
    - packs
---

## Naming Policies

Each policy within a Policy Pack must have a unique name. The name must be between 1 and 100 characters and may contain letters, numbers, dashes (-), underscores (_) or periods(.).

## Policy Assertions

Policy assertions should be complete sentences, specify the resource that has violated the policy, and be written using an imperative tone. The table below provides some examples of policy assertions.

| ✅                                                    | ❌                           |
| -----------                                           | -----------                  |
| "The RDS cluster must specify a node type."           | "Specify a node type."       |
| "The RDS cluster must have audit logging enabled."    | "Enable audit logging."      |

This format provides a clear message to end users, allowing them to understand what and why a policy is failing.
