
---
title: "Server"
block_external_search_index: true
---



Creates an Authorization Server.

This resource allows you to create and configure an Authorization Server.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as okta from "@pulumi/okta";

const example = new okta.auth.Server("example", {
    audiences: ["api://example"],
    description: "My Example Auth Server",
    issuerMode: "CUSTOM_URL",
    status: "ACTIVE",
});
```

> This content is derived from https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/auth_server.html.markdown.



## Create a Server Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/auth/#Server">Server</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/auth/#ServerArgs">ServerArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Server</span><span class="p">(resource_name, opts=None, </span>audiences=None<span class="p">, </span>credentials_rotation_mode=None<span class="p">, </span>description=None<span class="p">, </span>issuer_mode=None<span class="p">, </span>name=None<span class="p">, </span>status=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewServer<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/auth?tab=doc#ServerArgs">ServerArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/auth?tab=doc#Server">Server</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.Auth.Server.html">Server</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.Auth.ServerArgs.html">ServerArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The recipients that the tokens are intended for. This becomes the `aud` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Credentials<wbr>Rotation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key rotation mode for the authorization server. Can be `"AUTO"` or `"MANUAL"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issuer<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Allows you to use a custom issuer URL. It can be set to `"CUSTOM_URL"` or `"ORG_URL"`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The status of the auth server. It defaults to `"ACTIVE"`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The recipients that the tokens are intended for. This becomes the `aud` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Credentials<wbr>Rotation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The key rotation mode for the authorization server. Can be `"AUTO"` or `"MANUAL"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The description of the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issuer<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Allows you to use a custom issuer URL. It can be set to `"CUSTOM_URL"` or `"ORG_URL"`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The status of the auth server. It defaults to `"ACTIVE"`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The recipients that the tokens are intended for. This becomes the `aud` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>credentials<wbr>Rotation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key rotation mode for the authorization server. Can be `"AUTO"` or `"MANUAL"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issuer<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Allows you to use a custom issuer URL. It can be set to `"CUSTOM_URL"` or `"ORG_URL"`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The status of the auth server. It defaults to `"ACTIVE"`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The recipients that the tokens are intended for. This becomes the `aud` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>credentials_<wbr>rotation_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The key rotation mode for the authorization server. Can be `"AUTO"` or `"MANUAL"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description of the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issuer_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Allows you to use a custom issuer URL. It can be set to `"CUSTOM_URL"` or `"ORG_URL"`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The status of the auth server. It defaults to `"ACTIVE"`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Server Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The recipients that the tokens are intended for. This becomes the `aud` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Credentials<wbr>Last<wbr>Rotated</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The timestamp when the authorization server started to use the `kid` for signing tokens.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Credentials<wbr>Next<wbr>Rotation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The timestamp when the authorization server changes the key for signing tokens. Only returned when `credentials_rotation_mode` is `"AUTO"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Credentials<wbr>Rotation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key rotation mode for the authorization server. Can be `"AUTO"` or `"MANUAL"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of the authorization server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The complete URL for a Custom Authorization Server. This becomes the `iss` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Issuer<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Allows you to use a custom issuer URL. It can be set to `"CUSTOM_URL"` or `"ORG_URL"`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the JSON Web Key used for signing tokens issued by the authorization server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the authorization server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The status of the auth server. It defaults to `"ACTIVE"`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The recipients that the tokens are intended for. This becomes the `aud` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Credentials<wbr>Last<wbr>Rotated</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The timestamp when the authorization server started to use the `kid` for signing tokens.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Credentials<wbr>Next<wbr>Rotation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The timestamp when the authorization server changes the key for signing tokens. Only returned when `credentials_rotation_mode` is `"AUTO"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Credentials<wbr>Rotation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The key rotation mode for the authorization server. Can be `"AUTO"` or `"MANUAL"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The description of the authorization server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The complete URL for a Custom Authorization Server. This becomes the `iss` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Issuer<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Allows you to use a custom issuer URL. It can be set to `"CUSTOM_URL"` or `"ORG_URL"`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the JSON Web Key used for signing tokens issued by the authorization server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the authorization server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The status of the auth server. It defaults to `"ACTIVE"`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The recipients that the tokens are intended for. This becomes the `aud` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>credentials<wbr>Last<wbr>Rotated</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The timestamp when the authorization server started to use the `kid` for signing tokens.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>credentials<wbr>Next<wbr>Rotation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The timestamp when the authorization server changes the key for signing tokens. Only returned when `credentials_rotation_mode` is `"AUTO"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>credentials<wbr>Rotation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key rotation mode for the authorization server. Can be `"AUTO"` or `"MANUAL"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of the authorization server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The complete URL for a Custom Authorization Server. This becomes the `iss` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>issuer<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Allows you to use a custom issuer URL. It can be set to `"CUSTOM_URL"` or `"ORG_URL"`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the JSON Web Key used for signing tokens issued by the authorization server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the authorization server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The status of the auth server. It defaults to `"ACTIVE"`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The recipients that the tokens are intended for. This becomes the `aud` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>credentials_<wbr>last_<wbr>rotated</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The timestamp when the authorization server started to use the `kid` for signing tokens.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>credentials_<wbr>next_<wbr>rotation</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The timestamp when the authorization server changes the key for signing tokens. Only returned when `credentials_rotation_mode` is `"AUTO"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>credentials_<wbr>rotation_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The key rotation mode for the authorization server. Can be `"AUTO"` or `"MANUAL"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description of the authorization server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The complete URL for a Custom Authorization Server. This becomes the `iss` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>issuer_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Allows you to use a custom issuer URL. It can be set to `"CUSTOM_URL"` or `"ORG_URL"`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kid</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the JSON Web Key used for signing tokens issued by the authorization server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the authorization server.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The status of the auth server. It defaults to `"ACTIVE"`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Server Resource

Get an existing Server resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/auth/#ServerState">ServerState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/auth/#Server">Server</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>audiences=None<span class="p">, </span>credentials_last_rotated=None<span class="p">, </span>credentials_next_rotation=None<span class="p">, </span>credentials_rotation_mode=None<span class="p">, </span>description=None<span class="p">, </span>issuer=None<span class="p">, </span>issuer_mode=None<span class="p">, </span>kid=None<span class="p">, </span>name=None<span class="p">, </span>status=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetServer<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/auth?tab=doc#ServerState">ServerState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/go/okta/auth?tab=doc#Server">Server</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.Auth.Server.html">Server</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.Auth.ServerState.html">ServerState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The recipients that the tokens are intended for. This becomes the `aud` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Credentials<wbr>Last<wbr>Rotated</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The timestamp when the authorization server started to use the `kid` for signing tokens.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Credentials<wbr>Next<wbr>Rotation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The timestamp when the authorization server changes the key for signing tokens. Only returned when `credentials_rotation_mode` is `"AUTO"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Credentials<wbr>Rotation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key rotation mode for the authorization server. Can be `"AUTO"` or `"MANUAL"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The complete URL for a Custom Authorization Server. This becomes the `iss` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issuer<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Allows you to use a custom issuer URL. It can be set to `"CUSTOM_URL"` or `"ORG_URL"`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the JSON Web Key used for signing tokens issued by the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The status of the auth server. It defaults to `"ACTIVE"`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The recipients that the tokens are intended for. This becomes the `aud` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Credentials<wbr>Last<wbr>Rotated</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The timestamp when the authorization server started to use the `kid` for signing tokens.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Credentials<wbr>Next<wbr>Rotation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The timestamp when the authorization server changes the key for signing tokens. Only returned when `credentials_rotation_mode` is `"AUTO"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Credentials<wbr>Rotation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The key rotation mode for the authorization server. Can be `"AUTO"` or `"MANUAL"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The description of the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The complete URL for a Custom Authorization Server. This becomes the `iss` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issuer<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Allows you to use a custom issuer URL. It can be set to `"CUSTOM_URL"` or `"ORG_URL"`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kid</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the JSON Web Key used for signing tokens issued by the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The status of the auth server. It defaults to `"ACTIVE"`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The recipients that the tokens are intended for. This becomes the `aud` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>credentials<wbr>Last<wbr>Rotated</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The timestamp when the authorization server started to use the `kid` for signing tokens.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>credentials<wbr>Next<wbr>Rotation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The timestamp when the authorization server changes the key for signing tokens. Only returned when `credentials_rotation_mode` is `"AUTO"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>credentials<wbr>Rotation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key rotation mode for the authorization server. Can be `"AUTO"` or `"MANUAL"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The complete URL for a Custom Authorization Server. This becomes the `iss` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issuer<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Allows you to use a custom issuer URL. It can be set to `"CUSTOM_URL"` or `"ORG_URL"`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the JSON Web Key used for signing tokens issued by the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The status of the auth server. It defaults to `"ACTIVE"`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The recipients that the tokens are intended for. This becomes the `aud` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>credentials_<wbr>last_<wbr>rotated</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The timestamp when the authorization server started to use the `kid` for signing tokens.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>credentials_<wbr>next_<wbr>rotation</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The timestamp when the authorization server changes the key for signing tokens. Only returned when `credentials_rotation_mode` is `"AUTO"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>credentials_<wbr>rotation_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The key rotation mode for the authorization server. Can be `"AUTO"` or `"MANUAL"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description of the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The complete URL for a Custom Authorization Server. This becomes the `iss` claim in an access token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issuer_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Allows you to use a custom issuer URL. It can be set to `"CUSTOM_URL"` or `"ORG_URL"`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kid</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the JSON Web Key used for signing tokens issued by the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the authorization server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The status of the auth server. It defaults to `"ACTIVE"`
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

