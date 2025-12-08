---
title_tag: "Migrating existing AWS CDK applications to Pulumi"
meta_desc: Migrate your existing AWS CDK applications to Pulumi, including converting code and importing existing resources.
title: Migrating existing AWS CDK applications
h1: "Migrating existing AWS CDK applications to Pulumi"
meta_image: /images/docs/meta-images/docs-meta.png
aliases:
    - /docs/iac/guides/migration/migrating-to-pulumi/migrating-from-cdk/migrating-existing-cdk-app/
menu:
    iac:
      name: Migrating existing CDK
      parent: iac-guides-migration-from-cdk
      weight: 1
---

This guide walks through migrating an existing AWS CDK application to a Pulumi program that manages the same infrastructure.

#### Planning your Migration

Before running any tools, it is important to plan your migration strategy. Migrating involves two distinct parts: converting your **Code** (logic) and migrating your **State** (live resources).

### Strategy: Convert vs. Rewrite

How much of your existing code structure do you want to keep?

* **Convert (Lift and Shift)**: Translate your CDK resources 1:1 into Pulumi code, optionally using an automated conversion tool like `cdk2pulumi`. This is the fastest way to get a working program but results in low-level code without the high-level abstractions you might expect (making it a good candidate for refactoring).
* **Hybrid / Refactor (Recommended)**: Generate a working baseline (manually or via `cdk2pulumi`), then refactor the code into idiomatic Pulumi [Components](/docs/iac/concepts/resources/components/) before or after importing state. This balances speed with long-term maintainability.
* **Rewrite**: Manually write your Pulumi program from scratch. This is best if your CDK app has significant technical debt or if you want to fundamentally re-architect your infrastructure.

### Strategy: Import vs. Rehydrate

How do you want to handle your live resources?

* **Import**: Bring your existing AWS resources under Pulumi management without downtime. This is essential for stateful resources like Databases, periodic/retained S3 buckets, and VPCs.
* **Rehydrate (Blue/Green)**: Deploy a fresh copy of your infrastructure alongside the old one, switch traffic over, and delete the old stack. This is ideal for stateless applications or when you want to verify the new system with zero risk to the old one.

### Best Practices

Regardless of your strategy, follow these core principles:

1. **Migrate stacks as units**: CDK resources deploy via CloudFormation stacks. Migrate all resources in a stack together; partial stack moves stay risky if you still run CloudFormation updates because they operate on the whole stack.
1. **Move environment by environment**: Import into dev first, iterate until the preview is clean, then repeat for staging and prod. This surfaces parameterization gaps before you touch production.
1. **Verify after every import**: Run `pulumi preview` after each import and confirm zero changes before continuing. Any unexpected diff is a stop signal.
1. **Retire CloudFormation last**: Only delete CloudFormation stacks after Pulumi manages them with clean previews. Keeping the old state intact gives you a rollback path.

### Target Structure

The migration tools can import resources and generate code, but they don’t organize code for long-term maintainability. You should decide on your target structure early.

#### Consolidate multiple CDK Stacks

CDK applications typically organize resources into multiple Stacks per environment to manage blast radius and resource limits. Pulumi Stacks are more powerful and scalable, often allowing you to consolidate multiple CDK stacks into a single Pulumi Stack.

For example, a `StatefulStack` (RDS) and `AppStack` (Lambda) in CDK can be combined into one Pulumi Stack with `protect: true` enabled on the critical resources. This simplifies dependency management and deployment.

Consider a common scenario of creating your stateful resources (e.g. an RDS database) in one stack and your non-stateful resources (e.g. a Lambda Function) in a separate Stack.

```ts
import * as cdk from 'aws-cdk-lib/core';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as rds from 'aws-cdk-lib/aws-rds';

class StatefulStack extends cdk.Stack {
  public readonly cluster: rds.IDatabaseCluster;
  constructor(scope: Construct, id: string) {
    super(scope, id, {
      terminationProtection: true,
    });

    this.cluster = new rds.DatabaseCluster(this, 'cluster', { ... });
  }
}

interface AppStackProps extends cdk.StackProps {
    cluster: rds.IDatabaseCluster
}

class AppStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props: AppStackProps) {
    super(scope, id, props);

    new AppConstruct(this, 'app-construct', {
        cluster: props.cluster,
    })

  }
}

const app = new cdk.App();
const stateful = new StatefulStack(app, 'stateful-stack');
new AppStack(app, 'app-stack', {
    cluster: stateful.cluster,
});
```

When this is converted to a Pulumi program you would have a single Pulumi stack that defines both the RDS database and the Lambda Function. You would then set `protect: true` on the Pulumi RDS Database.

#### Handling CDK stages

AWS CDK Stages represent a group of stacks deployed to an environment (dev, prod). These directly map to [Pulumi Stacks](/docs/iac/concepts/stacks/). Similar to CDK stages, Pulumi stacks can be used to deploy groups of resources to different environments.

In AWS CDK applications differences in configuration between environments are typically configured through input parameters on the stage. In the example below, the `DatabaseCluster` uses a different `InstanceType` between the `dev` and `prod` environments. When we convert this application to Pulumi, we will move this configuration from the stage input properties to [stack configuration](/docs/iac/concepts/config/).

```ts
import * as cdk from 'aws-cdk-lib/core';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as rds from 'aws-cdk-lib/aws-rds';

interface StatefulStackProps extends cdk.StackProps {
  instanceType: ec2.InstanceType;
}

class StatefulStack extends cdk.Stack {
  public readonly cluster: rds.IDatabaseCluster;
  constructor(scope: Construct, id: string, props: StatefulStackProps) {
    super(scope, id, {
      ...props,
      terminationProtection: true,
    });

    this.cluster = new rds.DatabaseCluster(this, 'cluster', {
      writer: rds.ClusterInstance.provisioned('writer', {
        instanceType: props.instanceType,
      }),
      ...
    });
  }
}

interface AppStackProps extends cdk.StackProps {
    cluster: rds.IDatabaseCluster
}

class AppStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props: AppStackProps) {
    super(scope, id, props);

    new AppConstruct(this, 'app-construct', {
        cluster: props.cluster,
    })
  }
}

interface MyStageProps extends cdk.StageProps {
  instanceType: ec2.InstanceType;
}

class MyStage extends cdk.Stage {
  constructor(scope: Construct, id: string, props: MyStageProps) {
    super(scope, id, props);
      const stateful = new StatefulStack(app, 'stateful-stack', {
        instanceType: props.instanceType,
      });
      new AppStack(app, 'app-stack', {
          cluster: stateful.cluster,
      });
  }
}

const app = new cdk.App();
new MyStage(app, 'dev', {
  instanceType: ec2.InstanceType.of(ec2.InstanceClass.R6G, ec2.InstanceSize.MEDIUM),
});

new MyStage(app, 'prod', {
  instanceType: ec2.InstanceType.of(ec2.InstanceClass.R6G, ec2.InstanceSize.XLARGE),
});
```

When we convert the AWS CDK application we will:

* Combining the stacks like we did in the [Consolidate multiple CDK stacks](#consolidate-multiple-cdk-stacks) example
* Read the instance type from the [Pulumi configuration](/docs/iac/concepts/config/).

```ts
import * as pulumi from '@pulumi/pulumi';

const config = new pulumi.Config();
const instanceType = config.require('instanceType');

new ccapi.rds.DbInstance('instance', {
  ..., // trimmed for simplicity
  dbInstanceClass: instanceType,
}, { protect: true });
```

```shell
pulumi stack select dev
pulumi config set instanceType db.r6g.medium
```

#### Code organization

Converters typically output a single file. For maintainability, plan to split your resources into logical groups:

```shell
my-infrastructure/
├── index.ts           # Main entry point, exports
├── network.ts         # VPC, subnets, security groups
├── database.ts        # RDS, ElastiCache
├── compute.ts         # ECS, Lambda, EC2
└── dns.ts             # Route53, certificates
```

**Preserve structure from your source (Optional)**: If your original CDK constructs had a logical organization, you can optionally preserve it in Pulumi. This migration can also be taken as an opportunity to optimize this structure. Map CDK constructs to [Pulumi components](/docs/iac/concepts/resources/components/)—these are reusable abstractions that encapsulate related resources and can be shared across projects.

#### Converting CDK constructs

Constructs are the basic building blocks of CDK. A construct is a component within the application that represents one or more AWS CFN resources and their configuration.

**Construct levels**

* Level 1 (L1): Also known as CFN resources, they are the lowest-level construct and offer no abstraction. Each L1 construct maps directly to a single CFN resource.
* Level 2 (L2): Are the most widely used type. L2 constructs map directly to a single AWS CFN resource, but they provide a higher level abstraction than L1. They provide a higher level intent-based API that builds in sensible default property configurations, best practices, and generates a lot of boilerplate code and glue logic.
* Level 3 (L3): Also known as "patterns", they are the highest level of abstraction. L3 constructs are used to create entire AWS architectures for particular use cases. The `ecs-patterns` library includes examples such as `ApplicationLoadBalancedFargateService` that creates a complete load balanced ECS service.

When converting constructs, focus on preserving behavior rather than the exact class structure. For L1 and L2 constructs that map closely to individual resources, you can often translate them directly to Pulumi resources or small components. For L3 constructs that represent entire patterns, consider modeling them as Pulumi components that encapsulate the same inputs and outputs.

#### Mapping constructs to components

In many CDK applications, constructs are nested several layers deep. When moving to Pulumi, you have flexibility in how much of that nesting you preserve.

You can flatten overly deep hierarchies where intermediate constructs only exist to wire values between children. Focus on the constructs that represent meaningful boundaries (for example, "network", "database", "application service") and model those as Pulumi components.

For example, if you have a construct hierarchy like:

```text
- MyApp
  - MyNetworking
    - MyVpc
      - MySubnets
        - MyNatGateways
```

You might collapse this into a single `Network` component in Pulumi:

```text
- MyApp
  - Network
```

Or if your CDK application already has a well-factored `MyVpc` construct that is reused in multiple places, you might keep that as a separate Pulumi component. The goal is to arrive at a component hierarchy that matches how your team thinks about the system, not necessarily the exact original shape of the CDK construct tree.

#### Importing into components

After converting the code, if you choose to organize into Pulumi components you have two options:

**Option 1: Import first, then refactor into components**

This is the simpler approach. Import resources flat, then reorganize. After importing resources using the approaches above, create a component class and move resources inside it. Add aliases to indicate the resources used to be at the root level:

```ts

class MyVpc extends pulumi.ComponentResource {
    public vpc: aws.ec2.Vpc;

    constructor(name: string, opts?: pulumi.ComponentResourceOptions) {
        super("myinfra:network:MyVpc", name, {}, opts);

        // Resource was imported at root, now under this component
        this.vpc = new aws.ec2.Vpc(`${name}-vpc`, {
            cidrBlock: "10.0.0.0/16",
        }, {
            parent: this,
            aliases: [{ parent: pulumi.rootStackResource }],
        });

        this.registerOutputs();
    }
}
```

**Option 2: Import directly into component hierarchy**

If you write your component code first, you can import directly into the hierarchy using an import file with parent references:

```json
{
    "nameTable": {
        "network": "urn:pulumi:prod::myproject::myinfra:network:MyVpc::network"
    },
    "resources": [
        {
            "type": "aws:ec2/vpc:Vpc",
            "name": "network-vpc",
            "id": "vpc-0abc123",
            "parent": "network"
        }
    ]
}
```

## Execution Strategies

Once you have a plan, choose the execution path that fits your goals:

* [Approach A: The Automated Path (Recommended)](#approach-a-the-automated-path-recommended)
* [Approach B: Manual Migration](#approach-b-manual-migration)

### Approach A: The Automated Path (Recommended)

This path uses `cdk2pulumi` to convert your code and the `cdk-importer` tool to automatically generate the import mapping. This is the fastest way to migrate standard stacks.

**The Workflow:**

1. **Convert Code**: Generate a baseline Pulumi program.
1. **Verify Code**: Test the code on a fresh ephemeral stack.
1. **Generate Import**: Create an automated `import.json` mapping your new code to your existing AWS resources.
1. **Perform Import**: Bring the resources into Pulumi state.
1. **Refactor**: Clean up the code structure (optional but recommended).

#### 1. Convert Code

Use `cdk2pulumi` to convert your CDK code to Pulumi.

```shell
# Install the tool
pulumi plugin install tool cdk2pulumi

# Synthesize and convert
npx cdk synth
pulumi plugin run cdk2pulumi -- --assembly cdk.out --stacks MyStack-dev
```

This generates a `Pulumi.yaml` which you can then convert to your language of choice (e.g., TypeScript, Python, Go):

```shell
pulumi convert --from yaml --generate-only --language typescript --out ./converted-project
```

#### 2. Test converted code

Before importing, verify the generated code works by deploying it to a temporary stack (e.g., `dev-test`).

```shell
cd converted-project
pulumi stack init dev-test
pulumi up
# Verify, then destroy
pulumi destroy
pulumi stack rm dev-test
```

This ensures your code produces valid infrastructure before you try to map it to production resources.

#### 3. Generate Import File

Use the [Pulumi CDK importer tool](https://github.com/pulumi/pulumi-tool-cdk-importer) in `program iterate` mode. This inspects your converted program and your logical AWS resources to generate an `import.json` file **without modifying state**.

```shell
pulumi plugin install tool cdk-importer

pulumi plugin run cdk-importer -- program iterate \
  --local \
  --stack MyStack-dev \
  --input ./converted-project \
  --out ./import.json
```

#### 4. Import Resources

Once you are happy with `program iterate`, use `program import` to import the program into your stack state.

```shell
pulumi plugin run cdk-importer -- program import \
  --stack MyStack-dev \
  --input ./converted-project \
  --file ./import.json
```

Always run `pulumi preview` immediately after import to ensure there are no pending changes.

#### 5. Refactor

Now that your resources are imported and your state matches your code, you can safely refactor. You can move resources into ComponentResources, rename logical IDs, or split files. Refer to [Target Structure](#target-structure) for guidance on organizing your new Pulumi program.

* If you change a resource's name or parent component in your code, Pulumi will see it as a "Create new / Delete old" operation.
* To prevent this, use [aliases](/docs/iac/concepts/options/aliases/) to tell Pulumi "this new resource is actually that old resource".

### Approach B: Manual Migration

Use this approach if the automated tools fail for your specific pattern, or if you are rewriting your application from scratch.

1. **Write Code**: Manually write the Pulumi code to match your existing infrastructure.
1. **Import One-by-One**: Use the CLI to bring resources into state.

```shell
pulumi import aws:s3/bucket:Bucket my-bucket my-bucket-name
```

1. **Import in Bulk**: Create a manual `import.json` file.

```shell
pulumi import --file import.json
```

See [Finding AWS import IDs](/docs/iac/guides/migration/aws-import-ids/) for help identifying resource IDs.

### What to avoid

Avoid big bang migrations. Converting everything at once leaves you with too many variables when something goes wrong. If an import fails or a preview shows unexpected diffs, you won’t know which of fifty resources caused the problem.

Never skip verification. Always run `pulumi preview` after every import and confirm zero changes. Never assume an import worked correctly just because the command succeeded.

Don’t delete source state early. Keep your CloudFormation stacks intact until Pulumi fully owns the resources with clean previews. This gives you a fallback.

Don’t refactor while migrating. Get the migration working first, then optimize. Trying to improve code structure, switch providers, or clean up resources during the initial import creates compound problems. Decouple these concerns: first make it work, then make it better.

Don’t quit early. Iterate until your preview is completely clean with no diffs, no updates, and no replacements. “Close enough” isn’t good enough when the goal is zero disruption.

## The Golden Path: Recommended Workflow

In summary, the most reliable way to migrate is:

1. **Plan**: Decide on your target structure and strategy.
1. **Convert**: Use `cdk2pulumi` to get a working baseline of code.
1. **Verify Code**: Deploy to a disposable test stack to prove compilation and logic.
1. **Import**: Use `cdk-importer` to bring production state into Pulumi.
1. **Refactor**: Clean up the code into components and proper modules, using aliases to migrate state.
1. **Retire CloudFormation**: Only delete the old CFN stacks after Pulumi shows a clean preview and you have successfully deployed an update.
