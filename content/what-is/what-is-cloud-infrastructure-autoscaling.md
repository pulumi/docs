---
title: What Is Cloud Infrastructure Autoscaling?
meta_desc: "Autoscaling adds and removes cloud capacity automatically. Learn horizontal vs vertical, reactive vs predictive, the major cloud services, and common pitfalls."

type: what-is
page_title: Autoscaling 101

customer_logos:
  title: Leading engineering organizations are building with Pulumi
  logos:
    - items:
      - snowflake
      - tableau
      - atlassian
      - fauna
      - ware2go
    - items:
      - mindbody
      - sourcegraph
      - fenergo
      - skai
      - lemonade
    - items:
      - clearsale
      - angellist
      - webflow
      - supabase
      - ro
authors: ["zack-chase"]
---

**Autoscaling is the practice of automatically adding and removing compute capacity in response to observed load, so an application has just enough resources to meet demand without paying for resources it isn't using.** A scaling policy watches one or more signals (CPU usage, request count, queue depth, custom metrics), compares them to thresholds, and triggers the cloud provider to provision more capacity when load rises or release capacity when load falls.

Autoscaling is one of the foundational features that distinguishes cloud infrastructure from fixed on-premises capacity. It's available at every layer of a modern stack: VMs, containers, Kubernetes pods, serverless concurrency, managed databases, queue consumers, even global content distribution. Most production cloud applications use autoscaling at multiple layers at once, configured through [infrastructure as code](/what-is/what-is-infrastructure-as-code/) so the policies are reviewable and reproducible across environments.

In this article, we'll cover the key questions about cloud infrastructure autoscaling:

* Why does autoscaling matter?
* What is the difference between horizontal and vertical scaling?
* What types of autoscaling are there?
* What can be autoscaled in the cloud?
* How do cloud provider autoscaling services compare?
* What are common patterns and pitfalls?
* How do you define autoscaling as code?
* Frequently asked questions about autoscaling

## Why does autoscaling matter?

Three pressures explain why autoscaling is now table stakes for any production workload:

* **Cost.** Fixed capacity sized for peak load wastes money the rest of the time. Autoscaling keeps the fleet sized to actual demand and shrinks the over-provisioning bill, which industry estimates routinely put at 30–50% of cloud compute spend.
* **Reliability.** When traffic spikes, the gap between adding capacity in minutes and adding it in days is the gap between absorbing a launch and serving 5xx errors. Autoscaling closes the gap.
* **Operations.** Without autoscaling, someone has to be on call to watch dashboards and run scale-up scripts. With it, that human is replaced by a policy that runs in seconds. The on-call rotation gets to spend its time on the things automation can't handle.

## What is the difference between horizontal and vertical scaling?

Two ways to add capacity to a workload, with very different operational characteristics.

| Aspect | Vertical scaling (scaling up) | Horizontal scaling (scaling out) |
|---|---|---|
| What changes | A single instance gets bigger (more CPU, memory, network) | More instances are added |
| Workloads that suit it | Stateful systems that are hard to distribute (RDBMS primaries, legacy monoliths) | Stateless services, web tiers, queue workers |
| Time to apply | Often requires a restart | New instances boot in parallel; no impact to existing ones |
| Upper limit | The largest instance type the cloud offers | Effectively unlimited (within quota) |
| Cost shape | Often nonlinear: a 2× instance can cost more than 2× | Roughly linear: 2× instances ≈ 2× cost |
| Common autoscaler | Less common; usually a manual or scheduled action | The dominant pattern for autoscaling |

In practice, "autoscaling" almost always means horizontal autoscaling. Vertical scaling decisions tend to be manual or change-managed because they involve a restart and a sizing analysis. A few managed serverless databases (Aurora Serverless v2, Azure SQL Database serverless) automatically scale compute capacity up and down with load. Standard RDS only autoscales storage; instance-class changes there are a manual operation.

## What types of autoscaling are there?

Three trigger styles cover most use cases, often combined in the same policy.

* **Reactive autoscaling.** Add capacity when a metric exceeds a threshold; remove it when the metric drops below another. The simplest and most common pattern. Works well for predictable, smooth load and for workloads that can absorb a short delay while new capacity boots.
* **Scheduled autoscaling.** Pre-warm capacity at known busy times (market open, business hours, a marketing campaign) and shrink at known quiet times. Cheaper than over-provisioning permanently, faster than reactive scaling, but requires that you know the schedule.
* **Predictive autoscaling.** A model forecasts load using historical data and scales out before the spike arrives. AWS, Google Cloud, and Azure all offer predictive options on top of their reactive autoscalers. Useful for workloads with daily or weekly periodicity where reactive alone responds too slowly.

Most production setups combine reactive scaling for steady-state demand with either scheduled or predictive scaling for known patterns.

## What can be autoscaled in the cloud?

Almost every cloud primitive that runs compute has an autoscaler attached to it.

| Layer | Examples |
|---|---|
| Virtual machines | AWS Auto Scaling Groups, GCP Managed Instance Groups, Azure VM Scale Sets |
| Containers | ECS Service Auto Scaling, Fargate task scaling, Cloud Run instance scaling |
| Kubernetes pods | Horizontal Pod Autoscaler (HPA), Vertical Pod Autoscaler (VPA), KEDA for event-driven scaling |
| Kubernetes nodes | Cluster Autoscaler, Karpenter (on AWS), GKE node-pool autoscaling, AKS Cluster Autoscaler |
| Serverless functions | Concurrency-based scaling (Lambda, Cloud Functions, Azure Functions) |
| Databases | Aurora Serverless, DynamoDB on-demand and provisioned with autoscaling, Azure Cosmos DB autoscale RU, Spanner autoscaler |
| Caches and queues | DynamoDB autoscaled streams, SQS queue-based scaling for consumers, ElastiCache shard scaling |
| Load balancers | Most managed load balancers scale automatically without a knob |
| CDN / edge | Effectively infinite; capacity is the network |

A real production setup typically autoscales at several layers at once: the Kubernetes HPA scales pods, the Cluster Autoscaler scales the nodes those pods need, and the database tier (often Aurora Serverless or DynamoDB on-demand) scales independently.

## How do cloud provider autoscaling services compare?

The three major clouds each ship multiple autoscaling services for different primitives.

| Cloud | VM autoscaling | Container / K8s autoscaling | Serverless concurrency |
|---|---|---|---|
| **AWS** | Auto Scaling Groups; AWS Auto Scaling spans EC2, ECS, DynamoDB, Aurora, Spot Fleet | ECS Service Auto Scaling; HPA and Cluster Autoscaler on EKS; Karpenter | Lambda concurrency (reserved, provisioned, on-demand) |
| **Google Cloud** | Managed Instance Groups (MIGs) with reactive, scheduled, and predictive autoscaling | HPA, VPA, and Cluster Autoscaler on GKE; node-pool autoscaling | Cloud Run instance scaling; Cloud Functions concurrency |
| **Azure** | VM Scale Sets with Autoscale | AKS Cluster Autoscaler; HPA; KEDA integration | Azure Functions premium/consumption plans, Container Apps scaling |

Most teams pick the autoscaler that matches their compute primitive rather than the cloud provider as a whole. Autoscaling decisions are typically a single layer's concern, not an enterprise-wide one.

## What are common patterns and pitfalls?

A handful of patterns hold up well across providers:

* **Pair the application autoscaler with the node autoscaler.** Scaling pods without scaling nodes just stalls when the cluster runs out of room. Scaling nodes without scaling pods leaves room a workload won't use. HPA + Cluster Autoscaler (or Karpenter) is the canonical pairing on Kubernetes.
* **Set sane minimum and maximum bounds.** A runaway autoscaler with no upper bound can blow a monthly budget in hours. A minimum below your steady-state floor produces cold-start latency on every quiet period.
* **Mind cold starts.** Booting a VM, pulling a container image, JIT-compiling a runtime, and warming caches all take time. Reactive scaling that responds in 5 minutes is too slow for a 30-second traffic burst. Predictive or scheduled scaling, or pre-warmed concurrency, fills the gap.
* **Pick scaling metrics that lead, not lag.** CPU works for compute-bound workloads but lags for I/O-bound ones. Queue depth, request rate, or custom application metrics (like time-in-queue) often produce smoother scaling decisions.
* **Make scale-in safe.** Terminating an instance mid-request causes failed responses. Configure connection draining, lifecycle hooks, and `terminationGracePeriodSeconds` (on Kubernetes) to let in-flight work finish before instances go away.
* **Don't autoscale stateful primaries.** Read replicas can autoscale. Primary database instances generally cannot without explicit failover logic. Use a managed serverless database (Aurora Serverless, DynamoDB, Spanner) for state that has to scale with load.
* **Test scaling on the way down too.** Most teams test scale-out; failures often happen on scale-in (a popular service holds onto state, a queue worker shuts down before draining, an LB removes a healthy backend prematurely).
* **Cap the rate of change.** Scaling 10× in 30 seconds can stress shared dependencies (databases, caches, third-party APIs) more than the original traffic spike did. Step scaling and cooldown periods smooth the changes.

## How do you define autoscaling as code?

Autoscaling policies are infrastructure: they need to be reviewed, versioned, and identical across environments. The right place to define them is in [infrastructure as code](/what-is/what-is-infrastructure-as-code/) alongside the workloads they govern.

With Pulumi:

* **AWS Auto Scaling Groups** are first-class resources in the [`@pulumi/aws`](https://www.pulumi.com/registry/packages/aws/) package. The higher-level [`@pulumi/awsx`](https://github.com/pulumi/pulumi-awsx) Crosswalk package wraps ECS service scaling, ASG defaults, and ALB target tracking in a smaller API.
* **GCP Managed Instance Groups and autoscalers** are defined through [`@pulumi/gcp`](https://www.pulumi.com/registry/packages/gcp/) with the same dependency model as the underlying VMs.
* **Azure VM Scale Sets** are defined through [`@pulumi/azure-native`](https://www.pulumi.com/registry/packages/azure-native/).
* **Kubernetes HPAs, VPAs, KEDA scaled objects, and Cluster Autoscaler / Karpenter configurations** are defined through [`@pulumi/kubernetes`](https://www.pulumi.com/registry/packages/kubernetes/) alongside the workloads they scale. See [Infrastructure as Code for Kubernetes](/what-is/infrastructure-as-code-for-kubernetes/).
* **Policy as code for scaling guardrails.** [Pulumi CrossGuard](/docs/insights/policy/) policies can enforce "every production ASG must have a non-zero max," "no ASG without scale-in protection in stateful tiers," "production database autoscaling must have an upper bound."

[Get started with Pulumi](/docs/get-started/) to define autoscaling policies alongside the rest of your cloud infrastructure in TypeScript, Python, Go, C#, Java, or YAML.

## Frequently asked questions about autoscaling

### What's the difference between scaling, autoscaling, and elastic scaling?

"Scaling" is the act of changing capacity. "Autoscaling" is scaling driven by a policy without human intervention. "Elastic" is the marketing term cloud providers use for a workload that can scale up and down automatically; in practice it means "autoscaled" plus "billed only for what you use."

### Should I scale up or scale out?

Scale out by default for any stateless service: it's cheaper, more reliable, and easier to automate. Reserve scale-up for stateful systems (primary databases, in-memory caches with affinity, single-node tools) where horizontal scaling adds prohibitive complexity.

### How do I avoid paying for capacity I'm not using?

Set a low minimum, an appropriate maximum, and use reactive autoscaling with a metric that tracks demand (CPU, queue depth, custom). For serverless workloads, on-demand pricing usually wins unless you have very predictable steady-state load, in which case reserved capacity is cheaper.

### How fast does autoscaling react?

Depends on the primitive. Lambda and Cloud Run scale in seconds. Container schedulers (ECS, HPA + Cluster Autoscaler) scale in tens of seconds to a few minutes. Adding a new EC2 instance and waiting for it to be healthy in an ASG typically takes 2–5 minutes. For faster reaction, use predictive or scheduled scaling to pre-warm capacity.

### What is predictive autoscaling?

A model that forecasts future load using historical data and scales out in advance of the predicted spike. AWS Auto Scaling, Google Cloud MIGs, and Azure Autoscale all offer it. It's most useful for workloads with daily or weekly periodicity, like a consumer app whose traffic peaks at the same time every evening.

### Can I autoscale stateful workloads?

Read replicas and stateless components of stateful systems can autoscale. Primary database instances usually cannot, because adding or removing a primary requires explicit failover logic. The newer serverless database tier (Aurora Serverless v2, DynamoDB on-demand, Azure SQL serverless, Spanner autoscaler) provides autoscaled state by handling the underlying scaling operations — failover, resharding, or compute resizing depending on the service — inside the managed service.

### What's the relationship between HPA, VPA, and Cluster Autoscaler?

In Kubernetes: HPA (Horizontal Pod Autoscaler) changes the number of pod replicas. VPA (Vertical Pod Autoscaler) changes the CPU and memory requests of pods. Cluster Autoscaler (or Karpenter) changes the number of underlying nodes. HPA + Cluster Autoscaler is the standard pairing; VPA is often used for resource-request recommendations rather than continuous resizing.

### What's KEDA?

Kubernetes Event-Driven Autoscaler. It extends HPA to scale on external metrics like queue length, Kafka consumer lag, or HTTP request rate, beyond what the built-in HPA can reach. Commonly used for queue workers, event processors, and background jobs.

### How does autoscaling interact with cost management?

Autoscaling generally reduces cost compared to fixed peak provisioning, but it can also surprise teams when an upper bound is missing. Pair autoscaling with budget alerts in your cloud account and CrossGuard policies in your IaC that enforce a maximum on every ASG / MIG / scale set / HPA.

### How does autoscaling affect SLOs?

Used well, it improves availability by absorbing load. Used poorly (no cold-start mitigation, slow reactive scaling, primary database can't keep up), it can degrade latency right when traffic spikes. SLO dashboards should track latency during scaling events specifically, not just steady state.

## Learn more

Pulumi puts autoscaling policies in the same code that creates the resources they govern: an ASG, an HPA, a Cloud Run service, a DynamoDB table, and the policies that bound them. Reviewers see the full picture in one diff; auditors see a single source of truth. [Get started today](/docs/get-started/).

Related reading:

* [What is Infrastructure as Code (IaC)?](/what-is/what-is-infrastructure-as-code/)
* [What is DevOps?](/what-is/what-is-devops/)
* [Infrastructure as Code for Kubernetes](/what-is/infrastructure-as-code-for-kubernetes/)
* [What is Serverless?](/what-is/what-is-serverless/)
* [What is Configuration Management?](/what-is/what-is-configuration-management/)
