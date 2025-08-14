---
title: "Deployment Guardrails with Policy as Code"
date: 2025-02-10T09:00:00Z
draft: false
meta_desc: "Implement deployment guardrails with Pulumi CrossGuard to create safe self-service infrastructure balancing developer autonomy and control."
meta_image: meta.png
authors:
    - adam-gordon-bell
tags:
    - idp
    - platform-engineering
    - policy-as-code
    - crossguard
    - compliance
    - security
    - self-service
    - guardrails
---

**Building Safe Self-Service Infrastructure with Pulumi CrossGuard**

Welcome to the third post in our **IDP Best Practices** series. In this workshop, we explore how to implement **policy as code** with [Pulumi CrossGuard](/docs/iac/packages-and-automation/crossguard) to create deployment guardrails that make self-service infrastructure both powerful and safe.

Platform engineering is about enabling developer velocity while maintaining security and compliance. The challenge? How do you give teams the freedom to deploy infrastructure quickly without compromising on safety, security, or organizational standards? The answer lies in **automated guardrails** powered by policy as code.

<!--more-->

This post is part of our IDP Best Practices series:

* [How to Build an Internal Developer Platform: Strategy, Best Practices, and Self-Service Infrastructure](/blog/idp-strategy-planning-self-service-infrastructure-that-balances-developer-autonomy-with-operational-control)
* [Build Golden Paths with Infrastructure Components and Templates](/blog/build-golden-paths-infrastructure-components-and-templates)
* **Deployment Guardrails with Policy as Code** (you are here)
* Day 2 Platform Operations: Automating Drift Detection and Remediation
* Extend Your IDP for AI Applications: GPUs, Models, and Cost Controls
* Next-Gen IDPs: How to Modernize Legacy Infrastructure with Pulumi

{{% notes type="tip" %}}
**Want hands-on experience?** Access the [complete demo code](https://github.com/pulumi/workshops/tree/main/idp-component-policies) and [policy examples](https://github.com/pulumi/workshops/tree/main/idp-component-policies/demo-policies) from this workshop. Enroll in the free [IDP Builder Workshop Series](https://info.pulumi.com/idp/internal-developer-platform-workshops-course) for recordings and additional resources.
{{% /notes %}}

## The Platform Engineering Challenge: Speed vs. Safety

Picture this scenario from Statsig, a fast-growing feature flag platform processing 2 trillion events daily. They had one infrastructure engineer, Jason, who handled all infrastructure requests. When Jason went on parental leave, the entire engineering organization faced a bottleneck. Infrastructure requests piled up, deployments slowed, and the team realized they needed self-service infrastructure.

But here's the challenge: **How do you enable self-service without sacrificing security, compliance, or operational stability?**

This is where deployment guardrails with policy as code become essential. They transform the conversation from *"Talk to the infrastructure person"* to *"Ship with guardrails."*

## Understanding Platform Engineering Layers

Before diving into guardrails, let's understand where policy fits in your platform architecture:

### Layer 1: Foundational Infrastructure

* Security controls, shared networking, OIDC/IAM
* Managed by platform teams with strict access controls

### Layer 2: Shared Infrastructure

* VPCs, compute platforms, load balancers
* Standardized components with some customization

### Layer 3: Workloads Layer

* Deployable artifacts, pipelines, operability tools
* **This is where most self-service activity happens**
* **This is where guardrails are most critical**

The workloads layer is where developers need the most freedom but also where the most risk exists. It's the perfect place for policy-driven guardrails.

## What Are Deployment Guardrails?

Deployment guardrails are **automated policies** that:

1. **Prevent misconfigurations** before they reach production
2. **Enforce security standards** automatically
3. **Guide developers** toward best practices
4. **Enable safe self-service** by catching issues early

Think of guardrails like type checking in programming languages. They don't restrict creativity—they catch errors early and guide developers toward correct patterns.

## Introducing Pulumi CrossGuard: Policy as Code

[Pulumi CrossGuard](/docs/iac/packages-and-automation/crossguard) is Pulumi's policy as code framework that enables you to:

* Write policies in familiar programming languages ([Python](/docs/iac/packages-and-automation/crossguard/get-started#writing-policies-in-python), [TypeScript](/docs/iac/packages-and-automation/crossguard/get-started#writing-policies-in-typescript), Go)
* Enforce policies across all cloud resources and providers
* Run policies at different stages of the deployment lifecycle
* Integrate with CI/CD for automated enforcement

### Key Policy Types

**[Resource Policies](/docs/iac/packages-and-automation/crossguard/core-concepts#resource-validation)**: Validate individual resources

```python
def restrict_dangerous_ports(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "aws:lb/targetGroup:TargetGroup":
        port = args.props.get("port")
        dangerous_ports = ["22", "23", "3389"]
        if str(port) in dangerous_ports:
            report_violation("Dangerous port detected. Avoid using SSH, Telnet, or RDP ports.")
```

**[Stack Policies](/docs/iac/packages-and-automation/crossguard/core-concepts#stack-validation)**: Validate relationships across resources

```python
def validate_microservice_encryption(args: StackValidationArgs, report_violation: ReportViolation):
    microservice_components = []
    s3_buckets = []

    for resource in args.resources:
        if resource.resource_type == "custom:infrastructure:Microservice":
            microservice_components.append(resource)
        elif resource.resource_type == "aws:s3/bucket:Bucket":
            s3_buckets.append(resource)

    if microservice_components and s3_buckets:
        for bucket in s3_buckets:
            encryption = bucket.props.get("serverSideEncryptionConfiguration")
            if not encryption:
                report_violation("S3 bucket must have encryption enabled when used with microservice components.")
```

## Building Practical Guardrails: Real-World Examples

Let's walk through building guardrails for a microservice platform, starting with the component from our [previous workshop](/blog/build-golden-paths-infrastructure-components-and-templates).

### Example 1: Port Security Policy

**Problem**: Developers might accidentally expose services on dangerous ports like SSH (22) or RDP (3389).

**Solution**: A policy that blocks dangerous port configurations.

```python
import pulumi_policy as policy

def restrict_dangerous_ports_validation(args, report_violation):
    """Prevent services from running on dangerous ports."""
    if args.resource_type == "aws:lb/targetGroup:TargetGroup":
        port = args.props.get("port")
        dangerous_ports = ["22", "23", "3389", "5432", "3306"]

        if str(port) in dangerous_ports:
            report_violation(
                f"Port {port} is not allowed. This port is commonly used for "
                f"administrative services and should not be exposed via load balancer."
            )

restrict_dangerous_ports = policy.ResourceValidationPolicy(
    name="restrict-dangerous-ports",
    description="Prevent services from using dangerous ports",
    validate=restrict_dangerous_ports_validation,
    enforcement_level=policy.EnforcementLevel.MANDATORY
)
```

### Example 2: Resource Limits Policy

**Problem**: Teams might request oversized resources, leading to cost overruns.

**Solution**: A policy that enforces reasonable resource limits with advisory warnings.

```python
def limit_memory_validation(args, report_violation):
    """Limit memory allocation for microservices."""
    if args.resource_type == "custom:infrastructure:Microservice":
        # Extract memory from component tags or properties
        memory_str = args.props.get("memory", "512Mi")

        # Parse memory value (assuming format like "2Gi", "1024Mi")
        if memory_str.endswith("Gi"):
            memory_gb = float(memory_str[:-2])
            if memory_gb > 1:
                report_violation(
                    f"Memory allocation of {memory_str} exceeds recommended limit of 1Gi "
                    f"for microservices. Consider optimizing your application or "
                    f"contact the platform team for exceptions."
                )

limit_memory = policy.ResourceValidationPolicy(
    name="limit-microservice-memory",
    description="Enforce reasonable memory limits for microservices",
    validate=limit_memory_validation,
    enforcement_level=policy.EnforcementLevel.ADVISORY
)
```

### Example 3: Cross-Resource Security Policy

**Problem**: When microservices use S3 buckets, encryption should be mandatory.

**Solution**: A stack policy that validates encryption across related resources.

```python
def microservice_s3_encryption_validation(args, report_violation):
    """Ensure S3 buckets used with microservices have encryption enabled."""
    microservice_resources = []
    s3_buckets = []

    # Collect relevant resources
    for resource in args.resources:
        if resource.resource_type == "custom:infrastructure:Microservice":
            microservice_resources.append(resource)
        elif resource.resource_type == "aws:s3/bucket:Bucket":
            s3_buckets.append(resource)

    # If we have both microservices and S3 buckets, check encryption
    if microservice_resources and s3_buckets:
        for bucket in s3_buckets:
            sse_config = bucket.props.get("serverSideEncryptionConfiguration")
            if not sse_config:
                report_violation(
                    f"S3 bucket '{bucket.name}' must have server-side encryption "
                    f"enabled when used with microservice components."
                )

microservice_s3_encryption = policy.StackValidationPolicy(
    name="microservice-s3-encryption",
    description="Ensure S3 buckets used with microservices are encrypted",
    validate=microservice_s3_encryption_validation,
    enforcement_level=policy.EnforcementLevel.MANDATORY
)
```

## Policy Enforcement Models

Pulumi CrossGuard supports multiple [enforcement models](/docs/iac/packages-and-automation/crossguard/core-concepts#enforcement-levels) to fit different workflows:

### 1. Preventative Model

Policies run **before** resources are created:

* **Advantage**: Fast feedback, prevents bad deployments
* **Use case**: Block dangerous configurations before they reach the cloud
* **Example**: Validating port configurations, resource limits

```bash
# Policies run automatically during preview and deployment
pulumi preview  # Policies evaluated here
pulumi up      # Policies block deployment if violations found
```

### 2. Detective Model

Policies run **after** resources are created:

* **Advantage**: Can validate actual cloud state, including outputs
* **Use case**: Compliance scanning, drift detection
* **Example**: Checking that auto-generated ARNs follow naming conventions

### 3. CI/CD Integration

Policies run as part of your deployment pipeline:

* **Advantage**: Consistent enforcement across teams
* **Use case**: Pull request validation, deployment gates
* **Example**: [GitHub Actions](/docs/iac/packages-and-automation/continuous-delivery/github-actions) that block merges if policies fail

```yaml
# GitHub Actions example
- name: Run Policy Validation
  run: |
    pulumi preview --policy-pack ./policies
    if [ $? -ne 0 ]; then
      echo "Policy violations found. Deployment blocked."
      exit 1
    fi
```

## Policy Remediation: Beyond Detection

Modern policy frameworks don't just detect violations—they can **[automatically fix](/docs/iac/packages-and-automation/crossguard/core-concepts#remediation-policies)** them:

```python
def auto_tag_resources(args, report_violation):
    """Automatically add required tags to resources."""
    if args.resource_type == "aws:s3/bucket:Bucket":
        tags = args.props.get("tags", {})

        if "Department" not in tags:
            # Instead of just reporting, fix the issue
            if not hasattr(args, 'tags'):
                args.props["tags"] = {}
            args.props["tags"]["Department"] = "Engineering"
            return args.props  # Return modified properties

    return None  # No changes needed

auto_tag_policy = policy.ResourceValidationPolicy(
    name="auto-tag-resources",
    description="Automatically add required tags",
    validate=auto_tag_resources,
    enforcement_level=policy.EnforcementLevel.REMEDIATE
)
```

## Server-Side Policy Enforcement

For enterprise deployments, Pulumi provides [server-side policy enforcement](/docs/iac/packages-and-automation/crossguard/get-started#enforcing-a-policy-pack):

1. **Publish policies** to your Pulumi organization:

   ```bash
   pulumi policy publish ./my-policies
   ```

2. **[Create policy groups](/docs/pulumi-cloud/organization/organization-policies)** that combine policies with enforcement levels:
   * Target specific stacks or environments
   * Set different enforcement levels (advisory, mandatory)
   * Configure exceptions for special cases

3. **Automatic enforcement**: Policies run automatically without CLI flags

This ensures policies can't be bypassed and provides consistent governance across your organization.

## Compliance-Ready Policies

Pulumi provides hundreds of [pre-built policies](/docs/iac/packages-and-automation/crossguard/compliance-ready-policies) for common compliance frameworks:

```typescript
import { PolicyManager } from "@pulumi/policy";
import { policyManager } from "@pulumi/compliance-ready-policies/policy-manager";

new PolicyPack("aws-compliance-ready-policies-typescript", {
    policies: [
        ...policyManager.selectPolicies({
            vendors: ["aws"],
            services: ["ec2", "s3"],
            severities: ["medium", "high", "critical"],
            topics: ["encryption"],
            frameworks: ["pcidss"],
        }, "mandatory"),
    ],
});
```

This automatically includes policies for:

* **[PCI DSS](/docs/iac/packages-and-automation/crossguard/compliance-ready-policies#frameworks)**: Payment card industry standards
* **[SOC 2](/docs/iac/packages-and-automation/crossguard/compliance-ready-policies#frameworks)**: Security and compliance controls
* **[ISO 27001](/docs/iac/packages-and-automation/crossguard/compliance-ready-policies#frameworks)**: Information security management
* **[CIS Benchmarks](/docs/iac/packages-and-automation/crossguard/compliance-ready-policies#frameworks)**: Security configuration standards

## Best Practices for Policy Implementation

### 1. Start Small and Iterate

* Begin with 2-3 critical policies
* Use [advisory enforcement](/docs/iac/packages-and-automation/crossguard/core-concepts#enforcement-levels) initially
* Graduate to mandatory enforcement after team feedback

### 2. Provide Clear Error Messages

```python
def good_error_message(args, report_violation):
    if violation_detected:
        report_violation(
            "S3 bucket encryption is required for compliance. "
            "Add serverSideEncryptionConfiguration to fix this. "
            "See: https://docs.company.com/s3-encryption"
        )
```

### 3. Use Progressive Enforcement

* **[Advisory](/docs/iac/packages-and-automation/crossguard/core-concepts#advisory)**: Warn but allow deployment
* **[Mandatory](/docs/iac/packages-and-automation/crossguard/core-concepts#mandatory)**: Block deployment
* **[Remediate](/docs/iac/packages-and-automation/crossguard/core-concepts#remediation-policies)**: Automatically fix issues

### 4. Test Your Policies

```python
# Test policies with unit tests
def test_dangerous_port_policy():
    # Mock resource with port 22
    args = create_mock_args("aws:lb/targetGroup:TargetGroup", {"port": 22})
    violations = run_policy(restrict_dangerous_ports, args)
    assert len(violations) == 1
    assert "dangerous port" in violations[0].message.lower()
```

### 5. Document Escape Hatches

Not every policy will fit 100% of use cases. Provide clear processes for:

* Requesting policy exceptions
* Temporary exemptions for emergencies
* Appeals process for policy changes

## Real-World Success: Statsig's Transformation

After implementing guardrails, Statsig achieved remarkable results:

> *"We had a single infra owner. Parental leave forced us to build self-service, and that's when everything clicked. Developers open a PR, Pulumi previews the change right in the PR, and CI blocks risky changes. That's how you move fast safely. The magic was turning 'talk to the infra person' into 'ship with guardrails.'"*
>
> — Tyrone Wong, Infrastructure Engineer at Statsig

**Key outcomes:**

* **Faster deployments**: From 1.5 weeks to minutes
* **Reduced operational burden**: No more infrastructure ticket queues
* **Maintained security**: Automated policy enforcement
* **Improved developer satisfaction**: Self-service without friction

## Building Your Policy Strategy

### Phase 1: Assessment (Week 1-2)

* Audit current infrastructure patterns
* Identify common misconfigurations
* Document security requirements
* Survey developer pain points

### Phase 2: Foundation (Week 3-4)

* Implement 3-5 core policies
* Set up [CI/CD integration](/docs/iac/packages-and-automation/continuous-delivery)
* Start with advisory enforcement
* Create documentation and runbooks

### Phase 3: Expansion (Month 2)

* Add [compliance-specific policies](/docs/iac/packages-and-automation/crossguard/compliance-ready-policies)
* Implement [server-side enforcement](/docs/pulumi-cloud/organization/organization-policies)
* Create policy exemption processes
* Measure and track policy effectiveness

### Phase 4: Optimization (Ongoing)

* Monitor policy violations and trends
* Refine policies based on feedback
* Add [automated remediation](/docs/iac/packages-and-automation/crossguard/core-concepts#remediation-policies)
* Expand to new services and teams

## Measuring Policy Success

Track these metrics to validate your policy strategy:

### Security Metrics

* **Policy violation rate**: Percentage of deployments flagged
* **Time to remediation**: How quickly violations are fixed
* **Security incident reduction**: Fewer misconfigurations in production

### Developer Experience Metrics

* **Deployment velocity**: Time from code to production
* **Developer satisfaction**: Survey scores about platform experience
* **Support ticket volume**: Reduction in infrastructure requests

### Operational Metrics

* **Policy coverage**: Percentage of resources under policy control
* **Exemption rate**: How often policies are bypassed
* **Remediation automation**: Percentage of violations auto-fixed

## Common Pitfalls and How to Avoid Them

### Pitfall 1: Over-Engineering Policies

**Problem**: Creating overly complex policies that are hard to understand
**Solution**: Start simple, use clear naming, provide examples

### Pitfall 2: Policy Theater

**Problem**: Implementing policies that don't address real risks
**Solution**: Base policies on actual incidents and security requirements

### Pitfall 3: Poor Developer Experience

**Problem**: Cryptic error messages and no clear remediation steps
**Solution**: Invest in clear documentation and helpful error messages

### Pitfall 4: Inadequate Testing

**Problem**: Policies that break legitimate use cases
**Solution**: Test policies thoroughly with real scenarios before enforcement

## The Future of Policy as Code

As infrastructure becomes more complex, policy as code will evolve to include:

### AI-Enhanced Policies

* **Smart detection**: ML-powered anomaly detection
* **Contextual recommendations**: Policies that adapt based on usage patterns
* **Predictive enforcement**: Catching issues before they become violations

### Cross-Cloud Governance

* **Universal policies**: Rules that work across [AWS](/docs/iac/packages-and-automation/crossguard/compliance-ready-policies-aws), [Azure](/docs/iac/packages-and-automation/crossguard/compliance-ready-policies-azure), [GCP](/docs/iac/packages-and-automation/crossguard/compliance-ready-policies-gcp)
* **Federated enforcement**: Consistent policies across multiple cloud accounts
* **Compliance automation**: Automated evidence collection for audits

### Developer-Centric Policies

* **IDE integration**: Real-time policy feedback during development
* **Self-service exemptions**: Automated approval workflows
* **Learning policies**: Systems that improve based on developer feedback

## Getting Started: Your Action Plan

Ready to implement deployment guardrails? Here's your roadmap:

1. **Assess Current State** (Week 1)
   * Document existing infrastructure patterns
   * Identify security and compliance requirements
   * Survey developer pain points

2. **Create Foundation Policies** (Week 2-3)
   * Implement 3-5 core security policies
   * Set up local policy testing
   * Create clear documentation

3. **Integrate with CI/CD** (Week 4)
   * Add policy validation to pull requests
   * Configure deployment blocking for violations
   * Set up monitoring and alerting

4. **Expand and Optimize** (Month 2+)
   * Add compliance-specific policies
   * Implement server-side enforcement
   * Create exemption and appeals processes

5. **Scale Across Organization** (Month 3+)
   * Extend policies to all teams
   * Add automated remediation
   * Establish policy governance processes

## Conclusion: Enabling Safe Self-Service at Scale

Deployment guardrails with policy as code transform the platform engineering equation. Instead of choosing between speed and safety, you can have both. By automating policy enforcement, you enable developers to move fast while automatically maintaining security, compliance, and operational standards.

The key insight from successful platform teams like Statsig is that **guardrails enable freedom**. When developers know their deployments will be caught if they violate policies, they feel confident making infrastructure changes. When platform teams know policies automatically enforce standards, they can focus on strategic initiatives instead of manual reviews.

Policy as code isn't about restriction—it's about **intelligent automation** that makes the right thing the easy thing.

### Ready to Build Your Guardrails?

* **Explore the demo code**: Check out our [complete policy examples](https://github.com/pulumi/workshops/tree/main/idp-component-policies/demo-policies)
* **Learn more about CrossGuard**: Read the [official documentation](/docs/iac/packages-and-automation/crossguard)
* **Try AWSGuard**: Get started with [pre-built AWS policies](/docs/iac/packages-and-automation/crossguard/awsguard)
* **Explore compliance policies**: Browse our [compliance-ready policy catalog](/docs/iac/packages-and-automation/crossguard/compliance-ready-policies)
* **Get hands-on experience**: Join our [IDP Builder Workshop Series](https://info.pulumi.com/idp/internal-developer-platform-workshops-course)
* **Watch the webinar**: Learn about [policy as code for cloud compliance](https://www.pulumi.com/resources/cloud-compliance-policy-as-code/)
* **Connect with the community**: Join the [Pulumi Slack](https://slack.pulumi.com) #platform-engineering channel

*Next in our series: Day 2 Platform Operations - Automating Drift Detection and Remediation. Learn how to maintain infrastructure compliance after deployment and automatically remediate configuration drift.*

{{< get-started >}}
