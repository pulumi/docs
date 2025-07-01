---
title_tag: Pulumi Cloud Overview
meta_desc: Pulumi Cloud is a secure cloud service for individuals and teams using Pulumi's open-source SDK and Pulumi ESC.
title: Pulumi Cloud
h1: Pulumi Cloud Overview
docs_home: true
notitle: true
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    cloud:
        name: Pulumi Cloud
        identifier: cloud-home
aliases:
- /docs/reference/service/
- /docs/intro/console/accounts-and-organizations/editions/
- /docs/intro/console/
- /docs/intro/pulumi-service/
- /docs/intro/pulumi-cloud/
description: <p>Pulumi Cloud is a secure cloud service for individuals and teams using Pulumi's open-source SDK and Pulumi ESC.</p>
link_buttons:
  primary:
    label: Get Started
    link: /docs/pulumi-cloud/get-started/
  secondary:
    label: Create an account
    link: https://app.pulumi.com/signup

sections:
- type: flat
  heading: Overview
  description_md: |
    [Pulumi Cloud](https://app.pulumi.com) is a secure cloud service for individuals and teams using Pulumi's open-source SDK and Pulumi Environments, Secrets and Configuration (ESC).
    
    It manages deployment state and secrets, enables search across your clouds, runs deployments, integrates with CI/CD, and enforces policies and access controls.

    The Pulumi CLI automatically uses Pulumi Cloud unless you set up a [DIY backend](/docs/concepts/state/#using-a-diy-backend).
- type: button-cards
  heading: Featured Capabilities
  cards:
  - heading: Pulumi Copilot
    link: /docs/pulumi-cloud/copilot/
    description: Generative AI-powered intelligent cloud management
    primary_button_label: Get Started
    primary_button_link: /docs/pulumi-cloud/copilot/
    secondary_button_label: Learn More
    secondary_button_link: /docs/pulumi-cloud/copilot/#frequently-asked-questions
  - heading: Pulumi CrossGuard
    description: Enforce guardrails for security and compliance using policies in standard languages
    link: /docs/iac/crossguard/faq/
    primary_button_label: Get Started
    primary_button_link: /docs/iac/packages-and-automation/crossguard/get-started/
    secondary_button_label: Learn More
    secondary_button_link: /docs/iac/packages-and-automation/crossguard/core-concepts/
  - heading: Pulumi Deployments
    description: Automate deployment and operational workflows for cloud infrastructure
    link: /docs/pulumi-cloud/deployments/
    primary_button_label: Get Started
    primary_button_link: /docs/pulumi-cloud/deployments/get-started/
    secondary_button_label: Learn More
    secondary_button_link: /docs/pulumi-cloud/deployments/reference/
---