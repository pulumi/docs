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

These delays slow the entire delivery pipeline. Teams add buffer time for infrastructure delays, projects slip, and the business sees technology as slow-moving. Meanwhile, the real culprit—slow provisioning that kills momentum when ideas need testing—gets buried in ticket queues and approvals.

#### Day 2 And Beyond Chaos: Sprawling, Unpredictable Infrastructure = Operational Nightmare

Day 1 bottlenecks frustrate developers, but the real long-term cost is patching hell. Copy-paste infrastructure creates hundreds of snowflakes, each needing manual attention for every security fix or version bump. One-off configurations and custom environments pile up, creating technical debt no one fully understands.

Operations teams are overwhelmed by the basic, critical task of simply keeping the lights on across a sprawling, inconsistent landscape.

## The Solution: Two-Level Abstraction and Self Service

Self-service capabilities are most effective when built on a two-level abstraction model that separates the "what" (developer intent) from the "how" (implementation details). This approach enables organizations to combine the velocity of self-service with the control of centralized management.

Internal Developer Platforms (IDPs) often implement a "two-level" architecture that establishes a clear separation of responsibilities within an organization:

**Level 1: Platform Team (Module Definition)**
- Creates and maintains reusable infrastructure modules
- Embeds organizational standards and best practices
- Abstracts complex infrastructure details
- Implements security, compliance, and scalability guardrails
- Updates modules as technologies and requirements evolve

**Level 2: Application Developers (Module Consumption)**
- Discover available modules through a self-service catalog
- Compose pre-built modules to create application infrastructure
- Focus on application logic rather than infrastructure complexities
- Operate within organizational guardrails
- Deploy applications faster with standardized components

This approach balances standardization with flexibility, creating an environment where developers can move quickly while platform teams maintain control over critical infrastructure concerns.

## The Power of Intent-Based Specification

One of the most important benefits of the two-level approach is how it addresses the problem of **over-specification** versus **intent-based specification**:

**Over-specification** occurs when developers must define excessive infrastructure details that:
- Require specialized knowledge they may not possess
- Create tight coupling to specific implementations
- Make future changes difficult or impossible
- Lead to inconsistency across applications
- Distract from application logic

**Intent-based specification** means developers express exactly what their application needs to accomplish, without detailing how it should be implemented:
- Developers specify intent rather than implementation
- Platform teams can update underlying infrastructure without breaking applications
- Applications remain portable across different environments
- Defaults can evolve over time without requiring application changes
- New capabilities can be added without disrupting existing applications

The two-level approach embraces intent-based specification as a core principle. This intentional focus on developer intent rather than implementation details creates a more maintainable, evolvable system for both platform teams and application developers.

## Practical Example: Java Application with Kafka, PostgreSQL, and Redis

The platform team has defined several reusable modules:

#### Java Application Module

The platform team creates a module that handles all aspects of Java application deployment. This includes managing different Java runtime versions (8, 11, 17), configuring memory settings and JVM options, containerizing, setting up application scaling rules, and implementing standard health checks, monitoring, and kubernetes namespacing. Behind the scenes, the module handles container configurations, security scans, resource limits, and integration with the organization's logging infrastructure.

#### Kafka Integration Module

This module manages the complexities of Kafka integration, including broker connections, authentication methods, topic configurations, and security settings. The platform team handles details like setting up the proper SASL/SSL authentication, configuring appropriate replication factors, managing ACLs, and ensuring that all communication is encrypted in transit.

#### PostgreSQL Database Module

The database module abstracts database provisioning and management for different PostgreSQL versions. It handles configuration of different database sizes with appropriate CPU, memory, and storage allocations. The module also manages connection pooling, backup schedules, retention policies, and ensures proper encryption both at rest and in transit.

#### Redis Cache Module

For caching needs, the Redis module provides different cache sizes with appropriate memory and connection limits. It configures eviction policies, encryption, and integration with the organization's monitoring systems.

### Level 2: Developer Implementation

Developers interact with a much simpler interface. A new Java service using Kafka, postgres, redis can state it's intent:

```yaml
# Developer's configuration
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

## Benefits of Intent-Based Specification: Solving Day 1 and Day 2 Challenges

The intent-based specification approach directly addresses both the immediate bottlenecks and long-term operational challenges:

**Eliminating Day 1 Bottlenecks**
- **From Weeks to Minutes**: Developers who previously waited days for infrastructure can now self-provision in minutes using pre-approved modules
- **Focus Preservation**: By removing the context-switching penalty of infrastructure delays, developers maintain creative momentum
- **Reduced Learning Curve**: New team members can be productive immediately without extensive infrastructure knowledge

**The Self-Service Transformation in Action:**

Let me streamline the table while still covering all the essential points:

| Developer Experience | Platform Response |
|---|---|
| Submits simple YAML with intent-based configuration | Validates against policies and expands into complete infrastructure |
| Focuses on application needs, not infrastructure details | Provisions resources with appropriate sizing and security controls |
| Specifies "what" is needed, not "how" to configure it | Handles networking, monitoring, backups, and credentials |
| No expertise required in Kubernetes, networking, or security | Implements best practices automatically across all deployments |
| | Maintains and updates the underlying implementation over time |

This condensed version captures the essence of the relationship while reducing the number of rows and avoiding repetition.

**Preventing Day 2 Chaos**
- **Consistency By Design**: The copy-paste anti-pattern disappears as all applications use the same underlying modules, creating natural standardization
- **Simplified Patching and Updates**: When security vulnerabilities emerge, platform teams update modules once rather than hunting for every custom implementation
- **Evolution Without Disruption**: Infrastructure can be upgraded, replaced, or migrated without breaking dependent applications
- **Operational Clarity**: Operations teams gain predictable, consistent environments that follow established patterns

This approach transforms infrastructure from a developer burden into an organizational asset that becomes more valuable over time, rather than decaying into technical debt.

## Conclusion

The two-level architecture of IDPs creates a powerful interface between platform teams and application developers. By embracing intent-based specification, this approach enables developers to clearly express what they need with minimal complexity while giving platform teams the flexibility to implement and evolve the underlying infrastructure.

This approach ensures that developers can self-serve their infrastructure needs through composable modules, while platform teams maintain control over how those needs are ultimately fulfilled. The result is a development environment that balances speed and autonomy with standardization and control, creating a system that can evolve gracefully over time without disrupting the developer experience.