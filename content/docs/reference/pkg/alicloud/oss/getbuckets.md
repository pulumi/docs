
---
title: "GetBuckets"
block_external_search_index: true
---



This data source provides the OSS buckets of the current Alibaba Cloud user.

{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as alicloud from "@pulumi/alicloud";

const ossBucketsDs = pulumi.output(alicloud.oss.getBuckets({
    nameRegex: "sample_oss_bucket",
}, { async: true }));

export const firstOssBucketName = ossBucketsDs.buckets[0].name;
```

{{% /example %}}
{{% /examples %}}





## Using GetBuckets {#using}

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getBuckets<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/oss/#GetBucketsArgs">GetBucketsArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/oss/#GetBucketsResult">GetBucketsResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_buckets(</span>name_regex=None<span class="p">, </span>output_file=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupBuckets<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/v2/go/alicloud/oss?tab=doc#LookupBucketsArgs">LookupBucketsArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/v2/go/alicloud/oss?tab=doc#LookupBucketsResult">LookupBucketsResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetBuckets </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Oss.GetBucketsResult.html">GetBucketsResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.AliCloud.Oss.GetBucketsArgs.html">GetBucketsArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by bucket name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
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
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by bucket name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
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
        <span>name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by bucket name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output<wbr>File</span>
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
        <span>name_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by bucket name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetBuckets Result {#result}

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Buckets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucket">List&lt;Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Oss.<wbr>Outputs.<wbr>Get<wbr>Buckets<wbr>Bucket&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of buckets. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of bucket names. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Buckets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucket">[]Get<wbr>Buckets<wbr>Bucket</a></span>
    </dt>
    <dd>{{% md %}}A list of buckets. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}A list of bucket names. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>buckets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucket">Get<wbr>Buckets<wbr>Bucket[]</a></span>
    </dt>
    <dd>{{% md %}}A list of buckets. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}A list of bucket names. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>buckets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucket">List[Get<wbr>Buckets<wbr>Bucket]</a></span>
    </dt>
    <dd>{{% md %}}A list of buckets. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}A list of bucket names. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types


<h4 id="getbucketsbucket">Get<wbr>Buckets<wbr>Bucket</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetBucketsBucket">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/v2/go/alicloud/oss?tab=doc#GetBucketsBucket">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Bucket access control list. Possible values: `private`, `public-read` and `public-read-write`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cors<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketcorsrule">List&lt;Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Oss.<wbr>Inputs.<wbr>Get<wbr>Buckets<wbr>Bucket<wbr>Cors<wbr>Rule<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of CORS rule configurations. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Creation<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Bucket creation date.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Extranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Internet domain name for accessing the bucket from outside.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Intranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Intranet domain name for accessing the bucket from an ECS instance in the same region.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Lifecycle<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketlifecyclerule">List&lt;Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Oss.<wbr>Inputs.<wbr>Get<wbr>Buckets<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list CORS of lifecycle configurations. When Lifecycle is enabled, OSS automatically deletes the objects or transitions the objects (to another storage class) corresponding the lifecycle rules on a regular basis. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Region of the data center where the bucket is located.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketlogging">Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Oss.<wbr>Inputs.<wbr>Get<wbr>Buckets<wbr>Bucket<wbr>Logging<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A list of one element containing configuration parameters used for storing access log information. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Bucket name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Owner</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Bucket owner.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Referer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketrefererconfig">Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Oss.<wbr>Inputs.<wbr>Get<wbr>Buckets<wbr>Bucket<wbr>Referer<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A list of one element containing referer configuration. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>Side<wbr>Encryption<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketserversideencryptionrule">Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Oss.<wbr>Inputs.<wbr>Get<wbr>Buckets<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A configuration of default encryption for a bucket. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Object storage type. Possible values: `Standard`, `IA` and `Archive`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;</span>
    </dt>
    <dd>{{% md %}}A mapping of tags.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Versioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketversioning">Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Oss.<wbr>Inputs.<wbr>Get<wbr>Buckets<wbr>Bucket<wbr>Versioning<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}If present , the versioning state has been set on the bucket. It contains the following attribute.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Website</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketwebsite">Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Oss.<wbr>Inputs.<wbr>Get<wbr>Buckets<wbr>Bucket<wbr>Website<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A list of one element containing configuration parameters used when the bucket is used as a website. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policy</span>
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
        <span>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Bucket access control list. Possible values: `private`, `public-read` and `public-read-write`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cors<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketcorsrule">[]Get<wbr>Buckets<wbr>Bucket<wbr>Cors<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A list of CORS rule configurations. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Creation<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Bucket creation date.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Extranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Internet domain name for accessing the bucket from outside.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Intranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Intranet domain name for accessing the bucket from an ECS instance in the same region.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Lifecycle<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketlifecyclerule">[]Get<wbr>Buckets<wbr>Bucket<wbr>Lifecycle<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A list CORS of lifecycle configurations. When Lifecycle is enabled, OSS automatically deletes the objects or transitions the objects (to another storage class) corresponding the lifecycle rules on a regular basis. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Region of the data center where the bucket is located.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketlogging">Get<wbr>Buckets<wbr>Bucket<wbr>Logging</a></span>
    </dt>
    <dd>{{% md %}}A list of one element containing configuration parameters used for storing access log information. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Bucket name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Owner</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Bucket owner.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Referer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketrefererconfig">Get<wbr>Buckets<wbr>Bucket<wbr>Referer<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A list of one element containing referer configuration. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>Side<wbr>Encryption<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketserversideencryptionrule">Get<wbr>Buckets<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A configuration of default encryption for a bucket. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Object storage type. Possible values: `Standard`, `IA` and `Archive`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Versioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketversioning">Get<wbr>Buckets<wbr>Bucket<wbr>Versioning</a></span>
    </dt>
    <dd>{{% md %}}If present , the versioning state has been set on the bucket. It contains the following attribute.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Website</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketwebsite">Get<wbr>Buckets<wbr>Bucket<wbr>Website</a></span>
    </dt>
    <dd>{{% md %}}A list of one element containing configuration parameters used when the bucket is used as a website. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policy</span>
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
        <span>acl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Bucket access control list. Possible values: `private`, `public-read` and `public-read-write`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cors<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketcorsrule">Get<wbr>Buckets<wbr>Bucket<wbr>Cors<wbr>Rule[]</a></span>
    </dt>
    <dd>{{% md %}}A list of CORS rule configurations. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>creation<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Bucket creation date.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>extranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Internet domain name for accessing the bucket from outside.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>intranet<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Intranet domain name for accessing the bucket from an ECS instance in the same region.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>lifecycle<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketlifecyclerule">Get<wbr>Buckets<wbr>Bucket<wbr>Lifecycle<wbr>Rule[]</a></span>
    </dt>
    <dd>{{% md %}}A list CORS of lifecycle configurations. When Lifecycle is enabled, OSS automatically deletes the objects or transitions the objects (to another storage class) corresponding the lifecycle rules on a regular basis. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Region of the data center where the bucket is located.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketlogging">Get<wbr>Buckets<wbr>Bucket<wbr>Logging</a></span>
    </dt>
    <dd>{{% md %}}A list of one element containing configuration parameters used for storing access log information. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Bucket name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>owner</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Bucket owner.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>referer<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketrefererconfig">Get<wbr>Buckets<wbr>Bucket<wbr>Referer<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A list of one element containing referer configuration. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server<wbr>Side<wbr>Encryption<wbr>Rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketserversideencryptionrule">Get<wbr>Buckets<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}A configuration of default encryption for a bucket. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Object storage type. Possible values: `Standard`, `IA` and `Archive`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>versioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketversioning">Get<wbr>Buckets<wbr>Bucket<wbr>Versioning</a></span>
    </dt>
    <dd>{{% md %}}If present , the versioning state has been set on the bucket. It contains the following attribute.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>website</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketwebsite">Get<wbr>Buckets<wbr>Bucket<wbr>Website</a></span>
    </dt>
    <dd>{{% md %}}A list of one element containing configuration parameters used when the bucket is used as a website. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policy</span>
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
        <span>acl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Bucket access control list. Possible values: `private`, `public-read` and `public-read-write`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cors_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketcorsrule">List[Get<wbr>Buckets<wbr>Bucket<wbr>Cors<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A list of CORS rule configurations. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>creation_<wbr>date</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Bucket creation date.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>extranet_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Internet domain name for accessing the bucket from outside.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>intranet_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Intranet domain name for accessing the bucket from an ECS instance in the same region.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>lifecycle_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketlifecyclerule">List[Get<wbr>Buckets<wbr>Bucket<wbr>Lifecycle<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A list CORS of lifecycle configurations. When Lifecycle is enabled, OSS automatically deletes the objects or transitions the objects (to another storage class) corresponding the lifecycle rules on a regular basis. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Region of the data center where the bucket is located.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketlogging">Dict[Get<wbr>Buckets<wbr>Bucket<wbr>Logging]</a></span>
    </dt>
    <dd>{{% md %}}A list of one element containing configuration parameters used for storing access log information. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Bucket name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>owner</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Bucket owner.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>referer_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketrefererconfig">Dict[Get<wbr>Buckets<wbr>Bucket<wbr>Referer<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A list of one element containing referer configuration. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server_<wbr>side_<wbr>encryption_<wbr>rule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketserversideencryptionrule">Dict[Get<wbr>Buckets<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}A configuration of default encryption for a bucket. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Object storage type. Possible values: `Standard`, `IA` and `Archive`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>versioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketversioning">Dict[Get<wbr>Buckets<wbr>Bucket<wbr>Versioning]</a></span>
    </dt>
    <dd>{{% md %}}If present , the versioning state has been set on the bucket. It contains the following attribute.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>website</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketwebsite">Dict[Get<wbr>Buckets<wbr>Bucket<wbr>Website]</a></span>
    </dt>
    <dd>{{% md %}}A list of one element containing configuration parameters used when the bucket is used as a website. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getbucketsbucketcorsrule">Get<wbr>Buckets<wbr>Bucket<wbr>Cors<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetBucketsBucketCorsRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/v2/go/alicloud/oss?tab=doc#GetBucketsBucketCorsRule">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Allowed<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}Control whether the headers specified by Access-Control-Request-Headers in the OPTIONS prefetch command are allowed. Each header specified by Access-Control-Request-Headers must match a value in AllowedHeader. Each rule allows up to one wildcard “*” .
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Allowed<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}Specify the allowed methods for cross-domain requests. Possible values: `GET`, `PUT`, `DELETE`, `POST` and `HEAD`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Allowed<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The origins allowed for cross-domain requests. Multiple elements can be used to specify multiple allowed origins. Each rule allows up to one wildcard "\*". If "\*" is specified, cross-domain requests of all origins are allowed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Expose<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}Specify the response headers allowing users to access from an application (for example, a Javascript XMLHttpRequest object). The wildcard "\*" is not allowed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Age<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Specify the cache time for the returned result of a browser prefetch (OPTIONS) request to a specific resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Allowed<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}Control whether the headers specified by Access-Control-Request-Headers in the OPTIONS prefetch command are allowed. Each header specified by Access-Control-Request-Headers must match a value in AllowedHeader. Each rule allows up to one wildcard “*” .
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Allowed<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}Specify the allowed methods for cross-domain requests. Possible values: `GET`, `PUT`, `DELETE`, `POST` and `HEAD`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Allowed<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The origins allowed for cross-domain requests. Multiple elements can be used to specify multiple allowed origins. Each rule allows up to one wildcard "\*". If "\*" is specified, cross-domain requests of all origins are allowed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Expose<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}Specify the response headers allowing users to access from an application (for example, a Javascript XMLHttpRequest object). The wildcard "\*" is not allowed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Age<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Specify the cache time for the returned result of a browser prefetch (OPTIONS) request to a specific resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>allowed<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}Control whether the headers specified by Access-Control-Request-Headers in the OPTIONS prefetch command are allowed. Each header specified by Access-Control-Request-Headers must match a value in AllowedHeader. Each rule allows up to one wildcard “*” .
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>allowed<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}Specify the allowed methods for cross-domain requests. Possible values: `GET`, `PUT`, `DELETE`, `POST` and `HEAD`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>allowed<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The origins allowed for cross-domain requests. Multiple elements can be used to specify multiple allowed origins. Each rule allows up to one wildcard "\*". If "\*" is specified, cross-domain requests of all origins are allowed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>expose<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}Specify the response headers allowing users to access from an application (for example, a Javascript XMLHttpRequest object). The wildcard "\*" is not allowed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Age<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Specify the cache time for the returned result of a browser prefetch (OPTIONS) request to a specific resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>allowed<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}Control whether the headers specified by Access-Control-Request-Headers in the OPTIONS prefetch command are allowed. Each header specified by Access-Control-Request-Headers must match a value in AllowedHeader. Each rule allows up to one wildcard “*” .
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>allowed<wbr>Methods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}Specify the allowed methods for cross-domain requests. Possible values: `GET`, `PUT`, `DELETE`, `POST` and `HEAD`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>allowed<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The origins allowed for cross-domain requests. Multiple elements can be used to specify multiple allowed origins. Each rule allows up to one wildcard "\*". If "\*" is specified, cross-domain requests of all origins are allowed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>expose<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}Specify the response headers allowing users to access from an application (for example, a Javascript XMLHttpRequest object). The wildcard "\*" is not allowed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Age<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Specify the cache time for the returned result of a browser prefetch (OPTIONS) request to a specific resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getbucketsbucketlifecyclerule">Get<wbr>Buckets<wbr>Bucket<wbr>Lifecycle<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetBucketsBucketLifecycleRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/v2/go/alicloud/oss?tab=doc#GetBucketsBucketLifecycleRule">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicate whether the rule is enabled or not.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketlifecycleruleexpiration">Pulumi.<wbr>Ali<wbr>Cloud.<wbr>Oss.<wbr>Inputs.<wbr>Get<wbr>Buckets<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Expiration<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A list of one element containing expiration attributes of an object. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Unique ID of the rule.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Prefix applicable to a rule. Only those objects with a matching prefix can be affected by the rule.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicate whether the rule is enabled or not.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketlifecycleruleexpiration">Get<wbr>Buckets<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Expiration</a></span>
    </dt>
    <dd>{{% md %}}A list of one element containing expiration attributes of an object. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Unique ID of the rule.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Prefix applicable to a rule. Only those objects with a matching prefix can be affected by the rule.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Indicate whether the rule is enabled or not.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketlifecycleruleexpiration">Get<wbr>Buckets<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Expiration</a></span>
    </dt>
    <dd>{{% md %}}A list of one element containing expiration attributes of an object. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Unique ID of the rule.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Prefix applicable to a rule. Only those objects with a matching prefix can be affected by the rule.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicate whether the rule is enabled or not.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getbucketsbucketlifecycleruleexpiration">Dict[Get<wbr>Buckets<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Expiration]</a></span>
    </dt>
    <dd>{{% md %}}A list of one element containing expiration attributes of an object. It contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Unique ID of the rule.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Prefix applicable to a rule. Only those objects with a matching prefix can be affected by the rule.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getbucketsbucketlifecycleruleexpiration">Get<wbr>Buckets<wbr>Bucket<wbr>Lifecycle<wbr>Rule<wbr>Expiration</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetBucketsBucketLifecycleRuleExpiration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/v2/go/alicloud/oss?tab=doc#GetBucketsBucketLifecycleRuleExpiration">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Date after which the rule to take effect. The format is like 2017-03-09.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Indicate the number of days after the last object update until the rules take effect.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Date after which the rule to take effect. The format is like 2017-03-09.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Indicate the number of days after the last object update until the rules take effect.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>date</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Date after which the rule to take effect. The format is like 2017-03-09.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Indicate the number of days after the last object update until the rules take effect.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>date</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Date after which the rule to take effect. The format is like 2017-03-09.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Indicate the number of days after the last object update until the rules take effect.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getbucketsbucketlogging">Get<wbr>Buckets<wbr>Bucket<wbr>Logging</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetBucketsBucketLogging">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/v2/go/alicloud/oss?tab=doc#GetBucketsBucketLogging">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Bucket for storing access logs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Prefix of the saved access log file paths.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Bucket for storing access logs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Prefix of the saved access log file paths.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>target<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Bucket for storing access logs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>target<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Prefix of the saved access log file paths.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>target<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Bucket for storing access logs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>target<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Prefix of the saved access log file paths.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getbucketsbucketrefererconfig">Get<wbr>Buckets<wbr>Bucket<wbr>Referer<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetBucketsBucketRefererConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/v2/go/alicloud/oss?tab=doc#GetBucketsBucketRefererConfig">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Allow<wbr>Empty</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicate whether the access request referer field can be empty.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Referers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}Referer access whitelist.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Allow<wbr>Empty</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicate whether the access request referer field can be empty.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Referers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}Referer access whitelist.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>allow<wbr>Empty</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Indicate whether the access request referer field can be empty.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>referers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}Referer access whitelist.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>allow<wbr>Empty</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicate whether the access request referer field can be empty.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>referers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}Referer access whitelist.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getbucketsbucketserversideencryptionrule">Get<wbr>Buckets<wbr>Bucket<wbr>Server<wbr>Side<wbr>Encryption<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetBucketsBucketServerSideEncryptionRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/v2/go/alicloud/oss?tab=doc#GetBucketsBucketServerSideEncryptionRule">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Sse<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The server-side encryption algorithm to use.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Sse<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The server-side encryption algorithm to use.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>sse<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The server-side encryption algorithm to use.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>sse<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The server-side encryption algorithm to use.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getbucketsbucketversioning">Get<wbr>Buckets<wbr>Bucket<wbr>Versioning</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetBucketsBucketVersioning">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/v2/go/alicloud/oss?tab=doc#GetBucketsBucketVersioning">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A bucket versioning state. Possible values:`Enabled` and `Suspended`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A bucket versioning state. Possible values:`Enabled` and `Suspended`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A bucket versioning state. Possible values:`Enabled` and `Suspended`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A bucket versioning state. Possible values:`Enabled` and `Suspended`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getbucketsbucketwebsite">Get<wbr>Buckets<wbr>Bucket<wbr>Website</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetBucketsBucketWebsite">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/v2/go/alicloud/oss?tab=doc#GetBucketsBucketWebsite">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Error<wbr>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Key of the HTML document containing the error page.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Index<wbr>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Key of the HTML document containing the home page.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Error<wbr>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Key of the HTML document containing the error page.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Index<wbr>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Key of the HTML document containing the home page.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>error<wbr>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Key of the HTML document containing the error page.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>index<wbr>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Key of the HTML document containing the home page.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>error<wbr>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Key of the HTML document containing the error page.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>index<wbr>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Key of the HTML document containing the home page.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







