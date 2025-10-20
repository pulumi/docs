---
title_tag: "Tips for Writing Policy Packs | Pulumi Policy"
meta_desc: This page contains best practices for writing policy packs in Pulumi.
title: Best practices
h1: Policy Pack Best Practices
weight: 5
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    insights:
        name: Best Practices
        parent: insights-policy
        weight: 5
aliases:
  - /docs/insights/policy/policy-as-code/best-practices/
  - /docs/iac/crossguard/best-practices/
  - /docs/guides/crossguard/best-practices/
  - /docs/using-pulumi/crossguard/best-practices/
  - /docs/iac/packages-and-automation/crossguard/best-practices/
  - /docs/iac/using-pulumi/crossguard/best-practices/
---

## Naming policies

Each policy within a Policy Pack must have a unique name. The name must be between 1 and 100 characters and may contain letters, numbers, dashes (-), underscores (_) or periods(.).

## Policy assertions

Policy assertions should be complete sentences, specify the resource that has violated the policy, and be written using an imperative tone. The table below provides some examples of policy assertions.

| ✅                                                    | ❌                           |
| -----------                                           | -----------                  |
| "The RDS cluster must specify a node type."           | "Specify a node type."       |
| "The RDS cluster must have audit logging enabled."    | "Enable audit logging."      |

This format provides a clear message to end users, allowing them to understand what and why a policy is failing.
