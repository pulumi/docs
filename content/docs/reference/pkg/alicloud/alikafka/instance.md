
---
title: "Instance"
block_external_search_index: true
---



Provides an ALIKAFKA instance resource.

> **NOTE:** Available in 1.59.0+

> **NOTE:** ALIKAFKA instance resource only support create post pay instance. Creation or modification may took about 10-40 minutes.

> **NOTE:** Only the following regions support create alikafka pre paid instance.
[`cn-hangzhou`,`cn-beijing`,`cn-shenzhen`,`cn-shanghai`,`cn-qingdao`,`cn-hongkong`,`cn-huhehaote`,`cn-zhangjiakou`,`ap-southeast-1`,`ap-south-1`,`ap-southeast-5`]

> **NOTE:** Only the following regions support create alikafka post paid instance.
[`cn-hangzhou`,`cn-beijing`,`cn-shenzhen`,`cn-shanghai`,`cn-qingdao`,`cn-hongkong`,`cn-huhehaote`,`cn-zhangjiakou`,`ap-southeast-1`]

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/alikafka_instance.html.markdown.



## Create a Instance Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/alikafka/#Instance">Instance</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/alikafka/#InstanceArgs">InstanceArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Instance</span><span class="p">(resource_name, opts=None, </span>deploy_type=None<span class="p">, </span>disk_size=None<span class="p">, </span>disk_type=None<span class="p">, </span>eip_max=None<span class="p">, </span>io_max=None<span class="p">, </span>name=None<span class="p">, </span>paid_type=None<span class="p">, </span>spec_type=None<span class="p">, </span>tags=None<span class="p">, </span>topic_quota=None<span class="p">, </span>vswitch_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewInstance<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/alikafka?tab=doc#InstanceArgs">InstanceArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/alikafka?tab=doc#Instance">Instance</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Alikafka.Instance.html">Instance</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.AliKafka.InstanceArgs.html">InstanceArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Deploy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The deploy type of the instance. Currently only support two deploy type, 4: eip/vpc instance, 5: vpc instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disk<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The disk size of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The disk type of the instance. 0: efficient cloud disk , 1: SSD.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eip<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The max bandwidth of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Io<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The max value of io of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of your Kafka instance. The length should between 3 and 64 characters. If not set, will use instance id as instance name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Paid<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The paid type of the instance. Support two type, "PrePaid": pre paid type instance, "PostPaid": post paid type instance. Default is PostPaid. When modify this value, it only support adjust from post pay to pre pay. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spec<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The spec type of the instance. Support two type, "normal": normal version instance, "professional": professional version instance. Default is normal. When modify this value, it only support adjust from normal to professional. Note only pre paid type instance support professional specific type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Topic<wbr>Quota</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The max num of topic can be create of the instance. When modify this value, it only adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of attaching vswitch to instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Deploy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The deploy type of the instance. Currently only support two deploy type, 4: eip/vpc instance, 5: vpc instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disk<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The disk size of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The disk type of the instance. 0: efficient cloud disk , 1: SSD.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eip<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The max bandwidth of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Io<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The max value of io of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of your Kafka instance. The length should between 3 and 64 characters. If not set, will use instance id as instance name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Paid<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The paid type of the instance. Support two type, "PrePaid": pre paid type instance, "PostPaid": post paid type instance. Default is PostPaid. When modify this value, it only support adjust from post pay to pre pay. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spec<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The spec type of the instance. Support two type, "normal": normal version instance, "professional": professional version instance. Default is normal. When modify this value, it only support adjust from normal to professional. Note only pre paid type instance support professional specific type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Topic<wbr>Quota</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The max num of topic can be create of the instance. When modify this value, it only adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of attaching vswitch to instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>deploy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The deploy type of the instance. Currently only support two deploy type, 4: eip/vpc instance, 5: vpc instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disk<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The disk size of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The disk type of the instance. 0: efficient cloud disk , 1: SSD.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eip<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The max bandwidth of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>io<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The max value of io of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of your Kafka instance. The length should between 3 and 64 characters. If not set, will use instance id as instance name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>paid<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The paid type of the instance. Support two type, "PrePaid": pre paid type instance, "PostPaid": post paid type instance. Default is PostPaid. When modify this value, it only support adjust from post pay to pre pay. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spec<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The spec type of the instance. Support two type, "normal": normal version instance, "professional": professional version instance. Default is normal. When modify this value, it only support adjust from normal to professional. Note only pre paid type instance support professional specific type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>topic<wbr>Quota</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The max num of topic can be create of the instance. When modify this value, it only adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of attaching vswitch to instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>deploy_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The deploy type of the instance. Currently only support two deploy type, 4: eip/vpc instance, 5: vpc instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disk_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The disk size of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disk_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The disk type of the instance. 0: efficient cloud disk , 1: SSD.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eip_<wbr>max</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The max bandwidth of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>io_<wbr>max</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The max value of io of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of your Kafka instance. The length should between 3 and 64 characters. If not set, will use instance id as instance name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>paid_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The paid type of the instance. Support two type, "PrePaid": pre paid type instance, "PostPaid": post paid type instance. Default is PostPaid. When modify this value, it only support adjust from post pay to pre pay. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spec_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The spec type of the instance. Support two type, "normal": normal version instance, "professional": professional version instance. Default is normal. When modify this value, it only support adjust from normal to professional. Note only pre paid type instance support professional specific type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>topic_<wbr>quota</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The max num of topic can be create of the instance. When modify this value, it only adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vswitch_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of attaching vswitch to instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Instance Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Deploy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The deploy type of the instance. Currently only support two deploy type, 4: eip/vpc instance, 5: vpc instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disk<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The disk size of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The disk type of the instance. 0: efficient cloud disk , 1: SSD.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Eip<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The max bandwidth of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Io<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The max value of io of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of your Kafka instance. The length should between 3 and 64 characters. If not set, will use instance id as instance name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Paid<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The paid type of the instance. Support two type, "PrePaid": pre paid type instance, "PostPaid": post paid type instance. Default is PostPaid. When modify this value, it only support adjust from post pay to pre pay. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Spec<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The spec type of the instance. Support two type, "normal": normal version instance, "professional": professional version instance. Default is normal. When modify this value, it only support adjust from normal to professional. Note only pre paid type instance support professional specific type.
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
        <span>Topic<wbr>Quota</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The max num of topic can be create of the instance. When modify this value, it only adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of attaching VPC to instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of attaching vswitch to instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the kafka instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Deploy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The deploy type of the instance. Currently only support two deploy type, 4: eip/vpc instance, 5: vpc instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disk<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The disk size of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The disk type of the instance. 0: efficient cloud disk , 1: SSD.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Eip<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The max bandwidth of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Io<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The max value of io of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of your Kafka instance. The length should between 3 and 64 characters. If not set, will use instance id as instance name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Paid<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The paid type of the instance. Support two type, "PrePaid": pre paid type instance, "PostPaid": post paid type instance. Default is PostPaid. When modify this value, it only support adjust from post pay to pre pay. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Spec<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The spec type of the instance. Support two type, "normal": normal version instance, "professional": professional version instance. Default is normal. When modify this value, it only support adjust from normal to professional. Note only pre paid type instance support professional specific type.
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
        <span>Topic<wbr>Quota</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The max num of topic can be create of the instance. When modify this value, it only adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of attaching VPC to instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of attaching vswitch to instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the kafka instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>deploy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The deploy type of the instance. Currently only support two deploy type, 4: eip/vpc instance, 5: vpc instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disk<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The disk size of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The disk type of the instance. 0: efficient cloud disk , 1: SSD.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>eip<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The max bandwidth of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>io<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The max value of io of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of your Kafka instance. The length should between 3 and 64 characters. If not set, will use instance id as instance name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>paid<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The paid type of the instance. Support two type, "PrePaid": pre paid type instance, "PostPaid": post paid type instance. Default is PostPaid. When modify this value, it only support adjust from post pay to pre pay. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>spec<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The spec type of the instance. Support two type, "normal": normal version instance, "professional": professional version instance. Default is normal. When modify this value, it only support adjust from normal to professional. Note only pre paid type instance support professional specific type.
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
        <span>topic<wbr>Quota</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The max num of topic can be create of the instance. When modify this value, it only adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of attaching VPC to instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of attaching vswitch to instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the kafka instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>deploy_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The deploy type of the instance. Currently only support two deploy type, 4: eip/vpc instance, 5: vpc instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disk_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The disk size of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disk_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The disk type of the instance. 0: efficient cloud disk , 1: SSD.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>eip_<wbr>max</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The max bandwidth of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>io_<wbr>max</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The max value of io of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of your Kafka instance. The length should between 3 and 64 characters. If not set, will use instance id as instance name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>paid_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The paid type of the instance. Support two type, "PrePaid": pre paid type instance, "PostPaid": post paid type instance. Default is PostPaid. When modify this value, it only support adjust from post pay to pre pay. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>spec_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The spec type of the instance. Support two type, "normal": normal version instance, "professional": professional version instance. Default is normal. When modify this value, it only support adjust from normal to professional. Note only pre paid type instance support professional specific type.
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
        <span>topic_<wbr>quota</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The max num of topic can be create of the instance. When modify this value, it only adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of attaching VPC to instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vswitch_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of attaching vswitch to instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the kafka instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Instance Resource

Get an existing Instance resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/alikafka/#InstanceState">InstanceState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/alikafka/#Instance">Instance</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>deploy_type=None<span class="p">, </span>disk_size=None<span class="p">, </span>disk_type=None<span class="p">, </span>eip_max=None<span class="p">, </span>io_max=None<span class="p">, </span>name=None<span class="p">, </span>paid_type=None<span class="p">, </span>spec_type=None<span class="p">, </span>tags=None<span class="p">, </span>topic_quota=None<span class="p">, </span>vpc_id=None<span class="p">, </span>vswitch_id=None<span class="p">, </span>zone_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetInstance<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/alikafka?tab=doc#InstanceState">InstanceState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/alikafka?tab=doc#Instance">Instance</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Alikafka.Instance.html">Instance</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Alikafka.InstanceState.html">InstanceState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Deploy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The deploy type of the instance. Currently only support two deploy type, 4: eip/vpc instance, 5: vpc instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The disk size of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The disk type of the instance. 0: efficient cloud disk , 1: SSD.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eip<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The max bandwidth of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Io<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The max value of io of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of your Kafka instance. The length should between 3 and 64 characters. If not set, will use instance id as instance name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Paid<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The paid type of the instance. Support two type, "PrePaid": pre paid type instance, "PostPaid": post paid type instance. Default is PostPaid. When modify this value, it only support adjust from post pay to pre pay. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spec<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The spec type of the instance. Support two type, "normal": normal version instance, "professional": professional version instance. Default is normal. When modify this value, it only support adjust from normal to professional. Note only pre paid type instance support professional specific type.
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
        <span>Topic<wbr>Quota</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The max num of topic can be create of the instance. When modify this value, it only adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of attaching VPC to instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of attaching vswitch to instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the kafka instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Deploy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The deploy type of the instance. Currently only support two deploy type, 4: eip/vpc instance, 5: vpc instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The disk size of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The disk type of the instance. 0: efficient cloud disk , 1: SSD.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eip<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The max bandwidth of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Io<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The max value of io of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of your Kafka instance. The length should between 3 and 64 characters. If not set, will use instance id as instance name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Paid<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The paid type of the instance. Support two type, "PrePaid": pre paid type instance, "PostPaid": post paid type instance. Default is PostPaid. When modify this value, it only support adjust from post pay to pre pay. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spec<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The spec type of the instance. Support two type, "normal": normal version instance, "professional": professional version instance. Default is normal. When modify this value, it only support adjust from normal to professional. Note only pre paid type instance support professional specific type.
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
        <span>Topic<wbr>Quota</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The max num of topic can be create of the instance. When modify this value, it only adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of attaching VPC to instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of attaching vswitch to instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the kafka instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>deploy<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The deploy type of the instance. Currently only support two deploy type, 4: eip/vpc instance, 5: vpc instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The disk size of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The disk type of the instance. 0: efficient cloud disk , 1: SSD.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eip<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The max bandwidth of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>io<wbr>Max</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The max value of io of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of your Kafka instance. The length should between 3 and 64 characters. If not set, will use instance id as instance name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>paid<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The paid type of the instance. Support two type, "PrePaid": pre paid type instance, "PostPaid": post paid type instance. Default is PostPaid. When modify this value, it only support adjust from post pay to pre pay. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spec<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The spec type of the instance. Support two type, "normal": normal version instance, "professional": professional version instance. Default is normal. When modify this value, it only support adjust from normal to professional. Note only pre paid type instance support professional specific type.
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
        <span>topic<wbr>Quota</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The max num of topic can be create of the instance. When modify this value, it only adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of attaching VPC to instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of attaching vswitch to instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the kafka instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>deploy_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The deploy type of the instance. Currently only support two deploy type, 4: eip/vpc instance, 5: vpc instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The disk size of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The disk type of the instance. 0: efficient cloud disk , 1: SSD.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eip_<wbr>max</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The max bandwidth of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>io_<wbr>max</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The max value of io of the instance. When modify this value, it only support adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of your Kafka instance. The length should between 3 and 64 characters. If not set, will use instance id as instance name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>paid_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The paid type of the instance. Support two type, "PrePaid": pre paid type instance, "PostPaid": post paid type instance. Default is PostPaid. When modify this value, it only support adjust from post pay to pre pay. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spec_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The spec type of the instance. Support two type, "normal": normal version instance, "professional": professional version instance. Default is normal. When modify this value, it only support adjust from normal to professional. Note only pre paid type instance support professional specific type.
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
        <span>topic_<wbr>quota</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The max num of topic can be create of the instance. When modify this value, it only adjust to a greater value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of attaching VPC to instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vswitch_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of attaching vswitch to instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the kafka instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-alicloud">https://github.com/pulumi/pulumi-alicloud</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

