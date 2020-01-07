---
title: "Stacks"
meta_desc: An in depth look at Pulumi Stacks and their usage.
menu:
  intro:
    parent: concepts
    weight: 3

aliases: ["/docs/reference/stack/"]
---

Every Pulumi program is deployed to a **stack**.  A stack is an isolated, independently configurable
instance of a Pulumi program. Stacks are commonly used to denote different phases of development (such as **development**, **staging** and **production**) or feature branches (such as **feature-x-dev**, **jane-feature-x-dev**).

## Create a stack {#create-stack}

To create a new stack, use `pulumi stack init stackName`. This creates an empty stack `stackName` and sets it as the *active* stack.  The project that the stack is associated with is determined by finding the nearest `Pulumi.yaml` file.

The stack name must be unique within a project.

```bash
$ pulumi stack init staging
```

If you are using Pulumi in your organization, by default the stack will be created in your user account. To target the organization, name the stack using `orgName/stackName`:

```bash
$ pulumi stack init broomllc/staging
```

## Listing stacks

To see the list of stacks associated with the current project (the nearest `Pulumi.yaml` file), use `pulumi stack ls`.

```bash
$ pulumi stack ls
NAME                                      LAST UPDATE              RESOURCE COUNT
jane-dev                                  4 hours ago              97
staging*                                  n/a                      n/a
test                                      2 weeks ago              121
```

## Select a stack

The top-level `pulumi` operations `config`, `preview`, `update` and `destroy` operate on the *active* stack. To change the active stack, run `pulumi stack select`.

```bash
$ pulumi stack select jane-dev

$ pulumi stack ls
NAME                                      LAST UPDATE              RESOURCE COUNT
jane-dev*                                 4 hours ago              97
staging                                   n/a                      n/a
test                                      2 weeks ago              121
```

## Deploy a project

To deploy your project to the currently selected stack, run `pulumi up`. The operation uses the latest [configuration values]({{< relref "config" >}}) for the active stack.

> **Note:** Your stack can distinguish between execution for preview versus for update by using [pulumi.runtime.isDryRun()]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi/runtime#isDryRun" >}}).

## View stack resources

To view details of the currently selected stack, run `pulumi stack` with no arguments.  This displays the metadata, resources and output properties associated with the stack.

```bash
$ pulumi stack
Current stack is jane-dev:
    Last updated 1 week ago (2018-03-02 10:26:09.850357 -0800 PST)
    Pulumi version v0.11.0
    Plugin nodejs [language] version 0.11.0
    Plugin aws [resource] version 0.11.0

Current stack resources (3):
    TYPE                                             NAME
    pulumi:pulumi:Stack                              webserver-jane-dev
    aws:ec2/securityGroup:SecurityGroup              web-secgrp
    aws:ec2/instance:Instance                        web-server-www

Current stack outputs (2):
    OUTPUT                                           VALUE
    publicDns                                        ec2-18-218-85-197.us-east-2.compute.amazonaws.com
    publicIp                                         18.218.85.197

Use `pulumi stack select` to change stack; `pulumi stack ls` lists known ones
```

## View stack outputs {#outputs}

When you use top-level exports in your Pulumi [program]({{< relref "programming-model#programs" >}}), they become [stack outputs]({{< relref "programming-model#stack-outputs" >}}). Stack outputs can be viewed via `pulumi stack output` and are shown on the stack information page on pulumi.com.

### **JavaScript code**

```javascript
exports.publicDns = ...
exports.publicIp  = ...
```

### **CLI**

```bash
$ pulumi stack output
Current stack outputs (2):
    OUTPUT                                           VALUE
    publicDns                                        ec2-18-218-85-197.us-east-2.compute.amazonaws.com
    publicIp                                         18.218.85.197
```

The values of specific properties can also be retrieved directly, which is useful when writing scripts that use these output values.

```bash
$ pulumi stack output publicIp
18.218.85.197
```

See also [Inter-Stack Dependencies]({{< relref "organizing-stacks-projects#inter-stack-dependencies" >}}), which allow one stack to reference the outputs of another stack.

## Import and export a stack deployment

A stack can be exported to see the raw data associated with the stack.  This is useful when manual changes need to be applied to the stack due to changes made in the target cloud platform that Pulumi is not aware of.  The modified stack can then be imported to set the current state of the stack to the new values.

> **Note:** This is a powerful capability that subverts the usual way that Pulumi manages resources and ensures immutable and repeatable infrastructure deployments.  Importing an incorrect stack specification could lead to orphaning of cloud resources or the inability to make future updates to the stack.  Use care when using the import and export capabilities.

```bash
$ pulumi stack export > stack.json

$ pulumi stack import < stack.json
```

## Delete a stack

To delete a stack with no resources, run `pulumi stack rm`. Removing the stack will remove all stack history from pulumi.com and will delete the stack configuration file `Pulumi.<stack-name>.yaml`.

If a stack still has resources associated with it, they must first be deleted via `pulumi destroy`. This command uses the latest configuration values, rather than the ones that were last used when the program was deployed.

To force the deletion of a stack that still contains resources --- potentially orphaning them --- use `pulumi stack rm --force`.

## Stack tags

Stacks have associated metadata in the form of tags, with each tag consisting of a name and value. A set of built-in tags are automatically assigned and updated each time a stack is updated (such as `pulumi:project`, `pulumi:runtime`, `pulumi:description`, `gitHub:owner`, `gitHub:repo`, `vcs:owner`, `vcs:repo`, and `vcs:kind`). To view a stack's tags, run [`pulumi stack tag ls`]({{< relref "/docs/reference/cli/pulumi_stack_tag_ls" >}}).

> **Note:** Stack tags are only supported when logged into the [Pulumi Service backend]({{< relref "state" >}}).

Custom tags can be assigned to a stack by running [`pulumi stack tag set <name> <value>`]({{< relref "/docs/reference/cli/pulumi_stack_tag_set" >}}) and can be used to customize the grouping of stacks in the [Pulumi Console](https://app.pulumi.com). For example, if you have many projects with separate stacks for production, staging, and testing environments, it may be useful to group stacks by environment instead of by project. To do this, you could assign a custom tag named `environment` to each stack. For example, running `pulumi stack tag set environment production` assigns a custom `environment` tag with a value of `production` to the active stack. Once you've assigned an `environment` tag to each stack, you'll be able to group by `Tag: environment` in the Pulumi Console.

> **Note:** As a best practice, custom tags should not be prefixed with `pulumi:`, `gitHub:`, or `vcs:` to avoid conflicting with built-in tags that are assigned and updated with fresh values each time a stack is updated.

Tags can be deleted by running [`pulumi stack tag rm <name>`]({{< relref "/docs/reference/cli/pulumi_stack_tag_rm" >}}).
