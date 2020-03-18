
---
title: "FirehoseDeliveryStream"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides a Kinesis Firehose Delivery Stream resource. Amazon Kinesis Firehose is a fully managed, elastic service to easily deliver real-time data streams to destinations such as Amazon S3 and Amazon Redshift.

For more details, see the [Amazon Kinesis Firehose Documentation][1].

## Example Usage

### Extended S3 Destination

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("bucket", {
    acl: "private",
});
const firehoseRole = new aws.iam.Role("firehose_role", {
    assumeRolePolicy: `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "firehose.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
`,
});
const lambdaIam = new aws.iam.Role("lambda_iam", {
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
const lambdaProcessor = new aws.lambda.Function("lambda_processor", {
    code: new pulumi.asset.FileArchive("lambda.zip"),
    handler: "exports.handler",
    role: lambdaIam.arn,
    runtime: "nodejs8.10",
});
const extendedS3Stream = new aws.kinesis.FirehoseDeliveryStream("extended_s3_stream", {
    destination: "extended_s3",
    extendedS3Configuration: {
        bucketArn: bucket.arn,
        processingConfiguration: {
            enabled: true,
            processors: [{
                parameters: [{
                    parameterName: "LambdaArn",
                    parameterValue: pulumi.interpolate`${lambdaProcessor.arn}:$LATEST`,
                }],
                type: "Lambda",
            }],
        },
        roleArn: firehoseRole.arn,
    },
});
```

### S3 Destination

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("bucket", {
    acl: "private",
});
const firehoseRole = new aws.iam.Role("firehose_role", {
    assumeRolePolicy: `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "firehose.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
`,
});
const testStream = new aws.kinesis.FirehoseDeliveryStream("test_stream", {
    destination: "s3",
    s3Configuration: {
        bucketArn: bucket.arn,
        roleArn: firehoseRole.arn,
    },
});
```

### Redshift Destination

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const testCluster = new aws.redshift.Cluster("test_cluster", {
    clusterIdentifier: "tf-redshift-cluster-%d",
    clusterType: "single-node",
    databaseName: "test",
    masterPassword: "T3stPass",
    masterUsername: "testuser",
    nodeType: "dc1.large",
});
const testStream = new aws.kinesis.FirehoseDeliveryStream("test_stream", {
    destination: "redshift",
    redshiftConfiguration: {
        clusterJdbcurl: pulumi.interpolate`jdbc:redshift://${testCluster.endpoint}/${testCluster.databaseName}`,
        copyOptions: "delimiter '|'", // the default delimiter
        dataTableColumns: "test-col",
        dataTableName: "test-table",
        password: "T3stPass",
        roleArn: aws_iam_role_firehose_role.arn,
        s3BackupConfiguration: {
            bucketArn: aws_s3_bucket_bucket.arn,
            bufferInterval: 300,
            bufferSize: 15,
            compressionFormat: "GZIP",
            roleArn: aws_iam_role_firehose_role.arn,
        },
        s3BackupMode: "Enabled",
        username: "testuser",
    },
    s3Configuration: {
        bucketArn: aws_s3_bucket_bucket.arn,
        bufferInterval: 400,
        bufferSize: 10,
        compressionFormat: "GZIP",
        roleArn: aws_iam_role_firehose_role.arn,
    },
});
```

### Elasticsearch Destination

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const testCluster = new aws.elasticsearch.Domain("test_cluster", {});
const testStream = new aws.kinesis.FirehoseDeliveryStream("test_stream", {
    destination: "elasticsearch",
    elasticsearchConfiguration: {
        domainArn: testCluster.arn,
        indexName: "test",
        processingConfiguration: {
            enabled: true,
            processors: [{
                parameters: [{
                    parameterName: "LambdaArn",
                    parameterValue: pulumi.interpolate`${aws_lambda_function_lambda_processor.arn}:$LATEST`,
                }],
                type: "Lambda",
            }],
        },
        roleArn: aws_iam_role_firehose_role.arn,
        typeName: "test",
    },
    s3Configuration: {
        bucketArn: aws_s3_bucket_bucket.arn,
        bufferInterval: 400,
        bufferSize: 10,
        compressionFormat: "GZIP",
        roleArn: aws_iam_role_firehose_role.arn,
    },
});
```


### Splunk Destination

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const testStream = new aws.kinesis.FirehoseDeliveryStream("test_stream", {
    destination: "splunk",
    s3Configuration: {
        bucketArn: aws_s3_bucket_bucket.arn,
        bufferInterval: 400,
        bufferSize: 10,
        compressionFormat: "GZIP",
        roleArn: aws_iam_role_firehose.arn,
    },
    splunkConfiguration: {
        hecAcknowledgmentTimeout: 600,
        hecEndpoint: "https://http-inputs-mydomain.splunkcloud.com:443",
        hecEndpointType: "Event",
        hecToken: "51D4DA16-C61B-4F5F-8EC7-ED4301342A4A",
        s3BackupMode: "FailedEventsOnly",
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/kinesis_firehose_delivery_stream.html.markdown.



## Create a FirehoseDeliveryStream Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/kinesis/#FirehoseDeliveryStream">FirehoseDeliveryStream</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/kinesis/#FirehoseDeliveryStreamArgs">FirehoseDeliveryStreamArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">FirehoseDeliveryStream</span><span class="p">(resource_name, opts=None, </span>arn=None<span class="p">, </span>destination=None<span class="p">, </span>destination_id=None<span class="p">, </span>elasticsearch_configuration=None<span class="p">, </span>extended_s3_configuration=None<span class="p">, </span>kinesis_source_configuration=None<span class="p">, </span>name=None<span class="p">, </span>redshift_configuration=None<span class="p">, </span>s3_configuration=None<span class="p">, </span>server_side_encryption=None<span class="p">, </span>splunk_configuration=None<span class="p">, </span>tags=None<span class="p">, </span>version_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewFirehoseDeliveryStream<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamArgs">FirehoseDeliveryStreamArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStream">FirehoseDeliveryStream</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStream.html">FirehoseDeliveryStream</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamArgs.html">FirehoseDeliveryStreamArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a FirehoseDeliveryStream resource with the given unique name, arguments, and options.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) specifying the Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Destination</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Destination<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration options if elasticsearch is the destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Extended<wbr>S3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configuration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enhanced configuration options for the s3 destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Source<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamkinesissourceconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Kinesis<wbr>Source<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Redshift<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration options if redshift is the destination.
Using `redshift_configuration` requires the user to also specify a
`s3_configuration` block. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreams3configuration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>S3Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Required for non-S3 destinations. For S3 destination, use `extended_s3_configuration` instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamserversideencryption">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Server<wbr>Side<wbr>Encryption<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options.
Server-side encryption should not be enabled when a kinesis stream is configured as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Splunk<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the table version for the output data schema. Defaults to `LATEST`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) specifying the Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Destination</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Destination<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration options if elasticsearch is the destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Extended<wbr>S3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configuration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enhanced configuration options for the s3 destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Source<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamkinesissourceconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Kinesis<wbr>Source<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Redshift<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration options if redshift is the destination.
Using `redshift_configuration` requires the user to also specify a
`s3_configuration` block. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreams3configuration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>S3Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Required for non-S3 destinations. For S3 destination, use `extended_s3_configuration` instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamserversideencryption">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Server<wbr>Side<wbr>Encryption</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options.
Server-side encryption should not be enabled when a kinesis stream is configured as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Splunk<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the table version for the output data schema. Defaults to `LATEST`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) specifying the Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">destination</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">destination<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration options if elasticsearch is the destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">extended<wbr>S3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configuration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enhanced configuration options for the s3 destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis<wbr>Source<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamkinesissourceconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Kinesis<wbr>Source<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">redshift<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration options if redshift is the destination.
Using `redshift_configuration` requires the user to also specify a
`s3_configuration` block. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreams3configuration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>S3Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Required for non-S3 destinations. For S3 destination, use `extended_s3_configuration` instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamserversideencryption">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Server<wbr>Side<wbr>Encryption?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options.
Server-side encryption should not be enabled when a kinesis stream is configured as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">splunk<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the table version for the output data schema. Defaults to `LATEST`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) specifying the Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">destination</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">destination_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>elasticsearch_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration options if elasticsearch is the destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">extended_<wbr>s3_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configuration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enhanced configuration options for the s3 destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis_<wbr>source_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamkinesissourceconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>kinesis_<wbr>source_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">redshift_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>redshift_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration options if redshift is the destination.
Using `redshift_configuration` requires the user to also specify a
`s3_configuration` block. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreams3configuration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>s3_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Required for non-S3 destinations. For S3 destination, use `extended_s3_configuration` instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server_<wbr>side_<wbr>encryption</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamserversideencryption">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>server_<wbr>side_<wbr>encryption]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options.
Server-side encryption should not be enabled when a kinesis stream is configured as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">splunk_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>splunk_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the table version for the output data schema. Defaults to `LATEST`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## FirehoseDeliveryStream Output Properties

The following output properties are available:



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) specifying the Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Destination</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Destination<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration options if elasticsearch is the destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Extended<wbr>S3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configuration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Enhanced configuration options for the s3 destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Source<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamkinesissourceconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Kinesis<wbr>Source<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Redshift<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration options if redshift is the destination.
Using `redshift_configuration` requires the user to also specify a
`s3_configuration` block. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreams3configuration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>S3Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Required for non-S3 destinations. For S3 destination, use `extended_s3_configuration` instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamserversideencryption">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Server<wbr>Side<wbr>Encryption?</a></code>
            </td>
            <td class="align-top">{{% md %}} Encrypt at rest options.
Server-side encryption should not be enabled when a kinesis stream is configured as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Splunk<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies the table version for the output data schema. Defaults to `LATEST`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) specifying the Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Destination</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Destination<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration options if elasticsearch is the destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Extended<wbr>S3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configuration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Enhanced configuration options for the s3 destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Source<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamkinesissourceconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Kinesis<wbr>Source<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Redshift<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration options if redshift is the destination.
Using `redshift_configuration` requires the user to also specify a
`s3_configuration` block. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreams3configuration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>S3Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Required for non-S3 destinations. For S3 destination, use `extended_s3_configuration` instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamserversideencryption">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Server<wbr>Side<wbr>Encryption</a></code>
            </td>
            <td class="align-top">{{% md %}} Encrypt at rest options.
Server-side encryption should not be enabled when a kinesis stream is configured as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Splunk<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies the table version for the output data schema. Defaults to `LATEST`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) specifying the Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">destination</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">destination<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration options if elasticsearch is the destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">extended<wbr>S3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configuration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Enhanced configuration options for the s3 destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis<wbr>Source<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamkinesissourceconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Kinesis<wbr>Source<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">redshift<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration options if redshift is the destination.
Using `redshift_configuration` requires the user to also specify a
`s3_configuration` block. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreams3configuration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>S3Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Required for non-S3 destinations. For S3 destination, use `extended_s3_configuration` instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamserversideencryption">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Server<wbr>Side<wbr>Encryption?</a></code>
            </td>
            <td class="align-top">{{% md %}} Encrypt at rest options.
Server-side encryption should not be enabled when a kinesis stream is configured as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">splunk<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies the table version for the output data schema. Defaults to `LATEST`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) specifying the Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">destination</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">destination_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>elasticsearch_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration options if elasticsearch is the destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">extended_<wbr>s3_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configuration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} Enhanced configuration options for the s3 destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis_<wbr>source_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamkinesissourceconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>kinesis_<wbr>source_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">redshift_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>redshift_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration options if redshift is the destination.
Using `redshift_configuration` requires the user to also specify a
`s3_configuration` block. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreams3configuration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>s3_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} Required for non-S3 destinations. For S3 destination, use `extended_s3_configuration` instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server_<wbr>side_<wbr>encryption</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamserversideencryption">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>server_<wbr>side_<wbr>encryption]</a></code>
            </td>
            <td class="align-top">{{% md %}} Encrypt at rest options.
Server-side encryption should not be enabled when a kinesis stream is configured as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">splunk_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>splunk_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Specifies the table version for the output data schema. Defaults to `LATEST`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing FirehoseDeliveryStream Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/kinesis/#FirehoseDeliveryStreamState">FirehoseDeliveryStreamState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/kinesis/#FirehoseDeliveryStream">FirehoseDeliveryStream</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>destination=None<span class="p">, </span>destination_id=None<span class="p">, </span>elasticsearch_configuration=None<span class="p">, </span>extended_s3_configuration=None<span class="p">, </span>kinesis_source_configuration=None<span class="p">, </span>name=None<span class="p">, </span>redshift_configuration=None<span class="p">, </span>s3_configuration=None<span class="p">, </span>server_side_encryption=None<span class="p">, </span>splunk_configuration=None<span class="p">, </span>tags=None<span class="p">, </span>version_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetFirehoseDeliveryStream<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamState">FirehoseDeliveryStreamState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStream">FirehoseDeliveryStream</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStream.html">FirehoseDeliveryStream</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamState.html">FirehoseDeliveryStreamState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing FirehoseDeliveryStream resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following state arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) specifying the Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Destination</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Destination<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration options if elasticsearch is the destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Extended<wbr>S3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configuration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enhanced configuration options for the s3 destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Source<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamkinesissourceconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Kinesis<wbr>Source<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Redshift<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration options if redshift is the destination.
Using `redshift_configuration` requires the user to also specify a
`s3_configuration` block. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreams3configuration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>S3Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Required for non-S3 destinations. For S3 destination, use `extended_s3_configuration` instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamserversideencryption">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Server<wbr>Side<wbr>Encryption<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options.
Server-side encryption should not be enabled when a kinesis stream is configured as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Splunk<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the table version for the output data schema. Defaults to `LATEST`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) specifying the Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Destination</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Destination<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration options if elasticsearch is the destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Extended<wbr>S3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configuration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enhanced configuration options for the s3 destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Source<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamkinesissourceconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Kinesis<wbr>Source<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Redshift<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration options if redshift is the destination.
Using `redshift_configuration` requires the user to also specify a
`s3_configuration` block. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreams3configuration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>S3Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Required for non-S3 destinations. For S3 destination, use `extended_s3_configuration` instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamserversideencryption">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Server<wbr>Side<wbr>Encryption</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options.
Server-side encryption should not be enabled when a kinesis stream is configured as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Splunk<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the table version for the output data schema. Defaults to `LATEST`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) specifying the Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">destination</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">destination<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration options if elasticsearch is the destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">extended<wbr>S3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configuration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enhanced configuration options for the s3 destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis<wbr>Source<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamkinesissourceconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Kinesis<wbr>Source<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">redshift<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration options if redshift is the destination.
Using `redshift_configuration` requires the user to also specify a
`s3_configuration` block. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreams3configuration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>S3Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Required for non-S3 destinations. For S3 destination, use `extended_s3_configuration` instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamserversideencryption">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Server<wbr>Side<wbr>Encryption?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options.
Server-side encryption should not be enabled when a kinesis stream is configured as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">splunk<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the table version for the output data schema. Defaults to `LATEST`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) specifying the Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">destination</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">destination_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>elasticsearch_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration options if elasticsearch is the destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">extended_<wbr>s3_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configuration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enhanced configuration options for the s3 destination. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis_<wbr>source_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamkinesissourceconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>kinesis_<wbr>source_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A name to identify the stream. This is unique to the
AWS account and region the Stream is created in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">redshift_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>redshift_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration options if redshift is the destination.
Using `redshift_configuration` requires the user to also specify a
`s3_configuration` block. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreams3configuration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>s3_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Required for non-S3 destinations. For S3 destination, use `extended_s3_configuration` instead. Configuration options for the s3 destination (or the intermediate bucket if the destination
is redshift). More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server_<wbr>side_<wbr>encryption</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamserversideencryption">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>server_<wbr>side_<wbr>encryption]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options.
Server-side encryption should not be enabled when a kinesis stream is configured as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">splunk_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>splunk_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the table version for the output data schema. Defaults to `LATEST`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### FirehoseDeliveryStreamElasticsearchConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamElasticsearchConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamElasticsearchConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamElasticsearchConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamElasticsearchConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamElasticsearchConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamElasticsearchConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Buffering<wbr>Interval</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds between 60 to 900, before delivering it to the destination.  The default value is 300s.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffering<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs between 1 to 100, before delivering it to the destination.  The default value is 5MB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfigurationcloudwatchloggingoptions">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Amazon ES domain.  The IAM role must have permission for `DescribeElasticsearchDomain`, `DescribeElasticsearchDomains`, and `DescribeElasticsearchDomainConfig` after assuming `RoleARN`.  The pattern needs to be `arn:.*`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Index<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Elasticsearch index name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Index<wbr>Rotation<wbr>Period</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Elasticsearch index rotation period.  Index rotation appends a timestamp to the IndexName to facilitate expiration of old data.  Valid values are `NoRotation`, `OneHour`, `OneDay`, `OneWeek`, and `OneMonth`.  The default value is `OneDay`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Processing<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfigurationprocessingconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data processing configuration.  More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retry<wbr>Duration</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
After an initial failure to deliver to Splunk, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Backup<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Elasticsearch type name with maximum length of 100 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Buffering<wbr>Interval</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds between 60 to 900, before delivering it to the destination.  The default value is 300s.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffering<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs between 1 to 100, before delivering it to the destination.  The default value is 5MB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfigurationcloudwatchloggingoptions">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Amazon ES domain.  The IAM role must have permission for `DescribeElasticsearchDomain`, `DescribeElasticsearchDomains`, and `DescribeElasticsearchDomainConfig` after assuming `RoleARN`.  The pattern needs to be `arn:.*`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Index<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Elasticsearch index name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Index<wbr>Rotation<wbr>Period</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Elasticsearch index rotation period.  Index rotation appends a timestamp to the IndexName to facilitate expiration of old data.  Valid values are `NoRotation`, `OneHour`, `OneDay`, `OneWeek`, and `OneMonth`.  The default value is `OneDay`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Processing<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfigurationprocessingconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration<wbr>Processing<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data processing configuration.  More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retry<wbr>Duration</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
After an initial failure to deliver to Splunk, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Backup<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Elasticsearch type name with maximum length of 100 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">buffering<wbr>Interval</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds between 60 to 900, before delivering it to the destination.  The default value is 300s.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffering<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs between 1 to 100, before delivering it to the destination.  The default value is 5MB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfigurationcloudwatchloggingoptions">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Amazon ES domain.  The IAM role must have permission for `DescribeElasticsearchDomain`, `DescribeElasticsearchDomains`, and `DescribeElasticsearchDomainConfig` after assuming `RoleARN`.  The pattern needs to be `arn:.*`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">index<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Elasticsearch index name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">index<wbr>Rotation<wbr>Period</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Elasticsearch index rotation period.  Index rotation appends a timestamp to the IndexName to facilitate expiration of old data.  Valid values are `NoRotation`, `OneHour`, `OneDay`, `OneWeek`, and `OneMonth`.  The default value is `OneDay`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">processing<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfigurationprocessingconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration<wbr>Processing<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data processing configuration.  More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retry<wbr>Duration</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
After an initial failure to deliver to Splunk, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Backup<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Elasticsearch type name with maximum length of 100 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">buffering_<wbr>interval</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds between 60 to 900, before delivering it to the destination.  The default value is 300s.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffering_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs between 1 to 100, before delivering it to the destination.  The default value is 5MB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch_<wbr>logging_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfigurationcloudwatchloggingoptions">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>elasticsearch_<wbr>configuration_<wbr>cloudwatch_<wbr>logging_<wbr>options]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Amazon ES domain.  The IAM role must have permission for `DescribeElasticsearchDomain`, `DescribeElasticsearchDomains`, and `DescribeElasticsearchDomainConfig` after assuming `RoleARN`.  The pattern needs to be `arn:.*`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">index_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Elasticsearch index name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">index_<wbr>rotation_<wbr>period</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Elasticsearch index rotation period.  Index rotation appends a timestamp to the IndexName to facilitate expiration of old data.  Valid values are `NoRotation`, `OneHour`, `OneDay`, `OneWeek`, and `OneMonth`.  The default value is `OneDay`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">processing_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfigurationprocessingconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>elasticsearch_<wbr>configuration_<wbr>processing_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data processing configuration.  More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retry_<wbr>duration</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
After an initial failure to deliver to Splunk, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>backup_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Elasticsearch type name with maximum length of 100 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamElasticsearchConfigurationCloudwatchLoggingOptions.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>stream_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Processors</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfigurationprocessingconfigurationprocessor">List&lt;Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of data processors. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Processors</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfigurationprocessingconfigurationprocessor">[]kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of data processors. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">processors</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfigurationprocessingconfigurationprocessor">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of data processors. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">processors</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfigurationprocessingconfigurationprocessor">List[firehose_<wbr>delivery_<wbr>stream_<wbr>elasticsearch_<wbr>configuration_<wbr>processing_<wbr>configuration_<wbr>processor]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of data processors. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessor
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessor">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessor">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessor.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfigurationprocessingconfigurationprocessorparameter">List&lt;Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor<wbr>Parameter<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of processor parameters. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of processor. Valid Values: `Lambda`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfigurationprocessingconfigurationprocessorparameter">[]kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor<wbr>Parameter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of processor parameters. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of processor. Valid Values: `Lambda`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfigurationprocessingconfigurationprocessorparameter">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Elasticsearch<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor<wbr>Parameter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of processor parameters. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of processor. Valid Values: `Lambda`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamelasticsearchconfigurationprocessingconfigurationprocessorparameter">List[firehose_<wbr>delivery_<wbr>stream_<wbr>elasticsearch_<wbr>configuration_<wbr>processing_<wbr>configuration_<wbr>processor_<wbr>parameter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of processor parameters. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of processor. Valid Values: `Lambda`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorParameter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorParameter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorParameter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorParameterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorParameterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorParameterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamElasticsearchConfigurationProcessingConfigurationProcessorParameter.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Parameter<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Parameter<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">parameter<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">parameter_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter_<wbr>value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamExtendedS3Configuration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamExtendedS3Configuration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamExtendedS3Configuration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3Configuration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffer<wbr>Interval</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffer<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationcloudwatchloggingoptions">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression<wbr>Format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Data<wbr>Format<wbr>Conversion<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument for the serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3. More details given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Error<wbr>Output<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Prefix added to failed records before writing them to S3. This prefix appears immediately following the bucket name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;YYYY/MM/DD/HH&#34; time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Processing<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationprocessingconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Processing<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data processing configuration.  More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Backup<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurations3backupconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>S3Backup<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for backup in Amazon S3. Required if `s3_backup_mode` is `Enabled`. Supports the same fields as `s3_configuration` object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Backup<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffer<wbr>Interval</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffer<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationcloudwatchloggingoptions">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression<wbr>Format</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Data<wbr>Format<wbr>Conversion<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument for the serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3. More details given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Error<wbr>Output<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Prefix added to failed records before writing them to S3. This prefix appears immediately following the bucket name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;YYYY/MM/DD/HH&#34; time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Processing<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationprocessingconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Processing<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data processing configuration.  More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Backup<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurations3backupconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>S3Backup<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for backup in Amazon S3. Required if `s3_backup_mode` is `Enabled`. Supports the same fields as `s3_configuration` object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Backup<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffer<wbr>Interval</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffer<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationcloudwatchloggingoptions">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression<wbr>Format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">data<wbr>Format<wbr>Conversion<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument for the serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3. More details given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">error<wbr>Output<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Prefix added to failed records before writing them to S3. This prefix appears immediately following the bucket name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;YYYY/MM/DD/HH&#34; time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">processing<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationprocessingconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Processing<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data processing configuration.  More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Backup<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurations3backupconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>S3Backup<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for backup in Amazon S3. Required if `s3_backup_mode` is `Enabled`. Supports the same fields as `s3_configuration` object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Backup<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffer_<wbr>interval</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffer_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch_<wbr>logging_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationcloudwatchloggingoptions">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration_<wbr>cloudwatch_<wbr>logging_<wbr>options]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression_<wbr>format</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">data_<wbr>format_<wbr>conversion_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration_<wbr>data_<wbr>format_<wbr>conversion_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument for the serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3. More details given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">error_<wbr>output_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Prefix added to failed records before writing them to S3. This prefix appears immediately following the bucket name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;YYYY/MM/DD/HH&#34; time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">processing_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationprocessingconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration_<wbr>processing_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data processing configuration.  More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>backup_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurations3backupconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration_<wbr>s3_<wbr>backup_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for backup in Amazon S3. Required if `s3_backup_mode` is `Enabled`. Supports the same fields as `s3_configuration` object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>backup_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationCloudwatchLoggingOptions.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>stream_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Format<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationinputformatconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Input<wbr>Format<wbr>Configuration<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies the deserializer that you want Kinesis Data Firehose to use to convert the format of your data from JSON. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Output<wbr>Format<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationoutputformatconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Output<wbr>Format<wbr>Configuration<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies the serializer that you want Kinesis Data Firehose to use to convert the format of your data to the Parquet or ORC format. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Schema<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationschemaconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Schema<wbr>Configuration<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies the AWS Glue Data Catalog table that contains the column information. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Format<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationinputformatconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Input<wbr>Format<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies the deserializer that you want Kinesis Data Firehose to use to convert the format of your data from JSON. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Output<wbr>Format<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationoutputformatconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Output<wbr>Format<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies the serializer that you want Kinesis Data Firehose to use to convert the format of your data to the Parquet or ORC format. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Schema<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationschemaconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Schema<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies the AWS Glue Data Catalog table that contains the column information. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input<wbr>Format<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationinputformatconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Input<wbr>Format<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies the deserializer that you want Kinesis Data Firehose to use to convert the format of your data from JSON. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">output<wbr>Format<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationoutputformatconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Output<wbr>Format<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies the serializer that you want Kinesis Data Firehose to use to convert the format of your data to the Parquet or ORC format. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">schema<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationschemaconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Schema<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies the AWS Glue Data Catalog table that contains the column information. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input_<wbr>format_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationinputformatconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration_<wbr>data_<wbr>format_<wbr>conversion_<wbr>configuration_<wbr>input_<wbr>format_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies the deserializer that you want Kinesis Data Firehose to use to convert the format of your data from JSON. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">output_<wbr>format_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationoutputformatconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration_<wbr>data_<wbr>format_<wbr>conversion_<wbr>configuration_<wbr>output_<wbr>format_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies the serializer that you want Kinesis Data Firehose to use to convert the format of your data to the Parquet or ORC format. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">schema_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationschemaconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration_<wbr>data_<wbr>format_<wbr>conversion_<wbr>configuration_<wbr>schema_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies the AWS Glue Data Catalog table that contains the column information. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Deserializer</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationinputformatconfigurationdeserializer">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Input<wbr>Format<wbr>Configuration<wbr>Deserializer<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Deserializer</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationinputformatconfigurationdeserializer">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Input<wbr>Format<wbr>Configuration<wbr>Deserializer</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">deserializer</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationinputformatconfigurationdeserializer">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Input<wbr>Format<wbr>Configuration<wbr>Deserializer</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">deserializer</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationinputformatconfigurationdeserializer">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration_<wbr>data_<wbr>format_<wbr>conversion_<wbr>configuration_<wbr>input_<wbr>format_<wbr>configuration_<wbr>deserializer]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializer.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Hive<wbr>Json<wbr>Ser<wbr>De</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationinputformatconfigurationdeserializerhivejsonserde">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Input<wbr>Format<wbr>Configuration<wbr>Deserializer<wbr>Hive<wbr>Json<wbr>Ser<wbr>De<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument that specifies the native Hive / HCatalog JsonSerDe. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Open<wbr>XJson<wbr>Ser<wbr>De</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationinputformatconfigurationdeserializeropenxjsonserde">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Input<wbr>Format<wbr>Configuration<wbr>Deserializer<wbr>Open<wbr>XJson<wbr>Ser<wbr>De<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument that specifies the OpenX SerDe. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Hive<wbr>Json<wbr>Ser<wbr>De</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationinputformatconfigurationdeserializerhivejsonserde">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Input<wbr>Format<wbr>Configuration<wbr>Deserializer<wbr>Hive<wbr>Json<wbr>Ser<wbr>De</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument that specifies the native Hive / HCatalog JsonSerDe. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Open<wbr>XJson<wbr>Ser<wbr>De</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationinputformatconfigurationdeserializeropenxjsonserde">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Input<wbr>Format<wbr>Configuration<wbr>Deserializer<wbr>Open<wbr>XJson<wbr>Ser<wbr>De</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument that specifies the OpenX SerDe. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">hive<wbr>Json<wbr>Ser<wbr>De</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationinputformatconfigurationdeserializerhivejsonserde">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Input<wbr>Format<wbr>Configuration<wbr>Deserializer<wbr>Hive<wbr>Json<wbr>Ser<wbr>De?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument that specifies the native Hive / HCatalog JsonSerDe. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">open<wbr>XJson<wbr>Ser<wbr>De</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationinputformatconfigurationdeserializeropenxjsonserde">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Input<wbr>Format<wbr>Configuration<wbr>Deserializer<wbr>Open<wbr>XJson<wbr>Ser<wbr>De?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument that specifies the OpenX SerDe. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">hive_<wbr>json_<wbr>ser_<wbr>de</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationinputformatconfigurationdeserializerhivejsonserde">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration_<wbr>data_<wbr>format_<wbr>conversion_<wbr>configuration_<wbr>input_<wbr>format_<wbr>configuration_<wbr>deserializer_<wbr>hive_<wbr>json_<wbr>ser_<wbr>de]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument that specifies the native Hive / HCatalog JsonSerDe. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">open_<wbr>x_<wbr>json_<wbr>ser_<wbr>de</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationinputformatconfigurationdeserializeropenxjsonserde">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration_<wbr>data_<wbr>format_<wbr>conversion_<wbr>configuration_<wbr>input_<wbr>format_<wbr>configuration_<wbr>deserializer_<wbr>open_<wbr>x_<wbr>json_<wbr>ser_<wbr>de]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument that specifies the OpenX SerDe. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDeArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerHiveJsonSerDe.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Timestamp<wbr>Formats</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of how you want Kinesis Data Firehose to parse the date and time stamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime&#39;s DateTimeFormat format strings. For more information, see [Class DateTimeFormat](https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html). You can also use the special value millis to parse time stamps in epoch milliseconds. If you don&#39;t specify a format, Kinesis Data Firehose uses java.sql.Timestamp::valueOf by default.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Timestamp<wbr>Formats</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of how you want Kinesis Data Firehose to parse the date and time stamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime&#39;s DateTimeFormat format strings. For more information, see [Class DateTimeFormat](https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html). You can also use the special value millis to parse time stamps in epoch milliseconds. If you don&#39;t specify a format, Kinesis Data Firehose uses java.sql.Timestamp::valueOf by default.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">timestamp<wbr>Formats</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of how you want Kinesis Data Firehose to parse the date and time stamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime&#39;s DateTimeFormat format strings. For more information, see [Class DateTimeFormat](https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html). You can also use the special value millis to parse time stamps in epoch milliseconds. If you don&#39;t specify a format, Kinesis Data Firehose uses java.sql.Timestamp::valueOf by default.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">timestamp_<wbr>formats</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of how you want Kinesis Data Firehose to parse the date and time stamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime&#39;s DateTimeFormat format strings. For more information, see [Class DateTimeFormat](https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html). You can also use the special value millis to parse time stamps in epoch milliseconds. If you don&#39;t specify a format, Kinesis Data Firehose uses java.sql.Timestamp::valueOf by default.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDeArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationInputFormatConfigurationDeserializerOpenXJsonSerDe.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Case<wbr>Insensitive</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to true, which is the default, Kinesis Data Firehose converts JSON keys to lowercase before deserializing them.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Column<wbr>To<wbr>Json<wbr>Key<wbr>Mappings</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of column names to JSON keys that aren&#39;t identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, timestamp is a Hive keyword. If you have a JSON key named timestamp, set this parameter to `{ ts = &#34;timestamp&#34; }` to map this key to a column named ts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Convert<wbr>Dots<wbr>In<wbr>Json<wbr>Keys<wbr>To<wbr>Underscores</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to `true`, specifies that the names of the keys include dots and that you want Kinesis Data Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is &#34;a.b&#34;, you can define the column name to be &#34;a_b&#34; when using this option. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Case<wbr>Insensitive</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to true, which is the default, Kinesis Data Firehose converts JSON keys to lowercase before deserializing them.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Column<wbr>To<wbr>Json<wbr>Key<wbr>Mappings</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of column names to JSON keys that aren&#39;t identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, timestamp is a Hive keyword. If you have a JSON key named timestamp, set this parameter to `{ ts = &#34;timestamp&#34; }` to map this key to a column named ts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Convert<wbr>Dots<wbr>In<wbr>Json<wbr>Keys<wbr>To<wbr>Underscores</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to `true`, specifies that the names of the keys include dots and that you want Kinesis Data Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is &#34;a.b&#34;, you can define the column name to be &#34;a_b&#34; when using this option. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">case<wbr>Insensitive</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to true, which is the default, Kinesis Data Firehose converts JSON keys to lowercase before deserializing them.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">column<wbr>To<wbr>Json<wbr>Key<wbr>Mappings</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of column names to JSON keys that aren&#39;t identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, timestamp is a Hive keyword. If you have a JSON key named timestamp, set this parameter to `{ ts = &#34;timestamp&#34; }` to map this key to a column named ts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">convert<wbr>Dots<wbr>In<wbr>Json<wbr>Keys<wbr>To<wbr>Underscores</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to `true`, specifies that the names of the keys include dots and that you want Kinesis Data Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is &#34;a.b&#34;, you can define the column name to be &#34;a_b&#34; when using this option. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">case_<wbr>insensitive</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to true, which is the default, Kinesis Data Firehose converts JSON keys to lowercase before deserializing them.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">column_<wbr>to_<wbr>json_<wbr>key_<wbr>mappings</td>
            <td class="align-top">
                
                <code>Dict[str, str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of column names to JSON keys that aren&#39;t identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, timestamp is a Hive keyword. If you have a JSON key named timestamp, set this parameter to `{ ts = &#34;timestamp&#34; }` to map this key to a column named ts.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">convert_<wbr>dots_<wbr>in_<wbr>json_<wbr>keys_<wbr>to_<wbr>underscores</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When set to `true`, specifies that the names of the keys include dots and that you want Kinesis Data Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is &#34;a.b&#34;, you can define the column name to be &#34;a_b&#34; when using this option. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Serializer</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationoutputformatconfigurationserializer">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Output<wbr>Format<wbr>Configuration<wbr>Serializer<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Serializer</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationoutputformatconfigurationserializer">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Output<wbr>Format<wbr>Configuration<wbr>Serializer</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">serializer</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationoutputformatconfigurationserializer">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Output<wbr>Format<wbr>Configuration<wbr>Serializer</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">serializer</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationoutputformatconfigurationserializer">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration_<wbr>data_<wbr>format_<wbr>conversion_<wbr>configuration_<wbr>output_<wbr>format_<wbr>configuration_<wbr>serializer]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument that specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializer.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Orc<wbr>Ser<wbr>De</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationoutputformatconfigurationserializerorcserde">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Output<wbr>Format<wbr>Configuration<wbr>Serializer<wbr>Orc<wbr>Ser<wbr>De<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument that specifies converting data to the ORC format before storing it in Amazon S3. For more information, see [Apache ORC](https://orc.apache.org/docs/). More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parquet<wbr>Ser<wbr>De</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationoutputformatconfigurationserializerparquetserde">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Output<wbr>Format<wbr>Configuration<wbr>Serializer<wbr>Parquet<wbr>Ser<wbr>De<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument that specifies converting data to the Parquet format before storing it in Amazon S3. For more information, see [Apache Parquet](https://parquet.apache.org/documentation/latest/). More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Orc<wbr>Ser<wbr>De</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationoutputformatconfigurationserializerorcserde">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Output<wbr>Format<wbr>Configuration<wbr>Serializer<wbr>Orc<wbr>Ser<wbr>De</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument that specifies converting data to the ORC format before storing it in Amazon S3. For more information, see [Apache ORC](https://orc.apache.org/docs/). More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parquet<wbr>Ser<wbr>De</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationoutputformatconfigurationserializerparquetserde">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Output<wbr>Format<wbr>Configuration<wbr>Serializer<wbr>Parquet<wbr>Ser<wbr>De</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument that specifies converting data to the Parquet format before storing it in Amazon S3. For more information, see [Apache Parquet](https://parquet.apache.org/documentation/latest/). More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">orc<wbr>Ser<wbr>De</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationoutputformatconfigurationserializerorcserde">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Output<wbr>Format<wbr>Configuration<wbr>Serializer<wbr>Orc<wbr>Ser<wbr>De?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument that specifies converting data to the ORC format before storing it in Amazon S3. For more information, see [Apache ORC](https://orc.apache.org/docs/). More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parquet<wbr>Ser<wbr>De</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationoutputformatconfigurationserializerparquetserde">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Data<wbr>Format<wbr>Conversion<wbr>Configuration<wbr>Output<wbr>Format<wbr>Configuration<wbr>Serializer<wbr>Parquet<wbr>Ser<wbr>De?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument that specifies converting data to the Parquet format before storing it in Amazon S3. For more information, see [Apache Parquet](https://parquet.apache.org/documentation/latest/). More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">orc_<wbr>ser_<wbr>de</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationoutputformatconfigurationserializerorcserde">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration_<wbr>data_<wbr>format_<wbr>conversion_<wbr>configuration_<wbr>output_<wbr>format_<wbr>configuration_<wbr>serializer_<wbr>orc_<wbr>ser_<wbr>de]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument that specifies converting data to the ORC format before storing it in Amazon S3. For more information, see [Apache ORC](https://orc.apache.org/docs/). More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parquet_<wbr>ser_<wbr>de</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationdataformatconversionconfigurationoutputformatconfigurationserializerparquetserde">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration_<wbr>data_<wbr>format_<wbr>conversion_<wbr>configuration_<wbr>output_<wbr>format_<wbr>configuration_<wbr>serializer_<wbr>parquet_<wbr>ser_<wbr>de]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument that specifies converting data to the Parquet format before storing it in Amazon S3. For more information, see [Apache Parquet](https://parquet.apache.org/documentation/latest/). More details below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDeArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerOrcSerDe.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Block<wbr>Size<wbr>Bytes</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bloom<wbr>Filter<wbr>Columns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of column names for which you want Kinesis Data Firehose to create bloom filters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bloom<wbr>Filter<wbr>False<wbr>Positive<wbr>Probability</td>
            <td class="align-top">
                
                <code>double?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is `0.05`, the minimum is `0`, and the maximum is `1`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression code to use over data blocks. The possible values are `UNCOMPRESSED`, `SNAPPY`, and `GZIP`, with the default being `SNAPPY`. Use `SNAPPY` for higher decompression speed. Use `GZIP` if the compression ratio is more important than speed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dictionary<wbr>Key<wbr>Threshold</td>
            <td class="align-top">
                
                <code>double?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A float that represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to `1`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Padding</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set this to `true` to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Format<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of the file to write. The possible values are `V0_11` and `V0_12`. The default is `V0_12`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Padding<wbr>Tolerance</td>
            <td class="align-top">
                
                <code>double?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A float between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is `0.05`, which means 5 percent of stripe size. For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task. Kinesis Data Firehose ignores this parameter when `enable_padding` is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Row<wbr>Index<wbr>Stride</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of rows between index entries. The default is `10000` and the minimum is `1000`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stripe<wbr>Size<wbr>Bytes</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Block<wbr>Size<wbr>Bytes</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bloom<wbr>Filter<wbr>Columns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of column names for which you want Kinesis Data Firehose to create bloom filters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bloom<wbr>Filter<wbr>False<wbr>Positive<wbr>Probability</td>
            <td class="align-top">
                
                <code>*float64</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is `0.05`, the minimum is `0`, and the maximum is `1`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression code to use over data blocks. The possible values are `UNCOMPRESSED`, `SNAPPY`, and `GZIP`, with the default being `SNAPPY`. Use `SNAPPY` for higher decompression speed. Use `GZIP` if the compression ratio is more important than speed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dictionary<wbr>Key<wbr>Threshold</td>
            <td class="align-top">
                
                <code>*float64</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A float that represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to `1`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Padding</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set this to `true` to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Format<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of the file to write. The possible values are `V0_11` and `V0_12`. The default is `V0_12`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Padding<wbr>Tolerance</td>
            <td class="align-top">
                
                <code>*float64</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A float between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is `0.05`, which means 5 percent of stripe size. For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task. Kinesis Data Firehose ignores this parameter when `enable_padding` is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Row<wbr>Index<wbr>Stride</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of rows between index entries. The default is `10000` and the minimum is `1000`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stripe<wbr>Size<wbr>Bytes</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">block<wbr>Size<wbr>Bytes</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bloom<wbr>Filter<wbr>Columns</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of column names for which you want Kinesis Data Firehose to create bloom filters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bloom<wbr>Filter<wbr>False<wbr>Positive<wbr>Probability</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is `0.05`, the minimum is `0`, and the maximum is `1`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression code to use over data blocks. The possible values are `UNCOMPRESSED`, `SNAPPY`, and `GZIP`, with the default being `SNAPPY`. Use `SNAPPY` for higher decompression speed. Use `GZIP` if the compression ratio is more important than speed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dictionary<wbr>Key<wbr>Threshold</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A float that represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to `1`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Padding</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set this to `true` to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">format<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of the file to write. The possible values are `V0_11` and `V0_12`. The default is `V0_12`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">padding<wbr>Tolerance</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A float between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is `0.05`, which means 5 percent of stripe size. For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task. Kinesis Data Firehose ignores this parameter when `enable_padding` is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">row<wbr>Index<wbr>Stride</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of rows between index entries. The default is `10000` and the minimum is `1000`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stripe<wbr>Size<wbr>Bytes</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">block_<wbr>size_<wbr>bytes</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bloom_<wbr>filter_<wbr>columns</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of column names for which you want Kinesis Data Firehose to create bloom filters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bloom_<wbr>filter_<wbr>false_<wbr>positive_<wbr>probability</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is `0.05`, the minimum is `0`, and the maximum is `1`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression code to use over data blocks. The possible values are `UNCOMPRESSED`, `SNAPPY`, and `GZIP`, with the default being `SNAPPY`. Use `SNAPPY` for higher decompression speed. Use `GZIP` if the compression ratio is more important than speed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dictionary_<wbr>key_<wbr>threshold</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A float that represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to `1`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>padding</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set this to `true` to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">format_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of the file to write. The possible values are `V0_11` and `V0_12`. The default is `V0_12`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">padding_<wbr>tolerance</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A float between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is `0.05`, which means 5 percent of stripe size. For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task. Kinesis Data Firehose ignores this parameter when `enable_padding` is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">row_<wbr>index_<wbr>stride</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of rows between index entries. The default is `10000` and the minimum is `1000`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stripe_<wbr>size_<wbr>bytes</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDeArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationOutputFormatConfigurationSerializerParquetSerDe.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Block<wbr>Size<wbr>Bytes</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression code to use over data blocks. The possible values are `UNCOMPRESSED`, `SNAPPY`, and `GZIP`, with the default being `SNAPPY`. Use `SNAPPY` for higher decompression speed. Use `GZIP` if the compression ratio is more important than speed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Dictionary<wbr>Compression</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether to enable dictionary compression.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Padding<wbr>Bytes</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is `0`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Page<wbr>Size<wbr>Bytes</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Writer<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates the version of row format to output. The possible values are `V1` and `V2`. The default is `V1`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Block<wbr>Size<wbr>Bytes</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression code to use over data blocks. The possible values are `UNCOMPRESSED`, `SNAPPY`, and `GZIP`, with the default being `SNAPPY`. Use `SNAPPY` for higher decompression speed. Use `GZIP` if the compression ratio is more important than speed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Dictionary<wbr>Compression</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether to enable dictionary compression.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Padding<wbr>Bytes</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is `0`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Page<wbr>Size<wbr>Bytes</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Writer<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates the version of row format to output. The possible values are `V1` and `V2`. The default is `V1`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">block<wbr>Size<wbr>Bytes</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression code to use over data blocks. The possible values are `UNCOMPRESSED`, `SNAPPY`, and `GZIP`, with the default being `SNAPPY`. Use `SNAPPY` for higher decompression speed. Use `GZIP` if the compression ratio is more important than speed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Dictionary<wbr>Compression</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether to enable dictionary compression.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Padding<wbr>Bytes</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is `0`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">page<wbr>Size<wbr>Bytes</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">writer<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates the version of row format to output. The possible values are `V1` and `V2`. The default is `V1`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">block_<wbr>size_<wbr>bytes</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression code to use over data blocks. The possible values are `UNCOMPRESSED`, `SNAPPY`, and `GZIP`, with the default being `SNAPPY`. Use `SNAPPY` for higher decompression speed. Use `GZIP` if the compression ratio is more important than speed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>dictionary_<wbr>compression</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether to enable dictionary compression.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>padding_<wbr>bytes</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is `0`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">page_<wbr>size_<wbr>bytes</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">writer_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates the version of row format to output. The possible values are `V1` and `V2`. The default is `V1`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationDataFormatConversionConfigurationSchemaConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Catalog<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS Glue Data Catalog. If you don&#39;t supply this, the AWS account ID is used by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Database<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the name of the AWS Glue database that contains the schema for the output data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you don&#39;t specify an AWS Region, the default is the current region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Table<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the AWS Glue table that contains the column information that constitutes your data schema.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the table version for the output data schema. Defaults to `LATEST`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Catalog<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS Glue Data Catalog. If you don&#39;t supply this, the AWS account ID is used by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Database<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the name of the AWS Glue database that contains the schema for the output data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Region</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you don&#39;t specify an AWS Region, the default is the current region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Table<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the AWS Glue table that contains the column information that constitutes your data schema.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the table version for the output data schema. Defaults to `LATEST`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">catalog<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS Glue Data Catalog. If you don&#39;t supply this, the AWS account ID is used by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">database<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the name of the AWS Glue database that contains the schema for the output data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you don&#39;t specify an AWS Region, the default is the current region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">table<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the AWS Glue table that contains the column information that constitutes your data schema.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the table version for the output data schema. Defaults to `LATEST`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">catalog_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the AWS Glue Data Catalog. If you don&#39;t supply this, the AWS account ID is used by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">database_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the name of the AWS Glue database that contains the schema for the output data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you don&#39;t specify an AWS Region, the default is the current region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">table_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the AWS Glue table that contains the column information that constitutes your data schema.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the table version for the output data schema. Defaults to `LATEST`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Processors</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationprocessingconfigurationprocessor">List&lt;Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Processing<wbr>Configuration<wbr>Processor<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of data processors. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Processors</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationprocessingconfigurationprocessor">[]kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Processing<wbr>Configuration<wbr>Processor</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of data processors. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">processors</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationprocessingconfigurationprocessor">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Processing<wbr>Configuration<wbr>Processor[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of data processors. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">processors</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationprocessingconfigurationprocessor">List[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration_<wbr>processing_<wbr>configuration_<wbr>processor]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of data processors. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessor
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessor">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessor">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessor.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationprocessingconfigurationprocessorparameter">List&lt;Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Processing<wbr>Configuration<wbr>Processor<wbr>Parameter<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of processor parameters. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of processor. Valid Values: `Lambda`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationprocessingconfigurationprocessorparameter">[]kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Processing<wbr>Configuration<wbr>Processor<wbr>Parameter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of processor parameters. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of processor. Valid Values: `Lambda`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationprocessingconfigurationprocessorparameter">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>Processing<wbr>Configuration<wbr>Processor<wbr>Parameter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of processor parameters. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of processor. Valid Values: `Lambda`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurationprocessingconfigurationprocessorparameter">List[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration_<wbr>processing_<wbr>configuration_<wbr>processor_<wbr>parameter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of processor parameters. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of processor. Valid Values: `Lambda`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorParameter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorParameter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorParameter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorParameterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorParameterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorParameterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationProcessingConfigurationProcessorParameter.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Parameter<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Parameter<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">parameter<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">parameter_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter_<wbr>value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffer<wbr>Interval</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffer<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurations3backupconfigurationcloudwatchloggingoptions">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>S3Backup<wbr>Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression<wbr>Format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;YYYY/MM/DD/HH&#34; time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffer<wbr>Interval</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffer<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurations3backupconfigurationcloudwatchloggingoptions">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>S3Backup<wbr>Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression<wbr>Format</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;YYYY/MM/DD/HH&#34; time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffer<wbr>Interval</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffer<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurations3backupconfigurationcloudwatchloggingoptions">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Extended<wbr>S3Configuration<wbr>S3Backup<wbr>Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression<wbr>Format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;YYYY/MM/DD/HH&#34; time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffer_<wbr>interval</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffer_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch_<wbr>logging_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamextendeds3configurations3backupconfigurationcloudwatchloggingoptions">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>extended_<wbr>s3_<wbr>configuration_<wbr>s3_<wbr>backup_<wbr>configuration_<wbr>cloudwatch_<wbr>logging_<wbr>options]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression_<wbr>format</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;YYYY/MM/DD/HH&#34; time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationS3BackupConfigurationCloudwatchLoggingOptions.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>stream_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamKinesisSourceConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamKinesisSourceConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamKinesisSourceConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamKinesisSourceConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamKinesisSourceConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamKinesisSourceConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamKinesisSourceConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Stream<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The kinesis stream used as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Stream<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The kinesis stream used as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">kinesis<wbr>Stream<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The kinesis stream used as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">kinesis_<wbr>stream_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The kinesis stream used as the source of the firehose delivery stream.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamRedshiftConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamRedshiftConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamRedshiftConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamRedshiftConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamRedshiftConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamRedshiftConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamRedshiftConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurationcloudwatchloggingoptions">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Jdbcurl</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The jdbcurl of the redshift cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Copy<wbr>Options</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Copy options for copying the data from the s3 intermediate bucket into redshift, for example to change the default delimiter. For valid values, see the [AWS documentation](http://docs.aws.amazon.com/firehose/latest/APIReference/API_CopyCommand.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Data<wbr>Table<wbr>Columns</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data table columns that will be targeted by the copy command.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Data<wbr>Table<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the table in the redshift cluster that the s3 bucket will copy to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The password for the username above.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Processing<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurationprocessingconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data processing configuration.  More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retry<wbr>Duration</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
After an initial failure to deliver to Splunk, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Backup<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurations3backupconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>S3Backup<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for backup in Amazon S3. Required if `s3_backup_mode` is `Enabled`. Supports the same fields as `s3_configuration` object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Backup<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Username</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The username that the firehose delivery stream will assume. It is strongly recommended that the username and password provided is used exclusively for Amazon Kinesis Firehose purposes, and that the permissions for the account are restricted for Amazon Redshift INSERT permissions.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurationcloudwatchloggingoptions">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Jdbcurl</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The jdbcurl of the redshift cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Copy<wbr>Options</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Copy options for copying the data from the s3 intermediate bucket into redshift, for example to change the default delimiter. For valid values, see the [AWS documentation](http://docs.aws.amazon.com/firehose/latest/APIReference/API_CopyCommand.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Data<wbr>Table<wbr>Columns</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data table columns that will be targeted by the copy command.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Data<wbr>Table<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the table in the redshift cluster that the s3 bucket will copy to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The password for the username above.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Processing<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurationprocessingconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>Processing<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data processing configuration.  More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retry<wbr>Duration</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
After an initial failure to deliver to Splunk, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Backup<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurations3backupconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>S3Backup<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for backup in Amazon S3. Required if `s3_backup_mode` is `Enabled`. Supports the same fields as `s3_configuration` object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Backup<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Username</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The username that the firehose delivery stream will assume. It is strongly recommended that the username and password provided is used exclusively for Amazon Kinesis Firehose purposes, and that the permissions for the account are restricted for Amazon Redshift INSERT permissions.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurationcloudwatchloggingoptions">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Jdbcurl</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The jdbcurl of the redshift cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">copy<wbr>Options</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Copy options for copying the data from the s3 intermediate bucket into redshift, for example to change the default delimiter. For valid values, see the [AWS documentation](http://docs.aws.amazon.com/firehose/latest/APIReference/API_CopyCommand.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">data<wbr>Table<wbr>Columns</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data table columns that will be targeted by the copy command.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">data<wbr>Table<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the table in the redshift cluster that the s3 bucket will copy to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The password for the username above.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">processing<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurationprocessingconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>Processing<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data processing configuration.  More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retry<wbr>Duration</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
After an initial failure to deliver to Splunk, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Backup<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurations3backupconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>S3Backup<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for backup in Amazon S3. Required if `s3_backup_mode` is `Enabled`. Supports the same fields as `s3_configuration` object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Backup<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">username</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The username that the firehose delivery stream will assume. It is strongly recommended that the username and password provided is used exclusively for Amazon Kinesis Firehose purposes, and that the permissions for the account are restricted for Amazon Redshift INSERT permissions.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">cloudwatch_<wbr>logging_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurationcloudwatchloggingoptions">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>redshift_<wbr>configuration_<wbr>cloudwatch_<wbr>logging_<wbr>options]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>jdbcurl</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The jdbcurl of the redshift cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">copy_<wbr>options</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Copy options for copying the data from the s3 intermediate bucket into redshift, for example to change the default delimiter. For valid values, see the [AWS documentation](http://docs.aws.amazon.com/firehose/latest/APIReference/API_CopyCommand.html)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">data_<wbr>table_<wbr>columns</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data table columns that will be targeted by the copy command.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">data_<wbr>table_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the table in the redshift cluster that the s3 bucket will copy to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The password for the username above.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">processing_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurationprocessingconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>redshift_<wbr>configuration_<wbr>processing_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data processing configuration.  More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retry_<wbr>duration</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
After an initial failure to deliver to Splunk, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>backup_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurations3backupconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>redshift_<wbr>configuration_<wbr>s3_<wbr>backup_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for backup in Amazon S3. Required if `s3_backup_mode` is `Enabled`. Supports the same fields as `s3_configuration` object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>backup_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">username</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The username that the firehose delivery stream will assume. It is strongly recommended that the username and password provided is used exclusively for Amazon Kinesis Firehose purposes, and that the permissions for the account are restricted for Amazon Redshift INSERT permissions.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamRedshiftConfigurationCloudwatchLoggingOptions.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>stream_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamRedshiftConfigurationProcessingConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Processors</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurationprocessingconfigurationprocessor">List&lt;Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of data processors. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Processors</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurationprocessingconfigurationprocessor">[]kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of data processors. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">processors</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurationprocessingconfigurationprocessor">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of data processors. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">processors</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurationprocessingconfigurationprocessor">List[firehose_<wbr>delivery_<wbr>stream_<wbr>redshift_<wbr>configuration_<wbr>processing_<wbr>configuration_<wbr>processor]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of data processors. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessor
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessor">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessor">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessor.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurationprocessingconfigurationprocessorparameter">List&lt;Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor<wbr>Parameter<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of processor parameters. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of processor. Valid Values: `Lambda`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurationprocessingconfigurationprocessorparameter">[]kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor<wbr>Parameter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of processor parameters. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of processor. Valid Values: `Lambda`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurationprocessingconfigurationprocessorparameter">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor<wbr>Parameter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of processor parameters. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of processor. Valid Values: `Lambda`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurationprocessingconfigurationprocessorparameter">List[firehose_<wbr>delivery_<wbr>stream_<wbr>redshift_<wbr>configuration_<wbr>processing_<wbr>configuration_<wbr>processor_<wbr>parameter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of processor parameters. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of processor. Valid Values: `Lambda`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorParameter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorParameter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorParameter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorParameterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorParameterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorParameterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamRedshiftConfigurationProcessingConfigurationProcessorParameter.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Parameter<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Parameter<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">parameter<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">parameter_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter_<wbr>value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffer<wbr>Interval</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffer<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurations3backupconfigurationcloudwatchloggingoptions">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>S3Backup<wbr>Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression<wbr>Format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;YYYY/MM/DD/HH&#34; time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffer<wbr>Interval</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffer<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurations3backupconfigurationcloudwatchloggingoptions">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>S3Backup<wbr>Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression<wbr>Format</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;YYYY/MM/DD/HH&#34; time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffer<wbr>Interval</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffer<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurations3backupconfigurationcloudwatchloggingoptions">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Redshift<wbr>Configuration<wbr>S3Backup<wbr>Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression<wbr>Format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;YYYY/MM/DD/HH&#34; time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffer_<wbr>interval</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffer_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch_<wbr>logging_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamredshiftconfigurations3backupconfigurationcloudwatchloggingoptions">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>redshift_<wbr>configuration_<wbr>s3_<wbr>backup_<wbr>configuration_<wbr>cloudwatch_<wbr>logging_<wbr>options]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression_<wbr>format</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;YYYY/MM/DD/HH&#34; time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamRedshiftConfigurationS3BackupConfigurationCloudwatchLoggingOptions.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>stream_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamS3Configuration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamS3Configuration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamS3Configuration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamS3ConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamS3ConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamS3ConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamS3Configuration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffer<wbr>Interval</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffer<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreams3configurationcloudwatchloggingoptions">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>S3Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression<wbr>Format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;YYYY/MM/DD/HH&#34; time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffer<wbr>Interval</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Buffer<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreams3configurationcloudwatchloggingoptions">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>S3Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compression<wbr>Format</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;YYYY/MM/DD/HH&#34; time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffer<wbr>Interval</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffer<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreams3configurationcloudwatchloggingoptions">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>S3Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression<wbr>Format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;YYYY/MM/DD/HH&#34; time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffer_<wbr>interval</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">buffer_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting SizeInMBs to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec set SizeInMBs to be 10 MB or higher.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch_<wbr>logging_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreams3configurationcloudwatchloggingoptions">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>s3_<wbr>configuration_<wbr>cloudwatch_<wbr>logging_<wbr>options]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compression_<wbr>format</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compression format. If no value is specified, the default is UNCOMPRESSED. Other supported values are GZIP, ZIP &amp; Snappy. If the destination is redshift you cannot use ZIP or Snappy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the KMS key ARN the stream will use to encrypt data. If not set, no encryption will
be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;YYYY/MM/DD/HH&#34; time format prefix is automatically used for delivered S3 files. You can specify an extra prefix to be added in front of the time format prefix. Note that if the prefix ends with a slash, it appears as a folder in the S3 bucket
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren&#39;t allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamS3ConfigurationCloudwatchLoggingOptions.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>stream_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamServerSideEncryption
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamServerSideEncryption">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamServerSideEncryption">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamServerSideEncryptionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamServerSideEncryptionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamServerSideEncryptionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamServerSideEncryption.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamSplunkConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamSplunkConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamSplunkConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamSplunkConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamSplunkConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamSplunkConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamSplunkConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfigurationcloudwatchloggingoptions">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hec<wbr>Acknowledgment<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds between 180 and 600, that Kinesis Firehose waits to receive an acknowledgment from Splunk after it sends it data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hec<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP Event Collector (HEC) endpoint to which Kinesis Firehose sends your data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hec<wbr>Endpoint<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HEC endpoint type. Valid values are `Raw` or `Event`. The default value is `Raw`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hec<wbr>Token</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Processing<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfigurationprocessingconfiguration">Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data processing configuration.  More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retry<wbr>Duration</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
After an initial failure to deliver to Splunk, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Backup<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfigurationcloudwatchloggingoptions">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hec<wbr>Acknowledgment<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds between 180 and 600, that Kinesis Firehose waits to receive an acknowledgment from Splunk after it sends it data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hec<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP Event Collector (HEC) endpoint to which Kinesis Firehose sends your data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hec<wbr>Endpoint<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HEC endpoint type. Valid values are `Raw` or `Event`. The default value is `Raw`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hec<wbr>Token</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Processing<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfigurationprocessingconfiguration">*kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration<wbr>Processing<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data processing configuration.  More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retry<wbr>Duration</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
After an initial failure to deliver to Splunk, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Backup<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">cloudwatch<wbr>Logging<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfigurationcloudwatchloggingoptions">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration<wbr>Cloudwatch<wbr>Logging<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hec<wbr>Acknowledgment<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds between 180 and 600, that Kinesis Firehose waits to receive an acknowledgment from Splunk after it sends it data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hec<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP Event Collector (HEC) endpoint to which Kinesis Firehose sends your data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hec<wbr>Endpoint<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HEC endpoint type. Valid values are `Raw` or `Event`. The default value is `Raw`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hec<wbr>Token</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">processing<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfigurationprocessingconfiguration">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration<wbr>Processing<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data processing configuration.  More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retry<wbr>Duration</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
After an initial failure to deliver to Splunk, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Backup<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">cloudwatch_<wbr>logging_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfigurationcloudwatchloggingoptions">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>splunk_<wbr>configuration_<wbr>cloudwatch_<wbr>logging_<wbr>options]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch Logging Options for the delivery stream. More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hec_<wbr>acknowledgment_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds between 180 and 600, that Kinesis Firehose waits to receive an acknowledgment from Splunk after it sends it data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hec_<wbr>endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP Event Collector (HEC) endpoint to which Kinesis Firehose sends your data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hec_<wbr>endpoint_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HEC endpoint type. Valid values are `Raw` or `Event`. The default value is `Raw`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hec_<wbr>token</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">processing_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfigurationprocessingconfiguration">Dict[firehose_<wbr>delivery_<wbr>stream_<wbr>splunk_<wbr>configuration_<wbr>processing_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The data processing configuration.  More details are given below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retry_<wbr>duration</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
After an initial failure to deliver to Splunk, the total amount of time, in seconds between 0 to 7200, during which Firehose re-attempts delivery (including the first attempt).  After this time has elapsed, the failed documents are written to Amazon S3.  The default value is 300s.  There will be no retry if the value is 0.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>backup_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines how documents should be delivered to Amazon S3.  Valid values are `FailedEventsOnly` and `AllEvents`.  Default value is `FailedEventsOnly`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamSplunkConfigurationCloudwatchLoggingOptions.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch group name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">log_<wbr>stream_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CloudWatch log stream name for logging. This value is required if `enabled` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamSplunkConfigurationProcessingConfiguration.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Processors</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfigurationprocessingconfigurationprocessor">List&lt;Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of data processors. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Processors</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfigurationprocessingconfigurationprocessor">[]kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of data processors. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">processors</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfigurationprocessingconfigurationprocessor">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of data processors. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">processors</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfigurationprocessingconfigurationprocessor">List[firehose_<wbr>delivery_<wbr>stream_<wbr>splunk_<wbr>configuration_<wbr>processing_<wbr>configuration_<wbr>processor]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of data processors. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessor
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessor">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessor">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessor.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfigurationprocessingconfigurationprocessorparameter">List&lt;Pulumi.<wbr>Aws.<wbr>Kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor<wbr>Parameter<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of processor parameters. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of processor. Valid Values: `Lambda`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfigurationprocessingconfigurationprocessorparameter">[]kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor<wbr>Parameter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of processor parameters. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of processor. Valid Values: `Lambda`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfigurationprocessingconfigurationprocessorparameter">kinesis.<wbr>Firehose<wbr>Delivery<wbr>Stream<wbr>Splunk<wbr>Configuration<wbr>Processing<wbr>Configuration<wbr>Processor<wbr>Parameter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of processor parameters. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of processor. Valid Values: `Lambda`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code><a href="#firehosedeliverystreamsplunkconfigurationprocessingconfigurationprocessorparameter">List[firehose_<wbr>delivery_<wbr>stream_<wbr>splunk_<wbr>configuration_<wbr>processing_<wbr>configuration_<wbr>processor_<wbr>parameter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Array of processor parameters. More details are given below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of processor. Valid Values: `Lambda`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorParameter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorParameter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorParameter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorParameterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorParameterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorParameterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.FirehoseDeliveryStreamSplunkConfigurationProcessingConfigurationProcessorParameter.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Parameter<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Parameter<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">parameter<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">parameter_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter name. Valid Values: `LambdaArn`, `NumberOfRetries`, `RoleArn`, `BufferSizeInMBs`, `BufferIntervalInSeconds`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter_<wbr>value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Parameter value. Must be between 1 and 512 length (inclusive). When providing a Lambda ARN, you should specify the resource version as well.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







