---
title: "Best Backstage Alternatives for Developer Portals in 2026"
date: 2026-10-28
draft: false
meta_desc: "Compare Backstage alternatives for 2026: managed Backstage, Port, Cortex, OpsLevel, and Pulumi IDP, with honest tradeoffs on upkeep, catalog, and provisioning."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - platform-engineering
    - backstage
    - internal-developer-platform
    - devops
category: general
itemlist_name: "Backstage Alternatives for Developer Portals"
itemlist:
    - name: "Backstage"
    - name: "Managed Backstage (Roadie, Spotify Portal, Harness IDP)"
    - name: "Port"
    - name: "Cortex"
    - name: "OpsLevel"
    - name: "Pulumi IDP"
      url: "https://www.pulumi.com/"

social:
    twitter: |
        Backstage is a great framework, but running it is a job. We compared the main developer portal alternatives (managed Backstage, Port, Cortex, OpsLevel) and the platform layer that sits underneath any of them.
    linkedin: |
        Teams adopt Backstage for the catalog and then discover the real cost: plugin upkeep, catalog freshness, and a "create" button that still needs something to run behind it.

        We compared the main Backstage alternatives for 2026: managed Backstage (Roadie, Spotify Portal, Harness IDP), Port, Cortex, OpsLevel, and Pulumi IDP as the platform layer under any portal. Each entry lists who it fits and where it falls short, with sources linked.
    bluesky: |
        Backstage alternatives in 2026: managed Backstage, Port, Cortex, OpsLevel, and the platform layer underneath any portal.

        Who each one fits, what it costs you in upkeep, and what actually runs when a developer clicks "create."
---

The best Backstage alternatives in 2026 fall into three groups: managed Backstage (Roadie, Spotify Portal, Harness IDP), which keeps the framework and removes the hosting work; commercial portals (Port, Cortex, OpsLevel), which replace it with a SaaS catalog and scorecards; and a platform layer such as Pulumi IDP, which handles what runs when a developer clicks "create." Most teams need a portal choice and a platform choice, and they are separate decisions.

<!--more-->

A developer portal answers "what exists and who owns it." A platform answers "what gets built, under which rules, when someone asks for it." A portal without a working platform underneath is a nicer-looking status page. This guide covers the portal options first, then the platform layer, so you can pick each one on its own merits.

## Why are teams looking for Backstage alternatives?

Teams look for Backstage alternatives mainly because of the effort it takes to run. Backstage is an open source framework, not a finished product, so your team owns the hosting, the upgrades, the plugin choices, and the freshness of the catalog data.

Backstage itself is healthy. It is a [CNCF Incubating project](https://www.cncf.io/projects/backstage/), and the [Software Catalog](https://backstage.io/docs/features/software-catalog/) is described in its docs as "a centralized system that keeps track of ownership and metadata for all the software in your ecosystem." The friction shows up in the running of it. On r/devops, one thread on whether Backstage fits a team's needs includes a commenter who [decided against it](https://www.reddit.com/r/devops/comments/13k0h4n/is_backstage_a_good_solution_for_the_needs_of_our/) because it seemed like it would take an entire team to maintain, and another poster describes [frustration with scaffolder template workflows](https://www.reddit.com/r/devops/comments/1n0si3d/please_help_me_from_going_insane_with_backstage/). These are individual experiences, not measurements, but they match a common pattern: the first demo is quick, and the long tail of plugin upkeep and catalog hygiene is where the hours go.

## Portal or platform: which decision comes first?

Decide first whether your problem is visibility or execution. Visibility problems (nobody knows who owns a service, documentation is scattered, standards are unmeasured) are portal problems. Execution problems (provisioning takes a ticket, guardrails only exist as form fields, templates drift) are platform problems.

Every portal in this guide hands its "create" button to something else. Backstage's Scaffolder ships [built-in actions](https://backstage.io/docs/features/software-templates/builtin-actions/) for fetching template content, registering components, and publishing to git, and template authors wire up infrastructure themselves, for example with [Terraform and GitHub Actions](https://www.cncf.io/blog/2024/01/29/creating-infra-using-backstage-templates-terraform-and-github-actions/). Port documents [actions](https://docs.port.io/actions-and-automations/create-self-service-experiences/) as sending "a pre-defined payload" to your own infrastructure. That is a reasonable design. It also means the guardrails in a form field only apply to requests that come through that form.

## How we evaluated these tools

We compared each option on five questions:

1. **Time to first value and operating burden.** Who hosts it, upgrades it, and keeps it running?
2. **Catalog data model and freshness.** Is the catalog populated by auto-discovery, YAML in every repo, or both?
3. **What the self-service action runs on.** When a developer clicks the button, what does the work?
4. **Standards and scorecards.** Can you measure production readiness and drive improvement?
5. **Provisioning and policy.** Does the tool change infrastructure and enforce rules at that moment, or delegate both?

Pricing and feature details change quickly. We link to each vendor's own pages and describe only what those pages state as of October 2026. Where a vendor does not publish something, we say so.

## The best Backstage alternatives

### 1. Backstage (the baseline)

Backstage is the open source developer portal framework originally built at Spotify. It offers a [software catalog](https://backstage.io/docs/features/software-catalog/), [software templates](https://backstage.io/docs/features/software-templates/) that "load skeletons of code, template in some variables, and then publish" to GitHub or GitLab, TechDocs, and a large [plugin directory](https://backstage.io/plugins). The project reports more than 3,000 adopters in [a CNCF post](https://www.cncf.io/blog/2024/11/15/internal-developer-platforms-at-scale-with-the-certified-backstage-associate-cba-certification/).

**Best for:** Organizations with a dedicated platform team that wants full control and is comfortable maintaining a TypeScript and React codebase.

**Watch out for:** The work is yours: hosting, upgrades, plugin compatibility, and keeping catalog entries current. Scorecards and role-based access control come from plugins you pick or build.

### 2. Managed Backstage: Roadie, Spotify Portal, and Harness IDP

Managed options keep Backstage's catalog and plugin model and remove the operations work.

[Roadie](https://roadie.io/pricing/) says it has "been running a SaaS version of Backstage since 2020." Its pricing page lists automatic Backstage upgrades and open source plugins, with scorecards as an optional paid extra, and it states that data is stored in the EU.

[Spotify Portal](https://backstage.spotify.com/portal-migration) is described as "the SaaS, Spotify-managed edition of Backstage, built and operated by the same engineers who created and open sourced Backstage." Spotify's [FAQ](https://backstage.spotify.com/faqs) says its plugins are purchased as a bundle through the sales team.

[Harness IDP](https://www.harness.io/products/internal-developer-portal) states that organizations "can retain existing catalogs and plugins" while adding RBAC, SSO, and policy as code in a managed SaaS service, and it offers a free tier to try.

**Best for:** Teams that like the Backstage model and its plugin ecosystem but do not want to staff its upkeep.

**Watch out for:** You still model your catalog with Backstage concepts, and the self-service layer still delegates provisioning. Spotify Portal pricing is not published, so budget a sales conversation.

### 3. Port

Port is a SaaS portal built around a flexible data model. In its [glossary](https://docs.port.io/glossary/), a blueprint is "closer to a class definition in object-oriented programming," and entities are the instances. You define what a "service," "environment," or "cloud account" means for your organization rather than starting from a fixed schema.

[Self-service actions](https://docs.port.io/actions-and-automations/create-self-service-experiences/) can be run from the UI, the API, or by AI agents, and include guardrails such as manual approval. [Scorecards](https://docs.port.io/scorecards/overview/) track rules by level, such as Bronze, Silver, and Gold. Port is [SaaS](https://www.port.io/pricing), with a free plan that the pricing page lists as up to 15 seats, and its 2026 positioning leans heavily into AI agents and a "context lake" of engineering data.

**Best for:** Teams that want a configurable catalog without running the software, and that expect to model more than services.

**Watch out for:** Flexibility means design work up front. Actions send a payload to a backend you operate, so something else still provisions the infrastructure.

### 4. Cortex

Cortex describes itself as an "Engineering Operations Platform." Its strongest area is standards: [Scorecards](https://www.cortex.io/products/scorecard) turn "standards for production readiness, security, AI adoption, and more into automated guardrails," with initiatives that carry target dates. [Workflows](https://www.cortex.io/products/workflows) assemble multi-step processes from a block library of integrations, and Cortex offers a public [scorecard library](https://github.com/cortexapps/scorecard-library) on GitHub.

**Best for:** Engineering leaders whose main goal is raising and tracking service quality across many teams.

**Watch out for:** [Pricing is custom](https://www.cortex.io/pricing) per seat and not published, and we found no documentation describing a built-in cloud provisioning engine. Workflows orchestrate steps and hand off to whatever does the work.

### 5. OpsLevel

OpsLevel is a SaaS portal focused on catalog accuracy and maturity. Its [Service Suggestions](https://www.opslevel.com/resources/service-suggestions) feature discovers new services as they are deployed and helps you add them, which targets the stale-catalog problem directly. It also offers [scorecards, checks, and campaigns](https://www.opslevel.com/pricing) for cross-cutting initiatives, and [Actions](https://www.opslevel.com/resources/how-actions-work-in-opslevel) described as "one-click task automation with guardrails baked in."

**Best for:** Teams whose pain is an out-of-date catalog and who want maturity tracking without maintaining YAML in every repository.

**Watch out for:** [Pricing is custom](https://www.opslevel.com/pricing), and, as with the other portals, actions trigger automation rather than provisioning infrastructure themselves.

### 6. Pulumi IDP (the platform layer)

Pulumi IDP is the entry in this list that works at a different layer. It does not try to be a service ownership catalog. It supplies what runs behind the button, whichever portal sits in front.

- **Components and templates.** Platform teams package golden paths as versioned, tested code in TypeScript, Python, Go, C#, Java, or YAML, and publish them through a [private registry](/docs/idp/concepts/private-registry/). [Organization templates](/docs/idp/concepts/organization-templates/) scaffold real projects from those patterns, and [no-code stacks](/docs/idp/concepts/no-code-stacks/) let developers deploy approved components without writing code.
- **Policy where the change happens.** [Pulumi Policies](/docs/discovery-governance/concepts/policy-as-code/) run during preview and update, so a rule applies no matter which portal, script, or pipeline started the run. [Pulumi ESC](/docs/esc/) handles secrets and configuration for those stacks.
- **Visibility.** [Services](/docs/idp/concepts/services/) group stacks and resources into the thing a team owns, and [Pulumi Neo](/docs/ai/concepts/neo/) can help with infrastructure changes inside the same guardrails.
- **Portal compatibility.** The [Pulumi Backstage plugin](/docs/idp/integrations/backstage-plugin/) adds Pulumi cards, a catalog provider, and scaffolder actions (`pulumi:new`, `pulumi:preview`, `pulumi:up`, and others) to any Backstage instance, including managed ones. The [plugin announcement](/blog/pulumi-backstage-plugin/) walks through setup.

**Best for:** Teams whose bottleneck is execution: slow provisioning, drifting templates, and policy that only exists in a form.

**Watch out for:** Pulumi IDP is not an ownership-and-scorecard catalog product. If your first problem is "who owns this service," pair it with one of the portals above.

For the head-to-head with the open source framework, see [Pulumi vs. Backstage](/blog/backstage-vs-pulumi-idp-why-infrastructure-first-platform-engineering-matters/).

## How do the options compare?

| Tool | Category | Hosting | Catalog model | Self-service runs on | Scorecards | Provisioning and policy built in |
| --- | --- | --- | --- | --- | --- | --- |
| Backstage | Open source portal framework | Self-hosted | YAML entities and plugins | Scaffolder, wired by you | Via plugins | No |
| Roadie, Spotify Portal, Harness IDP | Managed Backstage | SaaS | Backstage model | Scaffolder, wired by you | Roadie: optional paid extra; Spotify: Soundcheck plugin; Harness: scorecards | No |
| Port | Commercial portal | SaaS | Custom blueprints | Your backend, via payload | Yes | No |
| Cortex | Commercial portal | See vendor | Catalog entities | Workflows and integrations | Yes, a core feature | No |
| OpsLevel | Commercial portal | SaaS | Auto-discovered catalog | Actions and automation | Yes | No |
| Pulumi IDP | Platform layer | Pulumi Cloud | Stacks and services | Pulumi components and templates | Not a catalog product | Yes |

## What about Atlassian Compass?

If you are weighing Compass, check Atlassian's plans first. Its support page on [migrating from Compass to DX](https://support.atlassian.com/compass/docs/migrate-from-compass-to-dx/) says access to Compass ends at the end of your contract or once Compass is no longer supported, which is planned for December 31, 2027. We left it out of the list for that reason.

## Backstage is too much to maintain: what should we do?

Start by naming what you maintain today. If the burden is hosting and upgrades, managed Backstage keeps your investment in plugins and templates. If the burden is a catalog nobody updates, a portal with auto-discovery or a flexible data model (OpsLevel, Port) addresses it directly. If the burden is that every new service still needs a platform engineer to provision it, no portal fixes that, and the work belongs in your components, templates, and policies.

Whichever portal you choose, keep the "create" button thin. Make it call a versioned component rather than a one-off script. Then you can change portals later without rewriting how infrastructure gets built, which is the cheapest insurance against the next portal migration.

## How do you choose?

| If your situation is... | Start with |
| --- | --- |
| A platform team that wants full control and enjoys TypeScript | Backstage |
| Backstage works, but upgrades and hosting eat time | Managed Backstage |
| You want a configurable SaaS catalog and actions | Port |
| Your priority is standards and service quality | Cortex |
| Your catalog is stale and you want discovery | OpsLevel |
| Provisioning is slow and guardrails are inconsistent | Pulumi IDP, with any portal on top |

## Frequently asked questions

### What is the best alternative to Backstage?

There is no single best alternative. Managed Backstage suits teams that want to keep the framework without the operations work, Port, Cortex, and OpsLevel suit teams that want a SaaS catalog, and Pulumi IDP suits teams that need the provisioning and policy layer under whichever portal they use.

### Can I use Pulumi with Backstage?

Yes. The [Pulumi Backstage plugin](/docs/idp/integrations/backstage-plugin/) adds Pulumi stack cards, a catalog provider, and scaffolder actions to a Backstage instance, so a template can create and update Pulumi stacks directly.

### Is a developer portal the same as an internal developer platform?

No. A portal is the interface developers see. A platform is the full set of tools, components, and guardrails behind it. For the longer explanation, see [what is an internal developer platform](/what-is/what-is-an-internal-developer-platform/).

## Where to go next

Pick the portal that fits how your teams find and measure services, then decide what executes the requests behind it. If provisioning and policy are your bottleneck, see how [Pulumi's internal developer platform](/product/internal-developer-platforms/) packages components, templates, and policies that any portal can call. For the build-versus-buy view across the whole stack, read [The Guide to Platform Engineering](/blog/the-guide-platform-engineering-idp-steps-best-practices/) and our post on [golden paths](/blog/golden-paths-infrastructure-components-and-templates/).
