---
title: "Feature Flagging Infrastructure Changes"
date: "2025-12-06"
meta_desc: Manage LaunchDarkly feature flags with Pulumi, add feature flags to manage your infrastructure, control and automatically update using ESC or LaunchDarkly!
meta_image: Feature_Flags.png
authors: 
  - "elisabeth-lichtie"
tags: ["launchdarkly", "feature flags", "esc", "aws"]
schema_type: auto
social:
    linkedin:
---

One of Pulumi's foundational benefits is that it allows you to manage your [infrastructure as software](https://www.pulumi.com/what-is/what-is-infrastructure-as-software/) with rich programming languages, verbose testing, and CI/CD patterns that you'd use with your application code. This post will cover applying another classic software development technique to your infrastructure: feature flagging. You can use feature flags to control change rollout, reduce the risk of new releases, and speed up the development of your infrastructure, the same way you do with your applications.

The examples in this post range from simply creating a flag and using it in a Lambda Function to fully integrating with LaunchDarkly to create a verbose flagging system for your infrastructure.

<!--more-->

## Creating flags with Pulumi

{{% notes type="info" %}}
Check out the code here: [1 Flag Application With LaunchDarkly](https://github.com/Elisabeth-Team/feature-flagging/tree/main/01-flag-application-launchdarkly).
{{% /notes %}}

Defining your flags in your infrastructure as code allows you to configure the flags and their rules with all the other supporting infrastructure for your code as well as encourage flag creation as a best practice in Pulumi Components or Templates.

TODO: talk a bit about the implementation: pulumi any terraform provider, configuring flags in code, and using flags in functions

## Creating infrastructure as code with flagging

{{% notes type="info" %}}
Check out the code here: [2 Flaggable Infrastructure](https://github.com/Elisabeth-Team/feature-flagging/tree/main/02-flaggable-infra).
{{% /notes %}}

{{% notes type="warning" %}}
Before deploying this code, you'll want to deploy either 03 (for [ESC Only](https://github.com/Elisabeth-Team/feature-flagging/tree/main/03-esc-with-webhook-for-updating)) or 04 (for [ESC and LaunchDarkly](https://github.com/Elisabeth-Team/feature-flagging/tree/main/04-flag-driven-infrastructure)) so that the environment is created and available.
{{% /notes %}}

TODO: talk about creating flaggable infrastructure, emphasize that you should generally follow flagging best practices, and that if you choose to automatically trigger updates on a flag or configuration change, you'll need to set deployment settings

## Configuring values with ESC

{{% notes type="info" %}}
Check out the code here: [3 ESC Auto-updating](https://github.com/Elisabeth-Team/feature-flagging/tree/main/03-esc-with-webhook-for-updating).
{{% /notes %}}

### Ingesting config from ESC

TODO: fill out this section with info about the implementation and its benefits

### Automatically triggering deployments with webhooks

{{% notes type="warning" %}}
There is some risk involved with automatically triggering updates. You can leave out the webhook and deploy manually if that's safer for your team.
{{% /notes %}}

TODO: fill out this section with info about the implementation and its benefits

## Ingesting flag values from LaunchDarkly

{{% notes type="info" %}}
Check out the code here: [4 LaunchDarkly Auto-updating](https://github.com/Elisabeth-Team/feature-flagging/tree/main/04-flag-driven-infrastructure).
{{% /notes %}}

### Ingesting flags from LaunchDarkly using ESC Connect

TODO: fill out this section with info about the implementation and its benefits. Mention that, as before, the code gets the value from its ESC environment

### Automatically triggering deployments with webhooks

{{% notes type="warning" %}}
There is some risk involved with automatically triggering updates. You can leave out the webhook and deploy manually if that's safer for your team.
{{% /notes %}}

TODO: fill out this section with info about the implementation and its benefits. Mention that this depends on you using a flagging system that has webhooks

## ESC Only vs ESC with LaunchDarkly

TODO: fill out this section. refer to the readme and mention that Launchdarkly has the benefit of managing your infra flags with your application flags for any changes that should go together (e.g. a button to send an email comes with the AWS SES configuration)

## Conclusion

TODO: fill out this section to nicely reemphasize core points
