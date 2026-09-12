---
title_tag: "Pulumi vs. Service Catalogs: Backstage, Port, and Cortex"
faq_schema: true
authors: ["pulumi-content-team"]
meta_desc: "Backstage, Port, and Cortex give developers a self-service catalog. Pulumi is the infrastructure as code engine that provisions safely underneath."
title: Service catalogs
h1: Service catalogs vs. infrastructure as code
menu:
    iac:
        name: Service catalogs
        parent: iac-comparisons
        weight: 32
---

A service catalog answers what exists and who owns it, giving developers a self-service front door for requesting new services. Infrastructure as code decides what actually gets created in the cloud and under which rules. Those are separate layers, and governance only holds where the cloud APIs actually get called.

[Backstage](https://backstage.io/), [Port](https://www.getport.io/), and [Cortex](https://www.cortex.io/) are service catalogs (sometimes called internal developer portals). They index every service, its owner, its documentation, and its health, and most add a self-service layer on top: templates or actions that let a developer request a new service without filing a ticket. That self-service layer usually hands off to something else to do the actual provisioning: a Terraform module, a CI/CD pipeline, a webhook to another system. This page is about that hand-off, what runs on the far side of the "create new service" button, and why the answer decides where your drift, your policy failures, and your on-call pages actually surface.

## What is Pulumi?

{{< what-is-pulumi >}}

Pulumi is the provisioning layer a catalog's self-service action typically calls, or should call, when a developer clicks "create." [Reusable components](/docs/iac/concepts/components/) are how a platform team packages a golden path (a compliant S3 bucket, a properly tagged Kubernetes namespace, a database with the right backup policy) as a first-class piece of software: versioned, tested, and published like any other package. [Pulumi Policies](/docs/discovery-governance/policy/) enforce the guardrails around it, written in Python, TypeScript, or Open Policy Agent Rego, and they run at the one point that actually touches the cloud API, which is the point where they can still block or fix something before it exists. The [Pulumi Backstage plugin](/docs/idp/integrations/backstage-plugin/) connects that provisioning layer directly to a Backstage catalog, so the catalog's front door and Pulumi's guardrails resolve to a single request, without two separate systems that have to stay in sync on their own.

## What are service catalogs?

A service catalog's core job is tracking ownership and metadata: which team owns which service, what it depends on, where its documentation lives, and how healthy it is right now. Backstage's own docs describe its catalog as "a centralized system that keeps track of ownership and metadata for all the software in your ecosystem." Cortex adds Scorecards on top of that same catalog data, scoring services against standards teams define. Port and Cortex both frame themselves as broader engineering platforms now (Port calls itself a developer platform, Cortex an "Engineering Operations Platform"), but the catalog, ownership, and health-tracking core is the same across all three.

The self-service layer sits beside the catalog, outside your cloud account. Backstage's Scaffolder ships [built-in actions](https://backstage.io/docs/features/software-templates/builtin-actions/) for fetching template content, registering the result in the catalog, and creating and publishing a git repository. That reference lists no built-in action that provisions cloud infrastructure; template authors wire that up themselves, commonly by generating Terraform and handing it to a CI/CD pipeline to apply, which is the pattern [CNCF's own walkthrough documents](https://www.cncf.io/blog/2024/01/29/creating-infra-using-backstage-templates-terraform-and-github-actions/). Backstage remains a CNCF Incubating project (accepted to the CNCF Sandbox in September 2020, moved to Incubating in March 2022), and the Terraform- and Pulumi-provisioning plugins in its ecosystem today, such as [the community Terraform plugin](https://github.com/joatmon08/backstage-plugin-terraform), are listed in the [Backstage plugin directory](https://backstage.io/plugins) as third-party additions rather than shipped as part of the core Backstage project.

Port's self-service actions declare an `invocationMethod`: a backend the action dispatches to, which can be a webhook to GitHub Actions, GitLab, Jenkins, or Azure DevOps, or Port's own execution agent. Port documents a pattern for wiring that webhook to a Terraform run for no-code provisioning, which is the same shape as Backstage's: the catalog's UI collects the request, and something you configure separately turns it into cloud resources. Cortex's Workflows are similar in kind: an automated, multi-step process with "integration blocks" that connect out to tools like GitHub, PagerDuty, ServiceNow, and Slack. We found no Cortex documentation claiming a built-in cloud-provisioning engine; Workflows orchestrate steps and hand off to whatever system on the other end actually does the work.

HashiCorp's Waypoint took a related, narrower approach aimed at build and deploy rather than a full catalog: a common abstraction over how an application gets built, deployed, and released. The open-source Waypoint Community Edition was archived in January 2024 and is no longer maintained. HCP Waypoint, HashiCorp's managed successor, still exists as a documented product, layered on top of no-code modules running on HCP Terraform, which puts it in roughly the same position as the catalogs above: a workflow and UI layer that hands the actual provisioning to Terraform underneath.

## Detailed comparison

| Feature | Software catalogs (Backstage, Port, Cortex) | Pulumi |
| --- | --- | --- |
| Core job | Index ownership, metadata, and health for every service; give developers a self-service front door | Author and provision the cloud resources a service actually runs on |
| Provisioning ownership | Delegated: a template, webhook, or workflow step hands off to Terraform, a pipeline, or another tool you configure | Native: Pulumi programs call cloud provider APIs directly, in Python, TypeScript, Go, C#, Java, or YAML |
| Guardrail enforcement point | In the catalog's UI or workflow config, before the hand-off; whatever runs after that point isn't inspected by the catalog | [At the API call itself](/docs/discovery-governance/policy/), via Pulumi Policies evaluated on every preview and update |
| Drift risk | The catalog's record of a service can go stale the moment infrastructure changes outside its templates or workflows | [`pulumi refresh`](/docs/iac/cli/commands/pulumi_refresh/) and scheduled drift detection compare actual cloud state to the program that's supposed to own it |
| Time to self-service | Fast for the catalog request itself; the underlying provisioning step is only as fast, tested, and safe as whatever the template author wired up | Fast and consistent, because the "create" button and the tested, versioned component are the same artifact |
| What the "create" button runs | A template, script, or webhook payload you write and maintain outside the catalog's own guarantees | A [versioned, tested component](/docs/iac/concepts/components/) published like any other package, with `pulumi preview` run before anything changes |
| Ownership of the service record | The catalog: name, team, dependencies, documentation, health | Pulumi: what's actually running, its configuration, and its full change history |

## Key differences

### The catalog is a front door; the execution engine sits elsewhere

None of the three catalogs above claim to be a provisioning engine. That's a fair design choice: a catalog's job is discoverability and ownership, and it does that well. The gap shows up when a platform team assumes the catalog's guardrails (the fields on a template form, the approvals on a workflow step) are the same as guardrails on the infrastructure itself. They aren't. A developer who bypasses the catalog and runs `terraform apply` by hand, or a script that calls a provider API directly, produces infrastructure the catalog never sees and never governs.

### Policy has to run where the API call happens

A guardrail written into a Backstage template field, a Port action form, or a Cortex workflow step only fires when someone uses that specific path. [Pulumi Policies](/docs/discovery-governance/policy/) run inside the same `pulumi preview` and `pulumi up` that create the resource, so the check applies no matter which catalog, script, or CI job kicked off the run, and a violation blocks the change before it reaches the cloud rather than getting flagged in a dashboard afterward.

### Reuse means something different at each layer

A catalog template is reused as a starting point: developers copy it and diverge. A [Pulumi component](/docs/iac/concepts/components/) is reused as a dependency: developers consume it as a versioned package, and a fix or a new compliance requirement in the component ships to every consumer through a version bump, the same way a library update does. That difference compounds as an organization's service count grows.

### The two layers are not mutually exclusive

Adopting Pulumi doesn't require giving up a catalog, and adopting a catalog doesn't require giving up governed provisioning. The [Pulumi Backstage plugin](/docs/idp/integrations/backstage-plugin/) puts Pulumi stacks, resources, and deployment status directly into a Backstage catalog entry, and a Backstage Scaffolder template can call a Pulumi component the same way it might currently call a Terraform module or a shell script. The catalog stays the front door; Pulumi becomes what actually runs behind it.

## When to use Pulumi or a service catalog

Reach for a catalog like Backstage, Port, or Cortex when the immediate problem is that engineers can't find who owns what, documentation is scattered, or there's no single place to see a service's health. That's a real, common problem, and none of these tools need Pulumi to solve it.

Reach for Pulumi when the problem is upstream of the catalog: infrastructure changes that bypass review, policy that only exists as a form field, or a "create service" button whose underlying Terraform or script has drifted from what a template author wrote a year ago. Most platform teams end up running both: a catalog for discovery and self-service requests, and Pulumi as the provisioning and policy layer the catalog's templates or workflows call into.

## Adoption

A catalog and Pulumi coexist most cleanly when the catalog's self-service action is a thin wrapper around a Pulumi component rather than a Terraform module or ad hoc script. Teams already running Backstage typically start with the [Pulumi Backstage plugin](/docs/idp/integrations/backstage-plugin/) to surface existing Pulumi stacks in the catalog, then migrate templates one at a time to call Pulumi components instead of whatever provisioned them before. Teams building their self-service layer from scratch can follow [golden paths built from reusable components and templates](/blog/golden-paths-infrastructure-components-and-templates/) and plug the resulting components into whichever catalog's UI they've standardized on.

## Frequently asked questions

### Is Pulumi a service catalog?

No. Pulumi is an infrastructure as code platform that authors and provisions cloud resources. It has no built-in catalog UI for browsing services by owner or health, though the [Pulumi Backstage plugin](/docs/idp/integrations/backstage-plugin/) surfaces Pulumi stacks inside a Backstage catalog.

### Can I use Pulumi with Backstage, Port, or Cortex?

Yes. All three catalogs support wiring a self-service action to any backend you can call from a webhook, a CI job, or a plugin, which includes a Pulumi program or component. The [Pulumi Backstage plugin](/docs/idp/integrations/backstage-plugin/) is the most direct integration path today.

### Who should enforce policy, the catalog or the provisioning layer?

The provisioning layer, because it's the only layer that sees every change regardless of which catalog, script, or pipeline initiated it. [Pulumi Policies](/docs/discovery-governance/policy/) evaluate every `pulumi preview` and `pulumi up`, so a rule holds even for infrastructure changes that never went through a catalog's template at all.

### Does adopting Pulumi mean giving up my existing catalog?

No. Pulumi replaces or governs the provisioning behind a catalog's self-service actions; it doesn't replace the catalog's ownership, documentation, or health tracking. Most teams keep their catalog and change what runs behind its "create" button.

### Does a catalog's self-service action actually provision cloud resources?

Usually not by itself. Backstage's Scaffolder, Port's actions, and Cortex's Workflows all dispatch to a backend you configure, commonly Terraform run through a pipeline. The catalog collects the request and tracks the result; something else does the provisioning.

## Next steps

- [Get started with Pulumi](/docs/get-started/)
- [Pulumi Backstage plugin](/docs/idp/integrations/backstage-plugin/)
- [Reusable components](/docs/iac/concepts/components/)
- [Pulumi Policies](/docs/discovery-governance/policy/)
- [What is an Internal Developer Platform?](/what-is/what-is-an-internal-developer-platform/)
- [Golden paths: infrastructure components and templates](/blog/golden-paths-infrastructure-components-and-templates/)
- [Pulumi vs. Backstage: why infrastructure-first platform engineering matters](/blog/backstage-vs-pulumi-idp-why-infrastructure-first-platform-engineering-matters/)
