---
title: What Is Cloud Misconfiguration?
meta_desc: "A cloud misconfiguration is an insecure setting on a cloud resource that exposes data or systems. Learn the common types and how to prevent them."
type: what-is
date: 2026-07-21T12:18:00-07:00
page_title: "What Is Cloud Misconfiguration?"
authors: ["alex-leventer"]
---

**A cloud misconfiguration is any setting on a cloud resource that leaves it less secure than it should be: a storage bucket left open to the public internet, an identity granted more permissions than it needs, a database reachable from anywhere, or logging switched off so no one can see what happened. It is a mistake in how a resource is configured, not a flaw in the cloud provider's software, and it is the single most common way that cloud data gets exposed.** Because cloud platforms expose thousands of tunable settings and default to convenience over lockdown, a single wrong toggle can turn a private resource into a public one.

Misconfigurations are distinct from software vulnerabilities. A vulnerability is a defect in code that an attacker exploits; a misconfiguration is a resource that is working exactly as configured, just configured insecurely. The distinction matters because the fix is different: you patch a vulnerability, but you correct a misconfiguration by changing the settings, and the most reliable way to get settings right at scale is to define them as code and check them automatically.

In this article, we'll cover the key questions about cloud misconfiguration:

* What is cloud misconfiguration?
* Why do cloud misconfigurations happen?
* What are the most common types of cloud misconfiguration?
* Why are cloud misconfigurations so dangerous?
* How do you detect and prevent cloud misconfigurations?
* How does infrastructure as code reduce misconfiguration?
* How does Pulumi help prevent cloud misconfigurations?
* Frequently asked questions about cloud misconfiguration

## What is cloud misconfiguration?

A cloud misconfiguration is a setting, or combination of settings, that makes a cloud resource insecure, non-compliant, or exposed. It can be as blunt as an object storage bucket with public read access, or as subtle as an identity policy that grants a wildcard permission no one noticed. In every case the resource is behaving exactly as it was told to; the problem is the instructions.

Cloud environments are configuration-heavy by design. Every resource (a virtual machine, a bucket, a database, a load balancer, an identity role) carries dozens of settings that control who can reach it, how data is stored, what gets logged, and what it is allowed to do. Cloud providers ship these resources with defaults chosen to get you running quickly, and those defaults are not always the most secure option. Multiply that surface area across hundreds of resources, several accounts, and a handful of regions, and the number of settings a team is responsible for gets very large very fast. Misconfiguration is what happens when even a small fraction of those settings are wrong.

The key mental model is that a misconfiguration is a governance problem, not a patching problem. There is no vendor update that fixes an over-permissive IAM role or a bucket you made public. The only fix is to change the configuration and, more importantly, to make sure it does not drift back to an insecure state later.

## Why do cloud misconfigurations happen?

Misconfigurations are rarely the result of negligence. They are the predictable outcome of complexity, speed, and manual processes colliding.

**Insecure or permissive defaults.** Providers optimize first-run experience, so a new resource may allow broad access until you tighten it. If no one tightens it, the default becomes the production setting.

**Scale and surface area.** A modern cloud estate spans many services, each with its own configuration model. No individual can hold the secure baseline for every service in their head, so gaps appear.

**Manual, console-driven changes.** When people configure resources by clicking through a web console (sometimes called ClickOps), the change leaves no reviewable record, is easy to get wrong, and is nearly impossible to reproduce consistently across environments.

**Configuration drift.** Even a correctly configured resource can [drift](/what-is/what-is-infrastructure-drift/) out of compliance when someone makes an out-of-band change (a "temporary" fix during an incident that never gets reverted, for example). Without continuous checking, no one notices until it is exploited.

**Speed and pressure.** Teams shipping quickly take shortcuts. A permission is widened to unblock a deploy, a security group is opened to debug connectivity, and the intended cleanup never happens.

**Human error.** Industry analysis attributes the overwhelming majority of cloud security failures to customer-side mistakes rather than provider faults. Gartner has predicted that [through 2025, 99% of cloud security failures would be the customer's fault](https://cloudsecurityalliance.org/blog/2023/08/14/managing-cloud-misconfigurations-risks), which is why removing manual steps is so effective at reducing them.

## What are the most common types of cloud misconfiguration?

A handful of patterns account for a large share of real-world incidents. Each is easy to create by accident and easy to state as a rule that a machine can check.

**Publicly accessible storage buckets.** Object storage (such as Amazon S3, Azure Blob Storage, or Google Cloud Storage) left open to public read (or write) access is the archetypal cloud data leak. Anyone with the URL can download the contents.

**Overly permissive IAM.** Identity and access policies that grant wildcard actions (`*`) or attach broad administrative rights violate least privilege. One compromised credential then has far more reach than it should.

**Open security groups and firewall rules.** Ingress rules that allow traffic from `0.0.0.0/0` (the entire internet) to sensitive ports (databases, SSH, RDP) expose services that should only be reachable internally.

**Unencrypted storage and databases.** Data at rest without encryption, or volumes and snapshots with encryption disabled, means a leaked copy is immediately readable.

**Disabled or missing logging.** Turning off audit logs, flow logs, or access logs removes the evidence trail. You cannot detect or investigate what you did not record.

**Exposed secrets.** API keys, passwords, and tokens hard-coded into configuration, environment variables, or committed to a repository turn a single leak into a broad compromise. Proper [secrets management](/what-is/what-is-secrets-management/) keeps them out of plaintext.

**Default or unchanged credentials.** Resources left with vendor-default usernames and passwords, or shared long-lived credentials that are never rotated, are trivial for attackers to guess or reuse.

| Misconfiguration | Risk it creates | How to prevent it |
|---|---|---|
| Public storage bucket | Data exposure and leakage to anyone on the internet | Enforce a rule that blocks public-access settings before deploy |
| Overly permissive IAM (`*`) | Excessive blast radius if a credential is compromised | Apply least privilege; scope actions and resources explicitly |
| Open security group (`0.0.0.0/0`) | Sensitive ports reachable from the whole internet | Restrict ingress to known CIDR ranges; deny broad ingress in policy |
| Unencrypted storage or database | Leaked data is immediately readable | Require encryption at rest on every storage resource |
| Disabled logging | No detection or forensic trail after an incident | Mandate audit, flow, and access logging by policy |
| Exposed or hard-coded secrets | One leak compromises many systems | Use a secrets manager; scan and block plaintext secrets |
| Default or stale credentials | Trivial unauthorized access | Rotate credentials; forbid vendor defaults |

## Why are cloud misconfigurations so dangerous?

Misconfigurations are dangerous because they are both common and high-impact. Unlike a software vulnerability that requires an attacker to develop or acquire an exploit, a public bucket or an open port needs no exploitation at all: it is simply available to whoever finds it. Automated scanners crawl the internet continuously looking for exactly these exposures.

The data backs this up. Gartner and the Cloud Security Alliance have found that [misconfigurations drive 80% of data security breaches](https://cloudsecurityalliance.org/blog/2023/08/14/managing-cloud-misconfigurations-risks). When a breach does occur, the cost is substantial: the average cost of a data breach has reached [$4.88 million globally and $10.22 million in the United States](https://www.ibm.com/reports/data-breach), according to IBM's 2024 Cost of a Data Breach report.

The blast radius compounds over time. A misconfigured resource is rarely isolated: other systems get built on top of it, data accumulates in it, and permissions granted through it get reused. By the time someone notices, correcting the setting is riskier and more disruptive than it would have been on day one. And because manual review does not scale across hundreds of pull requests and thousands of resources, a single mistake that slips past a human reviewer can sit undetected for months. This is why prevention (catching the misconfiguration before the resource is ever created) is so much cheaper than remediation.

## How do you detect and prevent cloud misconfigurations?

There is no single control that eliminates misconfiguration. Effective programs layer several practices into a defense-in-depth approach.

**Define infrastructure as code.** Provisioning resources through [infrastructure as code](/what-is/what-is-infrastructure-as-code/) rather than console clicks makes every setting explicit, reviewable, and repeatable. A configuration change becomes a code change that a teammate can read and approve.

**Shift security left.** Catch problems at the earliest possible moment (while the code is being written and reviewed) rather than after resources are live. A misconfiguration caught in a pull request costs minutes; one caught after a breach costs millions.

**Enforce policy as code.** [Policy as code](/what-is/what-is-policy-as-code/) expresses your security baseline as version-controlled rules that run automatically. Rules like "no bucket may be public" or "no security group may allow ingress from 0.0.0.0/0" are evaluated on every change and produce a pass or fail result, so enforcement no longer depends on a human remembering the rule.

**Apply least privilege.** Grant every identity only the permissions it needs, scoped to specific actions and resources, and prefer short-lived credentials over long-lived shared ones. This shrinks the blast radius of any single compromise.

**Run cloud security posture management (CSPM).** [CSPM](/what-is/what-is-cloud-security/) tools continuously scan a live cloud environment against a set of benchmarks (such as the CIS Foundations profiles) and flag resources that have drifted out of compliance. CSPM is detective: it finds misconfigurations that already exist, including those created outside of IaC. It complements preventative controls rather than replacing them.

**Monitor for drift.** Continuously compare the live state of your infrastructure against its declared, known-good configuration so that out-of-band changes are surfaced quickly instead of festering.

The strongest posture combines preventative controls (block the misconfiguration before it is created) with detective controls (find the ones that already exist or drifted in later). Neither alone is sufficient.

## How does infrastructure as code reduce misconfiguration?

Infrastructure as code attacks the root causes of misconfiguration directly, because it changes how settings get chosen and applied.

**Settings become explicit and reviewable.** When a resource is defined in code, every security-relevant setting (encryption, public access, ingress rules, IAM scope) is written down where a reviewer can see it. A pull request that opens a security group is visible in the diff, so a teammate can catch it before it merges. Configuration made by clicking through a console leaves no such artifact.

**Configuration is repeatable.** The same code produces the same resources across development, staging, and production. A secure baseline defined once applies everywhere, eliminating the environment-to-environment inconsistency where a resource is locked down in one place and wide open in another.

**Changes are versioned and auditable.** Every configuration change has an author, a timestamp, a reviewer, and a commit history. Compliance evidence becomes the repository history rather than a reconstruction after the fact, and any change can be rolled back.

**Automated checks get a place to run.** Because the configuration is code, automated policy checks can evaluate it before anything is deployed. That is the hook that makes preventative enforcement possible: the misconfiguration is caught while it is still just a proposed change.

Infrastructure as code does not, by itself, guarantee secure settings (you can still write code that makes a bucket public). What it guarantees is that the setting is visible, consistent, and checkable, which is the precondition for catching misconfigurations systematically instead of by luck. Even so, a gap remains where IaC adoption is incomplete: Datadog's State of DevSecOps 2024 found that while 71% of AWS organizations use IaC, 38% still used ClickOps in all accounts, including production, leaving room for misconfigurations to appear with no automated check.

## How does Pulumi help prevent cloud misconfigurations?

Pulumi addresses cloud misconfiguration on two fronts: making configuration reviewable and repeatable through infrastructure as code, and blocking or flagging insecure settings through policy as code. Pulumi is one part of a defense-in-depth strategy (dedicated CSPM platforms and cloud-native controls have their place too), but it closes the highest-leverage gap: catching misconfigurations before a resource is ever created.

**Infrastructure as code across every provider.** Pulumi lets you define cloud resources in TypeScript, Python, Go, C#, Java, or YAML across 200+ providers. Every setting is explicit in code, reviewed through pull requests, and applied consistently across environments, which removes the manual, console-driven changes that produce so many misconfigurations.

**Preventative policy enforcement during preview.** [Pulumi's policy as code](/docs/insights/policy/) evaluates resources during `pulumi preview` and `pulumi up`, before any change reaches the cloud. Rules such as "no S3 bucket may allow public access," "no security group may permit ingress from 0.0.0.0/0," or "all storage must be encrypted" run automatically on every deployment. A violation can warn (advisory mode), block the deployment (mandatory mode), or be corrected automatically (remediate mode), so a misconfiguration is stopped at the moment it is introduced rather than discovered after a breach.

**Pre-built compliance packs.** Pulumi publishes ready-to-use [policy packs](/docs/insights/policy/policy-packs/) for standards including CIS Foundations (AWS, Azure, and Google Cloud), NIST SP 800-53, and PCI DSS, so teams can enforce a recognized secure baseline without writing every rule from scratch.

**Audit of existing and discovered resources.** Preventative checks only cover what you deploy through Pulumi. To cover the rest, Pulumi's policy engine integrates with [Pulumi Discovery](/docs/insights/discovery/) to evaluate resources that already exist, including infrastructure provisioned with Terraform, CloudFormation, or directly through cloud consoles. This gives audit-mode visibility into misconfigurations across the whole estate, not just the resources managed with Pulumi.

**Drift detection.** Pulumi can run scheduled drift detection, comparing live infrastructure against its declared configuration and alerting when they diverge, so an out-of-band change that reintroduces a misconfiguration is surfaced instead of silently persisting.

[Discovery & governance](/product/discovery-governance/) lets a team prevent new misconfigurations at deploy time and continuously audit for existing ones, which is the preventative-plus-detective combination that a durable posture requires.

## Frequently asked questions about cloud misconfiguration

### What is cloud misconfiguration in simple terms?

Cloud misconfiguration is an insecure setting on a cloud resource. It means a resource (a storage bucket, a database, an identity, a firewall rule) has been configured in a way that exposes data or systems, such as making a bucket public or opening a database to the whole internet. The resource works as configured; the configuration is just wrong.

### What causes cloud misconfigurations?

They are caused by the collision of complexity, speed, and manual processes: insecure or permissive defaults, the sheer number of settings across a large cloud estate, changes made by clicking through a console with no review, configuration drift from out-of-band edits, and human error. Gartner has predicted that 99% of cloud security failures through 2025 would be the customer's fault, which is why automating configuration reduces them so effectively.

### What are examples of cloud misconfiguration?

Common examples include publicly accessible storage buckets, IAM policies that grant wildcard or administrative permissions, security groups that allow ingress from 0.0.0.0/0 to sensitive ports, storage and databases left unencrypted, disabled audit or access logging, secrets hard-coded into configuration or committed to a repository, and resources left with default or unrotated credentials.

### How do you prevent cloud misconfiguration?

Layer several controls: define infrastructure as code so settings are explicit and reviewable, shift security left to catch problems in pull requests, enforce policy as code so rules run automatically on every change, apply least privilege to identities, run CSPM tooling to scan live environments, and monitor for drift. Preventative controls that block a misconfiguration before deploy are cheaper than remediating one after the fact.

### What is the difference between a cloud misconfiguration and a vulnerability?

A vulnerability is a defect in software that an attacker must exploit, and you fix it by patching. A misconfiguration is a resource working exactly as configured, just configured insecurely, and you fix it by changing the settings. A public bucket needs no exploit at all: it is simply available to anyone who finds it. The two require different tools and different fixes, though both belong in a complete cloud security program.

### Does infrastructure as code prevent misconfiguration on its own?

Not entirely. Infrastructure as code makes every setting explicit, consistent across environments, versioned, and reviewable, which is the precondition for catching misconfigurations systematically. But you can still write code that configures a resource insecurely. The prevention comes from pairing IaC with policy as code, which automatically evaluates the configuration against security rules before it is deployed.

### Can misconfigurations be fixed automatically?

Yes, in some cases. Policy-as-code systems can support automatic remediation for settings where the correct value is deterministic. Pulumi's remediate enforcement level, for example, can enable encryption on a storage resource that a developer left unencrypted before the deployment proceeds, rather than simply failing. Remediation is most appropriate for rules where the fix is unambiguous and the goal is adoption.

## Learn more

Pulumi helps you prevent cloud misconfigurations at the source: define infrastructure as code so every setting is explicit and reviewable, then enforce security rules with policy as code that blocks insecure configurations during `pulumi preview` and audits existing resources through Insights. [Get started with Pulumi policy as code](/docs/insights/policy/get-started/) to catch your first misconfiguration before it reaches the cloud.

Related reading:

* [Pulumi policy as code documentation](/docs/insights/policy/)
* [Policy packs guide](/docs/insights/policy/policy-packs/)
* [Discovery & governance](/product/discovery-governance/)
* [Pulumi Discovery](/docs/insights/discovery/)
* [What is policy as code?](/what-is/what-is-policy-as-code/)
* [What is cloud security?](/what-is/what-is-cloud-security/)
* [What is infrastructure as code?](/what-is/what-is-infrastructure-as-code/)
* [What is infrastructure drift?](/what-is/what-is-infrastructure-drift/)
* [What is secrets management?](/what-is/what-is-secrets-management/)
* [What is platform engineering?](/what-is/what-is-platform-engineering/)
* [What is DevOps?](/what-is/what-is-devops/)
