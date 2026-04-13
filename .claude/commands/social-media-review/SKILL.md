---
user-invocable: true
description: Social media review for blog post PRs
argument: optional file path to a blog post (e.g., content/blog/my-post/index.md)
---

# Social Media Review

## Goal

Make people click through to the blog post. Every social post should leave the reader with an unresolved question they care about — something they can only answer by reading the article. If a reader can skip the article after reading the post, the post failed.

## Principles

- **Curiosity over completeness.** Withhold the key insight, approach, or verdict. Reveal enough to create tension, not enough to satisfy it.
- **Concrete over abstract.** Specific numbers, scenarios, and outcomes beat generic claims. "We migrated 200 stacks in three months" beats "we improved our migration process."
- **Reader's perspective.** Judge copy as a reader would — does this make me want to click? Not as an editor checking boxes.
- **Natural voice.** Posts should sound like a person wrote them, not like they were generated. No staccato fragments, no em dash chains, no constructed parallelism.

These posts are published from Pulumi's corporate accounts, not from individual authors.

## Flow

1. **Get the posts** — find the social copy to review (see Local/CI context below)
2. **Review** — evaluate each platform's copy against the critique rubric in `references/critique-rubric.md`. Return PASS or FAIL per platform with brief reasons (max 3 issues per platform)
3. **Draft** — for any FAIL or missing platforms, write replacement copy following the writing guide in `references/writing-guide.md`. Read the blog post to understand the content, but the copy should create curiosity, not summarize
4. **Verify character counts** — run `python3 -c "print(len('''<copy>'''))"` for each draft. Limits: X = 255, LinkedIn = 2950, Bluesky = 300. Revise any that exceed the limit
5. **Critique loop** — launch a sub-agent (Agent tool) to validate drafts. The sub-agent should read `references/critique-rubric.md` and evaluate the draft copy only (not the blog post). If FAIL, revise and re-critique. You may revise up to 2 times (3 total critiques). If the copy still fails after the third critique, present the best version with a note about which issues remain
6. **Output** — present the review and any suggested copy

## Output format

For each platform with copy, show the verdict in the heading (`#### Platform — PASS` or `#### Platform — FAIL`). For FAILs, include reasons as bullet points and 1-3 short guidance notes.

Missing platforms are NOT a failure. Do not mark them as FAIL. Note them separately and draft suggested copy so the author can choose to add them.

After the per-platform reviews, if any drafts were written, present them under `### Suggested copy` with character counts.

## Example output: all PASS

```
## Social Media Review

### content/blog/ai-coding-frameworks/index.md

#### X — PASS
#### LinkedIn — PASS
#### Bluesky — PASS
```

## Example output: FAIL with suggested copy

The original copy being reviewed:

X:
> AI coding agents fail in recognizable ways. Context fills up and early instructions fade, tests get skipped, and scope expands past what you asked for. Three separate community teams built frameworks to address these problems, each taking a completely different approach.
>
> We tested all three on real infrastructure workflows. Which one helps depends on which problem keeps hitting you.

LinkedIn:
> There is a pattern that teams building with AI coding agents tend to hit on longer projects. The first session is impressive. By the third, the agent has lost track of earlier requirements and started adding infrastructure nobody asked for.
>
> The context window is the core issue. It fills up, and earlier instructions carry less weight as it does. Writing better prompts helps at the start but does not solve the underlying problem.
>
> Three community frameworks tackled this in different ways. We spent a few weeks running all three on real Pulumi infrastructure work. Which one helps most comes down to which problem keeps showing up for you.

```
## Social Media Review

### content/blog/ai-coding-frameworks/index.md

#### X — FAIL

Reasons:
- Summarizes the article: names all three failure modes and gives the selection criterion
- Over character limit: 386 chars vs. 255 limit

Guidance:
- Lead with a concrete scenario, not an abstract list of failure categories

#### LinkedIn — FAIL

Reasons:
- Weak opening: "There is a pattern that teams tend to hit" is generic
- Summarizes the article's conclusion: reader learns it's three frameworks and "which helps depends on your problem"

Guidance:
- First line needs to stop the scroll with something specific

#### Bluesky — missing

No social copy for Bluesky. Suggested copy included below.

---

### Suggested copy

**X** (226/255 chars):
> We gave three AI coding frameworks the same Pulumi project. One produced a 41x speedup. One caught scope drift the others missed entirely. One we probably won't use again.
>
> Here's how they compared on real infrastructure work.

**LinkedIn** (504/2950 chars):
> We gave three open-source AI coding frameworks the same real infrastructure project and ran them for a few weeks.
>
> One produced a 41x speedup on a library release along the way. One caught a category of bug the other two missed entirely. One we probably won't reach for again.
>
> They have 270K combined GitHub stars and completely different theories about what goes wrong when agents work on longer projects. Turns out they're not all solving the same problem.
>
> Here's what we found and when to use which.

**Bluesky** (197/300 chars):
> We ran three AI coding frameworks on the same Pulumi infrastructure project for a few weeks. One caught scope drift the other two missed. One we probably won't use again.
>
> Here's how they compared.

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
```
