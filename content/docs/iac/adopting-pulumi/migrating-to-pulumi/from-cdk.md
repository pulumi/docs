---
title_tag: "Migrating from AWS CDK"
meta_desc: Migrate your existing AWS CDK TypeScript application
title: AWS CDK
h1: "Migrating from AWS CDK to Pulumi"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    name: AWS CDK
    parent: iac-adopting-migrate
    weight: 2
  usingpulumi:
    identifier: from-aws-cdk
    parent: migrating
    weight: 3
search:
  keywords:
    - AWS
    - CDK
    - AWS CDK
    - Stack Outputs
---

If your team has already provisioned infrastructure using AWS CDK, and you'd like to adopt Pulumi, you have two primary strategies you can take:

* [**Coexist**](#referencing-stack-outputs) with resources provisioned by CDK by referencing stack outputs.
* [**Convert**](#converting-cdk-applications) your CDK application to use [Pulumi CDK](https://github.com/pulumi/pulumi-cdk)

## Referencing Stack Outputs

It is possible to reference existing AWS CDK stacks from your program. It doesn't matter how these stacks were created. This lets you read properties of that CloudFormation stack for use within your Pulumi program. This includes output values computed from resources provisioned by that stack.

For instance, let's say your infrastructure team has provisioned your network infrastructure using CDK and you need to use the Subnet ID to provision something new from your Pulumi program. One approach is to hardcode that ID but this is brittle and, if it ever changes, you'd need to go and manually update the hardcoded value.

Instead, you can look up that stack by name and use one of its output values. The following example reads an AWS CDK stack named `my-network-stack` and then uses the exported `SubnetId` value to provision a brand new EC2 instance that runs in that subnet:

```ts
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

All we need to do is run `pulumi up` and the Pulumi runtime will know how to query the CDK stack and retrieve its output values. In this case, the CDK stack is treated entirely as read-only, and Pulumi will never attempt to modify it or any resources managed by it.

> Although we've hard-coded the AWS CDK stack name here &mdash; `"my-network-stack"` &mdash; it's common to dynamically compute a name using unique per-stack information, like the stack name, AWS region, or other configuration variables.

## Converting CDK Applications

Let's say you want to migrate from AWS CDK to Pulumi and that simply co-existing side-by-side as shown above isn't sufficient. In this case you can convert your AWS CDK application to a Pulumi CDK application using the [Pulumi CDK Adapter](https://github.com/pulumi/pulumi-cdk).

Using the below example as a starting point, we will convert this CDK application to use Pulumi CDK.

```ts
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

### Install Pulumi Dependencies

The Pulumi CDK Adapter requires the installation of the following npm packages:

* [@pulumi/aws](https://www.npmjs.com/package/@pulumi/aws)
* [@pulumi/aws-native](https://www.npmjs.com/package/@pulumi/aws-native)
* [@pulumi/docker-build](https://www.npmjs.com/package/@pulumi/docker-build)
* [@pulumi/pulumi](https://www.npmjs.com/package/@pulumi/pulumi)

```console
npm install @pulumi/aws @pulumi/aws-native @pulumi/docker-build @pulumi/pulumi
```

### Convert the CDK Stack and App

Replace the CDK `Stack` and `App` classes with Pulumi CDK `Stack` and `App` classes.

```ts
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

### Deploy the Pulumi Stack

Now that you have converted your AWS CDK application to a Pulumi CDK application you can use the Pulumi CLI to create a Pulumi Stack and deploy.

```console
$ pulumi up
```

## Converting Multi-Stack CDK Applications

If your CDK application contains multiple CDK Stacks they may fall into a couple of scenarios.

1. You have multiple CDK Stacks that all deploy to the same environment (AWS account/region).
2. You have multiple CDK Stacks that deploy to multiple environments

### Converting Same Environment Stacks

If all of your CDK Stacks deploy to the same environment you can combine them all into a single Pulumi CDK Stack.
Pulumi CDK Stacks do not have the same resource limits that CloudFormation Stacks have.
You can also control termination protection at the resource level in Pulumi instead of at the CloudFormation Stack level in CDK.

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

To convert this to a Pulumi CDK app, you would combine the two stacks into a single stack and then use `transforms` to set `protect: true` on the `DbCluster`.

```ts
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

### Converting Stacks with Different Environments

If your application has stacks in different environments you can convert it to Pulumi CDK as long as there are no dependencies between the stacks.
You would convert each individual CDK Stack to a Pulumi CDK Stack.

For example, this:

```ts
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

Would be converted to this:

```ts
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
      env: { region: 'us-east-2' },
    });

     new s3.Bucket(this, 'bucket1')
  }
}

const app = new pulumicdk.App('app', (scope: pulumicdk.App) => {
  new StackEast1(scope, 'east1-stack');
  new StackEast2(scope, 'east2-stack');
});
```

## Converting CDK Stages

An AWS CDK [Stage](https://docs.aws.amazon.com/cdk/v2/guide/stages.html) represents a group of one or more AWS CDK Stacks that are configured to deploy together to a particular environment.
For example, taking the example from above where we deploy a `StatefulStack` and an `AppStack`,
we would use stages to deploy these to different environments.

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

The AWS CDK Stages can be converted to [Pulumi Stacks](https://www.pulumi.com/docs/iac/concepts/stacks/).
Similar to CDK Stages, Pulumi Stacks can be used to deploy groups of resources to different environments.

In AWS CDK applications differences in configuration between environments are typically configured through input parameters on the Stage.
In the above example, the `DatabaseCluster` uses a different `InstanceType` between the `dev` and `prod` environments.
When we convert this application to Pulumi, we will move this configuration from the Stage input properties to [Stack Configuration](https://www.pulumi.com/docs/iac/concepts/config/)

When we convert the AWS CDK application we will:

* Combining the Stacks like we did in the [Multi Stack example](#converting-same-environment-stacks)
* Remove the use of CDK Stages
* Read the instance type from the [Pulumi Configuration](https://www.pulumi.com/docs/iac/concepts/config/).

```ts
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

Once we have converted the code, we create the `dev` Pulumi Stack and set the `instanceType` config property.

```console
$ pulumi stack init dev
$ pulumi config set instanceType r6g.medium
```

Then we create the `prod` Pulumi Stack and set the `instanceType` config property.

```console
$ pulumi stack init prod
$ pulumi config set instanceType r6g.xlarge
```

## Importing CDK Resources

All the prior examples in this guide discuss standing up a new Pulumi CDK Stack and creating new AWS resources.
If you want to instead have Pulumi import the state of your existing resources you can try the experimental [Pulumi CDK Import Tool](https://github.com/pulumi/pulumi-tool-cdk-importer).
This tool allows you to specify a CDK stack to import and then the resources in that stack will be imported into your Pulumi Stack so that Pulumi can take over management of those resources.

**1. Install the tool**

```console
$ pulumi plugin install tool cdk-importer
```

**2. Run the tool, passing in the name of the CDK Stack you want to import**

```console
$ pulumi plugin run cdk-importer -- -stack $StackName
```

**3. Run `pulumi preview` to ensure there are no diffs**

If there are any issues with importing, the tool can be run again to try the import again without it affecting previously imported resources.

## More Info

For more info on using Pulumi CDK check out the [Pulumi CDK Guide](https://www.pulumi.com/docs/iac/clouds/aws/guides/cdk/) or the [Pulumi CDK GitHub Repository](https://github.com/pulumi/pulumi-cdk) for more info.
