
---
title: "AnalyticsApplication"
block_external_search_index: true
---



Provides a Kinesis Analytics Application resource. Kinesis Analytics is a managed service that
allows processing and analyzing streaming data using standard SQL.

For more details, see the [Amazon Kinesis Analytics Documentation][1].

{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const testStream = new aws.kinesis.Stream("test_stream", {
    shardCount: 1,
});
const testApplication = new aws.kinesis.AnalyticsApplication("test_application", {
    inputs: {
        kinesisStream: {
            resourceArn: testStream.arn,
            roleArn: aws_iam_role_test.arn,
        },
        namePrefix: "test_prefix",
        parallelism: {
            count: 1,
        },
        schema: {
            recordColumns: [{
                mapping: "$.test",
                name: "test",
                sqlType: "VARCHAR(8)",
            }],
            recordEncoding: "UTF-8",
            recordFormat: {
                mappingParameters: {
                    json: {
                        recordRowPath: "$",
                    },
                },
            },
        },
    },
});
```

{{% /example %}}
{{% /examples %}}



## Create a AnalyticsApplication Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/kinesis/#AnalyticsApplication">AnalyticsApplication</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/kinesis/#AnalyticsApplicationArgs">AnalyticsApplicationArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">AnalyticsApplication</span><span class="p">(resource_name, opts=None, </span>cloudwatch_logging_options=None<span class="p">, </span>code=None<span class="p">, </span>description=None<span class="p">, </span>inputs=None<span class="p">, </span>name=None<span class="p">, </span>outputs=None<span class="p">, </span>reference_data_sources=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewAnalyticsApplication<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationArgs">AnalyticsApplicationArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplication">AnalyticsApplication</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.AnalyticsApplication.html">AnalyticsApplication</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.AnalyticsApplicationArgs.html">AnalyticsApplicationArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Cloudwatch<wbr>Logging<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationcloudwatchloggingoptions">Analytics<wbr>Application<wbr>Cloudwatch<wbr>Logging<wbr>Options<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The CloudWatch log stream options to monitor application errors.
See CloudWatch Logging Options below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SQL Code to transform input data, and generate output.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inputs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputs">Analytics<wbr>Application<wbr>Inputs<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Input configuration of the application. See Inputs below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Outputs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutput">List&lt;Analytics<wbr>Application<wbr>Output<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Output destination configuration of the application. See Outputs below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reference<wbr>Data<wbr>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasources">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}An S3 Reference Data Source for the application.
See Reference Data Sources below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of tags for the Kinesis Analytics Application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cloudwatch<wbr>Logging<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationcloudwatchloggingoptions">Analytics<wbr>Application<wbr>Cloudwatch<wbr>Logging<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}The CloudWatch log stream options to monitor application errors.
See CloudWatch Logging Options below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SQL Code to transform input data, and generate output.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inputs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputs">Analytics<wbr>Application<wbr>Inputs</a></span>
    </dt>
    <dd>{{% md %}}Input configuration of the application. See Inputs below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Outputs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutput">[]Analytics<wbr>Application<wbr>Output</a></span>
    </dt>
    <dd>{{% md %}}Output destination configuration of the application. See Outputs below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reference<wbr>Data<wbr>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasources">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources</a></span>
    </dt>
    <dd>{{% md %}}An S3 Reference Data Source for the application.
See Reference Data Sources below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of tags for the Kinesis Analytics Application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cloudwatch<wbr>Logging<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationcloudwatchloggingoptions">Analytics<wbr>Application<wbr>Cloudwatch<wbr>Logging<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}The CloudWatch log stream options to monitor application errors.
See CloudWatch Logging Options below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SQL Code to transform input data, and generate output.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inputs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputs">Analytics<wbr>Application<wbr>Inputs</a></span>
    </dt>
    <dd>{{% md %}}Input configuration of the application. See Inputs below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>outputs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutput">Analytics<wbr>Application<wbr>Output[]</a></span>
    </dt>
    <dd>{{% md %}}Output destination configuration of the application. See Outputs below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reference<wbr>Data<wbr>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasources">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources</a></span>
    </dt>
    <dd>{{% md %}}An S3 Reference Data Source for the application.
See Reference Data Sources below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of tags for the Kinesis Analytics Application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cloudwatch_<wbr>logging_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationcloudwatchloggingoptions">Dict[Analytics<wbr>Application<wbr>Cloudwatch<wbr>Logging<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}The CloudWatch log stream options to monitor application errors.
See CloudWatch Logging Options below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}SQL Code to transform input data, and generate output.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inputs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputs">Dict[Analytics<wbr>Application<wbr>Inputs]</a></span>
    </dt>
    <dd>{{% md %}}Input configuration of the application. See Inputs below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>outputs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutput">List[Analytics<wbr>Application<wbr>Output]</a></span>
    </dt>
    <dd>{{% md %}}Output destination configuration of the application. See Outputs below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reference_<wbr>data_<wbr>sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasources">Dict[Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources]</a></span>
    </dt>
    <dd>{{% md %}}An S3 Reference Data Source for the application.
See Reference Data Sources below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of tags for the Kinesis Analytics Application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## AnalyticsApplication Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Appliation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Create<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Timestamp when the application version was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Last<wbr>Update<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Timestamp when the application was last updated.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Status of the application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Version of the application.
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
    <dd>{{% md %}}The ARN of the Kinesis Analytics Appliation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Create<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Timestamp when the application version was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Last<wbr>Update<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Timestamp when the application was last updated.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Status of the application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Version of the application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">ARN</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Appliation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>create<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Timestamp when the application version was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>last<wbr>Update<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Timestamp when the application was last updated.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Status of the application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The Version of the application.
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
    <dd>{{% md %}}The ARN of the Kinesis Analytics Appliation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>create_<wbr>timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Timestamp when the application version was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>last_<wbr>update_<wbr>timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Timestamp when the application was last updated.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Status of the application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The Version of the application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing AnalyticsApplication Resource

Get an existing AnalyticsApplication resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/kinesis/#AnalyticsApplicationState">AnalyticsApplicationState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/kinesis/#AnalyticsApplication">AnalyticsApplication</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>cloudwatch_logging_options=None<span class="p">, </span>code=None<span class="p">, </span>create_timestamp=None<span class="p">, </span>description=None<span class="p">, </span>inputs=None<span class="p">, </span>last_update_timestamp=None<span class="p">, </span>name=None<span class="p">, </span>outputs=None<span class="p">, </span>reference_data_sources=None<span class="p">, </span>status=None<span class="p">, </span>tags=None<span class="p">, </span>version=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetAnalyticsApplication<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationState">AnalyticsApplicationState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplication">AnalyticsApplication</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.AnalyticsApplication.html">AnalyticsApplication</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kinesis.AnalyticsApplicationState.html">AnalyticsApplicationState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Appliation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cloudwatch<wbr>Logging<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationcloudwatchloggingoptions">Analytics<wbr>Application<wbr>Cloudwatch<wbr>Logging<wbr>Options<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The CloudWatch log stream options to monitor application errors.
See CloudWatch Logging Options below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SQL Code to transform input data, and generate output.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Create<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Timestamp when the application version was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inputs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputs">Analytics<wbr>Application<wbr>Inputs<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Input configuration of the application. See Inputs below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Update<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Timestamp when the application was last updated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Outputs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutput">List&lt;Analytics<wbr>Application<wbr>Output<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Output destination configuration of the application. See Outputs below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reference<wbr>Data<wbr>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasources">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}An S3 Reference Data Source for the application.
See Reference Data Sources below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Status of the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of tags for the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Version of the application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Appliation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cloudwatch<wbr>Logging<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationcloudwatchloggingoptions">Analytics<wbr>Application<wbr>Cloudwatch<wbr>Logging<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}The CloudWatch log stream options to monitor application errors.
See CloudWatch Logging Options below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SQL Code to transform input data, and generate output.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Create<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Timestamp when the application version was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Inputs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputs">Analytics<wbr>Application<wbr>Inputs</a></span>
    </dt>
    <dd>{{% md %}}Input configuration of the application. See Inputs below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Update<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Timestamp when the application was last updated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Outputs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutput">[]Analytics<wbr>Application<wbr>Output</a></span>
    </dt>
    <dd>{{% md %}}Output destination configuration of the application. See Outputs below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reference<wbr>Data<wbr>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasources">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources</a></span>
    </dt>
    <dd>{{% md %}}An S3 Reference Data Source for the application.
See Reference Data Sources below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Status of the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of tags for the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Version of the application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">ARN</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Appliation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cloudwatch<wbr>Logging<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationcloudwatchloggingoptions">Analytics<wbr>Application<wbr>Cloudwatch<wbr>Logging<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}The CloudWatch log stream options to monitor application errors.
See CloudWatch Logging Options below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SQL Code to transform input data, and generate output.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>create<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Timestamp when the application version was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inputs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputs">Analytics<wbr>Application<wbr>Inputs</a></span>
    </dt>
    <dd>{{% md %}}Input configuration of the application. See Inputs below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>last<wbr>Update<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Timestamp when the application was last updated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>outputs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutput">Analytics<wbr>Application<wbr>Output[]</a></span>
    </dt>
    <dd>{{% md %}}Output destination configuration of the application. See Outputs below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reference<wbr>Data<wbr>Sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasources">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources</a></span>
    </dt>
    <dd>{{% md %}}An S3 Reference Data Source for the application.
See Reference Data Sources below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Status of the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of tags for the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The Version of the application.
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
    <dd>{{% md %}}The ARN of the Kinesis Analytics Appliation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cloudwatch_<wbr>logging_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationcloudwatchloggingoptions">Dict[Analytics<wbr>Application<wbr>Cloudwatch<wbr>Logging<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}The CloudWatch log stream options to monitor application errors.
See CloudWatch Logging Options below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}SQL Code to transform input data, and generate output.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>create_<wbr>timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Timestamp when the application version was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>inputs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputs">Dict[Analytics<wbr>Application<wbr>Inputs]</a></span>
    </dt>
    <dd>{{% md %}}Input configuration of the application. See Inputs below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>last_<wbr>update_<wbr>timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Timestamp when the application was last updated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>outputs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutput">List[Analytics<wbr>Application<wbr>Output]</a></span>
    </dt>
    <dd>{{% md %}}Output destination configuration of the application. See Outputs below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reference_<wbr>data_<wbr>sources</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasources">Dict[Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources]</a></span>
    </dt>
    <dd>{{% md %}}An S3 Reference Data Source for the application.
See Reference Data Sources below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Status of the application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of tags for the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The Version of the application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Analytics<wbr>Application<wbr>Cloudwatch<wbr>Logging<wbr>Options</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationCloudwatchLoggingOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationCloudwatchLoggingOptions">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationCloudwatchLoggingOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationCloudwatchLoggingOptionsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Log<wbr>Stream<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the CloudWatch Log Stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to send application messages.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Log<wbr>Stream<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the CloudWatch Log Stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to send application messages.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>log<wbr>Stream<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the CloudWatch Log Stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to send application messages.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>log<wbr>Stream<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the CloudWatch Log Stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to send application messages.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Inputs</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationInputs">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationInputs">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name Prefix to use when creating an in-application stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschema">Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The Schema format of the data in the streaming source. See Source Schema below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kinesis<wbr>Firehose</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputskinesisfirehose">Analytics<wbr>Application<wbr>Inputs<wbr>Kinesis<wbr>Firehose<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The Kinesis Firehose configuration for the streaming source. Conflicts with `kinesis_stream`.
See Kinesis Firehose below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kinesis<wbr>Stream</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputskinesisstream">Analytics<wbr>Application<wbr>Inputs<wbr>Kinesis<wbr>Stream<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The Kinesis Stream configuration for the streaming source. Conflicts with `kinesis_firehose`.
See Kinesis Stream below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parallelism</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsparallelism">Analytics<wbr>Application<wbr>Inputs<wbr>Parallelism<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The number of Parallel in-application streams to create.
See Parallelism below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Processing<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsprocessingconfiguration">Analytics<wbr>Application<wbr>Inputs<wbr>Processing<wbr>Configuration<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The Processing Configuration to transform records as they are received from the stream.
See Processing Configuration below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Starting<wbr>Position<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsstartingpositionconfiguration">List&lt;Analytics<wbr>Application<wbr>Inputs<wbr>Starting<wbr>Position<wbr>Configuration<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stream<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name Prefix to use when creating an in-application stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschema">Analytics<wbr>Application<wbr>Inputs<wbr>Schema</a></span>
    </dt>
    <dd>{{% md %}}The Schema format of the data in the streaming source. See Source Schema below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kinesis<wbr>Firehose</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputskinesisfirehose">Analytics<wbr>Application<wbr>Inputs<wbr>Kinesis<wbr>Firehose</a></span>
    </dt>
    <dd>{{% md %}}The Kinesis Firehose configuration for the streaming source. Conflicts with `kinesis_stream`.
See Kinesis Firehose below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kinesis<wbr>Stream</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputskinesisstream">Analytics<wbr>Application<wbr>Inputs<wbr>Kinesis<wbr>Stream</a></span>
    </dt>
    <dd>{{% md %}}The Kinesis Stream configuration for the streaming source. Conflicts with `kinesis_firehose`.
See Kinesis Stream below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parallelism</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsparallelism">Analytics<wbr>Application<wbr>Inputs<wbr>Parallelism</a></span>
    </dt>
    <dd>{{% md %}}The number of Parallel in-application streams to create.
See Parallelism below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Processing<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsprocessingconfiguration">Analytics<wbr>Application<wbr>Inputs<wbr>Processing<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}The Processing Configuration to transform records as they are received from the stream.
See Processing Configuration below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Starting<wbr>Position<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsstartingpositionconfiguration">[]Analytics<wbr>Application<wbr>Inputs<wbr>Starting<wbr>Position<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stream<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name Prefix to use when creating an in-application stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschema">Analytics<wbr>Application<wbr>Inputs<wbr>Schema</a></span>
    </dt>
    <dd>{{% md %}}The Schema format of the data in the streaming source. See Source Schema below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kinesis<wbr>Firehose</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputskinesisfirehose">Analytics<wbr>Application<wbr>Inputs<wbr>Kinesis<wbr>Firehose</a></span>
    </dt>
    <dd>{{% md %}}The Kinesis Firehose configuration for the streaming source. Conflicts with `kinesis_stream`.
See Kinesis Firehose below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kinesis<wbr>Stream</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputskinesisstream">Analytics<wbr>Application<wbr>Inputs<wbr>Kinesis<wbr>Stream</a></span>
    </dt>
    <dd>{{% md %}}The Kinesis Stream configuration for the streaming source. Conflicts with `kinesis_firehose`.
See Kinesis Stream below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parallelism</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsparallelism">Analytics<wbr>Application<wbr>Inputs<wbr>Parallelism</a></span>
    </dt>
    <dd>{{% md %}}The number of Parallel in-application streams to create.
See Parallelism below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>processing<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsprocessingconfiguration">Analytics<wbr>Application<wbr>Inputs<wbr>Processing<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}The Processing Configuration to transform records as they are received from the stream.
See Processing Configuration below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>starting<wbr>Position<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsstartingpositionconfiguration">Analytics<wbr>Application<wbr>Inputs<wbr>Starting<wbr>Position<wbr>Configuration[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stream<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name Prefix to use when creating an in-application stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschema">Dict[Analytics<wbr>Application<wbr>Inputs<wbr>Schema]</a></span>
    </dt>
    <dd>{{% md %}}The Schema format of the data in the streaming source. See Source Schema below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kinesis<wbr>Firehose</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputskinesisfirehose">Dict[Analytics<wbr>Application<wbr>Inputs<wbr>Kinesis<wbr>Firehose]</a></span>
    </dt>
    <dd>{{% md %}}The Kinesis Firehose configuration for the streaming source. Conflicts with `kinesis_stream`.
See Kinesis Firehose below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kinesis<wbr>Stream</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputskinesisstream">Dict[Analytics<wbr>Application<wbr>Inputs<wbr>Kinesis<wbr>Stream]</a></span>
    </dt>
    <dd>{{% md %}}The Kinesis Stream configuration for the streaming source. Conflicts with `kinesis_firehose`.
See Kinesis Stream below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parallelism</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsparallelism">Dict[Analytics<wbr>Application<wbr>Inputs<wbr>Parallelism]</a></span>
    </dt>
    <dd>{{% md %}}The number of Parallel in-application streams to create.
See Parallelism below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>processing<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsprocessingconfiguration">Dict[Analytics<wbr>Application<wbr>Inputs<wbr>Processing<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}The Processing Configuration to transform records as they are received from the stream.
See Processing Configuration below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>starting<wbr>Position<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsstartingpositionconfiguration">List[Analytics<wbr>Application<wbr>Inputs<wbr>Starting<wbr>Position<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stream<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Inputs<wbr>Kinesis<wbr>Firehose</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationInputsKinesisFirehose">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationInputsKinesisFirehose">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsKinesisFirehoseArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsKinesisFirehoseOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Firehose delivery stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the stream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Firehose delivery stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the stream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Firehose delivery stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the stream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Firehose delivery stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the stream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Inputs<wbr>Kinesis<wbr>Stream</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationInputsKinesisStream">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationInputsKinesisStream">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsKinesisStreamArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsKinesisStreamOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the stream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the stream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the stream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the stream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Inputs<wbr>Parallelism</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationInputsParallelism">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationInputsParallelism">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsParallelismArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsParallelismOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Count of streams.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Count of streams.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The Count of streams.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The Count of streams.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Inputs<wbr>Processing<wbr>Configuration</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationInputsProcessingConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationInputsProcessingConfiguration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsProcessingConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsProcessingConfigurationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Lambda</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsprocessingconfigurationlambda">Analytics<wbr>Application<wbr>Inputs<wbr>Processing<wbr>Configuration<wbr>Lambda<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The Lambda function configuration. See Lambda below for more details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Lambda</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsprocessingconfigurationlambda">Analytics<wbr>Application<wbr>Inputs<wbr>Processing<wbr>Configuration<wbr>Lambda</a></span>
    </dt>
    <dd>{{% md %}}The Lambda function configuration. See Lambda below for more details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>lambda</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsprocessingconfigurationlambda">Analytics<wbr>Application<wbr>Inputs<wbr>Processing<wbr>Configuration<wbr>Lambda</a></span>
    </dt>
    <dd>{{% md %}}The Lambda function configuration. See Lambda below for more details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>lambda_</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsprocessingconfigurationlambda">Dict[Analytics<wbr>Application<wbr>Inputs<wbr>Processing<wbr>Configuration<wbr>Lambda]</a></span>
    </dt>
    <dd>{{% md %}}The Lambda function configuration. See Lambda below for more details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Inputs<wbr>Processing<wbr>Configuration<wbr>Lambda</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationInputsProcessingConfigurationLambda">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationInputsProcessingConfigurationLambda">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsProcessingConfigurationLambdaArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsProcessingConfigurationLambdaOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Lambda function.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the Lambda function.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Lambda function.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the Lambda function.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Lambda function.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the Lambda function.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the Lambda function.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the Lambda function.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Inputs<wbr>Schema</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationInputsSchema">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationInputsSchema">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsSchemaArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsSchemaOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Columns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordcolumn">List&lt;Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Column<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The Record Column mapping for the streaming source data element.
See Record Columns below for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordformat">Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The Record Format and mapping information to schematize a record.
See Record Format below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Record<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Encoding of the record in the streaming source.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Columns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordcolumn">[]Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Column</a></span>
    </dt>
    <dd>{{% md %}}The Record Column mapping for the streaming source data element.
See Record Columns below for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordformat">Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format</a></span>
    </dt>
    <dd>{{% md %}}The Record Format and mapping information to schematize a record.
See Record Format below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Record<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Encoding of the record in the streaming source.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Columns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordcolumn">Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Column[]</a></span>
    </dt>
    <dd>{{% md %}}The Record Column mapping for the streaming source data element.
See Record Columns below for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordformat">Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format</a></span>
    </dt>
    <dd>{{% md %}}The Record Format and mapping information to schematize a record.
See Record Format below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>record<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Encoding of the record in the streaming source.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Columns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordcolumn">List[Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Column]</a></span>
    </dt>
    <dd>{{% md %}}The Record Column mapping for the streaming source data element.
See Record Columns below for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordformat">Dict[Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format]</a></span>
    </dt>
    <dd>{{% md %}}The Record Format and mapping information to schematize a record.
See Record Format below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>record<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Encoding of the record in the streaming source.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Column</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationInputsSchemaRecordColumn">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationInputsSchemaRecordColumn">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsSchemaRecordColumnArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsSchemaRecordColumnOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the column.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sql<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SQL Type of the column.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Mapping reference to the data element.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the column.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sql<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SQL Type of the column.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Mapping reference to the data element.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the column.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sql<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SQL Type of the column.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Mapping reference to the data element.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the column.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sql<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The SQL Type of the column.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Mapping reference to the data element.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationInputsSchemaRecordFormat">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationInputsSchemaRecordFormat">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsSchemaRecordFormatArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsSchemaRecordFormatOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Mapping<wbr>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordformatmappingparameters">Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The Mapping Information for the record format.
See Mapping Parameters below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Record<wbr>Format<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of Record Format. Can be `CSV` or `JSON`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Mapping<wbr>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordformatmappingparameters">Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters</a></span>
    </dt>
    <dd>{{% md %}}The Mapping Information for the record format.
See Mapping Parameters below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Record<wbr>Format<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of Record Format. Can be `CSV` or `JSON`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>mapping<wbr>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordformatmappingparameters">Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters</a></span>
    </dt>
    <dd>{{% md %}}The Mapping Information for the record format.
See Mapping Parameters below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>record<wbr>Format<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of Record Format. Can be `CSV` or `JSON`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>mapping<wbr>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordformatmappingparameters">Dict[Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters]</a></span>
    </dt>
    <dd>{{% md %}}The Mapping Information for the record format.
See Mapping Parameters below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>record<wbr>Format<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of Record Format. Can be `CSV` or `JSON`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationInputsSchemaRecordFormatMappingParameters">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationInputsSchemaRecordFormatMappingParameters">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsSchemaRecordFormatMappingParametersArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsSchemaRecordFormatMappingParametersOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Csv</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordformatmappingparameterscsv">Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Csv<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Mapping information when the record format uses delimiters.
See CSV Mapping Parameters below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordformatmappingparametersjson">Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Json<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Mapping information when JSON is the record format on the streaming source.
See JSON Mapping Parameters below for more details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Csv</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordformatmappingparameterscsv">Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Csv</a></span>
    </dt>
    <dd>{{% md %}}Mapping information when the record format uses delimiters.
See CSV Mapping Parameters below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordformatmappingparametersjson">Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Json</a></span>
    </dt>
    <dd>{{% md %}}Mapping information when JSON is the record format on the streaming source.
See JSON Mapping Parameters below for more details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>csv</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordformatmappingparameterscsv">Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Csv</a></span>
    </dt>
    <dd>{{% md %}}Mapping information when the record format uses delimiters.
See CSV Mapping Parameters below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>json</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordformatmappingparametersjson">Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Json</a></span>
    </dt>
    <dd>{{% md %}}Mapping information when JSON is the record format on the streaming source.
See JSON Mapping Parameters below for more details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>csv</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordformatmappingparameterscsv">Dict[Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Csv]</a></span>
    </dt>
    <dd>{{% md %}}Mapping information when the record format uses delimiters.
See CSV Mapping Parameters below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>json</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationinputsschemarecordformatmappingparametersjson">Dict[Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Json]</a></span>
    </dt>
    <dd>{{% md %}}Mapping information when JSON is the record format on the streaming source.
See JSON Mapping Parameters below for more details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Csv</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsv">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsSchemaRecordFormatMappingParametersCsvOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Column<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Column Delimiter.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Row<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Row Delimiter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Column<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Column Delimiter.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Row<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Row Delimiter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Column<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Column Delimiter.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Row<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Row Delimiter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Column<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Column Delimiter.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Row<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Row Delimiter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Inputs<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Json</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationInputsSchemaRecordFormatMappingParametersJson">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsSchemaRecordFormatMappingParametersJsonOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Row<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Path to the top-level parent that contains the records.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Row<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Path to the top-level parent that contains the records.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Row<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Path to the top-level parent that contains the records.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Row<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Path to the top-level parent that contains the records.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Inputs<wbr>Starting<wbr>Position<wbr>Configuration</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationInputsStartingPositionConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationInputsStartingPositionConfiguration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsStartingPositionConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationInputsStartingPositionConfigurationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Starting<wbr>Position</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Starting<wbr>Position</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>starting<wbr>Position</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>starting_<wbr>position</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Output</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationOutput">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationOutput">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationOutputArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationOutputOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the in-application stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutputschema">Analytics<wbr>Application<wbr>Output<wbr>Schema<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The Schema format of the data written to the destination. See Destination Schema below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kinesis<wbr>Firehose</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutputkinesisfirehose">Analytics<wbr>Application<wbr>Output<wbr>Kinesis<wbr>Firehose<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The Kinesis Firehose configuration for the destination stream. Conflicts with `kinesis_stream`.
See Kinesis Firehose below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kinesis<wbr>Stream</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutputkinesisstream">Analytics<wbr>Application<wbr>Output<wbr>Kinesis<wbr>Stream<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The Kinesis Stream configuration for the destination stream. Conflicts with `kinesis_firehose`.
See Kinesis Stream below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lambda</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutputlambda">Analytics<wbr>Application<wbr>Output<wbr>Lambda<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The Lambda function destination. See Lambda below for more details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the in-application stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutputschema">Analytics<wbr>Application<wbr>Output<wbr>Schema</a></span>
    </dt>
    <dd>{{% md %}}The Schema format of the data written to the destination. See Destination Schema below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kinesis<wbr>Firehose</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutputkinesisfirehose">Analytics<wbr>Application<wbr>Output<wbr>Kinesis<wbr>Firehose</a></span>
    </dt>
    <dd>{{% md %}}The Kinesis Firehose configuration for the destination stream. Conflicts with `kinesis_stream`.
See Kinesis Firehose below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kinesis<wbr>Stream</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutputkinesisstream">Analytics<wbr>Application<wbr>Output<wbr>Kinesis<wbr>Stream</a></span>
    </dt>
    <dd>{{% md %}}The Kinesis Stream configuration for the destination stream. Conflicts with `kinesis_firehose`.
See Kinesis Stream below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lambda</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutputlambda">Analytics<wbr>Application<wbr>Output<wbr>Lambda</a></span>
    </dt>
    <dd>{{% md %}}The Lambda function destination. See Lambda below for more details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the in-application stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutputschema">Analytics<wbr>Application<wbr>Output<wbr>Schema</a></span>
    </dt>
    <dd>{{% md %}}The Schema format of the data written to the destination. See Destination Schema below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kinesis<wbr>Firehose</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutputkinesisfirehose">Analytics<wbr>Application<wbr>Output<wbr>Kinesis<wbr>Firehose</a></span>
    </dt>
    <dd>{{% md %}}The Kinesis Firehose configuration for the destination stream. Conflicts with `kinesis_stream`.
See Kinesis Firehose below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kinesis<wbr>Stream</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutputkinesisstream">Analytics<wbr>Application<wbr>Output<wbr>Kinesis<wbr>Stream</a></span>
    </dt>
    <dd>{{% md %}}The Kinesis Stream configuration for the destination stream. Conflicts with `kinesis_firehose`.
See Kinesis Stream below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lambda</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutputlambda">Analytics<wbr>Application<wbr>Output<wbr>Lambda</a></span>
    </dt>
    <dd>{{% md %}}The Lambda function destination. See Lambda below for more details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name of the in-application stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutputschema">Dict[Analytics<wbr>Application<wbr>Output<wbr>Schema]</a></span>
    </dt>
    <dd>{{% md %}}The Schema format of the data written to the destination. See Destination Schema below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kinesis<wbr>Firehose</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutputkinesisfirehose">Dict[Analytics<wbr>Application<wbr>Output<wbr>Kinesis<wbr>Firehose]</a></span>
    </dt>
    <dd>{{% md %}}The Kinesis Firehose configuration for the destination stream. Conflicts with `kinesis_stream`.
See Kinesis Firehose below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kinesis<wbr>Stream</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutputkinesisstream">Dict[Analytics<wbr>Application<wbr>Output<wbr>Kinesis<wbr>Stream]</a></span>
    </dt>
    <dd>{{% md %}}The Kinesis Stream configuration for the destination stream. Conflicts with `kinesis_firehose`.
See Kinesis Stream below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lambda_</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationoutputlambda">Dict[Analytics<wbr>Application<wbr>Output<wbr>Lambda]</a></span>
    </dt>
    <dd>{{% md %}}The Lambda function destination. See Lambda below for more details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Output<wbr>Kinesis<wbr>Firehose</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationOutputKinesisFirehose">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationOutputKinesisFirehose">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationOutputKinesisFirehoseArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationOutputKinesisFirehoseOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Firehose delivery stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the stream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Firehose delivery stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the stream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Firehose delivery stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the stream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Firehose delivery stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the stream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Output<wbr>Kinesis<wbr>Stream</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationOutputKinesisStream">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationOutputKinesisStream">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationOutputKinesisStreamArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationOutputKinesisStreamOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the stream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the stream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the stream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Stream.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the stream.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Output<wbr>Lambda</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationOutputLambda">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationOutputLambda">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationOutputLambdaArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationOutputLambdaOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Lambda function.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the Lambda function.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Lambda function.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the Lambda function.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Lambda function.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the Lambda function.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the Lambda function.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to access the Lambda function.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Output<wbr>Schema</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationOutputSchema">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationOutputSchema">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationOutputSchemaArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationOutputSchemaOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Record<wbr>Format<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Format Type of the records on the output stream. Can be `CSV` or `JSON`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Record<wbr>Format<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Format Type of the records on the output stream. Can be `CSV` or `JSON`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>record<wbr>Format<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Format Type of the records on the output stream. Can be `CSV` or `JSON`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>record<wbr>Format<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Format Type of the records on the output stream. Can be `CSV` or `JSON`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationReferenceDataSources">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationReferenceDataSources">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationReferenceDataSourcesArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationReferenceDataSourcesOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>S3</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcess3">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>S3Args</a></span>
    </dt>
    <dd>{{% md %}}The S3 configuration for the reference data source. See S3 Reference below for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschema">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The Schema format of the data in the streaming source. See Source Schema below for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Table<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The in-application Table Name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>S3</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcess3">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>S3</a></span>
    </dt>
    <dd>{{% md %}}The S3 configuration for the reference data source. See S3 Reference below for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschema">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema</a></span>
    </dt>
    <dd>{{% md %}}The Schema format of the data in the streaming source. See Source Schema below for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Table<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The in-application Table Name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>s3</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcess3">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>S3</a></span>
    </dt>
    <dd>{{% md %}}The S3 configuration for the reference data source. See S3 Reference below for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschema">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema</a></span>
    </dt>
    <dd>{{% md %}}The Schema format of the data in the streaming source. See Source Schema below for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>table<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The in-application Table Name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>s3</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcess3">Dict[Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>S3]</a></span>
    </dt>
    <dd>{{% md %}}The S3 configuration for the reference data source. See S3 Reference below for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschema">Dict[Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema]</a></span>
    </dt>
    <dd>{{% md %}}The Schema format of the data in the streaming source. See Source Schema below for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>table_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The in-application Table Name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the Kinesis Analytics Application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>S3</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationReferenceDataSourcesS3">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationReferenceDataSourcesS3">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationReferenceDataSourcesS3Args">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationReferenceDataSourcesS3Output">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Bucket<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The S3 Bucket ARN.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>File<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The File Key name containing reference data.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to send application messages.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Bucket<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The S3 Bucket ARN.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>File<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The File Key name containing reference data.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to send application messages.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>bucket<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The S3 Bucket ARN.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>file<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The File Key name containing reference data.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to send application messages.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>bucket<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The S3 Bucket ARN.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>file<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The File Key name containing reference data.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the IAM Role used to send application messages.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationReferenceDataSourcesSchema">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationReferenceDataSourcesSchema">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationReferenceDataSourcesSchemaArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationReferenceDataSourcesSchemaOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Columns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordcolumn">List&lt;Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Column<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The Record Column mapping for the streaming source data element.
See Record Columns below for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordformat">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The Record Format and mapping information to schematize a record.
See Record Format below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Record<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Encoding of the record in the streaming source.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Columns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordcolumn">[]Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Column</a></span>
    </dt>
    <dd>{{% md %}}The Record Column mapping for the streaming source data element.
See Record Columns below for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordformat">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format</a></span>
    </dt>
    <dd>{{% md %}}The Record Format and mapping information to schematize a record.
See Record Format below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Record<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Encoding of the record in the streaming source.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Columns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordcolumn">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Column[]</a></span>
    </dt>
    <dd>{{% md %}}The Record Column mapping for the streaming source data element.
See Record Columns below for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordformat">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format</a></span>
    </dt>
    <dd>{{% md %}}The Record Format and mapping information to schematize a record.
See Record Format below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>record<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Encoding of the record in the streaming source.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Columns</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordcolumn">List[Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Column]</a></span>
    </dt>
    <dd>{{% md %}}The Record Column mapping for the streaming source data element.
See Record Columns below for more details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordformat">Dict[Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format]</a></span>
    </dt>
    <dd>{{% md %}}The Record Format and mapping information to schematize a record.
See Record Format below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>record<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Encoding of the record in the streaming source.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Column</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationReferenceDataSourcesSchemaRecordColumn">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationReferenceDataSourcesSchemaRecordColumn">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationReferenceDataSourcesSchemaRecordColumnArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationReferenceDataSourcesSchemaRecordColumnOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the column.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sql<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SQL Type of the column.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Mapping reference to the data element.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the column.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sql<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SQL Type of the column.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Mapping reference to the data element.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the column.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sql<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SQL Type of the column.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Mapping reference to the data element.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the column.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sql<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The SQL Type of the column.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Mapping reference to the data element.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationReferenceDataSourcesSchemaRecordFormat">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationReferenceDataSourcesSchemaRecordFormat">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Mapping<wbr>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordformatmappingparameters">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The Mapping Information for the record format.
See Mapping Parameters below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Record<wbr>Format<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of Record Format. Can be `CSV` or `JSON`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Mapping<wbr>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordformatmappingparameters">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters</a></span>
    </dt>
    <dd>{{% md %}}The Mapping Information for the record format.
See Mapping Parameters below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Record<wbr>Format<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of Record Format. Can be `CSV` or `JSON`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>mapping<wbr>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordformatmappingparameters">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters</a></span>
    </dt>
    <dd>{{% md %}}The Mapping Information for the record format.
See Mapping Parameters below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>record<wbr>Format<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of Record Format. Can be `CSV` or `JSON`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>mapping<wbr>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordformatmappingparameters">Dict[Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters]</a></span>
    </dt>
    <dd>{{% md %}}The Mapping Information for the record format.
See Mapping Parameters below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>record<wbr>Format<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of Record Format. Can be `CSV` or `JSON`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParameters">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Csv</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordformatmappingparameterscsv">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Csv<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Mapping information when the record format uses delimiters.
See CSV Mapping Parameters below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordformatmappingparametersjson">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Json<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Mapping information when JSON is the record format on the streaming source.
See JSON Mapping Parameters below for more details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Csv</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordformatmappingparameterscsv">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Csv</a></span>
    </dt>
    <dd>{{% md %}}Mapping information when the record format uses delimiters.
See CSV Mapping Parameters below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordformatmappingparametersjson">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Json</a></span>
    </dt>
    <dd>{{% md %}}Mapping information when JSON is the record format on the streaming source.
See JSON Mapping Parameters below for more details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>csv</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordformatmappingparameterscsv">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Csv</a></span>
    </dt>
    <dd>{{% md %}}Mapping information when the record format uses delimiters.
See CSV Mapping Parameters below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>json</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordformatmappingparametersjson">Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Json</a></span>
    </dt>
    <dd>{{% md %}}Mapping information when JSON is the record format on the streaming source.
See JSON Mapping Parameters below for more details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>csv</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordformatmappingparameterscsv">Dict[Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Csv]</a></span>
    </dt>
    <dd>{{% md %}}Mapping information when the record format uses delimiters.
See CSV Mapping Parameters below for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>json</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#analyticsapplicationreferencedatasourcesschemarecordformatmappingparametersjson">Dict[Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Json]</a></span>
    </dt>
    <dd>{{% md %}}Mapping information when JSON is the record format on the streaming source.
See JSON Mapping Parameters below for more details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Csv</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsv">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersCsvOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Column<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Column Delimiter.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Row<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Row Delimiter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Column<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Column Delimiter.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Row<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Row Delimiter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Column<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Column Delimiter.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Row<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Row Delimiter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Column<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Column Delimiter.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Row<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Row Delimiter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Analytics<wbr>Application<wbr>Reference<wbr>Data<wbr>Sources<wbr>Schema<wbr>Record<wbr>Format<wbr>Mapping<wbr>Parameters<wbr>Json</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJson">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kinesis?tab=doc#AnalyticsApplicationReferenceDataSourcesSchemaRecordFormatMappingParametersJsonOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Row<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Path to the top-level parent that contains the records.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Record<wbr>Row<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Path to the top-level parent that contains the records.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Row<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Path to the top-level parent that contains the records.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>record<wbr>Row<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Path to the top-level parent that contains the records.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-aws">https://github.com/pulumi/pulumi-aws</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`aws` Terraform Provider](https://github.com/terraform-providers/terraform-provider-aws).</dd>
</dl>

