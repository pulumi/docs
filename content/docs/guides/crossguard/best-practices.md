---
title: Best Practices for Writing Policy Packs
linktitle: Best Practices

menu:
  userguides:
    parent: crossguard
    weight: 3
---
{{% crossguard-preview %}}

## Naming Policies

Each policy within a Policy Pack must have a unique name. The name must be between 1 and 100 characters and may contain letters, numbers, dashes (-), underscores (_) or periods(.).

## Policy Assertions

Policy assertions should be complete sentences, specify the resource that has violated the policy, and be written using an imperative tone. The table below provides some examples of policy assertions.

| ✅                                                    | ❌                           |
| -----------                                           | -----------                  |
| "The RDS cluster must specify a node type."           | "Specify a node type."       |
| "The RDS cluster must have audit logging enabled."    | "Enable audit logging."      |

This format provides a clear message to end users, allowing them to understand what and why a policy is failing.
