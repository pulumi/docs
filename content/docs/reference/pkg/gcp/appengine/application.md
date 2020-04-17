
---
title: "Application"
block_external_search_index: true
---



Allows creation and management of an App Engine application.

> App Engine applications cannot be deleted once they're created; you have to delete the
   entire project to delete the application. This provider will report the application has been
   successfully deleted; this is a limitation of the provider, and will go away in the future.
   This provider is not able to delete App Engine applications.

{{% examples %}}
{{% /examples %}}



## Create a Application Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/appengine/#Application">Application</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/appengine/#ApplicationArgs">ApplicationArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Application</span><span class="p">(resource_name, opts=None, </span>auth_domain=None<span class="p">, </span>feature_settings=None<span class="p">, </span>iap=None<span class="p">, </span>location_id=None<span class="p">, </span>project=None<span class="p">, </span>serving_status=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewApplication<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/appengine?tab=doc#ApplicationArgs">ApplicationArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/appengine?tab=doc#Application">Application</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.AppEngine.Application.html">Application</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.AppEngine.ApplicationArgs.html">ApplicationArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The [location](https://cloud.google.com/appengine/docs/locations)
to serve the app from.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The domain to authenticate users with when using App Engine's User API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Feature<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationfeaturesettings">Application<wbr>Feature<wbr>Settings<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A block of optional settings to configure specific App Engine features:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationiap">Application<wbr>Iap<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The project ID to create the application under.
~>**NOTE**: GCP only accepts project ID, not project number. If you are using number,
you may get a "Permission denied" error.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Serving<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The serving status of the app.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The [location](https://cloud.google.com/appengine/docs/locations)
to serve the app from.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The domain to authenticate users with when using App Engine's User API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Feature<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationfeaturesettings">Application<wbr>Feature<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}A block of optional settings to configure specific App Engine features:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationiap">Application<wbr>Iap</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The project ID to create the application under.
~>**NOTE**: GCP only accepts project ID, not project number. If you are using number,
you may get a "Permission denied" error.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Serving<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The serving status of the app.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The [location](https://cloud.google.com/appengine/docs/locations)
to serve the app from.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auth<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The domain to authenticate users with when using App Engine's User API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>feature<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationfeaturesettings">Application<wbr>Feature<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}A block of optional settings to configure specific App Engine features:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationiap">Application<wbr>Iap</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The project ID to create the application under.
~>**NOTE**: GCP only accepts project ID, not project number. If you are using number,
you may get a "Permission denied" error.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>serving<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The serving status of the app.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>location_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The [location](https://cloud.google.com/appengine/docs/locations)
to serve the app from.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auth_<wbr>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The domain to authenticate users with when using App Engine's User API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>feature_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationfeaturesettings">Dict[Application<wbr>Feature<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}A block of optional settings to configure specific App Engine features:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationiap">Dict[Application<wbr>Iap]</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The project ID to create the application under.
~>**NOTE**: GCP only accepts project ID, not project number. If you are using number,
you may get a "Permission denied" error.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>serving_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The serving status of the app.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Application Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Identifier of the app, usually `{PROJECT_ID}`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Code<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The GCS bucket code is being stored in for this app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The GCS bucket content is being stored in for this app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The default hostname for this app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Gcr<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The GCR domain used for storing managed Docker images for this app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Unique name of the app, usually `apps/{PROJECT_ID}`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Url<wbr>Dispatch<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationurldispatchrule">List&lt;Application<wbr>Url<wbr>Dispatch<wbr>Rule&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of dispatch rule blocks. Each block has a `domain`, `path`, and `service` field.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifier of the app, usually `{PROJECT_ID}`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Code<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The GCS bucket code is being stored in for this app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The GCS bucket content is being stored in for this app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The default hostname for this app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Gcr<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The GCR domain used for storing managed Docker images for this app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Unique name of the app, usually `apps/{PROJECT_ID}`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Url<wbr>Dispatch<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationurldispatchrule">[]Application<wbr>Url<wbr>Dispatch<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A list of dispatch rule blocks. Each block has a `domain`, `path`, and `service` field.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>app<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifier of the app, usually `{PROJECT_ID}`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>code<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The GCS bucket code is being stored in for this app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The GCS bucket content is being stored in for this app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The default hostname for this app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>gcr<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The GCR domain used for storing managed Docker images for this app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Unique name of the app, usually `apps/{PROJECT_ID}`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>url<wbr>Dispatch<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationurldispatchrule">Application<wbr>Url<wbr>Dispatch<wbr>Rule[]</a></span>
    </dt>
    <dd>{{% md %}}A list of dispatch rule blocks. Each block has a `domain`, `path`, and `service` field.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>app_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Identifier of the app, usually `{PROJECT_ID}`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>code_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The GCS bucket code is being stored in for this app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The GCS bucket content is being stored in for this app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default_<wbr>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The default hostname for this app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>gcr_<wbr>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The GCR domain used for storing managed Docker images for this app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Unique name of the app, usually `apps/{PROJECT_ID}`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>url_<wbr>dispatch_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationurldispatchrule">List[Application<wbr>Url<wbr>Dispatch<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A list of dispatch rule blocks. Each block has a `domain`, `path`, and `service` field.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Application Resource

Get an existing Application resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/appengine/#ApplicationState">ApplicationState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/appengine/#Application">Application</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>app_id=None<span class="p">, </span>auth_domain=None<span class="p">, </span>code_bucket=None<span class="p">, </span>default_bucket=None<span class="p">, </span>default_hostname=None<span class="p">, </span>feature_settings=None<span class="p">, </span>gcr_domain=None<span class="p">, </span>iap=None<span class="p">, </span>location_id=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, </span>serving_status=None<span class="p">, </span>url_dispatch_rules=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetApplication<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/appengine?tab=doc#ApplicationState">ApplicationState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/appengine?tab=doc#Application">Application</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.AppEngine.Application.html">Application</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.AppEngine.ApplicationState.html">ApplicationState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Identifier of the app, usually `{PROJECT_ID}`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The domain to authenticate users with when using App Engine's User API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Code<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The GCS bucket code is being stored in for this app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The GCS bucket content is being stored in for this app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The default hostname for this app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Feature<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationfeaturesettings">Application<wbr>Feature<wbr>Settings<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A block of optional settings to configure specific App Engine features:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gcr<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The GCR domain used for storing managed Docker images for this app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationiap">Application<wbr>Iap<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The [location](https://cloud.google.com/appengine/docs/locations)
to serve the app from.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Unique name of the app, usually `apps/{PROJECT_ID}`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The project ID to create the application under.
~>**NOTE**: GCP only accepts project ID, not project number. If you are using number,
you may get a "Permission denied" error.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Serving<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The serving status of the app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url<wbr>Dispatch<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationurldispatchrule">List&lt;Application<wbr>Url<wbr>Dispatch<wbr>Rule<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of dispatch rule blocks. Each block has a `domain`, `path`, and `service` field.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifier of the app, usually `{PROJECT_ID}`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The domain to authenticate users with when using App Engine's User API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Code<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The GCS bucket code is being stored in for this app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The GCS bucket content is being stored in for this app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The default hostname for this app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Feature<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationfeaturesettings">Application<wbr>Feature<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}A block of optional settings to configure specific App Engine features:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gcr<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The GCR domain used for storing managed Docker images for this app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationiap">Application<wbr>Iap</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The [location](https://cloud.google.com/appengine/docs/locations)
to serve the app from.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Unique name of the app, usually `apps/{PROJECT_ID}`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The project ID to create the application under.
~>**NOTE**: GCP only accepts project ID, not project number. If you are using number,
you may get a "Permission denied" error.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Serving<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The serving status of the app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url<wbr>Dispatch<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationurldispatchrule">[]Application<wbr>Url<wbr>Dispatch<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A list of dispatch rule blocks. Each block has a `domain`, `path`, and `service` field.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifier of the app, usually `{PROJECT_ID}`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auth<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The domain to authenticate users with when using App Engine's User API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>code<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The GCS bucket code is being stored in for this app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The GCS bucket content is being stored in for this app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The default hostname for this app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>feature<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationfeaturesettings">Application<wbr>Feature<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}A block of optional settings to configure specific App Engine features:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gcr<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The GCR domain used for storing managed Docker images for this app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationiap">Application<wbr>Iap</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The [location](https://cloud.google.com/appengine/docs/locations)
to serve the app from.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Unique name of the app, usually `apps/{PROJECT_ID}`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The project ID to create the application under.
~>**NOTE**: GCP only accepts project ID, not project number. If you are using number,
you may get a "Permission denied" error.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>serving<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The serving status of the app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url<wbr>Dispatch<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationurldispatchrule">Application<wbr>Url<wbr>Dispatch<wbr>Rule[]</a></span>
    </dt>
    <dd>{{% md %}}A list of dispatch rule blocks. Each block has a `domain`, `path`, and `service` field.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>app_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Identifier of the app, usually `{PROJECT_ID}`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auth_<wbr>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The domain to authenticate users with when using App Engine's User API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>code_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The GCS bucket code is being stored in for this app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The GCS bucket content is being stored in for this app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The default hostname for this app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>feature_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationfeaturesettings">Dict[Application<wbr>Feature<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}A block of optional settings to configure specific App Engine features:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gcr_<wbr>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The GCR domain used for storing managed Docker images for this app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iap</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationiap">Dict[Application<wbr>Iap]</a></span>
    </dt>
    <dd>{{% md %}}Settings for enabling Cloud Identity Aware Proxy
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The [location](https://cloud.google.com/appengine/docs/locations)
to serve the app from.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Unique name of the app, usually `apps/{PROJECT_ID}`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The project ID to create the application under.
~>**NOTE**: GCP only accepts project ID, not project number. If you are using number,
you may get a "Permission denied" error.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>serving_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The serving status of the app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url_<wbr>dispatch_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#applicationurldispatchrule">List[Application<wbr>Url<wbr>Dispatch<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A list of dispatch rule blocks. Each block has a `domain`, `path`, and `service` field.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Application<wbr>Feature<wbr>Settings</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ApplicationFeatureSettings">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ApplicationFeatureSettings">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/appengine?tab=doc#ApplicationFeatureSettingsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/appengine?tab=doc#ApplicationFeatureSettingsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Split<wbr>Health<wbr>Checks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Set to false to use the legacy health check instead of the readiness
and liveness checks.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Split<wbr>Health<wbr>Checks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Set to false to use the legacy health check instead of the readiness
and liveness checks.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>split<wbr>Health<wbr>Checks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Set to false to use the legacy health check instead of the readiness
and liveness checks.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>split<wbr>Health<wbr>Checks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Set to false to use the legacy health check instead of the readiness
and liveness checks.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Application<wbr>Iap</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ApplicationIap">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ApplicationIap">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/appengine?tab=doc#ApplicationIapArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/appengine?tab=doc#ApplicationIapOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Oauth2Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Oauth2Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth2Client<wbr>Secret<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Oauth2Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Oauth2Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth2Client<wbr>Secret<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>oauth2Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>oauth2Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth2Client<wbr>Secret<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>oauth2Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>oauth2Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth2Client<wbr>Secret<wbr>Sha256</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Application<wbr>Url<wbr>Dispatch<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ApplicationUrlDispatchRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/appengine?tab=doc#ApplicationUrlDispatchRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
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
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`google-beta` Terraform Provider](https://github.com/terraform-providers/terraform-provider-google-beta).</dd>
</dl>

