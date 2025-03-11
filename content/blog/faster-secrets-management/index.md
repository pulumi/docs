---
title: "Faster Stack Secrets in Pulumi IaC"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-03-10

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Pulumi IaC now processes stack secrets significantly faster improving deployment times without compromising security.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - daniel-bradley

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - features
    - releases
    - secrets
    - performance

# The social copy used to promote this post on Twitter and Linkedin. These
# properties do not actually create the post and have no effect on the
# generated blog page. They are here strictly for reference.

# Here are some examples of posts we have made in the past for inspiration:
# https://www.linkedin.com/feed/update/urn:li:activity:7171191945841561601
# https://www.linkedin.com/feed/update/urn:li:activity:7169021002394296320
# https://www.linkedin.com/feed/update/urn:li:activity:7155606616455737345
# https://twitter.com/PulumiCorp/status/1763265391042654623
# https://twitter.com/PulumiCorp/status/1762900472489185492
# https://twitter.com/PulumiCorp/status/1755637618631405655

social:
    twitter: "Faster. Stack. Secrets.
    
    We've optimized secrets management in Pulumi IaC to reduce deployment times while maintaining security. Stacks with many secrets can save up to 10 seconds per operation. Update to version 3.x to experience these performance improvements."
    linkedin: "Pulumi Infrastructure as Code now processes stack secrets more efficiently, reducing deployment times while maintaining robust security. Our latest update optimizes encryption and decryption operations through intelligent batching and smart change detection, eliminating unnecessary processing during updates. For stacks with many secrets, these improvements can save up to 10 seconds per operation, which adds up to significant time savings across your deployment pipeline. Update to version 3.x today to experience these performance improvements without any configuration changes required."

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

Pulumi now handles [stack secrets](https://www.pulumi.com/docs/concepts/secrets/) more efficiently through optimized encryption and decryption processes, reducing deployment times while maintaining security standards. Users of [Pulumi Cloud](https://www.pulumi.com/product/pulumi-cloud/) for state management will notice the most improvement due to new batch API capabilities.

<!--more-->

## Secrets Management in Pulumi

Pulumi Cloud transmits and stores stack state securely and in addition encrypts individual _secrets_ within the stack for more fine-grained protection. This encryption ensures that sensitive information—such as database passwords, API keys, and access tokens—remains protected even if someone gains access to your stack file.

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

1. Update to [Pulumi IaC version 3.x](https://www.pulumi.com/docs/install/) or later
2. No configuration changes are needed—the optimizations work automatically
3. Ensure you're using Pulumi Cloud as your secrets provider for additional speed gains

These improvements maintain complete backward compatibility with existing stacks and secret values. Your existing encrypted secrets will continue to work without any migration steps required.

## Conclusion

At Pulumi, we're committed to providing both robust security and exceptional performance. These secrets management optimizations represent our ongoing effort to improve the developer experience without compromising on security.

By reducing wait times during encryption and decryption operations, we're helping teams be more productive while maintaining the same high level of protection for sensitive information. This update exemplifies our philosophy that security and performance should complement rather than compete with each other.

Update to Pulumi IaC 3.x today to experience these performance improvements and [let us know what you think](https://github.com/pulumi/pulumi/issues/new)!
