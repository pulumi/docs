---
title: "Multi-Region Architecture Patterns That Actually Hold"
date: 2026-09-09
draft: false
meta_desc: "Multi-region designs usually fail at the seams, not the topology. A practical guide to picking a pattern, closing dependency gaps, and testing failover as code."
authors:
    - pulumi-content-team
tags:
    - infrastructure-as-code
    - aws
    - platform-engineering
    - devops
category: general
related_posts:
    - scaling-apps-across-multiple-regions
    - replicating-data-to-support-multi-region-applications
    - deploy-to-multiple-regions

social:
    twitter: |
        Multi-region outages rarely come from the wrong topology. They come from DNS, identity, or a control plane both regions still share.

        A practical guide to picking a pattern, closing the seams, and testing failover as code.
    linkedin: |
        Teams that adopt multi-region architecture usually get the topology question right: active-active, warm standby, pilot light, backup and restore. What breaks is everything underneath the topology diagram: DNS and edge routing, identity, secrets, CI/CD, and the provider's own control plane.

        We wrote a practical guide to choosing a pattern from honest recovery targets, inventorying the dependency seams that decide whether failover actually fires, and making the whole arrangement expressible and testable in infrastructure as code.
---

Most multi-region outages are not topology failures. They are seam failures: DNS, identity, secrets, or a control plane that both regions still depend on. Pick a pattern from honest recovery targets, then inventory what still ties your regions together, then make the whole arrangement testable in code.

<!--more-->

Two recent, unrelated incidents make the point better than a hypothetical could. In October 2025, AWS's [own post-event summary](https://aws.amazon.com/message/101925/) attributed hours of US-EAST-1 disruption to "a latent defect within the [DynamoDB] service's automated DNS management system that caused endpoint resolution failures" — a single naming record, not a data center failure. In November 2025, Cloudflare's [own writeup](https://blog.cloudflare.com/18-november-2025-outage/) traced a global outage to an oversized permissions-change side effect in one feature file, propagated to every machine on the network. Neither incident was caused by losing a region. Both were caused by something shared sitting underneath the regions.

That is the argument of this post: the topology decision (active-active, warm standby, pilot light, or backup and restore) matters, but it is not where most multi-region designs actually fail. They fail at the seams that still couple the regions together, and on assumptions about failover that nobody has actually tested.

## Do you actually need multi-region, or just multi-AZ?

You need multi-region only if your recovery targets require surviving the loss of an entire AWS Region (or GCP region, or Azure region) — not a single availability zone or data center. Most production outages are narrower than that, and multi-AZ deployment already covers them.

A useful gate: in May 2026, a cooling failure inside a single AWS data center in one availability zone of US-EAST-1 caused rack-level power loss and degraded EC2 and EBS in that AZ. A well-architected multi-AZ deployment is designed to absorb exactly this: traffic and state shift to the surviving AZs in the same region automatically, with no application-level failover logic and no cross-region data replication to reason about. Multi-region solves a different, more expensive problem — losing the region itself, or losing your primary cloud provider's control plane in that region — and it is worth the added cost and operational burden only when your recovery time and recovery point objectives (RTO and RPO) genuinely require surviving that.

If a single-AZ failure would violate your RTO or RPO, fix your AZ distribution first. It is far cheaper than building multi-region, and most teams that think they need multi-region actually need this.

## Which multi-region pattern fits: active-active, warm standby, pilot light, or backup and restore?

Once you've confirmed you need multi-region, the pattern follows from your RTO and RPO, not the other way around. AWS's [Disaster Recovery](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html) framing gives this a standard vocabulary that is useful even outside AWS:

| Pattern | RTO | RPO | Steady-state cost | Operational burden | Fits when |
| --- | --- | --- | --- | --- | --- |
| Backup and restore | Hours | Minutes–hours | Lowest — no standing compute | Low day to day, high during a real event | RTO in hours is acceptable; cost sensitivity is high |
| Pilot light | Minutes–hours | Minutes | Low — core data replicated, compute scaled to near zero | Medium — must scale up and validate under pressure | You want a documented, cheap floor under a worse outage |
| Warm standby | Minutes | Seconds–minutes | Medium — a scaled-down but running secondary | Medium — the standby needs its own health checks and drills | You need fast recovery without full duplicate cost |
| Active-active | Seconds or less | Near zero | Highest — full duplicate capacity, always serving traffic | Highest — every change ships to every region, always | RTO/RPO near zero; you can afford it and can operate it |

Our earlier post on [scaling applications across multiple regions](https://www.pulumi.com/blog/scaling-apps-across-multiple-regions/) maps these onto Pulumi stack topology in more depth — two live stacks for active-active and hot standby, and a cold-standby stack that allocates no resources until a failover `pulumi up` runs it. Worth reading in full if you're deciding between stack-per-region and a single parameterized stack.

Two patterns worth naming explicitly because they rarely show up in general infrastructure-as-code writing: pilot light keeps only the data tier warm and scales compute up on demand, which is a meaningfully cheaper middle ground than warm standby for teams that can tolerate minutes, not seconds, of recovery time. And backup and restore is a legitimate architecture, not a fallback for teams that "haven't gotten to" multi-region — for a lot of workloads, it is the correct answer.

## Why multi-region designs fail: the seams, not the topology

Picking a pattern from the table above only protects the layer you deliberately replicated. Most multi-region designs still have single points of failure hiding in the layers nobody put in the diagram:

- **DNS and edge routing.** If a single DNS provider or CDN sits in front of both regions, a fault there takes down access to both regions at once, regardless of how well the backend failed over. Cloudflare's November 2025 outage affected traffic broadly, independent of which origin region a request was destined for.
- **Identity and secrets.** If your identity provider or secrets manager is single-region, or single-provider, your "failed-over" region still can't authenticate services or fetch credentials.
- **CI/CD and the container registry.** A pipeline or registry with no cross-region redundancy means your standby region can't actually deploy a fix during the outage that made you need it.
- **Observability.** If your metrics and logging pipeline lives only in the primary region, you lose visibility into the failover at the exact moment you need it most.
- **State backend.** Your infrastructure-as-code state itself needs to be reachable during a regional event, or you can't run the `pulumi up` that executes the failover.
- **The provider's control plane.** DNS, IAM, and the management APIs that provision and route to your regions are often global or single-region services layered underneath a "multi-region" deployment. Both 2025 incidents cited above were control-plane and configuration-propagation failures, not regional capacity losses.

None of these show up on an architecture diagram that only draws application tiers per region. They show up on a dependency inventory, and that inventory — not the topology chart — is what should drive your design review.

## How do you reduce provider concentration risk without a full multi-cloud rewrite?

You don't need to run every workload on every cloud to reduce concentration risk. The highest-leverage move is putting the layers that decide whether failover fires on a different failure domain than the layer that's most likely to fail.

In practice, that usually means: keep your compute and data plane on your primary cloud provider, where the majority of your platform investment already lives, but put DNS and edge routing on a second provider so a single provider's outage can't simultaneously break your application and the routing decision that would work around it. It means running your CI/CD control plane and secrets manager somewhere that stays reachable even if your primary cloud region is degraded. And it means being honest that every seam you diversify adds real complexity and real cost — this is a targeted mitigation for specific dependency seams, not a mandate to duplicate your entire stack across providers.

[Gartner's guidance on multi-cloud strategy](https://www.gartner.com/en/information-technology/glossary/multicloud-strategy) frames this as a risk-and-cost tradeoff rather than a default, which matches what shows up in practice: most teams get more resilience per dollar from fixing their dependency seams within one provider than from a full second-provider rewrite.

## How do you express these patterns in infrastructure as code?

The pattern in the table above and the seam inventory above it both need to become code, not a runbook, or the design only exists on the day you wrote it down. Pulumi's [provider](https://www.pulumi.com/docs/iac/concepts/providers/) and [component](https://www.pulumi.com/docs/iac/concepts/components/) model gives you a direct way to do that: one explicit provider per region, one component that takes a region as a parameter, and a loop that instantiates it per region from a single program.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const regions = ["us-east-1", "us-west-2"];

for (const region of regions) {
    const provider = new aws.Provider(region, { region: region as aws.Region });

    new aws.dynamodb.GlobalTable("orders", {
        attributeDefinitions: [{ name: "id", type: "S" }],
        keySchema: [{ attributeName: "id", keyType: "HASH" }],
        replicas: regions.map((r) => ({ regionName: r })),
    }, { provider });
}
```

That component is what makes the failure mode from the seams section testable: if the same component didn't get instantiated identically in every region, a unit test asserting resource parity catches it before a deploy does. [Stack references](https://www.pulumi.com/docs/iac/concepts/stacks/#stackreferences) let a per-region stack read outputs from its peers when regions need to know about each other — a DNS failover record needs the health-check ID from every region it might route to, for instance. And [Pulumi ESC](https://www.pulumi.com/docs/esc/) is the right place for per-region configuration and secrets that need to be consistent across regions rather than drifting between them one `pulumi config set` at a time.

For the data layer specifically, the primitives differ by store, and it's worth using the current form rather than an older, deprecated one:

- DynamoDB: [`aws.dynamodb.GlobalTable`](https://www.pulumi.com/registry/packages/aws/api-docs/dynamodb/globaltable/), with a `replicas` list naming every region.
- Aurora: a [`aws.rds.GlobalCluster`](https://www.pulumi.com/registry/packages/aws/api-docs/rds/globalcluster/) with regional `aws.rds.Cluster` resources attached to it.
- S3: [`aws.s3.BucketReplicationConfig`](https://www.pulumi.com/registry/packages/aws/api-docs/s3/bucketreplicationconfig/) for cross-region replication.
- DNS failover: [`aws.route53.Record`](https://www.pulumi.com/registry/packages/aws/api-docs/route53/record/) with a failover routing policy and an [`aws.route53.HealthCheck`](https://www.pulumi.com/registry/packages/aws/api-docs/route53/healthcheck/), or a [`cloudflare.DnsRecord`](https://www.pulumi.com/registry/packages/cloudflare/) if you've put edge routing on a second provider, as above.

Our earlier post on [replicating data across regions](https://www.pulumi.com/blog/replicating-data-to-support-multi-region-applications/) goes deeper on the RPO tradeoffs behind each of these choices, and a companion post covers [deploying across multiple regions](https://www.pulumi.com/blog/deploy-to-multiple-regions/) with explicit provider resource options in more detail.

## How do you know the pattern actually holds?

This is the part most multi-region write-ups skip, and it's the part that decides whether a design that looked correct in a design review actually works during a real event. A design you have not exercised is a hypothesis, not a recovery plan.

A few concrete ways to close that gap, in order of effort:

1. **Unit-test resource parity.** If your regions are instantiated from one component, as above, a unit test can assert that every region got the same set of resources with the same configuration — catching drift before it ships.
2. **Enforce replication posture with a policy pack.** Pulumi's [policy as code](https://www.pulumi.com/docs/insights/policy/policy-packs/) lets you write a `ResourceValidationPolicy` that inspects a resource's declared properties and fails a preview if, say, a DynamoDB table is missing a required replica region, or an S3 bucket has no replication configuration attached. Set the enforcement level to `mandatory` and this becomes a real gate, not a suggestion.
3. **Review stacks on every pull request.** [Review stacks](https://www.pulumi.com/docs/deployments/concepts/review-stacks/) preview the multi-region diff on every PR touching this code, so a regression in one region's configuration shows up in code review, not in an incident.
4. **Run scheduled failover drills with Automation API.** The [Automation API](https://www.pulumi.com/docs/using-pulumi/automation-api/) lets you script an actual failover — promoting the standby, redirecting DNS, validating the application responds — on a schedule, rather than only when a real outage forces the first attempt.
5. **Treat drift on the standby as a signal, not noise.** Running [`pulumi preview --diff`](https://www.pulumi.com/docs/iac/cli/commands/pulumi_preview/) against your standby or pilot-light stack on a schedule tells you when it has quietly diverged from primary — the exact condition that turns a documented pattern into a failover that doesn't actually work when you need it.

None of this requires exotic tooling. It requires treating the standby the way you already treat production: tested, monitored, and reviewed on every change, rather than provisioned once and left alone until the day it has to work.

## Where to start

1. Write down your actual RTO and RPO before picking a pattern — most teams pick a pattern and then discover, mid-incident, what recovery time it actually gave them.
2. Inventory the seams (DNS, identity, secrets, CI/CD, observability, state backend, control plane) and note which ones are still single-region or single-provider.
3. Express the pattern as a parameterized component with one explicit provider per region, so every region is provably identical.
4. Add a policy pack that enforces your replication and failover requirements as a preview-time gate, not a wiki page.
5. Schedule a real failover drill. If you haven't run one, you don't know whether your design holds — you know what it looks like on a diagram.

Multi-region architecture is a legitimate, often necessary investment. It just isn't primarily a topology problem, and treating it as one is how a design that reads well in a review turns out to have a shared DNS provider, a single-region secrets manager, or a standby stack nobody has run a preview against in months. Fix the seams, then prove the pattern holds — in a policy check and a drill, not just in a document.

Ready to put this into code? [Get started with Pulumi](https://www.pulumi.com/docs/iac/get-started/) or explore the [multi-region examples in the Pulumi Registry](https://www.pulumi.com/registry/).
