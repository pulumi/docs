
---
title: "UserPool"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides a Cognito User Pool resource.

## Example Usage

### Basic configuration

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const pool = new aws.cognito.UserPool("pool", {});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool.markdown.



## Create a UserPool Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cognito/#UserPool">UserPool</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cognito/#UserPoolArgs">UserPoolArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">UserPool</span><span class="p">(resource_name, opts=None, </span>admin_create_user_config=None<span class="p">, </span>alias_attributes=None<span class="p">, </span>auto_verified_attributes=None<span class="p">, </span>device_configuration=None<span class="p">, </span>email_configuration=None<span class="p">, </span>email_verification_message=None<span class="p">, </span>email_verification_subject=None<span class="p">, </span>lambda_config=None<span class="p">, </span>mfa_configuration=None<span class="p">, </span>name=None<span class="p">, </span>password_policy=None<span class="p">, </span>schemas=None<span class="p">, </span>sms_authentication_message=None<span class="p">, </span>sms_configuration=None<span class="p">, </span>sms_verification_message=None<span class="p">, </span>tags=None<span class="p">, </span>user_pool_add_ons=None<span class="p">, </span>username_attributes=None<span class="p">, </span>verification_message_template=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewUserPool<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolArgs">UserPoolArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPool">UserPool</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPool.html">UserPool</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolArgs.html">UserPoolArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a UserPool resource with the given unique name, arguments, and options.

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
            <td class="align-top">Admin<wbr>Create<wbr>User<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpooladmincreateuserconfig">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Admin<wbr>Create<wbr>User<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for AdminCreateUser requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Alias<wbr>Attributes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Verified<wbr>Attributes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The attributes to be auto-verified. Possible values: email, phone_number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Device<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpooldeviceconfiguration">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Device<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for the user pool&#39;s device tracking.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolemailconfiguration">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Email<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Email Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the email verification message. Conflicts with `verification_message_template` configuration block `email_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Verification<wbr>Subject</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the email verification subject. Conflicts with `verification_message_template` configuration block `email_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpoollambdaconfig">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Lambda<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container for the AWS Lambda triggers associated with the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mfa<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)
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
The name of the attribute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#userpoolpasswordpolicy">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Password<wbr>Policy<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container for information about the user pool password policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Schemas</td>
            <td class="align-top">
                
                <code><a href="#userpoolschema">List&lt;Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Schema<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container with the schema attributes of a user pool. Schema attributes from the [standard attribute set](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes) only need to be specified if they are different from the default configuration. Maximum of 50 attributes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Authentication<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the SMS authentication message.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolsmsconfiguration">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Sms<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SMS Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the SMS verification message. Conflicts with `verification_message_template` configuration block `sms_message` argument.
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
A mapping of tags to assign to the User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Add<wbr>Ons</td>
            <td class="align-top">
                
                <code><a href="#userpooluserpooladdons">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>User<wbr>Pool<wbr>Add<wbr>Ons<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for user pool add-ons to enable user pool advanced security mode features.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Username<wbr>Attributes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Verification<wbr>Message<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#userpoolverificationmessagetemplate">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Verification<wbr>Message<wbr>Template<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The verification message templates configuration.
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
            <td class="align-top">Admin<wbr>Create<wbr>User<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpooladmincreateuserconfig">*User<wbr>Pool<wbr>Admin<wbr>Create<wbr>User<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for AdminCreateUser requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Alias<wbr>Attributes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Verified<wbr>Attributes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The attributes to be auto-verified. Possible values: email, phone_number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Device<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpooldeviceconfiguration">*User<wbr>Pool<wbr>Device<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for the user pool&#39;s device tracking.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolemailconfiguration">*User<wbr>Pool<wbr>Email<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Email Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the email verification message. Conflicts with `verification_message_template` configuration block `email_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Verification<wbr>Subject</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the email verification subject. Conflicts with `verification_message_template` configuration block `email_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpoollambdaconfig">*User<wbr>Pool<wbr>Lambda<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container for the AWS Lambda triggers associated with the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mfa<wbr>Configuration</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)
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
The name of the attribute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#userpoolpasswordpolicy">*User<wbr>Pool<wbr>Password<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container for information about the user pool password policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Schemas</td>
            <td class="align-top">
                
                <code><a href="#userpoolschema">[]User<wbr>Pool<wbr>Schema</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container with the schema attributes of a user pool. Schema attributes from the [standard attribute set](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes) only need to be specified if they are different from the default configuration. Maximum of 50 attributes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Authentication<wbr>Message</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the SMS authentication message.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolsmsconfiguration">*User<wbr>Pool<wbr>Sms<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SMS Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the SMS verification message. Conflicts with `verification_message_template` configuration block `sms_message` argument.
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
A mapping of tags to assign to the User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Add<wbr>Ons</td>
            <td class="align-top">
                
                <code><a href="#userpooluserpooladdons">*User<wbr>Pool<wbr>User<wbr>Pool<wbr>Add<wbr>Ons</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for user pool add-ons to enable user pool advanced security mode features.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Username<wbr>Attributes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Verification<wbr>Message<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#userpoolverificationmessagetemplate">*User<wbr>Pool<wbr>Verification<wbr>Message<wbr>Template</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The verification message templates configuration.
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
            <td class="align-top">admin<wbr>Create<wbr>User<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpooladmincreateuserconfig">cognito.<wbr>User<wbr>Pool<wbr>Admin<wbr>Create<wbr>User<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for AdminCreateUser requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">alias<wbr>Attributes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Verified<wbr>Attributes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The attributes to be auto-verified. Possible values: email, phone_number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">device<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpooldeviceconfiguration">cognito.<wbr>User<wbr>Pool<wbr>Device<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for the user pool&#39;s device tracking.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolemailconfiguration">cognito.<wbr>User<wbr>Pool<wbr>Email<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Email Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the email verification message. Conflicts with `verification_message_template` configuration block `email_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Verification<wbr>Subject</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the email verification subject. Conflicts with `verification_message_template` configuration block `email_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpoollambdaconfig">cognito.<wbr>User<wbr>Pool<wbr>Lambda<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container for the AWS Lambda triggers associated with the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mfa<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)
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
The name of the attribute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#userpoolpasswordpolicy">cognito.<wbr>User<wbr>Pool<wbr>Password<wbr>Policy?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container for information about the user pool password policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">schemas</td>
            <td class="align-top">
                
                <code><a href="#userpoolschema">cognito.<wbr>User<wbr>Pool<wbr>Schema[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container with the schema attributes of a user pool. Schema attributes from the [standard attribute set](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes) only need to be specified if they are different from the default configuration. Maximum of 50 attributes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms<wbr>Authentication<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the SMS authentication message.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolsmsconfiguration">cognito.<wbr>User<wbr>Pool<wbr>Sms<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SMS Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the SMS verification message. Conflicts with `verification_message_template` configuration block `sms_message` argument.
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
A mapping of tags to assign to the User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Add<wbr>Ons</td>
            <td class="align-top">
                
                <code><a href="#userpooluserpooladdons">cognito.<wbr>User<wbr>Pool<wbr>User<wbr>Pool<wbr>Add<wbr>Ons?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for user pool add-ons to enable user pool advanced security mode features.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">username<wbr>Attributes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">verification<wbr>Message<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#userpoolverificationmessagetemplate">cognito.<wbr>User<wbr>Pool<wbr>Verification<wbr>Message<wbr>Template?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The verification message templates configuration.
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
            <td class="align-top">admin_<wbr>create_<wbr>user_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#userpooladmincreateuserconfig">Dict[User<wbr>Pool<wbr>Admin<wbr>Create<wbr>User<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for AdminCreateUser requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">alias_<wbr>attributes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>verified_<wbr>attributes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The attributes to be auto-verified. Possible values: email, phone_number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">device_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#userpooldeviceconfiguration">Dict[User<wbr>Pool<wbr>Device<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for the user pool&#39;s device tracking.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolemailconfiguration">Dict[User<wbr>Pool<wbr>Email<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Email Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email_<wbr>verification_<wbr>message</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the email verification message. Conflicts with `verification_message_template` configuration block `email_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email_<wbr>verification_<wbr>subject</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the email verification subject. Conflicts with `verification_message_template` configuration block `email_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#userpoollambdaconfig">Dict[User<wbr>Pool<wbr>Lambda<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container for the AWS Lambda triggers associated with the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mfa_<wbr>configuration</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)
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
The name of the attribute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password_<wbr>policy</td>
            <td class="align-top">
                
                <code><a href="#userpoolpasswordpolicy">Dict[User<wbr>Pool<wbr>Password<wbr>Policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container for information about the user pool password policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">schemas</td>
            <td class="align-top">
                
                <code><a href="#userpoolschema">List[User<wbr>Pool<wbr>Schema]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container with the schema attributes of a user pool. Schema attributes from the [standard attribute set](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes) only need to be specified if they are different from the default configuration. Maximum of 50 attributes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms_<wbr>authentication_<wbr>message</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the SMS authentication message.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolsmsconfiguration">Dict[User<wbr>Pool<wbr>Sms<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SMS Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms_<wbr>verification_<wbr>message</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the SMS verification message. Conflicts with `verification_message_template` configuration block `sms_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>pool_<wbr>add_<wbr>ons</td>
            <td class="align-top">
                
                <code><a href="#userpooluserpooladdons">Dict[User<wbr>Pool<wbr>User<wbr>Pool<wbr>Add<wbr>Ons]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for user pool add-ons to enable user pool advanced security mode features.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">username_<wbr>attributes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">verification_<wbr>message_<wbr>template</td>
            <td class="align-top">
                
                <code><a href="#userpoolverificationmessagetemplate">Dict[User<wbr>Pool<wbr>Verification<wbr>Message<wbr>Template]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The verification message templates configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## UserPool Output Properties

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
            <td class="align-top">Admin<wbr>Create<wbr>User<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpooladmincreateuserconfig">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Admin<wbr>Create<wbr>User<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} The configuration for AdminCreateUser requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Alias<wbr>Attributes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Verified<wbr>Attributes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} The attributes to be auto-verified. Possible values: email, phone_number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Creation<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date the user pool was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Device<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpooldeviceconfiguration">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Device<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} The configuration for the user pool&#39;s device tracking.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolemailconfiguration">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Email<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} The Email Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A string representing the email verification message. Conflicts with `verification_message_template` configuration block `email_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Verification<wbr>Subject</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A string representing the email verification subject. Conflicts with `verification_message_template` configuration block `email_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpoollambdaconfig">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Lambda<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} A container for the AWS Lambda triggers associated with the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Modified<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date the user pool was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mfa<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the attribute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#userpoolpasswordpolicy">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Password<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} A container for information about the user pool password policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Schemas</td>
            <td class="align-top">
                
                <code><a href="#userpoolschema">List&lt;Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Schema&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A container with the schema attributes of a user pool. Schema attributes from the [standard attribute set](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes) only need to be specified if they are different from the default configuration. Maximum of 50 attributes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Authentication<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A string representing the SMS authentication message.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolsmsconfiguration">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Sms<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} The SMS Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A string representing the SMS verification message. Conflicts with `verification_message_template` configuration block `sms_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Add<wbr>Ons</td>
            <td class="align-top">
                
                <code><a href="#userpooluserpooladdons">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>User<wbr>Pool<wbr>Add<wbr>Ons?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for user pool add-ons to enable user pool advanced security mode features.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Username<wbr>Attributes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Verification<wbr>Message<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#userpoolverificationmessagetemplate">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Verification<wbr>Message<wbr>Template</a></code>
            </td>
            <td class="align-top">{{% md %}} The verification message templates configuration.
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
            <td class="align-top">Admin<wbr>Create<wbr>User<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpooladmincreateuserconfig">User<wbr>Pool<wbr>Admin<wbr>Create<wbr>User<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} The configuration for AdminCreateUser requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Alias<wbr>Attributes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Verified<wbr>Attributes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} The attributes to be auto-verified. Possible values: email, phone_number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Creation<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date the user pool was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Device<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpooldeviceconfiguration">*User<wbr>Pool<wbr>Device<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} The configuration for the user pool&#39;s device tracking.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolemailconfiguration">*User<wbr>Pool<wbr>Email<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} The Email Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A string representing the email verification message. Conflicts with `verification_message_template` configuration block `email_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Verification<wbr>Subject</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A string representing the email verification subject. Conflicts with `verification_message_template` configuration block `email_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpoollambdaconfig">User<wbr>Pool<wbr>Lambda<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} A container for the AWS Lambda triggers associated with the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Modified<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date the user pool was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mfa<wbr>Configuration</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the attribute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#userpoolpasswordpolicy">User<wbr>Pool<wbr>Password<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} A container for information about the user pool password policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Schemas</td>
            <td class="align-top">
                
                <code><a href="#userpoolschema">[]User<wbr>Pool<wbr>Schema</a></code>
            </td>
            <td class="align-top">{{% md %}} A container with the schema attributes of a user pool. Schema attributes from the [standard attribute set](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes) only need to be specified if they are different from the default configuration. Maximum of 50 attributes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Authentication<wbr>Message</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} A string representing the SMS authentication message.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolsmsconfiguration">*User<wbr>Pool<wbr>Sms<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} The SMS Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A string representing the SMS verification message. Conflicts with `verification_message_template` configuration block `sms_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Add<wbr>Ons</td>
            <td class="align-top">
                
                <code><a href="#userpooluserpooladdons">*User<wbr>Pool<wbr>User<wbr>Pool<wbr>Add<wbr>Ons</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for user pool add-ons to enable user pool advanced security mode features.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Username<wbr>Attributes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Verification<wbr>Message<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#userpoolverificationmessagetemplate">User<wbr>Pool<wbr>Verification<wbr>Message<wbr>Template</a></code>
            </td>
            <td class="align-top">{{% md %}} The verification message templates configuration.
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
            <td class="align-top">admin<wbr>Create<wbr>User<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpooladmincreateuserconfig">cognito.<wbr>User<wbr>Pool<wbr>Admin<wbr>Create<wbr>User<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} The configuration for AdminCreateUser requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">alias<wbr>Attributes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Verified<wbr>Attributes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} The attributes to be auto-verified. Possible values: email, phone_number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">creation<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date the user pool was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">device<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpooldeviceconfiguration">cognito.<wbr>User<wbr>Pool<wbr>Device<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} The configuration for the user pool&#39;s device tracking.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolemailconfiguration">cognito.<wbr>User<wbr>Pool<wbr>Email<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} The Email Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A string representing the email verification message. Conflicts with `verification_message_template` configuration block `email_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Verification<wbr>Subject</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A string representing the email verification subject. Conflicts with `verification_message_template` configuration block `email_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpoollambdaconfig">cognito.<wbr>User<wbr>Pool<wbr>Lambda<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} A container for the AWS Lambda triggers associated with the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last<wbr>Modified<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date the user pool was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mfa<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the attribute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#userpoolpasswordpolicy">cognito.<wbr>User<wbr>Pool<wbr>Password<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} A container for information about the user pool password policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">schemas</td>
            <td class="align-top">
                
                <code><a href="#userpoolschema">cognito.<wbr>User<wbr>Pool<wbr>Schema[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A container with the schema attributes of a user pool. Schema attributes from the [standard attribute set](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes) only need to be specified if they are different from the default configuration. Maximum of 50 attributes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms<wbr>Authentication<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A string representing the SMS authentication message.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolsmsconfiguration">cognito.<wbr>User<wbr>Pool<wbr>Sms<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} The SMS Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A string representing the SMS verification message. Conflicts with `verification_message_template` configuration block `sms_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Add<wbr>Ons</td>
            <td class="align-top">
                
                <code><a href="#userpooluserpooladdons">cognito.<wbr>User<wbr>Pool<wbr>User<wbr>Pool<wbr>Add<wbr>Ons?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for user pool add-ons to enable user pool advanced security mode features.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">username<wbr>Attributes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">verification<wbr>Message<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#userpoolverificationmessagetemplate">cognito.<wbr>User<wbr>Pool<wbr>Verification<wbr>Message<wbr>Template</a></code>
            </td>
            <td class="align-top">{{% md %}} The verification message templates configuration.
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
            <td class="align-top">admin_<wbr>create_<wbr>user_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#userpooladmincreateuserconfig">Dict[User<wbr>Pool<wbr>Admin<wbr>Create<wbr>User<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} The configuration for AdminCreateUser requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">alias_<wbr>attributes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>verified_<wbr>attributes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} The attributes to be auto-verified. Possible values: email, phone_number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">creation_<wbr>date</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The date the user pool was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">device_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#userpooldeviceconfiguration">Dict[User<wbr>Pool<wbr>Device<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} The configuration for the user pool&#39;s device tracking.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolemailconfiguration">Dict[User<wbr>Pool<wbr>Email<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} The Email Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email_<wbr>verification_<wbr>message</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A string representing the email verification message. Conflicts with `verification_message_template` configuration block `email_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email_<wbr>verification_<wbr>subject</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A string representing the email verification subject. Conflicts with `verification_message_template` configuration block `email_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#userpoollambdaconfig">Dict[User<wbr>Pool<wbr>Lambda<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} A container for the AWS Lambda triggers associated with the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last_<wbr>modified_<wbr>date</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The date the user pool was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mfa_<wbr>configuration</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the attribute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password_<wbr>policy</td>
            <td class="align-top">
                
                <code><a href="#userpoolpasswordpolicy">Dict[User<wbr>Pool<wbr>Password<wbr>Policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} A container for information about the user pool password policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">schemas</td>
            <td class="align-top">
                
                <code><a href="#userpoolschema">List[User<wbr>Pool<wbr>Schema]</a></code>
            </td>
            <td class="align-top">{{% md %}} A container with the schema attributes of a user pool. Schema attributes from the [standard attribute set](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes) only need to be specified if they are different from the default configuration. Maximum of 50 attributes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms_<wbr>authentication_<wbr>message</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A string representing the SMS authentication message.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolsmsconfiguration">Dict[User<wbr>Pool<wbr>Sms<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} The SMS Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms_<wbr>verification_<wbr>message</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A string representing the SMS verification message. Conflicts with `verification_message_template` configuration block `sms_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>pool_<wbr>add_<wbr>ons</td>
            <td class="align-top">
                
                <code><a href="#userpooluserpooladdons">Dict[User<wbr>Pool<wbr>User<wbr>Pool<wbr>Add<wbr>Ons]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block for user pool add-ons to enable user pool advanced security mode features.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">username_<wbr>attributes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">verification_<wbr>message_<wbr>template</td>
            <td class="align-top">
                
                <code><a href="#userpoolverificationmessagetemplate">Dict[User<wbr>Pool<wbr>Verification<wbr>Message<wbr>Template]</a></code>
            </td>
            <td class="align-top">{{% md %}} The verification message templates configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing UserPool Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cognito/#UserPoolState">UserPoolState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cognito/#UserPool">UserPool</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>admin_create_user_config=None<span class="p">, </span>alias_attributes=None<span class="p">, </span>arn=None<span class="p">, </span>auto_verified_attributes=None<span class="p">, </span>creation_date=None<span class="p">, </span>device_configuration=None<span class="p">, </span>email_configuration=None<span class="p">, </span>email_verification_message=None<span class="p">, </span>email_verification_subject=None<span class="p">, </span>endpoint=None<span class="p">, </span>lambda_config=None<span class="p">, </span>last_modified_date=None<span class="p">, </span>mfa_configuration=None<span class="p">, </span>name=None<span class="p">, </span>password_policy=None<span class="p">, </span>schemas=None<span class="p">, </span>sms_authentication_message=None<span class="p">, </span>sms_configuration=None<span class="p">, </span>sms_verification_message=None<span class="p">, </span>tags=None<span class="p">, </span>user_pool_add_ons=None<span class="p">, </span>username_attributes=None<span class="p">, </span>verification_message_template=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetUserPool<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolState">UserPoolState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPool">UserPool</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPool.html">UserPool</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolState.html">UserPoolState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing UserPool resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Admin<wbr>Create<wbr>User<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpooladmincreateuserconfig">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Admin<wbr>Create<wbr>User<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for AdminCreateUser requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Alias<wbr>Attributes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.
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
The ARN of the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Verified<wbr>Attributes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The attributes to be auto-verified. Possible values: email, phone_number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Creation<wbr>Date</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date the user pool was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Device<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpooldeviceconfiguration">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Device<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for the user pool&#39;s device tracking.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolemailconfiguration">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Email<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Email Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the email verification message. Conflicts with `verification_message_template` configuration block `email_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Verification<wbr>Subject</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the email verification subject. Conflicts with `verification_message_template` configuration block `email_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpoollambdaconfig">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Lambda<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container for the AWS Lambda triggers associated with the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Modified<wbr>Date</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date the user pool was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mfa<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)
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
The name of the attribute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#userpoolpasswordpolicy">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Password<wbr>Policy<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container for information about the user pool password policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Schemas</td>
            <td class="align-top">
                
                <code><a href="#userpoolschema">List&lt;Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Schema<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container with the schema attributes of a user pool. Schema attributes from the [standard attribute set](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes) only need to be specified if they are different from the default configuration. Maximum of 50 attributes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Authentication<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the SMS authentication message.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolsmsconfiguration">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Sms<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SMS Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the SMS verification message. Conflicts with `verification_message_template` configuration block `sms_message` argument.
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
A mapping of tags to assign to the User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Add<wbr>Ons</td>
            <td class="align-top">
                
                <code><a href="#userpooluserpooladdons">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>User<wbr>Pool<wbr>Add<wbr>Ons<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for user pool add-ons to enable user pool advanced security mode features.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Username<wbr>Attributes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Verification<wbr>Message<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#userpoolverificationmessagetemplate">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Verification<wbr>Message<wbr>Template<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The verification message templates configuration.
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
            <td class="align-top">Admin<wbr>Create<wbr>User<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpooladmincreateuserconfig">*User<wbr>Pool<wbr>Admin<wbr>Create<wbr>User<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for AdminCreateUser requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Alias<wbr>Attributes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.
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
The ARN of the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Verified<wbr>Attributes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The attributes to be auto-verified. Possible values: email, phone_number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Creation<wbr>Date</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date the user pool was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Device<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpooldeviceconfiguration">*User<wbr>Pool<wbr>Device<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for the user pool&#39;s device tracking.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolemailconfiguration">*User<wbr>Pool<wbr>Email<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Email Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the email verification message. Conflicts with `verification_message_template` configuration block `email_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Verification<wbr>Subject</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the email verification subject. Conflicts with `verification_message_template` configuration block `email_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpoollambdaconfig">*User<wbr>Pool<wbr>Lambda<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container for the AWS Lambda triggers associated with the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Last<wbr>Modified<wbr>Date</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date the user pool was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mfa<wbr>Configuration</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)
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
The name of the attribute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#userpoolpasswordpolicy">*User<wbr>Pool<wbr>Password<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container for information about the user pool password policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Schemas</td>
            <td class="align-top">
                
                <code><a href="#userpoolschema">[]User<wbr>Pool<wbr>Schema</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container with the schema attributes of a user pool. Schema attributes from the [standard attribute set](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes) only need to be specified if they are different from the default configuration. Maximum of 50 attributes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Authentication<wbr>Message</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the SMS authentication message.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolsmsconfiguration">*User<wbr>Pool<wbr>Sms<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SMS Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the SMS verification message. Conflicts with `verification_message_template` configuration block `sms_message` argument.
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
A mapping of tags to assign to the User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Add<wbr>Ons</td>
            <td class="align-top">
                
                <code><a href="#userpooluserpooladdons">*User<wbr>Pool<wbr>User<wbr>Pool<wbr>Add<wbr>Ons</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for user pool add-ons to enable user pool advanced security mode features.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Username<wbr>Attributes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Verification<wbr>Message<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#userpoolverificationmessagetemplate">*User<wbr>Pool<wbr>Verification<wbr>Message<wbr>Template</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The verification message templates configuration.
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
            <td class="align-top">admin<wbr>Create<wbr>User<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpooladmincreateuserconfig">cognito.<wbr>User<wbr>Pool<wbr>Admin<wbr>Create<wbr>User<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for AdminCreateUser requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">alias<wbr>Attributes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.
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
The ARN of the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Verified<wbr>Attributes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The attributes to be auto-verified. Possible values: email, phone_number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">creation<wbr>Date</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date the user pool was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">device<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpooldeviceconfiguration">cognito.<wbr>User<wbr>Pool<wbr>Device<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for the user pool&#39;s device tracking.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolemailconfiguration">cognito.<wbr>User<wbr>Pool<wbr>Email<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Email Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the email verification message. Conflicts with `verification_message_template` configuration block `email_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Verification<wbr>Subject</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the email verification subject. Conflicts with `verification_message_template` configuration block `email_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#userpoollambdaconfig">cognito.<wbr>User<wbr>Pool<wbr>Lambda<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container for the AWS Lambda triggers associated with the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last<wbr>Modified<wbr>Date</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date the user pool was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mfa<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)
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
The name of the attribute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#userpoolpasswordpolicy">cognito.<wbr>User<wbr>Pool<wbr>Password<wbr>Policy?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container for information about the user pool password policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">schemas</td>
            <td class="align-top">
                
                <code><a href="#userpoolschema">cognito.<wbr>User<wbr>Pool<wbr>Schema[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container with the schema attributes of a user pool. Schema attributes from the [standard attribute set](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes) only need to be specified if they are different from the default configuration. Maximum of 50 attributes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms<wbr>Authentication<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the SMS authentication message.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolsmsconfiguration">cognito.<wbr>User<wbr>Pool<wbr>Sms<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SMS Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms<wbr>Verification<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the SMS verification message. Conflicts with `verification_message_template` configuration block `sms_message` argument.
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
A mapping of tags to assign to the User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Add<wbr>Ons</td>
            <td class="align-top">
                
                <code><a href="#userpooluserpooladdons">cognito.<wbr>User<wbr>Pool<wbr>User<wbr>Pool<wbr>Add<wbr>Ons?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for user pool add-ons to enable user pool advanced security mode features.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">username<wbr>Attributes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">verification<wbr>Message<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#userpoolverificationmessagetemplate">cognito.<wbr>User<wbr>Pool<wbr>Verification<wbr>Message<wbr>Template?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The verification message templates configuration.
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
            <td class="align-top">admin_<wbr>create_<wbr>user_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#userpooladmincreateuserconfig">Dict[User<wbr>Pool<wbr>Admin<wbr>Create<wbr>User<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for AdminCreateUser requests.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">alias_<wbr>attributes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Attributes supported as an alias for this user pool. Possible values: phone_number, email, or preferred_username. Conflicts with `username_attributes`.
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
The ARN of the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>verified_<wbr>attributes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The attributes to be auto-verified. Possible values: email, phone_number.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">creation_<wbr>date</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date the user pool was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">device_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#userpooldeviceconfiguration">Dict[User<wbr>Pool<wbr>Device<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration for the user pool&#39;s device tracking.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolemailconfiguration">Dict[User<wbr>Pool<wbr>Email<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Email Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email_<wbr>verification_<wbr>message</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the email verification message. Conflicts with `verification_message_template` configuration block `email_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email_<wbr>verification_<wbr>subject</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the email verification subject. Conflicts with `verification_message_template` configuration block `email_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The endpoint name of the user pool. Example format: cognito-idp.REGION.amazonaws.com/xxxx_yyyyy
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#userpoollambdaconfig">Dict[User<wbr>Pool<wbr>Lambda<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container for the AWS Lambda triggers associated with the user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">last_<wbr>modified_<wbr>date</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The date the user pool was last modified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mfa_<wbr>configuration</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to enable multi-factor authentication. Must be one of the following values (ON, OFF, OPTIONAL)
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
The name of the attribute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password_<wbr>policy</td>
            <td class="align-top">
                
                <code><a href="#userpoolpasswordpolicy">Dict[User<wbr>Pool<wbr>Password<wbr>Policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container for information about the user pool password policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">schemas</td>
            <td class="align-top">
                
                <code><a href="#userpoolschema">List[User<wbr>Pool<wbr>Schema]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A container with the schema attributes of a user pool. Schema attributes from the [standard attribute set](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes) only need to be specified if they are different from the default configuration. Maximum of 50 attributes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms_<wbr>authentication_<wbr>message</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the SMS authentication message.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#userpoolsmsconfiguration">Dict[User<wbr>Pool<wbr>Sms<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SMS Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms_<wbr>verification_<wbr>message</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string representing the SMS verification message. Conflicts with `verification_message_template` configuration block `sms_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the User Pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>pool_<wbr>add_<wbr>ons</td>
            <td class="align-top">
                
                <code><a href="#userpooluserpooladdons">Dict[User<wbr>Pool<wbr>User<wbr>Pool<wbr>Add<wbr>Ons]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block for user pool add-ons to enable user pool advanced security mode features.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">username_<wbr>attributes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether email addresses or phone numbers can be specified as usernames when a user signs up. Conflicts with `alias_attributes`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">verification_<wbr>message_<wbr>template</td>
            <td class="align-top">
                
                <code><a href="#userpoolverificationmessagetemplate">Dict[User<wbr>Pool<wbr>Verification<wbr>Message<wbr>Template]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The verification message templates configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### UserPoolAdminCreateUserConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UserPoolAdminCreateUserConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UserPoolAdminCreateUserConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolAdminCreateUserConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolAdminCreateUserConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolAdminCreateUserConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolAdminCreateUserConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Allow<wbr>Admin<wbr>Create<wbr>User<wbr>Only</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Invite<wbr>Message<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#userpooladmincreateuserconfiginvitemessagetemplate">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Admin<wbr>Create<wbr>User<wbr>Config<wbr>Invite<wbr>Message<wbr>Template<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The invite message template structure.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Unused<wbr>Account<wbr>Validity<wbr>Days</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
**DEPRECATED** Use password_policy.temporary_password_validity_days instead - The user account expiration limit, in days, after which the account is no longer usable.
 {{% /md %}}

            Use password_policy.temporary_password_validity_days instead
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
            <td class="align-top">Allow<wbr>Admin<wbr>Create<wbr>User<wbr>Only</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Invite<wbr>Message<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#userpooladmincreateuserconfiginvitemessagetemplate">*User<wbr>Pool<wbr>Admin<wbr>Create<wbr>User<wbr>Config<wbr>Invite<wbr>Message<wbr>Template</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The invite message template structure.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Unused<wbr>Account<wbr>Validity<wbr>Days</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
**DEPRECATED** Use password_policy.temporary_password_validity_days instead - The user account expiration limit, in days, after which the account is no longer usable.
 {{% /md %}}

            Use password_policy.temporary_password_validity_days instead
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
            <td class="align-top">allow<wbr>Admin<wbr>Create<wbr>User<wbr>Only</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">invite<wbr>Message<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#userpooladmincreateuserconfiginvitemessagetemplate">cognito.<wbr>User<wbr>Pool<wbr>Admin<wbr>Create<wbr>User<wbr>Config<wbr>Invite<wbr>Message<wbr>Template?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The invite message template structure.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">unused<wbr>Account<wbr>Validity<wbr>Days</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
**DEPRECATED** Use password_policy.temporary_password_validity_days instead - The user account expiration limit, in days, after which the account is no longer usable.
 {{% /md %}}

            Use password_policy.temporary_password_validity_days instead
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
            <td class="align-top">allow<wbr>Admin<wbr>Create<wbr>User<wbr>Only</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to True if only the administrator is allowed to create user profiles. Set to False if users can sign themselves up via an app.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">invite<wbr>Message<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#userpooladmincreateuserconfiginvitemessagetemplate">Dict[User<wbr>Pool<wbr>Admin<wbr>Create<wbr>User<wbr>Config<wbr>Invite<wbr>Message<wbr>Template]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The invite message template structure.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">unused<wbr>Account<wbr>Validity<wbr>Days</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
**DEPRECATED** Use password_policy.temporary_password_validity_days instead - The user account expiration limit, in days, after which the account is no longer usable.
 {{% /md %}}

            Use password_policy.temporary_password_validity_days instead
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### UserPoolAdminCreateUserConfigInviteMessageTemplate
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UserPoolAdminCreateUserConfigInviteMessageTemplate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UserPoolAdminCreateUserConfigInviteMessageTemplate">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolAdminCreateUserConfigInviteMessageTemplateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolAdminCreateUserConfigInviteMessageTemplateOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolAdminCreateUserConfigInviteMessageTemplateArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolAdminCreateUserConfigInviteMessageTemplate.html">output</a> API doc for this type.
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
            <td class="align-top">Email<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The email message template. Must contain the `{####}` placeholder. Conflicts with `email_verification_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Subject</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The subject line for the email message template. Conflicts with `email_verification_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SMS message template. Must contain the `{####}` placeholder. Conflicts with `sms_verification_message` argument.
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
            <td class="align-top">Email<wbr>Message</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The email message template. Must contain the `{####}` placeholder. Conflicts with `email_verification_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Subject</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The subject line for the email message template. Conflicts with `email_verification_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Message</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SMS message template. Must contain the `{####}` placeholder. Conflicts with `sms_verification_message` argument.
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
            <td class="align-top">email<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The email message template. Must contain the `{####}` placeholder. Conflicts with `email_verification_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Subject</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The subject line for the email message template. Conflicts with `email_verification_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SMS message template. Must contain the `{####}` placeholder. Conflicts with `sms_verification_message` argument.
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
            <td class="align-top">email<wbr>Message</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The email message template. Must contain the `{####}` placeholder. Conflicts with `email_verification_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Subject</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The subject line for the email message template. Conflicts with `email_verification_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms<wbr>Message</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SMS message template. Must contain the `{####}` placeholder. Conflicts with `sms_verification_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### UserPoolDeviceConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UserPoolDeviceConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UserPoolDeviceConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolDeviceConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolDeviceConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolDeviceConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolDeviceConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">Challenge<wbr>Required<wbr>On<wbr>New<wbr>Device</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether a challenge is required on a new device. Only applicable to a new device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Device<wbr>Only<wbr>Remembered<wbr>On<wbr>User<wbr>Prompt</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, a device is only remembered on user prompt.
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
            <td class="align-top">Challenge<wbr>Required<wbr>On<wbr>New<wbr>Device</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether a challenge is required on a new device. Only applicable to a new device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Device<wbr>Only<wbr>Remembered<wbr>On<wbr>User<wbr>Prompt</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, a device is only remembered on user prompt.
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
            <td class="align-top">challenge<wbr>Required<wbr>On<wbr>New<wbr>Device</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether a challenge is required on a new device. Only applicable to a new device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">device<wbr>Only<wbr>Remembered<wbr>On<wbr>User<wbr>Prompt</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, a device is only remembered on user prompt.
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
            <td class="align-top">challenge<wbr>Required<wbr>On<wbr>New<wbr>Device</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether a challenge is required on a new device. Only applicable to a new device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">device<wbr>Only<wbr>Remembered<wbr>On<wbr>User<wbr>Prompt</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, a device is only remembered on user prompt.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### UserPoolEmailConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UserPoolEmailConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UserPoolEmailConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolEmailConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolEmailConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolEmailConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolEmailConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">Email<wbr>Sending<wbr>Account</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instruct Cognito to either use its built-in functional or Amazon SES to send out emails.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Reply<wbr>To<wbr>Email<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The REPLY-TO email address.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the email source.
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
            <td class="align-top">Email<wbr>Sending<wbr>Account</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instruct Cognito to either use its built-in functional or Amazon SES to send out emails.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Reply<wbr>To<wbr>Email<wbr>Address</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The REPLY-TO email address.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the email source.
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
            <td class="align-top">email<wbr>Sending<wbr>Account</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instruct Cognito to either use its built-in functional or Amazon SES to send out emails.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">reply<wbr>To<wbr>Email<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The REPLY-TO email address.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the email source.
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
            <td class="align-top">email<wbr>Sending<wbr>Account</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instruct Cognito to either use its built-in functional or Amazon SES to send out emails.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">reply<wbr>To<wbr>Email<wbr>Address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The REPLY-TO email address.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the email source.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### UserPoolLambdaConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UserPoolLambdaConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UserPoolLambdaConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolLambdaConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolLambdaConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolLambdaConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolLambdaConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Create<wbr>Auth<wbr>Challenge</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the lambda creating an authentication challenge.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A custom Message AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Define<wbr>Auth<wbr>Challenge</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines the authentication challenge.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Post<wbr>Authentication</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A post-authentication AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Post<wbr>Confirmation</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A post-confirmation AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pre<wbr>Authentication</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A pre-authentication AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pre<wbr>Sign<wbr>Up</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A pre-registration AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pre<wbr>Token<wbr>Generation</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow to customize identity token claims before token generation.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Migration</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user migration Lambda config type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Verify<wbr>Auth<wbr>Challenge<wbr>Response</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Verifies the authentication challenge response.
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
            <td class="align-top">Create<wbr>Auth<wbr>Challenge</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the lambda creating an authentication challenge.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Message</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A custom Message AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Define<wbr>Auth<wbr>Challenge</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines the authentication challenge.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Post<wbr>Authentication</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A post-authentication AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Post<wbr>Confirmation</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A post-confirmation AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pre<wbr>Authentication</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A pre-authentication AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pre<wbr>Sign<wbr>Up</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A pre-registration AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pre<wbr>Token<wbr>Generation</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow to customize identity token claims before token generation.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Migration</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user migration Lambda config type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Verify<wbr>Auth<wbr>Challenge<wbr>Response</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Verifies the authentication challenge response.
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
            <td class="align-top">create<wbr>Auth<wbr>Challenge</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the lambda creating an authentication challenge.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A custom Message AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">define<wbr>Auth<wbr>Challenge</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines the authentication challenge.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">post<wbr>Authentication</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A post-authentication AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">post<wbr>Confirmation</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A post-confirmation AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pre<wbr>Authentication</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A pre-authentication AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pre<wbr>Sign<wbr>Up</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A pre-registration AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pre<wbr>Token<wbr>Generation</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow to customize identity token claims before token generation.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Migration</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user migration Lambda config type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">verify<wbr>Auth<wbr>Challenge<wbr>Response</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Verifies the authentication challenge response.
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
            <td class="align-top">create<wbr>Auth<wbr>Challenge</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the lambda creating an authentication challenge.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Message</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A custom Message AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">define<wbr>Auth<wbr>Challenge</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines the authentication challenge.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">post<wbr>Authentication</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A post-authentication AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">post<wbr>Confirmation</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A post-confirmation AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pre<wbr>Authentication</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A pre-authentication AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pre<wbr>Sign<wbr>Up</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A pre-registration AWS Lambda trigger.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pre<wbr>Token<wbr>Generation</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allow to customize identity token claims before token generation.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Migration</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user migration Lambda config type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">verify<wbr>Auth<wbr>Challenge<wbr>Response</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Verifies the authentication challenge response.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### UserPoolPasswordPolicy
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UserPoolPasswordPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UserPoolPasswordPolicy">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolPasswordPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolPasswordPolicyOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolPasswordPolicyArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolPasswordPolicy.html">output</a> API doc for this type.
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
            <td class="align-top">Minimum<wbr>Length</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum length of the password policy that you have set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Lowercase</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you have required users to use at least one lowercase letter in their password.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Numbers</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you have required users to use at least one number in their password.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Symbols</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you have required users to use at least one symbol in their password.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Uppercase</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you have required users to use at least one uppercase letter in their password.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Temporary<wbr>Password<wbr>Validity<wbr>Days</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
In the password policy you have set, refers to the number of days a temporary password is valid. If the user does not sign-in during this time, their password will need to be reset by an administrator.
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
            <td class="align-top">Minimum<wbr>Length</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum length of the password policy that you have set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Lowercase</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you have required users to use at least one lowercase letter in their password.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Numbers</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you have required users to use at least one number in their password.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Symbols</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you have required users to use at least one symbol in their password.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Uppercase</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you have required users to use at least one uppercase letter in their password.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Temporary<wbr>Password<wbr>Validity<wbr>Days</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
In the password policy you have set, refers to the number of days a temporary password is valid. If the user does not sign-in during this time, their password will need to be reset by an administrator.
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
            <td class="align-top">minimum<wbr>Length</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum length of the password policy that you have set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require<wbr>Lowercase</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you have required users to use at least one lowercase letter in their password.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require<wbr>Numbers</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you have required users to use at least one number in their password.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require<wbr>Symbols</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you have required users to use at least one symbol in their password.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require<wbr>Uppercase</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you have required users to use at least one uppercase letter in their password.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">temporary<wbr>Password<wbr>Validity<wbr>Days</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
In the password policy you have set, refers to the number of days a temporary password is valid. If the user does not sign-in during this time, their password will need to be reset by an administrator.
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
            <td class="align-top">minimum<wbr>Length</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum length of the password policy that you have set.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require<wbr>Lowercase</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you have required users to use at least one lowercase letter in their password.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require_<wbr>numbers</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you have required users to use at least one number in their password.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require_<wbr>symbols</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you have required users to use at least one symbol in their password.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require<wbr>Uppercase</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether you have required users to use at least one uppercase letter in their password.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">temporary<wbr>Password<wbr>Validity<wbr>Days</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
In the password policy you have set, refers to the number of days a temporary password is valid. If the user does not sign-in during this time, their password will need to be reset by an administrator.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### UserPoolSchema
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UserPoolSchema">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UserPoolSchema">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolSchemaArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolSchemaOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolSchemaArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolSchema.html">output</a> API doc for this type.
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
            <td class="align-top">Attribute<wbr>Data<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The attribute data type. Must be one of `Boolean`, `Number`, `String`, `DateTime`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Developer<wbr>Only<wbr>Attribute</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the attribute type is developer only.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mutable</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the attribute can be changed once it has been created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the attribute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Number<wbr>Attribute<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#userpoolschemanumberattributeconstraints">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Schema<wbr>Number<wbr>Attribute<wbr>Constraints<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the constraints for an attribute of the number type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Required</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether a user pool attribute is required. If the attribute is required and the user does not provide a value, registration or sign-in will fail.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">String<wbr>Attribute<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#userpoolschemastringattributeconstraints">Pulumi.<wbr>Aws.<wbr>Cognito.<wbr>User<wbr>Pool<wbr>Schema<wbr>String<wbr>Attribute<wbr>Constraints<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
-Specifies the constraints for an attribute of the string type.
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
            <td class="align-top">Attribute<wbr>Data<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The attribute data type. Must be one of `Boolean`, `Number`, `String`, `DateTime`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Developer<wbr>Only<wbr>Attribute</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the attribute type is developer only.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mutable</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the attribute can be changed once it has been created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the attribute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Number<wbr>Attribute<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#userpoolschemanumberattributeconstraints">*User<wbr>Pool<wbr>Schema<wbr>Number<wbr>Attribute<wbr>Constraints</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the constraints for an attribute of the number type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Required</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether a user pool attribute is required. If the attribute is required and the user does not provide a value, registration or sign-in will fail.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">String<wbr>Attribute<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#userpoolschemastringattributeconstraints">*User<wbr>Pool<wbr>Schema<wbr>String<wbr>Attribute<wbr>Constraints</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
-Specifies the constraints for an attribute of the string type.
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
            <td class="align-top">attribute<wbr>Data<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The attribute data type. Must be one of `Boolean`, `Number`, `String`, `DateTime`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">developer<wbr>Only<wbr>Attribute</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the attribute type is developer only.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mutable</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the attribute can be changed once it has been created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the attribute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">number<wbr>Attribute<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#userpoolschemanumberattributeconstraints">cognito.<wbr>User<wbr>Pool<wbr>Schema<wbr>Number<wbr>Attribute<wbr>Constraints?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the constraints for an attribute of the number type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">required</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether a user pool attribute is required. If the attribute is required and the user does not provide a value, registration or sign-in will fail.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">string<wbr>Attribute<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#userpoolschemastringattributeconstraints">cognito.<wbr>User<wbr>Pool<wbr>Schema<wbr>String<wbr>Attribute<wbr>Constraints?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
-Specifies the constraints for an attribute of the string type.
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
            <td class="align-top">attribute<wbr>Data<wbr>Type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The attribute data type. Must be one of `Boolean`, `Number`, `String`, `DateTime`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">developer<wbr>Only<wbr>Attribute</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the attribute type is developer only.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mutable</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the attribute can be changed once it has been created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the attribute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">number<wbr>Attribute<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#userpoolschemanumberattributeconstraints">Dict[User<wbr>Pool<wbr>Schema<wbr>Number<wbr>Attribute<wbr>Constraints]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the constraints for an attribute of the number type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">required</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether a user pool attribute is required. If the attribute is required and the user does not provide a value, registration or sign-in will fail.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">string<wbr>Attribute<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#userpoolschemastringattributeconstraints">Dict[User<wbr>Pool<wbr>Schema<wbr>String<wbr>Attribute<wbr>Constraints]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
-Specifies the constraints for an attribute of the string type.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### UserPoolSchemaNumberAttributeConstraints
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UserPoolSchemaNumberAttributeConstraints">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UserPoolSchemaNumberAttributeConstraints">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolSchemaNumberAttributeConstraintsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolSchemaNumberAttributeConstraintsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolSchemaNumberAttributeConstraintsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolSchemaNumberAttributeConstraints.html">output</a> API doc for this type.
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
            <td class="align-top">Max<wbr>Value</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum value of an attribute that is of the number data type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Value</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum value of an attribute that is of the number data type.
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
            <td class="align-top">Max<wbr>Value</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum value of an attribute that is of the number data type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Value</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum value of an attribute that is of the number data type.
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
            <td class="align-top">max<wbr>Value</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum value of an attribute that is of the number data type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Value</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum value of an attribute that is of the number data type.
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
            <td class="align-top">max<wbr>Value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum value of an attribute that is of the number data type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum value of an attribute that is of the number data type.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### UserPoolSchemaStringAttributeConstraints
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UserPoolSchemaStringAttributeConstraints">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UserPoolSchemaStringAttributeConstraints">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolSchemaStringAttributeConstraintsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolSchemaStringAttributeConstraintsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolSchemaStringAttributeConstraintsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolSchemaStringAttributeConstraints.html">output</a> API doc for this type.
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
            <td class="align-top">Max<wbr>Length</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum length of an attribute value of the string type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Length</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum length of an attribute value of the string type.
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
            <td class="align-top">Max<wbr>Length</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum length of an attribute value of the string type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Length</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum length of an attribute value of the string type.
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
            <td class="align-top">max<wbr>Length</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum length of an attribute value of the string type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Length</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum length of an attribute value of the string type.
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
            <td class="align-top">max<wbr>Length</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum length of an attribute value of the string type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Length</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum length of an attribute value of the string type.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### UserPoolSmsConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UserPoolSmsConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UserPoolSmsConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolSmsConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolSmsConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolSmsConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolSmsConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">External<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The external ID used in IAM role trust relationships. For more information about using external IDs, see [How to Use an External ID When Granting Access to Your AWS Resources to a Third Party](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns<wbr>Caller<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Amazon SNS caller. This is usually the IAM role that you&#39;ve given Cognito permission to assume.
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
            <td class="align-top">External<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The external ID used in IAM role trust relationships. For more information about using external IDs, see [How to Use an External ID When Granting Access to Your AWS Resources to a Third Party](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns<wbr>Caller<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Amazon SNS caller. This is usually the IAM role that you&#39;ve given Cognito permission to assume.
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
            <td class="align-top">external<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The external ID used in IAM role trust relationships. For more information about using external IDs, see [How to Use an External ID When Granting Access to Your AWS Resources to a Third Party](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns<wbr>Caller<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Amazon SNS caller. This is usually the IAM role that you&#39;ve given Cognito permission to assume.
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
            <td class="align-top">external<wbr>Id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The external ID used in IAM role trust relationships. For more information about using external IDs, see [How to Use an External ID When Granting Access to Your AWS Resources to a Third Party](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns<wbr>Caller<wbr>Arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Amazon SNS caller. This is usually the IAM role that you&#39;ve given Cognito permission to assume.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### UserPoolUserPoolAddOns
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UserPoolUserPoolAddOns">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UserPoolUserPoolAddOns">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolUserPoolAddOnsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolUserPoolAddOnsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolUserPoolAddOnsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolUserPoolAddOns.html">output</a> API doc for this type.
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
            <td class="align-top">Advanced<wbr>Security<wbr>Mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The mode for advanced security, must be one of `OFF`, `AUDIT` or `ENFORCED`.
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
            <td class="align-top">Advanced<wbr>Security<wbr>Mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The mode for advanced security, must be one of `OFF`, `AUDIT` or `ENFORCED`.
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
            <td class="align-top">advanced<wbr>Security<wbr>Mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The mode for advanced security, must be one of `OFF`, `AUDIT` or `ENFORCED`.
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
            <td class="align-top">advanced<wbr>Security<wbr>Mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The mode for advanced security, must be one of `OFF`, `AUDIT` or `ENFORCED`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### UserPoolVerificationMessageTemplate
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UserPoolVerificationMessageTemplate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UserPoolVerificationMessageTemplate">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolVerificationMessageTemplateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cognito?tab=doc#UserPoolVerificationMessageTemplateOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolVerificationMessageTemplateArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cognito.UserPoolVerificationMessageTemplate.html">output</a> API doc for this type.
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
            <td class="align-top">Default<wbr>Email<wbr>Option</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default email option. Must be either `CONFIRM_WITH_CODE` or `CONFIRM_WITH_LINK`. Defaults to `CONFIRM_WITH_CODE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The email message template. Must contain the `{####}` placeholder. Conflicts with `email_verification_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Message<wbr>By<wbr>Link</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The email message template for sending a confirmation link to the user, it must contain the `{##Click Here##}` placeholder.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Subject</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The subject line for the email message template. Conflicts with `email_verification_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Subject<wbr>By<wbr>Link</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The subject line for the email message template for sending a confirmation link to the user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SMS message template. Must contain the `{####}` placeholder. Conflicts with `sms_verification_message` argument.
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
            <td class="align-top">Default<wbr>Email<wbr>Option</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default email option. Must be either `CONFIRM_WITH_CODE` or `CONFIRM_WITH_LINK`. Defaults to `CONFIRM_WITH_CODE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Message</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The email message template. Must contain the `{####}` placeholder. Conflicts with `email_verification_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Message<wbr>By<wbr>Link</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The email message template for sending a confirmation link to the user, it must contain the `{##Click Here##}` placeholder.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Subject</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The subject line for the email message template. Conflicts with `email_verification_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Email<wbr>Subject<wbr>By<wbr>Link</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The subject line for the email message template for sending a confirmation link to the user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sms<wbr>Message</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SMS message template. Must contain the `{####}` placeholder. Conflicts with `sms_verification_message` argument.
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
            <td class="align-top">default<wbr>Email<wbr>Option</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default email option. Must be either `CONFIRM_WITH_CODE` or `CONFIRM_WITH_LINK`. Defaults to `CONFIRM_WITH_CODE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The email message template. Must contain the `{####}` placeholder. Conflicts with `email_verification_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Message<wbr>By<wbr>Link</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The email message template for sending a confirmation link to the user, it must contain the `{##Click Here##}` placeholder.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Subject</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The subject line for the email message template. Conflicts with `email_verification_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Subject<wbr>By<wbr>Link</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The subject line for the email message template for sending a confirmation link to the user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms<wbr>Message</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SMS message template. Must contain the `{####}` placeholder. Conflicts with `sms_verification_message` argument.
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
            <td class="align-top">default<wbr>Email<wbr>Option</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default email option. Must be either `CONFIRM_WITH_CODE` or `CONFIRM_WITH_LINK`. Defaults to `CONFIRM_WITH_CODE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Message</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The email message template. Must contain the `{####}` placeholder. Conflicts with `email_verification_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Message<wbr>By<wbr>Link</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The email message template for sending a confirmation link to the user, it must contain the `{##Click Here##}` placeholder.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Subject</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The subject line for the email message template. Conflicts with `email_verification_subject` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">email<wbr>Subject<wbr>By<wbr>Link</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The subject line for the email message template for sending a confirmation link to the user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sms<wbr>Message</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SMS message template. Must contain the `{####}` placeholder. Conflicts with `sms_verification_message` argument.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







