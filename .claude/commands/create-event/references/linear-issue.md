# Linear tracking issue reference — Marketing team

Contents: where it lives · find before you create · title and fields · description blueprint · promotion sub-issues · form IDs · lifecycle updates · Luma (optional) · tool access and fallbacks.

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

The checklist lives in sub-issues, one per task, not as a markdown task list. When you **create** a parent, also create any of these that are missing, under it, in this order. Each gets the parent's project and the event date as its due date, except "After event/workshop emails", which gets no due date. Leave them unassigned; marketing assigns owners.

1. HubSpot form and Lists
1. SF campaign with a theme as parent campaign
1. Workshop link on /events page
1. Riverside invite w/ presenter links
1. SDR routing
1. Social organic promotion
1. Social paid promotion
1. Pulumi Cloud organization and invites
1. Targeted emails
1. After event/workshop emails

`/resources` now 301-redirects to `/events/`, so older parents still have a sub-issue titled "Workshop link on /resources page". Rename it to "Workshop link on /events page" when you touch that event. List sub-issues with `list_issues` and `parentId` set; never create a second copy of one that exists.

## Form IDs

`form.hubspot_form_id` (UUID) and `form.salesforce_campaign_id` (`701…`, 18 chars) are created by marketing while working the "HubSpot form and Lists" and "SF campaign …" sub-issues. They come back in any of three places. Check all of them, newest first:

1. Comments or the description on those two sub-issues.
1. Comments on the parent issue.
1. A review suggestion on the docs PR from a marketing reviewer. On pulumi/docs#22205, for example, a reviewer posted both IDs as a one-click `suggestion` block.

Extraction: HubSpot `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` · Salesforce `\b701[A-Za-z0-9]{15}\b`. Prefer values a comment labels explicitly ("form id", "campaign"); otherwise take the most recent match. Never invent IDs. Until they land, a gated page ships with empty strings and a `# TODO: wire in from <MA-n> …` comment.

## Lifecycle updates

The tracking issue is the team's view of progress, so keep it current at each milestone. Comment on the parent with what changed and why, rather than silently editing.

| Milestone | Update |
|---|---|
| Docs PR opened | Attach the PR as a link (`save_issue` `links`). Fill `TBD` fields the page settled (meta description, level, languages) with a `patch`, not a full rewrite. Comment with the PR link, whether it's a draft, and the form-ID state. |
| Form IDs wired in | Comment with both IDs and the commit. |
| Review cleared or approved | Comment with the review outcome and what's left before merge. |
| Page live | Confirm `https://www.pulumi.com/events/<slug>/` returns 200 and is linked from `/events/`. Then mark "Workshop link on /events page" `Done` with a comment that carries the live URL. |
| Luma created or made public | Attach the Luma link; comment on its visibility and whether it has a meeting URL. |

## Luma (optional)

Create a Luma event only when the user asks. Use the `pulumi-events` MCP server (`luma_create_event`):

- Check `luma_list_events` for a duplicate first.
- Set `visibility: private` until the event page is live, then switch it to `public` when the user asks (`luma_update_event`).
- Name it with the Linear title's capitalization, without the date or presenter.
- Use the event's timezone, and convert `start_at`/`end_at` to UTC.
- For the description, use the abstract and learn bullets plus a `**Presenter:**` line.
- The cover is the 1080×1080 card (`meta-square-large.png`). The server can't read local files, so push the bundle first and pass the `raw.githubusercontent.com/pulumi/docs/<commit-sha>/…` URL as `cover_image_url`.
- Leave `meeting_url` empty unless the user gives one.

## Tool access and fallbacks

Linear writes go through the Linear MCP tools (`get_issue`, `list_issues`, `list_projects`, `list_comments`, `save_issue`, `save_comment`). They aren't available everywhere: CI runs and `claude -p` usually lack the connector.

- **Dry-run**: no Linear or Luma writes. Write the exact would-be changes to `.context/create-event/<slug>/linear-preview.md`. That covers the title, every field, the full description, the sub-issues to create, and each update and comment, plus the tool call you would make for each.
- **Tools unavailable on a real run**: finish everything local and in GitHub. Then write the same `linear-preview.md` and tell the user plainly that Linear wasn't updated, so they (or an interactive session) can apply it.
- Reads that fail (issue not found, no access) are not fatal. Continue with the spec as given and flag it.
