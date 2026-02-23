---
title: "IDP Pattern: Security Updates using Components"
linktitle: "Security Updates using Components"
menu:
  idp:
    parent: idp-patterns
    weight: 100
aliases:
  - /docs/idp/best-practices/patterns/security-updates-using-components/
meta_desc: Implement security updates and patches through centralized component management
h1: "IDP Pattern: Security Updates using Components"
description: <p>Implement security updates and patches through centralized component management.</p>
---

## Description

This pattern involves centralizing security configurations and updates within Pulumi components, allowing platform teams to push security patches and updates across all applications by updating component versions. Teams consume components from a centralized registry and receive security updates automatically.

## When to use this pattern

- **Security compliance**: When you need to ensure consistent security configurations across all infrastructure
- **Centralized updates**: When you want to push security patches to all applications simultaneously
- **Audit requirements**: When you need to track and verify security configurations
- **Large organizations**: When managing security across many teams and applications

## When NOT to use this pattern

- **Unique security needs**: When applications have legitimate custom security requirements
- **Rapid iteration**: When security update processes would slow down development
- **Small teams**: When centralized management overhead exceeds benefits

## How to use this pattern

Components encapsulate security best practices and can be updated centrally, with applications consuming specific component versions that can be updated for security patches.

### Example

Platform team creates security-focused components:

```typescript
// components/secure-database.ts v1.2.3
export class SecureDatabase extends ComponentResource {
  constructor(name: string, args: SecureDatabaseArgs, opts?: ComponentResourceOptions) {
    super("acme:security:SecureDatabase", name, {}, opts);

    // Security configurations managed centrally
    const subnetGroup = new aws.rds.SubnetGroup(`${name}-subnet-group`, {
      subnetIds: args.privateSubnetIds, // Force private subnets
    }, { parent: this });

    const db = new aws.rds.Instance(name, {
      instanceClass: args.instanceClass,
      allocatedStorage: args.storage,

      // Security defaults managed by platform team
      storageEncrypted: true,
      kmsKeyId: args.kmsKeyId,
      dbSubnetGroupName: subnetGroup.name,
      vpcSecurityGroupIds: [this.createSecurityGroup(args.vpcId)],

      // Updated security settings (v1.2.3)
      enabledCloudwatchLogsExports: ["postgresql", "upgrade"],
      monitoringInterval: 60,
      performanceInsightsEnabled: true,

      // Force SSL connections
      parameterGroupName: this.createParameterGroup(),

      // Automated backups with encryption
      backupRetentionPeriod: args.backupRetentionDays,
      backupWindow: "03:00-04:00",
      maintenanceWindow: "sun:04:00-sun:05:00",

      tags: {
        SecurityCompliant: "true",
        ComponentVersion: "1.2.3",
        LastSecurityUpdate: "2024-01-15",
      },
    }, { parent: this });
  }

  private createSecurityGroup(vpcId: string): aws.ec2.SecurityGroup {
    return new aws.ec2.SecurityGroup("db-sg", {
      vpcId: vpcId,
      ingress: [{
        fromPort: 5432,
        toPort: 5432,
        protocol: "tcp",
        cidrBlocks: ["10.0.0.0/8"], // Only internal traffic
      }],
      // No egress rules - deny all outbound
    }, { parent: this });
  }

  private createParameterGroup(): aws.rds.ParameterGroup {
    return new aws.rds.ParameterGroup("secure-pg", {
      family: "postgres14",
      parameters: [
        { name: "ssl", value: "on" },
        { name: "log_statement", value: "all" },
        { name: "log_min_duration_statement", value: "1000" },
      ],
    }, { parent: this });
  }
}
```

Platform team creates policy to enforce current component versions:

```typescript
// policies/component-version-policy.ts
import { PolicyPack, validateResourceOfType } from "@pulumi/policy";
import { aws } from "@pulumi/aws";

const MINIMUM_COMPONENT_VERSIONS = {
  "SecureDatabase": "1.2.0",
  "SecureNetwork": "2.1.0",
  "SecureStorage": "1.5.0",
};

function isVersionOutdated(currentVersion: string, minimumVersion: string): boolean {
  const current = currentVersion.split('.').map(n => parseInt(n));
  const minimum = minimumVersion.split('.').map(n => parseInt(n));

  for (let i = 0; i < Math.max(current.length, minimum.length); i++) {
    const currentPart = current[i] || 0;
    const minimumPart = minimum[i] || 0;

    if (currentPart < minimumPart) return true;
    if (currentPart > minimumPart) return false;
  }
  return false;
}

new PolicyPack("component-version-enforcement", {
  policies: [{
    name: "enforce-minimum-component-versions",
    description: "Ensure all components are using minimum required versions for security",
    enforcementLevel: "mandatory",
    validateResource: validateResourceOfType(aws.rds.Instance, (instance, args, reportViolation) => {
      const componentVersion = instance.tags?.ComponentVersion;
      const componentName = instance.tags?.ComponentName;

      if (componentName && componentVersion) {
        const minimumVersion = MINIMUM_COMPONENT_VERSIONS[componentName];
        if (minimumVersion && isVersionOutdated(componentVersion, minimumVersion)) {
          reportViolation(
            `Component ${componentName} version ${componentVersion} is outdated. ` +
            `Minimum required version is ${minimumVersion} for security compliance.`
          );
        }
      } else if (instance.tags?.SecurityCompliant === "true") {
        reportViolation(
          "Security-compliant resources must include ComponentVersion and ComponentName tags"
        );
      }
    }),
  }],
});
```

Applications consume the secure component:

```typescript
// package.json
{
  "dependencies": {
    "@acme/security-components": "^1.2.3"
  }
}

// Application usage
import { SecureDatabase } from "@acme/security-components";

const database = new SecureDatabase("app-db", {
  instanceClass: "db.t3.small",
  storage: 100,
  kmsKeyId: kmsKey.arn,
  vpcId: vpc.id,
  privateSubnetIds: privateSubnets,
  backupRetentionDays: 7,
});
```

Platform team pushes security updates:

```bash
# Platform team updates component with security patch
npm version patch  # v1.2.4
npm publish

# Update minimum version requirements
# Update MINIMUM_COMPONENT_VERSIONS in policy

# Applications receive security updates
npm update @acme/security-components
pulumi up  # Deploys with new security configurations
```

The policy ensures that outdated component versions cannot be deployed, forcing teams to update to versions with the latest security patches.

## Related patterns

- [IDP Pattern: Components using other Components](/docs/idp/guides/best-practices/patterns/components-using-other-components) - For building secure component hierarchies
- [IDP Pattern: Policies as tests](/docs/idp/guides/best-practices/patterns/policies-as-tests) - For enforcing security policies
- [IDP Pattern: Validating Component Inputs using Policy functions](/docs/idp/guides/best-practices/patterns/validating-component-inputs-using-policy-functions) - For validating security configurations
