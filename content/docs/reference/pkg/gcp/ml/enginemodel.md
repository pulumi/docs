
---
title: "EngineModel"
block_external_search_index: true
---

Represents a machine learning solution.

A model can have multiple versions, each of which is a deployed, trained model
ready to receive prediction requests. The model itself is just a container.

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/ml_engine_model.html.markdown.



## Create a EngineModel Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/ml/#EngineModel">EngineModel</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/ml/#EngineModelArgs">EngineModelArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">EngineModel</span><span class="p">(resource_name, opts=None, </span>default_version=None<span class="p">, </span>description=None<span class="p">, </span>labels=None<span class="p">, </span>name=None<span class="p">, </span>online_prediction_console_logging=None<span class="p">, </span>online_prediction_logging=None<span class="p">, </span>project=None<span class="p">, </span>regions=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewEngineModel<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/ml?tab=doc#EngineModelArgs">EngineModelArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/ml?tab=doc#EngineModel">EngineModel</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Ml.EngineModel.html">EngineModel</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.ML.EngineModelArgs.html">EngineModelArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Default<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#enginemodeldefaultversion">Engine<wbr>Model<wbr>Default<wbr>Version<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The default version of the model. This version will be used to handle prediction requests that do not specify a version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description specified for the model when it was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}One or more labels that you can add, to organize your models.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name specified for the model.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Online<wbr>Prediction<wbr>Console<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Online<wbr>Prediction<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, online prediction access logs are sent to StackDriver Logging.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The list of regions where the model is going to be deployed. Currently only one region per model is supported
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#enginemodeldefaultversion">*Engine<wbr>Model<wbr>Default<wbr>Version</a></span>
    </dt>
    <dd>{{% md %}}The default version of the model. This version will be used to handle prediction requests that do not specify a version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The description specified for the model when it was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}One or more labels that you can add, to organize your models.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name specified for the model.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Online<wbr>Prediction<wbr>Console<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Online<wbr>Prediction<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, online prediction access logs are sent to StackDriver Logging.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The list of regions where the model is going to be deployed. Currently only one region per model is supported
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#enginemodeldefaultversion">Engine<wbr>Model<wbr>Default<wbr>Version?</a></span>
    </dt>
    <dd>{{% md %}}The default version of the model. This version will be used to handle prediction requests that do not specify a version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description specified for the model when it was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}One or more labels that you can add, to organize your models.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name specified for the model.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>online<wbr>Prediction<wbr>Console<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>online<wbr>Prediction<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, online prediction access logs are sent to StackDriver Logging.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The list of regions where the model is going to be deployed. Currently only one region per model is supported
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#enginemodeldefaultversion">Dict[Engine<wbr>Model<wbr>Default<wbr>Version]</a></span>
    </dt>
    <dd>{{% md %}}The default version of the model. This version will be used to handle prediction requests that do not specify a version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description specified for the model when it was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}One or more labels that you can add, to organize your models.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name specified for the model.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>online_<wbr>prediction_<wbr>console_<wbr>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>online_<wbr>prediction_<wbr>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, online prediction access logs are sent to StackDriver Logging.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The list of regions where the model is going to be deployed. Currently only one region per model is supported
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## EngineModel Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Default<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#enginemodeldefaultversion">Engine<wbr>Model<wbr>Default<wbr>Version?</a></span>
    </dt>
    <dd>{{% md %}}The default version of the model. This version will be used to handle prediction requests that do not specify a version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description specified for the model when it was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}One or more labels that you can add, to organize your models.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name specified for the model.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Online<wbr>Prediction<wbr>Console<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Online<wbr>Prediction<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, online prediction access logs are sent to StackDriver Logging.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The list of regions where the model is going to be deployed. Currently only one region per model is supported
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Default<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#enginemodeldefaultversion">*Engine<wbr>Model<wbr>Default<wbr>Version</a></span>
    </dt>
    <dd>{{% md %}}The default version of the model. This version will be used to handle prediction requests that do not specify a version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The description specified for the model when it was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}One or more labels that you can add, to organize your models.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name specified for the model.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Online<wbr>Prediction<wbr>Console<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Online<wbr>Prediction<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, online prediction access logs are sent to StackDriver Logging.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The list of regions where the model is going to be deployed. Currently only one region per model is supported
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>default<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#enginemodeldefaultversion">Engine<wbr>Model<wbr>Default<wbr>Version?</a></span>
    </dt>
    <dd>{{% md %}}The default version of the model. This version will be used to handle prediction requests that do not specify a version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description specified for the model when it was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}One or more labels that you can add, to organize your models.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name specified for the model.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>online<wbr>Prediction<wbr>Console<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>online<wbr>Prediction<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, online prediction access logs are sent to StackDriver Logging.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The list of regions where the model is going to be deployed. Currently only one region per model is supported
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>default_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#enginemodeldefaultversion">Dict[Engine<wbr>Model<wbr>Default<wbr>Version]</a></span>
    </dt>
    <dd>{{% md %}}The default version of the model. This version will be used to handle prediction requests that do not specify a version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description specified for the model when it was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}One or more labels that you can add, to organize your models.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name specified for the model.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>online_<wbr>prediction_<wbr>console_<wbr>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>online_<wbr>prediction_<wbr>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, online prediction access logs are sent to StackDriver Logging.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The list of regions where the model is going to be deployed. Currently only one region per model is supported
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing EngineModel Resource

Get an existing EngineModel resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/ml/#EngineModelState">EngineModelState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/ml/#EngineModel">EngineModel</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>default_version=None<span class="p">, </span>description=None<span class="p">, </span>labels=None<span class="p">, </span>name=None<span class="p">, </span>online_prediction_console_logging=None<span class="p">, </span>online_prediction_logging=None<span class="p">, </span>project=None<span class="p">, </span>regions=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetEngineModel<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/ml?tab=doc#EngineModelState">EngineModelState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/ml?tab=doc#EngineModel">EngineModel</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Ml.EngineModel.html">EngineModel</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Ml.EngineModelState.html">EngineModelState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Default<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#enginemodeldefaultversion">Engine<wbr>Model<wbr>Default<wbr>Version<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The default version of the model. This version will be used to handle prediction requests that do not specify a version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description specified for the model when it was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}One or more labels that you can add, to organize your models.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name specified for the model.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Online<wbr>Prediction<wbr>Console<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Online<wbr>Prediction<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, online prediction access logs are sent to StackDriver Logging.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The list of regions where the model is going to be deployed. Currently only one region per model is supported
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#enginemodeldefaultversion">*Engine<wbr>Model<wbr>Default<wbr>Version</a></span>
    </dt>
    <dd>{{% md %}}The default version of the model. This version will be used to handle prediction requests that do not specify a version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The description specified for the model when it was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}One or more labels that you can add, to organize your models.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name specified for the model.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Online<wbr>Prediction<wbr>Console<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Online<wbr>Prediction<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, online prediction access logs are sent to StackDriver Logging.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The list of regions where the model is going to be deployed. Currently only one region per model is supported
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#enginemodeldefaultversion">Engine<wbr>Model<wbr>Default<wbr>Version?</a></span>
    </dt>
    <dd>{{% md %}}The default version of the model. This version will be used to handle prediction requests that do not specify a version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description specified for the model when it was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}One or more labels that you can add, to organize your models.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name specified for the model.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>online<wbr>Prediction<wbr>Console<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>online<wbr>Prediction<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, online prediction access logs are sent to StackDriver Logging.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The list of regions where the model is going to be deployed. Currently only one region per model is supported
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#enginemodeldefaultversion">Dict[Engine<wbr>Model<wbr>Default<wbr>Version]</a></span>
    </dt>
    <dd>{{% md %}}The default version of the model. This version will be used to handle prediction requests that do not specify a version.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description specified for the model when it was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}One or more labels that you can add, to organize your models.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name specified for the model.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>online_<wbr>prediction_<wbr>console_<wbr>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, online prediction nodes send stderr and stdout streams to Stackdriver Logging
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>online_<wbr>prediction_<wbr>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, online prediction access logs are sent to StackDriver Logging.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The list of regions where the model is going to be deployed. Currently only one region per model is supported
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Engine<wbr>Model<wbr>Default<wbr>Version</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#EngineModelDefaultVersion">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#EngineModelDefaultVersion">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/ml?tab=doc#EngineModelDefaultVersionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/ml?tab=doc#EngineModelDefaultVersionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
