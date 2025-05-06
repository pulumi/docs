---
title_tag: Private Registry | Pulumi IDP
title: Private Registry
h1: "Private Registry"
meta_desc: This page provides an overview on how to get started with Pulumi IDP Private Registry.
weight: 3
menu:
  idp:
    parent: idp-get-started
    identifier: idp-get-started-private-registry
---

Pulumi Private Registry is the source of truth for an organization's infrastructure building blocks like components and templates -- the same [components](/docs/iac/concepts/resources/components/) and [templates](/docs/pulumi-cloud/developer-portals/templates/) that power golden path workflows in Pulumi. Platform engineers can codify organizational standards in their building blocks using features like [Pulumi ESC](/docs/esc/) and [Pulumi IaC Policies](/docs/insights/get-started/add-policies/), ensuring that all infrastructure users provision is compliant from the beginning.

Developers leverage templates and components in their preferred workflows, whether it be incorporating components into Pulumi programs, scaffolding a low-code program with components and YAML, or using the Pulumi console for no-code deployments. The private registry is also a resource for developers to discover components and templates, browse their APIs, and use READMEs to understand how to use them.

## Component Publishing

[Pulumi Components](/docs/iac/concepts/resources/components/) are a way to encapsulate resources in a reusable manner. Components are also a powerful way for platform teams to integrate security, compliance, and operational requirements into golden paths so that developers don't need to worry about it. Once a component is pushed to GitHub or GitLab, it is published to an organization's private registry using the `publish` CLI command. Pulumi automatically introspects the component schema and generates API docs, which are displayed in the registry.

### Publishing Components

If you're new to Pulumi components, the [Build a Component](/docs/iac/using-pulumi/extending-pulumi/build-a-component/) guide is a great resource for getting started. Once you've authored your component, push it to a GitHub or GitLab repository that Pulumi can access. Private repositories are supported, but the repository must be open to inbound requests.

#### Component Versioning

Pulumi checks for a git version tag when the `publish` command is executed and stores it as the component version. The tag must adhere to [to the semantic versioning standard](https://semver.org/).

#### Component README

A README is required when publishing a component. Pulumi renders markdown README files in the private registry. They're a great way to provide context for a component. By default, the Pulumi CLI looks for a README in the component's root directory. The `--readme` flag can be used to specify a custom source.

```bash
pulumi package publish /path/to/your/component --readme README_LOCATION
```

#### Specifying an Organization

If you're part of multiple organizations and do not have a [default organization](/docs/iac/cli/commands/pulumi_org_set-default/) set, you must specify the org by using the `--publisher` flag.

```bash
pulumi package publish /path/to/your/component --publisher ORG_NAME
```

#### CLI Publishing

The `publish` CLI command is used to publish components to the private registry.

```bash
pulumi package publish COMPONENT_LOCATION
```

For example, if your github organization is ACME and you are publishing the `k8s-cluster` component, you'd run:

```bash
pulumi package publish https://github.com/acme/k8s-cluster
```

#### Authenticating with Private Repositories

 If your repository is private, a valid `GITHUB_TOKEN` or `GITLAB_TOKEN` is required for all commands, including `publish`, `get schema`, and when using the component in a program -- `pulumi install`, `pulumi up`, etc.

 By default, the Pulumi CLI will look for a token in the `GITHUB_TOKEN` and `GITLAB_TOKEN` environment variables.

```bash
GITHUB_TOKEN="$(gh auth token)"
pulumi package publish COMPONENT_LOCATION
```

## Pulumi Templates

[Pulumi Templates](https://www.pulumi.com/docs/pulumi-cloud/developer-portals/templates/#defining-an-organization-template) are an efficient way to scaffold new Pulumi Programs. Organization Templates are sourced from GitHub repositories and are available to users in the private registry and [New Project Wizard](https://www.pulumi.com/docs/pulumi-cloud/developer-portals/new-project-wizard/).

### Template Publishing

{{% notes type="info" %}}
Organization templates require the Enterprise or Business Critical plan
{{% /notes %}}

To publish templates in the private registry, follow [this integration guide](https://www.pulumi.com/docs/pulumi-cloud/developer-portals/templates/#prerequisites). Once the integration is complete, discovered templates will appear in the private registry.

### Components in Templates

You can reference components in the `packages` section of the `Pulumi.yaml` project file. The component and its SDK are installed when running `pulumi install`.

```yaml
name: ${PROJECT}
description: ${DESCRIPTION}
runtime: yaml

packages:
  aws-k8s: github.com/flostadler/aws-k8s@v0.0.19

# Define the template's configuration settings
template:
  ....
resource:
  aws-k8s
```

{{< get-started-stepper >}}
