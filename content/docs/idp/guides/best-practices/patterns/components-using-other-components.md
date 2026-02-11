---
title: "IDP Pattern: Components using other Components"
linktitle: "Components using other Components"
menu:
  idp:
    parent: idp-patterns
    weight: 70
aliases:
  - /docs/idp/guides/best-practices/patterns/components-using-other-components/
meta_desc: Build complex infrastructure patterns by composing Pulumi components that use other components
h1: "IDP Pattern: Components using other Components"
description: <p>Build complex infrastructure patterns by composing Pulumi components that use other components.</p>
---

## Description

This pattern involves creating Pulumi components that internally use other components, creating a hierarchy of reusable infrastructure patterns. Higher-level components encapsulate complex architectures while lower-level components handle specific infrastructure concerns.

## When to use this pattern

- **Integrated architectures**: When you need to combine multiple types of infrastructure
- **Shared components**: When you have components that need to be used both internally by higher-level components and directly by end users
- **Reusable patterns**: When you have common architectural patterns across applications
- **Progressive complexity**: When you want to build from simple to complex components

## When NOT to use this pattern

- **Simple use cases**: When a single component would suffice
- **Over-abstraction**: When the complexity doesn't align with your organization's developer experience or policy needs

## How to use this pattern

Components can compose other components to build higher-level abstractions while maintaining clear interfaces and responsibilities.

### Example

Building a web application component that uses database and networking components:

```typescript
// Lower-level components
export class Database extends ComponentResource {
  public readonly connectionString: Output<string>;
  public readonly securityGroupId: Output<string>;

  constructor(name: string, args: DatabaseArgs, opts?: ComponentResourceOptions) {
    super("acme:components:Database", name, {}, opts);

    // Create security group for database access
    const dbSecurityGroup = new aws.ec2.SecurityGroup(`${name}-sg`, {
      vpcId: args.vpcId,
      ingress: [{
        protocol: "tcp",
        fromPort: 5432,
        toPort: 5432,
        cidrBlocks: [args.allowedCidr],
      }],
    });

    // Create DB subnet group
    const subnetGroup = new aws.rds.SubnetGroup(`${name}-subnet-group`, {
      subnetIds: args.subnetIds,
    });

    // Create RDS instance
    const db = new aws.rds.Instance(name, {
      engine: "postgres",
      instanceClass: args.instanceClass,
      allocatedStorage: args.storage,
      dbSubnetGroupName: subnetGroup.name,
      vpcSecurityGroupIds: [dbSecurityGroup.id],
      backupRetentionPeriod: args.backupDays || 7,
      // ... other configuration
    });

    this.connectionString = db.endpoint.apply(endpoint =>
      `postgresql://${args.username}:${args.password}@${endpoint}/${args.dbName}`
    );
    this.securityGroupId = dbSecurityGroup.id;
  }
}

export class Network extends ComponentResource {
  public readonly vpcId: Output<string>;
  public readonly subnetIds: Output<string[]>;

  constructor(name: string, args: NetworkArgs, opts?: ComponentResourceOptions) {
    super("acme:components:Network", name, {}, opts);

    const vpc = new aws.ec2.Vpc(name, {
      cidrBlock: args.cidrBlock,
    });

    // Create subnets, security groups, etc.
    this.vpcId = vpc.id;
    this.subnetIds = subnets.map(s => s.id);
  }
}

// Higher-level component using other components
export class WebApplication extends ComponentResource {
  constructor(name: string, args: WebApplicationArgs, opts?: ComponentResourceOptions) {
    super("acme:patterns:WebApplication", name, {}, opts);

    // Use network component
    const network = new Network(`${name}-network`, {
      cidrBlock: "10.0.0.0/16",
    }, { parent: this });

    // Use database component
    const database = new Database(`${name}-db`, {
      instanceClass: "db.t3.micro",
      storage: 20,
      username: args.dbUsername,
      password: args.dbPassword,
      dbName: args.dbName,
    }, { parent: this });

    // Application infrastructure using the components
    const app = new aws.ecs.Service(`${name}-app`, {
      // Use network.vpcId and database.connectionString
      // ... application configuration
    }, { parent: this });
  }
}
```

Teams can use the high-level component without managing individual infrastructure pieces:

```typescript
const myApp = new WebApplication("my-web-app", {
  dbUsername: "admin",
  dbPassword: dbPassword,
  dbName: "myapp",
});
```

## Related patterns

- [IDP Pattern: Container-based apps, centrally managed container infra](/docs/idp/guides/best-practices/patterns/container-based-apps-centrally-managed-infra) - Example of component composition
- [IDP Pattern: Validating Component Inputs using Policy functions](/docs/idp/guides/best-practices/patterns/validating-component-inputs-using-policy-functions) - For validating composed components
- [IDP Pattern: Security Updates using Components](/docs/idp/guides/best-practices/patterns/security-updates-using-components) - For updating component hierarchies
