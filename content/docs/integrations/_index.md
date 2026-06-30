---
title: Integrations
linktitle: Integrations
docs_home: true
notitle: true
norightnav: true
menu:
  integrations:
    identifier: integrations-home
    weight: 1
meta_desc: Integrations connect Pulumi with the clouds, version control systems, and tools you already use.
h1: Integrations
description: <p>Integrations connect Pulumi with the clouds, version control systems, and tools you already use.</p>

sections:
- type: button-cards
  heading: Clouds
  cards:
  - image: /logos/tech/aws.svg
    heading: AWS
    description: Build and manage AWS infrastructure with Pulumi providers, packages, templates, guides, ESC integrations, Insights, and policy packs.
    link: /docs/integrations/clouds/aws/
  - image: /logos/tech/azure.svg
    heading: Azure
    description: Build and manage Azure infrastructure with Pulumi providers, packages, templates, guides, ESC integrations, Insights, and policy packs.
    link: /docs/integrations/clouds/azure/
  - image: /logos/tech/gcp.svg
    heading: Google Cloud
    description: Build and manage Google Cloud infrastructure with Pulumi providers, packages, templates, guides, ESC integrations, Insights, and policy packs.
    link: /docs/integrations/clouds/gcp/
  - image: /logos/tech/kubernetes.svg
    heading: Kubernetes
    description: Manage Kubernetes clusters and application workloads, plus the Pulumi Kubernetes Operator for in-cluster stack management.
    link: /docs/integrations/clouds/kubernetes/

- type: button-cards
  heading: Version control
  cards:
  - image: /logos/tech/github.svg
    heading: GitHub App
    description: Surface Pulumi stack previews as PR comments and checks. Enable push-to-deploy via Pulumi Deployments.
    link: /docs/integrations/version-control/github-app/
  - image: /logos/tech/gitlab.svg
    heading: GitLab
    description: Surface Pulumi previews on merge requests, deploy on push, create review stacks, and use GitLab repos as template sources.
    link: /docs/integrations/version-control/gitlab/
  - image: /logos/tech/ci-cd/azure-devops.svg
    heading: Azure DevOps
    description: Connect Azure DevOps repositories to Pulumi Cloud Deployments to deploy on push, preview pull requests, and post PR summaries.
    link: /docs/integrations/version-control/azure-devops-integration/

- type: button-cards
  heading: Developer tools
  cards:
  - icon: code-window
    heading: VS Code
    description: Debug Pulumi programs, get Pulumi YAML language support, and manage ESC environments without leaving your editor.
    link: /docs/integrations/vs-code/

- type: flat
  heading: Have questions?
  description: <p>For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a>, <a href="https://github.com/pulumi" target="_blank">GitHub</a>, or <a href="/support/">contact support</a>.</p>
---
