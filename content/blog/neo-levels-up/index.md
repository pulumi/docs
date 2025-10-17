---
title: "Neo Gets Smarter: New Modes, CLI Access & Sonnet 4.5"

date: 2025-10-20

draft: false

meta_desc: Neo gets smarter with Operating Modes for flexible control, full CLI access to Pulumi and cloud tools, and Claude Sonnet 4.5 for complex infrastructure tasks.

meta_image: meta.png

authors:
    - neo-team

tags:
    - ai
    - ai-agents
    - platform-engineering
    - pulumi-neo

schema_type: auto

---

Neo just got significantly more capable. We've shipped three major updates: Operating Modes for flexible control, full ecosystem tool access, and Claude Sonnet 4.5 for better performance on complex infrastructure tasks.

<!--more-->

## You decide how much control you keep

The same action has different risks in different contexts. Building a new dev environment is low risk. Opening a PR that changes shared infrastructure requires more scrutiny.

Operating Modes let you adjust autonomy based on context:

* **Review Mode**: You approve the task plan, preview, and PR. You see everything before it happens.  
* **Balanced Mode**: Neo handles planning and previews. You approve mutating operations, such as updates or destroys. Less friction, control where it matters.  
* **Auto Mode**: Neo runs without stopping. For when you need speed and trust the outcome.

You can use Review Mode when Neo is updating production infrastructure. Use Balanced Mode when deploying application updates where you want to verify destructive changes but trust routine operations. Switch to Auto Mode when spinning up temporary dev environments for testing. You pick the mode that matches your situation. The same agent, flexible levels of autonomy.

## Neo can do more

Neo now has access to more tools and information. This means it can handle more complex scenarios and work with the broader ecosystem your infrastructure depends on.

* **Full Pulumi CLI access**: Neo can now run all Pulumi CLI operations, including stack imports, state management, and plugin operations that previously required manual intervention.

* **Ecosystem tooling built in**: Neo now includes kubectl, Helm, AWS CLI, GCP, and Oracle Cloud CLI. This means Neo can verify Kubernetes deployments, install Helm charts, and run cloud-specific operations without leaving your workflow.

* **Private registry search**: Your team builds reusable components to accelerate development and codify standards. Neo can now search your organization's private registry, including READMEs, to find and use them. You get the benefit of your team's existing work.

## Sonnet 4.5

Neo now runs on Anthropic's Sonnet 4.5 by default. Sonnet 4.5 delivers better performance on complex, multi-step infrastructure tasks that require sustained reasoning across multiple files and services.

## Try Neo

**Ready to try these features?**

* [Sign in to Pulumi Cloud](https://app.pulumi.com/signin?product=neo) and start a Neo task  
* [Read the Neo documentation](https://www.pulumi.com/docs/pulumi-cloud/neo/) for detailed guides  
* [Join the Community Slack](https://slack.pulumi.com/) to share feedback on the new features
