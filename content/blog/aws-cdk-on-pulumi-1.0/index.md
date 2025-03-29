---
title: "Announcing the 1.0 release of AWS CDK on Pulumi"
date: 2024-12-02T08:00:00-07:00
meta_desc: "Enhanced support of AWS CDK constructs from within Pulumi. Combine Pulumi
  and AWS CDK resources amd use Pulumi Cloud Platform to manage CDK"
meta_image: meta.png
authors:
  - matt-jeffryes
  - cory-hall
  - florian-stadler
  - anton-tayanovskyy
tags:
  - aws-cdk
search:
  keywords:
    - AWS
    - CDK
    - AWS CDK
    - CDK constructs
    - Cloud Engineering
---

At Pulumi, we're committed to delivering the widest range of cloud infrastructure building blocks for use in your cloud engineering projects.
In 2022, we introduced [preview](https://www.pulumi.com/blog/aws-cdk-on-pulumi/) support for integrating AWS CDK constructs into Pulumi programs
and today we're happy to announce the 1.0 release of our pulumi-cdk library for typescript. This first stable version completes support for common CDK features
enabling you to deploy almost any CDK construct with Pulumi.

<!--more-->

The pulumi-cdk library provides access to the many high-level libraries ('constructs') built by service teams at AWS and by the AWS CDK community. However, there were some limitations in the preview version of the library that prevented using some constructs and complicating migration of existing CDK stacks. Uncertainty about which constructs were supported has limited adoption of this rich ecosystem by Pulumi users.

With the new 1.0 release, pulumi-cdk has greatly expanded compatibility with all CDK features. Users can now confidently use Pulumi to deploy constructs they have written themselves or any of the 1600+ constructs in AWS's [construct hub](https://constructs.dev/search?cdk=aws-cdk&sort=downloadsDesc&offset=0). We're excited to bring Pulumi users access to all the high level interfaces curated by AWS and the CDK community.

Additionally, existing AWS CDK users now have an easier path to transition from CloudFormation to Pulumi, unlocking faster deployments, integration with Pulumi's vast provider ecosystem and all of the features of Pulumi's Cloud Engineering Platform (like [Policy as Code](https://www.pulumi.com/docs/using-pulumi/crossguard/), [Audit Logs](https://www.pulumi.com/docs/pulumi-cloud/audit-logs/), [Drift detection](https://www.pulumi.com/docs/pulumi-cloud/deployments/drift/), [Secrets](https://www.pulumi.com/docs/esc/get-started/), and much more).

## Deploying CDK Constructs with Pulumi

To deploy existing AWS CDK Constructs using Pulumi:

1. Create a class that derives from `pulumicdk.Stack` (which itself is derived from `awscdk.Stack`).
2. In the constructor, use any AWS CDK constructs from existing libraries such as [`aws-cdk-lib`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib-readme.html)
3. Create a `pulumicdk.App` instance that constructs an instance of your stack.

For example, the following program deploys an AWS Apprunner CDK Construct using Pulumi:

```typescript
import * as pulumi from '@pulumi/pulumi';
import * as pulumicdk from '@pulumi/cdk';
import { Service, Source } from '@aws-cdk/aws-apprunner-alpha';

class AppRunnerStack extends pulumicdk.Stack {
    url: pulumi.Output<string>;

    constructor(id: string, options?: pulumicdk.StackOptions) {
        super(id, options);

        const service = new Service(this, 'service', {
            source: Source.fromEcrPublic({
                imageConfiguration: { port: 8000 },
                imageIdentifier: 'public.ecr.aws/aws-containers/hello-app-runner:latest',
            }),
        });

        this.url = this.asOutput(service.serviceUrl);
    }
}

const app = new pulumicdk.App('app', (scope: pulumicdk.App): pulumicdk.AppOutputs => {
    const stack = new AppRunnerStack('teststack');
    return {
        url: stack.url,
    };
});
export const url = app.outputs['url'];
```

Deploy with a `pulumi up`:

```console
> pulumi up

Updating (dev)

View Live: https://app.pulumi.com/lukehoban/pulumi-cdk-apprunner/dev/updates/1

     Type                                   Name                       Status
 +   pulumi:pulumi:Stack                    pulumi-cdk-apprunner-dev   created
 +   └─ cdk:index:StackComponent            teststack                  created
 +      └─ cdk:construct:Service            teststack/adapter/service  created
 +         └─ aws-native:apprunner:Service  service6D174F83            created

Outputs:
    url: "2ez3iazupm.us-west-2.awsapprunner.com"

Resources:
    + 4 created
```

And curl the endpoint:

```console
> curl https://$(pulumi stack output url)

   ______                             __        __      __  _                  __
  / ____/___  ____  ____ __________ _/ /___  __/ /___ _/ /_(_)___  ____  _____/ /
 / /   / __ \/ __ \/ __ `/ ___/ __ `/ __/ / / / / __ `/ __/ / __ \/ __ \/ ___/ /
/ /___/ /_/ / / / / /_/ / /  / /_/ / /_/ /_/ / / /_/ / /_/ / /_/ / / / (__  )_/
\____/\____/_/ /_/\__, /_/   \__,_/\__/\__,_/_/\__,_/\__/_/\____/_/ /_/____(_)
                 /____/

        Congratulations, your service has successfully deployed on AWS App Runner.

Open it in your browser at https://2ez3iazupm.us-west-2.awsapprunner.com/

Try the workshop at https://apprunnerworkshop.com
Read the docs at https://docs.aws.amazon.com/apprunner
```

## Pulumi takes CDK apps to the next level

Combine CDK constructs with any of the features of Pulumi programs to deploy faster, easier and to any cloud. Use Pulumi functions and stack references to connect to pre-existing infrastructure and mix in resources from any provider to bring *all* of your infrastructure under management.

For example, we can use CDK's `ecs_patterns` to quickly create a loadbalanced Fargate service, but route traffic to it with a record in an exisiting CloudFlare DNS zone.

```typescript
import * as path from 'path';
import * as acm from 'aws-cdk-lib/aws-certificatemanager';
import * as aws from '@pulumi/aws';
import * as pulumi from '@pulumi/pulumi';
import * as pulumicdk from '@pulumi/cdk';
import * as cloudflare from '@pulumi/cloudflare';
import * as ecs from 'aws-cdk-lib/aws-ecs';
import * as ecsPatterns from 'aws-cdk-lib/aws-ecs-patterns';

let config = new pulumi.Config();
let accountId = config.requireSecret("cloudflare_account_id");
let zoneName = config.require("cloudflare_zone_name");
let certificateId = config.require("certificate_id");
let certificateKey = config.requireSecret("certificate_key");

class CloudFlareStack extends pulumicdk.Stack {
    constructor(app: pulumicdk.App, id: string) {
        super(app, id);

        // First Load the zone and certificate from CloudFlare
        ///////////////////////////////////////////////////////

        // Read the CloudFlare zone for the domain
        const zone = cloudflare.getZoneOutput({
            accountId,
            name: zoneName,
        });

        // read the certificate from CloudFlare
        const caCertificate = cloudflare.getOriginCaCertificateOutput({
          id: certificateId,
        });

        // Import the certificate in ACM
        const cert = new aws.acm.Certificate('import', {
            privateKey: certificateKey,
            certificateBody: caCertificate.certificate,
        });

        // Create a L2 reference from the cert arn
        const acmCert = acm.Certificate.fromCertificateArn(this, 'cert', pulumicdk.asString(cert.arn));

        // Next, use ECS Patterns to create a loadbalanced fargate service with the correct certificate
        ///////////////////////////////////////////////////////////////////////////////////////////////

        const loadBalancedFargateService = new ecsPatterns.ApplicationLoadBalancedFargateService(this, 'Service', {
          certificate: acmCert,
          redirectHTTP: true,
          taskImageOptions: {
            image: ecs.ContainerImage.fromRegistry("amazon/amazon-ecs-sample"),
          },
        });

        const alb = loadBalancedFargateService.loadBalancer;

        // Finally, Create a record in CloudFlare that directs to the service's loadbalancer
        ////////////////////////////////////////////////////////////////////////////////////

        new cloudflare.Record('alb', {
            name: 'cdk-alb',
            type: 'CNAME',
            zoneId: zone.zoneId,
            content: this.asOutput(alb.loadBalancerDnsName),
            proxied: true,
        });
    }
}

class MyApp extends pulumicdk.App {
    constructor() {
        super('app', (scope: pulumicdk.App) => {
            new CloudFlareStack(scope, 'cloudflare');
        });
    }
}

new MyApp();
```

Pulumi let's you read and create any resource type across thousands of different cloud service providers and integrate them with your CDK stacks.  Building CDK apps on Pulumi brings a host of other benefits too, including:

- Customize [resource options](https://www.pulumi.com/docs/iac/concepts/options/) (eg. to protect a database against accidental deletion or deploy to multiple regions in the same program)
- [Detect and manage drift](https://www.pulumi.com/docs/pulumi-cloud/deployments/drift/) with Pulumi deployments
- Track and store user actions and change history with [Audit Logs](https://www.pulumi.com/docs/pulumi-cloud/audit-logs/)
- And a host of other benefits from [Pulumi Cloud](https://www.pulumi.com/product/pulumi-cloud/)

## Expanded Features in pulumi-cdk 1.0

The 1.0 version of pulumi-cdk adds support for key CDK features such as: assets, custom resources, nested stacks, and aspects, so most existing CDK constructs will work with Pulumi without any modification. We've also eliminated the need to call `cdk bootstrap` before running `pulumi up` by integrating a custom Pulumi Synthesizer.

### Using CDK Aspects

Pulumi CDK now supports CDK aspects. For example, you can add the [cdk-nag](https://github.com/cdklabs/cdk-nag) aspect to your stack to enforce best practices:

```ts
import * as pulumicdk from '@pulumi/cdk';
import * as s3 from 'aws-cdk-lib/aws-s3';
import { AwsSolutionsChecks } from 'cdk-nag';

const app = new pulumicdk.App('app', (scope: pulumicdk.App): pulumicdk.AppOutputs => {
    const stack = new pulumicdk.Stack('example-stack');
    Aspects.of(stack).add(new AwsSolutionsChecks({ verbose: true }));

    new s3.Bucket(this, 'bucket');
});
```

#### Example Output

```console
[Error at /test-stack/bucket/Resource] AwsSolutions-S1: The S3 Bucket has server access logs disabled. The bucket should have server access logging enabled to provide detailed records for the requests that are made to the bucket.
[Error at /test-stack/bucket/Resource] AwsSolutions-S10: The S3 Bucket or bucket policy does not require requests to use SSL. You can use HTTPS (TLS) to help prevent potential attackers from eavesdropping on or manipulating network traffic using person-in-the-middle or similar attacks. You should allow only encrypted connections over HTTPS (TLS) using the aws:SecureTransport condition on Amazon S3 bucket policies.
```

### CDK assets

CDK's assets make it easy to bundle code and other files your application needs into an S3 bucket or a Docker container, eliminating extra steps from your build pipeline. For example you can use Docker container asset to deploy a Fargate service from local directory. CDK will build the container image and push to ECR on `pulumi up`.

```ts
import * as pulumicdk from '@pulumi/cdk';
import * as aws from '@pulumi/aws';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as ecs from 'aws-cdk-lib/aws-ecs';
import * as ecs_patterns from 'aws-cdk-lib/aws-ecs-patterns';

const app = new pulumicdk.App('app', (scope: pulumicdk.App) => {
    const stack = new pulumicdk.Stack('example-stack');

    const vpc = new ec2.Vpc(stack, 'MyVpc');
    const cluster = new ecs.Cluster(stack, 'fargate-service-autoscaling', { vpc });

    // Create Fargate Service
    const fargateService = new ecs_patterns.NetworkLoadBalancedFargateService(this, 'sample-app', {
        cluster,
        taskImageOptions: {
            image: ecs.ContainerImage.fromAsset(path.join(__dirname, './'), {
                // assetName is required and is used in the name of the ecr repository that is created
                assetName: 'cdk-fargate-example',
            }),
        },
    });
});
```

## Future direction

Currently AWS CDK on Pulumi is supported only for TypeScript users, but we're eager to bring the benefits of the CDK ecosystem to all Pulumi languages in the future. You can comment and upvote on [this tracking issue](https://github.com/pulumi/pulumi-cdk/issues/49), to let us know this is important to you.

We're also exploring options for importing state from CDK applications that are already deployed with CloudFormation to enable seamless migration for existing CDK users. Please let us know on [this tracking issue](https://github.com/pulumi/pulumi-cdk/issues/271) if you would be interested in testing this with us.

## Summary

The 1.0 release of AWS CDK support for Pulumi marks a significant expansion of opportunities to interoperate between the AWS CDK and Pulumi ecosystems. Existing AWS CDK users can now more easily adopt the full power, speed and flexibility of the Pulumi Cloud Platform and its diverse ecosystem.  And existing Pulumi users can benefit from the many expert curated constructs and libraries in the CDK community. We're excited to see what you'll build with these two great cloud technologies together.

The AWS CDK on Pulumi project is open source at [https://github.com/pulumi/pulumi-cdk](https://github.com/pulumi/pulumi-cdk) and on NPM at [https://www.npmjs.com/package/@pulumi/cdk](https://www.npmjs.com/package/@pulumi/cdk). Get started today\!
