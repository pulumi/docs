---
title: Blueprints
linktitle: Blueprints
menu:
  idp:
    parent: idp-best-practices
    identifier: idp-best-practices-blueprints
    weight: 30
meta_desc: Complete IDP blueprints that combine templates, components, environments, and policies to solve common platform engineering challenges
h1: IDP Blueprints
description: <p>Complete IDP blueprints that combine templates, components, environments, and policies to solve common platform engineering challenges.</p>
---

IDP Blueprints are comprehensive, production-ready solutions that demonstrate how to combine Pulumi IDP's [Four Factors framework](/docs/idp/best-practices/four-factors) to solve common platform engineering challenges. Unlike individual [patterns](/docs/idp/best-practices/patterns) that focus on specific techniques, blueprints provide complete end-to-end solutions that platform teams can implement directly or use as a foundation for their own customizations.

Each blueprint includes everything needed to deploy and operate a specific type of workload:

- **Templates** for developer self-service
- **Components** with secure defaults and business logic
- **Environment** configurations for different deployment contexts  
- **Policy packs** to enforce compliance and governance

## Blueprint Structure

Each blueprint is hosted in a single repository with a standardized directory structure that implements all four factors of the Pulumi IDP framework. This structure serves as a template for creating new blueprints and ensures consistency across your organization.

### Repository Structure

```
my-blueprint/
├── README.md                           # Blueprint overview and usage guide
├── docs/                               # Comprehensive documentation
│   ├── architecture.md                 # Architecture decisions and design
│   ├── template-guide.md              # Template usage and configuration
│   ├── component-guide.md             # Component customization guide  
│   ├── environment-guide.md           # Environment setup and management
│   └── policy-guide.md                # Policy enforcement and compliance
├── template/                          # Pulumi Template (Four Factors: Template)
│   ├── Pulumi.yaml                    # Template project definition
│   ├── package.json                   # Node.js dependencies (if applicable)
│   ├── tsconfig.json                  # TypeScript configuration (if applicable)
│   ├── index.ts                       # Template entry point
│   └── README.md                      # Template-specific documentation
├── components/                        # Pulumi Component (Four Factors: Component)
│   ├── PulumiPlugin.yaml             # Plugin definition file
│   ├── package.json                   # Component package definition
│   ├── tsconfig.json                  # TypeScript configuration
│   ├── index.ts                       # Component entry point and exports
│   ├── src/                           # Component implementation
│   │   ├── component.ts               # Main component logic
│   │   └── types.ts                   # Input/output type definitions
│   ├── tests/                         # Component testing
│   │   ├── unit/                      # Unit tests
│   │   └── integration/               # Integration tests
│   └── README.md                      # Component usage documentation
├── environments/                      # Pulumi ESC Environments (Four Factors: Environment)
│   ├── dev.yaml                       # Development environment configuration
│   ├── staging.yaml                   # Staging environment configuration
│   ├── prod.yaml                      # Production environment configuration
│   └── README.md                      # Environment management guide
├── policies/                          # CrossGuard Policy Pack (Four Factors: Policy)
│   ├── Pulumi.yaml                    # Policy pack project definition
│   ├── package.json                   # Policy pack dependencies
│   ├── tsconfig.json                  # TypeScript configuration
│   ├── index.ts                       # Policy definitions and exports
│   ├── tests/                         # Policy testing
│   │   ├── unit/                      # Policy unit tests
│   │   └── integration/               # Policy validation tests
│   └── README.md                      # Policy enforcement guide
└── examples/                          # Example implementations and usage
    ├── basic/                         # Basic usage example
    ├── advanced/                      # Advanced configuration example
    └── README.md                      # Examples overview
```

### Core Implementation Files

#### Template Implementation (`template/`)

The template provides the developer self-service interface:

- **`Pulumi.yaml`**: Project definition with template configuration section
- **`index.ts`**: Main template logic that instantiates the component
- **Template configuration**: Defines user inputs, defaults, and validation

#### Component Implementation (`components/`)

The component encapsulates organizational standards:

- **`PulumiPlugin.yaml`**: Required plugin definition for multi-language support
- **`src/component.ts`**: Main component class inheriting from ComponentResource
- **`src/types.ts`**: Input arguments and output types definitions
- **`index.ts`**: Component exports and public API

#### Environment Configuration (`environments/`)

ESC environments manage configuration and secrets:

- **Environment-specific YAML files**: Define configuration per deployment context
- **`imports`**: Reference shared configuration from other environments
- **`values`**: Configuration hierarchy including secrets and provider credentials
- **`environmentVariables`**: Export variables for stack configuration

#### Policy Pack (`policies/`)

CrossGuard policies enforce governance:

- **`index.ts`**: Policy definitions using validation and enforcement rules
- **Policy types**: ResourceValidation, StackValidation, and EnforcementLevel
- **Configuration**: Policy-specific settings and rule parameters

### Documentation Structure (`docs/`)

Each blueprint includes comprehensive documentation for all four factors:

- **`architecture.md`**: Overall system design, component relationships, and architectural decisions
- **`template-guide.md`**: How developers use the template, configuration options, and common workflows
- **`component-guide.md`**: Component architecture, customization points, and extension patterns
- **`environment-guide.md`**: Environment management, secrets handling, and multi-stage deployments
- **`policy-guide.md`**: Policy enforcement rules, compliance requirements, and remediation guidance

This structure ensures that every blueprint provides a complete, production-ready solution with clear separation of concerns and comprehensive documentation for platform teams and developers.

## Available Blueprints

### Secure Web App

A complete blueprint for deploying web applications with security best practices built in. Includes container orchestration, load balancing, TLS termination, and monitoring configuration.

**Use cases:** Frontend applications, API gateways, customer-facing web services
**Key features:** Zero-trust networking, automated certificate management, horizontal scaling

### Experimentation Sandbox

A safe, isolated environment for developer experimentation and prototyping. Provides cost controls, automatic cleanup, and security boundaries.

**Use cases:** Proof of concepts, training environments, temporary workloads
**Key features:** Cost budgets, time-based cleanup, network isolation

### Internal API Platform

A comprehensive platform for building, deploying, and operating internal APIs. Includes service discovery, authentication, rate limiting, and observability.

**Use cases:** Microservices architectures, internal tool APIs, data service endpoints
**Key features:** Service mesh integration, API versioning, automated documentation

### Multi-Tenant SaaS Platform

A scalable foundation for building software-as-a-service applications with proper tenant isolation, billing integration, and compliance controls.

**Use cases:** B2B SaaS products, customer portals, multi-tenant applications
**Key features:** Tenant isolation, usage tracking, compliance frameworks

### Data Engineering Platform

A modern data platform for ingesting, processing, and analyzing data at scale. Includes streaming pipelines, batch processing, and data governance.

**Use cases:** Data lakes, analytics workloads, ML pipelines
**Key features:** Schema management, data lineage, automated testing

## Getting Started

Before implementing any blueprint, ensure you have the foundational components in place:

### Prerequisites

1. **Pulumi IDP Setup**: Complete the [getting started guide](/docs/idp/get-started) to set up your Pulumi IDP environment
2. **Private Registry**: Configure a [private registry](/docs/idp/get-started/private-registry) for your organization's components and templates
3. **Policy Framework**: Establish your [policy requirements](/docs/iac/crossguard) and governance standards

### Implementation Approach

Each blueprint is designed to be:

- **Incrementally adoptable**: Start with core components and add features over time
- **Customizable**: Modify templates and components to match your organizational requirements
- **Composable**: Mix and match elements from different blueprints as needed

### Foundational Knowledge

Before diving into specific blueprints, familiarize yourself with:

- [Four Factors framework](/docs/idp/best-practices/four-factors) - The architectural foundation
- [IDP patterns](/docs/idp/best-practices/patterns) - Common techniques and approaches
- [Pulumi components](/docs/iac/concepts/components) - Building reusable infrastructure abstractions
- [ESC environments](/docs/esc/environments) - Managing configuration and secrets
- [Pulumi CrossGuard](/docs/iac/crossguard) - Enforcing policies and compliance

## Additional Resources

- [Get Started with Pulumi IDP](/docs/idp/get-started)
- [IDP Workflows](/docs/idp/get-started/workflows)
- [Private Registry Setup](/docs/idp/get-started/private-registry)
