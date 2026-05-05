---
title: "Testing the Social-Review Edit-in-Place Workflow"
date: 2099-12-31
draft: true
meta_desc: "Throwaway post to exercise the social-review CI workflow's edit-in-place behavior. Will be deleted before merge."
authors:
    - adam-gordon-bell
tags:
    - test
social:
    twitter: |
        In today's rapidly evolving and dynamic technological landscape of artificial intelligence and machine learning systems, organizations are leveraging cutting-edge solutions to unlock unprecedented value, drive transformational outcomes, and revolutionize the way teams collaborate and ship software in production environments at scale.
    linkedin: |
        Pushed a workflow change that should make the CI social-review comments quieter — one comment per PR, edited in place, no new entries on each push.

        Same pattern pulumi-bot already uses for preview links. Validating the path with a throwaway test post on a side PR.
    bluesky: |
        Quick test post for the new social-review CI workflow.

        Trying out edit-in-place: one comment per PR, updated each push, no more thread spam.
---

This is a throwaway post used to exercise the `claude-social-review.yml` workflow's edit-in-place behavior. It will be deleted before the workflow PR is merged. (Push 6: body edit retry — exercising the fixed regex, expecting skip via comment baseline.)

The Twitter copy above is deliberately over the 280-character limit to confirm the build still fails on objective character-limit violations. The LinkedIn copy is deliberately AI-toned to confirm Claude's PASS/FAIL judgment still surfaces in the comment without failing the build. The Bluesky copy is clean and human and should PASS.

When this post is pushed:

1. The workflow triggers (path matches `content/blog/*/index.md`).
2. Claude writes the review to `.social-review.md` with the `<!-- social-review -->` marker and a SHA/time footer.
3. The find-comment step returns no match (first run) — the create-or-update step posts a fresh comment.
4. The fail step kills the build because the Twitter copy exceeds 280 chars.

When the post is updated and pushed again:

1. Workflow re-triggers.
2. Claude writes a new `.social-review.md`.
3. The find-comment step matches by marker — returns the existing comment id.
4. The create-or-update step replaces the body in place.
5. The result on the PR: same comment, new content, no extra thread entries.
