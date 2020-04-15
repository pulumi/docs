
---
title: "GoogleIdentityProvider"
block_external_search_index: true
---






## Create a GoogleIdentityProvider Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/keycloak/oidc/#GoogleIdentityProvider">GoogleIdentityProvider</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/keycloak/oidc/#GoogleIdentityProviderArgs">GoogleIdentityProviderArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">GoogleIdentityProvider</span><span class="p">(resource_name, opts=None, </span>accepts_prompt_none_forward_from_client=None<span class="p">, </span>add_read_token_role_on_create=None<span class="p">, </span>authenticate_by_default=None<span class="p">, </span>client_id=None<span class="p">, </span>client_secret=None<span class="p">, </span>default_scopes=None<span class="p">, </span>disable_user_info=None<span class="p">, </span>enabled=None<span class="p">, </span>extra_config=None<span class="p">, </span>first_broker_login_flow_alias=None<span class="p">, </span>hide_on_login_page=None<span class="p">, </span>hosted_domain=None<span class="p">, </span>link_only=None<span class="p">, </span>post_broker_login_flow_alias=None<span class="p">, </span>provider_id=None<span class="p">, </span>realm=None<span class="p">, </span>request_refresh_token=None<span class="p">, </span>store_token=None<span class="p">, </span>trust_email=None<span class="p">, </span>use_user_ip_param=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewGoogleIdentityProvider<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-keycloak/sdk/go/keycloak/oidc?tab=doc#GoogleIdentityProviderArgs">GoogleIdentityProviderArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-keycloak/sdk/go/keycloak/oidc?tab=doc#GoogleIdentityProvider">GoogleIdentityProvider</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Keycloak/Pulumi.Keycloak.Oidc.GoogleIdentityProvider.html">GoogleIdentityProvider</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Keycloak/Pulumi.Keycloak.Oidc.GoogleIdentityProviderArgs.html">GoogleIdentityProviderArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Client ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Client Secret.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Realm Name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Accepts<wbr>Prompt<wbr>None<wbr>Forward<wbr>From<wbr>Client</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In
case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly
returned to client, but the request with prompt=none will be forwarded to this identity provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Add<wbr>Read<wbr>Token<wbr>Role<wbr>On<wbr>Create</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authenticate<wbr>By<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable authenticate users by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The scopes to be sent when asking for authorization. See the documentation for possible values, separator and default
value'. Default: 'openid profile email'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>User<wbr>Info</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Disable usage of User Info service to obtain additional user information? Default is to use this OIDC service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable this identity provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Extra<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>First<wbr>Broker<wbr>Login<wbr>Flow<wbr>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Alias of authentication flow, which is triggered after first login with this identity provider. Term 'First Login' means
that there is not yet existing Keycloak account linked with the authenticated identity provider account.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hide<wbr>On<wbr>Login<wbr>Page</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Hide On Login Page.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hosted<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set 'hd' query parameter when logging in with Google. Google will list accounts only for this domain. Keycloak validates
that the returned identity token has a claim for this domain. When '*' is entered, any hosted account can be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Link<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don't
want to allow login from the provider, but want to integrate with a provider
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Post<wbr>Broker<wbr>Login<wbr>Flow<wbr>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want
additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if
you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that
authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provider<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}provider id, is always google, unless you have a extended custom implementation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Refresh<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set 'access_type' query parameter to 'offline' when redirecting to google authorization endpoint, to get a refresh token
back. Useful if planning to use Token Exchange to retrieve Google token to access Google APIs when the user is not at
the browser.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Store<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable if tokens must be stored after authenticating users.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Trust<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If enabled then email provided by this provider is not verified even if verification is enabled for the realm.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>User<wbr>Ip<wbr>Param</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set 'userIp' query parameter when invoking on Google's User Info service. This will use the user's ip address. Useful if
Google is throttling access to the User Info service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Client ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Client Secret.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Realm Name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Accepts<wbr>Prompt<wbr>None<wbr>Forward<wbr>From<wbr>Client</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In
case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly
returned to client, but the request with prompt=none will be forwarded to this identity provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Add<wbr>Read<wbr>Token<wbr>Role<wbr>On<wbr>Create</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authenticate<wbr>By<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable authenticate users by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The scopes to be sent when asking for authorization. See the documentation for possible values, separator and default
value'. Default: 'openid profile email'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>User<wbr>Info</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Disable usage of User Info service to obtain additional user information? Default is to use this OIDC service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable this identity provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Extra<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>First<wbr>Broker<wbr>Login<wbr>Flow<wbr>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Alias of authentication flow, which is triggered after first login with this identity provider. Term 'First Login' means
that there is not yet existing Keycloak account linked with the authenticated identity provider account.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hide<wbr>On<wbr>Login<wbr>Page</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Hide On Login Page.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hosted<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set 'hd' query parameter when logging in with Google. Google will list accounts only for this domain. Keycloak validates
that the returned identity token has a claim for this domain. When '*' is entered, any hosted account can be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Link<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don't
want to allow login from the provider, but want to integrate with a provider
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Post<wbr>Broker<wbr>Login<wbr>Flow<wbr>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want
additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if
you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that
authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provider<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}provider id, is always google, unless you have a extended custom implementation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Refresh<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set 'access_type' query parameter to 'offline' when redirecting to google authorization endpoint, to get a refresh token
back. Useful if planning to use Token Exchange to retrieve Google token to access Google APIs when the user is not at
the browser.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Store<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable if tokens must be stored after authenticating users.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Trust<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If enabled then email provided by this provider is not verified even if verification is enabled for the realm.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>User<wbr>Ip<wbr>Param</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set 'userIp' query parameter when invoking on Google's User Info service. This will use the user's ip address. Useful if
Google is throttling access to the User Info service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Client ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Client Secret.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Realm Name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>accepts<wbr>Prompt<wbr>None<wbr>Forward<wbr>From<wbr>Client</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In
case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly
returned to client, but the request with prompt=none will be forwarded to this identity provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>add<wbr>Read<wbr>Token<wbr>Role<wbr>On<wbr>Create</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authenticate<wbr>By<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable/disable authenticate users by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The scopes to be sent when asking for authorization. See the documentation for possible values, separator and default
value'. Default: 'openid profile email'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable<wbr>User<wbr>Info</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Disable usage of User Info service to obtain additional user information? Default is to use this OIDC service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable/disable this identity provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>extra<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>first<wbr>Broker<wbr>Login<wbr>Flow<wbr>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Alias of authentication flow, which is triggered after first login with this identity provider. Term 'First Login' means
that there is not yet existing Keycloak account linked with the authenticated identity provider account.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hide<wbr>On<wbr>Login<wbr>Page</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Hide On Login Page.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hosted<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set 'hd' query parameter when logging in with Google. Google will list accounts only for this domain. Keycloak validates
that the returned identity token has a claim for this domain. When '*' is entered, any hosted account can be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>link<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don't
want to allow login from the provider, but want to integrate with a provider
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>post<wbr>Broker<wbr>Login<wbr>Flow<wbr>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want
additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if
you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that
authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provider<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}provider id, is always google, unless you have a extended custom implementation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Refresh<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Set 'access_type' query parameter to 'offline' when redirecting to google authorization endpoint, to get a refresh token
back. Useful if planning to use Token Exchange to retrieve Google token to access Google APIs when the user is not at
the browser.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>store<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable/disable if tokens must be stored after authenticating users.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>trust<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If enabled then email provided by this provider is not verified even if verification is enabled for the realm.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>User<wbr>Ip<wbr>Param</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Set 'userIp' query parameter when invoking on Google's User Info service. This will use the user's ip address. Useful if
Google is throttling access to the User Info service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Client ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>client_<wbr>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Client Secret.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Realm Name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>accepts_<wbr>prompt_<wbr>none_<wbr>forward_<wbr>from_<wbr>client</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In
case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly
returned to client, but the request with prompt=none will be forwarded to this identity provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>add_<wbr>read_<wbr>token_<wbr>role_<wbr>on_<wbr>create</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authenticate_<wbr>by_<wbr>default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable authenticate users by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The scopes to be sent when asking for authorization. See the documentation for possible values, separator and default
value'. Default: 'openid profile email'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable_<wbr>user_<wbr>info</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Disable usage of User Info service to obtain additional user information? Default is to use this OIDC service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable this identity provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>extra_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>first_<wbr>broker_<wbr>login_<wbr>flow_<wbr>alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Alias of authentication flow, which is triggered after first login with this identity provider. Term 'First Login' means
that there is not yet existing Keycloak account linked with the authenticated identity provider account.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hide_<wbr>on_<wbr>login_<wbr>page</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Hide On Login Page.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hosted_<wbr>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Set 'hd' query parameter when logging in with Google. Google will list accounts only for this domain. Keycloak validates
that the returned identity token has a claim for this domain. When '*' is entered, any hosted account can be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>link_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don't
want to allow login from the provider, but want to integrate with a provider
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>post_<wbr>broker_<wbr>login_<wbr>flow_<wbr>alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want
additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if
you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that
authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provider_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}provider id, is always google, unless you have a extended custom implementation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request_<wbr>refresh_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set 'access_type' query parameter to 'offline' when redirecting to google authorization endpoint, to get a refresh token
back. Useful if planning to use Token Exchange to retrieve Google token to access Google APIs when the user is not at
the browser.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>store_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable if tokens must be stored after authenticating users.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>trust_<wbr>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If enabled then email provided by this provider is not verified even if verification is enabled for the realm.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use_<wbr>user_<wbr>ip_<wbr>param</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set 'userIp' query parameter when invoking on Google's User Info service. This will use the user's ip address. Useful if
Google is throttling access to the User Info service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## GoogleIdentityProvider Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The alias uniquely identifies an identity provider and it is also used to build the redirect uri. In case of google this
is computed and always google
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Not used by this provider, Will be implicitly Google
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Internal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Internal Identity Provider Id
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The alias uniquely identifies an identity provider and it is also used to build the redirect uri. In case of google this
is computed and always google
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Not used by this provider, Will be implicitly Google
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Internal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Internal Identity Provider Id
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The alias uniquely identifies an identity provider and it is also used to build the redirect uri. In case of google this
is computed and always google
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Not used by this provider, Will be implicitly Google
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>internal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Internal Identity Provider Id
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The alias uniquely identifies an identity provider and it is also used to build the redirect uri. In case of google this
is computed and always google
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Not used by this provider, Will be implicitly Google
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>internal_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Internal Identity Provider Id
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing GoogleIdentityProvider Resource

Get an existing GoogleIdentityProvider resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/keycloak/oidc/#GoogleIdentityProviderState">GoogleIdentityProviderState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/keycloak/oidc/#GoogleIdentityProvider">GoogleIdentityProvider</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>accepts_prompt_none_forward_from_client=None<span class="p">, </span>add_read_token_role_on_create=None<span class="p">, </span>alias=None<span class="p">, </span>authenticate_by_default=None<span class="p">, </span>client_id=None<span class="p">, </span>client_secret=None<span class="p">, </span>default_scopes=None<span class="p">, </span>disable_user_info=None<span class="p">, </span>display_name=None<span class="p">, </span>enabled=None<span class="p">, </span>extra_config=None<span class="p">, </span>first_broker_login_flow_alias=None<span class="p">, </span>hide_on_login_page=None<span class="p">, </span>hosted_domain=None<span class="p">, </span>internal_id=None<span class="p">, </span>link_only=None<span class="p">, </span>post_broker_login_flow_alias=None<span class="p">, </span>provider_id=None<span class="p">, </span>realm=None<span class="p">, </span>request_refresh_token=None<span class="p">, </span>store_token=None<span class="p">, </span>trust_email=None<span class="p">, </span>use_user_ip_param=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetGoogleIdentityProvider<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-keycloak/sdk/go/keycloak/oidc?tab=doc#GoogleIdentityProviderState">GoogleIdentityProviderState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-keycloak/sdk/go/keycloak/oidc?tab=doc#GoogleIdentityProvider">GoogleIdentityProvider</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Keycloak/Pulumi.Keycloak.Oidc.GoogleIdentityProvider.html">GoogleIdentityProvider</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Keycloak/Pulumi.Keycloak.Oidc.GoogleIdentityProviderState.html">GoogleIdentityProviderState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Accepts<wbr>Prompt<wbr>None<wbr>Forward<wbr>From<wbr>Client</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In
case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly
returned to client, but the request with prompt=none will be forwarded to this identity provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Add<wbr>Read<wbr>Token<wbr>Role<wbr>On<wbr>Create</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The alias uniquely identifies an identity provider and it is also used to build the redirect uri. In case of google this
is computed and always google
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authenticate<wbr>By<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable authenticate users by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Client ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Client Secret.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The scopes to be sent when asking for authorization. See the documentation for possible values, separator and default
value'. Default: 'openid profile email'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>User<wbr>Info</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Disable usage of User Info service to obtain additional user information? Default is to use this OIDC service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Not used by this provider, Will be implicitly Google
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable this identity provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Extra<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>First<wbr>Broker<wbr>Login<wbr>Flow<wbr>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Alias of authentication flow, which is triggered after first login with this identity provider. Term 'First Login' means
that there is not yet existing Keycloak account linked with the authenticated identity provider account.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hide<wbr>On<wbr>Login<wbr>Page</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Hide On Login Page.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hosted<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set 'hd' query parameter when logging in with Google. Google will list accounts only for this domain. Keycloak validates
that the returned identity token has a claim for this domain. When '*' is entered, any hosted account can be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Internal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Internal Identity Provider Id
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Link<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don't
want to allow login from the provider, but want to integrate with a provider
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Post<wbr>Broker<wbr>Login<wbr>Flow<wbr>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want
additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if
you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that
authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provider<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}provider id, is always google, unless you have a extended custom implementation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Realm Name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Refresh<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set 'access_type' query parameter to 'offline' when redirecting to google authorization endpoint, to get a refresh token
back. Useful if planning to use Token Exchange to retrieve Google token to access Google APIs when the user is not at
the browser.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Store<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable if tokens must be stored after authenticating users.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Trust<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If enabled then email provided by this provider is not verified even if verification is enabled for the realm.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>User<wbr>Ip<wbr>Param</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set 'userIp' query parameter when invoking on Google's User Info service. This will use the user's ip address. Useful if
Google is throttling access to the User Info service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Accepts<wbr>Prompt<wbr>None<wbr>Forward<wbr>From<wbr>Client</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In
case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly
returned to client, but the request with prompt=none will be forwarded to this identity provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Add<wbr>Read<wbr>Token<wbr>Role<wbr>On<wbr>Create</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The alias uniquely identifies an identity provider and it is also used to build the redirect uri. In case of google this
is computed and always google
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authenticate<wbr>By<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable authenticate users by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Client ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Client Secret.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The scopes to be sent when asking for authorization. See the documentation for possible values, separator and default
value'. Default: 'openid profile email'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>User<wbr>Info</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Disable usage of User Info service to obtain additional user information? Default is to use this OIDC service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Not used by this provider, Will be implicitly Google
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable this identity provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Extra<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>First<wbr>Broker<wbr>Login<wbr>Flow<wbr>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Alias of authentication flow, which is triggered after first login with this identity provider. Term 'First Login' means
that there is not yet existing Keycloak account linked with the authenticated identity provider account.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hide<wbr>On<wbr>Login<wbr>Page</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Hide On Login Page.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hosted<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set 'hd' query parameter when logging in with Google. Google will list accounts only for this domain. Keycloak validates
that the returned identity token has a claim for this domain. When '*' is entered, any hosted account can be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Internal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Internal Identity Provider Id
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Link<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don't
want to allow login from the provider, but want to integrate with a provider
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Post<wbr>Broker<wbr>Login<wbr>Flow<wbr>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want
additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if
you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that
authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provider<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}provider id, is always google, unless you have a extended custom implementation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Realm Name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Refresh<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set 'access_type' query parameter to 'offline' when redirecting to google authorization endpoint, to get a refresh token
back. Useful if planning to use Token Exchange to retrieve Google token to access Google APIs when the user is not at
the browser.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Store<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable if tokens must be stored after authenticating users.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Trust<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If enabled then email provided by this provider is not verified even if verification is enabled for the realm.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>User<wbr>Ip<wbr>Param</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set 'userIp' query parameter when invoking on Google's User Info service. This will use the user's ip address. Useful if
Google is throttling access to the User Info service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accepts<wbr>Prompt<wbr>None<wbr>Forward<wbr>From<wbr>Client</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In
case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly
returned to client, but the request with prompt=none will be forwarded to this identity provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>add<wbr>Read<wbr>Token<wbr>Role<wbr>On<wbr>Create</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The alias uniquely identifies an identity provider and it is also used to build the redirect uri. In case of google this
is computed and always google
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authenticate<wbr>By<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable/disable authenticate users by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Client ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Client Secret.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The scopes to be sent when asking for authorization. See the documentation for possible values, separator and default
value'. Default: 'openid profile email'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable<wbr>User<wbr>Info</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Disable usage of User Info service to obtain additional user information? Default is to use this OIDC service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Not used by this provider, Will be implicitly Google
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable/disable this identity provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>extra<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>first<wbr>Broker<wbr>Login<wbr>Flow<wbr>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Alias of authentication flow, which is triggered after first login with this identity provider. Term 'First Login' means
that there is not yet existing Keycloak account linked with the authenticated identity provider account.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hide<wbr>On<wbr>Login<wbr>Page</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Hide On Login Page.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hosted<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Set 'hd' query parameter when logging in with Google. Google will list accounts only for this domain. Keycloak validates
that the returned identity token has a claim for this domain. When '*' is entered, any hosted account can be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>internal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Internal Identity Provider Id
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>link<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don't
want to allow login from the provider, but want to integrate with a provider
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>post<wbr>Broker<wbr>Login<wbr>Flow<wbr>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want
additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if
you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that
authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provider<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}provider id, is always google, unless you have a extended custom implementation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Realm Name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Refresh<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Set 'access_type' query parameter to 'offline' when redirecting to google authorization endpoint, to get a refresh token
back. Useful if planning to use Token Exchange to retrieve Google token to access Google APIs when the user is not at
the browser.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>store<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable/disable if tokens must be stored after authenticating users.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>trust<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If enabled then email provided by this provider is not verified even if verification is enabled for the realm.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>User<wbr>Ip<wbr>Param</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Set 'userIp' query parameter when invoking on Google's User Info service. This will use the user's ip address. Useful if
Google is throttling access to the User Info service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accepts_<wbr>prompt_<wbr>none_<wbr>forward_<wbr>from_<wbr>client</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In
case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly
returned to client, but the request with prompt=none will be forwarded to this identity provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>add_<wbr>read_<wbr>token_<wbr>role_<wbr>on_<wbr>create</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The alias uniquely identifies an identity provider and it is also used to build the redirect uri. In case of google this
is computed and always google
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authenticate_<wbr>by_<wbr>default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable authenticate users by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Client ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Client Secret.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The scopes to be sent when asking for authorization. See the documentation for possible values, separator and default
value'. Default: 'openid profile email'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable_<wbr>user_<wbr>info</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Disable usage of User Info service to obtain additional user information? Default is to use this OIDC service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Not used by this provider, Will be implicitly Google
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable this identity provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>extra_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>first_<wbr>broker_<wbr>login_<wbr>flow_<wbr>alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Alias of authentication flow, which is triggered after first login with this identity provider. Term 'First Login' means
that there is not yet existing Keycloak account linked with the authenticated identity provider account.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hide_<wbr>on_<wbr>login_<wbr>page</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Hide On Login Page.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hosted_<wbr>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Set 'hd' query parameter when logging in with Google. Google will list accounts only for this domain. Keycloak validates
that the returned identity token has a claim for this domain. When '*' is entered, any hosted account can be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>internal_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Internal Identity Provider Id
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>link_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don't
want to allow login from the provider, but want to integrate with a provider
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>post_<wbr>broker_<wbr>login_<wbr>flow_<wbr>alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want
additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if
you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that
authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provider_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}provider id, is always google, unless you have a extended custom implementation
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Realm Name
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request_<wbr>refresh_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set 'access_type' query parameter to 'offline' when redirecting to google authorization endpoint, to get a refresh token
back. Useful if planning to use Token Exchange to retrieve Google token to access Google APIs when the user is not at
the browser.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>store_<wbr>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable/disable if tokens must be stored after authenticating users.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>trust_<wbr>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If enabled then email provided by this provider is not verified even if verification is enabled for the realm.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use_<wbr>user_<wbr>ip_<wbr>param</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set 'userIp' query parameter when invoking on Google's User Info service. This will use the user's ip address. Useful if
Google is throttling access to the User Info service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-keycloak">https://github.com/pulumi/pulumi-keycloak</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

