
---
title: "AccountPasswordPolicy"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


> **Note:** There is only a single policy allowed per AWS account. An existing policy will be lost when using this resource as an effect of this limitation.

Manages Password Policy for the AWS Account.
See more about [Account Password Policy](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)
in the official AWS docs.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const strict = new aws.iam.AccountPasswordPolicy("strict", {
    allowUsersToChangePassword: true,
    minimumPasswordLength: 8,
    requireLowercaseCharacters: true,
    requireNumbers: true,
    requireSymbols: true,
    requireUppercaseCharacters: true,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_account_password_policy.html.markdown.



## Create a AccountPasswordPolicy Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/iam/#AccountPasswordPolicy">AccountPasswordPolicy</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/iam/#AccountPasswordPolicyArgs">AccountPasswordPolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">AccountPasswordPolicy</span><span class="p">(resource_name, id, opts=None, </span>allow_users_to_change_password=None<span class="p">, </span>hard_expiry=None<span class="p">, </span>max_password_age=None<span class="p">, </span>minimum_password_length=None<span class="p">, </span>password_reuse_prevention=None<span class="p">, </span>require_lowercase_characters=None<span class="p">, </span>require_numbers=None<span class="p">, </span>require_symbols=None<span class="p">, </span>require_uppercase_characters=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewAccountPasswordPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#AccountPasswordPolicyArgs">AccountPasswordPolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iam?tab=doc#AccountPasswordPolicy">AccountPasswordPolicy</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iam.AccountPasswordPolicy.html">AccountPasswordPolicy</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iam.AccountPasswordPolicyArgs.html">AccountPasswordPolicyArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a AccountPasswordPolicy resource with the given unique name, arguments, and options.

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
            <td class="align-top">Allow<wbr>Users<wbr>To<wbr>Change<wbr>Password</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to allow users to change their own password
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hard<wbr>Expiry</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Password<wbr>Age</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that an user password is valid.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Minimum<wbr>Password<wbr>Length</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Minimum length to require for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password<wbr>Reuse<wbr>Prevention</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of previous passwords that users are prevented from reusing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Lowercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to require lowercase characters for user passwords.
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
Whether to require numbers for user passwords.
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
Whether to require symbols for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Uppercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to require uppercase characters for user passwords.
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
            <td class="align-top">Allow<wbr>Users<wbr>To<wbr>Change<wbr>Password</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to allow users to change their own password
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hard<wbr>Expiry</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Password<wbr>Age</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that an user password is valid.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Minimum<wbr>Password<wbr>Length</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Minimum length to require for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password<wbr>Reuse<wbr>Prevention</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of previous passwords that users are prevented from reusing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Lowercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to require lowercase characters for user passwords.
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
Whether to require numbers for user passwords.
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
Whether to require symbols for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Uppercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to require uppercase characters for user passwords.
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
            <td class="align-top">allow<wbr>Users<wbr>To<wbr>Change<wbr>Password</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to allow users to change their own password
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hard<wbr>Expiry</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Password<wbr>Age</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that an user password is valid.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">minimum<wbr>Password<wbr>Length</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Minimum length to require for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password<wbr>Reuse<wbr>Prevention</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of previous passwords that users are prevented from reusing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require<wbr>Lowercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to require lowercase characters for user passwords.
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
Whether to require numbers for user passwords.
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
Whether to require symbols for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require<wbr>Uppercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to require uppercase characters for user passwords.
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
            <td class="align-top">allow_<wbr>users_<wbr>to_<wbr>change_<wbr>password</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to allow users to change their own password
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hard_<wbr>expiry</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>password_<wbr>age</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that an user password is valid.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">minimum_<wbr>password_<wbr>length</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Minimum length to require for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password_<wbr>reuse_<wbr>prevention</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of previous passwords that users are prevented from reusing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require_<wbr>lowercase_<wbr>characters</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to require lowercase characters for user passwords.
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
Whether to require numbers for user passwords.
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
Whether to require symbols for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require_<wbr>uppercase_<wbr>characters</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to require uppercase characters for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## AccountPasswordPolicy Output Properties

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
            <td class="align-top">Allow<wbr>Users<wbr>To<wbr>Change<wbr>Password</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to allow users to change their own password
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Expire<wbr>Passwords</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether passwords in the account expire.
Returns `true` if `max_password_age` contains a value greater than `0`.
Returns `false` if it is `0` or _not present_.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hard<wbr>Expiry</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Password<wbr>Age</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The number of days that an user password is valid.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Minimum<wbr>Password<wbr>Length</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} Minimum length to require for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password<wbr>Reuse<wbr>Prevention</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The number of previous passwords that users are prevented from reusing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Lowercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to require lowercase characters for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Numbers</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to require numbers for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Symbols</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to require symbols for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Uppercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to require uppercase characters for user passwords.
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
            <td class="align-top">Allow<wbr>Users<wbr>To<wbr>Change<wbr>Password</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to allow users to change their own password
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Expire<wbr>Passwords</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether passwords in the account expire.
Returns `true` if `max_password_age` contains a value greater than `0`.
Returns `false` if it is `0` or _not present_.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hard<wbr>Expiry</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Password<wbr>Age</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The number of days that an user password is valid.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Minimum<wbr>Password<wbr>Length</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} Minimum length to require for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password<wbr>Reuse<wbr>Prevention</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The number of previous passwords that users are prevented from reusing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Lowercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to require lowercase characters for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Numbers</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to require numbers for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Symbols</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to require symbols for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Uppercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to require uppercase characters for user passwords.
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
            <td class="align-top">allow<wbr>Users<wbr>To<wbr>Change<wbr>Password</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to allow users to change their own password
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">expire<wbr>Passwords</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether passwords in the account expire.
Returns `true` if `max_password_age` contains a value greater than `0`.
Returns `false` if it is `0` or _not present_.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hard<wbr>Expiry</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Password<wbr>Age</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The number of days that an user password is valid.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">minimum<wbr>Password<wbr>Length</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} Minimum length to require for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password<wbr>Reuse<wbr>Prevention</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The number of previous passwords that users are prevented from reusing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require<wbr>Lowercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Whether to require lowercase characters for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require<wbr>Numbers</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Whether to require numbers for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require<wbr>Symbols</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Whether to require symbols for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require<wbr>Uppercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Whether to require uppercase characters for user passwords.
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
            <td class="align-top">allow_<wbr>users_<wbr>to_<wbr>change_<wbr>password</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to allow users to change their own password
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">expire_<wbr>passwords</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether passwords in the account expire.
Returns `true` if `max_password_age` contains a value greater than `0`.
Returns `false` if it is `0` or _not present_.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hard_<wbr>expiry</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>password_<wbr>age</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The number of days that an user password is valid.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">minimum_<wbr>password_<wbr>length</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} Minimum length to require for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password_<wbr>reuse_<wbr>prevention</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The number of previous passwords that users are prevented from reusing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require_<wbr>lowercase_<wbr>characters</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to require lowercase characters for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require_<wbr>numbers</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to require numbers for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require_<wbr>symbols</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to require symbols for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require_<wbr>uppercase_<wbr>characters</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to require uppercase characters for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing AccountPasswordPolicy Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccountPasswordPolicyState, opts?: pulumi.CustomResourceOptions): AccountPasswordPolicy;
```

```python
def get(resource_name, id, opts=None, allow_<wbr>users_<wbr>to_<wbr>change_<wbr>password=None, expire_<wbr>passwords=None, hard_<wbr>expiry=None, max_<wbr>password_<wbr>age=None, minimum_<wbr>password_<wbr>length=None, password_<wbr>reuse_<wbr>prevention=None, require_<wbr>lowercase_<wbr>characters=None, require_<wbr>numbers=None, require_<wbr>symbols=None, require_<wbr>uppercase_<wbr>characters=None)
```

```go
func GetAccountPasswordPolicy(ctx *pulumi.Context, name string, id pulumi.IDInput, state *AccountPasswordPolicyState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static AccountPasswordPolicy Get(string name, Input<string> id, AccountPasswordPolicyState? state = null, CustomResourceOptions? options = null);
```

Get an existing AccountPasswordPolicy resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Allow<wbr>Users<wbr>To<wbr>Change<wbr>Password</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to allow users to change their own password
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Expire<wbr>Passwords</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether passwords in the account expire.
Returns `true` if `max_password_age` contains a value greater than `0`.
Returns `false` if it is `0` or _not present_.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hard<wbr>Expiry</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Password<wbr>Age</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that an user password is valid.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Minimum<wbr>Password<wbr>Length</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Minimum length to require for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password<wbr>Reuse<wbr>Prevention</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of previous passwords that users are prevented from reusing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Lowercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to require lowercase characters for user passwords.
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
Whether to require numbers for user passwords.
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
Whether to require symbols for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Uppercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to require uppercase characters for user passwords.
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
            <td class="align-top">Allow<wbr>Users<wbr>To<wbr>Change<wbr>Password</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to allow users to change their own password
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Expire<wbr>Passwords</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether passwords in the account expire.
Returns `true` if `max_password_age` contains a value greater than `0`.
Returns `false` if it is `0` or _not present_.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hard<wbr>Expiry</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Password<wbr>Age</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that an user password is valid.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Minimum<wbr>Password<wbr>Length</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Minimum length to require for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password<wbr>Reuse<wbr>Prevention</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of previous passwords that users are prevented from reusing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Lowercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to require lowercase characters for user passwords.
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
Whether to require numbers for user passwords.
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
Whether to require symbols for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Require<wbr>Uppercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to require uppercase characters for user passwords.
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
            <td class="align-top">allow<wbr>Users<wbr>To<wbr>Change<wbr>Password</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to allow users to change their own password
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">expire<wbr>Passwords</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether passwords in the account expire.
Returns `true` if `max_password_age` contains a value greater than `0`.
Returns `false` if it is `0` or _not present_.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hard<wbr>Expiry</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Password<wbr>Age</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that an user password is valid.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">minimum<wbr>Password<wbr>Length</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Minimum length to require for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password<wbr>Reuse<wbr>Prevention</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of previous passwords that users are prevented from reusing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require<wbr>Lowercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to require lowercase characters for user passwords.
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
Whether to require numbers for user passwords.
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
Whether to require symbols for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require<wbr>Uppercase<wbr>Characters</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to require uppercase characters for user passwords.
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
            <td class="align-top">allow_<wbr>users_<wbr>to_<wbr>change_<wbr>password</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to allow users to change their own password
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">expire_<wbr>passwords</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether passwords in the account expire.
Returns `true` if `max_password_age` contains a value greater than `0`.
Returns `false` if it is `0` or _not present_.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hard_<wbr>expiry</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether users are prevented from setting a new password after their password has expired
(i.e. require administrator reset)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>password_<wbr>age</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days that an user password is valid.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">minimum_<wbr>password_<wbr>length</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Minimum length to require for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password_<wbr>reuse_<wbr>prevention</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of previous passwords that users are prevented from reusing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require_<wbr>lowercase_<wbr>characters</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to require lowercase characters for user passwords.
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
Whether to require numbers for user passwords.
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
Whether to require symbols for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">require_<wbr>uppercase_<wbr>characters</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to require uppercase characters for user passwords.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}









