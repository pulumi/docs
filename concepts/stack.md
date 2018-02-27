---
title: "Stacks, previews, and updates"
---

Every Colada program is deployed to a **stack**.  A stack is an isolated, independently configurable
target in which programs will run. Stacks are commonly used to denote different phases of development (such as **development**, **staging** and **production**) or feature branches (such as **feature-x-dev**, **jane-feature-x-dev**).

A stack may define stack-specific configuration. To learn more, see [Defining stack settings](./config.html#config-stack).

A stack is created via `pulumi stack init`. A Colada program is then deployed to the stack via `pulumi preview` and `pulumi update`, which are described in the following sections.

## Create a stack

To create a new stack, use `pulumi stack init stackName`. This creates an empty stack `stackName` and sets it as the *active* stack. 

**Example**

TODO: add command, output, and flags, once finalized.

## Select a stack

The top-level `pulumi` operations `config`, `preview`, `update` and `destroy` operate on the *active* stack. To change the active stack, run `pulumi stack select`.

**Example**

TODO: add command and output

## View stack resources

To view resources currently deployed to a stack, run `pulumi stack` with no arguments.

Options:

-  `-i, --show-ids`. Display each resource's provider-assigned unique ID. For instance, with AWS, this displays [Amazon Resource Names](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html). 
-  `-u, --show-urns`. Display each resource's Colada-assigned globally unique URN
   
**Example**

TODO: add command and output

## List stacks

To list all known stacks, run `pulumi stack ls`. When using local stacks, this shows TBD.

## View stack outputs

When you use [output properties](./programming-model.html#output-properties) in your Colada program, they become stack outputs. Stack outputs can be viewed via `stack output`.

**Example**

```
$ pulumi stack output
Current stack outputs (1):
    OUTPUT                                           VALUE
    endpointUrl                                      https://m4i09o77b4.execute-api.us-west-2.amazonaws.com/stage/
```

## Import and export a stack deployment

TODO

## Delete a stack

To delete a stack with no resources, run `pulumi stack rm`. Removing the stack will remove the tracking information for the stack and will also delete stack settings in `Pulumi.yaml`.

TODO: document `--force` and document whether other locations of stack settings are affected when doing `stack rm`.

## Create, update and delete stack resources

### Preview updates to a stack

Before updating your running stack, it is recommended that you first view a preview of your the changes via `pulumi preview`. A stack must first be selected via `pulumi stack init` or `pulumi stack select`.

Since the Colada CLI runs your program in order to determine which infrastructure changes to apply, `pulumi preview` always provides a pessimistic set of resource changes. Once the program is actually deployed through `pulumi update`, the actual changes may be much smaller.

For more information, see [the Colada programming model](./programming-model.html).

### Update and deploy a Colada program

To deploy a Colada program to a stack for the first time, or to apply program changes to a running stack, use the `pulumi update` command. A stack must first be selected via `pulumi stack init` or `pulumi stack select`.

TODO: add command, output, and flags

### Delete all stack resources

To delete all resources in the selected stack, use the `pulumi destroy` command. 

## Local and managed stacks

There are two kinds of stacks, *local* and *managed*. With local stacks, the [checkpoint file](./checkpoint.html) is stored on your local machine. With managed stacks, the checkpoint is managed by Pulumi Enterprise.

TODO document how you create a local vs managed stack.
