# Linear tracking issue reference — Marketing team

Contents: where it lives · find before you create · title and fields · description blueprint · promotion sub-issues · form IDs · Deliverables intake · lifecycle updates · going live · Notion schedule row · Luma (optional) · tool access and fallbacks.

Every Pulumi-hosted workshop or webinar is tracked by a **parent issue in Linear** with a promotion checklist as sub-issues. That issue replaces the old GitHub tracking issue in `pulumi/marketing`, which this skill no longer creates. The reference blueprint is [MA-1045](https://linear.app/pulumi/issue/MA-1045/2026-10-22-give-your-coding-agent-an-elastic-memory-engin); copy its shape rather than inventing a new one.

## Where it lives

| Field | Value |
|---|---|
| Team | `Marketing` (identifier prefix `MA-`) |
| Project | The quarter's workshop project, named `Workshops (Q<n> <yy>)` — for example `Workshops (Q4 26)` for an event in October–December 2026. Pick the quarter of the **event date**, not today. Find it with `list_projects` (team `Marketing`, query `Workshops`). If that quarter's project doesn't exist yet, don't create one: ask in interactive mode, otherwise file into no project and flag it in the report. |
| Label | `Workshop` (also used for webinars and livestreams) |
| Due date | The event date (the earliest session for multi-session events) |
| Status | `In Progress` once the docs work starts |
| Assignee | Leave as is on an existing issue; on a new one, the person running the skill |

## Find before you create

Most parent issues **already exist**: they're synced from the Notion **Workshops & Webinars Schedule**, and the description says so in its first line. Notion is the source of truth for the title, date, and presenter, so:

1. A Linear URL or identifier in the input (`MA-1045`, `https://linear.app/pulumi/issue/MA-1045/...`) → `get_issue` and prefill from it.
1. Otherwise search: `list_issues` with team `Marketing`, the quarter's project, and a `query` of distinctive title words. A match is the tracking issue — offer it rather than creating a duplicate.
1. Create a new parent issue only when nothing matches, and say in the report that it isn't backed by a Notion row yet.

On a Notion-synced issue, **never rewrite the title, date, or presenter** to match the spec. If they disagree, use the issue's values when they're clearly newer, otherwise stop and ask (interactive) or flag the mismatch (unattended). You may fill fields the issue marks `TBD`, such as the meta description or the learn bullets.

Older events (before Q4 2026) were tracked in GitHub (`pulumi/marketing#<n>`, for example #1688). A `pulumi/marketing` issue URL is still accepted as **read-only** prefill for update mode. Never create new GitHub issues there.

## Title and fields

- **Title**: `[YYYY-MM-DD] <Session Title> (<presenter first names>)`. There's no colon after the date bracket. Several presenters are comma-separated (`(Adam, Engin, Mike Coleman)`); a multi-session event lists every date (`[2026-09-16 + 2026-10-14]`). The Linear title keeps Notion's capitalization even though the event page uses sentence case.
- **Labels**: `Workshop`. Add `needs-design` only when a designer-made card was requested.

## Description blueprint

Keep every heading, even when its content is `TBD`. The section text is the same set of strings as the event page; write them once and use them in both places.

```markdown
## Theme

<AI | IaC | Platform Engineering | Security | TF-Takeover>

## Workshop Description

**Session Title**: <title, ≤ 60 chars>

**Meta Description**: <50–160 chars, or *(TBD, 50–160 chars)*>

**Abstract**: <1–2 paragraphs>

**Join us to learn**:

* <outcome>
* <outcome>
* <outcome>

## Delivery Date and Time

YYYY-MM-DD, H:MM AM/PM TZ (Day)

## Duration

60 minutes

## Presenters

<Name, Company> — new presenters also get title, X handle, and LinkedIn when known

## Tags

level: <Beginner | Intermediate | Advanced>
topics: <same vocabulary as the event page>
languages:
clouds:

## HubSpot Segmentation

Interest: Topics - <topic>

## Funnel

Top of Funnel Promo: <checked | not checked (mid-funnel)>. Confirm in the bi-weekly Workshop planning call.
```

A Notion-synced issue starts with an italic "*Synced from the Notion …*" line and may carry a short context paragraph after it (for example, a pointer to the talk it's based on). Leave both alone.

## Promotion sub-issues

The checklist lives in sub-issues, one per task, not as a markdown task list. Marketing (usually Calon Alpar) creates them from a template when the Notion row is approved, so on an existing parent they are normally all there already. When you **create** a parent, also create any of these that are missing, under it, in this order. Each gets the parent's project and the event date as its due date, except "After event/workshop emails", which gets no due date. Leave them unassigned (marketing assigns owners), except Deliverables, which goes to the workshop owner (the parent's assignee).

1. HubSpot form and Lists
1. SF campaign with a theme as parent campaign
1. Workshop link on /events page
1. Riverside invite w/ presenter links
1. SDR routing
1. Social organic promotion
1. Social paid promotion
1. Targeted emails
1. After event/workshop emails
1. Deliverables (the invite-audience intake; see §Deliverables intake)

Parents created before Q4 2026 may still carry "Pulumi Cloud organization and invites". Leave it alone; don't create it on new parents. Copy the Deliverables description from the newest Deliverables sub-issue in the same project rather than writing your own, because its intake template changes.

`/resources` now 301-redirects to `/events/`, so older parents still have a sub-issue titled "Workshop link on /resources page". Rename it to "Workshop link on /events page" when you touch that event. List sub-issues with `list_issues` and `parentId` set; never create a second copy of one that exists.

## Form IDs

`form.hubspot_form_id` (UUID) and `form.salesforce_campaign_id` (`701…`, 18 chars) are created by marketing while working the "HubSpot form and Lists" and "SF campaign …" sub-issues. They come back in any of three places. Check all of them, newest first:

1. Comments or the description on those two sub-issues.
1. Comments on the parent issue.
1. A review suggestion on the docs PR from a marketing reviewer. On pulumi/docs#22205, for example, a reviewer posted both IDs as a one-click `suggestion` block.

Extraction: HubSpot `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` · Salesforce `\b701[A-Za-z0-9]{15}\b`. Prefer values a comment labels explicitly ("form id", "campaign"); otherwise take the most recent match. Never invent IDs. Until they land, a gated page ships with empty strings and a `# TODO: wire in from <MA-n> …` comment.

## Deliverables intake

The "Deliverables" sub-issue is an intake form that the **workshop owner** fills in. Marketing builds the HubSpot invite list and the invite emails from it, and nothing starts until the owner posts the `Ready to build` comment. Skipping it means no invite email goes out, so treat it as part of creating the event, not an optional extra.

The form has two parts. Fill every section; leave a section blank only when it really shouldn't filter anyone.

| Section | How to fill it |
|---|---|
| Function | Check the boxes that match the event's audience. Most technical workshops: Engineering / Platform / DevOps, plus Architecture. Add Security for a Security-theme event |
| Seniority | Practitioner. Add Executive buyer when the abstract promises something a lead takes back to the team (a checklist, a rollout plan) |
| Product usage | One or two sentences in your own words naming the Pulumi products the abstract relies on (ESC, Neo, the Kubernetes provider, Deployments, the MCP server). End with "Matching any one of these is enough." |
| Engagement signal | GitHub activity and Docs / AI pages visited by default. Add Attended a prior workshop for an Intermediate or Advanced event |
| Who to include | Prospects, Free self-serve, Self-serve customers. Leave Sales-led customers unchecked unless the user asks |
| Email guidance | Lead with the problem the abstract opens with, then the two or three things the demo shows. Name any partner and co-presenter. Give the CTA (`Save your spot`) with the event page's `#register` URL. If the title is over ~50 chars, suggest a shorter subject line |
| Send timing | Invite 1 about two weeks before the event (move it earlier to dodge a holiday or a big conference week), Invite 2 on the Tuesday of the week before, to non-registrants only. Give real dates |

Use the newest filled-in Deliverables sub-issue in the same project as the style reference (for example MA-1157). Edit the description with a `patch` that checks the boxes (`- [ ]` → `- [x]`) and inserts the text after each section's italic example line, so the template stays intact.

Then post the comment the form asks for. Copy the mention line from the form's own **Ready to build?** section (today `Ready to build @calon`), because the builder can change. Put the event page's state on the next line, and **check it before you write it** (§Going live, step 1): either the live `#register` URL, or "the page isn't live yet; it goes live when <PR link> merges". The mention sends a notification, so a wrong claim can't be quietly fixed later.

- Interactive: show the drafted intake and ask before posting the comment.
- `-y`: fill it and post the comment; the flag is the standing go-ahead.
- Dry-run or no Linear tools: write the filled sections and the comment to `linear-preview.md`.
- Already filled, or a `Ready to build` comment already exists: leave it alone, and report what's there.

## Lifecycle updates

The tracking issue is the team's view of progress, so keep it current at each milestone. Comment on the parent with what changed and why, rather than silently editing.

| Milestone | Update |
|---|---|
| Docs PR opened | Attach the PR as a link (`save_issue` `links`). Fill `TBD` fields the page settled (meta description, level, languages) with a `patch`, not a full rewrite. Comment with the PR link, whether it's a draft, and the form-ID state. |
| Form IDs wired in | Comment with both IDs and the commit. |
| Review cleared or approved | Comment with the review outcome and what's left before merge. |
| Deliverables filled | The intake is filled and the `Ready to build` comment is posted (§Deliverables intake). |
| Form IDs pending | If the "HubSpot form and Lists" sub-issue has an assignee and no IDs yet, comment there mentioning them, with the PR link, so they know the page is waiting on the form. |
| Page live | Run §Going live. |
| Luma created or made public | Attach the Luma link; comment on its visibility and whether it has a meeting URL. |

## Going live

Run this when the docs PR has merged: on a rerun of `/create-event <MA-n>` in update mode, with `--go-live`, or when the user says the page is live. Every step is idempotent, so skip the ones that are already done.

1. **Check, don't assume.** `gh pr view <n> --json state,mergedAt` must say `MERGED`, `https://www.pulumi.com/events/<slug>/` must return 200, and for a gated page the HTML must contain the `hubspot_form_id`. If any check fails, stop and report which one; nothing below runs.
1. **Luma**: if the event is `private`, switch it to `public` (`luma_update_event` with `visibility: public`). Interactive runs confirm first. If the Linear parent's Luma attachment title names the old visibility ("… (private)"), re-attach the same URL with the new title.
1. **Notion**: set the schedule row's `Live?` to `Yes` and update its links (§Notion schedule row).
1. **"Workshop link on /events page"**: mark it `Done`, attach the live URL as a link, and comment with the URL and the Luma link.
1. **"HubSpot form and Lists" and "SF campaign …"**: mark each `Done` when the live page carries its ID, with a one-line comment naming the ID. Leave them open if the page doesn't have the ID.
1. **Deliverables**: if no comment there already says the page is live, comment with the `#register` URL so the invite can link to it.
1. **Parent**: one comment summarizing what went live (page, Luma) and what's still open on the sub-issues.

## Notion schedule row

Every workshop has a row in the Notion **Workshops & Webinars Schedule** data source (`collection://69b62db4-cf6f-4d9a-af7f-450a9fd31378`). The Linear parent is synced from it, so it is the source of truth for the title, date, time, and presenter. Find it with `notion-search` on the title, restricted to that data source, and match the `Idea ID` to the slug when it's set.

- **Never change** `Title`, `Date`, `Day`, `Time`, `Presenter`, `Stage`, or `Source`. Those belong to the planning call.
- When the PR opens, you may set an empty `Idea ID` to the slug and add or refresh a short **Tracking and links** section in the page body: the Linear parent, the PR, and the Luma event with its visibility. Update the lines that are there rather than adding a second section.
- At go-live, set `Live?` to `Yes` and update the same lines: the live event URL instead of "draft", and Luma's new visibility.
- Dry-run or no Notion tools: put the intended edits in `linear-preview.md`.

## Luma (optional)

## Luma (optional)

Create a Luma event only when the user asks. Use the `pulumi-events` MCP server (`luma_create_event`):

- **Check for a duplicate first, properly.** `luma_list_events` returns the oldest events first, so a capped `limit` (such as 30) misses recent ones. Call it with no `limit` and match on the name and the start date. Also look for a Luma link already attached to the Linear parent or on the Notion row; that's the fastest way to find the event.
- Set `visibility: private` until the event page is live, then switch it to `public` at go-live (§Going live).
- Attach the Luma URL to the Linear parent as soon as the event exists, so later runs can find it without a search.
- Name it with the Linear title's capitalization, without the date or presenter.
- Use the event's timezone, and convert `start_at`/`end_at` to UTC.
- For the description, use the abstract and learn bullets plus a `**Presenter:**` line.
- The cover is the 1080×1080 card (`meta-square-large.png`). The server can't read local files, so push the bundle first and pass the `raw.githubusercontent.com/pulumi/docs/<commit-sha>/…` URL as `cover_image_url`.
- Leave `meeting_url` empty unless the user gives one or the Riverside sub-issue has the studio link.

## Tool access and fallbacks

Linear writes go through the Linear MCP tools (`get_issue`, `list_issues`, `list_projects`, `list_comments`, `save_issue`, `save_comment`). They aren't available everywhere: CI runs and `claude -p` usually lack the connector.

- **Dry-run**: no Linear or Luma writes. Write the exact would-be changes to `.context/create-event/<slug>/linear-preview.md`. That covers the title, every field, the full description, the sub-issues to create, and each update and comment, plus the tool call you would make for each.
- **Tools unavailable on a real run**: finish everything local and in GitHub. Then write the same `linear-preview.md` and tell the user plainly that Linear wasn't updated, so they (or an interactive session) can apply it.
- Reads that fail (issue not found, no access) are not fatal. Continue with the spec as given and flag it.
