---
title: "IDP Pattern: Validating Component Inputs using Policy functions"
linktitle: "Validating Component Inputs using Policy functions"
menu:
  idp:
    parent: idp-patterns
    weight: 80
aliases:
  - /docs/idp/guides/best-practices/patterns/validating-component-inputs-using-policy-functions/
meta_desc: Use Pulumi policy functions to validate component inputs and enforce constraints at the component level
allow_long_title: true
h1: "IDP Pattern: Validating Component Inputs using Policy functions"
description: <p>Use Pulumi policy functions to validate component inputs and enforce constraints at the component level.</p>
---

## Description

This pattern involves creating reusable policy functions that can be used both in Pulumi Policy Packs and within component constructors to validate inputs. This ensures consistent validation logic across policy enforcement and component creation.

## When to use this pattern

- **Consistent validation**: When you want the same validation logic in policies and components
- **Early error detection**: When you want to catch configuration errors before deployment
- **Reusable validation**: When validation logic should be shared across multiple components
- **Developer experience**: When you want to provide helpful error messages for invalid inputs

## When NOT to use this pattern

- **Simple components**: When input validation would be trivial or unnecessary
- **Performance concerns**: When validation logic is expensive and slows component creation
- **One-off validation**: When validation is only needed in one place

## How to use this pattern

Create policy functions that can be imported and used by both Policy Packs and component constructors.

### Example

Define reusable policy functions:

```typescript
// policies/database-validation.ts
export interface DatabaseValidationArgs {
  instanceClass: string;
  storage: number;
  backupRetentionDays: number;
  multiAz: boolean;
  environment: "dev" | "staging" | "prod";
}

export function validateDatabaseInputs(args: DatabaseValidationArgs): string[] {
  const errors: string[] = [];

  // Validate instance class format
  if (!args.instanceClass.startsWith("db.")) {
    errors.push("Instance class must start with 'db.' (e.g., 'db.t3.micro')");
  }

  // Validate storage constraints
  if (args.storage < 20 || args.storage > 16384) {
    errors.push("Storage must be between 20 GB and 16,384 GB");
  }

  // Validate backup retention based on environment
  const minRetention = args.environment === "prod" ? 7 : 1;
  if (args.backupRetentionDays < minRetention) {
    errors.push(`${args.environment} environment requires backup retention >= ${minRetention} days`);
  }

  // Validate multi-AZ requirement for production
  if (args.environment === "prod" && !args.multiAz) {
    errors.push("Production databases must have Multi-AZ enabled");
  }

  return errors;
}
```

Use the policy function in a Policy Pack:

```typescript
// policies/database-policy.ts
import { PolicyPack, validateResourceOfType } from "@pulumi/policy";
import { validateDatabaseInputs } from "./database-validation";
import { aws } from "@pulumi/aws";

new PolicyPack("database-policies", {
  policies: [{
    name: "database-configuration",
    description: "Validate database configuration meets organizational standards",
    enforcementLevel: "mandatory",
    validateResource: validateResourceOfType(aws.rds.Instance, (instance, args, reportViolation) => {
      const errors = validateDatabaseInputs({
        instanceClass: instance.instanceClass,
        storage: instance.allocatedStorage,
        backupRetentionDays: instance.backupRetentionPeriod || 0,
        multiAz: instance.multiAz || false,
        environment: instance.tags?.Environment || "dev",
      });

      errors.forEach(error => reportViolation(error));
    }),
  }],
});
```

Use the same policy function in a component:

```typescript
// components/database.ts
import { validateDatabaseInputs } from "../policies/database-validation";

export class Database extends ComponentResource {
  constructor(name: string, args: DatabaseArgs, opts?: ComponentResourceOptions) {
    super("acme:components:Database", name, {}, opts);

    // Validate inputs using the same policy function
    const errors = validateDatabaseInputs(args);
    if (errors.length > 0) {
      throw new Error(`Invalid database configuration:\n${errors.join('\n')}`);
    }

    // Create database with validated inputs
    const db = new aws.rds.Instance(name, {
      instanceClass: args.instanceClass,
      allocatedStorage: args.storage,
      backupRetentionPeriod: args.backupRetentionDays,
      multiAz: args.multiAz,
      tags: { Environment: args.environment },
    }, { parent: this });
  }
}
```

This ensures consistent validation whether the database is created directly or through a component.

## Related patterns

- [IDP Pattern: Policies as tests](/docs/idp/guides/best-practices/patterns/policies-as-tests) - For organization-wide policy enforcement
- [IDP Pattern: Cost control using Components, Policies, and constrained inputs](/docs/idp/guides/best-practices/patterns/cost-control-using-components-policies-constrained-inputs) - For cost-related validation
- [IDP Pattern: Components using other Components](/docs/idp/guides/best-practices/patterns/components-using-other-components) - For validating complex component hierarchies
