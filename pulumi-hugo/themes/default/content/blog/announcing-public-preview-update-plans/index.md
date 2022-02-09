---
title: "Announcing the public preview of Update Plans"
date: 2022-02-09
meta_desc: Update Plans enable you to see and confirm the updates that will be made to your infrastructure and then apply those updates at a later time.
meta_image: update_plans_preview.png
authors:
    - fraser-waters
tags:
    - features
---

Pulumi’s previews are an important part of any workflow where you want to see the changes that will be made to your infrastructure before actually making the changes (with `pulumi up`). However, today there is no guarantee that the `pulumi up` operation will do only what was previewed; if the program, or your infrastructure, changes between the preview and the update, the update might make additional changes to bring your infrastructure back in line with what’s defined in your program. We’ve [heard from many of you](https://github.com/pulumi/pulumi/issues/2318) that you need a strong guarantee about exactly which changes an update will make to your infrastructure, especially in critical and production environments.

<!--more-->

Today, I’m excited to announce the public preview of Update Plans, a new Pulumi feature which guarantees that operations shown in `pulumi preview` will run on `pulumi up`. Update Plans also help catch any unexpected changes that might happen between when you preview a change and when you apply that change. Update Plans work by saving the results of a `pulumi preview` to a _plan file_, which enables you to restrict subsequent `pulumi up` operations to only the actions saved in the plan file. This helps you ensure that what you saw in the `pulumi preview` is what will actually happen when you run `pulumi up`.

Here’s an example of Update Plans in action. In this example we're creating a new AWS EC2 instance and associated security group. First, we plan the change with `pulumi preview --save-plan plan.json`, and then we examine the plan file to see which resources the plan expects to change. Finally, we run an update that's constrained to the plan with `pulumi up --plan plan.json`.

{{< asciicast id="466347" >}}

To get started, you only need to add `--save-plan <file>` to the preview command and `--plan <file>` to the up command. In the video above, we demonstrated a pretty trivial example where our program did what our plan expected, so everything ran just as expected. But what if we changed our program to have a different `userData` value and ran it against the same plan? If we clear the infrastructure we just created and use the same plan with the changed program, then Update Plans will return an error and block the change.

{{< asciicast id="466462" >}}

When updates fail to validate against the plan, Pulumi will print what constraint failed. In the example above, the resource `urn:pulumi:dev::aws-ts-webserver::aws:ec2/instance:Instance::web-server-www` changed the value of the property `userData`.

## New scenario enabled by Update Plans: pull request validation workflows

Software development teams commonly use version control-based workflows to review and monitor the code that is added to a codebase. For example, many teams protect their primary branch (e.g. `main`, `master`, `trunk`) from direct code pushes and instead require a pull or merge request where the changes can be reviewed and continuous integration (CI) and tests can be run.

With Update Plans, this same workflow is now possible with infrastructure managed by Pulumi. Assuming you already have CI set up for your pull/merge requests, you can run `pulumi preview --save-plan PLAN-FILENAME` and output the resulting plan file as a CI artifact. Then, update the CI workflow that runs when changes are merged to run `pulumi up --plan PLAN-FILENAME`.

## Try Update Plans

{{% notes type="info" %}}

Update Plans are in public preview. We recommend using it only in non-critical, non-production scenarios during the preview period.

{{% /notes %}}

We’re eager for you to try the public preview of Update Plans and let us know what you think. To try it out, make sure you’ve updated to Pulumi [3.24.1](https://github.com/pulumi/pulumi/releases/tag/v3.24.1) then set the following environment variable in your shell:

```sh

PULUMI_EXPERIMENTAL=true

```

Then, save a plan file:

```sh

pulumi preview --save-plan plan.json

```

Finally, pass the plan file to the `pulumi up` command:

```sh

pulumi up --plan-file plan.json

```

When `PULUMI_EXPERIMENTAL` is set `pulumi up` will also generate a plan during it's preview stage which will then apply to the update if an explict plan hasn't been given via `--plan`. This ensures your `up` previews match what happens in the resulting operations.

We’d love to hear your thoughts on the Update Plans feature! Feel free to start discussions or ask questions using [GitHub Discussions in the `pulumi/pulumi` repository]([https://github.com/pulumi/pulumi/discussions/categories/preview-features](https://github.com/pulumi/pulumi/discussions/categories/preview-features)).
