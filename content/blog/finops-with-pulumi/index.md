---
title: "FinOps With Pulumi"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2023-02-14

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
# Max length is 160 characters.
meta_desc: FinOps must know. What is FinOps? Who is responsible, and what are the responsibilities? Cloud FinOps principles and FinOps with Pulumi in practice.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: FinOps automation policy check tag cloud resource label.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
    - matt-small
    - richard-shade

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - finops
    - policy-as-code
    - cloud-engineering
    - automation-api

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
---

## What is FinOps?

The [FinOps Foundation](https://www.finops.org/) eloquently defines FinOps as “an evolving cloud financial management discipline and cultural practice that enables organizations to get maximum business value by helping engineering, finance, technology and business teams to collaborate on data-driven spending decisions.”  Simply put, FinOps is the continuous effort to control cloud spend.

Just as organizations have adopted operations-focused best practices into software development cycles and have considered how to best insert security best practices along the way, financial best practices may also be codified by developers writing cloud programs.

Adopting a FinOps practice brings real world [OpEx(Operating Expenses)](https://en.wikipedia.org/wiki/Operating_expense) considerations to the decisions that cloud engineers regularly make. When you add FinOps to your [Cloud Center of Excellence](https://finops.world/en/organization-and-key-roles/), technical teams bring financial context into service level and recovery objectives, scaling and placement decisions, and business continuity planning.  Developers are typically more conscious of the resources they are using and consider the impact of their application design decisions at both development, test and production scale.  Therefore organizations usually realize substantial OpEx savings while better forecasting their growth.

## Who is Responsible for Cloud Financial Decisions?

In most smaller organizations, developers themselves are often responsible for the decisions that impact cost.  In larger organizations, this responsibility typically falls to a central IT or Cloud Platform team, often seen as the cost center for infrastructure, and the best team to optimize that spend continuously.  Some organizations are evolving toward FinOps as a practice, with dedicated teams responsible for enabling the organization to make smarter financial decisions and negotiating with cloud vendors for discounts.

Ultimately, the cloud account owner is responsible for the cloud bill, and failure to pay that bill will result in the suspension of cloud services. Given that infrastructure is often code, developers or IT teams are often made responsible for the task of optimization.  Optimization recommendations may range from simply deleting orphaned cloud resources to re-architecting the entire application to use a modern serverless framework that would consume less resources overall.

## Establishing FinOps Practices

The first step of establishing many FinOps practices is **determining the allocation of costs**.  It is easy to allocate costs to individual users launching cloud services, but it becomes compoundingly hard once pipeline automation, team structure, and business unit reporting come into play.  As an organization scales, it grows increasingly difficult to allocate costs across different business units and teams, across environments such as development versus production, or across application component services such as the data layer. Further, how does an organization account for supporting systems and services running alongside applications in the cloud, including third-party commercial software?

When starting your FinOps Journey is essential to understand cost allocation, typically done with consistent and enforced tagging of cloud resources.  Creating a Tag Policy is covered below.

## FinOps: Reactive vs. Proactive Optimization

Most FinOps processes today are reactive; once you have received your bill, you will observe (and pay) the costs and resources accounted for, review your architecture and make necessary adjustments such as reserving, reallocating or removing resources.  Next month, you will do it again, also factoring in your company’s cloud growth, application design changes, team shifts and other dynamics that occured in the meantime.  Many platforms, tools, and job descriptions are oriented toward this reactive optimization process.

Proactive optimization and enforcement means providing real time feedback on how cloud engineering architectural changes may impact cost and creating preventative policies which do not allow for budget-busting cloud services to be provisioned.  This is an evolving practice in many modern cloud-centric organizations.  As more cloud operations are defined as code, this preventative, proactive optimization model is becoming more popular.

Financial optimization can also come in the form of strategic sourcing; most cloud providers offer multiple discount mechanisms, including large enterprise discount plans for committed consumption that may extend to third party SaaS software purchased through the cloud marketplaces, as Pulumi is.  This level of optimization will provide dramatic savings on your top-line spend.

## FinOps with Pulumi

Using cloud engineering practices with Pulumi, you have the opportunity to implement both proactive and reactive models to control your cloud spend.

As an [infrastructure as code platform](/product/), **Pulumi is in the unique position to be proactive about managing your costs**.  

- You can design guardrails on your provisioning to limit expensive resource types or quantities,
- Direct resources to reserved allocations,
- Ensure resources are tagged and traceable to the correct cost center,
- Connect resources to your observability and dedicated FinOps platforms,
- Provide preventative visibility and control.  

Consider uses for CrossGuard Policy as Code, multi-language components for defining resource abstractions, and Automation API to package up orchestration into web service endpoints, as described in Pulumi Features below.

If you are proactively managing your infrastructure, then reactively, the largest contributor to financial overrun is drift; the misalignment between the desired state and the actual state.  Pulumi is used to define your desired state; however, many things may cause the actual state to begin to deviate from the desired state in your code, such as manual actions from the cloud console or ad-hoc deployment pipelines.

**Drift detection**, which is the name given to continuously scanning your environment to compare the actual state with the desired state and alerting and/or automatically remediating the difference in state, **is a primary method of managing these creeping cloud costs**.  Leverage an automation system, such as a CI tool, to implement continuous scanning against your Pulumi code as described below.

Remediation of any infrastructure mismanagement requires infrastructure reconfiguration action to be taken; often resources need to be replaced with better suited, more cost effective resources, and resources that were provisioned outside of acceptable policies may have to be destroyed.  However, any remediation should carefully consider the underlying reasoning for the misalignment in the first place. That should include both the reason for the initial deployment specifications as well as any decisions for why that’s no longer acceptable.  Be sure to consider all architectural decisions, such as disaster recovery and business continuity planning, regional latency, and any other impact to service level objectives (SLOs).  Understanding the context will help you code preventative measures into your Pulumi programs going forward and the self-documenting nature of infrastructure-as-code will ensure your decisions are memorialized for future developers and operators, for example, in a Stack README as described.

**Automation of remediation is a goal for many cloud engineering organizations; if the perfect state is defined in code, then any drift may indicate the need to reconcile back to the desired perfect state**.  Given that some cloud resources may necessarily drift due to limitations in how they are managed, a combination of alerting and remediation of known patterns is implemented.  For example, you might choose to detect and deprovision any newly instantiated resource not provisioned by Pulumi, but allow manual resizing of resources if needed.  Just be sure to capture any infrastructure and improvements you want to make default and/or repeatable as infrastructure as code.

## Best First Action: Implement a Tag Policy

Getting started with a FinOps usually falls to the resource owners or Cloud Engineering teams themselves.  The more resources you have, the more complex and noisy things are going to get and the harder it will be to both allocate costs and resources where they are needed, as well as identify and eliminate the unneeded ones.

Implementing Tag Policy is the best first action to take. Tags are the set of required cloud metadata tags for any resources provisioned by your organization.  While not every resource in every cloud may be tagged, most are. Getting into the practice early will help you maintain accountability for what you are running, demystify your cloud bills as they grow larger, and help update the application architecture or make cost-effective product decisions long-term.

### A Basic Tag Policy for FinOps will include:

1. **Owner** - the person responsible for this resource that you would contact if you had to (e.g., johndoe@pulumi.com)
2. **Origin** - the pipeline, process, and/or system through which this came to be (e.g., ArgoCD, Jenkins, Pulumi)
3. **Business Unit** - the team responsible typically maps to the cost center associated (e.g., Sales, Engineering)
4. **Environment** - the teams/customers this deployment services (e.g., Dev, Staging, Production)
5. **Application Component** - the part of the application that this resource serves (e.g., data pipeline, authentication, front end)*

You will now be able to report on and manage resources in those tag groups.  It’s advisable that you do not create too many required tags, or it will quickly get difficult to manage and it increases the likelihood of multiple tags applying, which reduces the insightfulness of the data.

Read more about Tag Policy implementation with Pulumi below, and for extended reading, refer to this post, [Automatically Enforcing AWS Resource Tagging Policies](/blog/automatically-enforcing-aws-resource-tagging-policies/) from CEO, Joe Duffy.

## Pulumi Features in Context

### Multi-Language Components

[Multi-language components](/blog/pulumiup-pulumi-packages-multi-language-components/) allow you to create repeatable infrastructure patterns, modular abstractions of resources and/or groups of resources that meet your desired configuration standards.  Packaging up resources within and across clouds, implementing standard deployment best practices, and making those components available to developers reduces the cognitive load that they have when building new applications from those pre-assembled, ready-to-run components.

Use these guardrails to enforce Tag Policies, for example that every tag for “Production” is actually “Production” and not “Prod” or “production” (yes, case sensitivity matters).  Or you may ensure teams only deploy resources such as VMs to regions where you have allocated Reserved Instances or other financial benefits in your application architecture. With MLCs end users have access to your component and not to the underlying infrastructure resources, guaranteeing repeatabality, however, in order to realize the benefits of MLCs, your developers must be empowered to leverage them, but limited from using other methods.

## CrossGuard

[CrossGuard Policy as Code](/docs/using-pulumi/crossguard/) allows an Organization to define global rules for how resources may be provisioned and prevent resources from being provisioned by Pulumi in any other configuration.  Pulumi Stacks that do not meet the Organization’s financial, security, data protection, or other pre-defined standards are prevented from provisioning any resources, and the developer is instructed to correct their desired configuration or program in accordance with the Organization-wide policies.

[Policy as code](/docs/using-pulumi/crossguard/) ensures that any Pulumi code written and run meets an organization’s stated policies. It is the ultimate preventative weapon to prevent financial, security, or other placement and provisioning decisions that may lead to exposure or overrun.

Go here for [examples of FinOps policies](https://github.com/pulumi/examples/tree/master/policy-packs/aws-ts-finops) to get you started!

## Automation API

Of the many things [Automation API](/docs/using-pulumi/automation-api/) allows you to do, one is you can create an HTTP endpoint for a Pulumi program.  Organizations have used this to control easy on/off switches for applications such as provisioning/deprovisioning single tenant SaaS architectures, short lived environments, and complex testing and blue/green deployments.  Because of the encapsulation of a Pulumi program and the simplification this provides, this endpoint may be directly exposed to those responsible for making the financial decisions in the moment, such as a Sales Engineer who must turn on a new POC environment for testing who then must be sure to shut that off when completed.  Oftentimes, these decisions are automated in processes and pipelines.

## Pulumi FinOps in Practice: Sweeping up Dev and QA

A common automation in FinOps is to destroy things that don’t meet your Tag Policy.  These “Sweeper Bots” will continuously query AWS for resources with specific tags and delete them.  Read more about how Pulumi has implemented this using Pulumi to set tags and Lambda to sweep through and remove resources that meet certain specifications in this post, [Controlling AWS Costs with Lambda and Pulumi](/blog/controlling-aws-costs-with-lambda-and-pulumi/).

## Conclusion

In the manner of ["Crawl, Walk, Run"](https://www.finops.org/framework/maturity-model/), it’s best to **start by implementing policies as code in a manner that will cause the most benefit while causing the least amount of change and/or downtime**.  Make sure you have the appropriate billing tags applied to all supported resources, ensuring you are able to allocate costs to the appropriate business units in your company. Then add in additional policies to make sure you are using instances covered by any reserved instance or similar savings plans.  Continue evolving your infrastructure and policy as code strategy to incorporate both preventative and reactive checks and balances.

Have questions about using Pulumi when implementing FinOps in your IaC pipelines? [Contact us](/contact/?form=sales) and let us know your questions or [request a demo](/request-a-demo/).
