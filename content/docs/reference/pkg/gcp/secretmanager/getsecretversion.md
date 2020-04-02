
---
title: "GetSecretVersion"
block_external_search_index: true
---

Get a Secret Manager secret's version. For more information see the [official documentation](https://cloud.google.com/secret-manager/docs/) and [API](https://cloud.google.com/secret-manager/docs/reference/rest/v1beta1/projects.secrets.versions).

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/datasource_google_secret_manager_secret_version.html.markdown.





## Using GetSecretVersion

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getSecretVersion<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/secretmanager/#GetSecretVersionArgs">GetSecretVersionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/secretmanager/#GetSecretVersionResult">GetSecretVersionResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_secret_version(</span>project=None<span class="p">, </span>secret=None<span class="p">, </span>version=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupSecretVersion<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/secretmanager?tab=doc#LookupSecretVersionArgs">LookupSecretVersionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/secretmanager?tab=doc#LookupSecretVersionResult">LookupSecretVersionResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetSecretVersion </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Secretmanager.GetSecretVersionResult.html">GetSecretVersionResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.SecretManager.GetSecretVersionArgs.html">GetSecretVersionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The project to get the secret version for. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secret to get the secret version for.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version of the secret to get. If it
is not provided, the latest version is retrieved.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The project to get the secret version for. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secret to get the secret version for.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The version of the secret to get. If it
is not provided, the latest version is retrieved.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The project to get the secret version for. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secret to get the secret version for.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version of the secret to get. If it
is not provided, the latest version is retrieved.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The project to get the secret version for. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The secret to get the secret version for.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The version of the secret to get. If it
is not provided, the latest version is retrieved.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetSecretVersion Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time at which the Secret was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Destroy<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time at which the Secret was destroyed. Only present if state is DESTROYED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}True if the current state of the SecretVersion is enabled.
{{% /md %}}</dd>

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
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The resource name of the SecretVersion. Format:
`projects/{{project}}/secrets/{{secret_id}}/versions/{{version}}`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secret<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secret data. No larger than 64KiB.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time at which the Secret was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Destroy<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time at which the Secret was destroyed. Only present if state is DESTROYED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}True if the current state of the SecretVersion is enabled.
{{% /md %}}</dd>

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
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The resource name of the SecretVersion. Format:
`projects/{{project}}/secrets/{{secret_id}}/versions/{{version}}`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secret<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secret data. No larger than 64KiB.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time at which the Secret was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>destroy<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time at which the Secret was destroyed. Only present if state is DESTROYED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}True if the current state of the SecretVersion is enabled.
{{% /md %}}</dd>

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
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The resource name of the SecretVersion. Format:
`projects/{{project}}/secrets/{{secret_id}}/versions/{{version}}`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secret<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secret data. No larger than 64KiB.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>create_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The time at which the Secret was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>destroy_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The time at which the Secret was destroyed. Only present if state is DESTROYED.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}True if the current state of the SecretVersion is enabled.
{{% /md %}}</dd>

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
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The resource name of the SecretVersion. Format:
`projects/{{project}}/secrets/{{secret_id}}/versions/{{version}}`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secret_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The secret data. No larger than 64KiB.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}







