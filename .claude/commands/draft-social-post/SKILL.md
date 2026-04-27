---
user-invocable: true
description: Draft (or revise) the X / LinkedIn / Bluesky social copy in a blog post's frontmatter, looping with self-critique until it would pass review.
argument: optional file path to a blog post (e.g., content/blog/my-post/index.md). If omitted, picks the blog file currently changed in `git status`.
---

# Draft social post

Local companion to `/social-media-review`. Read a blog post, write social copy into its frontmatter `social:` block, and loop until self-critique says it would pass review. Same rubric and writing guide as CI uses, so passing locally is a reasonable predictor of passing CI (not a guarantee — the LLM judges borderline copy non-deterministically).

## Flow

1. **Resolve the target file.**
   - If the user passed a path, use it.
   - Otherwise: run `git status --porcelain` and pick the single modified `content/blog/*/index.md`. If zero or more than one match, ask the user which file.

2. **Read the blog post and the existing `social:` block (if any).**
   - Always treat existing copy as a starting point to revise, never as final. The author invoked this skill because they want better copy.

3. **Draft following the writing guide.** Reuse `references/writing-guide.md` from the sibling skill — read it from `.claude/commands/social-media-review/references/writing-guide.md`. Draft for all three platforms (X / LinkedIn / Bluesky). If the existing copy has a usable hook, build on it; otherwise start fresh from the blog content. Honour platform structure rules: X = 2 paragraphs, LinkedIn = multiple short paragraphs, Bluesky = 2 paragraphs. Voice: if a single named author wrote a personal-experience post, use their name; otherwise corporate "we" (see writing-guide Voice section).

4. **Verify character counts before critique.** Run `python3 -c "print(len('''<copy>'''))"` for each draft. Body limits: X = 255, LinkedIn = 2950, Bluesky = 300. Revise any over-limit copy here — don't waste a critique round on a length failure.

5. **Critique loop.** Spawn a sub-agent (Agent tool, `general-purpose` subagent_type) with a clean slate. Brief: read `.claude/commands/social-media-review/references/critique-rubric.md`, evaluate the draft copy only (not the blog post), return PASS or FAIL per platform with brief reasons.
   - If all three PASS → done, go to step 6.
   - If any FAIL → revise based on the sub-agent's reasons, increment iteration counter, repeat from step 4.
   - Cap at 3 critique rounds total. If still failing after the third, take the best-scoring version and continue with a note in the output about which issues remain.

6. **Write the final copy back into the file's frontmatter.** Use the Edit tool to replace (or insert) the `social:` block. Preserve YAML formatting consistent with the rest of the frontmatter.

7. **Report.** Show:
   - Path written to.
   - Final per-platform copy + character counts.
   - Iteration count ("converged in N rounds" or "stopped at 3 rounds, X open issue").
   - One-line caveat: *"Local critique uses the same rubric as CI but verdicts on borderline copy are non-deterministic. CI is the source of truth."*

## Notes

- This skill **does not commit or push**. The author reviews the diff (`git diff content/blog/...`) and decides what to do with it.
- It's safe to re-run. Each invocation drafts fresh from the current frontmatter; it does not chain off prior critique runs.
- If the blog post has no body content yet (only frontmatter), tell the user — drafting against an empty post will produce generic copy.
