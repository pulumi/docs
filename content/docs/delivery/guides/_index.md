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

These guides walk through common Pulumi Delivery tasks:

- [Cloud credentials](/docs/delivery/guides/cloud-credentials/): Give each stage the cloud credentials it needs, either through the pipeline or with Pulumi ESC and OpenID Connect (OIDC).
- [Pipeline patterns](/docs/delivery/guides/pipeline-patterns/): Build stages from a helper function and smoke-test each deploy.
- [Connecting pipelines](/docs/delivery/guides/multiple-pipelines/): Pass values from an upstream pipeline to a downstream one, and run several pipelines from one repository.
