---
name: pr-review
description: Adjudicate open pull requests as a maintainer. `/pr-review` renders a queue of every open PR you can act on, sorted into stamp / judge / route / blocked with collision clusters first; `/pr-review N` renders one PR as that row expanded. Batch-approves and squash-merges the stamp set with a per-PR preflight, routes what isn't yours with the defect attached, unblocks conflicts, and refreshes stale reviews — one data model, one act layer, two renderings.
argument-hint: "[N] [--owner me|any|<role>|@login] [--domain docs,blog,…] [--verdict stamp,judge,route,blocked] [--author app/workprentice,pulumi-bot] [--since 7d] [--include-infra] [--strict-stances] [--board|--terminal] [--ai|--no-ai] [--act …]"
user-invocable: true
---

# Pull request review queue

The maintainer side of the review pipeline. CI posts the pinned review (the v3 author card + reviewer brief, or a legacy `<!-- CLAUDE_REVIEW N/M -->` monolith); this skill reads it as the source of truth for every open PR at once, computes one verdict per PR, and turns the approver's decisions into a batch of GitHub actions.

Deterministic scripts do the collecting, judging-by-rule and rendering; the model writes only the judgment calls on rows that earned one; a shared act primitive executes. Everything lives in `scripts/review-v3/` (covered by `make test-review-pipeline`):

| Step | Script | Model? |
|---|---|---|
| collect | `collect.py` → `.pr-review-queue.json` | no |
| analyze | `analyze.py` (verdict, reason codes, cross-PR) | no |
| judge | this skill, judge rows only → `.pr-review-judgments.json` | **yes** |
| render | `render.py` (board Artifact / detail / `--terminal`) | no |
| act | `act.py` (plan → preview → confirm → execute) | no |

## Usage

```text
/pr-review                                  # the queue: my lanes, board if anything needs judging
/pr-review 21598                            # one row, expanded (findings, preview links, actions)
/pr-review --verdict stamp --terminal       # just the stampable set, with the act command
/pr-review --owner any --domain blog        # what marketing has to decide
/pr-review --act --stamp 21550,21577 --route 21431:@cnunciato --unblock 21525

flags: --owner me|any|<role>|@login   --domain docs,blog,website,programs,infra,frontend,other   --include-handed-off
       --verdict stamp,judge,route,blocked   --author app/workprentice,pulumi-bot,any
       --since 7d   --include-infra   --strict-stances   --board|--terminal   --ai|--no-ai
       --act --stamp N,N --route N:@target --unblock N --fix N --close N --superseded-by M
             --refresh N --render N --deploy N [--merge-humans] [--no-merge] [--force] [--dry-run]
```

`--board` (the default when any row needs judging) publishes the page as an Artifact; `--terminal` prints the table and uses AskUserQuestion per judge row. Both are renderings of the same `queue.json`; there is no separate code path.

## Config: `~/.pr-review.yml`

Local, never committed. It says which routing lanes are *yours*; routing itself (lane → owning team) comes from `.github/review-routing.yml`.

```yaml
me: [docs, infra, frontend, other]   # lanes I approve for; blog/website route to marketing
stamp_max_lines: 40                  # a diff at or over this is never a stamp
stale_date_days: 3                   # a blog `date:` older than this is stale
link_fixes: mine                     # mine (default) | route: a link-only diff is yours whatever its lane
```

`link_fixes: mine` is for the redirect sweeps: a diff where every changed line is the same sentence with only a link rewritten (text or target; a word's casing may change too) gets `shape:link-only` and skips the lane check, since the lane owner's review buys nothing there. It's the queue's own bar, narrower than the Sentinel's mechanical bar, which counts any link edit as substantive. The row still has to clear the stamp bar; a sweep with open ⚠️ rows is a judge row with "approve as-is" as its primary.

Missing file: every lane counts as mine and the analyzer says so. `python3 scripts/review-v3/pr_review_config.py` prints the effective config. The AI-suspect allowlist stays at `~/.claude/pr-review/ai-suspect-authors.txt` (see `pr-review:references:trust-and-scrutiny`).

## The flow

Run the scripts from the repo root. Each is idempotent; re-running after acting updates the board rather than rewriting it.

### 1. Collect

```bash
python3 scripts/review-v3/collect.py --out .pr-review-queue.json [--pr N] [--author A] [--since 7d] [--ai|--no-ai]
```

Every open, non-draft PR (an explicit `--pr N` also collects a draft): title, author with the trust axes and risk tier, labels, files with patches, head/base SHAs, `mergeable_state` (re-asked while GitHub still says `unknown`), the check rollup, reviews, requested reviewers, the parsed pinned review (`review-worklist.py`, both surfaces), its `REVIEW_STATE`, triage's `<!-- TRIAGE_PROSE -->` comment, the reviewed-head SHA from `<!-- CLAUDE_REVIEW_HEAD … -->`, and the preview URL plus per-page links. Responses that only change when the PR does are cached under `/.pr-review-cache/<pr>/` per (head SHA, updated_at).

GitHub access: `gh` when installed, otherwise the REST API with `GITHUB_TOKEN` / `GH_TOKEN` (a Claude Code web session has the token but not `gh`). `--snapshot-dir DIR` reads endpoint JSON from files instead — the test backend, and the way to hand the scripts data fetched by the GitHub MCP tools: write each response to `DIR/GET/<endpoint path>.json` (`gh_client.py` documents the layout). GitHub App authors search as `author:app/<slug>` (`author:WorkPrentice` returns nothing); `--author` accepts any spelling.

Review status per PR, label-independent: `CURRENT` needs the card's `CLAUDE_REVIEW_HEAD` to prefix-match the live head — pushes made with `GITHUB_TOKEN` never fire `synchronize`, so a PR can sit at `review:no-blockers` with a review describing content a later commit replaced. `STALE` / `IN_PROGRESS` / `ERROR` / `ABSENT` / `TRIAGE_PROSE` otherwise.

> **v3 surface guard.** If a PR's review comments contain `<!-- CLAUDE_REVIEW_AUTHOR -->`, the PR is on the v3 surface and no local refresh machinery applies to it. The findings are the author card's blocking rows (🚨 / ❓, each with an `F<n>` id; dispositions live in its `REVIEW_STATE` block) plus the reviewer's guide's `### ⚠️ Check these before approving` rows — `collect.py` reads both. **Never run the local `docs-review:references:update` refresh or `pinned-comment.sh upsert` on a v3 PR** — they write a legacy monolith beside the cards. When a v3 review is `STALE`, the row is *blocked* with a `--refresh N` action that comments `@claude <reason> #update-review`; when it is `ERROR`, with a `--rerun N` action that comments `@claude <reason> #new-review` (the pipeline's from-scratch escape hatch); wait for the card to re-render (the label returns to `review:outstanding-issues` / `review:no-blockers`), then re-collect. The Sentinel check on the PR is the merge gate; stamp only when it is green or would be.

A legacy (v2) PR that is `STALE` gets the same `--refresh` action; the CI update lane rewrites the monolith. This skill never refreshes a review locally.

### 2. Analyze

```bash
python3 scripts/review-v3/analyze.py --in .pr-review-queue.json [--owner me] [--include-infra] [--strict-stances] [--domain …] [--verdict …] [--author …]
```

Per PR: `domains` (`classify_path` via `routing.resolve_lanes`), the owning role and team per domain, exactly one `verdict`, a `reasons` list of machine-readable codes, and `actions` (the `--act` fragments that apply). Cross-PR, computed over the full set before any filter: **collision clusters** (union-find over shared paths; a pair is `overlap` when the hunks intersect on the base side, else `same-file`, with a suggested merge order), **directional conflicts** (a PR adds links to a URL that exists only as a Hugo `aliases:` entry while another open PR removes links from it), **duplicate candidates** (shared file, similar title, opened within 10 minutes), **stale blog dates**, **self-accepted findings** (a `REVIEW_STATE` actor who is the PR author), **stale reviews**, and **stale brief summaries** (a "What this PR changes" bullet naming a value the diff no longer contains).

| Verdict | Meaning | Board |
|---|---|---|
| `stamp` | Every gate passes; approving asserts nothing beyond what's machine-verified. | "Approve & merge" starts selected. One command approves and squash-merges the set. |
| `judge` | Decidable from the board; something needs a human's call. | Judgment box: the lines, the question, a deep link, a recommended disposition. |
| `route` | Not this approver's lane per the routing matrix. | Batch "request review from owner"; any defect found rides along. |
| `blocked` | Can't merge regardless: conflict, red CI, stale review, changes requested. | Names the blocker and offers the mechanical unblock. |

**Handed off.** A PR whose requested reviewers include a human who isn't you (and don't include you) is waiting on them, not you. It keeps its verdict in `queue.json` but leaves the groups: the board and `--terminal` list it once, compactly, under "Waiting on others" (who, how old, a ✗ for red CI or ⚠ for a conflict), and `--include-handed-off` brings the full rows back when you need to act on one. A requested team counts as yours when `review-routing.yml` maps it to a lane in `me:`. The review request is the memory: it lives on the PR, every session sees it, and GitHub clears it when the reviewer acts, which is when the row returns. `--route N:@login` is therefore also the "don't show me this again" button. Collisions and directional conflicts against a handed-off PR are advisory (`:theirs`): they no longer gate your stamp, and a cluster with at most one of your PRs in it drops out of the pinned slots.

The stamp bar, **all required**: label `review:no-blockers` (`review:trivial` is not enough — no review ran); zero ⚠️ rows on the brief (zero low-confidence items on a legacy review); no self-accepted disposition; review `CURRENT`; `mergeable_state` in {clean, blocked} with checks green; no overlap collision, directional conflict or duplicate; one of the PR's domains is in `me`; no new file under `content/blog/`; no `layouts/` or `.github/` change unless `--include-infra`; changed lines under `stamp_max_lines`; scrutiny not heightened. Editorial stances on the brief block only with `--strict-stances`. Heightened scrutiny (AI-suspect on a human author) caps a row at `judge`. Precedence: blocked > route > stamp/judge.

Reason codes are `code[:detail]` from a closed vocabulary (`analyze.REASON_CODES`, echoed into `queue.json`): `risk:`, `scrutiny:`, `ai-suspect:`, `review:`, `label:`, `warnings:`, `outstanding:`, `self-accepted:`, `stances:`, `mergeable:`, `checks:`, `cluster:` (one per cluster: `C1:overlap:3/19` is this PR's place in the merge order, `C1:same-file` merges in any order, `C1:theirs` is mostly someone else's; `overlap` means two PRs touch the same or adjacent base lines, git's own conflict rule, not merely the same hunk), `review:base-merged` (the head moved only by merging the base, so the review still describes the diff and the row is not stale), `directional:`, `duplicate:`, `blog:`, `brief:`, `desc:`, `shape:` (`infra`, `link-only`), `size:`, `owner:`, `link-fixes:`, `route:` (the lane; `route:no-team` when its GitHub team doesn't exist yet, so the SLA person is the target instead), `handed-off:`, `merging-over:`, `not-governed`, `author:`, `trust:`, `draft`. The board shows the chips that change what you'd click and folds the rest behind "why".

Each collision cluster gets one recommendation, in words: **consolidate** (mostly one bot author's overlapping sweeps: one `--request-changes` on the newest asking for a single PR beats N serial merges), **chain** (merge the first in the order, then unblock the next: `--chain C1` does one link per run, and each link waits on CI), **ignore** (same-file only: any order works), or **theirs**. Those recommendations, plus the send-back / route / stamp batches, are the board's "Do next" list: one sentence and one button each, most leverage first.

### 3. Judge — the only model step

Only for rows whose verdict is `judge`. For each open finding on the row (`review.items` without a disposition, the brief's ⚠️ rows, or triage's prose bullets when `review:triage-prose`):

1. Quote the exact `-`/`+` lines at the finding's `file` and line from `files[].patch` in `queue.json`. Never paraphrase and never invent a quote; if the lines aren't in the patch, quote nothing and say so.
2. State in one sentence what the approver is deciding.
3. Recommend a disposition from `/address-review`'s vocabulary: `fixed | refuted | deferred | accepted | not-applicable`.
4. Emit the deep link `https://github.com/pulumi/docs/pull/N/files#diff-<sha256(path)>R<line>` (`compose-review.py::diff_anchor` is the helper; `render.py` computes it from `file` + `anchor` when you don't). No file or line → the link is "open the PR".

Also draft, when the row carries `desc:stale:*` or `desc:empty`, a corrected PR description (`fix_draft`), and optionally a `recommended` action: `stamp` to approve as-is, `request-changes` when the findings are the author's to fix (the judgments become the review body), `route`, or `close`. Send-back only reaches an author who can act on it: a person, or an agent bot that answers reviews (`workprentice`, Copilot). A PR opened by a workflow run — `pulumi-bot`'s content-review, glow-up and regen lanes, dependabot — carries `author:generated`, and a changes-requested review there would sit unread forever, so those rows take `close` instead (the lane re-queues the page on its next run) or a fix applied here. `merge_judgments` rewrites a `request-changes` recommendation on such a row to `close` rather than promising an author who will never answer. Write it all to `.pr-review-judgments.json`:

```json
{ "21598": { "judgments": [ { "finding_id": "F1", "file": "content/docs/iac/automation-api.md", "line": 412,
              "quote_minus": ["- [file an issue](…&template=bug_report.md&title=)"],
              "quote_plus": ["+ [file an issue](…?labels=needs-triage)"],
              "decision": "Did you mean to drop the bug-report template, or only the empty params?",
              "ask": "Restore template=bug_report.md so the link lands on the bug form.",
              "disposition": "accepted",
              "note": "The chooser page is a worse landing than the form; approver-only rationale.",
              "deep_link": "https://github.com/pulumi/docs/pull/21598/files#diff-…R412" } ],
            "fix_draft": { "kind": "description", "body": "### Proposed changes\n\n…" },
            "recommended": "stamp" } }
```

`decision` is the question you answered; `ask` is the sentence the author reads if the row goes back with `--request-changes` (on a generated row it is what the closing comment carries); `note` is your rationale and stays on the board. Then merge it: `python3 scripts/review-v3/analyze.py --in .pr-review-queue.json --judgments .pr-review-judgments.json`. A recommendation never lowers the computed verdict.

A `fixed` disposition means the diff already addresses the finding; the board shows it as "already fixed in the diff", not as a recommendation, and it is never a `--fix` action (that button appears only when the row carries a drafted description or one-click suggestions). For `/pr-review N` judge the one row. For the queue, judge every judge row before rendering; a row you skip renders its open findings under "Needs a call" without a quote.

### 4. Render and publish

```bash
python3 scripts/review-v3/render.py --in .pr-review-queue.json --board .pr-review-board.html   # the queue
python3 scripts/review-v3/render.py --in .pr-review-queue.json --detail N --out .pr-review-board.html   # /pr-review N
python3 scripts/review-v3/render.py --in .pr-review-queue.json --terminal [--pr N]
```

Publish with the Artifact tool (favicon 🗂️; update the same artifact on re-render rather than creating a new one). Pass `--artifact` when rendering for it: that form omits the document skeleton the Artifact tool adds itself. The default form is a standalone file for a browser or `screenshot.mjs`. The board opens with the tally, a progress line ("3 of 21 decisions made") and the "Do next" list; then the rows grouped owner → domain, showing only rows that need a decision by default (view chips add the stamp set and the blocked rows back); the collision detail folds at the bottom. Filter chips cover view / owner / domain / author / since and are literal: a row shows only while its value is lit in every group, so a group with nothing lit empties the board and says so ("reset chips" restores the defaults; `since` is the one threshold). Every action button is a toggle that composes the `/pr-review --act …` command shown at the bottom (a stamp row's "approve & merge" starts selected, so the default command merges the whole stamp set; the composer never repeats a fragment). Every row says on the button whether approving also merges: a bot row leads with "approve & merge" and offers "approve, don't merge"; a human-authored row leads with "approve, no merge" and offers "approve & merge". Both are decisions, so picking one puts out the other. A row takes one decision (approve either way, send back or close it out, route, unblock, refresh, re-run): lighting a second one puts out the first. Side actions (apply fixes, render preview, deploy) ride alongside whichever decision is lit, and only decisions count toward the progress line. The page never calls GitHub; the person copies the command, or asks you to run it.

Both renderings hide handed-off rows behind the "Waiting on others" list unless `--include-handed-off`. `--terminal` prints the table and, in this mode only, walk each judge row with AskUserQuestion (options: approve as-is / route / refresh / skip), then compose the same act command.

### 5. Act

```bash
python3 scripts/review-v3/act.py --in .pr-review-queue.json --stamp 21550,21577 --route 21431:@cnunciato --unblock 21525
python3 scripts/review-v3/act.py --execute .pr-review-plan.json [--dry-run]
```

The first command validates against the queue and writes `.pr-review-plan.json` plus a preview: for each step the PR, head SHA, the preflight it will run, the exact approval text, and every write. **Show the preview and get a yes before `--execute`** (an explicit `--act` in the user's own invocation counts as the yes for exactly that plan; a re-plan needs a new confirmation). Then execute, and report the per-step results.

- `--stamp N,N` — per PR, immediately before merging, re-fetch the PR: head unchanged since the plan, `mergeable_state` in {clean, blocked}, checks green, no changes-requested review. Then approve (one line per `pr-review:references:message-templates`, no footer) and squash-merge. A bot PR merges — dependabot, pulumi-bot and WorkPrentice alike, since they exist to be merged; a human-authored PR is approved only, because it is the author's to merge. `N:merge` and `N:no-merge` override that default for one PR (`--stamp 21550,21577:no-merge`), so a mixed batch stays one command; the blanket `--merge-humans` and `--no-merge` still apply where no per-PR mode is given. A failed preflight skips that PR and the batch continues. `--force` stamps a judge row (approve as-is); a blocked row is never stampable.
- `--route N:@user|@org/team` — request review and post one comment with the row's defects (reason codes + judgments). `N` alone uses the row's own route target.
- `--request-changes N` — post a changes-requested review built from the row's judgments (one line-anchored item each, `--reason` as the opening line, voice per author type from `pr-review:references:message-templates`) and apply `needs-author-response`. The author's turn; nothing merges until they answer. Refused on an `author:generated` row, which has no author to answer it, unless you pass `--force`.
- `--chain C1` — start a cluster's chain: stamp the first PR in its merge order (`--force` implied for a judge row), then merge base into the next so the following run finds it green. One link per run.
- `--unblock N` — merge the base branch into the head as a merge commit and push; a conflicted merge is aborted and reported, never resolved by hand here and never rebased or force-pushed.
- `--fix N` — apply the drafted description and any one-click ✏️ suggestions, commit, push.
- `--close N [--superseded-by M]` — with `M`, cross-link both and close N. Alone, close N with one comment: on an `author:generated` row that comment is written from the row's judgments and needs no `--reason`; on anyone else's PR `--reason` is required, because closing someone's work without saying why is worse than sitting on it.
- `--refresh N` — comment `@claude <reason> #update-review`.
- `--rerun N` — comment `@claude <reason> #new-review`: clears the cards and dispatches a fresh initial review, bypassing the trivial / frontmatter-only / draft / bot skips. The unblock on a `review:error` row; a side action ("run a full review") on a row where no review ran.
- `--render N` — screenshot the preview pages into `/.pr-review-shots/N/` (`screenshot.mjs`, Playwright); the detail view embeds them.
- `--deploy N` — dispatch `testing-build-and-deploy.yml` at the head branch (the `risk:infra` row action; see `pr-review:references:infrastructure-deployment`).

Which bot branches may be pushed to, and the action bar per row, are in `pr-review:references:action-menus`. Every comment `act.py` posts carries the Claude Code attribution footer except the approval body.

### 6. Re-collect, re-render

After acting, run collect (`--pr` for the touched PRs is enough) → analyze (`--judgments` again) → render, and update the same Artifact. Merged and closed PRs drop out; the board is the report.

## Hand-offs

- Author work (an open 🚨/❓ item, a fix the author should make): tell them to run `/address-review N`; that is where dispositions get recorded with the outcome the post-merge scrape reads.
- Your own PR: run `/address-review` first, then adjudicate.
- `/dashboard` shows only the open-PR count and points here.

## Errors

A failed step is reported in place (`✗ stamp #N: preflight refused: head-moved …`) and never stops the batch. Recover by re-collecting and re-planning; a `head-moved` refusal means someone pushed — judge the new diff. If `collect.py` can't reach GitHub it says which backend it tried; a `GhNotFound` from the snapshot backend names the endpoint file it wanted.
