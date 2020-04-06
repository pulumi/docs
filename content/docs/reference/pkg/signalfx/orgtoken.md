
---
title: "OrgToken"
block_external_search_index: true
---



Manage SignalFx org tokens.

> This content is derived from https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/org_token.html.markdown.



## Create a OrgToken Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#OrgToken">OrgToken</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#OrgTokenArgs">OrgTokenArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">OrgToken</span><span class="p">(resource_name, opts=None, </span>description=None<span class="p">, </span>disabled=None<span class="p">, </span>dpm_limits=None<span class="p">, </span>host_or_usage_limits=None<span class="p">, </span>name=None<span class="p">, </span>notifications=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewOrgToken<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#OrgTokenArgs">OrgTokenArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#OrgToken">OrgToken</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx..OrgToken.html">OrgToken</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx.OrgTokenArgs.html">OrgTokenArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
    <dd>{{% md %}}Description of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag that controls enabling the token. If set to `true`, the token is disabled, and you can't use it for authentication. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dpm<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokendpmlimits">Org<wbr>Token<wbr>Dpm<wbr>Limits<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specify DPM-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Or<wbr>Usage<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokenhostorusagelimits">Org<wbr>Token<wbr>Host<wbr>Or<wbr>Usage<wbr>Limits<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specify Usage-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of strings specifying where notifications will be sent when an incident occurs. See
https://developers.signalfx.com/v2/docs/detector-model#notifications-models for more info
{{% /md %}}</dd>

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
    <dd>{{% md %}}Description of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls enabling the token. If set to `true`, the token is disabled, and you can't use it for authentication. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dpm<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokendpmlimits">*Org<wbr>Token<wbr>Dpm<wbr>Limits</a></span>
    </dt>
    <dd>{{% md %}}Specify DPM-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Or<wbr>Usage<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokenhostorusagelimits">*Org<wbr>Token<wbr>Host<wbr>Or<wbr>Usage<wbr>Limits</a></span>
    </dt>
    <dd>{{% md %}}Specify Usage-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of strings specifying where notifications will be sent when an incident occurs. See
https://developers.signalfx.com/v2/docs/detector-model#notifications-models for more info
{{% /md %}}</dd>

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
    <dd>{{% md %}}Description of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag that controls enabling the token. If set to `true`, the token is disabled, and you can't use it for authentication. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dpm<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokendpmlimits">Org<wbr>Token<wbr>Dpm<wbr>Limits?</a></span>
    </dt>
    <dd>{{% md %}}Specify DPM-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Or<wbr>Usage<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokenhostorusagelimits">Org<wbr>Token<wbr>Host<wbr>Or<wbr>Usage<wbr>Limits?</a></span>
    </dt>
    <dd>{{% md %}}Specify Usage-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of strings specifying where notifications will be sent when an incident occurs. See
https://developers.signalfx.com/v2/docs/detector-model#notifications-models for more info
{{% /md %}}</dd>

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
    <dd>{{% md %}}Description of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls enabling the token. If set to `true`, the token is disabled, and you can't use it for authentication. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dpm_<wbr>limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokendpmlimits">Dict[Org<wbr>Token<wbr>Dpm<wbr>Limits]</a></span>
    </dt>
    <dd>{{% md %}}Specify DPM-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host_<wbr>or_<wbr>usage_<wbr>limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokenhostorusagelimits">Dict[Org<wbr>Token<wbr>Host<wbr>Or<wbr>Usage<wbr>Limits]</a></span>
    </dt>
    <dd>{{% md %}}Specify Usage-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of strings specifying where notifications will be sent when an incident occurs. See
https://developers.signalfx.com/v2/docs/detector-model#notifications-models for more info
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## OrgToken Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag that controls enabling the token. If set to `true`, the token is disabled, and you can't use it for authentication. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dpm<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokendpmlimits">Org<wbr>Token<wbr>Dpm<wbr>Limits?</a></span>
    </dt>
    <dd>{{% md %}}Specify DPM-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Host<wbr>Or<wbr>Usage<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokenhostorusagelimits">Org<wbr>Token<wbr>Host<wbr>Or<wbr>Usage<wbr>Limits?</a></span>
    </dt>
    <dd>{{% md %}}Specify Usage-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of strings specifying where notifications will be sent when an incident occurs. See
https://developers.signalfx.com/v2/docs/detector-model#notifications-models for more info
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls enabling the token. If set to `true`, the token is disabled, and you can't use it for authentication. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dpm<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokendpmlimits">*Org<wbr>Token<wbr>Dpm<wbr>Limits</a></span>
    </dt>
    <dd>{{% md %}}Specify DPM-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Host<wbr>Or<wbr>Usage<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokenhostorusagelimits">*Org<wbr>Token<wbr>Host<wbr>Or<wbr>Usage<wbr>Limits</a></span>
    </dt>
    <dd>{{% md %}}Specify Usage-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of strings specifying where notifications will be sent when an incident occurs. See
https://developers.signalfx.com/v2/docs/detector-model#notifications-models for more info
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag that controls enabling the token. If set to `true`, the token is disabled, and you can't use it for authentication. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dpm<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokendpmlimits">Org<wbr>Token<wbr>Dpm<wbr>Limits?</a></span>
    </dt>
    <dd>{{% md %}}Specify DPM-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>host<wbr>Or<wbr>Usage<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokenhostorusagelimits">Org<wbr>Token<wbr>Host<wbr>Or<wbr>Usage<wbr>Limits?</a></span>
    </dt>
    <dd>{{% md %}}Specify Usage-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of strings specifying where notifications will be sent when an incident occurs. See
https://developers.signalfx.com/v2/docs/detector-model#notifications-models for more info
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls enabling the token. If set to `true`, the token is disabled, and you can't use it for authentication. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dpm_<wbr>limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokendpmlimits">Dict[Org<wbr>Token<wbr>Dpm<wbr>Limits]</a></span>
    </dt>
    <dd>{{% md %}}Specify DPM-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>host_<wbr>or_<wbr>usage_<wbr>limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokenhostorusagelimits">Dict[Org<wbr>Token<wbr>Host<wbr>Or<wbr>Usage<wbr>Limits]</a></span>
    </dt>
    <dd>{{% md %}}Specify Usage-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of strings specifying where notifications will be sent when an incident occurs. See
https://developers.signalfx.com/v2/docs/detector-model#notifications-models for more info
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing OrgToken Resource

Get an existing OrgToken resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#OrgTokenState">OrgTokenState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#OrgToken">OrgToken</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>description=None<span class="p">, </span>disabled=None<span class="p">, </span>dpm_limits=None<span class="p">, </span>host_or_usage_limits=None<span class="p">, </span>name=None<span class="p">, </span>notifications=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetOrgToken<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#OrgTokenState">OrgTokenState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#OrgToken">OrgToken</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx..OrgToken.html">OrgToken</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx..OrgTokenState.html">OrgTokenState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag that controls enabling the token. If set to `true`, the token is disabled, and you can't use it for authentication. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dpm<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokendpmlimits">Org<wbr>Token<wbr>Dpm<wbr>Limits<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specify DPM-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Or<wbr>Usage<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokenhostorusagelimits">Org<wbr>Token<wbr>Host<wbr>Or<wbr>Usage<wbr>Limits<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specify Usage-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of strings specifying where notifications will be sent when an incident occurs. See
https://developers.signalfx.com/v2/docs/detector-model#notifications-models for more info
{{% /md %}}</dd>

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
    <dd>{{% md %}}Description of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls enabling the token. If set to `true`, the token is disabled, and you can't use it for authentication. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dpm<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokendpmlimits">*Org<wbr>Token<wbr>Dpm<wbr>Limits</a></span>
    </dt>
    <dd>{{% md %}}Specify DPM-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Or<wbr>Usage<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokenhostorusagelimits">*Org<wbr>Token<wbr>Host<wbr>Or<wbr>Usage<wbr>Limits</a></span>
    </dt>
    <dd>{{% md %}}Specify Usage-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of strings specifying where notifications will be sent when an incident occurs. See
https://developers.signalfx.com/v2/docs/detector-model#notifications-models for more info
{{% /md %}}</dd>

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
    <dd>{{% md %}}Description of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag that controls enabling the token. If set to `true`, the token is disabled, and you can't use it for authentication. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dpm<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokendpmlimits">Org<wbr>Token<wbr>Dpm<wbr>Limits?</a></span>
    </dt>
    <dd>{{% md %}}Specify DPM-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Or<wbr>Usage<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokenhostorusagelimits">Org<wbr>Token<wbr>Host<wbr>Or<wbr>Usage<wbr>Limits?</a></span>
    </dt>
    <dd>{{% md %}}Specify Usage-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of strings specifying where notifications will be sent when an incident occurs. See
https://developers.signalfx.com/v2/docs/detector-model#notifications-models for more info
{{% /md %}}</dd>

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
    <dd>{{% md %}}Description of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls enabling the token. If set to `true`, the token is disabled, and you can't use it for authentication. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dpm_<wbr>limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokendpmlimits">Dict[Org<wbr>Token<wbr>Dpm<wbr>Limits]</a></span>
    </dt>
    <dd>{{% md %}}Specify DPM-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host_<wbr>or_<wbr>usage_<wbr>limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#orgtokenhostorusagelimits">Dict[Org<wbr>Token<wbr>Host<wbr>Or<wbr>Usage<wbr>Limits]</a></span>
    </dt>
    <dd>{{% md %}}Specify Usage-based limits for this token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of strings specifying where notifications will be sent when an incident occurs. See
https://developers.signalfx.com/v2/docs/detector-model#notifications-models for more info
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Org<wbr>Token<wbr>Dpm<wbr>Limits</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#OrgTokenDpmLimits">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#OrgTokenDpmLimits">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#OrgTokenDpmLimitsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#OrgTokenDpmLimitsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dpm<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The datapoints per minute (dpm) limit for this token. If you exceed this limit, SignalFx sends out an alert.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dpm<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}DPM level at which SignalFx sends the notification for this token. If you don't specify a notification, SignalFx sends the generic notification.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dpm<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The datapoints per minute (dpm) limit for this token. If you exceed this limit, SignalFx sends out an alert.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dpm<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}DPM level at which SignalFx sends the notification for this token. If you don't specify a notification, SignalFx sends the generic notification.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dpm<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The datapoints per minute (dpm) limit for this token. If you exceed this limit, SignalFx sends out an alert.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dpm<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}DPM level at which SignalFx sends the notification for this token. If you don't specify a notification, SignalFx sends the generic notification.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dpm<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The datapoints per minute (dpm) limit for this token. If you exceed this limit, SignalFx sends out an alert.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dpm<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}DPM level at which SignalFx sends the notification for this token. If you don't specify a notification, SignalFx sends the generic notification.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Org<wbr>Token<wbr>Host<wbr>Or<wbr>Usage<wbr>Limits</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#OrgTokenHostOrUsageLimits">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#OrgTokenHostOrUsageLimits">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#OrgTokenHostOrUsageLimitsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#OrgTokenHostOrUsageLimitsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Max number of Docker containers that can use this token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Notification threshold for Docker containers
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Metrics<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Max number of custom metrics that can be sent with this token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Metrics<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Notification threshold for custom metrics
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>High<wbr>Res<wbr>Metrics<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Max number of hi-res metrics that can be sent with this toke
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>High<wbr>Res<wbr>Metrics<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Notification threshold for hi-res metrics
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Max number of hosts that can use this token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Notification threshold for hosts
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Max number of Docker containers that can use this token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Container<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Notification threshold for Docker containers
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Metrics<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Max number of custom metrics that can be sent with this token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Metrics<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Notification threshold for custom metrics
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>High<wbr>Res<wbr>Metrics<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Max number of hi-res metrics that can be sent with this toke
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>High<wbr>Res<wbr>Metrics<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Notification threshold for hi-res metrics
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Max number of hosts that can use this token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Notification threshold for hosts
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>container<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Max number of Docker containers that can use this token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>container<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Notification threshold for Docker containers
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Metrics<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Max number of custom metrics that can be sent with this token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Metrics<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Notification threshold for custom metrics
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>high<wbr>Res<wbr>Metrics<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Max number of hi-res metrics that can be sent with this toke
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>high<wbr>Res<wbr>Metrics<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Notification threshold for hi-res metrics
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Max number of hosts that can use this token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Notification threshold for hosts
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>container<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Max number of Docker containers that can use this token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>container<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Notification threshold for Docker containers
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Metrics<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Max number of custom metrics that can be sent with this token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Metrics<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Notification threshold for custom metrics
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>high<wbr>Res<wbr>Metrics<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Max number of hi-res metrics that can be sent with this toke
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>high<wbr>Res<wbr>Metrics<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Notification threshold for hi-res metrics
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Max number of hosts that can use this token
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>Notification<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Notification threshold for hosts
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-signalfx">https://github.com/pulumi/pulumi-signalfx</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

