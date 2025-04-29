---
title_tag: Private Registry | Pulumi IDP
title: Private Registry
h1: "Private Registry"
meta_desc: This page provides an overview on how to get started with Pulumi IDP.
weight: 3
menu:
  idp:
    parent: idp-get-started
    identifier: idp-get-started-private-registry
---

The Pulumi Private Registry is the source of truth for an organization's infrastructure building blocks like components and templates -- the same [components](/docs/iac/concepts/resources/components/) and [templates](/docs/pulumi-cloud/developer-portals/templates/) that power provisioning workflows in Pulumi. Platform engineers can codify organizational standards in Pulumi their building blocks using features like [Pulumi ESC](/docs/esc/) and [Pulumi IaC Policies](/docs/insights/get-started/add-policies/), ensuring all infrastructure that users provision is compliant from the beginning.

Developers leverage templates and components in their preferred workflows, whether it be incorporating components into Pulumi programs, scaffolding a low-code program with components and YAML, or using the Pulumi New Project Wizard for no-code deployments. The private registry is also a resource for developers to discover components and templates, browse their APIs, and use READMEs to understand how to use them READMEs.

## Pulumi Components

[Pulumi Components](/docs/iac/concepts/resources/components/) are a method for encapsulating resources in a reusable way. Components are also a powerful way for platform teams to scalably integrate security, compliance, and operational requirements into golden paths so that developers don't need to worry about. Once a component is pushed to GitHub or GitLab, the component is published to an organization's private registry with the `publish` CLI command. Pulumi automatically introspects the component schema and generates API docs, which are displayed in the registry.

### Component Authoring

If you're new to Pulumi components, the [Build a Component](/docs/iac/using-pulumi/extending-pulumi/build-a-component/) guide is a great resource for getting started. Once you've authored your component, push it to a GitHub or GitLab repository that Pulumi can access. Private repositories are supported, but the repository must be open to inbound requests.



#### Component Versioning

Pulumi checks for a git version tag when the `publish` command is executed and will store it as the component <a href="https://semver.org/" target="_blank">SemVer</a>.

#### CLI Publishing

The `publish` CLI command is used to publish components in the private registry.

```bash
$ pulumi package publish COMPONENT_LOCATION
```

For example, if you were publishing the [Pulumi AWSx component](https://github.com/pulumi/pulumi-awsx), you'd run:

The `publish` CLI command is used to publish components in the private registry.

```bash
$ pulumi package publish https://github.com/pulumi/pulumi-awsx
```

#### Authenticating with Private Repositories

 If your repository is private, a valid GITHUB_TOKEN is required for all commands, including publish, get schema, and when using the component in a program (pulumi install, pulumi up, etc).

 By default, the Pulumi CLI will look for a toke in the GITHUB_TOKEN environment variable

```bash
$ GITHUB_TOKEN="$(gh auth token)"
$ pulumi package publish COMPONENT_LOCATION
```

#### Component README

Pulumi renders markdown README files in the private registry. They're a great way to provide context for a component. By default, the Pulumi CLI looks for a README in the component's root directory. The `--readme` flag can be used to specify a custom source.

```bash
$ pulumi package publish /path/to/your/component --readme README_LOCATION
```

#### Specifying an Organization

If you're part of multiple organizations and do not have a default organization set, you need to specify the org by using the --publisher flag.

```bash
$ pulumi package publish /path/to/your/component --publisher ORG_NAME
```

## Template Publishing
Point to publishing org templates
Mention CLI publishing is coming soon

You can reference your components in the packages section of your Pulumi.yaml project file. This way, your component and its SDK are installed when running pulumi install.

```yaml
name: ${PROJECT}
description: ${DESCRIPTION}
runtime: yaml

packages:
  aws-k8s: github.com/flostadler/aws-k8s@v0.0.19

# Define the template's configuration settings
template:
```