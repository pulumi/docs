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

The Pulumi Private Registry is the source of truth for an organization's infrastructure building blocks. Users leverage the private registry to discover components and templates, browse their APIs, and understand how to use them to provision resources through READMEs.

## Component Publishing
Pulumi Components create sets of related resources, acting as an abstraction to encapsulate the details of their implementation. Components are published to the private registry with the Pulumi CLI. Once they are published, Pulumi automatically generates API docs, which are displayed in the registry. 

### CLI Publishing

Author your component, encapsulating security, compliance, and operational requirements
Optionally include a README
Run `pulumi package publish << component location >>`

### Customizing the README

This looks for a README in the component root directory; optionally use the `--readme` flag to point to one
Specifying an organization
If you're part of multiple organizations and do not have a default organization set, you need to specify the org by using `--publisher ORG_NAME`.

🧠 Note: If your repo is private, you’ll need to pass a valid GITHUB_TOKEN to all commands, including publish, get schema, and when using the component in a program (`pulumi install`, `pulumi up`, etc


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