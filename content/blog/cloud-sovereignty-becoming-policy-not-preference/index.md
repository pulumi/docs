---
title: "Cloud sovereignty is becoming policy, not preference"
date: 2026-10-22
draft: false
meta_desc: "EU proposals are turning data residency into a procurement requirement. Here is what it takes technically, and how policy as code verifies it."
authors:
    - pulumi-content-team
tags:
    - policy-as-code
    - compliance
    - governance
    - multi-cloud
    - security
category: general

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        EU proposals are moving data residency from a contract clause into procurement policy. For infrastructure teams the question becomes: can you prove where data lives, continuously?

        What residency requires technically, and how policy as code checks it.
    linkedin: |
        In May 2026, the European Commission was reported to be considering rules on where sensitive government data can be processed. In June it proposed the Cloud and AI Development Act, which includes sovereignty assurance levels for cloud services. The proposal still has to go through Parliament and Council, but the direction is clear: data residency is moving from a clause a few regulated buyers asked for into policy and procurement criteria.

        For infrastructure teams, the practical question changes from "do we have a residency statement?" to "can we show, continuously, where data actually lives?"

        Data residency has more leak paths than most diagrams show: replication, backups, audit logs, AI inference routing, and global control planes. A compliance document records intent. A policy that runs on every preview and deployment, and scans the resources already in your accounts, produces evidence.

        Our new post covers what the EU is weighing, what residency requires technically, and how policy as code and multi-region deployment enforce it.
    bluesky: |
        EU proposals are moving data residency from a contract clause into procurement policy. For infra teams, the question becomes: can you prove where data lives, continuously?

        What residency requires technically and how policy as code checks it.
---

The European Commission is weighing rules that would limit where sensitive public-sector data can be processed, and its June 2026 sovereignty package proposes tiered assurance levels for cloud services. If those proposals advance, data residency stops being a clause a few regulated buyers asked for and becomes a procurement requirement. For infrastructure teams, the question becomes whether you can show, continuously, where data actually lives.

<!--more-->

This post stays in the technical lane. It does not take a side in the policy debate. It covers what has been proposed, what data residency requires in practice, and how policy as code and multi-region deployment turn a residency statement into something you can verify.

## What is the EU actually weighing?

In May 2026, [CNBC reported](https://www.cnbc.com/2026/05/07/eu-commission-cloud-sensitive-data.html) that the European Commission was considering proposals that would restrict the use of U.S. cloud platforms for processing sensitive government data across EU countries. According to the report, the core idea is defining sectors that must be hosted on European cloud capacity. The proposals would not prohibit overseas cloud platforms from government contracts entirely. They would limit their use for sensitive data at public sector organizations, depending on the level of sensitivity. The report ties the discussion to the 2018 U.S. CLOUD Act, under which U.S. law enforcement can request data from American companies regardless of where the data is stored.

On June 3, 2026, the Commission put a formal proposal on the table as part of its European Technological Sovereignty Package, which includes a Cloud and AI Development Act. A [Jones Day summary](https://www.legal500.com/intelligence/european-union/media-telecoms-it-entertainment/eu-proposes-tech-sovereignty-package-with-major-implications-for-digital-markets) describes a single EU-wide sovereignty framework with four assurance levels for cloud services. It would require Member States to run sovereignty risk assessments, and it would require public authorities to host sensitive data on services controlled by EU entities. It also introduces "Union added-value" award criteria in public procurement. The same summary notes that the proposal now goes to the European Parliament and the Council, and that a timeline of 18 to 24 months to final adoption would not be unusual for proposals of this scope. [Tech.eu](https://tech.eu/2026/06/03/eu-says-tech-sovereignty-package-about-protecting-citizens/) reports that the package includes sovereignty requirements for cloud providers in sensitive sectors such as banking, energy, and healthcare.

Several things are still moving, and the final text may differ from the proposal. Supporters point to legal exposure and dependence on a small number of providers. Critics point to cost, capacity, and the risk of protectionism. Whichever way the text lands, buyers who write sovereignty into their requirements will need evidence.

The proposal also builds on earlier threads:

- **[GDPR Chapter V](https://eur-lex.europa.eu/eli/reg/2016/679/oj)** (Articles 44 to 49) already governs transfers of personal data to third countries. It sets conditions for transfers and does not require data to stay in the EU. The [EU-US Data Privacy Framework](https://www.legal500.com/intelligence/belgium/privacy/eu-general-court-upholds-eu%E2%80%93us-data-privacy-framework) survived a General Court challenge in September 2025.
- **The [Data Act](https://eur-lex.europa.eu/eli/reg/2023/2854/oj)** made cloud switching rules applicable in September 2025, with [switching charges prohibited from January 2027](https://cms.law/en/fra/legal-updates/eu-data-act-focus-on-cloud-services-switching-charges-who-should-shoulder-the-cost).
- **National programs** already exist. France's SecNumCloud qualification is one example, and [S3NS has received SecNumCloud 3.2 qualification](https://www.s3ns.io/en/offers/premi3ns-trusted-cloud) for its PREMI3NS offer. In Germany, [Schleswig-Holstein completed a migration of its mail system](https://www.schleswig-holstein.de/DE/landesregierung/ministerien-behoerden/I/Presse/PI/2025/cds/251006_cds_ox) in October 2025.
- **Providers have responded** with dedicated offerings. The [AWS European Sovereign Cloud](https://aws.amazon.com/blogs/aws/opening-the-aws-european-sovereign-cloud/) is generally available, described by AWS as physically and logically separate infrastructure with a first Region in Brandenburg, Germany.

## Why does sovereignty move into procurement?

A requirement in a procurement document changes how teams work. Award criteria and risk assessments need answers a reviewer can check. "Our data stays in the EU" is a claim. A list of resources, their locations, and the policy that blocks anything outside the approved set is evidence.

That shifts the burden onto the people who run infrastructure. Questions that used to arrive once a year in a security questionnaire arrive as a standing requirement: where is this data stored, where is it processed, who holds the keys, and how do you know none of that changed last Tuesday?

## What does data residency require technically?

Three terms get used interchangeably, and they should be kept apart:

- **Data residency** is where data is stored and processed physically.
- **Data sovereignty** is which jurisdiction's law applies to the data and to the company that holds it.
- **Operational control** is who can administer the systems and who holds the encryption keys.

Residency is the part infrastructure code can check most directly, so it is the usual starting point. It is also harder than picking an EU region. Data moves through paths that a region diagram does not show:

| Leak path | What can happen | Reference |
| --- | --- | --- |
| Replication | Objects replicate to a bucket in another Region | [S3 replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) |
| Backups | Backup copies are written to a vault in another Region | [AWS Backup cross-Region copy](https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-region-backup.html) |
| Audit logs | Multi-Region trails deliver log files from several Regions to one place | [CloudTrail multi-Region trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) |
| AI inference | Requests can be routed to another Region | [Bedrock cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html), [Azure deployment types](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types) |
| Geo-redundant storage | A secondary copy lives in a paired Region | [Azure storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy) |
| Global services | Some services are global and not tied to one Region | [AWS service endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) |

Each of these is a setting on a resource, a default on a service, or a feature someone turns on later. A residency design has to cover all of them, and it has to keep covering them as teams add resources.

Key management belongs on the same list. Where encryption keys live and who can use them affects the operational control question. The major clouds offer ways to keep keys outside the provider's own key service, including the [AWS KMS external key store](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html), [Azure Managed HSM](https://learn.microsoft.com/en-us/azure/key-vault/managed-hsm/overview), and [Google Cloud EKM](https://cloud.google.com/kms/docs/ekm).

## Why is a compliance document not enough?

A document records intent at a point in time. Infrastructure changes daily. Someone enables replication to fix a latency problem, a new service ships with a global default, or an engineer creates a bucket in the console during an incident. None of those events updates the document.

Each cloud has native guardrails for part of this problem: [AWS Control Tower Region deny](https://docs.aws.amazon.com/controltower/latest/userguide/region-deny.html) uses service control policies, Azure Policy has an [Allowed locations](https://learn.microsoft.com/en-us/azure/governance/policy/samples/built-in-policies) built-in, and Google Cloud has the [resource locations organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). These are worth using. They also differ by provider, so a team running more than one cloud ends up maintaining several rule sets with different semantics and no single record of what passed.

## How does policy as code turn residency into a check?

Policy as code moves the rule out of the document and into the path every change takes. With [Pulumi Policies](/product/discovery-governance/), you write policies in TypeScript, JavaScript, Python, or OPA (Rego). Per the [policy as code documentation](/docs/discovery-governance/concepts/policy-as-code/), policies evaluate during `pulumi preview` and `pulumi up` before anything changes in your cloud provider, and a violation of a mandatory policy stops the deployment.

Here is a policy that requires Cloud Storage buckets to live in an approved set of European locations:

```typescript
import * as gcp from "@pulumi/gcp";
import { PolicyPack, validateResourceOfType } from "@pulumi/policy";

const allowedLocations = new Set(["EU", "EUROPE-WEST1", "EUROPE-WEST3", "EUROPE-WEST4"]);

new PolicyPack("data-residency", {
    policies: [{
        name: "storage-in-approved-locations",
        description: "Cloud Storage buckets must live in approved EU locations.",
        enforcementLevel: "mandatory",
        validateResource: validateResourceOfType(gcp.storage.Bucket, (bucket, args, reportViolation) => {
            const location = (bucket.location ?? "").toUpperCase();
            if (!allowedLocations.has(location)) {
                reportViolation(`Bucket location "${bucket.location}" is outside the approved set.`);
            }
        }),
    }],
});
```

Run it against a program with `pulumi preview --policy-pack ./data-residency`. A bucket in `US-CENTRAL1` fails the preview with the message above, before the bucket exists. The same shape works for databases, queues, replication configurations, backup vaults, and any other resource type in the table above. Writing one policy per leak path gives you a checklist that runs on every change.

Enforcement levels support a gradual rollout. Policies can be advisory, mandatory, remediate, or disabled, so a team can start in advisory mode, see what would have failed, and move to mandatory once the existing estate is clean. Pre-built packs cover frameworks such as CIS, HITRUST, ISO 27001, NIST, PCI DSS, and CMMC, and policy groups apply packs to specific stacks or cloud accounts. That maps well to residency, where a regulated workload may carry a stricter rule than the rest of the estate. See [policy groups](/docs/discovery-governance/concepts/policy-as-code/policy-groups/) and the guide to [writing a policy pack](/docs/discovery-governance/guides/write-a-policy-pack/).

Preventative checks only see what goes through your pipeline. Resources created some other way need a second mechanism. According to the [Discovery documentation](/docs/discovery-governance/concepts/discovery/), Discovery scans your cloud accounts on a schedule and finds every resource in them, whether it was created with Pulumi, CloudFormation, Terraform, or the cloud console. Audit policy groups evaluate those discovered resources and report violations without blocking anything. The first mechanism stops new violations. The second finds the ones that already exist. Together they produce the thing a procurement reviewer asks for: a current inventory with locations and a record of what was checked. For more on that pattern, see [enforcing policy as code on discovered resources](/blog/enforcing-policy-as-code-on-discovered-resources-with-pulumi/). Teams with accounts in sovereign partitions can also read about [scanning every AWS partition with Pulumi Discovery](/blog/scan-aws-govcloud-china-with-pulumi-insights/).

Layer this with the native controls from the previous section. Region deny and organization policies block at the provider's API. Pulumi policies block earlier, in the preview, with an error message written for the person who made the change.

## How do multi-region and multi-provider deployment help?

Policy tells you what is allowed. Deployment architecture decides how cheaply you can comply. When the infrastructure is one program, a jurisdiction becomes a stack with its own configuration:

- **One program, one stack per jurisdiction.** The region, provider, and approved key service come from stack configuration, so adding a jurisdiction means adding a stack and not forking code.
- **Components for the pattern.** A reusable component for "storage with approved location, backups in the same jurisdiction, and keys in an approved store" gives every team the compliant version by default. See the earlier post on [deploying to multiple regions](/blog/deploy-to-multiple-regions/).
- **Portability as a procurement answer.** The Data Act's switching rules push toward being able to move. Infrastructure defined in general-purpose languages and kept in version control is easier to move than infrastructure that exists only as console state. A recent panel recap on [what actually protects you beyond the hyperscalers](/blog/beyond-the-hyperscalers-what-actually-protects-you/) covers the architecture side of that conversation.
- **Control of the tooling itself.** Some buyers want the management plane inside their own boundary too. Pulumi Cloud offers a [self-hosting option](/docs/administration/self-hosting/) for those cases.

## Where should you start?

You do not need to wait for the final text of any regulation to make progress. These steps are useful under almost any outcome:

1. **Inventory what you have.** Run discovery across every cloud account and list resources by location. Expect surprises.
1. **Classify the data.** Decide which workloads hold data that could fall under a sensitive category, and which locations are approved for each.
1. **Write the location policy in advisory mode.** One policy per resource type that stores or processes data. Read the violations before you enforce anything.
1. **Cover the leak paths.** Add policies for replication, backup copies, log destinations, AI inference configuration, and geo-redundant storage.
1. **Decide on keys.** Pick where encryption keys live and who can use them, and write a policy that requires it.
1. **Move to mandatory and keep the evidence.** Switch enforcement on, keep preview results and scan reports, and make them available to the people who answer procurement questionnaires.

## What should you do this quarter?

Pick one data-bearing workload and run steps one through four against it. The exercise takes days, produces a real list of gaps, and gives you a worked example to hand to the next team. If the proposed rules advance, the buyers who ask you for evidence will want an answer that comes from a system and not from a slide. If they change, you still have a cleaner estate and a faster way to answer the next audit.

To try the policy above, follow the [write a policy pack guide](/docs/discovery-governance/guides/write-a-policy-pack/) and point it at a test project.
