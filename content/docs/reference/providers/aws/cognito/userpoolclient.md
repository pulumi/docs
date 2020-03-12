
---
title: "UserPoolClient"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides a Cognito User Pool Client resource.

## Example Usage

### Create a basic user pool client

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const pool = new aws.cognito.UserPool("pool", {});
const client = new aws.cognito.UserPoolClient("client", {
    userPoolId: pool.id,
});
```

### Create a user pool client with no SRP authentication

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const pool = new aws.cognito.UserPool("pool", {});
const client = new aws.cognito.UserPoolClient("client", {
    explicitAuthFlows: ["ADMIN_NO_SRP_AUTH"],
    generateSecret: true,
    userPoolId: pool.id,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool_client.markdown.



## Create a UserPoolClient Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cognito/#UserPoolClient">UserPoolClient</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cognito/#UserPoolClientArgs">UserPoolClientArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

```python
def UserPoolClient(resource_name, id, opts=None, allowed_<wbr>oauth_<wbr>flows=None, allowed_<wbr>oauth_<wbr>flows_<wbr>user_<wbr>pool_<wbr>client=None, allowed_<wbr>oauth_<wbr>scopes=None, callback_<wbr>urls=None, default_<wbr>redirect_<wbr>uri=None, explicit_<wbr>auth_<wbr>flows=None, generate_<wbr>secret=None, logout_<wbr>urls=None, name=None, read_<wbr>attributes=None, refresh_<wbr>token_<wbr>validity=None, supported_<wbr>identity_<wbr>providers=None, user_<wbr>pool_<wbr>id=None, write_<wbr>attributes=None, __props__=None)
```

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewUserPoolClient<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolClientArgs">UserPoolClientArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolClient">UserPoolClient</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolClient.html">UserPoolClient</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolClientArgs.html">UserPoolClientArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a UserPoolClient resource with the given unique name, arguments, and options.

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
            <td class="align-top">Allowed<wbr>Oauth<wbr>Flows</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed OAuth flows (code, implicit, client_credentials).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allowed<wbr>Oauth<wbr>Flows<wbr>User<wbr>Pool<wbr>Client</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allowed<wbr>Oauth<wbr>Scopes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Callback<wbr>Urls</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed callback URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Redirect<wbr>Uri</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default redirect URI. Must be in the list of callback URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Explicit<wbr>Auth<wbr>Flows</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Generate<wbr>Secret</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Should an application secret be generated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logout<wbr>Urls</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed logout URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the application client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Attributes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of user pool attributes the application client can read from.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Refresh<wbr>Token<wbr>Validity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time limit in days refresh tokens are valid for.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Supported<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of provider names for the identity providers that are supported on this client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The user pool the client belongs to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Write<wbr>Attributes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of user pool attributes the application client can write to.
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
            <td class="align-top">Allowed<wbr>Oauth<wbr>Flows</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed OAuth flows (code, implicit, client_credentials).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allowed<wbr>Oauth<wbr>Flows<wbr>User<wbr>Pool<wbr>Client</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allowed<wbr>Oauth<wbr>Scopes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Callback<wbr>Urls</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed callback URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Redirect<wbr>Uri</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default redirect URI. Must be in the list of callback URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Explicit<wbr>Auth<wbr>Flows</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Generate<wbr>Secret</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Should an application secret be generated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logout<wbr>Urls</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed logout URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the application client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Attributes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of user pool attributes the application client can read from.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Refresh<wbr>Token<wbr>Validity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time limit in days refresh tokens are valid for.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Supported<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of provider names for the identity providers that are supported on this client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The user pool the client belongs to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Write<wbr>Attributes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of user pool attributes the application client can write to.
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
            <td class="align-top">allowed<wbr>Oauth<wbr>Flows</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed OAuth flows (code, implicit, client_credentials).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allowed<wbr>Oauth<wbr>Flows<wbr>User<wbr>Pool<wbr>Client</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allowed<wbr>Oauth<wbr>Scopes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">callback<wbr>Urls</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed callback URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Redirect<wbr>Uri</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default redirect URI. Must be in the list of callback URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">explicit<wbr>Auth<wbr>Flows</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">generate<wbr>Secret</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Should an application secret be generated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logout<wbr>Urls</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed logout URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the application client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read<wbr>Attributes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of user pool attributes the application client can read from.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">refresh<wbr>Token<wbr>Validity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time limit in days refresh tokens are valid for.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">supported<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of provider names for the identity providers that are supported on this client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The user pool the client belongs to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">write<wbr>Attributes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of user pool attributes the application client can write to.
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
            <td class="align-top">allowed_<wbr>oauth_<wbr>flows</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed OAuth flows (code, implicit, client_credentials).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allowed_<wbr>oauth_<wbr>flows_<wbr>user_<wbr>pool_<wbr>client</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allowed_<wbr>oauth_<wbr>scopes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">callback_<wbr>urls</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed callback URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>redirect_<wbr>uri</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default redirect URI. Must be in the list of callback URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">explicit_<wbr>auth_<wbr>flows</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">generate_<wbr>secret</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Should an application secret be generated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logout_<wbr>urls</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed logout URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the application client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read_<wbr>attributes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of user pool attributes the application client can read from.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">refresh_<wbr>token_<wbr>validity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time limit in days refresh tokens are valid for.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">supported_<wbr>identity_<wbr>providers</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of provider names for the identity providers that are supported on this client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>pool_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The user pool the client belongs to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">write_<wbr>attributes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of user pool attributes the application client can write to.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## UserPoolClient Output Properties

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
            <td class="align-top">Allowed<wbr>Oauth<wbr>Flows</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} List of allowed OAuth flows (code, implicit, client_credentials).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allowed<wbr>Oauth<wbr>Flows<wbr>User<wbr>Pool<wbr>Client</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allowed<wbr>Oauth<wbr>Scopes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Callback<wbr>Urls</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} List of allowed callback URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Secret</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The client secret of the user pool client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Redirect<wbr>Uri</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The default redirect URI. Must be in the list of callback URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Explicit<wbr>Auth<wbr>Flows</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Generate<wbr>Secret</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Should an application secret be generated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logout<wbr>Urls</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} List of allowed logout URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the application client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Attributes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} List of user pool attributes the application client can read from.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Refresh<wbr>Token<wbr>Validity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The time limit in days refresh tokens are valid for.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Supported<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} List of provider names for the identity providers that are supported on this client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The user pool the client belongs to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Write<wbr>Attributes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} List of user pool attributes the application client can write to.
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
            <td class="align-top">Allowed<wbr>Oauth<wbr>Flows</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of allowed OAuth flows (code, implicit, client_credentials).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allowed<wbr>Oauth<wbr>Flows<wbr>User<wbr>Pool<wbr>Client</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allowed<wbr>Oauth<wbr>Scopes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Callback<wbr>Urls</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of allowed callback URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Secret</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The client secret of the user pool client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Redirect<wbr>Uri</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The default redirect URI. Must be in the list of callback URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Explicit<wbr>Auth<wbr>Flows</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Generate<wbr>Secret</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Should an application secret be generated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logout<wbr>Urls</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of allowed logout URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the application client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Attributes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of user pool attributes the application client can read from.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Refresh<wbr>Token<wbr>Validity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The time limit in days refresh tokens are valid for.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Supported<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of provider names for the identity providers that are supported on this client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The user pool the client belongs to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Write<wbr>Attributes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of user pool attributes the application client can write to.
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
            <td class="align-top">allowed<wbr>Oauth<wbr>Flows</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} List of allowed OAuth flows (code, implicit, client_credentials).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allowed<wbr>Oauth<wbr>Flows<wbr>User<wbr>Pool<wbr>Client</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allowed<wbr>Oauth<wbr>Scopes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">callback<wbr>Urls</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} List of allowed callback URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client<wbr>Secret</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The client secret of the user pool client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Redirect<wbr>Uri</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The default redirect URI. Must be in the list of callback URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">explicit<wbr>Auth<wbr>Flows</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">generate<wbr>Secret</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Should an application secret be generated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logout<wbr>Urls</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} List of allowed logout URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the application client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read<wbr>Attributes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} List of user pool attributes the application client can read from.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">refresh<wbr>Token<wbr>Validity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The time limit in days refresh tokens are valid for.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">supported<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} List of provider names for the identity providers that are supported on this client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The user pool the client belongs to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">write<wbr>Attributes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} List of user pool attributes the application client can write to.
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
            <td class="align-top">allowed_<wbr>oauth_<wbr>flows</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} List of allowed OAuth flows (code, implicit, client_credentials).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allowed_<wbr>oauth_<wbr>flows_<wbr>user_<wbr>pool_<wbr>client</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allowed_<wbr>oauth_<wbr>scopes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">callback_<wbr>urls</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} List of allowed callback URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client_<wbr>secret</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The client secret of the user pool client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>redirect_<wbr>uri</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The default redirect URI. Must be in the list of callback URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">explicit_<wbr>auth_<wbr>flows</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">generate_<wbr>secret</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Should an application secret be generated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logout_<wbr>urls</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} List of allowed logout URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the application client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read_<wbr>attributes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} List of user pool attributes the application client can read from.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">refresh_<wbr>token_<wbr>validity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The time limit in days refresh tokens are valid for.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">supported_<wbr>identity_<wbr>providers</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} List of provider names for the identity providers that are supported on this client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>pool_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The user pool the client belongs to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">write_<wbr>attributes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} List of user pool attributes the application client can write to.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing UserPoolClient Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserPoolClientState, opts?: pulumi.CustomResourceOptions): UserPoolClient;
```

```python
def get(resource_name, id, opts=None, allowed_<wbr>oauth_<wbr>flows=None, allowed_<wbr>oauth_<wbr>flows_<wbr>user_<wbr>pool_<wbr>client=None, allowed_<wbr>oauth_<wbr>scopes=None, callback_<wbr>urls=None, client_<wbr>secret=None, default_<wbr>redirect_<wbr>uri=None, explicit_<wbr>auth_<wbr>flows=None, generate_<wbr>secret=None, logout_<wbr>urls=None, name=None, read_<wbr>attributes=None, refresh_<wbr>token_<wbr>validity=None, supported_<wbr>identity_<wbr>providers=None, user_<wbr>pool_<wbr>id=None, write_<wbr>attributes=None)
```

```go
func GetUserPoolClient(ctx *pulumi.Context, name string, id pulumi.IDInput, state *UserPoolClientState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static UserPoolClient Get(string name, Input<string> id, UserPoolClientState? state = null, CustomResourceOptions? options = null);
```

Get an existing UserPoolClient resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Allowed<wbr>Oauth<wbr>Flows</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed OAuth flows (code, implicit, client_credentials).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allowed<wbr>Oauth<wbr>Flows<wbr>User<wbr>Pool<wbr>Client</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allowed<wbr>Oauth<wbr>Scopes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Callback<wbr>Urls</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed callback URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Secret</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The client secret of the user pool client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Redirect<wbr>Uri</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default redirect URI. Must be in the list of callback URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Explicit<wbr>Auth<wbr>Flows</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Generate<wbr>Secret</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Should an application secret be generated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logout<wbr>Urls</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed logout URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the application client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Attributes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of user pool attributes the application client can read from.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Refresh<wbr>Token<wbr>Validity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time limit in days refresh tokens are valid for.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Supported<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of provider names for the identity providers that are supported on this client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user pool the client belongs to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Write<wbr>Attributes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of user pool attributes the application client can write to.
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
            <td class="align-top">Allowed<wbr>Oauth<wbr>Flows</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed OAuth flows (code, implicit, client_credentials).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allowed<wbr>Oauth<wbr>Flows<wbr>User<wbr>Pool<wbr>Client</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Allowed<wbr>Oauth<wbr>Scopes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Callback<wbr>Urls</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed callback URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Secret</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The client secret of the user pool client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Redirect<wbr>Uri</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default redirect URI. Must be in the list of callback URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Explicit<wbr>Auth<wbr>Flows</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Generate<wbr>Secret</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Should an application secret be generated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logout<wbr>Urls</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed logout URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the application client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Attributes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of user pool attributes the application client can read from.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Refresh<wbr>Token<wbr>Validity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time limit in days refresh tokens are valid for.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Supported<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of provider names for the identity providers that are supported on this client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user pool the client belongs to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Write<wbr>Attributes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of user pool attributes the application client can write to.
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
            <td class="align-top">allowed<wbr>Oauth<wbr>Flows</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed OAuth flows (code, implicit, client_credentials).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allowed<wbr>Oauth<wbr>Flows<wbr>User<wbr>Pool<wbr>Client</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allowed<wbr>Oauth<wbr>Scopes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">callback<wbr>Urls</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed callback URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client<wbr>Secret</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The client secret of the user pool client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Redirect<wbr>Uri</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default redirect URI. Must be in the list of callback URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">explicit<wbr>Auth<wbr>Flows</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">generate<wbr>Secret</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Should an application secret be generated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logout<wbr>Urls</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed logout URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the application client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read<wbr>Attributes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of user pool attributes the application client can read from.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">refresh<wbr>Token<wbr>Validity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time limit in days refresh tokens are valid for.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">supported<wbr>Identity<wbr>Providers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of provider names for the identity providers that are supported on this client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user pool the client belongs to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">write<wbr>Attributes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of user pool attributes the application client can write to.
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
            <td class="align-top">allowed_<wbr>oauth_<wbr>flows</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed OAuth flows (code, implicit, client_credentials).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allowed_<wbr>oauth_<wbr>flows_<wbr>user_<wbr>pool_<wbr>client</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">allowed_<wbr>oauth_<wbr>scopes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">callback_<wbr>urls</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed callback URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client_<wbr>secret</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The client secret of the user pool client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>redirect_<wbr>uri</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default redirect URI. Must be in the list of callback URLs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">explicit_<wbr>auth_<wbr>flows</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">generate_<wbr>secret</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Should an application secret be generated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logout_<wbr>urls</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of allowed logout URLs for the identity providers.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the application client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read_<wbr>attributes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of user pool attributes the application client can read from.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">refresh_<wbr>token_<wbr>validity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time limit in days refresh tokens are valid for.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">supported_<wbr>identity_<wbr>providers</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of provider names for the identity providers that are supported on this client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>pool_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user pool the client belongs to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">write_<wbr>attributes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of user pool attributes the application client can write to.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}









