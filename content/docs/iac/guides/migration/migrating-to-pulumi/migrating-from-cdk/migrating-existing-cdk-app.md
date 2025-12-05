---
title_tag: "Migrating existing AWS CDK applications to Pulumi"
meta_desc: Migrate your existing AWS CDK applications to Pulumi, including converting code and importing existing resources.
title: Migrating existing AWS CDK applications
h1: "Migrating existing AWS CDK applications to Pulumi"
meta_image: /images/docs/meta-images/docs-meta.png
aliases:
    - /docs/iac/guides/migration/migrating-to-pulumi/migrating-from-cdk/migrating-existing-cdk-app/
---

This guide walks through migrating an existing AWS CDK application to a Pulumi program that manages the same infrastructure.

## The golden path: incremental migration

The safest migration approach is **incremental**: migrate one logical group of resources at a time, verify each group before proceeding, and maintain the ability to roll back.

### Recommended workflow

Because CDK resources are grouped and deployed via CloudFormation stacks, you should migrate all resources in a stack together. Migrating only some resources in a CloudFormation stack is possible, but is more risky if you still expect to update some resources through CloudFormation since CloudFormation updates run on the entire stack.

Migrate one environment first. Import into dev, iterate until the preview is clean, then repeat for staging and prod. This reveals parameterization needs early and lets you refine your approach before touching production.

Verify at each step. After every import, run `pulumi preview` and confirm zero changes before proceeding. Any diff is a signal to stop and investigate. Never assume an import worked correctly.

Retire the old tool last. Only delete CloudFormation stacks after Pulumi successfully manages them with clean previews. Keeping the old state intact gives you a fallback if something goes wrong.

### Choose your convert/import approach

Pulumi offers multiple ways to convert and import resources.

#### Convert \+ Import

When migrating from CDK you can first convert the code to Pulumi using our `cdk2pulumi` converter tool. Converted code preserves structure better than import-generated code.

For CDK:

```shell
# 1. Install the cdk2pulumi tool
pulumi plugin install tool cdk2pulumi

# 2. Synthesize the CDK application and convert the stack
npx cdk synth
pulumi plugin run cdk2pulumi -- --assembly cdk.out --stacks MyStack-dev
```

The output of `cdk2pulumi` will be a couple of files:

- `Pulumi.yaml`: Pulumi yaml program containing the converted resources  
- `Pulumi.yaml.report.json`: A conversion report containing information on the resources converted

You can then convert this yaml program to your target language, for example:

```shell
# convert to typescript
pulumi convert --from yaml --generate-only --language typescript --out ./converted-project
```

### Testing converted code before importing

When using `cdk2pulumi` to migrate from CDK, you should test the generated code on a fresh stack before importing existing resources. Convert your source code, create a temporary test stack with `pulumi stack init test`, run `pulumi up` to deploy fresh infrastructure, verify everything works, then destroy the test stack with `pulumi destroy && pulumi stack rm test`. Now you can import your real resources with confidence.

This approach catches code errors, missing dependencies, and conversion issues before you touch production infrastructure. It’s particularly valuable when you’re converting complex modules or nested stacks, when the source code uses features that may not convert perfectly, or when you simply want to verify the code compiles and runs before importing.

Skip this step (or consider only running `pulumi preview`) when resources have globally unique names that would conflict with the test deployment, when creating duplicate infrastructure is costly or time-consuming, when you’re importing directly without conversion (so there’s no generated code to test), or when resources involve data that can’t be duplicated like databases or storage with existing data.

### Using the CDK importer tool (automated import files)

For larger stacks, manually building an `import.json` and chasing resource IDs can be tedious. The [Pulumi CDK importer tool](https://github.com/pulumi/pulumi-tool-cdk-importer) can generate a bulk import file for you by inspecting your Pulumi program and the underlying AWS resources.

> **Note**  
> The CDK importer tool is currently **experimental**. It may not support every CloudFormation/CDK pattern. Always review the generated import file and run `pulumi preview` until you see no unexpected changes before proceeding.

#### Install the importer tool

```shell
pulumi plugin install tool cdk-importer
```

#### When to use runtime vs program mode

The importer supports two main flows:

- **Runtime mode (`runtime`)**: Use this when you already have a Pulumi program that embeds your CDK app via [`pulumi-cdk`](https://github.com/pulumi/pulumi-cdk). Run from the directory containing your Pulumi program.
- **Program mode (`program import` / `program iterate`)**: Use this when you have a Pulumi program generated by `cdk2pulumi` (for example, in `./converted-project`) or a handwritten Pulumi program that represents your target state.

This guide focuses on **program mode**, since it aligns with the `cdk2pulumi` conversion flow.

#### Capturing an import file without touching your real stack

To generate an import file safely, you can use `program iterate`. This runs against a local backend and writes an enriched `import.json` without modifying your real Pulumi stack:

```shell
pulumi plugin run cdk-importer -- program iterate \
  --local \
  --stack MyStack-dev \
  --input ./converted-project \
  --out ./import.json
```

This mode is ideal when you want to inspect the generated import file and resolve IDs before you touch your real stack state. Because it uses a local backend, you can iterate multiple times without affecting production.

#### Applying the import file to your real stack

Once you are confident in the import file, you can switch to `program import` to apply it to your real stack:

```shell
pulumi plugin run cdk-importer -- program import \
  --stack MyStack-dev \
  --input ./converted-project \
  --file ./import.json
```

This runs your program against your real stack backend and uses the `import.json` file to import resources into Pulumi state. Always follow this with a `pulumi preview` and confirm there are no unexpected replacements or deletes before running `pulumi up`.

### Manual import

You can also import resources manually using the `pulumi import` CLI, either one resource at a time or from an `import.json` file. For help discovering the correct AWS IDs and understanding CloudFormation-specific edge cases, see [Finding AWS import IDs and special cases](/docs/iac/guides/migration/migrating-to-pulumi/aws-import-ids-and-special-cases/).

#### One-at-a-time vs bulk import

You can import resources individually or in bulk using an import file.

**One-at-a-time** works well when you’re learning the process:

```shell
pulumi import aws:s3/bucket:Bucket my-bucket my-bucket-name
```

With individual imports, you know exactly which resource caused a failure, debugging ID format issues is straightforward, and you have a clear recovery point if something goes wrong. This approach is best for your first migration or when working with unfamiliar resource types.

**Bulk import** is faster once you’re comfortable with the process:

```shell
pulumi import --file import.json
```

Where `import.json` contains:

```json
{
    "resources": [
        {
            "type": "aws:s3/bucket:Bucket",
            "name": "my-bucket",
            "id": "my-bucket-name"
        },
        {
            "type": "aws:s3/bucketPolicy:BucketPolicy",
            "name": "my-bucket-policy",
            "id": "my-bucket-name"
    }
]
}
```

Bulk import is faster for large migrations but makes failures harder to pinpoint and partial state harder to recover from. Use it when you’re confident in the ID formats and resource types.

When bulk importing, group resources by dependency layer: import VPCs before subnets, subnets before instances. If a bulk import fails partway through, check which resources made it into state with `pulumi stack export` and remove already-imported resources from your import file before retrying.

### What to avoid

Avoid big bang migrations. Converting everything at once leaves you with too many variables when something goes wrong. If an import fails or a preview shows unexpected diffs, you won’t know which of fifty resources caused the problem.

Never skip verification. Always run `pulumi preview` after every import and confirm zero changes. Never assume an import worked correctly just because the command succeeded.

Don’t delete source state early. Keep your CloudFormation stacks intact until Pulumi fully owns the resources with clean previews. This gives you a fallback.

Don’t refactor while migrating. Get the migration working first, then optimize. Trying to improve code structure, switch providers, or clean up resources during the initial import creates compound problems. Decouple these concerns: first make it work, then make it better.

Don’t quit early. Iterate until your preview is completely clean with no diffs, no updates, and no replacements. “Close enough” isn’t good enough when the goal is zero disruption.

## Planning your target structure

Before importing resources, design how your Pulumi project should be organized. The migration tools can import resources and generate code, but they don’t organize code for long-term maintainability.

### Consolidate multiple CDK Stacks

CDK applications typically organize resources into multiple Stacks per environment. This is done for a variety of reasons:

- **Reduce blast radius**: CFN has things like automatic rollback and stack level deletion protection. This leads to developers splitting resources into separate stacks. For example, they might put their stateful resources (e.g. RDS Database) in one stack with deletion protection turned on and then their application resources (e.g. ECS Services) in a separate stack. This allows them to more frequently deploy their ECS services without also updating the RDS database in the same operation.  
- **Resource Limits**: Historically CFN has had limits on the number of resources in a Stack, causing developers to have to split resources between stacks.  
- **Region boundary**: A Stack can only deploy resources in a single region. If your application deploys across multiple regions, you have to split between multiple stacks.

By contrast, Pulumi stacks:

- Can contain unlimited resources  
- Deletion protection can be configured on a per resource basis  
- Can deploy to multiple AWS accounts and regions

This means that when migrating a CDK application with multiple stacks, they can be combined into a single Pulumi Stack. A Pulumi Stack is more analogous to CDK [Stages](https://docs.aws.amazon.com/cdk/v2/guide/stages.html) where all resources that are deployed together to a single environment (i.e. dev, test, prod, etc) are grouped together.

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

### Handling CDK stages

An AWS CDK stage represents a group of one or more AWS CDK stacks that are configured to deploy together to a particular environment. For example, taking the example from above where we deploy a `StatefulStack` and an `AppStack`, we would use stages to deploy these to different environments.

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

The AWS CDK stages can be converted to [Pulumi stacks](/docs/iac/concepts/stacks/). Similar to CDK stages, Pulumi stacks can be used to deploy groups of resources to different environments.

In AWS CDK applications differences in configuration between environments are typically configured through input parameters on the stage. In the above example, the `DatabaseCluster` uses a different `InstanceType` between the `dev` and `prod` environments. When we convert this application to Pulumi, we will move this configuration from the stage input properties to [stack configuration](/docs/iac/concepts/config/).

When we convert the AWS CDK application we will:

- Combining the stacks like we did in the [Consolidate multiple CDK stacks](#consolidate-multiple-cdk-stacks) example  
- Read the instance type from the [Pulumi configuration](/docs/iac/concepts/config/).

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

### Code organization

Converters typically output a single file. For maintainability, split resources into logical groups:

```shell
my-infrastructure/
├── index.ts           # Main entry point, exports
├── network.ts         # VPC, subnets, security groups
├── database.ts        # RDS, ElastiCache
├── compute.ts         # ECS, Lambda, EC2
└── dns.ts             # Route53, certificates
```

**Preserve structure from your source (Optional)**: If your original CDK constructs had a logical organization, you can optionally preserve it in Pulumi. This migration can also be taken as an opportunity to optimize this structure. Map CDK constructs to [Pulumi components](/docs/iac/concepts/resources/components/)—these are reusable abstractions that encapsulate related resources and can be shared across projects.

Because Pulumi uses general-purpose languages like CDK, you can still use functions and classes for abstraction. Loops and conditionals work naturally. Components encapsulate patterns your team uses repeatedly and can be shared across projects, just like CDK constructs.

You can do this refactoring after migration. The first priority is getting resources imported cleanly—start with the generated code, then progressively improve the structure without changing the underlying infrastructure.

#### Converting CDK constructs

Constructs are the basic building blocks of CDK. A construct is a component within the application that represents one or more AWS CFN resources and their configuration.

**Construct levels**

- Level 1 (L1): Also known as CFN resources, they are the lowest-level construct and offer no abstraction. Each L1 construct maps directly to a single CFN resource.  
- Level 2 (L2): Are the most widely used type. L2 constructs map directly to a single AWS CFN resource, but they provide a higher level abstraction than L1. They provide a higher level intent-based API that builds in sensible default property configurations, best practices, and generates a lot of boilerplate code and glue logic.  
- Level 3 (L3): Also known as "patterns", they are the highest level of abstraction. L3 constructs are used to create entire AWS architectures for particular use cases. The `ecs-patterns` library includes examples such as `ApplicationLoadBalancedFargateService` that creates a complete load balanced ECS service.

When converting constructs, focus on preserving behavior rather than the exact class structure. For L1 and L2 constructs that map closely to individual resources, you can often translate them directly to Pulumi resources or small components. For L3 constructs that represent entire patterns, consider modeling them as Pulumi components that encapsulate the same inputs and outputs.

#### Mapping constructs to components

In many CDK applications, constructs are nested several layers deep. When moving to Pulumi, you have flexibility in how much of that nesting you preserve.

You can flatten overly deep hierarchies where intermediate constructs only exist to wire values between children. Focus on the constructs that represent meaningful boundaries (for example, "network", "database", "application service") and model those as Pulumi components.

For example, if you have a construct hierarchy like:

```
- MyApp
  - MyNetworking
    - MyVpc
      - MySubnets
        - MyNatGateways
```

You might collapse this into a single `Network` component in Pulumi:

```
- MyApp
  - Network
```

Or if your CDK application already has a well-factored `MyVpc` construct that is reused in multiple places, you might keep that as a separate Pulumi component. The goal is to arrive at a component hierarchy that matches how your team thinks about the system, not necessarily the exact original shape of the CDK construct tree.

### Importing into components

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
