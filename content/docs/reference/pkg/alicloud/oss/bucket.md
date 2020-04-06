
---
title: "Bucket"
block_external_search_index: true
---



Provides a resource to create a oss bucket and set its attribution.

> **NOTE:** The bucket namespace is shared by all users of the OSS system. Please set bucket name as unique as possible.

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/oss_bucket.html.markdown.



## Create a Bucket Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/oss/#Bucket">Bucket</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/oss/#BucketArgs">BucketArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Bucket</span><span class="p">(resource_name, opts=None, </span>acl=None<span class="p">, </span>bucket=None<span class="p">, </span>cors_rules=None<span class="p">, </span>force_destroy=None<span class="p">, </span>lifecycle_rules=None<span class="p">, </span>logging=None<span class="p">, </span>logging_isenable=None<span class="p">, </span>policy=None<span class="p">, </span>referer_config=None<span class="p">, </span>server_side_encryption_rule=None<span class="p">, </span>storage_class=None<span class="p">, </span>tags=None<span class="p">, </span>versioning=None<span class="p">, </span>website=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewBucket<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketArgs">BucketArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#Bucket">Bucket</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Oss.Bucket.html">Bucket</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Oss.BucketArgs.html">BucketArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/31898.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cors<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketcorsrule">List&lt;Bucket<wbr>Cors<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A rule of [Cross-Origin Resource Sharing](https://www.alibabacloud.com/help/doc-detail/31903.htm) (documented below). The items of core rule are no more than 10 for every OSS bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are not recoverable. Defaults to "false".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lifecycle<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecyclerule">List&lt;Bucket<wbr>Lifecycle<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A configuration of [object lifecycle management](https://www.alibabacloud.com/help/doc-detail/31904.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlogging">Bucket<wbr>Logging<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A Settings of [bucket logging](https://www.alibabacloud.com/help/doc-detail/31900.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Logging<wbr>Isenable</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}The flag of using logging enable container. Defaults true.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Deprecated from 1.37.0. When `logging` is set, the bucket logging will be able.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Json format text of bucket policy [bucket policy management](https://www.alibabacloud.com/help/doc-detail/100680.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Referer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketrefererconfig">Bucket<wbr>Referer<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The configuration of [referer](https://www.alibabacloud.com/help/doc-detail/31901.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Side<wbr>Encryption<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketserversideencryptionrule">Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A configuration of server-side encryption (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`, `Standard`. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the bucket. The items are no more than 10 for a bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Versioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketversioning">Bucket<wbr>Versioning<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A state of versioning (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Website</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketwebsite">Bucket<wbr>Website<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A website object(documented below).
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
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/31898.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cors<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketcorsrule">[]Bucket<wbr>Cors<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A rule of [Cross-Origin Resource Sharing](https://www.alibabacloud.com/help/doc-detail/31903.htm) (documented below). The items of core rule are no more than 10 for every OSS bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are not recoverable. Defaults to "false".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lifecycle<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecyclerule">[]Bucket<wbr>Lifecycle<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A configuration of [object lifecycle management](https://www.alibabacloud.com/help/doc-detail/31904.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlogging">*Bucket<wbr>Logging</a></span>
    </dt>
    <dd>{{% md %}}A Settings of [bucket logging](https://www.alibabacloud.com/help/doc-detail/31900.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Logging<wbr>Isenable</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}The flag of using logging enable container. Defaults true.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Deprecated from 1.37.0. When `logging` is set, the bucket logging will be able.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Json format text of bucket policy [bucket policy management](https://www.alibabacloud.com/help/doc-detail/100680.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Referer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketrefererconfig">*Bucket<wbr>Referer<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The configuration of [referer](https://www.alibabacloud.com/help/doc-detail/31901.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Side<wbr>Encryption<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketserversideencryptionrule">*Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A configuration of server-side encryption (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`, `Standard`. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the bucket. The items are no more than 10 for a bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Versioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketversioning">*Bucket<wbr>Versioning</a></span>
    </dt>
    <dd>{{% md %}}A state of versioning (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Website</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketwebsite">*Bucket<wbr>Website</a></span>
    </dt>
    <dd>{{% md %}}A website object(documented below).
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
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/31898.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cors<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketcorsrule">Bucket<wbr>Cors<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}A rule of [Cross-Origin Resource Sharing](https://www.alibabacloud.com/help/doc-detail/31903.htm) (documented below). The items of core rule are no more than 10 for every OSS bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are not recoverable. Defaults to "false".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lifecycle<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecyclerule">Bucket<wbr>Lifecycle<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}A configuration of [object lifecycle management](https://www.alibabacloud.com/help/doc-detail/31904.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlogging">Bucket<wbr>Logging?</a></span>
    </dt>
    <dd>{{% md %}}A Settings of [bucket logging](https://www.alibabacloud.com/help/doc-detail/31900.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>logging<wbr>Isenable</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}The flag of using logging enable container. Defaults true.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Deprecated from 1.37.0. When `logging` is set, the bucket logging will be able.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Json format text of bucket policy [bucket policy management](https://www.alibabacloud.com/help/doc-detail/100680.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>referer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketrefererconfig">Bucket<wbr>Referer<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The configuration of [referer](https://www.alibabacloud.com/help/doc-detail/31901.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Side<wbr>Encryption<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketserversideencryptionrule">Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule?</a></span>
    </dt>
    <dd>{{% md %}}A configuration of server-side encryption (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`, `Standard`. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the bucket. The items are no more than 10 for a bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>versioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketversioning">Bucket<wbr>Versioning?</a></span>
    </dt>
    <dd>{{% md %}}A state of versioning (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>website</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketwebsite">Bucket<wbr>Website?</a></span>
    </dt>
    <dd>{{% md %}}A website object(documented below).
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
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/31898.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cors_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketcorsrule">List[Bucket<wbr>Cors<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A rule of [Cross-Origin Resource Sharing](https://www.alibabacloud.com/help/doc-detail/31903.htm) (documented below). The items of core rule are no more than 10 for every OSS bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force_<wbr>destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are not recoverable. Defaults to "false".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lifecycle_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecyclerule">List[Bucket<wbr>Lifecycle<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A configuration of [object lifecycle management](https://www.alibabacloud.com/help/doc-detail/31904.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlogging">Dict[Bucket<wbr>Logging]</a></span>
    </dt>
    <dd>{{% md %}}A Settings of [bucket logging](https://www.alibabacloud.com/help/doc-detail/31900.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>logging_<wbr>isenable</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The flag of using logging enable container. Defaults true.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Deprecated from 1.37.0. When `logging` is set, the bucket logging will be able.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Json format text of bucket policy [bucket policy management](https://www.alibabacloud.com/help/doc-detail/100680.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>referer_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketrefererconfig">Dict[Bucket<wbr>Referer<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The configuration of [referer](https://www.alibabacloud.com/help/doc-detail/31901.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server_<wbr>side_<wbr>encryption_<wbr>rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketserversideencryptionrule">Dict[Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A configuration of server-side encryption (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`, `Standard`. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the bucket. The items are no more than 10 for a bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>versioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketversioning">Dict[Bucket<wbr>Versioning]</a></span>
    </dt>
    <dd>{{% md %}}A state of versioning (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>website</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketwebsite">Dict[Bucket<wbr>Website]</a></span>
    </dt>
    <dd>{{% md %}}A website object(documented below).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Bucket Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/31898.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cors<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketcorsrule">List&lt;Bucket<wbr>Cors<wbr>Rule&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A rule of [Cross-Origin Resource Sharing](https://www.alibabacloud.com/help/doc-detail/31903.htm) (documented below). The items of core rule are no more than 10 for every OSS bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Creation<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The creation date of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Extranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The extranet access endpoint of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Force<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are not recoverable. Defaults to "false".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Intranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The intranet access endpoint of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lifecycle<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecyclerule">List&lt;Bucket<wbr>Lifecycle<wbr>Rule&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A configuration of [object lifecycle management](https://www.alibabacloud.com/help/doc-detail/31904.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlogging">Bucket<wbr>Logging?</a></span>
    </dt>
    <dd>{{% md %}}A Settings of [bucket logging](https://www.alibabacloud.com/help/doc-detail/31900.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Logging<wbr>Isenable</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}The flag of using logging enable container. Defaults true.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Deprecated from 1.37.0. When `logging` is set, the bucket logging will be able.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Owner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The bucket owner.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Json format text of bucket policy [bucket policy management](https://www.alibabacloud.com/help/doc-detail/100680.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Referer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketrefererconfig">Bucket<wbr>Referer<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The configuration of [referer](https://www.alibabacloud.com/help/doc-detail/31901.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Server<wbr>Side<wbr>Encryption<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketserversideencryptionrule">Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule?</a></span>
    </dt>
    <dd>{{% md %}}A configuration of server-side encryption (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`, `Standard`. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the bucket. The items are no more than 10 for a bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Versioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketversioning">Bucket<wbr>Versioning?</a></span>
    </dt>
    <dd>{{% md %}}A state of versioning (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Website</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketwebsite">Bucket<wbr>Website?</a></span>
    </dt>
    <dd>{{% md %}}A website object(documented below).
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
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/31898.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cors<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketcorsrule">[]Bucket<wbr>Cors<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A rule of [Cross-Origin Resource Sharing](https://www.alibabacloud.com/help/doc-detail/31903.htm) (documented below). The items of core rule are no more than 10 for every OSS bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Creation<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The creation date of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Extranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The extranet access endpoint of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Force<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are not recoverable. Defaults to "false".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Intranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The intranet access endpoint of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lifecycle<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecyclerule">[]Bucket<wbr>Lifecycle<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A configuration of [object lifecycle management](https://www.alibabacloud.com/help/doc-detail/31904.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlogging">*Bucket<wbr>Logging</a></span>
    </dt>
    <dd>{{% md %}}A Settings of [bucket logging](https://www.alibabacloud.com/help/doc-detail/31900.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Logging<wbr>Isenable</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}The flag of using logging enable container. Defaults true.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Deprecated from 1.37.0. When `logging` is set, the bucket logging will be able.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Owner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The bucket owner.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Json format text of bucket policy [bucket policy management](https://www.alibabacloud.com/help/doc-detail/100680.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Referer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketrefererconfig">*Bucket<wbr>Referer<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The configuration of [referer](https://www.alibabacloud.com/help/doc-detail/31901.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Server<wbr>Side<wbr>Encryption<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketserversideencryptionrule">*Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A configuration of server-side encryption (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`, `Standard`. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the bucket. The items are no more than 10 for a bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Versioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketversioning">*Bucket<wbr>Versioning</a></span>
    </dt>
    <dd>{{% md %}}A state of versioning (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Website</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketwebsite">*Bucket<wbr>Website</a></span>
    </dt>
    <dd>{{% md %}}A website object(documented below).
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
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/31898.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cors<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketcorsrule">Bucket<wbr>Cors<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}A rule of [Cross-Origin Resource Sharing](https://www.alibabacloud.com/help/doc-detail/31903.htm) (documented below). The items of core rule are no more than 10 for every OSS bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>creation<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The creation date of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>extranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The extranet access endpoint of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>force<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are not recoverable. Defaults to "false".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>intranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The intranet access endpoint of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lifecycle<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecyclerule">Bucket<wbr>Lifecycle<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}A configuration of [object lifecycle management](https://www.alibabacloud.com/help/doc-detail/31904.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlogging">Bucket<wbr>Logging?</a></span>
    </dt>
    <dd>{{% md %}}A Settings of [bucket logging](https://www.alibabacloud.com/help/doc-detail/31900.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>logging<wbr>Isenable</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}The flag of using logging enable container. Defaults true.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Deprecated from 1.37.0. When `logging` is set, the bucket logging will be able.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>owner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The bucket owner.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Json format text of bucket policy [bucket policy management](https://www.alibabacloud.com/help/doc-detail/100680.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>referer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketrefererconfig">Bucket<wbr>Referer<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The configuration of [referer](https://www.alibabacloud.com/help/doc-detail/31901.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>server<wbr>Side<wbr>Encryption<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketserversideencryptionrule">Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule?</a></span>
    </dt>
    <dd>{{% md %}}A configuration of server-side encryption (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`, `Standard`. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the bucket. The items are no more than 10 for a bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>versioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketversioning">Bucket<wbr>Versioning?</a></span>
    </dt>
    <dd>{{% md %}}A state of versioning (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>website</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketwebsite">Bucket<wbr>Website?</a></span>
    </dt>
    <dd>{{% md %}}A website object(documented below).
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
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/31898.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cors_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketcorsrule">List[Bucket<wbr>Cors<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A rule of [Cross-Origin Resource Sharing](https://www.alibabacloud.com/help/doc-detail/31903.htm) (documented below). The items of core rule are no more than 10 for every OSS bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>creation_<wbr>date</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The creation date of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>extranet_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The extranet access endpoint of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>force_<wbr>destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are not recoverable. Defaults to "false".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>intranet_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The intranet access endpoint of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lifecycle_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecyclerule">List[Bucket<wbr>Lifecycle<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A configuration of [object lifecycle management](https://www.alibabacloud.com/help/doc-detail/31904.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlogging">Dict[Bucket<wbr>Logging]</a></span>
    </dt>
    <dd>{{% md %}}A Settings of [bucket logging](https://www.alibabacloud.com/help/doc-detail/31900.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>logging_<wbr>isenable</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The flag of using logging enable container. Defaults true.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Deprecated from 1.37.0. When `logging` is set, the bucket logging will be able.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>owner</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The bucket owner.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Json format text of bucket policy [bucket policy management](https://www.alibabacloud.com/help/doc-detail/100680.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>referer_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketrefererconfig">Dict[Bucket<wbr>Referer<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The configuration of [referer](https://www.alibabacloud.com/help/doc-detail/31901.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>server_<wbr>side_<wbr>encryption_<wbr>rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketserversideencryptionrule">Dict[Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A configuration of server-side encryption (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`, `Standard`. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the bucket. The items are no more than 10 for a bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>versioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketversioning">Dict[Bucket<wbr>Versioning]</a></span>
    </dt>
    <dd>{{% md %}}A state of versioning (documented below).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>website</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketwebsite">Dict[Bucket<wbr>Website]</a></span>
    </dt>
    <dd>{{% md %}}A website object(documented below).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Bucket Resource

Get an existing Bucket resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/oss/#BucketState">BucketState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/oss/#Bucket">Bucket</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>acl=None<span class="p">, </span>bucket=None<span class="p">, </span>cors_rules=None<span class="p">, </span>creation_date=None<span class="p">, </span>extranet_endpoint=None<span class="p">, </span>force_destroy=None<span class="p">, </span>intranet_endpoint=None<span class="p">, </span>lifecycle_rules=None<span class="p">, </span>location=None<span class="p">, </span>logging=None<span class="p">, </span>logging_isenable=None<span class="p">, </span>owner=None<span class="p">, </span>policy=None<span class="p">, </span>referer_config=None<span class="p">, </span>server_side_encryption_rule=None<span class="p">, </span>storage_class=None<span class="p">, </span>tags=None<span class="p">, </span>versioning=None<span class="p">, </span>website=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetBucket<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketState">BucketState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#Bucket">Bucket</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Oss.Bucket.html">Bucket</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Oss.BucketState.html">BucketState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/31898.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cors<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketcorsrule">List&lt;Bucket<wbr>Cors<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A rule of [Cross-Origin Resource Sharing](https://www.alibabacloud.com/help/doc-detail/31903.htm) (documented below). The items of core rule are no more than 10 for every OSS bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The creation date of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Extranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The extranet access endpoint of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are not recoverable. Defaults to "false".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Intranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The intranet access endpoint of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lifecycle<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecyclerule">List&lt;Bucket<wbr>Lifecycle<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A configuration of [object lifecycle management](https://www.alibabacloud.com/help/doc-detail/31904.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlogging">Bucket<wbr>Logging<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A Settings of [bucket logging](https://www.alibabacloud.com/help/doc-detail/31900.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Logging<wbr>Isenable</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}The flag of using logging enable container. Defaults true.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Deprecated from 1.37.0. When `logging` is set, the bucket logging will be able.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Owner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The bucket owner.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Json format text of bucket policy [bucket policy management](https://www.alibabacloud.com/help/doc-detail/100680.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Referer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketrefererconfig">Bucket<wbr>Referer<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The configuration of [referer](https://www.alibabacloud.com/help/doc-detail/31901.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Side<wbr>Encryption<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketserversideencryptionrule">Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A configuration of server-side encryption (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`, `Standard`. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the bucket. The items are no more than 10 for a bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Versioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketversioning">Bucket<wbr>Versioning<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A state of versioning (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Website</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketwebsite">Bucket<wbr>Website<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A website object(documented below).
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
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/31898.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cors<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketcorsrule">[]Bucket<wbr>Cors<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A rule of [Cross-Origin Resource Sharing](https://www.alibabacloud.com/help/doc-detail/31903.htm) (documented below). The items of core rule are no more than 10 for every OSS bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The creation date of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Extranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The extranet access endpoint of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are not recoverable. Defaults to "false".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Intranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The intranet access endpoint of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lifecycle<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecyclerule">[]Bucket<wbr>Lifecycle<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A configuration of [object lifecycle management](https://www.alibabacloud.com/help/doc-detail/31904.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The location of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlogging">*Bucket<wbr>Logging</a></span>
    </dt>
    <dd>{{% md %}}A Settings of [bucket logging](https://www.alibabacloud.com/help/doc-detail/31900.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Logging<wbr>Isenable</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}The flag of using logging enable container. Defaults true.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Deprecated from 1.37.0. When `logging` is set, the bucket logging will be able.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Owner</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The bucket owner.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Json format text of bucket policy [bucket policy management](https://www.alibabacloud.com/help/doc-detail/100680.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Referer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketrefererconfig">*Bucket<wbr>Referer<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The configuration of [referer](https://www.alibabacloud.com/help/doc-detail/31901.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Side<wbr>Encryption<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketserversideencryptionrule">*Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A configuration of server-side encryption (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`, `Standard`. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the bucket. The items are no more than 10 for a bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Versioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketversioning">*Bucket<wbr>Versioning</a></span>
    </dt>
    <dd>{{% md %}}A state of versioning (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Website</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketwebsite">*Bucket<wbr>Website</a></span>
    </dt>
    <dd>{{% md %}}A website object(documented below).
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
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/31898.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cors<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketcorsrule">Bucket<wbr>Cors<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}A rule of [Cross-Origin Resource Sharing](https://www.alibabacloud.com/help/doc-detail/31903.htm) (documented below). The items of core rule are no more than 10 for every OSS bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>creation<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The creation date of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>extranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The extranet access endpoint of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are not recoverable. Defaults to "false".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>intranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The intranet access endpoint of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lifecycle<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecyclerule">Bucket<wbr>Lifecycle<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}A configuration of [object lifecycle management](https://www.alibabacloud.com/help/doc-detail/31904.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlogging">Bucket<wbr>Logging?</a></span>
    </dt>
    <dd>{{% md %}}A Settings of [bucket logging](https://www.alibabacloud.com/help/doc-detail/31900.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>logging<wbr>Isenable</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}The flag of using logging enable container. Defaults true.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Deprecated from 1.37.0. When `logging` is set, the bucket logging will be able.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>owner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The bucket owner.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Json format text of bucket policy [bucket policy management](https://www.alibabacloud.com/help/doc-detail/100680.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>referer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketrefererconfig">Bucket<wbr>Referer<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The configuration of [referer](https://www.alibabacloud.com/help/doc-detail/31901.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Side<wbr>Encryption<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketserversideencryptionrule">Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule?</a></span>
    </dt>
    <dd>{{% md %}}A configuration of server-side encryption (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`, `Standard`. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the bucket. The items are no more than 10 for a bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>versioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketversioning">Bucket<wbr>Versioning?</a></span>
    </dt>
    <dd>{{% md %}}A state of versioning (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>website</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketwebsite">Bucket<wbr>Website?</a></span>
    </dt>
    <dd>{{% md %}}A website object(documented below).
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
    <dd>{{% md %}}The [canned ACL](https://www.alibabacloud.com/help/doc-detail/31898.htm) to apply. Defaults to "private".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cors_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketcorsrule">List[Bucket<wbr>Cors<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A rule of [Cross-Origin Resource Sharing](https://www.alibabacloud.com/help/doc-detail/31903.htm) (documented below). The items of core rule are no more than 10 for every OSS bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>creation_<wbr>date</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The creation date of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>extranet_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The extranet access endpoint of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force_<wbr>destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are not recoverable. Defaults to "false".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>intranet_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The intranet access endpoint of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lifecycle_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecyclerule">List[Bucket<wbr>Lifecycle<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A configuration of [object lifecycle management](https://www.alibabacloud.com/help/doc-detail/31904.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlogging">Dict[Bucket<wbr>Logging]</a></span>
    </dt>
    <dd>{{% md %}}A Settings of [bucket logging](https://www.alibabacloud.com/help/doc-detail/31900.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>logging_<wbr>isenable</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The flag of using logging enable container. Defaults true.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Deprecated from 1.37.0. When `logging` is set, the bucket logging will be able.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>owner</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The bucket owner.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Json format text of bucket policy [bucket policy management](https://www.alibabacloud.com/help/doc-detail/100680.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>referer_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketrefererconfig">Dict[Bucket<wbr>Referer<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The configuration of [referer](https://www.alibabacloud.com/help/doc-detail/31901.htm) (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server_<wbr>side_<wbr>encryption_<wbr>rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketserversideencryptionrule">Dict[Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A configuration of server-side encryption (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`, `Standard`. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the bucket. The items are no more than 10 for a bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>versioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketversioning">Dict[Bucket<wbr>Versioning]</a></span>
    </dt>
    <dd>{{% md %}}A state of versioning (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>website</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketwebsite">Dict[Bucket<wbr>Website]</a></span>
    </dt>
    <dd>{{% md %}}A website object(documented below).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Bucket<wbr>Cors<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#BucketCorsRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#BucketCorsRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketCorsRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketCorsRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies which headers are allowed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Allowed<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}Specifies which methods are allowed. Can be GET, PUT, POST, DELETE or HEAD.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Allowed<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}Specifies which origins are allowed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expose<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies expose header in the response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Age<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Specifies time in seconds that browser can cache the response for a preflight request.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies which headers are allowed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Allowed<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies which methods are allowed. Can be GET, PUT, POST, DELETE or HEAD.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Allowed<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies which origins are allowed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expose<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies expose header in the response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Age<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Specifies time in seconds that browser can cache the response for a preflight request.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allowed<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies which headers are allowed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>allowed<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Specifies which methods are allowed. Can be GET, PUT, POST, DELETE or HEAD.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>allowed<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Specifies which origins are allowed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expose<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies expose header in the response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Age<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Specifies time in seconds that browser can cache the response for a preflight request.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allowed<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies which headers are allowed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>allowed<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies which methods are allowed. Can be GET, PUT, POST, DELETE or HEAD.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>allowed<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies which origins are allowed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expose<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies expose header in the response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Age<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Specifies time in seconds that browser can cache the response for a preflight request.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Bucket<wbr>Lifecycle<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#BucketLifecycleRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#BucketLifecycleRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketLifecycleRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketLifecycleRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies lifecycle rule status.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expirations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecycleruleexpiration">List&lt;Bucket<wbr>Lifecycle<wbr>Rule<wbr>Expiration<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Specifies a period in the object's expire (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique identifier for the rule. If omitted, OSS bucket will assign a unique name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Object key prefix identifying one or more objects to which the rule applies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Transitions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecycleruletransition">List&lt;Bucket<wbr>Lifecycle<wbr>Rule<wbr>Transition<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the time when an object is converted to the IA or archive storage class during a valid life cycle. (documented below).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies lifecycle rule status.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expirations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecycleruleexpiration">[]Bucket<wbr>Lifecycle<wbr>Rule<wbr>Expiration</a></span>
    </dt>
    <dd>{{% md %}}Specifies a period in the object's expire (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Unique identifier for the rule. If omitted, OSS bucket will assign a unique name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Object key prefix identifying one or more objects to which the rule applies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Transitions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecycleruletransition">[]Bucket<wbr>Lifecycle<wbr>Rule<wbr>Transition</a></span>
    </dt>
    <dd>{{% md %}}Specifies the time when an object is converted to the IA or archive storage class during a valid life cycle. (documented below).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Specifies lifecycle rule status.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expirations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecycleruleexpiration">Bucket<wbr>Lifecycle<wbr>Rule<wbr>Expiration[]?</a></span>
    </dt>
    <dd>{{% md %}}Specifies a period in the object's expire (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Unique identifier for the rule. If omitted, OSS bucket will assign a unique name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Object key prefix identifying one or more objects to which the rule applies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>transitions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecycleruletransition">Bucket<wbr>Lifecycle<wbr>Rule<wbr>Transition[]?</a></span>
    </dt>
    <dd>{{% md %}}Specifies the time when an object is converted to the IA or archive storage class during a valid life cycle. (documented below).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies lifecycle rule status.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expirations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecycleruleexpiration">List[Bucket<wbr>Lifecycle<wbr>Rule<wbr>Expiration]</a></span>
    </dt>
    <dd>{{% md %}}Specifies a period in the object's expire (documented below).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Unique identifier for the rule. If omitted, OSS bucket will assign a unique name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Object key prefix identifying one or more objects to which the rule applies.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>transitions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#bucketlifecycleruletransition">List[Bucket<wbr>Lifecycle<wbr>Rule<wbr>Transition]</a></span>
    </dt>
    <dd>{{% md %}}Specifies the time when an object is converted to the IA or archive storage class during a valid life cycle. (documented below).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Expiration</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#BucketLifecycleRuleExpiration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#BucketLifecycleRuleExpiration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketLifecycleRuleExpirationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketLifecycleRuleExpirationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the date after which you want the corresponding action to take effect. The value obeys ISO8601 format like `2017-03-09`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Specifies the number of days after object creation when the specific rule action takes effect.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the date after which you want the corresponding action to take effect. The value obeys ISO8601 format like `2017-03-09`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Specifies the number of days after object creation when the specific rule action takes effect.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the date after which you want the corresponding action to take effect. The value obeys ISO8601 format like `2017-03-09`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>days</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Specifies the number of days after object creation when the specific rule action takes effect.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>date</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the date after which you want the corresponding action to take effect. The value obeys ISO8601 format like `2017-03-09`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>days</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Specifies the number of days after object creation when the specific rule action takes effect.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Transition</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#BucketLifecycleRuleTransition">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#BucketLifecycleRuleTransition">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketLifecycleRuleTransitionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketLifecycleRuleTransitionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Created<wbr>Before<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the time before which the rules take effect. The date must conform to the ISO8601 format and always be UTC 00:00. For example: 2002-10-11T00:00:00.000Z indicates that objects updated before 2002-10-11T00:00:00.000Z are deleted or converted to another storage class, and objects updated after this time (including this time) are not deleted or converted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Specifies the number of days after object creation when the specific rule action takes effect.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`, `Standard`. 
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Created<wbr>Before<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the time before which the rules take effect. The date must conform to the ISO8601 format and always be UTC 00:00. For example: 2002-10-11T00:00:00.000Z indicates that objects updated before 2002-10-11T00:00:00.000Z are deleted or converted to another storage class, and objects updated after this time (including this time) are not deleted or converted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Specifies the number of days after object creation when the specific rule action takes effect.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`, `Standard`. 
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>created<wbr>Before<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the time before which the rules take effect. The date must conform to the ISO8601 format and always be UTC 00:00. For example: 2002-10-11T00:00:00.000Z indicates that objects updated before 2002-10-11T00:00:00.000Z are deleted or converted to another storage class, and objects updated after this time (including this time) are not deleted or converted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>days</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Specifies the number of days after object creation when the specific rule action takes effect.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`, `Standard`. 
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>created<wbr>Before<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the time before which the rules take effect. The date must conform to the ISO8601 format and always be UTC 00:00. For example: 2002-10-11T00:00:00.000Z indicates that objects updated before 2002-10-11T00:00:00.000Z are deleted or converted to another storage class, and objects updated after this time (including this time) are not deleted or converted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>days</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Specifies the number of days after object creation when the specific rule action takes effect.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`, `Standard`. 
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Bucket<wbr>Logging</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#BucketLogging">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#BucketLogging">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketLoggingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketLoggingOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket that will receive the log objects.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To specify a key prefix for log objects.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket that will receive the log objects.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To specify a key prefix for log objects.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>target<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket that will receive the log objects.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To specify a key prefix for log objects.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>target<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the bucket that will receive the log objects.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To specify a key prefix for log objects.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Bucket<wbr>Referer<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#BucketRefererConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#BucketRefererConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketRefererConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketRefererConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Empty</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Allows referer to be empty. Defaults true.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Referers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The list of referer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Empty</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Allows referer to be empty. Defaults true.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Referers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of referer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Empty</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Allows referer to be empty. Defaults true.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>referers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The list of referer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Empty</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allows referer to be empty. Defaults true.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>referers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of referer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#BucketServerSideEncryptionRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#BucketServerSideEncryptionRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketServerSideEncryptionRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketServerSideEncryptionRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Sse<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The server-side encryption algorithm to use. Possible values: `AES256` and `KMS`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Sse<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The server-side encryption algorithm to use. Possible values: `AES256` and `KMS`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>sse<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The server-side encryption algorithm to use. Possible values: `AES256` and `KMS`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>sse<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The server-side encryption algorithm to use. Possible values: `AES256` and `KMS`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Bucket<wbr>Versioning</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#BucketVersioning">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#BucketVersioning">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketVersioningArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketVersioningOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the versioning state of a bucket. Valid values: `Enabled` and `Suspended`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the versioning state of a bucket. Valid values: `Enabled` and `Suspended`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the versioning state of a bucket. Valid values: `Enabled` and `Suspended`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the versioning state of a bucket. Valid values: `Enabled` and `Suspended`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Bucket<wbr>Website</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#BucketWebsite">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#BucketWebsite">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketWebsiteArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss?tab=doc#BucketWebsiteOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Error<wbr>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An absolute path to the document to return in case of a 4XX error.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Index<wbr>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Alicloud OSS returns this index document when requests are made to the root domain or any of the subfolders.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Error<wbr>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An absolute path to the document to return in case of a 4XX error.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Index<wbr>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Alicloud OSS returns this index document when requests are made to the root domain or any of the subfolders.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>error<wbr>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An absolute path to the document to return in case of a 4XX error.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>index<wbr>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Alicloud OSS returns this index document when requests are made to the root domain or any of the subfolders.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>error<wbr>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An absolute path to the document to return in case of a 4XX error.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>index<wbr>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Alicloud OSS returns this index document when requests are made to the root domain or any of the subfolders.
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

