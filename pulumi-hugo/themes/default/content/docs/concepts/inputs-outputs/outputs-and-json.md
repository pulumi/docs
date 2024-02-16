---
title_tag: "Working with Outputs and JSON | Inputs and Outputs"
meta_desc: "Learn more about outputs and how to use them with JSON objects in Pulumi."
title: Outputs & JSON
h1: Working with outputs and JSON
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    weight: 6
    parent: inputs-outputs
---

Often in the course of working with web technologies, you encounter JavaScript Object Notation (JSON) which is a popular specification for representing data. In many scenarios, you'll need to embed resource outputs into a JSON string. In these scenarios, you need to first _wait for the returned_ output, _then_ build the JSON string:

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
const contentBucket = new aws.s3.Bucket("content-bucket", {
  acl: "private",
  website: {
    indexDocument: "index.html",
    errorDocument: "index.html",
  },
  forceDestroy: true,
});

const originAccessIdentity = new aws.cloudfront.OriginAccessIdentity(
  "cloudfront",
  {
    comment: pulumi.interpolate`OAI-${contentBucket.bucketDomainName}`,
  }
);

// apply method
new aws.s3.BucketPolicy("cloudfront-bucket-policy", {
  bucket: contentBucket.bucket,
  policy: pulumi
    .all([contentBucket.bucket, originAccessIdentity.iamArn])
    .apply(([bucketName, iamArn]) =>
      JSON.stringify({
        Version: "2012-10-17",
        Statement: [
          {
            Sid: "CloudfrontAllow",
            Effect: "Allow",
            Principal: {
              AWS: iamArn,
            },
            Action: "s3:GetObject",
            Resource: `arn:aws:s3:::${bucketName}/*`,
          },
        ],
      })
    ),
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
bucket = aws.s3.Bucket(
    "content-bucket",
    acl="private",
    website=aws.s3.BucketWebsiteArgs(
        index_document="index.html", error_document="404.html"
    ),
)

origin_access_identity = aws.cloudfront.OriginAccessIdentity(
    "cloudfront",
    comment=pulumi.Output.concat("OAI-", bucket.id),
)

bucket_policy = aws.s3.BucketPolicy(
    "cloudfront-bucket-policy",
    bucket=bucket.bucket,
    policy=pulumi.Output.all(
        cloudfront_iam_arn=origin_access_identity.iam_arn,
        bucket_arn=bucket.arn
    ).apply(
        lambda args: json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "CloudfrontAllow",
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": args["cloudfront_iam_arn"],
                        },
                        "Action": "s3:GetObject",
                        "Resource": f"{args['bucket_arn']}/*",
                    }
                ],
            }
        )
    ),
    opts=pulumi.ResourceOptions(parent=bucket)
)
```

{{% /choosable %}}

{{% choosable language go %}}

{{% notes type="info" %}}
The Pulumi Go SDK does not currently support serializing or deserializing maps with unknown values.
It is tracked [here](https://github.com/pulumi/pulumi/issues/12460).

The following is a simplified example of using `pulumi.JSONMarshal` in Go.
{{% /notes %}}

```go
bucket, err := s3.NewBucket(ctx, "content-bucket", &s3.BucketArgs{
	Acl: pulumi.String("private"),
	Website: &s3.BucketWebsiteArgs{
		IndexDocument: pulumi.String("index.html"),
		ErrorDocument: pulumi.String("404.html"),
	},
})
if err != nil {
	return err
}

originAccessIdentity, err := cloudfront.NewOriginAccessIdentity(ctx, "cloudfront", &cloudfront.OriginAccessIdentityArgs{
		Comment: pulumi.Sprintf("OAI-%s", bucket.ID()),
})
if err != nil {
	return err
}

_, err = s3.NewBucketPolicy(ctx, "cloudfront-bucket-policy", &s3.BucketPolicyArgs{
	Bucket: bucket.ID(),
	Policy: pulumi.All(bucket.Arn, originAccessIdentity.IamArn).ApplyT(
		func(args []interface{}) (pulumi.StringOutput, error) {
			bucketArn := args[0].(string)
			iamArn := args[1].(string)

			policy, err := json.Marshal(map[string]interface{}{
				"Version": "2012-10-17",
				"Statement": []map[string]interface{}{
					{
						"Sid":    "CloudfrontAllow",
						"Effect": "Allow",
						"Principal": map[string]interface{}{
							"AWS": iamArn,
						},
						"Action":   "s3:GetObject",
						"Resource": bucketArn + "/*",
					},
				},
			})

			if err != nil {
				return pulumi.StringOutput{}, err
			}
			return pulumi.String(policy).ToStringOutput(), nil
		}).(pulumi.StringOutput),
}, pulumi.Parent(bucket))
if err != nil {
	return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var bucket = new Bucket("content-bucket", new BucketArgs
{
    Acl = "private",
    Website = new BucketWebsiteArgs
    {
        IndexDocument = "index.html",
        ErrorDocument = "404.html",
    },
});

var originAccessIdentity = new OriginAccessIdentity("cloudfront", new OriginAccessIdentityArgs
{
    Comment = Output.Format($"OAI-{bucket.Id}"),
});

var bucketPolicy = new BucketPolicy("cloudfront-bucket-policy", new BucketPolicyArgs
{
    Bucket = bucket.Bucket,
    Policy = Output.Tuple(bucket.Arn, originAccessIdentity.IamArn)
    .Apply(t =>
    {
        string bucketArn = t.Item1;
        string cloudfrontIamArn = t.Item2;

        var policy = new
        {
            Version = "2012-10-17",
            Statement = new object[]
            {
                new
                {
                    Sid = "CloudfrontAllow",
                    Effect = "Allow",
                    Principal = new { AWS = cloudfrontIamArn },
                    Action = "s3:GetObject",
                    Resource = $"{bucketArn}/*",
                },
            },
        };

        return JsonSerializer.Serialize(policy);
    }),
}, new CustomResourceOptions { Parent = bucket });
```

{{% /choosable %}}

{{< /chooser >}}

This operation is so common, Pulumi provides first-class helper functions for deserializing JSON string outputs into your language's native objects and serializing your language's native objects to JSON string outputs. These helper functions are designed to remove the process of manually resolving the output inside a {{< pulumi-apply >}}.

### Converting Outputs to JSON

You can natively represent the definition of an AWS Step Function State Machine and embed outputs from other resources then convert it to a JSON string.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const stateMachine = new awsnative.stepfunctions.StateMachine("stateMachine", {
    roleArn: sfnRole.arn,
    stateMachineType: "EXPRESS",
    definitionString: pulumi.jsonStringify({
        "Comment": "A Hello World example of the Amazon States Language using two AWS Lambda Functions",
        "StartAt": "Hello",
        "States": {
            "Hello": {
                "Type": "Task",
                "Resource": helloFunction.arn, // Pulumi Resource Output
                "Next": "World",
            },
            "World": {
                "Type": "Task",
                "Resource": worldFunction.arn, // Pulumi Resource Output
                "End": true,
            },
        },
    })
});
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
const stateMachine = new awsnative.stepfunctions.StateMachine("stateMachine", {
    roleArn: sfnRole.arn,
    stateMachineType: "EXPRESS",
    definitionString: pulumi.jsonStringify({
        "Comment": "A Hello World example of the Amazon States Language using two AWS Lambda Functions",
        "StartAt": "Hello",
        "States": {
            "Hello": {
                "Type": "Task",
                "Resource": helloFunction.arn, // Pulumi Resource Output
                "Next": "World",
            },
            "World": {
                "Type": "Task",
                "Resource": worldFunction.arn, // Pulumi Resource Output
                "End": true,
            },
        },
    })
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
state_machine = aws_native.stepfunctions.StateMachine("stateMachine",
    role_arn=sfn_role.arn,
    state_machine_type="EXPRESS",
    definition_string=pulumi.Output.json_dumps({
        "Comment": "A Hello World example of the Amazon States Language using two AWS Lambda Functions",
        "StartAt": "Hello",
        "States": {
            "Hello": {
                "Type": "Task",
                "Resource": hello_function.arn, # Pulumi Resource Output
                "Next": "World",
            },
            "World": {
                "Type": "Task",
                "Resource": world_function.arn, # Pulumi Resource Output
                "End": True,
            },
        },
    })
)
```

{{% /choosable %}}

{{% choosable language go %}}

{{% notes type="info" %}}
The Pulumi Go SDK does not currently support serializing or deserializing maps with unknown values.
It is tracked [here](https://github.com/pulumi/pulumi/issues/12460).

The following is a simplified example of using `pulumi.JSONMarshal` in Go.
{{% /notes %}}

```go
pulumi.JSONMarshal(pulumi.ToMapOutput(map[string]pulumi.Output{
    "bool": pulumi.ToOutput(true),
    "int":  pulumi.ToOutput(1),
    "str":  pulumi.ToOutput("hello"),
    "arr": pulumi.ToArrayOutput([]pulumi.Output{
        pulumi.ToOutput(false),
        pulumi.ToOutput(1.0),
        pulumi.ToOutput(""),
        pulumi.ToMapOutput(map[string]pulumi.Output{
            "key": pulumi.ToOutput("value"),
        }),
    }),
    "map": pulumi.ToMapOutput(map[string]pulumi.Output{
        "key": pulumi.ToOutput("value"),
    }),
    // The following functionality is currently unsupported as myResource
    // is an unknown value.
    "unknown": myResource.ApplyT(func(res interface{}) (interface{}, error) {
        return "Hello World!", nil
    }),
}))
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var stateMachine = Pulumi.Output.JsonSerialize(Output.Create(new {
        Comment = "A Hello World example of the Amazon States Language using two AWS Lambda Functions",
        StartAt = "Hello",
        States = new Dictionary<string, object?>{
        ["Hello"] = new {
            Type = "Task",
            Resource = helloFunction.Arn, // Pulumi Resource Output
            Next = "World",
        },
        ["World"] = new {
            Type = "Task",
            Resource = worldFunction.Arn, // Pulumi Resource Output
            End = true,
        },
    },
}));
```

{{% /choosable %}}

{{< /chooser >}}

### Parsing JSON Outputs to Objects

You can parse a JSON string into an object and then, inside of an Apply, manipulate the object to remove all of the policy statements.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const jsonIAMPolicy = pulumi.output(`{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::my-bucket"
        }
    ]
}`);

const policyWithNoStatements = pulumi.jsonParse(jsonIAMPolicy).apply(policy => {
    // delete the policy statements
    policy.Statement = [];
    return policy;
});
```

For more details [view the NodeJS documentation](/docs/reference/pkg/nodejs/pulumi/pulumi/).

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
const jsonIAMPolicy = pulumi.output(`{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::my-bucket"
        }
    ]
}`);

const policyWithNoStatements: Output<object> = pulumi.jsonParse(jsonIAMPolicy).apply(policy => {
    // delete the policy statements
    policy.Statement = [];
    return policy;
});
```

For more details [view the NodeJS documentation](/docs/reference/pkg/nodejs/pulumi/pulumi/).

{{% /choosable %}}

{{% choosable language python %}}

```python
json_iam_policy = pulumi.Output.from_input('''
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::my-bucket"
        }
    ]
}
''')

def update_policy(policy):
    # delete the policy statements
    policy.update({'Statement': []})
    return policy

policy_with_no_statements = \
    pulumi.Output.json_loads(json_IAM_policy).apply(update_policy)
```

For more details [view the Python documentation](/docs/reference/pkg/python/pulumi/).

{{% /choosable %}}

{{% choosable language go %}}

```go
jsonIAMPolicy := pulumi.ToOutput(`{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::my-bucket"
        }
    ]
}`).(pulumi.StringInput)

policyWithNoStatements := pulumi.JSONUnmarshal(jsonIAMPolicy).ApplyT(
    func(v interface{}) (interface{}, error) {

        // delete the policy statements
        v.(map[string]interface{})["Statement"] = []pulumi.ArrayOutput{}
        return v, nil
    })
```

For more details [view the Go documentation](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi).

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var jsonIAMPolicy = Output.Create(@"
        {
            ""Version"": ""2012-10-17"",
            ""Statement"": [
                {
                    ""Sid"": ""VisualEditor0"",
                    ""Effect"": ""Allow"",
                    ""Action"": [
                        ""s3:ListAllMyBuckets"",
                        ""s3:GetBucketLocation""
                    ],
                    ""Resource"": ""*""
                },
                {
                    ""Sid"": ""VisualEditor1"",
                    ""Effect"": ""Allow"",
                    ""Action"": [
                        ""s3:*""
                    ],
                    ""Resource"": ""arn:aws:s3:::my-bucket""
                }
            ]
        }
    ");

var policyWithNoStatements = Pulumi.Output.JsonDeserialize<IAMPolicy>(jsonIAMPolicy).Apply(policy =>
{
    // delete the policy statements.
    policy.Statement = Pulumi.Output.Create(new List<StatementEntry> { });
    return policy;
})
```

For more details [view the .NET documentation](/docs/reference/pkg/dotnet/Pulumi/Pulumi.Output.html).

{{% /choosable %}}

{{< /chooser >}}
