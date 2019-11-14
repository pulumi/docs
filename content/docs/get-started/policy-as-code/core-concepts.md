---
title: Core Concepts (Preview)
linktitle: Core Concepts
weight: 4
menu:
  getstarted:
    parent: pac
    identifier: pac-core-concepts
---
{{% pac-preview %}}

## Policy

A Policy contains specific logic you would like to enforce. For example, you may want to restrict the creation of public S3 buckets or you may disallow resource provisioning without tags. You can refer to other examples [here](https://github.com/pulumi/examples/tree/master/policy-packs).

Policies are written as validation functions that are evaluated against all resources in your Pulumi stack. If the validation function calls `reportViolation`, the associated resource will be considered in violation of the policy. `reportViolation` can be called multiple times to report multiple violations.

Policies validation functions are executed during `pulumi preview` and `pulumi update`, asserting that cloud resource definitions comply with the policy immediately before they are created or updated.

During `preview`, every resource is checked for policy violations, which are batched up into a final report. During the `update`, the first policy violation will halt the deployment.

When authoring a policy, you must specify an Enforcement Level: `advisory` or `mandatory`. An enforcement level of `advisory` simply prints a warning message to users. A `mandatory` enforcement level means that an update will halt before creating a resource that violates that policy.

## Policy Pack

A Policy Pack can contain one or more policies to enforce. Packs provide a way to group together similar policies. For example, you may decide to have one pack with AWS policies and another with Kubernetes-specific policies. That being said, there are no restrictions on which policies you combine within a pack, and you should pack them however makes sense for your organization. Currently, there is a limitation of 25 policies per pack.

Organization admins can author and publish Policy Packs to the Pulumi service.

## Policy Group

A Policy Group is a group of stacks with the same set of Policy Packs enforced. A stack may belong to multiple Policy Groups. An example use of Policy Groups is to have a different group per environment. For example, you can have one for your stacks in production and a more permissive Policy Group for your other environments such as `staging` and `dev`.

Organization admins can create new Policy Groups, add stacks to a Policy Group, or remove stacks from a group.

Each Policy Group has its own set of enforced Policy Packs. An organization administrator can add, remove, or update the version of the Policy Pack enforced on the Policy Group.

In cases where a stack belongs to multiple Policy Groups and is therefore required to run multiple versions of the same Policy Pack, only the latest version of the Policy Pack gets enforced. For example, if `my-stack` belongs to two Policy Groups and you want to enforce `my-aws-policy-pack` versions 2 and 3, only version 3 will be enforced. You may view the Policy Groups a stack belongs to as well as the currently enforced Policy Packs for the stack by navigating to a stack’s `Settings` tab and then `Policies`.

### Default Policy Group

Every organization has a default Policy Group. When the default Policy Group is created, all stacks in your organization are automatically added to that Policy Group. Additionally, all stacks that are created after adding the default Policy Group are automatically added to it. Organization admins can remove stacks from the default Policy Group as desired.
