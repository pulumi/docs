
---
title: "KubernetesCluster"
block_external_search_index: true
---

Manages a Managed Kubernetes Cluster (also known as AKS / Azure Kubernetes Service)

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kubernetes_cluster.html.markdown.



## Create a KubernetesCluster Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/containerservice/#KubernetesCluster">KubernetesCluster</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/containerservice/#KubernetesClusterArgs">KubernetesClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">KubernetesCluster</span><span class="p">(resource_name, opts=None, </span>addon_profile=None<span class="p">, </span>api_server_authorized_ip_ranges=None<span class="p">, </span>default_node_pool=None<span class="p">, </span>dns_prefix=None<span class="p">, </span>enable_pod_security_policy=None<span class="p">, </span>identity=None<span class="p">, </span>kubernetes_version=None<span class="p">, </span>linux_profile=None<span class="p">, </span>location=None<span class="p">, </span>name=None<span class="p">, </span>network_profile=None<span class="p">, </span>node_resource_group=None<span class="p">, </span>private_link_enabled=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>role_based_access_control=None<span class="p">, </span>service_principal=None<span class="p">, </span>tags=None<span class="p">, </span>windows_profile=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewKubernetesCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterArgs">KubernetesClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesCluster">KubernetesCluster</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Containerservice.KubernetesCluster.html">KubernetesCluster</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.ContainerService.KubernetesClusterArgs.html">KubernetesClusterArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Addon<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofile">Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `addon_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Server<wbr>Authorized<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The IP ranges to whitelist for incoming traffic to the masters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterdefaultnodepool">Kubernetes<wbr>Cluster<wbr>Default<wbr>Node<wbr>Pool<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `default_node_pool` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Dns<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Pod<wbr>Security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether Pod Security Policies are enabled. Note that this also requires role based access control to be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteridentity">Kubernetes<wbr>Cluster<wbr>Identity<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kubernetes<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Linux<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterlinuxprofile">Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `linux_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusternetworkprofile">Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `network_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group where the Kubernetes Nodes should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Link<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Based<wbr>Access<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterrolebasedaccesscontrol">Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `role_based_access_control` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service<wbr>Principal</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterserviceprincipal">Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `service_principal` block as documented below.
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
        <span>Windows<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterwindowsprofile">Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `windows_profile` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Addon<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofile">*Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `addon_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Server<wbr>Authorized<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The IP ranges to whitelist for incoming traffic to the masters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterdefaultnodepool">Kubernetes<wbr>Cluster<wbr>Default<wbr>Node<wbr>Pool</a></span>
    </dt>
    <dd>{{% md %}}A `default_node_pool` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Dns<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Pod<wbr>Security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether Pod Security Policies are enabled. Note that this also requires role based access control to be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteridentity">*Kubernetes<wbr>Cluster<wbr>Identity</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kubernetes<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Linux<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterlinuxprofile">*Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `linux_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusternetworkprofile">*Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `network_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group where the Kubernetes Nodes should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Link<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Based<wbr>Access<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterrolebasedaccesscontrol">*Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control</a></span>
    </dt>
    <dd>{{% md %}}A `role_based_access_control` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service<wbr>Principal</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterserviceprincipal">Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal</a></span>
    </dt>
    <dd>{{% md %}}A `service_principal` block as documented below.
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
        <span>Windows<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterwindowsprofile">*Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `windows_profile` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>addon<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofile">Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile?</a></span>
    </dt>
    <dd>{{% md %}}A `addon_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>api<wbr>Server<wbr>Authorized<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The IP ranges to whitelist for incoming traffic to the masters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterdefaultnodepool">Kubernetes<wbr>Cluster<wbr>Default<wbr>Node<wbr>Pool</a></span>
    </dt>
    <dd>{{% md %}}A `default_node_pool` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>dns<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Pod<wbr>Security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether Pod Security Policies are enabled. Note that this also requires role based access control to be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteridentity">Kubernetes<wbr>Cluster<wbr>Identity?</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kubernetes<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>linux<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterlinuxprofile">Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile?</a></span>
    </dt>
    <dd>{{% md %}}A `linux_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusternetworkprofile">Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile?</a></span>
    </dt>
    <dd>{{% md %}}A `network_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group where the Kubernetes Nodes should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Link<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role<wbr>Based<wbr>Access<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterrolebasedaccesscontrol">Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control?</a></span>
    </dt>
    <dd>{{% md %}}A `role_based_access_control` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service<wbr>Principal</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterserviceprincipal">Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal</a></span>
    </dt>
    <dd>{{% md %}}A `service_principal` block as documented below.
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
        <span>windows<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterwindowsprofile">Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile?</a></span>
    </dt>
    <dd>{{% md %}}A `windows_profile` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>addon_<wbr>profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofile">Dict[Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}A `addon_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>api_<wbr>server_<wbr>authorized_<wbr>ip_<wbr>ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The IP ranges to whitelist for incoming traffic to the masters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>default_<wbr>node_<wbr>pool</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterdefaultnodepool">Dict[Kubernetes<wbr>Cluster<wbr>Default<wbr>Node<wbr>Pool]</a></span>
    </dt>
    <dd>{{% md %}}A `default_node_pool` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>dns_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>pod_<wbr>security_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether Pod Security Policies are enabled. Note that this also requires role based access control to be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteridentity">Dict[Kubernetes<wbr>Cluster<wbr>Identity]</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kubernetes_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>linux_<wbr>profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterlinuxprofile">Dict[Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}A `linux_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusternetworkprofile">Dict[Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}A `network_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>resource_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group where the Kubernetes Nodes should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private_<wbr>link_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role_<wbr>based_<wbr>access_<wbr>control</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterrolebasedaccesscontrol">Dict[Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control]</a></span>
    </dt>
    <dd>{{% md %}}A `role_based_access_control` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service_<wbr>principal</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterserviceprincipal">Dict[Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal]</a></span>
    </dt>
    <dd>{{% md %}}A `service_principal` block as documented below.
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
        <span>windows_<wbr>profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterwindowsprofile">Dict[Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}A `windows_profile` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## KubernetesCluster Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Addon<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofile">Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `addon_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Api<wbr>Server<wbr>Authorized<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The IP ranges to whitelist for incoming traffic to the masters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterdefaultnodepool">Kubernetes<wbr>Cluster<wbr>Default<wbr>Node<wbr>Pool</a></span>
    </dt>
    <dd>{{% md %}}A `default_node_pool` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dns<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Pod<wbr>Security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether Pod Security Policies are enabled. Note that this also requires role based access control to be enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The FQDN of the Azure Kubernetes Managed Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteridentity">Kubernetes<wbr>Cluster<wbr>Identity?</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kube<wbr>Admin<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config for the admin account to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kube<wbr>Admin<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterkubeadminconfig">List&lt;Kubernetes<wbr>Cluster<wbr>Kube<wbr>Admin<wbr>Config&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `kube_admin_config` block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kube<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kube<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterkubeconfig">List&lt;Kubernetes<wbr>Cluster<wbr>Kube<wbr>Config&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `kube_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kubernetes<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Linux<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterlinuxprofile">Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile?</a></span>
    </dt>
    <dd>{{% md %}}A `linux_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusternetworkprofile">Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `network_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group where the Kubernetes Nodes should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The FQDN for the Kubernetes Cluster when private link has been enabled, which is only resolvable inside the Virtual Network used by the Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Link<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role<wbr>Based<wbr>Access<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterrolebasedaccesscontrol">Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control</a></span>
    </dt>
    <dd>{{% md %}}A `role_based_access_control` block.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Principal</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterserviceprincipal">Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal</a></span>
    </dt>
    <dd>{{% md %}}A `service_principal` block as documented below.
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
        <span>Windows<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterwindowsprofile">Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile?</a></span>
    </dt>
    <dd>{{% md %}}A `windows_profile` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Addon<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofile">Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `addon_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Api<wbr>Server<wbr>Authorized<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The IP ranges to whitelist for incoming traffic to the masters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterdefaultnodepool">Kubernetes<wbr>Cluster<wbr>Default<wbr>Node<wbr>Pool</a></span>
    </dt>
    <dd>{{% md %}}A `default_node_pool` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dns<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Pod<wbr>Security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether Pod Security Policies are enabled. Note that this also requires role based access control to be enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The FQDN of the Azure Kubernetes Managed Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteridentity">*Kubernetes<wbr>Cluster<wbr>Identity</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kube<wbr>Admin<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config for the admin account to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kube<wbr>Admin<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterkubeadminconfig">[]Kubernetes<wbr>Cluster<wbr>Kube<wbr>Admin<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A `kube_admin_config` block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kube<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kube<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterkubeconfig">[]Kubernetes<wbr>Cluster<wbr>Kube<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A `kube_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kubernetes<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Linux<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterlinuxprofile">*Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `linux_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusternetworkprofile">Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `network_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group where the Kubernetes Nodes should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The FQDN for the Kubernetes Cluster when private link has been enabled, which is only resolvable inside the Virtual Network used by the Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Link<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role<wbr>Based<wbr>Access<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterrolebasedaccesscontrol">Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control</a></span>
    </dt>
    <dd>{{% md %}}A `role_based_access_control` block.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Principal</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterserviceprincipal">Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal</a></span>
    </dt>
    <dd>{{% md %}}A `service_principal` block as documented below.
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
        <span>Windows<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterwindowsprofile">*Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `windows_profile` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>addon<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofile">Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `addon_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>api<wbr>Server<wbr>Authorized<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The IP ranges to whitelist for incoming traffic to the masters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterdefaultnodepool">Kubernetes<wbr>Cluster<wbr>Default<wbr>Node<wbr>Pool</a></span>
    </dt>
    <dd>{{% md %}}A `default_node_pool` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dns<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Pod<wbr>Security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether Pod Security Policies are enabled. Note that this also requires role based access control to be enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The FQDN of the Azure Kubernetes Managed Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteridentity">Kubernetes<wbr>Cluster<wbr>Identity?</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kube<wbr>Admin<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config for the admin account to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kube<wbr>Admin<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterkubeadminconfig">Kubernetes<wbr>Cluster<wbr>Kube<wbr>Admin<wbr>Config[]</a></span>
    </dt>
    <dd>{{% md %}}A `kube_admin_config` block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kube<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kube<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterkubeconfig">Kubernetes<wbr>Cluster<wbr>Kube<wbr>Config[]</a></span>
    </dt>
    <dd>{{% md %}}A `kube_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kubernetes<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>linux<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterlinuxprofile">Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile?</a></span>
    </dt>
    <dd>{{% md %}}A `linux_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusternetworkprofile">Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `network_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node<wbr>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group where the Kubernetes Nodes should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private<wbr>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The FQDN for the Kubernetes Cluster when private link has been enabled, which is only resolvable inside the Virtual Network used by the Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private<wbr>Link<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role<wbr>Based<wbr>Access<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterrolebasedaccesscontrol">Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control</a></span>
    </dt>
    <dd>{{% md %}}A `role_based_access_control` block.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service<wbr>Principal</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterserviceprincipal">Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal</a></span>
    </dt>
    <dd>{{% md %}}A `service_principal` block as documented below.
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
        <span>windows<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterwindowsprofile">Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile?</a></span>
    </dt>
    <dd>{{% md %}}A `windows_profile` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>addon_<wbr>profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofile">Dict[Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}A `addon_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>api_<wbr>server_<wbr>authorized_<wbr>ip_<wbr>ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The IP ranges to whitelist for incoming traffic to the masters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default_<wbr>node_<wbr>pool</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterdefaultnodepool">Dict[Kubernetes<wbr>Cluster<wbr>Default<wbr>Node<wbr>Pool]</a></span>
    </dt>
    <dd>{{% md %}}A `default_node_pool` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dns_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>pod_<wbr>security_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether Pod Security Policies are enabled. Note that this also requires role based access control to be enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The FQDN of the Azure Kubernetes Managed Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteridentity">Dict[Kubernetes<wbr>Cluster<wbr>Identity]</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kube_<wbr>admin_<wbr>config_<wbr>raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config for the admin account to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kube_<wbr>admin_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterkubeadminconfig">List[Kubernetes<wbr>Cluster<wbr>Kube<wbr>Admin<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A `kube_admin_config` block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kube_<wbr>config_<wbr>raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kube_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterkubeconfig">List[Kubernetes<wbr>Cluster<wbr>Kube<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A `kube_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kubernetes_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>linux_<wbr>profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterlinuxprofile">Dict[Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}A `linux_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusternetworkprofile">Dict[Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}A `network_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node_<wbr>resource_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group where the Kubernetes Nodes should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private_<wbr>fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The FQDN for the Kubernetes Cluster when private link has been enabled, which is only resolvable inside the Virtual Network used by the Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private_<wbr>link_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role_<wbr>based_<wbr>access_<wbr>control</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterrolebasedaccesscontrol">Dict[Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control]</a></span>
    </dt>
    <dd>{{% md %}}A `role_based_access_control` block.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service_<wbr>principal</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterserviceprincipal">Dict[Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal]</a></span>
    </dt>
    <dd>{{% md %}}A `service_principal` block as documented below.
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
        <span>windows_<wbr>profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterwindowsprofile">Dict[Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}A `windows_profile` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing KubernetesCluster Resource

Get an existing KubernetesCluster resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/containerservice/#KubernetesClusterState">KubernetesClusterState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/containerservice/#KubernetesCluster">KubernetesCluster</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>addon_profile=None<span class="p">, </span>api_server_authorized_ip_ranges=None<span class="p">, </span>default_node_pool=None<span class="p">, </span>dns_prefix=None<span class="p">, </span>enable_pod_security_policy=None<span class="p">, </span>fqdn=None<span class="p">, </span>identity=None<span class="p">, </span>kube_admin_config_raw=None<span class="p">, </span>kube_admin_configs=None<span class="p">, </span>kube_config_raw=None<span class="p">, </span>kube_configs=None<span class="p">, </span>kubernetes_version=None<span class="p">, </span>linux_profile=None<span class="p">, </span>location=None<span class="p">, </span>name=None<span class="p">, </span>network_profile=None<span class="p">, </span>node_resource_group=None<span class="p">, </span>private_fqdn=None<span class="p">, </span>private_link_enabled=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>role_based_access_control=None<span class="p">, </span>service_principal=None<span class="p">, </span>tags=None<span class="p">, </span>windows_profile=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetKubernetesCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterState">KubernetesClusterState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesCluster">KubernetesCluster</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Containerservice.KubernetesCluster.html">KubernetesCluster</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Containerservice.KubernetesClusterState.html">KubernetesClusterState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Addon<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofile">Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `addon_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Server<wbr>Authorized<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The IP ranges to whitelist for incoming traffic to the masters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterdefaultnodepool">Kubernetes<wbr>Cluster<wbr>Default<wbr>Node<wbr>Pool<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `default_node_pool` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Pod<wbr>Security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether Pod Security Policies are enabled. Note that this also requires role based access control to be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The FQDN of the Azure Kubernetes Managed Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteridentity">Kubernetes<wbr>Cluster<wbr>Identity<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kube<wbr>Admin<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config for the admin account to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kube<wbr>Admin<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterkubeadminconfig">List&lt;Kubernetes<wbr>Cluster<wbr>Kube<wbr>Admin<wbr>Config<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A `kube_admin_config` block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kube<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kube<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterkubeconfig">List&lt;Kubernetes<wbr>Cluster<wbr>Kube<wbr>Config<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A `kube_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kubernetes<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Linux<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterlinuxprofile">Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `linux_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusternetworkprofile">Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `network_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group where the Kubernetes Nodes should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The FQDN for the Kubernetes Cluster when private link has been enabled, which is only resolvable inside the Virtual Network used by the Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Link<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Based<wbr>Access<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterrolebasedaccesscontrol">Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `role_based_access_control` block.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Principal</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterserviceprincipal">Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `service_principal` block as documented below.
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
        <span>Windows<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterwindowsprofile">Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `windows_profile` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Addon<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofile">*Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `addon_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Server<wbr>Authorized<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The IP ranges to whitelist for incoming traffic to the masters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterdefaultnodepool">*Kubernetes<wbr>Cluster<wbr>Default<wbr>Node<wbr>Pool</a></span>
    </dt>
    <dd>{{% md %}}A `default_node_pool` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Pod<wbr>Security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether Pod Security Policies are enabled. Note that this also requires role based access control to be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The FQDN of the Azure Kubernetes Managed Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteridentity">*Kubernetes<wbr>Cluster<wbr>Identity</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kube<wbr>Admin<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config for the admin account to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kube<wbr>Admin<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterkubeadminconfig">[]Kubernetes<wbr>Cluster<wbr>Kube<wbr>Admin<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A `kube_admin_config` block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kube<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kube<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterkubeconfig">[]Kubernetes<wbr>Cluster<wbr>Kube<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A `kube_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kubernetes<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Linux<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterlinuxprofile">*Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `linux_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusternetworkprofile">*Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `network_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group where the Kubernetes Nodes should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The FQDN for the Kubernetes Cluster when private link has been enabled, which is only resolvable inside the Virtual Network used by the Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Link<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Based<wbr>Access<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterrolebasedaccesscontrol">*Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control</a></span>
    </dt>
    <dd>{{% md %}}A `role_based_access_control` block.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Principal</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterserviceprincipal">*Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal</a></span>
    </dt>
    <dd>{{% md %}}A `service_principal` block as documented below.
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
        <span>Windows<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterwindowsprofile">*Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `windows_profile` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>addon<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofile">Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile?</a></span>
    </dt>
    <dd>{{% md %}}A `addon_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>api<wbr>Server<wbr>Authorized<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The IP ranges to whitelist for incoming traffic to the masters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterdefaultnodepool">Kubernetes<wbr>Cluster<wbr>Default<wbr>Node<wbr>Pool?</a></span>
    </dt>
    <dd>{{% md %}}A `default_node_pool` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Pod<wbr>Security<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether Pod Security Policies are enabled. Note that this also requires role based access control to be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The FQDN of the Azure Kubernetes Managed Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteridentity">Kubernetes<wbr>Cluster<wbr>Identity?</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kube<wbr>Admin<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config for the admin account to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kube<wbr>Admin<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterkubeadminconfig">Kubernetes<wbr>Cluster<wbr>Kube<wbr>Admin<wbr>Config[]?</a></span>
    </dt>
    <dd>{{% md %}}A `kube_admin_config` block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kube<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kube<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterkubeconfig">Kubernetes<wbr>Cluster<wbr>Kube<wbr>Config[]?</a></span>
    </dt>
    <dd>{{% md %}}A `kube_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kubernetes<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>linux<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterlinuxprofile">Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile?</a></span>
    </dt>
    <dd>{{% md %}}A `linux_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusternetworkprofile">Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile?</a></span>
    </dt>
    <dd>{{% md %}}A `network_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group where the Kubernetes Nodes should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The FQDN for the Kubernetes Cluster when private link has been enabled, which is only resolvable inside the Virtual Network used by the Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Link<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role<wbr>Based<wbr>Access<wbr>Control</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterrolebasedaccesscontrol">Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control?</a></span>
    </dt>
    <dd>{{% md %}}A `role_based_access_control` block.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Principal</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterserviceprincipal">Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal?</a></span>
    </dt>
    <dd>{{% md %}}A `service_principal` block as documented below.
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
        <span>windows<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterwindowsprofile">Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile?</a></span>
    </dt>
    <dd>{{% md %}}A `windows_profile` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>addon_<wbr>profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofile">Dict[Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}A `addon_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>api_<wbr>server_<wbr>authorized_<wbr>ip_<wbr>ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The IP ranges to whitelist for incoming traffic to the masters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>node_<wbr>pool</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterdefaultnodepool">Dict[Kubernetes<wbr>Cluster<wbr>Default<wbr>Node<wbr>Pool]</a></span>
    </dt>
    <dd>{{% md %}}A `default_node_pool` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>pod_<wbr>security_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether Pod Security Policies are enabled. Note that this also requires role based access control to be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The FQDN of the Azure Kubernetes Managed Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteridentity">Dict[Kubernetes<wbr>Cluster<wbr>Identity]</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kube_<wbr>admin_<wbr>config_<wbr>raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config for the admin account to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kube_<wbr>admin_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterkubeadminconfig">List[Kubernetes<wbr>Cluster<wbr>Kube<wbr>Admin<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A `kube_admin_config` block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kube_<wbr>config_<wbr>raw</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kube_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterkubeconfig">List[Kubernetes<wbr>Cluster<wbr>Kube<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A `kube_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kubernetes_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>linux_<wbr>profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterlinuxprofile">Dict[Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}A `linux_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusternetworkprofile">Dict[Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}A `network_profile` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>resource_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group where the Kubernetes Nodes should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private_<wbr>fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The FQDN for the Kubernetes Cluster when private link has been enabled, which is only resolvable inside the Virtual Network used by the Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private_<wbr>link_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role_<wbr>based_<wbr>access_<wbr>control</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterrolebasedaccesscontrol">Dict[Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control]</a></span>
    </dt>
    <dd>{{% md %}}A `role_based_access_control` block.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>principal</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterserviceprincipal">Dict[Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal]</a></span>
    </dt>
    <dd>{{% md %}}A `service_principal` block as documented below.
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
        <span>windows_<wbr>profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterwindowsprofile">Dict[Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}A `windows_profile` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#KubernetesClusterAddonProfile">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterAddonProfile">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterAddonProfileArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterAddonProfileOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Aci<wbr>Connector<wbr>Linux</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofileaciconnectorlinux">Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Aci<wbr>Connector<wbr>Linux<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `aci_connector_linux` block. For more details, please visit [Create and configure an AKS cluster to use virtual nodes](https://docs.microsoft.com/en-us/azure/aks/virtual-nodes-portal).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofileazurepolicy">Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Azure<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `azure_policy` block as defined below. For more details please visit [Understand Azure Policy for Azure Kubernetes Service](https://docs.microsoft.com/en-ie/azure/governance/policy/concepts/rego-for-aks)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Application<wbr>Routing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofilehttpapplicationrouting">Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Http<wbr>Application<wbr>Routing<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `http_application_routing` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kube<wbr>Dashboard</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofilekubedashboard">Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Kube<wbr>Dashboard<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `kube_dashboard` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oms<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofileomsagent">Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Oms<wbr>Agent<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `oms_agent` block as defined below. For more details, please visit [How to onboard Azure Monitor for containers](https://docs.microsoft.com/en-us/azure/monitoring/monitoring-container-insights-onboard).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Aci<wbr>Connector<wbr>Linux</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofileaciconnectorlinux">*Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Aci<wbr>Connector<wbr>Linux</a></span>
    </dt>
    <dd>{{% md %}}A `aci_connector_linux` block. For more details, please visit [Create and configure an AKS cluster to use virtual nodes](https://docs.microsoft.com/en-us/azure/aks/virtual-nodes-portal).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofileazurepolicy">*Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Azure<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `azure_policy` block as defined below. For more details please visit [Understand Azure Policy for Azure Kubernetes Service](https://docs.microsoft.com/en-ie/azure/governance/policy/concepts/rego-for-aks)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Application<wbr>Routing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofilehttpapplicationrouting">*Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Http<wbr>Application<wbr>Routing</a></span>
    </dt>
    <dd>{{% md %}}A `http_application_routing` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kube<wbr>Dashboard</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofilekubedashboard">*Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Kube<wbr>Dashboard</a></span>
    </dt>
    <dd>{{% md %}}A `kube_dashboard` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oms<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofileomsagent">*Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Oms<wbr>Agent</a></span>
    </dt>
    <dd>{{% md %}}A `oms_agent` block as defined below. For more details, please visit [How to onboard Azure Monitor for containers](https://docs.microsoft.com/en-us/azure/monitoring/monitoring-container-insights-onboard).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>aci<wbr>Connector<wbr>Linux</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofileaciconnectorlinux">Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Aci<wbr>Connector<wbr>Linux?</a></span>
    </dt>
    <dd>{{% md %}}A `aci_connector_linux` block. For more details, please visit [Create and configure an AKS cluster to use virtual nodes](https://docs.microsoft.com/en-us/azure/aks/virtual-nodes-portal).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>azure<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofileazurepolicy">Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Azure<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `azure_policy` block as defined below. For more details please visit [Understand Azure Policy for Azure Kubernetes Service](https://docs.microsoft.com/en-ie/azure/governance/policy/concepts/rego-for-aks)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Application<wbr>Routing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofilehttpapplicationrouting">Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Http<wbr>Application<wbr>Routing?</a></span>
    </dt>
    <dd>{{% md %}}A `http_application_routing` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kube<wbr>Dashboard</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofilekubedashboard">Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Kube<wbr>Dashboard?</a></span>
    </dt>
    <dd>{{% md %}}A `kube_dashboard` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oms<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofileomsagent">Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Oms<wbr>Agent?</a></span>
    </dt>
    <dd>{{% md %}}A `oms_agent` block as defined below. For more details, please visit [How to onboard Azure Monitor for containers](https://docs.microsoft.com/en-us/azure/monitoring/monitoring-container-insights-onboard).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>aci<wbr>Connector<wbr>Linux</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofileaciconnectorlinux">Dict[Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Aci<wbr>Connector<wbr>Linux]</a></span>
    </dt>
    <dd>{{% md %}}A `aci_connector_linux` block. For more details, please visit [Create and configure an AKS cluster to use virtual nodes](https://docs.microsoft.com/en-us/azure/aks/virtual-nodes-portal).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>azure<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofileazurepolicy">Dict[Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Azure<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A `azure_policy` block as defined below. For more details please visit [Understand Azure Policy for Azure Kubernetes Service](https://docs.microsoft.com/en-ie/azure/governance/policy/concepts/rego-for-aks)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Application<wbr>Routing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofilehttpapplicationrouting">Dict[Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Http<wbr>Application<wbr>Routing]</a></span>
    </dt>
    <dd>{{% md %}}A `http_application_routing` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kube<wbr>Dashboard</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofilekubedashboard">Dict[Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Kube<wbr>Dashboard]</a></span>
    </dt>
    <dd>{{% md %}}A `kube_dashboard` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oms<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusteraddonprofileomsagent">Dict[Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Oms<wbr>Agent]</a></span>
    </dt>
    <dd>{{% md %}}A `oms_agent` block as defined below. For more details, please visit [How to onboard Azure Monitor for containers](https://docs.microsoft.com/en-us/azure/monitoring/monitoring-container-insights-onboard).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Aci<wbr>Connector<wbr>Linux</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#KubernetesClusterAddonProfileAciConnectorLinux">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterAddonProfileAciConnectorLinux">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterAddonProfileAciConnectorLinuxArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterAddonProfileAciConnectorLinuxOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the virtual node addon enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The subnet name for the virtual nodes to run. This is required when `aci_connector_linux` `enabled` argument is set to `true`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the virtual node addon enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The subnet name for the virtual nodes to run. This is required when `aci_connector_linux` `enabled` argument is set to `true`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Is the virtual node addon enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The subnet name for the virtual nodes to run. This is required when `aci_connector_linux` `enabled` argument is set to `true`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the virtual node addon enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The subnet name for the virtual nodes to run. This is required when `aci_connector_linux` `enabled` argument is set to `true`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Azure<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#KubernetesClusterAddonProfileAzurePolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterAddonProfileAzurePolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterAddonProfileAzurePolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterAddonProfileAzurePolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the Azure Policy for Kubernetes Add On enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the Azure Policy for Kubernetes Add On enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Is the Azure Policy for Kubernetes Add On enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the Azure Policy for Kubernetes Add On enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Http<wbr>Application<wbr>Routing</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#KubernetesClusterAddonProfileHttpApplicationRouting">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterAddonProfileHttpApplicationRouting">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterAddonProfileHttpApplicationRoutingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterAddonProfileHttpApplicationRoutingOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is HTTP Application Routing Enabled? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Application<wbr>Routing<wbr>Zone<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone Name of the HTTP Application Routing.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is HTTP Application Routing Enabled? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Application<wbr>Routing<wbr>Zone<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Zone Name of the HTTP Application Routing.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Is HTTP Application Routing Enabled? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Application<wbr>Routing<wbr>Zone<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone Name of the HTTP Application Routing.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is HTTP Application Routing Enabled? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Application<wbr>Routing<wbr>Zone<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Zone Name of the HTTP Application Routing.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Kube<wbr>Dashboard</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#KubernetesClusterAddonProfileKubeDashboard">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterAddonProfileKubeDashboard">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterAddonProfileKubeDashboardArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterAddonProfileKubeDashboardOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the Kubernetes Dashboard enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the Kubernetes Dashboard enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Is the Kubernetes Dashboard enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the Kubernetes Dashboard enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Oms<wbr>Agent</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#KubernetesClusterAddonProfileOmsAgent">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterAddonProfileOmsAgent">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterAddonProfileOmsAgentArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterAddonProfileOmsAgentOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the OMS Agent Enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Analytics<wbr>Workspace<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Log Analytics Workspace which the OMS Agent should send data to. Must be present if `enabled` is `true`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the OMS Agent Enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Analytics<wbr>Workspace<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Log Analytics Workspace which the OMS Agent should send data to. Must be present if `enabled` is `true`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Is the OMS Agent Enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log<wbr>Analytics<wbr>Workspace<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Log Analytics Workspace which the OMS Agent should send data to. Must be present if `enabled` is `true`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the OMS Agent Enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log_<wbr>analytics_<wbr>workspace_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Log Analytics Workspace which the OMS Agent should send data to. Must be present if `enabled` is `true`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Kubernetes<wbr>Cluster<wbr>Default<wbr>Node<wbr>Pool</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#KubernetesClusterDefaultNodePool">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterDefaultNodePool">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterDefaultNodePoolArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterDefaultNodePoolOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of Availability Zones across which the Node Pool should be spread.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Auto<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should [the Kubernetes Auto Scaler](https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler) be enabled for this Node Pool? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Node<wbr>Public<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should nodes in this Node Pool have a Public IP Address? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum number of nodes which should exist in this Node Pool. If specified this must be between `1` and `100`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Pods</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The minimum number of nodes which should exist in this Node Pool. If specified this must be between `1` and `100`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name which should be used for the default Kubernetes Node Pool. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The initial number of nodes which should exist in this Node Pool. If specified this must be between `1` and `100` and between `min_count` and `max_count`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A map of Kubernetes labels which should be applied to nodes in the Default Node Pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Taints</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g `key=value:NoSchedule`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Os<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The size of the OS Disk which should be used for each agent in the Node Pool. Changing this forces a new resource to be created.
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
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of Node Pool which should be created. Possible values are `AvailabilitySet` and `VirtualMachineScaleSets`. Defaults to `VirtualMachineScaleSets`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vm<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The size of the Virtual Machine, such as `Standard_DS2_v2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vnet<wbr>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of a Subnet where the Kubernetes Node Pool should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of Availability Zones across which the Node Pool should be spread.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Auto<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should [the Kubernetes Auto Scaler](https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler) be enabled for this Node Pool? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Node<wbr>Public<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should nodes in this Node Pool have a Public IP Address? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum number of nodes which should exist in this Node Pool. If specified this must be between `1` and `100`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Pods</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The minimum number of nodes which should exist in this Node Pool. If specified this must be between `1` and `100`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name which should be used for the default Kubernetes Node Pool. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The initial number of nodes which should exist in this Node Pool. If specified this must be between `1` and `100` and between `min_count` and `max_count`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A map of Kubernetes labels which should be applied to nodes in the Default Node Pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Taints</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g `key=value:NoSchedule`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Os<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The size of the OS Disk which should be used for each agent in the Node Pool. Changing this forces a new resource to be created.
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
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of Node Pool which should be created. Possible values are `AvailabilitySet` and `VirtualMachineScaleSets`. Defaults to `VirtualMachineScaleSets`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vm<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The size of the Virtual Machine, such as `Standard_DS2_v2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vnet<wbr>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of a Subnet where the Kubernetes Node Pool should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>availability<wbr>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of Availability Zones across which the Node Pool should be spread.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Auto<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should [the Kubernetes Auto Scaler](https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler) be enabled for this Node Pool? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Node<wbr>Public<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should nodes in this Node Pool have a Public IP Address? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum number of nodes which should exist in this Node Pool. If specified this must be between `1` and `100`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Pods</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The minimum number of nodes which should exist in this Node Pool. If specified this must be between `1` and `100`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name which should be used for the default Kubernetes Node Pool. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The initial number of nodes which should exist in this Node Pool. If specified this must be between `1` and `100` and between `min_count` and `max_count`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A map of Kubernetes labels which should be applied to nodes in the Default Node Pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Taints</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g `key=value:NoSchedule`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>os<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The size of the OS Disk which should be used for each agent in the Node Pool. Changing this forces a new resource to be created.
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
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of Node Pool which should be created. Possible values are `AvailabilitySet` and `VirtualMachineScaleSets`. Defaults to `VirtualMachineScaleSets`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vm<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The size of the Virtual Machine, such as `Standard_DS2_v2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vnet<wbr>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of a Subnet where the Kubernetes Node Pool should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>availability_<wbr>zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of Availability Zones across which the Node Pool should be spread.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>auto_<wbr>scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should [the Kubernetes Auto Scaler](https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler) be enabled for this Node Pool? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>node_<wbr>public_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should nodes in this Node Pool have a Public IP Address? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of nodes which should exist in this Node Pool. If specified this must be between `1` and `100`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>pods</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The minimum number of nodes which should exist in this Node Pool. If specified this must be between `1` and `100`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name which should be used for the default Kubernetes Node Pool. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The initial number of nodes which should exist in this Node Pool. If specified this must be between `1` and `100` and between `min_count` and `max_count`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A map of Kubernetes labels which should be applied to nodes in the Default Node Pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>taints</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g `key=value:NoSchedule`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>os_<wbr>disk_<wbr>size_<wbr>gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The size of the OS Disk which should be used for each agent in the Node Pool. Changing this forces a new resource to be created.
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
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of Node Pool which should be created. Possible values are `AvailabilitySet` and `VirtualMachineScaleSets`. Defaults to `VirtualMachineScaleSets`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vm_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The size of the Virtual Machine, such as `Standard_DS2_v2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vnet_<wbr>subnet_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of a Subnet where the Kubernetes Node Pool should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Kubernetes<wbr>Cluster<wbr>Identity</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#KubernetesClusterIdentity">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterIdentity">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterIdentityArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterIdentityOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Principal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The principal id of the system assigned identity which is used by master components.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Tenant ID used for Azure Active Directory Application. If this isn't specified the Tenant ID of the current Subscription is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of identity used for the managed cluster. At this time the only supported value is `SystemAssigned`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Principal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The principal id of the system assigned identity which is used by master components.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Tenant ID used for Azure Active Directory Application. If this isn't specified the Tenant ID of the current Subscription is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of identity used for the managed cluster. At this time the only supported value is `SystemAssigned`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>principal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The principal id of the system assigned identity which is used by master components.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Tenant ID used for Azure Active Directory Application. If this isn't specified the Tenant ID of the current Subscription is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of identity used for the managed cluster. At this time the only supported value is `SystemAssigned`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>principal_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The principal id of the system assigned identity which is used by master components.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Tenant ID used for Azure Active Directory Application. If this isn't specified the Tenant ID of the current Subscription is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of identity used for the managed cluster. At this time the only supported value is `SystemAssigned`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Kubernetes<wbr>Cluster<wbr>Kube<wbr>Admin<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterKubeAdminConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterKubeAdminConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Kubernetes cluster server host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A password or token used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A username used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Kubernetes cluster server host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A password or token used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A username used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Kubernetes cluster server host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A password or token used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A username used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Kubernetes cluster server host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A password or token used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A username used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Kubernetes<wbr>Cluster<wbr>Kube<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterKubeConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterKubeConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Kubernetes cluster server host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A password or token used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A username used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Kubernetes cluster server host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A password or token used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A username used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Kubernetes cluster server host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A password or token used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A username used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Kubernetes cluster server host.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A password or token used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A username used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#KubernetesClusterLinuxProfile">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterLinuxProfile">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterLinuxProfileArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterLinuxProfileOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Admin Username for the Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ssh<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterlinuxprofilesshkey">Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile<wbr>Ssh<wbr>Key<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}An `ssh_key` block. Only one is currently allowed. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Admin Username for the Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ssh<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterlinuxprofilesshkey">Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile<wbr>Ssh<wbr>Key</a></span>
    </dt>
    <dd>{{% md %}}An `ssh_key` block. Only one is currently allowed. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Admin Username for the Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ssh<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterlinuxprofilesshkey">Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile<wbr>Ssh<wbr>Key</a></span>
    </dt>
    <dd>{{% md %}}An `ssh_key` block. Only one is currently allowed. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>admin_<wbr>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Admin Username for the Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ssh_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterlinuxprofilesshkey">Dict[Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile<wbr>Ssh<wbr>Key]</a></span>
    </dt>
    <dd>{{% md %}}An `ssh_key` block. Only one is currently allowed. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile<wbr>Ssh<wbr>Key</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#KubernetesClusterLinuxProfileSshKey">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterLinuxProfileSshKey">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterLinuxProfileSshKeyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterLinuxProfileSshKeyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Public SSH Key used to access the cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Public SSH Key used to access the cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>key<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Public SSH Key used to access the cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>key<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Public SSH Key used to access the cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#KubernetesClusterNetworkProfile">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterNetworkProfile">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterNetworkProfileArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterNetworkProfileOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Service<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IP address within the Kubernetes service address range that will be used by cluster service discovery (kube-dns). This is required when `network_plugin` is set to `azure`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Docker<wbr>Bridge<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IP address (in CIDR notation) used as the Docker bridge IP address on nodes. This is required when `network_plugin` is set to `azure`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancer<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusternetworkprofileloadbalancerprofile">Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile<wbr>Load<wbr>Balancer<wbr>Profile<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `load_balancer_profile` block. This can only be specified when `load_balancer_sku` is set to `Standard`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancer<wbr>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the SKU of the Load Balancer used for this Kubernetes Cluster. Possible values are `Basic` and `Standard`. Defaults to `Standard`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Plugin</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Network plugin to use for networking. Currently supported values are `azure` and `kubenet`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Sets up network policy to be used with Azure CNI. [Network policy allows us to control the traffic flow between pods](https://docs.microsoft.com/en-us/azure/aks/use-network-policies). Currently supported values are `calico` and `azure`. Changing this forces a new resource to be created. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pod<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The CIDR to use for pod IP addresses. This field can only be set when `network_plugin` is set to `kubenet`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Network Range used by the Kubernetes service. This is required when `network_plugin` is set to `azure`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Service<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}IP address within the Kubernetes service address range that will be used by cluster service discovery (kube-dns). This is required when `network_plugin` is set to `azure`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Docker<wbr>Bridge<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}IP address (in CIDR notation) used as the Docker bridge IP address on nodes. This is required when `network_plugin` is set to `azure`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancer<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusternetworkprofileloadbalancerprofile">*Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile<wbr>Load<wbr>Balancer<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `load_balancer_profile` block. This can only be specified when `load_balancer_sku` is set to `Standard`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancer<wbr>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the SKU of the Load Balancer used for this Kubernetes Cluster. Possible values are `Basic` and `Standard`. Defaults to `Standard`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Plugin</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Network plugin to use for networking. Currently supported values are `azure` and `kubenet`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Sets up network policy to be used with Azure CNI. [Network policy allows us to control the traffic flow between pods](https://docs.microsoft.com/en-us/azure/aks/use-network-policies). Currently supported values are `calico` and `azure`. Changing this forces a new resource to be created. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pod<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The CIDR to use for pod IP addresses. This field can only be set when `network_plugin` is set to `kubenet`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Network Range used by the Kubernetes service. This is required when `network_plugin` is set to `azure`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Service<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IP address within the Kubernetes service address range that will be used by cluster service discovery (kube-dns). This is required when `network_plugin` is set to `azure`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>docker<wbr>Bridge<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IP address (in CIDR notation) used as the Docker bridge IP address on nodes. This is required when `network_plugin` is set to `azure`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load<wbr>Balancer<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusternetworkprofileloadbalancerprofile">Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile<wbr>Load<wbr>Balancer<wbr>Profile?</a></span>
    </dt>
    <dd>{{% md %}}A `load_balancer_profile` block. This can only be specified when `load_balancer_sku` is set to `Standard`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load<wbr>Balancer<wbr>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the SKU of the Load Balancer used for this Kubernetes Cluster. Possible values are `Basic` and `Standard`. Defaults to `Standard`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Plugin</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Network plugin to use for networking. Currently supported values are `azure` and `kubenet`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Sets up network policy to be used with Azure CNI. [Network policy allows us to control the traffic flow between pods](https://docs.microsoft.com/en-us/azure/aks/use-network-policies). Currently supported values are `calico` and `azure`. Changing this forces a new resource to be created. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pod<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The CIDR to use for pod IP addresses. This field can only be set when `network_plugin` is set to `kubenet`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Network Range used by the Kubernetes service. This is required when `network_plugin` is set to `azure`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Service<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}IP address within the Kubernetes service address range that will be used by cluster service discovery (kube-dns). This is required when `network_plugin` is set to `azure`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>docker<wbr>Bridge<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}IP address (in CIDR notation) used as the Docker bridge IP address on nodes. This is required when `network_plugin` is set to `azure`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load<wbr>Balancer<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusternetworkprofileloadbalancerprofile">Dict[Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile<wbr>Load<wbr>Balancer<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}A `load_balancer_profile` block. This can only be specified when `load_balancer_sku` is set to `Standard`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load<wbr>Balancer<wbr>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the SKU of the Load Balancer used for this Kubernetes Cluster. Possible values are `Basic` and `Standard`. Defaults to `Standard`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Plugin</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Network plugin to use for networking. Currently supported values are `azure` and `kubenet`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Sets up network policy to be used with Azure CNI. [Network policy allows us to control the traffic flow between pods](https://docs.microsoft.com/en-us/azure/aks/use-network-policies). Currently supported values are `calico` and `azure`. Changing this forces a new resource to be created. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pod<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The CIDR to use for pod IP addresses. This field can only be set when `network_plugin` is set to `kubenet`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Network Range used by the Kubernetes service. This is required when `network_plugin` is set to `azure`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile<wbr>Load<wbr>Balancer<wbr>Profile</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#KubernetesClusterNetworkProfileLoadBalancerProfile">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterNetworkProfileLoadBalancerProfile">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterNetworkProfileLoadBalancerProfileArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterNetworkProfileLoadBalancerProfileOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Effective<wbr>Outbound<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The outcome (resource IDs) of the specified arguments.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Managed<wbr>Outbound<wbr>Ip<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Count of desired managed outbound IPs for the cluster load balancer. Must be in the range of [1, 100].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Outbound<wbr>Ip<wbr>Address<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The ID of the Public IP Addresses which should be used for outbound communication for the cluster load balancer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Outbound<wbr>Ip<wbr>Prefix<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The ID of the outbound Public IP Address Prefixes which should be used for the cluster load balancer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Effective<wbr>Outbound<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The outcome (resource IDs) of the specified arguments.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Managed<wbr>Outbound<wbr>Ip<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Count of desired managed outbound IPs for the cluster load balancer. Must be in the range of [1, 100].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Outbound<wbr>Ip<wbr>Address<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The ID of the Public IP Addresses which should be used for outbound communication for the cluster load balancer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Outbound<wbr>Ip<wbr>Prefix<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The ID of the outbound Public IP Address Prefixes which should be used for the cluster load balancer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>effective<wbr>Outbound<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The outcome (resource IDs) of the specified arguments.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>managed<wbr>Outbound<wbr>Ip<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Count of desired managed outbound IPs for the cluster load balancer. Must be in the range of [1, 100].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>outbound<wbr>Ip<wbr>Address<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The ID of the Public IP Addresses which should be used for outbound communication for the cluster load balancer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>outbound<wbr>Ip<wbr>Prefix<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The ID of the outbound Public IP Address Prefixes which should be used for the cluster load balancer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>effective<wbr>Outbound<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The outcome (resource IDs) of the specified arguments.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>managed<wbr>Outbound<wbr>Ip<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Count of desired managed outbound IPs for the cluster load balancer. Must be in the range of [1, 100].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>outbound<wbr>Ip<wbr>Address<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The ID of the Public IP Addresses which should be used for outbound communication for the cluster load balancer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>outbound<wbr>Ip<wbr>Prefix<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The ID of the outbound Public IP Address Prefixes which should be used for the cluster load balancer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#KubernetesClusterRoleBasedAccessControl">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterRoleBasedAccessControl">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterRoleBasedAccessControlArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterRoleBasedAccessControlOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterrolebasedaccesscontrolazureactivedirectory">Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control<wbr>Azure<wbr>Active<wbr>Directory<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}An `azure_active_directory` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control Enabled? Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterrolebasedaccesscontrolazureactivedirectory">*Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control<wbr>Azure<wbr>Active<wbr>Directory</a></span>
    </dt>
    <dd>{{% md %}}An `azure_active_directory` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control Enabled? Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>azure<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterrolebasedaccesscontrolazureactivedirectory">Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control<wbr>Azure<wbr>Active<wbr>Directory?</a></span>
    </dt>
    <dd>{{% md %}}An `azure_active_directory` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control Enabled? Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>azure_<wbr>active_<wbr>directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesclusterrolebasedaccesscontrolazureactivedirectory">Dict[Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control<wbr>Azure<wbr>Active<wbr>Directory]</a></span>
    </dt>
    <dd>{{% md %}}An `azure_active_directory` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control Enabled? Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control<wbr>Azure<wbr>Active<wbr>Directory</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#KubernetesClusterRoleBasedAccessControlAzureActiveDirectory">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterRoleBasedAccessControlAzureActiveDirectory">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterRoleBasedAccessControlAzureActiveDirectoryArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterRoleBasedAccessControlAzureActiveDirectoryOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Client ID of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Server ID of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>App<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Server Secret of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Tenant ID used for Azure Active Directory Application. If this isn't specified the Tenant ID of the current Subscription is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Client ID of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Server ID of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>App<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Server Secret of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Tenant ID used for Azure Active Directory Application. If this isn't specified the Tenant ID of the current Subscription is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Client ID of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server<wbr>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Server ID of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server<wbr>App<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Server Secret of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Tenant ID used for Azure Active Directory Application. If this isn't specified the Tenant ID of the current Subscription is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Client ID of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server<wbr>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Server ID of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server<wbr>App<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Server Secret of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Tenant ID used for Azure Active Directory Application. If this isn't specified the Tenant ID of the current Subscription is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#KubernetesClusterServicePrincipal">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterServicePrincipal">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterServicePrincipalArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterServicePrincipalOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Client ID for the Service Principal.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Client Secret for the Service Principal.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Client ID for the Service Principal.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Client Secret for the Service Principal.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Client ID for the Service Principal.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Client Secret for the Service Principal.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Client ID for the Service Principal.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>client_<wbr>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Client Secret for the Service Principal.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#KubernetesClusterWindowsProfile">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#KubernetesClusterWindowsProfile">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterWindowsProfileArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/containerservice?tab=doc#KubernetesClusterWindowsProfileOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Admin Password for Windows VMs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Admin Username for Windows VMs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Admin Password for Windows VMs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Admin Username for Windows VMs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Admin Password for Windows VMs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Admin Username for Windows VMs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin_<wbr>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Admin Password for Windows VMs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>admin_<wbr>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Admin Username for Windows VMs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-azure">https://github.com/pulumi/pulumi-azure</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
