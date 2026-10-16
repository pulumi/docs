---
title: "Your agent will try to be helpful. Make sure helpful can't reach prod"
allow_long_title: true
date: 2026-10-16
draft: false
meta_desc: "Coding agents try to be helpful, and sometimes that deletes prod. What our live workshop taught us about boxing in Pulumi Neo with Docker Sandboxes and ESC."
feature_image: feature.png
authors:
    - engin-diri
    - adam-gordon-bell
    - mike-coleman
tags:
    - ai
    - ai-agents
    - pulumi-neo
    - docker
    - security
    - esc
# Required: exactly one category (a scalar) from the closed set in
# data/blog_categories.yaml. Use "general" for posts that don't clearly fit a
# specific kind. Validated by `make lint`.
category: community
schema_type: auto
resource_links:
    - type: video
      url: https://www.youtube.com/watch?v=aTimO_kMS0c
      text: "Watch the recording"
    - type: github
      url: https://github.com/pulumi/workshops/tree/main/neo-in-a-docker-sandbox
      text: "Workshop repo"
    - type: github
      url: https://github.com/dirien/infrastructure-sandbox-kit
      text: "Infrastructure sandbox kit"
    - type: documentation
      url: /docs/ai/neo/pulumi-cli/
      text: "Neo in the CLI"
    - type: documentation
      url: https://docs.docker.com/ai/sandboxes/
      text: "Docker Sandboxes docs"
    - type: slack
      url: https://slack.pulumi.com/

# Social media copy, auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        An agent on a staging task used a token from an unrelated file and wiped a production volume in 9 seconds, PocketOS's founder says. Then it wrote: "I didn't verify."

        Engin Diri, Adam Gordon Bell, and Docker's Mike Coleman on boxing in Pulumi Neo.
    linkedin: |
        In April, a coding agent fixing a staging credential mismatch used a token it found in an unrelated file and deleted a production volume. PocketOS founder Jer Crane concluded: "System prompts are advisory, not enforcing."

        Engin Diri, Adam Gordon Bell, and Docker's Mike Coleman ran the Neo in a Docker Sandbox workshop. The recap covers Adam's explanation for why agents do this (in training, a deleted database scores the same as an unfinished task), what Pulumi Neo's modes actually limit (read-only stops Pulumi Cloud writes, not everything), and what changed in Docker Sandboxes since August: global secrets that now reach running sandboxes, sandbox environment files, and cloud sandboxes.
    bluesky: |
        Why would a capable coding agent delete prod? Adam Gordon Bell's answer: in training, a deleted database scores the same as an unfinished task.

        Engin Diri recaps the Neo in a Docker Sandbox workshop: the Pulumi controls, the sandbox boundaries, and what changed since August.
---

In April, a coding agent on a routine staging task for PocketOS deleted the company's production volume in 9 seconds. According to [founder Jer Crane's account](https://www.theregister.com/software/2026/04/27/cursor-opus-agent-snuffs-out-startups-production-database/5224442), it used an API token it found in an unrelated file. Its explanation afterward: "I guessed that deleting a staging volume via the API would be scoped to staging only. I didn't verify." Railway recovered the data two days later.

Crane's conclusion was "System prompts are advisory, not enforcing." That is the premise of Neo in a Docker Sandbox, the workshop Adam Gordon Bell and I ran with Mike Coleman from Docker. If the prompt can't stop an agent, the limits have to sit where the agent can't negotiate with them. So we gave [Pulumi Neo](/docs/ai/neo/) two layers. A Docker Sandbox runs it in its own microVM, routes every outbound connection through a proxy, and injects the Pulumi token on the way out, so Neo never sees the real credential. Pulumi decides what Neo may change and when it has to ask.

This post walks through that setup and the demo. For why YOLO mode belongs in a sandbox at all, see [my August post](/blog/sandboxing-coding-agents-yolo-mode/).

<!--more-->

**Mike Coleman** is a Principal Solutions Architect at Docker. Mike's running joke about agents is that "they want to be helpful".

In the workshop, he told a story about exactly that:

{{< say author="mike-coleman" >}}
So yeah, I think that's actually one of the cooler things, because the thing I talk to people about agents a lot is [that] they just really want to please you. I don't know how many times I've done a demo. We have some other features that are enterprise features around governance for MCP servers, for instance. And so I'll be demoing this enterprise feature, and I'll be like, "Can you write to my Notion page?" And there will be a policy applied to the sandbox that says it can't. But I have a connector enabled in Claude somewhere. And it's like, "Well, not with that MCP server, but I can use this thing over here to do it."

And so the more you can create an environment where these alternate avenues are roadblocked, the safer you're gonna be with agentic workflows. And that's where we're coming at with the sandboxes: how do we take something that is as powerful as an agent, allow it to run as close to its full potential as possible, but avoid a bunch of catastrophic things, like the examples you talked about, the deleted database.
{{< /say >}}

{{< youtube "aTimO_kMS0c" >}}

## A deleted database scores the same as a failed task

Adam's explanation of why a capable agent does this starts with how it's trained.

{{< say author="adam-gordon-bell" >}}
But it's just a plus one or a zero. In the training environment the LLMs are trained in, if you solve a task, you get one point. If you don't solve the task, you get zero. But there's no in-between. If you destroy the entire repo, if you delete prod, that's the same thing. You got the task or you failed the task. There's no asymmetric downside.

The big thing that happens when you're working with production data, when you're operating real things and have real customers, is [that] there is asymmetric downside. There's lots of ways that things can go worse. [With] existing benchmarks, no matter what you do, the worst you can get on any task is: you didn't complete it. But in the real world, some tasks have a catastrophic downside.
{{< /say >}}

Open recipes such as [DeepSWE](https://www.together.ai/blog/deepswe) do use exactly that 1-or-0 reward. Adam's answer is a matrix he uses himself, with side effects on one axis and blast radius on the other.

| Side effect | Adam's example | What Adam said |
| --- | --- | --- |
| None | Review or draft a pull request | The zone to stay in |
| Reversible | Mark a database row inactive | Can be legitimate when the blast radius is small, such as a staging environment you can recreate, depending on your risk profile |
| Irreversible | Drop a database row | Can be acceptable when very little can go wrong, such as deleting a GitHub branch while `main` is protected |

His rule is to let agents act only when there are no side effects, when someone reviews the change, or when there's an easy way to recover. The PocketOS agent started inside that box, in staging, and left it.

## Six questions before an agent gets your cloud account

I opened the workshop with these questions:

{{< say author="engin-diri" >}}
So let's go through some questioning: before we give an agent a cloud account, what should be fulfilled?

The agent: who is this acting as? So let's talk about the who. And the what: what is the agent allowed to change? Actually also very important. And when: when does it stop and ask? When does the human-in-the-loop approach [come in], which was promoted at the beginning of the whole [agentic] stuff? The human-in-the-loop pattern was very, very big, and everybody's like, "Hey, there should be always the human approving stuff."

And then it shifted a little bit when everything comes around the Ralph loop, loop engineering and so on. Asking was considered something which slows [you] down. But again, still something maybe very important. [Important] is also to answer the question: where does the agent actually run? Then the credentials question comes: with what? Which credentials does it hold?

And what stops it when it [goes] wrong? [...] So keep [these] questions as a loose guardrail.
{{< /say >}}

<figure>
    <img src="/blog/running-pulumi-neo-in-a-docker-sandbox/agent-cloud-account-six-questions.webp" alt="Six cards that ask who the agent acts as, what it may change, when it stops to ask, where it runs, which credentials it holds, and what stops it when it gets something wrong.">
    <figcaption><em>The six questions the workshop answered before handing an agent a cloud account.</em></figcaption>
</figure>

Pulumi answers who, what, when, and what stops it. The sandbox answers where, and it splits the credentials question with Pulumi ESC (Environments, Secrets, and Configuration).

## Pulumi controls that live outside the prompt

[`pulumi neo`](/docs/ai/neo/pulumi-cli/) runs Neo in your terminal (Essentials, Pro, and Enterprise editions). Its controls live in Pulumi:

1. **Neo runs as you.** It uses your `pulumi login` and [role-based access control (RBAC)](/docs/ai/neo/permissions/) permissions, and its file and shell tool calls run locally, here inside the sandbox.
1. **Approval mode sets when it asks.** `--approval-mode manual`, the default, asks before every tool call, `balanced` only before `pulumi up`, and `auto` never.
1. **Read-only blocks Pulumi Cloud writes only.** With `--permission-mode read-only`, Neo can't trigger writes such as `pulumi up`, but it can still open ESC environments and reach the cloud accounts behind them. To [keep it out of an environment](/docs/ai/neo/permissions/#esc-secrets-and-downstream-cloud-access), don't grant your user or role `environment:open` on it.
1. **`protect: true` guards against accidental deletes.** A deployment that would delete a [protected resource](/docs/iac/concepts/resources/options/protect/) fails. Protection can still be lifted with `protect: false` or `pulumi state unprotect`, or bypassed with `--ignore-protect`.
1. **Pulumi Policies blocks unsafe changes.** Mandatory policies in a [preventative policy group](/docs/discovery-governance/concepts/policy-as-code/policy-groups/) (Pro and Enterprise editions) run on every `pulumi preview` and `pulumi up`, Neo's included, and stop a violating change before anything reaches the cloud. The workshop's pack included `s3-no-public-acl`.
1. **Pulumi ESC replaces stored cloud keys.** It mints short-lived AWS credentials through [OpenID Connect (OIDC)](/docs/esc/guides/configuring-oidc/aws/) for each run. They still reach the CLI, so they limit a leak's damage rather than prevent it.

## What a Docker Sandbox isolates

Each agent gets its own microVM, kernel, and Docker Engine. Only the workspace is mounted (plus a read-only skills store for supported agents), but SSH agent forwarding is on by default. All outbound TCP goes through a host proxy that injects proxy-managed credentials such as the Pulumi token. The `sbx` CLI and local sandboxes are free; centralized sandbox, network, and Model Context Protocol (MCP) controls are part of Docker's paid AI Governance.

## What changed in Docker Sandboxes since August

Three changes matter here:

1. **Secrets are global and reach running sandboxes.** Since v0.38.0 (August 6), `sbx secret set pulumi` covers every sandbox whose kit asks for it. Since v0.45.0 (September 21), [changing a global secret](https://docs.docker.com/ai/sandboxes/configuration/credentials/) updates running sandboxes without a restart.
1. **Sandbox environment files (experimental).** An `sbxenv.yaml` captures a sandbox's agent, kits, workspace, ports, and credentials for `sbx env run`. Mike compared it to a dev container definition. Docker now says to keep [the file](https://docs.docker.com/ai/sandboxes/configuration/environment-files/) under version control but outside the mounted workspace, because it can run host commands.
1. **Cloud sandboxes (experimental).** [`sbx --cloud run claude`](https://docs.docker.com/ai/sandboxes/cloud/) runs the sandbox in Docker's cloud, so it keeps going after you close the laptop. It needs `sbx` 0.45.0 or later and a pay-as-you-go Docker Agentic Platform subscription. New signups get a [one-time $250 compute credit](https://www.docker.com/c/sbx-promo/), instead of $25, through October 31, 2026.

## Running Neo inside a Docker Sandbox

Here's the demo, condensed (every script is in the [workshop repo](https://github.com/pulumi/workshops/tree/main/neo-in-a-docker-sandbox)). Store the token on the host, then start the sandbox from [my kit](https://github.com/dirien/infrastructure-sandbox-kit) plus a mixin for the demo's AWS region:

```bash
sbx secret set pulumi
sbx run --name neo-demo --kit ./01-sandbox/region-kit \
    ghcr.io/dirien/infrastructure-sandbox-kit:v0.10.0 ./02-app
```

A GHCR kit needs `ghcr.io/dirien/` in `kit.allowedSources` first. Neo isn't a built-in `sbx` agent, so the sandbox opens a shell, where `pulumi whoami -v` works through the injected token while the variable holds a placeholder:

```bash
echo "$PULUMI_ACCESS_TOKEN"
```

```output
proxy-managed
```

From the host, the workshop's `boundaries.sh` checks a host the kit doesn't allow and one it does:

```bash
sbx policy check network --sandbox neo-demo ifconfig.me
sbx policy check network --sandbox neo-demo api.pulumi.com
```

Under Balanced or Locked Down the first is denied, and `sbx policy log neo-demo` shows what the proxy refused.

<figure>
    <img src="/blog/running-pulumi-neo-in-a-docker-sandbox/sbx-egress-default-deny.webp" alt="Three cards. The hosts the kit allows, the regional AWS endpoints a mixin kit adds for this sandbox, and &quot;no matching rule&quot;, which is blocked at the host proxy. Below them is the mixin's YAML allow-list.">
    <figcaption><em>Default-deny holds under the Balanced and Locked Down presets; the Open preset allows all traffic. Without organization governance, a request that matches no rule is blocked and queued for your approval (<code>sbx policy approval ls</code>). The kit's allow-list shown is an excerpt.</em></figcaption>
</figure>

Then start Neo:

```bash
pulumi neo
```

Inside the sandbox, I think auto approval mode is defensible for throwaway work. But allowed hosts, AWS included, still receive whatever Neo sends, and ESC's short-lived credentials do reach the CLI, so keep the Pulumi controls on. We'd planned a last step, Neo trying to tear the stack down and `protect: true` refusing, but we didn't get to it live.

## Where to start

In an informal poll I ran at the end of the workshop, 8 of the 11 people who voted said they don't currently use a sandbox for their agents. If that's you, start closed: pick [Locked Down](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/) when the first start asks for a network preset. Read the denials in the terminal dashboard (`sbx` with no subcommand) or with `sbx policy log`, then approve them or add rules with `sbx policy allow network <host>`.

On the Pulumi side, run Neo [read-only, or at least with balanced approval](/docs/ai/neo/permissions/), near production, and back the stack with an [ESC environment that uses OIDC](/docs/esc/guides/configuring-oidc/aws/).

{{< blog/card "/events/neo-in-a-docker-sandbox/" >}}

And if your agent has already been helpful in production, tell me in the [Pulumi Community Slack](https://slack.pulumi.com/). I'm still collecting these.
