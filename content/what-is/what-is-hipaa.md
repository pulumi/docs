---
title: What is HIPAA?
meta_desc: "HIPAA is the US law that sets national standards for protecting health information. Learn its rules, who it covers, penalties, and how to comply."
type: what-is
page_title: "What is HIPAA?"
authors: ["alex-leventer"]
---

**HIPAA (the Health Insurance Portability and Accountability Act of 1996) is the US federal law that sets national standards for the privacy, security, and breach notification of protected health information (PHI).** It governs how healthcare providers, insurers, clearinghouses, and any vendor handling health data on their behalf may use, disclose, transmit, and store that data, and it carries civil and criminal penalties for organizations that fall short.

HIPAA was enacted to make health coverage portable across job changes and to bring consistent standards to an industry where patient records were transitioning from paper to electronic systems. The privacy and security provisions are what most people now mean when they say "HIPAA compliance." Subsequent legislation, most importantly the HITECH Act of 2009 and the 2013 Omnibus Rule, expanded the law's reach to vendors, increased penalties, and added mandatory breach notification. The law is administered by the US Department of Health and Human Services (HHS) Office for Civil Rights (OCR).

In this article, we'll cover the key questions about HIPAA:

* Why does HIPAA matter?
* Who has to comply with HIPAA?
* What is protected health information (PHI)?
* What are the HIPAA rules?
* What are the HIPAA Security Rule safeguards?
* What are the most common HIPAA violations?
* What are the penalties for HIPAA non-compliance?
* How do you achieve HIPAA compliance?
* How does HIPAA apply to cloud infrastructure?
* Frequently asked questions about HIPAA

## Why does HIPAA matter?

For any organization that touches US healthcare data, HIPAA isn't optional. The Office for Civil Rights resolves thousands of complaints each year and posts every breach affecting 500 or more people to a public list, often called the "wall of shame." Beyond the regulatory exposure, three things make HIPAA practically important:

* **Patient trust.** Without enforceable privacy rules, patients have less reason to share accurate medical information, which degrades the quality of care.
* **Contractual gating.** Any vendor that wants to do business with a covered entity has to sign a business associate agreement (BAA), and the customer's procurement team will demand evidence of HIPAA controls before signing.
* **Breach economics.** Healthcare consistently ranks as the highest-cost industry for data breaches in the IBM Cost of a Data Breach report, well above retail or financial services. A single incident routinely runs into the millions in remediation, notification, and litigation.

## Who has to comply with HIPAA?

HIPAA divides the regulated world into two groups.

**Covered entities** are the organizations the law directly governs:

* Healthcare providers that transmit health information electronically (hospitals, clinics, doctors, dentists, pharmacies, etc.)
* Health plans (insurance companies, HMOs, employer-sponsored plans, Medicare, Medicaid)
* Healthcare clearinghouses that process health-data transactions between providers and payers

**Business associates** are vendors that create, receive, maintain, or transmit PHI on behalf of a covered entity. The category is broad: cloud hosting providers, SaaS analytics tools, billing services, transcription services, IT consultants, document shredding companies. If you handle PHI for a covered entity, you're a business associate, and the same security and breach-notification obligations apply to you. Business associates must sign a BAA with the covered entity and may need their own BAAs with their subcontractors.

## What is protected health information (PHI)?

PHI is any individually identifiable health information that is created, used, or disclosed in the course of providing healthcare. When it's stored or transmitted electronically, it's called **electronic PHI (ePHI)**, which is the form HIPAA's Security Rule applies to.

The Privacy Rule lists 18 identifiers that, combined with health information, make a record PHI:

* Names
* All geographic subdivisions smaller than a state (street, city, ZIP for many regions)
* All elements of dates (other than year) tied to an individual
* Telephone, fax, email addresses
* Social Security numbers, medical record numbers, health plan beneficiary numbers, account numbers, certificate or license numbers
* Vehicle and device identifiers and serial numbers
* Web URLs and IP addresses tied to an individual
* Biometric identifiers including fingerprints and voice prints
* Full-face photographs and any comparable images
* Any other unique identifying number, characteristic, or code

If a dataset is fully de-identified per the Safe Harbor or Expert Determination methods, it's no longer PHI and falls outside HIPAA.

## What are the HIPAA rules?

Most HIPAA compliance work organizes around five rules issued by HHS over the past two decades.

| Rule | Year | What it covers |
|---|---|---|
| **Privacy Rule** | 2000 | Defines PHI and patient rights; sets the conditions under which PHI may be used or disclosed. (Modified 2002; compliance 2003.) |
| **Security Rule** | 2003 | Requires administrative, physical, and technical safeguards for ePHI. (Compliance 2005.) |
| **Enforcement Rule** | 2006 | Procedures for HHS investigations, hearings, and penalty calculations. |
| **Breach Notification Rule** | 2009 (HITECH) | Mandatory notification to individuals, HHS, and (for breaches ≥500 people) the media when unsecured PHI is exposed. |
| **Omnibus Rule** | 2013 | Extended direct liability to business associates, raised penalty tiers, tightened use of PHI for marketing and fundraising. |

The Privacy Rule sets policy (what may be done with PHI); the Security Rule sets technical baseline (how ePHI must be protected); the Breach Notification Rule sets incident handling (what to do when something goes wrong); the Enforcement Rule sets consequences; and the Omnibus Rule modernized everything for the cloud and SaaS era.

## What are the HIPAA Security Rule safeguards?

The Security Rule is what most engineering teams actually implement. It requires three categories of safeguards for ePHI.

| Category | What it covers | Example controls |
|---|---|---|
| **Administrative** | Policies, people, and process | Risk analysis, workforce training, access management procedures, security incident procedures, contingency planning, periodic security evaluations |
| **Physical** | Facility and device protection | Facility access controls, workstation use and security policies, device and media controls, equipment disposal |
| **Technical** | System-level controls on ePHI | Unique user IDs, encryption of ePHI at rest and in transit, automatic logoff, audit logs, integrity controls, transmission security |

The Security Rule classifies individual requirements as either **required** (must be implemented exactly) or **addressable** (must be implemented or, if not, documented with a justified alternative). Addressable is not the same as optional. Auditors expect a written rationale for any addressable requirement that isn't fully implemented.

## What are the most common HIPAA violations?

OCR breach data shows the same patterns year after year:

1. **Hacking and IT incidents.** The largest category by number of records exposed: phishing, ransomware, unauthorized access, compromised credentials.
1. **Unauthorized access and disclosure.** Employees viewing records they shouldn't (often called snooping), or mis-sent emails and faxes.
1. **Theft or loss of devices.** Unencrypted laptops, USB drives, and phones containing ePHI.
1. **Improper disposal.** Patient records thrown out without shredding; old hard drives sold without wiping.
1. **Lack of risk analysis.** No documented, ongoing assessment of where ePHI lives and what threatens it. A specific HIPAA requirement and one of the most-cited findings in enforcement actions.
1. **Missing or inadequate BAAs.** Sharing PHI with vendors before a business associate agreement is in place.
1. **Insufficient access controls.** Wide-open admin roles, shared accounts, no auditing.

## What are the penalties for HIPAA non-compliance?

HIPAA penalties run on a four-tier structure based on culpability, with per-violation amounts and an annual cap for each tier. HHS adjusts the dollar amounts annually for inflation, so figures shift each year; the structure is constant:

| Tier | Culpability | Range |
|---|---|---|
| 1 | The entity did not know and could not reasonably have known | Lowest per-violation amount |
| 2 | Reasonable cause, not willful neglect | Higher than tier 1 |
| 3 | Willful neglect, corrected within 30 days | Higher than tier 2 |
| 4 | Willful neglect, not corrected | Highest per-violation amount |

Beyond civil penalties, HIPAA also creates a three-tier criminal scheme under 42 U.S.C. § 1320d-6: knowingly obtaining or disclosing PHI starts at up to $50,000 and 1 year in prison; doing so under false pretenses raises it to $100,000 and 5 years; and doing so with intent to sell, transfer, or use PHI for commercial advantage, personal gain, or malicious harm carries the maximum of $250,000 and 10 years. State attorneys general can also bring civil actions, and private litigation under state law often follows large breaches.

For current dollar figures, see HHS's [HIPAA Compliance and Enforcement](https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/index.html) page, which links to the most recent civil monetary penalty inflation adjustments.

## How do you achieve HIPAA compliance?

Compliance is a continuous program, not a one-time project. The typical scope:

1. **Inventory PHI.** Map every system, vendor, and workflow that creates, stores, or transmits ePHI. You can't protect what you can't see.
1. **Run a risk analysis.** A documented, formal assessment of threats, vulnerabilities, and likelihoods for each ePHI asset. Required by the Security Rule and the single most-cited gap in OCR enforcement.
1. **Implement administrative, physical, and technical safeguards.** Each control either matches a required Security Rule provision or addresses an addressable one with a documented alternative.
1. **Sign BAAs with every business associate.** No PHI may flow to a vendor before the agreement is in place. Maintain a vendor inventory and refresh BAAs as relationships change.
1. **Train the workforce.** Annual at minimum, with role-specific content for anyone who touches ePHI. Document the training.
1. **Encrypt ePHI at rest and in transit.** Encryption is an addressable specification under the Security Rule, but properly encrypted data that's exposed is exempt from breach notification, which is a strong practical incentive to encrypt.
1. **Log and monitor.** Audit logs of access to ePHI, periodic review, alerting on anomalies. The Security Rule requires both logging and periodic review.
1. **Have an incident response plan.** Documented procedures for detecting, containing, and notifying on breaches of unsecured PHI, including the 60-day reporting deadline.
1. **Conduct periodic security evaluations.** A scheduled re-assessment to confirm controls still match how the business and the threat landscape have changed.

Smaller organizations often pursue a HITRUST CSF certification as a way to demonstrate HIPAA controls through a single, structured assessment that customers and auditors recognize. See [What is HITRUST?](/what-is/what-is-hitrust/) for how that fits into HIPAA programs.

## How does HIPAA apply to cloud infrastructure?

HHS has explicitly confirmed that covered entities and business associates may use cloud infrastructure to handle ePHI, including major providers like AWS, Azure, and Google Cloud. Three things have to be true:

1. The cloud provider signs a **business associate agreement** with you. AWS, Azure, and Google Cloud all have standard BAAs available for accounts handling PHI.
1. Only the **HIPAA-eligible services** within that provider are used for ePHI workloads. Each provider publishes a list; deviating from it is a common audit finding.
1. Your **own configuration** of those services meets Security Rule requirements: encryption, IAM, logging, network controls, key management.

The cloud provider's BAA covers the platform's security; the customer remains responsible for everything they configure on top. That maps directly onto the [shared responsibility model](/what-is/what-is-cloud-security/), and onto the configurations that [infrastructure as code](/what-is/what-is-infrastructure-as-code/) makes reviewable.

Concrete patterns that help:

* **Encrypt ePHI by default.** Customer-managed keys (KMS, Cloud KMS, Key Vault) for storage; TLS 1.2+ for transit. Encode this in Pulumi components so every new resource inherits compliant defaults.
* **Lock down access with least-privilege IAM.** Short-lived credentials, MFA, just-in-time elevation. Treat any wildcard permission as a finding.
* **Centralize secrets.** Use [Pulumi ESC](/product/esc/), AWS Secrets Manager, HashiCorp Vault, or Azure Key Vault. No plaintext secrets in code or state.
* **Enforce policy as code.** [Pulumi Policies](/docs/insights/policy/) in CI block insecure configurations (public S3, missing encryption, non-HIPAA-eligible service usage) before they merge.
* **Log everything.** CloudTrail, Activity Log, Cloud Audit Logs into a central store with retention that matches your policy. Alert on anything that looks like PHI exfiltration.
* **Audit your IaC.** Because every change is a pull request, you have a defensible record of who changed what and when. That record is exactly the artifact an OCR investigator asks for.

## Frequently asked questions about HIPAA

### Who needs to comply with HIPAA?

Two groups: covered entities (healthcare providers, health plans, healthcare clearinghouses) and business associates (vendors that handle PHI on a covered entity's behalf, such as cloud providers, SaaS tools, billing services, and IT consultants). If you create, receive, store, or transmit PHI for anyone in healthcare, HIPAA applies to you.

### What is the difference between HIPAA and HITECH?

HIPAA is the original 1996 law that created the privacy and security framework. HITECH (2009) is an amendment that strengthened it: it extended HIPAA's reach to business associates, increased penalties, mandated breach notification, and incentivized electronic health record adoption. In practice, modern HIPAA compliance includes HITECH.

### What is a business associate agreement (BAA)?

A contract between a covered entity and a vendor (or between two business associates) that specifies how the vendor will protect PHI and report breaches. Federal regulation requires a BAA before any PHI flows to the vendor. Major cloud providers publish standard BAAs for accounts that handle PHI.

### Is HIPAA compliance the same as HIPAA certification?

No. HHS does not issue HIPAA certifications. Any vendor claiming to be "HIPAA certified" is using shorthand for "we've completed a third-party assessment of HIPAA controls," most often a HITRUST CSF certification or a SOC 2 + HIPAA mapping. Real certification of compliance can only come from operating the program and surviving an audit.

### Can HIPAA-regulated data live in the public cloud?

Yes. HHS has explicitly confirmed that covered entities and business associates may use cloud infrastructure for PHI, provided the cloud provider signs a BAA, only HIPAA-eligible services are used, and the customer's own configuration meets Security Rule requirements.

### Is encryption required by HIPAA?

Encryption is classified as *addressable* by the Security Rule, meaning you must either implement it or document a justified alternative. In practice, encrypt. Properly encrypted PHI that's lost or exposed is exempt from breach notification, which is a strong incentive on top of the Security Rule itself.

### How long do you have to report a HIPAA breach?

For breaches affecting fewer than 500 individuals, the covered entity must notify each affected individual within 60 days of discovery and HHS within 60 days of the end of the calendar year. For breaches affecting 500 or more individuals, HHS and prominent media outlets must be notified within 60 days of discovery, and HHS publishes the breach to its public list.

### What are the penalties for a HIPAA violation?

Civil penalties follow a four-tier structure based on culpability, from "did not know" through "willful neglect, not corrected," with per-violation amounts and annual caps that HHS adjusts each year for inflation. Criminal violations can carry fines up to $250,000 and up to 10 years in prison. State attorneys general can also bring civil actions, and private state-law litigation often follows large breaches.

### Does HIPAA apply outside the United States?

HIPAA is US law and applies to PHI handled by US covered entities and their business associates regardless of where the data is processed. A non-US vendor handling PHI for a US healthcare provider is still a business associate and must comply. Non-US healthcare laws (GDPR's special-category data rules in the EU, PIPEDA in Canada, etc.) operate independently and may apply in addition to HIPAA.

### How does HIPAA relate to other compliance frameworks?

HIPAA is the legal floor for protecting health information in the US. Frameworks like [SOC 2](/what-is/what-is-soc-2/), ISO 27001, and [HITRUST](/what-is/what-is-hitrust/) provide structured ways to demonstrate controls that also map onto HIPAA's requirements. Many healthcare vendors maintain SOC 2 + HITRUST certifications specifically to show HIPAA readiness to customers without going through repeated bespoke audits.

## Learn more

Pulumi helps engineering teams put the controls behind HIPAA into version-controlled infrastructure: encrypted storage by default, least-privilege IAM, secrets pulled from a central vault, and [policy as code](/docs/insights/policy/) that blocks non-compliant configurations before they deploy. [Get started today](/docs/get-started/).

Related reading:

* [What is Cloud Security?](/what-is/what-is-cloud-security/)
* [What is HITRUST?](/what-is/what-is-hitrust/)
* [What is SOC 2?](/what-is/what-is-soc-2/)
* [What is Secrets Management?](/what-is/what-is-secrets-management/)
* [What is Configuration Management?](/what-is/what-is-configuration-management/)
