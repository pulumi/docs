
---
title: "SaslUser"
block_external_search_index: true
---



Provides an ALIKAFKA sasl user resource.

> **NOTE:** Available in 1.66.0+

> **NOTE:**  Only the following regions support create alikafka sasl user.
[`cn-hangzhou`,`cn-beijing`,`cn-shenzhen`,`cn-shanghai`,`cn-qingdao`,`cn-hongkong`,`cn-huhehaote`,`cn-zhangjiakou`,`ap-southeast-1`,`ap-south-1`,`ap-southeast-5`]

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/alikafka_sasl_user.html.markdown.



## Create a SaslUser Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/alikafka/#SaslUser">SaslUser</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/alikafka/#SaslUserArgs">SaslUserArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">SaslUser</span><span class="p">(resource_name, opts=None, </span>instance_id=None<span class="p">, </span>kms_encrypted_password=None<span class="p">, </span>kms_encryption_context=None<span class="p">, </span>password=None<span class="p">, </span>username=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewSaslUser<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/alikafka?tab=doc#SaslUserArgs">SaslUserArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/alikafka?tab=doc#SaslUser">SaslUser</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Alikafka.SaslUser.html">SaslUser</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.AliKafka.SaslUserArgs.html">SaslUserArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the ALIKAFKA Instance that owns the groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Encrypted<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An KMS encrypts password used to a db account. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Encryption<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a user with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Operation password. It may consist of letters, digits, or underlines, with a length of 1 to 64 characters. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Username for the sasl user. The length should between 1 to 64 characters. The characters can only contain 'a'-'z', 'A'-'Z', '0'-'9', '_' and '-'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the ALIKAFKA Instance that owns the groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Encrypted<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An KMS encrypts password used to a db account. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Encryption<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a user with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Operation password. It may consist of letters, digits, or underlines, with a length of 1 to 64 characters. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Username for the sasl user. The length should between 1 to 64 characters. The characters can only contain 'a'-'z', 'A'-'Z', '0'-'9', '_' and '-'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the ALIKAFKA Instance that owns the groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms<wbr>Encrypted<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An KMS encrypts password used to a db account. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms<wbr>Encryption<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a user with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Operation password. It may consist of letters, digits, or underlines, with a length of 1 to 64 characters. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Username for the sasl user. The length should between 1 to 64 characters. The characters can only contain 'a'-'z', 'A'-'Z', '0'-'9', '_' and '-'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>instance_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the ALIKAFKA Instance that owns the groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms_<wbr>encrypted_<wbr>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An KMS encrypts password used to a db account. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms_<wbr>encryption_<wbr>context</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a user with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Operation password. It may consist of letters, digits, or underlines, with a length of 1 to 64 characters. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Username for the sasl user. The length should between 1 to 64 characters. The characters can only contain 'a'-'z', 'A'-'Z', '0'-'9', '_' and '-'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## SaslUser Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the ALIKAFKA Instance that owns the groups.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kms<wbr>Encrypted<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An KMS encrypts password used to a db account. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kms<wbr>Encryption<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a user with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Operation password. It may consist of letters, digits, or underlines, with a length of 1 to 64 characters. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Username for the sasl user. The length should between 1 to 64 characters. The characters can only contain 'a'-'z', 'A'-'Z', '0'-'9', '_' and '-'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the ALIKAFKA Instance that owns the groups.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kms<wbr>Encrypted<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An KMS encrypts password used to a db account. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kms<wbr>Encryption<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a user with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Operation password. It may consist of letters, digits, or underlines, with a length of 1 to 64 characters. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Username for the sasl user. The length should between 1 to 64 characters. The characters can only contain 'a'-'z', 'A'-'Z', '0'-'9', '_' and '-'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the ALIKAFKA Instance that owns the groups.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kms<wbr>Encrypted<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An KMS encrypts password used to a db account. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kms<wbr>Encryption<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a user with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Operation password. It may consist of letters, digits, or underlines, with a length of 1 to 64 characters. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Username for the sasl user. The length should between 1 to 64 characters. The characters can only contain 'a'-'z', 'A'-'Z', '0'-'9', '_' and '-'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>instance_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the ALIKAFKA Instance that owns the groups.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kms_<wbr>encrypted_<wbr>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An KMS encrypts password used to a db account. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kms_<wbr>encryption_<wbr>context</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a user with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Operation password. It may consist of letters, digits, or underlines, with a length of 1 to 64 characters. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Username for the sasl user. The length should between 1 to 64 characters. The characters can only contain 'a'-'z', 'A'-'Z', '0'-'9', '_' and '-'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing SaslUser Resource

Get an existing SaslUser resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/alikafka/#SaslUserState">SaslUserState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/alikafka/#SaslUser">SaslUser</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>instance_id=None<span class="p">, </span>kms_encrypted_password=None<span class="p">, </span>kms_encryption_context=None<span class="p">, </span>password=None<span class="p">, </span>username=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetSaslUser<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/alikafka?tab=doc#SaslUserState">SaslUserState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/alikafka?tab=doc#SaslUser">SaslUser</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Alikafka.SaslUser.html">SaslUser</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Alikafka.SaslUserState.html">SaslUserState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the ALIKAFKA Instance that owns the groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Encrypted<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An KMS encrypts password used to a db account. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Encryption<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a user with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Operation password. It may consist of letters, digits, or underlines, with a length of 1 to 64 characters. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Username for the sasl user. The length should between 1 to 64 characters. The characters can only contain 'a'-'z', 'A'-'Z', '0'-'9', '_' and '-'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ID of the ALIKAFKA Instance that owns the groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Encrypted<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An KMS encrypts password used to a db account. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Encryption<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a user with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Operation password. It may consist of letters, digits, or underlines, with a length of 1 to 64 characters. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Username for the sasl user. The length should between 1 to 64 characters. The characters can only contain 'a'-'z', 'A'-'Z', '0'-'9', '_' and '-'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the ALIKAFKA Instance that owns the groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms<wbr>Encrypted<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An KMS encrypts password used to a db account. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms<wbr>Encryption<wbr>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a user with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Operation password. It may consist of letters, digits, or underlines, with a length of 1 to 64 characters. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Username for the sasl user. The length should between 1 to 64 characters. The characters can only contain 'a'-'z', 'A'-'Z', '0'-'9', '_' and '-'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the ALIKAFKA Instance that owns the groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms_<wbr>encrypted_<wbr>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An KMS encrypts password used to a db account. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms_<wbr>encryption_<wbr>context</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a user with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Operation password. It may consist of letters, digits, or underlines, with a length of 1 to 64 characters. You have to specify one of `password` and `kms_encrypted_password` fields.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Username for the sasl user. The length should between 1 to 64 characters. The characters can only contain 'a'-'z', 'A'-'Z', '0'-'9', '_' and '-'.
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

