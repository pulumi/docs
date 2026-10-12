---
name: create-event
description: "Creates a Pulumi event (workshop, webinar, or partner event) end to end: collects details from the prompt, the Linear tracking issue, or an interactive wizard, scaffolds the content/events/<slug>/ page bundle, generates social cards via event-meta-image, opens the docs PR, and keeps the Linear tracking issue (Marketing team) and its promotion sub-issues up to date — creating the issue from the blueprint only when none exists. Use when the user types /create-event or asks to create, add, announce, or set up a workshop, webinar, livestream, or event page, event registration, or a workshop tracking issue — even if they only say 'new workshop' or 'schedule a webinar'. Accepts pasted details, a Linear issue URL or MA-<n> identifier to prefill from, a brief file, --dry-run, and -y for no questions."
model: claude-opus-5
argument-hint: "[details | Linear issue URL or MA-<n> | brief file] [--dry-run] [-y] [--no-issue] [--no-pr] [--luma]"
metadata:
  companion-agent: event-creator   # .claude/agents/event-creator.md — executes the confirmed spec (see Step 4)
---

# /create-event — Create a Pulumi event (workshop / webinar / partner event)

You are the front half of a two-part flow. **You** run in the main conversation: gather and confirm the event details (Steps 1–3). The **event-creator subagent** (`.claude/agents/event-creator.md`, marked as `companion-agent` in the frontmatter above) is the back half: it executes the confirmed spec — bundle, social cards, PR, Linear updates (Step 4). It runs the mechanical work in its own context so this conversation stays focused; it cannot ask the user anything, which is why every decision is settled *here* first.

Display progress as **[Step X/5]**. Minimize open-ended questions: batch `AskUserQuestion` calls, prepopulate every option you can infer, and never re-ask what `$ARGUMENTS`, the tracking issue, or an earlier answer already settled.

References (read when needed, one level deep):
- `references/event-page.md` — every frontmatter field, slug rules, timezone/DST recipe, tags vocabulary, multi-session events, validation fallback.
- `references/linear-issue.md` — where the tracking issue lives, find-before-create, title and description blueprint (MA-1045), promotion sub-issues, where form IDs come back, lifecycle updates, optional Luma event, and fallbacks when the Linear tools aren't available.

## [Step 1/5] Parse input and detect context

Parse `$ARGUMENTS` / the user's message for:

- **Flags**: `--dry-run` (prepare everything, write PR/Linear previews, zero GitHub, Linear, or Luma writes — safe to run anytime); `-y` / `--yes` / `--non-interactive` / "no questions" (skip the wizard *and* the final confirmation, applying the defaults below — also assume this whenever running non-interactively, e.g. under `claude -p` or an eval, where questions can't be answered); `--no-issue` (`linear.issue: skip`); `--no-pr` (`run.pr: skip`); `--luma` (`luma.create: true`).
- **A Linear issue URL or `MA-<n>` identifier** → the tracking issue. `get_issue` it, then prefill title, date/time, duration, presenters, theme, tags, abstract, learn bullets, and HubSpot segmentation from its description (the blueprint sections in `references/linear-issue.md`). List its sub-issues and their comments, plus the parent's comments, for form IDs. Set `linear.issue: existing`. Fields marked `TBD` on the issue are still unknown — the wizard fills them.
- **A `pulumi/marketing` GitHub issue URL** (events tracked before Q4 2026) → read-only prefill via `gh issue view <n> --repo pulumi/marketing --json title,body --comments`. Never create or edit anything there; set `linear.issue: skip` unless a Linear issue also exists.
- **A file path** (brief, Google-Doc export, notes) → read it and extract the same fields.
- **Free text** → extract what's there.

Then check for prior art — this skill is **idempotent**:

- Derive the slug (lowercase title, spaces → hyphens, alphanumerics and hyphens only; drop filler words only if the user's title is over 60 chars).
- If `content/events/<slug>/index.md` exists → **update mode**: diff what the spec provides against the page, plan only the gap (most often: wiring in form IDs that landed in Linear or on the PR). If the page is complete and the tracking issue is current, report that the event is fully set up and stop — never duplicate.
- If no tracking issue was given, search Linear: `list_issues` with team `Marketing`, the event quarter's `Workshops (Q<n> <yy>)` project, and a `query` of distinctive title words. Most workshops already have a parent issue synced from the Notion schedule; a match → use it as the existing issue instead of creating a duplicate.
- **Check Linear access here**, in the main conversation. If the Linear tools are missing or need authentication, tell the user now (they can connect it with `/mcp`) — the subagent can't prompt for it. Without access, plan `linear.issue: preview` (see `references/linear-issue.md` §Tool access).

## [Step 2/5] Wizard — fill the gaps only

Ask **only for fields still unknown** after Step 1, in at most two `AskUserQuestion` batches (≤4 questions each), with smart defaults marked "(Recommended)". In `-y` mode skip entirely and take every default. Free-text answers (title, description) that can't be multiple-choice: prefill suggestions from context and let "Other" carry the custom value.

| Field | Default / guidance |
|---|---|
| Event type | `workshop` \| `webinar` \| `talk` (page) — partner-hosted events have no Linear blueprint yet: build the page, set `linear.issue: skip`, and flag it |
| Title | ≤ 60 chars (hard limit — trim with the user if over); sentence case on the page |
| Meta description | 50–160 chars, single sentence; suggest one from the abstract (the issue often has it as `TBD`) |
| Date + time + timezone | No default — this is the one field worth a blocking question outside `-y`; in `-y` with no date, use a weekday ~60 days out, 9:00 AM PT, and flag it loudly. A Notion-synced issue's date wins over a guess |
| Duration | `60 minutes` (90 when asked) |
| Location | `virtual`; otherwise `City, ST` |
| Gated | `true` for Pulumi-hosted workshops/webinars; `false` for external/on-demand |
| Hosted elsewhere? | If so, set `event_url` to the `https://…` URL or `/…` path; the stub redirects there and is never indexed, no form. Omit for a normal page |
| Description (abstract) | 1–2 paragraphs; draft from whatever the user gave and show it |
| Learn bullets | 3 outcome bullets by convention; keep the issue's count when it already lists them |
| Presenters | Prefill from the issue, else from git config → `data/team/team/<id>.toml` (role = its `title` + ", Pulumi"). Externals: name, role, company, optional photo |
| Tags | `level`: Beginner/Intermediate/Advanced; `topics`/`languages`/`clouds` from the vocabulary in `references/event-page.md` — reuse, don't mint |
| Theme | One of AI, IaC, Platform Engineering, Security, TF-Takeover (the issue's `## Theme`) |
| HubSpot segmentation | Optional; derive from tags; "when in doubt, do not add" |
| Form IDs | Only if already known (Linear sub-issues/comments, a PR suggestion, or the user). Never invented — pending IDs become frontmatter TODOs |
| needs-design | `false`; `true` adds the `needs-design` label for a designer-made card |
| Luma event | Only with `--luma` or when the user asks; private until the page is live |
| Sessions | Only when the user mentions multiple dates (AMER + EMEA etc.) — rules in `references/event-page.md` |

## [Step 3/5] Compose the spec and confirm

Assemble the **event spec** — the single artifact handed to the agent:

```yaml
event:
  title: ""            # ≤60 chars, sentence case
  slug: ""
  event_type: workshop # workshop | webinar | talk
  meta_desc: ""        # 50–160 chars
  date: YYYY-MM-DD
  time: "HH:MM"
  timezone: America/Los_Angeles   # IANA name; agent computes the DST-correct offset
  duration: 60 minutes
  location: virtual
  gated: true
  event_url: ""        # optional; https://… or /… when hosted elsewhere, else omit
  featured: false
  description: |
    ...
  learn: ["", "", ""]
  presenters:
    - {name: "", role: "", pulumi: true, photo: ""}   # role/photo auto-resolved for Pulumi folks
  tags: {level: Beginner, topics: [], languages: [], clouds: []}
  sessions: []         # optional; see references/event-page.md
linear:
  issue: existing      # existing | create | preview | skip
  id: ""               # MA-<n> when existing
  url: ""
  project: ""          # e.g. "Workshops (Q4 26)" — quarter of the event date
  theme: ""            # AI | IaC | Platform Engineering | Security | TF-Takeover
  needs_design: false
  hubspot_segmentation: []
  tbd_fills: {}        # issue fields marked TBD that this run settles, e.g. {meta_description: "..."}
  form: {hubspot_form_id: "", salesforce_campaign_id: ""}
luma:
  create: false        # true only when asked
run:
  dry_run: false
  images: auto         # auto | event-bound | standalone | skip
  pr: create           # create | skip
  branch: event/<slug>
```

Show the user the spec plus a short preview: the tracking issue (existing `MA-<n>` link, or the would-be title `[YYYY-MM-DD] <Title> (<presenter first names>)` plus the 10 promotion sub-issues), the files to be created, and which outward writes will really happen (PR, Linear, Luma). Then gate:

- **Dry-run** → proceed without asking (nothing outward happens).
- **`-y`** → proceed (the flag is the user's standing go-ahead), but still show the preview.
- **Otherwise** → one `AskUserQuestion`: "Create it now (PR + Linear updates)" / "Dry run first (Recommended for a first pass)" / "Cancel". Opening a PR, creating or editing Linear issues, and creating a Luma event are outward-facing — never do them silently.

## [Step 4/5] Delegate to the event-creator agent

Spawn the **event-creator** subagent (Task/Agent tool, `subagent_type: event-creator`), passing the spec verbatim as its task plus one line: "Execute this event spec per your protocol." Wait for the result — the next step depends on it.

If that agent type isn't registered in this session, don't stall: read `.claude/agents/event-creator.md` and execute its protocol yourself, inline, honoring the same hard rules (dry-run = zero GitHub/Linear/Luma writes; never push master; never invent form IDs; never rewrite Notion-owned fields on the tracking issue).

## [Step 5/5] Relay the report and next steps

Relay the agent's structured report, then close the loop:

1. **Preview before shipping**: the rendered PNGs (or the build's auto-card), and `make serve` → `http://localhost:1313/events/<slug>/`.
1. **Dry-run** → the previews live in `.context/create-event/<slug>/` (`pr-preview.md`, `linear-preview.md`); rerun without `--dry-run` to apply them.
1. **Pending form IDs** → the gated page ships with TODOs; they come back on the "HubSpot form and Lists" / "SF campaign …" sub-issues, the parent issue, or as a review suggestion on the PR. Rerun `/create-event <MA-n>` to wire them in (update mode), then comment on the tracking issue.
1. **PR is a draft** → mark ready after previewing; each ready-transition fires a full review, so do it once. Then work the review to zero with `/address-review`, and post the outcome on the tracking issue.
1. **After merge and deploy** → confirm `/events/<slug>/` is live and listed on `/events/`, then mark the "Workshop link on /events page" sub-issue Done (lifecycle table in `references/linear-issue.md`).
1. Suggest `/docs-review` for a content pass when the description was substantially drafted by the wizard.

## Error handling

- **Slug collision with a different event** (same slug, different topic) → suffix the slug (`-2026`, or the month) and tell the user.
- **Linear unavailable or unauthenticated** → finish everything local and in GitHub, write `linear-preview.md`, and tell the user Linear wasn't updated (they can connect it with `/mcp` and rerun).
- **Spec disagrees with a Notion-synced issue** (title, date, presenter) → Notion is the source of truth; ask (interactive) or flag the mismatch (unattended) instead of editing the issue.
- **No `Workshops (Q<n> <yy>)` project for the event's quarter** → don't create a project; ask, or file without one and flag it.
- **Date in the past** → confirm it's intentional (recordings/on-demand pages are legitimate).
- **User cancels at Step 3** → keep nothing outward; offer to save the spec to `.context/create-event/<slug>/spec.yaml` so a later run can resume from it.
