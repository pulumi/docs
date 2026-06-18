---
title: What is SOC 2?
meta_desc: "SOC 2 is an AICPA attestation that proves a service provider's controls meet the Trust Services Criteria. Learn Type I vs Type II, scope, and the audit process."
meta_image: /images/what-is/what-is-soc-2-meta.png
type: what-is
page_title: "What is SOC 2?"
authors: ["alex-leventer"]
---

**SOC 2 (System and Organization Controls 2) is an attestation report produced by an independent CPA firm that evaluates a service provider's controls against the AICPA's Trust Services Criteria (security, availability, processing integrity, confidentiality, and privacy).** A SOC 2 report is the document that most US enterprise buyers ask SaaS vendors to produce before signing a contract.

SOC 2 is voluntary. There is no law that requires it. It exists because enterprise procurement and security teams need a consistent way to evaluate the security posture of the dozens or hundreds of SaaS vendors they buy from, and bespoke vendor questionnaires don't scale. SOC 2 standardizes the evaluation: the AICPA defines the criteria, a CPA firm tests against them, and the resulting report is shared (under NDA) with prospective customers. SOC 2 is governed by the AICPA's [SSAE 18](https://us.aicpa.org/research/standards/auditattest/ssae) attestation standard.

In this article, we'll cover the key questions about SOC 2:

* Why does SOC 2 matter?
* What are the SOC 2 Trust Services Criteria?
* What is the difference between SOC 2 Type I and Type II?
* What are SOC 1, SOC 2, and SOC 3?
* What is a SOC 2+ report?
* What does the SOC 2 audit process involve?
* How does SOC 2 compare to ISO 27001 and HITRUST?
* How does infrastructure as code support SOC 2?
* Frequently asked questions about SOC 2

## Why does SOC 2 matter?

For a B2B SaaS company selling into US enterprise, SOC 2 is most often the security gate that controls revenue. Three forces drive its importance:

* **Sales unblocker.** Enterprise security reviews routinely ask "Do you have a SOC 2 Type II?" as the first question. A current report short-circuits a months-long bespoke security review and replaces it with a 30-minute discussion of the auditor's findings.
* **Trust without disclosure.** A SOC 2 report communicates the substance of a vendor's security program without exposing the underlying configurations, runbooks, or policies. It's the level of detail buyers want and vendors are willing to share.
* **Forcing function for the security program.** Even when no customer is asking for it yet, going through a SOC 2 program is the most common way for an early-stage company to formalize its security policies, controls, and incident response.

A SOC 2 isn't a regulatory requirement, but for most SaaS companies past the early-customer stage, not having one becomes an operational and competitive problem.

## What are the SOC 2 Trust Services Criteria?

The Trust Services Criteria (TSC) are the AICPA-defined principles a SOC 2 report attests to. There are five. Every SOC 2 report covers **Security**; the other four are optional and chosen based on what the service actually does for customers.

| Criterion | What it covers | When it applies |
|---|---|---|
| **Security** (required) | System protection against unauthorized access, both logical and physical. Also called the "common criteria." | Every SOC 2. |
| **Availability** | Whether the system meets its uptime/availability commitments. Includes performance monitoring, DR, business continuity. | Services with SLAs or uptime commitments. |
| **Processing Integrity** | Whether system processing is complete, accurate, timely, and authorized. | Services that transform or compute on customer data (payment processors, data pipelines, billing engines). |
| **Confidentiality** | How information designated confidential is protected (encryption, NDAs, secure disposal). | Services handling commercially sensitive customer data. |
| **Privacy** | How personal information is collected, used, retained, disclosed, and disposed of. Maps to fair information practices. | Services that collect personal data directly from end users. |

Most SaaS vendors start with just Security, then add Availability once they have a real uptime commitment. Confidentiality and Privacy are added when customer contracts or regulators require them. Processing Integrity is less common outside of fintech and data-processing platforms.

## What is the difference between SOC 2 Type I and Type II?

The two SOC 2 report types differ in what the auditor is attesting to.

| Aspect | Type I | Type II |
|---|---|---|
| Question answered | Are the controls suitably **designed** at this moment in time? | Are the controls **operating effectively** over a period? |
| Period covered | A single date | Typically 3 to 12 months (6- and 12-month windows are most common) |
| Evidence | Snapshot of policies, procedures, configurations | Multiple samples of each control across the period |
| Time to issue | Faster (often weeks) | Slower (months, plus the observation period) |
| Buyer preference | Acceptable as a starting point | Strongly preferred; required by most enterprise buyers |

A Type I is what most companies issue first because it can be earned as soon as the controls are designed and in place. A Type II requires those controls to have been running for at least 3 months (most first audits use a 6-month window; 12 months is standard for the steady-state cycle), with evidence collected throughout, and is what enterprise customers ultimately want to see. Many vendors do Type I once and then move to a continuous Type II cycle.

## What are SOC 1, SOC 2, and SOC 3?

The AICPA publishes three SOC report families. They sound similar but address different audiences.

| Report | What it covers | Audience |
|---|---|---|
| **SOC 1** | Internal controls over financial reporting (ICFR). | Customers' financial auditors. Required for service providers that affect customer financial statements (payroll, payment processing). |
| **SOC 2** | Trust Services Criteria (security, availability, processing integrity, confidentiality, privacy). | Customer security and procurement teams. The standard for SaaS. |
| **SOC 3** | Same scope as SOC 2 but in a public-summary format with no detailed control descriptions. | Public-facing marketing; can be posted on a website. |

For nearly every SaaS company, **SOC 2** is the report that matters. SOC 1 is for service providers whose offerings affect their customers' financial reporting. SOC 3 is the same content as SOC 2, packaged for public distribution; some vendors publish a SOC 3 alongside a SOC 2 so they can publicly attest to their compliance without exposing the report itself.

## What is a SOC 2+ report?

A SOC 2+ extends a standard SOC 2 to also cover the controls required by another framework. The auditor runs both assessments under one engagement and issues a combined report. Common combinations:

* **SOC 2 + HITRUST CSF.** Frequently chosen by healthcare-adjacent SaaS vendors. Produces a SOC 2 attestation and a HITRUST CSF report from a single audit.
* **SOC 2 + HIPAA.** Maps SOC 2 controls explicitly to HIPAA Security Rule requirements.
* **SOC 2 + ISO 27001.** A combined attestation against the Trust Services Criteria and the ISO Annex A control set, useful for vendors selling internationally.
* **SOC 2 + NIST CSF.** Maps SOC 2 controls to the NIST Cybersecurity Framework categories.
* **SOC 2 + CSA STAR.** Adds the Cloud Security Alliance's Cloud Controls Matrix.

SOC 2+ reduces audit fatigue: one engagement, one evidence collection, one set of auditor interviews. The trade-off is a longer audit and a higher fee than a SOC 2 alone.

## What does the SOC 2 audit process involve?

A typical first SOC 2 Type II runs 6–12 months from kickoff to issued report: usually 3–6 months of readiness and remediation, followed by the observation period and audit fieldwork.

1. **Scope the assessment.** Decide which Trust Services Criteria are in scope, which products and environments are covered, and which entity is the reporting organization.
1. **Readiness assessment.** A gap analysis (often done by the future auditor in a separate engagement, or by a compliance-automation vendor) that identifies missing or weak controls before the formal audit.
1. **Remediation.** Build the missing policies, procedures, and technical controls. Document everything. This is usually the longest phase for a first-time SOC 2.
1. **Observation period.** For Type II, controls must operate for the audit period (typically 6 or 12 months). Evidence is collected continuously through this window.
1. **Audit fieldwork.** The CPA firm tests samples of each control, interviews control owners, and reviews documentation. The auditor produces draft findings.
1. **Management response and report issuance.** Management responds to any exceptions; the auditor issues the final SOC 2 report.
1. **Annual renewal.** Most vendors recertify every 12 months on a rolling basis to maintain an unbroken Type II coverage window.

Vendors at the start of their SOC 2 journey often use **compliance-automation platforms** (Vanta, Drata, Secureframe, Thoropass) to manage policy templates, evidence collection, and continuous monitoring. They don't replace the auditor; they reduce the manual evidence burden for both first audit and annual recertification.

## How does SOC 2 compare to ISO 27001 and HITRUST?

All three demonstrate security maturity, but they take different approaches.

| Framework | Origin | Format | Scope | Buyer use |
|---|---|---|---|---|
| **SOC 2** | AICPA (US) | Attestation report from a CPA firm | Customer-defined controls tested against Trust Services Criteria | US enterprise buyers, most SaaS sales motions |
| **ISO/IEC 27001** | ISO/IEC (international) | Certification from an accredited certification body | ISMS scope defined by the organization, against Annex A controls | International buyers, especially EU and APAC |
| **HITRUST CSF** | HITRUST Alliance | Certification from HITRUST after External Assessor work | Risk-based controls drawn from HIPAA, NIST, ISO, PCI, GDPR, etc. | Healthcare and other regulated buyers |

Many SaaS vendors maintain SOC 2 plus one of the others: SOC 2 + ISO 27001 for global software vendors, SOC 2 + HITRUST for healthcare. See [What is HITRUST?](/what-is/what-is-hitrust/) for the healthcare-focused option.

## How does infrastructure as code support SOC 2?

A large share of SOC 2 evidence is technical: who has access to what, what's encrypted, what's logged, how changes get reviewed, how incidents are handled. These are the exact areas where [infrastructure as code](/what-is/what-is-infrastructure-as-code/) shortens the audit cycle and reduces remediation work.

Concrete patterns:

* **Change management evidence.** Every infrastructure change is a pull request with author, approver, and timestamp. The same artifact that lets developers ship is the artifact the auditor wants for change-management controls.
* **Access control as code.** IAM roles, group memberships, and trust policies live in Pulumi programs that get reviewed in code, not configured by hand in a console. Auditors can read the code and the diff history to verify least-privilege controls.
* **Policy as code in CI.** [Pulumi Policies](/docs/insights/policy/) block insecure configurations (public storage, missing encryption, wildcard IAM) in CI before they ever reach production. The auditor's question "how do you prevent public S3 buckets?" has a code-and-CI-log answer.
* **Secrets management.** [Pulumi ESC](/product/esc/) keeps secrets out of code, CI logs, and state files, and gives every read an audit trail. SOC 2 controls around access to sensitive credentials line up directly.
* **Reusable secure defaults.** Platform teams ship [Pulumi components](/docs/iac/concepts/components/) with encryption, logging, and IAM baked in. Product teams consume secure infrastructure by default, and the auditor sees a single component definition instead of dozens of one-off configurations to test.
* **Drift detection.** When a console click breaks the IaC contract, the next `pulumi preview` surfaces it. Auditors can see a clean control loop instead of asking how unauthorized changes would be detected.

[Get started with Pulumi](/docs/get-started/) to manage SOC 2-relevant cloud infrastructure as code in TypeScript, JavaScript, Python, Go, .NET, Java, or YAML.

## Frequently asked questions about SOC 2

### Is SOC 2 required by law?

No. SOC 2 is a voluntary attestation framework published by the AICPA. There is no jurisdiction where SOC 2 itself is legally required. It becomes effectively required through contracts when enterprise customers make a current SOC 2 report a condition of doing business.

### Is SOC 2 a certification?

Technically no. SOC 2 is an *attestation*, not a certification. An auditor attests that your controls meet the Trust Services Criteria; no body issues a "SOC 2 certificate." Even so, "SOC 2 certified" is common shorthand for "has a current SOC 2 Type II report."

### Type I or Type II: which one do I need?

In the long run, Type II. Type I attests to the *design* of controls at a moment in time; Type II attests that those controls *operated effectively* over a period (usually 6 or 12 months). Enterprise buyers ask for Type II. Many vendors issue a Type I first to get something to share with customers while they accumulate the observation period for their initial Type II.

### How long does SOC 2 take?

A first-time Type II typically takes 6–12 months from kickoff to issued report, dominated by remediation work and the observation period. Type I can be issued in a few weeks to a few months. Subsequent annual Type II cycles are faster, since the program is already running.

### How much does SOC 2 cost?

For a small-to-midsize SaaS company, first-year total cost (readiness + remediation + audit) commonly lands in the $30,000–$100,000 range. Audit fees alone are typically $15,000–$50,000 depending on scope and firm. Compliance-automation platforms add a per-year subscription but usually reduce the internal labor cost more than they add.

### Do we need to include all five Trust Services Criteria?

No. Security is the only required criterion. The other four (Availability, Processing Integrity, Confidentiality, Privacy) are included only when they're relevant to what the service does and what customers are asking for. Most SaaS companies start with Security alone or Security + Availability and add more over time.

### Who can perform a SOC 2 audit?

Only a CPA firm. Compliance-automation platforms and consultancies can prepare you for the audit, but the attestation report itself must be issued by a CPA firm licensed by a state board of accountancy and following the AICPA's SSAE 18 attestation standard. Choose a firm with real SaaS experience, since not every CPA firm does SOC 2 work.

### Can I share my SOC 2 report publicly?

Generally no. SOC 2 reports contain detail about your control environment, system descriptions, and sometimes specific findings that you don't want competitors or attackers reading. Reports are typically shared under NDA. If you want a publicly shareable summary, issue a SOC 3 alongside your SOC 2.

### Does a SOC 2 report cover subprocessors?

Partially. The report's system description should disclose subservice organizations and indicate whether their controls are "carved out" (not in scope, customer's responsibility to evaluate separately) or "inclusive" (in scope, tested as part of your audit). The carve-out method is more common. Subprocessors' own SOC 2 reports are how you complete the picture.

### How does SOC 2 relate to GDPR or other privacy laws?

A SOC 2 with the Privacy criterion covers the substance of many GDPR and CCPA controls, but a SOC 2 alone is not a GDPR or CCPA compliance certificate. Privacy laws have their own legal requirements (data subject rights, lawful basis, breach notification timelines) that go beyond what SOC 2 attests to. SOC 2 is often the substrate; privacy compliance sits on top.

## Learn more

Pulumi helps engineering teams put SOC 2 evidence into code: every change is a reviewable pull request, [policy as code](/docs/insights/policy/) blocks non-compliant configurations in CI, secrets live in [a central encrypted store](/product/esc/), and platform teams ship secure defaults as [reusable components](/docs/iac/concepts/components/). [Get started today](/docs/get-started/).

Related reading:

* [What is Cloud Security?](/what-is/what-is-cloud-security/)
* [What is HIPAA?](/what-is/what-is-hipaa/)
* [What is HITRUST?](/what-is/what-is-hitrust/)
* [What is Secrets Management?](/what-is/what-is-secrets-management/)
* [What is Configuration Management?](/what-is/what-is-configuration-management/)
