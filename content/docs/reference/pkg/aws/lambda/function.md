
---
title: "Function"
block_external_search_index: true
---

Provides a Lambda Function resource. Lambda allows you to trigger execution of code in response to events in AWS, enabling serverless backend solutions. The Lambda Function itself includes source code and runtime configuration.

For information about Lambda and how to use it, see [What is AWS Lambda?][1]

> **NOTE:** Due to [AWS Lambda improved VPC networking changes that began deploying in September 2019](https://aws.amazon.com/blogs/compute/announcing-improved-vpc-networking-for-aws-lambda-functions/), EC2 subnets and security groups associated with Lambda Functions can take up to 45 minutes to successfully delete.

## Example Usage

### Basic Example

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const iamForLambda = new aws.iam.Role("iam_for_lambda", {
    assumeRolePolicy: `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
`,
});
const testLambda = new aws.lambda.Function("test_lambda", {
    environment: {
        variables: {
            foo: "bar",
        },
    },
    code: new pulumi.asset.FileArchive("lambda_function_payload.zip"),
    handler: "exports.test",
    role: iamForLambda.arn,
    runtime: "nodejs12.x",
});
```

### Lambda Layers

> **NOTE:** The `aws.lambda.LayerVersion` attribute values for `arn` and `layer_arn` were swapped in version 2.0.0 of the this provider AWS Provider. For version 1.x, use `layer_arn` references. For version 2.x, use `arn` references.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleLayerVersion = new aws.lambda.LayerVersion("example", {});
const exampleFunction = new aws.lambda.Function("example", {
    // ... other configuration ...
    layers: [exampleLayerVersion.arn],
});
```

## CloudWatch Logging and Permissions

For more information about CloudWatch Logs for Lambda, see the [Lambda User Guide](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions-logs.html).

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// This is to optionally manage the CloudWatch Log Group for the Lambda Function.
// If skipping this resource configuration, also add "logs:CreateLogGroup" to the IAM policy below.
const example = new aws.cloudwatch.LogGroup("example", {
    retentionInDays: 14,
});
// See also the following AWS managed policy: AWSLambdaBasicExecutionRole
const lambdaLogging = new aws.iam.Policy("lambda_logging", {
    description: "IAM policy for logging from a lambda",
    path: "/",
    policy: `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*",
      "Effect": "Allow"
    }
  ]
}
`,
});
const lambdaLogs = new aws.iam.RolePolicyAttachment("lambda_logs", {
    policyArn: lambdaLogging.arn,
    role: aws_iam_role_iam_for_lambda.name,
});
const testLambda = new aws.lambda.Function("test_lambda", {}, { dependsOn: [example, lambdaLogs] });
```

## Specifying the Deployment Package

AWS Lambda expects source code to be provided as a deployment package whose structure varies depending on which `runtime` is in use.
See [Runtimes][6] for the valid values of `runtime`. The expected structure of the deployment package can be found in
[the AWS Lambda documentation for each runtime][8].

Once you have created your deployment package you can specify it either directly as a local file (using the `filename` argument) or
indirectly via Amazon S3 (using the `s3_bucket`, `s3_key` and `s3_object_version` arguments). When providing the deployment
package via S3 it may be useful to use the `aws.s3.BucketObject` resource to upload it.

For larger deployment packages it is recommended by Amazon to upload via S3, since the S3 API has better support for uploading
large files efficiently.

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_function.html.markdown.



## Create a Function Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#Function">Function</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#FunctionArgs">FunctionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Function</span><span class="p">(resource_name, opts=None, </span>code=None<span class="p">, </span>dead_letter_config=None<span class="p">, </span>description=None<span class="p">, </span>environment=None<span class="p">, </span>handler=None<span class="p">, </span>kms_key_arn=None<span class="p">, </span>layers=None<span class="p">, </span>memory_size=None<span class="p">, </span>name=None<span class="p">, </span>publish=None<span class="p">, </span>reserved_concurrent_executions=None<span class="p">, </span>role=None<span class="p">, </span>runtime=None<span class="p">, </span>s3_bucket=None<span class="p">, </span>s3_key=None<span class="p">, </span>s3_object_version=None<span class="p">, </span>source_code_hash=None<span class="p">, </span>tags=None<span class="p">, </span>timeout=None<span class="p">, </span>tracing_config=None<span class="p">, </span>vpc_config=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewFunction<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionArgs">FunctionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#Function">Function</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.Function.html">Function</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionArgs.html">FunctionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

#### Resource Arguments




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">Archive?</span>
    </dt>
    <dd>{{% md %}}The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dead<wbr>Letter<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiondeadletterconfig">Function<wbr>Dead<wbr>Letter<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Nested block to configure the function's *dead letter queue*. See details below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of what your Lambda Function does.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Environment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionenvironment">Function<wbr>Environment<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The Lambda environment's configuration settings. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Handler</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The function [entrypoint][3] in your code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ARN for the KMS encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Layers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Publish</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reserved<wbr>Concurrent<wbr>Executions</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}See [Runtimes][6] for valid values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The S3 key of an object containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Object<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The object version containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Code<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256("file.zip")` (this provider 0.11.12 and later) or `base64sha256(file("file.zip"))` (this provider 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tracing<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiontracingconfig">Function<wbr>Tracing<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionvpcconfig">Function<wbr>Vpc<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">pulumi.Archive</span>
    </dt>
    <dd>{{% md %}}The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dead<wbr>Letter<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiondeadletterconfig">*Function<wbr>Dead<wbr>Letter<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Nested block to configure the function's *dead letter queue*. See details below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of what your Lambda Function does.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Environment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionenvironment">*Function<wbr>Environment</a></span>
    </dt>
    <dd>{{% md %}}The Lambda environment's configuration settings. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Handler</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The function [entrypoint][3] in your code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ARN for the KMS encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Layers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A unique name for your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Publish</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reserved<wbr>Concurrent<wbr>Executions</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}See [Runtimes][6] for valid values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The S3 key of an object containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Object<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The object version containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Code<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256("file.zip")` (this provider 0.11.12 and later) or `base64sha256(file("file.zip"))` (this provider 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tracing<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiontracingconfig">*Function<wbr>Tracing<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionvpcconfig">*Function<wbr>Vpc<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">pulumi.asset.Archive?</span>
    </dt>
    <dd>{{% md %}}The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dead<wbr>Letter<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiondeadletterconfig">Function<wbr>Dead<wbr>Letter<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Nested block to configure the function's *dead letter queue*. See details below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of what your Lambda Function does.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>environment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionenvironment">Function<wbr>Environment?</a></span>
    </dt>
    <dd>{{% md %}}The Lambda environment's configuration settings. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>handler</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The function [entrypoint][3] in your code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ARN for the KMS encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>layers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>publish</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reserved<wbr>Concurrent<wbr>Executions</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">ARN</span>
    </dt>
    <dd>{{% md %}}IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}See [Runtimes][6] for valid values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The S3 key of an object containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3Object<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The object version containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Code<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256("file.zip")` (this provider 0.11.12 and later) or `base64sha256(file("file.zip"))` (this provider 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tracing<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiontracingconfig">Function<wbr>Tracing<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionvpcconfig">Function<wbr>Vpc<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">pulumi.Archive</span>
    </dt>
    <dd>{{% md %}}The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dead_<wbr>letter_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiondeadletterconfig">Dict[Function<wbr>Dead<wbr>Letter<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Nested block to configure the function's *dead letter queue*. See details below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of what your Lambda Function does.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>environment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionenvironment">Dict[Function<wbr>Environment]</a></span>
    </dt>
    <dd>{{% md %}}The Lambda environment's configuration settings. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>handler</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The function [entrypoint][3] in your code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms_<wbr>key_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN for the KMS encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>layers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>publish</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reserved_<wbr>concurrent_<wbr>executions</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}See [Runtimes][6] for valid values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The S3 key of an object containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3_<wbr>object_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The object version containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>code_<wbr>hash</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256("file.zip")` (this provider 0.11.12 and later) or `base64sha256(file("file.zip"))` (this provider 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tracing_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiontracingconfig">Dict[Function<wbr>Tracing<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionvpcconfig">Dict[Function<wbr>Vpc<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Function Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) identifying your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">Archive?</span>
    </dt>
    <dd>{{% md %}}The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dead<wbr>Letter<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiondeadletterconfig">Function<wbr>Dead<wbr>Letter<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Nested block to configure the function's *dead letter queue*. See details below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of what your Lambda Function does.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Environment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionenvironment">Function<wbr>Environment?</a></span>
    </dt>
    <dd>{{% md %}}The Lambda environment's configuration settings. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Handler</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The function [entrypoint][3] in your code.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Invoke<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)'s `uri`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ARN for the KMS encryption key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Last<wbr>Modified</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date this resource was last modified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Layers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Memory<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Publish</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Qualified<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Reserved<wbr>Concurrent<wbr>Executions</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}See [Runtimes][6] for valid values.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>S3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>S3Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The S3 key of an object containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>S3Object<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The object version containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Code<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256("file.zip")` (this provider 0.11.12 and later) or `base64sha256(file("file.zip"))` (this provider 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Code<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The size in bytes of the function .zip file.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the object.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tracing<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiontracingconfig">Function<wbr>Tracing<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Latest published version of your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionvpcconfig">Function<wbr>Vpc<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) identifying your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">pulumi.Archive</span>
    </dt>
    <dd>{{% md %}}The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dead<wbr>Letter<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiondeadletterconfig">*Function<wbr>Dead<wbr>Letter<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Nested block to configure the function's *dead letter queue*. See details below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of what your Lambda Function does.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Environment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionenvironment">*Function<wbr>Environment</a></span>
    </dt>
    <dd>{{% md %}}The Lambda environment's configuration settings. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Handler</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The function [entrypoint][3] in your code.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Invoke<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)'s `uri`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ARN for the KMS encryption key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Last<wbr>Modified</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date this resource was last modified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Layers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Memory<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Publish</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Qualified<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Reserved<wbr>Concurrent<wbr>Executions</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}See [Runtimes][6] for valid values.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>S3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>S3Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The S3 key of an object containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>S3Object<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The object version containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Code<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256("file.zip")` (this provider 0.11.12 and later) or `base64sha256(file("file.zip"))` (this provider 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Code<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The size in bytes of the function .zip file.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the object.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tracing<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiontracingconfig">Function<wbr>Tracing<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Latest published version of your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionvpcconfig">*Function<wbr>Vpc<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) identifying your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">pulumi.asset.Archive?</span>
    </dt>
    <dd>{{% md %}}The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dead<wbr>Letter<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiondeadletterconfig">Function<wbr>Dead<wbr>Letter<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Nested block to configure the function's *dead letter queue*. See details below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of what your Lambda Function does.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>environment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionenvironment">Function<wbr>Environment?</a></span>
    </dt>
    <dd>{{% md %}}The Lambda environment's configuration settings. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>handler</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The function [entrypoint][3] in your code.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>invoke<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)'s `uri`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ARN for the KMS encryption key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>last<wbr>Modified</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date this resource was last modified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>layers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>memory<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>publish</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>qualified<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>reserved<wbr>Concurrent<wbr>Executions</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">ARN</span>
    </dt>
    <dd>{{% md %}}IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}See [Runtimes][6] for valid values.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>s3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>s3Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The S3 key of an object containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>s3Object<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The object version containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source<wbr>Code<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256("file.zip")` (this provider 0.11.12 and later) or `base64sha256(file("file.zip"))` (this provider 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source<wbr>Code<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The size in bytes of the function .zip file.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the object.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tracing<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiontracingconfig">Function<wbr>Tracing<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Latest published version of your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionvpcconfig">Function<wbr>Vpc<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) identifying your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">pulumi.Archive</span>
    </dt>
    <dd>{{% md %}}The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dead_<wbr>letter_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiondeadletterconfig">Dict[Function<wbr>Dead<wbr>Letter<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Nested block to configure the function's *dead letter queue*. See details below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of what your Lambda Function does.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>environment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionenvironment">Dict[Function<wbr>Environment]</a></span>
    </dt>
    <dd>{{% md %}}The Lambda environment's configuration settings. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>handler</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The function [entrypoint][3] in your code.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>invoke_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)'s `uri`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kms_<wbr>key_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN for the KMS encryption key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>last_<wbr>modified</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The date this resource was last modified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>layers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>memory_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>publish</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>qualified_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>reserved_<wbr>concurrent_<wbr>executions</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}See [Runtimes][6] for valid values.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>s3_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>s3_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The S3 key of an object containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>s3_<wbr>object_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The object version containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source_<wbr>code_<wbr>hash</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256("file.zip")` (this provider 0.11.12 and later) or `base64sha256(file("file.zip"))` (this provider 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source_<wbr>code_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The size in bytes of the function .zip file.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the object.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tracing_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiontracingconfig">Dict[Function<wbr>Tracing<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Latest published version of your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionvpcconfig">Dict[Function<wbr>Vpc<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Function Resource

Get an existing Function resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#FunctionState">FunctionState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/lambda/#Function">Function</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>code=None<span class="p">, </span>dead_letter_config=None<span class="p">, </span>description=None<span class="p">, </span>environment=None<span class="p">, </span>handler=None<span class="p">, </span>invoke_arn=None<span class="p">, </span>kms_key_arn=None<span class="p">, </span>last_modified=None<span class="p">, </span>layers=None<span class="p">, </span>memory_size=None<span class="p">, </span>name=None<span class="p">, </span>publish=None<span class="p">, </span>qualified_arn=None<span class="p">, </span>reserved_concurrent_executions=None<span class="p">, </span>role=None<span class="p">, </span>runtime=None<span class="p">, </span>s3_bucket=None<span class="p">, </span>s3_key=None<span class="p">, </span>s3_object_version=None<span class="p">, </span>source_code_hash=None<span class="p">, </span>source_code_size=None<span class="p">, </span>tags=None<span class="p">, </span>timeout=None<span class="p">, </span>tracing_config=None<span class="p">, </span>version=None<span class="p">, </span>vpc_config=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetFunction<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionState">FunctionState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#Function">Function</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.Function.html">Function</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Lambda.FunctionState.html">FunctionState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>resource_name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

The following state arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) identifying your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">Archive?</span>
    </dt>
    <dd>{{% md %}}The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dead<wbr>Letter<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiondeadletterconfig">Function<wbr>Dead<wbr>Letter<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Nested block to configure the function's *dead letter queue*. See details below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of what your Lambda Function does.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Environment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionenvironment">Function<wbr>Environment<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The Lambda environment's configuration settings. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Handler</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The function [entrypoint][3] in your code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Invoke<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)'s `uri`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ARN for the KMS encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Modified</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The date this resource was last modified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Layers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Publish</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Qualified<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reserved<wbr>Concurrent<wbr>Executions</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See [Runtimes][6] for valid values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The S3 key of an object containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Object<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The object version containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Code<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256("file.zip")` (this provider 0.11.12 and later) or `base64sha256(file("file.zip"))` (this provider 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Code<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The size in bytes of the function .zip file.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tracing<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiontracingconfig">Function<wbr>Tracing<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Latest published version of your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionvpcconfig">Function<wbr>Vpc<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) identifying your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">pulumi.Archive</span>
    </dt>
    <dd>{{% md %}}The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dead<wbr>Letter<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiondeadletterconfig">*Function<wbr>Dead<wbr>Letter<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Nested block to configure the function's *dead letter queue*. See details below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of what your Lambda Function does.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Environment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionenvironment">*Function<wbr>Environment</a></span>
    </dt>
    <dd>{{% md %}}The Lambda environment's configuration settings. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Handler</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The function [entrypoint][3] in your code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Invoke<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)'s `uri`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ARN for the KMS encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Modified</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The date this resource was last modified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Layers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A unique name for your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Publish</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Qualified<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reserved<wbr>Concurrent<wbr>Executions</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}See [Runtimes][6] for valid values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The S3 key of an object containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>S3Object<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The object version containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Code<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256("file.zip")` (this provider 0.11.12 and later) or `base64sha256(file("file.zip"))` (this provider 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Code<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The size in bytes of the function .zip file.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tracing<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiontracingconfig">*Function<wbr>Tracing<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Latest published version of your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionvpcconfig">*Function<wbr>Vpc<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) identifying your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">pulumi.asset.Archive?</span>
    </dt>
    <dd>{{% md %}}The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dead<wbr>Letter<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiondeadletterconfig">Function<wbr>Dead<wbr>Letter<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Nested block to configure the function's *dead letter queue*. See details below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of what your Lambda Function does.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>environment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionenvironment">Function<wbr>Environment?</a></span>
    </dt>
    <dd>{{% md %}}The Lambda environment's configuration settings. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>handler</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The function [entrypoint][3] in your code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>invoke<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)'s `uri`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms<wbr>Key<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ARN for the KMS encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>last<wbr>Modified</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The date this resource was last modified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>layers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>publish</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>qualified<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reserved<wbr>Concurrent<wbr>Executions</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">ARN?</span>
    </dt>
    <dd>{{% md %}}IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See [Runtimes][6] for valid values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The S3 key of an object containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3Object<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The object version containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Code<wbr>Hash</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256("file.zip")` (this provider 0.11.12 and later) or `base64sha256(file("file.zip"))` (this provider 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Code<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The size in bytes of the function .zip file.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tracing<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiontracingconfig">Function<wbr>Tracing<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Latest published version of your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionvpcconfig">Function<wbr>Vpc<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) identifying your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">pulumi.Archive</span>
    </dt>
    <dd>{{% md %}}The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dead_<wbr>letter_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiondeadletterconfig">Dict[Function<wbr>Dead<wbr>Letter<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Nested block to configure the function's *dead letter queue*. See details below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of what your Lambda Function does.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>environment</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionenvironment">Dict[Function<wbr>Environment]</a></span>
    </dt>
    <dd>{{% md %}}The Lambda environment's configuration settings. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>handler</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The function [entrypoint][3] in your code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>invoke_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)'s `uri`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms_<wbr>key_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN for the KMS encryption key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>last_<wbr>modified</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The date this resource was last modified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>layers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>publish</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>qualified_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reserved_<wbr>concurrent_<wbr>executions</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}See [Runtimes][6] for valid values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The S3 key of an object containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>s3_<wbr>object_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The object version containing the function's deployment package. Conflicts with `filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>code_<wbr>hash</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256("file.zip")` (this provider 0.11.12 and later) or `base64sha256(file("file.zip"))` (this provider 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>code_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The size in bytes of the function .zip file.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tracing_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functiontracingconfig">Dict[Function<wbr>Tracing<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Latest published version of your Lambda Function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionvpcconfig">Dict[Function<wbr>Vpc<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Function<wbr>Dead<wbr>Letter<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FunctionDeadLetterConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FunctionDeadLetterConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionDeadLetterConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionDeadLetterConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of an SNS topic or SQS queue to notify when an invocation fails. If this
option is used, the function's IAM role must be granted suitable access to write to the target object,
which means allowing either the `sns:Publish` or `sqs:SendMessage` action on this ARN, depending on
which service is targeted.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of an SNS topic or SQS queue to notify when an invocation fails. If this
option is used, the function's IAM role must be granted suitable access to write to the target object,
which means allowing either the `sns:Publish` or `sqs:SendMessage` action on this ARN, depending on
which service is targeted.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>target<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of an SNS topic or SQS queue to notify when an invocation fails. If this
option is used, the function's IAM role must be granted suitable access to write to the target object,
which means allowing either the `sns:Publish` or `sqs:SendMessage` action on this ARN, depending on
which service is targeted.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>target_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of an SNS topic or SQS queue to notify when an invocation fails. If this
option is used, the function's IAM role must be granted suitable access to write to the target object,
which means allowing either the `sns:Publish` or `sqs:SendMessage` action on this ARN, depending on
which service is targeted.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Function<wbr>Environment</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FunctionEnvironment">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FunctionEnvironment">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionEnvironmentArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionEnvironmentOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A map that defines environment variables for the Lambda function.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A map that defines environment variables for the Lambda function.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A map that defines environment variables for the Lambda function.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A map that defines environment variables for the Lambda function.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Function<wbr>Tracing<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FunctionTracingConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FunctionTracingConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionTracingConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionTracingConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Can be either `PassThrough` or `Active`. If PassThrough, Lambda will only trace
the request from an upstream service if it contains a tracing header with
"sampled=1". If Active, Lambda will respect any tracing header it receives
from an upstream service. If no tracing header is received, Lambda will call
X-Ray for a tracing decision.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Can be either `PassThrough` or `Active`. If PassThrough, Lambda will only trace
the request from an upstream service if it contains a tracing header with
"sampled=1". If Active, Lambda will respect any tracing header it receives
from an upstream service. If no tracing header is received, Lambda will call
X-Ray for a tracing decision.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Can be either `PassThrough` or `Active`. If PassThrough, Lambda will only trace
the request from an upstream service if it contains a tracing header with
"sampled=1". If Active, Lambda will respect any tracing header it receives
from an upstream service. If no tracing header is received, Lambda will call
X-Ray for a tracing decision.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Can be either `PassThrough` or `Active`. If PassThrough, Lambda will only trace
the request from an upstream service if it contains a tracing header with
"sampled=1". If Active, Lambda will respect any tracing header it receives
from an upstream service. If no tracing header is received, Lambda will call
X-Ray for a tracing decision.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Function<wbr>Vpc<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FunctionVpcConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FunctionVpcConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionVpcConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/lambda?tab=doc#FunctionVpcConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of security group IDs associated with the Lambda function.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of subnet IDs associated with the Lambda function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of security group IDs associated with the Lambda function.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of subnet IDs associated with the Lambda function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of security group IDs associated with the Lambda function.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of subnet IDs associated with the Lambda function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>security_<wbr>group_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of security group IDs associated with the Lambda function.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnet_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of subnet IDs associated with the Lambda function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-aws">https://github.com/pulumi/pulumi-aws</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
