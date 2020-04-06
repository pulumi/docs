
---
title: "Cluster"
block_external_search_index: true
---



Provides a ADB cluster resource. A ADB cluster is an isolated database
environment in the cloud. A ADB cluster can contain multiple user-created
databases.

> **NOTE:** Available in v1.71.0+.

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/adb_cluster.html.markdown.



## Create a Cluster Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/adb/#Cluster">Cluster</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/adb/#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Cluster</span><span class="p">(resource_name, opts=None, </span>auto_renew_period=None<span class="p">, </span>db_cluster_category=None<span class="p">, </span>db_cluster_version=None<span class="p">, </span>db_node_class=None<span class="p">, </span>db_node_count=None<span class="p">, </span>db_node_storage=None<span class="p">, </span>description=None<span class="p">, </span>maintain_time=None<span class="p">, </span>pay_type=None<span class="p">, </span>period=None<span class="p">, </span>renewal_status=None<span class="p">, </span>security_ips=None<span class="p">, </span>tags=None<span class="p">, </span>vswitch_id=None<span class="p">, </span>zone_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/adb?tab=doc#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/adb?tab=doc#Cluster">Cluster</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Adb.Cluster.html">Cluster</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Adb.ClusterArgs.html">ClusterArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is `PrePaid`. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Cluster<wbr>Category</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cluster category. Value options: `Basic`, `Cluster`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cluster version. Value options: `3.0`, Default to `3.0`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_class of cluster node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The db_node_count of cluster node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The db_node_storage of cluster node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`. Currently, the resource can not supports change pay type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB cluster (in month). It is valid when pay_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renewal<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `AutoRenewal`, `Normal`, `NotRenewal`, Default to `NotRenewal`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is `PrePaid`. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Cluster<wbr>Category</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cluster category. Value options: `Basic`, `Cluster`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Cluster version. Value options: `3.0`, Default to `3.0`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_class of cluster node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The db_node_count of cluster node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The db_node_storage of cluster node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The description of cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`. Currently, the resource can not supports change pay type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB cluster (in month). It is valid when pay_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renewal<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Valid values are `AutoRenewal`, `Normal`, `NotRenewal`, Default to `NotRenewal`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is `PrePaid`. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Cluster<wbr>Category</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cluster category. Value options: `Basic`, `Cluster`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>db<wbr>Cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cluster version. Value options: `3.0`, Default to `3.0`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Node<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_class of cluster node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The db_node_count of cluster node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Node<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The db_node_storage of cluster node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`. Currently, the resource can not supports change pay type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB cluster (in month). It is valid when pay_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renewal<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `AutoRenewal`, `Normal`, `NotRenewal`, Default to `NotRenewal`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto_<wbr>renew_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is `PrePaid`. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db_<wbr>cluster_<wbr>category</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cluster category. Value options: `Basic`, `Cluster`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>db_<wbr>cluster_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cluster version. Value options: `3.0`, Default to `3.0`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db_<wbr>node_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The db_node_class of cluster node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db_<wbr>node_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The db_node_count of cluster node.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db_<wbr>node_<wbr>storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The db_node_storage of cluster node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description of cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintain_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pay_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`. Currently, the resource can not supports change pay type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB cluster (in month). It is valid when pay_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renewal_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Valid values are `AutoRenewal`, `Normal`, `NotRenewal`, Default to `NotRenewal`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vswitch_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Cluster Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is `PrePaid`. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Cluster<wbr>Category</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cluster category. Value options: `Basic`, `Cluster`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cluster version. Value options: `3.0`, Default to `3.0`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Node<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_class of cluster node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The db_node_count of cluster node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Node<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The db_node_storage of cluster node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`. Currently, the resource can not supports change pay type.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB cluster (in month). It is valid when pay_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Renewal<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `AutoRenewal`, `Normal`, `NotRenewal`, Default to `NotRenewal`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is `PrePaid`. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Cluster<wbr>Category</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cluster category. Value options: `Basic`, `Cluster`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Cluster version. Value options: `3.0`, Default to `3.0`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Node<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_class of cluster node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The db_node_count of cluster node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Node<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The db_node_storage of cluster node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The description of cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`. Currently, the resource can not supports change pay type.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB cluster (in month). It is valid when pay_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Renewal<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Valid values are `AutoRenewal`, `Normal`, `NotRenewal`, Default to `NotRenewal`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is `PrePaid`. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db<wbr>Cluster<wbr>Category</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cluster category. Value options: `Basic`, `Cluster`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db<wbr>Cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cluster version. Value options: `3.0`, Default to `3.0`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db<wbr>Node<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_class of cluster node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The db_node_count of cluster node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db<wbr>Node<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The db_node_storage of cluster node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`. Currently, the resource can not supports change pay type.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB cluster (in month). It is valid when pay_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>renewal<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `AutoRenewal`, `Normal`, `NotRenewal`, Default to `NotRenewal`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>auto_<wbr>renew_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is `PrePaid`. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db_<wbr>cluster_<wbr>category</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cluster category. Value options: `Basic`, `Cluster`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db_<wbr>cluster_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cluster version. Value options: `3.0`, Default to `3.0`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db_<wbr>node_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The db_node_class of cluster node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db_<wbr>node_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The db_node_count of cluster node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db_<wbr>node_<wbr>storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The db_node_storage of cluster node.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description of cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>maintain_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pay_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`. Currently, the resource can not supports change pay type.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB cluster (in month). It is valid when pay_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>renewal_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Valid values are `AutoRenewal`, `Normal`, `NotRenewal`, Default to `NotRenewal`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vswitch_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Cluster Resource

Get an existing Cluster resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/adb/#ClusterState">ClusterState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/adb/#Cluster">Cluster</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>auto_renew_period=None<span class="p">, </span>db_cluster_category=None<span class="p">, </span>db_cluster_version=None<span class="p">, </span>db_node_class=None<span class="p">, </span>db_node_count=None<span class="p">, </span>db_node_storage=None<span class="p">, </span>description=None<span class="p">, </span>maintain_time=None<span class="p">, </span>pay_type=None<span class="p">, </span>period=None<span class="p">, </span>renewal_status=None<span class="p">, </span>security_ips=None<span class="p">, </span>tags=None<span class="p">, </span>vswitch_id=None<span class="p">, </span>zone_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/adb?tab=doc#ClusterState">ClusterState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/adb?tab=doc#Cluster">Cluster</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Adb.Cluster.html">Cluster</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Adb.ClusterState.html">ClusterState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is `PrePaid`. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Cluster<wbr>Category</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cluster category. Value options: `Basic`, `Cluster`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cluster version. Value options: `3.0`, Default to `3.0`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Node<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The db_node_class of cluster node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The db_node_count of cluster node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Node<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The db_node_storage of cluster node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`. Currently, the resource can not supports change pay type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB cluster (in month). It is valid when pay_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renewal<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `AutoRenewal`, `Normal`, `NotRenewal`, Default to `NotRenewal`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is `PrePaid`. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Cluster<wbr>Category</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Cluster category. Value options: `Basic`, `Cluster`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Cluster version. Value options: `3.0`, Default to `3.0`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Node<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The db_node_class of cluster node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The db_node_count of cluster node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Node<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The db_node_storage of cluster node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The description of cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`. Currently, the resource can not supports change pay type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB cluster (in month). It is valid when pay_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Renewal<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Valid values are `AutoRenewal`, `Normal`, `NotRenewal`, Default to `NotRenewal`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is `PrePaid`. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>db<wbr>Cluster<wbr>Category</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cluster category. Value options: `Basic`, `Cluster`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>db<wbr>Cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cluster version. Value options: `3.0`, Default to `3.0`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>db<wbr>Node<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The db_node_class of cluster node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>db<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The db_node_count of cluster node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>db<wbr>Node<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The db_node_storage of cluster node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`. Currently, the resource can not supports change pay type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB cluster (in month). It is valid when pay_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renewal<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `AutoRenewal`, `Normal`, `NotRenewal`, Default to `NotRenewal`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto_<wbr>renew_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an cluster, in the unit of the month. It is valid when pay_type is `PrePaid`. Valid value:1, 2, 3, 6, 12, 24, 36, Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>db_<wbr>cluster_<wbr>category</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cluster category. Value options: `Basic`, `Cluster`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>db_<wbr>cluster_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cluster version. Value options: `3.0`, Default to `3.0`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>db_<wbr>node_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The db_node_class of cluster node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>db_<wbr>node_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The db_node_count of cluster node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>db_<wbr>node_<wbr>storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The db_node_storage of cluster node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description of cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintain_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pay_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`, Default to `PostPaid`. Currently, the resource can not supports change pay type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB cluster (in month). It is valid when pay_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>renewal_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Valid values are `AutoRenewal`, `Normal`, `NotRenewal`, Default to `NotRenewal`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an cluster. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vswitch_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB cluster.
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

