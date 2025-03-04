---
title: "Platform Engineering Pillars 3: Self-Service Infrastructure"
date: 2025-03-06T10:06:40-05:00
draft: false
meta_desc: Unlock developer productivity with self-service infrastructure through modular abstraction and intent-based specifications for your internal developer platform.
meta_image: meta.png
authors:
    - adam-gordon-bell
tags:
    - platform-engineering
    - platform-engineering-pillars
social:
    twitter: >
            Self-Service Infrastructure: the key to scaling platform engineering! Learn how to break free from approval bottlenecks, implement modular abstractions, and create two-level architectures that empower developers while maintaining governance. Stop fighting manual processes and start building platforms that scale.
    linkedin: >
            Self-service infrastructure is critical for successful platform engineering. Is your organization trapped in approval bottlenecks?

            🚨 The Challenges:
            • Copy-paste infrastructure anti-patterns
            • Ticketing system bottlenecks
            • Developers grappling with low-level details
            • Slow provisioning and inconsistent implementations

            🛠️ The Solution:
            Implement modular, intent-based infrastructure with a two-level abstraction model as a core pillar of your internal developer platform.
---

In previous articles, we explored the core principles of platform engineering and showed how Infrastructure as Code (IaC) builds a reliable foundation for a developer platform. With version-controlled infrastructure and automated deployments, teams can ensure consistency and repeatability across environments.

Even with these in place, a critical bottleneck remains: the provisioning process itself. Without proper modularity and a clear separation between intent and infrastructure details, things get messy—leading to friction, delays, and unnecessary complexity.

## The Missing Layer: Abstraction Through Modularity

This problem comes down to how infrastructure is defined and used. Without proper abstraction layers, infrastructure code often turns into:

- Massive YAML or HCL files with hundreds or thousands of lines of configuration
- Highly detailed specifications that require deep domain knowledge
- Environment-specific configurations with subtle variations across deployments
- Complex interdependencies that are difficult to trace and verify

This approach burdens developers with low-level details they don’t need to worry about, while platform teams become gatekeepers, reviewing intricate configurations. Alternatively, a traditional ticketing model takes over, discarding the benefits of modern practices.

What’s missing in many organizations is a proper abstraction layer between raw infrastructure code and developer needs. Without modular, reusable infrastructure patterns, every new application deployment becomes an exercise in starting from scratch—defining every detail instead of just stating what the application requires.

### Common Anti-Patterns Without Proper Abstraction

Without modular infrastructure, organizations typically fall into one of two problematic patterns.

**The Copy-Paste Anti-Pattern**

In many teams, developers copy and paste infrastructure code from past projects. They grab a similar setup, duplicate hundreds of lines of configuration, tweak settings, hope they got it right, and submit it for review. This leads to a brittle system with siloed knowledge—security fixes must be applied manually across every instance, no one has a full picture of the infrastructure and Day 2 Operations become error prone.

It feels like control, but it's not. Developers still rely on platform specialists to validate changes and catch mistakes.

**The Ticketing Anti-Pattern**

Alternatively, some organizations rely on rigid ticketing systems for infrastructure changes. A platform specialist applies the changes, ensuring security and consistency—but also creating bottlenecks. Developers might wait days or weeks for simple modifications, left out of the process entirely.

This guarantees expert oversight but strips developers of autonomy, making the platform team a bottleneck for every deployment.

Neither anti-pattern strikes a balance between standardization and autonomy, leading to either sloppy infrastructure (copy-paste) or slow deployments (ticketing).

### The Resulting Problems

#### Day 1 Bottleneck: Slow, Manual Infrastructure = Developer Gridlock

When provisioning becomes a bottleneck, developers with finished code wait days for infrastructure. This disrupts focus and forces frequent context switching. They juggle tasks to stay productive, then have to rebuild focus when infrastructure is ready.

These delays slow the entire delivery pipeline. Teams add buffer time for infrastructure delays, projects slip, and the business sees technology as slow-moving. Meanwhile, the real culprit—slow provisioning that kills momentum—gets buried in ticket queues and approvals.

#### Day 2 And Beyond Chaos: Sprawling, Unpredictable Infrastructure = Operational Nightmare

Day 1 bottlenecks frustrate developers, but the real long-term cost is patching hell. Copy-paste infrastructure creates hundreds of snowflakes, each needing manual attention for every security fix or version bump. One-off configurations and custom environments pile up, creating technical debt no one fully understands.

Operations teams are overwhelmed by the basic, critical task of simply keeping the lights on across a sprawling, inconsistent landscape.

## The Solution: Two-Level Abstraction and Self Service

Self-service works best with a two-layer model: what developers need (intent) and how it's implemented (infrastructure details). This lets teams move fast without losing control.

A strong self-service approach divides responsibilities into two clear layers:

**Level 1: Platform Team (Module Definition)**

- Builds and updates reusable infrastructure modules
- Bakes in security, compliance, and best practices
- Hides complexity so developers don’t need to worry about low-level details
- Sets guardrails for scalability, security, and compliance
- Updates modules as technologies and needs change

**Level 2: Application Developers (Module Consumption)**

- Browse a catalog of ready-made modules
- Compose pre-built modules to set up application infrastructure
- Spend time on code, not cloud configurations
- Operate within built-in guardrails
- Deploy applications faster using standardized components

This setup keeps things fast and flexible. Developers get the autonomy to build without reinventing infrastructure, while platform teams maintain control where it matters.

## The Power of Intent-Based Specification

The two-level approach works by replacing over-specification with intent-based design.

Over-specification happens when developers specify too many infrastructure details that:
- Require expertise they might not have
- Tightly couple infrastructure to specific implementations
- Make future changes hard or even impossible

Intent-based specification means developers state what their app needs, not how to implement it, meaning:
- Platform teams can update underlying infrastructure without breaking applications
- New capabilities can be added without disrupting existing applications

By focusing on what developers need, not how it's built, it creates a system that’s easier to maintain and evolve for both platform teams and developers.

## Practical Example: Java Application with Kafka, PostgreSQL, and Redis

The platform team provides reusable modules:

#### Java Application Module

This module handles everything needed to run a Java app. It covers the Java runtime, memory settings, JVM options, scaling rules, health checks, monitoring, and Kubernetes namespacing. It also manages containers, security scans, resource limits, and logging integration—so developers don’t have to.

#### Kafka Integration Module

Similarly this module simplifies Kafka integration, handling broker connections, authentication, topics, and security. It takes care of SASL/SSL authentication, replication factors, ACLs, and encryption. Developers just specify topics and schemas.

And so on for common infrastructure components used in the org.

### Level 2: Developer Implementation

Developers use a simpler interface. To deploy a new Java service with Kafka, PostgreSQL, and Redis, they only need to specify the required input parameters in the platform-defined modules:

```yaml
# Developer's intent based configuration
application:
  name: order-processing-service
  module: java-application
  version: 17
  memory: 2GB
  scaling:
    min: 2
    max: 10
  
integrations:
  - module: kafka
    topics:
      - name: incoming-orders
        partitions: 5
      - name: processed-orders
        partitions: 3
    consumer_group: order-processors
  
  - module: postgresql
    database: orders_db
    size: medium
    backup: enabled
  
  - module: redis
    size: small
    ttl: 3600
```

( Note: YAML not required. This code could be UI driven, or it could be written in your programming langague of choice. The point is it only specifies intent and defers specifics to the platform. )

## Solving Day 1 and Day 2 Challenges

The intent-based specification solves immediate and long term problems:

**Eliminating Day 1 Bottlenecks**
- **From Weeks to Minutes**: Developers who previously waited days for infrastructure can now self-provision in minutes using pre-approved modules
- **Focus Preservation**: By removing the context-switching penalty of infrastructure delays, developers maintain creative momentum
- **Reduced Learning Curve**: New team members can be productive immediately without extensive infrastructure knowledge

**The Self-Service Transformation in Action:**

| Developer Experience | Platform Response |
|---|---|
| Submits simple YAML with intent-based configuration | Validates against policies and expands into complete infrastructure |
| Focuses on application needs, not infrastructure details | Provisions resources with appropriate sizing and security controls |
| Specifies "what" is needed, not "how" to configure it | Handles networking, monitoring, backups, and credentials |
| No expertise required in Kubernetes, networking, or security | Implements best practices automatically across all deployments |
| | Maintains and updates the underlying implementation over time |

**Preventing Day 2 Chaos**
- **Consistency By Design**: The copy-paste anti-pattern disappears as all applications use the same underlying modules, creating natural standardization
- **Simplified Patching and Updates**: When security vulnerabilities emerge, platform teams update modules once rather than hunting for every custom implementation
- **Evolution Without Disruption**: Infrastructure can be upgraded, replaced, or migrated without breaking dependent applications
- **Operational Clarity**: Operations teams gain predictable, consistent environments that follow established patterns

This approach transforms infrastructure from a developer burden into an organizational asset that becomes more valuable over time, rather than decaying into technical debt.

### **Developer Interaction Models: Choosing Your Platform Interface**

The next key decision is how developers will actually *use* this platform.  The ideal interface balances ease of use with necessary flexibility.  Each organization may have different needs and so a spectrum of interaction models exist, each with its own trade-offs. Tree common approaches are: CLI-Driven Infrastructure as Code, the Self-Service Portal, and a Hybrid model.


| Aspect | CLI-Driven | Self-Service Portal | Hybrid Approach |
|--------|------------|---------------------|-----------------|
| **Developer Experience** | Code-based, using IaC tools directly | Click-based UI with forms and catalogs | Portal for common tasks, code for customization |
| **Code Visibility** | Full visibility and control | Limited or no visibility | Visible but with varying levels of access |
| **Governance** | Trust-based or PR reviews | Enforced through portal constraints | Guided paths with managed exceptions |
| **Learning Curve** | Higher (requires IaC knowledge) | Lower (minimal infrastructure knowledge) | Moderate (basic UI with optional advanced use) |
| **Best For** | Experienced teams needing flexibility | Teams prioritizing speed and standardization | Organizations with diverse skill levels |

#### **1. CLI-Driven Infrastructure as Code: Empowering Developers with Familiar Tools**

In this approach, platform teams build reusable infrastructure modules while developers consume them directly through code. Developers use familiar IaC tools like Pulumi CLI to instantiate these modules, with changes flowing through version control like any other code.

The key strength is transparency and familarity. Developers maintain visibility and ownership of their intent based defintions. This code-centric workflow integrates naturally with existing development practices.

However, this flexibility creates governance challenges. Appliation teams can work around standards requires either strong trust or approval processes that might reintroduce bottlenecks. The approach also assumes developers have some IaC knowledge, making it best suited for organizations with mature DevOps practices and experienced teams.

#### **2. Self-Service Portal: Click-Ops Simplicity for Rapid Provisioning**

The self-service portal approach creates a web interface where developers provision infrastructure without writing code. They simply browse a catalog, fill out forms, and click buttons to deploy standardized resources—all pre-configured by the platform team.

This approach keeps infrastructure code completely centralized and hidden from developers. The portal translates simple selections ("Add Database: Medium Size") into the appropriate underlying configurations, ensuring perfect compliance with organizational standards.

The result is dramatically reduced friction and learning curve, enabling even infrastructure novices to deploy resources in minutes. However, this simplicity comes at the cost of flexibility—customizations typically require platform team involvement, making this model ideal for organizations with predictable workloads or where standardization outweighs customization needs.

#### **3. Hybrid Approach: Code-Backed Self-Service**

The hybrid approach generates and modifies infrastructure code via pull requests from UI interactions. When developers configure resources through the portal, the system commits code to repositories automatically, creating a transparent workflow where changes are visible, reviewable, and auditable through standard Git processes.

This model provides both simplicity and flexibility. Routine tasks remain point-and-click while complex scenarios allow direct code editing within the same PR workflow. The approach maintains a complete audit trail through commit history while giving platform teams visibility into all changes.

The significant tradeoff is implementation complexity: building a system that generates commits and PRs based on version control integration requires substantial investment. Organizations must weigh this upfront cost against the long-term benefits of combining UI simplicity with code transparency.

## Conclusion

The two-level architecture of IDP self service creates a powerful interface between platform teams and application developers. By embracing intent-based specification, this approach enables developers to clearly express what they need with minimal complexity while giving platform teams the flexibility to implement and evolve the underlying infrastructure.

This approach ensures that developers can self-serve their infrastructure needs through composable modules, while platform teams maintain control over how those needs are ultimately fulfilled. The result is a development environment that balances speed and autonomy with standardization and control, creating a system that can evolve gracefully over time without disrupting the developer experience.