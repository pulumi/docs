---
title: Select the right model and subscription
meta_desc: Understanding your deployment options, subscription tiers, and support needs to help you choose the right approach for your organization.
weight: 1
menu:
    cloud:
        name: Select the right model 
        parent: pulumi-onboarding-guide
        identifier: select-a-model
---

Setting up your Pulumi Cloud account will lay the foundation for onboarding your team and enabling collaboration. Understanding your deployment options, subscription tiers, and support needs will help you choose the right approach for your organization.

## Choose your subscription tier

Your subscription tier determines the level of support, training, and features available to your team.

{{%notes type="info"%}}
Pulumi’s community has grown to hundreds of thousands of practitioners worldwide. Check out the [Pulumi Community](https://www.pulumi.com/community/) to connect!
{{%/notes%}}

### Individual and Team tiers

Perfect for smaller teams or getting started. Access community support through GitHub [Discussions](https://github.com/pulumi/pulumi/discussions) and [Issues](https://github.com/pulumi/pulumi/issues), [Community Slack](https://slack.pulumi.com), and free workshops.

You can also make use of the [Pulumi AI](https://www.pulumi.com/ai), detailed documentation in the [Pulumi Registry](https://www.pulumi.com/registry/), and the [examples repo](https://github.com/pulumi/examples) to help you get started.

### Enterprise and Business Critical tiers

Designed for larger organizations with mission-critical workloads. These tiers include:

- **Premium support**: Choose between 12x5 or 24x7 support with ticketing, guaranteed SLAs, and private Slack channels
- **Dedicated resources**: Personal account managers and architects to help solve complex problems
- **Priority access**: Prioritized bugs and feature requests, plus product roadmap reviews
- **Custom training**: Tailored onboarding and ongoing training for your team

Access your support through the [support portal](https://support.pulumi.com/hc/en-us) if you're on a premium plan.

{{% notes type="info" %}}
Learn more about the differences between our subscription tiers [here](https://www.pulumi.com/pricing/)
{{% /notes %}}

{{% notes type="info" %}}
For hands-on engineering support, consider Pulumi Professional Services. Our team can help design and implement best practices, build custom providers and components, migrate existing infrastructure, and more. We offer standard packages and custom solutions. [Learn more about Professional Services](https://www.pulumi.com/proserv/).
{{% /notes %}}

## Choose your deployment model

Pulumi Cloud offers two deployment options, each designed for different organizational needs and security requirements.

### SaaS (Recommended for most organizations)

Choose Pulumi Cloud SaaS if you want the simplest setup with enterprise-grade reliability built in. You get high availability, disaster recovery, and geo-replication out of the box, plus security and compliance features detailed in the [Pulumi Cloud Security Whitepaper](https://www.pulumi.com/security/pulumi-cloud-security-whitepaper.pdf). Simply sign up at [pulumi.com](http://pulumi.com) to get started.

### Self-hosted (For regulated or air-gapped environments)

{{% notes type="warning" %}}
Self-hosted Pulumi Cloud is only available for Business Critical customers.
{{% /notes %}}

Choose [self-hosted Pulumi Cloud](https://www.pulumi.com/product/self-hosted/) if you need complete control over your hosting environment. This is ideal for air-gapped environments or highly regulated industries like FedRAMP. You can deploy anywhere: on-premises, in your cloud account, or any infrastructure you control.

## Choose your billing approach

Pulumi offers flexible billing options to match your organization's procurement preferences.

### Monthly billing

Pay monthly with a credit card. This option provides flexibility and is ideal for teams that want to start quickly or have variable usage patterns.

### Annual commitment pricing

Pay upfront with invoicing to access significant cost savings through commitment pricing. This option works well for organizations with predictable usage and established procurement processes. [Contact us](https://www.pulumi.com/contact/) to explore commitment pricing options.

{{% notes type="info" %}}
Both billing options include detailed usage insights through the Billing & usage page in your organization settings. Track IaC resources, deployment minutes, ESC secrets, and download usage history. Only organization administrators and designated [billing administrators](https://www.pulumi.com/docs/pulumi-cloud/access-management/billing-managers/) can access these pages. You'll also receive monthly usage reports via email.
{{% /notes %}}

## Getting started with your chosen model

{{% notes type="info" %}}
Before getting started with self-hosted, you'll need to set up your [state backend](https://www.pulumi.com/docs/iac/concepts/state-and-backends/#logging-into-the-aws-s3-backend) and [self-hosting infrastructure](https://www.pulumi.com/docs/pulumi-cloud/admin/self-hosted/)

As part of this process, you'll choose a custom URL that you'll use instead of app.pulumi.com
{{% /notes %}}

### Create your account

Sign up using your email address and password, or connect with your GitHub, GitLab, or Atlassian identity at [app.pulumi.com/signup](http://app.pulumi.com/signup). After signup, you can configure SAML/SSO for team onboarding. Learn more about [account management](https://www.pulumi.com/docs/pulumi-cloud/access-management/teams/).

### Explore the console

Access the Pulumi Cloud console through the "Sign In" link at [pulumi.com](http://pulumi.com) or go directly to [app.pulumi.com](http://app.pulumi.com). The dashboard provides useful content and links, while the left navigation gives you access to stacks, resources, and settings. Use the search function to find specific resources, and click the sparkle icon to access Pulumi Copilot, your AI assistant.

{{< get-started-stepper >}}
