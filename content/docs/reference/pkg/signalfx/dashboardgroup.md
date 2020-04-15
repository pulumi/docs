
---
title: "DashboardGroup"
block_external_search_index: true
---



In the SignalFx web UI, a [dashboard group](https://developers.signalfx.com/dashboard_groups_reference.html) is a collection of dashboards.

> **NOTE** Dashboard groups cannot be accessed directly, but just via a dashboard contained in them. This is the reason why make show won't show any of yours dashboard groups.

> This content is derived from https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/dashboard_group.html.markdown.



## Create a DashboardGroup Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#DashboardGroup">DashboardGroup</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#DashboardGroupArgs">DashboardGroupArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">DashboardGroup</span><span class="p">(resource_name, opts=None, </span>authorized_writer_teams=None<span class="p">, </span>authorized_writer_users=None<span class="p">, </span>dashboards=None<span class="p">, </span>description=None<span class="p">, </span>import_qualifiers=None<span class="p">, </span>name=None<span class="p">, </span>teams=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDashboardGroup<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DashboardGroupArgs">DashboardGroupArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DashboardGroup">DashboardGroup</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx.DashboardGroup.html">DashboardGroup</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.SignalFx.DashboardGroupArgs.html">DashboardGroupArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Authorized<wbr>Writer<wbr>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}Team IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's team (or user id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Writer<wbr>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}User IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupdashboard">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Dashboard<wbr>Group<wbr>Dashboard<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}[Mirrored dashboards](https://docs.signalfx.com/en/latest/dashboards/dashboard-mirrors.html) in this dashboard group. **Note:** This feature is not present in all accounts. Please contact support if you are unsure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the dashboard group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Import<wbr>Qualifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupimportqualifier">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Dashboard<wbr>Group<wbr>Import<wbr>Qualifier<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the dashboard group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}Team IDs to associate the dashboard group to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Writer<wbr>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Team IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's team (or user id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Writer<wbr>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}User IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupdashboard">[]Dashboard<wbr>Group<wbr>Dashboard</a></span>
    </dt>
    <dd>{{% md %}}[Mirrored dashboards](https://docs.signalfx.com/en/latest/dashboards/dashboard-mirrors.html) in this dashboard group. **Note:** This feature is not present in all accounts. Please contact support if you are unsure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the dashboard group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Import<wbr>Qualifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupimportqualifier">[]Dashboard<wbr>Group<wbr>Import<wbr>Qualifier</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the dashboard group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Team IDs to associate the dashboard group to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>authorized<wbr>Writer<wbr>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Team IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's team (or user id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authorized<wbr>Writer<wbr>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}User IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupdashboard">Dashboard<wbr>Group<wbr>Dashboard[]</a></span>
    </dt>
    <dd>{{% md %}}[Mirrored dashboards](https://docs.signalfx.com/en/latest/dashboards/dashboard-mirrors.html) in this dashboard group. **Note:** This feature is not present in all accounts. Please contact support if you are unsure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the dashboard group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>import<wbr>Qualifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupimportqualifier">Dashboard<wbr>Group<wbr>Import<wbr>Qualifier[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the dashboard group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Team IDs to associate the dashboard group to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>authorized_<wbr>writer_<wbr>teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Team IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's team (or user id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authorized_<wbr>writer_<wbr>users</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}User IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupdashboard">List[Dashboard<wbr>Group<wbr>Dashboard]</a></span>
    </dt>
    <dd>{{% md %}}[Mirrored dashboards](https://docs.signalfx.com/en/latest/dashboards/dashboard-mirrors.html) in this dashboard group. **Note:** This feature is not present in all accounts. Please contact support if you are unsure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the dashboard group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>import_<wbr>qualifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupimportqualifier">List[Dashboard<wbr>Group<wbr>Import<wbr>Qualifier]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the dashboard group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Team IDs to associate the dashboard group to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Look up an Existing DashboardGroup Resource

Get an existing DashboardGroup resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#DashboardGroupState">DashboardGroupState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#DashboardGroup">DashboardGroup</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>authorized_writer_teams=None<span class="p">, </span>authorized_writer_users=None<span class="p">, </span>dashboards=None<span class="p">, </span>description=None<span class="p">, </span>import_qualifiers=None<span class="p">, </span>name=None<span class="p">, </span>teams=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetDashboardGroup<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DashboardGroupState">DashboardGroupState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DashboardGroup">DashboardGroup</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx.DashboardGroup.html">DashboardGroup</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx..DashboardGroupState.html">DashboardGroupState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Authorized<wbr>Writer<wbr>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}Team IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's team (or user id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Writer<wbr>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}User IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupdashboard">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Dashboard<wbr>Group<wbr>Dashboard<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}[Mirrored dashboards](https://docs.signalfx.com/en/latest/dashboards/dashboard-mirrors.html) in this dashboard group. **Note:** This feature is not present in all accounts. Please contact support if you are unsure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the dashboard group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Import<wbr>Qualifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupimportqualifier">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Dashboard<wbr>Group<wbr>Import<wbr>Qualifier<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the dashboard group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}Team IDs to associate the dashboard group to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Writer<wbr>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Team IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's team (or user id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Writer<wbr>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}User IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupdashboard">[]Dashboard<wbr>Group<wbr>Dashboard</a></span>
    </dt>
    <dd>{{% md %}}[Mirrored dashboards](https://docs.signalfx.com/en/latest/dashboards/dashboard-mirrors.html) in this dashboard group. **Note:** This feature is not present in all accounts. Please contact support if you are unsure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the dashboard group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Import<wbr>Qualifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupimportqualifier">[]Dashboard<wbr>Group<wbr>Import<wbr>Qualifier</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the dashboard group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Team IDs to associate the dashboard group to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>authorized<wbr>Writer<wbr>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Team IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's team (or user id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authorized<wbr>Writer<wbr>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}User IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupdashboard">Dashboard<wbr>Group<wbr>Dashboard[]</a></span>
    </dt>
    <dd>{{% md %}}[Mirrored dashboards](https://docs.signalfx.com/en/latest/dashboards/dashboard-mirrors.html) in this dashboard group. **Note:** This feature is not present in all accounts. Please contact support if you are unsure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the dashboard group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>import<wbr>Qualifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupimportqualifier">Dashboard<wbr>Group<wbr>Import<wbr>Qualifier[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the dashboard group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Team IDs to associate the dashboard group to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>authorized_<wbr>writer_<wbr>teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Team IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's team (or user id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authorized_<wbr>writer_<wbr>users</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}User IDs that have write access to this dashboard group. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupdashboard">List[Dashboard<wbr>Group<wbr>Dashboard]</a></span>
    </dt>
    <dd>{{% md %}}[Mirrored dashboards](https://docs.signalfx.com/en/latest/dashboards/dashboard-mirrors.html) in this dashboard group. **Note:** This feature is not present in all accounts. Please contact support if you are unsure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the dashboard group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>import_<wbr>qualifiers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupimportqualifier">List[Dashboard<wbr>Group<wbr>Import<wbr>Qualifier]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the dashboard group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Team IDs to associate the dashboard group to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Dashboard<wbr>Group<wbr>Dashboard</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#DashboardGroupDashboard">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#DashboardGroupDashboard">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DashboardGroupDashboardArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DashboardGroupDashboardOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dashboard<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The dashboard id to mirror
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description<wbr>Override</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description that will override the original dashboards's description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter<wbr>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupdashboardfilteroverride">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Dashboard<wbr>Group<wbr>Dashboard<wbr>Filter<wbr>Override<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The description that will override the original dashboards's description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Override</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name that will override the original dashboards's name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Variable<wbr>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupdashboardvariableoverride">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Dashboard<wbr>Group<wbr>Dashboard<wbr>Variable<wbr>Override<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dashboard<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The dashboard id to mirror
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description<wbr>Override</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description that will override the original dashboards's description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter<wbr>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupdashboardfilteroverride">[]Dashboard<wbr>Group<wbr>Dashboard<wbr>Filter<wbr>Override</a></span>
    </dt>
    <dd>{{% md %}}The description that will override the original dashboards's description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Override</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name that will override the original dashboards's name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Variable<wbr>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupdashboardvariableoverride">[]Dashboard<wbr>Group<wbr>Dashboard<wbr>Variable<wbr>Override</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dashboard<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The dashboard id to mirror
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description<wbr>Override</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description that will override the original dashboards's description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter<wbr>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupdashboardfilteroverride">Dashboard<wbr>Group<wbr>Dashboard<wbr>Filter<wbr>Override[]</a></span>
    </dt>
    <dd>{{% md %}}The description that will override the original dashboards's description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name<wbr>Override</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name that will override the original dashboards's name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>variable<wbr>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupdashboardvariableoverride">Dashboard<wbr>Group<wbr>Dashboard<wbr>Variable<wbr>Override[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dashboard<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The dashboard id to mirror
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description<wbr>Override</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description that will override the original dashboards's description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter<wbr>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupdashboardfilteroverride">List[Dashboard<wbr>Group<wbr>Dashboard<wbr>Filter<wbr>Override]</a></span>
    </dt>
    <dd>{{% md %}}The description that will override the original dashboards's description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name<wbr>Override</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name that will override the original dashboards's name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>variable<wbr>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupdashboardvariableoverride">List[Dashboard<wbr>Group<wbr>Dashboard<wbr>Variable<wbr>Override]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Dashboard<wbr>Group<wbr>Dashboard<wbr>Filter<wbr>Override</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#DashboardGroupDashboardFilterOverride">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#DashboardGroupDashboardFilterOverride">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DashboardGroupDashboardFilterOverrideArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DashboardGroupDashboardFilterOverrideOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A metric time series dimension or property name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}(Optional) List of of strings (which will be treated as an OR filter on the property).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Negated</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true,  only data that does not match the specified value of the specified property appear in the event overlay. Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A metric time series dimension or property name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}(Optional) List of of strings (which will be treated as an OR filter on the property).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Negated</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true,  only data that does not match the specified value of the specified property appear in the event overlay. Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A metric time series dimension or property name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}(Optional) List of of strings (which will be treated as an OR filter on the property).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>negated</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If true,  only data that does not match the specified value of the specified property appear in the event overlay. Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>property</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A metric time series dimension or property name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}(Optional) List of of strings (which will be treated as an OR filter on the property).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>negated</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true,  only data that does not match the specified value of the specified property appear in the event overlay. Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Dashboard<wbr>Group<wbr>Dashboard<wbr>Variable<wbr>Override</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#DashboardGroupDashboardVariableOverride">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#DashboardGroupDashboardVariableOverride">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DashboardGroupDashboardVariableOverrideArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DashboardGroupDashboardVariableOverrideOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A metric time series dimension or property name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}(Optional) List of of strings (which will be treated as an OR filter on the property).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values<wbr>Suggesteds</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}A list of strings of suggested values for this variable; these suggestions will receive priority when values are autosuggested for this variable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A metric time series dimension or property name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}(Optional) List of of strings (which will be treated as an OR filter on the property).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values<wbr>Suggesteds</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of strings of suggested values for this variable; these suggestions will receive priority when values are autosuggested for this variable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A metric time series dimension or property name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}(Optional) List of of strings (which will be treated as an OR filter on the property).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values<wbr>Suggesteds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of strings of suggested values for this variable; these suggestions will receive priority when values are autosuggested for this variable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>property</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A metric time series dimension or property name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}(Optional) List of of strings (which will be treated as an OR filter on the property).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values<wbr>Suggesteds</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of strings of suggested values for this variable; these suggestions will receive priority when values are autosuggested for this variable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Dashboard<wbr>Group<wbr>Import<wbr>Qualifier</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#DashboardGroupImportQualifier">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#DashboardGroupImportQualifier">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DashboardGroupImportQualifierArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DashboardGroupImportQualifierOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Metric</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupimportqualifierfilter">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Dashboard<wbr>Group<wbr>Import<wbr>Qualifier<wbr>Filter<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Metric</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupimportqualifierfilter">[]Dashboard<wbr>Group<wbr>Import<wbr>Qualifier<wbr>Filter</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>metric</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupimportqualifierfilter">Dashboard<wbr>Group<wbr>Import<wbr>Qualifier<wbr>Filter[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>metric</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#dashboardgroupimportqualifierfilter">List[Dashboard<wbr>Group<wbr>Import<wbr>Qualifier<wbr>Filter]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Dashboard<wbr>Group<wbr>Import<wbr>Qualifier<wbr>Filter</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#DashboardGroupImportQualifierFilter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#DashboardGroupImportQualifierFilter">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DashboardGroupImportQualifierFilterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DashboardGroupImportQualifierFilterOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A metric time series dimension or property name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}(Optional) List of of strings (which will be treated as an OR filter on the property).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Negated</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true,  only data that does not match the specified value of the specified property appear in the event overlay. Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A metric time series dimension or property name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}(Optional) List of of strings (which will be treated as an OR filter on the property).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Negated</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true,  only data that does not match the specified value of the specified property appear in the event overlay. Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A metric time series dimension or property name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}(Optional) List of of strings (which will be treated as an OR filter on the property).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>negated</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If true,  only data that does not match the specified value of the specified property appear in the event overlay. Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>property</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A metric time series dimension or property name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}(Optional) List of of strings (which will be treated as an OR filter on the property).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>negated</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true,  only data that does not match the specified value of the specified property appear in the event overlay. Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-signalfx">https://github.com/pulumi/pulumi-signalfx</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

