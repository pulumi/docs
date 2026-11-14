---
title_tag: Pulumi Delivery limits
meta_desc: Size and time limits for Pulumi Delivery pipelines and runs.
title: Limits
h1: Limits
menu:
  delivery:
    name: Limits
    parent: delivery-home
    weight: 30
aliases: []
---

## Size and time limits

Pulumi Delivery enforces these limits on each pipeline and run:

| Limit | Value |
| --- | --- |
| Pipelines in an organization on the Free edition | 1 |
| Stack entries, jobs, and artifacts in a pipeline | 1,000. Each `Stacks` entry, `Job`, and `Artifact` counts as one. |
| Stages in a pipeline | 1,000 |
| Sources in a pipeline | 100 |
| Config per `Stacks` entry | 100 keys and 64 KiB |
| [Passes](/docs/delivery/concepts/#runs) in a run | 5,000, then the run fails. |
| Time limit of a pass | 1 hour |
| Time limit of a stack update or job | 2 hours by default. Set `timeout` on a `Stacks` entry or `Job` to change it, from 5 minutes to 24 hours. |
| Job outputs | 1 MiB |
| [Run stack](/docs/delivery/concepts/#runs) retention | Deleted 90 days after the run ends |

<!-- TODO(launch): Confirm that a pass doesn't wait on stack updates or jobs (whose limit can be up to 24 hours), and say so here. -->
