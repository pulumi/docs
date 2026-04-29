---
user-invocable: true
description: Draft (or revise) the X / LinkedIn / Bluesky social copy in a blog post's frontmatter, looping with self-critique until it would pass review.
argument: optional file path to a blog post (e.g., content/blog/my-post/index.md). If omitted, picks the blog file currently changed in `git status`.
---

# Draft social post

Read a blog post, write or revise social copy into its frontmatter `social:` block, and loop with self-critique until each platform passes review. Preserve existing copy that already works — only repair or draft fresh when there's a real problem.

## Flow

1. **Resolve the target file.**
   - If the user passed a path, use it.
   - Otherwise: run `git status --porcelain` and pick the single modified `content/blog/*/index.md`. If zero or more than one match, ask the user which file.

2. **Read the blog post in full and any existing `social:` block.** The blog body is the source of truth for every specific you'll use — read it before drafting, not after. Title, URL slug, `meta_desc`, and tags are not authoritative; the body is.

3. **Per-platform: classify and act.** For each of X, LinkedIn, Bluesky:

   - **Empty (`""`), missing key, or LLM-fill junk** — draft fresh from the blog body using `.claude/commands/social-media-review/references/writing-guide.md` (see "Drafting from a blank `social:` block" — it includes the verify-specifics-against-body checklist). Honour platform structure: X = 2 paragraphs, LinkedIn = multiple short paragraphs, Bluesky = 2 paragraphs. Voice: if a single named author wrote a personal-experience post, name them in third person; otherwise corporate "we".

   - **Existing copy that breaks a hard rule** (banned phrases, "I" voice, URL in body, hashtags, markdown, paragraph structure, char limits — see `.claude/commands/social-media-review/references/critique-rubric.md`) — minimum-change repair. Drop the hashtag, swap the "I" to "we", trim the over-limit tail. Don't recast paragraphs or "improve" the voice. The original specifics and structure stay.

   - **Existing copy that passes hard rules and reads naturally** — leave it. Do not rewrite for taste.

   For LLM-fill recognition (staccato fragments as drama, em-dash chains, generic openers like "In today's cloud landscape…", buzzword stacks), see `.claude/commands/social-media-review/references/writing-guide.md` "Spotting and replacing LLM-fill copy". Don't try to patch around LLM patterns; throw them out and draft fresh from the article.

   **For any platform you draft fresh, verify each specific against the blog body** before moving on. Walk back through the draft and confirm every number, named tool, named person, attribution, and percentage appears in the body. Common error shapes: numbers pulled from the URL slug instead of the body, generalizations beyond what the body says, attribution flips (third-party finding credited to "we"), voice mismatch (corporate "we" on a personal-experience post). If a claim doesn't trace, drop it or replace it with one that does.

4. **Verify character counts before critique.** Pipe each draft into `python3 -c "import sys; print(len(sys.stdin.read().rstrip('\n')))"` (avoids quoting/escaping problems with apostrophes or triple quotes in copy). Body limits: X = 255, LinkedIn = 2950, Bluesky = 300. Revise any over-limit copy here.

5. **Critique loop.** Spawn a sub-agent (Agent tool, `general-purpose` subagent_type) with a clean slate. Brief: read `.claude/commands/social-media-review/references/critique-rubric.md`, evaluate the copy only (not the blog post), return PASS or FAIL per platform. Default verdict is PASS — only FAIL on hard-rule breaks.
   - All three PASS → go to step 6.
   - Any FAIL → repair based on the cited reasons (minimum-change semantics from step 3), repeat from step 4.
   - Cap at 3 critique rounds. If still failing, keep the most recent draft and note the open issues in the report.

6. **Advisory pass — only on `kept` platforms.** For each platform whose existing copy passed hard rules and you left untouched, spawn a sub-agent against `.claude/commands/social-media-review/references/suggestions-rubric.md` to surface stylistic notes (weak opener, summarizes article, missing pointer, etc.). Do NOT modify the kept copy — surface the notes in step 8's report so the user can decide whether to apply them. PASS stays PASS. Skip this pass on platforms you repaired or drafted — the new copy is the actionable feedback already; layering advisory notes on top is noise.

7. **Write the final copy into the frontmatter.** Use the Edit tool to replace (or insert) the `social:` block. Use 4-space indent and `|` block-literal style for multi-line copy — see `content/blog/neo-integration-catalog/index.md` for a well-formatted example. Only touch platforms whose copy actually changed.

8. **Report.** Show the path written to and per-platform status:
   - `kept` — original passed and was preserved
   - `repaired (N chars changed)` — minimum-change fix
   - `drafted` — wrote fresh
   - Final character counts for each platform
   - Iteration count ("converged in N rounds" or "stopped at 3, X open issue")
   - For each `kept` platform with advisory notes, list them under "Suggestions for kept platforms (advisory — not applied)" so the user can decide whether to address them in a follow-up. Omit the section if all kept platforms returned "no suggestions".

## Edge cases

- If the blog post has no body content yet (only frontmatter), tell the user — drafting against an empty post produces generic copy.
- If the user wants the existing copy preserved verbatim regardless of issues, they should say so in the invocation; otherwise this skill applies the classification above.
- If all three platforms classify as `kept`, report that and exit without writing — no edit is needed.
