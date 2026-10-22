---
title: Pulumi Backstage plugin
title_tag: Get started with the Pulumi Backstage plugin
h1: Pulumi Backstage plugin
meta_desc: Learn about the Pulumi Backstage plugin for integrating Pulumi with your developer portal.
menu:
  idp:
    name: Pulumi Backstage plugin
    parent: idp-integrations
    weight: 20
    identifier: idp-integrations-backstage-plugin
aliases:
- /docs/idp/concepts/backstage-plugin/
- /docs/idp/developer-portals/backstage/
- /docs/pulumi-cloud/developer-platforms/backstage/
- /docs/pulumi-cloud/developer-portals/backstage/
---

[Backstage](https://backstage.io/) is an open-source framework for building developer portals. The [Pulumi Backstage Plugin](https://github.com/pulumi/pulumi-backstage-plugin) enables organizations to integrate Pulumi with their Backstage instance.

## Features

The plugin provides:

- **Pulumi cards and activity view**: Cards for Backstage components and systems that show the Pulumi stack, organization, project, and stack outputs, along with a stack activity view. Entities with multiple stacks or organizations display them as tabs.
- **Pulumi Dashboard**: An optional standalone page showing organization-wide metrics, recent stack updates, deployments, and resource trends.
- **Scaffolding actions**: Actions for the Backstage template system:
  - `pulumi:new` - Create new Pulumi projects from [organization templates](/docs/idp/concepts/organization-templates)
  - `pulumi:up` - Run a Pulumi stack update
  - `pulumi:preview` - Preview the changes a stack update would make
  - `pulumi:destroy` - Destroy the resources in a stack
  - `pulumi:deployment:config` - Configure [Pulumi Deployments](/docs/deployments/) settings for a stack
  - `pulumi:deployment:run` - Run a Pulumi deployment
- **Catalog provider**: A catalog backend module that imports Pulumi stacks into the Backstage software catalog as Resource entities.

## Installation

The Pulumi Backstage Plugin is available through the [Backstage Plugin directory](https://backstage.io/plugins/). For detailed installation and configuration instructions, see:

- [Pulumi Backstage Plugin repository](https://github.com/pulumi/pulumi-backstage-plugin)
- [Roadie Pulumi Backstage Plugin guide](https://roadie.io/docs/integrations/pulumi/)
