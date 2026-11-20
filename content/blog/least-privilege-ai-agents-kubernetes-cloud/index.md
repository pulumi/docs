---
title: "Least Privilege for AI Agents on Kubernetes and Cloud"
date: 2026-11-12
draft: false
meta_desc: "Give AI agents on Kubernetes and cloud infrastructure one privilege at a time: short-lived ESC credentials, namespace RBAC, policy as code, and approvals."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - ai-agents
    - ai
    - security
    - kubernetes
    - policy-as-code
    - esc
    - oidc
    - pulumi-neo
category: best-practices
schema_type: auto
faq_schema: true

social:
    twitter: |
        An agent that investigates a cluster needs read access. One that ships to production needs more, but not by default.

        A privilege ladder for agents on Kubernetes and cloud: scoped RBAC, short-lived OIDC credentials, policy as code.
    linkedin: |
        Most teams give an AI agent the same credentials they would give an engineer on call, then add an approval prompt and hope it catches the dangerous calls.

        A sturdier pattern is to treat each action as something the agent earns. Reading a cluster, previewing a change, applying to a dev stack, applying to production, and editing RBAC or IAM each get their own credential, scope, and gate. The credentials come from Pulumi ESC as short-lived OIDC sessions, the Kubernetes permissions are namespaced Roles with no wildcards, and a policy pack stops the one change an agent should never make alone: widening its own access.

        The post walks through the ladder, with ESC and Pulumi code you can adapt.
    bluesky: |
        Give an AI agent the privileges it needs for the next action, and nothing for the one after.

        A privilege ladder for agents on Kubernetes and cloud: scoped RBAC, short-lived OIDC credentials, policy as code.
---

Least privilege for an AI agent means granting it only the access needed for the action in front of it, using credentials that expire quickly, and requiring a policy check or a human before it moves up to a riskier action. For agents operating Kubernetes and cloud infrastructure, that works best as a ladder of separate credentials, one rung per kind of action.

<!--more-->

It is easy to start an agent with an engineer's access: someone exports a cloud profile or points a kubeconfig at it, and the agent can do whatever that engineer could. That is convenient for a demo. It is also the setup that turns one wrong tool call into an incident. [OWASP names the root causes of excessive agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) in LLM applications as one or more of excessive functionality, excessive permissions, and excessive autonomy, and a borrowed engineer identity supplies all three at once.

This post covers how to give agents that operate Kubernetes and cloud infrastructure, whether you use Pulumi Neo, a coding agent, or an MCP client, only the access each action needs. It focuses on the agent as an operator of your infrastructure. If you are hosting agents as workloads on a cluster, start with [how to run AI agents on Kubernetes with Pulumi](/blog/ai-agents-on-kubernetes/).

## Why aren't approval prompts enough for AI agents?

Approval prompts control when an agent asks before it acts. Permissions control what the agent can reach in the first place. Only the second one is a boundary, because a prompt that a person clicks through on the fortieth request has stopped being a control.

Pulumi's own documentation takes this position for Neo. Its permissions page says that [approval settings control when Neo asks before taking an action, and that approval does not grant additional access](/docs/ai/concepts/neo/permissions/). It also says that if you need Neo to stay within a boundary, you should set that boundary with permissions, meaning the user's RBAC and the ESC environments they can open, rather than relying on approval prompts to catch every access. OWASP gives the same advice for any LLM application: [implement authorization in downstream systems rather than relying on an LLM to decide if an action is allowed](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/). Approvals still matter for high-impact actions, and we will put them where they belong. They just sit on top of permissions.

## What is a privilege ladder for AI agents?

A privilege ladder is a list of the kinds of action an agent might take, ordered from least to most dangerous, with a separate credential and a separate gate for each. The agent starts on the bottom rung and moves up only when the task calls for it and the gate for that rung is satisfied.

| Rung | What the agent does | Cloud credential | Kubernetes access | Gate |
| --- | --- | --- | --- | --- |
| 1. Investigate | Reads state, logs, and events | Read-only role from a read-only ESC environment | `get`, `list`, `watch` in named namespaces | Environment Open on the read-only environment only |
| 2. Preview | Runs `pulumi preview` against proposed code | Same read-only role | Same read Role | Stack Read, plus policy packs run during preview |
| 3. Propose | Opens a pull request with the change | None for the cloud | None | Normal code review |
| 4. Apply to non-production | Runs the update on a dev or staging stack | Write role scoped to that account, from its own ESC environment | A deployer Role in that namespace | Mandatory policy packs, optional approval |
| 5. Apply to production | Runs the update on a production stack | Separate write role and ESC environment, short session | A deployer Role in production namespaces | Mandatory policy packs and human approval |
| 6. Change access | Edits RBAC, IAM, or trust policies | Not held by the agent | Not held by the agent | Policy block plus a named human approver |

Rungs 1 and 2 are where agents spend most of their time, and they never need write access. Rung 3 is the one that lets an agent propose a change without being able to make it. Neo can [propose changes to your IaC through a pull request](/docs/ai/concepts/neo/permissions/) instead of editing state directly. The rest of this post builds the rungs out.

## How do you give an agent short-lived cloud credentials?

Put each rung in its own Pulumi ESC environment, and have the environment log in to the cloud over OIDC. ESC's login providers [issue short-lived credentials for downstream services](/docs/esc/providers/login/), and OIDC is the recommended authentication mode wherever it is supported. For AWS, [Pulumi Cloud exchanges a short-lived OIDC token for temporary credentials by assuming an IAM role](/docs/esc/providers/login/aws-login/), so there are no long-lived keys for the agent to leak or for you to rotate.

Here is an environment for the investigation rung. It assumes a read-only role, binds the session to this environment through the OIDC subject, and attaches a managed policy so the session can never exceed read-only access, even if someone later broadens the role:

```yaml
# myorg/agents/read-only
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: arn:aws:iam::012345678912:role/agent-read-only
          sessionName: agent-investigate
          subjectAttributes:
            - currentEnvironment.name
          policyArns:
            - arn:aws:iam::aws:policy/ReadOnlyAccess
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}
    AWS_REGION: us-west-2
```

Three of those settings do the least-privilege work:

- **`subjectAttributes`** customizes the OIDC token's subject claim so the IAM role's trust policy can restrict which environments may assume it. A write role can then trust only the write environment, which means the read-only environment cannot borrow it. By default the subject follows the pattern `pulumi:environments:org:<org-name>:env:<project>/<environment>`, as the [OIDC configuration guide](/docs/esc/guides/configuring-oidc/) describes.
- **`policyArns`** attaches managed policies to the session. The effective permissions are the intersection of the role's permissions and those policies, so it grants a session strictly less than the role allows.
- **`duration`** caps how long the credentials live. Keep it short on higher rungs. The IAM role's own maximum session duration also applies, so check it when you set a number.

Google Cloud and Azure have equivalent [login providers](/docs/esc/providers/login/), so the same one-environment-per-rung layout carries across clouds.

Then control who can open each environment. Pulumi's [least-privilege guide](/docs/administration/guides/least-privilege/) calls opening an environment the sensitive action, because that is what resolves its secrets and credentials. Give the agent's identity Environment Open on the read-only environment and nothing on the write environments. If the agent runs through an org token via the [Pulumi MCP server](/docs/ai/guides/set-up-mcp-server/), the role assigned to that token is how you limit what the agent can see and do in Pulumi Cloud, whereas a personal access token acts as you everywhere.

For production writes, ESC [open approvals](/docs/esc/concepts/approvals/) enable just-in-time access patterns: the agent asks to open the write environment, a person approves, and the session lives for an hour or less. Approvals are available on the Pro and Enterprise editions.

## How do you scope what an agent can do inside a Kubernetes cluster?

Give each agent its own ServiceAccount, bind it to a namespaced Role, and keep the verbs and resources specific. The Kubernetes project's [RBAC good practices](https://kubernetes.io/docs/concepts/security/rbac-good-practices/) say minimal RBAC rights should be assigned to users and service accounts, that permissions should be assigned at the namespace level where possible with RoleBindings instead of ClusterRoleBindings, and that wildcard permissions should be avoided, especially across all resources. They also say to avoid cluster-admin.

Here is a Pulumi program for the investigation rung and the non-production deploy rung in one namespace:

```typescript
import * as k8s from "@pulumi/kubernetes";

const ns = "payments-dev";

const agent = new k8s.core.v1.ServiceAccount("ops-agent", {
    metadata: { name: "ops-agent", namespace: ns },
});

// Rung 1: read and diagnose. No Secrets, no writes.
const reader = new k8s.rbac.v1.Role("ops-agent-read", {
    metadata: { name: "ops-agent-read", namespace: ns },
    rules: [
        {
            apiGroups: [""],
            resources: ["pods", "pods/log", "services", "events", "configmaps"],
            verbs: ["get", "list", "watch"],
        },
        {
            apiGroups: ["apps"],
            resources: ["deployments", "replicasets"],
            verbs: ["get", "list", "watch"],
        },
    ],
});

new k8s.rbac.v1.RoleBinding("ops-agent-read", {
    metadata: { name: "ops-agent-read", namespace: ns },
    roleRef: { apiGroup: "rbac.authorization.k8s.io", kind: "Role", name: reader.metadata.name },
    subjects: [{ kind: "ServiceAccount", name: agent.metadata.name, namespace: ns }],
});

// Rung 4: a separate Role for the deploy step, bound only when that rung is in play.
export const deployerRole = new k8s.rbac.v1.Role("ops-agent-deploy", {
    metadata: { name: "ops-agent-deploy", namespace: ns },
    rules: [
        {
            apiGroups: ["apps"],
            resources: ["deployments"],
            verbs: ["get", "list", "watch", "patch", "update"],
        },
    ],
});
```

The Role leaves Secrets out on purpose, because `list` and `watch` on Secrets return their contents, so a read-only role that includes them is not read-only in practice. The deployer Role can patch Deployments in one namespace and cannot create RoleBindings, touch other namespaces, or delete anything.

Two details keep the rest of the chain short-lived. Kubernetes since v1.22 issues [short-lived, automatically rotated tokens through the TokenRequest API](https://kubernetes.io/docs/concepts/security/service-accounts/), so the agent should not use a long-lived ServiceAccount token Secret. And where an agent needs to run commands against a cluster, ESC can hand it a kubeconfig without leaving one on disk: with a cluster environment configured as in the [Kubernetes cluster access guide](/docs/esc/guides/integrate-with/kubernetes-cluster-access/), `pulumi env run <project>/<environment> -- kubectl get namespaces` opens the environment, renders the kubeconfig as a temporary file, sets `KUBECONFIG`, and runs the command. If you prefer to keep the agent's own identity low-powered, Kubernetes also supports impersonation, and its docs note that a low-privileged account with impersonation rights can avoid accidental modification of cluster resources.

## What stops an agent from widening its own access?

An agent that writes infrastructure code can write the RBAC and IAM that widen its own access, so those changes need a gate that does not depend on the agent's judgment. That makes "change access" the top rung, and the right gate is a mandatory policy that fails the deployment before anything changes.

[Pulumi Policies](/docs/discovery-governance/concepts/policy-as-code/) evaluates during `pulumi preview` and `pulumi up`, before anything changes in your cloud provider, and a violation of a mandatory policy stops the deployment. Here is a policy pack that rejects the two most common ways to hand out too much in Kubernetes: binding cluster-admin and writing wildcard verbs.

```typescript
import * as k8s from "@pulumi/kubernetes";
import { PolicyPack, validateResourceOfType } from "@pulumi/policy";

new PolicyPack("agent-access-guardrails", {
    policies: [
        {
            name: "no-cluster-admin-bindings",
            description: "Nothing may bind the cluster-admin ClusterRole.",
            enforcementLevel: "mandatory",
            validateResource: validateResourceOfType(
                k8s.rbac.v1.ClusterRoleBinding,
                (binding, _, reportViolation) => {
                    if (binding.roleRef.name === "cluster-admin") {
                        reportViolation("Binding cluster-admin requires a human-reviewed exception.");
                    }
                },
            ),
        },
        {
            name: "no-wildcard-role-verbs",
            description: "Roles must list verbs and resources explicitly.",
            enforcementLevel: "mandatory",
            validateResource: validateResourceOfType(
                k8s.rbac.v1.Role,
                (role, _, reportViolation) => {
                    for (const rule of role.rules ?? []) {
                        if ((rule.verbs ?? []).includes("*") || (rule.resources ?? []).includes("*")) {
                            reportViolation("Wildcard verbs or resources are not allowed in agent-managed Roles.");
                        }
                    }
                },
            ),
        },
    ],
});
```

Run it with `pulumi preview --policy-pack <path>`, or attach it through a policy group so it applies to the stacks and accounts you choose. The docs note that policy groups let you enforce stricter policies in production than in development, which maps neatly onto the ladder: advisory on a dev stack where you want to learn what agents attempt, mandatory everywhere an agent can reach production. The same idea extends to IAM, for example by rejecting policy documents that grant `*:*` or trust policies that name a broader principal. For the broader catalog of what policy checks catch, see [deployment guardrails with policy as code](/blog/deployment-guardrails-with-policy-as-code/).

Policy does not replace the human at this rung. When a pull request touches RBAC or IAM, route it to a named approver, and keep the agent's credentials from being able to apply that change on its own. OWASP's guidance is to [require a human to approve high-impact actions before they are taken](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/), and changes to access are the clearest example.

## How should an agent's permissions grow over time?

Start the agent on rung 1 and widen deliberately, one rung and one scope at a time. Neo's documentation recommends exactly this posture: [prefer read-only cloud roles in ESC environments and broaden them deliberately](/docs/ai/concepts/neo/permissions/). Neo also acts with the permissions of the person invoking it and never receives more access than that person has, so the ceiling is set by the user's RBAC and the environments they can open. Neo's read-only mode, covered in [Neo read-only mode](/blog/neo-read-only-mode/), is a good first deployment because it lets a team watch what an agent investigates before granting a single write.

A practical rollout looks like this:

1. Run the agent on the read-only environment for a few weeks and review what it opens and asks for in your [audit logs](/docs/administration/concepts/audit-logs/).
2. Add the preview rung, with advisory policy packs, so you see which proposals would have been blocked.
3. Enable non-production apply, with mandatory policy and a short session duration.
4. Add production only through an approval-gated ESC environment, with its own role, subject, and `policyArns`.

Isolation is a separate layer from privilege. If the agent also runs code on a laptop or runner, the [sandboxing guide for coding agents](/blog/sandboxing-coding-agents-yolo-mode/) covers keeping that environment contained, and ESC's [OIDC tokens for any service](/blog/esc-oidc-tokens-for-any-service/) extends the same short-lived pattern to the other APIs an agent calls.

## Frequently asked questions

### What is least privilege for AI agents?

Least privilege for AI agents means an agent holds only the permissions the current action requires, for as short a time as possible. In infrastructure work that translates to read-only credentials by default, separate credentials for writes, short-lived sessions instead of stored keys, and a human or policy gate before high-impact actions.

### Should an AI agent get cluster-admin to troubleshoot Kubernetes?

No. Troubleshooting needs `get`, `list`, and `watch` on a defined set of resources in the namespaces involved. Cluster-admin lets the agent change or delete anything, including the RBAC that limits it. Start with a namespaced read Role, and raise access only when a specific action needs it.

### How do short-lived credentials help with AI agents?

Short-lived credentials limit how long a leaked or misused credential is useful, and they remove the stored key that an agent could print into a log or send to a model. With ESC's OIDC login, the session expires on its own and nothing needs rotating.

### Do human approvals replace least privilege?

No. Approvals decide when an agent asks before it acts, and they are most useful for high-impact steps such as production applies and access changes. Permissions decide what the agent can do at all, so they have to be set first and approvals layered on top.

### How does this apply to Pulumi Neo?

Neo acts on behalf of the user who invokes it and can only do what that user could do. You shape its reach with the user's RBAC and the ESC environments they can open, choose between default and read-only permission modes, and pick a Review, Balanced, or Auto approval mode for how often it asks.

## Next steps

To try this with an agent on your own infrastructure, start with a read-only ESC environment and [Pulumi Neo](/product/neo/), then add rungs as your team gains confidence. You can [sign up for Pulumi Cloud](https://app.pulumi.com/signup) to create the environments and policy groups used in this post.
