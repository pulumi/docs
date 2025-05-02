---
title_tag: Workflows | Pulumi IDP
title: Workflows
h1: "Workflows"
meta_desc: This page provides an overview on Pulumi IDP Workflows.
weight: 3
menu:
  idp:
    parent: idp-get-started
    identifier: idp-get-started-workflows
---
The main goal of internal developer platforms is to provide self-service workflows that enable developers to provision infrastructure. Where pain is often felt is in attempting to offer multiple workflow types that maintain the consistency that platform teams desire. Thanks to Pulumi IDP’s bottom-up approach, workflows can be driven from the same components and templates, ensuring flexibility, consistency, and scalability.

## No-Code

In a no-code workflow, users can instantly create and deploy Pulumi programs without worrying about the underlying IaC code or stack config. The no-code workflow is built on Pulumi organization templates and stores stack config in Pulumi ESC, eliminating the need to write to a VCS.

{{% notes type="info" %}}
No-code workflows require [Pulumi Deployments](/docs/pulumi-cloud/deployments/)
{{% /notes %}}

To create a no-code stack, start by selecting New Project in the left navigation. Choose a template from the catalog, and select next. Provide any required configuration, and select “Deployments - no-code” as the deployment method. Select the Create Project button, which will deploy the stack and store the config in ESC – no VCS commits required.

To create additional stacks in the project, navigate to a project and select Add Stack in the top right corner. From there, select the Pulumi Deployments No-code option and deploy the stack.

## Low-Code

Developers often want to compose their own Pulumi programs, but platform engineering teams may wish to limit them to using standardized components. Pulumi private registry, components, and YAML programs make the process simple.

Platform engineers can author components in any programming language, encapsulating security and compliance at the source. Once published to the private registry, developers can discover components and view their automatically generated API documentation. Once they’ve identified the necessary components, using them is as simple as adding them as package dependencies in the YAML program file.

```yaml
name: kubernetes-cluster
description: k8s cluster for the auth service
packages:
  cluster: github.com/acme-corp/k8s-cluster
resources:
  cluster:
    nodes: 5
```

## Full-Code

In many cases, developers need to author IaC programs – but that doesn’t mean they need to start from scratch. Pulumi Organization Templates are an efficient way for developers to scaffold programs based on platform engineering-authored templates that are built using registry-published components. Templates can be instantiated locally from the CLI or in the Pulumi console using the new project wizard.
