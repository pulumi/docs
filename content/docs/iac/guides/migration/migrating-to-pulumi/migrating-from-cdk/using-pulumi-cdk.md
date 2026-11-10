---
title_tag: "Using Pulumi with AWS CDK"
meta_desc: Use the Pulumi CDK adapter to run your existing AWS CDK applications with Pulumi.
title: Using Pulumi with AWS CDK
h1: "Using Pulumi with AWS CDK"
aliases:
    - /docs/iac/guides/migration/migrating-to-pulumi/migrating-from-cdk/using-pulumi-cdk/
menu:
    iac:
      name: Using Pulumi with AWS CDK
      parent: iac-guides-migration-from-cdk
      weight: 2
---

This guide covers two ways to use Pulumi alongside AWS CDK:

* [Reference outputs from existing AWS CDK stacks](#referencing-stack-outputs) in a Pulumi program, so CDK and Pulumi run side by side and CDK keeps managing its own stacks.
* [Convert your AWS CDK application](#converting-cdk-applications) to run your existing AWS CDK constructs with Pulumi as the underlying engine, through the Pulumi CDK adapter.

If you instead want to migrate to a pure Pulumi program and import existing CDK-managed resources, see [Migrating existing AWS CDK applications to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/migrating-from-cdk/migrating-existing-cdk-app/).

## Referencing stack outputs

You can reference existing AWS CDK stacks from your Pulumi program, no matter how those stacks were created. This lets you read properties of that CloudFormation stack for use within your Pulumi program, including output values computed from resources provisioned by that stack.

For instance, suppose your infrastructure team has provisioned your network infrastructure using CDK and you need to use the Subnet ID to provision something new from your Pulumi program. One approach is to hardcode that ID, but this is brittle: if the ID ever changes, you'd need to manually update the hardcoded value.

Instead, you can look up that stack by name and use one of its output values. The following example reads an AWS CDK stack named `my-network-stack` and then uses the exported `SubnetId` value to provision a brand new EC2 instance that runs in that subnet:

```typescript
import * as aws from "@pulumi/aws";

const network = aws.cloudformation.getStackOutput({
    name: "my-network-stack",
});

const subnetId = network.outputs["SubnetId"];

const web = new aws.ec2.Instance("web", {
    ami: "ami-0adc0e3ef2558cb1f", // us-west-2 AMI
    instanceType: "t3.micro",
    subnetId: subnetId,
});
```

Run `pulumi up`, and the Pulumi runtime queries the CDK stack and retrieves its output values. In this case, the CDK stack is treated entirely as read-only, and Pulumi never attempts to modify it or any resources managed by it.

> Although this example hard-codes the AWS CDK stack name &mdash; `"my-network-stack"` &mdash; it's common to dynamically compute a name using unique per-stack information, like the stack name, AWS region, or other configuration variables.

## Converting CDK applications

If you want to migrate from AWS CDK to Pulumi, and [referencing stack outputs](#referencing-stack-outputs) to run the two side by side isn't enough, you can convert your AWS CDK application to a Pulumi CDK application using the [Pulumi CDK Adapter](https://github.com/pulumi/pulumi-cdk).

The following steps convert this CDK application to use Pulumi CDK:

```typescript
import * as cdk from 'aws-cdk-lib/core';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';

class TestStack extends cdk.Stack {
  constructor(scope: Construct, id: string) {
    super(scope, id);

    new s3.Bucket(this, 'Bucket');

  }
}

const app = new cdk.App();
new TestStack(app, 'import-test');
```

### Create a Pulumi project

The Pulumi CLI deploys from a Pulumi project, so create a Pulumi TypeScript project and stack, then configure the AWS region for both the AWS and AWS Cloud Control providers:

```console
$ pulumi new aws-typescript
$ pulumi config set aws-native:region us-east-2
$ pulumi config set aws:region us-east-2
```

### Install Pulumi dependencies

The Pulumi CDK Adapter requires the installation of the following npm packages:

* [@pulumi/aws](https://www.npmjs.com/package/@pulumi/aws)
* [@pulumi/aws-native](https://www.npmjs.com/package/@pulumi/aws-native)
* [@pulumi/docker-build](https://www.npmjs.com/package/@pulumi/docker-build)
* [@pulumi/pulumi](https://www.npmjs.com/package/@pulumi/pulumi)
* [@pulumi/cdk](https://www.npmjs.com/package/@pulumi/cdk)

Your CDK code also needs `aws-cdk-lib`, so install it in the new project along with the adapter's packages:

```console
npm install @pulumi/aws @pulumi/aws-native @pulumi/cdk @pulumi/docker-build @pulumi/pulumi aws-cdk-lib
```

### Convert the CDK stack and app

Move your CDK code into the project's `index.ts` file, then replace the CDK `Stack` and `App` classes with Pulumi CDK `Stack` and `App` classes.

```typescript
import * as pulumicdk from '@pulumi/cdk';
import * as s3 from 'aws-cdk-lib/aws-s3';

class TestStack extends pulumicdk.Stack {
  constructor(scope: pulumicdk.App, id: string) {
    super(scope, id);

    new s3.Bucket(this, 'Bucket');

  }
}

const app = new pulumicdk.App('app', (scope: pulumicdk.App) => {
    new TestStack(scope, 'import-test');
});
```

### Deploy the Pulumi stack

Now that you have converted your AWS CDK application to a Pulumi CDK application, use the Pulumi CLI to deploy it to the stack you created:

```console
$ pulumi up
```

## Converting multi-stack CDK applications

If your CDK application contains multiple CDK stacks, they usually fall into one of two scenarios:

1. You have multiple CDK stacks that all deploy to the same environment (AWS account/region).
1. You have multiple CDK stacks that deploy to multiple environments.

### Converting same-environment stacks

If all your CDK stacks deploy to the same environment, you can combine them into a single Pulumi CDK stack.
Pulumi CDK stacks do not have the same resource limits that CloudFormation stacks have.
You can also control termination protection at the resource level in Pulumi instead of at the CloudFormation stack level in CDK.

Consider a common scenario of creating your stateful resources (for example, an RDS database) in one stack and your non-stateful resources (for example, a Lambda function) in a separate stack.

```typescript
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

To convert this to a Pulumi CDK app, combine the two stacks into a single stack and then use `transforms` to set `protect: true` on the `DbCluster`.

```typescript
import * as pulumi from '@pulumi/pulumi';
import * as pulumicdk from '@pulumi/cdk';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as rds from 'aws-cdk-lib/aws-rds';

interface AppStackProps extends pulumicdk.StackProps { }

class AppStack extends pulumicdk.Stack {
  constructor(scope: pulumicdk.App, id: string, props: AppStackProps) {
    super(scope, id, props);

    const cluster = new rds.DatabaseCluster(this, 'cluster', { ... });
    new AppConstruct(this, 'app-construct', {
        cluster: cluster,
    })

  }
}

const app = new pulumicdk.App('app', (scope: pulumicdk.App) => {
  new AppStack(app, 'app-stack');
}, {
    transforms: [
        (args: pulumi.ResourceTransformArgs): pulumi.ResourceTransformResult => {
            if (args.type === 'aws-native:rds:DbCluster') {
                return {
                    props: args.props,
                    opts: pulumi.mergeOptions(args.opts, { protect: true }),
                };
            }
            return undefined;
        },
    ]
});
```

### Converting stacks with different environments

If your application has stacks in different environments, you can convert it to Pulumi CDK as long as there are no dependencies between the stacks.
Convert each individual CDK stack to a Pulumi CDK stack.

For example, take this CDK application:

```typescript
import * as cdk from 'aws-cdk-lib/core';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';

class StackEast1 extends cdk.Stack {
  constructor(scope: Construct, id: string) {
    super(scope, id, {
      env: { region: 'us-east-1' },
    });

     new s3.Bucket(this, 'bucket1')
  }
}

class StackEast2 extends cdk.Stack {
  constructor(scope: Construct, id: string) {
    super(scope, id, {
      env: { region: 'us-east-2' },
    });

     new s3.Bucket(this, 'bucket1')
  }
}

const app = new cdk.App();
new StackEast1(app, 'east1-stack');
new StackEast2(app, 'east2-stack');
```

It converts to this Pulumi CDK application:

```typescript
import * as ccapi from '@pulumi/aws-native';
import * as aws from '@pulumi/aws';
import * as pulumicdk from '@pulumi/cdk';
import * as s3 from 'aws-cdk-lib/aws-s3';

class StackEast1 extends pulumicdk.Stack {
  constructor(scope: pulumicdk.App, id: string) {
    super(scope, id, {
      props: {
        env: { region: 'us-east-1' },
      },
      // pass explicit providers for the 'us-east-1' region
      providers: [
        new ccapi.Provider('ccapi', {
            region: 'us-east-1',
        }),
        new aws.Provider('aws', {
            region: 'us-east-1',
        }),
      ]
    });

     new s3.Bucket(this, 'bucket1')
  }
}

class StackEast2 extends pulumicdk.Stack {
  constructor(scope: pulumicdk.App, id: string) {
    super(scope, id, {
      props: {
        env: { region: 'us-east-2' },
      },
    });

     new s3.Bucket(this, 'bucket1')
  }
}

const app = new pulumicdk.App('app', (scope: pulumicdk.App) => {
  new StackEast1(scope, 'east1-stack');
  new StackEast2(scope, 'east2-stack');
});
```

## Converting CDK stages

An AWS CDK [Stage](https://docs.aws.amazon.com/cdk/v2/guide/stages.html) represents a group of one or more AWS CDK stacks that are configured to deploy together to a particular environment.
For example, the [same-environment example](#converting-same-environment-stacks) deploys a `StatefulStack` and an `AppStack`;
a CDK application would use stages to deploy these to different environments.

```typescript
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

The AWS CDK stages can be converted to [Pulumi stacks](/docs/iac/concepts/stacks/).
Like CDK stages, Pulumi stacks can be used to deploy groups of resources to different environments.

In AWS CDK applications, differences in configuration between environments are typically configured through input parameters on the stage.
In this example, the `DatabaseCluster` uses a different `InstanceType` between the `dev` and `prod` environments.
When you convert this application to Pulumi, you move this configuration from the stage input properties to [stack configuration](/docs/iac/concepts/config/).

To convert the AWS CDK application:

* Combine the stacks, as in the [multi-stack example](#converting-same-environment-stacks).
* Remove the use of CDK stages.
* Read the instance type from the [Pulumi configuration](/docs/iac/concepts/config/).

```typescript
import * as pulumi from '@pulumi/pulumi';
import * as pulumicdk from '@pulumi/cdk';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as rds from 'aws-cdk-lib/aws-rds';

const config = new pulumi.Config();
const instanceType = config.require('instanceType');

interface AppStackProps extends pulumicdk.StackProps {
  instanceType: ec2.InstanceType;
}

class AppStack extends pulumicdk.Stack {
  constructor(scope: pulumicdk.App, id: string, props: AppStackProps) {
    super(scope, id, props);

    const cluster = new rds.DatabaseCluster(this, 'cluster', {
      writer: rds.ClusterInstance.provisioned('writer', {
        instanceType: props.instanceType,
      }),
      ...
    });
    new AppConstruct(this, 'app-construct', {
        cluster: cluster,
    })

  }
}

const app = new pulumicdk.App('app', (scope: pulumicdk.App) => {
  new AppStack(app, 'app-stack', {
    instanceType: new ec2.InstanceType(instanceType),
  });
}, {
    transforms: [
        (args: pulumi.ResourceTransformArgs): pulumi.ResourceTransformResult => {
            if (args.type === 'aws-native:rds:DbCluster') {
                return {
                    props: args.props,
                    opts: pulumi.mergeOptions(args.opts, { protect: true }),
                };
            }
            return undefined;
        },
    ]
});
```

After converting the code, create the `dev` Pulumi stack and set the `instanceType` config property.

```console
$ pulumi stack init dev
$ pulumi config set instanceType r6g.medium
```

Then create the `prod` Pulumi stack and set the `instanceType` config property.

```console
$ pulumi stack init prod
$ pulumi config set instanceType r6g.xlarge
```

## Importing CDK resources

All the prior examples in this guide discuss standing up a new Pulumi CDK stack and creating new AWS resources.
If you want to instead have Pulumi import the state of your existing resources you can try the experimental [Pulumi CDK Import Tool](https://github.com/pulumi/pulumi-tool-cdk-importer).
This tool allows you to specify a CDK stack to import and then the resources in that stack will be imported into your Pulumi stack so that Pulumi can take over management of those resources.

**1. Install the tool**

```console
$ pulumi plugin install tool cdk-importer
```

**2. Run the tool, passing in the name of the CDK stack you want to import**

```console
$ pulumi plugin run cdk-importer -- runtime --stack $StackName
```

**3. Run `pulumi preview` to ensure there are no diffs**

If there are any issues with importing, the tool can be run again to try the import again without it affecting previously imported resources.

## More info

For more information about using Pulumi CDK, see the [Pulumi CDK guide](/dev/tutorials/aws-cdk/) or the [Pulumi CDK GitHub repository](https://github.com/pulumi/pulumi-cdk).
