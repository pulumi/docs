---
title: "Manage Cloud Visibility and Governance with Infrastructure as Code"
allow_long_title: true
date: 2026-01-26T09:00:00-08:00
draft: false
meta_desc: Discover cloud resources and enforce governance policies with new Pulumi Service Provider resources for visibility and compliance as code.
meta_image: meta.png
authors:
    - insights-team
tags:
    - features
    - pulumi-cloud
    - policy-as-code
---

Do you know what cloud resources are running in your environment right now? Many organizations struggle to maintain visibility across their cloud estate, especially for resources created outside of infrastructure as code. Without complete visibility, you can't enforce compliance, optimize costs, or identify security risks.

Today, we're excited to announce new resources in the [Pulumi Service Provider](/registry/packages/pulumiservice/) that solve this problem by enabling you to discover all cloud resources and enforce governance policies programmatically using infrastructure as code.

<!--more-->

With these new resources, you can:

- **Discover all cloud resources** across AWS, Azure, GCP, Kubernetes, or OCI environments, including resources not managed by Pulumi
- **Import discovered resources** into Pulumi management using [Visual Import](/docs/insights/discovery/visual-import/) to bring unmanaged infrastructure under IaC control
- **Enforce compliance at scale** by organizing resources into Policy Groups and applying policy packs
- **Automate governance workflows** by managing everything through code, enabling GitOps and CI/CD integration

## What's New

The Pulumi Service Provider now includes three new resources for managing cloud visibility and governance:

| Resource | Description |
|----------|-------------|
| `InsightsAccount` | Configures cloud provider scanning for resource discovery |
| `PolicyGroup` | Organizes stacks or cloud accounts for policy enforcement |
| `getPolicyPacks` / `getPolicyPack` | Data sources for querying available policy packs |

Let's explore each of these in detail.

## Insights Accounts: Discover Your Cloud Resources

An `InsightsAccount` connects Pulumi Cloud to your cloud provider, enabling automated scanning and discovery of all resources in your environment. This gives you complete visibility into your cloud estate, including resources that aren't managed by Pulumi.

### Key Features

- **Multi-cloud support**: Scan AWS, Azure, GCP, Kubernetes, and OCI environments
- **Scheduled scanning**: Configure daily automated scans or trigger them on-demand
- **Resource tagging**: Organize your accounts with custom tags

### Example: Creating an AWS Insights Account

{{< chooser language "yaml,typescript,python,go" >}}
{{% choosable language yaml %}}

```yaml
name: insights-example
runtime: yaml
resources:
  # ESC environment with AWS credentials
  aws-credentials:
    type: pulumiservice:Environment
    properties:
      organization: my-org
      project: insights
      name: aws-credentials
      yaml:
        fn::stringAsset: |
          values:
            aws:
              login:
                fn::open::aws-login:
                  oidc:
                    roleArn: arn:aws:iam::123456789012:role/PulumiInsightsRole
                    sessionName: pulumi-insights
            environmentVariables:
              AWS_REGION: us-west-2

  # Insights account for AWS scanning
  aws-insights:
    type: pulumiservice:InsightsAccount
    properties:
      organizationName: my-org
      accountName: production-aws
      provider: aws
      environment: insights/aws-credentials
      scanSchedule: daily
      providerConfig:
        regions:
          - us-west-2
          - us-east-1
      tags:
        environment: production
        team: platform
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as pulumiservice from "@pulumi/pulumiservice";

// ESC environment with AWS credentials
const awsCredentials = new pulumiservice.Environment("aws-credentials", {
    organization: "my-org",
    project: "insights",
    name: "aws-credentials",
    yaml: new pulumi.asset.StringAsset(`
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789012:role/PulumiInsightsRole
          sessionName: pulumi-insights
  environmentVariables:
    AWS_REGION: us-west-2
`),
});

// Insights account for AWS scanning
const awsInsights = new pulumiservice.InsightsAccount("aws-insights", {
    organizationName: "my-org",
    accountName: "production-aws",
    provider: "aws",
    environment: pulumi.interpolate`${awsCredentials.project}/${awsCredentials.name}`,
    scanSchedule: "daily",
    providerConfig: {
        regions: ["us-west-2", "us-east-1"],
    },
    tags: {
        environment: "production",
        team: "platform",
    },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_pulumiservice as pulumiservice

# ESC environment with AWS credentials
aws_credentials = pulumiservice.Environment("aws-credentials",
    organization="my-org",
    project="insights",
    name="aws-credentials",
    yaml=pulumi.StringAsset("""
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789012:role/PulumiInsightsRole
          sessionName: pulumi-insights
  environmentVariables:
    AWS_REGION: us-west-2
"""))

# Insights account for AWS scanning
aws_insights = pulumiservice.InsightsAccount("aws-insights",
    organization_name="my-org",
    account_name="production-aws",
    provider="aws",
    environment=pulumi.Output.concat(aws_credentials.project, "/", aws_credentials.name),
    scan_schedule="daily",
    provider_config={
        "regions": ["us-west-2", "us-east-1"],
    },
    tags={
        "environment": "production",
        "team": "platform",
    })
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-pulumiservice/sdk/go/pulumiservice"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// ESC environment with AWS credentials
		awsCredentials, err := pulumiservice.NewEnvironment(ctx, "aws-credentials", &pulumiservice.EnvironmentArgs{
			Organization: pulumi.String("my-org"),
			Project:      pulumi.String("insights"),
			Name:         pulumi.String("aws-credentials"),
			Yaml: pulumi.NewStringAsset(`
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789012:role/PulumiInsightsRole
          sessionName: pulumi-insights
  environmentVariables:
    AWS_REGION: us-west-2
`),
		})
		if err != nil {
			return err
		}

		// Insights account for AWS scanning
		_, err = pulumiservice.NewInsightsAccount(ctx, "aws-insights", &pulumiservice.InsightsAccountArgs{
			OrganizationName: pulumi.String("my-org"),
			AccountName:      pulumi.String("production-aws"),
			Provider:         pulumi.String("aws"),
			Environment: pulumi.Sprintf("%s/%s", awsCredentials.Project, awsCredentials.Name),
			ScanSchedule:     pulumi.String("daily"),
			ProviderConfig: pulumi.Map{
				"regions": pulumi.ToStringArray([]string{"us-west-2", "us-east-1"}),
			},
			Tags: pulumi.StringMap{
				"environment": pulumi.String("production"),
				"team":        pulumi.String("platform"),
			},
		})
		if err != nil {
			return err
		}

		return nil
	})
}
```

{{% /choosable %}}
{{% /chooser %}}

## Policy Groups: Enforce Compliance at Scale

A `PolicyGroup` lets you organize resources and apply policy packs for compliance enforcement. Policy Groups support two entity types: Stacks and Accounts.

You can configure policy groups in two modes:

- **Audit mode**: Reports policy violations without blocking operations. This supports both Stacks and Accounts.
- **Preventative mode**: Blocks operations that violate policies. This mode is only available for Stacks.

### Example: Stack-Based Policy Group

Apply compliance policies to your Pulumi stacks:

{{< chooser language "yaml,typescript" >}}
{{% choosable language yaml %}}

```yaml
name: policy-group-example
runtime: yaml
resources:
  production-policies:
    type: pulumiservice:PolicyGroup
    properties:
      name: production-compliance
      organizationName: my-org
      entityType: stacks
      mode: preventative
      stacks:
        - name: production
          routingProject: my-app
        - name: staging
          routingProject: my-app
      policyPacks:
        - name: cis-aws
          displayName: CIS AWS Foundations Benchmark
          version: 1
          versionTag: "1.5.0"
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumiservice from "@pulumi/pulumiservice";

const productionPolicies = new pulumiservice.PolicyGroup("production-policies", {
    name: "production-compliance",
    organizationName: "my-org",
    entityType: "stacks",
    mode: "preventative",
    stacks: [
        { name: "production", routingProject: "my-app" },
        { name: "staging", routingProject: "my-app" },
    ],
    policyPacks: [
        {
            name: "cis-aws",
            displayName: "CIS AWS Foundations Benchmark",
            version: 1,
            versionTag: "1.5.0",
        },
    ],
});
```

{{% /choosable %}}
{{% /chooser %}}

### Example: Account-Based Policy Group

Apply compliance policies to your cloud accounts for resource governance:

{{< chooser language "yaml,typescript" >}}
{{% choosable language yaml %}}

```yaml
name: insights-policy-group
runtime: yaml
resources:
  # Insights account
  aws-insights:
    type: pulumiservice:InsightsAccount
    properties:
      organizationName: my-org
      accountName: production-aws
      provider: aws
      environment: insights/aws-credentials

  # Policy group targeting the Insights account
  cloud-compliance:
    type: pulumiservice:PolicyGroup
    properties:
      name: cloud-resource-compliance
      organizationName: my-org
      entityType: accounts
      mode: audit
      accounts:
        - ${aws-insights.accountName}
      policyPacks:
        - name: aws-security-best-practices
          displayName: AWS Security Best Practices
          version: 2
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumiservice from "@pulumi/pulumiservice";

// Insights account
const awsInsights = new pulumiservice.InsightsAccount("aws-insights", {
    organizationName: "my-org",
    accountName: "production-aws",
    provider: "aws",
    environment: "insights/aws-credentials",
});

// Policy group targeting the Insights account
const cloudCompliance = new pulumiservice.PolicyGroup("cloud-compliance", {
    name: "cloud-resource-compliance",
    organizationName: "my-org",
    entityType: "accounts",
    mode: "audit",
    accounts: [awsInsights.accountName],
    policyPacks: [
        {
            name: "aws-security-best-practices",
            displayName: "AWS Security Best Practices",
            version: 2,
        },
    ],
});
```

{{% /choosable %}}
{{% /chooser %}}

## Querying Policy Packs

Use the `getPolicyPacks` and `getPolicyPack` data sources to discover available policy packs in your organization:

{{< chooser language "yaml,typescript" >}}
{{% choosable language yaml %}}

```yaml
name: policy-packs-query
runtime: yaml
variables:
  # List all available policy packs
  availablePacks:
    fn::invoke:
      function: pulumiservice:getPolicyPacks
      arguments:
        organizationName: my-org
      return: policyPacks

outputs:
  policyPacks: ${availablePacks}
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumiservice from "@pulumi/pulumiservice";

// List all available policy packs
const availablePacks = pulumiservice.getPolicyPacksOutput({
    organizationName: "my-org",
});

export const policyPacks = availablePacks.policyPacks;
```

{{% /choosable %}}
{{% /chooser %}}

## Getting Started

To start using these new resources:

**Update the Pulumi Service Provider** to the latest version:

{{< chooser language "typescript,python,go,csharp,yaml" >}}
{{% choosable language typescript %}}

```bash
npm install @pulumi/pulumiservice@latest
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
pip install --upgrade pulumi-pulumiservice
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
go get github.com/pulumi/pulumi-pulumiservice/sdk/go/pulumiservice@latest
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
dotnet add package Pulumi.PulumiService
```

{{% /choosable %}}
{{% choosable language yaml %}}

No package installation needed for YAML - just use the resources directly.

{{% /choosable %}}
{{% /chooser %}}

## Learn More

- [Pulumi Service Provider documentation](/registry/packages/pulumiservice/)
- [Pulumi Insights documentation](/docs/insights/)
- [Policy as Code documentation](/docs/insights/policy/)

We're excited to see how you use these new capabilities to improve visibility and governance across your cloud infrastructure. As always, we welcome your feedback in our [Community Slack](https://slack.pulumi.com/) or on [GitHub](https://github.com/pulumi/pulumi-pulumiservice).
