---
title: "Best Secrets Management Tools in 2026"
date: 2026-07-30
draft: false
meta_desc: "Compare the best secrets management tools of 2026: Vault, cloud-native managers, Pulumi ESC, Doppler, and Infisical, on scope, operations, and cost."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - secrets-management
    - security
    - esc
    - platform-engineering
    - devops
category: general
faq_schema: true
---

Almost every security incident that starts with a leaked credential traces back to the same root cause: a secret that was stored somewhere it shouldn't have been, copied into somewhere worse, and then forgotten. [Secrets management](/what-is/what-is-secrets-management/) is the practice of keeping credentials, API keys, tokens, and certificates out of source code and configuration files, storing them in a system built to encrypt, access-control, audit, and rotate them instead.

<!--more-->

The category has expanded well beyond "a place to put passwords." Modern teams rarely operate on a single cloud, so secrets end up spread across AWS, Azure, and Google Cloud native stores, a self-hosted Vault cluster, a SaaS vendor or two, and the environment variables in every CI pipeline. The tools below approach that reality from different angles: cloud-native managers optimize for depth within one provider, general-purpose secret stores like Vault optimize for breadth and dynamic credentials, developer-first SaaS tools optimize for ease of use, and configuration-layer tools optimize for giving teams one consistent interface across everything they already run. Here are the leading options in 2026 and where each one fits.

## Pulumi ESC

[Pulumi ESC](/product/esc/) (Environments, Secrets, and Configuration) takes a different position from most tools on this list: rather than being one more place to store secrets, it's a configuration and secrets layer that composes the stores you already use. Environments are defined as hierarchical, versioned documents that can pull values from AWS Secrets Manager, Azure Key Vault, Google Secret Manager, HashiCorp Vault, 1Password, and others, then expose them to applications, CI/CD, and infrastructure code through one consistent interface, whether that's the CLI (`esc run`), SDKs, environment variables, or a file.

Its distinguishing feature is dynamic credentials: instead of storing long-lived cloud access keys at all, ESC uses OIDC to generate short-lived credentials on demand, which sidesteps the rotation problem by removing the standing secret. The CLI is open source, and ESC works independently of whether you use Pulumi for infrastructure as code.

The tradeoff is that ESC is a composition and orchestration layer, not a low-level secret store with its own encryption engine and secrets-engine ecosystem the way Vault is. Teams that need a single native store on one cloud, and nothing more, may find a cloud-native manager simpler; ESC earns its place specifically when secrets and configuration are spread across multiple backends and teams want to stop managing each one separately.

## HashiCorp Vault

[HashiCorp Vault](/what-is/what-is-hashicorp-vault/) is the most established general-purpose secrets management platform, and for many organizations it's still the reference point every other tool is measured against. Beyond static secret storage, Vault provides dynamic secrets (generating short-lived database credentials, cloud IAM credentials, and PKI certificates on demand), encryption as a service, and a large ecosystem of secrets engines and auth methods that cover almost any backend.

That breadth is also its cost. Running Vault yourself means operating a highly available, correctly sealed and unsealed, carefully access-controlled distributed system, which is a real platform-team responsibility rather than a set-and-forget service. HashiCorp offers HCP Vault as a managed option to offload that burden, and following HashiCorp's 2023 move to the Business Source License, the community fork [OpenBao](https://openbao.org/) now exists under the Linux Foundation for teams that want Vault's model under permissive open-source governance. Vault remains the strongest choice for teams that genuinely need dynamic secrets and encryption-as-a-service at scale and have the platform capacity to operate it. For a direct feature comparison, see [Pulumi ESC vs. HashiCorp Vault](/docs/esc/vs/vault/).

## AWS Secrets Manager

[AWS Secrets Manager](/what-is/what-is-aws-secrets-manager/) is AWS's native service for storing and rotating secrets, tightly integrated with IAM for access control and KMS for encryption. Its standout capability is built-in automatic rotation: for supported services like RDS, it can rotate database credentials on a schedule using managed Lambda functions, with no rotation logic for your team to write.

The natural limit is scope. Secrets Manager is an AWS service, so its identity model, integrations, and console experience assume an AWS-centric world; teams running workloads on more than one cloud will need a second store for everything outside AWS. Pricing is per secret per month plus API calls, which is inexpensive for a handful of secrets but worth modeling if you generate large numbers of them. For AWS-only teams that want rotation handled natively, it's a strong default; if you're weighing whether to move beyond it, the cross-cloud and configuration-layer options on this list are the ones worth comparing.

## Azure Key Vault

[Azure Key Vault](/what-is/what-is-azure-key-vault/) is Microsoft's native offering for secrets, encryption keys, and certificates, with the distinction that it manages all three in one service. It integrates with Azure RBAC and managed identities for access control, supports HSM-backed keys for workloads with hardware-security requirements, and handles certificate lifecycle management including issuance and renewal through integrated certificate authorities.

Like the other cloud-native managers, its center of gravity is its own platform: Key Vault is the obvious choice for teams standardized on Azure, and less natural as a cross-cloud store. Its combined handling of keys, secrets, and certificates makes it particularly appealing when certificate management is a first-class need rather than an afterthought.

## Google Cloud Secret Manager

[Google Cloud Secret Manager](/what-is/what-is-google-cloud-secret-manager/) is GCP's native secrets service, built around a clean, versioned model where each secret holds immutable versions you enable, disable, or destroy explicitly. It integrates with Cloud IAM for fine-grained access control and supports both automatic and user-managed replication policies for controlling where secret data is stored regionally.

Its scope, again, is its own cloud. For teams on Google Cloud, it's a straightforward, well-designed native option; its explicit versioning model is a genuine strength for auditability, since every change produces a discrete, addressable version rather than mutating a value in place.

## Doppler

[Doppler](/docs/esc/vs/doppler/) is a SaaS secrets manager built around developer experience, with a polished dashboard, a strong CLI, and a wide catalog of integrations that sync secrets into cloud providers, CI/CD systems, and hosting platforms. Its model of projects and environment-specific configs maps cleanly onto how teams already think about dev, staging, and production, and its secret-referencing feature lets one config inherit from another to reduce duplication.

The tradeoff is that Doppler is a proprietary SaaS platform, so teams with strict data-residency or self-hosting requirements will need to weigh that, and its focus is secret storage and sync rather than the dynamic-credential generation that Vault or a configuration layer like ESC provide. For teams that prioritize fast onboarding and a clean developer workflow over self-hosting control, it's a popular and capable choice.

## Infisical

[Infisical](/docs/esc/vs/infisical/) is an open-source secrets management platform that has grown quickly with teams who want a modern developer experience without committing to a proprietary SaaS. It can be self-hosted or used as a managed cloud service, and it pairs secret storage with features like automatic secret rotation, dynamic secrets for some backends, and built-in secret scanning to catch credentials accidentally committed to Git.

Being open source is its central appeal: teams that want to inspect, self-host, and avoid vendor lock-in get that here in a way the proprietary SaaS options can't match. The tradeoff is maturity and ecosystem depth relative to Vault, which has a longer track record and a wider set of enterprise integrations; for many teams that gap is shrinking and worth trading for the openness and lighter operational model.

## 1Password Secrets Automation

1Password Secrets Automation extends the [1Password](https://1password.com/) password manager many organizations already use into machine and infrastructure access, using Connect servers and service accounts to let applications and pipelines read secrets from 1Password vaults programmatically. For teams already standardized on 1Password for human credential storage, it offers a way to unify human and machine secrets under one system and one audit trail.

Its natural fit is exactly that scenario. If 1Password isn't already in your stack, adopting it primarily as an infrastructure secrets store is a less obvious fit than a purpose-built platform, but the appeal of one consistent vault for both people and services is real for organizations that have invested in it.

## CyberArk Conjur

CyberArk Conjur is a secrets management platform aimed squarely at the enterprise and security-first end of the market, with a heritage in privileged access management. It focuses on machine identity, strong role-based access control, detailed audit trails, and policy-as-code definitions for who and what can access which secrets, which makes it a common choice in regulated industries with demanding compliance requirements.

That enterprise orientation is both its strength and its threshold. Conjur (available as an open-source edition and a commercial enterprise product) brings the governance and audit depth large security organizations require, at the cost of more setup and operational investment than the developer-first tools on this list. Teams whose primary driver is compliance and centralized privileged-access control will find it well-suited; smaller teams optimizing for speed usually won't need its depth.

## Comparison table

| Tool | Type | Scope | Dynamic secrets | Hosting | Best for |
|---|---|---|---|---|---|
| Pulumi ESC | Configuration & secrets layer | Cross-cloud, composes other stores | Yes, via OIDC (no standing keys) | Managed; open-source CLI | Unifying secrets and config across multiple backends and clouds |
| HashiCorp Vault | General-purpose secrets platform | Cross-cloud, broad backends | Yes, extensive | Self-hosted or HCP Vault (managed) | Dynamic secrets and encryption-as-a-service at scale |
| AWS Secrets Manager | Cloud-native manager | AWS | Rotation for supported services | Managed by AWS | AWS-only teams wanting native rotation |
| Azure Key Vault | Cloud-native manager | Azure | Limited | Managed by Azure | Azure teams needing secrets, keys, and certificates together |
| Google Cloud Secret Manager | Cloud-native manager | Google Cloud | No native dynamic secrets | Managed by GCP | GCP teams wanting a clean, versioned native store |
| Doppler | Developer-first SaaS | Cross-platform via integrations | No | Managed SaaS | Fast onboarding and a polished developer workflow |
| Infisical | Open-source platform | Cross-platform | Some backends | Self-hosted or managed | Teams wanting open source without a proprietary SaaS |
| 1Password Secrets Automation | Vault extension | Cross-platform | No | Managed SaaS | Teams already standardized on 1Password |
| CyberArk Conjur | Enterprise platform | Cross-platform | Yes | Self-hosted or enterprise | Regulated enterprises prioritizing governance and audit |

## How to choose

If your team operates entirely on one cloud and expects to stay there, the native manager for that provider, AWS Secrets Manager, Azure Key Vault, or Google Cloud Secret Manager, is usually the path of least resistance: it's already integrated with your identity model, requires no extra infrastructure, and, in the AWS case, handles rotation for you.

If you need dynamic secrets and encryption-as-a-service across many backends and have a platform team with the capacity to operate a distributed system, HashiCorp Vault remains the deepest option, with HCP Vault or OpenBao available depending on whether your priority is offloading operations or open governance.

If developer experience and speed of adoption are the deciding factors, Doppler and Infisical both optimize for that, with Infisical the choice when open source and self-hosting matter and Doppler the choice when a managed, polished workflow matters most.

If your actual problem isn't which store to use but the fact that you already have several, secrets and configuration spread across clouds, a Vault cluster, and CI environment variables, then a configuration layer like Pulumi ESC is aimed at that specific pain: it composes your existing stores rather than replacing them, adds dynamic OIDC-based credentials so you can retire long-lived keys, and gives applications and infrastructure code one consistent way to consume everything. It's the strongest fit for teams managing sprawl rather than starting from a clean single-cloud slate.

## Frequently asked questions

### What is the best secrets management tool?

There isn't a single best tool; the right choice depends on your cloud footprint and who operates it. Teams on one cloud are usually best served by that provider's native manager. Teams needing dynamic secrets at scale lean toward HashiCorp Vault. Teams managing secrets spread across several systems benefit most from a configuration layer like Pulumi ESC that unifies them.

### What is the difference between a secrets manager and a vault?

The terms overlap, but "vault" usually implies a general-purpose platform, like HashiCorp Vault, that not only stores secrets but also generates dynamic credentials and provides encryption as a service. "Secrets manager" more often describes a service focused on securely storing, access-controlling, and rotating secrets, such as the cloud-native managers. In practice many tools do some of both.

### Do I still need a secrets manager if I use AWS, Azure, or Google Cloud?

Each major cloud ships a capable native secrets manager, and for single-cloud teams that's often all you need. The gap appears when you operate across more than one cloud or add SaaS and self-hosted systems, since each native manager only covers its own platform. That's where a cross-cloud store or a configuration layer that composes multiple managers becomes valuable.

### What is the best open-source secrets management tool?

Infisical is a popular open-source secrets management platform for teams wanting a modern developer experience they can self-host. OpenBao, the Linux Foundation fork of HashiCorp Vault, is the open-source path for teams that want Vault's dynamic-secrets model under permissive governance. Pulumi ESC's CLI is also open source, and CyberArk offers an open-source Conjur edition.

### How do secrets managers work with infrastructure as code?

Infrastructure as code needs credentials to provision resources, and hardcoding them into programs or state is exactly what secrets management exists to prevent. Most secrets tools integrate with IaC by injecting secrets at runtime rather than storing them in code. Pulumi ESC does this natively, supplying both configuration and short-lived cloud credentials to Pulumi programs and other tools without any standing secret in the codebase.

### Are environment variables enough for managing secrets?

Environment variables are fine for local development but weak as a primary secrets strategy: they're easily leaked through logs, process listings, and shared shell history, and they offer no encryption at rest, access control, rotation, or audit trail. A secrets manager provides those controls, and tools like Pulumi ESC can still project secrets into environment variables at runtime so you keep the convenience without storing the values in plaintext.

For a deeper introduction to the concepts behind these tools, see our guide to [secrets management](/what-is/what-is-secrets-management/).

## Conclusion

The secrets management landscape in 2026 reflects a world where almost no team runs on a single system anymore. Cloud-native managers are excellent within their own boundaries, HashiCorp Vault remains the most capable general-purpose platform for those who can operate it, and a newer generation of developer-first and open-source tools has lowered the barrier to doing secrets management well. The harder problem for most organizations isn't picking one store, it's that they already have several and no consistent way to use them. Start by being honest about how much sprawl you actually have: if the answer is "one cloud, a handful of secrets," a native manager is enough, and if it's "secrets everywhere and no single interface," a configuration and secrets layer like Pulumi ESC is built for exactly that. Either way, the goal is the same, getting credentials out of your code and into a system designed to protect them.

{{< blog/cta-button "Get started with Pulumi ESC" "/product/esc/" >}}
