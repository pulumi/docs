
---
title: "FirewallPolicy"
block_external_search_index: true
---

Manages an Azure Front Door Web Application Firewall Policy instance.

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/frontdoor_firewall_policy.html.markdown.



## Create a FirewallPolicy Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/frontdoor/#FirewallPolicy">FirewallPolicy</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/frontdoor/#FirewallPolicyArgs">FirewallPolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">FirewallPolicy</span><span class="p">(resource_name, opts=None, </span>custom_block_response_body=None<span class="p">, </span>custom_block_response_status_code=None<span class="p">, </span>custom_rules=None<span class="p">, </span>enabled=None<span class="p">, </span>managed_rules=None<span class="p">, </span>mode=None<span class="p">, </span>name=None<span class="p">, </span>redirect_url=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewFirewallPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyArgs">FirewallPolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicy">FirewallPolicy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Frontdoor.FirewallPolicy.html">FirewallPolicy</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.FrontDoor.Inputs.FirewallPolicyArgs.html">FirewallPolicyArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Custom<wbr>Block<wbr>Response<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response body. The body must be specified in base64 encoding.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Block<wbr>Response<wbr>Status<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response status code. Possible values are `200`, `403`, `405`, `406`, or `429`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicycustomrule">List&lt;Pulumi.<wbr>Azure.<wbr>Front<wbr>Door.<wbr>Inputs.<wbr>Firewall<wbr>Policy<wbr>Custom<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `custom_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Is the policy a enabled state or disabled state. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Managed<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedrule">List&lt;Pulumi.<wbr>Azure.<wbr>Front<wbr>Door.<wbr>Inputs.<wbr>Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `managed_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The firewall policy mode. Possible values are `Detection`, `Prevention` and defaults to `Prevention`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If action type is redirect, this field represents redirect URL for the client.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Web Application Firewall Policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Block<wbr>Response<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response body. The body must be specified in base64 encoding.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Block<wbr>Response<wbr>Status<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response status code. Possible values are `200`, `403`, `405`, `406`, or `429`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicycustomrule">[]Firewall<wbr>Policy<wbr>Custom<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}One or more `custom_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Is the policy a enabled state or disabled state. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Managed<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedrule">[]Firewall<wbr>Policy<wbr>Managed<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}One or more `managed_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The firewall policy mode. Possible values are `Detection`, `Prevention` and defaults to `Prevention`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If action type is redirect, this field represents redirect URL for the client.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Web Application Firewall Policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Block<wbr>Response<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response body. The body must be specified in base64 encoding.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Block<wbr>Response<wbr>Status<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response status code. Possible values are `200`, `403`, `405`, `406`, or `429`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicycustomrule">Firewall<wbr>Policy<wbr>Custom<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `custom_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Is the policy a enabled state or disabled state. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>managed<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedrule">Firewall<wbr>Policy<wbr>Managed<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `managed_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The firewall policy mode. Possible values are `Detection`, `Prevention` and defaults to `Prevention`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If action type is redirect, this field represents redirect URL for the client.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Web Application Firewall Policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>block_<wbr>response_<wbr>body</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response body. The body must be specified in base64 encoding.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>block_<wbr>response_<wbr>status_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response status code. Possible values are `200`, `403`, `405`, `406`, or `429`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicycustomrule">List[Firewall<wbr>Policy<wbr>Custom<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}One or more `custom_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the policy a enabled state or disabled state. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>managed_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedrule">List[Firewall<wbr>Policy<wbr>Managed<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}One or more `managed_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The firewall policy mode. Possible values are `Detection`, `Prevention` and defaults to `Prevention`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>redirect_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If action type is redirect, this field represents redirect URL for the client.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the resource group. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Web Application Firewall Policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## FirewallPolicy Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Custom<wbr>Block<wbr>Response<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response body. The body must be specified in base64 encoding.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Block<wbr>Response<wbr>Status<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response status code. Possible values are `200`, `403`, `405`, `406`, or `429`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicycustomrule">List&lt;Pulumi.<wbr>Azure.<wbr>Front<wbr>Door.<wbr>Outputs.<wbr>Firewall<wbr>Policy<wbr>Custom<wbr>Rule&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `custom_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Is the policy a enabled state or disabled state. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Frontend<wbr>Endpoint<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}the Frontend Endpoints associated with this Front Door Web Application Firewall policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Resource location.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Managed<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedrule">List&lt;Pulumi.<wbr>Azure.<wbr>Front<wbr>Door.<wbr>Outputs.<wbr>Firewall<wbr>Policy<wbr>Managed<wbr>Rule&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `managed_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The firewall policy mode. Possible values are `Detection`, `Prevention` and defaults to `Prevention`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If action type is redirect, this field represents redirect URL for the client.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Web Application Firewall Policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Custom<wbr>Block<wbr>Response<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response body. The body must be specified in base64 encoding.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Block<wbr>Response<wbr>Status<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response status code. Possible values are `200`, `403`, `405`, `406`, or `429`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicycustomrule">[]Firewall<wbr>Policy<wbr>Custom<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}One or more `custom_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Is the policy a enabled state or disabled state. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Frontend<wbr>Endpoint<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}the Frontend Endpoints associated with this Front Door Web Application Firewall policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Resource location.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Managed<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedrule">[]Firewall<wbr>Policy<wbr>Managed<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}One or more `managed_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The firewall policy mode. Possible values are `Detection`, `Prevention` and defaults to `Prevention`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If action type is redirect, this field represents redirect URL for the client.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Web Application Firewall Policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>custom<wbr>Block<wbr>Response<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response body. The body must be specified in base64 encoding.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom<wbr>Block<wbr>Response<wbr>Status<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response status code. Possible values are `200`, `403`, `405`, `406`, or `429`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicycustomrule">Firewall<wbr>Policy<wbr>Custom<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `custom_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Is the policy a enabled state or disabled state. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>frontend<wbr>Endpoint<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}the Frontend Endpoints associated with this Front Door Web Application Firewall policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Resource location.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>managed<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedrule">Firewall<wbr>Policy<wbr>Managed<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `managed_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The firewall policy mode. Possible values are `Detection`, `Prevention` and defaults to `Prevention`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If action type is redirect, this field represents redirect URL for the client.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Web Application Firewall Policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>custom_<wbr>block_<wbr>response_<wbr>body</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response body. The body must be specified in base64 encoding.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom_<wbr>block_<wbr>response_<wbr>status_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response status code. Possible values are `200`, `403`, `405`, `406`, or `429`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicycustomrule">List[Firewall<wbr>Policy<wbr>Custom<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}One or more `custom_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the policy a enabled state or disabled state. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>frontend_<wbr>endpoint_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}the Frontend Endpoints associated with this Front Door Web Application Firewall policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Resource location.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>managed_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedrule">List[Firewall<wbr>Policy<wbr>Managed<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}One or more `managed_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The firewall policy mode. Possible values are `Detection`, `Prevention` and defaults to `Prevention`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>redirect_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If action type is redirect, this field represents redirect URL for the client.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the resource group. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Web Application Firewall Policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing FirewallPolicy Resource

Get an existing FirewallPolicy resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/frontdoor/#FirewallPolicyState">FirewallPolicyState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/frontdoor/#FirewallPolicy">FirewallPolicy</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>custom_block_response_body=None<span class="p">, </span>custom_block_response_status_code=None<span class="p">, </span>custom_rules=None<span class="p">, </span>enabled=None<span class="p">, </span>frontend_endpoint_ids=None<span class="p">, </span>location=None<span class="p">, </span>managed_rules=None<span class="p">, </span>mode=None<span class="p">, </span>name=None<span class="p">, </span>redirect_url=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetFirewallPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyState">FirewallPolicyState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicy">FirewallPolicy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Frontdoor.FirewallPolicy.html">FirewallPolicy</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Frontdoor.FirewallPolicyState.html">FirewallPolicyState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Custom<wbr>Block<wbr>Response<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response body. The body must be specified in base64 encoding.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Block<wbr>Response<wbr>Status<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response status code. Possible values are `200`, `403`, `405`, `406`, or `429`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicycustomrule">List&lt;Pulumi.<wbr>Azure.<wbr>Front<wbr>Door.<wbr>Inputs.<wbr>Firewall<wbr>Policy<wbr>Custom<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `custom_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Is the policy a enabled state or disabled state. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Frontend<wbr>Endpoint<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}the Frontend Endpoints associated with this Front Door Web Application Firewall policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Resource location.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Managed<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedrule">List&lt;Pulumi.<wbr>Azure.<wbr>Front<wbr>Door.<wbr>Inputs.<wbr>Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `managed_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The firewall policy mode. Possible values are `Detection`, `Prevention` and defaults to `Prevention`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If action type is redirect, this field represents redirect URL for the client.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the resource group. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Web Application Firewall Policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Block<wbr>Response<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response body. The body must be specified in base64 encoding.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Block<wbr>Response<wbr>Status<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response status code. Possible values are `200`, `403`, `405`, `406`, or `429`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicycustomrule">[]Firewall<wbr>Policy<wbr>Custom<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}One or more `custom_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Is the policy a enabled state or disabled state. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Frontend<wbr>Endpoint<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}the Frontend Endpoints associated with this Front Door Web Application Firewall policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Resource location.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Managed<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedrule">[]Firewall<wbr>Policy<wbr>Managed<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}One or more `managed_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The firewall policy mode. Possible values are `Detection`, `Prevention` and defaults to `Prevention`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If action type is redirect, this field represents redirect URL for the client.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Web Application Firewall Policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Block<wbr>Response<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response body. The body must be specified in base64 encoding.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Block<wbr>Response<wbr>Status<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response status code. Possible values are `200`, `403`, `405`, `406`, or `429`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicycustomrule">Firewall<wbr>Policy<wbr>Custom<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `custom_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Is the policy a enabled state or disabled state. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>frontend<wbr>Endpoint<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}the Frontend Endpoints associated with this Front Door Web Application Firewall policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Resource location.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>managed<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedrule">Firewall<wbr>Policy<wbr>Managed<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `managed_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The firewall policy mode. Possible values are `Detection`, `Prevention` and defaults to `Prevention`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If action type is redirect, this field represents redirect URL for the client.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the resource group. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Web Application Firewall Policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>block_<wbr>response_<wbr>body</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response body. The body must be specified in base64 encoding.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>block_<wbr>response_<wbr>status_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}If a `custom_rule` block's action type is `block`, this is the response status code. Possible values are `200`, `403`, `405`, `406`, or `429`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicycustomrule">List[Firewall<wbr>Policy<wbr>Custom<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}One or more `custom_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the policy a enabled state or disabled state. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>frontend_<wbr>endpoint_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}the Frontend Endpoints associated with this Front Door Web Application Firewall policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Resource location.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>managed_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedrule">List[Firewall<wbr>Policy<wbr>Managed<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}One or more `managed_rule` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The firewall policy mode. Possible values are `Detection`, `Prevention` and defaults to `Prevention`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>redirect_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If action type is redirect, this field represents redirect URL for the client.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the resource group. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Web Application Firewall Policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Firewall<wbr>Policy<wbr>Custom<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#FirewallPolicyCustomRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#FirewallPolicyCustomRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyCustomRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyCustomRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The action to perform when the rule is matched. Possible values are `Allow`, `Block`, `Log`, or `Redirect`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Is the rule is enabled or disabled? Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicycustomrulematchcondition">List&lt;Pulumi.<wbr>Azure.<wbr>Front<wbr>Door.<wbr>Inputs.<wbr>Firewall<wbr>Policy<wbr>Custom<wbr>Rule<wbr>Match<wbr>Condition<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `match_condition` block defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Gets name of the resource that is unique within a policy. This name can be used to access the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The priority of the rule. Rules with a lower value will be evaluated before rules with a higher value. Defaults to `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rate<wbr>Limit<wbr>Duration<wbr>In<wbr>Minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The rate limit duration in minutes. Defaults to `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rate<wbr>Limit<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The rate limit threshold. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of rule. Possible values are `MatchRule` or `RateLimitRule`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The action to perform when the rule is matched. Possible values are `Allow`, `Block`, `Log`, or `Redirect`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Is the rule is enabled or disabled? Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicycustomrulematchcondition">[]Firewall<wbr>Policy<wbr>Custom<wbr>Rule<wbr>Match<wbr>Condition</a></span>
    </dt>
    <dd>{{% md %}}One or more `match_condition` block defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Gets name of the resource that is unique within a policy. This name can be used to access the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The priority of the rule. Rules with a lower value will be evaluated before rules with a higher value. Defaults to `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rate<wbr>Limit<wbr>Duration<wbr>In<wbr>Minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The rate limit duration in minutes. Defaults to `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rate<wbr>Limit<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The rate limit threshold. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of rule. Possible values are `MatchRule` or `RateLimitRule`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The action to perform when the rule is matched. Possible values are `Allow`, `Block`, `Log`, or `Redirect`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Is the rule is enabled or disabled? Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicycustomrulematchcondition">Firewall<wbr>Policy<wbr>Custom<wbr>Rule<wbr>Match<wbr>Condition[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `match_condition` block defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Gets name of the resource that is unique within a policy. This name can be used to access the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The priority of the rule. Rules with a lower value will be evaluated before rules with a higher value. Defaults to `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rate<wbr>Limit<wbr>Duration<wbr>In<wbr>Minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The rate limit duration in minutes. Defaults to `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rate<wbr>Limit<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The rate limit threshold. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of rule. Possible values are `MatchRule` or `RateLimitRule`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>action</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The action to perform when the rule is matched. Possible values are `Allow`, `Block`, `Log`, or `Redirect`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the rule is enabled or disabled? Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicycustomrulematchcondition">List[Firewall<wbr>Policy<wbr>Custom<wbr>Rule<wbr>Match<wbr>Condition]</a></span>
    </dt>
    <dd>{{% md %}}One or more `match_condition` block defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Gets name of the resource that is unique within a policy. This name can be used to access the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The priority of the rule. Rules with a lower value will be evaluated before rules with a higher value. Defaults to `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rate<wbr>Limit<wbr>Duration<wbr>In<wbr>Minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The rate limit duration in minutes. Defaults to `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rate<wbr>Limit<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The rate limit threshold. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of rule. Possible values are `MatchRule` or `RateLimitRule`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Firewall<wbr>Policy<wbr>Custom<wbr>Rule<wbr>Match<wbr>Condition</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#FirewallPolicyCustomRuleMatchCondition">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#FirewallPolicyCustomRuleMatchCondition">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyCustomRuleMatchConditionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyCustomRuleMatchConditionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Match<wbr>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}Up to `100` possible values to match.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Match<wbr>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The request variable to compare with. Possible values are `Cookies`, `PostArgs`, `QueryString`, `RemoteAddr`, `RequestBody`, `RequestHeader`, `RequestMethod`, or `RequestUri`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Negation<wbr>Condition</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should the result of the condition be negated.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Comparison type to use for matching with the variable value. Possible values are `Any`, `BeginsWith`, `Contains`, `EndsWith`, `Equal`, `GeoMatch`, `GreaterThan`, `GreaterThanOrEqual`, `IPMatch`, `LessThan`, `LessThanOrEqual` or `RegEx`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Match against a specific key if the `match_variable` is `QueryString`, `PostArgs`, `RequestHeader` or `Cookies`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Transforms</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Up to `5` transforms to apply. Possible values are `Lowercase`, `RemoveNulls`, `Trim`, `Uppercase`, `URLDecode` or`URLEncode`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Match<wbr>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Up to `100` possible values to match.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Match<wbr>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The request variable to compare with. Possible values are `Cookies`, `PostArgs`, `QueryString`, `RemoteAddr`, `RequestBody`, `RequestHeader`, `RequestMethod`, or `RequestUri`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Negation<wbr>Condition</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should the result of the condition be negated.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Comparison type to use for matching with the variable value. Possible values are `Any`, `BeginsWith`, `Contains`, `EndsWith`, `Equal`, `GeoMatch`, `GreaterThan`, `GreaterThanOrEqual`, `IPMatch`, `LessThan`, `LessThanOrEqual` or `RegEx`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Match against a specific key if the `match_variable` is `QueryString`, `PostArgs`, `RequestHeader` or `Cookies`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Transforms</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Up to `5` transforms to apply. Possible values are `Lowercase`, `RemoveNulls`, `Trim`, `Uppercase`, `URLDecode` or`URLEncode`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>match<wbr>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Up to `100` possible values to match.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>match<wbr>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The request variable to compare with. Possible values are `Cookies`, `PostArgs`, `QueryString`, `RemoteAddr`, `RequestBody`, `RequestHeader`, `RequestMethod`, or `RequestUri`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>negation<wbr>Condition</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should the result of the condition be negated.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Comparison type to use for matching with the variable value. Possible values are `Any`, `BeginsWith`, `Contains`, `EndsWith`, `Equal`, `GeoMatch`, `GreaterThan`, `GreaterThanOrEqual`, `IPMatch`, `LessThan`, `LessThanOrEqual` or `RegEx`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Match against a specific key if the `match_variable` is `QueryString`, `PostArgs`, `RequestHeader` or `Cookies`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>transforms</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Up to `5` transforms to apply. Possible values are `Lowercase`, `RemoveNulls`, `Trim`, `Uppercase`, `URLDecode` or`URLEncode`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>match<wbr>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Up to `100` possible values to match.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>match<wbr>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The request variable to compare with. Possible values are `Cookies`, `PostArgs`, `QueryString`, `RemoteAddr`, `RequestBody`, `RequestHeader`, `RequestMethod`, or `RequestUri`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>negation<wbr>Condition</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should the result of the condition be negated.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Comparison type to use for matching with the variable value. Possible values are `Any`, `BeginsWith`, `Contains`, `EndsWith`, `Equal`, `GeoMatch`, `GreaterThan`, `GreaterThanOrEqual`, `IPMatch`, `LessThan`, `LessThanOrEqual` or `RegEx`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Match against a specific key if the `match_variable` is `QueryString`, `PostArgs`, `RequestHeader` or `Cookies`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>transforms</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Up to `5` transforms to apply. Possible values are `Lowercase`, `RemoveNulls`, `Trim`, `Uppercase`, `URLDecode` or`URLEncode`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Firewall<wbr>Policy<wbr>Managed<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#FirewallPolicyManagedRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#FirewallPolicyManagedRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyManagedRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyManagedRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Exclusions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleexclusion">List&lt;Pulumi.<wbr>Azure.<wbr>Front<wbr>Door.<wbr>Inputs.<wbr>Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Exclusion<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `exclusion` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleoverride">List&lt;Pulumi.<wbr>Azure.<wbr>Front<wbr>Door.<wbr>Inputs.<wbr>Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `override` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the managed rule to use with this resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version on the managed rule to use with this resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Exclusions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleexclusion">[]Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Exclusion</a></span>
    </dt>
    <dd>{{% md %}}One or more `exclusion` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleoverride">[]Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override</a></span>
    </dt>
    <dd>{{% md %}}One or more `override` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the managed rule to use with this resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version on the managed rule to use with this resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>exclusions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleexclusion">Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Exclusion[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `exclusion` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleoverride">Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `override` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the managed rule to use with this resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version on the managed rule to use with this resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>exclusions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleexclusion">List[Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Exclusion]</a></span>
    </dt>
    <dd>{{% md %}}One or more `exclusion` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleoverride">List[Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override]</a></span>
    </dt>
    <dd>{{% md %}}One or more `override` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the managed rule to use with this resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The version on the managed rule to use with this resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Exclusion</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#FirewallPolicyManagedRuleExclusion">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#FirewallPolicyManagedRuleExclusion">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyManagedRuleExclusionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyManagedRuleExclusionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Match<wbr>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The variable type to be excluded. Possible values are `QueryStringArgNames`, `RequestBodyPostArgNames`, `RequestCookieNames`, `RequestHeaderNames`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: `Equals`, `Contains`, `StartsWith`, `EndsWith`, `EqualsAny`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Selector for the value in the `match_variable` attribute this exclusion applies to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Match<wbr>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The variable type to be excluded. Possible values are `QueryStringArgNames`, `RequestBodyPostArgNames`, `RequestCookieNames`, `RequestHeaderNames`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: `Equals`, `Contains`, `StartsWith`, `EndsWith`, `EqualsAny`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Selector for the value in the `match_variable` attribute this exclusion applies to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>match<wbr>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The variable type to be excluded. Possible values are `QueryStringArgNames`, `RequestBodyPostArgNames`, `RequestCookieNames`, `RequestHeaderNames`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: `Equals`, `Contains`, `StartsWith`, `EndsWith`, `EqualsAny`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Selector for the value in the `match_variable` attribute this exclusion applies to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>match<wbr>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The variable type to be excluded. Possible values are `QueryStringArgNames`, `RequestBodyPostArgNames`, `RequestCookieNames`, `RequestHeaderNames`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: `Equals`, `Contains`, `StartsWith`, `EndsWith`, `EqualsAny`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Selector for the value in the `match_variable` attribute this exclusion applies to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#FirewallPolicyManagedRuleOverride">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#FirewallPolicyManagedRuleOverride">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyManagedRuleOverrideArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyManagedRuleOverrideOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Exclusions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleoverrideexclusion">List&lt;Pulumi.<wbr>Azure.<wbr>Front<wbr>Door.<wbr>Inputs.<wbr>Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override<wbr>Exclusion<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `exclusion` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rule<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The managed rule group to override.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleoverriderule">List&lt;Pulumi.<wbr>Azure.<wbr>Front<wbr>Door.<wbr>Inputs.<wbr>Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `rule` blocks as defined below. If none are specified, all of the rules in the group will be disabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Exclusions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleoverrideexclusion">[]Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override<wbr>Exclusion</a></span>
    </dt>
    <dd>{{% md %}}One or more `exclusion` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rule<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The managed rule group to override.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleoverriderule">[]Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}One or more `rule` blocks as defined below. If none are specified, all of the rules in the group will be disabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>exclusions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleoverrideexclusion">Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override<wbr>Exclusion[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `exclusion` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rule<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The managed rule group to override.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleoverriderule">Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `rule` blocks as defined below. If none are specified, all of the rules in the group will be disabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>exclusions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleoverrideexclusion">List[Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override<wbr>Exclusion]</a></span>
    </dt>
    <dd>{{% md %}}One or more `exclusion` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rule<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The managed rule group to override.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleoverriderule">List[Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}One or more `rule` blocks as defined below. If none are specified, all of the rules in the group will be disabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override<wbr>Exclusion</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#FirewallPolicyManagedRuleOverrideExclusion">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#FirewallPolicyManagedRuleOverrideExclusion">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyManagedRuleOverrideExclusionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyManagedRuleOverrideExclusionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Match<wbr>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The variable type to be excluded. Possible values are `QueryStringArgNames`, `RequestBodyPostArgNames`, `RequestCookieNames`, `RequestHeaderNames`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: `Equals`, `Contains`, `StartsWith`, `EndsWith`, `EqualsAny`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Selector for the value in the `match_variable` attribute this exclusion applies to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Match<wbr>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The variable type to be excluded. Possible values are `QueryStringArgNames`, `RequestBodyPostArgNames`, `RequestCookieNames`, `RequestHeaderNames`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: `Equals`, `Contains`, `StartsWith`, `EndsWith`, `EqualsAny`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Selector for the value in the `match_variable` attribute this exclusion applies to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>match<wbr>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The variable type to be excluded. Possible values are `QueryStringArgNames`, `RequestBodyPostArgNames`, `RequestCookieNames`, `RequestHeaderNames`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: `Equals`, `Contains`, `StartsWith`, `EndsWith`, `EqualsAny`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Selector for the value in the `match_variable` attribute this exclusion applies to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>match<wbr>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The variable type to be excluded. Possible values are `QueryStringArgNames`, `RequestBodyPostArgNames`, `RequestCookieNames`, `RequestHeaderNames`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: `Equals`, `Contains`, `StartsWith`, `EndsWith`, `EqualsAny`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Selector for the value in the `match_variable` attribute this exclusion applies to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#FirewallPolicyManagedRuleOverrideRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#FirewallPolicyManagedRuleOverrideRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyManagedRuleOverrideRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyManagedRuleOverrideRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The action to be applied when the rule matches. Possible values are `Allow`, `Block`, `Log`, or `Redirect`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Is the managed rule override enabled or disabled. Defaults to `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Exclusions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleoverrideruleexclusion">List&lt;Pulumi.<wbr>Azure.<wbr>Front<wbr>Door.<wbr>Inputs.<wbr>Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override<wbr>Rule<wbr>Exclusion<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `exclusion` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rule<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Identifier for the managed rule.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The action to be applied when the rule matches. Possible values are `Allow`, `Block`, `Log`, or `Redirect`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Is the managed rule override enabled or disabled. Defaults to `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Exclusions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleoverrideruleexclusion">[]Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override<wbr>Rule<wbr>Exclusion</a></span>
    </dt>
    <dd>{{% md %}}One or more `exclusion` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rule<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Identifier for the managed rule.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The action to be applied when the rule matches. Possible values are `Allow`, `Block`, `Log`, or `Redirect`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Is the managed rule override enabled or disabled. Defaults to `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>exclusions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleoverrideruleexclusion">Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override<wbr>Rule<wbr>Exclusion[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `exclusion` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rule<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Identifier for the managed rule.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>action</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The action to be applied when the rule matches. Possible values are `Allow`, `Block`, `Log`, or `Redirect`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the managed rule override enabled or disabled. Defaults to `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>exclusions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#firewallpolicymanagedruleoverrideruleexclusion">List[Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override<wbr>Rule<wbr>Exclusion]</a></span>
    </dt>
    <dd>{{% md %}}One or more `exclusion` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rule_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Identifier for the managed rule.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Firewall<wbr>Policy<wbr>Managed<wbr>Rule<wbr>Override<wbr>Rule<wbr>Exclusion</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#FirewallPolicyManagedRuleOverrideRuleExclusion">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#FirewallPolicyManagedRuleOverrideRuleExclusion">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyManagedRuleOverrideRuleExclusionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/frontdoor?tab=doc#FirewallPolicyManagedRuleOverrideRuleExclusionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Match<wbr>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The variable type to be excluded. Possible values are `QueryStringArgNames`, `RequestBodyPostArgNames`, `RequestCookieNames`, `RequestHeaderNames`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: `Equals`, `Contains`, `StartsWith`, `EndsWith`, `EqualsAny`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Selector for the value in the `match_variable` attribute this exclusion applies to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Match<wbr>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The variable type to be excluded. Possible values are `QueryStringArgNames`, `RequestBodyPostArgNames`, `RequestCookieNames`, `RequestHeaderNames`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: `Equals`, `Contains`, `StartsWith`, `EndsWith`, `EqualsAny`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Selector for the value in the `match_variable` attribute this exclusion applies to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>match<wbr>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The variable type to be excluded. Possible values are `QueryStringArgNames`, `RequestBodyPostArgNames`, `RequestCookieNames`, `RequestHeaderNames`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: `Equals`, `Contains`, `StartsWith`, `EndsWith`, `EqualsAny`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Selector for the value in the `match_variable` attribute this exclusion applies to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>match<wbr>Variable</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The variable type to be excluded. Possible values are `QueryStringArgNames`, `RequestBodyPostArgNames`, `RequestCookieNames`, `RequestHeaderNames`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Comparison operator to apply to the selector when specifying which elements in the collection this exclusion applies to. Possible values are: `Equals`, `Contains`, `StartsWith`, `EndsWith`, `EqualsAny`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Selector for the value in the `match_variable` attribute this exclusion applies to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







