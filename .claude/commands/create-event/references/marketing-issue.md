# Marketing tracking issue reference — pulumi/marketing

Contents: template routing · fetch-then-fill · title/label/assignee conventions · body sections · form-ID sequencing · gh commands · workshop template snapshot.

Every Pulumi-hosted event gets a tracking issue in `pulumi/marketing` — it drives the marketing checklist (HubSpot form, SF campaign, BigMarker, promotion) and is where the form IDs come back. Example of the finished shape: pulumi/marketing#1688.

## Template routing

| Event | Template file | Labels (from template) |
|---|---|---|
| Pulumi-hosted workshop **or webinar/livestream** | `.github/ISSUE_TEMPLATE/pulumi-workshop.md` | `area/livestream`, `area/workshop` |
| Partner-hosted event | `.github/ISSUE_TEMPLATE/partner-event.md` | `area/partners` |
| Sponsored/conference | `sponsored-event.yml` — out of scope for this skill; point the user at the form | — |

There is no separate webinar template — webinars use the workshop template (it covers any virtual session).

## Fetch, then fill

Always fetch the **live** template so drift never bites:

```bash
gh api repos/pulumi/marketing/contents/.github/ISSUE_TEMPLATE/pulumi-workshop.md --jq '.content' | base64 -d
```

Parse its YAML frontmatter for `labels` and `assignees` (currently `calon-pulumi, isaac-pulumi, SaraDPH` — but trust the fetch, not this sentence). Fill the body sections; keep every section heading even when empty, and keep the `## Tasks` checklist verbatim and unchecked — it's marketing's worksheet, not yours. If the fetch fails (offline), fall back to the snapshot at the bottom, and say so in the report.

## Title, labels, assignees

- **Title**: `[YYYY-MM-DD]: <Session Title> (<presenter first name>)` — the date is the delivery date; the parenthetical matches team practice (see #1688).
- **Labels**: the template's own, plus `kind/task`; plus `needs-design` only when a designer-made card was requested.
- **Assignees**: from the template frontmatter.

## Body sections (workshop template)

- `## Theme` — exactly one of: `AI`, `IaC`, `Platform Engineering`, `Security`, `TF-Takeover`.
- `## Workshop Description` — four labeled parts: **Session Title** (≤ 60 chars), **Meta Description** (50–160 chars), **Abstract** (1–2 paragraphs), **Join us to learn** (3 bullets). These are the same strings as the event page — write once, use in both.
- `## Delivery Date and Time` — `YYYY-MM-DD, H:MM AM/PM TZ`. Workshops are ideally filed ~60 days out (30 for partner events); don't block on less, just note it.
- `## Duration` — `60 minutes` standard, `90 minutes` allowed.
- `## Presenters` — repeat presenters: name only. New presenters: name, title, company, X handle and LinkedIn if available.
- `## Tags` — `level:` / `topics:` / `languages:` / `clouds:` — same case-sensitive vocabulary as the event page filters.
- `## HubSpot Segmentation` — optional property lines; fill only what clearly applies ("When in doubt, do not add").
- `## Tasks` — verbatim from the template, all unchecked.

## Form-ID sequencing (why issue-first matters)

The docs PR wants `form.hubspot_form_id` + `form.salesforce_campaign_id`; marketing creates those **from** the tracking issue and posts them back as a comment. So: file the issue first, ship the page with TODO placeholders if the IDs haven't landed, and wire them in later via update mode. Extraction from comments:

```bash
gh issue view <n> --repo pulumi/marketing --comments
# HubSpot form id: [0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}
# SF campaign id:  \b701[A-Za-z0-9]{15}\b
```

Take the most recent match if several appear; if a comment labels them explicitly ("form id", "campaign"), prefer the labeled values.

## gh commands

```bash
# create (real runs only — dry-run writes issue-preview.md instead)
gh issue create --repo pulumi/marketing \
  --title "[2026-09-24]: Getting Started with Pulumi on AWS (Engin)" \
  --label area/livestream --label area/workshop --label kind/task \
  --assignee calon-pulumi --assignee isaac-pulumi --assignee SaraDPH \
  --body-file .context/create-event/<slug>/issue-body.md

# search for an existing issue before creating
gh issue list --repo pulumi/marketing --search "<title words>" --state all --limit 5
```

## Snapshot: pulumi-workshop.md (fallback only — fetched 2026-08; the live file wins)

```markdown
---
name: Pulumi Workshop
about: Marketing activities for a virtual workshop hosted by Pulumi
title: "[YYYY-MM-DD]: [WORKSHOP_NAME]"
labels: area/livestream, area/workshop
assignees: calon-pulumi, isaac-pulumi, SaraDPH
---

## Theme

## Workshop Description

**Session Title**:

**Meta Description**:

**Abstract**:

**Join us to learn**:
-
-
-

## Delivery Date and Time

## Duration
60 minutes

## Presenters

## Tags

level:
topics:
languages:
clouds:

## HubSpot Segmentation

Interest: Topics -
Interest: Infrastructure Type -
Interest: Cloud Provider -
Interest: Competitive Set -
Interest: Programming Languages -
Preferred Programming Language -

## Tasks

- [ ] Workshop details (Date/time, Title, Abstracts, Agenda, Presenters)
- [ ] HubSpot form and Lists
- [ ] SF campaign with a theme as parent campaign
- [ ] Workshop Link on /resources page
- [ ] BigMarker Invite w/presenter links
- [ ] SDR routing
- [ ] Social Organic promotion
- [ ] Social Paid promotion
- [ ] Pulumi Cloud organization and invites
- [ ] Targeted emails
- [ ] After event/workshop emails
```
