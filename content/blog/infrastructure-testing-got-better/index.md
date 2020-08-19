---
title: "At Scale Infrastructure Testing With Pulumi"
date: 2020-05-28
meta_desc: "Pulumi accelerates infrastructure testing 60x with mocking and unit tests."
meta_image: dustin-farris.png
authors:
    - dustin-farris
tags:
    - test driven development
    - unit testing
---

**Guest Article:** Dustin Farris is an experienced cloud engineering consultant.  He’s currently building a new data lake for a large public university using Pulumi. The project handles sensitive student and research data and as a result, his team must meet stringent QA and security requirements.  Dustin shows how resource mocking in Pulumi makes testing and verification faster than ever before.

<!--more-->

The university IT team has ambitious goals for a new data lake that we’re building.  We need to follow AWS Well-Architected standards, adopt cutting-edge tools, and demonstrate provable quality and security from development to production.

Advancements in available cloud services give us the opportunity to deliver better performance, scalability, reliability, and security.  We are redesigning our infrastructure to include:

1. [AWS Database Migration Service (DMS)](https://aws.amazon.com/dms/) for connectivity to on-prem, legacy databases;
1. [AWS Glue](https://aws.amazon.com/glue/) for extracting, transforming and loading (ETL) new data;
1. [AWS Lambda](https://aws.amazon.com/lambda/) Step Functions for workflows; and
1. [AWS Lake Formation](https://aws.amazon.com/lake-formation/) for creating a secure data catalog available for analytics tools.

With this shift, it makes sense to throw out old configurations and pick the best tools for the job rather than be encumbered by legacy DSLs. We use Pulumi as our Infrastructure as Code tool of choice because it has all of the capabilities we need:

* Pulumi supports TypeScript - the modern programming language that the team prefers for its static typing capabilities.
* It works ‘out of the box’ with modern Integrated Development Environments (IDEs) like Visual Studio Code.
* Because Pulumi uses familiar programming languages, we can unit test our code
* By virtue of working with TypeScript, it natively supports Mocha - our testing framework of choice.

##### *Watch Dustin Farris and Lee Zen demonstrate unit testing on this episode of [Modern Infrastructure Wednesday](https://www.youtube.com/playlist?list=PLyy8Vx2ZoWloyj3V5gXzPraiKStO2GGZw).*

{{< youtube "ydR61dZmKgU" >}}

## Accelerating Verification

There are many benefits to using Pulumi to develop and test infrastructure. First, the team has the immediate benefit of modern language and IDE support: things like missing arguments are now visible in-line as we define resources.  In addition, state tracking and version control capabilities, for all cloud provider resources, make for a terrific experience in terms of productivity.

Second, creating standard infrastructure stacks for the team helps everyone move faster.  We create environments for each developer in separate AWS accounts so they can develop features without impacting other developers and we don’t have to wait for central IT to provision resources. Pulumi’s support for ephemeral environments means that developers can spin-up and spin-down stacks quickly, in order to verify that changes to the desired state are actually reflected in the provisioned resources.  This makes integration testing far easier, and ephemeral environments keep cloud costs down because they are easily destroyed when they are no longer needed.

Ideally, a unit test should demonstrate that a new component or resource works in isolation from other dependencies.  Resource mocking mimics complex infrastructure in lieu of spinning up the dedicated infrastructure for a test (which would be slow and potentially expensive.) This step is critical for preventing configuration mistakes from reaching production.

The unit test suite for our data lake consists of over 700 tests and previously took almost 20 minutes to execute.  With improvements to StackReference mocking and the new ‘monitor mock’ feature, these same tests now run in about 20 seconds.  _That’s 60x faster over our previous performance!_

## Getting Started with Resource Mocking

Continuously testing resource definitions is a best practice and it’s incredibly easy to get started. In this example, we mock a resource name to attach to an IAM Policy Role. The test checks that we attach the correct policy to the expected role.

**test-setup**.**ts**

```ts
/**
 * Create the mock resource
 */
pulumi.runtime.setMocks({
   newResource: function (
       resourceType: string,
       name: string,
       inputs: any,
       provider?: string,
       id?: string,
   ): { id: string; state: Record<string, any> } {
       const defaultState = {
           arn: `${name}-arn`,
           name: name,
           ...inputs,
       };
       // Use id unless it's blank or missing.
       const resourceId = id?.trim() ? id : `${name}-id`;
       return { id: resourceId, state: defaultState };
   },
   call: function (): Record<string, any> {
       return {};
   },
});
```

**infra**.**ts**

```ts
export const attachment = new aws.iam.RolePolicyAttachment(
   "role-policy-attachment",
   {
       policyArn: policy.arn,
       role: role.name,
   },
);
```

**infra**.**spec**.**ts**

```ts
/**
 * Returns a resource output's value, even if it's undefined.
 */
const getOutput = <T>(output: pulumi.Output<T>): Promise<T | undefined> =>
   (output as any).promise() as Promise<T>;
​
describe("attachment", () => {
   it("attaches the policy", async () => {
       assert.equal(
           await getOutput(attachment.policyArn),
           await getOutput(policy.arn),
       );
   });
   it("attaches to the role", async () => {
       assert.equal(
           await getOutput(attachment.role),
           await getOutput(role.name),
       );
   });
});
```

The key part is that we never actually talk to the cloud provider. Instead, we are able to mock the output values that we’d typically expect to have from using the provider such as the ARN. In the above example, you can see we simply mock out the ARN by returning “${name}-arn” instead of whatever the cloud provider would actually assign. There are many powerful ways to use this mocking to ensure that certain output properties are set or to mock the return of certain lookup calls to the cloud provider.

## Testing with Policies

In addition to resource testing with mocks, we can test the entire stack with policies. This example ensures that the EKS cluster uses version 1.13 deployed on a custom VPC.

**infra**.**ts**

```ts
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";

// Create a custom VPC.
const vpc = new awsx.ec2.Vpc("my-vpc");

// Create a basic EKS cluster.
const cluster = new eks.Cluster("my-cluster", {
    desiredCapacity: 2,
    minSize: 1,
    maxSize: 2,
    storageClasses: "gp2",
    deployDashboard: false,
    version: "1.13",
    vpcId: vpc.id,
    subnetIds: vpc.publicSubnetIds,
});
```

**policy**.**test**

```ts
const stackPolicy: policy.StackValidationPolicy = {
    name: "eks-test",
    description: "EKS integration tests.",
    enforcementLevel: "mandatory",
    validateStack: async (args, reportViolation) => {
        const clusterResources = args.resources.filter(r => r.isType(aws.eks.Cluster));
        if (clusterResources.length !== 1) {
            reportViolation(`Expected one EKS Cluster but found ${clusterResources.length}`);
            return;
        }

        const cluster = clusterResources[0].asType(aws.eks.Cluster)!;
        if (cluster.version !== "1.13") {
            reportViolation(`Expected EKS Cluster '${cluster.name}' version to be '1.13' but found '${cluster.version}'`);
        }

        const vpcId = cluster.vpcConfig.vpcId;
        if (!vpcId) {
            // 'isDryRun==true' means the test are running in preview.
            // If so, the VPC might not exist yet even though it's defined in the program.
            // We shouldn't fail the test then to avoid false negatives.
            if (!pulumi.runtime.isDryRun()) {
                reportViolation(`EKS Cluster '${cluster.name}' has unknown VPC`);
            }
            return;
        }

        const ec2 = new aws.sdk.EC2({region: aws.config.region});
        const response = await ec2.describeVpcs().promise();
        const defaultVpc = response.Vpcs?.find(vpc => vpc.IsDefault);
        if (!defaultVpc) {
            reportViolation("Default VPC not found");
            return;
        }

        if (defaultVpc.VpcId === vpcId) {
            reportViolation(`EKS Cluster '${cluster.name}' should not use the default VPC`);
        }
    },
}

const tests = new policy.PolicyPack("tests-pack", {
    policies: [stackPolicy],
});
```

Policy tests run on the entire stack are integration tests. We have two policies. The first policy is to check the EKS version which is done without deploying because the version is an input value. Next, we check to see if the tests are running in preview. The test returns a violation if the VPC has not been deployed because it does not have an output for the policy to validate .

## Next Steps

After working with Pulumi to build-out our data lake and implementing robust, end-to-end testing, the team is now moving towards Continuous Integration and Continuous Delivery (CI/CD) using AWS CodePipeline. We are also looking forward to Pulumi’s new policy-as-code framework, CrossGuard, to set guardrails on infrastructure and enforce compliance - further advancing the team’s QA and security goals.  

## Conclusion

Testing is just one of the superpowers that Pulumi 2.0 delivers. For more information, see our [Testing User Guide]({{< relref "/docs/guides/testing" >}}) and [worked examples](https://github.com/pulumi/examples#testing) on GitHub in the language of your choice.
