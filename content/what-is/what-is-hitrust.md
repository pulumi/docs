---
title: What is HITRUST?
meta_desc: "HITRUST CSF is a certifiable security framework that harmonizes HIPAA, NIST, ISO 27001, and more into one assessment. Learn the levels, scope, and process."
meta_image: /images/what-is/what-is-hitrust-meta.png
type: what-is
page_title: "What is HITRUST?"
authors: ["asaf-ashirov"]
---

**HITRUST is an independent organization that maintains the HITRUST CSF, a certifiable security and privacy framework that consolidates the requirements from dozens of regulations and standards (HIPAA, NIST, ISO 27001, PCI DSS, GDPR, state laws) into a single set of prescriptive controls.** An organization completes one HITRUST assessment against the CSF and uses the resulting report to demonstrate compliance with all the underlying frameworks at once, rather than running separate audits for each.

HITRUST started in 2007 inside the healthcare industry as a way to bring order to the overlapping audit demands placed on covered entities and their vendors. It has since expanded well beyond healthcare and is widely used in financial services, public sector, and SaaS. HITRUST itself does not perform the audits; assessments are run by independent External Assessors (CPA firms, consultancies) and reviewed and certified by HITRUST.

In this article, we'll cover the key questions about HITRUST:

* Why does HITRUST matter?
* What is the HITRUST CSF?
* What does the HITRUST CSF harmonize?
* What are the HITRUST assessment types?
* How are HITRUST controls scored?
* How is HITRUST different from HIPAA, SOC 2, and ISO 27001?
* What does HITRUST certification involve?
* How does infrastructure as code support HITRUST controls?
* Frequently asked questions about HITRUST

## Why does HITRUST matter?

For a healthcare or healthtech vendor, HITRUST is often the most direct path to selling into US health plans, hospital systems, and large pharmacy benefit managers. Customer security teams ask for it by name in vendor questionnaires, and the certification short-circuits a lot of bespoke security review. Three forces drive its adoption:

* **One audit, many frameworks.** Instead of separate audits for HIPAA, NIST 800-53, and ISO 27001, a single HITRUST r2 assessment maps to all of them. For vendors selling into regulated buyers, that's a sizable reduction in audit toil.
* **Demonstrably lower breach rate.** HITRUST publishes that fewer than 1% of HITRUST-certified environments report a security breach in a given year, compared with much higher double-digit rates across the broader industry. Whether that's selection bias or the controls themselves, the number is what buyers cite.
* **Predictable contractual gate.** Large healthcare buyers increasingly require HITRUST CSF certification (or evidence of an active assessment) as a precondition of executing a business associate agreement. Without it, deals stall.

## What is the HITRUST CSF?

The HITRUST CSF (Common Security Framework) is a prescriptive, certifiable set of security and privacy controls. Unlike HIPAA, which describes outcomes without specifying technical controls, the CSF spells out concrete requirement statements that an organization either implements or doesn't.

The framework is structured around:

* **14 control categories** that cover the breadth of an information security program (access control, vulnerability management, business continuity, etc.).
* **49 control objectives** that describe what each category is trying to achieve.
* **156 control references** that name specific controls.
* **More than 1,900 requirement statements** distributed across **19 assessment domains**, which is where the actual audit testing happens.

The CSF is **risk-based and scalable**. The requirements that apply to your organization depend on factors like industry, organization size, geographic footprint, data sensitivity, and the systems in scope. A small health-tech SaaS gets a different requirement set than a national hospital network. The framework also has a *threat-adaptive* layer that updates control requirements based on observed threat intelligence and breach data.

## What does the HITRUST CSF harmonize?

The point of the CSF is to roll many compliance regimes into one. The latest CSF versions cross-reference 60+ major authoritative sources (HITRUST's marketing site totals "over 70" when you count sub-standards), including:

* **Healthcare:** HIPAA, HITECH, 42 CFR Part 2
* **US federal:** NIST SP 800-53, NIST SP 800-171, FedRAMP, CMMC
* **International:** ISO/IEC 27001, ISO/IEC 27002, ISO 27799, GDPR
* **Payment:** PCI DSS
* **Cloud:** Cloud Security Alliance CCM, FedRAMP cloud controls
* **State laws:** New York DFS Cybersecurity Regulation, Texas Health & Safety Code, MA 201 CMR 17.00, and others

A HITRUST report can be issued with a specific cross-reference set, so a vendor can hand the same report to an auditor who needs HIPAA evidence and another who needs NIST 800-53 evidence.

## What are the HITRUST assessment types?

HITRUST publishes three assessment levels. They differ in scope, rigor, validity period, and the assurance they provide to a relying customer.

| Assessment | Scope | Validity | Best for |
|---|---|---|---|
| **e1 (Essentials)** | ~44 foundational requirements covering basic cyber hygiene. | 1 year | Early-stage vendors and small organizations establishing a baseline. |
| **i1 (Implemented)** | ~182 controls covering leading security practices, threat-adapted. | 1 year (rapid recertification in year 2) | Mid-market vendors that need to demonstrate solid practices to enterprise buyers. |
| **r2 (Risk-Based, 2-Year)** | Customized scope drawn from the full CSF (often 350+ requirements), tailored by risk factors. | 2 years (with an interim assessment at year 1) | The traditional "HITRUST certified" report. Required by most healthcare enterprise buyers. |

The earlier terminology ("HITRUST CSF Validated," "HITRUST CSF Certified") still appears in older contracts; r2 is the current name for the highest-rigor option.

## How are HITRUST controls scored?

Each in-scope requirement is evaluated against a five-level **PRISMA-derived maturity model**. A control isn't just present or absent; the assessor scores how mature its implementation is across these levels:

1. **Policy.** A written, approved policy exists that addresses the requirement.
1. **Procedure.** Documented procedures translate the policy into operational steps.
1. **Implemented.** The control is actually operating in systems and processes.
1. **Measured.** The control's effectiveness is tested and reported on.
1. **Managed.** Findings from measurement feed back into improvements over time.

Each level gets a percentage score (0-100%). The overall control score is a weighted combination across the levels, and a control passes certification at 3+ (a passing score, conventionally 62+ out of 100). The same maturity framing applies whether the assessment is e1, i1, or r2.

## How is HITRUST different from HIPAA, SOC 2, and ISO 27001?

These frameworks overlap heavily, but they answer different questions.

| Framework | What it is | Prescriptive controls? | Auditor model | Common use |
|---|---|---|---|---|
| **HIPAA** | US federal law for health information | No (outcomes, not controls) | HHS / OCR enforcement | Mandatory for US health data |
| **HITRUST CSF** | Certifiable framework that maps to many regimes | Yes (1,900+ requirement statements) | HITRUST + External Assessor | Healthcare and other regulated vendors that want one audit for many regimes |
| **SOC 2** | AICPA attestation against Trust Services Criteria | Partially (criteria, customer-defined controls) | Independent CPA firm | SaaS vendors selling to US enterprise buyers |
| **ISO/IEC 27001** | International ISMS standard | Partially (risk-based selection from Annex A via SoA) | Accredited certification body | International enterprises and vendors selling globally |

In practice:

* **HIPAA** is a legal floor for US health data.
* **HITRUST** is how a healthcare vendor *proves* it meets HIPAA (and many other regimes) to its customers.
* **SOC 2** is how a SaaS vendor proves operational security to enterprise buyers, often paired with HITRUST in healthcare.
* **ISO 27001** is the international equivalent for global buyers.

Many healthcare-adjacent vendors maintain both SOC 2 and HITRUST. SOC 2 gives buyers an attestation against a familiar US criteria set; HITRUST gives them a healthcare-specific, certifiable framework.

## What does HITRUST certification involve?

A typical r2 certification runs 6–18 months from kickoff to report, depending on scope, prior maturity, and remediation load. The major phases:

1. **Readiness assessment (optional but typical).** A self-assessment or facilitated gap analysis using HITRUST's MyCSF platform to identify control gaps before a paid audit.
1. **Scoping.** Determine which systems, locations, and data types are in scope and which risk factors drive your specific requirement set.
1. **Remediation.** Implement the missing controls, write the missing policies and procedures, and operate them long enough to produce evidence.
1. **Validated assessment.** An authorized External Assessor tests every in-scope control across the maturity levels, gathers evidence, and submits findings to HITRUST.
1. **HITRUST QA and report issuance.** HITRUST reviews the External Assessor's work and issues the certified report.
1. **Interim assessment (year 1).** For r2, a lighter-weight check during the certification period to confirm controls are still operating.
1. **Recertification.** Every two years for r2, annually for e1 and i1.

The first time through, expect months of work on policies, procedures, and evidence collection. Subsequent cycles are faster because the program is already running.

## How does infrastructure as code support HITRUST controls?

A large share of HITRUST CSF requirements describe technical infrastructure controls: encryption, network segmentation, IAM, logging, configuration management, change control, vulnerability management. These are exactly the controls that [infrastructure as code](/what-is/what-is-infrastructure-as-code/) lets you enforce, audit, and prove.

Pulumi ships a HITRUST policy pack specifically for AWS:

```bash
pulumi policy new aws-hitrust-compliance-policies-typescript
```

The pack contains prebuilt [CrossGuard](/docs/insights/policy/) policies that block non-compliant configurations in CI before they deploy. Source and customization details are in the [aws-hitrust-compliance-policies-typescript template](https://github.com/pulumi/templates-policy/tree/master/aws-hitrust-compliance-policies-typescript).

More broadly, Pulumi helps with HITRUST control maturity in concrete ways:

* **Policy maturity (level 1).** Encode security policy as code with [Pulumi CrossGuard](/docs/insights/policy/). Policy lives in version control with the same review process as application code.
* **Procedure maturity (level 2).** The Pulumi program is itself the procedure. The same code is run by every engineer in every environment.
* **Implementation maturity (level 3).** Pulumi applies the configuration. The state file is evidence that the control was deployed.
* **Measurement maturity (level 4).** `pulumi preview` and policy reports give auditors continuous evidence of compliance status across accounts and clouds.
* **Managed maturity (level 5).** Findings from policy violations and drift detection flow into the same backlog as application bugs and feed the next iteration.

* **Centralized secrets.** [Pulumi ESC](/product/esc/) keeps secrets out of code and CI logs, with audit trails for every read.
* **Reusable secure defaults.** Platform teams ship [Pulumi components](/docs/iac/concepts/components/) with HITRUST-aligned settings baked in (encryption, logging, restricted IAM), so product teams consume compliant infrastructure by default.

[Get started with Pulumi](/docs/get-started/) to manage HITRUST-relevant cloud infrastructure as code in TypeScript, Python, Go, C#, Java, or YAML.

## Frequently asked questions about HITRUST

### What does HITRUST stand for?

HITRUST originally stood for "Health Information Trust Alliance." The organization has since dropped the long-form name and goes by HITRUST. The framework itself is the HITRUST CSF (Common Security Framework).

### Is HITRUST only for healthcare?

No. HITRUST originated in healthcare and is still most common there, but the CSF is used well beyond it — financial services, public sector, and SaaS in particular. The harmonized control set works for any organization that has to satisfy multiple compliance regimes at once.

### Is HITRUST certification required for HIPAA compliance?

No. HIPAA is a US federal law; HITRUST is a private framework. You can be HIPAA-compliant without HITRUST, and HITRUST certification doesn't automatically make you HIPAA-compliant. HITRUST is widely used because a single CSF assessment cross-references to HIPAA requirements, which makes it easier to demonstrate HIPAA compliance to customers and auditors.

### What's the difference between HITRUST CSF Certified and HITRUST r2?

They refer to the same assessment level. "HITRUST CSF Certified" was the older naming; "r2" (Risk-Based, 2-Year) is the current name, introduced in 2021. Reports issued before then typically use the older terminology, but the rigor is unchanged.

### How long does HITRUST certification take?

A first-time r2 certification typically runs 6–18 months from kickoff to issued report, including readiness, remediation, validated assessment, and HITRUST QA review. The lighter-weight e1 and i1 assessments run shorter (often 4–9 months for first-time issuance). Recertification cycles are faster than the first round.

### How much does HITRUST certification cost?

Total cost varies widely by scope and assessment level. MyCSF platform subscriptions start around $18,000 per year (per HITRUST's published pricing). The External Assessor fee for an r2 is typically in the low-to-mid six figures for a first-time assessment. Internal remediation and program-building costs usually exceed the external fees. Smaller e1 and i1 assessments are correspondingly cheaper.

### Can a HITRUST report replace a SOC 2 report?

Not directly. Many enterprise buyers (especially outside healthcare) specifically ask for SOC 2, and an AICPA-issued SOC 2 attestation is the only way to satisfy that request. There is a combined HITRUST + AICPA SOC 2 report option that lets a single audit produce both a SOC 2 attestation and a HITRUST CSF report, which is a common path for vendors that need both.

### What is MyCSF?

MyCSF is HITRUST's web-based assessment platform. It hosts the requirement set tailored to your organization, captures evidence and scoring, and is the system of record that External Assessors and HITRUST QA use to review your assessment. Every HITRUST assessment runs in MyCSF.

### How does HITRUST treat cloud infrastructure?

HITRUST treats cloud workloads like any other in-scope system. The customer is responsible for controls on the configurations they own (IAM, encryption, network, logging), while the cloud provider is responsible for the platform. AWS, Azure, and Google Cloud all publish HITRUST-relevant control inheritance documentation that customers can cite to reduce their own evidence burden for shared controls.

### What is "control inheritance" in HITRUST?

A way to reuse controls operated by another party (a cloud provider, a SaaS vendor, or a shared internal service) instead of testing them yourself. If AWS has a current HITRUST report, you can inherit its physical security and platform-level controls and only test the controls you operate on top. Inheritance significantly reduces the size of a customer's assessment.

## Learn more

Pulumi gives engineering teams the tooling to make HITRUST CSF controls live in code: encrypted resources by default, least-privilege IAM, [CrossGuard policies](/docs/insights/policy/) that block non-compliant infrastructure in CI, and a pre-built [AWS HITRUST policy pack](https://github.com/pulumi/templates-policy/tree/master/aws-hitrust-compliance-policies-typescript) to accelerate the technical work. [Get started today](/docs/get-started/).

Related reading:

* [What is HIPAA?](/what-is/what-is-hipaa/)
* [What is SOC 2?](/what-is/what-is-soc-2/)
* [What is Cloud Security?](/what-is/what-is-cloud-security/)
* [What is Secrets Management?](/what-is/what-is-secrets-management/)
* [What is Configuration Management?](/what-is/what-is-configuration-management/)
