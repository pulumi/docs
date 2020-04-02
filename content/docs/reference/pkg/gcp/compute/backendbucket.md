
---
title: "BackendBucket"
block_external_search_index: true
---

Backend buckets allow you to use Google Cloud Storage buckets with HTTP(S)
load balancing.

An HTTP(S) load balancer can direct traffic to specified URLs to a
backend bucket rather than a backend service. It can send requests for
static content to a Cloud Storage bucket and requests for dynamic content
to a virtual machine instance.


To get more information about BackendBucket, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/v1/backendBuckets)
* How-to Guides
    * [Using a Cloud Storage bucket as a load balancer backend](https://cloud.google.com/compute/docs/load-balancing/http/backend-bucket)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_backend_bucket.html.markdown.



## Create a BackendBucket Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#BackendBucket">BackendBucket</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#BackendBucketArgs">BackendBucketArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">BackendBucket</span><span class="p">(resource_name, opts=None, </span>bucket_name=None<span class="p">, </span>cdn_policy=None<span class="p">, </span>description=None<span class="p">, </span>enable_cdn=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewBackendBucket<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendBucketArgs">BackendBucketArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendBucket">BackendBucket</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.BackendBucket.html">BackendBucket</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.BackendBucketArgs.html">BackendBucketArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cloud Storage bucket name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendbucketcdnpolicy">Backend<wbr>Bucket<wbr>Cdn<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this Backend Bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional textual description of the resource; provided by the client when the resource is created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendBucket.
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
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cloud Storage bucket name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendbucketcdnpolicy">*Backend<wbr>Bucket<wbr>Cdn<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this Backend Bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An optional textual description of the resource; provided by the client when the resource is created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendBucket.
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
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cloud Storage bucket name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendbucketcdnpolicy">Backend<wbr>Bucket<wbr>Cdn<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this Backend Bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional textual description of the resource; provided by the client when the resource is created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendBucket.
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
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>bucket_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cloud Storage bucket name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cdn_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendbucketcdnpolicy">Dict[Backend<wbr>Bucket<wbr>Cdn<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this Backend Bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An optional textual description of the resource; provided by the client when the resource is created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendBucket.
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
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## BackendBucket Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cloud Storage bucket name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendbucketcdnpolicy">Backend<wbr>Bucket<wbr>Cdn<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this Backend Bucket.
{{% /md %}}</dd>

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
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional textual description of the resource; provided by the client when the resource is created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendBucket.
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

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cloud Storage bucket name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendbucketcdnpolicy">Backend<wbr>Bucket<wbr>Cdn<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this Backend Bucket.
{{% /md %}}</dd>

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
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An optional textual description of the resource; provided by the client when the resource is created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendBucket.
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

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Cloud Storage bucket name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendbucketcdnpolicy">Backend<wbr>Bucket<wbr>Cdn<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this Backend Bucket.
{{% /md %}}</dd>

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
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional textual description of the resource; provided by the client when the resource is created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendBucket.
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

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>bucket_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cloud Storage bucket name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cdn_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendbucketcdnpolicy">Dict[Backend<wbr>Bucket<wbr>Cdn<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this Backend Bucket.
{{% /md %}}</dd>

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
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An optional textual description of the resource; provided by the client when the resource is created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendBucket.
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

</dl>
{{% /choosable %}}








## Look up an Existing BackendBucket Resource

Get an existing BackendBucket resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#BackendBucketState">BackendBucketState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#BackendBucket">BackendBucket</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>bucket_name=None<span class="p">, </span>cdn_policy=None<span class="p">, </span>creation_timestamp=None<span class="p">, </span>description=None<span class="p">, </span>enable_cdn=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, </span>self_link=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetBackendBucket<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendBucketState">BackendBucketState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendBucket">BackendBucket</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.BackendBucket.html">BackendBucket</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.BackendBucketState.html">BackendBucketState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cloud Storage bucket name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendbucketcdnpolicy">Backend<wbr>Bucket<wbr>Cdn<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this Backend Bucket.
{{% /md %}}</dd>

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
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional textual description of the resource; provided by the client when the resource is created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendBucket.
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

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Cloud Storage bucket name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendbucketcdnpolicy">*Backend<wbr>Bucket<wbr>Cdn<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this Backend Bucket.
{{% /md %}}</dd>

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
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An optional textual description of the resource; provided by the client when the resource is created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendBucket.
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

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Cloud Storage bucket name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cdn<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendbucketcdnpolicy">Backend<wbr>Bucket<wbr>Cdn<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this Backend Bucket.
{{% /md %}}</dd>

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
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An optional textual description of the resource; provided by the client when the resource is created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendBucket.
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

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>bucket_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Cloud Storage bucket name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cdn_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendbucketcdnpolicy">Dict[Backend<wbr>Bucket<wbr>Cdn<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}Cloud CDN configuration for this Backend Bucket.
{{% /md %}}</dd>

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
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An optional textual description of the resource; provided by the client when the resource is created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>cdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, enable Cloud CDN for this BackendBucket.
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

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Backend<wbr>Bucket<wbr>Cdn<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#BackendBucketCdnPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#BackendBucketCdnPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendBucketCdnPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#BackendBucketCdnPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Signed<wbr>Url<wbr>Cache<wbr>Max<wbr>Age<wbr>Sec</span>
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
        <span>Signed<wbr>Url<wbr>Cache<wbr>Max<wbr>Age<wbr>Sec</span>
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
        <span>signed<wbr>Url<wbr>Cache<wbr>Max<wbr>Age<wbr>Sec</span>
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
        <span>signed<wbr>Url<wbr>Cache<wbr>Max<wbr>Age<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
