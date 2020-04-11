
---
title: "Model"
block_external_search_index: true
---



Provides a SageMaker model resource.

{{% examples %}}
## Example Usage
{{% example %}}

Basic usage:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const model = new aws.sagemaker.Model("m", {
    executionRoleArn: aws_iam_role_foo.arn,
    primaryContainer: {
        image: "174872318107.dkr.ecr.us-west-2.amazonaws.com/kmeans:1",
    },
});
const assumeRole = pulumi.output(aws.iam.getPolicyDocument({
    statements: [{
        actions: ["sts:AssumeRole"],
        principals: [{
            identifiers: ["sagemaker.amazonaws.com"],
            type: "Service",
        }],
    }],
}, { async: true }));
const role = new aws.iam.Role("r", {
    assumeRolePolicy: assumeRole.json,
});
```

{{% /example %}}
{{% /examples %}}



## Create a Model Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/sagemaker/#Model">Model</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/sagemaker/#ModelArgs">ModelArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Model</span><span class="p">(resource_name, opts=None, </span>containers=None<span class="p">, </span>enable_network_isolation=None<span class="p">, </span>execution_role_arn=None<span class="p">, </span>name=None<span class="p">, </span>primary_container=None<span class="p">, </span>tags=None<span class="p">, </span>vpc_config=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewModel<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#ModelArgs">ModelArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#Model">Model</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Sagemaker.Model.html">Model</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Sagemaker.ModelArgs.html">ModelArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelcontainer">List&lt;Model<wbr>Container<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Network<wbr>Isolation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Execution<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A role that SageMaker can assume to access model artifacts and docker images for deployment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Primary<wbr>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelprimarycontainer">Model<wbr>Primary<wbr>Container<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelvpcconfig">Model<wbr>Vpc<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelcontainer">[]Model<wbr>Container</a></span>
    </dt>
    <dd>{{% md %}}Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Network<wbr>Isolation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Execution<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A role that SageMaker can assume to access model artifacts and docker images for deployment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Primary<wbr>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelprimarycontainer">*Model<wbr>Primary<wbr>Container</a></span>
    </dt>
    <dd>{{% md %}}The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelvpcconfig">*Model<wbr>Vpc<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelcontainer">Model<wbr>Container[]?</a></span>
    </dt>
    <dd>{{% md %}}Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Network<wbr>Isolation</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>execution<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A role that SageMaker can assume to access model artifacts and docker images for deployment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>primary<wbr>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelprimarycontainer">Model<wbr>Primary<wbr>Container?</a></span>
    </dt>
    <dd>{{% md %}}The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelvpcconfig">Model<wbr>Vpc<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelcontainer">List[Model<wbr>Container]</a></span>
    </dt>
    <dd>{{% md %}}Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>network_<wbr>isolation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>execution_<wbr>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A role that SageMaker can assume to access model artifacts and docker images for deployment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>primary_<wbr>container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelprimarycontainer">Dict[Model<wbr>Primary<wbr>Container]</a></span>
    </dt>
    <dd>{{% md %}}The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelvpcconfig">Dict[Model<wbr>Vpc<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Model Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) assigned by AWS to this model.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelcontainer">List&lt;Model<wbr>Container&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Network<wbr>Isolation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Execution<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A role that SageMaker can assume to access model artifacts and docker images for deployment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Primary<wbr>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelprimarycontainer">Model<wbr>Primary<wbr>Container?</a></span>
    </dt>
    <dd>{{% md %}}The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelvpcconfig">Model<wbr>Vpc<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
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
    <dd>{{% md %}}The Amazon Resource Name (ARN) assigned by AWS to this model.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelcontainer">[]Model<wbr>Container</a></span>
    </dt>
    <dd>{{% md %}}Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Network<wbr>Isolation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Execution<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A role that SageMaker can assume to access model artifacts and docker images for deployment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Primary<wbr>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelprimarycontainer">*Model<wbr>Primary<wbr>Container</a></span>
    </dt>
    <dd>{{% md %}}The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelvpcconfig">*Model<wbr>Vpc<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
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
    <dd>{{% md %}}The Amazon Resource Name (ARN) assigned by AWS to this model.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelcontainer">Model<wbr>Container[]?</a></span>
    </dt>
    <dd>{{% md %}}Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Network<wbr>Isolation</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>execution<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A role that SageMaker can assume to access model artifacts and docker images for deployment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>primary<wbr>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelprimarycontainer">Model<wbr>Primary<wbr>Container?</a></span>
    </dt>
    <dd>{{% md %}}The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelvpcconfig">Model<wbr>Vpc<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
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
    <dd>{{% md %}}The Amazon Resource Name (ARN) assigned by AWS to this model.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelcontainer">List[Model<wbr>Container]</a></span>
    </dt>
    <dd>{{% md %}}Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>network_<wbr>isolation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>execution_<wbr>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A role that SageMaker can assume to access model artifacts and docker images for deployment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>primary_<wbr>container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelprimarycontainer">Dict[Model<wbr>Primary<wbr>Container]</a></span>
    </dt>
    <dd>{{% md %}}The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelvpcconfig">Dict[Model<wbr>Vpc<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Model Resource

Get an existing Model resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/sagemaker/#ModelState">ModelState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/sagemaker/#Model">Model</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>containers=None<span class="p">, </span>enable_network_isolation=None<span class="p">, </span>execution_role_arn=None<span class="p">, </span>name=None<span class="p">, </span>primary_container=None<span class="p">, </span>tags=None<span class="p">, </span>vpc_config=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetModel<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#ModelState">ModelState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#Model">Model</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Sagemaker.Model.html">Model</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Sagemaker.ModelState.html">ModelState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
    <dd>{{% md %}}The Amazon Resource Name (ARN) assigned by AWS to this model.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelcontainer">List&lt;Model<wbr>Container<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Network<wbr>Isolation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Execution<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A role that SageMaker can assume to access model artifacts and docker images for deployment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Primary<wbr>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelprimarycontainer">Model<wbr>Primary<wbr>Container<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelvpcconfig">Model<wbr>Vpc<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
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
    <dd>{{% md %}}The Amazon Resource Name (ARN) assigned by AWS to this model.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelcontainer">[]Model<wbr>Container</a></span>
    </dt>
    <dd>{{% md %}}Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Network<wbr>Isolation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Execution<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A role that SageMaker can assume to access model artifacts and docker images for deployment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Primary<wbr>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelprimarycontainer">*Model<wbr>Primary<wbr>Container</a></span>
    </dt>
    <dd>{{% md %}}The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelvpcconfig">*Model<wbr>Vpc<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
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
    <dd>{{% md %}}The Amazon Resource Name (ARN) assigned by AWS to this model.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelcontainer">Model<wbr>Container[]?</a></span>
    </dt>
    <dd>{{% md %}}Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Network<wbr>Isolation</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>execution<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A role that SageMaker can assume to access model artifacts and docker images for deployment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>primary<wbr>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelprimarycontainer">Model<wbr>Primary<wbr>Container?</a></span>
    </dt>
    <dd>{{% md %}}The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelvpcconfig">Model<wbr>Vpc<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
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
    <dd>{{% md %}}The Amazon Resource Name (ARN) assigned by AWS to this model.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>containers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelcontainer">List[Model<wbr>Container]</a></span>
    </dt>
    <dd>{{% md %}}Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>network_<wbr>isolation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>execution_<wbr>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A role that SageMaker can assume to access model artifacts and docker images for deployment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the model (must be unique). If omitted, this provider will assign a random, unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>primary_<wbr>container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelprimarycontainer">Dict[Model<wbr>Primary<wbr>Container]</a></span>
    </dt>
    <dd>{{% md %}}The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#modelvpcconfig">Dict[Model<wbr>Vpc<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Model<wbr>Container</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ModelContainer">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ModelContainer">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#ModelContainerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#ModelContainerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The DNS host name for the container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Environment</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Environment variables for the Docker container.
A list of key value pairs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The registry path where the inference code image is stored in Amazon ECR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Model<wbr>Data<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URL for the S3 location where model artifacts are stored.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The DNS host name for the container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Environment</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Environment variables for the Docker container.
A list of key value pairs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The registry path where the inference code image is stored in Amazon ECR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Model<wbr>Data<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The URL for the S3 location where model artifacts are stored.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>container<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The DNS host name for the container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>environment</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Environment variables for the Docker container.
A list of key value pairs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The registry path where the inference code image is stored in Amazon ECR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>model<wbr>Data<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URL for the S3 location where model artifacts are stored.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>container<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The DNS host name for the container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>environment</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Environment variables for the Docker container.
A list of key value pairs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The registry path where the inference code image is stored in Amazon ECR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>model<wbr>Data<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URL for the S3 location where model artifacts are stored.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Model<wbr>Primary<wbr>Container</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ModelPrimaryContainer">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ModelPrimaryContainer">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#ModelPrimaryContainerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#ModelPrimaryContainerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The DNS host name for the container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Environment</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Environment variables for the Docker container.
A list of key value pairs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The registry path where the inference code image is stored in Amazon ECR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Model<wbr>Data<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URL for the S3 location where model artifacts are stored.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The DNS host name for the container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Environment</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Environment variables for the Docker container.
A list of key value pairs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The registry path where the inference code image is stored in Amazon ECR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Model<wbr>Data<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The URL for the S3 location where model artifacts are stored.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>container<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The DNS host name for the container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>environment</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Environment variables for the Docker container.
A list of key value pairs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The registry path where the inference code image is stored in Amazon ECR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>model<wbr>Data<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URL for the S3 location where model artifacts are stored.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>container<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The DNS host name for the container.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>environment</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Environment variables for the Docker container.
A list of key value pairs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The registry path where the inference code image is stored in Amazon ECR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>model<wbr>Data<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URL for the S3 location where model artifacts are stored.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Model<wbr>Vpc<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ModelVpcConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ModelVpcConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#ModelVpcConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/sagemaker?tab=doc#ModelVpcConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnets</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
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
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnets</span>
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
        <span>security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnets</span>
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
        <span>security_<wbr>group_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnets</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
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

