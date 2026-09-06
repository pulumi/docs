---
title: "Best Infrastructure as Code (IaC) Tools for 2026"
title_tag: "Best Infrastructure as Code Tools in 2026"
date: 2026-07-05
updated: 2026-08-19
draft: false
meta_desc: "Compare 10 IaC tools for 2026 on pricing, licensing, release cadence, and AI-agent readiness: Pulumi, Terraform, OpenTofu, CDK, Bicep, and more."
authors:
    - asaf-ashirov
    - isaac-harris
tags:
    - infrastructure-as-code
    - terraform
    - aws
    - azure
    - google-cloud
    - kubernetes
    - devops
category: general
aliases:
    - /what-is/top-iac-tools/
faq_schema: true
itemlist_name: "Core Infrastructure as Code Tools"
itemlist:
    - name: "Pulumi IaC"
      url: "https://www.pulumi.com/"
    - name: "Terraform"
    - name: "AWS CDK"
    - name: "AWS CloudFormation"
    - name: "Azure Resource Manager (ARM)"
    - name: "Azure Bicep"
    - name: "Google Cloud Infrastructure Manager"
    - name: "Kubernetes YAML"
    - name: "Crossplane"
    - name: "OpenTofu"
---

The best infrastructure as code (IaC) tools in 2026 are Pulumi, Terraform, OpenTofu, AWS CDK, AWS CloudFormation, Azure ARM, Azure Bicep, Google Cloud Infrastructure Manager, Kubernetes YAML, and Crossplane. Each takes a different approach to defining and provisioning infrastructure, from general-purpose programming languages to declarative templates, and each carries distinct licensing, pricing, and AI-agent readiness tradeoffs worth weighing before you commit. As of August 2026, [Pulumi's own package registry](https://www.pulumi.com/registry/) lists more than 300 packages — first-party providers, bridged Terraform providers, and community components — illustrating how far multi-cloud coverage has expanded across the ecosystem.

<!--more-->

{{% hcl-note %}}

As infrastructure complexity grows, teams increasingly seek approaches that provide the same developer productivity tools they use for application development. While template-based and domain-specific language approaches serve many use cases effectively, teams with complex requirements or programming backgrounds often find that general-purpose programming languages offer advantages in testing, abstraction, and collaboration.

This comprehensive guide examines the most effective infrastructure as code tools available today, providing detailed analysis of core IaC platforms, complementary tools, and related technologies through the lens of software engineering best practices. Whether you're starting fresh with IaC or evaluating alternatives to overcome limitations in your current toolchain, we'll help you navigate this complex landscape and choose solutions that truly bring software engineering to infrastructure.

Ready to try one of these approaches yourself? [Get started with Pulumi for free](/docs/install/) and provision your first resource in minutes, or [see Pulumi Neo in action](/product/neo/) to explore how an AI agent can manage infrastructure changes alongside your team.

## What is Infrastructure as Code?

[Infrastructure as Code (IaC)](/what-is/what-is-infrastructure-as-code/) is an approach to automating the provisioning and management of infrastructure using software engineering principles, approaches, and tools. Rather than manually configuring servers, networks, and cloud resources through user interfaces or command-line tools, IaC enables you to define your entire infrastructure declaratively through code.

This approach brings the same benefits that have revolutionized software development—version control, automated testing, code reviews, and CI/CD pipelines—to infrastructure management.

## What Are Infrastructure as Code Tools?

Infrastructure as Code tools are platforms and frameworks that enable you to define, provision, and manage infrastructure resources through code rather than manual processes. These tools translate your infrastructure definitions into API calls that create, modify, or destroy cloud resources across various providers.

The most effective IaC tools share several key characteristics:

- **Goal-state focus**: Define your desired infrastructure outcome, whether through declarative syntax (like YAML/JSON templates) or imperative languages that express declarative intent
- **Multi-cloud support**: Work across different cloud providers and services
- **State management**: Track the current state of your infrastructure
- **Preview capabilities**: Show what changes will be made before applying them
- **Idempotency**: Safe to run multiple times with consistent results

## Why Infrastructure as Code Tools Are Essential

The shift to IaC tools addresses fundamental challenges that manual infrastructure management cannot solve at scale:

**Accelerates Deployment Velocity**: Teams can provision complex multi-cloud architectures in minutes instead of weeks. This speed enables faster time-to-market and more frequent, reliable deployments.

**Enables True Collaboration**: Infrastructure becomes code that teams can review, test, and approve together. This collaborative approach reduces errors and ensures knowledge sharing across the organization.

**Eliminates Configuration Drift**: Manual changes lead to inconsistencies between environments. IaC ensures your production, staging, and development environments remain identical, eliminating the notorious "works on my machine" syndrome for infrastructure.

**Provides Cost Control**: Automated provisioning and deprovisioning prevents resource sprawl. Teams can easily track infrastructure costs, set budget alerts, and optimize resource usage across environments.

**Ensures Compliance and Security**: Codified security policies and compliance requirements are automatically enforced across all deployments. Audit trails become automatic, and policy violations are caught before deployment.

**Guarantees Business Continuity**: Complete infrastructure definitions stored in version control enable rapid disaster recovery. Organizations can reconstruct entire environments from code, minimizing downtime and data loss.

## Infrastructure as Code Tools Overview

This guide covers the following infrastructure as code tools and platforms:

### 10 Most Used IaC Tools in 2026

1. **[Pulumi IaC](#1-pulumi)** - Modern IaC with general-purpose programming languages
2. **[Terraform](#2-terraform)** - BUSL-licensed IaC from HashiCorp that uses the HCL domain-specific language
3. **[AWS CDK](#3-aws-cloud-development-kit-cdk)** - Cloud Development Kit for AWS
4. **[AWS CloudFormation](#4-aws-cloudformation)** - Native AWS integration
5. **[Azure Resource Manager (ARM)](#5-azure-resource-manager-arm)** - Native Azure JSON templates
6. **[Azure Bicep](#6-azure-bicep)** - Azure-native domain-specific language that compiles to ARM
7. **[Google Cloud Infrastructure Manager](#7-google-cloud-infrastructure-manager)** - Terraform-based solution for Google Cloud
8. **[Kubernetes YAML](#8-kubernetes-yaml)** - Native Kubernetes resource definitions
9. **[Crossplane](#9-crossplane)** - Kubernetes as universal control plane
10. **[OpenTofu](#10-opentofu)** - Open-source Terraform alternative

### Configuration Management Tools  

- **[Chef](#chef)** - Configuration management and compliance automation
- **[Puppet](#puppet)** - Configuration management and compliance automation  
- **[Salt](#salt)** - Configuration management and remote execution

### Application and Platform Management Tools

- **[Kubernetes](#kubernetes-container-orchestration-platform)** - Container orchestration platform

### Security and Compliance Tools

- **[Pulumi ESC](#pulumi-esc)** - Configuration and secrets management platform
- **[Pulumi Insights](#pulumi-insights)** - Cloud resource search, analytics, and compliance platform
- **[Snyk](#security-scanning-tools)** - Developer security platform with IaC scanning
- **[Wiz](#security-scanning-tools)** - Comprehensive cloud security platform
- **[HashiCorp Sentinel](#security-scanning-tools)** - Policy-as-code framework for Terraform
- **[Checkov](#security-scanning-tools)** - Static analysis for IaC security
- **[TFLint](#linting-and-validation-tools)** - Terraform linting and validation

### Infrastructure Automation and Management Platforms

- **[Pulumi Cloud](#iac-automation-platforms)** - Managed service for Pulumi IaC with enterprise features
- **[HashiCorp Cloud Platform](#iac-automation-platforms)** - Enterprise SaaS platform for Terraform management and automation
- **[Spacelift](#iac-automation-platforms)** - Automation platform for IaC workflows (not an IaC tool itself)
- **[Env0](#iac-automation-platforms)** - Governance and automation platform for existing IaC tools

## Core Infrastructure as Code Tools

Here's how the core IaC tools compare at a glance before we go deep on each one:

| Tool | Language / approach | Clouds supported | License | Latest stable release (Aug 2026) | Best for |
|---|---|---|---|---|---|
| [Pulumi](#1-pulumi) | Python, TypeScript, JavaScript, Go, .NET, Java, YAML, or HCL | AWS, Azure, Google Cloud, Kubernetes, and 170+ other providers | Apache-2.0 | v3.259.0 (2026-08-19) | Teams who want flexible, language-agnostic IaC for infrastructure and operations |
| [Terraform](#2-terraform) | HCL (HashiCorp's DSL) | AWS, Azure, Google Cloud, and hundreds of community providers | BUSL-1.1 | v1.15.9 (2026-08-19) | Teams with existing Terraform expertise and established workflows |
| [AWS CDK](#3-aws-cloud-development-kit-cdk) | TypeScript, Python, Java, C#, Go (compiles to CloudFormation) | AWS only | Apache-2.0 | v2.266.0 (2026-08-19) | AWS-focused teams who prefer programming languages over templates |
| [AWS CloudFormation](#4-aws-cloudformation) | JSON/YAML templates | AWS only | Proprietary (managed service) | Continuously updated by AWS | AWS-only deployments requiring deep service integration |
| [Azure ARM](#5-azure-resource-manager-arm) | JSON templates | Azure only | Proprietary (managed service) | Continuously updated by Microsoft | Azure-native deployments requiring comprehensive platform integration |
| [Azure Bicep](#6-azure-bicep) | Bicep DSL (compiles to ARM JSON) | Azure only | MIT | v0.46.1 (2026-07-30) | Azure deployments requiring improved readability and developer experience |
| [Google Cloud Infrastructure Manager](#7-google-cloud-infrastructure-manager) | HCL (Terraform-based) | Google Cloud | Proprietary (managed service) | Continuously updated by Google | Google Cloud Platform deployments using Terraform |
| [Kubernetes YAML](#8-kubernetes-yaml) | YAML manifests | Any Kubernetes cluster | Apache-2.0 | v1.36.4 (2026-08-20) | Teams managing container-native applications and cloud-native infrastructure |
| [Crossplane](#9-crossplane) | YAML / Kubernetes CRDs | Multi-cloud, orchestrated through Kubernetes | Apache-2.0 | v2.4.0 (2026-08-20) | Kubernetes-first organizations managing multi-cloud infrastructure |
| [OpenTofu](#10-opentofu) | HCL (community-governed Terraform fork) | AWS, Azure, Google Cloud, and the Terraform provider ecosystem | MPL-2.0 | v1.12.6 (2026-08-19) | Teams seeking an open-source Terraform alternative with community governance |

Use the table as a map: each tool links to its full breakdown below, where you'll find licensing, key features, and the tradeoffs behind each "best for." Version and release-date figures were checked against each project's GitHub releases on 2026-08-22.

### Pricing at a glance

Tool cost is rarely the license alone. Here's what each option actually costs to run, based on published pricing as of August 2026:

| Tool | Free tier | Entry paid tier | Enterprise / top tier |
|---|---|---|---|
| Pulumi | Individual: free forever, 1 user, unlimited stacks, 500 workflow min/mo, 5M Pulumi Neo tokens/mo | Team: from $40/mo (≈40 credits, up to 10 users) | Enterprise from $400/mo; Business Critical (custom) |
| Terraform (HCP Terraform) | Free up to 500 managed resources, 1 concurrent run | Essentials: $0.10/resource/mo | Standard $0.47/resource/mo; Premium $0.99/resource/mo; self-hosted Terraform Enterprise (custom) |
| AWS CDK | No tool fee — free and open source | N/A | N/A (pay only for provisioned AWS resources) |
| AWS CloudFormation | No tool fee — included with AWS | N/A | N/A (pay only for provisioned AWS resources) |
| Azure ARM | No tool fee — included with Azure | N/A | N/A (pay only for provisioned Azure resources) |
| Azure Bicep | No tool fee — free and open source | N/A | N/A (pay only for provisioned Azure resources) |
| Google Cloud Infrastructure Manager | No tool fee — included with Google Cloud | N/A | N/A (pay only for provisioned Google Cloud resources) |
| Kubernetes YAML | Free and open source | N/A (cluster infra costs apply) | N/A |
| Crossplane | Free and open source | N/A (cluster infra costs apply) | N/A |
| OpenTofu | Free and open source | N/A | N/A |

Spacelift and env0, two managed CI/CD layers frequently compared against these core tools, publish their own tiers but denominate them differently — per-seat and per-worker rather than per-resource — with quote-based pricing at the top end. Check their pricing pages directly, since the figures change often and don't map cleanly onto the table above.

### License, governance, and release cadence

For teams weighing long-term risk, licensing model and governance matter as much as features. This is the reference table competitors rarely publish in one place:

| Tool | License | Governing body | Latest version | Released | GitHub stars |
|---|---|---|---|---|---|
| Pulumi | Apache-2.0 | Pulumi Corporation | v3.259.0 | 2026-08-19 | ~25.6k |
| Terraform | BUSL-1.1 (not OSI-approved) | HashiCorp (an IBM company) | v1.15.9 | 2026-08-19 | ~49.5k |
| AWS CDK | Apache-2.0 | AWS | v2.266.0 | 2026-08-19 | ~12.9k |
| AWS CloudFormation | Proprietary | AWS | Managed service | Continuous | N/A |
| Azure ARM | Proprietary | Microsoft | Managed service | Continuous | N/A |
| Azure Bicep | MIT | Microsoft | v0.46.1 | 2026-07-30 | ~3.6k |
| Google Cloud Infrastructure Manager | Proprietary | Google Cloud | Managed service | Continuous | N/A |
| Kubernetes | Apache-2.0 | CNCF | v1.36.4 | 2026-08-20 | ~124.9k |
| Crossplane | Apache-2.0 | CNCF | v2.4.0 | 2026-08-20 | ~12.0k |
| OpenTofu | MPL-2.0 | Linux Foundation | v1.12.6 | 2026-08-19 | ~29.9k |

Terraform's move to the Business Source License in 2023 is the reason OpenTofu exists at all: OpenTofu forked from Terraform's last MPL-2.0 release and now operates under Linux Foundation governance, which is the deciding factor for teams that require an OSI-approved license.

### Which IaC tool fits your situation?

If you're short on time, start here:

| Your situation | Recommended tool | Why |
|---|---|---|
| You want one language across every cloud, plus native testing and packages | Pulumi | Real programming languages (Python, TypeScript, Go, C#, Java) with unit tests, IDE support, and 170+ providers |
| You have deep existing Terraform/HCL expertise and workflows | Terraform | Largest ecosystem and community knowledge base, despite the BUSL-1.1 licensing tradeoff |
| You need an open-source, community-governed Terraform-compatible tool | OpenTofu | MPL-2.0, Linux Foundation governance, high HCL compatibility |
| You're AWS-only and want programming languages instead of templates | AWS CDK | Compiles to CloudFormation, so it inherits native AWS support with a real language on top |
| You're AWS-only and want a fully managed, zero-tooling option | AWS CloudFormation | No separate tool to install or license; deepest AWS service coverage |
| You're Azure-only and want better readability than raw ARM JSON | Azure Bicep | MIT-licensed DSL that compiles to ARM, with a much better authoring experience |
| You're Kubernetes-first and want infrastructure managed via CRDs | Crossplane | Extends the Kubernetes control plane to manage cloud infrastructure declaratively |
| You're deploying AI agents to manage infrastructure changes | Pulumi | Real languages give agents testable, reviewable code to reason about, rather than HCL diffs, which are harder for an agent to test against — see [Pulumi Neo](/product/neo/) |

### 1. Pulumi

License: Apache-2.0  
Latest stable release: v3.259.0 (2026-08-19)  
Best For: Teams who want flexible, language-agnostic IaC for infrastructure and operations

Pulumi IaC represents a modern approach to infrastructure as code, fundamentally changing how teams approach infrastructure by enabling the use of general-purpose programming languages like Python, TypeScript, JavaScript, Go, .NET, and Java, plus YAML and HCL for simpler configurations. Unlike tools that force teams to learn proprietary domain-specific languages (DSLs), Pulumi leverages familiar languages and software engineering practices, providing unprecedented flexibility, powerful abstractions, and seamless integration with existing development workflows.

Pulumi's approach combines the best of both imperative and declarative paradigms: you use imperative programming languages to define your desired infrastructure state, but the Pulumi engine processes this declaratively to determine what changes are needed to achieve your intended outcome.

### Key Features:

- **Universal language support**: Use Python, TypeScript, JavaScript, Go, .NET, Java, YAML, or HCL configurations—no new DSL to learn
- **Any cloud, any architecture**: Deploy to AWS, Azure, Google Cloud, Kubernetes, and 170+ other providers
- **Real programming constructs**: Leverage loops, conditionals, functions, classes, packages, and third-party libraries
- **Superior developer experience**: Full IDE support with IntelliSense, debugging, and refactoring
- **Built-in testing**: [Unit and integration testing](/docs/iac/guides/testing/) for infrastructure code
- **Policy as Code**: Enforce compliance and security policies with [CrossGuard](/docs/insights/policy/)
- **Component ecosystem**: Rich library of reusable infrastructure components

Universal Language Code Examples:

{{< chooser language "typescript,python,go,csharp,yaml" />}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Create a VPC with automatic subnets
const vpc = new awsx.ec2.Vpc("main-vpc", {
    cidrBlock: "10.0.0.0/16",
    numberOfAvailabilityZones: 2,
});

// Create an ECS cluster
const cluster = new aws.ecs.Cluster("app-cluster");

// Create an Application Load Balancer
const alb = new awsx.elasticloadbalancingv2.ApplicationLoadBalancer("app-alb", {
    vpcId: vpc.vpcId,
    subnetIds: vpc.publicSubnetIds,
});

// Deploy a containerized application
const service = new awsx.ecs.FargateService("app-service", {
    cluster: cluster.arn,
    taskDefinitionArgs: {
        container: {
            image: "nginx:latest",
            memory: 128,
            ports: [{
                containerPort: 80,
                targetGroup: alb.defaultTargetGroup,
            }],
        },
    },
});

export const vpcId = vpc.vpcId;
export const serviceUrl = alb.loadBalancer.dnsName;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx

# Create a VPC with automatic subnets
vpc = awsx.ec2.Vpc("main-vpc",
    cidr_block="10.0.0.0/16",
    number_of_availability_zones=2)

# Create an ECS cluster
cluster = aws.ecs.Cluster("app-cluster")

# Create an Application Load Balancer
alb = awsx.elasticloadbalancingv2.ApplicationLoadBalancer("app-alb",
    vpc_id=vpc.vpc_id,
    subnet_ids=vpc.public_subnet_ids)

# Deploy a containerized application
service = awsx.ecs.FargateService("app-service",
    cluster=cluster.arn,
    task_definition_args=awsx.ecs.FargateServiceTaskDefinitionArgs(
        container=awsx.ecs.TaskDefinitionContainerDefinitionArgs(
            image="nginx:latest",
            memory=128,
            ports=[awsx.ecs.TaskDefinitionPortMappingArgs(
                container_port=80,
                target_group=alb.default_target_group
            )]
        )
    ))

pulumi.export("vpc_id", vpc.vpc_id)
pulumi.export("service_url", alb.load_balancer.dns_name)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ecs"
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ec2"
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/elasticloadbalancingv2"
	awsxecs "github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ecs"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create a VPC with automatic subnets
		vpc, err := ec2.NewVpc(ctx, "main-vpc", &ec2.VpcArgs{
			CidrBlock:                pulumi.String("10.0.0.0/16"),
			NumberOfAvailabilityZones: pulumi.Int(2),
		})
		if err != nil {
			return err
		}

		// Create an ECS cluster
		cluster, err := ecs.NewCluster(ctx, "app-cluster", nil)
		if err != nil {
			return err
		}

		// Create an Application Load Balancer
		alb, err := elasticloadbalancingv2.NewApplicationLoadBalancer(ctx, "app-alb", &elasticloadbalancingv2.ApplicationLoadBalancerArgs{
			VpcId:     vpc.VpcId,
			SubnetIds: vpc.PublicSubnetIds,
		})
		if err != nil {
			return err
		}

		// Deploy a containerized application
		_, err = awsxecs.NewFargateService(ctx, "app-service", &awsxecs.FargateServiceArgs{
			Cluster: cluster.Arn,
			TaskDefinitionArgs: &awsxecs.FargateServiceTaskDefinitionArgs{
				Container: &awsxecs.TaskDefinitionContainerDefinitionArgs{
					Image:  pulumi.String("nginx:latest"),
					Memory: pulumi.Int(128),
					Ports: awsxecs.TaskDefinitionPortMappingArray{
						&awsxecs.TaskDefinitionPortMappingArgs{
							ContainerPort: pulumi.Int(80),
							TargetGroup:   alb.DefaultTargetGroup,
						},
					},
				},
			},
		})
		if err != nil {
			return err
		}

		ctx.Export("vpcId", vpc.VpcId)
		ctx.Export("serviceUrl", alb.LoadBalancer.DnsName())
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Aws = Pulumi.Aws;
using Awsx = Pulumi.Awsx;

return await Deployment.RunAsync(() =>
{
    // Create a VPC with automatic subnets
    var vpc = new Awsx.Ec2.Vpc("main-vpc", new()
    {
        CidrBlock = "10.0.0.0/16",
        NumberOfAvailabilityZones = 2,
    });

    // Create an ECS cluster
    var cluster = new Aws.Ecs.Cluster("app-cluster");

    // Create an Application Load Balancer
    var alb = new Awsx.ElasticLoadBalancingV2.ApplicationLoadBalancer("app-alb", new()
    {
        VpcId = vpc.VpcId,
        SubnetIds = vpc.PublicSubnetIds,
    });

    // Deploy a containerized application
    var service = new Awsx.Ecs.FargateService("app-service", new()
    {
        Cluster = cluster.Arn,
        TaskDefinitionArgs = new Awsx.Ecs.Inputs.FargateServiceTaskDefinitionArgs
        {
            Container = new Awsx.Ecs.Inputs.TaskDefinitionContainerDefinitionArgs
            {
                Image = "nginx:latest",
                Memory = 128,
                Ports = new[]
                {
                    new Awsx.Ecs.Inputs.TaskDefinitionPortMappingArgs
                    {
                        ContainerPort = 80,
                        TargetGroup = alb.DefaultTargetGroup,
                    },
                },
            },
        },
    });

    return new Dictionary<string, object?>
    {
        ["vpcId"] = vpc.VpcId,
        ["serviceUrl"] = alb.LoadBalancer.Apply(lb => lb.DnsName),
    };
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: aws-ecs-example
runtime: yaml
description: An example that deploys an ECS Fargate service with load balancer

resources:
  # Create a VPC with automatic subnets
  main-vpc:
    type: awsx:ec2:Vpc
    properties:
      cidrBlock: "10.0.0.0/16"
      numberOfAvailabilityZones: 2

  # Create an ECS cluster
  app-cluster:
    type: aws:ecs:Cluster

  # Create an Application Load Balancer
  app-alb:
    type: awsx:elasticloadbalancingv2:ApplicationLoadBalancer
    properties:
      vpcId: ${main-vpc.vpcId}
      subnetIds: ${main-vpc.publicSubnetIds}

  # Deploy a containerized application
  app-service:
    type: awsx:ecs:FargateService
    properties:
      cluster: ${app-cluster.arn}
      taskDefinitionArgs:
        container:
          image: "nginx:latest"
          memory: 128
          ports:
            - containerPort: 80
              targetGroup: ${app-alb.defaultTargetGroup}

outputs:
  vpcId: ${main-vpc.vpcId}
  serviceUrl: ${app-alb.loadBalancer.dnsName}
```

{{% /choosable %}}

Key Features:

- **General-purpose language support**: Use Python, TypeScript, JavaScript, Go, .NET, Java, YAML, or HCL without learning new DSLs
- **Software engineering practices**: Full IDE support, comprehensive testing frameworks, debugging capabilities
- **Multi-cloud flexibility**: [170+ providers](/registry/), with native AWS, Azure, Google Cloud, and Kubernetes providers offering same-day access to new cloud features
- **Incremental adoption**: Migration tools and state integration for gradual transitions
- **Open source licensing**: Apache 2.0 ensures long-term freedom and flexibility

> "We use Pulumi widely at Wiz. It enabled our product to support multi-cloud and to scale quickly — scaling and driving hundreds of thousands of infrastructure updates every day."
>
> — Yarin Miran, Senior Software Engineer, [Wiz](https://www.pulumi.com/case-studies/wiz/)

Considerations:

- **Learning curve**: Teams new to programming may prefer template-based approaches initially
- **Ecosystem maturity**: Smaller community compared to more established tools like Terraform
- **Tool complexity**: Advanced features may require more setup than simpler template systems

Organizations moving to programming-language-based IaC report deployment-time reductions ranging from roughly 70% to 99% — SANS at 70%, Unity at 80%, and Starburst at 99% (two weeks down to about three hours). These improvements typically occur when transitioning from manual processes or basic template systems to automated approaches with comprehensive testing, IDE integration, and code reusability. Results vary based on starting point, team expertise, infrastructure complexity, and specific use cases.

> **Ready to get started?** [Experience Pulumi's programming language approach](/docs/get-started/) and see how familiar languages can transform your infrastructure management with comprehensive testing, powerful abstractions, and seamless multi-cloud support.

### 2. Terraform

License: Business Source License (BUSL-1.1), not OSI-approved  
Latest stable release: v1.15.9 (2026-08-19)  
Best For: Teams with existing Terraform expertise and established workflows

[Terraform](/docs/iac/comparisons/terraform/) uses HashiCorp Configuration Language (HCL) to define infrastructure across multiple cloud providers. However, its 2023 licensing change to BUSL-1.1 (no longer open source) and inherent limitations with domain-specific languages create challenges for teams requiring advanced software engineering practices.

Key Features:

- **Extensive provider ecosystem**: Largest collection of community-maintained providers covering virtually every cloud service
- **Established workflows**: Mature plan-and-apply process with extensive tooling and CI/CD integrations
- **Community and resources**: Vast ecosystem of modules, extensive documentation, training materials, and community support
- **Enterprise adoption**: Widely adopted in enterprises with established processes and expertise
- **Module ecosystem**: Rich collection of reusable Terraform modules for common patterns

When Terraform Works Well:

- Teams with existing HCL expertise and Terraform investments
- Infrastructure patterns that fit well within HCL's declarative model
- Teams comfortable with template-based approaches

Considerations for Complex Scenarios:

- **Language constraints**: HCL's domain-specific nature can require workarounds for complex logic compared to general-purpose programming languages
- **Testing approach**: Primarily supports integration testing; teams needing comprehensive unit testing may require additional tooling
- **IDE experience**: While improving, HCL tooling provides less comprehensive support than mature programming language ecosystems
- **State management**: Requires manual backend configuration and locking setup for team collaboration

Code Example:

```hcl
data "aws_availability_zones" "available" {}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "main-vpc"
  }
}

resource "aws_subnet" "public" {
  count             = 2
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.${count.index + 1}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]

  tags = {
    Name = "public-subnet-${count.index + 1}"
  }
}
```

### 3. AWS Cloud Development Kit (CDK)

License: Apache-2.0  
Latest stable release: v2.266.0 (2026-08-19)  
Best For: AWS-focused teams who prefer programming languages over templates

AWS CDK allows you to define AWS infrastructure using familiar programming languages, synthesizing CloudFormation templates for deployment while providing higher-level abstractions. CDK addresses many limitations of traditional template-based approaches by enabling general-purpose programming languages.

Key Features:

- **General-purpose programming languages**: TypeScript, Python, Java, C#, JavaScript, and Go with full IDE integration
- **AWS-optimized constructs**: High-level components encapsulating AWS best practices
- **Type safety**: Compile-time checking and IntelliSense support
- **CloudFormation reliability**: Built on AWS's proven deployment engine

Notable Limitations:

- **AWS-only ecosystem**: Locked into single cloud provider, limiting multi-cloud strategies
- **CloudFormation constraints**: Inherits template size limits and deployment restrictions
- **Vendor lock-in**: Deep AWS integration makes migration to other clouds challenging
- **Limited cross-cloud consistency**: Teams need different tools and approaches for multi-cloud deployments

CDK represents a significant improvement over CloudFormation templates but constrains organizations to AWS-only infrastructure strategies.

Code Example:

```typescript
import * as cdk from 'aws-cdk-lib';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as ecs from 'aws-cdk-lib/aws-ecs';
import { Construct } from 'constructs';

export class MyStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = new ec2.Vpc(this, 'MyVpc', {
      maxAzs: 2
    });

    const cluster = new ecs.Cluster(this, 'MyCluster', {
      vpc: vpc
    });

    const taskDefinition = new ecs.FargateTaskDefinition(this, 'TaskDef', {
      memoryLimitMiB: 512,
      cpu: 256
    });

    taskDefinition.addContainer('web', {
      image: ecs.ContainerImage.fromRegistry('nginx:latest'),
      portMappings: [{ containerPort: 80 }]
    });

    new ecs.FargateService(this, 'MyService', {
      cluster: cluster,
      taskDefinition: taskDefinition
    });
  }
}
```

### 4. AWS CloudFormation

License: Proprietary (AWS Service)  
Best For: AWS-only deployments requiring deep service integration

AWS CloudFormation provides the foundation for infrastructure as code on AWS, offering native integration with all AWS services and deep platform-specific features.

Pulumi Integration: Pulumi provides [native AWS providers](/docs/integrations/clouds/aws/) that offer the same comprehensive AWS service coverage as CloudFormation, with the added benefit of using general-purpose programming languages. You can also [import existing CloudFormation stacks](/docs/iac/guides/migration/import/) into Pulumi for gradual migration or hybrid management approaches.

Key Features:

- **AWS-native**: First-party support for all AWS services
- **JSON/YAML templates**: Declarative resource definitions
- **Stack management**: Organized resource grouping and lifecycle management
- **Change sets**: Preview infrastructure changes before deployment
- **Service integration**: Deep integration with other AWS services

Code Example:

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsHostnames: true
      Tags:
        - Key: Name
          Value: MyVPC

  MySubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref MyVPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone: !Select [0, !GetAZs '']
```

### 5. Azure Resource Manager (ARM)

License: Proprietary (Microsoft Service)  
Best For: Azure-native deployments requiring comprehensive platform integration

Azure Resource Manager provides the foundational infrastructure as code solution for Microsoft Azure, offering complete support for Azure services through JSON-based ARM templates. As Azure's native IaC solution, ARM templates provide the most comprehensive coverage of Azure services and features.

Pulumi Integration: Pulumi's [native Azure providers](/docs/integrations/clouds/azure/) offer equivalent comprehensive Azure service coverage with general-purpose programming languages. ARM templates can be [imported into Pulumi](/docs/iac/guides/migration/import/), and you can reference ARM deployments from Pulumi programs for hybrid scenarios.

Key Features:

- **Azure-native**: Complete Azure service coverage with first-party support
- **JSON templates**: Declarative resource definitions in JSON format
- **Resource groups**: Logical organization of related resources
- **Deployment modes**: Complete or incremental deployment options
- **Comprehensive integration**: Deep integration with Azure services and features

Code Example:

```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "resources": [
    {
      "type": "Microsoft.Storage/storageAccounts",
      "apiVersion": "2023-01-01",
      "name": "mystorageaccount",
      "location": "[resourceGroup().location]",
      "sku": {
        "name": "Standard_LRS"
      },
      "kind": "StorageV2"
    }
  ]
}
```

## Cloud-Native and Community Declarative Tools

The remaining five tools take a more declarative, cloud- or platform-native approach: four are scoped to a single cloud or a single control plane, and OpenTofu is the exception as a general-purpose, multi-cloud Terraform fork included here for its shared declarative, community-governed lineage. Each trades some of the flexibility of a general-purpose language for tighter integration with the platform it targets, or in OpenTofu's case, for open governance over a widely adopted DSL.

### 6. Azure Bicep

License: MIT  
Latest stable release: v0.46.1 (2026-07-30)  
Best For: Azure deployments requiring improved readability and developer experience

Azure Bicep is a domain-specific language (DSL) that simplifies Azure Resource Manager template authoring. Bicep files compile transparently to ARM templates, providing all the capabilities of ARM with significantly improved syntax and developer experience.

Key Features:

- **Simplified syntax**: Clean, readable syntax compared to JSON ARM templates
- **ARM compilation**: Compiles to ARM templates for deployment, ensuring full compatibility
- **Type safety**: Strong typing and IntelliSense support in development environments
- **Modular design**: Support for modules and code reuse across projects
- **Azure-native**: Complete Azure service coverage through ARM template compilation

Code Example:

```bicep
@description('Storage Account type')
@allowed([
  'Standard_LRS'
  'Standard_GRS'
  'Standard_ZRS'
  'Premium_LRS'
])
param storageAccountType string = 'Standard_LRS'

@description('Location for the storage account.')
param location string = resourceGroup().location

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'mystorageaccount'
  location: location
  sku: {
    name: storageAccountType
  }
  kind: 'StorageV2'
  properties: {}
}
```

### 7. Google Cloud Infrastructure Manager

License: Proprietary (Google Service)  
Best For: Google Cloud Platform deployments using Terraform

Google Cloud Infrastructure Manager automates the deployment and management of Google Cloud infrastructure resources using Terraform configurations, representing Google's modern approach to infrastructure as code. Infrastructure Manager replaces Google Cloud Deployment Manager, which reached end of support on December 31, 2025.

Key Features:

- **Terraform-based**: Uses standard Terraform configurations declaratively
- **Automated workflows**: Handles Terraform init, validate, and apply operations
- **Version control integration**: Supports Git repositories and Cloud Storage
- **Deployment tracking**: Comprehensive metadata storage and logging
- **Multiple Terraform versions**: Flexibility in Terraform version selection
- **Cloud Build integration**: Leverages Google Cloud Build for execution environment
- **Migration path**: Provides upgrade path from legacy Cloud Deployment Manager

Code Example:

```hcl
# main.tf - Terraform configuration for Infrastructure Manager
resource "google_compute_instance" "vm_instance" {
  name         = "my-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {
      // Ephemeral public IP
    }
  }

  metadata = {
    startup-script = "echo Hello from Infrastructure Manager!"
  }
}

output "instance_ip" {
  value = google_compute_instance.vm_instance.network_interface[0].access_config[0].nat_ip
}
```

### 8. Kubernetes YAML

License: Apache-2.0  
Latest stable release: Kubernetes v1.36.4 (2026-08-20)  
Best For: Teams managing container-native applications and cloud-native infrastructure

Kubernetes YAML manifests represent one of the most widely adopted forms of infrastructure as code, enabling teams to define, version, and manage containerized applications and their supporting infrastructure through declarative configuration files.

Key Features:

- **Declarative configuration**: Define desired state through human-readable YAML files
- **Native Kubernetes integration**: Direct integration with Kubernetes API without additional tools
- **GitOps compatibility**: Version control YAML files for automated deployment workflows
- **Resource relationships**: Define dependencies and relationships between Kubernetes resources
- **Extensive ecosystem**: Rich ecosystem of operators and custom resources extending functionality

Code Example:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
  labels:
    app: web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: web-app
        image: nginx:1.27
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"
---
apiVersion: v1
kind: Service
metadata:
  name: web-app-service
spec:
  selector:
    app: web-app
  ports:
  - port: 80
    targetPort: 80
  type: LoadBalancer
```

### 9. Crossplane

License: Apache-2.0  
Latest stable release: v2.4.0 (2026-08-20)  
Best For: Kubernetes-first organizations managing multi-cloud infrastructure

Crossplane is a Cloud-Native Framework for Platform Engineering that extends Kubernetes to help organizations build custom infrastructure management platforms, allowing teams to provision and manage cloud resources using Kubernetes APIs and patterns.

Pulumi Integration: Pulumi offers the [Pulumi Kubernetes Operator (PKO)](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/) that provides similar Kubernetes-native infrastructure management capabilities, plus support for YAML-based definitions. Teams can also use Pulumi programs to provision the underlying infrastructure that Crossplane manages, creating layered infrastructure management approaches.

Key Features:

- **Kubernetes-native**: Uses CRDs and standard Kubernetes patterns
- **Composite resources**: Create higher-level infrastructure abstractions
- **GitOps compatibility**: Seamless integration with GitOps workflows
- **Multi-cloud support**: Provision resources across cloud providers
- **Policy integration**: Leverage Kubernetes RBAC and admission controllers

Code Example:

```yaml
apiVersion: ec2.aws.crossplane.io/v1alpha1
kind: VPC
metadata:
  name: sample-vpc
spec:
  cidrBlock: 10.0.0.0/16
  region: us-east-1
  tags:
    Name: sample-vpc
  providerConfigRef:
    name: aws-provider-config
```

### 10. OpenTofu

License: Mozilla Public License 2.0  
Latest stable release: v1.12.6 (2026-08-19)  
Best For: Teams seeking an open-source Terraform alternative with community governance

OpenTofu emerged as a fork of Terraform v1.5.x following HashiCorp's license change, maintained by the Linux Foundation. It provides [high, but not full, compatibility with Terraform](/docs/iac/comparisons/opentofu/) while ensuring long-term open-source availability under MPL 2.0 licensing.

Key Features:

- **True open source**: MPL 2.0 license with community governance via Linux Foundation ensuring long-term accessibility
- **Terraform compatibility**: Largely maintains existing workflows, modules, and provider ecosystem, with some divergence emerging as the projects evolve independently
- **Community-driven development**: Transparent roadmap, open contribution process, and vendor-neutral governance
- **License certainty**: Removes concerns about future licensing restrictions for commercial use

When OpenTofu Makes Sense:

- Organizations requiring guaranteed open-source licensing for compliance or philosophical reasons
- Teams with significant Terraform investments wanting to avoid vendor lock-in
- Environments where community governance and transparency are priorities
- Projects needing long-term license stability

Architectural Considerations:
As a Terraform fork, OpenTofu inherits the same architectural approach, which means teams evaluating it should consider whether HCL-based infrastructure definition meets their long-term needs for testing, IDE integration, and developer productivity, or whether a programming language-based approach might better serve complex scenarios.

Code Example:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1d0"
  instance_type = "t3.micro"

  tags = {
    Name = "HelloWorld"
  }
}

output "instance_ip" {
  value = aws_instance.web.public_ip
}
```

### Ansible

License: GPL v3  
Best For: Configuration management with some infrastructure provisioning capabilities

> [!INFO]
> Ansible is primarily a configuration management tool, not a pure Infrastructure as Code tool. While Ansible can provision some cloud resources, its core strength lies in configuring and managing software on existing systems rather than comprehensive infrastructure provisioning.

Ansible provides configuration management and limited infrastructure provisioning through its agentless architecture and simple YAML-based playbooks.

Pulumi Integration: Rather than competing with Ansible, Pulumi complements it perfectly. Use Pulumi for infrastructure provisioning and Ansible for configuration management. Pulumi's Command provider can execute Ansible playbooks as part of your infrastructure deployment, and many Pulumi customers use both tools together for comprehensive infrastructure automation. [See example: Deploy WordPress to AWS using Pulumi and Ansible](/blog/deploy-wordpress-aws-pulumi-ansible/).

Key Features:

- **Agentless architecture**: No software installation required on target systems
- **YAML playbooks**: Human-readable automation definitions
- **Idempotent operations**: Safe to run multiple times
- **Large module library**: Extensive built-in functionality for various systems
- **Push-based execution**: Centralized control and execution

Code Example:

```yaml
---
- name: Provision AWS infrastructure
  hosts: localhost
  tasks:
    - name: Create VPC
      amazon.aws.ec2_vpc_net:
        name: ansible-vpc
        cidr_block: 10.0.0.0/16
        region: us-east-1
        tags:
          Environment: production
      register: vpc

    - name: Create subnet
      amazon.aws.ec2_vpc_subnet:
        vpc_id: "{{ vpc.vpc.id }}"
        cidr: 10.0.1.0/24
        region: us-east-1
        tags:
          Name: ansible-subnet
```

### Chef

License: Apache 2.0  
Best For: Complex configuration management scenarios requiring programmable logic

> [!INFO]
> Chef is a configuration management tool, not an Infrastructure as Code tool. Chef focuses on configuring and maintaining software, services, and system settings on existing infrastructure rather than provisioning cloud resources.

Chef provides configuration management and system automation using Ruby-based recipes and cookbooks, offering powerful programmability for complex configuration scenarios.

Key Features:

- **Ruby DSL**: Full programming language for configuration logic
- **Agent-based architecture**: Continuous compliance and drift detection
- **Cookbook ecosystem**: Reusable configuration patterns and community recipes
- **Test Kitchen**: Infrastructure testing and validation framework
- **Enterprise features**: Advanced reporting and compliance capabilities

Code Example:

```ruby
# cookbook/recipes/default.rb
package 'nginx' do
  action :install
end

service 'nginx' do
  action [:enable, :start]
end

template '/etc/nginx/sites-available/default' do
  source 'default.erb'
  owner 'root'
  group 'root'
  mode '0644'
  notifies :restart, 'service[nginx]'
end
```

### Puppet

License: Apache 2.0  
Best For: Enterprise environments requiring strong governance and compliance

> [!INFO]
> Puppet is primarily a configuration management tool, not a pure Infrastructure as Code tool. Puppet specializes in maintaining desired configuration state on existing systems and ensuring compliance, rather than provisioning cloud infrastructure.

Puppet offers enterprise-grade configuration management with a focus on compliance, governance, and declarative system state management.

Key Features:

- **Declarative language**: Puppet DSL for describing desired system state
- **Compliance reporting**: Built-in governance and audit capabilities
- **Forge marketplace**: Community modules and enterprise content
- **Enterprise support**: Professional services and enterprise features
- **Continuous enforcement**: Ongoing configuration compliance monitoring

Code Example:

```puppet
# manifests/webserver.pp
class webserver {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => '<h1>Hello from Puppet!</h1>',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0644',
  }
}
```

### Salt

License: Apache 2.0  
Best For: Python-oriented teams requiring high-performance configuration management

> [!INFO]
> Salt is primarily a configuration management and remote execution tool, not a pure Infrastructure as Code tool. While Salt can manage some infrastructure components, its primary focus is on configuring systems and executing commands across large infrastructures.

Salt provides fast, scalable configuration management and remote execution using Python, designed for high-performance system automation at scale.

Key Features:

- **Python-based**: Leverage the Python ecosystem and libraries
- **High performance**: Fast execution across large infrastructures
- **Event-driven automation**: Reactive automation and orchestration
- **Pillar data system**: Secure, hierarchical data management
- **Flexible communication**: Support for various communication patterns

Code Example:

```yaml
# /srv/salt/webserver.sls
nginx:
  pkg.installed: []
  service.running:
    - enable: True
    - require:
      - pkg: nginx

/var/www/html/index.html:
  file.managed:
    - source: salt://files/index.html
    - user: www-data
    - group: www-data
    - mode: 644
```

## Infrastructure as Code Tools

### Kubernetes - Container Orchestration Platform

License: Apache 2.0  
Best For: Container-native infrastructure and application management

While primarily a [container orchestration](/topics/containers/) platform, Kubernetes itself serves as an infrastructure as code tool through its declarative YAML manifests and API-driven resource management.

Key Features:

- **Declarative configuration**: YAML-based resource definitions
- **API-driven**: RESTful API for all resource operations
- **Self-healing**: Automatic recovery and reconciliation
- **Extensible**: Custom resources and controllers
- **GitOps compatible**: Works seamlessly with Git-based workflows

Code Example:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.27
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
  - port: 80
    targetPort: 80
  type: LoadBalancer
```

## Infrastructure as Code Security and Compliance Tools

While the tools above focus on provisioning and managing infrastructure, a complete IaC ecosystem includes security scanning and compliance tools. These tools complement your primary IaC tool by providing security analysis, policy enforcement, and compliance checking:

### Security Scanning Tools

Snyk - License: Proprietary  
Leading developer security platform that includes comprehensive infrastructure as code scanning alongside container and application security. Provides real-time vulnerability detection, compliance checking, and automated remediation guidance. Integrates with popular development tools and CI/CD pipelines with extensive enterprise adoption.

Wiz - License: Proprietary  
Comprehensive cloud security platform that includes infrastructure as code scanning capabilities. Provides vulnerability management, compliance monitoring, and security posture assessment across cloud environments. Offers integration with development workflows and supports multiple IaC formats with strong enterprise presence.

Checkov - License: Apache 2.0  
Popular open-source static analysis tool for infrastructure as code that scans cloud infrastructure configurations for security and compliance issues. Supports Terraform, CloudFormation, Kubernetes, Helm, ARM templates, and more. Integrates with CI/CD pipelines and provides over 1000+ built-in policies covering CIS benchmarks, PCI DSS, and GDPR compliance.

### Linting and Validation Tools

TFLint - License: MPL 2.0  
Terraform linter focused on possible errors, best practices, and security issues in Terraform configurations. Provides pluggable rule sets for cloud providers (AWS, Azure, GCP) and helps enforce coding standards, detect deprecated syntax, and prevent common configuration errors.

These security tools integrate into CI/CD pipelines alongside your chosen IaC tool to provide comprehensive security coverage throughout the infrastructure lifecycle.

### Pulumi ESC

License: Apache 2.0 (Open Source) / Proprietary (SaaS)  
Best For: Teams needing centralized configuration and secrets management across environments and tools

Pulumi ESC (Environments, Secrets, and Configuration) is a comprehensive platform for managing configuration data, secrets, and environment variables across your entire infrastructure and application stack. ESC provides a single source of truth for configuration that works with any infrastructure tool, not just Pulumi.

Key Features:

- **Universal configuration management**: Works with any infrastructure tool, CI/CD system, or application
- **Hierarchical environments**: Compose configuration from multiple sources with inheritance and overrides
- **Dynamic secrets**: Integration with cloud providers for short-lived credentials and just-in-time access
- **Policy-based access control**: Fine-grained permissions and audit logging for configuration access
- **Multiple consumption methods**: CLI, REST API, SDK integration, and direct cloud provider integration
- **GitOps workflows**: Version control integration with pull request-based configuration management

Code Example:

```yaml
# Production environment configuration
values:
  app:
    name: myapp
    version: ${fn.fromJSON(aws.ecr.getAuthorizationToken).password}
  database:
    connectionString: ${pulumi.database.connectionString}
imports:
  - shared/common
  - aws/production
```

### Pulumi Insights

License: Proprietary (SaaS)  
Best For: Organizations needing comprehensive cloud resource visibility, search, and compliance monitoring

Pulumi Insights provides cloud resource search, analytics, and compliance capabilities across your entire multi-cloud infrastructure, regardless of how resources were provisioned. It offers a unified view of your cloud resources with powerful search, cost analysis, and policy enforcement.

Key Features:

- **Universal cloud inventory**: Discover and catalog resources across AWS, Azure, Google Cloud, and Kubernetes
- **Advanced search and analytics**: Query resources by tags, properties, relationships, and compliance status
- **Cost optimization insights**: Resource cost analysis, trends, and optimization recommendations
- **Compliance monitoring**: Continuous policy evaluation and drift detection across all cloud resources
- **Resource relationships**: Understand dependencies and relationships between cloud resources
- **Integration with any IaC tool**: Works with resources created by Pulumi, Terraform, CloudFormation, or manually

Use Cases:

- **Cloud governance**: Ensure compliance with organizational policies and industry standards
- **Cost management**: Identify unused resources and optimization opportunities
- **Security auditing**: Track resource configurations and detect security misconfigurations
- **Multi-cloud visibility**: Single pane of glass for resources across different cloud providers

## Infrastructure Automation and Management Platforms

While the above tools focus on defining and provisioning infrastructure, several platforms provide automation, orchestration, and management capabilities that work with infrastructure as code tools. Important: These are not IaC tools themselves, but rather automation platforms that rely on underlying IaC tools.

### IaC Automation Platforms

Pulumi Cloud
Best For: Teams using Pulumi IaC who need enterprise-grade collaboration, security, and governance

Pulumi Cloud is the smartest and easiest way to automate, secure, and manage everything you run in the cloud. It serves as the managed service companion to Pulumi's open-source infrastructure as code tool, providing enterprise capabilities that extend beyond basic IaC functionality.

The relationship between Pulumi IaC and Pulumi Cloud follows a Git/GitHub model: Pulumi IaC is like Git (fully open source and functional on its own), while Pulumi Cloud is like GitHub (a managed service that makes the open-source tool much easier to use securely at scale with teams).

Key Features:

- **Managed state backend**: Secure, scalable state management with transactional protocols
- **Team collaboration**: Full audit logs, RBAC, and identity provider integration
- **Centralized secrets management**: Pulumi ESC for configuration and secrets across environments
- **Cloud inventory and insights**: Pulumi Insights for search, compliance, and drift detection
- **Remote deployments**: CI/CD integrations and automated workflows
- **Policy enforcement**: Built-in security and compliance policy as code
- **Multi-product platform**: Integrated IaC, secrets management, and cloud insights

Pulumi IaC works with or without Pulumi Cloud - you can use DIY backends (S3, Azure Blob, etc.) or the managed service. However, Pulumi Cloud becomes the default experience when you install the Pulumi CLI, providing instant collaboration capabilities without the overhead of building and maintaining your own infrastructure management platform.

HashiCorp Cloud Platform (HCP) - License: Proprietary (SaaS)  
Best For: Organizations standardizing on HashiCorp tools across infrastructure and security lifecycle management

HashiCorp Cloud Platform (HCP) is an enterprise-grade SaaS platform that provides unified lifecycle management for infrastructure and security operations. HCP Terraform (formerly Terraform Cloud) serves as the managed service for Terraform/OpenTofu workflows, while the broader platform integrates multiple HashiCorp tools.

Key Features:

- **HCP Terraform management**: Workspace organization, remote execution, and state management for Terraform
- **Infrastructure lifecycle automation**: Continuous validation, drift detection, and module lifecycle management
- **Private VCS access**: Secure integration with private version control repositories
- **Policy enforcement**: Sentinel policy-as-code framework for compliance and governance
- **Integrated security services**: HCP Vault for secrets management, HCP Consul for service networking
- **Enterprise access controls**: RBAC, SAML SSO integration, and fine-grained permissions
- **Module and image management**: HCP Packer for automated machine/container image creation

HCP focuses specifically on HashiCorp tool integration and provides a comprehensive platform for organizations that have standardized on the HashiCorp ecosystem for infrastructure and security operations.

Spacelift - Spacelift is not an infrastructure as code tool—it's an automation and workflow platform that relies on other IaC tools like Terraform, OpenTofu, Pulumi, CloudFormation, and Kubernetes. Spacelift provides CI/CD pipelines, policy enforcement, and collaboration features for teams using these underlying IaC tools.

Env0 - Env0 is not an infrastructure as code tool—it's an automation platform that provides workflow management, governance, and collaboration features for existing IaC tools like Terraform, OpenTofu, and Terragrunt. It adds CI/CD pipelines, cost management, and policy enforcement on top of these tools.

Atlantis - An open-source tool that provides GitOps-style workflows for Terraform and OpenTofu by automatically running terraform plan and apply operations via pull request automation.

### Development Environment Tools

Vagrant - Vagrant is not an infrastructure as code tool—it's a development environment management tool that creates and configures lightweight, reproducible virtual development environments. While it can provision VMs, its focus is on local development environments rather than cloud infrastructure provisioning.

Docker Compose - While not an IaC tool, Docker Compose defines multi-container applications and can be used alongside IaC tools for application deployment after infrastructure provisioning.

These platforms and tools serve important roles in the infrastructure automation ecosystem but should not be confused with infrastructure as code tools themselves. They enhance and orchestrate the work of actual IaC tools rather than replacing them.

## The Future of Infrastructure as Code

The infrastructure as code landscape is rapidly evolving toward software engineering maturity, with several transformative trends reshaping how organizations approach infrastructure:

Software Engineering Convergence: The most significant trend is the convergence of infrastructure and software engineering practices. Organizations are moving away from limited DSLs toward full programming languages that enable testing, debugging, refactoring, and other software engineering best practices. This shift enables infrastructure teams to leverage the same tools, skills, and methodologies that have proven successful in application development.

Real-Time Cloud Integration: Native cloud provider SDK integration is becoming the standard, replacing community-maintained providers that lag behind new cloud features. Organizations expect same-day access to new cloud services without waiting weeks or months for provider updates.

Comprehensive Testing Paradigms: Infrastructure testing is evolving beyond basic integration tests to include unit testing, property-based testing, and continuous validation. Teams are applying test-driven development principles to infrastructure, catching issues before deployment rather than discovering them in production.

Internal Developer Platform Evolution: Organizations are building sophisticated Internal Developer Platforms that provide self-service infrastructure capabilities while maintaining governance and compliance. These platforms leverage infrastructure as code tools to create standardized, reusable components that accelerate development velocity.

AI-Enhanced Development: Integration of AI tools to help generate, optimize, and troubleshoot infrastructure code, with particular strength in environments that use familiar programming languages where AI assistance is most mature. Emerging technologies like Model Context Protocol (MCP) and AI prompt templates are beginning to enable more sophisticated AI-infrastructure interactions.

> "In under a year, AI has completely reshaped how we build applications. With Pulumi Neo, platform engineering is now catching up."
>
> — Joe Duffy, Founder & CEO, [Pulumi](https://www.prnewswire.com/news-releases/introducing-pulumi-neo-the-industrys-first-ai-powered-platform-engineer-302556718.html)

These trends favor tools that embrace software engineering principles from the ground up, rather than attempting to retrofit programming capabilities onto template-based or DSL-limited approaches.

{{< blog/cta-card title="Bring software engineering to IaC" >}}
Define infrastructure across AWS, Azure, Google Cloud, and Kubernetes in the language your team already knows, with testing, IDE support, and reusable components.
{{< /blog/cta-card >}}

## Migration and Adoption Strategies

Organizations don't need to choose between maintaining existing infrastructure and adopting modern IaC approaches. Proven migration strategies enable gradual adoption while preserving operational stability.

### Incremental Adoption Approaches

Team-by-Team Migration: Start with new projects or specific teams, allowing gradual skill development and process refinement. Teams can maintain existing infrastructure while building new capabilities with modern tools.

Project-by-Project Transition: Migrate individual applications or services incrementally, enabling teams to learn and optimize approaches before expanding scope.

Hybrid Operations: Use state integration and import tools to reference existing infrastructure while building new components with modern IaC tools.

### Proven Migration Timelines

Real-world migrations demonstrate that adoption can be remarkably fast with proper tooling:

- **Atlassian Bitbucket**: Converted a Terraform-managed CI/CD pipeline to Pulumi's Python-based IaC in 2 days, using the automatic conversion tool and the team's existing Python experience — because every developer on the team already wrote Python, they could bring existing skills straight to the new infrastructure code.
- **Enterprise migrations**: Typical team migrations complete in weeks, not months, depending on infrastructure complexity and team preparation
- **Learning curve**: Teams with programming experience adapt to language-based IaC approaches within days, while those new to programming may require additional training time

> "When we did it with Terraform, it took two weeks to do [infrastructure deployments]. Now we do it in about three hours a day. So that's how much of an improvement Pulumi gave us on our deployment time."
>
> — Matt Stephenson, Senior Principal Software Engineer, [Starburst](https://www.pulumi.com/case-studies/starburst/)

### Migration Tools and Resources

Automated Conversion: Tools like tf2pulumi and pulumi convert automatically translate existing infrastructure definitions, preserving logic and structure while upgrading to modern approaches.

State Integration: Import existing cloud resources and reference Terraform state during transition periods, enabling zero-downtime migrations.

Training and Support: Comprehensive documentation, tutorials, and community resources accelerate team onboarding and reduce migration risks.

### Best Practices for Successful Adoption

1. **Start with pilot projects** to build confidence and establish patterns
2. **Leverage automated migration tools** to reduce manual conversion effort
3. **Maintain state integration** during transition periods for operational continuity
4. **Invest in team training** to maximize productivity gains from modern approaches
5. **Establish testing practices** early to realize reliability and quality benefits

The key insight: migration to modern IaC approaches is a technical upgrade, not a complete rebuild. Organizations can preserve existing investments while gaining access to superior tooling and practices.

## Frequently Asked Questions

### Which IaC tool should I choose for AWS?

For teams wanting programming languages: Pulumi IaC and AWS CDK both offer excellent developer experiences with general-purpose programming languages. Pulumi provides multi-cloud flexibility, while CDK offers deep AWS-native integration.

For AWS-only deployments: CloudFormation provides the deepest native AWS service support and direct integration with AWS services.

For Terraform ecosystem users: OpenTofu provides open-source licensing with Terraform compatibility, while Terraform offers extensive community resources and established workflows.

### Is Terraform still worth learning in 2026?

Terraform remains a valuable skill and viable choice for many scenarios, though teams should consider their specific needs and long-term goals:

When Terraform Makes Sense:

- Teams building on existing Terraform infrastructure and expertise
- Organizations with successful Terraform workflows and established processes
- Projects that benefit from Terraform's extensive module ecosystem
- Teams comfortable with HCL and template-based approaches

When to Consider Alternatives:

- Teams wanting comprehensive testing capabilities (unit, property, integration testing)
- Organizations requiring full IDE support with debugging and refactoring
- Projects needing complex programmatic logic or extensive code reuse
- Teams with strong programming backgrounds who prefer familiar languages

Key Considerations:

- **Licensing**: Terraform's Business Source License may create restrictions for some commercial scenarios
- **Ecosystem**: Terraform has the largest provider ecosystem and community resources
- **Learning investment**: Consider whether learning HCL aligns with your team's skill development goals
- **Migration options**: Tools exist for migrating between different IaC platforms when needs change

The choice often depends on team background, infrastructure complexity, and development workflow preferences rather than one approach being universally superior.

### How do I get started with infrastructure as code?

Choose Based on Your Team Profile:

1. **Programming-oriented teams**: Consider Pulumi IaC for familiar languages with full IDE support, testing frameworks, and multi-cloud flexibility
2. **Template-oriented teams**: OpenTofu or Terraform offer extensive community resources, established workflows, and broad ecosystem support
3. **Cloud-specific teams**: Native tools (AWS CDK/CloudFormation, Azure ARM/Bicep, Google Cloud Infrastructure Manager) provide deep platform integration
4. **Kubernetes-focused teams**: Consider Crossplane or Pulumi Kubernetes Operator for container-native approaches

Getting Started Steps:

1. **Start small**: Begin with simple projects like deploying a single application or basic infrastructure
2. **Use examples**: Leverage existing templates, tutorials, and community examples to accelerate learning
3. **Plan for growth**: Consider how your tool choice will scale with team size and infrastructure complexity
4. **Experiment**: Most tools offer free tiers or trials - try multiple approaches with simple projects to find what fits your team best

### What's the difference between configuration management and infrastructure provisioning?

- Infrastructure provisioning (Pulumi IaC, Terraform, CloudFormation) creates and manages cloud resources like VMs, networks, and databases
- Configuration management (Ansible, Chef, Puppet) configures and maintains software on existing systems
- Many modern tools do both, with Pulumi IaC and Ansible offering comprehensive capabilities across both domains

### Can I use multiple IaC tools together?

Absolutely! Many organizations use complementary tools for different aspects of infrastructure management:

Pulumi + Configuration Management:

- Pulumi + Ansible: Infrastructure provisioning + server configuration ([example](/blog/deploy-wordpress-aws-pulumi-ansible/))
- Pulumi + Chef/Puppet: [Cloud resources](/docs/get-started/) + complex configuration management

Pulumi + Native Cloud Tools:

- Reference existing CloudFormation/ARM deployments from Pulumi programs
- Import CloudFormation/ARM resources into Pulumi for gradual migration
- Use Pulumi alongside CDK for different parts of AWS infrastructure

Pulumi + Kubernetes:

- [Pulumi Kubernetes Operator (PKO)](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/) for GitOps workflows
- Pulumi + Crossplane for layered infrastructure management
- Pulumi + security scanners like Checkov or Terrascan for compliance

Terraform + Pulumi Coexistence:

- Use Terraform for base infrastructure and Pulumi for Internal Developer Platforms (IDPs)
- Reference existing Terraform state from Pulumi programs during gradual migration
- Manage different infrastructure layers with different tools based on team expertise

Pulumi IaC is designed for heterogeneous environments where multiple tools may be in use. For example, you can manage existing Terraform or CloudFormation resources with Pulumi, either using both tools in tandem or for temporary management while migrating to native Pulumi IaC code. Other Pulumi tools, like Pulumi IDP, also enable you to manage IaC self-service workflows like other tools on this list. See what's possible when [migrating to Pulumi](/docs/iac/guides/migration/).

### Which tool has the best learning resources?

- Pulumi: Excellent documentation with examples in multiple languages, comprehensive tutorials
- Terraform/OpenTofu: Extensive community content, many courses and books available
- AWS CDK: Outstanding official documentation with workshops and examples
- Kubernetes: Vast ecosystem but steeper learning curve

### How important is open-source licensing for IaC tools?

Very important for long-term strategy:

- Apache 2.0 (Pulumi, CDK) offers maximum flexibility
- MPL 2.0 (OpenTofu) ensures open-source availability
- BUSL (Terraform) restricts commercial competitors
- Proprietary (CloudFormation, ARM) ties you to specific vendors

Choose open-source tools like Pulumi or OpenTofu to avoid vendor lock-in.

### What about security and compliance?

All major IaC tools support security best practices:

- Built-in policy engines: Pulumi CrossGuard, AWS Config, Azure Policy
- Third-party scanners: Checkov, KICS, Terrascan work with all tools
- Compliance frameworks: Most tools support SOC 2, PCI DSS, CIS benchmarks
- Secret management: Integration with Vault, AWS Secrets Manager, Azure Key Vault

Pulumi offers the most comprehensive built-in security features with CrossGuard policy as code.

### Can I migrate from one IaC tool to another?

Yes, and many organizations are successfully migrating to overcome limitations in their current tools. Migration tools and proven approaches exist:

Proven Migration Success Stories:

- **Atlassian Bitbucket**: Converted a Terraform-managed CI/CD pipeline to Pulumi's Python-based IaC in 2 days, using the automatic conversion tool and the team's existing Python experience
- **Starburst**: Achieved 112x faster deployments after incrementally migrating from Terraform
- **Multiple organizations**: Report deployment-time reductions ranging from roughly 70% to 99% after moving to programming language-based approaches

Available Migration Tools:

- **Pulumi**: Offers [`pulumi convert`](/docs/iac/guides/migration/#conversion) for importing from Terraform, ARM, and CloudFormation with state integration
- **Terraformer**: Can import existing cloud resources into Terraform/OpenTofu
- **CDK Migrate**: Helps move from CloudFormation to CDK
- **Manual migration**: Always possible by recreating resources in the new tool

Migration Strategies:

- **Incremental adoption**: Migrate team-by-team or project-by-project without disruption
- **State integration**: Reference existing infrastructure during transition periods
- **Zero downtime**: Tools like Pulumi enable seamless migration without service interruption

The key is choosing tools that provide comprehensive migration support and incremental adoption paths rather than requiring "rip and replace" approaches.

### How much do infrastructure as code tools cost in 2026?

Cloud-native tools like AWS CDK, CloudFormation, Azure ARM, Azure Bicep, and Google Cloud Infrastructure Manager carry no separate tool fee: you pay only for the cloud resources you provision. Open-source tools including OpenTofu, Kubernetes, and Crossplane are also free to run, though you still cover your own compute and cluster costs.

Managed platforms price differently. Pulumi Cloud's Individual plan is free forever for one user with unlimited stacks and projects, 500 workflow minutes per month, and 5 million Pulumi Neo tokens per month; Team plans start around $40/month for up to 10 users, and Enterprise starts around $400/month, scaling with the number of managed resources. HCP Terraform is free for up to 500 managed resources with one concurrent run, then moves to per-resource pricing (roughly $0.10 to $0.99 per resource per month depending on tier), with self-hosted Terraform Enterprise available at custom pricing for larger organizations. Figures reflect published pricing as of August 2026 and change periodically, so confirm current rates before budgeting.

### Which infrastructure as code tools work best with AI coding agents?

Tools built on general-purpose programming languages give AI agents the biggest advantage, because agents can read, generate, test, and refactor real code the same way they do application code. Pulumi is explicitly built for this: it lets agents like [Pulumi Neo](/product/neo/) propose changes, run previews, respond to failures, and open pull requests using the same Python, TypeScript, Go, C#, or Java that developers already write and test, rather than reasoning about HCL diffs or templated JSON/YAML that are harder for a language-aware toolchain to test against.

Declarative DSL-based tools such as Terraform and OpenTofu can also be driven by AI coding assistants, and both ship a native test framework (`terraform test` / `tofu test`) plus language servers and editor extensions. What agents don't get in HCL is the depth of the surrounding toolchain — the assertion and mocking libraries, package ecosystem, and refactoring tools that come free with a general-purpose language — so validating an agent-generated change tends to take more bespoke scaffolding. That's a tradeoff, not a hard blocker — plenty of teams drive HCL with agents productively today. It does mean general-purpose-language IaC starts from a stronger position for agent-driven work: AI coding assistants such as Claude Code, Cursor, and Codex reach Pulumi through the same code-first path they already use for application code, with no IaC-specific tooling to bolt on.

### What is the most popular infrastructure as code tool in 2026?

By GitHub stars, Kubernetes leads the broader infrastructure ecosystem at roughly 124,900 stars, reflecting its role as the de facto container orchestration standard rather than a pure IaC tool. Among dedicated IaC tools, Terraform remains the most-starred at roughly 49,500, followed by OpenTofu at roughly 29,900, Pulumi at roughly 25,600, AWS CDK at roughly 12,900, and Crossplane at roughly 12,000 (measured 2026-08-22; star counts change continuously and are one signal among many, not a ranking of technical merit). Terraform's larger community reflects a decade of first-mover adoption, while Pulumi, OpenTofu, and Crossplane have grown fastest among teams prioritizing general-purpose languages, open governance, or Kubernetes-native infrastructure management, respectively.

## Conclusion: The Evolution of Infrastructure as Code

The infrastructure as code landscape in 2026 reflects a maturing field where different approaches serve different organizational needs and team preferences. The evolution from manual processes to automated infrastructure has branched into multiple viable paths, each with distinct advantages.

The Spectrum of Approaches:

Template-based tools like Terraform and OpenTofu continue to serve teams effectively, particularly those comfortable with declarative configuration and established HCL workflows. Cloud-native solutions provide deep platform integration for single-cloud strategies. Programming language-based approaches offer familiar development experiences for teams seeking comprehensive testing, IDE integration, and code reusability.

Evidence of Success Across Approaches:

Organizations achieve significant improvements regardless of their chosen path—the key is selecting tools that align with team expertise and infrastructure requirements. Understanding [what DevOps is](/what-is/what-is-devops/) and [platform engineering concepts](/what-is/what-is-platform-engineering/) helps inform these decisions. Success stories span the entire ecosystem, from Terraform's widespread enterprise adoption to programming language approaches enabling dramatic productivity gains at companies like Unity, Snowflake, and Starburst.

Choosing Your Path:

The most successful organizations focus on key decision criteria:

- **Team background**: Match tools to existing skills and preferred development approaches
- **Infrastructure complexity**: Consider testing, abstraction, and maintainability needs
- **Organizational constraints**: Factor in licensing, governance, and compliance requirements
- **Growth trajectory**: Plan for how needs may evolve with scale and team expansion
- **Integration requirements**: Ensure compatibility with existing workflows and toolchains

The Future of Infrastructure:

The industry continues evolving toward treating infrastructure as software, but this transformation takes many forms. Organizations exploring [serverless architectures](/serverless/) and container strategies particularly benefit from programmable infrastructure approaches. Whether through enhanced DSLs, visual design tools, programming languages, or hybrid approaches, the goal remains consistent: enabling teams to manage infrastructure with the same reliability, collaboration, and velocity they expect from modern software development.

For teams ready to embrace programming language-based infrastructure as code, [get started with Pulumi for free](/docs/install/) to experience how familiar languages and software engineering practices can transform infrastructure management with comprehensive testing, powerful abstractions, and seamless multi-cloud support. Want to see where infrastructure is headed next? [Explore Pulumi Neo](/product/neo/), the AI agent that proposes changes, runs previews, and opens PRs alongside your team.
