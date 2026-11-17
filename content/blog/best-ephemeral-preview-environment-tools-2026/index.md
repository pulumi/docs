---
title: "Best Ephemeral Preview Environment Tools in 2026"
date: 2026-11-17
draft: false
meta_desc: "Seven ephemeral environments tools compared for 2026: Pulumi, Northflank, Render, Okteto, Signadot, Bunnyshell, and Argo CD for per-PR preview environments."
authors:
    - pulumi-content-team
tags:
    - devops
    - ci-cd
    - platform-engineering
    - kubernetes
    - infrastructure-as-code
category: general
faq_schema: true
itemlist_name: "Ephemeral Preview Environment Tools"
itemlist:
    - name: "Pulumi"
      url: "https://www.pulumi.com/"
    - name: "Northflank"
      url: "https://northflank.com/"
    - name: "Render"
      url: "https://render.com/"
    - name: "Okteto"
      url: "https://www.okteto.com/"
    - name: "Signadot"
      url: "https://www.signadot.com/"
    - name: "Bunnyshell"
      url: "https://www.bunnyshell.com/"
    - name: "Argo CD ApplicationSet"
      url: "https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Pull-Request/"

related_posts:
    - building-kubernetes-pr-previews-with-shared-pulumi-components
    - eks-vcluster-ephemeral-environments-with-pulumi

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        "Preview environments" can mean a frontend URL, a full-stack copy, or a request-routed sandbox on a shared cluster.

        We compared seven ways to get one per pull request: Pulumi, Northflank, Render, Okteto, Signadot, Bunnyshell, and Argo CD.
    linkedin: |
        Ask teams what a preview environment is and you get three common answers: a frontend URL, a full-stack copy with its own database, or a sandbox that shares a cluster with everyone else.

        The right tool depends on which one you need, where it has to run, and who owns the cleanup when a pull request closes.

        We compared seven options on spin-up, teardown and cost hygiene, config-as-code, where they run, and CI/CD fit: Pulumi, Northflank, Render, Okteto, Signadot, Bunnyshell, and the Argo CD ApplicationSet pull request generator.

        No vendor in the list publishes a measured spin-up time, and the post says so.
    bluesky: |
        Ephemeral environments range from a frontend preview URL to a full-stack copy per pull request to a sandbox on a shared cluster.

        We compared seven tools on teardown, config-as-code, where they run, and cost control, and flagged what vendors don't publish.
---

An ephemeral preview environment is a short-lived, isolated copy of your application (and often its infrastructure) created automatically when a pull request opens and destroyed when it merges or closes. It lets reviewers and tests exercise a change before it reaches staging. This post compares seven ways to run ephemeral environments in 2026.

<!--more-->

Some tools give you a URL for a frontend build. Some clone a whole production stack, database included. One routes requests to a changed service on a shared cluster so nothing else is duplicated.

## How we evaluated these tools

Every tool below was checked against its own documentation and pricing page in November 2026, and each claim links to its source. We scored them on five criteria:

1. **Spin-up time.** How quickly a pull request gets a working environment. No vendor in this list publishes a measured figure, so we describe the mechanism and say where the number is missing.
2. **Teardown and cost hygiene.** Whether environments are destroyed on merge or close, and whether TTLs, idle shutdown, or caps exist for the ones people forget.
3. **Config as code or UI.** Whether the environment definition lives in your repo and goes through review.
4. **Where it runs.** The vendor's cloud, your cloud account, or your Kubernetes cluster.
5. **CI/CD and Git integration.** Which Git hosts and pipelines trigger it.

Where a vendor page does not state something, we write "not documented" and name the date. A few details come from a vendor's own blog or home page rather than its docs; those are linked as such.

## How the tools compare

| Tool | Approach | Config | Where it runs | Best-fit team | Pricing model |
|---|---|---|---|---|---|
| Pulumi | Stack per PR through Review Stacks or the Automation API | Real languages, `Pulumi.pr.yaml` | Any cloud, 180+ providers | Teams that want preview infrastructure defined in code | Free (1 user); Essentials $40/mo, Pro $400/mo, plus usage and your cloud bill |
| Northflank | Template of services, databases, and jobs per PR | UI or Northflank templates | Northflank cloud or your cloud (BYOC) | Small to large teams wanting a PaaS with databases per PR | Free tier; usage-based from $0.01667/vCPU-hour |
| Render | Copy of the production Blueprint per PR | `render.yaml` | Render cloud | Teams already on Render | Pro $25/mo plus compute |
| Okteto | Kubernetes namespace per PR | `okteto.yml` | Your cluster | Kubernetes teams of any size | Free to 5 users; paid tiers per user |
| Signadot | Sandboxes on a shared baseline | Sandbox spec YAML | Your cluster (hosted control plane) | Microservice teams with a stable staging baseline | Free 50 sandboxes/mo; Business $250/mo |
| Bunnyshell | Namespace per environment | `bunnyshell.yaml` | Your cluster | Teams with Compose, Helm, or Terraform stacks | $0.007/min per active environment |
| Argo CD PR generator | One Application per open PR | ApplicationSet YAML | Your cluster | Platform teams already running Argo CD | No license cost |

## Pulumi: preview infrastructure defined in your own language

Pulumi treats a preview environment as a stack: a separate, parameterized instance of your infrastructure program. That covers the compute that runs your app and the cloud resources around it: networks, databases, queues, buckets, and DNS.

Pulumi offers two routes to one stack per pull request:

- **Review Stacks.** With Pulumi Deployments, [Review Stacks](/docs/deployments/concepts/review-stacks/) create an environment when a pull request opens, update it on each commit, and destroy it when the PR merges or closes. They work with GitHub, GitLab, Azure DevOps, and Bitbucket. You name a `pr` stack, add a `Pulumi.pr.yaml`, set `pullRequestTemplate: true` in Deployment Settings, and the stack outputs appear as a PR comment.
- **Automation API.** If you would rather drive things from your own CI, the [Automation API](/docs/iac/concepts/automation-api/) wraps `pulumi up`, `preview`, `destroy`, and `stack init` in a typed SDK, so a pipeline step can create and delete a per-PR stack. It is available on every edition.

Per-environment configuration goes through [Pulumi ESC](/docs/esc/concepts/environments/), which composes shared and per-environment values and supports [short-lived cloud credentials through OIDC](/docs/esc/providers/login/aws-login/). [TTL stacks](/docs/deployments/concepts/ttl/) destroy a stack after a set time, which helps when a PR sits open for weeks. TTL stacks are on the Pro and Enterprise editions. See the [TTL announcement](/blog/ttl/) for the design.

Pulumi pairs well with a Kubernetes cluster, too. Two worked examples on this blog: [per-PR Kubernetes previews from a shared component](/blog/building-kubernetes-pr-previews-with-shared-pulumi-components/) and an [EKS and vCluster environment factory](/blog/eks-vcluster-ephemeral-environments-with-pulumi/).

**Strengths:** any cloud and any resource a [provider](/registry/) supports; the definition is ordinary code with loops, functions, and tests; the same program deploys dev, PR, and production. **Trade-offs:** Pulumi provisions infrastructure, so you bring the app build and runtime (containers, a cluster, or a PaaS). Review Stacks run through Pulumi Cloud Deployments and need Deployment Settings configured, so they depend on Pulumi Cloud the way Northflank previews depend on its control plane. There is no built-in request-routing sandbox like Signadot's. Spin-up time depends on your stack and is not published. **Pricing:** Free is $0 for one user and includes 500 workflow minutes per month; Essentials is $40/month and Pro is $400/month, with Enterprise custom. Managed resources and workflow minutes ($0.01 each) draw from the edition's credits, so per-PR stacks add Pulumi usage on top of your cloud bill. Details are in the [edition guide](/docs/administration/get-started/choose-edition/).

**Best for:** teams whose previews need real cloud infrastructure (databases, queues, IAM) that must match production, and who want that defined in the same language as the app.

## Northflank: a PaaS template that includes databases

Northflank describes a preview environment template that bundles services, managed databases, jobs, and secrets, then instantiates it from a pull request, the CLI, or the API. Its [preview environments page](https://northflank.com/product/preview-environments) says you can manage them through the UI or IaC templates.

Idle and duration policies are part of the offer: per Northflank's [own roundup](https://northflank.com/blog/tools-for-ephemeral-environments), templates can set teardown after a duration, idle shutdown, and active-hours limits. It runs on Northflank's cloud or in your own account on AWS, GCP, Azure, Civo, CoreWeave, Oracle Cloud, or on-prem (bring your own cloud).

**Strengths:** databases and jobs live in the template, so a preview can run integration tests; many cloud targets; usage-based pricing with unlimited users. **Trade-offs:** the template format is Northflank-specific, so previews depend on its control plane. Its feature claims here come from Northflank's product page and its own roundup blog. Spin-up time is not documented on the pages we checked as of November 2026. **Pricing:** a free tier, then [pay as you go](https://northflank.com/pricing) from $0.01667 per vCPU-hour and $0.00833 per GB-hour of memory.

**Best for:** teams that want full-stack previews, databases included, without running Kubernetes themselves.

## Render: one Blueprint covers production and previews

Render creates a fresh copy of your Blueprint (services, datastores, environment groups) per pull request, per its [preview environments docs](https://render.com/docs/preview-environments). A `previews.generation` setting in `render.yaml` chooses automatic creation or manual creation by adding `[render preview]` to the PR title. Previews are destroyed on merge or close, and `previews.expireAfterDays` removes ones with no recent commits. Datastore copies start empty unless you seed them.

**Strengths:** one file serves production and previews; per-preview plan overrides keep compute small; a flat workspace fee with unlimited seats. **Trade-offs:** it runs only on Render's cloud; full-stack previews need the Pro plan or higher (Hobby has single-service previews); each preview's compute is billed on top; GitLab merge requests do not get status updates per the same docs. Spin-up time is not documented as of November 2026. **Pricing:** per the [pricing page](https://render.com/pricing), Hobby is $0 plus compute with single-service previews, and Pro is $25/month plus compute with full-stack previews.

**Best for:** small to mid-size teams already on Render, or teams without Kubernetes who want full-stack previews with little setup.

## Okteto: a namespace per PR inside your own cluster

Okteto runs in your Kubernetes cluster. A GitHub Actions or GitLab CI job deploys the app into a [preview environment](https://www.okteto.com/docs/previews/) using the `deploy` section of the Okteto Manifest (`okteto.yml`), which can reference Docker Compose files. The pipeline destroys the preview when the PR closes on GitHub or the branch is deleted on GitLab. The home page says idle environments sleep and unused ones are deleted, while the pricing page puts garbage collection and cost controls on Scale and Enterprise.

**Strengths:** config lives in the repo; self-hosted on every tier; priced per user; a free tier. **Trade-offs:** you operate Okteto in your cluster; Bitbucket Pipelines and Azure DevOps are listed as "coming soon" in the docs; garbage collection and cost controls are on paid tiers; Scale and Enterprise pricing is on request. Spin-up time is not documented as of November 2026. **Pricing:** per the [pricing page](https://www.okteto.com/pricing/), the free tier covers up to 5 users and 500 environments per month.

**Best for:** engineering teams already on Kubernetes that want previews and development environments from one tool.

## Signadot: sandboxes on a shared baseline

Signadot duplicates only the services a pull request changes and routes requests carrying a routing key to them, while everything else is shared from a baseline environment. The vendor says an environment ["starts in seconds"](https://www.signadot.com/) and lets hundreds share one cluster, but publishes no benchmark.

You define a sandbox in YAML with a TTL field, and the GitHub App [deletes the sandbox when the PR closes](https://www.signadot.com/docs/guides/integrate-ci/github). It runs in your cluster and needs request routing through Istio or the Signadot sidecar.

**Strengths:** per Signadot, an environment costs a fraction of a full copy; many concurrent PRs fit on one cluster; billing counts sandboxes created, and uptime is not metered. **Trade-offs:** isolation is at the request level, so schema changes and stateful components need resource plugins; you maintain a baseline environment; Kubernetes only. **Pricing:** per the [pricing page](https://www.signadot.com/pricing), Starter is free with 50 sandboxes a month and Business is $250/month for 100.

**Best for:** microservice teams on Kubernetes with a stable shared staging baseline, where copying the full stack per PR would be slow or expensive.

## Bunnyshell: Compose, Helm, and Terraform definitions on your cluster

Bunnyshell creates a Kubernetes namespace per environment from a `bunnyshell.yaml` that can wrap Docker Compose, Helm, Terraform, or raw manifests. Environments are created on PR open and [destroyed on merge or close](https://www.bunnyshell.com/ephemeral-environments/); the UI and PR-comment commands are also available. It connects to your own cluster on EKS, AKS, or GKE.

**Strengths:** accepts several definition formats; per-minute billing tracks uptime; data stays in your infrastructure. **Trade-offs:** you need a Kubernetes cluster; no free tier, only a 14-day trial; the home page says "in seconds" while the ephemeral environments page says "in minutes", with no benchmark. **Pricing:** per the [pricing page](https://www.bunnyshell.com/pricing/), $0.007 per minute per active environment. As arithmetic, one environment left running for 30 days costs about $302, so stopping idle environments matters.

**Best for:** teams with existing Compose, Helm, or Terraform definitions and a Kubernetes cluster who want a managed layer on top.

## Argo CD ApplicationSet: the open source DIY route

The [Pull Request generator](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Pull-Request/) in Argo CD's ApplicationSet controller polls your Git host and creates one Argo CD Application per open PR, typically deploying into a namespace you template per PR. The Application is removed when the PR no longer matches (closed, or the filter label removed). It supports GitHub, GitLab, Gitea, Bitbucket Server, Bitbucket Cloud, and Azure DevOps.

**Strengths:** no license cost and no extra vendor; fits GitOps shops that already run Argo CD. **Trade-offs:** you build everything else: image builds, databases, DNS and ingress per PR, PR comments with URLs, data seeding, and cost controls. Polling defaults to every 30 minutes unless you configure a webhook. The generator has no idle sleep, so you add that yourself. Spin-up time depends on your manifests and sync. The docs also note that only admins should create ApplicationSets with PR generators.

**Best for:** platform teams with Argo CD in production who want per-PR namespaces and are happy to own the surrounding glue.

## Also considered

- **Vercel and Netlify.** Both create a [preview deployment per push or PR](https://vercel.com/docs/deployments/environments) for frontends and functions, and Netlify's Free plan lists [unlimited deploy previews](https://www.netlify.com/pricing/). Backend services, databases, and queues are outside that scope, so full-stack teams pair them with another tool.
- **Qovery.** Namespace-per-PR on your cloud accounts or Kubernetes cluster, with preview environments on every tier including [Free](https://www.qovery.com/pricing), then plans from $299/month.
- **Railway.** PR environments are [created on open and deleted on merge or close](https://docs.railway.com/guides/environments) on Railway's cloud.
- **Shipyard.** Now part of StackGen, per its site banner.
- **Release.** Markets ephemeral preview environments in your own cloud; its pricing is not public as of November 2026, so we left it out of the comparison.
- **Uffizzi.** The open source repository's last push was in August 2024, so we did not include it.

## How is an ephemeral preview environment different from a staging environment?

A staging environment is long-lived and shared: every change queues through it, and it holds whatever state the last tester left. An ephemeral preview environment is created per pull request, isolated from other changes, and deleted when the PR closes. Staging covers the integrated build and previews cover a single change, so many teams keep both.

## How to choose

1. **Do you run Kubernetes already?** If yes, Okteto, Signadot, Bunnyshell, Argo CD, or Pulumi (which can provision the cluster and its namespaces) fit. If not, look at Northflank, Render, or Pulumi on a non-Kubernetes target.
2. **How much of the stack must be copied?** Frontend only: Vercel or Netlify. A handful of services with a database: Northflank, Render, or Pulumi. Dozens of microservices: Signadot's shared-baseline model avoids copying them all.
3. **Does the preview need real cloud resources?** If a PR must test IAM, networking, or managed services, use a tool that provisions infrastructure, such as Pulumi or Terraform-backed Bunnyshell.
4. **Who owns cleanup?** Pick a tool with TTL or idle shutdown, or write that logic yourself.
5. **Where must it run?** Your own account or cluster narrows the list to BYOC options and the self-hosted ones.

## Frequently asked questions

### Do I need Kubernetes for ephemeral preview environments?

No. Render and Northflank run previews on their own platforms, and Pulumi can provision per-PR stacks for any cloud, including serverless and VM-based apps. Okteto, Signadot, Bunnyshell, and the Argo CD generator all assume a Kubernetes cluster.

### How do I control the cost of ephemeral environments?

Destroy environments on merge or close, add a TTL for ones that linger, shrink compute per preview, and stop idle environments. Render offers `expireAfterDays`, Northflank offers idle and duration policies, Signadot sandboxes carry a TTL, and Pulumi offers TTL stacks on Pro and Enterprise.

### Can I build my own pull request environments with Terraform or Pulumi?

Yes. Any IaC tool can create a stack or workspace per branch from a CI job and destroy it on close. With Pulumi, the [Automation API](/docs/iac/concepts/automation-api/) lets you do that in your own pipeline code. You then own the lifecycle logic, such as cleanup of abandoned environments.

### Are review apps the same as preview environments?

The terms overlap. "Review apps" is the older name from PaaS platforms, usually meaning one app copy per pull request. "Preview environments" and "ephemeral environments" often include databases and supporting infrastructure too.

### How fast do preview environments start?

It depends on your build, image pull, and data seeding. None of the vendors in this post publishes a measured spin-up time, so test with your own stack before choosing.

## Where to go next

If your previews need real cloud resources, start with the Review Stacks docs linked above or the [Kubernetes PR previews walkthrough](/blog/building-kubernetes-pr-previews-with-shared-pulumi-components/). For a wider view of the tooling around clusters, see [Best Kubernetes Infrastructure as Code Tools in 2026](/blog/best-kubernetes-iac-tools-2026/).
