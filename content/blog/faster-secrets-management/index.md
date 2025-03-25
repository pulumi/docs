---
title: "Faster Secrets in Pulumi IaC"
date: 2025-03-13T01:00:00-07:00
draft: false
meta_desc: Pulumi IaC now processes stack secrets significantly faster improving deployment
  times without compromising security.
meta_image: meta.png
authors:
  - daniel-bradley
tags:
  - features
  - releases
  - secrets
  - performance
social:
  twitter: "Faster. IaC. Secrets.\nWe've optimized secrets management in Pulumi IaC
    to reduce deployment times while maintaining security. Stacks with many secrets
    can save up to 10 seconds per operation. Update to version 3.155.0 to experience
    these performance improvements."
  linkedin: "Pulumi Infrastructure as Code now processes stack secrets more efficiently,
    reducing deployment times while maintaining robust security. Our latest update
    optimizes encryption and decryption operations through intelligent batching and
    smart change detection, eliminating unnecessary processing during updates. For
    stacks with many secrets, these improvements can save up to 10 seconds per operation,
    which adds up to significant time savings across your deployment pipeline. Update
    to version 3.155.0 today to experience these performance improvements without
    any configuration changes required."
search:
  keywords:
    - secrets
    - iac
    - faster
    - compromising
    - improving
    - significantly
    - processes
---

Pulumi now handles [secrets](https://www.pulumi.com/docs/concepts/secrets/) more efficiently through optimized encryption and decryption processes, reducing deployment times while maintaining security standards. Users of [Pulumi Cloud](https://www.app.pulumi.com) for state management will notice the most improvement due to new batch API capabilities.

<!--more-->

## Secrets Management in Pulumi

Pulumi Infrastructure as Code (IaC)'s built-in secrets management encrypts individual _secrets_ within the stack for fine-grained protection. Pulumi Cloud transmits and stores stack state securely, ensuring that sensitive information—such as database passwords, API keys, and access tokens—remains protected even if someone gains access to your stack file. For organizations with more complex secrets management needs, Pulumi also offers [Pulumi ESC](/product/esc/) (Environments, Secrets, and Configuration), which provides centralized secrets management with hierarchical environments and dynamic credential generation.

Beyond simple encryption, Pulumi tracks the transitive use of secrets to prevent accidental exposure of sensitive values. This tracking works across your entire infrastructure definition, ensuring secrets remain protected:

- Within the stack state
- In CLI output
- In the [Pulumi Cloud console](https://app.pulumi.com/)

When using Pulumi Cloud as your secrets provider, all encryption and decryption operations happen server-side without transmitting the encryption key to the Pulumi program. Combined with Pulumi Cloud's robust user authorization and SSO integration, this creates a comprehensive security framework that ensures only authorized team members can access sensitive information.

## Performance Challenges with Secrets

While security is paramount, performance is equally crucial for developer productivity. Every second spent waiting for encryption or decryption operations is time not spent building and improving your infrastructure.

Previously, when working with stacks containing numerous secrets, users could experience noticeable delays during operations that required encryption or decryption. This was primarily due to:

- Individual network requests for each secret operation
- Network latency compounding with each separate request

For teams with complex infrastructure containing dozens or hundreds of secrets, these delays could add up to significant wait times.

## Our Performance Improvements

We've reduced network overhead by batching encryption work into a single request instead of making separate encryption requests for each secret. This batching approach:

- Reduces the total number of HTTP requests
- Minimizes the impact of network latency
- Allows for more efficient server-side processing

This is combined with identifying when no secrets have changed between intermediate deployment steps to bypass the work of re-encrypting all secrets.

### Measurable Performance Gains

The performance improvements are particularly noticeable for stacks with many secrets or in environments with higher network latency:

| Secrets Count | Network Latency | Typical Time Savings |
|---------------|-----------------|----------------------|
| 10            | 100ms           | ~1 second            |
| 25            | 150ms           | ~4 seconds           |
| 50+           | 150ms           | 10+ seconds          |
| 100+          | 150ms           | 20+ seconds          |

The performance improvements are noticeable for stacks with many secrets or in environments with higher network latency. For teams running CI/CD pipelines with frequent deployments, these savings compound throughout the day, potentially saving significant cumulative wait time across your engineering organization.

## Getting Started

To benefit from these performance improvements:

1. Update to [Pulumi IaC version 3.155.0](https://www.pulumi.com/docs/install/) or later
2. No configuration changes are needed—the optimizations work automatically
3. Ensure you're using Pulumi Cloud as your secrets provider for additional speed gains

These improvements maintain complete backward compatibility with existing stacks and secret values. Your existing encrypted secrets will continue to work without any migration steps required.

## Conclusion

At Pulumi, we're committed to providing both robust security and exceptional performance. These secrets management optimizations represent our ongoing effort to improve the developer experience without compromising on security.

By reducing wait times during encryption and decryption operations, we're helping teams be more productive while maintaining the same high level of protection for sensitive information. This update exemplifies our philosophy that security and performance should complement rather than compete with each other.

## Beyond Stack Secrets: Pulumi ESC

While these performance improvements enhance Pulumi's built-in secrets management, some organizations require more advanced capabilities. If you need secrets to be centrally managed, composable, and reusable across teams and applications, [Pulumi ESC](/product/esc/) (Environments, Secrets, and Configuration) may be a better fit. Pulumi ESC keeps sensitive information out of source control, supports hierarchical environments, and enables dynamic credential generation. It's designed for organizations that need to share secrets between multiple teams, applications, and infrastructure deployments while maintaining strict access controls and auditability.

### Get Started Today

Update to Pulumi IaC 3.155.0 today to experience these performance improvements and [let us know what you think](https://github.com/pulumi/pulumi/issues/new)!
