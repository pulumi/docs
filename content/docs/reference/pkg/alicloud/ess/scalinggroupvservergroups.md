
---
title: "ScalingGroupVServerGroups"
block_external_search_index: true
---



Attaches/Detaches vserver groups to a specified scaling group.

> **NOTE:** The load balancer of which vserver groups belongs to must be in `active` status.

> **NOTE:** If scaling group's network type is `VPC`, the vserver groups must be in the same `VPC`.
 
> **NOTE:** A scaling group can have at most 5 vserver groups attached by default.

> **NOTE:** Vserver groups and the default group of loadbalancer share the same backend server quota.

> **NOTE:** When attach vserver groups to scaling group, existing ECS instances will be added to vserver groups; Instead, ECS instances will be removed from vserver group when detach.

> **NOTE:** Detach action will be executed before attach action.

> **NOTE:** Vserver group is defined uniquely by `loadbalancer_id`, `vserver_group_id`, `port`.

> **NOTE:** Modifing `weight` attribute means detach vserver group first and then, attach with new weight parameter.

> **NOTE:** Resource `alicloud.ess.ScalingGroupVServerGroups` is available in 1.53.0+.

## Block vserver_group

the vserver_group supports the following:

* `loadbalancer_id` - (Required) Loadbalancer server ID of VServer Group.
* `vserver_attributes` - (Required) A list of VServer Group attributes. See Block vserver_attribute below for details.

## Block vserver_attribute

* `vserver_group_id` - (Required) ID of VServer Group.
* `port` - (Required) - The port will be used for VServer Group backend server.
* `weight` - (Required) The weight of an ECS instance attached to the VServer Group.

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/ess_scalinggroup_vserver_groups.markdown.



## Create a ScalingGroupVServerGroups Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ess/#ScalingGroupVServerGroups">ScalingGroupVServerGroups</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ess/#ScalingGroupVServerGroupsArgs">ScalingGroupVServerGroupsArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">ScalingGroupVServerGroups</span><span class="p">(resource_name, opts=None, </span>force=None<span class="p">, </span>scaling_group_id=None<span class="p">, </span>vserver_groups=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewScalingGroupVServerGroups<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ess?tab=doc#ScalingGroupVServerGroupsArgs">ScalingGroupVServerGroupsArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ess?tab=doc#ScalingGroupVServerGroups">ScalingGroupVServerGroups</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ess.ScalingGroupVServerGroups.html">ScalingGroupVServerGroups</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ess.ScalingGroupVServerGroupsArgs.html">ScalingGroupVServerGroupsArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the scaling group.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vserver<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scalinggroupvservergroupsvservergroup">List&lt;Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of vserver groups attached on scaling group. See Block vserver_group below for details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the scaling group.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vserver<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scalinggroupvservergroupsvservergroup">[]Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group</a></span>
    </dt>
    <dd>{{% md %}}A list of vserver groups attached on scaling group. See Block vserver_group below for details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the scaling group.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vserver<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scalinggroupvservergroupsvservergroup">Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group[]</a></span>
    </dt>
    <dd>{{% md %}}A list of vserver groups attached on scaling group. See Block vserver_group below for details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scaling_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the scaling group.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vserver_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scalinggroupvservergroupsvservergroup">List[Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group]</a></span>
    </dt>
    <dd>{{% md %}}A list of vserver groups attached on scaling group. See Block vserver_group below for details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## ScalingGroupVServerGroups Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the scaling group.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vserver<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scalinggroupvservergroupsvservergroup">List&lt;Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of vserver groups attached on scaling group. See Block vserver_group below for details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the scaling group.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vserver<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scalinggroupvservergroupsvservergroup">[]Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group</a></span>
    </dt>
    <dd>{{% md %}}A list of vserver groups attached on scaling group. See Block vserver_group below for details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the scaling group.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vserver<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scalinggroupvservergroupsvservergroup">Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group[]</a></span>
    </dt>
    <dd>{{% md %}}A list of vserver groups attached on scaling group. See Block vserver_group below for details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scaling_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the scaling group.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vserver_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scalinggroupvservergroupsvservergroup">List[Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group]</a></span>
    </dt>
    <dd>{{% md %}}A list of vserver groups attached on scaling group. See Block vserver_group below for details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing ScalingGroupVServerGroups Resource

Get an existing ScalingGroupVServerGroups resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ess/#ScalingGroupVServerGroupsState">ScalingGroupVServerGroupsState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ess/#ScalingGroupVServerGroups">ScalingGroupVServerGroups</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>force=None<span class="p">, </span>scaling_group_id=None<span class="p">, </span>vserver_groups=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetScalingGroupVServerGroups<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ess?tab=doc#ScalingGroupVServerGroupsState">ScalingGroupVServerGroupsState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ess?tab=doc#ScalingGroupVServerGroups">ScalingGroupVServerGroups</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ess.ScalingGroupVServerGroups.html">ScalingGroupVServerGroups</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ess.ScalingGroupVServerGroupsState.html">ScalingGroupVServerGroupsState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the scaling group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vserver<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scalinggroupvservergroupsvservergroup">List&lt;Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A list of vserver groups attached on scaling group. See Block vserver_group below for details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ID of the scaling group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vserver<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scalinggroupvservergroupsvservergroup">[]Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group</a></span>
    </dt>
    <dd>{{% md %}}A list of vserver groups attached on scaling group. See Block vserver_group below for details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the scaling group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vserver<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scalinggroupvservergroupsvservergroup">Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group[]?</a></span>
    </dt>
    <dd>{{% md %}}A list of vserver groups attached on scaling group. See Block vserver_group below for details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scaling_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the scaling group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vserver_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scalinggroupvservergroupsvservergroup">List[Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group]</a></span>
    </dt>
    <dd>{{% md %}}A list of vserver groups attached on scaling group. See Block vserver_group below for details.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#ScalingGroupVServerGroupsVserverGroup">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#ScalingGroupVServerGroupsVserverGroup">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ess?tab=doc#ScalingGroupVServerGroupsVserverGroupArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ess?tab=doc#ScalingGroupVServerGroupsVserverGroupOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Loadbalancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vserver<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scalinggroupvservergroupsvservergroupvserverattribute">List&lt;Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group<wbr>Vserver<wbr>Attribute<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Loadbalancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vserver<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scalinggroupvservergroupsvservergroupvserverattribute">[]Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group<wbr>Vserver<wbr>Attribute</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>loadbalancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vserver<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scalinggroupvservergroupsvservergroupvserverattribute">Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group<wbr>Vserver<wbr>Attribute[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>loadbalancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vserver<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#scalinggroupvservergroupsvservergroupvserverattribute">List[Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group<wbr>Vserver<wbr>Attribute]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Scaling<wbr>Group<wbr>VServer<wbr>Groups<wbr>Vserver<wbr>Group<wbr>Vserver<wbr>Attribute</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#ScalingGroupVServerGroupsVserverGroupVserverAttribute">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#ScalingGroupVServerGroupsVserverGroupVserverAttribute">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ess?tab=doc#ScalingGroupVServerGroupsVserverGroupVserverAttributeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ess?tab=doc#ScalingGroupVServerGroupsVserverGroupVserverAttributeOutput">output</a> API doc for this type.
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
        <span>Vserver<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
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
        <span>Vserver<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
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
        <span>vserver<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
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
        <span>vserver<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
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

