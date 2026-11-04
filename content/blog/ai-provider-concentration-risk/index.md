---
title: "AI-provider concentration risk: lessons from Sept 3"
date: 2026-11-04
draft: false
meta_desc: "Three AI providers had overlapping outages on September 3. Learn what AI-provider concentration risk is, how to measure it, and how to reduce it with code."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - ai
    - llm
    - cloud-engineering
    - infrastructure-as-code
category: perspectives
faq_schema: true
social:
    twitter: |
        On September 3, ChatGPT, Claude, and Grok had outages that overlapped for about 93 minutes. Each had its own cause. If your fallback model sits next to your primary one, you have concentration risk.
    linkedin: |
        On September 3, 2026, ChatGPT, Claude, and Grok each had an outage, and eWeek's timeline comparison found all three affected at once for 93 minutes. The vendors cited different causes, and none linked the incidents.

        For teams that treat a second model API as their failover plan, the lesson is about correlation. Providers can fail independently and still fail together, and a spike of displaced traffic can land on whichever provider you picked as the backup.

        We wrote up how to measure your AI-provider concentration exposure, how to keep provider choice in code instead of scattered across services, and how to rehearse provider loss before it happens.
    bluesky: |
        Three AI providers had outages on Sept 3 that overlapped for about 93 minutes. Different causes, same bad morning for anyone whose fallback model was one of the other two.

        How to measure and reduce AI-provider concentration risk:
---
AI-provider concentration risk is the exposure you carry when your product depends on a small number of model providers whose compute, hosting, and failure modes overlap more than their brands suggest. A primary model and a "fallback" model can fail on the same morning, which turns a failover plan into a second outage.

On September 3, 2026, that scenario played out in public. This post covers what happened, why a second API key is a weaker hedge than it looks, and three concrete steps: inventory your dependencies, keep provider choice in code, and rehearse provider loss.

## What happened on September 3

Three of the best-known AI providers had separate incidents that overlapped:

| Provider | Published incident | Stated cause |
|---|---|---|
| Anthropic | [Elevated errors for multiple models](https://status.claude.com/incidents/461yvfrzpwtt), affecting claude.ai, the Claude API, Claude Code, and Claude Cowork; resolved at 16:16 UTC | None published |
| OpenAI | [Elevated errors across ChatGPT and Codex](https://status.openai.com/incidents/01M1KWEDH417T2CF44YYHZDFCR), 14:43 to 16:55 UTC | A [routing configuration change](https://status.openai.com/incidents/01M1KWEDH417T2CF44YYHZDFCR/write-up) that "prevented affected requests from reaching our services" |
| xAI (Grok) | A roughly three-hour, 37-minute outage, per [eWeek](https://www.eweek.com/news/chatgpt-claude-grok-gemini-outages/) | An outage at its Memphis compute center, per xAI's statement on X |

After lining up the vendors' published timelines, eWeek [found that ChatGPT, Claude, and Grok were simultaneously affected for 93 minutes](https://www.eweek.com/news/chatgpt-claude-grok-gemini-outages/). The same report notes that no vendor has linked the incidents and that their timing alone does not establish a common cause.

The Cloud Security Alliance reached a similar reading in its [September 19 research note on the triple AI outage](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/09/CSA_research_note_triple_ai_outage_concentration_risk_20260919-csa-styled.pdf). It describes the events as "most plausibly overlapping, independently caused outages rather than one common outage with several symptoms," and reports that none of AWS, Azure, or Google Cloud recorded downtime that day.

Independent causes do not make the risk smaller for a team that depended on two of the three. A customer's application sees a provider that stopped answering, whatever the reason. As the MSP Integra put it in [AI Has Become Business Infrastructure. Recent Outages Expose the Risk](https://www.integramsp.com/2026/09/03/recent-outages-expose-risk/): "Convenience eventually becomes dependency, and dependency requires a continuity plan."

## Why are AI providers more correlated than they look?

Several forces can pull providers' fates together even when their engineering teams never coordinate:

- **Shared compute suppliers.** In May 2026, Anthropic announced an agreement with SpaceX to use [all of the compute capacity at the Colossus 1 data center](https://finance.yahoo.com/sectors/technology/articles/anthropic-wants-elon-musks-space-182840734.html), more than 300 megawatts and over 220,000 Nvidia GPUs. The CSA published a research note on September 9 titled [One Data Center, Two AI Rivals: Concentration Risk](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-provider-concentration-risk-20260909-cs/) whose title poses the question of what happens when competing model providers draw on the same physical infrastructure. Public reporting does not confirm that the Memphis facility behind Grok's outage is the one Anthropic leases, so treat the link as a question to ask your vendors, not a finding.
- **Spillover demand.** OpenAI's write-up says that as routing was restored, "returning traffic overloaded some services, prolonging recovery." The same dynamic applies across vendors. When one provider degrades, its users move to another, and your fallback may be busiest at the moment you need it.
- **Opaque supply chains.** An API key tells you nothing about which data centers, GPU fleets, or cloud regions sit behind it. Two vendors can look independent from your side of the API and share a dependency you cannot see.

A fallback chosen by brand name rather than by what sits underneath it can leave you with two dependencies and one real point of failure.

## How do you measure your AI-provider concentration exposure?

Measure it by building a dependency map: list every place your systems call a model, record the provider and the infrastructure behind each call, and rank each dependency by how much breaks when it fails. Three passes get you there.

1. **Inventory every model call.** Search code, CI pipelines, internal agents, and secrets stores for provider SDKs and API keys. Include teams that adopted AI tooling without going through platform review. Also list managed AI services running inside your own cloud accounts, such as Amazon Bedrock, Azure OpenAI, or Vertex AI.
2. **Map each call to a provider and an underlying platform.** For every dependency, write down the vendor, the hosting cloud or compute supplier if the vendor discloses it, the region, and whether a fallback exists. Mark the cells you cannot fill in. Unknowns are findings.
3. **Score by criticality.** Rank each dependency by customer impact if it disappears for three hours: hard failure, degraded experience, or internal-only inconvenience. Concentration shows up when your high-criticality rows share a provider or a platform.

For the managed services in your own accounts, you do not have to rely on spreadsheets. [Pulumi Discovery](/docs/discovery-governance/concepts/discovery/) scans your cloud provider accounts and builds an inventory of resources "regardless of how those resources were created or are currently managed," with search and resource relationships on top. It covers what runs in your cloud accounts. Calls to third-party model APIs still need the code and secrets search from step one.

## How do you reduce AI-provider concentration with portable infrastructure code?

Keep provider choice in one place that you can change and redeploy. When model endpoints, credentials, and gateway settings are scattered across services, switching providers during an incident means editing many things under pressure. When they are defined in one program, a switch is a configuration change followed by a preview and an update.

Pulumi lets you write that program in TypeScript, Python, Go, C#, or Java, and the same program can target AWS, Azure, and Google Cloud through their providers. Here is a minimal pattern that selects the active AI backend from stack configuration:

```typescript
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();

// "primary" and "fallback" are stack-level choices, not hard-coded vendors.
const primary = config.require("aiPrimary");   // e.g. "bedrock"
const fallback = config.require("aiFallback"); // e.g. "azure-openai"

const backends: Record<string, { endpoint: pulumi.Input<string>; key: pulumi.Output<string> }> = {
    bedrock: {
        endpoint: config.require("bedrockEndpoint"),
        key: config.requireSecret("bedrockKey"),
    },
    "azure-openai": {
        endpoint: config.require("azureOpenAiEndpoint"),
        key: config.requireSecret("azureOpenAiKey"),
    },
};

// Downstream resources read the active backend from one place.
export const activeEndpoint = backends[primary].endpoint;
export const fallbackEndpoint = backends[fallback].endpoint;
```

Store the per-provider credentials in [Pulumi ESC](/docs/esc/) so each environment pulls its own secrets, and drive the rest through [stack configuration](/docs/iac/concepts/config/). Choose fallbacks for independence, not familiarity: prefer a provider on a different hosting platform from your primary, and ask each vendor what compute stands behind its service.

If your needs include capacity you control, a self-hosted option can be part of the mix. Our post on [running AI infrastructure with the Pulumi AICR provider](/blog/self-hosted-ai-infrastructure-pulumi-aicr/) shows how to deploy GPU clusters across clouds from code, and the [AI infrastructure tools guide](/blog/ai-infrastructure-tools/) compares the wider landscape. For the clouds Pulumi supports, see the [cloud integrations overview](/docs/integrations/clouds/).

## How do you test a provider-loss scenario?

Rehearse it in a non-production stack before it happens in production. A game day for provider loss takes an afternoon:

1. **Remove the primary.** Blank or revoke the primary provider's key in a staging stack, or block its endpoint at the network layer.
2. **Observe the failure mode.** Record what users see, how long detection takes, and whether retries pile up and make things worse.
3. **Switch by configuration.** Change the stack config to point at the fallback, run `pulumi preview` to review the change, then `pulumi up`. Time the whole switch.
4. **Check fallback capacity.** Confirm quotas, rate limits, and model availability on the fallback can carry your real traffic. Spillover from other displaced customers is the case to plan for.
5. **Decide the degraded mode.** Some features should fail closed, some should serve cached or simpler results, and some can queue. Write those decisions down per feature.

Repeat the exercise on a schedule, such as quarterly, and after any change in providers, models, or hosting regions.

## What this approach does not fix

Provider outages will keep happening, and no amount of infrastructure code prevents a vendor's routing change from going wrong. A second provider adds cost and testing work, and models differ in behavior, so a fallback can return different answers. The goal is narrower: know your dependencies, avoid hidden overlap between primary and fallback, and make the switch a rehearsed procedure.

## Frequently asked questions

### What is AI-provider concentration risk?

It is the exposure created when a product relies on one or a few AI model providers whose infrastructure, compute suppliers, or failure modes overlap. If those providers degrade together, or a displaced-traffic surge hits your backup, a multi-vendor plan can still lose the feature entirely.

### Did the September 3 outages share a single cause?

No shared cause has been confirmed. OpenAI cited a routing configuration change, xAI cited an outage at its Memphis compute center, and Anthropic published no root cause. The Cloud Security Alliance's September 19 note judged them most plausibly overlapping, independently caused outages.

### Is a multi-provider AI setup worth the cost?

It depends on how much the feature matters. For customer-facing features where a three-hour outage is costly, a tested fallback usually pays for itself. For internal or low-stakes uses, a documented degraded mode may be enough. Score each dependency by impact before you spend.

### How often should we test provider failover?

Quarterly is a reasonable starting cadence, plus after any change to providers, models, regions, or quotas. A failover path that has not been exercised recently should be treated as unproven, and the cost of a staging drill is small compared with discovering a quota limit during an incident.

## Get started

Start with the inventory. A scan of your own cloud accounts covers the managed model services, and [Pulumi IaC](/docs/iac/) lets you keep provider choice in code you can review, preview, and redeploy.
