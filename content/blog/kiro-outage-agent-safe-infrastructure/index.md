---
title: "What the Kiro Outage Teaches About Agent-Safe Infrastructure"
date: 2026-10-08
draft: false
meta_desc: "Amazon and its critics disagree on why Kiro deleted an environment, but both accounts point to the same fix: guardrails in the infrastructure layer."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - ai-agents
    - ai
    - policy-as-code
    - pulumi-neo
    - security
category: perspectives
schema_type: auto
faq_schema: true

# Social media copy: auto-posted to X, LinkedIn, and Bluesky when merged to master.
social:
    twitter: "An agent decided to delete and recreate an environment. Amazon says a misconfigured role was the cause. Either account leads to the same fix: an agent can do whatever its credentials and pipeline allow, so guardrails belong in your infrastructure layer. What that looks like:"
    linkedin: "In December 2025, an AWS engineer reportedly let the Kiro coding agent fix an issue, and the agent chose to delete and recreate the environment. Amazon says a misconfigured role was the cause, and the Financial Times reported it as an agent acting without intervention.\\n\\nBoth accounts agree on the mechanics: the agent could do exactly what its role allowed, and nothing structural stopped a destructive plan. We walk through what preview, mandatory policy, protect, approvals, and audit logs would each have done, and how to set them up today."
    bluesky: "An agent decided to delete and recreate an environment. Amazon says a misconfigured role was the cause. Either way, an agent can do whatever its credentials and pipeline allow, so the guardrails belong in the infrastructure layer. Here is what that looks like:"
---

In December 2025, AWS engineers reportedly let the Kiro agent fix an issue in Cost Explorer, and it chose to delete and recreate the environment, causing a 13-hour disruption in one China region. Amazon says the cause was a misconfigured role. Either way, an agent can do whatever its credentials and pipeline permit, so safety belongs in the infrastructure layer.

<!--more-->

## What happened in the Kiro outage

The Financial Times [reported in February 2026](https://www.ft.com/content/00c282de-ed14-4acd-a948-bc8d6bdb339d) that a 13-hour disruption affecting one AWS service followed engineers allowing Kiro, Amazon's agentic coding tool, to make changes. According to [The Register's summary of the report](https://www.theregister.com/2026/02/20/amazon_denies_kiro_agentic_ai_behind_outage/), Kiro opted to "delete and recreate the environment." [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/multiple-aws-outages-caused-by-ai-coding-bot-blunder-report-claims-amazon-says-both-incidents-were-user-error) added that the service was in parts of mainland China and that AI tools were treated as an extension of the user, with the same permissions and no secondary approval required.

Amazon [published its own account](https://www.aboutamazon.com/news/aws/aws-service-outage-ai-bot-kiro). It describes an "extremely limited event" affecting a single service, AWS Cost Explorer, in one of 39 regions, with no customer inquiries. It attributes the event to "misconfigured access controls," and says the same issue could occur with any developer tool or manual action. Amazon also says Kiro requests authorization before acting by default, but the engineer in this case held a role with broader permissions than expected.

Neither account disputes that Kiro was in the loop or that the environment was deleted. They disagree about where to place the cause. We are not in a position to settle that, and the rest of this post does not depend on it.

## What went wrong

Three conditions lined up, and each one is common in teams adopting coding agents.

1. **The agent inherited a human-sized role.** The agent acted with the permissions of the engineer driving it. When that role was broader than anyone intended, the agent's reach was broader too.
2. **A destructive plan ran without a gate.** "Delete and recreate" is a perfectly reasonable plan for a throwaway environment. Nothing in the path asked whether this was one, or whether a person had seen the plan before it ran.
3. **Nothing structural protected the resource.** The only defense was the agent choosing not to delete it. Choices made by a model are not a control.

The pattern predates Kiro. In July 2025, a Replit agent [deleted a production database during a code freeze](https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/). In 2026, a coding agent working in a Cursor session reportedly found an API token and [deleted a production volume and its backups in seconds](https://tech.yahoo.com/ai/claude/articles/violated-every-principle-given-ai-181500433.html). In each case the agent did what its access allowed.

Amazon's own remedy is instructive. It says additional safeguards include mandatory peer review for production access. That is a guardrail added outside the agent, which is the same conclusion you reach whether you call the incident an AI error or a user error. Fixing the role and adding a review gate both move the safety property out of the model's judgment and into the system.

## What would a guardrail have done here

Take the reported plan, delete and recreate an environment, and walk it through a governed Pulumi workflow.

- **Scoped credentials.** An agent working on a Cost Explorer issue does not need delete rights on production. With least-privilege, short-lived credentials, the destructive call fails at the cloud provider.
- **A preview that shows the damage.** [`pulumi preview`](/docs/iac/cli/commands/pulumi_preview/) lists every create, update, replace, and delete before anything happens. A plan that removes an environment shows up as a wall of deletes that a reviewer or a policy can act on.
- **A mandatory policy.** [Policy as code](/what-is/what-is-policy-as-code/) evaluates the planned resources and blocks the update at the `mandatory` enforcement level. No role or flag on the agent's side overrides it.
- **`protect` on stateful resources.** A resource marked [`protect`](/docs/iac/concepts/resources/options/protect/) cannot be deleted by any deployment, no matter who or what drives it. The engine returns an error instead.
- **Approval before apply.** A person reads the preview and approves the `up`, so a destructive plan has to get past someone who can see it.
- **An audit trail.** [Audit logs](/docs/administration/concepts/audit-logs/) record who, or which agent acting for whom, changed what.

Here is a mandatory policy that requires `protect` on common stateful AWS resources. Attach it to a policy group that targets your production stacks.

```typescript
import { PolicyPack, ResourceValidationPolicy } from "@pulumi/policy";

const statefulTypes = [
    "aws:rds/instance:Instance",
    "aws:dynamodb/table:Table",
    "aws:s3/bucket:BucketV2",
];

const protectStatefulResources: ResourceValidationPolicy = {
    name: "protect-stateful-resources",
    description: "Stateful resources in production must set protect: true.",
    enforcementLevel: "mandatory",
    validateResource: (args, reportViolation) => {
        if (statefulTypes.includes(args.type) && !args.opts.protect) {
            reportViolation(
                `${args.name} is a stateful resource and must set protect: true.`,
            );
        }
    },
};

new PolicyPack("agent-safe-production", {
    policies: [protectStatefulResources],
});
```

The policy also covers the escape route. If an agent edits a program to drop `protect` from a production database, the next update violates the policy and is blocked. If it removes the resource while it is still protected, the engine refuses to delete it. Removing the flag through a state edit takes separate credentials, which the scoped role withholds and the audit log records.

> "The smartest agent in the world still needs guardrails, audit trails, and policy enforcement to be trusted with production systems at scale, and that layer gets more valuable as agents get more capable, not less."
>
> Joe Duffy, Pulumi co-founder and CEO, in [The Agentic Infrastructure Era](/blog/the-agentic-infrastructure-era/)

| | Ungoverned agent workflow | Governed agent workflow |
| --- | --- | --- |
| Credentials | Inherits the engineer's full role | Scoped to the task, read-only by default |
| Plan visibility | Agent decides and acts | Preview shows every delete and replace |
| Destructive operations | Allowed if the role allows | Blocked by mandatory policy and `protect` |
| Approval | Optional or absent | Required before apply on production |
| Audit | Reconstructed after the fact | Recorded as the change happens |
| Recovery | Depends on backups nobody tested | Protected resources never leave the stack |

## How do you design for agent-safe infrastructure today

You can adopt these in order, and each step helps on its own.

1. **Give agents the narrowest role that finishes the task.** Start read-only, and grant write access per task. Pulumi [RBAC](/docs/administration/concepts/rbac/) controls what a user, and therefore an agent acting as that user, can do on each stack.
2. **Run every change through preview.** Make `pulumi preview` output a required artifact of any agent run, and treat a nonzero count of deletes or replaces as a stop sign. Our post on [sandboxing coding agents](/blog/sandboxing-coding-agents-yolo-mode/) covers keeping agents contained while they work.
3. **Write mandatory policies for destructive operations.** Start with the stateful resources you would be unable to rebuild. The [deployment guardrails post](/blog/deployment-guardrails-with-policy-as-code/) shows how to roll policies out across stacks.
4. **Set `protect` on stateful production resources**, and consider [`retainOnDelete`](/docs/iac/concepts/resources/options/retainondelete/) where the cloud resource must survive even if the Pulumi resource is removed.
5. **Require approval on the apply step.** Keep a person between the preview and `pulumi up`, and gate production credentials with [ESC approvals](/docs/esc/concepts/approvals/) where your pipeline allows.
6. **Review the audit log.** Look for agent-driven changes the same way you review human ones.
7. **Start agents in the most restrictive mode.** [Pulumi Neo](/product/neo/) supports approval workflows with human-in-the-loop controls. Its Review mode asks for approval before previews, updates, and pull requests, Balanced mode asks before updates, and Auto mode asks for nothing. Docs recommend starting with the most restrictive mode, and [read-only mode](/blog/neo-read-only-mode/) and [plan mode](/blog/neo-plan-mode/) tighten it further.

For the wider picture, see [what agentic infrastructure is](/what-is/what-is-agentic-infrastructure/).

## Frequently asked questions

### What caused the AWS Kiro outage?

The Financial Times reported that a 13-hour disruption to one AWS service followed engineers letting Kiro make changes, with the agent choosing to delete and recreate the environment. Amazon attributes the event to a misconfigured role that gave the engineer broader permissions than expected. Both accounts agree the agent acted within the access it had.

### Was the Kiro outage AI error or human error?

Reports and Amazon's response differ on the cause, and we cannot adjudicate it from outside. The practical lesson is the same under either reading. Narrow the role, show the plan before it runs, block destructive changes to stateful resources by policy, and require approval, so safety does not depend on any one actor's judgment.

### What is agent-safe infrastructure?

Agent-safe infrastructure limits what an AI agent can break regardless of what it decides to do. It combines least-privilege credentials, a reviewable preview of every change, mandatory policy checks, engine-level protection for stateful resources, approval before apply, and audit logs. The controls live in the infrastructure layer, not in the agent's prompt.

### How do you stop an AI agent from deleting production resources?

Combine several controls. Scope the agent's credentials so deletes fail, set `protect` on stateful resources so the Pulumi engine rejects any deployment that would delete them, enforce a mandatory policy that requires `protect` in production, and require human approval before apply. Audit logs then show every attempt.

### Should AI agents have production access?

Yes, with limits. Agents are most useful when they can preview and propose changes against real infrastructure. Give them read access by default, run changes through preview and policy, and keep a person approving production applies until your controls and audit history earn more autonomy.
