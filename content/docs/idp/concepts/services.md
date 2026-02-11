---
title_tag: Services | Pulumi IDP
title: Services
h1: "Services"
meta_desc: Learn about Pulumi Services for organizing and managing infrastructure entities.
aliases:
  - /docs/idp/get-started/services/
menu:
  idp:
    parent: idp-concepts
    identifier: idp-concepts-services
    weight: 50
---

Pulumi Services are logical groupings of Pulumi entities such as [stacks](/docs/iac/concepts/stacks/) and [ESC environments](/docs/esc/environments/). They enable users to model infrastructure in Pulumi in a way that is familiar to them.

## Creating a service

A service can be created during the project and stack creation flows. They can also be created manually from the services list page by selecting the Create Service button, where the name, description, entities, and properties can be set.

## Adding entities to a service

Entities can be added when a service is created or after the fact.

1. Click Add Service for a new service or Add Entity for an existing service.
2. At the bottom of the page, there is an Add Entities section. Select the Add Entities button.
3. Select Add Stack or Add Environment based on which entity type you'd like to add to the service.
4. In the pane that slides out from the right, you can search for and add select stacks to add to the service. Once finished, select Add Entities.
5. Save the service.

## Service Properties

Service properties are metadata that provide additional context to a service. Properties can be a URL, such as an observability dashboard link, free-form text describing the service in more detail, Slack channels, or Teams channels. Properties can be set during the service creation flow or after the fact.
