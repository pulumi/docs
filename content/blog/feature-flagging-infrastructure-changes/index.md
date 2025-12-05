---
title: "Feature Flagging for Your Infrastructure"
date: "2025-12-06"
meta_desc: Apply feature flagging to infrastructure with Pulumi. Control rollouts, reduce deployment risk, and automate updates using ESC or LaunchDarkly.
meta_image: Feature_Flags.png
authors: 
  - "elisabeth-lichtie"
tags: ["launchdarkly", "feature flags", "esc", "aws"]
schema_type: auto
social:
    linkedin:
---

One of Pulumi's foundational benefits is that it allows you to manage your [infrastructure as software](https://www.pulumi.com/what-is/what-is-infrastructure-as-software/) with rich programming languages, robust testing, and CI/CD patterns that you'd use with your application code. This post will cover applying another classic software development technique to your infrastructure: feature flagging. You can use feature flags to control change rollout, reduce the risk of new releases, and speed up the development of your infrastructure, the same way you do with your applications.

The examples in this post range from simply creating a flag and using it in a Lambda function to fully integrating with LaunchDarkly to build a comprehensive flagging system for your infrastructure.

<!--more-->

## Creating flags with Pulumi

{{% notes type="info" %}}
Check out the code here: [1 Flag Application With LaunchDarkly](https://github.com/Elisabeth-Team/feature-flagging/tree/main/01-flag-application-launchdarkly).
{{% /notes %}}

When you define flags in your infrastructure as code, you can configure them alongside all the supporting infrastructure your code needs. You can also encourage flag creation as a best practice in Pulumi components or templates.

With Pulumi, you can use [any Terraform provider](https://www.pulumi.com/docs/iac/concepts/resources/providers/#terraform-bridge-providers) to manage your feature flags, whether that's LaunchDarkly, Statsig, Split, Flagsmith, or any other feature flagging tool with Terraform support. This lets you define flags, targeting rules, and the infrastructure they control in a single codebase. The example uses the [LaunchDarkly provider](https://registry.terraform.io/providers/launchdarkly/launchdarkly/latest/docs) to create flags and supporting infrastructure:

```typescript
const flag = new launchdarkly.FeatureFlag("example-flag", {
  key: "exampleFlag",
  projectKey: "default",
  variationType: "boolean"
}, { provider });
```

The Lambda function evaluates the flag at runtime using the LaunchDarkly SDK key from environment variables, allowing you to toggle behavior without redeploying code.

## Using flags to control infrastructure

{{% notes type="info" %}}
Check out the code here: [2 Flaggable Infrastructure](https://github.com/Elisabeth-Team/feature-flagging/tree/main/02-flaggable-infra).
{{% /notes %}}

{{% notes type="warning" %}}
Before deploying this code, deploy either 03 (for [ESC Only](https://github.com/Elisabeth-Team/feature-flagging/tree/main/03-esc-with-webhook-for-updating)) or 04 (for [ESC and LaunchDarkly](https://github.com/Elisabeth-Team/feature-flagging/tree/main/04-flag-driven-infrastructure)) so that the environment is created and available.
{{% /notes %}}

Once you have flags defined, you can use them to control infrastructure provisioning. Apply the same best practices you would for application feature flags: keep flags focused, remove them when they're no longer needed, and document their purpose. In this example, a boolean flag controls whether internet-facing resources are created:

```typescript
const config = new pulumi.Config();
const flags: Record<string, any> | undefined = config.getObject("flags");
const enableInternetAccess = flags ? flags["enableInternetAccess"] : false;

if (enableInternetAccess) {
  // Create Internet Gateway, public subnet, route table, and routes
}
```

To enable automatic infrastructure updates when flags change (as shown in examples 3 and 4), configure [deployment settings](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/deploymentsettings/) in your stack. This requires:

1. The Pulumi GitHub App installed on your repository
1. Webhook configuration to trigger deployments when configuration values change

With these in place, changing a flag value automatically triggers a deployment.

## Configuring values with ESC

{{% notes type="info" %}}
Check out the code here: [3 ESC Auto-updating](https://github.com/Elisabeth-Team/feature-flagging/tree/main/03-esc-with-webhook-for-updating).
{{% /notes %}}

### Ingesting config from ESC

[Pulumi ESC](https://www.pulumi.com/docs/esc/) provides a centralized way to manage configuration and secrets. For teams that don't need the full feature set of a dedicated flagging service, you can store flag values directly in an ESC environment. Your infrastructure stack imports this environment and reads flag values at deployment time:

```typescript
const pulumiProv = new pulumiservice.Environment("flaggingEnv", {
  name: "config",
  organization: pulumi.getOrganization(),
  yaml: new pulumi.asset.StringAsset(`values:
  pulumiConfig:
    flags:
      enableInternetAccess: 'true'`),
});
```

This approach keeps all configuration in one place, eliminates dependencies on external services, and works seamlessly with Pulumi's existing stack configuration system. You can update flag values through the Pulumi CLI or Cloud console.

### Automatically triggering deployments with webhooks

{{% notes type="warning" %}}
There is some risk involved with automatically triggering updates. You can leave out the webhook and deploy manually if that's safer for your team.
{{% /notes %}}

Set up a [Pulumi Cloud webhook](https://www.pulumi.com/docs/pulumi-cloud/webhooks/) to automatically deploy infrastructure when ESC environment values change. The example creates an AWS Lambda function behind API Gateway that receives webhook events and triggers deployments via the Pulumi Deployments API:

```typescript
const webhook = new pulumiservice.Webhook("escEnvironmentWebhook", {
  organizationName: pulumi.getOrganization(),
  displayName: "ESC Environment Change Webhook",
  payloadUrl: api.apiEndpoint.apply((endpoint) => `${endpoint}/webhook`),
  active: true,
  filters: ["environment_revision_created"],
});
```

When you update a flag value in ESC, the webhook fires, the Lambda identifies which stacks use that environment, and triggers their redeployment. This creates a continuous delivery pipeline for infrastructure configuration changes.

## Ingesting flag values from LaunchDarkly

{{% notes type="info" %}}
Check out the code here: [4 LaunchDarkly Auto-updating](https://github.com/Elisabeth-Team/feature-flagging/tree/main/04-flag-driven-infrastructure).
{{% /notes %}}

### Ingesting flags from LaunchDarkly using ESC Connect

If your team already uses LaunchDarkly for application feature flags, you can integrate those same flags with your infrastructure using [ESC Connect](https://www.pulumi.com/docs/esc/integrations/dynamic-secrets/external/). This is also a good option if you need enterprise-level features like advanced targeting rules or percentage rollouts.

This approach unifies application and infrastructure flag management. The ESC environment uses `fn::open::external` to query a Lambda function that fetches current flag values from LaunchDarkly:

```yaml
values:
  pulumiConfig:
    flags: ${customSecrets.response}
  customSecrets:
    fn::open::external:
      url: ${getterUrl}
      request:
        secretName: ANY_SECRET
      secret: true
```

Your infrastructure code remains unchanged: it still imports the ESC environment and reads flag values the same way as in example 3. The difference is that flag values now come from LaunchDarkly, giving you access to advanced features like targeting rules, percentage rollouts, and flag scheduling.

### Automatically triggering deployments with webhooks

{{% notes type="warning" %}}
There is some risk involved with automatically triggering updates. You can leave out the webhook and deploy manually if that's safer for your team.
{{% /notes %}}

LaunchDarkly's webhook system can trigger infrastructure updates whenever a flag changes. Here's how the automation flow works:

```mermaid
graph LR
    A[Update Flag in LaunchDarkly] --> B[LaunchDarkly Webhook]
    B --> C[API Gateway]
    C --> D[Lambda Function]
    D --> E[Pulumi Deployments API]
    E --> F[Infrastructure Updates]
```

When the infrastructure deploys, it retrieves the current flag values through ESC:

```mermaid
graph LR
    A[Infrastructure Stack] --> B[ESC Environment]
    B --> C[fn::open::external]
    C --> D[Flag Getter Lambda]
    D --> E[LaunchDarkly SDK]
    E --> |Flag Value| D
    D --> |Flag Value| C
    C --> |Flag Value| B
    B --> |Flag Value| A
```

The Lambda function is configured as a webhook endpoint in LaunchDarkly:

```typescript
const launchDarklyWebhook = new LaunchDarklyWebhook("myWebhook", {
  pulumiProv: provCreation.pulumiEnv,
  flagKey: launchdarklyFlag.key,
  pulumiTokenSecret,
  lambdaRole,
}, { provider });
```

This creates a full automation loop: change a flag in LaunchDarkly's UI, and your infrastructure automatically updates to reflect the new value. This pattern works with any feature flagging service that supports webhooks.

## ESC Only vs ESC with LaunchDarkly

Both approaches enable automated infrastructure updates based on flag changes, but they suit different use cases:

| Aspect | ESC Only (Example 3) | ESC with LaunchDarkly (Example 4) |
|--------|---------------------|-----------------------------------|
| **Complexity** | Simpler setup with fewer moving parts | More components but unified with application flags |
| **Dependencies** | No external services required | Requires LaunchDarkly subscription |
| **Flag Management** | Edit via Pulumi CLI or Cloud console | Edit via LaunchDarkly UI with full feature set |
| **Advanced Features** | Basic flag storage, versioning, and approvals | Targeting rules, percentage rollouts, experiments, scheduling |
| **Best For** | Teams wanting simple config management | Teams already using LaunchDarkly or needing sophisticated flag controls |
| **Key Benefit** | Centralized Pulumi-native configuration | Unified management of application and infrastructure flags |
| **Example Use Case** | Toggle infrastructure features on/off | Coordinate UI button enablement with AWS SES infrastructure provisioning |

## Conclusion

Infrastructure deserves the same development practices as application code. Feature flags let you control rollouts, reduce deployment risk, and coordinate changes across your entire system, not just in your applications, but in the infrastructure that supports them.

Pulumi makes infrastructure feature flagging practical. Whether you choose the simplicity of ESC-only flag management or integrate with an enterprise service like LaunchDarkly, you can build infrastructure that responds dynamically to configuration changes while maintaining the same development practices you use for application code.
