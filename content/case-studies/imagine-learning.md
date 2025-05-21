---
title_tag: Imagine Learning | Case Studies
title: "Imagine Learning: Modernizing IDP with Pulumi"
description: |
    Imagine Learning used Pulumi to modernize their Internal Developer Platform, dramatically reducing deployment times and enabling management of hundreds of environments across multiple AWS regions.
meta_desc: Imagine Learning used Pulumi with GitOps to modernize their IDP, reducing deployment times and improving infrastructure visibility.
meta_image: /images/case-studies/imagine-learning-meta.png

customer_name: Imagine Learning
customer_logo: /images/case-studies/imagine-learning.png
customer_url: https://www.imaginelearning.com/

exec_summary: |
   Imagine Learning, a leading K-12 education technology company serving millions of students nationwide, needed to modernize their Internal Developer Platform (IDP) to meet growing enterprise demands. By implementing Pulumi with GitOps methodologies and ArgoCD, they created a scalable, automated solution that dramatically reduced deployment times, improved infrastructure visibility, and enabled them to manage hundreds of environments consistently across multiple AWS regions. Their "GitOps bridge pattern" using Pulumi removed barriers between infrastructure and Kubernetes deployments, allowing developers to use familiar programming languages while ensuring consistent, reliable infrastructure across their entire organization.

quote_block:
    quote: |
        "Building new environments takes hours now; it doesn't take weeks or even months."
    quote_attrib: Blake Romano, Senior Software Engineer, Imagine Learning
    headline_stat: 1.5 Months
    headline: Time to recoup investmnet in Pulumi

hide_pulumi_footer: true

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: Challenges
      anchor: scaling-education-infrastructure-for-the-next-generation
    - label: Solution
      anchor: building-a-gitops-bridge-with-pulumi
    - label: Results
      anchor: accelerated-delivery-and-enhanced-operational-excellence
    - label: Conclusion
      anchor: looking-forward-a-foundation-for-educational-innovation
---

## About Imagine Learning

Imagine Learning is a leading K-12 education technology company serving millions of students nationwide. Their applications support diverse learning activities across multiple subjects and grade levels, requiring numerous environments for development, testing, staging, and production. As the company has grown, so has the need for a scalable, reliable infrastructure to support their educational technology solutions.

## Scaling Education Infrastructure for the Next Generation

As a technology company focused on K-12 education, Imagine Learning's infrastructure needs are both complex and critical. Their existing Internal Developer Platform was struggling to keep pace with evolving demands, creating several challenges:

1. **Limited infrastructure visibility:** "It was really hard to determine the current state of every environment we managed," notes Blake Romano, Senior Software Engineer at Imagine Learning. Platform engineers lacked a unified view of their infrastructure, making it difficult to maintain consistency and troubleshoot issues.

2. **Complex, fragmented deployment processes:** "Deploying wasn't easy; there were multiple different pipelines depending on what you were deploying and how it would go out," explains Romano. This complexity increased cognitive load on developers and slowed down delivery cycles.

3. **Specialized language requirements:** Their existing infrastructure as code solution required team members to learn yet another specialized language outside their regular development workflows.

4. **Manual synchronization between infrastructure and Kubernetes:** Keeping Kubernetes configurations aligned with infrastructure changes required significant manual effort, increasing the risk of configuration drift and errors.

5. **Limited scalability:** As the company continued to grow, they needed a solution that could potentially scale to hundreds of environments while maintaining security and consistency.

These challenges were particularly acute because of Imagine Learning's commitment to educational excellence. Any downtime or inconsistency could directly impact teachers and students who rely on their platforms daily.

## Building a GitOps Bridge with Pulumi

After evaluating various options, Imagine Learning implemented what Romano calls the "GitOps bridge pattern" using Pulumi, ArgoCD, and GitHub to create a modern, scalable platform.

{{< youtube "1Q3XPmenthg" >}}

### Implementation Details

Imagine Learning's solution comprises several integrated components that work together to create a seamless workflow from infrastructure provisioning to application deployment:

Imagine Learning chose Pulumi to manage their multi-region infrastructure, leveraging TypeScript instead of specialized domain-specific languages. "Pulumi allows you to write infrastructure as code in a language you already know," explains Romano. "There's no more typing of this very weird syntax that I'm not super familiar with. If I'm writing my application code and I'm moving into writing some infrastructure code, it's the same coding language and the same coding semantics that I'm used to."

The team implemented Pulumi's Crosswalk for AWS library to apply best practices across their infrastructure, creating reusable components for consistency across environments. They managed multiple stacks with different configurations for development, staging, and production, while successfully deploying resources across multiple AWS regions including US-East-1, US-East-2, and US-West-2.

At the heart of their solution is a GitOps-driven workflow with Git as the single source of truth for both infrastructure and application configuration. They automated Pulumi deployments using GitHub Actions when changes are merged to the main branch, ensuring that Pulumi previews run on all stacks during pull requests to validate changes before merging. The team also implemented comprehensive testing and validation workflows to ensure all infrastructure changes were safe and reliable.

Perhaps the most innovative aspect of Imagine Learning's approach is what they call the "GitOps Bridge Pattern." This creates a seamless connection between Pulumi-managed infrastructure and Kubernetes using ArgoCD cluster secrets. They store infrastructure outputs from Pulumi (such as IAM role ARNs, VPC IDs, and other resource identifiers) as annotations in Kubernetes secrets, which Pulumi manages in GitHub and automatically updates when infrastructure changes. ArgoCD is configured to detect changes in these secrets and update cluster configurations accordingly, eliminating manual synchronization.

For dynamic environment management, the team implemented consistent configuration across all environments through Pulumi stack references. They created conditional deployment logic for environment-specific components, used Pulumi's state management to track all resources across environments, and integrated automated backup and disaster recovery solutions to ensure operational resilience.

The team chose Pulumi for several compelling reasons:

- **Familiar languages:** Developers could write infrastructure code in the same language as their application code (TypeScript), reducing context switching and learning curves.
- **Code reuse:** They could manage many different environments with different configurations using a single codebase, keeping their infrastructure definition DRY (Don't Repeat Yourself).
- **Comprehensive visibility:** The Pulumi UI provided auditing capabilities and state management, making it easy to track changes and troubleshoot issues.
- **Multi-region support:** They could easily deploy to multiple AWS regions from a single stack, supporting their geographic distribution needs.

## Accelerated Delivery and Enhanced Operational Excellence

By implementing the GitOps bridge pattern with Pulumi and ArgoCD, Imagine Learning achieved transformative improvements in their infrastructure management capabilities:

### Dramatically Accelerated Deployments

The most immediate and striking benefit was the dramatic reduction in deployment times, directly addressing their previous challenge of complex, fragmented deployment processes. "We have super fast deployments now to all of our environments at once," says Romano. "If I need to make a change, for example to an IAM role that needs to be used in Kubernetes, I can get that deployed out within probably 5-10 minutes."

This represents a dramatic improvement over their previous workflow, where similar changes could take days or weeks to propagate across all environments. Creating entirely new environments has also been transformed. "Building new environments takes hours now; it doesn't take weeks or even months," explains Romano.

### Enhanced Visibility and Confidence

The combination of Pulumi and GitOps methodologies has provided unprecedented visibility into their infrastructure, solving their previous challenge of limited infrastructure visibility:

- **Clear change previews:** "When I do a Pulumi preview, I get a nice diff of what is going to change and what specifically is going to change. Using GitHub Actions, I can automate that so every stack shows me that preview before I actually merge it into my main branch."
- **Built-in auditing:** "I get built-in auditing in the Pulumi UI of changes going on. I now have an easy way to check what were the changes that went out and what actually changed according to Pulumi."
- **State management:** "Pulumi manages state; it has all the information about what is currently deployed and what is the state of that resource."

### Reduced Cognitive Load and Context Switching

The platform team has experienced a significant reduction in cognitive overhead, addressing their challenge of specialized language requirements:

- **Consistent language:** "I'm no longer using some new language and some new tool to do my infrastructure as code. I'm just doing it in the same programming language I'm using throughout the rest of my day."
- **Unified GitOps pattern:** "We now have this continuity between our GitOps patterns. My GitOps pattern is now also with my infrastructure as code."
- **Automatic propagation:** "Updates to infrastructure in Pulumi automatically propagate to Kubernetes. There's no longer this world where I have to maybe go environment by environment."

This automated propagation directly solves their previous challenge of manual synchronization between infrastructure and Kubernetes.

### Enterprise-Grade Scalability

The solution has positioned Imagine Learning for continued growth and success, addressing their challenge of limited scalability:

- **Ability to scale to hundreds of environments:** "This model allows us to scale to potentially hundreds of different environments if we need to," says Romano, "which really meets our need to scale as an enterprise."
- **Consistent patterns across regions:** The solution works seamlessly across multiple AWS regions, supporting geographic distribution of services.
- **Reduced platform team burden:** The new approach reduces the burden on the platform team by streamlining infrastructure management and Kubernetes integration.

### Measurable Return on Investment

The productivity improvements achieved through Pulumi have delivered significant ROI for Imagine Learning. With a 10% productivity improvement across their engineering team of approximately 30 people, the company effectively gained the equivalent of 1.5 additional full-time developers without increasing headcount.

The payback period for their Pulumi investment was just 1.5 months, making this a highly cost-effective solution. More importantly, this additional capacity allows Imagine Learning to focus on innovation and educational excellence rather than infrastructure maintenance.

## Looking Forward: A Foundation for Educational Innovation

With their new platform in place, Imagine Learning's technology team can now focus on innovation rather than maintenance. The GitOps bridge pattern with Pulumi has given them a scalable, reliable foundation that can grow with their business needs while maintaining security and consistency.

The infrastructure modernization directly supports Imagine Learning's mission to provide excellent educational technology. By reducing deployment times and operational overhead, they can deliver new features and improvements to teachers and students more quickly, enhancing the learning experience.

Romano summarizes the impact: "All this has allowed us to move really quickly and also reliably. I'm not having to worry about copying what's in my infrastructure as code outputs and then pushing it in or building some custom connector between the two. I'm using the standardized patterns with ArgoCD and with Pulumi to get this connection flowing for any number of environments that I manage."

For educational technology companies like Imagine Learning, this kind of operational excellence translates directly into better educational outcomes. Fast, reliable infrastructure enables them to focus on their core mission: developing innovative educational technology that helps students succeed.
