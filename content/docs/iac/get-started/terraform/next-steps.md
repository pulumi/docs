---
title_tag: Next Steps | Pulumi for Terraform Users
title: Next Steps
h1: "Next Steps"
meta_desc: Explore advanced Pulumi features and resources for Terraform users ready to deepen their integration or consider migration.
weight: 9
menu:
    iac:
        name: Next Steps
        parent: terraform-get-started
        weight: 9

aliases:
---

## Congratulations!

You've completed the Pulumi for Terraform Users guide and learned how to:

* Reference existing Terraform state files from Pulumi
* Use any Terraform provider in Pulumi programs
* Import and use Terraform modules directly
* Convert HCL code to Pulumi when beneficial
* Orchestrate both Terraform and Pulumi deployments together

## What's next?

Based on your journey through this guide, consider these next steps:

1. **Start small**: Begin with a simple coexistence pattern in your current environment
2. **Experiment**: Try different integration approaches to find what works for your team
3. **Build expertise**: Invest in learning both Terraform and Pulumi deeply
4. **Share knowledge**: Document your integration patterns for your team
5. **Consider migration**: When ready, plan a gradual migration to Pulumi for new projects

Our goal is to empower you to use the right tool for the job while maintaining a cohesive infrastructure management strategy.

## Advanced integration patterns

Beyond the examples shown, there are some more advanced integration patterns you can employ. These will be very dependent on your particular needs, so take these recommendations as a general guide to some strategies you can use to manage more complex environments.

### Multi-stack architectures

Organize complex infrastructure with multiple interconnected stacks:

```typescript
// Core infrastructure stack (could be Terraform)
export const vpc = new aws.ec2.Vpc("main", {
    cidrBlock: "10.0.0.0/16",
});

// Application stack (Pulumi)
const coreInfra = new pulumi.StackReference("core-infra");
const vpcId = coreInfra.getOutput("vpcId");

// Database stack (Terraform via state reference)
const dbState = new terraform.state.S3Reference("database", {
    bucket: "my-terraform-state",
    key: "database/terraform.tfstate",
});
```

### Complex state referencing

Handle complex state structures and transformations:

```typescript
// Reference multiple Terraform states
const networkState = new terraform.state.S3Reference("network", {
    bucket: "terraform-state",
    key: "network/terraform.tfstate",
});

const securityState = new terraform.state.S3Reference("security", {
    bucket: "terraform-state",
    key: "security/terraform.tfstate",
});

// Transform and combine outputs
const subnetIds = networkState.getOutput("private_subnet_ids");
const securityGroupIds = securityState.getOutput("security_group_ids");

// Create resources using combined state
const cluster = new aws.ecs.Cluster("app-cluster", {
    // Configure using multiple state outputs
    configuration: {
        executeCommandConfiguration: {
            kmsKeyId: securityState.getOutput("kms_key_id"),
            logging: "DEFAULT",
        },
    },
});
```

## Migration strategies

### Gradual migration approaches

When ready to migrate from Terraform to Pulumi:

1. **Import existing resources**: Use `pulumi import` to bring Terraform-managed resources under Pulumi management
2. **Parallel management**: Run both tools temporarily while migrating
3. **State migration**: Transfer state ownership gradually, resource-by-resource
4. **Validation**: Ensure identical infrastructure before switching

### Import existing resources

```bash
# Import existing Terraform resources into Pulumi
$ pulumi import aws:ec2/vpc:Vpc main-vpc vpc-12345
$ pulumi import aws:ec2/subnet:Subnet private-subnet-1 subnet-67890
$ pulumi import aws:ecs/cluster:Cluster app-cluster my-cluster
```

### State migration utilities

Create utilities to help with migration:

```typescript
// Migration helper utility
export class TerraformMigrationHelper {
    constructor(private terraformStateRef: terraform.state.S3Reference) {}

    // Import all resources of a given type
    async importResourceType(resourceType: string, pulumiType: string) {
        const resources = await this.terraformStateRef.getOutput("resources");
        const filtered = resources.filter(r => r.type === resourceType);

        for (const resource of filtered) {
            console.log(`Importing ${resourceType} ${resource.name}`);
            // Use Pulumi import API to import resources
        }
    }

    // Validate that imported resources match Terraform state
    async validateImports() {
        // Compare Terraform state with Pulumi state
        // Report any differences
    }
}
```

## Advanced Pulumi features

### Policies for policy enforcement

Implement infrastructure policies that work across both Terraform and Pulumi:

```typescript
// policies/index.ts
import * as aws from "@pulumi/aws";
import { PolicyPack, validateResourceOfType } from "@pulumi/policy";

new PolicyPack("terraform-integration-policies", {
    policies: [
        {
            name: "require-tags",
            description: "All resources must have required tags",
            enforcementLevel: "mandatory",
            validateResource: validateResourceOfType(aws.ec2.Instance, (instance, args, reportViolation) => {
                const requiredTags = ["Environment", "Owner", "Project"];
                const tags = instance.tags || {};

                for (const tag of requiredTags) {
                    if (!tags[tag]) {
                        reportViolation(`Missing required tag: ${tag}`);
                    }
                }
            }),
        },
        {
            name: "no-public-buckets",
            description: "S3 buckets cannot be publicly accessible",
            enforcementLevel: "mandatory",
            validateResource: validateResourceOfType(aws.s3.Bucket, (bucket, args, reportViolation) => {
                if (bucket.acl === "public-read" || bucket.acl === "public-read-write") {
                    reportViolation("S3 bucket cannot have public ACL");
                }
            }),
        },
    ],
});
```

### Automation API for programmatic control

Embed Pulumi in applications for dynamic infrastructure management:

```typescript
// automation-api-example.ts
import * as pulumi from "@pulumi/pulumi/automation";
import * as aws from "@pulumi/aws";

async function createEnvironmentStack(environmentName: string) {
    const stackName = `${environmentName}-app`;

    // Create or select stack
    const stack = await pulumi.LocalWorkspace.createOrSelectStack({
        stackName,
        projectName: "dynamic-environments",
        program: async () => {
            // Reference shared Terraform infrastructure
            const tfState = new pulumi.terraform.state.S3Reference("shared-infra", {
                bucket: "terraform-state",
                key: "shared/terraform.tfstate",
            });

            // Create environment-specific resources
            const app = new aws.ecs.Service(`${environmentName}-app`, {
                cluster: tfState.getOutput("cluster_name"),
                taskDefinition: tfState.getOutput("task_definition_arn"),
                desiredCount: environmentName === "production" ? 3 : 1,
            });

            return {
                appArn: app.arn,
                appName: app.name,
            };
        },
    });

    // Configure stack
    await stack.setConfig("aws:region", { value: "us-west-2" });

    // Deploy stack
    const upResult = await stack.up({ onOutput: console.log });

    return upResult.outputs;
}

// Usage
createEnvironmentStack("staging").then(outputs => {
    console.log("Staging environment created:", outputs);
});
```

### Component resources for reusability

Create reusable components that integrate with Terraform, behind the scenes, leaving the complexity of multi-tool management to your platform team, not your development teams:

```typescript
// components/WebApplication.ts
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as terraform from "@pulumi/terraform";

export interface WebApplicationArgs {
    terraformInfrastructure: terraform.state.S3Reference;
    containerImage: string;
    environment: string;
    desiredCount?: number;
}

export class WebApplication extends pulumi.ComponentResource {
    public readonly service: aws.ecs.Service;
    public readonly loadBalancer: aws.lb.LoadBalancer;
    public readonly url: pulumi.Output<string>;

    constructor(name: string, args: WebApplicationArgs, opts?: pulumi.ComponentResourceOptions) {
        super("custom:WebApplication", name, {}, opts);

        const defaultParent = { parent: this };

        // Get infrastructure from Terraform
        const clusterName = args.terraformInfrastructure.getOutput("cluster_name");
        const vpcId = args.terraformInfrastructure.getOutput("vpc_id");
        const subnetIds = args.terraformInfrastructure.getOutput("subnet_ids");

        // Create load balancer
        this.loadBalancer = new aws.lb.LoadBalancer(`${name}-alb`, {
            name: `${name}-alb`,
            loadBalancerType: "application",
            subnets: subnetIds,
            internal: false,
        }, defaultParent);

        // Create ECS service
        const taskDefinition = new aws.ecs.TaskDefinition(`${name}-task`, {
            family: name,
            networkMode: "awsvpc",
            requiresCompatibilities: ["FARGATE"],
            cpu: "256",
            memory: "512",
            containerDefinitions: pulumi.interpolate`[{
                "name": "${name}",
                "image": "${args.containerImage}",
                "portMappings": [{"containerPort": 80}],
                "environment": [{"name": "ENV", "value": "${args.environment}"}]
            }]`,
        }, defaultParent);

        this.service = new aws.ecs.Service(`${name}-service`, {
            cluster: clusterName,
            taskDefinition: taskDefinition.arn,
            desiredCount: args.desiredCount || 1,
            launchType: "FARGATE",
            networkConfiguration: {
                subnets: subnetIds,
                assignPublicIp: true,
            },
        }, defaultParent);

        this.url = pulumi.interpolate`http://${this.loadBalancer.dnsName}`;

        this.registerOutputs({
            service: this.service,
            loadBalancer: this.loadBalancer,
            url: this.url,
        });
    }
}

// Usage: developers create WebApplications in Pulumi, without knowing they depend on Terraform-managed resources
const app = new WebApplication("my-app", {
    terraformInfrastructure: infrastructureState,
    containerImage: "nginx:latest",
    environment: "production",
    desiredCount: 3,
});
```

## Learning resources

### Documentation and guides

* **[Pulumi Architecture & Concepts](/docs/intro/concepts/)**: Deep dive into Pulumi's architecture
* **[Adopting Pulumi](/docs/using-pulumi/adopting-pulumi/)**: Comprehensive migration strategies
* **[Pulumi vs Terraform](/docs/intro/vs/terraform/)**: Detailed comparison of features
* **[Automation API](/docs/using-pulumi/automation-api/)**: Programmatic infrastructure management
* **[Policy as Code](/docs/insights/policy/)**: Infrastructure governance and compliance

### Community resources

* **[Pulumi Community](https://pulumi.com/community/)**: Join the community slack and forum
* **[Examples Repository](https://github.com/pulumi/examples)**: Browse hundreds of real-world examples
* **[Pulumi Blog](https://pulumi.com/blog/)**: Latest updates and case studies
* **[Pulumi YouTube Channel](https://www.youtube.com/pulumitv)**: Video tutorials and demos

### Case studies and real-world implementations

* **[Snowflake's Multi-Cloud Strategy](https://www.pulumi.com/case-studies/snowflake/)**: How Snowflake uses Pulumi with existing tools
* **[Mercedes-Benz's Platform Engineering](https://www.pulumi.com/case-studies/mercedes-benz/)**: Large-scale infrastructure modernization
* **[Lemonade's Insurance Platform](https://www.pulumi.com/case-studies/lemonade/)**: Rapid development with Pulumi and Terraform

## Getting help and Contributing to Pulumi

Reach out to us via these support channels:

* **[Pulumi Community Slack](https://slack.pulumi.com/)**: Real-time community support
* **[GitHub Issues](https://github.com/pulumi/pulumi/issues)**: Bug reports and feature requests
* **[Pulumi Support](https://support.pulumi.com/)**: Professional support for Pulumi Cloud customers

### Open source contributions

We always welcome contributions, especially from our more advanced users who have practical experience building with both Terraform and Pulumi. Here are some ways you can contribute to the Pulumi ecosystem:

* **[Contribute to Pulumi](https://github.com/pulumi/pulumi/blob/master/CONTRIBUTING.md)**: Help improve Pulumi
* **[Building & Extending](/docs/iac/guides/building-extending/)**: Create new providers and components
* **[Examples and Templates](https://github.com/pulumi/examples/blob/master/CONTRIBUTING.md)**: Share your patterns

### Community engagement

* **[Pulumi Blog](https://www.pulumi.com/blog/)**: Write about your experience
* **[Community Events](https://www.pulumi.com/events/)**: Speak at meetups and conferences
* **[User Groups](https://www.pulumi.com/community/)**: Join or start a local user group

---

*Have questions or feedback about this guide? Join us in the [Pulumi Community Slack](https://slack.pulumi.com/) or [open an issue](https://github.com/pulumi/docs/issues) on GitHub.*
