---
title: Setting up for success
meta_desc: Make key decisions about security, testing strategies, and code reusability that will set your team up for success.
aliases:
  - /docs/pulumi-cloud/get-started/onboarding-guide/setting-up-for-success/
  - /docs/deployments/get-started/onboarding-guide/setting-up-for-success/
weight: 3
menu:
    administration:
        name: Setting up for success
        parent: pulumi-onboarding-guide
        identifier: setting-up-for-success
---
Before creating projects and shipping to the cloud, make key decisions that will set your team up for success. Focus on security, testing strategies, and code reusability: all the essential considerations for scaling infrastructure as code effectively.

## Secure your infrastructure from day one

Security is a team effort that's best established from the outset. Pulumi Cloud makes it easy to adopt security best practices during team onboarding.

### Choose your compliance approach

Modern enterprises face rigorous compliance requirements. Pulumi Cloud is SOC 2 Type II certified and AWS-reviewed for compliance best practices. The infrastructure hosting Pulumi Cloud aligns with IT security standards including SOC 1/SSAE 16/ISAE 3402, SOC 2, SOC 3, FISMA, FedRAMP, DOD SRG Levels 2 and 4, PCI DSS Level 1, EU Model Clauses, ISO 9001/27001/27017/27018, ITAR, IRAP, FIPS 140-2, MLPS Level 3, and MTCS. Learn more at [Pulumi Security](https://www.pulumi.com/security/).

Use Pulumi's Policy as Code engine, [CrossGuard](https://www.pulumi.com/docs/iac/crossguard/), to enforce compliant infrastructure practices. CrossGuard includes hundreds of out-of-the-box policies for AWS, Azure, Google Cloud, and Kubernetes, spanning PCI DSS, ISO 27001, SOC 2, HITRUST, and CIS Benchmarks. You can also write custom policies for your specific industry or enterprise requirements.

CrossGuard identifies issues in existing cloud infrastructure and prevents new problems from being introduced. Configure it at various warning and error levels, and apply it flexibly across projects—for example, GDPR rules might only apply to infrastructure in European regions. CrossGuard also features automatic remediations.

Pulumi Cloud maintains an audit log of every activity and who performed it for complete visibility.

### Select your cloud authentication method

Pulumi supports hundreds of cloud providers, though most organizations use AWS, Azure, Google Cloud, and Kubernetes. Other supported providers include SaaS infrastructure products like Cloudflare, DataDog, MongoDB, and Snowflake, plus on-premises technologies like VMware vSphere. Find the complete list in the [Pulumi Registry](https://pulumi.com/registry), your one-stop shop for provider documentation and configuration guidance.

**Recommended approach:** Use Pulumi ESC's OpenID Connect (OIDC) support for [dynamic, short-lived credentials](https://www.pulumi.com/docs/esc/integrations/dynamic-login-credentials/). This is the most secure method and should be preferred for supported providers.

**Alternative approach:** If your chosen cloud lacks Pulumi ESC OIDC support, consult the registry documentation. Each provider has an "Install & config" section with authentication guidance. See [AWS Installation & Configuration](https://www.pulumi.com/docs/esc/integrations/dynamic-login-credentials/) as an example. Pulumi uses native tools and techniques for authentication, keeping it consistent with your existing usage patterns.

## Test your infrastructure code

Infrastructure as code is code and should be tested. This yields more predictable deployments, increases confidence, and minimizes costly mistakes. Pulumi's use of standard languages gives you access to entire ecosystems of testing tools and techniques.

### Choose your testing strategy

Implement a three-tier testing approach:

**Unit tests** test targeted functionality without deploying actual cloud infrastructure. These are part of your inner development loop and run quickly. Pulumi makes it easy to mock cloud capabilities for this testing.

**Policy as Code** acts as a form of testing that blocks deployments failing to meet predetermined policies. This was covered in your security decisions above.

**Integration tests** coordinate with actual Pulumi deployments to verify that real infrastructure is provisioned to specification.

### Consider advanced testing techniques

Build sophisticated test strategies on this foundation. Options include fuzz testing to verify your infrastructure configurations react correctly to varying inputs, or chaos testing that destroys infrastructure components to test system responses.

Also consider using linters and static analysis tools to enforce industry standards and your team's coding guidelines. See the [Testing Pulumi programs guide](https://www.pulumi.com/docs/iac/guides/testing/) for more details.

## Share and reuse code effectively

Pulumi projects, stacks, and environments help reduce "sprawl"—the copy-and-paste configurations that legacy IaC tools create. Sprawl causes unintended drift between environments and can lead to outages and security mistakes.

### Choose your abstraction level

**[Components](https://www.pulumi.com/docs/iac/concepts/components/)** are IaC resources you define to abstract and encapsulate one or more other resources. For example, an AWS Virtual Private Cloud (VPC) might consist of dozens of resources: public and private subnets, Internet and NAT Gateways, the VPC itself, and more. Rather than coding the VPC definition in every project—potentially hundreds or thousands of lines of code—use a component. The Pulumi AWSX package offers a VPC component out of the box, but you can create your own by subclassing the component resource base class.

Components provide all the benefits of native language packages: storage in package managers, versioning, secure dependencies, and more.

**[Templates](https://www.pulumi.com/docs/idp/concepts/organization-templates/)** are blueprints that scaffold entirely new projects. While components encapsulate cloud resource usage patterns, templates provide standard starting points for complete projects with many resources. [Pulumi offers templates](https://www.pulumi.com/templates/) for common architectures and patterns, but you can create your own. You can also register your organization's templates in the Pulumi Cloud New Project Wizard for easy access.

### Make the decision

Start with existing components and templates, then create custom ones as your team identifies common patterns. This approach ensures consistency and reduces maintenance overhead as you scale.

{{< get-started-stepper >}}
