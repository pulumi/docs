
---
title: "MultiClusterApp"
block_external_search_index: true
---






## Create a MultiClusterApp Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/rancher2/#MultiClusterApp">MultiClusterApp</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/rancher2/#MultiClusterAppArgs">MultiClusterAppArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">MultiClusterApp</span><span class="p">(resource_name, opts=None, </span>annotations=None<span class="p">, </span>answers=None<span class="p">, </span>catalog_name=None<span class="p">, </span>labels=None<span class="p">, </span>members=None<span class="p">, </span>name=None<span class="p">, </span>revision_history_limit=None<span class="p">, </span>revision_id=None<span class="p">, </span>roles=None<span class="p">, </span>targets=None<span class="p">, </span>template_name=None<span class="p">, </span>template_version=None<span class="p">, </span>upgrade_strategy=None<span class="p">, </span>wait=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewMultiClusterApp<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#MultiClusterAppArgs">MultiClusterAppArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#MultiClusterApp">MultiClusterApp</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Rancher2/Pulumi.Rancher2..MultiClusterApp.html">MultiClusterApp</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Rancher2/Pulumi.Rancher2.MultiClusterAppArgs.html">MultiClusterAppArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Annotations for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Answers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappanswer">List&lt;Multi<wbr>Cluster<wbr>App<wbr>Answer<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Catalog<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app catalog name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Labels for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappmember">List&lt;Multi<wbr>Cluster<wbr>App<wbr>Member<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Revision<wbr>History<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app revision history limit. Default `10` (int)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Revision<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Current revision id for the multi cluster app (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The multi cluster app roles (list)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Targets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterapptarget">List&lt;Multi<wbr>Cluster<wbr>App<wbr>Target<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app target projects (list)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Template<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Template<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template version. Default: `latest` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Upgrade<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappupgradestrategy">Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app upgrade strategy (list MaxItems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Wait until the multi cluster app is active. Default `true` (bool)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Annotations for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Answers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappanswer">[]Multi<wbr>Cluster<wbr>App<wbr>Answer</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Catalog<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app catalog name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Labels for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappmember">[]Multi<wbr>Cluster<wbr>App<wbr>Member</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Revision<wbr>History<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The multi cluster app revision history limit. Default `10` (int)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Revision<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Current revision id for the multi cluster app (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app roles (list)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Targets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterapptarget">[]Multi<wbr>Cluster<wbr>App<wbr>Target</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app target projects (list)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Template<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Template<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template version. Default: `latest` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Upgrade<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappupgradestrategy">*Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app upgrade strategy (list MaxItems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Wait until the multi cluster app is active. Default `true` (bool)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Annotations for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>answers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappanswer">Multi<wbr>Cluster<wbr>App<wbr>Answer[]?</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>catalog<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app catalog name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Labels for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappmember">Multi<wbr>Cluster<wbr>App<wbr>Member[]?</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>revision<wbr>History<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app revision history limit. Default `10` (int)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>revision<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Current revision id for the multi cluster app (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The multi cluster app roles (list)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>targets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterapptarget">Multi<wbr>Cluster<wbr>App<wbr>Target[]</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app target projects (list)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>template<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>template<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template version. Default: `latest` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>upgrade<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappupgradestrategy">Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy?</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app upgrade strategy (list MaxItems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Wait until the multi cluster app is active. Default `true` (bool)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Annotations for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>answers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappanswer">List[Multi<wbr>Cluster<wbr>App<wbr>Answer]</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>catalog_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The multi cluster app catalog name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Labels for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappmember">List[Multi<wbr>Cluster<wbr>App<wbr>Member]</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The multi cluster app name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>revision_<wbr>history_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The multi cluster app revision history limit. Default `10` (int)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>revision_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Current revision id for the multi cluster app (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The multi cluster app roles (list)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>targets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterapptarget">List[Multi<wbr>Cluster<wbr>App<wbr>Target]</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app target projects (list)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>template_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>template_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template version. Default: `latest` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>upgrade_<wbr>strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappupgradestrategy">Dict[Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy]</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app upgrade strategy (list MaxItems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Wait until the multi cluster app is active. Default `true` (bool)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## MultiClusterApp Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object></span>
    </dt>
    <dd>{{% md %}}Annotations for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Answers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappanswer">List&lt;Multi<wbr>Cluster<wbr>App<wbr>Answer&gt;</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Catalog<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app catalog name (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object></span>
    </dt>
    <dd>{{% md %}}Labels for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappmember">List&lt;Multi<wbr>Cluster<wbr>App<wbr>Member&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app name (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Revision<wbr>History<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app revision history limit. Default `10` (int)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Revision<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Current revision id for the multi cluster app (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The multi cluster app roles (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Targets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterapptarget">List&lt;Multi<wbr>Cluster<wbr>App<wbr>Target&gt;</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app target projects (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Template<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template name (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Template<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template version. Default: `latest` (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Template<wbr>Version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The multi cluster app template version ID (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Upgrade<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappupgradestrategy">Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app upgrade strategy (list MaxItems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Wait</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Wait until the multi cluster app is active. Default `true` (bool)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Annotations for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Answers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappanswer">[]Multi<wbr>Cluster<wbr>App<wbr>Answer</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Catalog<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app catalog name (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Labels for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappmember">[]Multi<wbr>Cluster<wbr>App<wbr>Member</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app name (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Revision<wbr>History<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The multi cluster app revision history limit. Default `10` (int)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Revision<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Current revision id for the multi cluster app (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app roles (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Targets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterapptarget">[]Multi<wbr>Cluster<wbr>App<wbr>Target</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app target projects (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Template<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template name (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Template<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template version. Default: `latest` (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Template<wbr>Version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The multi cluster app template version ID (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Upgrade<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappupgradestrategy">Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app upgrade strategy (list MaxItems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Wait</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Wait until the multi cluster app is active. Default `true` (bool)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}Annotations for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>answers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappanswer">Multi<wbr>Cluster<wbr>App<wbr>Answer[]</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>catalog<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app catalog name (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}Labels for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappmember">Multi<wbr>Cluster<wbr>App<wbr>Member[]?</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app name (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>revision<wbr>History<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app revision history limit. Default `10` (int)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>revision<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Current revision id for the multi cluster app (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The multi cluster app roles (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>targets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterapptarget">Multi<wbr>Cluster<wbr>App<wbr>Target[]</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app target projects (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>template<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template name (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>template<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template version. Default: `latest` (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>template<wbr>Version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The multi cluster app template version ID (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>upgrade<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappupgradestrategy">Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app upgrade strategy (list MaxItems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>wait</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Wait until the multi cluster app is active. Default `true` (bool)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Annotations for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>answers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappanswer">List[Multi<wbr>Cluster<wbr>App<wbr>Answer]</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>catalog_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The multi cluster app catalog name (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Labels for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappmember">List[Multi<wbr>Cluster<wbr>App<wbr>Member]</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The multi cluster app name (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>revision_<wbr>history_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The multi cluster app revision history limit. Default `10` (int)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>revision_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Current revision id for the multi cluster app (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The multi cluster app roles (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>targets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterapptarget">List[Multi<wbr>Cluster<wbr>App<wbr>Target]</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app target projects (list)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>template_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template name (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>template_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template version. Default: `latest` (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>template_<wbr>version_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(Computed) The multi cluster app template version ID (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>upgrade_<wbr>strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappupgradestrategy">Dict[Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy]</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app upgrade strategy (list MaxItems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>wait</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Wait until the multi cluster app is active. Default `true` (bool)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing MultiClusterApp Resource

Get an existing MultiClusterApp resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/rancher2/#MultiClusterAppState">MultiClusterAppState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/rancher2/#MultiClusterApp">MultiClusterApp</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>annotations=None<span class="p">, </span>answers=None<span class="p">, </span>catalog_name=None<span class="p">, </span>labels=None<span class="p">, </span>members=None<span class="p">, </span>name=None<span class="p">, </span>revision_history_limit=None<span class="p">, </span>revision_id=None<span class="p">, </span>roles=None<span class="p">, </span>targets=None<span class="p">, </span>template_name=None<span class="p">, </span>template_version=None<span class="p">, </span>template_version_id=None<span class="p">, </span>upgrade_strategy=None<span class="p">, </span>wait=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetMultiClusterApp<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#MultiClusterAppState">MultiClusterAppState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#MultiClusterApp">MultiClusterApp</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Rancher2/Pulumi.Rancher2..MultiClusterApp.html">MultiClusterApp</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Rancher2/Pulumi.Rancher2..MultiClusterAppState.html">MultiClusterAppState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Annotations for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Answers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappanswer">List&lt;Multi<wbr>Cluster<wbr>App<wbr>Answer<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Catalog<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app catalog name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Labels for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappmember">List&lt;Multi<wbr>Cluster<wbr>App<wbr>Member<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Revision<wbr>History<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app revision history limit. Default `10` (int)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Revision<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Current revision id for the multi cluster app (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app roles (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Targets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterapptarget">List&lt;Multi<wbr>Cluster<wbr>App<wbr>Target<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app target projects (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Template<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Template<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template version. Default: `latest` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Template<wbr>Version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(Computed) The multi cluster app template version ID (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Upgrade<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappupgradestrategy">Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app upgrade strategy (list MaxItems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Wait until the multi cluster app is active. Default `true` (bool)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Annotations for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Answers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappanswer">[]Multi<wbr>Cluster<wbr>App<wbr>Answer</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Catalog<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app catalog name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Labels for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappmember">[]Multi<wbr>Cluster<wbr>App<wbr>Member</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Revision<wbr>History<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The multi cluster app revision history limit. Default `10` (int)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Revision<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Current revision id for the multi cluster app (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app roles (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Targets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterapptarget">[]Multi<wbr>Cluster<wbr>App<wbr>Target</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app target projects (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Template<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Template<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template version. Default: `latest` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Template<wbr>Version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}(Computed) The multi cluster app template version ID (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Upgrade<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappupgradestrategy">*Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app upgrade strategy (list MaxItems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Wait until the multi cluster app is active. Default `true` (bool)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Annotations for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>answers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappanswer">Multi<wbr>Cluster<wbr>App<wbr>Answer[]?</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>catalog<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app catalog name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Labels for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappmember">Multi<wbr>Cluster<wbr>App<wbr>Member[]?</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>revision<wbr>History<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app revision history limit. Default `10` (int)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>revision<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Current revision id for the multi cluster app (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app roles (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>targets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterapptarget">Multi<wbr>Cluster<wbr>App<wbr>Target[]?</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app target projects (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>template<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>template<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template version. Default: `latest` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>template<wbr>Version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(Computed) The multi cluster app template version ID (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>upgrade<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappupgradestrategy">Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy?</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app upgrade strategy (list MaxItems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Wait until the multi cluster app is active. Default `true` (bool)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Annotations for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>answers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappanswer">List[Multi<wbr>Cluster<wbr>App<wbr>Answer]</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>catalog_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The multi cluster app catalog name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Labels for multi cluster app object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>members</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappmember">List[Multi<wbr>Cluster<wbr>App<wbr>Member]</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app answers (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The multi cluster app name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>revision_<wbr>history_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The multi cluster app revision history limit. Default `10` (int)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>revision_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Current revision id for the multi cluster app (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The multi cluster app roles (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>targets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterapptarget">List[Multi<wbr>Cluster<wbr>App<wbr>Target]</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app target projects (list)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>template_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template name (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>template_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The multi cluster app template version. Default: `latest` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>template_<wbr>version_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(Computed) The multi cluster app template version ID (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>upgrade_<wbr>strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappupgradestrategy">Dict[Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy]</a></span>
    </dt>
    <dd>{{% md %}}The multi cluster app upgrade strategy (list MaxItems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Wait until the multi cluster app is active. Default `true` (bool)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Multi<wbr>Cluster<wbr>App<wbr>Answer</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/input/#MultiClusterAppAnswer">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/output/#MultiClusterAppAnswer">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#MultiClusterAppAnswerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#MultiClusterAppAnswerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cluster ID for answer (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Project ID for target (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Key/values for answer (map)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Cluster ID for answer (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Project ID for target (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Key/values for answer (map)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cluster ID for answer (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Project ID for target (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Key/values for answer (map)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cluster_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cluster ID for answer (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Project ID for target (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Key/values for answer (map)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Multi<wbr>Cluster<wbr>App<wbr>Member</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/input/#MultiClusterAppMember">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/output/#MultiClusterAppMember">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#MultiClusterAppMemberArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#MultiClusterAppMemberOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Access<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Member access type. Valid values: `["member" | "owner" | "read-only"]` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>Principal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Member group principal id (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Principal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Member user principal id (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Access<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Member access type. Valid values: `["member" | "owner" | "read-only"]` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>Principal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Member group principal id (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Principal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Member user principal id (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Member access type. Valid values: `["member" | "owner" | "read-only"]` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group<wbr>Principal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Member group principal id (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user<wbr>Principal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Member user principal id (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Member access type. Valid values: `["member" | "owner" | "read-only"]` (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group_<wbr>principal_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Member group principal id (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user_<wbr>principal_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Member user principal id (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Multi<wbr>Cluster<wbr>App<wbr>Target</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/input/#MultiClusterAppTarget">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/output/#MultiClusterAppTarget">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#MultiClusterAppTargetArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#MultiClusterAppTargetOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}App ID for target (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}App health state for target (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Project ID for target (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}App state for target (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}App ID for target (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}App health state for target (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Project ID for target (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}App state for target (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}App ID for target (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}App health state for target (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Project ID for target (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}App state for target (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}App ID for target (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}App health state for target (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>project_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Project ID for target (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}App state for target (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/input/#MultiClusterAppUpgradeStrategy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/output/#MultiClusterAppUpgradeStrategy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#MultiClusterAppUpgradeStrategyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#MultiClusterAppUpgradeStrategyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Rolling<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappupgradestrategyrollingupdate">Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy<wbr>Rolling<wbr>Update<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Upgrade strategy rolling update (list MaxItems:1)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Rolling<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappupgradestrategyrollingupdate">*Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy<wbr>Rolling<wbr>Update</a></span>
    </dt>
    <dd>{{% md %}}Upgrade strategy rolling update (list MaxItems:1)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>rolling<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappupgradestrategyrollingupdate">Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy<wbr>Rolling<wbr>Update?</a></span>
    </dt>
    <dd>{{% md %}}Upgrade strategy rolling update (list MaxItems:1)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>rolling<wbr>Update</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#multiclusterappupgradestrategyrollingupdate">Dict[Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy<wbr>Rolling<wbr>Update]</a></span>
    </dt>
    <dd>{{% md %}}Upgrade strategy rolling update (list MaxItems:1)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Multi<wbr>Cluster<wbr>App<wbr>Upgrade<wbr>Strategy<wbr>Rolling<wbr>Update</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/input/#MultiClusterAppUpgradeStrategyRollingUpdate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/output/#MultiClusterAppUpgradeStrategyRollingUpdate">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#MultiClusterAppUpgradeStrategyRollingUpdateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#MultiClusterAppUpgradeStrategyRollingUpdateOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Batch<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Rolling update batch size. Default `1` (int)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Rolling update interval. Default `1` (int)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Batch<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Rolling update batch size. Default `1` (int)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Rolling update interval. Default `1` (int)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>batch<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Rolling update batch size. Default `1` (int)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Rolling update interval. Default `1` (int)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>batch<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Rolling update batch size. Default `1` (int)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Rolling update interval. Default `1` (int)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-rancher2">https://github.com/pulumi/pulumi-rancher2</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

