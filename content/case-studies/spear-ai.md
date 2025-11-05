---
title_tag: Spear AI | Case Studies
title: "Spear AI: Achieving Government ATO in 3 Months"
description: |
    Defense tech startup accelerates compliance timelines to bring capabilities to market up to 6x faster while enabling rapid deployment across air-gapped cloud and edge environments.
meta_desc: Learn how Spear AI used Pulumi to achieve government Authorization to Operate in 3 months.

customer_name: Spear AI
customer_logo: /logos/customers/spearAI.svg
customer_url: https://www.spear.ai/

quote_block:
  quote: |
      “We gave our auditors access to our policy packs because it’s far easier to understand and prove controls in code than in docs and diagrams. With Pulumi’s Policy as Code approach, that manual review process has gone away. We’ve reduced our Authority to Operate (ATO) timeline from a year and a half to expecting approval in three months.” Michael Hunter, CEO, Spear AI
  quote_attrib: Michael Hunter, CEO, Spear AI
  headline_stat: 6x faster time to achieve ATO

exec_summary: |
    Spear AI delivers cutting-edge AI solutions that accelerate mission-critical decision-making for defense operators. By transforming how tactical sensor data is processed and analyzed, Spear AI enhances situational awareness and operational capacity across edge and cloud environments. The company specializes in automated data labeling and intelligent model deployment for complex sensor systems, enabling the US Navy to maintain tactical superiority through faster, more informed decisions in dynamic operational environments. 
    
    The Spear AI engineering team faced several challenges in bringing these advanced capabilities to market, including deploying and managing resources at multiple clearance levels, ranging from AWS commercial cloud to GovCloud, air-gapped AWS Top Secret Cloud, and even hardware at sea. They chose Pulumi to help bring their capabilities to market quickly, leveraging its infrastructure as code and policy-enforcement capabilities that work across all these use cases. By adopting Pulumi, the team was able to quickly stand up development environments, deploy services that comply with AWS Secret Cloud restrictions, and achieve Authorization to Operate (ATO) in 3 months – a process that can take up to 24 months to meet stringent defense requirements. 
    
    By partnering with Pulumi, the Spear AI team is pioneering the future of defense infrastructure: demonstrating how modern platform engineering will transform government technology delivery.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: Challenge
      anchor: challenge-military-grade-infrastructure-at-the-speed-of-ai
    - label: Solution
      anchor: solution-infrastructure-as-code-with-built-in-governance
    - label: Architecture
      anchor: architecture-reproducible-environments-from-cloud-to-submarine
    - label: Results
      anchor: results-transforming-government-compliance-through-code
    - label: Technical Implementation
      anchor: technical-implementation-modern-development-workflows
    - label: Looking Forward
      anchor: looking-forward-infrastructure-for-national-security-innovation
    - label: About Spear AI
      anchor: about-spear-ai
---

## Challenge: Military-grade Infrastructure at the Speed of AI

As an innovator in the defense technology space, Spear AI faced a unique infrastructure challenge that would test the limits of traditional tooling: they needed to build infrastructure that could operate on standard AWS cloud services for development, the classified air-gapped AWS Secret Cloud for government operations, and manage edge deployments on nuclear submarines. These are daunting requirements for any organization, let alone a seed-stage startup.

The traditional path to government Authorization to Operate (ATO) certification, a mandatory cybersecurity process for Department of Defense contractors, typically takes 6 to 24 months of manual documentation, security testing, remediation, and review. "The accreditation process with the government is intense," explains Michael Hunter, co-founder and CEO at Spear AI. "The first part consists of an architecture review, and the second part involves demonstrating security controls. The traditional process involved reviewing templates line by line, implementing tests, and creating architectural diagrams. Then, auditors go through architecture diagrams and the cloud console to click around to see if the diagram matches the implementation."

For a fast-moving startup, this timeline and manual process posed a bottleneck that could derail their ability to get their product to market and serve government customers. Instead of adopting a lengthy, manual process, the team sought to accelerate time to market by applying preventive policies and state management to demonstrate compliance in a verifiable, automated way.

## Solution: Infrastructure as Code with Built-in Governance

After evaluating legacy infrastructure approaches and next-generation solutions, Spear AI selected Pulumi as the only platform capable of meeting both defense-grade security requirements and delivering startup speed.

"We specifically liked the guardrails that Pulumi policy capabilities provided," Michael notes. "We were very attracted to the idea of writing infrastructure in TypeScript and using all the benefits of modern languages. We wanted to try something new as we had a lot of bad experiences with template-driven tools like Terraform."

Dennis Torres, VP of Software, says: "CDK isn't portable - if you want to deploy to non-AWS environments like submarines, it's not really the right tool. With Terraform's HCL, it's hard to use and tends to grow out of control unless you're very diligent about splitting things into modules."

The team implemented a comprehensive infrastructure strategy using:

- [Pulumi Infrastructure as Code](https://www.pulumi.com/docs/iac/) for multi-environment deployments
- [Policy as Code](https://www.pulumi.com/docs/support/faq/policies/) for automated compliance verification
- [Pulumi ESC](https://www.pulumi.com/product/secrets-management/) for secrets and configuration management
- [Review Stacks](https://www.pulumi.com/docs/deployments/deployments/review-stacks/) for rapid development environment provisioning and cost management
- [Kubernetes](https://www.pulumi.com/registry/packages/kubernetes/api-docs/) for portability across all deployment targets, from Amazon EKS to edge clusters

## Architecture: Reproducible Environments from Cloud to Submarine

Spear AI's infrastructure spans three critical environments, each with unique constraints:

### 1. Development Environment (AWS Commercial Cloud)

The Spear team uses Pulumi to manage standard AWS services for rapid iteration and testing, integrated with modern development workflows including GitHub Actions, Vercel deployments, and Neon database branching.

### 2. Government Environments (AWS GovCloud, AWS Secret Cloud, AWS Top Secret Cloud)

Production operates in regions ranging from GovCloud to the air-gapped AWS Secret Cloud environment and will also need to support Top Secret Cloud. These environments lack many standard services, such as Amazon SES (email), ACM (certificate management), and third-party APIs for AI/ML model serving. Spear AI uses Pulumi to rapidly provision custom services to replicate missing cloud functionality in this environment.

### 3. Edge Deployments (Nuclear Submarines)

On-premises Kubernetes environments make it easy to mirror cloud architectures at the edge. "If you think of a nuclear submarine, it's essentially a data center underwater," Michael explains.

The unifying technology is EKS, chosen explicitly for its portability. "We're migrating everything to EKS to take advantage of the uniformity and portability that EKS enables," Dennis explains. "There's no ECS on a submarine—it's just easier for us to write a Kubernetes pod once and deploy it across all environments from sea to cloud," says Dennis.

## Results: Transforming Government Compliance Through Code

### 6x Faster Authority to Operate (ATO)

The most dramatic result was the compression of government compliance timelines from an average of 18 months to 3 months. This acceleration came from Pulumi's ability to express security controls as code rather than traditional documentation and templates.

"We gave our auditors access to our policy packs because it's far easier to understand and prove controls in code than in a bunch of docs and diagrams," Michael explains. "That process [of manual review] has gone away. We've gone down from a year and a half to expecting an ATO in three months."

### Improved Code Readability and Review Speed

The shift from Terraform HCL to TypeScript dramatically improved code review and audit processes. "When you look at a Pulumi stack, it's just easier to understand and grok versus Terraform HCL," Dennis notes. "HCL is far too verbose, which makes it hard for auditors to really understand how your proposed implementation works."

This readability improvement directly impacts compliance review speed, as auditors can more easily verify security controls embedded in readable code rather than parsing complex domain-specific languages that can be 10 times more verbose.

### Democratized Infrastructure Access

By using familiar programming languages, Spear AI achieved infrastructure democratization across its engineering team. "It doesn't end up falling on any one person's plate—any engineer, if they need to make a change to the stack, can do so, even if they're not an infrastructure expert," Dennis explains. "The combination of modern languages and policy gives the team safety and control."

This follows the same model as Docker's democratization effect: "Everyone can modify a Dockerfile and spin up their infrastructure in their local machine. If it works there, it will work in the cloud."

### Rapid Service Provisioning

The combination of Pulumi's development velocity and Review Stacks capabilities enables rapid experimentation. Dennis was able to "spin up new capabilities in less than a week," compared to estimates of "over a month" using traditional approaches.

Michael provides a broader context: "We have one cloud engineer who has done the work of seven cloud engineers at a traditional government contractor that is not using Pulumi - and we're building comparable infrastructure in half the time."

Pulumi's preview deployments integrate seamlessly with existing development workflows. "Having preview deployments trigger on pull request is a workflow that we're used to and was really difficult before with other infrastructure as code tools," Dennis explains.

The team leverages this capability alongside other branch-based development tools:

- Next.js applications with Vercel branch deployments
- Postgres databases with Neon branch deployments
- Infrastructure with Pulumi review stacks

## Technical Implementation: Modern Development Workflows

Learn more in the [Pulumi documentation](/docs/).

### Policy as Code for Automated Compliance

Pulumi's policy packs enable Spear AI to encode security requirements directly into its infrastructure deployment process. This ensures that every deployment can automatically prove compliance with government requirements, without manual review.

### Secrets Management with Pulumi ESC

"We're using ESC for config and for secrets," Dennis confirms. This avoids the common pitfall of "committing all the secrets to a repo," significantly improving security posture and collaboration workflows.

### Developer Experience Benefits

"It's fun to write Pulumi code," Dennis observes. "Because it's a programming language, you inherit all the benefits that you get from your programming language of choice: you get benefits like type completion." Now that the team is adopting LLM-powered code assistants like Anthropic Claude, they are finding that type completion is even more valuable.

## Looking Forward: Infrastructure for National Security Innovation

Spear AI's success with Pulumi establishes the new standard for defense technology delivery. This isn't just one company's success story: it's a blueprint that will fundamentally transform how government contractors approach infrastructure, compliance, and speed to mission. By pioneering infrastructure as code for the most demanding environments on Earth, Spear AI and Pulumi have proven that there's no trade-off between security and speed, between compliance and innovation. This approach will become the standard for any organization serious about both governance and velocity.

This success establishes Pulumi as the platform enabling the next generation of defense technology companies. As AI and cloud-native approaches become mission-critical, the infrastructure platform that enables both speed and security will determine competitive advantage in national security.

As Michael concludes, "The time from first commit to production code was lower than I was expecting. If I can do it, anybody on the team should be able to do it."

## About Spear AI

Spear AI is a defense technology startup building AI-powered solutions for government and military applications. They operate across multiple security environments, from commercial cloud to classified systems and edge deployments on naval vessels.

---

Ready to accelerate your compliance timeline while maintaining security?

[Start Free](https://app.pulumi.com/signup) | [Talk with an Expert](/contact/?form=request-a-demo)
