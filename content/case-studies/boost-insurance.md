---
title_tag: Boost Insurance | Case Studies
title: "How Boost Insurance Eliminates Data Breach Risk with Pulumi"
allow_long_title: true
description: |
    Boost Insurance built a self-service platform with Pulumi that provisions ephemeral, time-bound environments in the cloud — meeting strict regulatory compliance and data residency requirements while keeping production data off developer laptops.
meta_desc: Boost Insurance uses Pulumi to meet regulatory compliance and data residency needs, keeping production data off laptops and eliminating breach risk.

customer_name: Boost Insurance
industry: financial-services
customer_logo: /logos/customers/boost-insurance.svg
customer_url: https://www.boostinsurance.com/

quote_block:
  quote: |
      "You're telling me I don't have to store 400 gigs worth of database backups on my laptop in order to debug production?"
  quote_attrib: Richard Genthner, CISO at Boost Insurance
  headline_stat: Zero
  headline: production data on developer laptops, eliminating breach risk

exec_summary: |
    [Boost Insurance](https://www.boostinsurance.com/) operates in one of the most heavily regulated industries in the United States. To debug production issues, developers had been downloading database snapshots to their laptops, bringing hundreds of gigabytes of sensitive data onto their personal machines. Boost's platform engineering team used Pulumi's Automation API, Pulumi Deployments, and Pulumi ESC to build a self-service platform enabling developers to provision isolated, time-limited database environments entirely in the cloud, ensuring production data no longer leaves Boost's controlled infrastructure and saving developers roughly 30 minutes per debugging session.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: The Challenge
      anchor: the-challenge
    - label: What Boost Built
      anchor: the-solution
    - label: Results
      anchor: results
    - label: How Pulumi Works
      anchor: how-pulumi-works
    - label: Conclusion
      anchor: conclusion
---

## The business challenge {#the-challenge}

Boost Insurance operates in one of the most heavily regulated industries in the United States.
Every policy the platform issues or binds — even a test policy — becomes a matter of record that
must be reported to regulatory bodies. That means production data can't be used for testing, and
reproducing production issues in a development environment is often impractical.

Developers needed access to production data to debug real-world issues, and the only option was
to download database snapshots to their laptops. For a 100 GB quoting database, that meant
45-minute downloads for remote team members, hundreds of gigabytes of sensitive data stored on
personal machines, and no guarantee that data stayed within the company's security perimeter.

"Someone goes and steals a developer's laptop — we now have a reportable breach," said Richard
Genthner, CISO at Boost Insurance. "We have to report not only to our partners, but to the state
of New York, all 50 states, and the federal government. We have to notify every single person
that's ever had a policy with us. It becomes a massive problem."

Boost has developers working remotely across multiple countries, and some partner contracts
explicitly require that data never leaves the United States — a strict data residency requirement.
Their existing access-control tooling handled credential management and query logging, but couldn't
solve the fundamental problem: production data was leaving the cloud and landing on laptops.

## What Boost built {#the-solution}

Boost's platform engineering team built an internal developer platform in Go that provisions
isolated, time-limited database environments entirely within the cloud. The platform uses
Pulumi's [Automation API](/docs/iac/concepts/automation-api/) to manage infrastructure
programmatically and offers developers three ways to interact with it: a web UI, a CLI, and a
desktop client.

When a developer needs to debug a production issue, they log into the platform, select a database
backup, and configure the environment — instance size, disk space, and a time-to-live ranging from
8 to 96 hours. The platform then provisions an isolated VPC with a Cloud SQL (PostgreSQL)
instance, restores the backup using Cloud SQL's native import API directly from a GCS bucket, and
sets up Identity-Aware Proxy (IAP)-protected routes with query logging for secure access.

The entire provisioning process takes about 15 minutes. When the TTL expires, the environment
tears itself down automatically.

## The results {#results}

The platform addresses some of Boost's most critical risks while delivering measurable
productivity gains:

- **Data breach risk eliminated.** Production data no longer leaves the cloud. Every isolated
environment lives within Boost's controlled GCP infrastructure, and data residency requirements
are satisfied by default. The scenario that kept leadership up at night — a stolen laptop triggering
a multi-state regulatory notification — is no longer possible.

- **30 minutes saved per developer per debugging session.** Restoring a database in the cloud takes
about 15 minutes, compared to 45 or more minutes for a remote developer to download and restore
locally. Across Boost's development team, that adds up to significant recovered engineering time.

- **Self-service replaces an operational bottleneck.** Before the platform, developers had to wait
for the platform engineering team to manually provision database environments. Now developers
create, extend, and tear down isolated environments on their own, freeing up the platform team to
focus on higher-value work.

- **Audit compliance built in.** Every database connection is routed through IAP-protected tunnels
with full query logging, maintaining the audit trail that insurance regulators require — the same
capability that the previous tooling provided, now integrated directly into the platform.

## How Pulumi makes it work {#how-pulumi-works}

Boost selected Pulumi because its feature set aligned with the specific requirements of a
self-service, compliance-focused platform.

The [Automation API](/docs/iac/concepts/automation-api/) is the foundation. By embedding Pulumi
directly in their Go application, the team could deliver a polished self-service experience — a web
UI, a CLI, and a desktop client — all backed by the same infrastructure-as-code logic, without
asking developers to learn Pulumi themselves.

[Pulumi Deployments](/docs/deployments/) and its [TTL stacks](/docs/deployments/concepts/ttl/)
feature keep costs predictable and close a security gap by making every environment temporary by
design. Each isolated database is provisioned with a configurable lifetime, and when it expires
Pulumi Deployments tears down the stack and all of its resources automatically — so no forgotten
environment lingers to accumulate cost or hold sensitive data.

[Pulumi ESC (Environments, Secrets, and Configuration)](/docs/esc/) shrinks Boost's attack surface
by eliminating long-lived service account keys. It issues short-lived, per-project credentials
across Boost's multi-project GCP environment using OIDC federation, and Pulumi Deployments consumes
them automatically when provisioning and destroying environments — keeping the credential lifecycle
fully automated.

[Pulumi Cloud](/docs/administration/) gives Boost's compliance team the audit records they need
without building custom logging infrastructure — exportable logs of every change across the
platform. It also provides centralized visibility into every active environment, with stacks,
resources, and update history in one place.

## Conclusion {#conclusion}

By building on Pulumi's infrastructure platform, Boost turned a serious
compliance liability into a self-service capability its developers actually enjoy using. Production
data stays inside Boost's controlled GCP infrastructure, isolated environments spin up in about 15
minutes and tear themselves down on schedule, and the audit trail regulators require is captured
automatically — all without needing to file a request to the platform team.

For any organization that has to reconcile fast developer access with strict data-handling
requirements, Boost's platform shows the two aren't at odds. With infrastructure as code as the
foundation, self-service and compliance reinforce each other rather than compete — freeing the
platform team to keep raising the bar instead of fielding one-off provisioning requests.
