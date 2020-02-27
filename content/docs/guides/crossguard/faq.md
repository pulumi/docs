---
title: CrossGuard Frequently Asked Questions
meta_desc: This page contains Frequently Asked Questions about Pulumi CrossGuard and Policy Packs.
linktitle: Frequently Asked Questions
weight: 4

menu:
  userguides:
    parent: crossguard
---
{{% crossguard-preview %}}

## Is CrossGuard open source?

The [Pulumi Policy SDK](https://github.com/pulumi/pulumi-policy) that allows you to express policies and using the local `--policy-pack` flag (as part of the Pulumi CLI) to enforce Policy Packs is also open source.

Enforcing Policy Packs across an organization and viewing Policy Pack results in the Pulumi Console are part of Pulumi CrossGuard and are only available to preview for Team Pro and Enterprise organizations.

## How do Policy Packs enforced by the service interact with Policy Packs specified by the local Policy Pack flag?

Policy Packs enforced by the Pulumi Console are always run by the Pulumi CLI.

Therefore, if a Policy Pack is specified locally using `--policy-pack`, the Pulumi CLI will run the local Policy Pack as well as the Policy Packs enforced by the Pulumi Console. A violation by any of the Policy Packs would halt an update.

## What happens if a stack belongs to multiple Policy Groups?

If a stack belongs to multiple Policy Groups, the Pulumi Service will aggregate all required Policy Packs from those Policy Groups. Only one of version of each Policy Pack will be run per update.

This means that if a stack belongs to multiple Policy Groups that specify different versions of a Policy Pack, only the newest version of that pack will be run. For example, if a stack `my-stack` belongs to Policy Group `production-stacks` that requires Policy Pack `aws-policies` version 2 and Policy Group `platform-stacks` that requires Policy Pack `aws-policies` version 4, only version 4 of `aws-policies` would be run.

Under a stack's "Settings" tab you can take a look at the Policy Packs that would be enforced on a `preview` or `update` as well as the Policy Groups that the stack belongs to.

![Stack Policy Settings](/images/docs/guides/crossguard/stack-policies.jpg)

## How does Policy as Code work during a stack import or refresh?

During `pulumi stack import`, Policy Packs are not run. This command does not modify any resources and simply allows you to make manual changes to the state file. During the next update, the resources and state file would be updated based on the stack's Pulumi program, which must be in compliance to succeed.

During `pulumi refresh`, no resources are modified. This command simply updates the state file with the current state of the resources. If there are out-of-compliance resources that get consumed into the state file during the `pulumi refresh` command, they will be updated during the next update to reflect the declared infrastructure from the stack's Pulumi program. The Pulumi program must be in compliance with the required Policy Packs for the update to be successful.

## What happens if I add a Policy Pack that causes an existing resource to become out-of-compliance?

The next preview or update of the stack with fail due to the policy violation. The stack will need to be fixed before it can be updated.

A stack with out-of-compliance resources can be destroyed.
