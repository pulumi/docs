---
title_tag: "Pulumi Integrations"
meta_desc: Connect Pulumi with your version control system, CI/CD tools, and developer platform using Pulumi-maintained integrations.
title: Integrations
linktitle: Integrations
h1: Integrations
meta_image: /images/docs/meta-images/docs-meta.png
docs_home: true
notitle: true
norightnav: true
menu:
  integrations:
    identifier: integrations-home
    weight: 1
description: |
  Pulumi-maintained integrations connect Pulumi with your version control system and CI/CD tools, enabling infrastructure previews on pull requests and automated pipeline workflows.

sections:
- type: button-cards
  heading: VCS integrations
  cards:
  - image: /logos/tech/github.svg
    heading: GitHub App
    description: Surface Pulumi stack previews as PR comments and checks. Enable push-to-deploy via Pulumi Deployments.
    link: /docs/integrations/github-app/
  - image: /logos/tech/gitlab.svg
    heading: GitLab
    description: Add Pulumi previews to merge requests, run Pulumi in GitLab CI, and use GitLab repos as IDP template sources.
    link: /docs/integrations/gitlab/
  - image: /logos/tech/ci-cd/azure-devops.svg
    heading: Azure DevOps
    description: Install the Pulumi task extension to run Pulumi commands in Azure Pipelines without custom scripts.
    link: /docs/integrations/azure-devops/

- type: flat
  heading: Have questions?
  description: <p>For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a>, <a href="https://github.com/pulumi" target="_blank">GitHub</a>, or <a href="/support/">contact support</a>.</p>
---
