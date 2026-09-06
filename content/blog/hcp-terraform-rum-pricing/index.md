---
title: "HCP Terraform RUM pricing: what to model before renewal"
date: 2026-09-06
meta_desc: "HCP Terraform now bills on Resources Under Management (RUM): an hourly-peak meter on every managed resource in state. Here's what to model before you renew."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - terraform
    - pricing
    - platform-engineering
category: best-practices
related_posts:
    - pulumi-neo-security

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        HCP Terraform bills on Resources Under Management now: a peak-per-hour meter across every managed resource in your state.

        Here's what actually counts, how the meter reads a replacement, and how to count your own RUM before renewal.
    linkedin: |
        HCP Terraform's pricing model changed from per-seat to Resources Under Management (RUM), and the vendor's own docs are thin on the mechanics that determine your bill.

        A few things worth knowing before a renewal conversation: RUM only counts resources where mode = "managed" in state (null_resource and terraform_data resources are excluded, even though local-only resources like random_id are not). The meter reads the peak concurrent count in each clock hour, not a monthly average, and a partial hour still bills as a full hour. A blue/green cutover or a resource replacement can double your hourly count for the hour it happens, because the old and new resources both exist briefly.

        We wrote up the definition, the metering mechanics, the current tier rates, and two jq/API one-liners to count your own RUM before you're staring at a renewal number you didn't expect.
    bluesky: |
        HCP Terraform bills on Resources Under Management now: a peak-per-hour meter across every managed resource in state.

        Here's what counts, how the meter reads a replacement, and how to count your own RUM before renewal.
---

HCP Terraform's Resources Under Management (RUM) is a metered count of every resource with `mode = "managed"` in your state files, and HashiCorp bills it on the peak count observed in each clock hour, not a monthly average. That single design choice, peak-per-hour rather than average, is why two teams with the same resource count can see very different bills, and it's the part most pricing writeups skip.

HashiCorp [moved HCP Terraform off per-seat pricing and onto RUM in 2023](https://www.pulumi.com/docs/iac/comparisons/terraform-cloud/), and retired the legacy free plan on March 31, 2026. Pulumi's own [HCP Terraform comparison page](https://www.pulumi.com/docs/iac/comparisons/terraform-cloud/) covers why teams are re-evaluating HCP Terraform as a result. This post covers what that comparison page doesn't: what actually counts as a billable resource, how the hourly meter reads your infrastructure, what the current tiers cost, and how to count your own number before a renewal conversation.

## What counts as a resource under management?

A managed resource, per [HashiCorp's own definition](https://developer.hashicorp.com/terraform/cloud-docs/overview), is any resource in an HCP Terraform-managed state file where `mode = "managed"`, counted from the first `terraform plan` or `terraform apply` that touches it. Both workspace and Stacks resources count toward the same total.

Three kinds of resource roll up into the same number, whether they come from a `count` or `for_each` block, a module, or a plain `resource` block:

- Resources provisioned directly by a Terraform provider, such as an AWS VPC or an Azure resource group.
- Resources created through `count` and `for_each` meta-arguments — each instance counts separately.
- Resources provisioned by modules and no-code-ready modules — the resources they create count, not the module call itself.

Three categories do not count, and one of them is easy to get backwards:

- `null_resource` and `terraform_data` resources are explicitly excluded, even though they carry `mode = "managed"` in state.
- Data sources, anything with `mode = "data"`, are excluded.
- Local values and variables never count; they aren't resources at all.

The one nuance worth sitting with: a "local only" resource with no remote object behind it, `random_id` or `random_password` for example, still counts toward RUM, because it's a managed resource in state. If your estate leans on `null_resource` blocks for provisioning glue, as many older Terraform Enterprise migrations do, your actual billable count is lower than a naive `terraform state list` count would suggest.

## How the meter reads your infrastructure: peak per hour, not average per month

HashiCorp charges [per managed resource, per hour, from provisioning to destruction](https://developer.hashicorp.com/terraform/cloud-docs/overview), and **each partial hour bills as a full hour**. The number that determines an hour's cost is the peak count of managed resources observed during that hour, aggregated across every HCP Terraform organization under one HCP account.

HashiCorp's own worked example makes the practical effect clear. Take an Essentials-plan organization running a three-hour operation:

1. **Hour one:** 1,000 resources exist, no changes. Cost: $0.14.
2. **Hour two:** 1,000 new resources are added, 500 are changed in place, and 500 are destroyed, for a peak of 2,000 resources observed at some point in that hour. Cost: $0.27. Running total: $0.41.
3. **Hour three:** No further changes. Peak count settles to 1,500. Cost: $0.20. Running total: $0.61.

Notice hour two: the peak, not the net change, is what bills. A resource replacement, the kind Terraform performs whenever a change forces a destroy-and-recreate rather than an update in place, briefly holds both the old and the new resource in state at once. So does a blue/green environment cutover, or a preview environment spun up alongside the environment it's testing against. None of that shows up in a static "how many resources do I have" count; it only shows up in the hourly peak, which is exactly the number that bills.

## What the tiers cost right now

HCP Terraform currently runs four plans: Free, Essentials, Standard, and Premium. Free caps at 500 managed resources and charges nothing. Essentials, Standard, and Premium bill pay-as-you-go per managed resource per hour, and are also available under HashiCorp Flex, a committed-usage plan with volume discounts negotiated per account.

HashiCorp's own docs point to [HashiCorp's IBM-hosted price list](https://www.ibm.com/products/hashicorp/pricing) for the Essentials rate and route Standard and Premium to sales for a quote; that price list happens to publish hourly rates for all three tiers, so we're citing it here alongside the docs.

| Plan | Rate per resource-hour | Approx. per resource-month (720 hrs) |
|---|---|---|
| Free | $0 (up to 500 resources) | $0 |
| Essentials | $0.0001359 | $0.098 |
| Standard | $0.00064 | $0.461 |
| Premium | $0.00135 | $0.972 |

Rates as read from IBM's published HashiCorp price list on 2026-09-06; HashiCorp's own worked example (which yields $97.85/month for 1,000 resources at the Essentials rate) corroborates the Essentials figure directly. The monthly column is our own arithmetic, at HashiCorp's own 720-hour (30-day) convention from its worked example, applied to a resource that exists continuously all month. You may see a $0.99/month figure elsewhere for Premium; that comes from a 730-hour average-month convention, not HashiCorp's own 720-hour worked example, which is what we use throughout. Real bills track actual hourly peaks, so treat the monthly figures as a planning estimate, not a quote.

At scale, the arithmetic compounds the way any per-unit metric does:

| Managed resources | Essentials/mo | Standard/mo | Premium/mo |
|---|---|---|---|
| 1,000 | $98 | $461 | $972 |
| 5,000 | $489 | $2,304 | $4,860 |
| 20,000 | $1,957 | $9,216 | $19,440 |

Standard and Premium also carry concurrency add-ons, Remote Concurrency and Agent Concurrency, priced per concurrent run-hour on top of the per-resource charge; see IBM's price list for current rates, since HashiCorp's own docs route this pricing to sales.

## How to count your own RUM before a renewal conversation

None of the above matters until you know your own number, and the honest way to get it is to count directly rather than guess from a dashboard snapshot.

For a single workspace, from a local state file:

```bash
terraform state list | grep -vE '(^|\.)data\.' | grep -v 'null_resource\.' | wc -l
```

That excludes data sources and `null_resource` addresses, but it won't catch `terraform_data` resources by name alone, and it treats every `count`/`for_each` instance as one line, which matches how RUM counts them. For a precise count that also excludes `terraform_data` by its actual attributes rather than a naming guess, pull the JSON state and filter on `mode` and `type` directly:

```bash
terraform show -json > /tmp/state.json
jq '[.. | objects
      | select(.mode? == "managed")
      | select(.type? != "null_resource" and .type? != "terraform_data")
      | .address] | length' /tmp/state.json
```

Across every workspace in an org, the HCP Terraform API exposes a `resource-count` attribute per workspace, so you can sum it without opening each workspace in the UI:

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN" \
  "https://app.terraform.io/api/v2/organizations/$ORG/workspaces?page%5Bsize%5D=100" \
| jq '[.data[].attributes["resource-count"]] | add'
```

Three caveats worth keeping in mind before you trust any of these numbers in a renewal conversation. The API call above paginates at 100 workspaces per page, so an org with more than that needs to walk pages and sum across them. RUM is aggregated across every HCP Terraform organization under one HCP account, so a single org's total understates the bill if your estate spans more than one org. And every command here returns a point-in-time snapshot, while the meter that actually bills you is the peak observed within each hour, so the true number during a busy deploy window will run higher than whatever you counted at rest.

## Where estimates go wrong

The gap between "resources I think I have" and "resources HashiCorp bills for" tends to open in three specific places.

**Preview and ephemeral environments.** Every environment spun up per pull request, and left running even briefly alongside the environment it's testing against, adds its full resource count to that hour's peak. A team running ten preview environments of 50 resources each is carrying 500 extra resources in every hour those environments exist, on top of whatever's permanent.

**Replacements, not just growth.** As the worked example above shows, a resource replacement (destroy-and-recreate, not update-in-place) briefly doubles that resource's contribution to the hourly peak. A migration or a cutover that replaces a large chunk of an estate in one operation can spike a single hour's bill well above what the estate's steady-state count would suggest, even though nothing about the estate actually grew.

**Module fan-out is not a lever.** It's tempting to assume that consolidating a sprawl of small modules into fewer, larger ones would reduce a bill built on a per-resource meter. It won't. RUM counts the resources a module provisions, not how many times the module itself is called or how it's organized. Reorganizing modules changes how the code reads; it does nothing to the number HashiCorp bills.

## What happens when you cross the free tier

The Free plan covers up to 500 managed resources at no charge. Above that, an organization moves onto Essentials, Standard, or Premium, and paid plans carry no free allowance of their own, so the full managed-resource count bills rather than only the resources past 500. Since HashiCorp retired the legacy user-based Free plan on March 31, 2026, organizations still on it were migrated automatically to the enhanced Free tier, which is the 500-resource cap described above. If your organization was on the older plan, that's a change worth confirming before you assume your current usage still fits inside it.

## Modeling growth before a renewal

The RUM model rewards a specific kind of forecasting: not "how many resources do we have today," but "what's the trajectory, and what's the peak we'll actually hit." A workable method:

1. Pull your current billable count with the commands above, separately for steady-state infrastructure and anything ephemeral (previews, short-lived test environments).
2. Estimate growth over the renewal term from your last two to three quarters of net resource change, not from headcount or team size, since RUM doesn't track either.
3. Add a peak allowance on top of steady-state growth for known-recurring events: migrations, blue/green cutovers, and the busiest month of preview-environment activity in your history.
4. Run that projected peak through the plan's rate to get a range, not a point estimate, and compare it against the tier and any Flex commitment discount your HashiCorp account team offers at that volume.

Applied to the table above, an estate growing from 1,000 to 5,000 managed resources over a renewal term on the Standard plan moves from roughly $461 to $2,304 a month, a jump that tracks the estate's growth curve rather than any change in team size. That's the number worth having before the renewal conversation starts, not during it.

## How RUM compares with other control-plane pricing models

RUM is one of several models control-plane vendors use to price infrastructure automation, and it's worth knowing where each one puts the pressure:

| Vendor | Pricing model | What scales the bill |
|---|---|---|
| HCP Terraform | Per managed resource, billed on hourly peak | Estate size and churn |
| Pulumi Cloud | Per resource, billed hourly and prorated, drawn from a shared credit pool | Estate size, prorated to actual existence time |
| Spacelift | Worker concurrency tiers | Parallel run capacity, not resource count |
| Scalr | Per run, with a free monthly run allowance | Deployment frequency, not resource count |
| env0 | Usage-based, per successful apply or per environment after a free run allowance | Deployment frequency and environment count |
| Terrateam | Flat annual plan above a free run allowance | A fixed fee, not usage |

Worth saying plainly: Pulumi Cloud also meters IaC resources per resource-hour, and also bills a partial resource-hour as a full hour, so this isn't a case where one model rounds and the other doesn't. The difference is granularity of the billing unit (resource-hours toward a shared credit pool, rather than a flat monthly per-resource price) and that the same pool also covers configuration and secrets management rather than billing infrastructure resources in isolation.

If a resource-based bill that scales unpredictably with estate size and churn, rather than with the people managing it, is the part of this pricing shift you're trying to get ahead of, the fuller picture, tier-by-tier feature comparison and migration path included, is in Pulumi's [HCP Terraform comparison](https://www.pulumi.com/docs/iac/comparisons/terraform-cloud/).

One more disambiguation worth a sentence: Pulumi's own Cloud REST API separately exposes a metric it also calls "resources under management," describing the count of resources Pulumi Cloud tracks across your stacks. That's a different, Pulumi-specific usage metric; it isn't the HashiCorp billing term this post is about.

## Next steps

Start by counting your own RUM with the commands above, separating steady-state resources from ephemeral ones, and running that number through a renewal-term growth model rather than a snapshot. If the outcome looks like your bill is set to track your estate's growth curve more than your team's, and you want a model that ties cost to actual resource lifetime instead, read the full [Pulumi vs. HCP Terraform comparison](https://www.pulumi.com/docs/iac/comparisons/terraform-cloud/) for the feature-by-feature breakdown and a path to adopt Pulumi Cloud without leaving Terraform behind.
