---
title: "Best AI SRE and AIOps Tools in 2026"
date: 2026-10-02
draft: false
meta_desc: "Ten AI SRE and AIOps tools for 2026 compared on production track record, human approval, stack fit, and what each vendor says about failure modes."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - ai
    - ai-agents
    - devops
    - platform-engineering
    - automation
category: general
faq_schema: true
itemlist_name: "AI SRE and AIOps Tools"
itemlist:
    - name: "Datadog Bits AI SRE"
      url: "https://www.datadoghq.com/product/ai/bits-investigation/"
    - name: "PagerDuty SRE Agent"
      url: "https://docs.pagerduty.com/ai-automation/advance/sre-agent"
    - name: "Dynatrace Intelligence"
      url: "https://www.dynatrace.com/platform/artificial-intelligence/"
    - name: "Resolve AI"
      url: "https://resolve.ai/"
    - name: "Traversal"
      url: "https://traversal.com/"
    - name: "Cleric"
      url: "https://cleric.ai/"
    - name: "incident.io AI SRE"
      url: "https://incident.io/ai-sre"
    - name: "AWS DevOps Agent"
      url: "https://aws.amazon.com/devops-agent/"
    - name: "Azure SRE Agent"
      url: "https://learn.microsoft.com/azure/sre-agent/overview"
    - name: "HolmesGPT"
      url: "https://github.com/HolmesGPT/holmesgpt"

# Social media copy, auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        AI SRE tools promise faster incident response. Benchmarks and engineers say the results are uneven.

        We compared 10 tools on track record, human approval, stack fit, and how openly vendors discuss failure modes.
    linkedin: |
        Every observability and incident vendor now sells an "AI SRE." Public benchmarks tell a more cautious story: IBM's ITBench found agents resolving 13.8% of SRE scenarios in 2025, and engineers keep asking which of these tools are ready for production.

        We compared ten AI SRE and AIOps tools (Datadog, PagerDuty, Dynatrace, Resolve AI, Traversal, Cleric, incident.io, AWS DevOps Agent, Azure SRE Agent, and HolmesGPT) on four criteria: production track record, human-in-the-loop safeguards, fit with your existing IaC and observability stack, and transparency about failure modes.

        The guide also covers what changes when an agent gets write access to infrastructure, and flags which numbers are vendor-reported.
    bluesky: |
        AI SRE tools promise faster incident response, but public benchmarks and engineers report uneven results.

        We compared 10 tools on track record, human approval, stack fit, and how openly vendors discuss failure modes.
---

AI SRE and AIOps tools use language models and statistical correlation to cut the manual work of incident response. They group noisy alerts, investigate a failing service across logs, metrics, traces, and recent changes, propose a root cause, and in some products suggest or apply a fix. They vary widely in how much they do without a human.

<!--more-->

Every observability and incident vendor now sells an "AI SRE." This guide compares ten of them, plus one open-source pair worth knowing, against the criteria SREs keep raising: does it work on real incidents, who approves its actions, does it fit your stack, and does the vendor say where it fails. Vendor-reported numbers are labeled as such, and several vendors do not publish pricing or accuracy data at all.

## What do AI SRE and AIOps tools actually do?

They do three different jobs, and many products blur them together in marketing.

| Job | What it means | Typical autonomy | Example |
| :--- | :--- | :--- | :--- |
| Alert correlation | Group and deduplicate alerts into incidents, reduce noise | Fully automatic, low risk | BigPanda, Dynatrace causal analysis |
| Investigation and root cause analysis | Query telemetry, code changes, and past incidents, then rank hypotheses | Autonomous, read-only | Datadog, Cleric, Traversal, HolmesGPT |
| Remediation | Open a pull request, run a runbook, or change a live system | Usually gated by approval | Azure SRE Agent, Dynatrace Cloud SRE Agent |

Older AIOps products concentrated on the first job. The 2025 and 2026 wave of "AI SRE" products concentrates on the second and is moving toward the third. When you read a product page, check which job the headline claim actually describes.

## Why are engineers skeptical of AI SRE tools?

The evidence that independent parties can check is thin, and the numbers that exist are modest.

- **ITBench.** IBM Research published [ITBench](https://arxiv.org/abs/2502.05352) in February 2025, with 94 real-world scenarios. Agents built on state-of-the-art models resolved 13.8% of the SRE scenarios, 25.2% of the security and compliance scenarios, and 0% of the FinOps scenarios. Models have improved since, so treat this as a 2025 baseline.
- **OTelBench.** Quesma's [OTelBench](https://quesma.com/blog/introducing-otel-bench/) tested 14 models on OpenTelemetry instrumentation tasks. The best model passed 29%. Quesma sells related tooling, and the task is narrower than incident response, but instrumentation quality decides what an AI SRE can see. In the [Hacker News discussion](https://news.ycombinator.com/item?id=46811588), commenters described agents deleting failing tests or papering over problems instead of reporting them.
- **Vendor numbers.** Most published figures for MTTR reduction or "root cause accuracy" come from the vendors, usually from customer case studies, without a public methodology.
- **Community threads.** Engineers in r/sre and r/devops are asking the same questions, for example in [SRE tools feel all over the place lately](https://www.reddit.com/r/sre/comments/1ou2u0s/sre_tools_feel_all_over_the_place_lately/). Read the comments there for first-hand experience. This guide does not paraphrase them.

Run a trial against your own past incidents before you believe any headline number.

## How should you evaluate an AI SRE tool?

Start with four criteria, and ask each vendor to answer them in writing.

1. **Production track record.** Ask for named customers, the number of real incidents handled, and any public benchmark. A launch announcement does not count as a track record.
2. **Human-in-the-loop safeguards.** Find out what the tool can change by default, whether every action needs approval, and whether you can restrict it to read-only. Check that actions are logged.
3. **Integration with your stack.** A tool bound to one vendor's telemetry sees only that vendor's data. Check support for your observability stack, your incident tool, your source control, and your infrastructure as code repositories, since many incidents trace back to a change.
4. **Transparency about failure modes.** Look for confidence scores, cited evidence, hypotheses marked as inconclusive, and documentation of known limits. A tool that cannot say "I don't know" will eventually state a wrong cause with confidence.

Also test cost predictability. Several products meter usage in credits or agent-time units, and the bill depends on how many investigations your alerts trigger.

## Which are the best AI SRE and AIOps tools in 2026?

The ten below span observability platforms, incident management vendors, startups, cloud providers, and open source. Order does not imply rank.

### 1. Datadog Bits AI SRE (Bits Investigation)

[Datadog's agent](https://www.datadoghq.com/product/ai/bits-investigation/) investigates alerts on its own, generates root-cause hypotheses, and tests them against telemetry, Kubernetes events, and recent changes. Each hypothesis is labeled validated, invalidated, or inconclusive, with supporting evidence. Datadog now brands the product Bits Investigation, but most people still search for Bits AI SRE.

- **Safeguards:** Investigation is autonomous. Follow-up actions such as posting to Slack or creating a Jira ticket run on one click. Bits Code can propose a fix as a pull request for engineers to review.
- **Integrations:** Datadog telemetry, Slack, GitHub, Jira, and ServiceNow through Case Management.
- **Evidence:** Datadog says thousands of organizations used it during limited availability. It has not published an accuracy benchmark that we found.
- **Watch-outs:** It reasons over Datadog's own data, so telemetry elsewhere is invisible to it. Pricing uses shared AI credits, starting at $500 per month for 500 credits billed annually or $1.30 per credit on demand.

### 2. PagerDuty SRE Agent

[PagerDuty's SRE Agent](https://docs.pagerduty.com/ai-automation/advance/sre-agent) (called Paige, part of PagerDuty Advance) ingests runbooks, event data, and logs, surfaces likely causes, recommends diagnostic and remediation steps, and recalls similar past incidents. It can also generate and update runbooks. For a deeper look at PagerDuty with infrastructure code, see our post on [incident response as code with PagerDuty and Pulumi](/blog/incident-response-as-code-pagerduty-pulumi/).

- **Safeguards:** Mostly advisory. It recommends, and you act through Slack, the incident page, or the console. A "virtual responder" mode that investigates as soon as an incident triggers is in early access.
- **Integrations:** CloudWatch, Datadog, Grafana, New Relic, Sentry, Splunk, and GitHub as a knowledge source.
- **Evidence:** We found no named customers or accuracy data on the pages we read.
- **Watch-outs:** It needs PagerDuty AI, and the Operations or Reliability Console also needs AIOps. Dollar pricing is not public. Usage is metered in AI Actions.

### 3. Dynatrace Intelligence

Dynatrace folded its Davis AI into [Dynatrace Intelligence](https://www.dynatrace.com/platform/artificial-intelligence/), introduced in early 2026 and described as agentic AI combined with deterministic causal AI. A July 2026 announcement added an Autonomous SRE Agent that starts on new problems and a Cloud SRE Agent that coordinates remediation across AWS, Azure, and Google Cloud with an auditable record.

- **Safeguards:** Dynatrace describes the system as transparent, auditable, and governed. We could not verify the approval mechanics for each new agent.
- **Integrations:** AWS, Azure, Google Cloud, ServiceNow, Atlassian, and PagerDuty.
- **Evidence:** Dynatrace's causal engine has a long production history in alert correlation. The new agents are recent, and Western Governors University is quoted in the announcement.
- **Watch-outs:** Confirm which agents are generally available and what they cost before planning around them.

### 4. Resolve AI

[Resolve AI](https://resolve.ai/) positions itself as an AI SRE that goes on call, finds root cause, and mitigates. It also passes production context to coding agents for remediation.

- **Safeguards:** The homepage claims it autonomously resolves incidents. We could not find a public description of the approval and permission model, so ask for it.
- **Integrations:** The public pages we read do not list them.
- **Evidence:** Resolve publishes case studies for DoorDash, Coinbase, and Zscaler. The Coinbase study reports 72% faster investigation time and the Zscaler study reports 30% fewer engineers in war rooms. Both are self-reported.
- **Watch-outs:** Pricing is not public, and the accuracy claims come without a published methodology.

### 5. Traversal

[Traversal](https://traversal.com/) combines language models, agents, and causal machine learning to find root cause from logs, metrics, and traces, and infers cause and effect instead of correlating anomalies. Its Workers join an incident channel and decide when to engage.

- **Safeguards:** The vendor says it deploys read-only by default with no agents or sidecars on top of existing observability tools. It supports bring-your-own-cloud and bring-your-own-model, so telemetry and source code stay in your environment.
- **Evidence:** Traversal says Workers have run across hundreds of real incidents, a vendor-reported figure.
- **Watch-outs:** It is a young company, so ask for references in your industry. Pricing is not public.

### 6. Cleric

[Cleric](https://cleric.ai/) investigates alerts and keeps operational memory from past incidents. Its homepage shows it opening a pull request for approval.

- **Safeguards:** Read-only by default, with every action logged and each investigation auditable.
- **Integrations:** Datadog and Grafana for metrics, Kubernetes and EKS for events, GitHub, PagerDuty, and the kubectl, gh, and aws command lines.
- **Evidence:** The company lists SOC 2 Type II compliance. We did not find named customers or a public benchmark.
- **Watch-outs:** Pricing is credit-based, at $1 per credit on monthly plans, with negotiated enterprise terms.

### 7. incident.io AI SRE

[incident.io](https://incident.io/ai-sre) starts debugging when an incident is declared. It connects telemetry, code changes, and past incidents, and can name the likely pull request behind a problem.

- **Safeguards:** The page says the only change it can make to your systems is a pull request that you review and merge.
- **Transparency:** Findings carry a confidence score and sources, with an audit trail of the evidence.
- **Evidence:** turbopuffer has published a case study. The "up to 80% of incident response" figure on the site is a marketing claim.
- **Watch-outs:** It is Slack-native. Root cause analysis is an add-on on higher tiers, and the price is not listed.

### 8. AWS DevOps Agent

[AWS DevOps Agent](https://aws.amazon.com/devops-agent/) was announced as a free preview at re:Invent 2025 and became generally available on March 31, 2026. It investigates incidents, answers on-demand SRE questions, recommends preventive changes, and tests releases.

- **Safeguards:** Its mitigation plans are written as specifications for developers and coding agents such as Kiro. We did not find documentation of it executing changes on its own.
- **Integrations:** CloudWatch, Datadog, Dynatrace, New Relic, Splunk, Grafana, GitHub, GitLab, Azure DevOps, ServiceNow, PagerDuty, and Slack.
- **Pricing:** $0.0083 per agent-second. AWS's own example works out to about $39.84 a month for ten eight-minute investigations, with connected services billed separately.
- **Watch-outs:** We found no named customers. It is the most transparent on price of the commercial tools here.

### 9. Azure SRE Agent

[Azure SRE Agent](https://learn.microsoft.com/azure/sre-agent/overview) reached general availability in March 2026. It has two run modes. In review mode an administrator approves write actions before they run. In autonomous mode the agent applies them without waiting.

- **Integrations:** Azure resources, Application Insights, GitHub, PagerDuty, ServiceNow, and MCP connectors.
- **Evidence:** Microsoft reports 1,300 or more agents deployed internally, 35,000 or more incidents mitigated, and 20,000 or more engineering hours saved. Those are Microsoft's own figures. Ecolab is a named customer.
- **Watch-outs:** Billing combines an always-on charge of 4 Azure Agent Units per agent-hour with token-metered usage. A GitHub issue on the project reports consumption rising in May 2026 without user changes, so watch costs closely.

### 10. HolmesGPT (and k8sgpt)

[HolmesGPT](https://github.com/HolmesGPT/holmesgpt) is an open-source investigation agent in the CNCF sandbox, under the Apache-2.0 license. It works with Prometheus, Grafana, Datadog, Kubernetes, Helm, GitHub, PagerDuty, OpsGenie, Jira, and Slack, and runs against any major LLM provider.

- **Safeguards:** It is read-only and respects Kubernetes RBAC by default. Remediation is a separate opt-in toolset, so you grant execute access deliberately.
- **Evidence:** The repository has about 3,500 GitHub stars and shipped release 0.42.0 on September 16, 2026. We found no named customers.
- **Watch-outs:** You operate it and pay your own model costs.

[k8sgpt](https://github.com/k8sgpt-ai/k8sgpt) is a CNCF sandbox project with about 8,200 stars that scans clusters and explains findings with an LLM. It diagnoses only and has an `--anonymize` flag for data sent to the model. Teams that want to see what AI-assisted diagnosis does with their own incidents before buying anything often start with one of these two.

## What changes when an AI agent has write access to infrastructure?

Diagnosis mistakes cost you time. Write mistakes cost you an outage. Once an agent can change a live system, the safeguards you already apply to people matter: a preview of the change, policy checks before it applies, scoped credentials, and an approval step for anything destructive.

Most of the tools above stop at read-only investigation plus a pull request for a person to merge, and that is a sensible default. Infrastructure written as code gives a pull request something concrete to review, and tools such as [policy as code](/docs/discovery-governance/concepts/policy-as-code/) can block an unsafe change before it ships. Drift is a related case, covered in our post on [drift detection and remediation](/blog/day-2-operations-drift-detection-and-remediation/).

Pulumi Neo applies the same idea to infrastructure changes. You can cap its permissions with [read-only mode](/blog/neo-read-only-mode/) and set what it may do in the [permissions model](/docs/ai/neo/permissions/), and it can preview changes and open pull requests before anything deploys. Read more on the [Neo product page](/product/neo/). Neo is an infrastructure agent rather than an incident investigation tool, so it sits alongside the products above. For a broader list of AI tools across the infrastructure lifecycle, see [Best AI Infrastructure Tools in 2026](/blog/ai-infrastructure-tools/).

## How do the ten tools compare?

| Tool | Type and deployment | Default autonomy | Human approval | Stack fit | Public evidence | Best for |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Datadog Bits AI SRE | Observability platform, SaaS | Autonomous investigation | One-click actions, PR review | Datadog data | Vendor-reported adoption | Datadog-centric teams |
| PagerDuty SRE Agent | Incident management, SaaS | Advisory | Recommendations only | Multi-vendor connectors | None found | PagerDuty shops |
| Dynatrace Intelligence | Observability platform, SaaS | Agents on new problems | Described as governed, details unverified | Dynatrace, cloud providers | Long causal AI history | Large Dynatrace estates |
| Resolve AI | Startup, SaaS | Claims autonomous resolution | Not public | Not public | Self-reported case studies | Teams that want a dedicated vendor |
| Traversal | Startup, SaaS or BYOC | Read-only by default | Not public | Layers on existing tools | Vendor-reported incident count | Teams with data residency needs |
| Cleric | Startup, SaaS | Read-only by default | PR for approval | Datadog, Grafana, Kubernetes | SOC 2 Type II | Kubernetes-heavy teams |
| incident.io AI SRE | Incident management, SaaS | Investigates on declared incident | PR only, you merge | Slack-native | One case study | incident.io customers |
| AWS DevOps Agent | Cloud provider, managed | Investigation and plans | Plans for developers | AWS plus many third parties | None found | AWS-centric teams |
| Azure SRE Agent | Cloud provider, managed | Review or autonomous mode | Per-mode approval | Azure plus connectors | Vendor-reported internal results | Azure-centric teams |
| HolmesGPT | Open source, self-hosted | Read-only | Remediation opt-in | Broad, any LLM | Open repository | Teams that want control and low cost |

## Are AI SRE tools production ready?

Investigation tools are ready to trial in production in read-only mode, and several vendors design them that way. Treat remediation with more caution. The public benchmarks show agents still miss most hard scenarios, and almost none of the vendor numbers have independent verification. A fair reading is that these tools can shorten the first ten minutes of an incident and are not yet a substitute for an on-call engineer.

## How should you choose?

1. **Replay your last ten incidents.** Ask each shortlisted vendor to investigate alerts from past incidents where you know the cause, and score the results.
2. **Start read-only.** Keep write access off until you have seen how the tool behaves, then enable it for one low-risk action at a time.
3. **Match your existing vendors.** If you already pay for Datadog, Dynatrace, PagerDuty, incident.io, AWS, or Azure, price their native agent first.
4. **Run an open-source baseline.** HolmesGPT or k8sgpt gives you a floor to compare commercial tools against.
5. **Model the bill.** Estimate investigations per month from your alert volume before signing a credit-based contract.
