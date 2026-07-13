---
title: ESC webhooks for secret rotations
date: 2026-06-26
aliases:
    - /releases/changelog/esc-secret-rotation-webhooks/
meta_desc: ESC rotation webhooks notify you immediately whenever a secret rotation happens.
authors:
    - sean-yeh
---

[ESC secret-rotation webhooks](/docs/esc/concepts/webhooks/) enable you to be notified whenever an ESC secret rotation happens, so your dependent services can take action accordingly.

Like all Pulumi webhooks, ESC webhooks are configurable in the Pulumi Cloud console, [with the Pulumi Service Provider](/docs/esc/integrations/pulumi-service-provider/), or [with the Pulumi CLI](/docs/iac/cli/commands/pulumi_env_webhook/).

To learn more about rotation webhooks, [read the announcement post](/blog/introducing-esc-secret-rotation-webhooks/) or [check out the docs](/docs/esc/concepts/webhooks/).
