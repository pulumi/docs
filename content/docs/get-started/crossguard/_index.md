---
title: Get Started with Policy as Code
meta_desc: Pulumi CrossGuard is a product that provides gated deployments via Policy as Code. Enforce best practices
           and security compliance when creating cloud resources.
linktitle: Policy as Code ("CrossGuard")
menu:
  getstarted:
    identifier: pac
    weight: 3
aliases: ["/docs/get-started/policy-as-code/"]
---

Pulumi CrossGuard is a product that provides gated deployments via Policy as Code.

Often organizations want to empower developers to manage their infrastructure yet are concerned about giving them full access. CrossGuard allows administrators to provide autonomy to their developers while ensuring compliance to defined organization policies.

Using Policy as Code, users can express business or security rules as functions that are executed against resources in their stacks. Then using CrossGuard, organization administrators can apply these rules to particular stacks within their organization. When policies are executed as part of your Pulumi deployments, any violation will gate or block that update from proceeding.

Policies can be written in TypeScript/JavaScript (Node.js) or Python and can be applied to stacks written in any language.

{{% notes %}}
Python support is currently in preview.
{{% /notes %}}

## Terminology

* **Policy Pack** - a set of related policies - i.e. “Security”, “Cost Optimization”, “Data Location”. The categorization of policies into a policy pack is left up to the user.
* **Policy** - an individual policy - i.e. “prohibit use of instances larger than t3.medium”.
* **Enforcement Level** - the impact of a policy violation - i.e. “mandatory” or “advisory”.

Learn more about [Policy as Code core concepts]({{< prelref "/docs/guides/crossguard/core-concepts" >}}).

## Creating a Policy Pack

Let's start with authoring your first Policy Pack.

{{< get-started-stepper >}}
