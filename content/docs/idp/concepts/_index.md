---
title: Concepts
title_tag: Pulumi IDP Concepts
h1: Pulumi IDP Concepts
meta_desc: Learn about the concepts and components of Pulumi IDP.
menu:
  idp:
    parent: idp-home
    identifier: idp-concepts
    weight: 1
aliases:
  - /docs/idp/get-started/
  - /docs/idp/developer-portals/
  - /docs/pulumi-cloud/developer-portals/
  - /docs/pulumi-cloud/developer-platforms/
---

An Internal Developer Platform (IDP) is a tool platform teams use to provide self-service golden path workflows for users to perform Day 1 and Day 2 activities. Platform engineers codify golden paths by incorporating security, compliance, cost, and other requirements in infrastructure building blocks.

Pulumi IDP is a bottom-up approach for platform teams to provide self-service workflows to their users, from Day 0 to Day 2. Unlike an Internal Developer Portal, Pulumi IDP facilitates concrete outcomes, not just information consumption.

Pulumi IDP can facilitate workflows across the Day 0-2 spectrum thanks to powerful features like [Private Registry](/docs/idp/concepts/private-registry/), [Components](/docs/iac/concepts/resources/components/), [Templates](/docs/idp/concepts/organization-templates/), [Services](/docs/idp/concepts/services/), and more. By using a bottom-up approach, platform engineers can codify security, compliance, and operational requirements in their golden paths without additional effort.

## Day 0 - Establish a central source of truth for golden paths

Platform engineers and other centralized teams curate an infrastructure source of truth by authoring and publishing components and templates to the private registry. Templates and components are codified with security, compliance, and operational standards to ensure golden paths are hardened from the beginning.

Learn more about [Pulumi Private Registry](/docs/idp/concepts/private-registry/), [Pulumi Components](/docs/iac/concepts/resources/components/), and [Pulumi Templates](/docs/idp/concepts/organization-templates/). You can also learn about securing artifacts with [Pulumi ESC](/docs/esc/) and ensuring compliance and standards with [Pulumi Policies](/docs/insights/get-started/add-policies/).

## Day 1 - Provision infrastructure through flexible workflows

Depending on their use case and the available golden paths, developers may choose to scaffold several components in a Pulumi YAML program. Alternatively, they can point and click to deploy a no-code workload directly from the Pulumi console using the [New Project Wizard](/docs/idp/concepts/new-project-wizard/). Or, in custom use cases, they may write a Pulumi program in their preferred programming language. Regardless, thanks to the bottom-up approach of the Pulumi IDP, workloads are deployed via golden paths, leveraging artifacts that have been authored and approved by platform teams.

Learn more about the [Pulumi Private Registry](/docs/idp/concepts/private-registry/), [no-code workflows](/docs/idp/concepts/no-code-stacks/), and [Pulumi Deployments](/docs/deployments/deployments/).

## Day 2 - Confidently maintain and extend infrastructure

Users can easily model their infrastructure using Pulumi services, logical groupings of Pulumi entities, such as stacks and ESC environments. Users can also adjust configuration and redeploy stacks directly from the Pulumi UI when using no-code workflows.

Learn more about [no-code workflows](/docs/idp/concepts/no-code-stacks/) and [Pulumi Services](/docs/idp/concepts/services/).

## Custom IDP

Pulumi's flexible building blocks can support organizations with bespoke needs who need to build their own IDP. You can integrate Pulumi with your existing developer portal using [Organization Templates](/docs/idp/concepts/organization-templates/), the [Pulumi Backstage Plugin](/docs/idp/concepts/backstage-plugin/), or by [publishing from GitHub Actions](/docs/idp/guides/publishing-from-github-actions/).
