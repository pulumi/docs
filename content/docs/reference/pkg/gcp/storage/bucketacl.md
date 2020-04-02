
---
title: "BucketACL"
block_external_search_index: true
---

Authoritatively manages a bucket's ACLs in Google cloud storage service (GCS). For more information see
[the official documentation](https://cloud.google.com/storage/docs/access-control/lists)
and
[API](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls).

Bucket ACLs can be managed non authoritatively using the `storage_bucket_access_control` resource. Do not use these two resources in conjunction to manage the same bucket.

Permissions can be granted either by ACLs or Cloud IAM policies. In general, permissions granted by Cloud IAM policies do not appear in ACLs, and permissions granted by ACLs do not appear in Cloud IAM policies. The only exception is for ACLs applied directly on a bucket and certain bucket-level Cloud IAM policies, as described in [Cloud IAM relation to ACLs](https://cloud.google.com/storage/docs/access-control/iam#acls).

**NOTE** This resource will not remove the `project-owners-<project_id>` entity from the `OWNER` role.

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/storage_bucket_acl.html.markdown.



## Create a BucketACL Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/storage/#BucketACL">BucketACL</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/storage/#BucketACLArgs">BucketACLArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">BucketACL</span><span class="p">(resource_name, opts=None, </span>bucket=None<span class="p">, </span>default_acl=None<span class="p">, </span>predefined_acl=None<span class="p">, </span>role_entities=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewBucketACL<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/storage?tab=doc#BucketACLArgs">BucketACLArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/storage?tab=doc#BucketACL">BucketACL</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Storage.BucketACL.html">BucketACL</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Storage.BucketACLArgs.html">BucketACLArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket it applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Configure this ACL to be the default ACL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Predefined<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `role_entity` is not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Entities</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefined_acl` is not.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket it applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Configure this ACL to be the default ACL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Predefined<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `role_entity` is not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Entities</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefined_acl` is not.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket it applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Configure this ACL to be the default ACL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>predefined<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `role_entity` is not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role<wbr>Entities</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefined_acl` is not.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the bucket it applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Configure this ACL to be the default ACL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>predefined_<wbr>acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `role_entity` is not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role_<wbr>entities</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefined_acl` is not.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## BucketACL Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket it applies to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Configure this ACL to be the default ACL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Predefined<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `role_entity` is not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role<wbr>Entities</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefined_acl` is not.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket it applies to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Configure this ACL to be the default ACL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Predefined<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `role_entity` is not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role<wbr>Entities</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefined_acl` is not.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket it applies to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Configure this ACL to be the default ACL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>predefined<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `role_entity` is not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role<wbr>Entities</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefined_acl` is not.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the bucket it applies to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default_<wbr>acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Configure this ACL to be the default ACL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>predefined_<wbr>acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `role_entity` is not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role_<wbr>entities</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefined_acl` is not.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing BucketACL Resource

Get an existing BucketACL resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/storage/#BucketACLState">BucketACLState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/storage/#BucketACL">BucketACL</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>bucket=None<span class="p">, </span>default_acl=None<span class="p">, </span>predefined_acl=None<span class="p">, </span>role_entities=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetBucketACL<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/storage?tab=doc#BucketACLState">BucketACLState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/storage?tab=doc#BucketACL">BucketACL</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Storage.BucketACL.html">BucketACL</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Storage.BucketACLState.html">BucketACLState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the bucket it applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Configure this ACL to be the default ACL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Predefined<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `role_entity` is not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Entities</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefined_acl` is not.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket it applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Configure this ACL to be the default ACL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Predefined<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `role_entity` is not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Entities</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefined_acl` is not.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the bucket it applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Configure this ACL to be the default ACL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>predefined<wbr>Acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `role_entity` is not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role<wbr>Entities</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefined_acl` is not.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the bucket it applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Configure this ACL to be the default ACL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>predefined_<wbr>acl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The [canned GCS ACL](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl) to apply. Must be set if `role_entity` is not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role_<wbr>entities</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of role/entity pairs in the form `ROLE:entity`. See [GCS Bucket ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  for more details. Must be set if `predefined_acl` is not.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
