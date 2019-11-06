---
title: Get Started with Policy as Code (Preview)
linktitle: Policy as Code
menu:
  getstarted:
    identifier: Policy as Code
    weight: 3

aliases: ["/docs/quickstart/policy-as-code/"]
---
{{% pac-preview %}}

Pulumi has an exciting new feature which provides Gated Deployments via Policy as Code.

Often organizations want to empower developers to manage their infrastructure yet are concerned about giving them full access. Policy as Code (PaC) allows administrators to provide autonomy to their developers while ensuring compliance to defined organization policies.

With this new feature, users can express business or security rules as functions that are executed against resources in their stacks. When policies are executed as part of your Pulumi deployments, any violation will gate or block that update from proceeding.

Organization administrators can write and publish Policy Packs for their organization. These Policy Packs can be enforced against different Policy Groups or groups of stacks.

## Terminology

* **Policy Pack** - a set of related policies - i.e. “Security”, “Cost Optimization”, “Data Location”. The categorization of policies into a policy pack is left up to the user.
* **Policy** - an individual policy - i.e. “prohibit use of instances larger than t3.medium”.
* **Enforcement Level** - the impact of a policy violation - i.e. “mandatory” or “advisory”.

You can learn more about the core concepts of Policy as Code [here]({{< relref "core-concepts" >}}).

## Creating a Policy Pack

Let's start with authoring your first Policy Pack.

{{< get-started-stepper >}}
