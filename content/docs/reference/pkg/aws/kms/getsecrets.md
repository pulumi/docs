
---
title: "GetSecrets"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Decrypt multiple secrets from data encrypted with the AWS KMS service.

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_secrets.html.markdown.





## Using GetSecrets

{{< langchoose csharp nojavascript >}}


<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getSecrets<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/kms/#GetSecretsArgs">GetSecretsArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#InvokeOptions">pulumi.InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/kms/#GetSecretsResult">GetSecretsResult</a></span>></span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_secrets(</span>secrets=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupSecrets<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kms?tab=doc#LookupSecretsArgs">LookupSecretsArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kms?tab=doc#LookupSecretsResult">LookupSecretsResult</a></span>, error)</span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kms.GetSecretsResult.html">Pulumi.Aws.Kms.GetSecretsResult</a></span>> <span class="p">GetSecrets(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kms.GetSecretsArgs.html">GetSecretsArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>



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
            <td class="align-top">Secrets</td>
            <td class="align-top">
                
                <code><a href="#getsecretssecret">List&lt;Pulumi.<wbr>Aws.<wbr>Kms.<wbr>Get<wbr>Secrets<wbr>Secret<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One or more encrypted payload definitions from the KMS service. See the Secret Definitions below.
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
            <td class="align-top">Secrets</td>
            <td class="align-top">
                
                <code><a href="#getsecretssecret">[]kms.<wbr>Get<wbr>Secrets<wbr>Secret</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One or more encrypted payload definitions from the KMS service. See the Secret Definitions below.
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
            <td class="align-top">secrets</td>
            <td class="align-top">
                
                <code><a href="#getsecretssecret">kms.<wbr>Get<wbr>Secrets<wbr>Secret[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One or more encrypted payload definitions from the KMS service. See the Secret Definitions below.
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
            <td class="align-top">secrets</td>
            <td class="align-top">
                
                <code><a href="#getsecretssecret">List[get_<wbr>secrets_<wbr>secret]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One or more encrypted payload definitions from the KMS service. See the Secret Definitions below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## GetSecrets Result

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
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Plaintext</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} Map containing each `secret` `name` as the key with its decrypted plaintext value
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Secrets</td>
            <td class="align-top">
                
                <code><a href="#getsecretssecret">List&lt;Pulumi.<wbr>Aws.<wbr>Kms.<wbr>Get<wbr>Secrets<wbr>Secret&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Plaintext</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} Map containing each `secret` `name` as the key with its decrypted plaintext value
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Secrets</td>
            <td class="align-top">
                
                <code><a href="#getsecretssecret">[]kms.<wbr>Get<wbr>Secrets<wbr>Secret</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">plaintext</td>
            <td class="align-top">
                
                <code>{[key: string]: string}</code>
            </td>
            <td class="align-top">{{% md %}} Map containing each `secret` `name` as the key with its decrypted plaintext value
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">secrets</td>
            <td class="align-top">
                
                <code><a href="#getsecretssecret">kms.<wbr>Get<wbr>Secrets<wbr>Secret[]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">plaintext</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} Map containing each `secret` `name` as the key with its decrypted plaintext value
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">secrets</td>
            <td class="align-top">
                
                <code><a href="#getsecretssecret">List[get_<wbr>secrets_<wbr>secret]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Supporting Types

#### GetSecretsSecret
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetSecretsSecret">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetSecretsSecret">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kms?tab=doc#GetSecretsSecretArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kms?tab=doc#GetSecretsSecret">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kms.GetSecretsSecretArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kms.GetSecretsSecret.html">output</a> API doc for this type.
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
            <td class="align-top">Context</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional mapping that makes up the Encryption Context for the secret.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grant<wbr>Tokens</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional list of Grant Tokens for the secret.
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
The name to export this secret under in the attributes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Payload</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Base64 encoded payload, as returned from a KMS encrypt operation.
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
            <td class="align-top">Context</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional mapping that makes up the Encryption Context for the secret.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Grant<wbr>Tokens</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional list of Grant Tokens for the secret.
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
The name to export this secret under in the attributes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Payload</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Base64 encoded payload, as returned from a KMS encrypt operation.
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
            <td class="align-top">context</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional mapping that makes up the Encryption Context for the secret.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grant<wbr>Tokens</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional list of Grant Tokens for the secret.
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
The name to export this secret under in the attributes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">payload</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Base64 encoded payload, as returned from a KMS encrypt operation.
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
            <td class="align-top">context</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional mapping that makes up the Encryption Context for the secret.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">grant_<wbr>tokens</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional list of Grant Tokens for the secret.
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
The name to export this secret under in the attributes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">payload</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Base64 encoded payload, as returned from a KMS encrypt operation.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







