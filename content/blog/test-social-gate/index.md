---
title: "Test post — social review gate"
allow_long_title: true
date: 2026-04-27
draft: true
meta_desc: "Throwaway post to exercise the social-review gate workflow. Will be removed before merge."
authors:
    - adam-gordon-bell
tags:
    - test
social:
    twitter: >
        Testing the social review gate. This copy is throwaway and will not be
        published anywhere. Reviewing this is purely a CI exercise.
    linkedin: >
        Testing the social review gate.

        This LinkedIn post is throwaway content for CI verification. Nothing
        here will be posted to any real account.
    bluesky: >
        Testing the social review gate. Throwaway copy for CI verification of
        the new gating workflow.
---

This blog post exists only to exercise the social media review gate workflow on PR #18705. It will be removed from the branch before any merge.

<!--more-->

The gate's job is to skip re-running the social review when a PR push doesn't actually change the social copy in the frontmatter, killing the non-deterministic flapping and the wasted Claude turns. This file is the test fixture.

Additional paragraph appended after the initial review. This edits only the post body — the `social:` frontmatter block is untouched. The gate should classify this push as SKIP and avoid re-running the LLM review.

Yet another body-only paragraph. With the fixed gate, this push should now find the prior successful run as a baseline, see that the `social:` block is unchanged, and skip the review.

Third body-only edit — exercising the gate after the API-filter fix.
