---
title: "Pulumi for All Your IaC — Including Terraform and HCL"
date: 2025-12-18T00:00:00-00:00
draft: false
meta_desc: Pulumi Cloud can now manage Terraform, Pulumi IaC now speaks HCL, and we'll cover your costs until your HashiCorp contract ends.
meta_image: meta.png
authors:
    - joe-duffy
tags:
    - iac
    - terraform
    - hcl
    - hashicorp
---

We work with thousands of customers who prefer Pulumi due to our modern approach to infrastructure that delivers faster time to market with built-in security and compliance. Yet we know many organizations have years of investments into tools like Terraform. At the same time, HashiCorp customers are increasingly telling us about their frustrations post-IBM acquisition: rate increases, loss of open source heritage, overnight rug-pull of CDKTF, … and the hits just keep on coming. Today, we’re excited to announce three new ways Pulumi is enabling customers of HashiCorp, an IBM Company, who want a better, open source friendly, modern solution for their IaC to choose Pulumi. First, Pulumi Cloud will support Terraform and OpenTofu, so you can continue using any Terraform or Pulumi CLI and language with the complete Pulumi Cloud product, including our infrastructure engineering AI agent, Neo. Second, Pulumi’s own open source IaC tool will support HCL natively as one of its many languages, alongside the industry’s best languages including Python, TypeScript, Go, C#, Java, and YAML. Pulumi is multi-language at its core and many organizations are diverse and polyglot—these new capabilities truly make Pulumi the most universal IaC platform with the broadest support. Third, we’re offering flexible financing to make it easy to depart HashiCorp for Pulumi.

## The TL;DR

Pulumi Cloud now manages Terraform/OpenTofu with full visibility, governance, and agentic AI included. Pulumi IaC now speaks HCL alongside general purpose languages and YAML. And we'll cover your costs until your HashiCorp contract ends.

## Terraform/OpenTofu in Pulumi Cloud

Pulumi has always been two things: Pulumi IaC, the multi-language, open source infrastructure as code technology, and Pulumi Cloud, our commercial platform that includes infrastructure state management and visibility, our AI agent Neo, secrets management, policy as code, governance, and much more. You can think of it like Git (the tool) versus GitHub (the SaaS).

Historically, we required that you choose Pulumi IaC to benefit from Pulumi Cloud but over time we’ve been moving away from that, such as with our AI and governance features: you point us at any cloud accounts, and we’ll help you make sense of and tame them, regardless of how the accounts’ resources were deployed (Pulumi, CDK, Terraform, … even manual point and click). Today, we are taking that one step further and letting you run Terraform, OpenTofu, *or* Pulumi IaC as your tool of choice, while still benefitting from Pulumi Cloud’s full suite of capabilities.

The great thing about this is that even if you choose Terraform or OpenTofu IaC on the client, you will still benefit from all of the capabilities of our server, from AI to governance to visibility and more. Terraform statefiles and workspaces will show up effectively the same way Pulumi stacks do, and you’ll get full visibility of who is changing what and when including diffs and logs.

Why would we do such a thing? As we’ve worked with larger and larger companies in our journey to thousands of customers, we’ve seen that there’s significant Terraform out there in the world. Even if a team’s long-term objective is to migrate to 100% Pulumi – reaping the many benefits of modern IaC, like faster time to market by catering better to a polyglot world of developers, infrastructure experts, security engineers, and AI/ML teams – that transition doesn’t happen overnight. Many teams legitimately want a mix of IaC tools. Ensuring all infrastructure is fully automated, secured, and managed is a more righteous outcome to focus on rather than debating one’s choice of IaC tool or language. There are many paths you can take, and now Pulumi can be your one platform to stay on top of all of it and drive towards this outcome.

Support for Terraform/OpenTofu state is in private beta and we are beginning to work with customers directly as we get it ready for prime time. We anticipate general availability in Q1 2026.

## HCL Language Support in Pulumi IaC

At Pulumi, we love our languages. We now support six – depending on how you count: Python, TypeScript, Go, any .NET language (like C#), and any JVM language (like Java itself), and even YAML. Having this broad array of languages is a massive unlock: you suddenly get access to the full ecosystem of tooling and expertise around these languages, including rich syntax (for loops, if statements, functions), IDEs, testing frameworks, true sharing and reuse, and ensuring that LLMs deeply understand your IaC. This choice of language is then married with the best of declarative IaC, so you still get the belts and suspenders safety of a desired state IaC tool.

But we work with customers all the time where some of the team is more comfortable with and/or genuinely prefers HCL. The HCL language was purpose-built for IaC through Terraform and, now, OpenTofu and is easy for simple use cases. We actually shipped YAML support two years ago because it’s an industry standard and we kept hearing about simpler use cases where you didn’t need a full blown language (especially e.g. when code-generating IaC or supporting simple developer self-service CI/CD pipelines where a handful of lines of YAML do the trick). But despite that, there’s a ton of muscle memory with HCL in the IaC community.

We are not dogmatic about languages, we love all of them. The L in HCL and YAML stands for “language” and we’ve always had a “come one, come all” mindset. As soon as we see enough market demand for a given language, we will add it. Well, that time has come for HCL.

The good news is that this is not a bolt on. Just like any of the other Pulumi languages, you have full access to the entirety of the Pulumi ecosystem, including thousands of providers. Thanks to our Terraform bridge, if there’s a Terraform provider out there, it just works. This is explicitly not meant to be a lift-and-shift migration option – we have many other techniques for that, including the new Terraform support in Pulumi Cloud – but is instead for teammates who are more comfortable with or prefer HCL over general-purpose languages, but still want to leverage the more modern Pulumi IaC engine with its advanced multi-language capabilities.

HCL support also integrates with Pulumi’s multi-language technology in a deep way, so that you can author modules in one language and consume them from another. This will let, for example, platform teams author complex components in, say, Go – with the rich facilities offered by the language – and then expose them to teammates who consume them in HCL (or vice versa!)

Similar to Terraform support in Pulumi Cloud, HCL is currently in private beta and we will work with customers directly to ensure it meets our quality standards, with a goal of general availability in Q1 2026.

## Builds on Existing Coexist/Convert Capabilities

These two new technical capabilities augment an existing array of tools that make it easy for you to choose Pulumi as your IaC platform of choice, even in organizations with hybrid client-side IaC tools, and languages may be general-purpose, HCL, or a mixture thereof.

Pulumi IaC supports using any Terraform provider. Many of them are available pre-built in the Pulumi Registry, however, in the event one isn’t pre-published, you can generate one on demand using [the “Any Terraform Provider”](https://www.pulumi.com/blog/any-terraform-provider/). Pulumi doesn’t use the Terraform engine, but rather it leverages the resource schemas and create, read, update, and delete methods in them.

We have numerous migration tools. The first is Neo, our infrastructure engineering agent, who has Terraform-specific skills to migrate code and state. Neo leverages a number of building blocks that you can use directly instead. That includes [the `pulumi convert --from terraform` command](https://www.pulumi.com/blog/converting-full-terraform-programs-to-pulumi/) which understands how to convert Terraform/OpenTofu HCL or CDKTF code into a Pulumi language of your choosing, preserving code structure including migrating modules to Pulumi components. We also support directly importing resources from your cloud accounts directly, either at the CLI or visually in Pulumi Cloud. Read more about migration [here](https://www.pulumi.com/docs/iac/guides/migration/).

You can [deploy Terraform modules](https://www.pulumi.com/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) straight off the shelf from your favorite Pulumi language. That works as well for any supported Pulumi language, including HCL, and it shows up as though the underlying module resources were managed natively in Pulumi. This ensures if your team has a collection of battle tested best practices encoded as Terraform modules, and either plan to keep some Terraform or even migrate eventually, you don’t need to migrate right away.

Finally, [you can reference Terraform state outputs](https://www.pulumi.com/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#referencing-terraform-state) from Pulumi programs and configurations. Using this you could, for example, keep your network defined in Terraform and define a layer of higher level infrastructure that consumes VPC and subnet IDs from that lower-layer network workspace. This can be useful if there’s short- or long-term coexistence between Terraform and Pulumi IaC programs, such as during an ongoing migration effort or in a hybrid team.

## Pulumi Covered Until Your HashiCorp, an IBM Company, Renewal

Even with the new technical capabilities above, we realize many customers already have HashiCorp contracts that may have them locked into a single vendor. The last thing we want is for you to have to pay for two IaC solutions for a period of time. Additionally, we want to ensure that the transition is as smooth as possible and your team is set up for long-term success.

To make it easier to say yes to Pulumi, we are offering three things:

* **Escape hatch for your current contract**. We know paying for two IaC solutions at once is a non-starter, so we’re letting you apply credits purchased from HashiCorp towards your Pulumi usage until your next renewal, avoiding double pay.

* **Free IaC modernization workshop.** Our professional services cloud architects will host a free IaC modernization workshop to review where you’re at with your IaC already and share best practices of how to adopt the Pulumi platform at scale we’ve learned from working with world-class organizations like BMW, NVIDIA, and Supabase. You will leave this session trained up and equipped to succeed with the next phase of your IaC journey.

* **Return on investment (ROI) calculation**. We will show you how the move to Pulumi will not only be spend-neutral thanks to the escape hatch, but how much value and savings you should expect to see, given our experience helping innovators like Snowflake accelerate their time to market – going from code to cloud in weeks to hours.

These ensure there’s no financial penalty for switching, a very clear ROI, and no learning curve. We have always been proud to work with customers of all sizes in all industries, so these offers are available to you whether you’re a Global 2000, startup, or somewhere in between.

## Why Snowflake, BMW, and Wiz Switched to Pulumi

We’ve worked with thousands of companies over 8+ years to build what we view as the most innovative infrastructure as code platform on the market. We’re biased, of course, but our customers range from innovative startups, to established public technology companies, to Global 2000, and everywhere in between, and they tell us this all of the time.

For example:

* [Snowflake](https://www.pulumi.com/case-studies/snowflake/) radically improved time to market on their path to IPO. “When we demonstrated to people that what used to take a week and a half now, with Pulumi, took under a day, they were shocked.”  

* [Lemonade](https://www.pulumi.com/case-studies/lemonade/) switched from Terraform to Pulumi so they could embed business logic into infrastructure, share and reuse logic, and scale their lean ops team to support a much larger group of developers. "We're not limited to one-size-fits-all configurations, but can actually implement environment-specific customizations for our infrastructure."

* [BMW](https://www.pulumi.com/case-studies/bmw/) was able to establish a center of infrastructure excellence that they call CodeCraft, standardizing all infrastructure delivery, and scaling to support 10,000+ developers.

* [Supabase](https://www.pulumi.com/case-studies/supabase/) was able to scale to meet the heightened demands and pace of AI, saying that “the infrastructure team acts as groundkeepers of our Pulumi practices, not gatekeepers, but promoters for the entire org."

* [Wiz](https://www.pulumi.com/case-studies/wiz/) manages over 1 million resources, tens of thousands Kubernetes clusters, and hundreds of data centers, with over 100,000 daily updates.

Here’s why:

**Language choice.** Especially with the addition of Terraform/OpenTofu support, and HCL language support natively in Pulumi IaC, the Pulumi platform truly is the most universal IaC platform available. It democratizes access to infrastructure across the entire organization which often has very varied and diverse skillsets. By embracing general-purpose languages, it allows engineering teams to apply rigor to how they manage infrastructure, improving productivity – translating directly to time to market – robustness, and standards compliance.

**AI native.** We’ve been infusing AI into our platform for over three years now, culminating in the release of our infrastructure engineering agent, [Neo](https://pulumi.com/neo). Neo is like Claude Code for your infrastructure and allows you to automate short- and long-horizon infrastructure tasks, like spinning up and scaling infrastructure, upgrading clusters, getting compliant, reducing cloud waste, and so much more. Neo works over any infrastructure no matter how it was provisioned.

**Standard enterprise capabilities and controls.** Regardless of language or IaC tool choice, you still get one central standardized set of capabilities and controls. This ensures you have one “mission control” from which to standardize, secure, and govern your entire cloud estate, regardless of what client-side tool choice (or even in the presence of click-ops).

**Full visibility of what’s happening, when, where, and why.** The Pulumi platform always gives you total visibility into your cloud estate so you can quickly understand what is going on. This helps you wrap your hands around your cloud and chart a course to 100% IaC, the table stakes nirvana many organizations are trying to get to, and the choice of language is one small part.

The final point isn’t even a technical one, but we hear it from our customers all the time:

**Customer love as our #1 company value.** Our first company value is “when the customer is successful, we are too” – and we live it and breathe it daily. I just visited a new customer to review how the project is going yesterday and their head of cloud infrastructure and EVP of product were in the room and both went out of their way to express gratitude for how our team really showed up to help get them on the right track. We don’t view customers as a transaction, we view it as a lifetime partnership, and treat our customers with the respect they deserve. We won’t sleep at night until you’re on the cloud path that you envisioned when selecting Pulumi.

To learn more about our product capabilities, visit these pages:

* [Platform Overview](https://www.pulumi.com/product/)  
* [Infrastructure as Code](https://www.pulumi.com/product/infrastructure-as-code/)  
* [Agentic Infrastructure Engineering with Neo](https://www.pulumi.com/product/neo/)  
* [Secrets & Configuration](https://www.pulumi.com/product/secrets-management/)  
* [Insights & Governance](https://www.pulumi.com/product/insights-governance/)  
* [Internal Developer Platforms](https://www.pulumi.com/product/internal-developer-platforms/)

## Get Started Today

If you’d like to join the private beta waitlist for the new Terraform/OpenTofu and HCL capabilities, or take advantage of the financial flexibility options, please [get in touch](https://www.pulumi.com/contact/?form=sales).

We will work with you closely on a three step process to adopt Pulumi: First, the modernization workshop; then a rapid proof of value; and finally an adoption plan that avoids you double paying Pulumi and HashiCorp.

If you’d like to try Pulumi on your own immediately, you can [sign up for Pulumi Cloud here](https://app.pulumi.com/signup), or [go through our open source IaC getting started tutorial here](https://pulumi.com/start).

We can’t wait to earn the right to work together.
