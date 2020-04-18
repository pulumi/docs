
---
title: "JobDefinition"
block_external_search_index: true
---



Provides a Batch Job Definition resource.

{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const test = new aws.batch.JobDefinition("test", {
    containerProperties: `{
	"command": ["ls", "-la"],
	"image": "busybox",
	"memory": 1024,
	"vcpus": 1,
	"volumes": [
      {
        "host": {
          "sourcePath": "/tmp"
        },
        "name": "tmp"
      }
    ],
	"environment": [
		{"name": "VARNAME", "value": "VARVAL"}
	],
	"mountPoints": [
		{
          "sourceVolume": "tmp",
          "containerPath": "/tmp",
          "readOnly": false
        }
	],
    "ulimits": [
      {
        "hardLimit": 1024,
        "name": "nofile",
        "softLimit": 1024
      }
    ]
}
`,
    type: "container",
});
```

{{% /example %}}
{{% /examples %}}
## retry_strategy

`retry_strategy` supports the following:

* `attempts` - (Optional) The number of times to move a job to the `RUNNABLE` status. You may specify between `1` and `10` attempts.

## timeout

`timeout` supports the following:

* `attempt_duration_seconds` - (Optional) The time duration in seconds after which AWS Batch terminates your jobs if they have not finished. The minimum value for the timeout is `60` seconds.



## Create a JobDefinition Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/batch/#JobDefinition">JobDefinition</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/batch/#JobDefinitionArgs">JobDefinitionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">JobDefinition</span><span class="p">(resource_name, opts=None, </span>container_properties=None<span class="p">, </span>name=None<span class="p">, </span>parameters=None<span class="p">, </span>retry_strategy=None<span class="p">, </span>timeout=None<span class="p">, </span>type=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewJobDefinition<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/batch?tab=doc#JobDefinitionArgs">JobDefinitionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/batch?tab=doc#JobDefinition">JobDefinition</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Batch.JobDefinition.html">JobDefinition</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Batch.JobDefinitionArgs.html">JobDefinitionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Container<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Specifies the parameter substitution placeholders to set in the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitionretrystrategy">Job<wbr>Definition<wbr>Retry<wbr>Strategy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of `retry_strategy` is `1`.  Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitiontimeout">Job<wbr>Definition<wbr>Timeout<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `timeout` is `1`. Defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of job definition.  Must be `container`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Specifies the parameter substitution placeholders to set in the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitionretrystrategy">*Job<wbr>Definition<wbr>Retry<wbr>Strategy</a></span>
    </dt>
    <dd>{{% md %}}Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of `retry_strategy` is `1`.  Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitiontimeout">*Job<wbr>Definition<wbr>Timeout</a></span>
    </dt>
    <dd>{{% md %}}Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `timeout` is `1`. Defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of job definition.  Must be `container`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>container<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Specifies the parameter substitution placeholders to set in the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitionretrystrategy">Job<wbr>Definition<wbr>Retry<wbr>Strategy?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of `retry_strategy` is `1`.  Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitiontimeout">Job<wbr>Definition<wbr>Timeout?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `timeout` is `1`. Defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of job definition.  Must be `container`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>container_<wbr>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Specifies the parameter substitution placeholders to set in the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry_<wbr>strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitionretrystrategy">Dict[Job<wbr>Definition<wbr>Retry<wbr>Strategy]</a></span>
    </dt>
    <dd>{{% md %}}Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of `retry_strategy` is `1`.  Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitiontimeout">Dict[Job<wbr>Definition<wbr>Timeout]</a></span>
    </dt>
    <dd>{{% md %}}Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `timeout` is `1`. Defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of job definition.  Must be `container`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## JobDefinition Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name of the job definition.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Container<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the job definition.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Specifies the parameter substitution placeholders to set in the job definition.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retry<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitionretrystrategy">Job<wbr>Definition<wbr>Retry<wbr>Strategy?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of `retry_strategy` is `1`.  Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Revision</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The revision of the job definition.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitiontimeout">Job<wbr>Definition<wbr>Timeout?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `timeout` is `1`. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of job definition.  Must be `container`
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
    <dd>{{% md %}}The Amazon Resource Name of the job definition.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Container<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the job definition.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Specifies the parameter substitution placeholders to set in the job definition.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retry<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitionretrystrategy">*Job<wbr>Definition<wbr>Retry<wbr>Strategy</a></span>
    </dt>
    <dd>{{% md %}}Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of `retry_strategy` is `1`.  Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Revision</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The revision of the job definition.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitiontimeout">*Job<wbr>Definition<wbr>Timeout</a></span>
    </dt>
    <dd>{{% md %}}Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `timeout` is `1`. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of job definition.  Must be `container`
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
    <dd>{{% md %}}The Amazon Resource Name of the job definition.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>container<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the job definition.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Specifies the parameter substitution placeholders to set in the job definition.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retry<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitionretrystrategy">Job<wbr>Definition<wbr>Retry<wbr>Strategy?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of `retry_strategy` is `1`.  Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>revision</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The revision of the job definition.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitiontimeout">Job<wbr>Definition<wbr>Timeout?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `timeout` is `1`. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of job definition.  Must be `container`
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
    <dd>{{% md %}}The Amazon Resource Name of the job definition.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>container_<wbr>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the job definition.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Specifies the parameter substitution placeholders to set in the job definition.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retry_<wbr>strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitionretrystrategy">Dict[Job<wbr>Definition<wbr>Retry<wbr>Strategy]</a></span>
    </dt>
    <dd>{{% md %}}Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of `retry_strategy` is `1`.  Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>revision</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The revision of the job definition.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitiontimeout">Dict[Job<wbr>Definition<wbr>Timeout]</a></span>
    </dt>
    <dd>{{% md %}}Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `timeout` is `1`. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of job definition.  Must be `container`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing JobDefinition Resource

Get an existing JobDefinition resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/batch/#JobDefinitionState">JobDefinitionState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/batch/#JobDefinition">JobDefinition</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>container_properties=None<span class="p">, </span>name=None<span class="p">, </span>parameters=None<span class="p">, </span>retry_strategy=None<span class="p">, </span>revision=None<span class="p">, </span>timeout=None<span class="p">, </span>type=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetJobDefinition<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/batch?tab=doc#JobDefinitionState">JobDefinitionState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/batch?tab=doc#JobDefinition">JobDefinition</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Batch.JobDefinition.html">JobDefinition</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Batch.JobDefinitionState.html">JobDefinitionState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
    <dd>{{% md %}}The Amazon Resource Name of the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Specifies the parameter substitution placeholders to set in the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitionretrystrategy">Job<wbr>Definition<wbr>Retry<wbr>Strategy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of `retry_strategy` is `1`.  Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Revision</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The revision of the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitiontimeout">Job<wbr>Definition<wbr>Timeout<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `timeout` is `1`. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of job definition.  Must be `container`
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
    <dd>{{% md %}}The Amazon Resource Name of the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Specifies the parameter substitution placeholders to set in the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitionretrystrategy">*Job<wbr>Definition<wbr>Retry<wbr>Strategy</a></span>
    </dt>
    <dd>{{% md %}}Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of `retry_strategy` is `1`.  Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Revision</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The revision of the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitiontimeout">*Job<wbr>Definition<wbr>Timeout</a></span>
    </dt>
    <dd>{{% md %}}Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `timeout` is `1`. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of job definition.  Must be `container`
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
    <dd>{{% md %}}The Amazon Resource Name of the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>container<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Specifies the parameter substitution placeholders to set in the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitionretrystrategy">Job<wbr>Definition<wbr>Retry<wbr>Strategy?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of `retry_strategy` is `1`.  Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>revision</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The revision of the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitiontimeout">Job<wbr>Definition<wbr>Timeout?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `timeout` is `1`. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of job definition.  Must be `container`
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
    <dd>{{% md %}}The Amazon Resource Name of the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>container_<wbr>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Specifies the parameter substitution placeholders to set in the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry_<wbr>strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitionretrystrategy">Dict[Job<wbr>Definition<wbr>Retry<wbr>Strategy]</a></span>
    </dt>
    <dd>{{% md %}}Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of `retry_strategy` is `1`.  Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>revision</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The revision of the job definition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobdefinitiontimeout">Dict[Job<wbr>Definition<wbr>Timeout]</a></span>
    </dt>
    <dd>{{% md %}}Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `timeout` is `1`. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of job definition.  Must be `container`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Job<wbr>Definition<wbr>Retry<wbr>Strategy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#JobDefinitionRetryStrategy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#JobDefinitionRetryStrategy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/batch?tab=doc#JobDefinitionRetryStrategyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/batch?tab=doc#JobDefinitionRetryStrategyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Attempts</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Attempts</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>attempts</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>attempts</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Definition<wbr>Timeout</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#JobDefinitionTimeout">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#JobDefinitionTimeout">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/batch?tab=doc#JobDefinitionTimeoutArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/batch?tab=doc#JobDefinitionTimeoutOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Attempt<wbr>Duration<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Attempt<wbr>Duration<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>attempt<wbr>Duration<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>attempt<wbr>Duration<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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

