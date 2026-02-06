---
title: "Pulumi Neo Now Supports AGENTS.md"
date: 2026-02-06
draft: false
meta_desc: "Neo now reads AGENTS.md files to follow your project conventions automatically, using the same format as Cursor, GitHub Copilot, and other AI coding tools."
meta_image: meta.png
authors:
    - neo-team
tags:
    - neo
    - ai
    - features
schema_type: auto

social:
    twitter: |
        Neo now reads AGENTS.md files.

        Same format as Codex, Windsurf, and GitHub Copilot. Write your project conventions once, and every AI tool follows them automatically.

        No more "remember to add the environment tag" on every task.
    linkedin: |
        **Neo Now Supports AGENTS.md**

        Every codebase has conventions that aren't captured in linters: naming patterns, test commands, deployment rules. Without a shared format, you end up repeating these instructions to every AI tool you use.

        **The Solution**
        AGENTS.md is an open standard for project instructions, already supported by Cursor, Windsurf, GitHub Copilot, Zed, and over 60,000 open source projects. Neo now reads these files automatically.

        **How It Works**
        Add an AGENTS.md file to your repo with your project conventions. Neo picks it up on the next task. In monorepos, you can have specific instructions in subdirectories. Your conversation instructions always take precedence when you need to override.

        Write once, every tool follows.
---

Neo now reads [AGENTS.md](https://agents.md/) files, the open standard for giving AI coding tools context about your project. If you're already using AGENTS.md, Neo will pick up those same instructions automatically.

<!--more-->

## The problem AGENTS.md solves

Every codebase has conventions that aren't captured in linters or formatters. Maybe your team uses a specific naming pattern for infrastructure resources. Maybe there's a particular way you structure tests, or commands that need to run in a certain order. These are the things you'd explain to a new team member, and now you can explain them to AI tools too.

Without something like AGENTS.md, you end up repeating yourself. Every conversation starts with "remember to use TypeScript" or "make sure you add the environment tag." It's tedious, and things slip through.

AGENTS.md gives these instructions a home. You write them once, commit the file to your repo, and any tool that supports the format picks them up automatically.

## What to put in yours

Think about what you'd tell someone on their first day working in the codebase. How do you run tests? Are there naming conventions? Any gotchas they should know about?

Here's an example for a Pulumi project:

```markdown
# Infrastructure conventions

Run tests with `make test`. This spins up LocalStack, so Docker must be running.

Stacks are named `{service}-{region}-{env}` (e.g., `payments-us-west-2-prod`).
Only the platform team deploys to prod stacks.

All resources need these tags: `cost-center`, `team`, `environment`.

Reusable components live in `components/`. Check there before writing
something new.
```

There's no required structure, just markdown. Some teams write a few lines, others write detailed guides. Start small and add things as you notice yourself repeating instructions.

## How Neo handles AGENTS.md

When you point Neo at a repository, it reads any AGENTS.md file it finds and applies those instructions to its work. You don't need to mention the file or remind Neo about your conventions.

If you have a monorepo, you can put AGENTS.md files in subdirectories too. Neo uses the nearest one to wherever it's working, so you can have general instructions at the root and more specific ones in subpackages.

Your instructions in conversation always take precedence, so you can override the file when you need to. If you've also set up [Custom Instructions](/docs/ai/settings/#custom-instructions) at the organization level, Neo applies those first, then AGENTS.md on top.

## Works with the tools you're already using

AGENTS.md is an open format supported by most AI coding tools: Cursor, Windsurf, GitHub Copilot, Zed, and now Neo. If your team uses different tools for different tasks, they'll all follow the same project conventions without any extra configuration.

The format is managed by the Agentic AI Foundation under the Linux Foundation, and it's already in use in over 60,000 open source projects. See [agents.md](https://agents.md/) for the full specification.

## Get started

Add an AGENTS.md file to your repository and Neo will start using it on your next task. For more on configuring Neo, including organization-wide Custom Instructions and Slash Commands, see the [Settings documentation](/docs/ai/settings/).
