---
title: Environments (ESC)
title_tag: Environments, Secrets, and Configuration (ESC)
h1: Environments, Secrets, and Configuration (ESC)
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  usingpulumi:
    identifier: esc
    weight: 4
---

Pulumi ESC allows teams to tackle configuration complexity at scale, alleviating maintenance and operational burden and reducing costly mistakes, and creating a more secure by default posture. Let's walk through some of the key capabilities of Pulumi ESC.

## Import - Removing Duplication and Copy/Paste

Platform and service teams can centralize and control common config and secrets by creating environments that other teams can import. They can trace what other environments or stacks are using their configuration and assess blast radius of any changes.

### Organizing Environments

Environments can map to your organizational team or security boundaries, rather than just named deployment targets.

Imagine a hypothetical dev organization comprised of a few teams:

* The billing service team, that manages secrets/config for the payment processor
* The communications team, that manages secrets/config for the mailing service and texting service.
* The central platform team, that owns most common config, including OIDC config and the keys/config for the feature flag system.

Teams can manage permissions to these environments to minimize security exposure.

Here is one way those teams might organize their environments:

![A diagram showing how the different environments with team based organization](img/team_environments.png)

## Authentication and RBAC

Teams can create environments and then control what permissions others have to those environments. They can control who can update and preview environments, as well as who can open environments and see secrets. Audit logs let teams know who has changed or accessed configuration.

## OIDC and access Secrets

Teams can setup OIDC in their cloud providers to allow environments to retrieve dynamic short-lived credentials. They can also pull secrets from other secrets managers and vaults.

These can be used with [Pulumi IaC](/docs/concepts/environments/#using-with-pulumi-iac) with `pulumi up`. These can be used to [run external CLIs](/docs/concepts/environments/#running-third-party-commands-using-pulumi-esc-secrets-and-config) like `aws`, `kubectl`, and more.

## Conceptual Overview of Environments

Go deeper on how environments can be managed using [Pulumi ESC](/docs/concepts/environments/).

## Getting Started with Pulumi ESC

Here is a link to our [fancy new tutorial](/docs/using-pulumi/esc/get-started/).

## ESC CLI overview

Please see [ESC CLI overview](esc/) for details on interacting with environments using the command line.

## Syntax Reference

[Pulumi ESC yaml syntax](reference/) shows examples of simple and complex configuration, imports, and common providers.
