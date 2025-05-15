---
title: "Secure AWS Lambda with IAM ABAC Policies"
date: 2022-07-19
updated: 2025-03-26
meta_desc: "Learn how to implement Attribute-Based Access Control (ABAC) for AWS Lambda using Pulumi. Secure deployments with IAM role tags and policy conditions."
meta_image: meta.png
authors:
- paul-stack
- lee-briggs
- isaac-harris
tags:
- aws
- lambda
- iam
- serverless
---

Event-driven, serverless functions have become a defining feature of many modern cloud architectures. With recent
capabilities such as [AWS Lambda URLs](https://www.pulumi.com/blog/lambda-urls-launch/) and
[AWS Lambda Containers](https://www.pulumi.com/blog/aws-lambda-container-support/), AWS has made it clear that Lambda
Functions are a platform that teams can use to deliver increasingly sophisticated services without worrying about
managing underlying compute resources.

Today, AWS announced another advancement for their Lambda Functions platform: [Attribute-Based Access Control
(ABAC)](https://aws.amazon.com/blogs/compute/scaling-aws-lambda-permissions-with-attribute-based-access-control-abac/). At its core, ABAC support brings more granular permissions that are automatically applied based on IAM role tags,
Lambda tags, or both. This update builds on well-established Role-Based Access Control (RBAC) principles while making it
possible to implement granular controls without permissions updates for every new user and resource.

## What are Attributes?

Attributes are a key or key/value pair - in AWS, these attributes are called tags. Tags can be applied to multiple
roles – for example identifying members of a team.

Across many teams, your organization may share a lot of common roles, and, in order to enforce the principle of least access,
you may wish to restrict access across teams such that Developer Team members cannot access Ops Team resources and vice versa.

## Using ABAC for AWS Lambda Functions

For this example, we’ll define a new role 'abac-test' as well as a team attribute that must have the value of either
'developers' or 'ops' to enable creating a Lambda function.

![Diagram showing AWS IAM Role permissions controlled by attributes. An AWS Lambda function tries to create a Lambda Role, which is allowed or denied based on IAM policy conditions tied to role tags. Access is granted to roles tagged as “developers” or “ops,” and denied to “sith_lords.”](./figure1.png)

To get started, let's first install the Pulumi AWS provider:

{{< chooser language "typescript,csharp,python,go" >}}
{{% choosable language typescript %}}

```bash
$ npm install @pulumi/aws
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ dotnet add package Pulumi.Aws
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
$ pip3 install pulumi_aws
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
$ go get github.com/pulumi/pulumi-aws/sdk/v5
```

{{% /choosable %}}
{{< /chooser >}}

Now, create a new IAM Role that a user can assume:

{{< chooser language "typescript,csharp,python,go,yaml" >}}
{{% choosable language typescript %}}

```typescript
const role = new aws.iam.Role("abac-test", {
    assumeRolePolicy: JSON.stringify({
        Version: "2012-10-17",
        Statement: [
            {
                Sid: "",
                Effect: "Allow",
                Principal: {
                    AWS: "arn:aws:iam::MYACCOUNTID:root",
                },
                Action: "sts:AssumeRole",
            },
        ],
    }),
});
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var role = new Aws.Iam.Role("abac-test", new Aws.Iam.RoleArgs
{
    AssumeRolePolicy = JsonSerializer.Serialize(new Dictionary<string, object?>
    {
        { "Version", "2012-10-17" },
        { "Statement", new[]
            {
                new Dictionary<string, object?>
                {
                    { "Action", "sts:AssumeRole" },
                    { "Effect", "Allow" },
                    { "Principal", new Dictionary<string, object?>
                    {
                        { "AWS", "arn:aws:iam::MYACCOUNTID:root" },
                    } },
                },
            }
         },
    }),
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
role = aws.iam.Role("abac-test",
                    assume_role_policy=json.dumps({
                        "Version": "2012-10-17",
                        "Statement": [{
                            "Action": "sts:AssumeRole",
                            "Effect": "Allow",
                            "Principal": {
                                "AWS": "arn:aws:iam::MYACCOUNTID:root",
                            },
                        }],
                    }),
                    tags={
                        "Team": "developers",
                    })
```

{{% /choosable %}}
{{% choosable language go %}}

```go
role, err := iam.NewRole(ctx, "abac-test", &iam.RoleArgs{
  AssumeRolePolicy: pulumi.String(`{
    "Version": "2012-10-17",
    "Statement": [{
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::MYACCOUNTID:root"
      },
      "Action": "sts:AssumeRole"
    }]
  }`),
})
if err != nil {
  return err
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
  abacTest:
      type: aws:iam:Role
      properties:
          assumeRolePolicy:
              Fn::ToJSON:
                  Version: 2012-10-17
                  Statement:
                      - Action: sts:AssumeRole
                        Effect: Allow
                        Principal:
                            AWS: arn:aws:iam::MYACCOUNTID:root
```

{{% /choosable %}}
{{< /chooser >}}

Let's now create a new IAM Policy that allows a user to create Lambda functions:

{{< chooser language "typescript,csharp,python,go,yaml" >}}
{{% choosable language typescript %}}

```typescript
const createPolicy = new aws.iam.Policy(
    "createLambda",
    {
        policy: JSON.stringify({
            Version: "2012-10-17",
            Statement: [
                {
                    Effect: "Allow",
                    Action: ["lambda:CreateFunction", "lambda:TagResource"],
                    Resource: "arn:aws:lambda:*:*:function:*",
                    Condition: {
                        // the requesting resource must have a tag with
                        // team = developers/ops
                        StringEquals: {
                            "aws:RequestTag/Team": ["developers", "ops"], // must match
                        },
                        // your request must contain these tags
                        // eg. project, but you might not have this defined yet
                        "ForAllValues:StringEquals": {
                            "aws:TagKeys": "Team", // must exist
                        },
                    },
                },
                {
                    // Pulumi needs to check what functions exist and what versions exist to create updates and new versions
                    Effect: "Allow",
                    Action: [
                        "lambda:GetFunction",
                        "lambda:ListVersionsByFunction",
                        "lambda:GetFunctionCodeSigningConfig",
                    ],
                    Resource: "*",
                },
                {
                    Effect: "Allow",
                    // These are assume role policies
                    Action: ["iam:ListRoles", "iam:PassRole"],
                    Resource: "*",
                },
            ],
        }),
    },
);
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var createPolicy = new Aws.Iam.Policy("createPolicy", new Aws.Iam.PolicyArgs
{
    PolicyDocument = JsonSerializer.Serialize(new Dictionary<string, object?>
    {
        { "Version", "2012-10-17" },
        { "Statement", new[]
            {
                new Dictionary<string, object?>
                {
                    { "Effect", "Allow" },
                    { "Action", new[]
                        {
                            "lambda:CreateFunction",
                            "lambda:TagResource",
                        }
                     },
                    { "Resource", "arn:aws:lambda:*:*:function:*" },
                    { "Condition", new Dictionary<string, object?>
                    {
                        // the requesting resource must have a tag with
                        // team = developers/ops
                        { "StringEquals", new Dictionary<string, object?>
                        {
                            { "aws:RequestTag/Team", new[]
                                {
                                    "developers",
                                    "ops",
                                }
                             },
                        } },
                        // your request must contain these tags
                        // eg. project, but you might not have this defined yet
                        { "ForAllValues:StringEquals", new Dictionary<string, object?>
                        {
                            { "aws:TagKeys", new[]
                                {
                                    "Team",
                                }
                             },
                        } },
                    } },
                },
                new Dictionary<string, object?>
                {
                    // Pulumi needs to check what functions exist and what versions exist to create updates and new versions
                    { "Effect", "Allow" },
                    { "Action", new[]
                        {
                            "lambda:GetFunction",
                            "lambda:ListVersionsByFunction",
                            "lambda:GetFunctionCodeSigningConfig",
                        }
                     },
                    { "Resource", "*" },
                },
                new Dictionary<string, object?>
                {
                    // These are assume role policies
                    { "Effect", "Allow" },
                    { "Action", new[]
                        {
                            "iam:ListRoles",
                            "iam:PassRole",
                        }
                     },
                    { "Resource", "*" },
                },
            }
         },
    }),
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
create_policy = aws.iam.Policy("createPolicy", policy=json.dumps({
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "lambda:CreateFunction",
                "lambda:TagResource",
            ],
            "Resource": "arn:aws:lambda:*:*:function:*",
            "Condition": {
                #the requesting resource must have a tag with
                #team = developers/ops
                "StringEquals": {
                    "aws:RequestTag/Team": [
                        "developers",
                        "ops",
                    ],
                },
                # your request must contain these tags
                # eg. project, but you might not have this defined yet
                "ForAllValues:StringEquals": {
                    "aws:TagKeys": ["Team"],
                },
            },
        },
        {
            # Pulumi needs to check what functions exist and what versions exist to create updates and new versions
            "Effect": "Allow",
            "Action": [
                "lambda:GetFunction",
                "lambda:ListVersionsByFunction",
                "lambda:GetFunctionCodeSigningConfig",
            ],
            "Resource": "*",
        },
        {
            # These are assume role policies
            "Effect": "Allow",
            "Action": [
                "iam:ListRoles",
                "iam:PassRole",
            ],
            "Resource": "*",
        },
    ],
}))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
createPolicy, err := iam.NewRolePolicy(ctx, "createPolicy", &iam.RoleArgs{
  Policy: pulumi.String(`{
    "Version": "2012-10-17",
    "Statement": [{
      "Sid": "",
      "Effect": "Allow",
      "Condition": map[string]interface{}{
        "StringEquals": map[string]interface{}{
          "aws:RequestTag/Team": []string{
            "developers",
            "ops",
          },
        },
        "ForAllValues:StringEquals": map[string]interface{}{
          "aws:TagKeys": []string{
            "Team",
          },
        },
      },
      "Resource": "arn:aws:lambda:*:*:function:*",
      "Action": []string{
        "lambda:CreateFunction",
        "lambda:TagResource",
      },
    },
    {
      "Effect": "Allow",
      "Resource": "*",
      "Action": []string{
        "lambda:GetFunction",
        "lambda:ListVersionsByFunction",
        "lambda:GetFunctionCodeSigningConfig",
      },
    },
    {
      {
        "Effect": "Allow",
        "Resource": "*",
        "Action": []string{
          "lambda:CreateFunction",
          "lambda:TagResource",
        },
      }
    }]
  }`),
})
if err != nil {
  return err
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
  createPolicy:
    type: aws:iam:Policy
    properties:
      policy:
        Fn::ToJSON:
          Version: 2012-10-17
          Statement:
            - Effect: Allow
              Action:
                - lambda:CreateFunction
                - lambda:TagResource
              Resource: 'arn:aws:lambda:*:*:function:*'
              Condition:
                StringEquals:
                  aws:RequestTag/Team:
                    - developers
                    - ops
                ForAllValues:StringEquals:
                  aws:TagKeys:
                    - Team
            - Effect: Allow
              Action:
                - lambda:GetFunction
                - lambda:ListVersionsByFunction
                - lambda:GetFunctionCodeSigningConfig
              Resource: '*'
            - Effect: Allow
              Action:
                - iam:ListRoles
                - iam:PassRole
              Resource: '*'
```

{{% /choosable %}}
{{< /chooser >}}

Notice, as part of the policy condition, we ensure that the requesting resource must have a tag with `team: developers` or `team: ops`.

Let's ensure that this policy is attached to the Role we initially created:

{{< chooser language "typescript,csharp,python,go,yaml" >}}
{{% choosable language typescript %}}

```typescript
const rpa = new aws.iam.RolePolicyAttachment("rpa", {
    policyArn: createPolicy.arn,
    role: role,
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var rpa = new Aws.Iam.RolePolicyAttachment("rpa", new Aws.Iam.RolePolicyAttachmentArgs
{
    PolicyArn = createPolicy.Arn,
    Role = role.Name,
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
rpa = aws.iam.RolePolicyAttachment("rpa",
    policy_arn=create_policy.arn,
    role=role.name)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
rpa, err := iam.NewRolePolicyAttachment(ctx, "rpa", &iam.RolePolicyAttachmentArgs{
    PolicyArn: createPolicy.Arn,
    Role:      role.Name,
})
if err != nil {
    return err
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
  rpa:
    type: aws:iam:RolePolicyAttachment
    properties:
      policyArn: ${createPolicy.arn}
      role: ${abacTest.name}
```

{{% /choosable %}}
{{< /chooser >}}

We can deploy these resources using the command `pulumi update`:

```bash
pulumi up
Previewing update (abac-testing)

View Live: https://app.pulumi.com/stack72/aws-abac-test/abac-testing/previews/c6fb4580-2706-47ee-8a56-b8942631254e

     Type                             Name                        Plan
 +   pulumi:pulumi:Stack              aws-abac-test-abac-testing  create
 +   ├─ aws:iam:Policy                createLambda                create
 +   ├─ aws:iam:Role                  abac-test                   create
 +   └─ aws:iam:RolePolicyAttachment  createPolicy                create

Resources:
    + 4 to create

Do you want to perform this update? yes
Updating (abac-testing)

View Live: https://app.pulumi.com/stack72/aws-abac-test/abac-testing/updates/1

     Type                             Name                        Status
 +   pulumi:pulumi:Stack              aws-abac-test-abac-testing  created
 +   ├─ aws:iam:Role                  abac-test                   created
 +   ├─ aws:iam:Policy                createLambda                created
 +   └─ aws:iam:RolePolicyAttachment  createPolicy                created

Resources:
    + 4 created

Duration: 7s
```

For the purposes of testing, we are now going to create a specific [AWS Provider resource](https://www.pulumi.com/docs/concepts/resources/providers/) that we can pass the IAM Role details to assume.

{{< chooser language "typescript,csharp,python,go,yaml" >}}
{{% choosable language typescript %}}

```typescript
const abacUserProvider = new aws.Provider(
    "assumeRole",
    {
        // assume the previously created role with the ABAC configured policy into our provider
        assumeRole: {
            roleArn: role.arn,
            sessionName: "abacTesting",
        },
        region: "us-east-1",
    },
    {
        // we want to depend on the role policy attachment being in place before we create the provider
        dependsOn: [rpa],
    }
);
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var abacUserProvider = new Aws.Provider("abacUserProvider", new Aws.ProviderArgs
{
    AssumeRole = new Aws.Config.Inputs.AssumeRoleArgs
    {
        RoleArn = role.Arn,
        SessionName = "abacTesting",
    },
    Region = "us-east-1",
}, new CustomResourceOptions
{
    DependsOn =
    {
        rpa,
    },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
abac_user_provider = pulumi.providers.Aws("abacUserProvider",
    assume_role=aws.config.AssumeRoleArgs(
        role_arn=role.arn,
        session_name="abacTesting",
    ),
    region="us-east-1",
    opts=pulumi.ResourceOptions(depends_on=[rpa]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
abacUserProvider, err := providers.Newaws(ctx, "abacUserProvider", &providers.awsArgs{
    AssumeRole: config.AssumeRole{
        RoleArn:     role.Arn,
        SessionName: "abacTesting",
    },
    Region: "us-east-1",
}, pulumi.DependsOn([]pulumi.Resource{
    rpa,
}))
if err != nil {
    return err
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
  abacUserProvider:
    type: pulumi:providers:aws
    properties:
      assumeRole:
        roleArn: ${role.arn}
        sessionName: "abacTesting"
      region: "us-east-1"
    options:
      dependsOn:
        - ${rpa}
```

{{% /choosable %}}
{{< /chooser >}}

Now we can create an AWS Lambda with Pulumi as follows:

{{< chooser language "typescript,csharp,python,go,yaml" >}}
{{% choosable language typescript %}}

```typescript
const lambdaRole = new aws.iam.Role("iamRole", {
    assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({
        Service: "lambda.amazonaws.com",
    }),
});

const deleteLambdaPolicy = new aws.iam.Policy(
    "deleteLambdaPolicy",
    {
        policy: JSON.stringify({
            Version: "2012-10-17",
            Statement: [
                {
                    Effect: "Allow",
                    Action: ["lambda:DeleteFunction"],
                    Resource: "*",
                },
            ],
        }),
    },
    { parent: lambdaRole }
);

new aws.iam.RolePolicyAttachment(
    `deletePolicy`,
    {
        policyArn: deletePolicy.arn,
        role: role,
    },
    { parent: deletePolicy })

const lambda = new aws.lambda.Function(
    "lambdaFunction",
    {
        code: new pulumi.asset.AssetArchive({
            ".": new pulumi.asset.FileArchive("./app"),
        }),
        runtime: "nodejs12.x",
        role: lambdaRole.arn,
        handler: "index.handler",
    },
    { provider: abacUserProvider }
);
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var lambdaRole = new Aws.Iam.Role("lambdaRole", new Aws.Iam.RoleArgs
{
    AssumeRolePolicy = JsonSerializer.Serialize(new Dictionary<string, object?>
    {
        { "Version", "2012-10-17" },
        { "Statement", new[]
            {
                new Dictionary<string, object?>
                {
                    { "Action", "sts:AssumeRole" },
                    { "Effect", "Allow" },
                    { "Principal", new Dictionary<string, object?>
                    {
                        { "Service", "lambda.amazonaws.com" },
                    } },
                },
            }
         },
    }),
});
var deletePolicy = new Aws.Iam.Policy("deletePolicy", new Aws.Iam.PolicyArgs
{
    PolicyDocument = JsonSerializer.Serialize(new Dictionary<string, object?>
    {
        { "Version", "2012-10-17" },
        { "Statement", new[]
            {
                new Dictionary<string, object?>
                {
                    { "Action", "lambda:DeleteFunction" },
                    { "Effect", "Allow" },
                    { "Resource", "*" },
                },
            }
         },
    }),
});
var deletePolicyAttachment = new Aws.Iam.RolePolicyAttachment("deletePolicyAttachment", new Aws.Iam.RolePolicyAttachmentArgs
{
    Role = role.Name,
    PolicyArn = deletePolicy.Arn,
});
var lambdaFunction = new Aws.Lambda.Function("lambdaFunction", new Aws.Lambda.FunctionArgs
{
    Code = new FileArchive("./app"),
    Role = lambdaRole.Arn,
    Handler = "index.handler",
    Runtime = "nodejs14.x",
}, new CustomResourceOptions
{
    Provider = abacUserProvider,
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
lambda_role = aws.iam.Role("lambdaRole", assume_role_policy=json.dumps({
    "Version": "2012-10-17",
    "Statement": [{
        "Action": "sts:AssumeRole",
        "Effect": "Allow",
        "Principal": {
            "Service": "lambda.amazonaws.com",
        },
    }],
}))
delete_policy = aws.iam.Policy("deletePolicy", policy=json.dumps({
    "Version": "2012-10-17",
    "Statement": [{
        "Action": "lambda:DeleteFunction",
        "Effect": "Allow",
        "Resource": "*",
    }],
}))
delete_policy_attachment = aws.iam.RolePolicyAttachment("deletePolicyAttachment",
    role=role.name,
    policy_arn=delete_policy.arn)
lambda_function = aws.lambda_.Function("lambdaFunction",
    code=pulumi.FileArchive("./app"),
    role=lambda_role.arn,
    handler="index.handler",
    runtime="nodejs14.x",
    opts=pulumi.ResourceOptions(provider=abac_user_provider))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
lambdaRole, err := iam.NewRole(ctx, "lambdaRole", &iam.RoleArgs{
  AssumeRolePolicy: pulumi.String(`{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }]
  }`),
})
if err != nil {
  return err
}

deletePolicy, err := iam.NewRolePolicy(ctx, "deletePoicy", &iam.RoleArgs{
  Policy: pulumi.String(`{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Resource": "*",
      "Action": []string{
        "lambda:DeleteFunction",
      },
    }]
  }`),
})
if err != nil {
  return err
}

_, err = iam.NewRolePolicyAttachment(ctx, "deletePolicyAttachment", &iam.RolePolicyAttachmentArgs{
  Role:      role.Name,
  PolicyArn: deletePolicy.Arn,
})
if err != nil {
  return err
}

_, err = lambda.NewFunction(ctx, "lambdaFunction", &lambda.FunctionArgs{
  Code:    pulumi.NewFileArchive("./app"),
  Role:    lambdaRole.Arn,
  Handler: pulumi.String("index.handler"),
  Runtime: pulumi.String("nodejs14.x"),
}, pulumi.Provider(abacUserProvider))
if err != nil {
  return err
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
  lambdaRole:
    type: aws:iam:Role
    properties:
      assumeRolePolicy:
        Fn::ToJSON:
          Version: 2012-10-17
          Statement:
            - Action: sts:AssumeRole
              Effect: Allow
              Principal:
                Service: lambda.amazonaws.com
  deletePolicy:
    type: aws:iam:Policy
    properties:
      policy:
        Fn::ToJSON:
          Version: 2012-10-17
          Statement:
            - Action: lambda:DeleteFunction
              Effect: Allow
              Resource: '*'
  deletePolicyAttachment:
    type: aws:iam:RolePolicyAttachment
    properties:
      role: ${abacRole.name}
      policyArn: ${deletePolicy.arn}
  lambdaFunction:
    type: aws:lambda:Function
    properties:
      code:
        Fn::FileArchive: ./app
      role: ${lambdaRole.arn}
      handler: index.handler
      runtime: nodejs14.x
```

{{% /choosable %}}
{{< /chooser >}}

If we try and deploy the lambda, we will get the following using the role we are going to assume then we will get an error
as the lambda function has no `Team` tag.

```bash
pulumi up
Previewing update (abac-testing)

View Live: https://app.pulumi.com/stack72/aws-abac-test/abac-testing/previews/7fdc10b2-5e44-497e-a067-f2e8b257496c

     Type                                   Name                        Plan
     pulumi:pulumi:Stack                    aws-abac-test-abac-testing
 +   ├─ aws:iam:Role                        iamRole                     create
     ├─ aws:iam:Role                        abac-test
 +   │  └─ aws:iam:Policy                   deletePolicy                create
 +   │     └─ aws:iam:RolePolicyAttachment  deletePolicy                create
 +   ├─ pulumi:providers:aws                assumeRole                  create
 +   └─ aws:lambda:Function                 lambdaFunction              create

Resources:
    + 5 to create
    4 unchanged

Do you want to perform this update? yes
Updating (abac-testing)

View Live: https://app.pulumi.com/stack72/aws-abac-test/abac-testing/updates/2

     Type                                   Name                        Status                  Info
     pulumi:pulumi:Stack                    aws-abac-test-abac-testing  **failed**              1 error
 +   ├─ aws:iam:Role                        iamRole                     created
     ├─ aws:iam:Role                        abac-test
 +   │  └─ aws:iam:Policy                   deletePolicy                created
 +   │     └─ aws:iam:RolePolicyAttachment  deletePolicy                created
 +   ├─ pulumi:providers:aws                assumeRole                  created
 +   └─ aws:lambda:Function                 lambdaFunction              **creating failed**     1 error

Diagnostics:
  pulumi:pulumi:Stack (aws-abac-test-abac-testing):
    error: update failed

  aws:lambda:Function (lambdaFunction):
    error: 1 error occurred:
    	* error creating Lambda Function (1): AccessDeniedException:
    	status code: 403, request id: 4a8676f2-2b68-4d42-ad4b-f0e10ca31afd

Resources:
    + 4 created
    4 unchanged

Duration: 6s
```

If we add the correct `Team` tag to the Lambda function then the deploy will proceed as expected:

```bash
pulumi up
Previewing update (abac-testing)

View Live: https://app.pulumi.com/stack72/aws-abac-test/abac-testing/previews/0afa267f-5f9f-43f5-9e00-d3ee19dbf2b8

     Type                    Name                        Plan
     pulumi:pulumi:Stack     aws-abac-test-abac-testing
 +   └─ aws:lambda:Function  lambdaFunction              create

Resources:
    + 1 to create
    8 unchanged

Do you want to perform this update? yes
Updating (abac-testing)

View Live: https://app.pulumi.com/stack72/aws-abac-test/abac-testing/updates/3

     Type                    Name                        Status
     pulumi:pulumi:Stack     aws-abac-test-abac-testing
 +   └─ aws:lambda:Function  lambdaFunction              created

Resources:
    + 1 created
    8 unchanged

Duration: 9s
```

## Try It Out!

Lambda ABAC capabilities will help you to simplify governance by helping you to standardize roles and maintain security boundaries between teams. A common use case is using tags to restrict/enable the invoke action for a function in addition to the create action demonstrated above.
Give Lambda ABAC functionality a try and let us know what you think in [Community Slack](https://slack.pulumi.com).
