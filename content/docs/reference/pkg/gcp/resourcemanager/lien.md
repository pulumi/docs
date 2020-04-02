
---
title: "Lien"
block_external_search_index: true
---

A Lien represents an encumbrance on the actions that can be performed on a resource.

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/resource_manager_lien.html.markdown.



## Create a Lien Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/resourcemanager/#Lien">Lien</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/resourcemanager/#LienArgs">LienArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Lien</span><span class="p">(resource_name, opts=None, </span>origin=None<span class="p">, </span>parent=None<span class="p">, </span>reason=None<span class="p">, </span>restrictions=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewLien<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/resourcemanager?tab=doc#LienArgs">LienArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/resourcemanager?tab=doc#Lien">Lien</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Resourcemanager.Lien.html">Lien</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.ResourceManager.LienArgs.html">LienArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Origin</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically.
Maximum length of 200 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens
are supported. Since a variety of objects can have Liens against them, you must provide the type prefix (e.g.
"projects/my-project-name").
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200
characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM
permission. The server will validate the permissions against those for which Liens are supported. An empty list is
meaningless and will be rejected. e.g. ['resourcemanager.projects.delete']
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Origin</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically.
Maximum length of 200 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens
are supported. Since a variety of objects can have Liens against them, you must provide the type prefix (e.g.
"projects/my-project-name").
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200
characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM
permission. The server will validate the permissions against those for which Liens are supported. An empty list is
meaningless and will be rejected. e.g. ['resourcemanager.projects.delete']
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>origin</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically.
Maximum length of 200 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens
are supported. Since a variety of objects can have Liens against them, you must provide the type prefix (e.g.
"projects/my-project-name").
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200
characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM
permission. The server will validate the permissions against those for which Liens are supported. An empty list is
meaningless and will be rejected. e.g. ['resourcemanager.projects.delete']
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>origin</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically.
Maximum length of 200 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens
are supported. Since a variety of objects can have Liens against them, you must provide the type prefix (e.g.
"projects/my-project-name").
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200
characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM
permission. The server will validate the permissions against those for which Liens are supported. An empty list is
meaningless and will be rejected. e.g. ['resourcemanager.projects.delete']
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Lien Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Time of creation
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A system-generated unique identifier for this Lien.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Origin</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically.
Maximum length of 200 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens
are supported. Since a variety of objects can have Liens against them, you must provide the type prefix (e.g.
"projects/my-project-name").
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200
characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM
permission. The server will validate the permissions against those for which Liens are supported. An empty list is
meaningless and will be rejected. e.g. ['resourcemanager.projects.delete']
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Time of creation
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A system-generated unique identifier for this Lien.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Origin</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically.
Maximum length of 200 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens
are supported. Since a variety of objects can have Liens against them, you must provide the type prefix (e.g.
"projects/my-project-name").
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200
characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM
permission. The server will validate the permissions against those for which Liens are supported. An empty list is
meaningless and will be rejected. e.g. ['resourcemanager.projects.delete']
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Time of creation
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A system-generated unique identifier for this Lien.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>origin</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically.
Maximum length of 200 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens
are supported. Since a variety of objects can have Liens against them, you must provide the type prefix (e.g.
"projects/my-project-name").
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200
characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM
permission. The server will validate the permissions against those for which Liens are supported. An empty list is
meaningless and will be rejected. e.g. ['resourcemanager.projects.delete']
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>create_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Time of creation
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A system-generated unique identifier for this Lien.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>origin</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically.
Maximum length of 200 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens
are supported. Since a variety of objects can have Liens against them, you must provide the type prefix (e.g.
"projects/my-project-name").
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200
characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM
permission. The server will validate the permissions against those for which Liens are supported. An empty list is
meaningless and will be rejected. e.g. ['resourcemanager.projects.delete']
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Lien Resource

Get an existing Lien resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/resourcemanager/#LienState">LienState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/resourcemanager/#Lien">Lien</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>create_time=None<span class="p">, </span>name=None<span class="p">, </span>origin=None<span class="p">, </span>parent=None<span class="p">, </span>reason=None<span class="p">, </span>restrictions=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetLien<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/resourcemanager?tab=doc#LienState">LienState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/resourcemanager?tab=doc#Lien">Lien</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Resourcemanager.Lien.html">Lien</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Resourcemanager.LienState.html">LienState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time of creation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A system-generated unique identifier for this Lien.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Origin</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically.
Maximum length of 200 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens
are supported. Since a variety of objects can have Liens against them, you must provide the type prefix (e.g.
"projects/my-project-name").
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM
permission. The server will validate the permissions against those for which Liens are supported. An empty list is
meaningless and will be rejected. e.g. ['resourcemanager.projects.delete']
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Time of creation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A system-generated unique identifier for this Lien.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Origin</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically.
Maximum length of 200 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens
are supported. Since a variety of objects can have Liens against them, you must provide the type prefix (e.g.
"projects/my-project-name").
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM
permission. The server will validate the permissions against those for which Liens are supported. An empty list is
meaningless and will be rejected. e.g. ['resourcemanager.projects.delete']
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time of creation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A system-generated unique identifier for this Lien.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>origin</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically.
Maximum length of 200 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens
are supported. Since a variety of objects can have Liens against them, you must provide the type prefix (e.g.
"projects/my-project-name").
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM
permission. The server will validate the permissions against those for which Liens are supported. An empty list is
meaningless and will be rejected. e.g. ['resourcemanager.projects.delete']
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>create_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Time of creation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A system-generated unique identifier for this Lien.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>origin</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically.
Maximum length of 200 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parent</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens
are supported. Since a variety of objects can have Liens against them, you must provide the type prefix (e.g.
"projects/my-project-name").
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM
permission. The server will validate the permissions against those for which Liens are supported. An empty list is
meaningless and will be rejected. e.g. ['resourcemanager.projects.delete']
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
