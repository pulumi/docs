
---
title: "IdentityPool"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides an AWS Cognito Identity Pool.

## Example Usage

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

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_identity_pool.markdown.



## Create a IdentityPool Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cognito/#IdentityPool">IdentityPool</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cognito/#IdentityPoolArgs">IdentityPoolArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

```python
def IdentityPool(resource_name, id, opts=None, allow_<wbr>unauthenticated_<wbr>identities=None, cognito_<wbr>identity_<wbr>providers=None, developer_<wbr>provider_<wbr>name=None, identity_<wbr>pool_<wbr>name=None, openid_<wbr>connect_<wbr>provider_<wbr>arns=None, saml_<wbr>provider_<wbr>arns=None, supported_<wbr>login_<wbr>providers=None, tags=None, __props__=None)
```

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewIdentityPool<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPoolArgs">IdentityPoolArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPool">IdentityPool</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPool.html">IdentityPool</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPoolArgs.html">IdentityPoolArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a IdentityPool resource with the given unique name, arguments, and options.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Allow<wbr>Unauthenticated<wbr>Identities</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the identity pool supports unauthenticated logins or not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cognito<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#identitypoolcognitoidentityprovider">List&lt;Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An array of Amazon Cognito Identity user pools and their client IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Developer<wbr>Provider<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;domain&#34; by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Pool<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Cognito Identity Pool name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Openid<wbr>Connect<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of OpendID Connect provider ARNs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Saml<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Supported<wbr>Login<wbr>Providers</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-Value pairs mapping provider names to provider app IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the Identity Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Allow<wbr>Unauthenticated<wbr>Identities</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the identity pool supports unauthenticated logins or not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cognito<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#identitypoolcognitoidentityprovider">[]cognito.<wbr>Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An array of Amazon Cognito Identity user pools and their client IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Developer<wbr>Provider<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;domain&#34; by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Pool<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Cognito Identity Pool name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Openid<wbr>Connect<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of OpendID Connect provider ARNs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Saml<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Supported<wbr>Login<wbr>Providers</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-Value pairs mapping provider names to provider app IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the Identity Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">allow<wbr>Unauthenticated<wbr>Identities</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the identity pool supports unauthenticated logins or not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cognito<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#identitypoolcognitoidentityprovider">cognito.<wbr>Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An array of Amazon Cognito Identity user pools and their client IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">developer<wbr>Provider<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;domain&#34; by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity<wbr>Pool<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Cognito Identity Pool name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">openid<wbr>Connect<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of OpendID Connect provider ARNs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">saml<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">supported<wbr>Login<wbr>Providers</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-Value pairs mapping provider names to provider app IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the Identity Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">allow_<wbr>unauthenticated_<wbr>identities</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the identity pool supports unauthenticated logins or not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cognito_<wbr>identity_<wbr>providers</td>
            <td class="align-top">
                
                <code><a href="#identitypoolcognitoidentityprovider">list[identity_<wbr>pool_<wbr>cognito_<wbr>identity_<wbr>provider]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An array of Amazon Cognito Identity user pools and their client IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">developer_<wbr>provider_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;domain&#34; by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity_<wbr>pool_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Cognito Identity Pool name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">openid_<wbr>connect_<wbr>provider_<wbr>arns</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of OpendID Connect provider ARNs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">saml_<wbr>provider_<wbr>arns</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">supported_<wbr>login_<wbr>providers</td>
            <td class="align-top">
                
                <code>dict{string}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-Value pairs mapping provider names to provider app IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the Identity Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## IdentityPool Output Properties

The following output properties are available:



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Allow<wbr>Unauthenticated<wbr>Identities</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether the identity pool supports unauthenticated logins or not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the identity pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cognito<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#identitypoolcognitoidentityprovider">List&lt;Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} An array of Amazon Cognito Identity user pools and their client IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Developer<wbr>Provider<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The &#34;domain&#34; by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Pool<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Cognito Identity Pool name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Openid<wbr>Connect<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A list of OpendID Connect provider ARNs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Saml<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Supported<wbr>Login<wbr>Providers</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} Key-Value pairs mapping provider names to provider app IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the Identity Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Allow<wbr>Unauthenticated<wbr>Identities</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether the identity pool supports unauthenticated logins or not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the identity pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cognito<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#identitypoolcognitoidentityprovider">[]cognito.<wbr>Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider</a></code>
            </td>
            <td class="align-top">{{% md %}} An array of Amazon Cognito Identity user pools and their client IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Developer<wbr>Provider<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The &#34;domain&#34; by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Pool<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Cognito Identity Pool name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Openid<wbr>Connect<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of OpendID Connect provider ARNs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Saml<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Supported<wbr>Login<wbr>Providers</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} Key-Value pairs mapping provider names to provider app IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the Identity Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">allow<wbr>Unauthenticated<wbr>Identities</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether the identity pool supports unauthenticated logins or not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the identity pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cognito<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#identitypoolcognitoidentityprovider">cognito.<wbr>Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} An array of Amazon Cognito Identity user pools and their client IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">developer<wbr>Provider<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The &#34;domain&#34; by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity<wbr>Pool<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Cognito Identity Pool name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">openid<wbr>Connect<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} A list of OpendID Connect provider ARNs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">saml<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">supported<wbr>Login<wbr>Providers</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} Key-Value pairs mapping provider names to provider app IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the Identity Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">allow_<wbr>unauthenticated_<wbr>identities</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether the identity pool supports unauthenticated logins or not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the identity pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cognito_<wbr>identity_<wbr>providers</td>
            <td class="align-top">
                
                <code><a href="#identitypoolcognitoidentityprovider">list[identity_<wbr>pool_<wbr>cognito_<wbr>identity_<wbr>provider]</a></code>
            </td>
            <td class="align-top">{{% md %}} An array of Amazon Cognito Identity user pools and their client IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">developer_<wbr>provider_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The &#34;domain&#34; by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity_<wbr>pool_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Cognito Identity Pool name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">openid_<wbr>connect_<wbr>provider_<wbr>arns</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} A list of OpendID Connect provider ARNs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">saml_<wbr>provider_<wbr>arns</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">supported_<wbr>login_<wbr>providers</td>
            <td class="align-top">
                
                <code>dict{string}</code>
            </td>
            <td class="align-top">{{% md %}} Key-Value pairs mapping provider names to provider app IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the Identity Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing IdentityPool Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IdentityPoolState, opts?: pulumi.CustomResourceOptions): IdentityPool;
```

```python
def get(resource_name, id, opts=None, allow_<wbr>unauthenticated_<wbr>identities=None, arn=None, cognito_<wbr>identity_<wbr>providers=None, developer_<wbr>provider_<wbr>name=None, identity_<wbr>pool_<wbr>name=None, openid_<wbr>connect_<wbr>provider_<wbr>arns=None, saml_<wbr>provider_<wbr>arns=None, supported_<wbr>login_<wbr>providers=None, tags=None)
```

```go
func GetIdentityPool(ctx *pulumi.Context, name string, id pulumi.IDInput, state *IdentityPoolState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static IdentityPool Get(string name, Input<string> id, IdentityPoolState? state = null, CustomResourceOptions? options = null);
```

Get an existing IdentityPool resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following state arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Allow<wbr>Unauthenticated<wbr>Identities</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the identity pool supports unauthenticated logins or not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the identity pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cognito<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#identitypoolcognitoidentityprovider">List&lt;Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An array of Amazon Cognito Identity user pools and their client IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Developer<wbr>Provider<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;domain&#34; by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Pool<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Cognito Identity Pool name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Openid<wbr>Connect<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of OpendID Connect provider ARNs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Saml<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Supported<wbr>Login<wbr>Providers</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-Value pairs mapping provider names to provider app IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the Identity Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Allow<wbr>Unauthenticated<wbr>Identities</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the identity pool supports unauthenticated logins or not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the identity pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cognito<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#identitypoolcognitoidentityprovider">[]cognito.<wbr>Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An array of Amazon Cognito Identity user pools and their client IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Developer<wbr>Provider<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;domain&#34; by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Identity<wbr>Pool<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Cognito Identity Pool name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Openid<wbr>Connect<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of OpendID Connect provider ARNs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Saml<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Supported<wbr>Login<wbr>Providers</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-Value pairs mapping provider names to provider app IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the Identity Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">allow<wbr>Unauthenticated<wbr>Identities</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the identity pool supports unauthenticated logins or not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the identity pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cognito<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code><a href="#identitypoolcognitoidentityprovider">cognito.<wbr>Identity<wbr>Pool<wbr>Cognito<wbr>Identity<wbr>Provider[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An array of Amazon Cognito Identity user pools and their client IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">developer<wbr>Provider<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;domain&#34; by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity<wbr>Pool<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Cognito Identity Pool name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">openid<wbr>Connect<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of OpendID Connect provider ARNs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">saml<wbr>Provider<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">supported<wbr>Login<wbr>Providers</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-Value pairs mapping provider names to provider app IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the Identity Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">allow_<wbr>unauthenticated_<wbr>identities</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the identity pool supports unauthenticated logins or not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the identity pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cognito_<wbr>identity_<wbr>providers</td>
            <td class="align-top">
                
                <code><a href="#identitypoolcognitoidentityprovider">list[identity_<wbr>pool_<wbr>cognito_<wbr>identity_<wbr>provider]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An array of Amazon Cognito Identity user pools and their client IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">developer_<wbr>provider_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The &#34;domain&#34; by which Cognito will refer to your users. This name acts as a placeholder that allows your
backend and the Cognito service to communicate about the developer provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">identity_<wbr>pool_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Cognito Identity Pool name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">openid_<wbr>connect_<wbr>provider_<wbr>arns</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of OpendID Connect provider ARNs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">saml_<wbr>provider_<wbr>arns</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An array of Amazon Resource Names (ARNs) of the SAML provider for your identity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">supported_<wbr>login_<wbr>providers</td>
            <td class="align-top">
                
                <code>dict{string}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-Value pairs mapping provider names to provider app IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the Identity Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### IdentityPoolCognitoIdentityProvider
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#IdentityPoolCognitoIdentityProvider">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#IdentityPoolCognitoIdentityProvider">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPoolCognitoIdentityProviderArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#IdentityPoolCognitoIdentityProviderOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPoolCognitoIdentityProviderArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.IdentityPoolCognitoIdentityProvider.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Client<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The client ID for the Amazon Cognito Identity User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Provider<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The provider name for an Amazon Cognito Identity User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Token<wbr>Check</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether server-side token validation is enabled for the identity provider’s token or not.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Client<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The client ID for the Amazon Cognito Identity User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Provider<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The provider name for an Amazon Cognito Identity User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Token<wbr>Check</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether server-side token validation is enabled for the identity provider’s token or not.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">client<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The client ID for the Amazon Cognito Identity User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">provider<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The provider name for an Amazon Cognito Identity User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server<wbr>Side<wbr>Token<wbr>Check</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether server-side token validation is enabled for the identity provider’s token or not.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">client_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The client ID for the Amazon Cognito Identity User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">provider_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The provider name for an Amazon Cognito Identity User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server_<wbr>side_<wbr>token_<wbr>check</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether server-side token validation is enabled for the identity provider’s token or not.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







