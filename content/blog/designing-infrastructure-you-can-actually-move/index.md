---
title: "Designing Infrastructure You Can Actually Move"
date: 2026-10-08T06:00:00-07:00
meta_desc: "Railway's May 2026 outage began when Google Cloud suspended its account. What it takes to make infrastructure movable, and where portability stops."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - multi-cloud
    - google-cloud
    - platform-engineering
    - infrastructure-as-code
    - migration
category: perspectives
schema_type: auto
social:
    twitter: |
        Google Cloud suspended Railway's production account on May 19. Access came back in 9 minutes. Full recovery took about 8 hours.

        What makes infrastructure movable, and what portability can't do for you:
    linkedin: |
        On May 19, 2026, Google Cloud placed Railway's production account in suspended status. Railway had a P0 ticket open within two minutes and account access back in nine, yet customers were affected for about eight hours.

        We wrote up what the incident shows about single-account risk, why moving clouds is hard, what lowers the cost of a forced move, and what a portable Pulumi program does and does not give you.
    bluesky: |
        Google Cloud suspended Railway's production account on May 19. Access was back in 9 minutes, but full recovery took about 8 hours. A look at single-account risk and what makes infrastructure movable.
---

On the evening of May 19, 2026, Google Cloud placed Railway's production account in suspended status. Railway had a top-priority ticket open within two minutes and had account access back within nine. Customers were still affected for roughly eight hours, because getting an account back is a different thing from getting a running platform back.

<!--more-->

Most of us have a disaster recovery plan for a failed zone or a failed region. Far fewer have one for the account itself disappearing. This post walks through what happened at Railway, the general shape of the risk, why moving between clouds is hard, and which engineering choices make a forced move cheaper. It also says plainly what no tool can do for you.

## What happened at Railway

Railway published a [detailed postmortem](https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage). At about 22:20 UTC, Google Cloud suspended Railway's production account. Railway says the suspension was incorrect. A [Register report](https://www.theregister.com/off-prem/2026/05/20/google-cloud-suspended-major-customer-railwaycom-without-cause-causing-outage/5243111) described it as coming out of the blue for a customer that spends an eight-figure sum a year on the platform.

Access to the account was restored at 22:29 UTC. Restoring the account did not restore the services inside it. Compute had stopped, disks were inaccessible, and networking was down. Disks were ready again at 23:54 UTC, and networking and edge routing returned in the early hours of May 20.

The most instructive detail is that Railway had already done a lot of the hard work. It had moved much of its infrastructure onto its own hardware and onto AWS, and those workloads kept running at first. But the edge proxies fetched their routes from a control-plane API hosted on Google Cloud. When the cached routes began expiring about fifteen minutes in, the proxies started returning 404s, and over the following hours workloads in every region became unreachable. The dashboard, API, login, and databases went down with them.

Railway's response was to remove the dependency: make the network a true mesh with no Google Cloud component in the hot path, and spread database shards across AWS and its own metal. The postmortem closes with "we ultimately own this one." That is a candid thing to publish, and the lesson in it applies to every team that runs on a hyperscaler, which is nearly everyone.

## Any single cloud can switch you off

The [Hacker News discussion](https://news.ycombinator.com/item?id=48201484) of the incident centered on two points: the suspension arrived without any outreach, and it appeared to be automated. Those complaints describe a structural property of buying infrastructure from anyone, and the same questions apply to any provider.

Cloud providers' terms generally let them suspend an account, for reasons such as automated fraud and abuse detection, billing problems, policy flags, legal orders, and operator error. Railway describes its own case as an incorrect suspension. In May 2024, [Google's own review of the UniSuper incident](https://cloud.google.com/blog/products/infrastructure/details-of-google-cloud-gcve-incident) described a customer's private cloud subscription being deleted because of a blank parameter during provisioning, and UniSuper was down for about a week. [SSLMate's founder reported](https://www.theregister.com/off-prem/2025/11/04/google-cloud-suspended-customers-account-three-times/270791) that Google suspended his account three times and concluded that he could not rely on having a Google account for production use.

These events are rare, and each has a different cause. What they share is the blast radius. The account sits above regions and availability zones in the hierarchy, so multi-zone and multi-region designs inside that account give no protection. You can build a flawless high-availability setup and still lose all of it at once, because one decision outside your control applies to the whole account.

## Moving is hard, and here is why

Writing "go multi-cloud" in a postmortem review takes one line. Doing it takes a different order of effort, and the people in that Hacker News thread were right to argue about cost and availability.

- **Data has gravity.** Terabytes do not move quickly, egress fees apply, and a live database needs replication and a cutover window. Moving data is usually the slowest and riskiest part of any migration.
- **Managed services differ.** Pub/Sub, SNS, and SQS overlap but are not interchangeable. IAM models differ in their fundamentals. Cloud Run and ECS make different assumptions about networking, scaling, and deployment. BigQuery has no drop-in equivalent.
- **The surrounding systems are entangled.** DNS, certificates, identity providers, secrets, CI credentials, and monitoring all reference the provider you are leaving.
- **People and runbooks are tied to a cloud.** Your on-call engineers know one console and one set of failure modes.

No tool makes this painless, and any tool that claims to should be treated with suspicion. The honest goal is more modest: reduce the number of surprises and the amount of manual work when you have to move, and know your dependencies before an incident reveals them.

## What lowers the cost of a forced move

Teams that recover from a forced move quickly tend to share a few habits, and most of them concern how the infrastructure is defined.

**Everything is in code you can read.** If your infrastructure was built in a console or with one-off scripts, the first step of any migration is archaeology. If it lives in a real programming language, the inventory exists and can be searched. Railway's hidden dependency, a control plane the data plane quietly relied on, is the kind of thing a review of the full dependency graph can surface before an incident does. Resources created by hand can be brought under management with [`pulumi import`](/docs/iac/guides/migration/import/), which is a worthwhile first project on its own.

**Provider-specific code lives behind a seam.** When application teams call a function like `webService(...)` and only one module knows which cloud answers, a second implementation becomes a contained project. A general-purpose language makes this seam natural, with interfaces, functions, and packages. The [comparison of Pulumi and Terraform](/docs/iac/comparisons/terraform/) covers how that kind of abstraction differs from what HCL offers.

**Configuration is separate from logic.** Per-stack [configuration](/docs/iac/concepts/config/) lets the same program run with different settings in different [stacks](/docs/iac/concepts/stacks/), so a second environment is a config file and not a fork.

**The second path is tested.** A seam you have never run behind is a hypothesis. Standing up the alternative in a throwaway stack tells you what it really needs.

## What a portable Pulumi program looks like

Here is a small TypeScript program. It defines a `WebService` contract, two implementations (Cloud Run on Google Cloud and Fargate on AWS), and a single function that picks one from stack configuration. Each implementation is a [component](/docs/iac/concepts/components/), so callers see one resource and its outputs.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";
import * as awsx from "@pulumi/awsx";

export interface WebServiceArgs {
    image: string;
    port: number;
    env: Record<string, pulumi.Input<string>>;
}

export interface WebService {
    url: pulumi.Output<string>;
}

class CloudRunService extends pulumi.ComponentResource implements WebService {
    public readonly url: pulumi.Output<string>;

    constructor(name: string, args: WebServiceArgs, opts?: pulumi.ComponentResourceOptions) {
        super("example:platform:CloudRunService", name, {}, opts);
        const svc = new gcp.cloudrunv2.Service(name, {
            location: "us-central1",
            template: {
                containers: [{
                    image: args.image,
                    ports: { containerPort: args.port },
                    envs: Object.entries(args.env).map(([k, v]) => ({ name: k, value: v })),
                }],
            },
        }, { parent: this });
        new gcp.cloudrunv2.ServiceIamMember(`${name}-public`, {
            name: svc.name,
            location: svc.location,
            role: "roles/run.invoker",
            member: "allUsers",
        }, { parent: this });
        this.url = svc.uri;
        this.registerOutputs({ url: this.url });
    }
}

class FargateService extends pulumi.ComponentResource implements WebService {
    public readonly url: pulumi.Output<string>;

    constructor(name: string, args: WebServiceArgs, opts?: pulumi.ComponentResourceOptions) {
        super("example:platform:FargateService", name, {}, opts);
        const lb = new awsx.lb.ApplicationLoadBalancer(name, {}, { parent: this });
        new awsx.ecs.FargateService(name, {
            assignPublicIp: true,
            taskDefinitionArgs: {
                container: {
                    name,
                    image: args.image,
                    cpu: 256,
                    memory: 512,
                    essential: true,
                    portMappings: [{ containerPort: args.port, targetGroup: lb.defaultTargetGroup }],
                    environment: Object.entries(args.env).map(([k, v]) => ({ name: k, value: v })),
                },
            },
        }, { parent: this });
        this.url = pulumi.interpolate`http://${lb.loadBalancer.dnsName}`;
        this.registerOutputs({ url: this.url });
    }
}

// The only place that knows which cloud is in use.
export function webService(name: string, args: WebServiceArgs): WebService {
    const cloud = new pulumi.Config().require("cloud");
    switch (cloud) {
        case "gcp": return new CloudRunService(name, args);
        case "aws": return new FargateService(name, args);
        default: throw new Error(`Unsupported cloud: ${cloud}`);
    }
}

const api = webService("api", {
    image: "registry.example.com/api:1.4.2",
    port: 8080,
    env: { LOG_LEVEL: "info" },
});

export const apiUrl = api.url;
```

Running `pulumi config set cloud gcp` in one stack and `pulumi config set cloud aws` in another gives two environments from one program. The caller at the bottom does not change.

What carries over is the contract, the call site, and the configuration. What does not carry over is the work inside each implementation. Both classes are provider-specific code that you write, test, and maintain. The example also leaves out the hard parts: it has no database, no queue, no DNS, and no TLS. Adding those means choosing equivalent services on each side and deciding how far the seam can honestly go. Some services will not fit behind an interface without hiding differences that matter.

## What portability buys you, and what it does not

| Portability gives you | Portability does not give you |
| --- | --- |
| A complete, searchable inventory of what you run | Your data on the other side |
| A second implementation you can stand up and rehearse in a non-production stack | Equivalent behavior from different managed services |
| A smaller set of unknowns when a move is forced | Relief from egress costs |
| A way to find single-account dependencies, such as a control plane, before an incident does | A replacement for a tested failover plan |

A rehearsed plan beats an improvised one, and that is the realistic claim. A forced move will still be a hard week. The goal is to make it a hard week with a map.

## Where to start this quarter

You do not need a full multi-cloud architecture to reduce this risk. These steps are each worth doing alone:

1. **Put everything in code, including the control plane.** DNS, identity, secrets, and the services that decide where traffic goes are the usual blind spots.
2. **Trace your hot path for single-account dependencies.** Ask what stops working within minutes if your cloud account becomes unreachable. Railway's cached routes lasted about fifteen minutes.
3. **Write the seam for one service.** Pick a stateless service and put its provider-specific code behind an interface.
4. **Stand up the second implementation once, in a throwaway stack.** Note what surprised you, then tear it down.
5. **Keep backups of your data outside the provider's account.** If the account is suspended, backups inside it are suspended too.
6. **Know your escalation path.** Find out who you would contact at your provider, how long that takes, and what support tier you have. In the Register's account, Google's support took about an hour to engage.

For a broader discussion of how engineers who have priced leaving a hyperscaler think about this, see our recorded panel, [Beyond the Hyperscalers: What Actually Protects You](/blog/beyond-the-hyperscalers-what-actually-protects-you/).

Railway's postmortem is worth reading in full, and the practical takeaway from it applies to everyone: the dependency that hurts you is often the one you stopped noticing. Making your infrastructure readable, searchable, and rehearsed will not prevent a suspension, but it changes how much you have to figure out while the clock is running.
