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

In May I told you to [trim the root instruction file until it fits on one screen](/blog/stop-tuning-prompts-build-a-harness/). I also said anything that needs a hard guarantee belongs in a hook. In June I argued that [the model that wrote the code shouldn't be the one grading it](/blog/stop-prompting-design-the-loop/). Several papers published this summer tested related questions.

Most of the findings support that advice, while the research on subagent costs calls for more caution. Below are ten tips for working with any coding agent. Each one is checked against what the research measured, which is sometimes narrower than the abstract suggests.

<!--more-->

Instructions kept only in chat can disappear during summarization. Nearly every fix below moves something out of the chat and into a file, a hook, a test, or a fresh session. That's what I meant in June by "the agent forgets, the repo does not."

## Agent instructions

### 1. Write for the agent, not for a new hire

A new hire can ask a teammate what a vague convention means. An agent may proceed with an interpretation you never intended. Anthropic's [docs on project instructions](https://code.claude.com/docs/en/memory) ask for instructions "concrete enough to verify," like "API handlers live in `src/api/handlers/`" instead of "Keep files organized."

One line in my own Go instructions says to wrap errors with `fmt.Errorf("...: %w", err)` and never discard one silently. An agent can follow that, and a reviewer can check it. Try doing either with "handle errors properly."

The instruction file is also where agents look first. A Peking University study by Zhijun Gao and Jing Chen [traced 557 real agent sessions](https://arxiv.org/abs/2608.20195) and sorted every documentation touch. Instruction files and the agents' own working notes made up 60.5% of them, and API references only 1.3%. The authors couldn't show that any particular writing style changes behavior. Most of their sessions also came from Claude Code, so the style question is still open.

### 2. Treat agent instructions like code, because they rot

Specific instructions go stale. Rename a folder or swap a database, and the file keeps describing a codebase that no longer exists. The agent then has two options: burn turns reconciling the two, or believe the file.

How often does that happen? Christoph Treude and Sebastian Baltes [ran an existing documentation checker](https://arxiv.org/abs/2606.09090), DOCER, unchanged over 612 agent config files from 356 randomly sampled GitHub repositories. In close to one in four of those repositories, a file named a function, path, or script that had since vanished from the code.

The authors call the number a feasibility signal rather than a precise rate. That's fair, since only 32 of the 50 flags they checked by hand were real. A second paper explains why rot piles up. Across 441 repositories, [73.8% of AI configuration files](https://arxiv.org/abs/2608.25241) were committed once and never touched again.

A crude version of the check ran in September against the AGENTS.md of the repository this blog is built from. It flagged 37 of 124 path-like references. Nearly all were noise, mostly relative paths and files that live in other repositories. One wasn't. Since a dark mode change in June, the file had been pointing agents at a `docs-logo.html` partial that was never added to the repository.

The authors suggest running the check in CI, and DOCER already has a [GitHub Actions version](https://github.com/wesleytanws/DOCER_tool). In May I described [a `Stop` hook that drafts instruction-file updates](/blog/stop-tuning-prompts-build-a-harness/) at the end of every session. It catches drift while the diff is still small. Either works if a human reads what it flags.

### 3. Keep AGENTS.md short, but don't delete it

The mistake I see most often is a root AGENTS.md that has grown into a small book loaded into every session. Anthropic's docs for Claude Code set a target of [under 200 lines per file](https://code.claude.com/docs/en/memory), because "longer files consume more context and reduce adherence." Codex [stops reading AGENTS.md files](https://learn.chatgpt.com/docs/agent-configuration/agents-md) once they add up to 32 KiB by default. Since v2.1.277, Claude Code [reads AGENTS.md directly](https://code.claude.com/docs/en/memory#agents-md) as well, so one short file can now brief both agents.

The cleanest measurement of that cost comes from outside coding. Lodha and colleagues at Microsoft [followed a GPT-5 agent](https://arxiv.org/abs/2606.10209) that itemizes hotel expenses. They trimmed the tool-call history it carried from step to step down to the last five calls. Completion went up from 71.0% to 79.0%, and the agent used 63.9% fewer tokens doing it.

Closer to home, a team from ETH Zurich and LogicStar.ai [tested context files](https://arxiv.org/abs/2602.11988) with Claude Code, Codex, and Qwen Code. The files didn't measurably help. Neither the generated nor the developer-written ones produced a statistically significant gain in task success. The generated ones also raised inference cost by 20% or more.

Don't delete the file, though. [Denisov-Blanch and colleagues](https://arxiv.org/abs/2608.25241) followed 509 open-source repositories after they adopted coding agents. Among the agent-first ones, those with no committed AI configuration saw cognitive complexity grow 53%. The ones with at least an instruction file grew 27%. The authors call that hypothesis-generating rather than causal.

It's still a good reason to keep the file and prune it instead. Anthropic's [best practices](https://code.claude.com/docs/en/best-practices) suggest one question for every line: "Would removing this cause Claude to make mistakes? If not, cut it." Whatever survives the cut but only matters for some tasks belongs in skills or subdirectory files that load when the work gets there.

## Long sessions

### 4. Don't let /compact carry your instructions

When a session gets long, `/compact` is the obvious move: summarize, free up the window, keep going. The research says to watch what you let it summarize.

A University of Passau team [ran real agent config files through several compactors](https://arxiv.org/abs/2608.22752), including Claude Code's `/compact` on Sonnet 4.6. The prompt asked them to keep every safety instruction verbatim. After five rounds in a row, each halving the text, 10% of the safety instructions were left. After just one round, 53% survived, despite the prompt asking to preserve them all.

Shiyang Chen [measured what agents do afterwards](https://arxiv.org/abs/2606.22528). Across seven models, one compaction raised policy violations from 0% to 30%, and to 59% for the worst two.

Where the policy lived decided most of it. Policies in a preserved system message held. The same policies given as a standing user instruction, a memory entry, or tool output decayed by 33 to 50 points. For DeepSeek-V4, a compacted policy did worse than no policy at all. The summary kept the pending task and dropped the policy that constrained it.

Claude Code handles part of this for you. After `/compact`, it [re-injects its project-root instruction file from disk](https://code.claude.com/docs/en/context-window#what-survives-compaction). Anything you only typed into the chat gets summarized with the rest. AGENTS.md isn't on that list, so if your instructions live there, a [`SessionStart` hook that matches `compact`](https://code.claude.com/docs/en/hooks-guide#re-inject-context-after-compaction) is the documented way to put them back.

Summaries aren't useless. The expense agent from tip 3 did best, at 91.6%, when a summary replaced the tool calls it dropped. Summaries are fine for the trail of what happened.

The better habit is to keep each task small enough that the session never needs compacting. Anthropic's best practices already say to run `/clear` between unrelated tasks. When a task runs long anyway, a handoff note you write yourself beats a summary you can't inspect. In August I wrote that [prompt guardrails degrade with context length](/blog/sandboxing-coding-agents-yolo-mode/), and compaction is one way that happens.

### 5. Use hooks for what must always happen

An instruction in a markdown file is a request. The model honors it most of the time. That's fine for naming conventions, and not fine for anything that has to happen every time. Ask an agent to run the tests before it finishes and it usually will. A `Stop` hook runs them every time and hands the failures back. Claude Code's [hooks guide](https://code.claude.com/docs/en/hooks-guide) calls that "deterministic control: certain actions always happen rather than relying on the LLM to choose to run them."

Chen's fix points the same way: pinning the policy outside the summary took about 47 tokens and brought violations back to 0%. A hook goes further still. It never enters the context, so compaction has nothing to drop. For infrastructure, [Pulumi Policies](/docs/discovery-governance/policy/) plays that role at deploy time: a mandatory policy blocks a noncompliant deployment, whatever the agent was told.

My own setup has two small guardrail hooks. One blocks destructive shell commands, and the other scans every edited file for secrets. While I was working on this post, [rtk](https://github.com/rtk-ai/rtk), a `PreToolUse` hook I use to compress command output, collided with Claude Code's worktree isolation check. Every git command in the session was refused until I called git by its full path. That's the behavior you want for the checks that matter, and a good reason to keep the list of hooks short.

### 6. Don't switch to a bigger model mid-task

When a session goes sideways, it's tempting to type `/model`, pick the bigger one, and keep going. Keeping the same transcript can carry earlier mistakes into the stronger model's attempt. Drew Breunig describes this as [context poisoning](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html): an error "makes it into the context, where it is repeatedly referenced."

This tip has the strongest paper on the list. A group at AWS [ran all 500 SWE-bench Verified tasks](https://arxiv.org/abs/2608.24358) with a cheap model that hands over to a strong one partway through. They tested Claude Haiku 4.5 to Opus 4.7 plus a GPT pair, across 58,000 runs. Handing over the full transcript recovered 47% of the gap between the two Claude models and 36% for GPT. It also cost more: $1.61 a task, against $0.72 for starting with Opus. Restarting Opus from scratch, even after paying for Haiku's wasted attempt, came to $0.90 and solved more.

When they dropped the transcript and kept only the file edits on disk, recovery climbed to 64% for Claude and 84% for GPT. If the task needs the big model, start with it. If you're already halfway in, write down what's done and where it's stuck. Then open a new session on the stronger model, and point it at that note and the working tree.

## Parallel agents

### 7. Count the tokens your subagents burn

Parallel agents burn tokens fast. Anthropic's write-up of [its multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) puts rough numbers on it. Agents use about 4× the tokens of a chat. Multi-agent systems use about 15×. The same post notes that most coding tasks parallelize less well than research does. Claude Code's [cost docs](https://code.claude.com/docs/en/costs) put agent teams at roughly 7× the tokens of a standard session when teammates run in plan mode.

The cost figures qualify my earlier advice. In May I told you to [use the Explore subagent liberally](/blog/stop-tuning-prompts-build-a-harness/), and for exploration I still would. A subagent that reads forty files to find the three that matter keeps all forty out of your main session.

On Claude subscription plans, `/usage` now breaks recent usage down by subagents, skills, plugins, and MCP servers, so you can see where it went. I prefer to decide which tasks get delegated before the agent starts spawning helpers. In [the parallel coding playbook](/blog/parallel-coding-playbook-for-pulumi/), the parallelism came from issues a human wrote, and that's how I'd keep it.

### 8. Skip the coordinator agent

The team-lead pattern is tempting. One agent assigns the work, the others report back and message each other, and you get to watch it all happen. Claude Code's own [agent teams](https://code.claude.com/docs/en/agent-teams) are still "experimental and disabled by default," and the research gives a reason not to rush.

Giuseppe Destefanis and Tomaso Aste at UCL [tested the cheapest kind of coordinator](https://arxiv.org/abs/2608.16801): a prompt that names one agent the lead. Their sample covered 1,902 graded Claude Code runs, with teams of one to sixteen agents. The coordinator created no communication hub and no reliable improvement.

The failure worth remembering came from an eight-step invoice pipeline, which worked in nine of ten runs with two or four agents. With eight, one agent per step, it failed all ten. Every failure sat on the same seam: whether to round at each step or once at the end. The agents discussed rounding in all ten runs. It didn't help. As the authors put it, "Talking more did not close an interface that nobody owned."

The tasks were synthetic Python, and the coordinator was only a prompt label. Still, Walden Yan at Cognition [described the mechanism in 2025](https://cognition.com/blog/dont-build-multi-agents): "Actions carry implicit decisions, and conflicting decisions carry bad results." The rounding failure is a clean example of that.

A main agent that hands out self-contained tasks and collects the results is enough. Give every interface between those tasks an owner, and write the contract into a file. That's what stood out in GSD when I [compared orchestration frameworks in April](/blog/claude-code-orchestration-frameworks/): its orchestrator never touches source files.

## Checking the work

### 9. Plan the checks first, and keep the writer out of them

Two habits belong together here. Decide before the first line of code how the work gets checked. Pick the tools the agent uses to test itself, the tests it writes, and the command that proves the build. Know what you'll look at when it says it's done.

The second habit is to never let the model that wrote the code approve it. Anthropic's [best practices](https://code.claude.com/docs/en/best-practices) call this a writer/reviewer pattern. Their reason: "a fresh context improves code review since Claude won't be biased toward code it just wrote."

The best measurement comes from an unusual source: [an evaluation of Leni](https://arxiv.org/abs/2607.17044), an AI business analyst. The company that builds Leni wrote it, and the results come from single runs, so read it with that in mind. Of the agent's 11-point gain on SpreadsheetBench Verified, scaffolding and prompting account for 9.5. The verification loop added the last 1.5 by rescuing six tasks, but only two when the model that produced the output did the checking.

The code repair study in the next tip saw the same thing from the other side. Left to decide on its own when to stop, the model accepted 99.8% of its answers, and 29.5% of what it accepted was wrong. A gate on the visible tests cut that to 2.4%.

Run the tests and build before review, then [review the change in a fresh session](/blog/stop-prompting-design-the-loop/).

### 10. Stop revising once it passes

An Alibaba Cloud team [tested repeated revision](https://arxiv.org/abs/2607.24604) by forcing three revisions on each of 30 HumanEval repair tasks with a 7-billion-parameter open model. With test traces as feedback, 82.0% of runs were correct after the first revision. The second revision knocked that down to 67.3%, and the third only brought it back to 69.3%. About 85% found a correct patch at some point along the way, while about one in six found one and then lost it. With plain pass-or-fail feedback, 8.0% found a correct patch and then lost it.

Test output from an older version of the code was one source of mistakes. In one task, the model read a stale report from a version with a Caesar shift of 12. It then changed the correct shift of 4 back to 12, in every seed.

The study used a small model, but the precautions are straightforward. Commit the moment the tests pass, so there's a last-known-good version to go back to. Rerun the tests on the current code before each revision instead of feeding back output from three edits ago. Set a retry limit for fixes that keep failing.

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

Start by checking the paths and commands in your root AGENTS.md. Fix anything stale, then remove instructions the agent doesn't need.
