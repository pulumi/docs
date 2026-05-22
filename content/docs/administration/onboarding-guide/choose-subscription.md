---
title: Select the right model and subscription
meta_desc: Understanding your deployment options, subscription tiers, and support needs to help you choose the right approach for your organization.
aliases:
  - /docs/pulumi-cloud/get-started/onboarding-guide/choose-subscription/
  - /docs/deployments/get-started/onboarding-guide/choose-subscription/
weight: 1
menu:
    administration:
        name: Select the right model
        parent: pulumi-onboarding-guide
        identifier: select-a-model
---

Setting up your Pulumi Cloud account will lay the foundation for onboarding your team and enabling collaboration. Understanding your deployment options, subscription tiers, and support needs will help you choose the right approach for your organization.

## Choose your subscription tier

Your subscription tier determines the level of support, training, and features available to your team.

{{%notes type="info"%}}
Pulumi’s community has grown to hundreds of thousands of practitioners worldwide. Check out the [Pulumi Community](/community/) to connect!
{{%/notes%}}

### Individual and Team tiers

Perfect for smaller teams or getting started. Access community support through GitHub [Discussions](https://github.com/pulumi/pulumi/discussions) and [Issues](https://github.com/pulumi/pulumi/issues), [Community Slack](https://slack.pulumi.com), and free workshops.

You can also make use of the [Pulumi Neo](/product/neo/), detailed documentation in the [Pulumi Registry](/registry/), and the [examples repo](https://github.com/pulumi/examples) to help you get started.

### Enterprise and Business Critical tiers

Designed for larger organizations with mission-critical workloads. These tiers include:

- **Premium support**: 12x5 or 24x7 support is available with ticketing, guaranteed SLAs, and private Slack channels
- **Dedicated resources**: Personal account managers and architects to help solve complex problems
- **Priority access**: Prioritized bugs and feature requests, plus product roadmap reviews
- **Custom training**: Tailored onboarding and ongoing training for your team

Access your support through the [support portal](https://support.pulumi.com/hc/en-us) if you're on a premium plan.

{{% notes type="info" %}}
Learn more about the differences between [our subscription tiers](/pricing/).
{{% /notes %}}

{{% notes type="info" %}}
For hands-on engineering support, consider Pulumi Professional Services. Our team can help design and implement best practices, build custom providers and components, migrate existing infrastructure, and more. We offer standard packages and custom solutions. [Learn more about Professional Services](/proserv/).
{{% /notes %}}

## Choose your deployment model

Pulumi Cloud offers two deployment options, each designed for different organizational needs and security requirements.

### SaaS (Recommended for most organizations)

Choose Pulumi Cloud SaaS if you want the simplest setup with enterprise-grade reliability built in. You get high availability, disaster recovery, and geo-replication out of the box, plus security and compliance features detailed in the [Pulumi Cloud Security Whitepaper](/security/pulumi-cloud-security-whitepaper). Sign up at [pulumi.com](/) to get started.

### Self-hosted (For regulated or air-gapped environments)

{{% notes type="warning" %}}
Self-hosted Pulumi Cloud is only available for Business Critical customers.
{{% /notes %}}

Choose [self-hosted Pulumi Cloud](/product/self-hosted/) if you need complete control over your hosting environment. This is ideal for air-gapped environments or customers who require an isolated version of the Pulumi platform. You can deploy anywhere: on-premises, in your cloud account, or any infrastructure you control.

{{% notes type="info" %}}

To get started with self-hosted Pulumi Cloud, follow the [self-hosting infrastructure](/docs/administration/self-hosting/) guide. Because Pulumi Cloud isn't yet available to store state during the initial bootstrap process, you'll need a [DIY backend](/docs/iac/guides/basics/using-a-diy-backend/) to manage state for the deployment that stands up the platform.

{{% /notes %}}

## Choose your billing approach

Pulumi offers flexible billing options to match your organization's procurement preferences.

### Monthly billing

Pay monthly with a credit card. This option provides flexibility and is ideal for teams that want to start quickly or have variable usage patterns.

### Annual commitment pricing

Pay upfront with invoicing to access significant cost savings through commitment pricing. This option works well for organizations with predictable usage and established procurement processes. [Contact us](/contact/) to explore commitment pricing options.

{{% notes type="info" %}}
Both billing options include detailed usage insights through the Billing & usage page in your organization settings. Track IaC resources, deployment minutes, ESC secrets, and download usage history. Only organization administrators and designated [billing administrators](/docs/administration/organizations-teams/billing-managers/) can access these pages. You'll also receive monthly usage reports via email.
{{% /notes %}}

## Getting started with your chosen model

{{% notes type="info" %}}

If you are using a self-hosted installation of the Pulumi platform, the URLs used in the following documentation will need to be replaced with your instance's customer URLs.

{{% /notes %}}

### Create your account

Sign up using your email address and password, or connect with your GitHub, GitLab, or Atlassian identity at [app.pulumi.com/signup](https://app.pulumi.com/signup). After signup, you can configure SAML/SSO for team onboarding. Learn more about [account management](/docs/administration/organizations-teams/teams/).

### Explore the console

Access the Pulumi Cloud console through the "Sign In" link at [pulumi.com](/) or go directly to [app.pulumi.com](https://app.pulumi.com/signin). The dashboard provides useful content and links, while the left navigation gives you access to stacks, resources, and settings. Use the search function to find specific resources, and select the sparkle icon to access Pulumi Neo, your AI agent.

{{< get-started-stepper >}}
