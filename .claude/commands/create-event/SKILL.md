---
name: create-event
description: "Creates a Pulumi event (workshop, webinar, or partner event) end to end: collects details from the prompt or an interactive wizard, scaffolds the content/events/<slug>/ page bundle, generates social cards via event-meta-image, files the tracking issue in pulumi/marketing from its issue template, and opens the docs PR. Use when the user types /create-event or asks to create, add, announce, or set up a workshop, webinar, livestream, or event page, event registration, or a workshop marketing issue — even if they only say 'new workshop' or 'schedule a webinar'. Accepts pasted details, a pulumi/marketing issue URL to prefill from, a brief file, --dry-run, and -y for no questions."
model: claude-opus-5
argument-hint: "[details | marketing issue URL | brief file] [--dry-run] [-y] [--no-issue] [--no-pr]"
metadata:
  companion-agent: event-creator   # .claude/agents/event-creator.md — executes the confirmed spec (see Step 4)
---

# /create-event — Create a Pulumi event (workshop / webinar / partner event)

You are the front half of a two-part flow. **You** run in the main conversation: gather and confirm the event details (Steps 1–3). The **event-creator subagent** (`.claude/agents/event-creator.md`, marked as `companion-agent` in the frontmatter above) is the back half: it executes the confirmed spec — bundle, social cards, marketing issue, PR (Step 4). It runs the mechanical work in its own context so this conversation stays focused; it cannot ask the user anything, which is why every decision is settled *here* first.

Display progress as **[Step X/5]**. Minimize open-ended questions: batch `AskUserQuestion` calls, prepopulate every option you can infer, and never re-ask what `$ARGUMENTS`, a fetched issue, or an earlier answer already settled.

References (read when needed, one level deep):
- `references/event-page.md` — every frontmatter field, slug rules, timezone/DST recipe, tags vocabulary, multi-session events, validation fallback.
- `references/marketing-issue.md` — issue template routing and snapshots, title/label/assignee conventions, form-ID sequencing and extraction.

## [Step 1/5] Parse input and detect context

Parse `$ARGUMENTS` / the user's message for:

- **Flags**: `--dry-run` (prepare everything, write issue/PR previews, zero GitHub writes — safe to run anytime); `-y` / `--yes` / `--non-interactive` / "no questions" (skip the wizard *and* the final confirmation, applying the defaults below — also assume this whenever running non-interactively, e.g. under `claude -p` or an eval, where questions can't be answered); `--no-issue` (`marketing.issue: skip`); `--no-pr` (`run.pr: skip`).
- **A pulumi/marketing issue URL or number** → this is an existing tracking issue. `gh issue view <n> --repo pulumi/marketing --json title,body,labels --comments` and prefill: title, date/time, duration, presenters, theme, tags, abstract, learn bullets — and scan the comments for HubSpot form ID / Salesforce campaign ID (regexes in `references/marketing-issue.md`). Set `marketing.issue: existing`.
- **A file path** (brief, Google-Doc export, notes) → read it and extract the same fields.
- **Free text** → extract what's there.

Then check for prior art — this skill is **idempotent**:

- Derive the slug (lowercase title, spaces → hyphens, alphanumerics and hyphens only; drop filler words only if the user's title is over 60 chars).
- If `content/events/<slug>/index.md` exists → **update mode**: diff what the spec provides against the page, plan only the gap (most often: wiring in form IDs that landed on the issue). If page *and* issue exist and there is no gap, report that the event is fully set up and stop — never duplicate.
- If no tracking issue was given, search for one: `gh issue list --repo pulumi/marketing --search "<title words>" --state all --limit 5`. A match → offer it as the existing issue instead of creating a duplicate.

## [Step 2/5] Wizard — fill the gaps only

Ask **only for fields still unknown** after Step 1, in at most two `AskUserQuestion` batches (≤4 questions each), with smart defaults marked "(Recommended)". In `-y` mode skip entirely and take every default. Free-text answers (title, description) that can't be multiple-choice: prefill suggestions from context and let "Other" carry the custom value.

| Field | Default / guidance |
|---|---|
| Event type | `workshop` \| `webinar` \| `talk` (page) — partner-hosted events route to the partner template, see `references/marketing-issue.md` |
| Title | ≤ 60 chars (hard limit — trim with the user if over) |
| Meta description | 50–160 chars, single sentence; suggest one from the abstract |
| Date + time + timezone | No default — this is the one field worth a blocking question outside `-y`; in `-y` with no date, use a weekday ~60 days out, 9:00 AM PT, and flag it loudly |
| Duration | `60 minutes` (90 when asked) |
| Location | `virtual`; otherwise `City, ST` |
| Gated | `true` for Pulumi-hosted workshops/webinars; `false` for external/on-demand |
| External? | Default `false`. `true` → `url_slug` = external URL + `block_external_search_index: true`, no form |
| Description (abstract) | 1–2 paragraphs; draft from whatever the user gave and show it |
| Learn bullets | Exactly 3 outcome bullets (template convention); draft them |
| Presenters | Prefill from git config → `data/team/team/<id>.toml` (role = its `title` + ", Pulumi"). Externals: name, role, company, optional photo |
| Tags | `level`: Beginner/Intermediate/Advanced; `topics`/`languages`/`clouds` from the vocabulary in `references/event-page.md` — reuse, don't mint |
| Marketing theme | One of AI, IaC, Platform Engineering, Security, TF-Takeover (issue template's closed set) |
| HubSpot segmentation | Optional; derive from tags; "when in doubt, do not add" |
| Form IDs | Only if already known (issue comments / user). Never invented — pending IDs become frontmatter TODOs |
| needs-design | `false`; `true` adds the label for a designer-made card |
| Sessions | Only when the user mentions multiple dates (AMER + EMEA etc.) — rules in `references/event-page.md` |

## [Step 3/5] Compose the spec and confirm

Assemble the **event spec** — the single artifact handed to the agent:

```yaml
event:
  title: ""            # ≤60 chars
  slug: ""
  event_type: workshop # workshop | webinar | talk
  meta_desc: ""        # 50–160 chars
  date: YYYY-MM-DD
  time: "HH:MM"
  timezone: America/Los_Angeles   # IANA name; agent computes the DST-correct offset
  duration: 60 minutes
  location: virtual
  gated: true
  external: false
  external_url: ""
  featured: false
  description: |
    ...
  learn: ["", "", ""]
  presenters:
    - {name: "", role: "", pulumi: true, photo: ""}   # role/photo auto-resolved for Pulumi folks
  tags: {level: Beginner, topics: [], languages: [], clouds: []}
  sessions: []         # optional; see references/event-page.md
marketing:
  theme: ""            # AI | IaC | Platform Engineering | Security | TF-Takeover
  issue: create        # create | existing | skip
  issue_url: ""
  needs_design: false
  hubspot_segmentation: {}
  form: {hubspot_form_id: "", salesforce_campaign_id: ""}
run:
  dry_run: false
  images: auto         # auto | event-bound | standalone | skip
  pr: create           # create | skip
  branch: event/<slug>
```

Show the user the spec plus a short preview: the would-be issue title (`[YYYY-MM-DD]: <Title> (<presenter first name>)`), the files to be created, and whether issue/PR will really be created. Then gate:

- **Dry-run** → proceed without asking (nothing outward happens).
- **`-y`** → proceed (the flag is the user's standing go-ahead), but still show the preview.
- **Otherwise** → one `AskUserQuestion`: "Create it now (issue + PR)" / "Dry run first (Recommended for a first pass)" / "Cancel". Creating a GitHub issue and PR is outward-facing — never do it silently.

## [Step 4/5] Delegate to the event-creator agent

Spawn the **event-creator** subagent (Task/Agent tool, `subagent_type: event-creator`), passing the spec verbatim as its task plus one line: "Execute this event spec per your protocol." Wait for the result — the next step depends on it.

If that agent type isn't registered in this session, don't stall: read `.claude/agents/event-creator.md` and execute its protocol yourself, inline, honoring the same hard rules (dry-run = zero GitHub writes; never push master; never invent form IDs).

## [Step 5/5] Relay the report and next steps

Relay the agent's structured report, then close the loop:

1. **Preview before shipping**: the rendered PNGs (or the build's auto-card), and `make serve` → `http://localhost:1313/events/<slug>/`.
2. **Dry-run** → the previews live in `.context/create-event/<slug>/`; rerun without `--dry-run` to create the issue and PR.
3. **Pending form IDs** → gated page ships with TODOs; watch the tracking issue for marketing's comment, then rerun `/create-event <issue-url>` to wire them in (update mode).
4. **PR is a draft** → mark ready after previewing; each ready-transition fires a full review, so do it once.
5. Suggest `/docs-review` for a content pass when the description was substantially drafted by the wizard.

## Error handling

- **Slug collision with a different event** (same slug, different topic) → suffix the slug (`-2026`, or the month) and tell the user.
- **`gh` unauthenticated / marketing repo unreachable** → finish everything local, write the issue preview, and hand the user the exact `gh issue create` command to run.
- **Date in the past** → confirm it's intentional (recordings/on-demand pages are legitimate).
- **User cancels at Step 3** → keep nothing outward; offer to save the spec to `.context/create-event/<slug>/spec.yaml` so a later run can resume from it.
