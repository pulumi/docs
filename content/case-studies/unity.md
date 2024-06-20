---
title_tag: Unity | Case Studies
title: Unity Technologies Modernizes Infrastructure Management
description: |
    By leveraging Pulumi, the Unity Aura team successfully modernized their CI/CD & infrastructure management.
meta_desc: By leveraging Pulumi, the Unity Aura team successfully modernized their CI/CD & infrastructure management.

customer_name: Unity
customer_logo: /logos/customers/unity.png
customer_url: https://unity.com/

exec_summary: |
    tbd

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: Introduction
      anchor: introduction
    - label: Migrating Jenkins to Amazon EKS
      anchor: migration
    - label: Adopting GitHub Actions Self-Hosted Runners for CI/CD
      anchor: adopting-github-actions
    - label: Empowering Developers with Pulumi's Automation API
      anchor: empowering-developers
    - label: Ensuring Consistency and Preventing Drift with Automation API
      anchor: preventing-drift
    - label: Efficiency Gains Over Other IaC Tools
      anchor: efficiency
    - label: Speeding up Projects with Pulumi Copilot
      anchor: copilot
    - label: Results
      anchor: results
    - label: Conclusion
      anchor: conclusion
---

## About Unity

tbd

## Introduction

[Unity](https://unity.com/) is the world's leading platform for creating and operating interactive, real-time 3D (RT3D) content. In November 2022, Unity merged with ironSource to help mobile content creators prosper with a leading business platform designed to turn any app into a successful business. Today, 84 of the top 100 games use the [Unity Grow](https://unity.com/grow) platform as part of their monetization strategy.

The [Aura](https://unity.com/solutions/device-management) division within Unity supports engaging telcos, operators and their clients throughout the mobile device lifecycle. Aura’s DevOps team wanted to modernize their developer platform and CI/CD systems to improve performance, control costs and simplify the process of version upgrades. Their legacy Jenkins service was hard to maintain, and they needed a robust solution to streamline their CI/CD processes, enable self-service for developers, and maintain infrastructure integrity.

Aura turned to Pulumi to automate infrastructure management, reduce deployment times, and boost overall team productivity by enabling more team members to write and deploy infrastructure as code using their standard software release process and preferred programming language: TypeScript.

## Migrating Jenkins to Amazon EKS {#migration}

The Aura DevOps team’s journey with Pulumi began with the migration of their Amazon ECS services to EKS and one of those services is their aging [Jenkins](https://www.jenkins.io/) service. The original service relied on ECS with a lot of manual Jenkins configuration required.  The team wanted to manage Jenkins configuration using source control and follow the release process used for all other software development. They also wanted better performance and cost improvements made possible by moving to EKS. Using Pulumi's infrastructure as code (IaC) capabilities, the DevOps team was able to quickly provision a new Jenkins instance along with associated service accounts, networking, and IAM roles. The team also configured Cloudfront and WAF to enable Jenkins to connect with GitHub. Finally, they utilized the Karpenter provisioner Custom Resource Definition (CRD) to automate the process of provisioning and deprovisioning nodes, depending on the scheduling requirements of the pods that served as Jenkins agents. The configuration for Jenkins was maintained as Pulumi stack configuration. This approach simplified the application of source control, made tracking changes more straightforward, and facilitated the deployment of updates to Jenkins.

The new EKS-based architecture improved execution time and made it easier for the team to upgrade Jenkins versions faster to take advantage of new features. The team also used Pulumi to implement AWS resource tagging – making it easier for their FinOps team to track costs at a more granular level.

## Adopting GitHub Actions Self-Hosted Runners for CI/CD {#adopting-github-actions}

Despite these improvements, Jenkins upgrades and plugin management continued to be a burden and the team decided to use a more modern system that would offer a simpler setup process and easier maintenance compared to Jenkins.

To further accelerate deployment times, and to maintain security best practices, Aura adopted [GitHub Actions](https://github.com/features/actions/) with self-hosted runners on EKS. Once again, the team used Pulumi to manage the EKS and workload deployments and related AWS resources. To improve performance, the team broke up monolithic Jenkins jobs into smaller tasks in GitHub Actions.

<img class="block mx-auto md:max-w-4xl my-8"
src="/images/case-studies/unity-gh-diagram.png" alt="Unity GitHub Actions diagram">

## Empowering Developers with Pulumi's Automation API {#empowering-developers}

One of Aura's core goals was to enable their developers to self-serve cloud infrastructure in a process that’s tightly coupled with their existing development process on GitHub. By leveraging Pulumi's Automation API and reusable infrastructure libraries, Aura’s DevOps team provided developers with custom CLI-based tools they needed to deploy and manage infrastructure independently. This enhanced developer productivity and reduced the dependency on DevOps team resources for creating new infrastructure. Because Pulumi enabled the DevOps team and developers to standardize on one language: TypeScript, everyone could understand and contribute to infrastructure improvements in this model.

The benefit to developers is that they can independently provision new cloud resources to test their product and deliver new features faster.

## Ensuring Consistency and Preventing Drift with Automation API {#preventing-drift}

To give all stakeholders confidence in the infrastructure provisioning process, the team uses `pulumi preview` and `pulumi refresh` from its Automation API workflow to detect and correct drift. This capability runs whenever a developer initiates a deployment and ensures that any unauthorized modifications are promptly identified and addressed, safeguarding the integrity of the development environment - bringing the infrastructure back in line with the desired state defined in the Pulumi program.

## Efficiency Gains Over Other IaC Tools {#efficiency}

The DevOps team estimates that Aura's infrastructure projects were completed faster using Pulumi compared to an equivalent effort using other tools in the market. “If we take Terraform for instance, it relies on HCL and lacks support for Object Oriented Programming (OOP) concepts like classes, objects, inheritance,” says Eilon Ashkenazi, DevOps Engineer on the Aura team. “An equivalent deployment would take significantly more lines of infrastructure code to implement while yielding IaC that is less reusable.”

In a previous approach, a typical client-facing service deployed with Ansible and console updates could take up to a week or more for DevOps to set up new environments for developers and now developers are able to self-serve new environments that fit their needs in a few hours (and potentially faster for simpler deployments).

The ease of use and collaboration with developers using TypeScript, coupled with Pulumi’s powerful automation features, allowed Aura to achieve their CI/CD modernization and infrastructure management goals quickly, without the need for the developers to learn an unfamiliar syntax such as HCL or YAML.

## Speeding up Projects with Pulumi Copilot {#copilot}

The team has had early success using Pulumi Copilot to augment their efforts. For example, a developer needed to set up a DocumentDB instance but an equivalent component was missing from the standard `pulumi-kit` provided by DevOps (the Aura team’s TypeScript package for Pulumi components). Using Pulumi AI, the developer was able to quickly understand the steps needed to create this new resource type and self-serve a reference implementation for their development environment. This helped remove DevOps as a bottleneck and accelerate development while the team could focus on formalizing updates to `pulumi-kit` for production.

## Results

- **Reduced Infrastructure provisioning time:** Migration to Amazon EKS and GitHub Actions self-hosted runners significantly speed up the process of provisioning new infrastructure components for the developers.
- **Increased Developer Autonomy:** Pulumi's Automation API and infrastructure libraries empowered developers to self-serve cloud infrastructure following best practices.
- **Enhanced Infrastructure Integrity:** Pulumi Automation API ensured consistent and reliable infrastructure.
- **Boosted Productivity:** Pulumi AI accelerated development cycles by removing bottlenecks - turning week-long processes into hours (or less).

## Conclusion

By leveraging Pulumi, the Unity Aura team successfully modernized their CI/CD & infrastructure management, resulting in faster deployments, increased developer autonomy, and enhanced infrastructure integrity. The partnership with Pulumi has positioned Aura from Unity for continued success and innovation in the competitive gaming and mobile industries.
