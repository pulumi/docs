
---
title: "IdentityPool"
block_external_search_index: true
---



Provides an AWS Cognito Identity Pool.

{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as fs from "fs";

const defaultSamlProvider = new aws.iam.SamlProvider("default", {
    samlMetadataDocument: fs.readFileSync("saml-metadata.xml", "utf-8"),
});
const main = new aws.cognito.IdentityPool("main", {
    allowUnauthenticatedIdentities: false,
    cognitoIdentityProviders: [
        {
            clientId: "6lhlkkfbfb4q5kpp90urffae",
            providerName: "cognito-idp.us-east-1.amazonaws.com/us-east-1_Tv0493apJ",
            serverSideTokenCheck: false,
        },
        {
            clientId: "7kodkvfqfb4qfkp39eurffae",
            providerName: "cognito-idp.us-east-1.amazonaws.com/eu-west-1_Zr231apJu",
            serverSideTokenCheck: false,
        },
    ],
    identityPoolName: "identity pool",
    openidConnectProviderArns: ["arn:aws:iam::123456789012:oidc-provider/foo.example.com"],
    samlProviderArns: [defaultSamlProvider.arn],
    supportedLoginProviders: {
        "accounts.google.com": "123456789012.apps.googleusercontent.com",
        "graph.facebook.com": "7346241598935552",
    },
});
```

{{% /example %}}
{{% /examples %}}



## Create a IdentityPool Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cognito/#IdentityPool">IdentityPool</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cognito/#IdentityPoolArgs">IdentityPoolArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">IdentityPool</span><span class="p">(resource_name, opts=None, </span>allow_unauthenticated_identities=None<span class="p">, </span>cognito_identity_providers=None<span class="p">, </span>developer_provider_name=None<span class="p">, </span>identity_pool_name=None<span class="p">, </span>openid_connect_provider_arns=None<span class="p">, </span>saml_provider_arns=None<span class="p">, </span>supported_login_providers=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewIdentityPool<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPoolArgs">IdentityPoolArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPool">IdentityPool</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPool.html">IdentityPool</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPoolArgs.html">IdentityPoolArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Identity<wbr>Pool<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cognito Identity Pool name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Unauthenticated<wbr>Identities</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the identity pool supports unauthenticated logins or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cognito<wbr>Identity<wbr>Providers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#identitypoolcognitoidentityprovider">List&lt;Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}An array of Amazon Cognito Identity user pools and their client IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Developer<wbr>Provider<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Openid<wbr>Connect<wbr>Provider<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}A list of OpendID Connect provider ARNs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Saml<wbr>Provider<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Supported<wbr>Login<wbr>Providers</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}Key-Value pairs mapping provider names to provider app IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Identity Pool.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Identity<wbr>Pool<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cognito Identity Pool name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Unauthenticated<wbr>Identities</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the identity pool supports unauthenticated logins or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cognito<wbr>Identity<wbr>Providers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#identitypoolcognitoidentityprovider">[]Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider</a></span>
    </dt>
    <dd>{{% md %}}An array of Amazon Cognito Identity user pools and their client IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Developer<wbr>Provider<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Openid<wbr>Connect<wbr>Provider<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of OpendID Connect provider ARNs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Saml<wbr>Provider<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Supported<wbr>Login<wbr>Providers</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Key-Value pairs mapping provider names to provider app IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Identity Pool.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>identity<wbr>Pool<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cognito Identity Pool name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Unauthenticated<wbr>Identities</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the identity pool supports unauthenticated logins or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cognito<wbr>Identity<wbr>Providers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#identitypoolcognitoidentityprovider">Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider[]</a></span>
    </dt>
    <dd>{{% md %}}An array of Amazon Cognito Identity user pools and their client IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>developer<wbr>Provider<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>openid<wbr>Connect<wbr>Provider<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of OpendID Connect provider ARNs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>saml<wbr>Provider<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>supported<wbr>Login<wbr>Providers</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}Key-Value pairs mapping provider names to provider app IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Identity Pool.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>identity_<wbr>pool_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cognito Identity Pool name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>unauthenticated_<wbr>identities</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the identity pool supports unauthenticated logins or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cognito_<wbr>identity_<wbr>providers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#identitypoolcognitoidentityprovider">List[Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider]</a></span>
    </dt>
    <dd>{{% md %}}An array of Amazon Cognito Identity user pools and their client IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>developer_<wbr>provider_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>openid_<wbr>connect_<wbr>provider_<wbr>arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of OpendID Connect provider ARNs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>saml_<wbr>provider_<wbr>arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>supported_<wbr>login_<wbr>providers</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Key-Value pairs mapping provider names to provider app IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Identity Pool.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## IdentityPool Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the identity pool.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the identity pool.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the identity pool.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the identity pool.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing IdentityPool Resource

Get an existing IdentityPool resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cognito/#IdentityPoolState">IdentityPoolState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cognito/#IdentityPool">IdentityPool</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>allow_unauthenticated_identities=None<span class="p">, </span>arn=None<span class="p">, </span>cognito_identity_providers=None<span class="p">, </span>developer_provider_name=None<span class="p">, </span>identity_pool_name=None<span class="p">, </span>openid_connect_provider_arns=None<span class="p">, </span>saml_provider_arns=None<span class="p">, </span>supported_login_providers=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetIdentityPool<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPoolState">IdentityPoolState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPool">IdentityPool</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPool.html">IdentityPool</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPoolState.html">IdentityPoolState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Allow<wbr>Unauthenticated<wbr>Identities</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the identity pool supports unauthenticated logins or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the identity pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cognito<wbr>Identity<wbr>Providers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#identitypoolcognitoidentityprovider">List&lt;Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}An array of Amazon Cognito Identity user pools and their client IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Developer<wbr>Provider<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity<wbr>Pool<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cognito Identity Pool name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Openid<wbr>Connect<wbr>Provider<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}A list of OpendID Connect provider ARNs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Saml<wbr>Provider<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Supported<wbr>Login<wbr>Providers</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}Key-Value pairs mapping provider names to provider app IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Identity Pool.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Unauthenticated<wbr>Identities</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the identity pool supports unauthenticated logins or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the identity pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cognito<wbr>Identity<wbr>Providers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#identitypoolcognitoidentityprovider">[]Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider</a></span>
    </dt>
    <dd>{{% md %}}An array of Amazon Cognito Identity user pools and their client IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Developer<wbr>Provider<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity<wbr>Pool<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cognito Identity Pool name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Openid<wbr>Connect<wbr>Provider<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of OpendID Connect provider ARNs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Saml<wbr>Provider<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Supported<wbr>Login<wbr>Providers</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Key-Value pairs mapping provider names to provider app IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Identity Pool.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Unauthenticated<wbr>Identities</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the identity pool supports unauthenticated logins or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN of the identity pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cognito<wbr>Identity<wbr>Providers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#identitypoolcognitoidentityprovider">Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider[]</a></span>
    </dt>
    <dd>{{% md %}}An array of Amazon Cognito Identity user pools and their client IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>developer<wbr>Provider<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity<wbr>Pool<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cognito Identity Pool name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>openid<wbr>Connect<wbr>Provider<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of OpendID Connect provider ARNs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>saml<wbr>Provider<wbr>Arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>supported<wbr>Login<wbr>Providers</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}Key-Value pairs mapping provider names to provider app IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Identity Pool.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>unauthenticated_<wbr>identities</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the identity pool supports unauthenticated logins or not.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN of the identity pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cognito_<wbr>identity_<wbr>providers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#identitypoolcognitoidentityprovider">List[Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider]</a></span>
    </dt>
    <dd>{{% md %}}An array of Amazon Cognito Identity user pools and their client IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>developer_<wbr>provider_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity_<wbr>pool_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cognito Identity Pool name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>openid_<wbr>connect_<wbr>provider_<wbr>arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of OpendID Connect provider ARNs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>saml_<wbr>provider_<wbr>arns</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>supported_<wbr>login_<wbr>providers</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Key-Value pairs mapping provider names to provider app IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the Identity Pool.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#IdentityPoolCognitoIdentityProvider">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#IdentityPoolCognitoIdentityProvider">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPoolCognitoIdentityProviderArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPoolCognitoIdentityProviderOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The client ID for the Amazon Cognito Identity User Pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provider<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The provider name for an Amazon Cognito Identity User Pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Side<wbr>Token<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether server-side token validation is enabled for the identity provider’s token or not.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The client ID for the Amazon Cognito Identity User Pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provider<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The provider name for an Amazon Cognito Identity User Pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Side<wbr>Token<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether server-side token validation is enabled for the identity provider’s token or not.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The client ID for the Amazon Cognito Identity User Pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provider<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The provider name for an Amazon Cognito Identity User Pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Side<wbr>Token<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether server-side token validation is enabled for the identity provider’s token or not.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The client ID for the Amazon Cognito Identity User Pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provider_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The provider name for an Amazon Cognito Identity User Pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Side<wbr>Token<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether server-side token validation is enabled for the identity provider’s token or not.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-aws">https://github.com/pulumi/pulumi-aws</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`aws` Terraform Provider](https://github.com/terraform-providers/terraform-provider-aws).</dd>
</dl>

