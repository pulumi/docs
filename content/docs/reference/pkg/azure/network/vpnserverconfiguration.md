
---
title: "VpnServerConfiguration"
block_external_search_index: true
---

Manages a VPN Server Configuration.

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/vpn_server_configuration.html.markdown.



## Create a VpnServerConfiguration Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/network/#VpnServerConfiguration">VpnServerConfiguration</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/network/#VpnServerConfigurationArgs">VpnServerConfigurationArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">VpnServerConfiguration</span><span class="p">(resource_name, opts=None, </span>azure_active_directory_authentications=None<span class="p">, </span>client_revoked_certificates=None<span class="p">, </span>client_root_certificates=None<span class="p">, </span>ipsec_policy=None<span class="p">, </span>location=None<span class="p">, </span>name=None<span class="p">, </span>radius_server=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>tags=None<span class="p">, </span>vpn_authentication_types=None<span class="p">, </span>vpn_protocols=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewVpnServerConfiguration<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfigurationArgs">VpnServerConfigurationArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfiguration">VpnServerConfiguration</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Network.VpnServerConfiguration.html">VpnServerConfiguration</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Network.Inputs.VpnServerConfigurationArgs.html">VpnServerConfigurationArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Azure<wbr>Active<wbr>Directory<wbr>Authentications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationazureactivedirectoryauthentication">List&lt;Vpn<wbr>Server<wbr>Configuration<wbr>Azure<wbr>Active<wbr>Directory<wbr>Authentication<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A `azure_active_directory_authentication` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Revoked<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrevokedcertificate">List&lt;Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Revoked<wbr>Certificate<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_revoked_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrootcertificate">List&lt;Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Root<wbr>Certificate<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_root_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationipsecpolicy">Vpn<wbr>Server<wbr>Configuration<wbr>Ipsec<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Azure location where this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Radius<wbr>Server</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserver">Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `radius_server` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group in which this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vpn<wbr>Authentication<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A list of one of more Authentication Types applicable for this VPN Server Configuration. Possible values are `AAD` (Azure Active Directory), `Certificate` and `Radius`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpn<wbr>Protocols</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of VPN Protocols to use for this Server Configuration. Possible values are `IkeV2` and `OpenVPN`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Active<wbr>Directory<wbr>Authentications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationazureactivedirectoryauthentication">[]Vpn<wbr>Server<wbr>Configuration<wbr>Azure<wbr>Active<wbr>Directory<wbr>Authentication</a></span>
    </dt>
    <dd>{{% md %}}A `azure_active_directory_authentication` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Revoked<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrevokedcertificate">[]Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Revoked<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_revoked_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrootcertificate">[]Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Root<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_root_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationipsecpolicy">*Vpn<wbr>Server<wbr>Configuration<wbr>Ipsec<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Azure location where this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Radius<wbr>Server</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserver">*Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server</a></span>
    </dt>
    <dd>{{% md %}}A `radius_server` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group in which this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vpn<wbr>Authentication<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A list of one of more Authentication Types applicable for this VPN Server Configuration. Possible values are `AAD` (Azure Active Directory), `Certificate` and `Radius`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpn<wbr>Protocols</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of VPN Protocols to use for this Server Configuration. Possible values are `IkeV2` and `OpenVPN`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>azure<wbr>Active<wbr>Directory<wbr>Authentications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationazureactivedirectoryauthentication">Vpn<wbr>Server<wbr>Configuration<wbr>Azure<wbr>Active<wbr>Directory<wbr>Authentication[]?</a></span>
    </dt>
    <dd>{{% md %}}A `azure_active_directory_authentication` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Revoked<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrevokedcertificate">Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Revoked<wbr>Certificate[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_revoked_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrootcertificate">Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Root<wbr>Certificate[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_root_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationipsecpolicy">Vpn<wbr>Server<wbr>Configuration<wbr>Ipsec<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Azure location where this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>radius<wbr>Server</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserver">Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server?</a></span>
    </dt>
    <dd>{{% md %}}A `radius_server` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group in which this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vpn<wbr>Authentication<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A list of one of more Authentication Types applicable for this VPN Server Configuration. Possible values are `AAD` (Azure Active Directory), `Certificate` and `Radius`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpn<wbr>Protocols</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of VPN Protocols to use for this Server Configuration. Possible values are `IkeV2` and `OpenVPN`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>azure_<wbr>active_<wbr>directory_<wbr>authentications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationazureactivedirectoryauthentication">List[Vpn<wbr>Server<wbr>Configuration<wbr>Azure<wbr>Active<wbr>Directory<wbr>Authentication]</a></span>
    </dt>
    <dd>{{% md %}}A `azure_active_directory_authentication` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>revoked_<wbr>certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrevokedcertificate">List[Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Revoked<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_revoked_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>root_<wbr>certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrootcertificate">List[Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Root<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_root_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipsec_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationipsecpolicy">Dict[Vpn<wbr>Server<wbr>Configuration<wbr>Ipsec<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Azure location where this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>radius_<wbr>server</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserver">Dict[Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server]</a></span>
    </dt>
    <dd>{{% md %}}A `radius_server` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group in which this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vpn_<wbr>authentication_<wbr>types</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A list of one of more Authentication Types applicable for this VPN Server Configuration. Possible values are `AAD` (Azure Active Directory), `Certificate` and `Radius`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpn_<wbr>protocols</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of VPN Protocols to use for this Server Configuration. Possible values are `IkeV2` and `OpenVPN`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## VpnServerConfiguration Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Azure<wbr>Active<wbr>Directory<wbr>Authentications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationazureactivedirectoryauthentication">List&lt;Vpn<wbr>Server<wbr>Configuration<wbr>Azure<wbr>Active<wbr>Directory<wbr>Authentication&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A `azure_active_directory_authentication` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Client<wbr>Revoked<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrevokedcertificate">List&lt;Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Revoked<wbr>Certificate&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_revoked_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Client<wbr>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrootcertificate">List&lt;Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Root<wbr>Certificate&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_root_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationipsecpolicy">Vpn<wbr>Server<wbr>Configuration<wbr>Ipsec<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure location where this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Radius<wbr>Server</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserver">Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server?</a></span>
    </dt>
    <dd>{{% md %}}A `radius_server` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group in which this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpn<wbr>Authentication<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A list of one of more Authentication Types applicable for this VPN Server Configuration. Possible values are `AAD` (Azure Active Directory), `Certificate` and `Radius`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpn<wbr>Protocols</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of VPN Protocols to use for this Server Configuration. Possible values are `IkeV2` and `OpenVPN`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Azure<wbr>Active<wbr>Directory<wbr>Authentications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationazureactivedirectoryauthentication">[]Vpn<wbr>Server<wbr>Configuration<wbr>Azure<wbr>Active<wbr>Directory<wbr>Authentication</a></span>
    </dt>
    <dd>{{% md %}}A `azure_active_directory_authentication` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Client<wbr>Revoked<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrevokedcertificate">[]Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Revoked<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_revoked_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Client<wbr>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrootcertificate">[]Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Root<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_root_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationipsecpolicy">*Vpn<wbr>Server<wbr>Configuration<wbr>Ipsec<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure location where this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Radius<wbr>Server</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserver">*Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server</a></span>
    </dt>
    <dd>{{% md %}}A `radius_server` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group in which this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpn<wbr>Authentication<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A list of one of more Authentication Types applicable for this VPN Server Configuration. Possible values are `AAD` (Azure Active Directory), `Certificate` and `Radius`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpn<wbr>Protocols</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of VPN Protocols to use for this Server Configuration. Possible values are `IkeV2` and `OpenVPN`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>azure<wbr>Active<wbr>Directory<wbr>Authentications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationazureactivedirectoryauthentication">Vpn<wbr>Server<wbr>Configuration<wbr>Azure<wbr>Active<wbr>Directory<wbr>Authentication[]?</a></span>
    </dt>
    <dd>{{% md %}}A `azure_active_directory_authentication` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>client<wbr>Revoked<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrevokedcertificate">Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Revoked<wbr>Certificate[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_revoked_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>client<wbr>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrootcertificate">Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Root<wbr>Certificate[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_root_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationipsecpolicy">Vpn<wbr>Server<wbr>Configuration<wbr>Ipsec<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure location where this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>radius<wbr>Server</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserver">Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server?</a></span>
    </dt>
    <dd>{{% md %}}A `radius_server` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group in which this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpn<wbr>Authentication<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A list of one of more Authentication Types applicable for this VPN Server Configuration. Possible values are `AAD` (Azure Active Directory), `Certificate` and `Radius`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpn<wbr>Protocols</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of VPN Protocols to use for this Server Configuration. Possible values are `IkeV2` and `OpenVPN`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>azure_<wbr>active_<wbr>directory_<wbr>authentications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationazureactivedirectoryauthentication">List[Vpn<wbr>Server<wbr>Configuration<wbr>Azure<wbr>Active<wbr>Directory<wbr>Authentication]</a></span>
    </dt>
    <dd>{{% md %}}A `azure_active_directory_authentication` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>client_<wbr>revoked_<wbr>certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrevokedcertificate">List[Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Revoked<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_revoked_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>client_<wbr>root_<wbr>certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrootcertificate">List[Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Root<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_root_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ipsec_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationipsecpolicy">Dict[Vpn<wbr>Server<wbr>Configuration<wbr>Ipsec<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Azure location where this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>radius_<wbr>server</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserver">Dict[Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server]</a></span>
    </dt>
    <dd>{{% md %}}A `radius_server` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group in which this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpn_<wbr>authentication_<wbr>types</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A list of one of more Authentication Types applicable for this VPN Server Configuration. Possible values are `AAD` (Azure Active Directory), `Certificate` and `Radius`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpn_<wbr>protocols</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of VPN Protocols to use for this Server Configuration. Possible values are `IkeV2` and `OpenVPN`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing VpnServerConfiguration Resource

Get an existing VpnServerConfiguration resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/network/#VpnServerConfigurationState">VpnServerConfigurationState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/network/#VpnServerConfiguration">VpnServerConfiguration</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>azure_active_directory_authentications=None<span class="p">, </span>client_revoked_certificates=None<span class="p">, </span>client_root_certificates=None<span class="p">, </span>ipsec_policy=None<span class="p">, </span>location=None<span class="p">, </span>name=None<span class="p">, </span>radius_server=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>tags=None<span class="p">, </span>vpn_authentication_types=None<span class="p">, </span>vpn_protocols=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetVpnServerConfiguration<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfigurationState">VpnServerConfigurationState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfiguration">VpnServerConfiguration</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Network.VpnServerConfiguration.html">VpnServerConfiguration</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Network.VpnServerConfigurationState.html">VpnServerConfigurationState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Azure<wbr>Active<wbr>Directory<wbr>Authentications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationazureactivedirectoryauthentication">List&lt;Vpn<wbr>Server<wbr>Configuration<wbr>Azure<wbr>Active<wbr>Directory<wbr>Authentication<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A `azure_active_directory_authentication` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Revoked<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrevokedcertificate">List&lt;Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Revoked<wbr>Certificate<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_revoked_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrootcertificate">List&lt;Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Root<wbr>Certificate<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_root_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationipsecpolicy">Vpn<wbr>Server<wbr>Configuration<wbr>Ipsec<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Azure location where this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Radius<wbr>Server</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserver">Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `radius_server` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group in which this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpn<wbr>Authentication<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A list of one of more Authentication Types applicable for this VPN Server Configuration. Possible values are `AAD` (Azure Active Directory), `Certificate` and `Radius`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpn<wbr>Protocols</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of VPN Protocols to use for this Server Configuration. Possible values are `IkeV2` and `OpenVPN`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Active<wbr>Directory<wbr>Authentications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationazureactivedirectoryauthentication">[]Vpn<wbr>Server<wbr>Configuration<wbr>Azure<wbr>Active<wbr>Directory<wbr>Authentication</a></span>
    </dt>
    <dd>{{% md %}}A `azure_active_directory_authentication` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Revoked<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrevokedcertificate">[]Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Revoked<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_revoked_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrootcertificate">[]Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Root<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_root_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationipsecpolicy">*Vpn<wbr>Server<wbr>Configuration<wbr>Ipsec<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Azure location where this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Radius<wbr>Server</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserver">*Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server</a></span>
    </dt>
    <dd>{{% md %}}A `radius_server` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group in which this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpn<wbr>Authentication<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A list of one of more Authentication Types applicable for this VPN Server Configuration. Possible values are `AAD` (Azure Active Directory), `Certificate` and `Radius`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpn<wbr>Protocols</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of VPN Protocols to use for this Server Configuration. Possible values are `IkeV2` and `OpenVPN`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>azure<wbr>Active<wbr>Directory<wbr>Authentications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationazureactivedirectoryauthentication">Vpn<wbr>Server<wbr>Configuration<wbr>Azure<wbr>Active<wbr>Directory<wbr>Authentication[]?</a></span>
    </dt>
    <dd>{{% md %}}A `azure_active_directory_authentication` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Revoked<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrevokedcertificate">Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Revoked<wbr>Certificate[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_revoked_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrootcertificate">Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Root<wbr>Certificate[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_root_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationipsecpolicy">Vpn<wbr>Server<wbr>Configuration<wbr>Ipsec<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Azure location where this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>radius<wbr>Server</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserver">Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server?</a></span>
    </dt>
    <dd>{{% md %}}A `radius_server` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group in which this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpn<wbr>Authentication<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A list of one of more Authentication Types applicable for this VPN Server Configuration. Possible values are `AAD` (Azure Active Directory), `Certificate` and `Radius`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpn<wbr>Protocols</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of VPN Protocols to use for this Server Configuration. Possible values are `IkeV2` and `OpenVPN`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>azure_<wbr>active_<wbr>directory_<wbr>authentications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationazureactivedirectoryauthentication">List[Vpn<wbr>Server<wbr>Configuration<wbr>Azure<wbr>Active<wbr>Directory<wbr>Authentication]</a></span>
    </dt>
    <dd>{{% md %}}A `azure_active_directory_authentication` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>revoked_<wbr>certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrevokedcertificate">List[Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Revoked<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_revoked_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>root_<wbr>certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationclientrootcertificate">List[Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Root<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_root_certificate` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipsec_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationipsecpolicy">Dict[Vpn<wbr>Server<wbr>Configuration<wbr>Ipsec<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Azure location where this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>radius_<wbr>server</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserver">Dict[Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server]</a></span>
    </dt>
    <dd>{{% md %}}A `radius_server` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group in which this VPN Server Configuration should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpn_<wbr>authentication_<wbr>types</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A list of one of more Authentication Types applicable for this VPN Server Configuration. Possible values are `AAD` (Azure Active Directory), `Certificate` and `Radius`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpn_<wbr>protocols</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of VPN Protocols to use for this Server Configuration. Possible values are `IkeV2` and `OpenVPN`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Vpn<wbr>Server<wbr>Configuration<wbr>Azure<wbr>Active<wbr>Directory<wbr>Authentication</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#VpnServerConfigurationAzureActiveDirectoryAuthentication">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#VpnServerConfigurationAzureActiveDirectoryAuthentication">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfigurationAzureActiveDirectoryAuthenticationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfigurationAzureActiveDirectoryAuthenticationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Audience which should be used for authentication.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Issuer which should be used for authentication.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tenant</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Tenant which should be used for authentication.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Audience which should be used for authentication.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Issuer which should be used for authentication.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tenant</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Tenant which should be used for authentication.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Audience which should be used for authentication.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Issuer which should be used for authentication.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tenant</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Tenant which should be used for authentication.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Audience which should be used for authentication.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Issuer which should be used for authentication.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tenant</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Tenant which should be used for authentication.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Revoked<wbr>Certificate</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#VpnServerConfigurationClientRevokedCertificate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#VpnServerConfigurationClientRevokedCertificate">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfigurationClientRevokedCertificateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfigurationClientRevokedCertificateOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name used to uniquely identify this certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Thumbprint of the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name used to uniquely identify this certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Thumbprint of the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name used to uniquely identify this certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Thumbprint of the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A name used to uniquely identify this certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Thumbprint of the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Vpn<wbr>Server<wbr>Configuration<wbr>Client<wbr>Root<wbr>Certificate</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#VpnServerConfigurationClientRootCertificate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#VpnServerConfigurationClientRootCertificate">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfigurationClientRootCertificateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfigurationClientRootCertificateOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name used to uniquely identify this certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Cert<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Public Key Data associated with the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name used to uniquely identify this certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Cert<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Public Key Data associated with the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name used to uniquely identify this certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>public<wbr>Cert<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Public Key Data associated with the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A name used to uniquely identify this certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>public<wbr>Cert<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Public Key Data associated with the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Vpn<wbr>Server<wbr>Configuration<wbr>Ipsec<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#VpnServerConfigurationIpsecPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#VpnServerConfigurationIpsecPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfigurationIpsecPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfigurationIpsecPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dh<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DH Group, used in IKE Phase 1. Possible values include `DHGroup1`, `DHGroup2`, `DHGroup14`, `DHGroup24`, `DHGroup2048`, `ECP256`, `ECP384` and `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ike<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IKE encryption algorithm, used for IKE Phase 2. Possible values include `AES128`, `AES192`, `AES256`, `DES`, `DES3`, `GCMAES128` and `GCMAES256`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ike<wbr>Integrity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IKE encryption integrity algorithm, used for IKE Phase 2. Possible values include `GCMAES128`, `GCMAES256`, `MD5`, `SHA1`, `SHA256` and `SHA384`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ipsec<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPSec encryption algorithm, used for IKE phase 1. Possible values include `AES128`, `AES192`, `AES256`, `DES`, `DES3`, `GCMAES128`, `GCMAES192`, `GCMAES256` and `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ipsec<wbr>Integrity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPSec integrity algorithm, used for IKE phase 1. Possible values include `GCMAES128`, `GCMAES192`, `GCMAES256`, `MD5`, `SHA1` and `SHA256`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Pfs<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Pfs Group, used in IKE Phase 2. Possible values include `ECP256`, `ECP384`, `PFS1`, `PFS2`, `PFS14`, `PFS24`, `PFS2048`, `PFSMM` and `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sa<wbr>Data<wbr>Size<wbr>Kilobytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The IPSec Security Association payload size in KB for a Site-to-Site VPN tunnel.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sa<wbr>Lifetime<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The IPSec Security Association lifetime in seconds for a Site-to-Site VPN tunnel.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dh<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DH Group, used in IKE Phase 1. Possible values include `DHGroup1`, `DHGroup2`, `DHGroup14`, `DHGroup24`, `DHGroup2048`, `ECP256`, `ECP384` and `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ike<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IKE encryption algorithm, used for IKE Phase 2. Possible values include `AES128`, `AES192`, `AES256`, `DES`, `DES3`, `GCMAES128` and `GCMAES256`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ike<wbr>Integrity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IKE encryption integrity algorithm, used for IKE Phase 2. Possible values include `GCMAES128`, `GCMAES256`, `MD5`, `SHA1`, `SHA256` and `SHA384`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ipsec<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPSec encryption algorithm, used for IKE phase 1. Possible values include `AES128`, `AES192`, `AES256`, `DES`, `DES3`, `GCMAES128`, `GCMAES192`, `GCMAES256` and `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ipsec<wbr>Integrity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPSec integrity algorithm, used for IKE phase 1. Possible values include `GCMAES128`, `GCMAES192`, `GCMAES256`, `MD5`, `SHA1` and `SHA256`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Pfs<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Pfs Group, used in IKE Phase 2. Possible values include `ECP256`, `ECP384`, `PFS1`, `PFS2`, `PFS14`, `PFS24`, `PFS2048`, `PFSMM` and `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sa<wbr>Data<wbr>Size<wbr>Kilobytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The IPSec Security Association payload size in KB for a Site-to-Site VPN tunnel.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sa<wbr>Lifetime<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The IPSec Security Association lifetime in seconds for a Site-to-Site VPN tunnel.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dh<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DH Group, used in IKE Phase 1. Possible values include `DHGroup1`, `DHGroup2`, `DHGroup14`, `DHGroup24`, `DHGroup2048`, `ECP256`, `ECP384` and `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ike<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IKE encryption algorithm, used for IKE Phase 2. Possible values include `AES128`, `AES192`, `AES256`, `DES`, `DES3`, `GCMAES128` and `GCMAES256`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ike<wbr>Integrity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IKE encryption integrity algorithm, used for IKE Phase 2. Possible values include `GCMAES128`, `GCMAES256`, `MD5`, `SHA1`, `SHA256` and `SHA384`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ipsec<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPSec encryption algorithm, used for IKE phase 1. Possible values include `AES128`, `AES192`, `AES256`, `DES`, `DES3`, `GCMAES128`, `GCMAES192`, `GCMAES256` and `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ipsec<wbr>Integrity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPSec integrity algorithm, used for IKE phase 1. Possible values include `GCMAES128`, `GCMAES192`, `GCMAES256`, `MD5`, `SHA1` and `SHA256`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>pfs<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Pfs Group, used in IKE Phase 2. Possible values include `ECP256`, `ECP384`, `PFS1`, `PFS2`, `PFS14`, `PFS24`, `PFS2048`, `PFSMM` and `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sa<wbr>Data<wbr>Size<wbr>Kilobytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The IPSec Security Association payload size in KB for a Site-to-Site VPN tunnel.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sa<wbr>Lifetime<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The IPSec Security Association lifetime in seconds for a Site-to-Site VPN tunnel.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dh<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The DH Group, used in IKE Phase 1. Possible values include `DHGroup1`, `DHGroup2`, `DHGroup14`, `DHGroup24`, `DHGroup2048`, `ECP256`, `ECP384` and `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ike<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IKE encryption algorithm, used for IKE Phase 2. Possible values include `AES128`, `AES192`, `AES256`, `DES`, `DES3`, `GCMAES128` and `GCMAES256`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ike<wbr>Integrity</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IKE encryption integrity algorithm, used for IKE Phase 2. Possible values include `GCMAES128`, `GCMAES256`, `MD5`, `SHA1`, `SHA256` and `SHA384`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ipsec<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IPSec encryption algorithm, used for IKE phase 1. Possible values include `AES128`, `AES192`, `AES256`, `DES`, `DES3`, `GCMAES128`, `GCMAES192`, `GCMAES256` and `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ipsec<wbr>Integrity</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IPSec integrity algorithm, used for IKE phase 1. Possible values include `GCMAES128`, `GCMAES192`, `GCMAES256`, `MD5`, `SHA1` and `SHA256`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>pfs<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Pfs Group, used in IKE Phase 2. Possible values include `ECP256`, `ECP384`, `PFS1`, `PFS2`, `PFS14`, `PFS24`, `PFS2048`, `PFSMM` and `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sa<wbr>Data<wbr>Size<wbr>Kilobytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The IPSec Security Association payload size in KB for a Site-to-Site VPN tunnel.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sa<wbr>Lifetime<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The IPSec Security Association lifetime in seconds for a Site-to-Site VPN tunnel.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#VpnServerConfigurationRadiusServer">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#VpnServerConfigurationRadiusServer">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfigurationRadiusServerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfigurationRadiusServerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Address of the Radius Server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserverclientrootcertificate">List&lt;Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server<wbr>Client<wbr>Root<wbr>Certificate<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_root_certificate` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secret used to communicate with the Radius Server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserverserverrootcertificate">List&lt;Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server<wbr>Server<wbr>Root<wbr>Certificate<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `server_root_certificate` blocks as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Address of the Radius Server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserverclientrootcertificate">[]Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server<wbr>Client<wbr>Root<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_root_certificate` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secret used to communicate with the Radius Server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserverserverrootcertificate">[]Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server<wbr>Server<wbr>Root<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}One or more `server_root_certificate` blocks as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Address of the Radius Server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserverclientrootcertificate">Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server<wbr>Client<wbr>Root<wbr>Certificate[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_root_certificate` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secret used to communicate with the Radius Server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server<wbr>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserverserverrootcertificate">Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server<wbr>Server<wbr>Root<wbr>Certificate[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `server_root_certificate` blocks as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Address of the Radius Server.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>root_<wbr>certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserverclientrootcertificate">List[Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server<wbr>Client<wbr>Root<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}One or more `client_root_certificate` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Secret used to communicate with the Radius Server.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server<wbr>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#vpnserverconfigurationradiusserverserverrootcertificate">List[Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server<wbr>Server<wbr>Root<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}One or more `server_root_certificate` blocks as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server<wbr>Client<wbr>Root<wbr>Certificate</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#VpnServerConfigurationRadiusServerClientRootCertificate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#VpnServerConfigurationRadiusServerClientRootCertificate">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfigurationRadiusServerClientRootCertificateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfigurationRadiusServerClientRootCertificateOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name used to uniquely identify this certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Thumbprint of the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name used to uniquely identify this certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Thumbprint of the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name used to uniquely identify this certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Thumbprint of the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A name used to uniquely identify this certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Thumbprint of the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Vpn<wbr>Server<wbr>Configuration<wbr>Radius<wbr>Server<wbr>Server<wbr>Root<wbr>Certificate</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#VpnServerConfigurationRadiusServerServerRootCertificate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#VpnServerConfigurationRadiusServerServerRootCertificate">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfigurationRadiusServerServerRootCertificateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VpnServerConfigurationRadiusServerServerRootCertificateOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name used to uniquely identify this certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Cert<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Public Key Data associated with the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name used to uniquely identify this certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Cert<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Public Key Data associated with the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A name used to uniquely identify this certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>public<wbr>Cert<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Public Key Data associated with the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A name used to uniquely identify this certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>public<wbr>Cert<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Public Key Data associated with the Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







