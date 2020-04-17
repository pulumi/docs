
---
title: "Job"
block_external_search_index: true
---



Manages a job resource within a Dataproc cluster within GCE. For more information see
[the official dataproc documentation](https://cloud.google.com/dataproc/).

!> **Note:** This resource does not support 'update' and changing any attributes will cause the resource to be recreated.



## Create a Job Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/dataproc/#Job">Job</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/dataproc/#JobArgs">JobArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Job</span><span class="p">(resource_name, opts=None, </span>force_delete=None<span class="p">, </span>hadoop_config=None<span class="p">, </span>hive_config=None<span class="p">, </span>labels=None<span class="p">, </span>pig_config=None<span class="p">, </span>placement=None<span class="p">, </span>project=None<span class="p">, </span>pyspark_config=None<span class="p">, </span>reference=None<span class="p">, </span>region=None<span class="p">, </span>scheduling=None<span class="p">, </span>spark_config=None<span class="p">, </span>sparksql_config=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewJob<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobArgs">JobArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#Job">Job</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Dataproc.Job.html">Job</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Dataproc.JobArgs.html">JobArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-required"
            title="Required">
        <span>Placement</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobplacement">Job<wbr>Placement<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hadoop<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhadoopconfig">Job<wbr>Hadoop<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hive<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhiveconfig">Job<wbr>Hive<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to add to the job.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pig<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpigconfig">Job<wbr>Pig<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The project in which the `cluster` can be found and jobs
subsequently run against. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pyspark<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpysparkconfig">Job<wbr>Pyspark<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobreference">Job<wbr>Reference<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to `global`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobscheduling">Job<wbr>Scheduling<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Optional. Job scheduling configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spark<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparkconfig">Job<wbr>Spark<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sparksql<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparksqlconfig">Job<wbr>Sparksql<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Placement</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobplacement">Job<wbr>Placement</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hadoop<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhadoopconfig">Job<wbr>Hadoop<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hive<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhiveconfig">Job<wbr>Hive<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to add to the job.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pig<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpigconfig">Job<wbr>Pig<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The project in which the `cluster` can be found and jobs
subsequently run against. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pyspark<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpysparkconfig">Job<wbr>Pyspark<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobreference">Job<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to `global`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobscheduling">Job<wbr>Scheduling</a></span>
    </dt>
    <dd>{{% md %}}Optional. Job scheduling configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spark<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparkconfig">Job<wbr>Spark<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sparksql<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparksqlconfig">Job<wbr>Sparksql<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>placement</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobplacement">Job<wbr>Placement</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hadoop<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhadoopconfig">Job<wbr>Hadoop<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hive<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhiveconfig">Job<wbr>Hive<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to add to the job.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pig<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpigconfig">Job<wbr>Pig<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The project in which the `cluster` can be found and jobs
subsequently run against. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pyspark<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpysparkconfig">Job<wbr>Pyspark<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobreference">Job<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to `global`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobscheduling">Job<wbr>Scheduling</a></span>
    </dt>
    <dd>{{% md %}}Optional. Job scheduling configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spark<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparkconfig">Job<wbr>Spark<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sparksql<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparksqlconfig">Job<wbr>Sparksql<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>placement</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobplacement">Dict[Job<wbr>Placement]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force_<wbr>delete</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hadoop_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhadoopconfig">Dict[Job<wbr>Hadoop<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hive_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhiveconfig">Dict[Job<wbr>Hive<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to add to the job.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pig_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpigconfig">Dict[Job<wbr>Pig<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The project in which the `cluster` can be found and jobs
subsequently run against. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pyspark_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpysparkconfig">Dict[Job<wbr>Pyspark<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobreference">Dict[Job<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to `global`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobscheduling">Dict[Job<wbr>Scheduling]</a></span>
    </dt>
    <dd>{{% md %}}Optional. Job scheduling configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spark_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparkconfig">Dict[Job<wbr>Spark<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sparksql_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparksqlconfig">Dict[Job<wbr>Sparksql<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Job Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Driver<wbr>Controls<wbr>Files<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Driver<wbr>Output<wbr>Resource<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A URI pointing to the location of the stdout of the job's driver program.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobstatus">Job<wbr>Status</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Driver<wbr>Controls<wbr>Files<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Driver<wbr>Output<wbr>Resource<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A URI pointing to the location of the stdout of the job's driver program.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobstatus">Job<wbr>Status</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>driver<wbr>Controls<wbr>Files<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>driver<wbr>Output<wbr>Resource<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A URI pointing to the location of the stdout of the job's driver program.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobstatus">Job<wbr>Status</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>driver_<wbr>controls_<wbr>files_<wbr>uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>driver_<wbr>output_<wbr>resource_<wbr>uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A URI pointing to the location of the stdout of the job's driver program.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobstatus">Dict[Job<wbr>Status]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Job Resource

Get an existing Job resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/dataproc/#JobState">JobState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/dataproc/#Job">Job</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>driver_controls_files_uri=None<span class="p">, </span>driver_output_resource_uri=None<span class="p">, </span>force_delete=None<span class="p">, </span>hadoop_config=None<span class="p">, </span>hive_config=None<span class="p">, </span>labels=None<span class="p">, </span>pig_config=None<span class="p">, </span>placement=None<span class="p">, </span>project=None<span class="p">, </span>pyspark_config=None<span class="p">, </span>reference=None<span class="p">, </span>region=None<span class="p">, </span>scheduling=None<span class="p">, </span>spark_config=None<span class="p">, </span>sparksql_config=None<span class="p">, </span>status=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetJob<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobState">JobState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#Job">Job</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Dataproc.Job.html">Job</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Dataproc.JobState.html">JobState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Driver<wbr>Controls<wbr>Files<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Driver<wbr>Output<wbr>Resource<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A URI pointing to the location of the stdout of the job's driver program.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hadoop<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhadoopconfig">Job<wbr>Hadoop<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hive<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhiveconfig">Job<wbr>Hive<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to add to the job.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pig<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpigconfig">Job<wbr>Pig<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Placement</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobplacement">Job<wbr>Placement<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The project in which the `cluster` can be found and jobs
subsequently run against. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pyspark<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpysparkconfig">Job<wbr>Pyspark<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobreference">Job<wbr>Reference<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to `global`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobscheduling">Job<wbr>Scheduling<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Optional. Job scheduling configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spark<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparkconfig">Job<wbr>Spark<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sparksql<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparksqlconfig">Job<wbr>Sparksql<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobstatus">Job<wbr>Status<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Driver<wbr>Controls<wbr>Files<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Driver<wbr>Output<wbr>Resource<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A URI pointing to the location of the stdout of the job's driver program.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hadoop<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhadoopconfig">Job<wbr>Hadoop<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hive<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhiveconfig">Job<wbr>Hive<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to add to the job.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pig<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpigconfig">Job<wbr>Pig<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Placement</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobplacement">Job<wbr>Placement</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The project in which the `cluster` can be found and jobs
subsequently run against. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pyspark<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpysparkconfig">Job<wbr>Pyspark<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobreference">Job<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to `global`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobscheduling">Job<wbr>Scheduling</a></span>
    </dt>
    <dd>{{% md %}}Optional. Job scheduling configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spark<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparkconfig">Job<wbr>Spark<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sparksql<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparksqlconfig">Job<wbr>Sparksql<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobstatus">Job<wbr>Status</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>driver<wbr>Controls<wbr>Files<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>driver<wbr>Output<wbr>Resource<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A URI pointing to the location of the stdout of the job's driver program.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hadoop<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhadoopconfig">Job<wbr>Hadoop<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hive<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhiveconfig">Job<wbr>Hive<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to add to the job.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pig<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpigconfig">Job<wbr>Pig<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>placement</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobplacement">Job<wbr>Placement</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The project in which the `cluster` can be found and jobs
subsequently run against. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pyspark<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpysparkconfig">Job<wbr>Pyspark<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobreference">Job<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to `global`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobscheduling">Job<wbr>Scheduling</a></span>
    </dt>
    <dd>{{% md %}}Optional. Job scheduling configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spark<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparkconfig">Job<wbr>Spark<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sparksql<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparksqlconfig">Job<wbr>Sparksql<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobstatus">Job<wbr>Status</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>driver_<wbr>controls_<wbr>files_<wbr>uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>driver_<wbr>output_<wbr>resource_<wbr>uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A URI pointing to the location of the stdout of the job's driver program.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force_<wbr>delete</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hadoop_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhadoopconfig">Dict[Job<wbr>Hadoop<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hive_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhiveconfig">Dict[Job<wbr>Hive<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to add to the job.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pig_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpigconfig">Dict[Job<wbr>Pig<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>placement</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobplacement">Dict[Job<wbr>Placement]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The project in which the `cluster` can be found and jobs
subsequently run against. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pyspark_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpysparkconfig">Dict[Job<wbr>Pyspark<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobreference">Dict[Job<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to `global`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobscheduling">Dict[Job<wbr>Scheduling]</a></span>
    </dt>
    <dd>{{% md %}}Optional. Job scheduling configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spark_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparkconfig">Dict[Job<wbr>Spark<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sparksql_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparksqlconfig">Dict[Job<wbr>Sparksql<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobstatus">Dict[Job<wbr>Status]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Job<wbr>Hadoop<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobHadoopConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobHadoopConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobHadoopConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobHadoopConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Archive<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhadoopconfigloggingconfig">Job<wbr>Hadoop<wbr>Config<wbr>Logging<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Main<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Main<wbr>Jar<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the jar file containing the main class. Examples: 'gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar' 'hdfs:/tmp/test-samples/custom-wordcount.jar' 'file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar'. Conflicts with `main_class`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Archive<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhadoopconfigloggingconfig">Job<wbr>Hadoop<wbr>Config<wbr>Logging<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Main<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Main<wbr>Jar<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the jar file containing the main class. Examples: 'gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar' 'hdfs:/tmp/test-samples/custom-wordcount.jar' 'file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar'. Conflicts with `main_class`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>archive<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>file<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhadoopconfigloggingconfig">Job<wbr>Hadoop<wbr>Config<wbr>Logging<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>main<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>main<wbr>Jar<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the jar file containing the main class. Examples: 'gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar' 'hdfs:/tmp/test-samples/custom-wordcount.jar' 'file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar'. Conflicts with `main_class`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>archive<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>file<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhadoopconfigloggingconfig">Dict[Job<wbr>Hadoop<wbr>Config<wbr>Logging<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>main<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>main<wbr>Jar<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the jar file containing the main class. Examples: 'gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar' 'hdfs:/tmp/test-samples/custom-wordcount.jar' 'file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar'. Conflicts with `main_class`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Hadoop<wbr>Config<wbr>Logging<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobHadoopConfigLoggingConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobHadoopConfigLoggingConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobHadoopConfigLoggingConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobHadoopConfigLoggingConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Hive<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobHiveConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobHiveConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobHiveConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobHiveConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Continue<wbr>On<wbr>Failure</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the script that contains SQL queries.
Conflicts with `query_list`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Script<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}Mapping of query variable names to values (equivalent to the Spark SQL command: `SET name="value";`).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Continue<wbr>On<wbr>Failure</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the script that contains SQL queries.
Conflicts with `query_list`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Script<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Mapping of query variable names to values (equivalent to the Spark SQL command: `SET name="value";`).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>continue<wbr>On<wbr>Failure</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the script that contains SQL queries.
Conflicts with `query_list`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>script<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}Mapping of query variable names to values (equivalent to the Spark SQL command: `SET name="value";`).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>continue<wbr>On<wbr>Failure</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the script that contains SQL queries.
Conflicts with `query_list`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>script<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Mapping of query variable names to values (equivalent to the Spark SQL command: `SET name="value";`).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Pig<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobPigConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobPigConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobPigConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobPigConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Continue<wbr>On<wbr>Failure</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpigconfigloggingconfig">Job<wbr>Pig<wbr>Config<wbr>Logging<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the script that contains SQL queries.
Conflicts with `query_list`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Script<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}Mapping of query variable names to values (equivalent to the Spark SQL command: `SET name="value";`).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Continue<wbr>On<wbr>Failure</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpigconfigloggingconfig">Job<wbr>Pig<wbr>Config<wbr>Logging<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the script that contains SQL queries.
Conflicts with `query_list`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Script<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Mapping of query variable names to values (equivalent to the Spark SQL command: `SET name="value";`).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>continue<wbr>On<wbr>Failure</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpigconfigloggingconfig">Job<wbr>Pig<wbr>Config<wbr>Logging<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the script that contains SQL queries.
Conflicts with `query_list`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>script<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}Mapping of query variable names to values (equivalent to the Spark SQL command: `SET name="value";`).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>continue<wbr>On<wbr>Failure</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpigconfigloggingconfig">Dict[Job<wbr>Pig<wbr>Config<wbr>Logging<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the script that contains SQL queries.
Conflicts with `query_list`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>script<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Mapping of query variable names to values (equivalent to the Spark SQL command: `SET name="value";`).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Pig<wbr>Config<wbr>Logging<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobPigConfigLoggingConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobPigConfigLoggingConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobPigConfigLoggingConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobPigConfigLoggingConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Placement</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobPlacement">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobPlacement">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobPlacementArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobPlacementOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cluster<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cluster<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cluster<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cluster<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Pyspark<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobPysparkConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobPysparkConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobPysparkConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobPysparkConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Main<wbr>Python<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Archive<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpysparkconfigloggingconfig">Job<wbr>Pyspark<wbr>Config<wbr>Logging<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Python<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}HCFS file URIs of Python files to pass to the PySpark framework. Supported file types: .py, .egg, and .zip.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Main<wbr>Python<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Archive<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpysparkconfigloggingconfig">Job<wbr>Pyspark<wbr>Config<wbr>Logging<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Python<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}HCFS file URIs of Python files to pass to the PySpark framework. Supported file types: .py, .egg, and .zip.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>main<wbr>Python<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>archive<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>file<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpysparkconfigloggingconfig">Job<wbr>Pyspark<wbr>Config<wbr>Logging<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>python<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}HCFS file URIs of Python files to pass to the PySpark framework. Supported file types: .py, .egg, and .zip.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>main<wbr>Python<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>archive<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>file<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpysparkconfigloggingconfig">Dict[Job<wbr>Pyspark<wbr>Config<wbr>Logging<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>python<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}HCFS file URIs of Python files to pass to the PySpark framework. Supported file types: .py, .egg, and .zip.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Pyspark<wbr>Config<wbr>Logging<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobPysparkConfigLoggingConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobPysparkConfigLoggingConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobPysparkConfigLoggingConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobPysparkConfigLoggingConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Reference</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobReference">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobReference">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobReferenceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobReferenceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Job<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Job<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>job<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>job_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Scheduling</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobScheduling">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobScheduling">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobSchedulingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobSchedulingOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Failures<wbr>Per<wbr>Hour</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Failures<wbr>Per<wbr>Hour</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Failures<wbr>Per<wbr>Hour</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Failures<wbr>Per<wbr>Hour</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Spark<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobSparkConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobSparkConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobSparkConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobSparkConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Archive<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparkconfigloggingconfig">Job<wbr>Spark<wbr>Config<wbr>Logging<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Main<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Main<wbr>Jar<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the jar file containing the main class. Examples: 'gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar' 'hdfs:/tmp/test-samples/custom-wordcount.jar' 'file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar'. Conflicts with `main_class`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Archive<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparkconfigloggingconfig">Job<wbr>Spark<wbr>Config<wbr>Logging<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Main<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Main<wbr>Jar<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the jar file containing the main class. Examples: 'gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar' 'hdfs:/tmp/test-samples/custom-wordcount.jar' 'file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar'. Conflicts with `main_class`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>archive<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>file<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparkconfigloggingconfig">Job<wbr>Spark<wbr>Config<wbr>Logging<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>main<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>main<wbr>Jar<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the jar file containing the main class. Examples: 'gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar' 'hdfs:/tmp/test-samples/custom-wordcount.jar' 'file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar'. Conflicts with `main_class`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>archive<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The arguments to pass to the driver. Do not include arguments, such as -libjars or -Dfoo=bar, that can be set as job properties, since a collision may occur that causes an incorrect job submission.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>file<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of files to be copied to the working directory of Hadoop drivers and distributed tasks. Useful for naively parallel tasks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparkconfigloggingconfig">Dict[Job<wbr>Spark<wbr>Config<wbr>Logging<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>main<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>main<wbr>Jar<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the jar file containing the main class. Examples: 'gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar' 'hdfs:/tmp/test-samples/custom-wordcount.jar' 'file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar'. Conflicts with `main_class`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Spark<wbr>Config<wbr>Logging<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobSparkConfigLoggingConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobSparkConfigLoggingConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobSparkConfigLoggingConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobSparkConfigLoggingConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Sparksql<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobSparksqlConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobSparksqlConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobSparksqlConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobSparksqlConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparksqlconfigloggingconfig">Job<wbr>Sparksql<wbr>Config<wbr>Logging<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the script that contains SQL queries.
Conflicts with `query_list`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Script<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}Mapping of query variable names to values (equivalent to the Spark SQL command: `SET name="value";`).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparksqlconfigloggingconfig">Job<wbr>Sparksql<wbr>Config<wbr>Logging<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the script that contains SQL queries.
Conflicts with `query_list`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Script<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Mapping of query variable names to values (equivalent to the Spark SQL command: `SET name="value";`).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparksqlconfigloggingconfig">Job<wbr>Sparksql<wbr>Config<wbr>Logging<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the script that contains SQL queries.
Conflicts with `query_list`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>script<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}Mapping of query variable names to values (equivalent to the Spark SQL command: `SET name="value";`).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>jar<wbr>File<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}HCFS URIs of jar files to be added to the Spark CLASSPATH.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobsparksqlconfigloggingconfig">Dict[Job<wbr>Sparksql<wbr>Config<wbr>Logging<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>File<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The HCFS URI of the script that contains SQL queries.
Conflicts with `query_list`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>script<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Mapping of query variable names to values (equivalent to the Spark SQL command: `SET name="value";`).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Sparksql<wbr>Config<wbr>Logging<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobSparksqlConfigLoggingConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobSparksqlConfigLoggingConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobSparksqlConfigLoggingConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobSparksqlConfigLoggingConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>driver<wbr>Log<wbr>Levels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Status</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobStatus">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/dataproc?tab=doc#JobStatusOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Details</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>State<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Substate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Details</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>State<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Substate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>details</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>state<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>substate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>details</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>state<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>substate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`google-beta` Terraform Provider](https://github.com/terraform-providers/terraform-provider-google-beta).</dd>
</dl>

