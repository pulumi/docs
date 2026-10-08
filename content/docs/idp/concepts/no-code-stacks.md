---
title_tag: No-code stacks | Pulumi IDP
title: No-code stacks
h1: "No-code stacks"
meta_desc: Learn about Pulumi's no-code workflow for deploying infrastructure without writing code.
aliases:
  - /docs/idp/get-started/workflows/
menu:
  idp:
    parent: idp-concepts
    identifier: idp-concepts-no-code-stacks
    weight: 40
---
No-code stacks enable users to instantly create and deploy Pulumi programs without writing or managing IaC code or stack configuration. The no-code workflow is built on [organization templates](/docs/idp/concepts/organization-templates/) and stores stack configuration in [Pulumi ESC](/docs/esc/), eliminating the need to work with version control systems.

{{% notes type="info" %}}
No-code workflows are currently available for projects created through the [New Project Wizard](/docs/idp/concepts/new-project-wizard/) May 6th, 2025 or later. We're actively working to eliminate this requirement.
{{% /notes %}}

{{% notes type="info" %}}
No-code workflows require:

- [Pulumi Deployments](/docs/deployments/concepts/)
- [Pulumi ESC](/docs/esc/) enabled for the organization, since that is where the stack's configuration is stored
- At least one [version control integration](/docs/integrations/version-control/) configured for the organization. Any provider works — GitHub, GitLab, Azure DevOps, or Bitbucket — and the template can be sourced from a different provider than the one you have connected. The no-code stack itself is not written to a repository.

The template must come from a repository on one of those providers or from the [private registry](/docs/idp/concepts/organization-templates/#registry-backed-templates).
{{% /notes %}}

## Creating a no-code project

To create a no-code stack, use the [New Project Wizard](/docs/idp/concepts/new-project-wizard/) by selecting New Project in the left navigation. Choose a template from the catalog, and select next. Provide any required configuration, and select "Deployments - no-code" as the deployment method. Select the Create Project button, which will deploy the stack and store the config in ESC – no VCS commits required.

## Adding stacks to a no-code project

To create additional stacks in a no-code project, navigate to the project and select Add Stack in the top right corner. From there, select the Pulumi Deployments No-code option and deploy the stack.
