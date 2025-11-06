---
title_tag: Supabase | Case Studies
title: Supabase Democratizes Infrastructure Across Every Engineering Team
description: |
    Open-source Postgres platform scales from single-region manual deployments to 16-region automated infrastructure with 80,000 Pulumi resources.
meta_desc: Open-source Postgres platform scales from single-region manual deployments to 16-region automated infrastructure with 80,000 Pulumi resources.

customer_name: Supabase
customer_logo: /logos/customers/supabase-wordmark.svg
customer_url: https://supabase.com/

quote_block:
    quote: |
        "The infrastructure team acts as groundkeepers of our Pulumi practices, not gatekeepers, but promoters for the entire org."
    quote_attrib: Paul Cioanca, Platform Engineer at Supabase
    headline_stat: 1 week
    headline: |
        Infrastructure readiness for new region deployment, enabling rapid global expansion.

exec_summary: |
    Supabase is the open-source Postgres development platform that's built to scale to millions. It is an all-in-one suite with Database, Auth, Storage, Edge Functions, Real-Time, and Vector search. With a generous free tier and thriving open-source community, Supabase has experienced explosive growth, now serving customers across 16 AWS regions and managing approximately 80,000 Pulumi resources, up from 30,000 just one year ago. The infrastructure team at Supabase faced a critical scaling challenge: how to support rapid business growth and regional expansion while enabling every engineering team to ship, run, and monitor their own infrastructure. Traditional infrastructure-as-code tools created mental context switching between application code (TypeScript) and infrastructure definitions (proprietary DSLs). At the same time, manual deployment processes couldn't keep pace with customer demand for new regions and features. By adopting Pulumi within Supabase's first 4-5 months of existence, the company built its entire multi-region strategy on a foundation that treats infrastructure as real code. The platform now enables new-region deployment in approximately 1 week for infrastructure readiness, with full General Availability following approximately 2 weeks later. Infrastructure contributors grew from 1-2 people to over 40 active engineers across the organization. At the same time, every product team (Storage, Platform API, Auth, and others) deploys and manages their own services independently. As Paul Cioanca, Platform Engineer at Supabase, explains: "The infrastructure team acts as groundkeepers of our Pulumi practices, not gatekeepers, but promoters for the entire org."

sections:
    - label: Executive Summary
      anchor: executive-summary
    - label: About Supabase
      anchor: about-supabase
    - label: Challenge
      anchor: challenge
    - label: Why not Terraform?
      anchor: why-not-terraform
    - label: Solution
      anchor: solution
    - label: Results
      anchor: results
    - label: Business impact
      anchor: business-impact
    - label: Looking forward
      anchor: looking-forward
    - label: Conclusion
      anchor: conclusion
---

## About Supabase {#about-supabase}

<div class="float-left mr-4 mb-4 w-48">
<img src="/images/case-studies/paul-cioanca-supabase.jpg" alt="Paul Cioanca" class="w-full rounded-lg">
<p class="text-sm text-center mt-2">Paul Cioanca, Platform Engineer at Supabase</p>
</div>

[Supabase](https://supabase.com/) is the open-source Postgres development platform that's built to scale to millions. It is an all-in-one suite with Database, Auth, Storage, Edge Functions, Real-Time, and Vector search. With a generous free tier and thriving open-source community, Supabase has experienced explosive growth, now serving customers across 16 AWS regions and managing approximately 80,000 Pulumi resources, up from 30,000 just one year ago.

The infrastructure team at Supabase faced a critical scaling challenge: how to support rapid business growth and regional expansion while enabling every engineering team to ship, run, and monitor their own infrastructure. Traditional infrastructure-as-code tools created mental context switching between application code (TypeScript) and infrastructure definitions (proprietary DSLs). At the same time, manual deployment processes couldn't keep pace with customer demand for new regions and features.

## Challenge: Manual Deployments Don't Scale with Explosive Growth {#challenge}

Five years ago, Supabase operated from a single AWS region with a deployment process that couldn't scale: one engineer manually clicking through cloud consoles to provision infrastructure. If that person was unavailable, deployments stopped entirely. The setup only worked on their local machine, creating a single point of failure that threatened the company's ability to meet growing customer demand.

"We had no visibility into what was being deployed," Paul recalls. "It was manual, click-ops deployments across multiple clouds, and we knew we needed to solve this before we could scale."

As customer demand grew, particularly from enterprise users who started by "tinkering in their spare time" with Supabase's generous free tier, the team faced mounting pressure to expand into new regions for performance, compliance, and regulatory requirements. GDPR in Europe, California privacy regulations, and UAE government requirements all demanded multi-region capabilities that manual processes couldn't deliver reliably.

### Why Not Terraform? {#why-not-terraform}

The team evaluated existing infrastructure-as-code solutions, but found them lacking for Supabase's needs. "Terraform's HCL required us to move between TypeScript for our application services and proprietary DSLs for infrastructure," Paul explains. "This mental context switching, combined with obscure features and syntax, meant we were optimizing for learning proprietary tools instead of delivering our product."

The team wanted infrastructure that felt like an extension of their application code, not a separate domain requiring specialized knowledge and constant context switching between tools and languages.

## Solution: Infrastructure in the Same Language as Services {#solution}

Supabase adopted Pulumi early in the company's existence, making a fundamental bet that infrastructure should use the same language as application code. Since all Supabase services are written in TypeScript, the team chose Pulumi's TypeScript support to eliminate mental overhead and leverage existing language expertise.

The implementation transformed their deployment process:

### PR-Based Workflow with Automated Previews

The team transitioned from local machine deployments to automated pipelines using Pulumi's GitHub integration. When engineers propose infrastructure changes, Pulumi's GitHub App automatically generates preview comments on pull requests before merge, showing precisely what resources will be created, modified, or deleted. This gives non-infrastructure engineers visibility without requiring them to run Pulumi locally.

### Single-Click Production Deployments

What once required manual clicking through multiple cloud consoles now happens with a single click to production. The organization gained visibility into infrastructure changes across the entire company, while maintaining confidence through staging-to-production deployment patterns.

### Multi-Cloud Composition

Supabase takes a pragmatic approach to cloud vendors, using the best tool for each job:

- **AWS**: Primary compute, instance provisioning, and platform services
- **Cloudflare**: Edge compute, compliance, WAF, and traffic routing
- **GCP**: BigQuery for data analytics and pipelines

With Pulumi, Supabase's application teams compose multi-cloud stacks atomically within a single deployment. A typical stack might include AWS services for compute, Cloudflare routing, and DNS configuration, and additional providers, all without having to jump between three different cloud consoles.

<img class="block mx-auto md:max-w-4xl my-8"
src="/images/case-studies/supabase-architecture-diagram.png" alt="supabase-architecture-diagram">

## Results: From Single Region to Global Infrastructure {#results}

### Regional Expansion: 1 Week to Infrastructure Readiness

The most dramatic impact is seen in Supabase's regional expansion capabilities. Most recently, Supabase expanded into three European regions (eu-west-3, eu-north-1, eu-central-2) to better meet customer proximity needs and comply with GDPR requirements.

Each new region requires replicating 1,000-1,500 Pulumi resources, representing the complete platform infrastructure stack needed to support customer databases. With Pulumi, infrastructure becomes ready in approximately one week, with the whole region reaching General Availability roughly two weeks later, after coordinating with cross-functional teams and departments.

"For regional expansion, it's enough to update a few lines of Pulumi stack config," Paul explains. "At our scale, doing this manually would be nearly impossible to execute reliably."

This capability has become fundamental to Supabase's business model. At today's scale (80,000 resources across 16 regions), manual regional expansion would be, as Paul describes it, "nigh-impossible."

### Infrastructure Democratization: Over 40 Active Contributors

Infrastructure contribution grew from 1-2 people writing infrastructure code to over 40 active contributors across the organization. More importantly, every engineering team at Supabase now ships, runs, and monitors their own infrastructure independently.

Within Supabase, the Storage team, Platform API team, Auth team, and others all deploy services using Pulumi without waiting for infrastructure team pairing sessions or PR ping-pong. "Instead of having somebody spend a week trying to figure out how these things connect, they're able to get it out in one day or maybe less just by composing load balancing, database, application runtime cloud primitives," Paul notes.

This shift happened because Pulumi removed barriers to entry. "Since it's just another programming language with control structures and external packages, it makes for a good transition from application code to infrastructure as code," Paul explains.

### Reusable Components: NPM Packages for Infrastructure

The team created standard infrastructure components as NPM packages, leveraging TypeScript's packaging model and ecosystem. This prevented teams from "redefining the same thing in different ways" and established reproducible patterns across applications. When launching new products or components, engineering teams find that "the primitives are already there," dramatically accelerating time-to-ship.

### Self-Service Example: Platform API Migration

The Supabase Platform API team recently deployed globally available platform API services for low-latency operations. Implementation took 3 days, with coordination from decision to production spanning 2 weeks.

The team's services were hosted on a secondary cloud provider, which offered limited operational visibility and deployment reliability. The team made the strategic decision to migrate to AWS to align with the organization's standard infrastructure patterns. Because Pulumi uses the same language that the Platform API team writes their application services in, engineers could immediately contribute to infrastructure without switching mental contexts.

### Managing Exponential Growth: 30K to 80K Resources

Resource count has grown from approximately 30,000 to 80,000 in just one year, mirroring Supabase's explosive business expansion. The networking backbone stack alone manages roughly 20,000 resources.

As stacks grew larger, Pulumi's composability allowed the team to split them into multiple components and stacks. "We drove ourselves into this corner, but we didn't have to escalate to support to figure a way out," Paul notes.

### Operational Confidence Through Staging Parity

Supabase maintains staging-to-production parity: the same Pulumi code deploys to staging, then to production a day later. This validates changes in staging before any production impact, giving teams, as Paul calls it, "psychological safety" to stay in the familiar TypeScript ecosystem.

## Business Impact: Infrastructure That Scales With Growth {#business-impact}

### AI Builder Partnerships

In the past year, Supabase has partnered with AI application builders like Lovable, Bolt, Figma Make, and Vercel v0. When users specify application requirements, these platforms provision Supabase databases instantly, complete with real-time data streaming and storage servers.

With more than 43,000 databases launched daily across over 1 million managed databases, Supabase's infrastructure must automatically handle massive scale. The company now manages 11.2 million total databases created, processing over 100,000 API calls per second while maintaining the reliability that 4.5 million developers and 250,000 community members depend on.

## Looking Forward: Infrastructure That Grows With You {#looking-forward}

Supabase's success with Pulumi demonstrates a fundamental principle: infrastructure tooling should accelerate product delivery, not slow it down. By choosing technology that matched their existing expertise (TypeScript) and treating infrastructure as real code, Supabase eliminated the artificial boundary between application and infrastructure engineering.

"We've internalized the workflow and take it for granted now," Paul reflects. "What friction we encountered was mostly self-inflicted. We haven't hit overt or unsolvable usability issues with Pulumi itself."

As Paul concludes: "The infrastructure team acts as groundkeepers of our Pulumi practices, not gatekeepers, but promoters for the entire org."

## Conclusion

By adopting Pulumi within Supabase's first 4-5 months of existence, the company built its entire multi-region strategy on a foundation that treats infrastructure as real code. The platform now enables new-region deployment in approximately 1 week for infrastructure readiness, with full General Availability following approximately 2 weeks later. Infrastructure contributors grew from 1-2 people to over 40 active engineers across the organization. At the same time, every product team (Storage, Platform API, Auth, and others) deploys and manages their own services independently. The partnership with Pulumi has positioned Supabase for continued success and innovation in the competitive cloud database market.
