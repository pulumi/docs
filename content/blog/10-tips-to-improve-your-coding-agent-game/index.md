---
title: "10 tips to improve your coding agent game"
date: 2026-09-21
draft: false
meta_desc: "Ten coding agent habits checked against the research behind them, from rules files that rot and /compact to model switching, subagents, and review."
feature_image: feature.png
authors:
    - engin-diri
tags:
    - ai
    - ai-agents
    - claude-code
    - codex
# Required: exactly one category (a scalar) from the closed set in
# data/blog_categories.yaml. Use "general" for posts that don't clearly fit a
# specific kind. Validated by `make lint`.
category: best-practices
schema_type: auto

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        Switching to a bigger model halfway through a task recovered less than half the quality gap in an AWS study, and cost more than twice as much as starting with the big model.

        That's one of ten coding agent tips, each checked against the research behind it.
    linkedin: |
        This summer, a run of arXiv papers put numbers on how coding agents behave: what they read, what survives /compact, and what a mid-task model switch really costs.

        Engin Diri turned the research into ten tips. Rules files rot: 23% of repositories in one sample referenced code that no longer existed. One /compact round kept about half of an agent's safety rules. Escalating to a bigger model mid-task cost more than twice as much as starting with it in an AWS study, and a restart did better. And the model that wrote the code shouldn't be the one that approves it.
    bluesky: |
        Ten coding agent tips, each checked against the research.

        The most expensive habit on the list: escalating to a bigger model mid-task. In an AWS study on SWE-bench, restarting Opus from scratch cost less and solved more than handing it Haiku's transcript.
---

In May I told you to keep the root CLAUDE.md to one screen and to put the rules that must hold into hooks. In June I said the model that wrote the code shouldn't be the one grading it. This summer, a run of arXiv papers put numbers on those habits and a few others.

Most of the numbers back those habits harder than I did. One cuts against advice from that same May post. Here are ten tips for working with any coding agent, each checked against what the research actually measured.

<!--more-->

Read side by side, the papers point the same way. The conversation with your agent is a lossy place to keep anything that matters, and nearly every fix below moves something out of the chat and into a file, a hook, a test, or a fresh session. In June I put it as [the agent forgets, the repo does not](/blog/stop-prompting-design-the-loop/), and these papers show how much it forgets.

## Rules files

### 1. Write rules for the agent, not for a new hire

A new hire can take a vague convention and work out what it means from the code around it. An agent fills the gap with a guess. Anthropic's [guidance on CLAUDE.md and AGENTS.md files](https://code.claude.com/docs/en/memory) asks for instructions "concrete enough to verify," like "API handlers live in `src/api/handlers/`" instead of "Keep files organized." One line in my own Go rules says to wrap errors with `fmt.Errorf("...: %w", err)` and never discard one silently. An agent can follow that and a reviewer can check it, which you can't say about "handle errors properly."

The research shows why the effort pays. Zhijun Gao and Jing Chen at Peking University [traced 557 real agent sessions](https://arxiv.org/abs/2608.20195) to see which documentation agents touch. Instruction files and the agents' own working notes made up 60.5% of those interactions, API references 1.3%. The authors couldn't show that any particular writing style changes behavior, and most sessions came from Claude Code. They did show where agents look.

### 2. Treat rules files like code, because they rot

Specific rules go stale. Rename a folder or swap a database and the rules file keeps describing the old codebase. The agent either burns turns reconciling the two or believes the file.

Christoph Treude and Sebastian Baltes [ran an existing documentation checker](https://arxiv.org/abs/2606.09090), DOCER, over 612 agent config files in 356 randomly sampled GitHub repositories. In 82 of those repositories, 23.0%, a CLAUDE.md, AGENTS.md, or Copilot instructions file named a function, path, or script that has since disappeared from the code. That's close to one repository in four, and the authors call it a feasibility signal rather than a precise rate: only 32 of the 50 flags they checked by hand were real. A second paper explains why rot piles up. In 441 repositories, [73.8% of AI configuration files](https://arxiv.org/abs/2608.25241) were committed once and never touched again.

A crude version of the check, run in September against the AGENTS.md of the repository this blog is built from, flagged 37 of 124 path-like references. Nearly all were noise, like relative paths and files that live in other repositories. One was real. Since a dark mode change in June, the file had been pointing agents at a `docs-logo.html` partial that was never added to the repository.

The authors suggest running the check in CI, and DOCER has a [GitHub Actions version](https://github.com/wesleytanws/DOCER_tool). In May I described [a `Stop` hook that proposes CLAUDE.md updates](/blog/stop-tuning-prompts-build-a-harness/) at the end of each session. Either works, as long as a human reads what it flags.

### 3. Keep the rules file short, but don't delete it

The mistake I see most often is a root CLAUDE.md that has grown into a small book, so every session pays for conventions the current task will never touch. Anthropic's docs set a target of [under 200 lines per CLAUDE.md file](https://code.claude.com/docs/en/memory), because "longer files consume more context and reduce adherence." Codex, by default, [stops reading AGENTS.md files](https://learn.chatgpt.com/docs/agent-configuration/agents-md) once they add up to 32 KiB. Claude Code has read [AGENTS.md too](https://code.claude.com/docs/en/memory#agents-md) since v2.1.277, but a repository with both files gets only the CLAUDE.md, unless the CLAUDE.md imports AGENTS.md or you set **Project instructions** to `claude-md-and-agents-md`.

The cleanest measurement of that cost isn't about coding agents. [Lodha and colleagues at Microsoft](https://arxiv.org/abs/2606.10209) followed a GPT-5 agent that itemizes hotel expenses, and trimmed its tool-call history: keeping only the last five tool calls raised completion from 71.0% to 79.0% on 63.9% fewer tokens. Closer to home, [Gloaguen and colleagues at ETH Zurich and LogicStar.ai](https://arxiv.org/abs/2602.11988) tested context files with Claude Code, Codex, and Qwen Code. Neither generated nor developer-written files produced a statistically significant gain in task success, and the generated ones raised inference cost by 20% or more. If an agent wrote your rules file and nobody has edited it since, that's the kind that added cost in the study without a measurable gain.

Don't overcorrect, though. [Denisov-Blanch and colleagues](https://arxiv.org/abs/2608.25241) followed 509 open-source repositories after they adopted coding agents. Among agent-first repositories, the ones with no committed AI configuration saw cognitive complexity grow 53%, against 27% for the ones with at least a rules file. It's correlational, but it's a reason to keep the file. For each line in it, Anthropic's [best practices](https://code.claude.com/docs/en/best-practices) suggest one question: "Would removing this cause Claude to make mistakes? If not, cut it."

## Long sessions

### 4. Don't let /compact carry your rules

When a session gets long, `/compact` is the path of least resistance: summarize, free up the window, keep going. The research says to be careful what you let it summarize.

[Zerhoudi, Mitrović, and Granitzer at the University of Passau](https://arxiv.org/abs/2608.22752) ran real agent config files through several compactors, including Sonnet 4.6 behind Claude Code's `/compact`, with a prompt that asked to keep every safety rule verbatim. Five rounds in a row, each halving the text, left 10% of the safety rules. One round left 53%, and that's the figure to act on: half the safety rules gone in a single pass, from a prompt that asked to keep them all.

[Shiyang Chen](https://arxiv.org/abs/2606.22528) measured what agents do next. Across seven models, one compaction raised policy violations from 0% to 30%, and to 59% for the worst two. Rules in a preserved system message held, while the same rules given as a user instruction, a memory entry, or tool output decayed by 33 to 50 points. For DeepSeek-V4, a compacted policy did worse than no policy at all, because "the summary normalizes the pending task while discarding the rule."

Claude Code already protects part of this. After `/compact`, it [re-reads the project-root CLAUDE.md from disk](https://code.claude.com/docs/en/memory), while rules you typed into the chat get no such guarantee. Standing rules belong in a file, and summaries are for the trail of what happened. The expense agent from tip 3 scored best, at 91.6%, when its dropped tool calls were replaced by a summary.

Better still, size the work so a session never needs compacting. Anthropic's best practices say to run `/clear` between unrelated tasks, and when one task runs long, a handoff note you write yourself beats a summary you can't see. In August I wrote that [prompt guardrails degrade with context length](/blog/sandboxing-coding-agents-yolo-mode/); these papers measure what that post could only argue.

### 5. Move load-bearing rules into hooks

A rule in a markdown file is a request. The model honors it most of the time, which is fine for naming conventions and wrong for anything that has to happen every time. Ask an agent to run the tests before it finishes and it usually will. A `Stop` hook runs them every time and hands the failures back. Claude Code's [hooks guide](https://code.claude.com/docs/en/hooks-guide) calls it "deterministic control: certain actions always happen rather than relying on the LLM to choose to run them."

Chen's fix points the same way. Pinning the policy outside the summary took about 47 tokens and brought violations back to 0%, and a hook goes further by never entering the context at all. For infrastructure, [Pulumi Policies](/docs/discovery-governance/policy/) plays that role at the deployment boundary: a mandatory policy blocks a noncompliant deployment, whatever the agent was told.

My own setup has two small guardrail hooks, one that blocks destructive shell commands and one that scans edited files for secrets. Hooks don't negotiate, in either direction. While I worked on this post, [rtk](https://github.com/rtk-ai/rtk), a `PreToolUse` hook I use to compress command output, collided with Claude Code's worktree isolation check, and every git command was refused until I called git by its full path. That's the behavior you want from rules that matter, and a reason to keep the list of hooks short.

### 6. Don't switch to a bigger model mid-task

When a session goes sideways, it's tempting to type `/model`, pick the bigger one, and keep going. The trouble is that the conversation is already contaminated. Drew Breunig calls it [context poisoning](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html): an error "makes it into the context, where it is repeatedly referenced."

This tip has the strongest paper on the list. [Ganz and colleagues at AWS](https://arxiv.org/abs/2608.24358) ran all 500 SWE-bench Verified tasks with a cheap model handing over to a strong one partway through, Claude Haiku 4.5 to Opus 4.7 and a GPT pair, across 58,000 runs. With the full transcript, the handoff recovered 47% of the gap between the two Claude models, and 36% for GPT. The handoff also cost more: $1.61 a task, against $0.72 for starting with Opus. Restarting Opus from scratch, even after paying for Haiku's wasted attempt, cost $0.90 and solved more.

The most useful result for day-to-day work: dropping the transcript and keeping only the file edits on disk raised recovery to 64% for Claude and 84% for GPT. If the task needs the big model, start with it. If you're already halfway in, write down what's done and where it's stuck, then open a new session on the stronger model and point it at that note and the working tree.

## Parallel agents

### 7. Count the tokens your subagents burn

Anthropic's write-up of [its multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) gives a rough multiplier: agents use about 4× the tokens of a chat, and multi-agent systems about 15×. The same post notes that most coding tasks parallelize less well than research does. Claude Code's [cost docs](https://code.claude.com/docs/en/costs) put agent teams at roughly 7× the tokens of a standard session when teammates run in plan mode.

This is the one that cuts against my own advice. In May I told you to [use the Explore subagent liberally](/blog/stop-tuning-prompts-build-a-harness/), and for exploration I still would, since it keeps forty files of noise out of the main session.

But watch the bill. On Claude subscription plans, `/usage` now breaks recent usage down by subagents, skills, plugins, and MCP servers, so you can see where it went. An agent that starts a dozen helpers on its own is spending budget nobody approved. In [the parallel coding playbook](/blog/parallel-coding-playbook-for-pulumi/), the parallelism came from issues a human wrote, and that's how I'd keep it.

### 8. Skip the coordinator agent

The team-lead pattern is tempting: one agent assigns the work, and the others report back and message each other. Claude Code's own [agent teams](https://code.claude.com/docs/en/agent-teams) are still "experimental and disabled by default," and the research gives a reason not to rush.

[Giuseppe Destefanis and Tomaso Aste at UCL](https://arxiv.org/abs/2608.16801) tested the cheapest kind of coordinator, a prompt that names one agent the lead, across 1,902 graded Claude Code runs with teams of one to sixteen agents. It created no communication hub and no reliable improvement.

The clearest failure came from an eight-step invoice pipeline. With two or four agents it worked in nine of ten runs. With eight, one per step, it failed all ten on the same seam: whether to round at each step or once at the end. The agents discussed rounding in all ten runs. In the authors' words, "Talking more did not close an interface that nobody owned."

The tasks were synthetic Python and the coordinator was only a prompt label, but Walden Yan at Cognition [described the mechanism in 2025](https://cognition.com/blog/dont-build-multi-agents): "Actions carry implicit decisions, and conflicting decisions carry bad results." The rounding seam is that sentence with a test suite attached. A main agent that hands out self-contained tasks and collects the results is enough, as long as every interface between those tasks has an owner and the contract lives in a file. That's what stood out about GSD when I [compared orchestration frameworks in April](/blog/claude-code-orchestration-frameworks/): its orchestrator never touches source files and keeps state on disk.

## Checking the work

### 9. Plan the checks first, and keep the writer out of them

Two habits belong together: never let the model that wrote the code approve it, and plan the validation before any code exists. Anthropic's [best practices](https://code.claude.com/docs/en/best-practices) call the first one a writer/reviewer pattern, because "a fresh context improves code review since Claude won't be biased toward code it just wrote."

The best measurement of the second comes from [an evaluation of Leni](https://arxiv.org/abs/2607.17044), an AI business analyst, written by the company that builds it and based on single runs. With that caveat, the breakdown is useful. Of the agent's 11-point gain on SpreadsheetBench Verified, scaffolding and prompting account for 9.5. The verification loop added the last 1.5 by rescuing six tasks, and when the model that produced the output also did the checking, it rescued two.

The code repair study in the next tip saw the same from the other side. Left to decide on its own when to stop, the model accepted 99.8% of its answers, and 29.5% of what it accepted was wrong. A gate on the visible tests cut that to 2.4%.

In [the loop post](/blog/stop-prompting-design-the-loop/) I said the model that wrote the code is far too generous grading its own homework. Review in a fresh session, and let a test suite or a build give a hard yes or no before anyone reads the change.

### 10. Stop revising once it passes

More rounds feel like more polish. [Gao, Yang, and Yang at Alibaba Cloud](https://arxiv.org/abs/2607.24604) tested that by forcing three revisions on each of 30 HumanEval repair tasks with a 7-billion-parameter open model. With test traces as feedback, 82.0% of runs were correct after the first revision, 67.3% after the second, and 69.3% after the third. About 85% found a correct patch at some point along the way, and 16.0% found one and then lost it, or 8.0% when the feedback was a plain pass or fail.

That's one loop in six throwing away a working fix, and the authors sum it up as "Iteration supplies proposals, not reliability." The paper also pins down one mechanism. Test output from an older version of the code misleads the model, and in one task a stale report from a version with a Caesar shift of 12 made it change the correct shift of 4 back to 12, in every seed.

The models were small, but the fixes are cheap. Commit as soon as the tests pass, so there's a last-known-good version to go back to. Rerun the tests on the current code before each revision. And cap the rounds instead of asking for one more pass to make it perfect.

## Where to start

If you have one afternoon, go in this order:

1. **Run a drift check on your rules files.** Read what it flags yourself.
1. **Cut the root file to what's specific and true.** Move the rest into skills or subdirectory files.
1. **Turn one rule into a hook.** For most teams, that's running the tests.
1. **Restart instead of compacting or escalating.** Write the handoff note yourself.
1. **Commit on green, and review in a separate session.**

{{< blog/cta-card title="Give your agent a hard yes or no" href="/docs/ai/" >}}
For infrastructure code, `pulumi preview` gives an agent a deterministic diff to check, and a mandatory policy blocks a noncompliant deployment. Wire those checks into Claude Code, Codex, Cursor, or Pulumi Neo with Agent Skills and the Pulumi MCP server.
{{< /blog/cta-card >}}

Treat the chat as disposable. Everything that has to survive it belongs on disk.
