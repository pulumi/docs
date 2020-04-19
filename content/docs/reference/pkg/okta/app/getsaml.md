
---
title: "GetSaml"
block_external_search_index: true
---



Use this data source to retrieve the collaborators for a given repository.

{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as okta from "@pulumi/okta";

const example = pulumi.output(okta.app.getSaml({
    label: "Example App",
}, { async: true }));
```

{{% /example %}}
{{% /examples %}}





## Using GetSaml {#using}

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getSaml<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/app/#GetSamlArgs">GetSamlArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/okta/app/#GetSamlResult">GetSamlResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_saml(</span>accessibility_error_redirect_url=None<span class="p">, </span>accessibility_login_redirect_url=None<span class="p">, </span>accessibility_self_service=None<span class="p">, </span>active_only=None<span class="p">, </span>app_settings_json=None<span class="p">, </span>assertion_signed=None<span class="p">, </span>attribute_statements=None<span class="p">, </span>audience=None<span class="p">, </span>authn_context_class_ref=None<span class="p">, </span>auto_submit_toolbar=None<span class="p">, </span>default_relay_state=None<span class="p">, </span>destination=None<span class="p">, </span>digest_algorithm=None<span class="p">, </span>features=None<span class="p">, </span>hide_ios=None<span class="p">, </span>hide_web=None<span class="p">, </span>honor_force_authn=None<span class="p">, </span>id=None<span class="p">, </span>idp_issuer=None<span class="p">, </span>label=None<span class="p">, </span>label_prefix=None<span class="p">, </span>recipient=None<span class="p">, </span>request_compressed=None<span class="p">, </span>response_signed=None<span class="p">, </span>signature_algorithm=None<span class="p">, </span>sp_issuer=None<span class="p">, </span>sso_url=None<span class="p">, </span>subject_name_id_format=None<span class="p">, </span>subject_name_id_template=None<span class="p">, </span>user_name_template=None<span class="p">, </span>user_name_template_suffix=None<span class="p">, </span>user_name_template_type=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupSaml<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/v2/go/okta/app?tab=doc#LookupSamlArgs">LookupSamlArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/v2/go/okta/app?tab=doc#LookupSamlResult">LookupSamlResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetSaml </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.App.GetSamlResult.html">GetSamlResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Okta/Pulumi.Okta.App.GetSamlArgs.html">GetSamlArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Accessibility<wbr>Error<wbr>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Custom error page URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Accessibility<wbr>Login<wbr>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Custom login page URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Accessibility<wbr>Self<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable self service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Active<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}tells the provider to query for only `ACTIVE` applications.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Settings<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Application settings in JSON format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Assertion<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether the SAML assertion is digitally signed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Attribute<wbr>Statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsamlattributestatement">List&lt;Get<wbr>Saml<wbr>Attribute<wbr>Statement<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}SAML Attribute statements.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Audience</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Audience restriction.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authn<wbr>Context<wbr>Class<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the SAML authentication context class for the assertion’s authentication statement.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Submit<wbr>Toolbar</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Display auto submit toolbar.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Relay<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies a specific application resource in an IDP initiated SSO scenario.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the location where the SAML response is intended to be sent inside of the SAML assertion.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Digest<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Determines the digest algorithm used to digitally sign the SAML assertion and response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Features</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}features enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hide<wbr>Ios</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Do not display application icon on mobile app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hide<wbr>Web</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Do not display application icon to users
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Honor<wbr>Force<wbr>Authn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Prompt user to re-authenticate if SP asks for it.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}`id` of application to retrieve, conflicts with `label` and `label_prefix`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Idp<wbr>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}SAML issuer ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The label of the app to retrieve, conflicts with `label_prefix` and `id`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Label<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Label prefix of the app to retrieve, conflicts with `label` and `id`. This will tell the provider to do a `starts with` query as opposed to an `equals` query.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recipient</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The location where the app may present the SAML assertion.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Compressed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Denotes whether the request is compressed or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether the SAML auth response message is digitally signed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Signature<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Signature algorithm used ot digitally sign the assertion and response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sp<wbr>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}SAML service provider issuer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sso<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Single Sign on Url.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subject<wbr>Name<wbr>Id<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the SAML processing rules.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subject<wbr>Name<wbr>Id<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Template for app user's username when a user is assigned to the app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Name<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Username template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Name<wbr>Template<wbr>Suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Username template suffix.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Name<wbr>Template<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Username template type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Accessibility<wbr>Error<wbr>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Custom error page URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Accessibility<wbr>Login<wbr>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Custom login page URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Accessibility<wbr>Self<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable self service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Active<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}tells the provider to query for only `ACTIVE` applications.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Settings<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Application settings in JSON format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Assertion<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether the SAML assertion is digitally signed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Attribute<wbr>Statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsamlattributestatement">[]Get<wbr>Saml<wbr>Attribute<wbr>Statement</a></span>
    </dt>
    <dd>{{% md %}}SAML Attribute statements.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Audience</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Audience restriction.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authn<wbr>Context<wbr>Class<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the SAML authentication context class for the assertion’s authentication statement.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Submit<wbr>Toolbar</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Display auto submit toolbar.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Relay<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies a specific application resource in an IDP initiated SSO scenario.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the location where the SAML response is intended to be sent inside of the SAML assertion.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Digest<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Determines the digest algorithm used to digitally sign the SAML assertion and response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Features</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}features enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hide<wbr>Ios</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Do not display application icon on mobile app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hide<wbr>Web</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Do not display application icon to users
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Honor<wbr>Force<wbr>Authn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Prompt user to re-authenticate if SP asks for it.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}`id` of application to retrieve, conflicts with `label` and `label_prefix`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Idp<wbr>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}SAML issuer ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The label of the app to retrieve, conflicts with `label_prefix` and `id`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Label<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Label prefix of the app to retrieve, conflicts with `label` and `id`. This will tell the provider to do a `starts with` query as opposed to an `equals` query.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recipient</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The location where the app may present the SAML assertion.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Compressed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Denotes whether the request is compressed or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether the SAML auth response message is digitally signed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Signature<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Signature algorithm used ot digitally sign the assertion and response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sp<wbr>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}SAML service provider issuer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sso<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Single Sign on Url.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subject<wbr>Name<wbr>Id<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the SAML processing rules.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subject<wbr>Name<wbr>Id<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Template for app user's username when a user is assigned to the app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Name<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Username template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Name<wbr>Template<wbr>Suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Username template suffix.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Name<wbr>Template<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Username template type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accessibility<wbr>Error<wbr>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Custom error page URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>accessibility<wbr>Login<wbr>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Custom login page URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>accessibility<wbr>Self<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable self service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>active<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}tells the provider to query for only `ACTIVE` applications.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Settings<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Application settings in JSON format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>assertion<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Determines whether the SAML assertion is digitally signed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>attribute<wbr>Statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsamlattributestatement">Get<wbr>Saml<wbr>Attribute<wbr>Statement[]</a></span>
    </dt>
    <dd>{{% md %}}SAML Attribute statements.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>audience</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Audience restriction.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authn<wbr>Context<wbr>Class<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the SAML authentication context class for the assertion’s authentication statement.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Submit<wbr>Toolbar</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Display auto submit toolbar.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Relay<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies a specific application resource in an IDP initiated SSO scenario.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the location where the SAML response is intended to be sent inside of the SAML assertion.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>digest<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Determines the digest algorithm used to digitally sign the SAML assertion and response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>features</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}features enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hide<wbr>Ios</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Do not display application icon on mobile app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hide<wbr>Web</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Do not display application icon to users
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>honor<wbr>Force<wbr>Authn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Prompt user to re-authenticate if SP asks for it.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}`id` of application to retrieve, conflicts with `label` and `label_prefix`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>idp<wbr>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}SAML issuer ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The label of the app to retrieve, conflicts with `label_prefix` and `id`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>label<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Label prefix of the app to retrieve, conflicts with `label` and `id`. This will tell the provider to do a `starts with` query as opposed to an `equals` query.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recipient</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The location where the app may present the SAML assertion.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Compressed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Denotes whether the request is compressed or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Determines whether the SAML auth response message is digitally signed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>signature<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Signature algorithm used ot digitally sign the assertion and response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sp<wbr>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}SAML service provider issuer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sso<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Single Sign on Url.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subject<wbr>Name<wbr>Id<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the SAML processing rules.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subject<wbr>Name<wbr>Id<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Template for app user's username when a user is assigned to the app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user<wbr>Name<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Username template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user<wbr>Name<wbr>Template<wbr>Suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Username template suffix.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user<wbr>Name<wbr>Template<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Username template type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accessibility_<wbr>error_<wbr>redirect_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Custom error page URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>accessibility_<wbr>login_<wbr>redirect_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Custom login page URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>accessibility_<wbr>self_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable self service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>active_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}tells the provider to query for only `ACTIVE` applications.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>app_<wbr>settings_<wbr>json</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Application settings in JSON format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>assertion_<wbr>signed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether the SAML assertion is digitally signed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>attribute_<wbr>statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsamlattributestatement">List[Get<wbr>Saml<wbr>Attribute<wbr>Statement]</a></span>
    </dt>
    <dd>{{% md %}}SAML Attribute statements.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>audience</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Audience restriction.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authn_<wbr>context_<wbr>class_<wbr>ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Identifies the SAML authentication context class for the assertion’s authentication statement.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto_<wbr>submit_<wbr>toolbar</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Display auto submit toolbar.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>relay_<wbr>state</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Identifies a specific application resource in an IDP initiated SSO scenario.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Identifies the location where the SAML response is intended to be sent inside of the SAML assertion.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>digest_<wbr>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Determines the digest algorithm used to digitally sign the SAML assertion and response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>features</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}features enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hide_<wbr>ios</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Do not display application icon on mobile app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hide_<wbr>web</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Do not display application icon to users
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>honor_<wbr>force_<wbr>authn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Prompt user to re-authenticate if SP asks for it.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}`id` of application to retrieve, conflicts with `label` and `label_prefix`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>idp_<wbr>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}SAML issuer ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The label of the app to retrieve, conflicts with `label_prefix` and `id`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>label_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Label prefix of the app to retrieve, conflicts with `label` and `id`. This will tell the provider to do a `starts with` query as opposed to an `equals` query.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recipient</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The location where the app may present the SAML assertion.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request_<wbr>compressed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Denotes whether the request is compressed or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response_<wbr>signed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether the SAML auth response message is digitally signed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>signature_<wbr>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Signature algorithm used ot digitally sign the assertion and response.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sp_<wbr>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}SAML service provider issuer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sso_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Single Sign on Url.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subject_<wbr>name_<wbr>id_<wbr>format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Identifies the SAML processing rules.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subject_<wbr>name_<wbr>id_<wbr>template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Template for app user's username when a user is assigned to the app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user_<wbr>name_<wbr>template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Username template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user_<wbr>name_<wbr>template_<wbr>suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Username template suffix.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user_<wbr>name_<wbr>template_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Username template type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetSaml Result {#result}

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}description of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Certificate key ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}name of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}status of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Accessibility<wbr>Error<wbr>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Custom error page URL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Accessibility<wbr>Login<wbr>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Custom login page URL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Accessibility<wbr>Self<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable self service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Active<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>App<wbr>Settings<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Application settings in JSON format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Assertion<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether the SAML assertion is digitally signed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Attribute<wbr>Statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsamlattributestatement">List&lt;Get<wbr>Saml<wbr>Attribute<wbr>Statement&gt;</a></span>
    </dt>
    <dd>{{% md %}}SAML Attribute statements.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Audience</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Audience restriction.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Authn<wbr>Context<wbr>Class<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the SAML authentication context class for the assertion’s authentication statement.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Auto<wbr>Submit<wbr>Toolbar</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Display auto submit toolbar.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Relay<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies a specific application resource in an IDP initiated SSO scenario.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the location where the SAML response is intended to be sent inside of the SAML assertion.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Digest<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Determines the digest algorithm used to digitally sign the SAML assertion and response.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Features</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}features enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hide<wbr>Ios</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Do not display application icon on mobile app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hide<wbr>Web</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Do not display application icon to users
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Honor<wbr>Force<wbr>Authn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Prompt user to re-authenticate if SP asks for it.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}id of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Idp<wbr>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}SAML issuer ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}label of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Label<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Recipient</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The location where the app may present the SAML assertion.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Request<wbr>Compressed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Denotes whether the request is compressed or not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Response<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether the SAML auth response message is digitally signed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Signature<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Signature algorithm used ot digitally sign the assertion and response.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sp<wbr>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}SAML service provider issuer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sso<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Single Sign on Url.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subject<wbr>Name<wbr>Id<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the SAML processing rules.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subject<wbr>Name<wbr>Id<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Template for app user's username when a user is assigned to the app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Name<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Username template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Name<wbr>Template<wbr>Suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Username template suffix.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Name<wbr>Template<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Username template type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}description of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Certificate key ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}name of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}status of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Accessibility<wbr>Error<wbr>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Custom error page URL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Accessibility<wbr>Login<wbr>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Custom login page URL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Accessibility<wbr>Self<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable self service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Active<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>App<wbr>Settings<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Application settings in JSON format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Assertion<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether the SAML assertion is digitally signed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Attribute<wbr>Statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsamlattributestatement">[]Get<wbr>Saml<wbr>Attribute<wbr>Statement</a></span>
    </dt>
    <dd>{{% md %}}SAML Attribute statements.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Audience</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Audience restriction.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Authn<wbr>Context<wbr>Class<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the SAML authentication context class for the assertion’s authentication statement.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Auto<wbr>Submit<wbr>Toolbar</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Display auto submit toolbar.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Relay<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies a specific application resource in an IDP initiated SSO scenario.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the location where the SAML response is intended to be sent inside of the SAML assertion.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Digest<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Determines the digest algorithm used to digitally sign the SAML assertion and response.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Features</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}features enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hide<wbr>Ios</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Do not display application icon on mobile app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hide<wbr>Web</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Do not display application icon to users
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Honor<wbr>Force<wbr>Authn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Prompt user to re-authenticate if SP asks for it.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}id of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Idp<wbr>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}SAML issuer ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}label of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Label<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Recipient</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The location where the app may present the SAML assertion.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Request<wbr>Compressed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Denotes whether the request is compressed or not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Response<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether the SAML auth response message is digitally signed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Signature<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Signature algorithm used ot digitally sign the assertion and response.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sp<wbr>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}SAML service provider issuer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sso<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Single Sign on Url.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subject<wbr>Name<wbr>Id<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the SAML processing rules.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subject<wbr>Name<wbr>Id<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Template for app user's username when a user is assigned to the app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Name<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Username template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Name<wbr>Template<wbr>Suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Username template suffix.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Name<wbr>Template<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Username template type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}description of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Certificate key ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}name of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}status of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>accessibility<wbr>Error<wbr>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Custom error page URL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>accessibility<wbr>Login<wbr>Redirect<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Custom login page URL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>accessibility<wbr>Self<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable self service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>active<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>app<wbr>Settings<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Application settings in JSON format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>assertion<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Determines whether the SAML assertion is digitally signed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>attribute<wbr>Statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsamlattributestatement">Get<wbr>Saml<wbr>Attribute<wbr>Statement[]</a></span>
    </dt>
    <dd>{{% md %}}SAML Attribute statements.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>audience</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Audience restriction.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>authn<wbr>Context<wbr>Class<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the SAML authentication context class for the assertion’s authentication statement.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>auto<wbr>Submit<wbr>Toolbar</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Display auto submit toolbar.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default<wbr>Relay<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies a specific application resource in an IDP initiated SSO scenario.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the location where the SAML response is intended to be sent inside of the SAML assertion.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>digest<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Determines the digest algorithm used to digitally sign the SAML assertion and response.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>features</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}features enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hide<wbr>Ios</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Do not display application icon on mobile app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hide<wbr>Web</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Do not display application icon to users
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>honor<wbr>Force<wbr>Authn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Prompt user to re-authenticate if SP asks for it.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}id of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>idp<wbr>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}SAML issuer ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}label of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>label<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>recipient</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The location where the app may present the SAML assertion.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>request<wbr>Compressed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Denotes whether the request is compressed or not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>response<wbr>Signed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Determines whether the SAML auth response message is digitally signed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>signature<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Signature algorithm used ot digitally sign the assertion and response.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sp<wbr>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}SAML service provider issuer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sso<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Single Sign on Url.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subject<wbr>Name<wbr>Id<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Identifies the SAML processing rules.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subject<wbr>Name<wbr>Id<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Template for app user's username when a user is assigned to the app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user<wbr>Name<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Username template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user<wbr>Name<wbr>Template<wbr>Suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Username template suffix.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user<wbr>Name<wbr>Template<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Username template type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}description of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Certificate key ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}name of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}status of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>accessibility_<wbr>error_<wbr>redirect_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Custom error page URL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>accessibility_<wbr>login_<wbr>redirect_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Custom login page URL.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>accessibility_<wbr>self_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable self service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>active_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>app_<wbr>settings_<wbr>json</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Application settings in JSON format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>assertion_<wbr>signed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether the SAML assertion is digitally signed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>attribute_<wbr>statements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsamlattributestatement">List[Get<wbr>Saml<wbr>Attribute<wbr>Statement]</a></span>
    </dt>
    <dd>{{% md %}}SAML Attribute statements.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>audience</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Audience restriction.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>authn_<wbr>context_<wbr>class_<wbr>ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Identifies the SAML authentication context class for the assertion’s authentication statement.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>auto_<wbr>submit_<wbr>toolbar</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Display auto submit toolbar.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default_<wbr>relay_<wbr>state</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Identifies a specific application resource in an IDP initiated SSO scenario.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Identifies the location where the SAML response is intended to be sent inside of the SAML assertion.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>digest_<wbr>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Determines the digest algorithm used to digitally sign the SAML assertion and response.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>features</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}features enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hide_<wbr>ios</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Do not display application icon on mobile app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hide_<wbr>web</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Do not display application icon to users
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>honor_<wbr>force_<wbr>authn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Prompt user to re-authenticate if SP asks for it.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}id of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>idp_<wbr>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}SAML issuer ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}label of application.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>label_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>recipient</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The location where the app may present the SAML assertion.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>request_<wbr>compressed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Denotes whether the request is compressed or not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>response_<wbr>signed</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether the SAML auth response message is digitally signed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>signature_<wbr>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Signature algorithm used ot digitally sign the assertion and response.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sp_<wbr>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}SAML service provider issuer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sso_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Single Sign on Url.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subject_<wbr>name_<wbr>id_<wbr>format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Identifies the SAML processing rules.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subject_<wbr>name_<wbr>id_<wbr>template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Template for app user's username when a user is assigned to the app.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user_<wbr>name_<wbr>template</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Username template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user_<wbr>name_<wbr>template_<wbr>suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Username template suffix.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user_<wbr>name_<wbr>template_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Username template type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types


<h4 id="getsamlattributestatement">Get<wbr>Saml<wbr>Attribute<wbr>Statement</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/input/#GetSamlAttributeStatement">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/okta/types/output/#GetSamlAttributeStatement">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/v2/go/okta/app?tab=doc#GetSamlAttributeStatementArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-okta/sdk/v2/go/okta/app?tab=doc#GetSamlAttributeStatement">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}name of application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}name of application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}name of application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}name of application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}







