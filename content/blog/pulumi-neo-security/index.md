---
title: "Neo Security: Securing Infrastructure in the Agentic Era"
date: 2026-08-28
meta_desc: "Pulumi Neo Security threat models and traces attack paths across your entire cloud estate. Find and fix problems before the bad actors do."
feature_image: feature.png
authors:
    - joe-duffy
tags:
    - ai
    - security
    - pulumi-neo
category: product
related_posts:
    - pulumi-context-api

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        Neo Security is our infrastructure security agent. It uses context about your full cloud estate—resources, semantics, code, reachability, runtime data, and more—to build a model of your estate and analyze it. Each finding is actionable thanks to IaC.
    linkedin: |
        Neo Security is our infrastructure security agent, now in research preview.

        Most security tooling reads your code, or scans your cloud, and reports what looks wrong. Neo Security uses everything Pulumi already knows about your estate: the resources actually deployed, the reference graph connecting them, the infrastructure code that created them where it exists, the permissions and firewall rules the cloud actually enforces, runtime data, and policy results.

        It builds a threat model out of all of that, then works through every point an attacker could use. It runs against your infrastructure regardless of how it was provisioned, across AWS, Azure, Google Cloud, Kubernetes, and thousands of other providers.

        Each finding is actionable thanks to IaC. Pulumi already declares and applies infrastructure change, so a proven finding comes back as a proposed diff and a pull request rather than a ticket.

        It is in research preview starting today and if you'd like a free scan to try it out, please get in touch.
    bluesky: |
        Neo Security is our infrastructure security agent. It uses context about your full cloud estate—resources, semantics, code, reachability, runtime data, and more—to build a model of your estate and analyze it. Each finding is actionable thanks to IaC.
---

Recently, AI systems have started turning up exploitable flaws in code that survived
decades of human review. The frontier labs have released useful tools to help uncover
many of these flaws through agent-led static code analysis.

This is a huge leap ahead, but cloud infrastructure has many exploitable flaws that code
analysis alone cannot find. These flaws are often as severe as the ones in code, or
worse, and they await discovery by malicious agents on offense. We realized recently we
can uniquely help here. At Pulumi, we have complete visibility into your entire cloud estate:
infrastructure resources, their semantics, connections and dependencies between them,
runtime logs and information, and more -- and have built an entire context graph out of them that is accessible to agents.

Thanks to large language models, the cost of analyzing that full context graph is no longer prohibitive.
As a result, today we're opening a research preview of **Pulumi Neo Security**. Neo Security
is an agent that can find exploitable flaws in your cloud infrastructure. It starts with a threat model of your cloud estate, and then works
systematically through every potential point of attack. The result is a security posture
report that is immediately actionable thanks to Pulumi's infrastructure as code technology.

Neo Security works on your existing infrastructure regardless of how it was provisioned, across
any of our thousands of cloud providers including AWS, Azure, Google Cloud, and
Kubernetes.

We're releasing it in research preview to begin, so we can work closely with customers to
run and address any findings. If you'd like to give it a try, [contact us](/contact/).

<!--more-->

## How it finds attack paths

Neo Security's aim is to provide a high-confidence, actionable security posture report.
It does so as follows:

**It builds a threat model before it looks for anything.** It works out what
your crown jewels are, which resources are accessible to outside actors, which accounts
hold production data, where the trust boundaries sit between the internet, your workloads,
and the identities those workloads carry, and which attackers are realistic for your
organization. This is what gives it relative risk and blast radius. Without it, a
development sandbox would be treated the same as a production database.

**Then it looks for attack vectors rather than resources.** Working from that threat
model, it maps internet entry points, federation and trust relationships, workload
identity, lateral movement between accounts, data and secret reachability, and the ways
those combine. The goal is to find, for each misconfiguration, the worst outcome it
enables.

**It pulls together six planes of evidence at once.** Each plane lives in a
different system, and Neo has visibility into all of them:

- **Resource inventory.** The discovered infrastructure inventory across all cloud accounts,
  regions, and resource types. For example: AWS S3 buckets and EC2 VMs, GKE clusters and
  the Kubernetes resources within them, Azure functions, Cloudflare CDNs, Snowflake data
  warehouses, and even hybrid and private cloud resources. This includes resources provisioned outside of IaC.
- **The reference graph.** This tells Neo which workload carries which identity, which identity reaches
  which data, and which stack manages which discovered resource. Neo Security reads this
  plane through the [Context API](/blog/pulumi-context-api/) we shipped earlier this
  week: a single query walks relationships across the estate and returns every result
  with the path that reached it.
- **Intent.** When available, Neo reads the infrastructure code that
  created a resource, whether Pulumi or Terraform IaC, for the semantics a cloud API doesn't
  know about: comments surrounding resources, the resource declarations and relationships,
  logic and naming, code commit and review history, and more.
- **Runtime state.** Information that isn't statically known from code and
  infrastructure metadata. This includes logs and metrics, uptime information and boot logs
  for servers, network traffic, and more. This is enabled by Neo having access to any tools
  a platform engineer would.
- **Policy and compliance results.** Pulumi's [discovery and
  governance](/product/discovery-governance/) capabilities ship over 150 built-in
  policies, many of them security rules, mapped to CIS Controls, NIST SP 800-53,
  HITRUST CSF, and PCI DSS. Enterprises can also write their own. Neo Security uses
  existing scanned resources and their violations as well as the policy definitions
  to discover potential risks in the infrastructure beyond known violations.
- **The provider's own answers.** Some questions configuration cannot settle, so Neo
  asks the cloud directly: Access Analyzer for external reachability, public-access checks
  on storage, and policy simulation for whether a principal can actually perform an
  action. This is what resolves the permissions and firewall rules that survive once every
  overlapping rule, boundary, and service control policy has been applied.

Neo uses this information to build a model of your estate and home in on validated paths,
proving and refuting attack vectors, and prioritizing based on severity and confidence. The
result is a short list, each entry carrying its evidence and, where source is available, a
fix as specific lines of code. The analysis deeply understands each cloud's identity model, networking, and data services
well enough to resolve effective permissions and firewall rules and to ask the providers
directly. The assessment phase is read-only throughout.

## Findings become pull requests

Most security tools stop at telling you something is wrong, which leaves the hardest part
— remediation — as an exercise for the reader. Pulumi already declares and applies
infrastructure change, so a proven finding becomes a proposed diff, a preview of what
would change, and a pull request for a person to review. Remediation is the only part that
writes anything, and only ever a proposed change in a repository, with deployment left to
your existing reviewed workflow.

## What a report looks like

We have worked with several teams to run Neo Security against real production estates of different shapes and
maturity, and it repeatedly found critical vulnerabilities the owners did not know
existed. A single run reconciles thousands of managed resources against the account's
discovered inventory across every region in use.

Here are example findings, anonymized and generalized from real runs:

| # | Finding | Severity | Confidence |
|---|---------|----------|------------|
| 1 | Deployment federation role grants administrator access with no subject-claim condition | critical | high |
| 2 | Build role trusts source-control OIDC with a wildcard on the branch claim | high | confirmed |
| 3 | Build policy grants `iam:AttachRolePolicy` on every role in the account | high | confirmed |
| 4 | Test Kubernetes cluster API endpoint reachable from any address | high | confirmed |
| 5 | Security groups named for production allow all TCP and SSH from `0.0.0.0/0` | high | confirmed |
| 6 | Public compute instance with IMDSv1 and suspected secrets in user data | high | medium |
| 7 | Load balancer HTTP listener forwards API requests without enforcing TLS | medium | high |
| 8 | CDN connects to its origin over HTTP-only, exposing auth headers in transit | medium | high |
| 9 | Static access key for the mail-sending user, unrotated for over a year | medium | high |
| 10 | Mail-sending policy allows send-as on any verified identity | medium | high |
| 11 | Database snapshot shared with an account outside the organization | medium | confirmed |
| 12 | Analytics tool auto-provisions any account on the corporate domain | medium | medium |
| 13 | No management-plane audit trail defined in IaC | low | high |
| 14 | No WAF on the internet-facing load balancer or CDN | low | high |

The implications of these example findings range from complete production account take-over, to
poor encryption practices that put sensitive data at risk, to improperly authenticated
email services that could be abused for phishing campaigns, to static unrotated keys that
leave the account open to risks should it leak, and many other unfortunate outcomes. Each
comes with a severity and risk so you can prioritize accordingly, and Neo works to exclude
disproven findings and those without consequence.

## Getting a scan

We have been impressed what the combination of the latest frontier models, the unique context
Pulumi has across several dimensions of your infrastructure, and giving the agent deep security
domain expertise have been able to produce. We hope it helps the world of infrastructure get more secure.

Pulumi Neo Security is open now to a small group of invited customers, and the initial scan
is free during the research preview. We're looking for estates with real complexity and risk:
multi-cloud and multi-account, a good mix of resource types, IaC and non-IaC resources,
and those for which their infrastructure security is paramount.

Attackers are going to point agents at cloud infrastructure next. We would rather you find
these problems first and we want to help. If you want to try a scan, [get in touch](/contact/).
