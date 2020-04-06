
---
title: "Trail"
block_external_search_index: true
---



Provides a new resource to manage [Action Trail](https://www.alibabacloud.com/help/doc-detail/28804.htm).

> **NOTE:** Available in 1.35.0+

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/actiontrail.html.markdown.



## Create a Trail Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/actiontrail/#Trail">Trail</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/actiontrail/#TrailArgs">TrailArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Trail</span><span class="p">(resource_name, opts=None, </span>event_rw=None<span class="p">, </span>name=None<span class="p">, </span>oss_bucket_name=None<span class="p">, </span>oss_key_prefix=None<span class="p">, </span>role_name=None<span class="p">, </span>sls_project_arn=None<span class="p">, </span>sls_write_role_arn=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewTrail<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/actiontrail?tab=doc#TrailArgs">TrailArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/actiontrail?tab=doc#Trail">Trail</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Actiontrail.Trail.html">Trail</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.ActionTrail.TrailArgs.html">TrailArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Event<wbr>Rw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the event is a read or a write event. Valid values: Read, Write, and All. Default value: Write.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the trail to be created, which must be unique for an account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Oss<wbr>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The OSS bucket to which the trail delivers logs. Ensure that this is an existing OSS bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oss<wbr>Key<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The prefix of the specified OSS bucket name. This parameter can be left empty.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The RAM role in ActionTrail permitted by the user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sls<wbr>Project<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sls<wbr>Write<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service role.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Rw</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Indicates whether the event is a read or a write event. Valid values: Read, Write, and All. Default value: Write.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the trail to be created, which must be unique for an account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Oss<wbr>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The OSS bucket to which the trail delivers logs. Ensure that this is an existing OSS bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oss<wbr>Key<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The prefix of the specified OSS bucket name. This parameter can be left empty.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The RAM role in ActionTrail permitted by the user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sls<wbr>Project<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sls<wbr>Write<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service role.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>event<wbr>Rw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the event is a read or a write event. Valid values: Read, Write, and All. Default value: Write.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the trail to be created, which must be unique for an account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>oss<wbr>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The OSS bucket to which the trail delivers logs. Ensure that this is an existing OSS bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oss<wbr>Key<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The prefix of the specified OSS bucket name. This parameter can be left empty.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The RAM role in ActionTrail permitted by the user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sls<wbr>Project<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sls<wbr>Write<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service role.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>event_<wbr>rw</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicates whether the event is a read or a write event. Valid values: Read, Write, and All. Default value: Write.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the trail to be created, which must be unique for an account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>oss_<wbr>bucket_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The OSS bucket to which the trail delivers logs. Ensure that this is an existing OSS bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oss_<wbr>key_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The prefix of the specified OSS bucket name. This parameter can be left empty.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The RAM role in ActionTrail permitted by the user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sls_<wbr>project_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sls_<wbr>write_<wbr>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service role.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Trail Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Event<wbr>Rw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the event is a read or a write event. Valid values: Read, Write, and All. Default value: Write.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the trail to be created, which must be unique for an account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Oss<wbr>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The OSS bucket to which the trail delivers logs. Ensure that this is an existing OSS bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Oss<wbr>Key<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The prefix of the specified OSS bucket name. This parameter can be left empty.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The RAM role in ActionTrail permitted by the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sls<wbr>Project<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service project.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sls<wbr>Write<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service role.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Event<wbr>Rw</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Indicates whether the event is a read or a write event. Valid values: Read, Write, and All. Default value: Write.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the trail to be created, which must be unique for an account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Oss<wbr>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The OSS bucket to which the trail delivers logs. Ensure that this is an existing OSS bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Oss<wbr>Key<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The prefix of the specified OSS bucket name. This parameter can be left empty.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The RAM role in ActionTrail permitted by the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sls<wbr>Project<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service project.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sls<wbr>Write<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service role.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>event<wbr>Rw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the event is a read or a write event. Valid values: Read, Write, and All. Default value: Write.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the trail to be created, which must be unique for an account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>oss<wbr>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The OSS bucket to which the trail delivers logs. Ensure that this is an existing OSS bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>oss<wbr>Key<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The prefix of the specified OSS bucket name. This parameter can be left empty.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The RAM role in ActionTrail permitted by the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sls<wbr>Project<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service project.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sls<wbr>Write<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service role.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>event_<wbr>rw</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicates whether the event is a read or a write event. Valid values: Read, Write, and All. Default value: Write.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the trail to be created, which must be unique for an account.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>oss_<wbr>bucket_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The OSS bucket to which the trail delivers logs. Ensure that this is an existing OSS bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>oss_<wbr>key_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The prefix of the specified OSS bucket name. This parameter can be left empty.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The RAM role in ActionTrail permitted by the user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sls_<wbr>project_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service project.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sls_<wbr>write_<wbr>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service role.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Trail Resource

Get an existing Trail resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/actiontrail/#TrailState">TrailState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/actiontrail/#Trail">Trail</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>event_rw=None<span class="p">, </span>name=None<span class="p">, </span>oss_bucket_name=None<span class="p">, </span>oss_key_prefix=None<span class="p">, </span>role_name=None<span class="p">, </span>sls_project_arn=None<span class="p">, </span>sls_write_role_arn=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetTrail<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/actiontrail?tab=doc#TrailState">TrailState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/actiontrail?tab=doc#Trail">Trail</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Actiontrail.Trail.html">Trail</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Actiontrail.TrailState.html">TrailState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Event<wbr>Rw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the event is a read or a write event. Valid values: Read, Write, and All. Default value: Write.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the trail to be created, which must be unique for an account.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oss<wbr>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The OSS bucket to which the trail delivers logs. Ensure that this is an existing OSS bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oss<wbr>Key<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The prefix of the specified OSS bucket name. This parameter can be left empty.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The RAM role in ActionTrail permitted by the user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sls<wbr>Project<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sls<wbr>Write<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service role.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Rw</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Indicates whether the event is a read or a write event. Valid values: Read, Write, and All. Default value: Write.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the trail to be created, which must be unique for an account.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oss<wbr>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The OSS bucket to which the trail delivers logs. Ensure that this is an existing OSS bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oss<wbr>Key<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The prefix of the specified OSS bucket name. This parameter can be left empty.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The RAM role in ActionTrail permitted by the user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sls<wbr>Project<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sls<wbr>Write<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service role.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>event<wbr>Rw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Indicates whether the event is a read or a write event. Valid values: Read, Write, and All. Default value: Write.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the trail to be created, which must be unique for an account.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oss<wbr>Bucket<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The OSS bucket to which the trail delivers logs. Ensure that this is an existing OSS bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oss<wbr>Key<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The prefix of the specified OSS bucket name. This parameter can be left empty.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The RAM role in ActionTrail permitted by the user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sls<wbr>Project<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sls<wbr>Write<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service role.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>event_<wbr>rw</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicates whether the event is a read or a write event. Valid values: Read, Write, and All. Default value: Write.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the trail to be created, which must be unique for an account.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oss_<wbr>bucket_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The OSS bucket to which the trail delivers logs. Ensure that this is an existing OSS bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oss_<wbr>key_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The prefix of the specified OSS bucket name. This parameter can be left empty.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The RAM role in ActionTrail permitted by the user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sls_<wbr>project_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service project.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sls_<wbr>write_<wbr>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique ARN of the Log Service role.
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

