
---
title: "GetSecret"
block_external_search_index: true
---








## Using GetSecret

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getSecret<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/keymanager/#GetSecretArgs">GetSecretArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/keymanager/#GetSecretResult">GetSecretResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_secret(</span>acl_only=None<span class="p">, </span>algorithm=None<span class="p">, </span>bit_length=None<span class="p">, </span>created_at_filter=None<span class="p">, </span>expiration_filter=None<span class="p">, </span>mode=None<span class="p">, </span>name=None<span class="p">, </span>region=None<span class="p">, </span>secret_type=None<span class="p">, </span>updated_at_filter=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupSecret<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/keymanager?tab=doc#LookupSecretArgs">LookupSecretArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/keymanager?tab=doc#LookupSecretResult">LookupSecretResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetSecret </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Keymanager.GetSecretResult.html">GetSecretResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.KeyManager.GetSecretArgs.html">GetSecretArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Acl<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Select the Secret with an ACL that contains the user.
Project scope is ignored. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Secret algorithm.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bit<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The Secret bit length.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Created<wbr>At<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Date filter to select the Secret with
created matching the specified criteria. See Date Filters below for more
detail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Date filter to select the Secret with
expiration matching the specified criteria. See Date Filters below for more
detail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Secret mode.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Secret name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V1 KeyManager client.
A KeyManager client is needed to fetch a secret. If omitted, the `region`
argument of the provider is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Secret type. For more information see
[Secret types](https://docs.openstack.org/barbican/latest/api/reference/secret_types.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Updated<wbr>At<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Date filter to select the Secret with
updated matching the specified criteria. See Date Filters below for more
detail.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Acl<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Select the Secret with an ACL that contains the user.
Project scope is ignored. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Secret algorithm.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bit<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The Secret bit length.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Created<wbr>At<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Date filter to select the Secret with
created matching the specified criteria. See Date Filters below for more
detail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Date filter to select the Secret with
expiration matching the specified criteria. See Date Filters below for more
detail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Secret mode.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Secret name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V1 KeyManager client.
A KeyManager client is needed to fetch a secret. If omitted, the `region`
argument of the provider is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secret<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Secret type. For more information see
[Secret types](https://docs.openstack.org/barbican/latest/api/reference/secret_types.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Updated<wbr>At<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Date filter to select the Secret with
updated matching the specified criteria. See Date Filters below for more
detail.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>acl<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Select the Secret with an ACL that contains the user.
Project scope is ignored. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Secret algorithm.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bit<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The Secret bit length.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>created<wbr>At<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Date filter to select the Secret with
created matching the specified criteria. See Date Filters below for more
detail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Date filter to select the Secret with
expiration matching the specified criteria. See Date Filters below for more
detail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Secret mode.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Secret name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V1 KeyManager client.
A KeyManager client is needed to fetch a secret. If omitted, the `region`
argument of the provider is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Secret type. For more information see
[Secret types](https://docs.openstack.org/barbican/latest/api/reference/secret_types.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>updated<wbr>At<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Date filter to select the Secret with
updated matching the specified criteria. See Date Filters below for more
detail.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>acl_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Select the Secret with an ACL that contains the user.
Project scope is ignored. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Secret algorithm.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bit_<wbr>length</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The Secret bit length.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>created_<wbr>at_<wbr>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Date filter to select the Secret with
created matching the specified criteria. See Date Filters below for more
detail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration_<wbr>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Date filter to select the Secret with
expiration matching the specified criteria. See Date Filters below for more
detail.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Secret mode.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Secret name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V1 KeyManager client.
A KeyManager client is needed to fetch a secret. If omitted, the `region`
argument of the provider is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secret_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Secret type. For more information see
[Secret types](https://docs.openstack.org/barbican/latest/api/reference/secret_types.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>updated_<wbr>at_<wbr>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Date filter to select the Secret with
updated matching the specified criteria. See Date Filters below for more
detail.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetSecret Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Acl<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Acls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsecretacl">List&lt;Get<wbr>Secret<wbr>Acl&gt;</a></span>
    </dt>
    <dd>{{% md %}}The list of ACLs assigned to a secret. The `read` structure is described below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bit<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object></span>
    </dt>
    <dd>{{% md %}}The map of the content types, assigned on the secret.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date the secret ACL was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created<wbr>At<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Creator<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The creator of the secret.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date the secret will expire.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expiration<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
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
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object></span>
    </dt>
    <dd>{{% md %}}The map of metadata, assigned on the secret, which has been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Payload</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secret payload.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Payload<wbr>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secret encoding.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Payload<wbr>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secret content type.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secret reference / where to find the secret.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secret<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The status of the secret.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Updated<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date the secret ACL was last updated.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Updated<wbr>At<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Acl<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Acls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsecretacl">[]Get<wbr>Secret<wbr>Acl</a></span>
    </dt>
    <dd>{{% md %}}The list of ACLs assigned to a secret. The `read` structure is described below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bit<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Content<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}The map of the content types, assigned on the secret.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date the secret ACL was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created<wbr>At<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Creator<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The creator of the secret.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date the secret will expire.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expiration<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
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
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}The map of metadata, assigned on the secret, which has been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Payload</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secret payload.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Payload<wbr>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secret encoding.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Payload<wbr>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secret content type.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secret reference / where to find the secret.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secret<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The status of the secret.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Updated<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date the secret ACL was last updated.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Updated<wbr>At<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>acl<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>acls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsecretacl">Get<wbr>Secret<wbr>Acl[]</a></span>
    </dt>
    <dd>{{% md %}}The list of ACLs assigned to a secret. The `read` structure is described below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bit<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}The map of the content types, assigned on the secret.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date the secret ACL was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created<wbr>At<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>creator<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The creator of the secret.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date the secret will expire.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expiration<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
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
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}The map of metadata, assigned on the secret, which has been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>payload</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secret payload.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>payload<wbr>Content<wbr>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secret encoding.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>payload<wbr>Content<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secret content type.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secret<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secret reference / where to find the secret.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secret<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The status of the secret.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>updated<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date the secret ACL was last updated.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>updated<wbr>At<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>acl_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>acls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsecretacl">List[Get<wbr>Secret<wbr>Acl]</a></span>
    </dt>
    <dd>{{% md %}}The list of ACLs assigned to a secret. The `read` structure is described below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bit_<wbr>length</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>content_<wbr>types</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}The map of the content types, assigned on the secret.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created_<wbr>at</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The date the secret ACL was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created_<wbr>at_<wbr>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>creator_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The creator of the secret.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The date the secret will expire.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expiration_<wbr>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
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
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}The map of metadata, assigned on the secret, which has been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>payload</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The secret payload.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>payload_<wbr>content_<wbr>encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Secret encoding.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>payload_<wbr>content_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Secret content type.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secret_<wbr>ref</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The secret reference / where to find the secret.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secret_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The status of the secret.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>updated_<wbr>at</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The date the secret ACL was last updated.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>updated_<wbr>at_<wbr>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Secret<wbr>Acl</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/output/#GetSecretAcl">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/keymanager?tab=doc#GetSecretAcl">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Read</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsecretaclread">Get<wbr>Secret<wbr>Acl<wbr>Read<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Read</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsecretaclread">Get<wbr>Secret<wbr>Acl<wbr>Read</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>read</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsecretaclread">Get<wbr>Secret<wbr>Acl<wbr>Read</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>read</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsecretaclread">Dict[Get<wbr>Secret<wbr>Acl<wbr>Read]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Secret<wbr>Acl<wbr>Read</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/output/#GetSecretAclRead">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/keymanager?tab=doc#GetSecretAclRead">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Created<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date the secret ACL was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project<wbr>Access</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether the secret is accessible project wide.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Updated<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date the secret ACL was last updated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The list of user IDs, which are allowed to access the secret, when
`project_access` is set to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Created<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date the secret ACL was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project<wbr>Access</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether the secret is accessible project wide.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Updated<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date the secret ACL was last updated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of user IDs, which are allowed to access the secret, when
`project_access` is set to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>created<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date the secret ACL was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project<wbr>Access</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether the secret is accessible project wide.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>updated<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The date the secret ACL was last updated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>users</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The list of user IDs, which are allowed to access the secret, when
`project_access` is set to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>created_<wbr>at</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The date the secret ACL was created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project<wbr>Access</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the secret is accessible project wide.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>updated_<wbr>at</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The date the secret ACL was last updated.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>users</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of user IDs, which are allowed to access the secret, when
`project_access` is set to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







