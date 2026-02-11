---
title: "IDP Pattern: Cost control using Components, Policies, and constrained inputs"
linktitle: "Cost control using Components, Policies, and constrained inputs"
menu:
  idp:
    parent: idp-patterns
    weight: 90
aliases:
  - /docs/idp/best-practices/patterns/cost-control-using-components-policies-constrained-inputs/
meta_desc: Implement cost control through constrained component inputs, policies, and predefined options
allow_long_title: true
h1: "IDP Pattern: Cost control using Components, Policies, and constrained inputs"
description: <p>Implement cost control through constrained component inputs, policies, and predefined options.</p>
---

## Description

This pattern combines Pulumi components with constrained input types and policies to control infrastructure costs. By limiting available options and enforcing cost-related policies, organizations can prevent expensive configurations while maintaining developer productivity.

## When to use this pattern

- **Cost optimization**: When you need to control infrastructure spending across teams
- **Standardized sizing**: When you want to limit resource sizes to approved configurations
- **Budget enforcement**: When you need to prevent accidentally expensive deployments
- **Governance at scale**: When multiple teams need consistent cost controls

## When NOT to use this pattern

- **Flexible requirements**: When teams legitimately need varied resource configurations
- **Cost-insensitive environments**: When cost control is not a primary concern
- **Rapid experimentation**: When strict controls would impede innovation

## How to use this pattern

Define constrained input types and policies that enforce cost-related rules while providing components that only accept approved configurations.

### Example

Define cost-conscious types and validation:

```typescript
// types/cost-controls.ts
export type InstanceSize = "small" | "medium" | "large";
export type Environment = "dev" | "staging" | "prod";

export const INSTANCE_CONFIGS = {
  small: { instanceClass: "db.t3.micro", maxStorage: 100 },
  medium: { instanceClass: "db.t3.small", maxStorage: 500 },
  large: { instanceClass: "db.t3.medium", maxStorage: 1000 },
} as const;

export const ENVIRONMENT_LIMITS = {
  dev: { maxInstances: 2, allowedSizes: ["small"] as InstanceSize[] },
  staging: { maxInstances: 3, allowedSizes: ["small", "medium"] as InstanceSize[] },
  prod: { maxInstances: 10, allowedSizes: ["small", "medium", "large"] as InstanceSize[] },
} as const;

export function validateCostConstraints(size: InstanceSize, environment: Environment): string[] {
  const errors: string[] = [];
  const limits = ENVIRONMENT_LIMITS[environment];

  if (!limits.allowedSizes.includes(size)) {
    errors.push(`${environment} environment only allows sizes: ${limits.allowedSizes.join(", ")}`);
  }

  return errors;
}
```

Create cost-controlled components:

```typescript
// components/cost-controlled-database.ts
import { InstanceSize, Environment, INSTANCE_CONFIGS, validateCostConstraints } from "../types/cost-controls";

export interface CostControlledDatabaseArgs {
  size: InstanceSize;
  environment: Environment;
  storage: number;
}

export class CostControlledDatabase extends ComponentResource {
  constructor(name: string, args: CostControlledDatabaseArgs, opts?: ComponentResourceOptions) {
    super("acme:components:CostControlledDatabase", name, {}, opts);

    // Validate cost constraints
    const errors = validateCostConstraints(args.size, args.environment);
    if (errors.length > 0) {
      throw new Error(`Cost constraint violations:\n${errors.join('\n')}`);
    }

    const config = INSTANCE_CONFIGS[args.size];

    // Enforce storage limits
    if (args.storage > config.maxStorage) {
      throw new Error(`${args.size} size allows maximum ${config.maxStorage} GB storage`);
    }

    // Create database with cost-controlled configuration
    const db = new aws.rds.Instance(name, {
      instanceClass: config.instanceClass,
      allocatedStorage: args.storage,
      tags: {
        Environment: args.environment,
        Size: args.size,
        CostControlled: "true",
      },
    }, { parent: this });
  }
}
```

Enforce cost policies organization-wide:

```typescript
// policies/cost-control-policy.ts
import { PolicyPack, validateResourceOfType } from "@pulumi/policy";
import { validateCostConstraints } from "../types/cost-controls";
import { aws } from "@pulumi/aws";

new PolicyPack("cost-control-policies", {
  policies: [{
    name: "database-cost-control",
    description: "Enforce cost controls on database instances",
    enforcementLevel: "mandatory",
    validateResource: validateResourceOfType(aws.rds.Instance, (instance, args, reportViolation) => {
      const size = instance.tags?.Size as InstanceSize;
      const environment = instance.tags?.Environment as Environment;

      if (size && environment) {
        const errors = validateCostConstraints(size, environment);
        errors.forEach(error => reportViolation(error));
      }
    }),
  }],
});
```

Teams use constrained options:

```typescript
// Application team usage
const database = new CostControlledDatabase("app-db", {
  size: "medium",        // Limited to predefined sizes
  environment: "prod",   // Must match environment constraints
  storage: 200,          // Must be within size limits
});
```

## Related patterns

- [IDP Pattern: Policies as tests](/docs/idp/guides/best-practices/patterns/policies-as-tests) - For enforcing cost policies
- [IDP Pattern: Validating Component Inputs using Policy functions](/docs/idp/guides/best-practices/patterns/validating-component-inputs-using-policy-functions) - For shared validation logic
- [IDP Pattern: Components using other Components](/docs/idp/guides/best-practices/patterns/components-using-other-components) - For cost-controlled component hierarchies
