---
title: "10 tips to improve your coding agent game"
date: 2026-09-21
draft: false
meta_desc: "Ten coding agent habits checked against the research behind them, from AGENTS.md drift and /compact to model switching, subagents, and review."
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
        This summer, a run of arXiv papers put numbers on how coding agents behave: what they read, what survives /compact, and what a mid-task model switch costs.

        Engin Diri turned the research into ten tips. Agent instruction files rot: 23% of repositories in one sample referenced code that no longer existed. One /compact round kept about half of an agent's safety instructions. Escalating to a bigger model mid-task cost more than twice as much as starting with it in an AWS study, and a restart did better. And the model that wrote the code shouldn't be the one that approves it.
    bluesky: |
        Ten coding agent tips, each checked against the research.

        The most expensive habit on the list: escalating to a bigger model mid-task. In an AWS study on SWE-bench, restarting Opus from scratch cost less and solved more than handing it Haiku's transcript.
---

In May I told you to [trim the root instruction file until it fits on one screen](/blog/stop-tuning-prompts-build-a-harness/), and to back anything that needs a hard guarantee with a hook. In June I argued that [the model that wrote the code shouldn't be the one grading it](/blog/stop-prompting-design-the-loop/). Advice like that is cheap. This summer, a run of arXiv papers started measuring it.

Most of the numbers back those habits harder than I did. One cuts against something I wrote in that same May post, and I'll own that when we get there. Below are ten tips for working with any coding agent, each checked against what the research measured, which is sometimes narrower than the abstract suggests.

<!--more-->

Read side by side, the papers point one way. The chat with your agent is a lossy place to keep anything that matters. Nearly every fix below moves something out of the chat and into a file, a hook, a test, or a fresh session, which is what I meant in June by "the agent forgets, the repo does not." Now there's data on how much it forgets.

## Agent instructions

### 1. Write for the agent, not for a new hire

A new hire can take a vague convention and work out what it means from the code around it. An agent can't. It fills the gap with a guess, and the guess sounds confident. Anthropic's [docs on project instructions](https://code.claude.com/docs/en/memory) ask for instructions "concrete enough to verify," like "API handlers live in `src/api/handlers/`" instead of "Keep files organized."

One line in my own Go instructions says to wrap errors with `fmt.Errorf("...: %w", err)` and never discard one silently. An agent can follow that, and a reviewer can check it. Try doing either with "handle errors properly."

The instruction file is also where agents look first. A Peking University study by Zhijun Gao and Jing Chen [traced 557 real agent sessions](https://arxiv.org/abs/2608.20195) and sorted every documentation touch: instruction files and the agents' own working notes made up 60.5% of them, API references only 1.3%. The authors couldn't show that any particular writing style changes behavior, and most of their sessions came from Claude Code, so the style question is still open.

### 2. Treat agent instructions like code, because they rot

Specific instructions go stale. Rename a folder or swap a database, and the file keeps describing a codebase that no longer exists, which leaves the agent two options: burn turns reconciling the two, or believe the file.

How often does that happen? Christoph Treude and Sebastian Baltes [ran an existing documentation checker](https://arxiv.org/abs/2606.09090), DOCER, unchanged over 612 agent config files from 356 randomly sampled GitHub repositories. In 82 of those repositories, 23.0%, a file named a function, path, or script that has since vanished from the code. That's close to one in four.

The authors call the number a feasibility signal rather than a precise rate, and with good reason, since only 32 of the 50 flags they checked by hand were real. A second paper explains why rot piles up. Across 441 repositories, [73.8% of AI configuration files](https://arxiv.org/abs/2608.25241) were committed once and never touched again.

A crude version of the check, run in September against the AGENTS.md of the repository this blog is built from, flagged 37 of 124 path-like references. Nearly all were noise, mostly relative paths and files that live in other repositories. One wasn't. Since a dark mode change in June, the file had been pointing agents at a `docs-logo.html` partial that was never added to the repository.

The authors suggest running the check in CI, and DOCER already has a [GitHub Actions version](https://github.com/wesleytanws/DOCER_tool). In May I described [a `Stop` hook that drafts instruction-file updates](/blog/stop-tuning-prompts-build-a-harness/) at the end of every session, which catches drift while the diff behind it is still small. Either works if a human reads what it flags.

### 3. Keep AGENTS.md short, but don't delete it

The mistake I see most often is a root AGENTS.md that has grown into a small book. Every session pays for the whole thing. Anthropic's docs for Claude Code set a target of [under 200 lines per file](https://code.claude.com/docs/en/memory), because "longer files consume more context and reduce adherence." Codex [stops reading AGENTS.md files](https://learn.chatgpt.com/docs/agent-configuration/agents-md) once they add up to 32 KiB by default, and since v2.1.277, Claude Code [reads AGENTS.md directly](https://code.claude.com/docs/en/memory#agents-md) as well, which means one short file can now brief both agents.

The cleanest measurement of that cost comes from outside coding. Lodha and colleagues at Microsoft [followed a GPT-5 agent](https://arxiv.org/abs/2606.10209) that itemizes hotel expenses. When they trimmed the tool-call history it carried from step to step down to the last five calls, completion went up from 71.0% to 79.0%, and the agent used 63.9% fewer tokens doing it.

Closer to home, a team from ETH Zurich and LogicStar.ai [tested context files](https://arxiv.org/abs/2602.11988) with Claude Code, Codex, and Qwen Code. The files didn't measurably help. Neither the generated nor the developer-written ones produced a statistically significant gain in task success, and the generated ones raised inference cost by 20% or more. If an agent wrote your AGENTS.md and nobody has edited it since, you're paying for it without a measurable return.

Don't delete the file, though. [Denisov-Blanch and colleagues](https://arxiv.org/abs/2608.25241) followed 509 open-source repositories after they adopted coding agents, and among the agent-first ones, those with no committed AI configuration saw cognitive complexity grow 53%, against 27% for the ones with at least an instruction file. The authors call that hypothesis-generating rather than causal. It's still a good reason to keep the file, and to prune it with the question Anthropic's [best practices](https://code.claude.com/docs/en/best-practices) suggest for every line: "Would removing this cause Claude to make mistakes? If not, cut it." Whatever survives the cut but only matters for some tasks belongs in skills or subdirectory files that load when the work gets there.

## Long sessions

### 4. Don't let /compact carry your instructions

When a session gets long, `/compact` is the obvious move: summarize, free up the window, keep going. The research says to watch what you let it summarize.

A University of Passau team [ran real agent config files through several compactors](https://arxiv.org/abs/2608.22752), Claude Code's `/compact` on Sonnet 4.6 among them, with a prompt that asked to keep every safety instruction verbatim. After five rounds in a row, each halving the text, 10% of the safety instructions were left. That's the number in the abstract. The one to act on is the first round, where 53% survived, which means half the safety instructions were gone after a single pass, from a prompt that asked to keep them all.

Shiyang Chen [measured what agents do afterwards](https://arxiv.org/abs/2606.22528). Across seven models, one compaction raised policy violations from 0% to 30%, and to 59% for the worst two. Where the policy lived decided most of it. Policies in a preserved system message held, while the same policies given as a standing user instruction, a memory entry, or tool output decayed by 33 to 50 points. For DeepSeek-V4, a compacted policy did worse than no policy at all, because the summary kept the pending task and dropped the policy that constrained it.

Claude Code handles part of this for you. After `/compact`, it [re-injects its project-root instruction file from disk](https://code.claude.com/docs/en/context-window#what-survives-compaction), while anything you only typed into the chat gets summarized with the rest. AGENTS.md isn't on that list, so if your instructions live there, a [`SessionStart` hook that matches `compact`](https://code.claude.com/docs/en/hooks-guide#re-inject-context-after-compaction) is the documented way to put them back.

Summaries aren't useless. The expense agent from tip 3 did best, at 91.6%, when the tool calls it dropped were replaced by a summary, so they're fine for the trail of what happened. For a long task, though, a handoff note you write yourself beats a summary you can't inspect, and Anthropic's best practices already say to run `/clear` between unrelated tasks. In August I wrote that [prompt guardrails degrade with context length](/blog/sandboxing-coding-agents-yolo-mode/). These papers put numbers on that.

### 5. Use hooks for what must always happen

An instruction in a markdown file is a request. The model honors it most of the time, which is fine for naming conventions and not fine for anything that has to happen every time. Ask an agent to run the tests before it finishes and it usually will, but for tests, usually isn't enough. A `Stop` hook runs them every time and hands the failures back. Claude Code's [hooks guide](https://code.claude.com/docs/en/hooks-guide) calls that "deterministic control: certain actions always happen rather than relying on the LLM to choose to run them."

Chen's fix points the same way: pinning the policy outside the summary took about 47 tokens and brought violations back to 0%. A hook goes further still. It never enters the context, so compaction has nothing to drop. For infrastructure, [Pulumi Policies](/docs/discovery-governance/policy/) plays that role at the deployment boundary, where a mandatory policy blocks a noncompliant deployment no matter what the agent was told.

My own setup has two small guardrail hooks. One blocks destructive shell commands, and the other scans every edited file for secrets. Hooks also apply to you. I found that out while working on this post, when [rtk](https://github.com/rtk-ai/rtk), a `PreToolUse` hook I use to compress command output, collided with Claude Code's worktree isolation check. Every git command in the session was refused until I called git by its full path. That's the behavior you want for the checks that matter, and a good reason to keep the list of hooks short.

### 6. Don't switch to a bigger model mid-task

When a session goes sideways, it's tempting to type `/model`, pick the bigger one, and keep going. Don't. The transcript is already contaminated, and Drew Breunig has a name for it, [context poisoning](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html): an error "makes it into the context, where it is repeatedly referenced."

This tip has the strongest paper on the list. A group at AWS [ran all 500 SWE-bench Verified tasks](https://arxiv.org/abs/2608.24358) with a cheap model that hands over to a strong one partway through, Claude Haiku 4.5 to Opus 4.7 plus a GPT pair, across 58,000 runs. Handing over the full transcript recovered 47% of the gap between the two Claude models and 36% for GPT. It also cost more: $1.61 a task, against $0.72 for starting with Opus. Restarting Opus from scratch, even after paying for Haiku's wasted attempt, came to $0.90 and solved more.

When they dropped the transcript and kept only the file edits on disk, recovery climbed to 64% for Claude and 84% for GPT. If the task needs the big model, start with it. If you're already halfway in, write down what's done and where it's stuck, then open a new session on the stronger model and point it at that note and the working tree.

## Parallel agents

### 7. Count the tokens your subagents burn

Parallel agents burn tokens fast. Anthropic's write-up of [its multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) puts rough numbers on it: agents use about 4× the tokens of a chat, and multi-agent systems about 15×. The same post notes that most coding tasks parallelize less well than research does. Claude Code's [cost docs](https://code.claude.com/docs/en/costs) put agent teams at roughly 7× the tokens of a standard session when teammates run in plan mode.

This is the one that cuts against my own advice. In May I told you to [use the Explore subagent liberally](/blog/stop-tuning-prompts-build-a-harness/), and for exploration I still would, because a subagent that reads forty files to find the three that matter keeps all forty out of your main session.

But watch the bill. On Claude subscription plans, `/usage` now breaks recent usage down by subagents, skills, plugins, and MCP servers, so you can see where it went. An agent that starts a dozen helpers on its own is spending budget nobody approved. In [the parallel coding playbook](/blog/parallel-coding-playbook-for-pulumi/), the parallelism came from issues a human wrote, and that's how I'd keep it.

### 8. Skip the coordinator agent

The team-lead pattern is tempting. One agent assigns the work, the others report back and message each other, and you get to watch it all happen. Claude Code's own [agent teams](https://code.claude.com/docs/en/agent-teams) are still "experimental and disabled by default," and the research gives a reason not to rush.

Giuseppe Destefanis and Tomaso Aste at UCL [tested the cheapest kind of coordinator](https://arxiv.org/abs/2608.16801), a prompt that names one agent the lead, across 1,902 graded Claude Code runs with teams of one to sixteen agents. It created no communication hub and no reliable improvement.

The failure worth remembering came from an eight-step invoice pipeline. With two or four agents, it worked in nine of ten runs. With eight, one agent per step, it failed all ten, every time on the same seam: whether to round at each step or once at the end. The agents discussed rounding in all ten runs. It didn't help. As the authors put it, "Talking more did not close an interface that nobody owned."

The tasks were synthetic Python and the coordinator was only a prompt label, but Walden Yan at Cognition [described the mechanism in 2025](https://cognition.com/blog/dont-build-multi-agents): "Actions carry implicit decisions, and conflicting decisions carry bad results." The rounding failure is a clean example of that.

A main agent that hands out self-contained tasks and collects the results is enough, as long as every interface between those tasks has an owner and the contract lives in a file. That's the design that stood out in GSD when I [compared orchestration frameworks in April](/blog/claude-code-orchestration-frameworks/). Its orchestrator never touches source files and keeps its state on disk.

## Checking the work

### 9. Plan the checks first, and keep the writer out of them

Two habits belong together here. Decide before the first line of code how the work gets checked: which tools the agent uses to test itself, which tests it writes, which command proves the build, and what you'll look at when it says it's done. Then never let the model that wrote the code be the one that approves it. Anthropic's [best practices](https://code.claude.com/docs/en/best-practices) call that second habit a writer/reviewer pattern, because "a fresh context improves code review since Claude won't be biased toward code it just wrote."

The best measurement comes from an unusual source, [an evaluation of Leni](https://arxiv.org/abs/2607.17044), an AI business analyst, written by the company that builds it and based on single runs. Read it with that in mind. Of the agent's 11-point gain on SpreadsheetBench Verified, scaffolding and prompting account for 9.5. The verification loop added the last 1.5 by rescuing six tasks, and when the model that produced the output also did the checking, it rescued two.

The code repair study in the next tip saw the same thing from the other side. Left to decide on its own when to stop, the model accepted 99.8% of its answers, and 29.5% of what it accepted was wrong. A gate on the visible tests cut that to 2.4%.

In [the loop post](/blog/stop-prompting-design-the-loop/) I said the model that wrote the code is far too generous grading its own homework. The fix hasn't changed: review in a fresh session, and let a test suite or a build pass or fail the change before anyone, human or model, reads it.

### 10. Stop revising once it passes

More rounds feel like more polish. An Alibaba Cloud team [tested that](https://arxiv.org/abs/2607.24604) by forcing three revisions on each of 30 HumanEval repair tasks with a 7-billion-parameter open model. With test traces as feedback, 82.0% of runs were correct after the first revision, and the second revision knocked that down to 67.3%. The third only brought it back to 69.3%. About 85% found a correct patch at some point along the way, while 16.0% found one and then lost it, or 8.0% when the feedback was a plain pass or fail.

That's one loop in six throwing away a working fix. The authors' summary is blunt: "Iteration supplies proposals, not reliability." They also pin down one mechanism worth knowing, which is that test output from an older version of the code misleads the model. In one task, a stale report from a version with a Caesar shift of 12 made it change the correct shift of 4 back to 12, and it did so in every seed.

The models were small, but the fixes are cheap. Commit the moment the tests pass, so there's a last-known-good version to go back to. Rerun the tests on the current code before each revision instead of feeding back output from three edits ago. And cap the rounds. One more pass to make it perfect is how a working fix gets lost.

## Where to start

If you have one afternoon, go in this order:

1. **Run a drift check on every AGENTS.md you have.** Read what it flags yourself.
1. **Cut the root file to what's specific and true.** Move the rest into skills or subdirectory files.
1. **Move one must-run step into a hook.** For most teams, that's running the tests.
1. **Restart instead of compacting or escalating.** Write the handoff note yourself.
1. **Commit on green, and review in a separate session.**

{{< blog/cta-card title="Check infrastructure changes before they ship" href="/docs/ai/" >}}
For infrastructure code, `pulumi preview` gives an agent a deterministic diff to check, and a mandatory policy blocks a noncompliant deployment. Wire those checks into Claude Code, Codex, Cursor, or Pulumi Neo with Agent Skills and the Pulumi MCP server.
{{< /blog/cta-card >}}

Start with the drift check. Nearly three quarters of AI configuration files never get a second commit, so yours is probably overdue.
