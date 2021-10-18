---
title: Sourcegraph
description: |
    Pulumi helps to supercharge Kubernetes deployments at Sourcegraph, ensuring their team has continuous access to the latest builds.
meta_desc: |
    Pulumi helps to supercharge Kubernetes deployments at Sourcegraph, ensuring their team has continuous access to the latest builds.

customer_name: Sourcegraph
customer_logo: /logos/customers/sourcegraph-logo.svg
customer_url: https://about.sourcegraph.com/

exec_summary: |
    Sourcegraph selects Pulumi to deploy its latest software on Google Kubernetes Engine --- eliminating deployment headaches and ensuring their team has continuous access to the latest builds.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: Supercharged Deployments
      anchor: supercharged-deployments
    - label: Best-in-class Development Tools
      anchor: best-in-class-development-tools
    - label: Deploy to GKE with Pulumi
      anchor: deploy-to-gke-with-pulumi
---

## About Sourcegraph

Sourcegraph’s mission is to empower everyone to be able to build software. Its Universal Code Search platform makes the entire codebase of an organization accessible to every single developer and DevOps team member. This makes it easy to dive into unfamiliar parts of the code, discover and share reusable packages, make code reviews fast and thorough, cut down incident response time, and enforce security and code-quality best practices. Sourcegraph encourages knowledge sharing and boosts engineering velocity, helping your team ship higher-quality code, faster.

## Supercharged Deployments

Just as the Pulumi team uses its own technology to [build Pulumi]({{< relref "/blog/how-we-use-pulumi-to-build-pulumi" >}}), the Sourcegraph team uses Sourcegraph as an integral part of building its product. Having team members leverage pre-release versions in their day-to-day work ensures that each new version gets put through its paces before it reaches customers. This process, often known as [self-hosting or 'dogfooding'](https://en.wikipedia.org/wiki/Eating_your_own_dog_food), is a common practice within technology companies and it requires that the development team has access to the latest pre-release software. Given this requirement, rapid deployments are critical to ensure that the latest version is in use and that deployments don’t delay development.

Sourcegraph selected Pulumi to deploy their latest versions to [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine) (GKE), ensuring that their deployments are quick, secure, and always available. This keeps the development team productive while they use and validate each new release. Specifically, Pulumi helped Sourcegraph automate deploying and managing the primary dogfood instance of the Sourcegraph service. This helped improve the deployment process by simplifying multi-user configuration changes --- increasing the team’s confidence in each deployment.

> "Pulumi has changed how our team works by giving us deployment superpowers. It’s great to run ‘pulumi up’ and not have to worry about deploying an invalid configuration."

> --- Beyang Liu, Sourcegraph CTO

## Best-in-class Development Tools

Pulumi simplifies Sourcegraph deployments in many ways. One key benefit is that it was far easier to configure and manage Kubernetes using TypeScript and modern development environments instead of writing (and then troubleshooting!) YAML. The team’s new deployment workflow is far simpler than what they previously experienced with text-based configuration. Using Pulumi helps Sourcegraph's team frequently deploy new versions with confidence and eliminates deployment errors that previously meant spending hours debugging.

The main benefits of working with programming languages instead of domain-specific languages include: proper logic constructs and object references to compose interconnected API resources, reusability of common modules, and clear end-to-end orchestration of infrastructure. Using existing IDEs, compilers, and linters to catch issues and incompatibilities further boosts team velocity.

By adopting Pulumi, the team is able to achieve their rapid deployment goals while using the same tools that they know, love, and use every day developing Sourcegraph for creating and managing all of their cloud infrastructure needs.

[Learn more about Sourcegraph.](https://about.sourcegraph.com)

## Deploy to GKE with Pulumi

Just like Sourcegraph, you can use Pulumi to deploy your applications to GKE in a snap. Learn how to acquire your deployment superpowers here: [GKE + Pulumi]({{< relref "/registry/packages/kubernetes/how-to-guides/gke" >}}).
