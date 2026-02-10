---
title: Pulumi Backstage plugin
title_tag: Get started with the Pulumi Backstage plugin
h1: Pulumi Backstage plugin
meta_desc: Learn about the Pulumi Backstage plugin for integrating Pulumi with your developer portal.
menu:
  idp:
    name: Pulumi Backstage plugin
    parent: idp-concepts
    weight: 60
    identifier: idp-concepts-backstage-plugin
aliases:
- /docs/idp/developer-portals/backstage/
- /docs/pulumi-cloud/developer-platforms/backstage/
- /docs/pulumi-cloud/developer-portals/backstage/
---

[Backstage](https://backstage.io/) is an open-source framework for building developer portals. The [Pulumi Backstage Plugin](https://github.com/pulumi/pulumi-backstage-plugin) enables organizations to integrate Pulumi with their Backstage instance.

## Features

The plugin provides:

- **Stack Activity View**: A Pulumi tab that displays stack activity for Backstage projects containing Pulumi stacks
- **Scaffolding Actions**: Two scaffolding actions for the Backstage template system:
  - `pulumi:new` - Create new Pulumi projects from [organization templates](/docs/idp/concepts/organization-templates)
  - `pulumi:up` - Trigger Pulumi stack updates

## Installation

The Pulumi Backstage Plugin is available through the [Backstage Plugin directory](https://backstage.io/plugins/). For detailed installation and configuration instructions, see:

- [Pulumi Backstage Plugin repository](https://github.com/pulumi/pulumi-backstage-plugin)
- [Roadie Pulumi Backstage Plugin guide](https://roadie.io/backstage/plugins/pulumi/)
