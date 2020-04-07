
---
title: "IkePolicy"
block_external_search_index: true
---



Manages a V2 Neutron IKE policy resource within OpenStack.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as openstack from "@pulumi/openstack";

const policy1 = new openstack.vpnaas.IkePolicy("policy_1", {});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/vpnaas_ike_policy_v2.html.markdown.



## Create a IkePolicy Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/vpnaas/#IkePolicy">IkePolicy</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/vpnaas/#IkePolicyArgs">IkePolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">IkePolicy</span><span class="p">(resource_name, opts=None, </span>auth_algorithm=None<span class="p">, </span>description=None<span class="p">, </span>encryption_algorithm=None<span class="p">, </span>ike_version=None<span class="p">, </span>lifetimes=None<span class="p">, </span>name=None<span class="p">, </span>pfs=None<span class="p">, </span>phase1_negotiation_mode=None<span class="p">, </span>region=None<span class="p">, </span>tenant_id=None<span class="p">, </span>value_specs=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewIkePolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/vpnaas?tab=doc#IkePolicyArgs">IkePolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/vpnaas?tab=doc#IkePolicy">IkePolicy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Vpnaas.IkePolicy.html">IkePolicy</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.VPNaaS.IkePolicyArgs.html">IkePolicyArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the policy.
Changing this updates the description of the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encryption<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ike<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lifetimes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ikepolicylifetime">List&lt;Ike<wbr>Policy<wbr>Lifetime<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this updates the name of
the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pfs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Phase1Negotiation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the policy.
Changing this updates the description of the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encryption<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ike<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lifetimes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ikepolicylifetime">[]Ike<wbr>Policy<wbr>Lifetime</a></span>
    </dt>
    <dd>{{% md %}}The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this updates the name of
the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pfs</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Phase1Negotiation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auth<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the policy.
Changing this updates the description of the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encryption<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ike<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lifetimes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ikepolicylifetime">Ike<wbr>Policy<wbr>Lifetime[]?</a></span>
    </dt>
    <dd>{{% md %}}The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this updates the name of
the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pfs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>phase1Negotiation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auth_<wbr>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the policy.
Changing this updates the description of the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encryption_<wbr>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ike_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lifetimes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ikepolicylifetime">List[Ike<wbr>Policy<wbr>Lifetime]</a></span>
    </dt>
    <dd>{{% md %}}The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this updates the name of
the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pfs</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>phase1_<wbr>negotiation_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value_<wbr>specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## IkePolicy Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Auth<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the policy.
Changing this updates the description of the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Encryption<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ike<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lifetimes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ikepolicylifetime">List&lt;Ike<wbr>Policy<wbr>Lifetime&gt;</a></span>
    </dt>
    <dd>{{% md %}}The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this updates the name of
the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pfs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Phase1Negotiation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Auth<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the policy.
Changing this updates the description of the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Encryption<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ike<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lifetimes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ikepolicylifetime">[]Ike<wbr>Policy<wbr>Lifetime</a></span>
    </dt>
    <dd>{{% md %}}The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this updates the name of
the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pfs</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Phase1Negotiation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>auth<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the policy.
Changing this updates the description of the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>encryption<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ike<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lifetimes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ikepolicylifetime">Ike<wbr>Policy<wbr>Lifetime[]</a></span>
    </dt>
    <dd>{{% md %}}The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this updates the name of
the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pfs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>phase1Negotiation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>auth_<wbr>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the policy.
Changing this updates the description of the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>encryption_<wbr>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ike_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lifetimes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ikepolicylifetime">List[Ike<wbr>Policy<wbr>Lifetime]</a></span>
    </dt>
    <dd>{{% md %}}The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this updates the name of
the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pfs</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>phase1_<wbr>negotiation_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>value_<wbr>specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing IkePolicy Resource

Get an existing IkePolicy resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/vpnaas/#IkePolicyState">IkePolicyState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/vpnaas/#IkePolicy">IkePolicy</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>auth_algorithm=None<span class="p">, </span>description=None<span class="p">, </span>encryption_algorithm=None<span class="p">, </span>ike_version=None<span class="p">, </span>lifetimes=None<span class="p">, </span>name=None<span class="p">, </span>pfs=None<span class="p">, </span>phase1_negotiation_mode=None<span class="p">, </span>region=None<span class="p">, </span>tenant_id=None<span class="p">, </span>value_specs=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetIkePolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/vpnaas?tab=doc#IkePolicyState">IkePolicyState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/vpnaas?tab=doc#IkePolicy">IkePolicy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Vpnaas.IkePolicy.html">IkePolicy</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Vpnaas.IkePolicyState.html">IkePolicyState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Auth<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the policy.
Changing this updates the description of the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encryption<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ike<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lifetimes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ikepolicylifetime">List&lt;Ike<wbr>Policy<wbr>Lifetime<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this updates the name of
the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pfs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Phase1Negotiation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the policy.
Changing this updates the description of the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encryption<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ike<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lifetimes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ikepolicylifetime">[]Ike<wbr>Policy<wbr>Lifetime</a></span>
    </dt>
    <dd>{{% md %}}The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this updates the name of
the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pfs</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Phase1Negotiation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auth<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the policy.
Changing this updates the description of the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encryption<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ike<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lifetimes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ikepolicylifetime">Ike<wbr>Policy<wbr>Lifetime[]?</a></span>
    </dt>
    <dd>{{% md %}}The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this updates the name of
the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pfs</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>phase1Negotiation<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auth_<wbr>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
Default is sha1. Changing this updates the algorithm of the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The human-readable description for the policy.
Changing this updates the description of the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encryption_<wbr>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
The default value is aes-128. Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ike_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is v1 or v2. Default is v1.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lifetimes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ikepolicylifetime">List[Ike<wbr>Policy<wbr>Lifetime]</a></span>
    </dt>
    <dd>{{% md %}}The lifetime of the security association. Consists of Unit and Value.
- `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
Default is seconds.
- `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
Default is 3600.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the policy. Changing this updates the name of
the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pfs</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>phase1_<wbr>negotiation_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IKE mode. A valid value is main, which is the default.
Changing this updates the existing policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VPN service. If omitted, the
`region` argument of the provider is used. Changing this creates a new
service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The owner of the policy. Required if admin wants to
create a service for another policy. Changing this creates a new policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value_<wbr>specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Ike<wbr>Policy<wbr>Lifetime</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/input/#IkePolicyLifetime">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/output/#IkePolicyLifetime">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/vpnaas?tab=doc#IkePolicyLifetimeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/vpnaas?tab=doc#IkePolicyLifetimeOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Units</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Units</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>units</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>units</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-openstack">https://github.com/pulumi/pulumi-openstack</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

