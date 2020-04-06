
---
title: "ServerGroup"
block_external_search_index: true
---



A virtual server group contains several ECS instances. The virtual server group can help you to define multiple listening dimension,
and to meet the personalized requirements of domain name and URL forwarding.

> **NOTE:** One ECS instance can be added into multiple virtual server groups.

> **NOTE:** One virtual server group can be attached with multiple listeners in one load balancer.

> **NOTE:** One Classic and Internet load balancer, its virtual server group can add Classic and VPC ECS instances.

> **NOTE:** One Classic and Intranet load balancer, its virtual server group can only add Classic ECS instances.

> **NOTE:** One VPC load balancer, its virtual server group can only add the same VPC ECS instances.

## Block servers

The servers mapping supports the following:

* `server_ids` - (Required) A list backend server ID (ECS instance ID).
* `port` - (Required) The port used by the backend server. Valid value range: [1-65535].
* `weight` - (Optional) Weight of the backend server. Valid value range: [0-100]. Default to 100.
* `type` - (Optional, Available in 1.51.0+) Type of the backend server. Valid value ecs, eni. Default to eni.

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/slb_server_group.html.markdown.



## Create a ServerGroup Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/slb/#ServerGroup">ServerGroup</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/slb/#ServerGroupArgs">ServerGroupArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">ServerGroup</span><span class="p">(resource_name, opts=None, </span>delete_protection_validation=None<span class="p">, </span>load_balancer_id=None<span class="p">, </span>name=None<span class="p">, </span>servers=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewServerGroup<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#ServerGroupArgs">ServerGroupArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#ServerGroup">ServerGroup</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Slb.ServerGroup.html">ServerGroup</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Slb.ServerGroupArgs.html">ServerGroupArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Load Balancer ID which is used to launch a new virtual server group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the virtual server group. Our plugin provides a default name: "tf-server-group".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#servergroupserver">List&lt;Server<wbr>Group<wbr>Server<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A list of ECS instances to be added. At most 20 ECS instances can be supported in one resource. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Load Balancer ID which is used to launch a new virtual server group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the virtual server group. Our plugin provides a default name: "tf-server-group".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#servergroupserver">[]Server<wbr>Group<wbr>Server</a></span>
    </dt>
    <dd>{{% md %}}A list of ECS instances to be added. At most 20 ECS instances can be supported in one resource. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Load Balancer ID which is used to launch a new virtual server group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the virtual server group. Our plugin provides a default name: "tf-server-group".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#servergroupserver">Server<wbr>Group<wbr>Server[]?</a></span>
    </dt>
    <dd>{{% md %}}A list of ECS instances to be added. At most 20 ECS instances can be supported in one resource. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>delete_<wbr>protection_<wbr>validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>load_<wbr>balancer_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Load Balancer ID which is used to launch a new virtual server group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the virtual server group. Our plugin provides a default name: "tf-server-group".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#servergroupserver">List[Server<wbr>Group<wbr>Server]</a></span>
    </dt>
    <dd>{{% md %}}A list of ECS instances to be added. At most 20 ECS instances can be supported in one resource. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## ServerGroup Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Load Balancer ID which is used to launch a new virtual server group.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the virtual server group. Our plugin provides a default name: "tf-server-group".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#servergroupserver">List&lt;Server<wbr>Group<wbr>Server&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of ECS instances to be added. At most 20 ECS instances can be supported in one resource. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Load Balancer ID which is used to launch a new virtual server group.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the virtual server group. Our plugin provides a default name: "tf-server-group".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#servergroupserver">[]Server<wbr>Group<wbr>Server</a></span>
    </dt>
    <dd>{{% md %}}A list of ECS instances to be added. At most 20 ECS instances can be supported in one resource. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Load Balancer ID which is used to launch a new virtual server group.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the virtual server group. Our plugin provides a default name: "tf-server-group".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#servergroupserver">Server<wbr>Group<wbr>Server[]</a></span>
    </dt>
    <dd>{{% md %}}A list of ECS instances to be added. At most 20 ECS instances can be supported in one resource. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>delete_<wbr>protection_<wbr>validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>load_<wbr>balancer_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Load Balancer ID which is used to launch a new virtual server group.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the virtual server group. Our plugin provides a default name: "tf-server-group".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#servergroupserver">List[Server<wbr>Group<wbr>Server]</a></span>
    </dt>
    <dd>{{% md %}}A list of ECS instances to be added. At most 20 ECS instances can be supported in one resource. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing ServerGroup Resource

Get an existing ServerGroup resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/slb/#ServerGroupState">ServerGroupState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/slb/#ServerGroup">ServerGroup</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>delete_protection_validation=None<span class="p">, </span>load_balancer_id=None<span class="p">, </span>name=None<span class="p">, </span>servers=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetServerGroup<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#ServerGroupState">ServerGroupState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#ServerGroup">ServerGroup</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Slb.ServerGroup.html">ServerGroup</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Slb.ServerGroupState.html">ServerGroupState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Load Balancer ID which is used to launch a new virtual server group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the virtual server group. Our plugin provides a default name: "tf-server-group".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#servergroupserver">List&lt;Server<wbr>Group<wbr>Server<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A list of ECS instances to be added. At most 20 ECS instances can be supported in one resource. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Load Balancer ID which is used to launch a new virtual server group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the virtual server group. Our plugin provides a default name: "tf-server-group".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#servergroupserver">[]Server<wbr>Group<wbr>Server</a></span>
    </dt>
    <dd>{{% md %}}A list of ECS instances to be added. At most 20 ECS instances can be supported in one resource. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Load Balancer ID which is used to launch a new virtual server group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the virtual server group. Our plugin provides a default name: "tf-server-group".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#servergroupserver">Server<wbr>Group<wbr>Server[]?</a></span>
    </dt>
    <dd>{{% md %}}A list of ECS instances to be added. At most 20 ECS instances can be supported in one resource. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>delete_<wbr>protection_<wbr>validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load_<wbr>balancer_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Load Balancer ID which is used to launch a new virtual server group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the virtual server group. Our plugin provides a default name: "tf-server-group".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#servergroupserver">List[Server<wbr>Group<wbr>Server]</a></span>
    </dt>
    <dd>{{% md %}}A list of ECS instances to be added. At most 20 ECS instances can be supported in one resource. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Server<wbr>Group<wbr>Server</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#ServerGroupServer">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#ServerGroupServer">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#ServerGroupServerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#ServerGroupServerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-alicloud">https://github.com/pulumi/pulumi-alicloud</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

