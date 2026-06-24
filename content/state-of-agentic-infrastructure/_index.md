---
title: State of Agentic Infrastructure 2026
meta_desc: How 510 platform, DevOps, and product engineers use AI agents in infrastructure today, and where they expect things to go over the next six months.
meta_image: /images/state-of-agentic-infrastructure/meta.png

hero:
  eyebrow: State of
  title: Agentic Infrastructure
  year: "2026"
  intro: |
    We surveyed 510 platform, DevOps, and product engineers to find out how AI agents are actually
    showing up in infrastructure work today, and where teams expect things to go over the next six months.
  toc:
    - num: "01"
      label: Who we surveyed
      anchor: who-we-surveyed
    - num: "02"
      label: The infrastructure baseline
      anchor: the-infrastructure-baseline
    - num: "03"
      label: Agents in the workflow today
      anchor: agents-in-the-workflow-today
    - num: "04"
      label: AI in monitoring and operations
      anchor: ai-in-monitoring-and-operations
    - num: "05"
      label: The six-month outlook and sentiment
      anchor: the-six-month-outlook-and-sentiment

findings:
  overline: What we found
  points:
    - The people we surveyed don't sit where you'd expect—a third do infrastructure work from product and app teams, not a dedicated infra group.
    - Speed is no longer the problem. Teams ship fast; what they lack is control over consistency, cost, and security.
    - Agents are already everywhere in the workflow—only 4% use none—but a human still signs off before production.
    - "Confidence is outrunning controls: trust in agents is climbing faster than the governance around it, and teams expect even more agent-generated infrastructure within six months."

sections:
  - anchor: who-we-surveyed
    number: "01"
    title: Who we surveyed
    overview:
      key_insights:
        - Our respondents are hands-on practitioners—engineers spread across product, DevOps, platform, and ops teams rather than a single infrastructure group.
        - The sample centers on mid-sized software companies, not startups or large enterprises—teams with real scale but still moving fast.
      by_the_numbers:
        - 510 platform, DevOps, and product engineers
        - Product and app developers are the largest group (35%), ahead of DevOps (23%) and platform engineering (17%)
        - 65% work at companies of 201–5,000 people, and 65% are in Software / SaaS
      takeaway: Among the people we surveyed, infrastructure work reaches well beyond the infra team—a third sit on product or app development teams.
    questions:
      - id: Q1
        kind: bar-horizontal
        heading: Which best describes your team?
        options:
          - label: "Product / app development"
            percent: 35
            highlight: true
          - label: "DevOps"
            percent: 23
          - label: "Cloud / infra ops"
            percent: 17
          - label: "Platform engineering"
            percent: 17
          - label: "Security"
            percent: 6
          - label: "SRE"
            percent: 2

      - id: Q2
        kind: column-vertical
        heading: How large is your company?
        options:
          - label: "1–50"
            percent: 5
          - label: "51–200"
            percent: 16
          - label: "201–1,000"
            percent: 33
            highlight: true
          - label: "1,001–5,000"
            percent: 32
            highlight: true
          - label: "5,000+"
            percent: 14

      - id: Q3
        kind: bar-horizontal
        heading: What industry are you in?
        options:
          - label: "Software / SaaS"
            percent: 65
            highlight: true
          - label: "Financial services"
            percent: 7
          - label: "E-commerce / retail"
            percent: 7
          - label: "Healthcare"
            percent: 5
          - label: "Government / public sector"
            percent: 5
          - label: "Media / entertainment"
            percent: 3
          - label: "Other"
            percent: 8
            other: true

  - anchor: the-infrastructure-baseline
    number: "02"
    title: The infrastructure baseline
    overview:
      key_insights:
        - "These teams are mature and ship fast: quick deploy cadence and self-service platforms are already standard."
        - "But governance stays manual: review gates (61%) still outweigh policy-as-code in CI (54%)."
      by_the_numbers:
        - 82% deploy to production weekly or more often
        - "Multi-cloud is the norm: AWS 64%, Google Cloud 55%, Azure 45%"
        - 63% already run an internal developer platform or golden paths in production
      takeaway: "Speed is solved; control isn't. Only 7% cite slow provisioning. The real pain is consistency (28%), cost (24%), and security (20%)."
    questions:
      - id: Q5
        kind: bar-horizontal
        heading: Which cloud providers does your infrastructure run on today?
        options:
          - { label: "AWS", percent: 64, highlight: true }
          - { label: "Azure", percent: 45, highlight: true }
          - { label: "Google Cloud", percent: 55, highlight: true }
          - { label: "Cloudflare", percent: 28 }
          - { label: "On-prem/bare metal", percent: 9 }
      - id: Q6
        kind: column-vertical
        heading: How often do you deploy infrastructure changes to production?
        options:
          - { label: "Multiple times a day", percent: 18, highlight: true }
          - { label: "Daily", percent: 26, highlight: true }
          - { label: "Weekly", percent: 38, highlight: true }
          - { label: "Monthly", percent: 12 }
          - { label: "Less often", percent: 6 }
      - id: Q7
        kind: bar-horizontal
        heading: How do you handle policy and compliance in your infra pipeline?
        options:
          - { label: "Policy-as-code in CI", percent: 54 }
          - { label: "Manual review/approval gates", percent: 61, highlight: true }
          - { label: "Post-deploy scanning only", percent: 33 }
          - { label: "Manual process", percent: 41 }
          - { label: "No formal process", percent: 4 }
      - id: Q8
        kind: bar-horizontal
        heading: What's your biggest technical challenge in managing infrastructure?
        options:
          - { label: "Configuration drift", percent: 10 }
          - { label: "Secrets/security", percent: 20 }
          - { label: "Multi-environment consistency", percent: 28, highlight: true }
          - { label: "Cost management", percent: 24 }
          - { label: "Slow provisioning", percent: 7 }
          - { label: "Debugging failed applies", percent: 12 }
      - id: Q9
        kind: stacked-bar
        heading: How is infrastructure ownership structured on your team?
        options:
          - { label: "Dedicated platform/infra team", percent: 47, highlight: true }
          - { label: "Embedded in product teams", percent: 30 }
          - { label: "Fully self-service for developers", percent: 22 }
          - { label: "No clear ownership", percent: 2 }
      - id: Q10
        kind: stacked-bar
        heading: Do you have an internal developer platform or golden paths for provisioning?
        options:
          - { label: "Yes, in production", percent: 63, highlight: true }
          - { label: "Building one now", percent: 24 }
          - { label: "No plans", percent: 14 }

  - anchor: agents-in-the-workflow-today
    number: "03"
    title: Agents in the workflow today
    overview:
      key_insights:
        - The headline tools split by size—Claude Code is the favorite at companies under ~200, while Copilot's lead grows with headcount, reaching 70%+ in orgs of 1,000 or more.
        - Today's agents mostly review and advise rather than write—authoring infrastructure code trails every other use at 29%.
        - "81% let agents change production, but almost all of that is gated: \"with approval\" (62%) far outweighs \"autonomously\" (19%)."
      by_the_numbers:
        - Only 4% use no AI in their infrastructure workflow
        - AI shows up most in code review (70%), security scanning (56%), and cost optimization (52%)
        - GitHub Copilot (62%) and Claude Code (56%) lead the tools in use
        - 45% say agents already handle half or more of their infra work
      takeaway: Agents are everywhere in the workflow, but a human still signs off before production.
    questions:
      - id: Q11
        kind: bar-horizontal
        heading: Where are you using AI or agents in your infra workflow today?
        options:
          - { label: "Authoring IaC", percent: 29 }
          - { label: "Code review", percent: 70, highlight: true }
          - { label: "Docs/runbooks", percent: 43 }
          - { label: "Incident response", percent: 47 }
          - { label: "Cost optimization", percent: 52 }
          - { label: "Security scanning", percent: 56 }
          - { label: "None", percent: 4 }
      - id: Q12
        kind: bar-horizontal
        heading: Which AI tools do you use for infrastructure work?
        options:
          - { label: "Claude Code", percent: 56, highlight: true }
          - { label: "Cursor", percent: 22 }
          - { label: "GitHub Copilot", percent: 62, highlight: true }
          - { label: "Pulumi Neo", percent: 12 }
          - { label: "Codex", percent: 38 }
          - { label: "Devin", percent: 11 }
          - { label: "In-house agents", percent: 24 }
          - { label: "None", percent: 5 }
      - id: Q13
        kind: column-vertical
        heading: How much of your infrastructure work is done by agents?
        options:
          - { label: "0%", percent: 3 }
          - { label: "Under 25%", percent: 23 }
          - { label: "25–50%", percent: 30 }
          - { label: "50–75%", percent: 26, highlight: true }
          - { label: "75–90%", percent: 15, highlight: true }
          - { label: "90–99%", percent: 2, highlight: true }
          - { label: "100%", percent: 2, highlight: true }
      - id: Q15
        kind: stacked-bar
        heading: Do you let AI agents change production infrastructure?
        options:
          - { label: "Yes, autonomously", percent: 19 }
          - { label: "Yes, with approval", percent: 62, highlight: true }
          - { label: "Only in non-prod", percent: 9 }
          - { label: "No", percent: 10 }

  - anchor: ai-in-monitoring-and-operations
    number: "04"
    title: AI in monitoring and operations
    overview:
      key_insights:
        - Monitoring is one of the most widely adopted places for AI, led by anomaly detection.
        - "Autonomy stays gated even here: \"suggests fixes\" (37%) and \"remediates with approval\" (31%) are the common modes."
      by_the_numbers:
        - 64% already use AI for infrastructure monitoring; just 6% have ruled it out
        - Top uses are anomaly detection (57%), auto-remediation (45%), and predictive scaling (44%)
        - Just 12% run fully autonomous monitoring
      takeaway: "Even the most-adopted use case keeps a human in the loop: agents suggest, people approve."
    questions:
      - id: Q16
        kind: stacked-bar
        heading: Do you use AI for infrastructure monitoring?
        options:
          - { label: "Yes", percent: 64, highlight: true }
          - { label: "Evaluating", percent: 31 }
          - { label: "No", percent: 6 }
      - id: Q17
        kind: bar-horizontal
        heading: What do you use AI-driven monitoring for?
        options:
          - { label: "Anomaly detection", percent: 57, highlight: true }
          - { label: "Root-cause/triage", percent: 42 }
          - { label: "Predictive scaling", percent: 44 }
          - { label: "Drift detection", percent: 39 }
          - { label: "Cost anomalies", percent: 44 }
          - { label: "Auto-remediation", percent: 45 }
          - { label: "None", percent: 5 }
      - id: Q18
        kind: column-vertical
        heading: How autonomous is your AI monitoring?
        options:
          - { label: "Alerts only", percent: 20 }
          - { label: "Suggests fixes", percent: 37, highlight: true }
          - { label: "Remediates with approval", percent: 31, highlight: true }
          - { label: "Fully autonomous", percent: 12 }

  - anchor: the-six-month-outlook-and-sentiment
    number: "05"
    title: The six-month outlook and sentiment
    overview:
      key_insights:
        - Teams expect to hand agents more work—across the board, the share of infrastructure they expect agents to generate rises over the next six months.
        - 63% say they trust agents to make production changes, which runs ahead of the manual-approval reality from the earlier sections.
      by_the_numbers:
        - Teams expecting agents to generate 50% or more of their infra code rise from 45% today to 52% in six months
        - The "under 25%" group shrinks from 23% to 15%
        - 82% agree AI will meaningfully change how they write infrastructure within 12 months
        - 72% say proactive AI monitoring has reduced their incident volume
      takeaway: "Stated trust is outrunning real guardrails: 63% say they trust agents in production, yet almost every change still needs manual approval. The next six months are about closing that gap."
    questions:
      - id: Q14
        overline: "05.Q13 → Q14"
        kind: grouped-column
        heading: "Share of infrastructure code that is AI-generated, today vs. in six months"
        series:
          - Today
          - In six months
        categories:
          - { label: "0%", values: [3, 3] }
          - { label: "Under 25%", values: [23, 15] }
          - { label: "25–50%", values: [30, 31] }
          - { label: "50–75%", values: [26, 31] }
          - { label: "75–90%", values: [15, 14] }
          - { label: "90–99%", values: [2, 6] }
          - { label: "100%", values: [2, 1] }
      - id: Q19
        kind: diverging
        heading: How strongly do teams agree?
        scale:
          - Strongly disagree
          - Disagree
          - Neutral
          - Agree
          - Strongly agree
        statements:
          - { label: "AI and agents will meaningfully change how we write infrastructure within 12 months", values: [2.16, 2.75, 13.33, 53.53, 28.24] }
          - { label: "Our current tooling makes it easy to onboard a new engineer to our infrastructure", values: [2.16, 3.73, 20.20, 44.71, 29.22] }
          - { label: "Managed platforms have reduced our operational burden", values: [1.76, 6.86, 18.04, 49.61, 23.73] }
          - { label: "Proactive AI monitoring has reduced our incident volume", values: [3.14, 6.08, 19.22, 48.24, 23.33] }
          - { label: "I trust AI agents to make production infrastructure changes", values: [4.71, 10.39, 22.16, 40.39, 22.35] }
          - { label: "We spend too much time on undifferentiated infrastructure toil", values: [6.08, 19.22, 27.65, 33.14, 13.92] }

cta:
  heading: Put agents to work on your infrastructure
  intro: |
    Pulumi gives engineers and agents one platform to build, deploy, and manage cloud
    infrastructure — with the guardrails to let agents ship safely.
  items:
    - title: Pulumi Neo
      icon: pulumi-neo
      desc: An AI agent that plans and executes infrastructure changes, and waits for your approval before touching production.
      href: /product/neo/
      cta: Explore Neo
    - title: Pulumi IaC
      icon: pulumi-iac
      desc: Define infrastructure in TypeScript, Python, Go, and more — the real languages agents already know how to write.
      href: /product/infrastructure-as-code/
      cta: Explore IaC
    - title: Pulumi MCP server
      icon: plugs-connected
      desc: Connect Claude Code, Copilot, and your own agents to your infrastructure through the Model Context Protocol.
      href: /docs/ai/integrations/mcp/
      cta: Read the docs
    - title: Pulumi Agent Skills
      icon: head-circuit
      desc: Knowledge packages that teach Claude Code, Cursor, and other agents to build and manage infrastructure.
      href: /docs/ai/skills/
      cta: Explore skills
---
