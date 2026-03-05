---
title: "Treating Prompts Like Code: A Content Engineer's AI Workflow"
date: 2026-03-05
draft: false
meta_desc: "How I built a modular AI workflow system to scale a solo docs practice — treating prompts like code, with reusable skills, shared context, and CI/CD."
meta_image: meta.png
authors:
    - cam-soper
tags:
    - ai
    - automation
    - developer-experience
schema_type: auto
---

Pulumi has a lot of engineers. It has marketers, solution architects, developer advocates. Everyone has something to contribute to docs and blog posts — domain expertise, hard-won lessons, real-world examples. What they don't all have is familiarity with our [Hugo](https://gohugo.io) setup, our style guide, our metadata conventions, or where a new document is supposed to live in the navigation tree. I joined Pulumi in July 2025 as a Senior Technical Content Engineer. A few weeks in, my sole teammate departed. The docs practice was now, functionally, me.

The problem was clear enough: how do you take one docs engineer's accumulated knowledge and make it available to everyone who needs it, without that engineer becoming a bottleneck?

I started packaging it. Here's what that looked like in practice.

<!--more-->

## The real problem AI solves

Everyone talks about AI making you faster. That's not wrong, but it's not the most interesting part — at least not for me.

The most interesting part is what it does to the *starting* problem. I have an ADHD brain (not formally diagnosed, but with enough self-recognition to know what's going on). I know what that means for my relationship with most tasks: I can see the problem, I understand it, I want to fix it, and then the sheer weight of starting crushes me flat.

When I'm stuck on a task, the issue is almost never that I don't know what to do. It's that my brain is trying to hold the entire finished product in working memory while simultaneously producing the first step. That's an enormous cognitive tax, and for an ADHD brain it's often insurmountable.

Talking through a problem conversationally is a completely different cognitive load. I can tell [Claude](https://claude.ai) "here's the issue, here's what I'm trying to accomplish, here's what's weird about it," and suddenly I'm not staring at a blank page anymore. I'm in a conversation. The scaffold exists. I can build on it.

I've been in this situation before. In a previous role writing training modules at Microsoft, I did some of my best work, not because the work was easy, but because I had a collaborator. A friend to think out loud with. Someone to say "okay, so what are we actually trying to say here?" That conversational scaffolding was the difference between spinning and shipping.

In my current role as a team of one, AI turned out to be that collaborator.

This isn't really a productivity story. It's closer to a cognitive accommodation story. And I'd bet a lot of people — diagnosed or not — will recognize what I'm describing.

## Treating prompts like code

If conversational scaffolding could lower my own activation energy, the next question was obvious: could I build that for anyone who needed it? I knew I wanted to use AI to solve this problem, but I didn't want to just write a bunch of one-off prompts. That would be a maintenance nightmare, and it wouldn't scale beyond me. I needed a system. Claude Code calls these reusable prompts *skills* — other platforms have the same idea under names like plugins or extensions. My first real experiment was `/docs-review` — a reusable prompt that would run my writing through a consistent set of criteria before I committed it. Nothing fancy. I just wanted a reliable bar that didn't depend on my mood or how much coffee I'd had.

Then it occurred to me: every PR to our docs repo should get this automatically. So I wired it into our CI/CD pipeline. Meagan, my manager, loved it — and after a few weeks, she noticed that PR quality had improved dramatically. On almost every PR, contributors were now spontaneously pushing an "Addressing feedback" commit right after the automated review posts — catching and fixing issues before I ever saw the PR.

That's when something clicked: I wasn't writing prompts anymore. I was writing *modules* — reusable, composable pieces of my own expertise.

The insight was straightforward, but it changed how I thought about the whole system: if multiple skills need the same context — our style guide, our review criteria, our content standards — that context should live in one place and get consumed by everything that needs it. Just like a shared library. Just like any decent software project.

I created a `REVIEW-CRITERIA.md` file as the single source of truth for what a "good" docs PR review looks like at Pulumi. Every skill that does any kind of review pulls from it. Change it once, and everything gets smarter at once. Likewise with our style guide, our Hugo conventions, our navigation structure. All of that lives in central reference files that any skill can pull from. If something changes, I change it in one place and all the skills get the update.

This also matters for token efficiency — which sounds like a nerdy footnote but isn't, especially when automated reviews are running on every PR. Duplicating context across skills bloats token usage fast. Modularizing keeps it lean. Your CI/CD pipeline doesn't care about elegance, but it definitely cares about cost.

The mental model I kept coming back to: **Don't Repeat Yourself.** It's the same principle that makes good software maintainable. It turns out it makes good AI workflows maintainable too.

## The skill catalog

From there, the system grew organically. Whenever I found myself doing something more than once, I asked: "Can I turn this into a skill?" Here's a sampling of what that produced:

**`/fix-issue`** — takes a [GitHub](https://github.com) issue and recommends a concrete plan of attack, so I go from "here's a ticket" to "here's what I'm doing" without the spinning-up tax.

**`/shipit`** — runs pre-commit checks, writes a focused commit message, and drafts a PR description.

**`/pr-review`** — full doc review on a PR branch: style guide, code examples, screenshots, optional test deployment, then an Approve/Merge/Request Changes dialog with a drafted comment.

**`/slack-to-issue`** — converts `#docs` [Slack](https://slack.com) conversations into properly formed GitHub issues. Slack is where decisions happen; issues are where work gets tracked.

**`/glow-up`** — runs an older doc through the modern style guide and flags outdated screenshots, for digging out of accumulated technical debt.

**`/new-doc`** and **`/new-blog-post`** — guide anyone through adding a new document or blog post with the right location, metadata, and navigation wiring. Engineers, marketers, whoever. The barrier to contributing just dropped significantly.

**`/docs-tools`** — helps other repo users discover that any of this exists. Discoverability is a real problem with internal tooling.

{{< notes type="info" >}}
Slack's built-in Claude integration isn't the same Claude running your Claude Code workflows — they don't share context or custom instructions. If you want consistent criteria across both surfaces, you need to bring your own backend. That's exactly what `/slack-to-issue` handles.
{{< /notes >}}

Other people started contributing skills to the repo — not because I asked, but because the pattern was legible enough to extend. Someone built a skill for SEO analysis. Marketing added their own review criteria. Engineers contributed workflows I never would have thought to build.

The thing I'd built as a personal survival tool had become a shared platform. That happened because I treated the prompts like code: modular, reusable, documented, open for contribution.

## Honest limitations

It's not a replacement for human judgment. These are probabilistic tools — they're right most of the time, not all of the time. `/pr-review` doesn't approve PRs autonomously. It highlights things and then asks me, the human, to read them and make the call. The AI does the first pass; I do the last one. That's not a workaround for a limitation — that's the design.

The system isn't finished, either. It's probably never finished. I'm still tweaking review criteria, still finding edge cases where a skill produces something weird, still adding new tools as new pain points emerge. Treating prompts like code means treating them like software: you ship, you iterate, you maintain. There's no version 1.0 and done.

And the ADHD angle is real but it's not magic. There are still days where the paralysis wins. AI lowers the activation energy for starting; it doesn't eliminate it. I'm still the one who has to show up. I suppose I could automate that too, but then we'd be in a whole different kind of dystopia.

## Lessons to share

**Know your models and their costs.** At Pulumi we primarily use Claude, and I work in [Claude Code](https://claude.ai/claude-code); for most tasks I reach for Sonnet rather than Opus. Opus is excellent, but it's significantly more expensive, and well-crafted instructions to Sonnet handle the vast majority of my work just as effectively.

**Treat it like a coworker.** Don't just issue commands and wait for output. Ask what it thinks. Push back when it's wrong. Explain your reasoning. The more you engage conversationally, the better the results tend to be. That extends to alignment, too — before diving into a complex task, talk through the approach first. A few minutes of alignment up front beats iterating on a misunderstood spec. I've gone as far as adding personal instructions to my config — things like playing along when I'm pretending to be Captain Picard, or using colorful language when the context calls for it. (Yes, those are literal config settings.) That sounds frivolous, but it isn't: a tool you actually enjoy using is a tool you'll reach for instead of avoid.

**Modularize your workflow.** Don't write one giant monolithic prompt that tries to do everything. Break it into focused skills that do one thing well and share common context through a central reference file. Easier to maintain, easier to debug, cheaper to run.

**Version control your prompts.** Your skills are code. Treat them like code. Commit them, review them, iterate on them. If a skill starts producing weird output after a tweak, you'll want to know what changed.

**Think about token burn rate.** This matters most when running automation in CI/CD. Keep your skills focused — a skill that checks style doesn't need to load your Hugo navigation conventions. The model only reads what you give it, so give it only what it needs.

**Not everything needs to be a prompt.** This one is underappreciated: skills can include scripts, and that's often the right call. When my team moves a doc in the repo, it needs to happen via `git mv` to preserve history, and we need to add a redirect alias to the front matter to prevent 404s and protect SEO. That's not something I want an AI to reason through from scratch every time — it's a solved problem. So it's a script. The skill just knows the script exists and what it does. Claude orchestrates; the script executes. That's a cleaner, more reliable division of labor than asking an LLM to reinvent the wheel on every run.

**Not everything needs to be generative.** Corollary to the last point: if you need deterministic output, don't use probabilistic tools. We have a skill that generates the meta image for blog posts — procedurally, not generatively. No AI-generated imagery. We have a brand to protect, and "let the AI vibe it out" isn't a content strategy. The skill follows our visual standards programmatically and produces something consistent every time. Know what you're automating and why.

## What's next

The next frontier is bringing some of this tooling to the less technical members of the team — marketing, in particular. The skills I've built assume a certain comfort level with terminals and repos. That's fine for engineers. It's a barrier for everyone else. A friendly interface would lower that bar significantly — that's the direction I'm currently exploring.

If you're a technical writer, a developer advocate, or a solo practitioner figuring out how AI fits into your workflow, the approach described here is a solid starting point. The tools matter, but the mental model matters more: treat your prompts like code. Make them reusable. Document them. Share them.

The blank page is still there. It's just a lot less intimidating when you've got a good collaborator and a solid set of tools.

Our docs repo is public, so the skills are there for anyone who wants them. If you're building something similar, steal freely — or contribute back.

{{< blog/cta-button "See our docs skills for inspiration" "https://github.com/pulumi/docs/tree/master/.claude/commands" "_blank" >}}
