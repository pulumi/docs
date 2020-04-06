
---
title: "Policy"
block_external_search_index: true
---






## Create a Policy Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ram/#Policy">Policy</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ram/#PolicyArgs">PolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Policy</span><span class="p">(resource_name, opts=None, </span>description=None<span class="p">, </span>document=None<span class="p">, </span>force=None<span class="p">, </span>name=None<span class="p">, </span>statements=None<span class="p">, </span>version=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ram?tab=doc#PolicyArgs">PolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ram?tab=doc#Policy">Policy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ram.Policy.html">Policy</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ram.PolicyArgs.html">PolicyArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the RAM policy. This name can have a string of 1 to 1024 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Document of the RAM policy. It is required when the `statement` is not specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}This parameter is used for resource destroy. Default value is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policystatement">List&lt;Policy<wbr>Statement<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Statements of the RAM policy document. It is required when the `document` is not specified.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;statement&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Version of the RAM policy document. Valid value is `1`. Default value is `1`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;version&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

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
    <dd>{{% md %}}Description of the RAM policy. This name can have a string of 1 to 1024 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Document of the RAM policy. It is required when the `statement` is not specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}This parameter is used for resource destroy. Default value is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policystatement">[]Policy<wbr>Statement</a></span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Statements of the RAM policy document. It is required when the `document` is not specified.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;statement&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Version of the RAM policy document. Valid value is `1`. Default value is `1`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;version&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

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
    <dd>{{% md %}}Description of the RAM policy. This name can have a string of 1 to 1024 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>document</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Document of the RAM policy. It is required when the `statement` is not specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}This parameter is used for resource destroy. Default value is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policystatement">Policy<wbr>Statement[]?</a></span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Statements of the RAM policy document. It is required when the `document` is not specified.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;statement&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Version of the RAM policy document. Valid value is `1`. Default value is `1`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;version&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

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
    <dd>{{% md %}}Description of the RAM policy. This name can have a string of 1 to 1024 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>document</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Document of the RAM policy. It is required when the `statement` is not specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}This parameter is used for resource destroy. Default value is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policystatement">List[Policy<wbr>Statement]</a></span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Statements of the RAM policy document. It is required when the `document` is not specified.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;statement&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Version of the RAM policy document. Valid value is `1`. Default value is `1`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;version&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

</dl>
{{% /choosable %}}







## Policy Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Attachment<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The policy attachment count.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the RAM policy. This name can have a string of 1 to 1024 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Document of the RAM policy. It is required when the `statement` is not specified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}This parameter is used for resource destroy. Default value is `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policystatement">List&lt;Policy<wbr>Statement&gt;</a></span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Statements of the RAM policy document. It is required when the `document` is not specified.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;statement&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The policy type.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Version of the RAM policy document. Valid value is `1`. Default value is `1`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;version&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Attachment<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The policy attachment count.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of the RAM policy. This name can have a string of 1 to 1024 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Document of the RAM policy. It is required when the `statement` is not specified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}This parameter is used for resource destroy. Default value is `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policystatement">[]Policy<wbr>Statement</a></span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Statements of the RAM policy document. It is required when the `document` is not specified.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;statement&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The policy type.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Version of the RAM policy document. Valid value is `1`. Default value is `1`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;version&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>attachment<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The policy attachment count.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the RAM policy. This name can have a string of 1 to 1024 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>document</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Document of the RAM policy. It is required when the `statement` is not specified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}This parameter is used for resource destroy. Default value is `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policystatement">Policy<wbr>Statement[]</a></span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Statements of the RAM policy document. It is required when the `document` is not specified.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;statement&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The policy type.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Version of the RAM policy document. Valid value is `1`. Default value is `1`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;version&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>attachment_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The policy attachment count.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the RAM policy. This name can have a string of 1 to 1024 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>document</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Document of the RAM policy. It is required when the `statement` is not specified.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}This parameter is used for resource destroy. Default value is `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policystatement">List[Policy<wbr>Statement]</a></span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Statements of the RAM policy document. It is required when the `document` is not specified.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;statement&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The policy type.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Version of the RAM policy document. Valid value is `1`. Default value is `1`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;version&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

</dl>
{{% /choosable %}}








## Look up an Existing Policy Resource

Get an existing Policy resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ram/#PolicyState">PolicyState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ram/#Policy">Policy</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>attachment_count=None<span class="p">, </span>description=None<span class="p">, </span>document=None<span class="p">, </span>force=None<span class="p">, </span>name=None<span class="p">, </span>statements=None<span class="p">, </span>type=None<span class="p">, </span>version=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ram?tab=doc#PolicyState">PolicyState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ram?tab=doc#Policy">Policy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ram.Policy.html">Policy</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ram.PolicyState.html">PolicyState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Attachment<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The policy attachment count.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the RAM policy. This name can have a string of 1 to 1024 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Document of the RAM policy. It is required when the `statement` is not specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}This parameter is used for resource destroy. Default value is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policystatement">List&lt;Policy<wbr>Statement<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Statements of the RAM policy document. It is required when the `document` is not specified.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;statement&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The policy type.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Version of the RAM policy document. Valid value is `1`. Default value is `1`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;version&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Attachment<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The policy attachment count.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of the RAM policy. This name can have a string of 1 to 1024 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Document</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Document of the RAM policy. It is required when the `statement` is not specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}This parameter is used for resource destroy. Default value is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policystatement">[]Policy<wbr>Statement</a></span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Statements of the RAM policy document. It is required when the `document` is not specified.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;statement&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The policy type.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Version of the RAM policy document. Valid value is `1`. Default value is `1`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;version&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>attachment<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The policy attachment count.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the RAM policy. This name can have a string of 1 to 1024 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>document</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Document of the RAM policy. It is required when the `statement` is not specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}This parameter is used for resource destroy. Default value is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policystatement">Policy<wbr>Statement[]?</a></span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Statements of the RAM policy document. It is required when the `document` is not specified.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;statement&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The policy type.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Version of the RAM policy document. Valid value is `1`. Default value is `1`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;version&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>attachment_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The policy attachment count.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the RAM policy. This name can have a string of 1 to 1024 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>document</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Document of the RAM policy. It is required when the `statement` is not specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}This parameter is used for resource destroy. Default value is `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the RAM policy. This name can have a string of 1 to 128 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policystatement">List[Policy<wbr>Statement]</a></span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Statements of the RAM policy document. It is required when the `document` is not specified.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;statement&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The policy type.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) Version of the RAM policy document. Valid value is `1`. Default value is `1`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Field &#39;version&#39; has been deprecated from version 1.49.0, and use field &#39;document&#39; to replace. {{% /md %}}</p></dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Policy<wbr>Statement</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#PolicyStatement">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#PolicyStatement">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ram?tab=doc#PolicyStatementArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ram?tab=doc#PolicyStatementOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Actions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) List of operations for the `resource`. The format of each item in this list is `${service}:${action_name}`, such as `oss:ListBuckets` and `ecs:Describe*`. The `${service}` can be `ecs`, `oss`, `ots` and so on, the `${action_name}` refers to the name of an api interface which related to the `${service}`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) This parameter indicates whether or not the `action` is allowed. Valid values are `Allow` and `Deny`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) List of specific objects which will be authorized. The format of each item in this list is `acs:${service}:${region}:${account_id}:${relative_id}`, such as `acs:ecs:*:*:instance/inst-002` and `acs:oss:*:1234567890000:mybucket`. The `${service}` can be `ecs`, `oss`, `ots` and so on, the `${region}` is the region info which can use `*` replace when it is not supplied, the `${account_id}` refers to someone's Alicloud account id or you can use `*` to replace, the `${relative_id}` is the resource description section which related to the `${service}`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Actions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) List of operations for the `resource`. The format of each item in this list is `${service}:${action_name}`, such as `oss:ListBuckets` and `ecs:Describe*`. The `${service}` can be `ecs`, `oss`, `ots` and so on, the `${action_name}` refers to the name of an api interface which related to the `${service}`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) This parameter indicates whether or not the `action` is allowed. Valid values are `Allow` and `Deny`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resources</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) List of specific objects which will be authorized. The format of each item in this list is `acs:${service}:${region}:${account_id}:${relative_id}`, such as `acs:ecs:*:*:instance/inst-002` and `acs:oss:*:1234567890000:mybucket`. The `${service}` can be `ecs`, `oss`, `ots` and so on, the `${region}` is the region info which can use `*` replace when it is not supplied, the `${account_id}` refers to someone's Alicloud account id or you can use `*` to replace, the `${relative_id}` is the resource description section which related to the `${service}`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>actions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) List of operations for the `resource`. The format of each item in this list is `${service}:${action_name}`, such as `oss:ListBuckets` and `ecs:Describe*`. The `${service}` can be `ecs`, `oss`, `ots` and so on, the `${action_name}` refers to the name of an api interface which related to the `${service}`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) This parameter indicates whether or not the `action` is allowed. Valid values are `Allow` and `Deny`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resources</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) List of specific objects which will be authorized. The format of each item in this list is `acs:${service}:${region}:${account_id}:${relative_id}`, such as `acs:ecs:*:*:instance/inst-002` and `acs:oss:*:1234567890000:mybucket`. The `${service}` can be `ecs`, `oss`, `ots` and so on, the `${region}` is the region info which can use `*` replace when it is not supplied, the `${account_id}` refers to someone's Alicloud account id or you can use `*` to replace, the `${relative_id}` is the resource description section which related to the `${service}`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>actions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) List of operations for the `resource`. The format of each item in this list is `${service}:${action_name}`, such as `oss:ListBuckets` and `ecs:Describe*`. The `${service}` can be `ecs`, `oss`, `ots` and so on, the `${action_name}` refers to the name of an api interface which related to the `${service}`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) This parameter indicates whether or not the `action` is allowed. Valid values are `Allow` and `Deny`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resources</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}(It has been deprecated from version 1.49.0, and use field 'document' to replace.) List of specific objects which will be authorized. The format of each item in this list is `acs:${service}:${region}:${account_id}:${relative_id}`, such as `acs:ecs:*:*:instance/inst-002` and `acs:oss:*:1234567890000:mybucket`. The `${service}` can be `ecs`, `oss`, `ots` and so on, the `${region}` is the region info which can use `*` replace when it is not supplied, the `${account_id}` refers to someone's Alicloud account id or you can use `*` to replace, the `${relative_id}` is the resource description section which related to the `${service}`.
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

