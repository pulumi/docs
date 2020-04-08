
---
title: "Node"
block_external_search_index: true
---



A Cloud TPU instance.


To get more information about Node, see:

* [API documentation](https://cloud.google.com/tpu/docs/reference/rest/)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/tpu/docs/)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/tpu_node.html.markdown.



## Create a Node Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/tpu/#Node">Node</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/tpu/#NodeArgs">NodeArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Node</span><span class="p">(resource_name, opts=None, </span>accelerator_type=None<span class="p">, </span>cidr_block=None<span class="p">, </span>description=None<span class="p">, </span>labels=None<span class="p">, </span>name=None<span class="p">, </span>network=None<span class="p">, </span>project=None<span class="p">, </span>scheduling_config=None<span class="p">, </span>tensorflow_version=None<span class="p">, </span>zone=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewNode<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/tpu?tab=doc#NodeArgs">NodeArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/tpu?tab=doc#Node">Node</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Tpu.Node.html">Node</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Tpu.NodeArgs.html">NodeArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Accelerator<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of hardware accelerators associated with this node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute
Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP
address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block
conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network
that is using that CIDR block.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The user-supplied description of the TPU. Maximum of 512 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The immutable name of the TPU.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a network to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on
which this API has been activated. If none is provided, "default" will be used.
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
        <span>Scheduling<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeschedulingconfig">Node<wbr>Scheduling<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Sets the scheduling options for this TPU instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tensorflow<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version of Tensorflow running in the Node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The GCP location for the TPU.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Accelerator<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of hardware accelerators associated with this node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute
Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP
address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block
conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network
that is using that CIDR block.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The user-supplied description of the TPU. Maximum of 512 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The immutable name of the TPU.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of a network to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on
which this API has been activated. If none is provided, "default" will be used.
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
        <span>Scheduling<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeschedulingconfig">*Node<wbr>Scheduling<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Sets the scheduling options for this TPU instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tensorflow<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version of Tensorflow running in the Node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The GCP location for the TPU.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>accelerator<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of hardware accelerators associated with this node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute
Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP
address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block
conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network
that is using that CIDR block.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The user-supplied description of the TPU. Maximum of 512 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The immutable name of the TPU.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a network to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on
which this API has been activated. If none is provided, "default" will be used.
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
        <span>scheduling<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeschedulingconfig">Node<wbr>Scheduling<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Sets the scheduling options for this TPU instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tensorflow<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version of Tensorflow running in the Node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The GCP location for the TPU.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>accelerator_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of hardware accelerators associated with this node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cidr_<wbr>block</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute
Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP
address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block
conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network
that is using that CIDR block.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The user-supplied description of the TPU. Maximum of 512 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The immutable name of the TPU.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of a network to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on
which this API has been activated. If none is provided, "default" will be used.
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
        <span>scheduling_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeschedulingconfig">Dict[Node<wbr>Scheduling<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Sets the scheduling options for this TPU instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tensorflow_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The version of Tensorflow running in the Node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The GCP location for the TPU.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Node Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Accelerator<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of hardware accelerators associated with this node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute
Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP
address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block
conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network
that is using that CIDR block.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The user-supplied description of the TPU. Maximum of 512 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The immutable name of the TPU.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of a network to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on
which this API has been activated. If none is provided, "default" will be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodenetworkendpoint">List&lt;Node<wbr>Network<wbr>Endpoint&gt;</a></span>
    </dt>
    <dd>{{% md %}}The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the
node first reach out to the first (index 0) entry.
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
        <span>Scheduling<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeschedulingconfig">Node<wbr>Scheduling<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Sets the scheduling options for this TPU instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The service account used to run the tensor flow services within the node. To share resources, including Google Cloud
Storage data, with the Tensorflow job running in the Node, this account must have permissions to that data.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tensorflow<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version of Tensorflow running in the Node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The GCP location for the TPU.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Accelerator<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of hardware accelerators associated with this node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute
Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP
address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block
conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network
that is using that CIDR block.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The user-supplied description of the TPU. Maximum of 512 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The immutable name of the TPU.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of a network to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on
which this API has been activated. If none is provided, "default" will be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodenetworkendpoint">[]Node<wbr>Network<wbr>Endpoint</a></span>
    </dt>
    <dd>{{% md %}}The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the
node first reach out to the first (index 0) entry.
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
        <span>Scheduling<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeschedulingconfig">*Node<wbr>Scheduling<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Sets the scheduling options for this TPU instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The service account used to run the tensor flow services within the node. To share resources, including Google Cloud
Storage data, with the Tensorflow job running in the Node, this account must have permissions to that data.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tensorflow<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version of Tensorflow running in the Node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The GCP location for the TPU.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>accelerator<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of hardware accelerators associated with this node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute
Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP
address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block
conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network
that is using that CIDR block.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The user-supplied description of the TPU. Maximum of 512 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The immutable name of the TPU.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of a network to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on
which this API has been activated. If none is provided, "default" will be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodenetworkendpoint">Node<wbr>Network<wbr>Endpoint[]</a></span>
    </dt>
    <dd>{{% md %}}The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the
node first reach out to the first (index 0) entry.
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
        <span>scheduling<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeschedulingconfig">Node<wbr>Scheduling<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Sets the scheduling options for this TPU instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The service account used to run the tensor flow services within the node. To share resources, including Google Cloud
Storage data, with the Tensorflow job running in the Node, this account must have permissions to that data.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tensorflow<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version of Tensorflow running in the Node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The GCP location for the TPU.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>accelerator_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of hardware accelerators associated with this node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cidr_<wbr>block</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute
Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP
address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block
conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network
that is using that CIDR block.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The user-supplied description of the TPU. Maximum of 512 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The immutable name of the TPU.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of a network to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on
which this API has been activated. If none is provided, "default" will be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodenetworkendpoint">List[Node<wbr>Network<wbr>Endpoint]</a></span>
    </dt>
    <dd>{{% md %}}The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the
node first reach out to the first (index 0) entry.
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
        <span>scheduling_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeschedulingconfig">Dict[Node<wbr>Scheduling<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Sets the scheduling options for this TPU instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service_<wbr>account</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The service account used to run the tensor flow services within the node. To share resources, including Google Cloud
Storage data, with the Tensorflow job running in the Node, this account must have permissions to that data.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tensorflow_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The version of Tensorflow running in the Node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The GCP location for the TPU.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Node Resource

Get an existing Node resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/tpu/#NodeState">NodeState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/tpu/#Node">Node</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>accelerator_type=None<span class="p">, </span>cidr_block=None<span class="p">, </span>description=None<span class="p">, </span>labels=None<span class="p">, </span>name=None<span class="p">, </span>network=None<span class="p">, </span>network_endpoints=None<span class="p">, </span>project=None<span class="p">, </span>scheduling_config=None<span class="p">, </span>service_account=None<span class="p">, </span>tensorflow_version=None<span class="p">, </span>zone=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetNode<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/tpu?tab=doc#NodeState">NodeState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/tpu?tab=doc#Node">Node</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Tpu.Node.html">Node</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Tpu.NodeState.html">NodeState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Accelerator<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of hardware accelerators associated with this node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute
Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP
address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block
conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network
that is using that CIDR block.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The user-supplied description of the TPU. Maximum of 512 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The immutable name of the TPU.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a network to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on
which this API has been activated. If none is provided, "default" will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodenetworkendpoint">List&lt;Node<wbr>Network<wbr>Endpoint<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the
node first reach out to the first (index 0) entry.
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
        <span>Scheduling<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeschedulingconfig">Node<wbr>Scheduling<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Sets the scheduling options for this TPU instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service account used to run the tensor flow services within the node. To share resources, including Google Cloud
Storage data, with the Tensorflow job running in the Node, this account must have permissions to that data.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tensorflow<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version of Tensorflow running in the Node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The GCP location for the TPU.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Accelerator<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of hardware accelerators associated with this node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute
Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP
address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block
conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network
that is using that CIDR block.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The user-supplied description of the TPU. Maximum of 512 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The immutable name of the TPU.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of a network to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on
which this API has been activated. If none is provided, "default" will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodenetworkendpoint">[]Node<wbr>Network<wbr>Endpoint</a></span>
    </dt>
    <dd>{{% md %}}The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the
node first reach out to the first (index 0) entry.
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
        <span>Scheduling<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeschedulingconfig">*Node<wbr>Scheduling<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Sets the scheduling options for this TPU instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The service account used to run the tensor flow services within the node. To share resources, including Google Cloud
Storage data, with the Tensorflow job running in the Node, this account must have permissions to that data.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tensorflow<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The version of Tensorflow running in the Node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The GCP location for the TPU.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accelerator<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of hardware accelerators associated with this node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute
Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP
address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block
conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network
that is using that CIDR block.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The user-supplied description of the TPU. Maximum of 512 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The immutable name of the TPU.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a network to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on
which this API has been activated. If none is provided, "default" will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodenetworkendpoint">Node<wbr>Network<wbr>Endpoint[]?</a></span>
    </dt>
    <dd>{{% md %}}The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the
node first reach out to the first (index 0) entry.
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
        <span>scheduling<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeschedulingconfig">Node<wbr>Scheduling<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Sets the scheduling options for this TPU instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service account used to run the tensor flow services within the node. To share resources, including Google Cloud
Storage data, with the Tensorflow job running in the Node, this account must have permissions to that data.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tensorflow<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version of Tensorflow running in the Node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The GCP location for the TPU.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accelerator_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of hardware accelerators associated with this node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cidr_<wbr>block</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute
Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP
address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block
conflicts with any subnetworks in the user's provided network, or the provided network is peered with another network
that is using that CIDR block.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The user-supplied description of the TPU. Maximum of 512 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The immutable name of the TPU.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of a network to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on
which this API has been activated. If none is provided, "default" will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>endpoints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodenetworkendpoint">List[Node<wbr>Network<wbr>Endpoint]</a></span>
    </dt>
    <dd>{{% md %}}The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the
node first reach out to the first (index 0) entry.
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
        <span>scheduling_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodeschedulingconfig">Dict[Node<wbr>Scheduling<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Sets the scheduling options for this TPU instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>account</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The service account used to run the tensor flow services within the node. To share resources, including Google Cloud
Storage data, with the Tensorflow job running in the Node, this account must have permissions to that data.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tensorflow_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The version of Tensorflow running in the Node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The GCP location for the TPU.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Node<wbr>Network<wbr>Endpoint</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#NodeNetworkEndpoint">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/tpu?tab=doc#NodeNetworkEndpointOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
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
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
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
        <span>ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
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
        <span>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Node<wbr>Scheduling<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#NodeSchedulingConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#NodeSchedulingConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/tpu?tab=doc#NodeSchedulingConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/tpu?tab=doc#NodeSchedulingConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
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
    
</dl>

