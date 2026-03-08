---
title_tag: "Pulumi Version Control Integrations"
meta_desc: Connect Pulumi with your version control system using Pulumi-maintained integrations for GitHub, GitLab, and Azure DevOps.
title: Version Control
linktitle: Version Control
h1: Version Control
meta_image: /images/docs/meta-images/docs-meta.png
docs_home: true
notitle: true
norightnav: true
menu:
  version-control:
    identifier: version-control-home
    weight: 1
aliases:
- /docs/integrations/
description: |
  Pulumi-maintained version control integrations connect Pulumi with your VCS provider, enabling infrastructure previews on pull requests and automated deployment workflows.

sections:
- type: button-cards
  heading: VCS integrations
  cards:
  - image: /logos/tech/github.svg
    heading: GitHub App
    description: Surface Pulumi stack previews as PR comments and checks. Enable push-to-deploy via Pulumi Deployments.
    link: /docs/version-control/github-app/
  - image: /logos/tech/gitlab.svg
    heading: GitLab
    description: Add Pulumi previews to merge requests, run Pulumi in GitLab CI, and use GitLab repos as IDP template sources.
    link: /docs/version-control/gitlab/
  - image: /logos/tech/ci-cd/azure-devops.svg
    heading: Azure DevOps Integration
    description: Connect Azure DevOps repositories to Pulumi Cloud Deployments to deploy on push, preview pull requests, and post PR summaries.
    link: /docs/version-control/azure-devops-integration/

- type: flat
  heading: Have questions?
  description: <p>For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a>, <a href="https://github.com/pulumi" target="_blank">GitHub</a>, or <a href="/support/">contact support</a>.</p>
---
