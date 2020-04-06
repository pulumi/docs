
---
title: "GetBucketObjects"
block_external_search_index: true
---



This data source provides the objects of an OSS bucket.

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/oss_bucket_objects.html.markdown.





## Using GetBucketObjects

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getBucketObjects<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/oss/#GetBucketObjectsArgs">GetBucketObjectsArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/oss/#GetBucketObjectsResult">GetBucketObjectsResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_bucket_objects(</span>bucket_name=None<span class="p">, </span>key_prefix=None<span class="p">, </span>key_regex=None<span class="p">, </span>output_file=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupBucketObjects<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#LookupBucketObjectsArgs">LookupBucketObjectsArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#LookupBucketObjectsResult">LookupBucketObjectsResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetBucketObjects </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Oss.GetBucketObjectsResult.html">GetBucketObjectsResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Oss.GetBucketObjectsArgs.html">GetBucketObjectsArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the bucket that contains the objects to find.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filter results by the given key prefix (such as "path/to/folder/logs-").
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}Name of the bucket that contains the objects to find.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filter results by the given key prefix (such as "path/to/folder/logs-").
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}Name of the bucket that contains the objects to find.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filter results by the given key prefix (such as "path/to/folder/logs-").
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}Name of the bucket that contains the objects to find.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filter results by the given key prefix (such as "path/to/folder/logs-").
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetBucketObjects Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Objects</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketobjectsobject">List&lt;Get<wbr>Bucket<wbr>Objects<wbr>Object&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of bucket objects. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Objects</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketobjectsobject">[]Get<wbr>Bucket<wbr>Objects<wbr>Object</a></span>
    </dt>
    <dd>{{% md %}}A list of bucket objects. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>objects</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketobjectsobject">Get<wbr>Bucket<wbr>Objects<wbr>Object[]</a></span>
    </dt>
    <dd>{{% md %}}A list of bucket objects. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>objects</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketobjectsobject">List[Get<wbr>Bucket<wbr>Objects<wbr>Object]</a></span>
    </dt>
    <dd>{{% md %}}A list of bucket objects. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Bucket<wbr>Objects<wbr>Object</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetBucketObjectsObject">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#GetBucketObjectsObject">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Object access control list. Possible values: `default`, `private`, `public-read` and `public-read-write`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Caching behavior along the request/reply chain. Read [RFC2616 Cache-Control](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Presentational information for the object. Read [RFC2616 Content-Disposition](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Content encodings that have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [RFC2616 Content-Encoding](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Content<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Size of the object in bytes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Content<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}MD5 value of the content. Read [MD5](https://www.alibabacloud.com/help/doc-detail/31978.htm) for computing method.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Standard MIME type describing the format of the object data, e.g. "application/octet-stream".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ETag generated for the object (MD5 sum of the object content).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Expires</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Expiration date for the the request/response. Read [RFC2616 Expires](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Object key.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Last<wbr>Modification<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Last modification time of the object.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>Side<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Server-side encryption of the object in OSS. It can be empty or `AES256`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sse<wbr>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If present, specifies the ID of the Key Management Service(KMS) master encryption key that was used for the object.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Object storage type. Possible values: `Standard`, `IA` and `Archive`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Object access control list. Possible values: `default`, `private`, `public-read` and `public-read-write`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Caching behavior along the request/reply chain. Read [RFC2616 Cache-Control](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Presentational information for the object. Read [RFC2616 Content-Disposition](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Content encodings that have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [RFC2616 Content-Encoding](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Content<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Size of the object in bytes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Content<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}MD5 value of the content. Read [MD5](https://www.alibabacloud.com/help/doc-detail/31978.htm) for computing method.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Standard MIME type describing the format of the object data, e.g. "application/octet-stream".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ETag generated for the object (MD5 sum of the object content).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Expires</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Expiration date for the the request/response. Read [RFC2616 Expires](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Object key.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Last<wbr>Modification<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Last modification time of the object.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>Side<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Server-side encryption of the object in OSS. It can be empty or `AES256`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sse<wbr>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If present, specifies the ID of the Key Management Service(KMS) master encryption key that was used for the object.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Object storage type. Possible values: `Standard`, `IA` and `Archive`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Object access control list. Possible values: `default`, `private`, `public-read` and `public-read-write`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Caching behavior along the request/reply chain. Read [RFC2616 Cache-Control](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Presentational information for the object. Read [RFC2616 Content-Disposition](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Content encodings that have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [RFC2616 Content-Encoding](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>content<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Size of the object in bytes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>content<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}MD5 value of the content. Read [MD5](https://www.alibabacloud.com/help/doc-detail/31978.htm) for computing method.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Standard MIME type describing the format of the object data, e.g. "application/octet-stream".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ETag generated for the object (MD5 sum of the object content).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>expires</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Expiration date for the the request/response. Read [RFC2616 Expires](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Object key.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>last<wbr>Modification<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Last modification time of the object.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server<wbr>Side<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Server-side encryption of the object in OSS. It can be empty or `AES256`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sse<wbr>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If present, specifies the ID of the Key Management Service(KMS) master encryption key that was used for the object.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Object storage type. Possible values: `Standard`, `IA` and `Archive`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Object access control list. Possible values: `default`, `private`, `public-read` and `public-read-write`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cache_<wbr>control</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Caching behavior along the request/reply chain. Read [RFC2616 Cache-Control](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>content_<wbr>disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Presentational information for the object. Read [RFC2616 Content-Disposition](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>content_<wbr>encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Content encodings that have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [RFC2616 Content-Encoding](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>content_<wbr>length</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Size of the object in bytes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>content_<wbr>md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}MD5 value of the content. Read [MD5](https://www.alibabacloud.com/help/doc-detail/31978.htm) for computing method.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>content_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Standard MIME type describing the format of the object data, e.g. "application/octet-stream".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ETag generated for the object (MD5 sum of the object content).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>expires</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Expiration date for the the request/response. Read [RFC2616 Expires](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Object key.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>last<wbr>Modification<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Last modification time of the object.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server_<wbr>side_<wbr>encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Server-side encryption of the object in OSS. It can be empty or `AES256`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sse<wbr>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If present, specifies the ID of the Key Management Service(KMS) master encryption key that was used for the object.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Object storage type. Possible values: `Standard`, `IA` and `Archive`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







