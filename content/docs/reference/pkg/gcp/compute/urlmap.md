
---
title: "URLMap"
block_external_search_index: true
---

UrlMaps are used to route requests to a backend service based on rules
that you define for the host and path of an incoming URL.


To get more information about UrlMap, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/urlMaps)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_url_map.html.markdown.



## Create a URLMap Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#URLMap">URLMap</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#URLMapArgs">URLMapArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">URLMap</span><span class="p">(resource_name, opts=None, </span>default_service=None<span class="p">, </span>description=None<span class="p">, </span>header_action=None<span class="p">, </span>host_rules=None<span class="p">, </span>name=None<span class="p">, </span>path_matchers=None<span class="p">, </span>project=None<span class="p">, </span>tests=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewURLMap<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapArgs">URLMapArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMap">URLMap</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.URLMap.html">URLMap</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.Inputs.URLMapArgs.html">URLMapArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Default<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The backend service or backend bucket to use when none of the given rules match.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderaction">URLMap<wbr>Header<wbr>Action<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specifies changes to request and response headers that need to take effect for the selected backendService. The
headerAction specified here take effect after headerAction specified under pathMatcher.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaphostrule">List&lt;URLMap<wbr>Host<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The list of HostRules to use against the URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcher">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The list of named PathMatchers to use against the URL.
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
        <span>Tests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaptest">List&lt;URLMap<wbr>Test<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The list of expected URL mapping tests. Request to update this UrlMap will succeed only if all of the test cases pass.
You can specify a maximum of 100 tests per UrlMap.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The backend service or backend bucket to use when none of the given rules match.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderaction">*URLMap<wbr>Header<wbr>Action</a></span>
    </dt>
    <dd>{{% md %}}Specifies changes to request and response headers that need to take effect for the selected backendService. The
headerAction specified here take effect after headerAction specified under pathMatcher.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaphostrule">[]URLMap<wbr>Host<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}The list of HostRules to use against the URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcher">[]URLMap<wbr>Path<wbr>Matcher</a></span>
    </dt>
    <dd>{{% md %}}The list of named PathMatchers to use against the URL.
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
        <span>Tests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaptest">[]URLMap<wbr>Test</a></span>
    </dt>
    <dd>{{% md %}}The list of expected URL mapping tests. Request to update this UrlMap will succeed only if all of the test cases pass.
You can specify a maximum of 100 tests per UrlMap.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The backend service or backend bucket to use when none of the given rules match.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderaction">URLMap<wbr>Header<wbr>Action?</a></span>
    </dt>
    <dd>{{% md %}}Specifies changes to request and response headers that need to take effect for the selected backendService. The
headerAction specified here take effect after headerAction specified under pathMatcher.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaphostrule">URLMap<wbr>Host<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}The list of HostRules to use against the URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcher">URLMap<wbr>Path<wbr>Matcher[]?</a></span>
    </dt>
    <dd>{{% md %}}The list of named PathMatchers to use against the URL.
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
        <span>tests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaptest">URLMap<wbr>Test[]?</a></span>
    </dt>
    <dd>{{% md %}}The list of expected URL mapping tests. Request to update this UrlMap will succeed only if all of the test cases pass.
You can specify a maximum of 100 tests per UrlMap.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The backend service or backend bucket to use when none of the given rules match.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>header_<wbr>action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderaction">Dict[URLMap<wbr>Header<wbr>Action]</a></span>
    </dt>
    <dd>{{% md %}}Specifies changes to request and response headers that need to take effect for the selected backendService. The
headerAction specified here take effect after headerAction specified under pathMatcher.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaphostrule">List[URLMap<wbr>Host<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}The list of HostRules to use against the URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path_<wbr>matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcher">List[URLMap<wbr>Path<wbr>Matcher]</a></span>
    </dt>
    <dd>{{% md %}}The list of named PathMatchers to use against the URL.
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
        <span>tests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaptest">List[URLMap<wbr>Test]</a></span>
    </dt>
    <dd>{{% md %}}The list of expected URL mapping tests. Request to update this UrlMap will succeed only if all of the test cases pass.
You can specify a maximum of 100 tests per UrlMap.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## URLMap Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The backend service or backend bucket to use when none of the given rules match.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderaction">URLMap<wbr>Header<wbr>Action?</a></span>
    </dt>
    <dd>{{% md %}}Specifies changes to request and response headers that need to take effect for the selected backendService. The
headerAction specified here take effect after headerAction specified under pathMatcher.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Host<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaphostrule">List&lt;URLMap<wbr>Host<wbr>Rule&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The list of HostRules to use against the URL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Map<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The unique identifier for the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Path<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcher">List&lt;URLMap<wbr>Path<wbr>Matcher&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The list of named PathMatchers to use against the URL.
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
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaptest">List&lt;URLMap<wbr>Test&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The list of expected URL mapping tests. Request to update this UrlMap will succeed only if all of the test cases pass.
You can specify a maximum of 100 tests per UrlMap.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The backend service or backend bucket to use when none of the given rules match.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderaction">*URLMap<wbr>Header<wbr>Action</a></span>
    </dt>
    <dd>{{% md %}}Specifies changes to request and response headers that need to take effect for the selected backendService. The
headerAction specified here take effect after headerAction specified under pathMatcher.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Host<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaphostrule">[]URLMap<wbr>Host<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}The list of HostRules to use against the URL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Map<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The unique identifier for the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Path<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcher">[]URLMap<wbr>Path<wbr>Matcher</a></span>
    </dt>
    <dd>{{% md %}}The list of named PathMatchers to use against the URL.
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
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaptest">[]URLMap<wbr>Test</a></span>
    </dt>
    <dd>{{% md %}}The list of expected URL mapping tests. Request to update this UrlMap will succeed only if all of the test cases pass.
You can specify a maximum of 100 tests per UrlMap.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The backend service or backend bucket to use when none of the given rules match.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderaction">URLMap<wbr>Header<wbr>Action?</a></span>
    </dt>
    <dd>{{% md %}}Specifies changes to request and response headers that need to take effect for the selected backendService. The
headerAction specified here take effect after headerAction specified under pathMatcher.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>host<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaphostrule">URLMap<wbr>Host<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}The list of HostRules to use against the URL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>map<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The unique identifier for the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>path<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcher">URLMap<wbr>Path<wbr>Matcher[]?</a></span>
    </dt>
    <dd>{{% md %}}The list of named PathMatchers to use against the URL.
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
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaptest">URLMap<wbr>Test[]?</a></span>
    </dt>
    <dd>{{% md %}}The list of expected URL mapping tests. Request to update this UrlMap will succeed only if all of the test cases pass.
You can specify a maximum of 100 tests per UrlMap.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>creation_<wbr>timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The backend service or backend bucket to use when none of the given rules match.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>header_<wbr>action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderaction">Dict[URLMap<wbr>Header<wbr>Action]</a></span>
    </dt>
    <dd>{{% md %}}Specifies changes to request and response headers that need to take effect for the selected backendService. The
headerAction specified here take effect after headerAction specified under pathMatcher.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>host_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaphostrule">List[URLMap<wbr>Host<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}The list of HostRules to use against the URL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>map_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The unique identifier for the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>path_<wbr>matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcher">List[URLMap<wbr>Path<wbr>Matcher]</a></span>
    </dt>
    <dd>{{% md %}}The list of named PathMatchers to use against the URL.
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
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaptest">List[URLMap<wbr>Test]</a></span>
    </dt>
    <dd>{{% md %}}The list of expected URL mapping tests. Request to update this UrlMap will succeed only if all of the test cases pass.
You can specify a maximum of 100 tests per UrlMap.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing URLMap Resource

Get an existing URLMap resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#URLMapState">URLMapState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#URLMap">URLMap</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>creation_timestamp=None<span class="p">, </span>default_service=None<span class="p">, </span>description=None<span class="p">, </span>fingerprint=None<span class="p">, </span>header_action=None<span class="p">, </span>host_rules=None<span class="p">, </span>map_id=None<span class="p">, </span>name=None<span class="p">, </span>path_matchers=None<span class="p">, </span>project=None<span class="p">, </span>self_link=None<span class="p">, </span>tests=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetURLMap<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapState">URLMapState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMap">URLMap</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.URLMap.html">URLMap</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.URLMapState.html">URLMapState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The backend service or backend bucket to use when none of the given rules match.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderaction">URLMap<wbr>Header<wbr>Action<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specifies changes to request and response headers that need to take effect for the selected backendService. The
headerAction specified here take effect after headerAction specified under pathMatcher.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaphostrule">List&lt;URLMap<wbr>Host<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The list of HostRules to use against the URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Map<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The unique identifier for the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcher">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The list of named PathMatchers to use against the URL.
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
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaptest">List&lt;URLMap<wbr>Test<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The list of expected URL mapping tests. Request to update this UrlMap will succeed only if all of the test cases pass.
You can specify a maximum of 100 tests per UrlMap.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The backend service or backend bucket to use when none of the given rules match.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderaction">*URLMap<wbr>Header<wbr>Action</a></span>
    </dt>
    <dd>{{% md %}}Specifies changes to request and response headers that need to take effect for the selected backendService. The
headerAction specified here take effect after headerAction specified under pathMatcher.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaphostrule">[]URLMap<wbr>Host<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}The list of HostRules to use against the URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Map<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The unique identifier for the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcher">[]URLMap<wbr>Path<wbr>Matcher</a></span>
    </dt>
    <dd>{{% md %}}The list of named PathMatchers to use against the URL.
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
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaptest">[]URLMap<wbr>Test</a></span>
    </dt>
    <dd>{{% md %}}The list of expected URL mapping tests. Request to update this UrlMap will succeed only if all of the test cases pass.
You can specify a maximum of 100 tests per UrlMap.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The backend service or backend bucket to use when none of the given rules match.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderaction">URLMap<wbr>Header<wbr>Action?</a></span>
    </dt>
    <dd>{{% md %}}Specifies changes to request and response headers that need to take effect for the selected backendService. The
headerAction specified here take effect after headerAction specified under pathMatcher.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaphostrule">URLMap<wbr>Host<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}The list of HostRules to use against the URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>map<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The unique identifier for the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcher">URLMap<wbr>Path<wbr>Matcher[]?</a></span>
    </dt>
    <dd>{{% md %}}The list of named PathMatchers to use against the URL.
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
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaptest">URLMap<wbr>Test[]?</a></span>
    </dt>
    <dd>{{% md %}}The list of expected URL mapping tests. Request to update this UrlMap will succeed only if all of the test cases pass.
You can specify a maximum of 100 tests per UrlMap.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>creation_<wbr>timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Creation timestamp in RFC3339 text format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The backend service or backend bucket to use when none of the given rules match.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An optional description of this resource. Provide this property when you create the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>header_<wbr>action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderaction">Dict[URLMap<wbr>Header<wbr>Action]</a></span>
    </dt>
    <dd>{{% md %}}Specifies changes to request and response headers that need to take effect for the selected backendService. The
headerAction specified here take effect after headerAction specified under pathMatcher.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaphostrule">List[URLMap<wbr>Host<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}The list of HostRules to use against the URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>map_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The unique identifier for the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and
comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression
'[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all following characters
must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path_<wbr>matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcher">List[URLMap<wbr>Path<wbr>Matcher]</a></span>
    </dt>
    <dd>{{% md %}}The list of named PathMatchers to use against the URL.
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
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tests</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmaptest">List[URLMap<wbr>Test]</a></span>
    </dt>
    <dd>{{% md %}}The list of expected URL mapping tests. Request to update this UrlMap will succeed only if all of the test cases pass.
You can specify a maximum of 100 tests per UrlMap.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>URLMap<wbr>Header<wbr>Action</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapHeaderAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapHeaderAction">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapHeaderActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapHeaderActionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderactionrequestheaderstoadd">List&lt;URLMap<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderactionresponseheaderstoadd">List&lt;URLMap<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderactionrequestheaderstoadd">[]URLMap<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderactionresponseheaderstoadd">[]URLMap<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderactionrequestheaderstoadd">URLMap<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderactionresponseheaderstoadd">URLMap<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderactionrequestheaderstoadd">List[URLMap<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmapheaderactionresponseheaderstoadd">List[URLMap<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapHeaderActionRequestHeadersToAdd">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapHeaderActionRequestHeadersToAdd">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapHeaderActionRequestHeadersToAddArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapHeaderActionRequestHeadersToAddOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapHeaderActionResponseHeadersToAdd">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapHeaderActionResponseHeadersToAdd">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapHeaderActionResponseHeadersToAddArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapHeaderActionResponseHeadersToAddOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Host<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapHostRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapHostRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapHostRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapHostRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Path<wbr>Matcher</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Path<wbr>Matcher</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>path<wbr>Matcher</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>path<wbr>Matcher</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcher">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcher">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherheaderaction">URLMap<wbr>Path<wbr>Matcher<wbr>Header<wbr>Action<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrule">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Route<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterule">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherheaderaction">*URLMap<wbr>Path<wbr>Matcher<wbr>Header<wbr>Action</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrule">[]URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Route<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterule">[]URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherheaderaction">URLMap<wbr>Path<wbr>Matcher<wbr>Header<wbr>Action?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrule">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>route<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterule">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>header_<wbr>action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherheaderaction">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Header<wbr>Action]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrule">List[URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>route<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterule">List[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Header<wbr>Action</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherHeaderAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherHeaderAction">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherHeaderActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherHeaderActionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherheaderactionrequestheaderstoadd">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherheaderactionresponseheaderstoadd">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherheaderactionrequestheaderstoadd">[]URLMap<wbr>Path<wbr>Matcher<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherheaderactionresponseheaderstoadd">[]URLMap<wbr>Path<wbr>Matcher<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherheaderactionrequestheaderstoadd">URLMap<wbr>Path<wbr>Matcher<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherheaderactionresponseheaderstoadd">URLMap<wbr>Path<wbr>Matcher<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherheaderactionrequestheaderstoadd">List[URLMap<wbr>Path<wbr>Matcher<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherheaderactionresponseheaderstoadd">List[URLMap<wbr>Path<wbr>Matcher<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherHeaderActionRequestHeadersToAdd">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherHeaderActionRequestHeadersToAdd">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherHeaderActionRequestHeadersToAddArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherHeaderActionRequestHeadersToAddOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherHeaderActionResponseHeadersToAdd">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherHeaderActionResponseHeadersToAdd">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherHeaderActionResponseHeadersToAddArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherHeaderActionResponseHeadersToAddOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherPathRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherPathRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Route<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteaction">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathruleurlredirect">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Url<wbr>Redirect<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Route<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteaction">*URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathruleurlredirect">*URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Url<wbr>Redirect</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>paths</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>route<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteaction">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathruleurlredirect">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Url<wbr>Redirect?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>paths</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>route<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteaction">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathruleurlredirect">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Url<wbr>Redirect]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherPathRuleRouteAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherPathRuleRouteAction">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cors<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactioncorspolicy">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Cors<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fault<wbr>Injection<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionfaultinjectionpolicy">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Mirror<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionrequestmirrorpolicy">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Request<wbr>Mirror<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionretrypolicy">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactiontimeout">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Timeout<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionurlrewrite">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Url<wbr>Rewrite<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weighted<wbr>Backend<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionweightedbackendservice">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cors<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactioncorspolicy">*URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Cors<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fault<wbr>Injection<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionfaultinjectionpolicy">*URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Mirror<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionrequestmirrorpolicy">*URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Request<wbr>Mirror<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionretrypolicy">*URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactiontimeout">*URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Timeout</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionurlrewrite">*URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Url<wbr>Rewrite</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weighted<wbr>Backend<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionweightedbackendservice">[]URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cors<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactioncorspolicy">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Cors<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fault<wbr>Injection<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionfaultinjectionpolicy">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Mirror<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionrequestmirrorpolicy">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Request<wbr>Mirror<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionretrypolicy">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactiontimeout">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Timeout?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionurlrewrite">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Url<wbr>Rewrite?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weighted<wbr>Backend<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionweightedbackendservice">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cors<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactioncorspolicy">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Cors<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fault<wbr>Injection<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionfaultinjectionpolicy">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Mirror<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionrequestmirrorpolicy">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Request<wbr>Mirror<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionretrypolicy">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactiontimeout">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Timeout]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionurlrewrite">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Url<wbr>Rewrite]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weighted<wbr>Backend<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionweightedbackendservice">List[URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Cors<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherPathRuleRouteActionCorsPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherPathRuleRouteActionCorsPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionCorsPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionCorsPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Origin<wbr>Regexes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expose<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Age</span>
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
        <span>Allow<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Origin<wbr>Regexes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expose<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Age</span>
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
        <span>allow<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Origin<wbr>Regexes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expose<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Age</span>
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
        <span>allow<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Origin<wbr>Regexes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expose<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Age</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherPathRuleRouteActionFaultInjectionPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherPathRuleRouteActionFaultInjectionPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionFaultInjectionPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionFaultInjectionPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Abort</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionfaultinjectionpolicyabort">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Abort<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionfaultinjectionpolicydelay">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Abort</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionfaultinjectionpolicyabort">*URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Abort</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionfaultinjectionpolicydelay">*URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>abort</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionfaultinjectionpolicyabort">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Abort?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionfaultinjectionpolicydelay">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>abort</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionfaultinjectionpolicyabort">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Abort]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionfaultinjectionpolicydelay">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Abort</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbort">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionFaultInjectionPolicyAbortOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Http<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">double</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Http<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>http<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>percentage</span>
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
        <span>http<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelay">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Fixed<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionfaultinjectionpolicydelayfixeddelay">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay<wbr>Fixed<wbr>Delay<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">double</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Fixed<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionfaultinjectionpolicydelayfixeddelay">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay<wbr>Fixed<wbr>Delay</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>fixed<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionfaultinjectionpolicydelayfixeddelay">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay<wbr>Fixed<wbr>Delay</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>percentage</span>
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
        <span>fixed<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionfaultinjectionpolicydelayfixeddelay">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay<wbr>Fixed<wbr>Delay]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay<wbr>Fixed<wbr>Delay</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelay">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Request<wbr>Mirror<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherPathRuleRouteActionRequestMirrorPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherPathRuleRouteActionRequestMirrorPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionRequestMirrorPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionRequestMirrorPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Backend<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Backend<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>backend<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>backend_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherPathRuleRouteActionRetryPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherPathRuleRouteActionRetryPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionRetryPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionRetryPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Per<wbr>Try<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionretrypolicypertrytimeout">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy<wbr>Per<wbr>Try<wbr>Timeout<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Per<wbr>Try<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionretrypolicypertrytimeout">*URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy<wbr>Per<wbr>Try<wbr>Timeout</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>per<wbr>Try<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionretrypolicypertrytimeout">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy<wbr>Per<wbr>Try<wbr>Timeout?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry<wbr>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>per<wbr>Try<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionretrypolicypertrytimeout">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy<wbr>Per<wbr>Try<wbr>Timeout]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry<wbr>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy<wbr>Per<wbr>Try<wbr>Timeout</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeout">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionRetryPolicyPerTryTimeoutOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Timeout</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherPathRuleRouteActionTimeout">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherPathRuleRouteActionTimeout">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionTimeoutArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionTimeoutOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Url<wbr>Rewrite</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherPathRuleRouteActionUrlRewrite">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherPathRuleRouteActionUrlRewrite">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionUrlRewriteArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionUrlRewriteOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path<wbr>Prefix<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path<wbr>Prefix<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path<wbr>Prefix<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path<wbr>Prefix<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherPathRuleRouteActionWeightedBackendService">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherPathRuleRouteActionWeightedBackendService">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionWeightedBackendServiceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionWeightedBackendServiceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Backend<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionweightedbackendserviceheaderaction">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Args?</a></span>
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
        <span>Backend<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionweightedbackendserviceheaderaction">*URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action</a></span>
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
        <span>backend<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionweightedbackendserviceheaderaction">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action?</a></span>
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
        <span>backend_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>header_<wbr>action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionweightedbackendserviceheaderaction">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action]</a></span>
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





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherPathRuleRouteActionWeightedBackendServiceHeaderAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherPathRuleRouteActionWeightedBackendServiceHeaderAction">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionWeightedBackendServiceHeaderActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionWeightedBackendServiceHeaderActionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionweightedbackendserviceheaderactionrequestheaderstoadd">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionweightedbackendserviceheaderactionresponseheaderstoadd">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionweightedbackendserviceheaderactionrequestheaderstoadd">[]URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionweightedbackendserviceheaderactionresponseheaderstoadd">[]URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionweightedbackendserviceheaderactionrequestheaderstoadd">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionweightedbackendserviceheaderactionresponseheaderstoadd">URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionweightedbackendserviceheaderactionrequestheaderstoadd">List[URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherpathrulerouteactionweightedbackendserviceheaderactionresponseheaderstoadd">List[URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherPathRuleRouteActionWeightedBackendServiceHeaderActionRequestHeadersToAdd">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherPathRuleRouteActionWeightedBackendServiceHeaderActionRequestHeadersToAdd">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionWeightedBackendServiceHeaderActionRequestHeadersToAddArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionWeightedBackendServiceHeaderActionRequestHeadersToAddOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherPathRuleRouteActionWeightedBackendServiceHeaderActionResponseHeadersToAdd">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherPathRuleRouteActionWeightedBackendServiceHeaderActionResponseHeadersToAdd">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionWeightedBackendServiceHeaderActionResponseHeadersToAddArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleRouteActionWeightedBackendServiceHeaderActionResponseHeadersToAddOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Path<wbr>Rule<wbr>Url<wbr>Redirect</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherPathRuleUrlRedirect">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherPathRuleUrlRedirect">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleUrlRedirectArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherPathRuleUrlRedirectOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Https<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Prefix<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Redirect<wbr>Response<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Strip<wbr>Query</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Https<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Prefix<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Redirect<wbr>Response<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Strip<wbr>Query</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>https<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>prefix<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>redirect<wbr>Response<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>strip<wbr>Query</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>https<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>prefix<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>redirect<wbr>Response<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>strip<wbr>Query</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouteruleheaderaction">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Header<wbr>Action<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchrule">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Route<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteaction">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouteruleurlredirect">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Url<wbr>Redirect<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouteruleheaderaction">*URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Header<wbr>Action</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchrule">[]URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Route<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteaction">*URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouteruleurlredirect">*URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Url<wbr>Redirect</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouteruleheaderaction">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Header<wbr>Action?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchrule">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>route<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteaction">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouteruleurlredirect">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Url<wbr>Redirect?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>header_<wbr>action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouteruleheaderaction">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Header<wbr>Action]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchrule">List[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>route<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteaction">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouteruleurlredirect">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Url<wbr>Redirect]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Header<wbr>Action</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleHeaderAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleHeaderAction">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleHeaderActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleHeaderActionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouteruleheaderactionrequestheaderstoadd">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouteruleheaderactionresponseheaderstoadd">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouteruleheaderactionrequestheaderstoadd">[]URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouteruleheaderactionresponseheaderstoadd">[]URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouteruleheaderactionrequestheaderstoadd">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouteruleheaderactionresponseheaderstoadd">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouteruleheaderactionrequestheaderstoadd">List[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouteruleheaderactionresponseheaderstoadd">List[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleHeaderActionRequestHeadersToAdd">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleHeaderActionRequestHeadersToAdd">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleHeaderActionRequestHeadersToAddArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleHeaderActionRequestHeadersToAddOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleHeaderActionResponseHeadersToAdd">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleHeaderActionResponseHeadersToAdd">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleHeaderActionResponseHeadersToAddArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleHeaderActionResponseHeadersToAddOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleMatchRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleMatchRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleMatchRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleMatchRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Full<wbr>Path<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Header<wbr>Matches</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchruleheadermatch">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Header<wbr>Match<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ignore<wbr>Case</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata<wbr>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchrulemetadatafilter">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Metadata<wbr>Filter<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Prefix<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>Parameter<wbr>Matches</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchrulequeryparametermatch">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Query<wbr>Parameter<wbr>Match<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Regex<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Full<wbr>Path<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Header<wbr>Matches</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchruleheadermatch">[]URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Header<wbr>Match</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ignore<wbr>Case</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata<wbr>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchrulemetadatafilter">[]URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Metadata<wbr>Filter</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Prefix<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Query<wbr>Parameter<wbr>Matches</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchrulequeryparametermatch">[]URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Query<wbr>Parameter<wbr>Match</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Regex<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>full<wbr>Path<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>header<wbr>Matches</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchruleheadermatch">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Header<wbr>Match[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ignore<wbr>Case</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata<wbr>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchrulemetadatafilter">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Metadata<wbr>Filter[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>prefix<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>Parameter<wbr>Matches</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchrulequeryparametermatch">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Query<wbr>Parameter<wbr>Match[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>regex<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>full<wbr>Path<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>header<wbr>Matches</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchruleheadermatch">List[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Header<wbr>Match]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ignore<wbr>Case</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata_<wbr>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchrulemetadatafilter">List[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Metadata<wbr>Filter]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>prefix<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>query<wbr>Parameter<wbr>Matches</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchrulequeryparametermatch">List[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Query<wbr>Parameter<wbr>Match]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>regex<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Header<wbr>Match</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleMatchRuleHeaderMatch">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleMatchRuleHeaderMatch">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleMatchRuleHeaderMatchArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleMatchRuleHeaderMatchOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Exact<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Invert<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Prefix<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Present<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Range<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchruleheadermatchrangematch">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Header<wbr>Match<wbr>Range<wbr>Match<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Regex<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Suffix<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Exact<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Invert<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Prefix<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Present<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Range<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchruleheadermatchrangematch">*URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Header<wbr>Match<wbr>Range<wbr>Match</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Regex<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Suffix<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>exact<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>invert<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>prefix<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>present<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>range<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchruleheadermatchrangematch">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Header<wbr>Match<wbr>Range<wbr>Match?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>regex<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>suffix<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>exact<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>invert<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>prefix<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>present<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>range<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchruleheadermatchrangematch">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Header<wbr>Match<wbr>Range<wbr>Match]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>regex<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>suffix<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Header<wbr>Match<wbr>Range<wbr>Match</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleMatchRuleHeaderMatchRangeMatch">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleMatchRuleHeaderMatchRangeMatch">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleMatchRuleHeaderMatchRangeMatchArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleMatchRuleHeaderMatchRangeMatchOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Range<wbr>End</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Range<wbr>Start</span>
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
        <span>Range<wbr>End</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Range<wbr>Start</span>
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
        <span>range<wbr>End</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>range<wbr>Start</span>
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
        <span>range<wbr>End</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>range<wbr>Start</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Metadata<wbr>Filter</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleMatchRuleMetadataFilter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleMatchRuleMetadataFilter">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleMatchRuleMetadataFilterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleMatchRuleMetadataFilterOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Filter<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchrulemetadatafilterfilterlabel">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Metadata<wbr>Filter<wbr>Filter<wbr>Label<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Filter<wbr>Match<wbr>Criteria</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Filter<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchrulemetadatafilterfilterlabel">[]URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Metadata<wbr>Filter<wbr>Filter<wbr>Label</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Filter<wbr>Match<wbr>Criteria</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>filter<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchrulemetadatafilterfilterlabel">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Metadata<wbr>Filter<wbr>Filter<wbr>Label[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>filter<wbr>Match<wbr>Criteria</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>filter<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulematchrulemetadatafilterfilterlabel">List[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Metadata<wbr>Filter<wbr>Filter<wbr>Label]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>filter<wbr>Match<wbr>Criteria</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Metadata<wbr>Filter<wbr>Filter<wbr>Label</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleMatchRuleMetadataFilterFilterLabel">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleMatchRuleMetadataFilterFilterLabel">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleMatchRuleMetadataFilterFilterLabelArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleMatchRuleMetadataFilterFilterLabelOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Match<wbr>Rule<wbr>Query<wbr>Parameter<wbr>Match</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleMatchRuleQueryParameterMatch">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleMatchRuleQueryParameterMatch">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleMatchRuleQueryParameterMatchArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleMatchRuleQueryParameterMatchOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Exact<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Present<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Regex<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Exact<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Present<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Regex<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>exact<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>present<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>regex<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>exact<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>present<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>regex<wbr>Match</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleRouteAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleRouteAction">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cors<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactioncorspolicy">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Cors<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fault<wbr>Injection<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionfaultinjectionpolicy">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Mirror<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionrequestmirrorpolicy">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Request<wbr>Mirror<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionretrypolicy">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactiontimeout">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Timeout<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionurlrewrite">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Url<wbr>Rewrite<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weighted<wbr>Backend<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionweightedbackendservice">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cors<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactioncorspolicy">*URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Cors<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fault<wbr>Injection<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionfaultinjectionpolicy">*URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Mirror<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionrequestmirrorpolicy">*URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Request<wbr>Mirror<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionretrypolicy">*URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactiontimeout">*URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Timeout</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionurlrewrite">*URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Url<wbr>Rewrite</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weighted<wbr>Backend<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionweightedbackendservice">[]URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cors<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactioncorspolicy">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Cors<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fault<wbr>Injection<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionfaultinjectionpolicy">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Mirror<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionrequestmirrorpolicy">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Request<wbr>Mirror<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionretrypolicy">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactiontimeout">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Timeout?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionurlrewrite">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Url<wbr>Rewrite?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weighted<wbr>Backend<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionweightedbackendservice">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cors<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactioncorspolicy">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Cors<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fault<wbr>Injection<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionfaultinjectionpolicy">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Mirror<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionrequestmirrorpolicy">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Request<wbr>Mirror<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionretrypolicy">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactiontimeout">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Timeout]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionurlrewrite">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Url<wbr>Rewrite]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weighted<wbr>Backend<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionweightedbackendservice">List[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Cors<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleRouteActionCorsPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleRouteActionCorsPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionCorsPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionCorsPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Origin<wbr>Regexes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expose<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Age</span>
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
        <span>Allow<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Origin<wbr>Regexes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expose<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Age</span>
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
        <span>allow<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Origin<wbr>Regexes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expose<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Age</span>
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
        <span>allow<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Origin<wbr>Regexes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expose<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Age</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Abort</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionfaultinjectionpolicyabort">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Abort<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionfaultinjectionpolicydelay">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Abort</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionfaultinjectionpolicyabort">*URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Abort</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionfaultinjectionpolicydelay">*URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>abort</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionfaultinjectionpolicyabort">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Abort?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionfaultinjectionpolicydelay">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>abort</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionfaultinjectionpolicyabort">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Abort]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionfaultinjectionpolicydelay">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Abort</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyAbort">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyAbort">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyAbortArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyAbortOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>percentage</span>
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
        <span>http<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyDelay">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyDelay">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyDelayArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyDelayOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fixed<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionfaultinjectionpolicydelayfixeddelay">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay<wbr>Fixed<wbr>Delay<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fixed<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionfaultinjectionpolicydelayfixeddelay">*URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay<wbr>Fixed<wbr>Delay</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fixed<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionfaultinjectionpolicydelayfixeddelay">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay<wbr>Fixed<wbr>Delay?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>percentage</span>
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
        <span>fixed<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionfaultinjectionpolicydelayfixeddelay">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay<wbr>Fixed<wbr>Delay]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Fault<wbr>Injection<wbr>Policy<wbr>Delay<wbr>Fixed<wbr>Delay</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyDelayFixedDelay">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyDelayFixedDelay">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyDelayFixedDelayArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionFaultInjectionPolicyDelayFixedDelayOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Request<wbr>Mirror<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleRouteActionRequestMirrorPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleRouteActionRequestMirrorPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionRequestMirrorPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionRequestMirrorPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Backend<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Backend<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>backend<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>backend_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleRouteActionRetryPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleRouteActionRetryPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionRetryPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionRetryPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Num<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Per<wbr>Try<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionretrypolicypertrytimeout">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy<wbr>Per<wbr>Try<wbr>Timeout<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Num<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Per<wbr>Try<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionretrypolicypertrytimeout">*URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy<wbr>Per<wbr>Try<wbr>Timeout</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Conditions</span>
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
        <span>num<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>per<wbr>Try<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionretrypolicypertrytimeout">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy<wbr>Per<wbr>Try<wbr>Timeout?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry<wbr>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>num<wbr>Retries</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>per<wbr>Try<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionretrypolicypertrytimeout">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy<wbr>Per<wbr>Try<wbr>Timeout]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry<wbr>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Retry<wbr>Policy<wbr>Per<wbr>Try<wbr>Timeout</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleRouteActionRetryPolicyPerTryTimeout">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleRouteActionRetryPolicyPerTryTimeout">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionRetryPolicyPerTryTimeoutArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionRetryPolicyPerTryTimeoutOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Timeout</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleRouteActionTimeout">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleRouteActionTimeout">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionTimeoutArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionTimeoutOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>nanos</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Url<wbr>Rewrite</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleRouteActionUrlRewrite">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleRouteActionUrlRewrite">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionUrlRewriteArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionUrlRewriteOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path<wbr>Prefix<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path<wbr>Prefix<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path<wbr>Prefix<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path<wbr>Prefix<wbr>Rewrite</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleRouteActionWeightedBackendService">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleRouteActionWeightedBackendService">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Backend<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionweightedbackendserviceheaderaction">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Args?</a></span>
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
        <span>Backend<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionweightedbackendserviceheaderaction">*URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action</a></span>
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
        <span>backend<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>header<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionweightedbackendserviceheaderaction">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action?</a></span>
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
        <span>backend_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>header_<wbr>action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionweightedbackendserviceheaderaction">Dict[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action]</a></span>
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





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceHeaderAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceHeaderAction">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceHeaderActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceHeaderActionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionweightedbackendserviceheaderactionrequestheaderstoadd">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionweightedbackendserviceheaderactionresponseheaderstoadd">List&lt;URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionweightedbackendserviceheaderactionrequestheaderstoadd">[]URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionweightedbackendserviceheaderactionresponseheaderstoadd">[]URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionweightedbackendserviceheaderactionrequestheaderstoadd">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionweightedbackendserviceheaderactionresponseheaderstoadd">URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionweightedbackendserviceheaderactionrequestheaderstoadd">List[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Adds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#urlmappathmatcherrouterulerouteactionweightedbackendserviceheaderactionresponseheaderstoadd">List[URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Headers<wbr>To<wbr>Removes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Request<wbr>Headers<wbr>To<wbr>Add</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceHeaderActionRequestHeadersToAdd">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceHeaderActionRequestHeadersToAdd">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceHeaderActionRequestHeadersToAddArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceHeaderActionRequestHeadersToAddOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Route<wbr>Action<wbr>Weighted<wbr>Backend<wbr>Service<wbr>Header<wbr>Action<wbr>Response<wbr>Headers<wbr>To<wbr>Add</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceHeaderActionResponseHeadersToAdd">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceHeaderActionResponseHeadersToAdd">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceHeaderActionResponseHeadersToAddArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleRouteActionWeightedBackendServiceHeaderActionResponseHeadersToAddOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>Header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
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
        <span>header<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>header<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>replace</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Path<wbr>Matcher<wbr>Route<wbr>Rule<wbr>Url<wbr>Redirect</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapPathMatcherRouteRuleUrlRedirect">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapPathMatcherRouteRuleUrlRedirect">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleUrlRedirectArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapPathMatcherRouteRuleUrlRedirectOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Https<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Prefix<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Redirect<wbr>Response<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Strip<wbr>Query</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Https<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Prefix<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Redirect<wbr>Response<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Strip<wbr>Query</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>https<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>prefix<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>redirect<wbr>Response<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>strip<wbr>Query</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>https<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>prefix<wbr>Redirect</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>redirect<wbr>Response<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>strip<wbr>Query</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>URLMap<wbr>Test</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#URLMapTest">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#URLMapTest">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapTestArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#URLMapTestOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}







