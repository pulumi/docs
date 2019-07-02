---
title: Stacks
expanded_url: /docs/tour/programs/
menu:
  tour:
    parent: programs
    weight: 1
---

A stack is an instance of your Pulumi program.

You'll create and manipulate them frequently, and they are one of Pulumi's most fundamental concepts.  We glossed over
them in the first lesson by simply using `pulumi new` to create our first stack, but we'll now learn more about them.

There are many reasons we might want more than one stack for our program:

* Individual developer or test stacks
* Shared environments like `prod`, `staging`, and `dev`
* Replicated instances within an environment like `prod-na-east`, `prod-na-west`, and `prod-asia`
* Single tenanted instances of a SaaS product like `acmecorp`, `contoso`, and `northwind`

Each stack is entirely isolated from all other stacks, enabling concurrent deployments and fine-grained access controls.

The [`pulumi stack`]({{< relref "/docs/reference/cli/pulumi_stack.md" >}}) command manages everything about stacks.

The `stack ls` command shows us the current project's stacks and some basic information about each one:

```bash
$ pulumi stack ls
NAME                   RESOURCE COUNT     URL
broomllc/prod          73                 https://app.pulumi.com/broomllc/prod
broomllc/staging*      88                 https://app.pulumi.com/broomllc/staging
```

The `*` next to `staging` indicates that's the stack we're on.  Most CLI commands are contextual depending on the
current project working directory and stack for it that has been selected.  Also note that some stacks have fully
qualified names if they are within an organization, like these ones that belong to the `broomllc` team.

To create a stack, use `stack init`:

```bash
$ pulumi stack init cbroom-dev
```

To select a different existing stack, so updates will target it, we can use `stack select`:

```bash
$ pulumi stack select prod
```

After we are done with a stack, we can remove it using `stack rm`:

```bash
$ pulumi stack rm cbroom-dev
```

This will prompt us interactively but we can pass `--yes` to skip the prompts.  If there are still resources inside of
the stack, Pulumi will refuse to remove it until we've run a `destroy`, although `--force` will override this.

***

Now that we've seen how to manage our stacks, let's see how to use packages in our program.

<div class="tour-nav">
    <a class="tour-button enabled" href="{{< relref "programs.md" >}}" title="Beyond the Basics">◀</a>
    <span class="tour-index"><strong>2</strong>/8</span>
    <a class="tour-button enabled" href="{{< relref "programs-packages.md" >}}" title="Packages">▶</a>
</div>
