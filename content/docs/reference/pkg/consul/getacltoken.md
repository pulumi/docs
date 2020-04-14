
---
title: "GetAclToken"
block_external_search_index: true
---



The `consul..AclToken` data source returns the information related to the
`consul..AclToken` resource with the exception of its secret ID.

If you want to get the secret ID associated with a token, use the
[`consul..getAclTokenSecretId` data source](https://www.terraform.io/docs/providers/consul/d/acl_token_secret_id.html).

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as consul from "@pulumi/consul";

const test = pulumi.output(consul.getAclToken({
    accessorId: "00000000-0000-0000-0000-000000000002",
}, { async: true }));

export const consulAclPolicies = test.policies!;
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-consul/blob/master/website/docs/d/acl_token.html.markdown.





## Using GetAclToken

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getAclToken<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/consul/#GetAclTokenArgs">GetAclTokenArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/consul/#GetAclTokenResult">GetAclTokenResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_acl_token(</span>accessor_id=None<span class="p">, </span>description=None<span class="p">, </span>local=None<span class="p">, </span>namespace=None<span class="p">, </span>policies=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupAclToken<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-consul/sdk/go/consul/?tab=doc#GetAclTokenArgs">GetAclTokenArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-consul/sdk/go/consul/?tab=doc#LookupAclTokenResult">LookupAclTokenResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetAclToken </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Consul/Pulumi.Consul.GetAclTokenResult.html">GetAclTokenResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Consul/Pulumi.Consul.GetAclTokenArgs.html">GetAclTokenArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Accessor<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The accessor ID of the ACL token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description of the ACL token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the ACL token is local to the datacenter it was created within.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The namespace to lookup the ACL token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getacltokenpolicy">List&lt;Get<wbr>Acl<wbr>Token<wbr>Policy<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of policies associated with the ACL token. Each entry has
an `id` and a `name` attribute.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Accessor<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The accessor ID of the ACL token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description of the ACL token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the ACL token is local to the datacenter it was created within.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The namespace to lookup the ACL token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getacltokenpolicy">[]Get<wbr>Acl<wbr>Token<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A list of policies associated with the ACL token. Each entry has
an `id` and a `name` attribute.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>accessor<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The accessor ID of the ACL token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description of the ACL token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the ACL token is local to the datacenter it was created within.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The namespace to lookup the ACL token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getacltokenpolicy">Get<wbr>Acl<wbr>Token<wbr>Policy[]</a></span>
    </dt>
    <dd>{{% md %}}A list of policies associated with the ACL token. Each entry has
an `id` and a `name` attribute.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>accessor_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The accessor ID of the ACL token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description of the ACL token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the ACL token is local to the datacenter it was created within.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The namespace to lookup the ACL token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getacltokenpolicy">List[Get<wbr>Acl<wbr>Token<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A list of policies associated with the ACL token. Each entry has
an `id` and a `name` attribute.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetAclToken Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Accessor<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description of the ACL token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Local</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the ACL token is local to the datacenter it was created within.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getacltokenpolicy">List&lt;Get<wbr>Acl<wbr>Token<wbr>Policy&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of policies associated with the ACL token. Each entry has
an `id` and a `name` attribute.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Accessor<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description of the ACL token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Local</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the ACL token is local to the datacenter it was created within.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getacltokenpolicy">[]Get<wbr>Acl<wbr>Token<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A list of policies associated with the ACL token. Each entry has
an `id` and a `name` attribute.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>accessor<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description of the ACL token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>local</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the ACL token is local to the datacenter it was created within.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getacltokenpolicy">Get<wbr>Acl<wbr>Token<wbr>Policy[]</a></span>
    </dt>
    <dd>{{% md %}}A list of policies associated with the ACL token. Each entry has
an `id` and a `name` attribute.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>accessor_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description of the ACL token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>local</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the ACL token is local to the datacenter it was created within.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getacltokenpolicy">List[Get<wbr>Acl<wbr>Token<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A list of policies associated with the ACL token. Each entry has
an `id` and a `name` attribute.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Acl<wbr>Token<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/consul/types/input/#GetAclTokenPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/consul/types/output/#GetAclTokenPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-consul/sdk/go/consul/?tab=doc#GetAclTokenPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-consul/sdk/go/consul/?tab=doc#GetAclTokenPolicy">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}







