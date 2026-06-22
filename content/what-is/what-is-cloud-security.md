---
title: What is Cloud Security?
meta_desc: "Cloud security is the practice of protecting cloud workloads, data, and identities. Learn the shared responsibility model, key risks, and proven controls."
meta_image: /images/what-is/what-is-cloud-security-meta.png
type: what-is
page_title: "What is Cloud Security?"
authors: ["cam-soper"]
---

**Cloud security is the set of policies, controls, technologies, and operational practices that protect cloud workloads, data, identities, and infrastructure from attack and accidental exposure.** It spans every layer of a modern stack, from the cloud provider's physical data centers to your IAM policies, network rules, container images, secrets, and the application code that runs on top.

Cloud security is a partnership: the provider secures the platform, and you secure what you build on it. That division is the shared responsibility model, and the large majority of cloud security incidents are not provider failures. They're customer-side misconfigurations. Modern teams treat cloud security as an engineering problem: configurations live in [infrastructure as code](/what-is/what-is-infrastructure-as-code/), [policies](/docs/insights/policy/) run in CI, secrets are pulled from a [centralized vault](/product/esc/), and every change is reviewed in Git before it touches production.

In this article, we'll cover the key questions about cloud security:

* Why does cloud security matter?
* How is cloud security different from on-premises security?
* What is the shared responsibility model?
* What are the CIA triad and core principles of cloud security?
* What are the main domains of cloud security?
* What are the biggest cloud security risks?
* What are cloud security best practices?
* How does infrastructure as code strengthen cloud security?
* Frequently asked questions about cloud security

## Why does cloud security matter?

Public cloud is where most new software is built and run, and the stakes are higher than they were on-prem. Three forces make cloud security a board-level concern.

### The attack surface keeps growing

A typical cloud-native app spans hundreds of resources: VMs, container clusters, managed databases, object storage, queues, IAM roles, API gateways, SaaS integrations. Each one is reachable through an API. The attack surface is no longer a single network edge; it now extends across credentials, public storage, and overly-permissive roles in every account.

### Misconfigurations are the dominant failure mode

The large majority of cloud breaches trace back to customer-side configuration mistakes, not exploits of the cloud platforms themselves. Public S3 buckets, IAM roles with `*` permissions, unrestricted security groups, and forgotten dev environments all create exposures that automated scanners are continuously hunting for.

### Regulation has caught up

GDPR, HIPAA, PCI DSS, SOC 2, ISO 27001, FedRAMP, and HITRUST all now require demonstrable controls on cloud workloads. Failure to comply has direct financial and contractual consequences, and the cost of a serious breach (incident response, regulatory penalties, customer churn, reputational damage) routinely reaches the millions.

## How is cloud security different from on-premises security?

The disciplines overlap, but the cloud changes most of the operating assumptions.

| Dimension | On-premises | Cloud |
|---|---|---|
| Perimeter | Network edge (firewalls, DMZ) | Identity and API surface |
| Infrastructure | Long-lived, manually configured | Ephemeral, API-provisioned |
| Responsibility | Fully owned by the organization | Shared with the provider |
| Pace of change | Days to weeks | Minutes to hours |
| Primary risk | External network attack | Misconfiguration and excessive permissions |
| Inventory | Static asset database | Dynamic, multi-account, multi-cloud |

The practical consequence is that cloud security has to be automated. There are too many resources changing too quickly for manual reviews to keep up, which is why infrastructure as code, policy as code, and continuous detection are the standard tooling rather than optional add-ons.

## What is the shared responsibility model?

Every major cloud provider (AWS, Azure, Google Cloud) operates a shared responsibility model that splits security duties between provider and customer. The split depends on the service model.

| Layer | IaaS (e.g. EC2) | PaaS (e.g. App Engine) | SaaS (e.g. Microsoft 365) |
|---|---|---|---|
| Physical security | Provider | Provider | Provider |
| Network infrastructure | Provider | Provider | Provider |
| Host operating system | **Customer** | Provider | Provider |
| Application runtime | **Customer** | Provider | Provider |
| Application code | **Customer** | **Customer** | Provider |
| Data and content | **Customer** | **Customer** | **Customer** |
| Identity and access | **Customer** | **Customer** | **Customer** |
| Configuration | **Customer** | **Customer** | **Customer** |

Customers always own data, identity, and configuration. The lower the abstraction (IaaS), the more operating-system and runtime work the customer takes on. The higher the abstraction (SaaS), the more the provider handles. Most avoidable cloud breaches live in one of the rows labeled **Customer**.

## What are the CIA triad and core principles of cloud security?

The CIA triad is the canonical framework for what security controls should achieve. It maps cleanly onto cloud workloads.

* **Confidentiality.** Only authorized identities can read sensitive data. Achieved through encryption at rest and in transit, IAM, network isolation, and secrets management.
* **Integrity.** Data and infrastructure aren't modified by unauthorized parties, and when they are, the change is detected. Achieved through signed artifacts, immutable infrastructure, audit logs, and drift detection.
* **Availability.** Services stay reachable to the people meant to reach them, even during attack or failure. Achieved through redundancy, DDoS protection, capacity planning, and incident response.

A handful of additional principles round out modern cloud security practice: **defense in depth** (multiple overlapping controls), **least privilege** (only the access strictly required), **zero trust** (no implicit trust based on network location), and **secure by default** (insecure configurations require a deliberate override).

## What are the main domains of cloud security?

Cloud security is broad. Most programs are organized around six domains.

### Identity and access management (IAM)

The cloud's primary perimeter. Modern IAM covers user federation, role-based and attribute-based access control, service identities (workload identity, IAM roles for service accounts), MFA, just-in-time elevation, and short-lived credentials.

### Data protection

Classification, encryption with keys managed via KMS or HSM, data loss prevention, secure backups, and data residency controls.

### Network security

VPC design, security groups, network ACLs, service mesh policies, private endpoints, egress filtering, web application firewalls, and DDoS protection.

### Application and workload security

SBOM and dependency scanning, container image signing and scanning, runtime protection, API gateways, and secrets injection at runtime via [Pulumi ESC](/product/esc/) or similar tooling.

### Configuration and posture management

Cloud security posture management (CSPM), infrastructure as code, [policy as code](/docs/insights/policy/), drift detection, and automated remediation.

### Detection and response

Centralized logging, SIEM, threat detection, behavior analytics, and cloud-native incident response runbooks.

## What are the biggest cloud security risks?

The OWASP Cloud-Native Application Security Top 10 and the Cloud Security Alliance's "Top Threats" reports converge on a fairly consistent list:

1. **Misconfigurations.** Publicly accessible storage, overly permissive IAM, open security groups. The single biggest source of cloud breaches.
1. **Identity and credential compromise.** Phished users, leaked access keys, long-lived service account credentials.
1. **Insecure APIs and interfaces.** Unauthenticated endpoints, broken object-level authorization, missing rate limits.
1. **Insider threat and account abuse.** Employees, contractors, or compromised accounts with more access than they need.
1. **Supply chain attacks.** Compromised dependencies, container base images, or CI/CD pipelines.
1. **Insufficient logging and monitoring.** Without telemetry, attackers can operate undetected for months.
1. **Data exfiltration.** Lateral movement leading to bulk extraction of customer or PII data.
1. **Shared-technology vulnerabilities.** Cross-tenant issues in multi-tenant services. Rare but high-impact.
1. **Compliance and regulatory failures.** Controls that exist on paper but aren't enforced in the running system.
1. **Shadow IT and unsanctioned cloud usage.** Teams spinning up resources outside the central security program.

## What are cloud security best practices?

A practical baseline that holds up across providers and team sizes:

* **Define infrastructure as code.** Replace console clicks with version-controlled [infrastructure as code](/what-is/what-is-infrastructure-as-code/) so every cloud change is reviewable and reproducible.
* **Enforce policy as code in CI.** Block insecure configurations before they deploy with tools like [Pulumi Policies](/docs/insights/policy/) or Open Policy Agent.
* **Apply least privilege everywhere.** Default deny; grant the minimum access needed; prefer short-lived, scoped credentials over long-lived keys.
* **Centralize secrets and configuration.** Keep secrets out of code and CI logs. Pull secrets at runtime from a dedicated store such as HashiCorp Vault or AWS Secrets Manager, and use [Pulumi ESC](/product/esc/) to aggregate and broker access to those stores so applications, CI jobs, and Pulumi programs all see a single, audited interface.
* **Encrypt by default.** Use provider-managed or customer-managed keys for data at rest and TLS for data in transit. Make the unencrypted path the harder one.
* **Centralize logging and monitoring.** Ship logs from every account, region, and service to a single store, and define alerts on policy violations, not just on errors.
* **Patch and rotate continuously.** Rebuild images, rotate keys, and refresh certificates on a schedule rather than on incident.
* **Practice incident response.** Maintain cloud-specific runbooks, automate the obvious responses, and run tabletop exercises before you need them.
* **Audit IAM regularly.** Run least-privilege reviews, expire dormant credentials, and use tooling that surfaces unused permissions.

## How does infrastructure as code strengthen cloud security?

The configurations that cause most cloud breaches (public buckets, open ports, wildcard IAM) are the exact configurations that infrastructure as code makes reviewable, auditable, and enforceable.

With Pulumi:

* **Every change is a pull request.** Security reviewers see exactly what's about to happen before it lands.
* **Policy as code blocks insecure changes.** [Pulumi Policies](/docs/insights/policy/) run in CI alongside `pulumi preview`, so a public bucket or a `0.0.0.0/0` ingress rule never reaches production.
* **Secrets are pulled at runtime.** [Pulumi ESC](/product/esc/) holds encrypted secrets and pulls them on demand into Pulumi programs, CI jobs, and applications. No plaintext secrets in code or state files.
* **Drift is observable.** When a console click breaks the IaC contract, the next preview surfaces it.
* **Reuse safe defaults.** Platform teams ship [Pulumi components](/docs/iac/concepts/components/) with the right encryption, logging, and IAM settings baked in, so product teams consume secure infrastructure without having to relearn it every time.

[Get started with Pulumi](/docs/get-started/) to manage cloud infrastructure as code in TypeScript, Python, Go, C#, Java, or YAML.

## Frequently asked questions about cloud security

### What is cloud security in simple terms?

Cloud security is the discipline of protecting workloads, data, and identities that run in or rely on cloud services. It combines technical controls (encryption, IAM, network rules, monitoring), operational practices (change management, incident response), and a shared responsibility model with the cloud provider.

### Who is responsible for cloud security?

Both the cloud provider and the customer. The provider secures the physical infrastructure and the platform; the customer secures their data, identities, configuration, and (for IaaS) the operating system and runtime. The split shifts depending on whether the service is IaaS, PaaS, or SaaS, but the customer is always responsible for their own data and access controls.

### What are the most common causes of cloud breaches?

Misconfigurations. Public storage, IAM roles with overly broad permissions, open security groups, and leaked long-lived credentials account for the majority of incidents, far more than vulnerabilities in the cloud platforms themselves.

### What is the shared responsibility model?

A formal split of security duties between the cloud provider and the customer. The provider is responsible for the security *of* the cloud (hardware, networking, host hypervisor). The customer is responsible for security *in* the cloud (data, IAM, configuration, application code).

### What is the difference between cloud security and cybersecurity?

Cybersecurity is the broader discipline of protecting any digital system. Cloud security is the specialization that focuses on workloads and data hosted in cloud environments, with extra emphasis on identity, API surfaces, and configuration, the areas where cloud differs most from on-premises.

### Is the cloud more secure than on-premises infrastructure?

Generally yes, when it's used well. Cloud providers invest more in physical, network, and platform security than most individual organizations can. The catch is that the customer side of the shared responsibility model still has to be done correctly, and most "cloud breaches" are misconfigurations on the customer side rather than provider failures.

### What is cloud security posture management (CSPM)?

CSPM tools continuously inspect cloud accounts for misconfigurations, policy violations, and risky permissions, and either flag or auto-remediate them. They sit on top of the provider's APIs and produce a continuous report card on configuration drift across many accounts and clouds.

### How does compliance relate to cloud security?

Compliance frameworks (SOC 2, ISO 27001, HIPAA, PCI DSS, FedRAMP) define what controls have to be in place; cloud security is how you implement and continuously prove them. Cloud-native tools like IAM analyzers, policy as code, audit logs, and CSPM make it easier to demonstrate compliance because the configuration is itself an artifact you can audit.

### What is zero trust in a cloud context?

Zero trust means no identity, network, or device is trusted by default. Every request is authenticated, authorized, and ideally encrypted, regardless of where it comes from. In the cloud, that translates into workload identity, mTLS between services, just-in-time access elevation, and continuous verification of session context.

### How do I start improving cloud security on an existing footprint?

1. Inventory what you have. Many breaches start with assets the security team didn't know existed.
1. Turn on logging in every account and region; ship logs to a central store.
1. Enforce MFA on every human user and remove long-lived access keys.
1. Run a CSPM or [Pulumi Policies](/docs/insights/policy/) pass to find public storage, wildcard IAM, and open ports.
1. Move new infrastructure to [code](/what-is/what-is-infrastructure-as-code/) and adopt policy as code so the same mistakes don't recur.

## Learn more

Pulumi is built for the teams responsible for cloud security: platform engineers, security engineers, and SREs who want infrastructure they can review, test, and prove safe before it ships. [Get started today](/docs/get-started/).

Related reading:

* [What is Infrastructure as Code (IaC)?](/what-is/what-is-infrastructure-as-code/)
* [What is Secrets Management?](/what-is/what-is-secrets-management/)
* [What is Configuration Management?](/what-is/what-is-configuration-management/)
* [What is SOC 2?](/what-is/what-is-soc-2/)
* [What is HIPAA?](/what-is/what-is-hipaa/)
* [What is HITRUST?](/what-is/what-is-hitrust/)
