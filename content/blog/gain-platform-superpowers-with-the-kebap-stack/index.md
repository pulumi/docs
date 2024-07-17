---
title: "Platform Superpowers With the KEBAP Stack"
date: 2024-07-22
draft: false
allow_long_title: true
meta_desc: "The KEBAP stack is a standardized GitOps stack that combines Kubernetes, External Secrets Operator, Backstage, Argo CD, and Pulumi. Learn how it can help you streamline your software delivery process."
meta_image: meta.png

authors:
- engin-diri

tags:
- kubernetes
- external-secrets-operator
- backstage
- argo-cd
- pulumi
- kyverno
- gitops

social:
  twitter: "The KEBAP stack is a standardized GitOps stack that combines Kubernetes, External Secrets Operator, Backstage, Argo CD, and Pulumi. Learn how it can help accelerate your platform engineering efforts."
  linkedin: |
    The KEBAP stack is a standardized GitOps stack that combines:
    - Kubernetes
    - External Secrets Operator
    - Backstage
    - Argo CD
    - Pulumi

    Learn how it can help you streamline your software delivery process by using standard tools and practices across your infrastructure projects. 

    This helps reduce the time required to establish development and production environments from months to minutes. #GitOps #Kubernetes #ArgoCD #Pulumi #Backstage
---

At Pulumi's Customer Experience Team, we frequently assist software infrastructure teams in transitioning from
traditional software delivery paradigms to Cloud Native approaches. Most of our customers use the introduction of an
infrastructure as code tool as a starting point to reevaluate their entire software delivery process and adopt a more
streamlined, automated, and secure approach.

While the CNCF landscape remains as complex as ever and new tools are introduced daily, we've found that a recurring
pattern in our solutions. We've distilled this pattern into a standardized stack that we call the `KEBAP` stack, because
who doesn't love a good kebap after a long day of coding?

## What's in the KEBAP Stack?

The `KEBAP` stack consists of the following components:

- **K**ubernetes (with Kyverno as a bonus)
- **E**xternal Secrets Operator
- **B**ackstage
- **A**rgo CD
- **P**ulumi

This combination forms a standardized GitOps stack applicable to various infrastructure projects. By implementing the
`KEBAP` stack, we've consistently reduced the time required for teams to establish development and production
environments from months to minutes.

## Let's Break It Down

Let's take a closer look at each component of the `KEBAP` stack and understand how they work together to streamline the
software delivery process.

The five layers of the `KEBAP` stack are designed to address different aspects of the software delivery process:

### Kubernetes

Kubernetes serves as the orchestration layer. It's now the dominant container orchestration platform across the
industry. Kubernetes provides a declarative framework for managing the infrastructure on which your applications will
run, ensuring that your application deployment configuration is fully automated and auditable.

### External Secrets Operator (ESO)

ESO addresses the challenge of securely managing secrets in Kubernetes. It integrates with various secret stores (such
as AWS Secrets Manager, HashiCorp Vault, Google Secrets Manager, Azure Key Vault) in a consistent way. This allows you
to configure access to the secret store once for all your required secrets, enhancing security and simplifying
management.

### Backstage

Backstage is an open platform for building developer portals. It provides a centralized place for managing software
catalogs, documentation, and tooling. This layer helps in organizing microservices and infrastructure, streamlining the
process for developers to create, manage, and explore services.

### Argo CD

Argo CD handles the deployment layer, ensuring that the current deployment matches what is declaratively defined in the
source. It's emerging as the de facto standard due to its rich front-end and powerful features. Argo CD implements the
GitOps model, continuously monitoring your Git repositories and automatically updating the deployed applications to
match the desired state.

### Pulumi

Pulumi manages the definition of the infrastructure. It allows you to use familiar programming languages to define your
infrastructure as code, providing more flexibility and power than traditional YAML or domain-specific languages. The
Pulumi Kubernetes Operator enables you to manage your infrastructure directly from within Kubernetes, offering seamless
integration with your existing Kubernetes workflows.

### Bonus: Kyverno

As a bonus, Kyverno can be used to enforce policies and automate security and operational best practices in Kubernetes
clusters. Kyverno is a policy engine designed for Kubernetes that allows you to define policies as code and enforce them
at runtime. This ensures that your Kubernetes clusters are secure and compliant with your organization's policies.

## Putting all the Pieces Together

The `KEBAP` stack fulfills the requirements of a robust GitOps implementation:

1. Kubernetes provides the 'declarative infrastructure' through its use of YAML to define the cluster configuration.
2. Applications run as immutable and versioned containers on these declaratively-defined clusters.
3. Argo CD serves as the GitOps 'agent', ensuring deployments match the defined state.
4. Pulumi provisions the supporting infrastructure and bootstraps the running application platform.
5. Backstage offers a developer portal for service management and discovery.
6. External Secrets Operator ensures secure and consistent secrets management across different environments.

All components are version-controlled in Git, ensuring auditability and traceability.

## The End Result

The `KEBAP` stack results in a secure, automated, auditable, reproducible, and programmable set of
environments for building, testing, and operating software. This leads to significant cost savings by automating
processes that previously required manual intervention and substantial time investment.

The `KEBAP` stack also facilitates:

- Consistent environments across development, staging, and production
- Improved security through automated secret management and policy enforcement
- Faster onboarding for new team members
- Easier compliance with regulatory requirements due to increased auditability

If you're interested in real-world applications of the `KEBAP` stack, we have numerous case studies and examples to share.
Feel free to reach out for more information on how this approach can benefit your organization.
