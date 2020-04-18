
---
title: "ServerClaim"
block_external_search_index: true
---



Creates an Authorization Server Claim.

This resource allows you to create and configure an Authorization Server Claim.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as okta from "@pulumi/okta";

const example = new okta.auth.ServerClaim("example", {
    authServerId: "<auth server id>",
    claimType: "IDENTITY",
    scopes: [okta_auth_server_scope_example.name],
    value: "String.substringAfter(user.email, \"@\") == \"example.com\"",
});
```

> This content is derived from https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server_claim.html.markdown.



## Create a ServerClaim Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/auth/#ServerClaim">ServerClaim</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/auth/#ServerClaimArgs">ServerClaimArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">ServerClaim</span><span class="p">(resource_name, opts=None, </span>always_include_in_token=None<span class="p">, </span>auth_server_id=None<span class="p">, </span>claim_type=None<span class="p">, </span>group_filter_type=None<span class="p">, </span>name=None<span class="p">, </span>scopes=None<span class="p">, </span>status=None<span class="p">, </span>value=None<span class="p">, </span>value_type=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewServerClaim<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/auth?tab=doc#ServerClaimArgs">ServerClaimArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/auth?tab=doc#ServerClaim">ServerClaim</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.Auth.ServerClaim.html">ServerClaim</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.Auth.ServerClaimArgs.html">ServerClaimArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Always<wbr>Include<wbr>In<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to include claims in token, by default is is set to `true`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Auth<wbr>Server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Application's display name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Claim<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>Filter<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the claim.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The list of scopes the auth server claim is tied to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The status of the application. It defaults to `"ACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The value of the claim.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Always<wbr>Include<wbr>In<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether to include claims in token, by default is is set to `true`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Auth<wbr>Server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Application's display name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Claim<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>Filter<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the claim.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of scopes the auth server claim is tied to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The status of the application. It defaults to `"ACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The value of the claim.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>always<wbr>Include<wbr>In<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to include claims in token, by default is is set to `true`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>auth<wbr>Server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Application's display name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>claim<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group<wbr>Filter<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the claim.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The list of scopes the auth server claim is tied to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The status of the application. It defaults to `"ACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The value of the claim.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>always_<wbr>include_<wbr>in_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether to include claims in token, by default is is set to `true`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>auth_<wbr>server_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Application's display name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>claim_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group_<wbr>filter_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the claim.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of scopes the auth server claim is tied to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The status of the application. It defaults to `"ACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The value of the claim.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## ServerClaim Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Always<wbr>Include<wbr>In<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to include claims in token, by default is is set to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Auth<wbr>Server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Application's display name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Claim<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Group<wbr>Filter<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the claim.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The list of scopes the auth server claim is tied to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The status of the application. It defaults to `"ACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The value of the claim.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Value<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Always<wbr>Include<wbr>In<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether to include claims in token, by default is is set to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Auth<wbr>Server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Application's display name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Claim<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Group<wbr>Filter<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the claim.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of scopes the auth server claim is tied to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The status of the application. It defaults to `"ACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The value of the claim.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Value<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>always<wbr>Include<wbr>In<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to include claims in token, by default is is set to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>auth<wbr>Server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Application's display name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>claim<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>group<wbr>Filter<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the claim.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The list of scopes the auth server claim is tied to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The status of the application. It defaults to `"ACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The value of the claim.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>value<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>always_<wbr>include_<wbr>in_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether to include claims in token, by default is is set to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>auth_<wbr>server_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Application's display name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>claim_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>group_<wbr>filter_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the claim.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of scopes the auth server claim is tied to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The status of the application. It defaults to `"ACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The value of the claim.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>value_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing ServerClaim Resource

Get an existing ServerClaim resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/auth/#ServerClaimState">ServerClaimState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/auth/#ServerClaim">ServerClaim</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>always_include_in_token=None<span class="p">, </span>auth_server_id=None<span class="p">, </span>claim_type=None<span class="p">, </span>group_filter_type=None<span class="p">, </span>name=None<span class="p">, </span>scopes=None<span class="p">, </span>status=None<span class="p">, </span>value=None<span class="p">, </span>value_type=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetServerClaim<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/auth?tab=doc#ServerClaimState">ServerClaimState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/auth?tab=doc#ServerClaim">ServerClaim</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.Auth.ServerClaim.html">ServerClaim</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.Auth.ServerClaimState.html">ServerClaimState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Always<wbr>Include<wbr>In<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to include claims in token, by default is is set to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Application's display name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Claim<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>Filter<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the claim.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The list of scopes the auth server claim is tied to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The status of the application. It defaults to `"ACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The value of the claim.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Always<wbr>Include<wbr>In<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether to include claims in token, by default is is set to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Application's display name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Claim<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>Filter<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the claim.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of scopes the auth server claim is tied to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The status of the application. It defaults to `"ACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The value of the claim.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>always<wbr>Include<wbr>In<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to include claims in token, by default is is set to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auth<wbr>Server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Application's display name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>claim<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group<wbr>Filter<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the claim.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The list of scopes the auth server claim is tied to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The status of the application. It defaults to `"ACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The value of the claim.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>always_<wbr>include_<wbr>in_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether to include claims in token, by default is is set to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auth_<wbr>server_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Application's display name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>claim_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies whether the claim is for an access token `"RESOURCE"` or ID token `"IDENTITY"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group_<wbr>filter_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the type of group filter if `value_type` is `"GROUPS"`. Can be set to one of the following `"STARTS_WITH"`, `"EQUALS"`, `"CONTAINS"`, `"REGEX"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the claim.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of scopes the auth server claim is tied to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The status of the application. It defaults to `"ACTIVE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The value of the claim.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of value of the claim. It can be set to `"EXPRESSION"` or `"GROUPS"`. It defaults to `"EXPRESSION"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-okta">https://github.com/pulumi/pulumi-okta</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

