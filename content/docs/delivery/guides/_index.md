---
title: Guides
title_tag: Pulumi Delivery guides
meta_desc: Task-oriented guides for Pulumi Delivery, covering cloud credentials for each stage, common pipeline patterns, and connecting pipelines.
menu:
  delivery:
    name: Guides
    parent: delivery-home
    identifier: delivery-guides
    weight: 20
---

These guides walk through common Pulumi Delivery tasks. Each one stands on its own, so start with whichever matches what you're trying to do.

- [Cloud credentials](/docs/delivery/guides/cloud-credentials/): Give each stage the cloud credentials it needs, using Pulumi ESC and OIDC.
- [Pipeline patterns](/docs/delivery/guides/pipeline-patterns/): Build stages from a helper function, smoke-test each deploy, and update stacks that depend on each other.
- [Connect pipelines](/docs/delivery/guides/multiple-pipelines/): Pass values from an upstream pipeline to a downstream one, and run several pipelines from one repository.
