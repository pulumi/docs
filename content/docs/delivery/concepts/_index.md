---
title: Concepts
title_tag: Pulumi Delivery concepts
h1: How Pulumi Delivery works
meta_desc: How Pulumi Delivery models a release pipeline as a Pulumi program, and how pipelines, runs, stages, members, sources, and releases relate.
menu:
  delivery:
    name: Concepts
    parent: delivery-home
    identifier: delivery-concepts
    weight: 10
aliases: []
---

<!-- TODO(launch): Add `pulumi_cloud_feature: delivery` to the front matter once pulumi/marketing-web adds a hidden `delivery` feature (min_edition: essentials) and its sync PR updates data/pulumi_editions.yaml. Then drop the hand-written edition sentence. -->

<!-- TODO(launch): Product owner to confirm positioning paragraph against the final launch and messaging brief (MA-849). -->

Most teams with more than a handful of stacks end up writing release orchestration by hand: a CI job that runs `pulumi up` on the network stack, waits, runs the app stacks, pauses for someone to look at staging, and then does it all again for production. Pulumi Delivery replaces that glue with a Pulumi program. You declare your sources, stages, stacks, jobs, and gates in TypeScript, Python, Go, C#, or Java, and Pulumi Cloud runs each release through the stages in order.

Because the pipeline is a Pulumi program, it's versioned with your code and reviewed like any other change. You can use loops, functions, and conditionals to build it, and it gets previews and a history like any other stack.

{{% notes type="info" %}}
Pulumi Delivery is in public preview. Behavior, the SDK, and the REST API routes under `/api/preview/` can change before general availability.
{{% /notes %}}

## The pipeline program and the pipeline stack

The pipeline lives in a repository as a Pulumi project. It declares exactly one `Pipeline` resource, which names the source and directory of the program itself. You register the pipeline by running `pulumi up` on its stack, called the _pipeline stack_. Registration finishes with exit code 10, because the members it declared are waiting for a run.

## Runs

A _run_ takes one release through the stages. Each run gets its own _run stack_, named `<pipeline stack>-r<run number>`, where Pulumi Cloud executes the pipeline program. Run stacks don't show up in stack lists or search; open one from the page of its run. Don't run `pulumi up` on a run stack yourself.

A run moves forward in _passes_. A pass is one execution of the pipeline program on the run stack, and each pass makes as much progress as the stages and gates allow.

## Stages

A _stage_ is a step of the pipeline, usually one environment. A stage waits for its upstream stages, listed in `from`, and for its gate, set in `when`. A stage deploys one run at a time. If a newer run arrives while an older one is still waiting for the stage or its gate, the newer run takes its place. A run the stage has already admitted is never replaced.

See [Stages and gates](/docs/delivery/concepts/stages-and-gates/).

## Members

A _member_ is a resource that does work in a stage:

- `Stacks` updates one or more existing stacks.
- `Job` runs a shell command.
- `Artifact` publishes a value for other pipelines to read.

See [Members](/docs/delivery/concepts/members/).

## Sources and releases

A _source_ is a repository and branch. A source locks its commit when the run first creates it, so every stage of a run works from the same code. The sources you declare together make up the _release_, which has a release number. Read it from `pipeline.releaseNumber`, and read a source's commit from `source.commit`. Both are unknown during registration and preview and known during a run.

Declare every source at the top level of the program. A source created from a member output after the first pass can't lock a commit, and the run fails.

A _trigger_ on a source decides whether a change starts a run. See [Sources and triggers](/docs/delivery/concepts/sources-and-triggers/).

## How the pieces fit together

```mermaid
flowchart LR
    push[Push to main] --> src[GitHubSource]
    src --> run[Run with release N]
    run --> dev[Stage: dev]
    dev --> devm[Stacks + smoke Job]
    devm --> gate{Gate: approval}
    gate --> prod[Stage: prod]
    prod --> prodm[Stacks]
```

<!-- TODO(launch): Replace with a design-approved diagram or console screenshot if design provides one. -->

## How Delivery relates to Pulumi Deployments

<!-- TODO(launch): Product owner to decide the coexistence story (DLV-532) before this section ships. Current draft below is a placeholder. -->

[Pulumi Deployments](/docs/deployments/) runs Pulumi operations for a single stack from its deployment settings. Delivery orchestrates updates across many stacks and environments, with ordering and gates between them. Delivery doesn't read a stack's deployment settings and doesn't do its own OIDC exchange; see [Cloud credentials](/docs/delivery/guides/cloud-credentials/) for how to give members credentials.

## Next steps

- [Get started](/docs/delivery/get-started/) with a two-stage pipeline.
- Read about [sources and triggers](/docs/delivery/concepts/sources-and-triggers/).
