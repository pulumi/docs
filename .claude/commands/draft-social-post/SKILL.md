---
user-invocable: true
description: Draft (or revise) the X / LinkedIn / Bluesky social copy in a blog post's frontmatter, looping with self-critique until it would pass review.
argument: optional file path to a blog post (e.g., content/blog/my-post/index.md). If omitted, picks the blog file currently changed in `git status`.
---

# Draft social post

Read a blog post, write social copy into its frontmatter `social:` block, and loop with self-critique until each platform passes review.

## Flow

1. **Resolve the target file.**
   - If the user passed a path, use it.
   - Otherwise: run `git status --porcelain` and pick the single modified `content/blog/*/index.md`. If zero or more than one match, ask the user which file.

2. **Read the blog post and any existing `social:` block.** Treat existing copy as a starting point to revise, never as final.

3. **Draft following the writing guide at `.claude/commands/social-media-review/references/writing-guide.md`.** Draft for all three platforms (X / LinkedIn / Bluesky). Honour platform structure: X = 2 paragraphs, LinkedIn = multiple short paragraphs, Bluesky = 2 paragraphs. Voice: if a single named author wrote a personal-experience post, use their name; otherwise corporate "we".

4. **Verify character counts before critique.** Pipe each draft into `python3 -c "import sys; print(len(sys.stdin.read().rstrip('\n')))"` (avoids quoting/escaping problems with apostrophes or triple quotes in copy). Body limits: X = 255, LinkedIn = 2950, Bluesky = 300. Revise any over-limit copy here.

5. **Critique loop.** Spawn a sub-agent (Agent tool, `general-purpose` subagent_type) with a clean slate. Brief: read `.claude/commands/social-media-review/references/critique-rubric.md`, evaluate the draft copy only (not the blog post), return PASS or FAIL per platform with brief reasons.
   - All three PASS → go to step 6.
   - Any FAIL → revise based on reasons, repeat from step 4.
   - Cap at 3 critique rounds. If still failing, keep the most recent draft and note the open issues in the report.

6. **Write the final copy into the frontmatter.** Use the Edit tool to replace (or insert) the `social:` block. Use 4-space indent and `|` block-literal style for multi-line copy — see `content/blog/neo-integration-catalog/index.md` for a well-formatted example.

7. **Report.** Show the path written to, the final per-platform copy with character counts, and the iteration count ("converged in N rounds" or "stopped at 3, X open issue").

## Edge cases

- If the blog post has no body content yet (only frontmatter), tell the user — drafting against an empty post produces generic copy.
- If the file already has `social:` copy that the author wants to preserve verbatim for one platform, they should say so in the invocation; otherwise this skill rewrites all three.
