---
title: "Testable IAM Policy Documents"
date: 2021-05-12
meta_desc: "Pulumi community member Thierry de Pauw introduces a Node module for checking and validating IAM policy documents."
meta_image: testable_iam_policy.png
authors:
    - thierry-de-pauw
tags:
    - AWS
    - IAM
---

I was relieved to find Pulumi. Finally, we have testable Infrastructure as Code. We can write fast unit tests that we can execute locally without needing the cloud. However, I was a bit disappointed. Pulumi does not have a full representation of IAM Policy documents. Fortunately, it was relatively easy to build a library that did this!

<!--more-->

Policy documents are assigned using JSON objects that should follow the AWS
IAM JSON Policy syntax.

```typescript
const policy = new aws.iam.Policy("policy", {
    description: "My test policy",
    policy: JSON.stringify({
        Version: "2012-10-17",
        Statement: [{
            Action: ["ec2:Describe*"],
            Effect: "Allow",
            Resource: "*",
        }],
    }),
});
```

However, it is perfectly possible to pass an invalid IAM Policy document because there is no validation. You will only notice if it is invalid the minute the policy is applied in the AWS cloud. That creates an unreasonably long feedback loop, incurring a significant amount of waiting and time to correct.

To avoid this, I prefer to write my policies as Policy as Code. It avoids
common syntax errors, reduces the feedback cycle, and increases
your delivery throughput.

Having to pass a JSON as a policy document did not feel optimal.

I work in the financial industry, and compliance is important. So, I searched for something that allowed me to easily unit test IAM Policy documents, preferably at the Statement level,to help us adhere to security requirements.

Before reinventing the wheel, I searched for existing packages in
JavaScript for manipulating IAM Policy documents.

Pulumi has the [`aws.iam.getPolicyDocument`]({{< relref "/registry/packages/aws/api-docs/iam/getpolicydocument" >}}) API. That looked interesting because it allows writing the policies as Policy as Code. But you cannot properly unit test the IAM Policy document produced by
`aws.iam.getPolicyDocument` function. When Pulumi runs in testing mode, that function is not available unless you mock it. Huh. That is not very helpful.

I dug further to find Node.js packages for manipulating IAM Policy documents. Not much. Except for [AWS CDK](https://docs.aws.amazon.com/cdk/api/latest/typescript/api/aws-iam.html). But you must drag the whole CDK Node.js package into your project only to handle IAM Policy documents. But, the AWS CDK was a good starting point for designing [@thinkinglabs/aws-iam-policy](https://github.com/thinkinglabs/aws-iam-policy).

## A simple identity-based policy

Let us look at the code sample on `pulumi.com` for
[`aws.iam.Policy`](https://www.pulumi.com/docs/reference/pkg/aws/iam/policy/).

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const policy = new aws.iam.Policy("policy", {
    description: "My test policy",
    policy: JSON.stringify({
        Version: "2012-10-17",
        Statement: [{
            Action: ["ec2:Describe*"],
            Effect: "Allow",
            Resource: "*",
        }],
    }),
});
```

Using `@thinkinglabs/aws-iam-policy`, that would look as follows.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import {PolicyDocument, Statement} from "@thinkinglabs/aws-iam-policy";

export const policy = new aws.iam.Policy("policy", {
    description: "My test policy",
    policy: grantEC2Describe(),
});

function grantEC2Describe() {
  return new PolicyDocument([
    new Statement({
      effect: "Allow",
      actions: ["ec2:Describe*"],
      resources: ["*"],
    }),
  ]).json
}
```

To test if the IAM Policy is a valid identity-based policy, we can use `PolicyDocument.validateForIdentityPolicy()`, which returns an array of `string` error messages. If it returns an empty array, the IAM Policy is valid.

```typescript
import {expect} from "chai";
import "./mocks";
import * as pulumi from '@pulumi/pulumi';
import {PolicyDocument, Statement} from '@thinkinglabs/aws-iam-policy';

import * as sut from "../src/index";

const get = <T>(output: pulumi.Output<T> | undefined): Promise<T | undefined> | undefined =>
  output ? (output as any).promise() as Promise<T> : undefined;

describe("IAM Policy", function() {

  it('should be a valid identity-based policy', async () => {
    const doc = await get(sut.policy.policy) as string
    const policy = PolicyDocument.fromJson(doc);

    expect(policy.validateForIdentityPolicy()).to.be.empty;
  });
});
```

## A more complex resource-based policy

As a regulated industry, we are required to closely control who has access to what. What scares us most is to inadvertently grant a right to someone that could result in non-compliance, for instance, granting delete S3 bucket rights or granting access to confidential information stored in an S3 Bucket.

To avoid this, we make extensive use of S3 Bucket policies composed of several statements granting:

- admin access to administrators,
- usage access to users
- and denying delete bucket rights for everyone.

Let us create an S3 Bucket with a Bucket Policy having multiple Statements.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import {PolicyDocument, Statement, AnonymousUserPrincipal, RootAccountPrincipal} from "@thinkinglabs/aws-iam-policy";

const adminRole = new aws.iam.Role("admin-role", {
  assumeRolePolicy: createAssumeRolePolicy(),
});
const userRole = new aws.iam.Role("user-role", {
  assumeRolePolicy: createAssumeRolePolicy(),
});
const bucket = new aws.s3.Bucket("bucket", {acl: "private"});
const bucketPolicy = new aws.s3.BucketPolicy("bucketPolicy", {
  bucket: bucket.id,
  policy: createS3BucketPolicy("0123456789012", bucket, [adminRole], [userRole]),
});

function createAssumeRolePolicy() {
  return new PolicyDocument([
    new Statement({
      effect: "Allow",
      principals: [new RootAccountPrincipal("123412341234")],
      actions: ["sts:AssumeRole"],
    }),
  ]).json;
}

export function createS3BucketPolicy(
    accountId: string,
    bucket: aws.s3.Bucket,
    bucketAdmins: aws.iam.Role[],
    bucketUsers: aws.iam.Role[],
) {
  return pulumi.all([
    bucket.arn,
    bucketAdmins.map((role) => role.uniqueId),
    bucketUsers.map((role) => role.uniqueId)
  ]).apply(([bucketArn, bucketAdminUniqueIds, bucketUserUniqueIds]) => {
      return new PolicyDocument([
        new Statement({
          sid: "Allow access for Bucket Administrators",
          effect: "Deny",
          principals: [new AnonymousUserPrincipal()],
          actions: [
            "s3:PutBucketPolicy",
            "s3:GetBucketPolicy*",
            "s3:DeleteBucketPolicy",
          ],
          resources: [bucketArn],
          conditions: {
            StringNotLike: {
              "aws:userId": [accountId]
                  .concat(bucketAdminUniqueIds.map((uniqueId) => `${uniqueId}:*`)),
            },
          },
        }),
        new Statement({
          sid: "Allow use of the bucket",
          effect: "Deny",
          principals: [new AnonymousUserPrincipal()],
          actions: ["s3:ListBucket*", "s3:Get*", "s3:PutObject*", "s3:DeleteObject*"],
          resources: [bucketArn, `${bucketArn}/*`],
          conditions: {
            StringNotLike: {
              "aws:userId": [accountId]
                  .concat(bucketAdminUniqueIds.map((uniqueId) => `${uniqueId}:*`))
                  .concat(bucketUserUniqueIds.map((uniqueId) => `${uniqueId}:*`)),
            },
          },
        }),
        new Statement({
          sid: "Deny delete bucket",
          effect: "Deny",
          principals: [new AnonymousUserPrincipal()],
          actions: ["s3:DeleteBucket"],
          resources: [bucketArn],
        })],
      ).json;
  });
}
```

To test if the S3 Bucket Policy allows access for bucket administrators, we need to check if a Statement is present in the Policy and test the content of that single Statement.

`@thinkinglabs/aws-iam-policy` provides the ability to retrieve a single
Statement by its `Sid` if one was provided.

```typescript
const statement = policy.getStatement("MyFancySID");
```

Let us test if the S3 Bucket Policy grants admin rights for administrators by checking if the Policy contains the Statement "*Allow access for Bucket Administrators*".

```typescript
import {expect} from "chai";
import "./mocks";
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import {PolicyDocument, Statement, AnonymousUserPrincipal} from "@thinkinglabs/aws-iam-policy";

describe("S3 Bucket Policy", function() {
  const accountId = "123456789012";
  const bucket = new aws.s3.Bucket("a-bucket", {});
  const adminRole = new aws.iam.Role("admin-role", {
    assumeRolePolicy: "aPolicy",
  });
  const userRole = new aws.iam.Role("user-role", {
    assumeRolePolicy: "aPolicy",
  });

  const doc = sut.createS3BucketPolicy(accountId, bucket, [adminRole], [userRole]);

  let policy: PolicyDocument;
  before(async () => {
    policy = PolicyDocument.fromJson(await get(doc) as string);
  });

  it("should allow access for Bucket Administrators", function() {
    const statement = policy.getStatement("Allow access for Bucket Administrators");
    expect(statement).to.deep.equal(new Statement({
      actions: [
        "s3:PutBucketPolicy",
        "s3:GetBucketPolicy*",
        "s3:DeleteBucketPolicy",
      ],
      effect: "Deny",
      principals: [new AnonymousUserPrincipal()],
      resources: ["a-bucket-arn"],
      conditions: {
        StringNotLike: {"aws:userId": ["123456789012", "admin-role-unique-id:*"]},
      },
      sid: "Allow access for Bucket Administrators",
    }));
  });

});
```

The test needs some fake IAM Roles. This is achieved by including a `mocks` module.

```typescript
import * as pulumi from '@pulumi/pulumi';

pulumi.runtime.setMocks({
  newResource: function(args: pulumi.runtime.MockResourceArgs): { id: string, state: Record<string, any>} {
    const defaultState = {
      arn: `${args.name}-arn`,
      name: args.name,
      ...args.inputs,
    };
    switch (args.type) {
      case 'aws:iam/role:Role':
        defaultState['uniqueId'] = `${args.name}-unique-id`;
        break;
      default:
        break;
    }

    const resourceId = args.id?.trim() ? args.id : `${args.name}-id`;

    return {id: resourceId, state: defaultState};
  },
  call: function(args: pulumi.runtime.MockCallArgs) {
    switch (args.token) {
    }
    return args.inputs;
  },
});
```

## Ideas for future improvements

At the moment, `Condition` accepts any JSON object. Valid or not, it will serialize the object to JSON as-is. To avoid building an invalid `Condition` element, I am planning to add an object model for this. The API would look something like this.

```typescript
new Statement({
  effect: "Deny",
  ...
  conditions: [
    new Condition("StringNotLike", "aws:userId", ["userId1", "userId2", ...]),
  ]
})
```

I am also planning to add validation for `Sid`s. According to the AWS IAM documentation, a `Sid` only accepts alphanumerical characters `[a-zA-Z0-9]`. But I see that resource-based Policies for some services accept spaces for `Sid`s. AWS does not document this. Although the documentation for [S3 Bucket Policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html#example-bucket-policies-use-case-4) and [KMS Key Policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default) clearly show examples with spaces for `Sid`s.

The library does not support `NotPrincipal`, `NotAction`, and `NotResource`
because I did not need them at the time. At some point, I will add support for
that too.

## Conclusion

As you can see, you can extend a Pulumi program with existing Node modules or write your own. By testing IAM policies before deployment, we can avoid errors before deployments and provide guardrails for developers.
