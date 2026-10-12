---
title: "17 Secrets Management Tools Compared for 2027"
date: 2025-07-24
updated: 2026-09-25
draft: false
meta_desc: "Compare 17 secrets management tools for 2027 on pricing, licensing, and rotation: Vault, OpenBao, AWS Secrets Manager, Azure Key Vault, and Pulumi ESC."
authors:
    - asaf-ashirov
    - boris-schlosser
tags:
    - secrets-management
    - security
    - devops
    - configuration-as-code
    - esc
category: general
faq_schema: true
itemlist_name: "Secrets Management Tools"
itemlist:
    - name: "Pulumi ESC"
      url: "https://www.pulumi.com/docs/esc/"
    - name: "Doppler"
      url: "https://www.doppler.com/"
    - name: "Infisical"
      url: "https://infisical.com/"
    - name: "HashiCorp Vault"
      url: "https://www.hashicorp.com/products/vault"
    - name: "OpenBao"
      url: "https://openbao.org/"
    - name: "CyberArk Conjur"
      url: "https://www.cyberark.com/products/secrets-manager/"
    - name: "Akeyless"
      url: "https://www.akeyless.io/"
    - name: "AWS Secrets Manager"
      url: "https://aws.amazon.com/secrets-manager/"
    - name: "Azure Key Vault"
      url: "https://azure.microsoft.com/products/key-vault"
    - name: "Google Secret Manager"
      url: "https://cloud.google.com/security/products/secret-manager"
    - name: "1Password Secrets Automation"
      url: "https://1password.com/products/secrets-automation"
    - name: "Bitwarden Secrets Manager"
      url: "https://bitwarden.com/products/secrets-manager/"
    - name: "GitGuardian"
      url: "https://www.gitguardian.com/"
    - name: "TruffleHog"
      url: "https://trufflesecurity.com/trufflehog"
    - name: "External Secrets Operator"
      url: "https://external-secrets.io/"
    - name: "SOPS"
      url: "https://github.com/getsops/sops"
    - name: "Sealed Secrets"
      url: "https://github.com/bitnami-labs/sealed-secrets"
---

[Secrets management](/what-is/what-is-secrets-management/) tools store, distribute, and rotate the credentials your applications depend on: database passwords, API keys, TLS certificates, and the tokens that let one service talk to another. The right tool depends less on which one has the longest feature list and more on how many clouds you run, how much operational overhead your team can absorb, and whether you're trying to replace a secret store or orchestrate the ones you already have.

<!--more-->

This guide compares 17 tools across secrets orchestration platforms, enterprise vaults, cloud-native managers, developer-focused tools, scanning and detection tools, and the Kubernetes-native layer, with a decision framework and honest answers to the questions people are actually asking about secrets management in 2027.

<!--more-->

## At a glance: 17 secrets management tools compared

| Tool | Category | Deployment | License / model | Rotation | Best for |
|---|---|---|---|---|---|
| [Pulumi ESC](#pulumi-esc-environments-secrets-and-configuration) | Orchestration | Managed SaaS or self-hosted | Open-source engine, commercial platform | Dynamic, short-lived OIDC credentials | Teams orchestrating multiple existing stores |
| [Doppler](#doppler) | Orchestration | Managed SaaS | Commercial | Sync-based, integrations-driven | Developer-experience-first teams |
| [Infisical](#infisical) | Orchestration | Self-hosted or managed | Open-source core, commercial cloud | Dynamic secrets on paid tiers | Teams wanting open-source with a cloud option |
| [HashiCorp Vault](#hashicorp-vault) | Enterprise vault | Self-hosted or HCP-managed | BSL 1.1 (source-available) | Dynamic secrets, 50+ engines | Complex, multi-cloud enterprises with platform teams |
| [OpenBao](#openbao) | Enterprise vault | Self-hosted | Open source (MPL 2.0) | Dynamic secrets (Vault-compatible) | Teams that want Vault's model without the BSL |
| [CyberArk Conjur](#cyberark-conjur) | Enterprise vault | Self-hosted or Conjur Cloud | Commercial, open-source core | Policy-driven rotation | Regulated industries needing PAM integration |
| [Akeyless](#akeyless) | Enterprise vault | Managed SaaS | Commercial, usage-based | Just-in-time, zero-knowledge | Cloud-first teams avoiding self-hosted ops |
| [AWS Secrets Manager](#aws-secrets-manager) | Cloud-native | Managed (AWS) | Usage-based | Native for RDS/Aurora + Managed External Secrets | AWS-centric workloads |
| [Azure Key Vault](#azure-key-vault) | Cloud-native | Managed (Azure) | Usage-based | Certificate auto-renewal | Azure and FIPS-regulated environments |
| [Google Secret Manager](#google-secret-manager) | Cloud-native | Managed (GCP) | Usage-based | Notification-only, no execution | GCP-native, high-scale global apps |
| [1Password Secrets Automation](#1password-secrets-automation) | Developer-focused | Managed SaaS | Bundled with Business plan | Manual with CLI/CI hooks | Mixed technical and non-technical teams |
| [Bitwarden Secrets Manager](#bitwarden-secrets-manager) | Developer-focused | Managed SaaS or self-hosted | Per-user, machine accounts included | Manual with CLI/CI hooks | Cost-conscious small and mid-size teams |
| [GitGuardian](#gitguardian) | Scanning | Managed SaaS | Commercial, free tier | N/A — detection, not storage | Large codebases, DevSecOps programs |
| [TruffleHog](#trufflehog) | Scanning | Self-hosted or CLI | Open source, commercial add-ons | N/A — detection, not storage | Teams wanting open-source scanning |
| [External Secrets Operator](#external-secrets-operator) | Kubernetes-native | Self-hosted (K8s operator) | Open source (Apache 2.0), CNCF Sandbox | Syncs from upstream store on interval | Kubernetes teams syncing external vaults |
| [SOPS](#sops) | Kubernetes-native | CLI / GitOps | Open source (MPL 2.0), CNCF | Manual, encrypted-in-git | GitOps teams encrypting values in version control |
| [Sealed Secrets](#sealed-secrets) | Kubernetes-native | Self-hosted (K8s controller) | Open source (Apache 2.0) | Manual, one-way encryption | Simple GitOps without an external vault |

## Secrets orchestration platforms

Orchestration platforms connect and coordinate multiple secret sources rather than requiring you to abandon your existing infrastructure. Instead of migrating wholesale to another secret store, they act as a unified layer over the stores you already run, adding dynamic credential generation and configuration-as-code on top.

### Pulumi ESC (Environments, Secrets, and Configuration)

[Pulumi ESC](/docs/esc/) orchestrates the secret stores you already have, connecting HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, Google Secret Manager, 1Password, and 20-plus other providers through a unified interface. You can modernize your secrets workflow without abandoning current infrastructure investments.

The platform's [configuration-as-code approach](/docs/esc/concepts/) defines hierarchical YAML environments that cascade from base configuration through development, staging, and production. Define common settings once, inherit them everywhere, and keep appropriate security boundaries between environments.

ESC provides [audit logging](/docs/esc/administration/audit-logs/) with user identity, timestamp, access method, and resource detail on every access, supporting compliance frameworks like SOC 2 and GDPR. Dynamic credential generation is the bigger differentiator: instead of storing long-lived AWS access keys or Azure service principal secrets, ESC provisions short-lived OIDC tokens on demand through its [provider model](/docs/esc/providers/), so credentials expire automatically rather than sitting around waiting to be misused.

The platform keeps a zero-lock-in posture through its [open-source engine](https://github.com/pulumi/esc) and [SDK support](/docs/esc/languages-sdks/) for TypeScript, Python, Go, and .NET. GitGuardian's own 2027 tooling roundup independently describes ESC as pulling credentials dynamically from AWS Secrets Manager, Azure Key Vault, Google Secret Manager, Vault, and 1Password via OIDC, with automated rotation shipped for AWS IAM keys and Postgres/MySQL credentials — third-party confirmation of the orchestration model rather than Pulumi's own marketing copy.

ESC's [free tier](/pricing/) covers unlimited environments, and usage-based pricing for advanced features scales with organizational growth. For teams with strict data residency requirements, [Pulumi's self-hosting options](/product/self-hosted/) add cost predictability and control. ESC fits best when you're running multiple clouds or already have secrets scattered across several stores; if you have exactly one secret store and no plans to add a second, a cloud-native manager or a lighter developer tool may be all you need.

### Doppler

Doppler focuses on developer experience: an intuitive interface, branch-based environment management, and real-time secret sync across connected services. Pricing has moved well past its old entry point — the free Developer plan covers 3 users, and additional users on that tier run [$8/user/month](https://www.doppler.com/pricing), while the Team plan (after a 14-day trial) is $21/user/month. Doppler's newer positioning explicitly does not charge per AI agent or non-human identity, only per human seat, which matters as more of the calls hitting your secrets are coming from agents rather than people.

### Infisical

Infisical pairs an open-source core with a managed cloud option, and it now prices secrets management [per identity](https://infisical.com/pricing) — human and machine — rather than per human user. The free tier covers 5 identities; Pro runs $20/identity/month billed annually ($23 month-to-month), with Advanced at $40/identity/month annually for dynamic-secret proxying and stronger access controls.

Infisical has also shipped **Agent Vault**, an open-source credential broker built specifically for AI agents: it sits between an agent and the API it calls, hands the agent's sandbox a placeholder value, and swaps in the real credential only as the request leaves the sandbox — a direct response to agents that would otherwise need standing access to real secrets. It's a newer, standalone project, and it overlaps in purpose with the "Agent Proxy" capability bundled into Infisical's paid tiers, so check Infisical's own docs for which one fits your deployment before you commit to either. Infisical has also broadened its scope beyond secrets into certificate management and privileged access, positioning itself as an identity security platform rather than a single-purpose vault.

## Enterprise secrets vaults

Enterprise vaults prioritize maximum flexibility, extensibility, and compliance depth, aimed at organizations with dedicated security or platform teams.

### HashiCorp Vault

[HashiCorp Vault](/what-is/what-is-hashicorp-vault/) is still the reference point for enterprise secrets management, with dynamic secrets generation across 50-plus systems and support for more than 100 authentication methods and secret engines. Two changes matter for anyone budgeting or evaluating Vault today. First, HashiCorp is now HashiCorp, an IBM Company: IBM's roughly $6.4 billion acquisition closed February 27, 2025, and Vault ships under IBM's stewardship going forward. Second, Vault moved off the open-source MPL 2.0 license to the Business Source License (BSL) 1.1 starting with v1.15.0 in August 2023, so Vault today is source-available rather than OSI-approved open source. HCP Vault Dedicated, the managed offering, now bills by the cluster-hour rather than the flat per-node rate some older comparisons still quote; a production-grade cluster commonly runs well over $1,000/month, so confirm current numbers directly with HashiCorp before you budget against an old figure.

Vault remains the right call for organizations that need maximum flexibility, run genuinely complex multi-cloud environments, and have the DevOps expertise to operate it well.

### OpenBao

The BSL relicensing is the reason [OpenBao](https://openbao.org/) exists. OpenBao is a Linux Foundation and OpenSSF-hosted fork of Vault, forked from the last MPL-licensed release, and it keeps growing on its own open-source cadence — the 2.5.x line was current through 2026. It's Vault-API-compatible, so most Vault clients, Terraform providers, and integrations work against it with minimal changes. It's showing up in GitOps-heavy Kubernetes stacks where teams want Vault's dynamic-secrets model without accepting a source-available license. If you're evaluating Vault today and licensing terms matter to your organization, put OpenBao on the shortlist before you sign anything.

### CyberArk Conjur

CyberArk Conjur focuses on enterprise security and compliance, backed by CyberArk's broader privileged access management suite for session monitoring, just-in-time access, and threat detection. CyberArk now also offers **Conjur Cloud**, a managed SaaS version, alongside the self-hosted Conjur Enterprise and open-source editions — a meaningful change for teams that wanted Conjur's policy engine without running the infrastructure themselves. Enterprise licensing is scale-based; Conjur targets regulated industries and organizations for whom compliance depth outweighs operational simplicity.

### Akeyless

Akeyless delivers enterprise vault capabilities as SaaS, using zero-knowledge, client-side encryption so that even Akeyless can't read customer secrets. The free tier covers roughly 5 clients with a small allotment of static and dynamic secrets; beyond that, Akeyless bills on usage across clients, transactions, connectors, and certificate volume rather than a flat per-seat price, so get a quote against your actual usage pattern before comparing it to a per-user competitor. It suits cloud-first teams that want enterprise vault features without operating the underlying infrastructure.

## Cloud-native secrets managers

Cloud-native managers trade portability for tight integration with one provider's identity and service ecosystem.

### AWS Secrets Manager

[AWS Secrets Manager](/what-is/what-is-aws-secrets-manager/) integrates natively with more than 50 AWS services, with automatic rotation built in for RDS, Aurora, and several other databases. The newest addition is **Managed External Secrets (MES)**, launched November 2025, which extends AWS's zero-code rotation model to third-party SaaS credentials rather than just AWS-native ones. At launch it covered Salesforce, BigID, and Snowflake; AWS has been adding partners through 2026, including Datadog, Jenkins/SonarQube integrations, and further SaaS providers, so check the [MES partner list](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-secrets-manager-managed-external-secrets/) for your specific vendor before assuming coverage. Pricing is unchanged: $0.40 per secret per month plus $0.05 per 10,000 API calls.

AWS Secrets Manager is the default choice for [AWS-native organizations](/docs/integrations/clouds/aws/) that want rotation handled for them rather than built by hand.

### Azure Key Vault

[Azure Key Vault](/what-is/what-is-azure-key-vault/) manages secrets, keys, and certificates with Azure Active Directory-based access control and certificate lifecycle management with automatic renewal. Its cryptographic validation has moved forward: Premium tier and Managed HSM now run on **FIPS 140-3 Level 3** validated hardware, a step up from the FIPS 140-2 Level 2 figure still floating around in older comparisons. Standard tier pricing runs on a per-10,000-operations basis; confirm the current rate directly against [Azure's pricing page](https://azure.microsoft.com/pricing/details/key-vault/) since Microsoft revises these more often than the marketing pages update. Azure Key Vault is the natural fit for [Azure-centric organizations](/docs/integrations/clouds/azure/) and government contractors who need FIPS-validated HSMs without standing up their own.

### Google Secret Manager

[Google Secret Manager](/what-is/what-is-google-cloud-secret-manager/) is built for high-volume, globally distributed workloads, with automatic replication across GCP regions and IAM-based, condition-aware permissions. One thing hasn't changed: Secret Manager still has no built-in rotation *execution*. Its "rotation" feature only fires a Pub/Sub notification on schedule; you still have to write the Cloud Function (or equivalent) that actually rotates the credential and no dynamic secrets generation exists at all. Pricing runs about $0.06 per secret-version per month plus $0.03 per 10,000 access operations after a small free tier. It's the right pick for [GCP-native teams](/docs/integrations/clouds/gcp/) prioritizing scale and low latency who are comfortable owning their own rotation logic.

## Developer-focused tools

These tools trade some enterprise depth for ease of adoption, often serving as a team's first secrets manager.

### 1Password Secrets Automation

1Password's developer tooling — CLI, SDKs, SSH and Git commit signing, and secrets management — is no longer sold as a separate "Secrets Automation" SKU. It's bundled into the standard Business plan at $8.99/user/month (paid annually), with more advanced privileged-access and AI-agent runtime credential features available only through custom Enterprise quotes. 1Password remains a strong fit for mixed technical and non-technical teams that want zero-knowledge encryption without asking non-engineers to learn a CLI.

### Bitwarden Secrets Manager

Bitwarden's Teams plan runs $6/user/month and includes up to 20 machine accounts, unlimited secrets and projects, and audit logging; Enterprise runs $12/user/month with up to 50 machine accounts plus SSO/SCIM and granular access control. Machine-account support for CI/CD is built in rather than an add-on, which is the main reason small and mid-size teams pick it over a heavier vault.

## Application security and secrets scanning

Scanning tools find secrets that have already leaked into code, commits, or CI logs, which is a different and complementary job to everything above.

### GitGuardian

GitGuardian scans commits, pull requests, and issues across GitHub, GitLab, Bitbucket, and Azure DevOps in real time, detecting over 350 secret types. Its published Standard tier runs [$18/developer/month](https://www.gitguardian.com/pricing) for teams of 26-100 developers; above that, and for Enterprise, pricing moves to a custom quote. GitGuardian fits organizations with large codebases and formal DevSecOps programs that need to catch exposure before it reaches production.

### TruffleHog

TruffleHog is open-source secrets detection combining entropy analysis with pattern matching across more than 700 credential types, plus historical git-history scanning to find out when and how a credential first landed in a repo. It integrates with GitHub Actions, GitLab CI, and Jenkins, and an enterprise tier adds commercial support. TruffleHog suits teams that want transparent, self-hostable detection without a SaaS dependency.

## Kubernetes-native secrets tools

If you're running Kubernetes, "how do I get external secrets into a Pod" is a separate question from "which vault do I use," and a small set of purpose-built, CNCF-affiliated tools answer it.

### External Secrets Operator

External Secrets Operator (ESO) syncs secrets from Vault, AWS, Azure, GCP, and other external stores into native Kubernetes Secrets on a configurable refresh interval, using Custom Resource Definitions so it fits normal Kubernetes operational patterns. It's Apache 2.0-licensed, lives in the CNCF Sandbox, and has become the de facto standard for this job — if you're syncing an external vault into Kubernetes today and not using ESO, it's worth asking why.

### SOPS

[SOPS](https://github.com/getsops/sops) (Secrets OPerationS) encrypts individual values inside YAML, JSON, or .env files so the encrypted file itself can live safely in Git — the encryption keys come from AWS KMS, GCP KMS, Azure Key Vault, PGP, or age. It's MPL 2.0-licensed, adopted by the CNCF, and maintained independently of any single vendor. Flux CD supports SOPS natively; Argo CD needs a plugin like KSOPS or helm-secrets to do the same. SOPS is the right tool when your GitOps workflow wants secrets encrypted *in* version control rather than fetched from an external store at deploy time.

### Sealed Secrets

Sealed Secrets, maintained under bitnami-labs (Bitnami itself now sits under Broadcom, a provenance detail worth knowing rather than a red flag), takes a one-way approach: a cluster-side controller holds a private key, and anyone can encrypt a secret against the matching public key without needing cluster access. The encrypted "SealedSecret" is safe to commit to Git and only decrypts inside the cluster that holds the private key. It's a simpler mental model than SOPS or ESO for teams that don't want to run or connect to an external vault at all.

A few narrower AWS- and GCP-specific tools are worth a mention without a full section each: Segment's **Chamber** wraps AWS Parameter Store for teams that want the cheapest possible option and already live in AWS, and Google's **Berglas** optimizes secret injection for Cloud Run and other serverless GCP workloads. Lyft's **Confidant**, previously a common recommendation in this space, was archived by its maintainers in 2025 and is now read-only — don't stand up new infrastructure on it.

{{< blog/cta-card title="Try secrets orchestration" href="/docs/esc/" >}}
Pulumi ESC connects your existing secret stores behind a single interface, adding configuration as code and dynamic, short-lived credentials.
{{< /blog/cta-card >}}

## Secrets management for AI agents and non-human identities

The growing number of AI agents, CI jobs, and service accounts now outnumber human users in most environments, and they're the newest source of pressure on secrets management. This "non-human identity" (NHI) surge changes the threat model: an agent with standing access to a real API key can be manipulated into misusing it, and a credential embedded in an agent's configuration is a credential that can leak through logs, prompts, or a misconfigured MCP server.

The practitioner consensus, echoed across security forums, is blunt: a secrets manager protects storage, not workflow, and the fix is making credentials as short-lived and invisible to the calling code as possible. Three patterns are emerging as the default response:

- **Short-lived, dynamically generated credentials** instead of long-lived API keys, so a leaked credential is worthless within minutes rather than valid indefinitely. This is the model Pulumi ESC, Vault, and Akeyless all built around before "AI agent" was the reason to want it.
- **Credential proxies for agents**, like Infisical's Agent Vault, which hand an agent a placeholder value and inject the real credential only at the network edge, so the agent's own context never holds a usable secret.
- **Configuration hygiene for agent tooling**, since scanners have found real credentials sitting in plaintext inside MCP server configuration files — the same mistake as committing a `.env` file to Git, just in a newer wrapper.

If your organization is deploying AI coding agents or infrastructure agents like Pulumi Neo, treat their credential access the same way you'd treat a new service account: scope it narrowly, make it short-lived, and put it behind the same [orchestration layer](/product/secrets-management/) as everything else, rather than handing it a static key because it was faster to wire up.

## How to choose: a practical decision framework

Most teams overthink this decision. In practice, three questions get you most of the way there:

1. **Do you use exactly one secret store today, with no plans to add a second?** Use your cloud provider's native tool — AWS Secrets Manager, Azure Key Vault, or Google Secret Manager. It's cheaper, better integrated, and there's nothing to orchestrate yet.
2. **Do you operate across multiple clouds, or do you already have secrets scattered across more than one store?** This is when an orchestration layer (Pulumi ESC) or a self-hosted vault (HashiCorp Vault or OpenBao) earns its keep, because the alternative is manually keeping several stores in sync.
3. **Is your team small, cost-sensitive, or short on dedicated security headcount?** Skip the enterprise vaults entirely. A developer-focused tool like Bitwarden Secrets Manager or Infisical's free tier will cover real needs without the operational weight of running Vault yourself — a complaint that shows up constantly in practitioner discussions about the cost and staffing burden of HA Vault-plus-Consul deployments.

Compliance and licensing add a fourth filter on top of those three: government and regulated environments often need FIPS-validated HSMs (Azure Key Vault, CyberArk), and organizations wary of the BSL should weigh OpenBao against Vault before committing either way, on top of anything above.

## Frequently asked questions

### What's the difference between AWS Secrets Manager and HashiCorp Vault?

AWS Secrets Manager is a managed, AWS-only service with native rotation for AWS databases and, since late 2025, a growing set of third-party SaaS integrations through Managed External Secrets. HashiCorp Vault is self-hosted (or HCP-managed) and cloud-agnostic, supporting over 50 dynamic secret engines across any infrastructure. Choose Secrets Manager if you're AWS-only; choose Vault or OpenBao if you're multi-cloud or need engines AWS doesn't offer.

### Is base64 encoding in Kubernetes Secrets actually secure?

No. Base64 is an encoding, not encryption, and anyone with read access to etcd or the Kubernetes API can decode a [Kubernetes Secret](/what-is/what-are-kubernetes-secrets/) trivially. Kubernetes Secrets need encryption at rest enabled on etcd plus an external tool — Sealed Secrets, SOPS, or External Secrets Operator pulling from a real vault — to be meaningfully protected.

### What are the best secrets management tools for a self-hosted, small team setup?

Passbolt, Bitwarden Secrets Manager, and Infisical's self-hosted open-source edition are the most commonly recommended options for teams that want to avoid a SaaS dependency without taking on Vault's operational overhead. For Kubernetes-only workloads, Sealed Secrets is the simplest self-hosted option with no external service to run at all.

### What's the best way to manage secrets in GitHub Actions?

Use [GitHub's native encrypted repository or organization secrets](/what-is/what-is-a-github-action-secret/) for simple cases, and OIDC federation to your cloud provider (AWS, Azure, GCP) instead of long-lived cloud credentials wherever possible. For larger organizations already running Vault, Pulumi ESC, or Doppler, pull secrets into the workflow at runtime through that platform's GitHub Action rather than duplicating them into GitHub's own secret store.

### How often should secrets actually be rotated?

Static, long-lived credentials (API keys, service account passwords) should rotate on a schedule — 90 days is a common baseline, tighter for anything privileged. The better answer, where it's available, is to stop rotating on a calendar and instead issue short-lived dynamic credentials that expire automatically after minutes or hours, which is the model Vault, OpenBao, Akeyless, and Pulumi ESC all support.

### What is zero-trust secrets management?

Zero-trust secrets management assumes any credential could be compromised and limits the damage a single leaked secret can do: short lifetimes, narrow scope, and no standing access. In practice that means dynamic credential generation over static secrets, fine-grained per-identity access instead of broad service accounts, and full audit trails so a compromise is visible fast rather than discovered months later.

### Should I use HashiCorp Vault or OpenBao?

If you need commercial support, HCP's managed offering, or you're already standardized on Vault, staying with Vault under HashiCorp (now HashiCorp, an IBM Company) is the lower-friction path. If the Business Source License is a blocker for your organization, or you want to stay on a fully open-source, community-governed project, OpenBao is API-compatible with Vault and run under the Linux Foundation and OpenSSF.

### What is a non-human identity (NHI) and why does it matter for secrets management?

A non-human identity is any credentialed actor that isn't a person — a CI job, a service account, or an AI agent. NHIs already outnumber human identities in most organizations, and they're driving demand for short-lived, narrowly scoped credentials and agent-specific credential proxies, since a static API key handed to an autonomous agent is a much larger blast radius than the same key handed to a person.

### Do I need a dedicated secrets manager if I'm already using environment variables?

Environment variables are only a delivery mechanism: they don't rotate, audit access, or prevent a secret from ending up in a log or a crash dump. Even a lightweight tool like Bitwarden Secrets Manager or Infisical's free tier adds rotation, access logging, and centralized revocation that plain environment variables can't provide on their own.

### Can I use more than one secrets management tool at once?

Yes, and most organizations of any size end up doing exactly that: a cloud-native manager for cloud-native workloads, a Kubernetes-native tool like External Secrets Operator or SOPS for cluster secrets, and an orchestration layer like Pulumi ESC on top to keep configuration and access consistent across all of them rather than managing each store's quirks separately.

## Choosing the right path forward

Secrets management has moved from simple storage to orchestration, and the practical test for any tool on this list is whether it reduces the number of places a credential can leak from. Start with the decision framework above rather than the feature list: a single-cloud team gains little from Vault's flexibility, and a multi-cloud team will eventually regret standardizing on a single provider's native tool.

Whatever you land on, prioritize dynamic and short-lived credentials over static ones wherever your tooling supports it, keep AI agents on the same narrow, auditable access as any other non-human identity, and treat secrets management as infrastructure orchestration rather than a single point product. [Pulumi ESC](/docs/esc/) is built for exactly that orchestration layer — pulling from AWS Secrets Manager, Azure Key Vault, Vault, or whatever you already run, and adding [configuration-as-code](/what-is/what-is-infrastructure-as-code/) and dynamic credentials on top without asking you to migrate away from anything first.

---

*Ready to bring configuration and secrets together? [Explore Pulumi ESC](/docs/esc/) and see how orchestrating your existing secret stores compares to running another one from scratch.*
