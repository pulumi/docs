
---
title: "BucketObject"
block_external_search_index: true
---



Provides a resource to put a object(content or file) to a oss bucket.

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/oss_bucket_object.html.markdown.



## Create a BucketObject Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/oss/#BucketObject">BucketObject</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/oss/#BucketObjectArgs">BucketObjectArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">BucketObject</span><span class="p">(resource_name, opts=None, </span>acl=None<span class="p">, </span>bucket=None<span class="p">, </span>cache_control=None<span class="p">, </span>content=None<span class="p">, </span>content_disposition=None<span class="p">, </span>content_encoding=None<span class="p">, </span>content_md5=None<span class="p">, </span>content_type=None<span class="p">, </span>expires=None<span class="p">, </span>key=None<span class="p">, </span>kms_key_id=None<span class="p">, </span>server_side_encryption=None<span class="p">, </span>source=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewBucketObject<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketObjectArgs">BucketObjectArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketObject">BucketObject</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Oss.BucketObject.html">BucketObject</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Oss.BucketObjectArgs.html">BucketObjectArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/52284.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket to put the file in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies caching behavior along the request/reply chain. Read [RFC2616 Cache-Control](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The literal content being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies presentational information for the object. Read [RFC2616 Content-Disposition](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [RFC2616 Content-Encoding](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The MD5 value of the content. Read [MD5](https://www.alibabacloud.com/help/doc-detail/31978.htm) for computing method.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expires</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies expire date for the the request/response. Read [RFC2616 Expires](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the object once it is in the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the primary key managed by KMS. This parameter is valid when the value of `server_side_encryption` is set to KMS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Side<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies server-side encryption of the object in OSS. Valid values are `AES256`, `KMS`. Default value is `AES256`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path to the source file being uploaded to the bucket.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/52284.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket to put the file in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies caching behavior along the request/reply chain. Read [RFC2616 Cache-Control](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The literal content being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies presentational information for the object. Read [RFC2616 Content-Disposition](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [RFC2616 Content-Encoding](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The MD5 value of the content. Read [MD5](https://www.alibabacloud.com/help/doc-detail/31978.htm) for computing method.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expires</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies expire date for the the request/response. Read [RFC2616 Expires](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the object once it is in the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the primary key managed by KMS. This parameter is valid when the value of `server_side_encryption` is set to KMS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Side<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies server-side encryption of the object in OSS. Valid values are `AES256`, `KMS`. Default value is `AES256`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The path to the source file being uploaded to the bucket.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/52284.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket to put the file in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies caching behavior along the request/reply chain. Read [RFC2616 Cache-Control](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The literal content being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies presentational information for the object. Read [RFC2616 Content-Disposition](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [RFC2616 Content-Encoding](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The MD5 value of the content. Read [MD5](https://www.alibabacloud.com/help/doc-detail/31978.htm) for computing method.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expires</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies expire date for the the request/response. Read [RFC2616 Expires](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the object once it is in the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the primary key managed by KMS. This parameter is valid when the value of `server_side_encryption` is set to KMS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Side<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies server-side encryption of the object in OSS. Valid values are `AES256`, `KMS`. Default value is `AES256`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path to the source file being uploaded to the bucket.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/52284.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the bucket to put the file in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cache_<wbr>control</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies caching behavior along the request/reply chain. Read [RFC2616 Cache-Control](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The literal content being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies presentational information for the object. Read [RFC2616 Content-Disposition](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [RFC2616 Content-Encoding](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The MD5 value of the content. Read [MD5](https://www.alibabacloud.com/help/doc-detail/31978.htm) for computing method.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expires</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies expire date for the the request/response. Read [RFC2616 Expires](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the object once it is in the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms_<wbr>key_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the primary key managed by KMS. This parameter is valid when the value of `server_side_encryption` is set to KMS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server_<wbr>side_<wbr>encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies server-side encryption of the object in OSS. Valid values are `AES256`, `KMS`. Default value is `AES256`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The path to the source file being uploaded to the bucket.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## BucketObject Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/52284.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket to put the file in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies caching behavior along the request/reply chain. Read [RFC2616 Cache-Control](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The literal content being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies presentational information for the object. Read [RFC2616 Content-Disposition](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [RFC2616 Content-Encoding](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the content length of request.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The MD5 value of the content. Read [MD5](https://www.alibabacloud.com/help/doc-detail/31978.htm) for computing method.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the ETag generated for the object (an MD5 sum of the object content).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expires</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies expire date for the the request/response. Read [RFC2616 Expires](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the object once it is in the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the primary key managed by KMS. This parameter is valid when the value of `server_side_encryption` is set to KMS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Server<wbr>Side<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies server-side encryption of the object in OSS. Valid values are `AES256`, `KMS`. Default value is `AES256`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path to the source file being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique version ID value for the object, if bucket versioning is enabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/52284.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket to put the file in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies caching behavior along the request/reply chain. Read [RFC2616 Cache-Control](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The literal content being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies presentational information for the object. Read [RFC2616 Content-Disposition](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [RFC2616 Content-Encoding](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the content length of request.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The MD5 value of the content. Read [MD5](https://www.alibabacloud.com/help/doc-detail/31978.htm) for computing method.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the ETag generated for the object (an MD5 sum of the object content).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expires</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies expire date for the the request/response. Read [RFC2616 Expires](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the object once it is in the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the primary key managed by KMS. This parameter is valid when the value of `server_side_encryption` is set to KMS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Server<wbr>Side<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies server-side encryption of the object in OSS. Valid values are `AES256`, `KMS`. Default value is `AES256`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The path to the source file being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique version ID value for the object, if bucket versioning is enabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/52284.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket to put the file in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies caching behavior along the request/reply chain. Read [RFC2616 Cache-Control](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The literal content being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies presentational information for the object. Read [RFC2616 Content-Disposition](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [RFC2616 Content-Encoding](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the content length of request.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The MD5 value of the content. Read [MD5](https://www.alibabacloud.com/help/doc-detail/31978.htm) for computing method.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the ETag generated for the object (an MD5 sum of the object content).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expires</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies expire date for the the request/response. Read [RFC2616 Expires](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the object once it is in the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the primary key managed by KMS. This parameter is valid when the value of `server_side_encryption` is set to KMS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>server<wbr>Side<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies server-side encryption of the object in OSS. Valid values are `AES256`, `KMS`. Default value is `AES256`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path to the source file being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique version ID value for the object, if bucket versioning is enabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/52284.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the bucket to put the file in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cache_<wbr>control</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies caching behavior along the request/reply chain. Read [RFC2616 Cache-Control](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The literal content being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content_<wbr>disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies presentational information for the object. Read [RFC2616 Content-Disposition](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content_<wbr>encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [RFC2616 Content-Encoding](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content_<wbr>length</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the content length of request.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content_<wbr>md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The MD5 value of the content. Read [MD5](https://www.alibabacloud.com/help/doc-detail/31978.htm) for computing method.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the ETag generated for the object (an MD5 sum of the object content).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expires</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies expire date for the the request/response. Read [RFC2616 Expires](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the object once it is in the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kms_<wbr>key_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the primary key managed by KMS. This parameter is valid when the value of `server_side_encryption` is set to KMS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>server_<wbr>side_<wbr>encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies server-side encryption of the object in OSS. Valid values are `AES256`, `KMS`. Default value is `AES256`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The path to the source file being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique version ID value for the object, if bucket versioning is enabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing BucketObject Resource

Get an existing BucketObject resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/oss/#BucketObjectState">BucketObjectState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/oss/#BucketObject">BucketObject</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>acl=None<span class="p">, </span>bucket=None<span class="p">, </span>cache_control=None<span class="p">, </span>content=None<span class="p">, </span>content_disposition=None<span class="p">, </span>content_encoding=None<span class="p">, </span>content_length=None<span class="p">, </span>content_md5=None<span class="p">, </span>content_type=None<span class="p">, </span>etag=None<span class="p">, </span>expires=None<span class="p">, </span>key=None<span class="p">, </span>kms_key_id=None<span class="p">, </span>server_side_encryption=None<span class="p">, </span>source=None<span class="p">, </span>version_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetBucketObject<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketObjectState">BucketObjectState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketObject">BucketObject</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Oss.BucketObject.html">BucketObject</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Oss.BucketObjectState.html">BucketObjectState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/52284.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the bucket to put the file in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies caching behavior along the request/reply chain. Read [RFC2616 Cache-Control](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The literal content being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies presentational information for the object. Read [RFC2616 Content-Disposition](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [RFC2616 Content-Encoding](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the content length of request.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The MD5 value of the content. Read [MD5](https://www.alibabacloud.com/help/doc-detail/31978.htm) for computing method.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the ETag generated for the object (an MD5 sum of the object content).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expires</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies expire date for the the request/response. Read [RFC2616 Expires](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the object once it is in the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the primary key managed by KMS. This parameter is valid when the value of `server_side_encryption` is set to KMS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Side<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies server-side encryption of the object in OSS. Valid values are `AES256`, `KMS`. Default value is `AES256`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path to the source file being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique version ID value for the object, if bucket versioning is enabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/52284.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket to put the file in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies caching behavior along the request/reply chain. Read [RFC2616 Cache-Control](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The literal content being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies presentational information for the object. Read [RFC2616 Content-Disposition](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [RFC2616 Content-Encoding](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the content length of request.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The MD5 value of the content. Read [MD5](https://www.alibabacloud.com/help/doc-detail/31978.htm) for computing method.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the ETag generated for the object (an MD5 sum of the object content).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expires</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies expire date for the the request/response. Read [RFC2616 Expires](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the object once it is in the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the primary key managed by KMS. This parameter is valid when the value of `server_side_encryption` is set to KMS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Side<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies server-side encryption of the object in OSS. Valid values are `AES256`, `KMS`. Default value is `AES256`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The path to the source file being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A unique version ID value for the object, if bucket versioning is enabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/52284.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the bucket to put the file in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cache<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies caching behavior along the request/reply chain. Read [RFC2616 Cache-Control](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The literal content being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies presentational information for the object. Read [RFC2616 Content-Disposition](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [RFC2616 Content-Encoding](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the content length of request.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The MD5 value of the content. Read [MD5](https://www.alibabacloud.com/help/doc-detail/31978.htm) for computing method.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the ETag generated for the object (an MD5 sum of the object content).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expires</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies expire date for the the request/response. Read [RFC2616 Expires](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the object once it is in the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the primary key managed by KMS. This parameter is valid when the value of `server_side_encryption` is set to KMS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Side<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies server-side encryption of the object in OSS. Valid values are `AES256`, `KMS`. Default value is `AES256`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The path to the source file being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique version ID value for the object, if bucket versioning is enabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/52284.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the bucket to put the file in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cache_<wbr>control</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies caching behavior along the request/reply chain. Read [RFC2616 Cache-Control](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The literal content being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>disposition</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies presentational information for the object. Read [RFC2616 Content-Disposition](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [RFC2616 Content-Encoding](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>length</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the content length of request.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>md5</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The MD5 value of the content. Read [MD5](https://www.alibabacloud.com/help/doc-detail/31978.htm) for computing method.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the ETag generated for the object (an MD5 sum of the object content).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expires</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies expire date for the the request/response. Read [RFC2616 Expires](https://www.ietf.org/rfc/rfc2616.txt) for further details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the object once it is in the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms_<wbr>key_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the primary key managed by KMS. This parameter is valid when the value of `server_side_encryption` is set to KMS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server_<wbr>side_<wbr>encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies server-side encryption of the object in OSS. Valid values are `AES256`, `KMS`. Default value is `AES256`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The path to the source file being uploaded to the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique version ID value for the object, if bucket versioning is enabled.
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

