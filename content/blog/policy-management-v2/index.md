---
title: "Introducing Policy Management 2.0"
date: 2025-09-15
authors:
    - luke-ward
meta_desc: "Discover the new, streamlined user experience for Pulumi Policy as Code (CrossGuard)."
meta_image: "meta.png"
tags:
    - pulumi-service
    - policy-as-code
    - crossguard
    - features
    - user-experience
---

Pulumi's Policy as Code solution, CrossGuard, is a powerful tool for enforcing compliance, security, cost, and best practices across your infrastructure. It allows you to programmatically define and enforce rules for your cloud resources. However, as more and more users have adopted CrossGuard, we've heard your feedback that the user experience for discovering, applying, and managing policies could be much simpler.

Today, we're excited to announce a fundamental redesign of the CrossGuard UX in the Pulumi Service, aimed at making it more intuitive, discoverable, and scalable.

<!--more-->

## The Challenges with Policy Management

Based on your feedback, we identified several key areas of friction in the existing Policy as Code workflow:

* **Difficult Discovery:** Finding and trying out available policy packs was a cumbersome, multi-step process. Users had to navigate a console wizard, then switch to the CLI to run `pulumi policy new` and `pulumi policy publish` just to see a policy pack in the Pulumi Service. This context-switching was a major hurdle to exploration.
* **Complex Application Workflow:** Applying a policy was too complex. It involved publishing the policy, creating a "Policy Group," adding the policy pack to that group, and then manually associating stacks or accounts with that group. While Policy Groups offer powerful ways to bundle policies, the initial setup process was a barrier for many.

## A New, Simplified Approach

Our primary goal is to increase the adoption of Pulumi CrossGuard by lowering the barrier to entry and making policies easier to work with. The new experience is built around a simple principle: a streamlined, in-console experience for discovery and management.

### In-Console Discoverability

We are making it dramatically easier to find and understand policy packs. You can now browse a rich marketplace of policy packs directly within the Pulumi Service—no CLI required for Pulumi- or Partner-authored packs.

You’ll find:

* **A rich browsing experience:** See all available policy packs in one place.
* **Detailed information:** Each pack comes with a detailed description, the policies included, configuration options, and usage instructions.
* **Organization-approved packs:** Org admins can curate a list of approved policy packs for your organization, ensuring that your teams are using a vetted set of policies.

### Streamlined Policy Management

With policies being easier to discover and understand, managing them within your organization becomes simpler. The improved visibility allows administrators to quickly see which policies are available and curate the right set of approved policies for their teams. This makes the process of adding them to Policy Groups and applying them to stacks more straightforward and less error-prone.

## Management and Permissions

The new experience also comes with improved management and permission features:

* **Versioning:** All policy packs are versioned, so you have a clear history of changes and can control which version of a pack is applied.
* **Permissions:** We are introducing more granular permissions for policy management. Organization admins can control who can read and write policies, enabling security teams and auditors to manage and review policies without needing full admin privileges.

## What's Next?

This is just the beginning of our journey to create a best-in-class Policy as Code experience. We will continue to invest in making the entire lifecycle of policy management—from authoring and discovery to application and reporting—a seamless and powerful experience for every member of your team.

## Conclusion

The new Pulumi CrossGuard experience is a major step forward in making Policy as Code accessible, scalable, and easy to use. By focusing on discoverability and a simplified workflow, we've removed major points of friction that stood in the way of adopting a secure-by-default infrastructure.

We'd love for you to try out the new Pulumi Service console! Don't hesitate to reach out on the [Pulumi Community Slack](https://slack.pulumi.com/) to share your thoughts. We look forward to hearing what you think of these changes!
