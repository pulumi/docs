
---
title: "GetSecrets"
block_external_search_index: true
---



Decrypt multiple secrets from data encrypted with the AWS KMS service.

{{% examples %}}
{{% /examples %}}





## Using GetSecrets

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getSecrets<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/kms/#GetSecretsArgs">GetSecretsArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/kms/#GetSecretsResult">GetSecretsResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_secrets(</span>secrets=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupSecrets<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kms?tab=doc#LookupSecretsArgs">LookupSecretsArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kms?tab=doc#LookupSecretsResult">LookupSecretsResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetSecrets </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kms.GetSecretsResult.html">GetSecretsResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Kms.GetSecretsArgs.html">GetSecretsArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsecretssecret">List&lt;Get<wbr>Secrets<wbr>Secret<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more encrypted payload definitions from the KMS service. See the Secret Definitions below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsecretssecret">[]Get<wbr>Secrets<wbr>Secret</a></span>
    </dt>
    <dd>{{% md %}}One or more encrypted payload definitions from the KMS service. See the Secret Definitions below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsecretssecret">Get<wbr>Secrets<wbr>Secret[]</a></span>
    </dt>
    <dd>{{% md %}}One or more encrypted payload definitions from the KMS service. See the Secret Definitions below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsecretssecret">List[Get<wbr>Secrets<wbr>Secret]</a></span>
    </dt>
    <dd>{{% md %}}One or more encrypted payload definitions from the KMS service. See the Secret Definitions below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetSecrets Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Plaintext</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string></span>
    </dt>
    <dd>{{% md %}}Map containing each `secret` `name` as the key with its decrypted plaintext value
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsecretssecret">List&lt;Get<wbr>Secrets<wbr>Secret&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Plaintext</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Map containing each `secret` `name` as the key with its decrypted plaintext value
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsecretssecret">[]Get<wbr>Secrets<wbr>Secret</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>plaintext</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}Map containing each `secret` `name` as the key with its decrypted plaintext value
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsecretssecret">Get<wbr>Secrets<wbr>Secret[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>plaintext</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Map containing each `secret` `name` as the key with its decrypted plaintext value
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsecretssecret">List[Get<wbr>Secrets<wbr>Secret]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Secrets<wbr>Secret</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetSecretsSecret">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetSecretsSecret">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kms?tab=doc#GetSecretsSecretArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/kms?tab=doc#GetSecretsSecret">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}An optional mapping that makes up the Encryption Context for the secret.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grant<wbr>Tokens</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}An optional list of Grant Tokens for the secret.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name to export this secret under in the attributes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Payload</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Base64 encoded payload, as returned from a KMS encrypt operation.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Context</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}An optional mapping that makes up the Encryption Context for the secret.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grant<wbr>Tokens</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}An optional list of Grant Tokens for the secret.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name to export this secret under in the attributes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Payload</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Base64 encoded payload, as returned from a KMS encrypt operation.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>context</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}An optional mapping that makes up the Encryption Context for the secret.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grant<wbr>Tokens</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}An optional list of Grant Tokens for the secret.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name to export this secret under in the attributes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>payload</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Base64 encoded payload, as returned from a KMS encrypt operation.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>context</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}An optional mapping that makes up the Encryption Context for the secret.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grant<wbr>Tokens</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}An optional list of Grant Tokens for the secret.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name to export this secret under in the attributes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>payload</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Base64 encoded payload, as returned from a KMS encrypt operation.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







