---
user-invocable: true
description: Social media review for blog post PRs
argument: optional file path to a blog post (e.g., content/blog/my-post/index.md)
---

# Social Media Review

## Goal

Tee up the article. Don't deliver it. The post's job is to set up what the article reveals — the reader has to read the article to get the reveal. If a reader can skip the article after reading the post, the post failed.

## Principles

- **Curiosity over completeness.** Withhold the key insight, approach, or verdict. Reveal enough to create tension, not enough to satisfy it.
- **Concrete over abstract.** Specific numbers, scenarios, and outcomes beat generic claims. "We migrated 200 stacks in three months" beats "we improved our migration process."
- **Reader's perspective.** Judge copy as a reader would — would I want to keep reading after this? Not as an editor checking boxes.
- **Natural voice.** Posts should sound like a person wrote them, not like they were generated. No staccato fragments, no em dash chains, no constructed parallelism.

These posts are published from Pulumi's corporate accounts, not from individual authors.

## Flow

1. **Get the posts** — find the social copy to review (see Local/CI context below). Read the blog body too — you'll need it for any platforms that are missing or unsalvageable.
2. **Review** — evaluate each platform's existing copy against the critique rubric in `references/critique-rubric.md`. Default verdict is PASS; only FAIL on hard-rule breaks (banned phrases, "I" voice, URL in body, hashtags, markdown, paragraph structure, char limits). Stylistic concerns are NOT failure conditions here. **An empty string (`""`) or omitted platform key counts as missing — skip the critic for that platform and route it to step 3's draft branch.**
3. **Repair or draft** — for each platform that didn't PASS:
   - **Existing copy that hard-fails** — produce minimum-change copy. Preserve the original voice, specifics, and structure; change only what's needed to satisfy the rule that broke. A hashtag at the end? Drop the hashtag. "I" voice? Swap to "we". URL in body? Remove it. Char overflow? Trim the tail. Substantial rewrites only when the original is unsalvageable (multiple compounding rule breaks, wrong specifics, or content unrelated to the article).
   - **Missing platform OR empty string OR existing copy is empty / LLM-fill junk** — draft fresh from the blog post. **Read the blog body before drafting.** Every specific in the draft (number, named tool, named person, attribution, percentage, comparison) must trace to a line in the blog body — do NOT pull numbers from the URL slug, title, or `meta_desc`. If the article is by a single named author writing personal experience, name them in third person; otherwise corporate "we". Use `references/writing-guide.md` for shape (see "Drafting from a blank `social:` block" and "Spotting and replacing LLM-fill copy"). Honor platform structure: X = 2 paragraphs, LinkedIn = multiple short paragraphs, Bluesky = 2 paragraphs.

   What minimum-change repair looks like:
   - **Hashtag drop:** `Define your rules once and catch errors before they hit stacks. #DevOps` → delete ` #DevOps`. ~8 chars changed; everything else identical.
   - **Voice swap:** `Looking ahead, I'm rapidly expanding platform capabilities` → swap `I'm` to `we're`. ~2 chars changed; specifics, structure, and surrounding sentences untouched.
   - **Trim to fit:** if the post is 322/255 chars, drop the appended sentence (or the most recent addition) rather than recasting. The cut should be a clean tail trim, not a rewrite.

   If the repair changes more than the rule break demands — recasting paragraphs, swapping verbs, "improving" the voice — back up. The critic only complained about one thing.

   **Verify drafted specifics against the blog body before step 4.** Every number, name, and attribution must appear in the body — not the title, slug, or `meta_desc`. If a claim doesn't trace, drop it or replace it.
4. **Verify character counts** — run `python3 -c "print(len('''<copy>'''))"` for ALL repaired or drafted copy before submitting to critique. Limits: X = 255, LinkedIn = 2950, Bluesky = 300. Revise any that exceed the limit. Do not skip this step — sending over-limit copy to the critique loop wastes a round.
5. **Critique loop** — launch a sub-agent (Agent tool) to validate the repaired/drafted copy. The sub-agent should read `references/critique-rubric.md` and evaluate the copy only (not the blog post). If FAIL, revise and re-critique. You may iterate up to 2 times (3 total critiques). If the copy still fails after the third critique, present the best version with a note about which issues remain.
6. **Suggestions pass** — for any platform whose **original** copy passed the critic without needing a repair, launch a separate sub-agent (Agent tool) against `references/suggestions-rubric.md` to surface advisory style notes (missing pointer, curiosity gap closed, weak opener, summarizes article, etc.). This NEVER affects the verdict — PASS stays PASS. Skip this pass for any platform that was repaired or drafted from scratch — the new copy is the actionable feedback already; layering advisory notes on top is noise.
7. **Output** — present the review, any repaired/drafted copy, and the suggestions section.

## Output format

Keep the review short and scannable. A blogger should be able to read it in 30 seconds and know exactly what to fix.

For each platform, show the verdict in the heading:
- `#### Platform — PASS` if the original copy passed the critic
- `#### Platform — FAIL` if the original copy failed the critic and was repaired
- `#### Platform — missing` if the platform had no copy and was drafted

For FAILs, include reasons as bullet points (the hard rule broken). No long analysis — the reasons plus the suggested copy are enough.

After the per-platform reviews, if any platforms were repaired OR drafted, present the new copy under `### Suggested copy` with character counts.

If any platform's original copy passed without needing a repair, present advisory notes from the suggestions pass under `### Suggestions (advisory)`, grouped by platform. Only include platforms that ran the suggestions pass (i.e., not the repaired ones, not the missing ones). If all run platforms returned "no suggestions", omit this section entirely — do not write `### Suggestions (advisory)` followed by silence. Suggestions never change the PASS/FAIL verdict.

## Example output: all PASS, no advisory

```
## Social Media Review

### content/blog/ai-coding-frameworks/index.md

#### X — PASS
#### LinkedIn — PASS
#### Bluesky — PASS
```

## Example output: PASS with advisory notes

```
## Social Media Review

### content/blog/ai-coding-frameworks/index.md

#### X — PASS
#### LinkedIn — PASS
#### Bluesky — PASS

---

### Suggestions (advisory)

These are stylistic notes — they don't block the post.

**X**
- Opening "There's a common challenge teams face" earns nothing — lead with the named tool or specific number from the article
- Final line summarizes the verdict; withhold which framework won

**LinkedIn**
- Missing pointer — the post just ends; add a line that signals there's more in the article
```

## Example output: FAIL repair + missing draft + PASS with advisory

The original copy being reviewed:

X (309 chars, over the 255 limit):
> AI coding agents fail in recognizable ways: context fades, tests get skipped, scope expands past what you asked for. Three community teams built frameworks for this, each taking a different approach.
>
> We tested all three on real infrastructure work. Which one helps depends on which problem keeps hitting you.

LinkedIn (passes hard rules, but summarizes):
> There is a pattern that teams building with AI coding agents tend to hit on longer projects. The first session is impressive. By the third, the agent has lost track of earlier requirements and started adding infrastructure nobody asked for.
>
> The context window is the core issue. It fills up, and earlier instructions carry less weight as it does. Writing better prompts helps at the start but does not solve the underlying problem.
>
> Three community frameworks tackled this in different ways. We spent a few weeks running all three on real Pulumi infrastructure work. Which one helps most comes down to which problem keeps showing up for you.

Bluesky: not provided.

```
## Social Media Review

### content/blog/ai-coding-frameworks/index.md

#### X — FAIL

Reasons:
- Over character limit: 309 chars vs. 255 limit

#### LinkedIn — PASS

#### Bluesky — missing

No copy provided. Suggested copy drafted below.

---

### Suggested copy

**X** (249/255 chars) — clean tail trim; final sentence dropped, everything else identical:
> AI coding agents fail in recognizable ways: context fades, tests get skipped, scope expands past what you asked for. Three community teams built frameworks for this, each taking a different approach.
>
> We tested all three on real infrastructure work.

**Bluesky** (197/300 chars) — drafted from the article:
> We ran three AI coding frameworks on the same Pulumi infrastructure project for a few weeks. One caught scope drift the other two missed. One we probably won't use again.
>
> Here's how they compared.

---

### Suggestions (advisory)

These are stylistic notes — they don't block the post.

**LinkedIn**
- "There is a pattern that teams building with AI coding agents tend to hit" is a generic opener — lead with the speedup or the bug the framework caught
- Final paragraph reveals the article's conclusion ("which helps comes down to which problem keeps showing up") — withhold the mapping so the reader still has something to find out

---

To apply these suggestions, comment: `@claude please update the social posts in the frontmatter with the suggested copy from the social media review above`
```

## Local context

Unless the prompt explicitly says "You are running in a CI environment", you are running locally. Follow this section, not the CI section.

1. Read the blog post at the given path. If no path is given, look for blog posts with uncommitted changes (`git diff --name-only` and `git diff --cached --name-only`) that match `content/blog/*/index.md`.
2. Extract the `social:` block from the frontmatter (twitter, linkedin, bluesky).
3. Run the flow above.
4. Print the full review and any suggested copy directly in the conversation. Do not post to GitHub. Do not include a CTA.

## CI context

When running in CI:

1. Read `.social-check-output.txt` for the list of posts to review and their social copy.
2. Run the flow above.
3. Post your findings as a single PR comment using `gh pr comment <PR_NUMBER> --body "<your review>"`. The PR number is provided in the workflow prompt. Title the comment `## Social Media Review`.
4. End the comment with a CTA:

```
To apply these suggestions, comment: `@claude please update the social posts in the frontmatter with the suggested copy from the social media review above`

To re-run the social media review after updates, comment: `/social-review`
```
