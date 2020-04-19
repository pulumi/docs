
---
title: "GetKubernetesCluster"
block_external_search_index: true
---



Use this data source to access information about an existing Managed Kubernetes Cluster (AKS).

{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as azure from "@pulumi/azure";

const example = pulumi.output(azure.containerservice.getKubernetesCluster({
    name: "myakscluster",
    resourceGroupName: "my-example-resource-group",
}, { async: true }));
```

{{% /example %}}
{{% /examples %}}





## Using GetKubernetesCluster {#using}

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getKubernetesCluster<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/containerservice/#GetKubernetesClusterArgs">GetKubernetesClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/containerservice/#GetKubernetesClusterResult">GetKubernetesClusterResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_kubernetes_cluster(</span>name=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupKubernetesCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/containerservice?tab=doc#LookupKubernetesClusterArgs">LookupKubernetesClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/containerservice?tab=doc#LookupKubernetesClusterResult">LookupKubernetesClusterResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetKubernetesCluster </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Containerservice.GetKubernetesClusterResult.html">GetKubernetesClusterResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.ContainerService.GetKubernetesClusterArgs.html">GetKubernetesClusterArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the managed Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the managed Kubernetes Cluster exists.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the managed Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the managed Kubernetes Cluster exists.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the managed Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the managed Kubernetes Cluster exists.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the managed Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the managed Kubernetes Cluster exists.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetKubernetesCluster Result {#result}

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Addon<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofile">List&lt;Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `addon_profile` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Agent<wbr>Pool<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteragentpoolprofile">List&lt;Get<wbr>Kubernetes<wbr>Cluster<wbr>Agent<wbr>Pool<wbr>Profile&gt;</a></span>
    </dt>
    <dd>{{% md %}}An `agent_pool_profile` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Api<wbr>Server<wbr>Authorized<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The IP ranges to whitelist for incoming traffic to the masters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dns<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The DNS Prefix of the managed Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The FQDN of the Azure Kubernetes Managed Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kube<wbr>Admin<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config for the admin account to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kube<wbr>Admin<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterkubeadminconfig">List&lt;Get<wbr>Kubernetes<wbr>Cluster<wbr>Kube<wbr>Admin<wbr>Config&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `kube_admin_config` block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kube<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded Kubernetes configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kube<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterkubeconfig">List&lt;Get<wbr>Kubernetes<wbr>Cluster<wbr>Kube<wbr>Config&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `kube_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kubernetes<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The version of Kubernetes used on the managed Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Linux<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterlinuxprofile">List&lt;Get<wbr>Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `linux_profile` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Azure Region in which the managed Kubernetes Cluster exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name assigned to this pool of agents.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusternetworkprofile">List&lt;Get<wbr>Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `network_profile` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Auto-generated Resource Group containing AKS Cluster resources.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The FQDN of this Kubernetes Cluster when private link has been enabled. This name is only resolvable inside the Virtual Network where the Azure Kubernetes Service is located                   
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Link<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Does this Kubernetes Cluster have the Kubernetes API exposed via Private Link?                           
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role<wbr>Based<wbr>Access<wbr>Controls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterrolebasedaccesscontrol">List&lt;Get<wbr>Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `role_based_access_control` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Principals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterserviceprincipal">List&lt;Get<wbr>Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `service_principal` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Windows<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterwindowsprofile">List&lt;Get<wbr>Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `windows_profile` block as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Addon<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofile">[]Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `addon_profile` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Agent<wbr>Pool<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteragentpoolprofile">[]Get<wbr>Kubernetes<wbr>Cluster<wbr>Agent<wbr>Pool<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}An `agent_pool_profile` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Api<wbr>Server<wbr>Authorized<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The IP ranges to whitelist for incoming traffic to the masters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dns<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The DNS Prefix of the managed Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The FQDN of the Azure Kubernetes Managed Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kube<wbr>Admin<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config for the admin account to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kube<wbr>Admin<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterkubeadminconfig">[]Get<wbr>Kubernetes<wbr>Cluster<wbr>Kube<wbr>Admin<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A `kube_admin_config` block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kube<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded Kubernetes configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kube<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterkubeconfig">[]Get<wbr>Kubernetes<wbr>Cluster<wbr>Kube<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A `kube_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kubernetes<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of Kubernetes used on the managed Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Linux<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterlinuxprofile">[]Get<wbr>Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `linux_profile` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Azure Region in which the managed Kubernetes Cluster exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name assigned to this pool of agents.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusternetworkprofile">[]Get<wbr>Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `network_profile` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Auto-generated Resource Group containing AKS Cluster resources.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The FQDN of this Kubernetes Cluster when private link has been enabled. This name is only resolvable inside the Virtual Network where the Azure Kubernetes Service is located                   
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Link<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Does this Kubernetes Cluster have the Kubernetes API exposed via Private Link?                           
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role<wbr>Based<wbr>Access<wbr>Controls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterrolebasedaccesscontrol">[]Get<wbr>Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control</a></span>
    </dt>
    <dd>{{% md %}}A `role_based_access_control` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Principals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterserviceprincipal">[]Get<wbr>Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal</a></span>
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
        <span>Windows<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterwindowsprofile">[]Get<wbr>Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}A `windows_profile` block as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>addon<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofile">Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile[]</a></span>
    </dt>
    <dd>{{% md %}}A `addon_profile` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>agent<wbr>Pool<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteragentpoolprofile">Get<wbr>Kubernetes<wbr>Cluster<wbr>Agent<wbr>Pool<wbr>Profile[]</a></span>
    </dt>
    <dd>{{% md %}}An `agent_pool_profile` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>api<wbr>Server<wbr>Authorized<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The IP ranges to whitelist for incoming traffic to the masters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dns<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The DNS Prefix of the managed Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The FQDN of the Azure Kubernetes Managed Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kube<wbr>Admin<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config for the admin account to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kube<wbr>Admin<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterkubeadminconfig">Get<wbr>Kubernetes<wbr>Cluster<wbr>Kube<wbr>Admin<wbr>Config[]</a></span>
    </dt>
    <dd>{{% md %}}A `kube_admin_config` block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kube<wbr>Config<wbr>Raw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded Kubernetes configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kube<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterkubeconfig">Get<wbr>Kubernetes<wbr>Cluster<wbr>Kube<wbr>Config[]</a></span>
    </dt>
    <dd>{{% md %}}A `kube_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kubernetes<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of Kubernetes used on the managed Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>linux<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterlinuxprofile">Get<wbr>Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile[]</a></span>
    </dt>
    <dd>{{% md %}}A `linux_profile` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Azure Region in which the managed Kubernetes Cluster exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name assigned to this pool of agents.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusternetworkprofile">Get<wbr>Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile[]</a></span>
    </dt>
    <dd>{{% md %}}A `network_profile` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node<wbr>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Auto-generated Resource Group containing AKS Cluster resources.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private<wbr>Fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The FQDN of this Kubernetes Cluster when private link has been enabled. This name is only resolvable inside the Virtual Network where the Azure Kubernetes Service is located                   
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private<wbr>Link<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Does this Kubernetes Cluster have the Kubernetes API exposed via Private Link?                           
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role<wbr>Based<wbr>Access<wbr>Controls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterrolebasedaccesscontrol">Get<wbr>Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control[]</a></span>
    </dt>
    <dd>{{% md %}}A `role_based_access_control` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service<wbr>Principals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterserviceprincipal">Get<wbr>Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal[]</a></span>
    </dt>
    <dd>{{% md %}}A `service_principal` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>windows<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterwindowsprofile">Get<wbr>Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile[]</a></span>
    </dt>
    <dd>{{% md %}}A `windows_profile` block as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>addon_<wbr>profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofile">List[Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}A `addon_profile` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>agent_<wbr>pool_<wbr>profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteragentpoolprofile">List[Get<wbr>Kubernetes<wbr>Cluster<wbr>Agent<wbr>Pool<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}An `agent_pool_profile` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>api_<wbr>server_<wbr>authorized_<wbr>ip_<wbr>ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The IP ranges to whitelist for incoming traffic to the masters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dns_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The DNS Prefix of the managed Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The FQDN of the Azure Kubernetes Managed Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kube_<wbr>admin_<wbr>config_<wbr>raw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Raw Kubernetes config for the admin account to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kube_<wbr>admin_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterkubeadminconfig">List[Get<wbr>Kubernetes<wbr>Cluster<wbr>Kube<wbr>Admin<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A `kube_admin_config` block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kube_<wbr>config_<wbr>raw</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded Kubernetes configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kube_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterkubeconfig">List[Get<wbr>Kubernetes<wbr>Cluster<wbr>Kube<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A `kube_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kubernetes_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The version of Kubernetes used on the managed Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>linux_<wbr>profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterlinuxprofile">List[Get<wbr>Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}A `linux_profile` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Azure Region in which the managed Kubernetes Cluster exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name assigned to this pool of agents.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusternetworkprofile">List[Get<wbr>Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}A `network_profile` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node_<wbr>resource_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Auto-generated Resource Group containing AKS Cluster resources.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private_<wbr>fqdn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The FQDN of this Kubernetes Cluster when private link has been enabled. This name is only resolvable inside the Virtual Network where the Azure Kubernetes Service is located                   
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private_<wbr>link_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Does this Kubernetes Cluster have the Kubernetes API exposed via Private Link?                           
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role_<wbr>based_<wbr>access_<wbr>controls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterrolebasedaccesscontrol">List[Get<wbr>Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control]</a></span>
    </dt>
    <dd>{{% md %}}A `role_based_access_control` block as documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service_<wbr>principals</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterserviceprincipal">List[Get<wbr>Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal]</a></span>
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
        <span>windows_<wbr>profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterwindowsprofile">List[Get<wbr>Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}A `windows_profile` block as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types


<h4 id="getkubernetesclusteraddonprofile">Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetKubernetesClusterAddonProfile">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/containerservice?tab=doc#GetKubernetesClusterAddonProfile">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Azure<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofileazurepolicy">List&lt;Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Azure<wbr>Policy<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `azure_policy` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Http<wbr>Application<wbr>Routings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofilehttpapplicationrouting">List&lt;Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Http<wbr>Application<wbr>Routing<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `http_application_routing` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Kube<wbr>Dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofilekubedashboard">List&lt;Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Kube<wbr>Dashboard<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `kube_dashboard` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Oms<wbr>Agents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofileomsagent">List&lt;Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Oms<wbr>Agent<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `oms_agent` block.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Azure<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofileazurepolicy">[]Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Azure<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `azure_policy` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Http<wbr>Application<wbr>Routings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofilehttpapplicationrouting">[]Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Http<wbr>Application<wbr>Routing</a></span>
    </dt>
    <dd>{{% md %}}A `http_application_routing` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Kube<wbr>Dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofilekubedashboard">[]Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Kube<wbr>Dashboard</a></span>
    </dt>
    <dd>{{% md %}}A `kube_dashboard` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Oms<wbr>Agents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofileomsagent">[]Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Oms<wbr>Agent</a></span>
    </dt>
    <dd>{{% md %}}A `oms_agent` block.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>azure<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofileazurepolicy">Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Azure<wbr>Policy[]</a></span>
    </dt>
    <dd>{{% md %}}A `azure_policy` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>http<wbr>Application<wbr>Routings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofilehttpapplicationrouting">Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Http<wbr>Application<wbr>Routing[]</a></span>
    </dt>
    <dd>{{% md %}}A `http_application_routing` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>kube<wbr>Dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofilekubedashboard">Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Kube<wbr>Dashboard[]</a></span>
    </dt>
    <dd>{{% md %}}A `kube_dashboard` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>oms<wbr>Agents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofileomsagent">Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Oms<wbr>Agent[]</a></span>
    </dt>
    <dd>{{% md %}}A `oms_agent` block.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>azure<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofileazurepolicy">List[Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Azure<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A `azure_policy` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>http<wbr>Application<wbr>Routings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofilehttpapplicationrouting">List[Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Http<wbr>Application<wbr>Routing]</a></span>
    </dt>
    <dd>{{% md %}}A `http_application_routing` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>kube<wbr>Dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofilekubedashboard">List[Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Kube<wbr>Dashboard]</a></span>
    </dt>
    <dd>{{% md %}}A `kube_dashboard` block.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>oms<wbr>Agents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusteraddonprofileomsagent">List[Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Oms<wbr>Agent]</a></span>
    </dt>
    <dd>{{% md %}}A `oms_agent` block.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getkubernetesclusteraddonprofileazurepolicy">Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Azure<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetKubernetesClusterAddonProfileAzurePolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/containerservice?tab=doc#GetKubernetesClusterAddonProfileAzurePolicy">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getkubernetesclusteraddonprofilehttpapplicationrouting">Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Http<wbr>Application<wbr>Routing</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetKubernetesClusterAddonProfileHttpApplicationRouting">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/containerservice?tab=doc#GetKubernetesClusterAddonProfileHttpApplicationRouting">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Http<wbr>Application<wbr>Routing<wbr>Zone<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
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
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Http<wbr>Application<wbr>Routing<wbr>Zone<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
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
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>http<wbr>Application<wbr>Routing<wbr>Zone<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
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
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>http<wbr>Application<wbr>Routing<wbr>Zone<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Zone Name of the HTTP Application Routing.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getkubernetesclusteraddonprofilekubedashboard">Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Kube<wbr>Dashboard</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetKubernetesClusterAddonProfileKubeDashboard">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/containerservice?tab=doc#GetKubernetesClusterAddonProfileKubeDashboard">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getkubernetesclusteraddonprofileomsagent">Get<wbr>Kubernetes<wbr>Cluster<wbr>Addon<wbr>Profile<wbr>Oms<wbr>Agent</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetKubernetesClusterAddonProfileOmsAgent">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/containerservice?tab=doc#GetKubernetesClusterAddonProfileOmsAgent">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Log<wbr>Analytics<wbr>Workspace<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the Log Analytics Workspace which the OMS Agent should send data to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Log<wbr>Analytics<wbr>Workspace<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the Log Analytics Workspace which the OMS Agent should send data to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>log<wbr>Analytics<wbr>Workspace<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the Log Analytics Workspace which the OMS Agent should send data to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>log_<wbr>analytics_<wbr>workspace_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the Log Analytics Workspace which the OMS Agent should send data to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getkubernetesclusteragentpoolprofile">Get<wbr>Kubernetes<wbr>Cluster<wbr>Agent<wbr>Pool<wbr>Profile</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetKubernetesClusterAgentPoolProfile">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/containerservice?tab=doc#GetKubernetesClusterAgentPoolProfile">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Availability<wbr>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The availability zones used for the nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of Agents (VM's) in the Pool.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enable<wbr>Auto<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}If the auto-scaler is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Maximum number of nodes for auto-scaling
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Pods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum number of pods that can run on each agent.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Min<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Minimum number of nodes for auto-scaling
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the managed Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Node<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Os<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The size of the Agent VM's Operating System Disk in GB.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Os<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Operating System used for the Agents.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the Agent Pool.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vm<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The size of each VM in the Agent Pool (e.g. `Standard_F1`).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vnet<wbr>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet where the Agents in the Pool are provisioned.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Node<wbr>Public<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Taints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The list of Kubernetes taints which are applied to nodes in the agent pool
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Availability<wbr>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The availability zones used for the nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of Agents (VM's) in the Pool.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enable<wbr>Auto<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}If the auto-scaler is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Maximum number of nodes for auto-scaling
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Pods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum number of pods that can run on each agent.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Min<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Minimum number of nodes for auto-scaling
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the managed Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Node<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Os<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The size of the Agent VM's Operating System Disk in GB.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Os<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Operating System used for the Agents.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the Agent Pool.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vm<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The size of each VM in the Agent Pool (e.g. `Standard_F1`).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vnet<wbr>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet where the Agents in the Pool are provisioned.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Node<wbr>Public<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Taints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The list of Kubernetes taints which are applied to nodes in the agent pool
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>availability<wbr>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The availability zones used for the nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of Agents (VM's) in the Pool.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enable<wbr>Auto<wbr>Scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}If the auto-scaler is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Maximum number of nodes for auto-scaling
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Pods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The maximum number of pods that can run on each agent.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>min<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Minimum number of nodes for auto-scaling
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the managed Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>node<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>os<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The size of the Agent VM's Operating System Disk in GB.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>os<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Operating System used for the Agents.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the Agent Pool.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vm<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The size of each VM in the Agent Pool (e.g. `Standard_F1`).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vnet<wbr>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet where the Agents in the Pool are provisioned.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Node<wbr>Public<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Taints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The list of Kubernetes taints which are applied to nodes in the agent pool
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>availability_<wbr>zones</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The availability zones used for the nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of Agents (VM's) in the Pool.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enable_<wbr>auto_<wbr>scaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}If the auto-scaler is enabled.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Maximum number of nodes for auto-scaling
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max_<wbr>pods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The maximum number of pods that can run on each agent.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>min_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Minimum number of nodes for auto-scaling
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the managed Kubernetes Cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>node_<wbr>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>os_<wbr>disk_<wbr>size_<wbr>gb</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The size of the Agent VM's Operating System Disk in GB.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>os_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Operating System used for the Agents.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of the Agent Pool.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vm_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The size of each VM in the Agent Pool (e.g. `Standard_F1`).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vnet_<wbr>subnet_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet where the Agents in the Pool are provisioned.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>node_<wbr>public_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>taints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The list of Kubernetes taints which are applied to nodes in the agent pool
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getkubernetesclusterkubeadminconfig">Get<wbr>Kubernetes<wbr>Cluster<wbr>Kube<wbr>Admin<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetKubernetesClusterKubeAdminConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/containerservice?tab=doc#GetKubernetesClusterKubeAdminConfig">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Kubernetes cluster server host.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A password or token used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A username used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Kubernetes cluster server host.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A password or token used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A username used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Kubernetes cluster server host.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A password or token used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A username used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Kubernetes cluster server host.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A password or token used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A username used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getkubernetesclusterkubeconfig">Get<wbr>Kubernetes<wbr>Cluster<wbr>Kube<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetKubernetesClusterKubeConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/containerservice?tab=doc#GetKubernetesClusterKubeConfig">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Kubernetes cluster server host.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A password or token used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A username used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Kubernetes cluster server host.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A password or token used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A username used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Kubernetes cluster server host.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A password or token used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A username used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Kubernetes cluster server host.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A password or token used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A username used to authenticate to the Kubernetes cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getkubernetesclusterlinuxprofile">Get<wbr>Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetKubernetesClusterLinuxProfile">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/containerservice?tab=doc#GetKubernetesClusterLinuxProfile">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The username associated with the administrator account of the Windows VMs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterlinuxprofilesshkey">List&lt;Get<wbr>Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile<wbr>Ssh<wbr>Key<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}An `ssh_key` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The username associated with the administrator account of the Windows VMs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterlinuxprofilesshkey">[]Get<wbr>Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile<wbr>Ssh<wbr>Key</a></span>
    </dt>
    <dd>{{% md %}}An `ssh_key` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The username associated with the administrator account of the Windows VMs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterlinuxprofilesshkey">Get<wbr>Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile<wbr>Ssh<wbr>Key[]</a></span>
    </dt>
    <dd>{{% md %}}An `ssh_key` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>admin_<wbr>username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The username associated with the administrator account of the Windows VMs.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterlinuxprofilesshkey">List[Get<wbr>Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile<wbr>Ssh<wbr>Key]</a></span>
    </dt>
    <dd>{{% md %}}An `ssh_key` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getkubernetesclusterlinuxprofilesshkey">Get<wbr>Kubernetes<wbr>Cluster<wbr>Linux<wbr>Profile<wbr>Ssh<wbr>Key</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetKubernetesClusterLinuxProfileSshKey">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/containerservice?tab=doc#GetKubernetesClusterLinuxProfileSshKey">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Public SSH Key used to access the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Public SSH Key used to access the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>key<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Public SSH Key used to access the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>key<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Public SSH Key used to access the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getkubernetesclusternetworkprofile">Get<wbr>Kubernetes<wbr>Cluster<wbr>Network<wbr>Profile</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetKubernetesClusterNetworkProfile">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/containerservice?tab=doc#GetKubernetesClusterNetworkProfile">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dns<wbr>Service<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}IP address within the Kubernetes service address range used by cluster service discovery (kube-dns).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Docker<wbr>Bridge<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}IP address (in CIDR notation) used as the Docker bridge IP address on nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Load<wbr>Balancer<wbr>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Plugin</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Network plugin used such as `azure` or `kubenet`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Network policy to be used with Azure CNI. Eg: `calico` or `azure`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Pod<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The CIDR used for pod IP addresses.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Network range used by the Kubernetes service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dns<wbr>Service<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}IP address within the Kubernetes service address range used by cluster service discovery (kube-dns).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Docker<wbr>Bridge<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}IP address (in CIDR notation) used as the Docker bridge IP address on nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Load<wbr>Balancer<wbr>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Plugin</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Network plugin used such as `azure` or `kubenet`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Network policy to be used with Azure CNI. Eg: `calico` or `azure`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Pod<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The CIDR used for pod IP addresses.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Network range used by the Kubernetes service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dns<wbr>Service<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}IP address within the Kubernetes service address range used by cluster service discovery (kube-dns).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>docker<wbr>Bridge<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}IP address (in CIDR notation) used as the Docker bridge IP address on nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>load<wbr>Balancer<wbr>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Plugin</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Network plugin used such as `azure` or `kubenet`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Network policy to be used with Azure CNI. Eg: `calico` or `azure`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>pod<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The CIDR used for pod IP addresses.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Network range used by the Kubernetes service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dns<wbr>Service<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}IP address within the Kubernetes service address range used by cluster service discovery (kube-dns).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>docker<wbr>Bridge<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}IP address (in CIDR notation) used as the Docker bridge IP address on nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>load<wbr>Balancer<wbr>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Plugin</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Network plugin used such as `azure` or `kubenet`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Network policy to be used with Azure CNI. Eg: `calico` or `azure`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>pod<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The CIDR used for pod IP addresses.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Network range used by the Kubernetes service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getkubernetesclusterrolebasedaccesscontrol">Get<wbr>Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetKubernetesClusterRoleBasedAccessControl">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/containerservice?tab=doc#GetKubernetesClusterRoleBasedAccessControl">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Azure<wbr>Active<wbr>Directories</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterrolebasedaccesscontrolazureactivedirectory">List&lt;Get<wbr>Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control<wbr>Azure<wbr>Active<wbr>Directory<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `azure_active_directory` block as documented above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Azure<wbr>Active<wbr>Directories</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterrolebasedaccesscontrolazureactivedirectory">[]Get<wbr>Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control<wbr>Azure<wbr>Active<wbr>Directory</a></span>
    </dt>
    <dd>{{% md %}}A `azure_active_directory` block as documented above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>azure<wbr>Active<wbr>Directories</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterrolebasedaccesscontrolazureactivedirectory">Get<wbr>Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control<wbr>Azure<wbr>Active<wbr>Directory[]</a></span>
    </dt>
    <dd>{{% md %}}A `azure_active_directory` block as documented above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>azure<wbr>Active<wbr>Directories</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getkubernetesclusterrolebasedaccesscontrolazureactivedirectory">List[Get<wbr>Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control<wbr>Azure<wbr>Active<wbr>Directory]</a></span>
    </dt>
    <dd>{{% md %}}A `azure_active_directory` block as documented above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Role Based Access Control enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getkubernetesclusterrolebasedaccesscontrolazureactivedirectory">Get<wbr>Kubernetes<wbr>Cluster<wbr>Role<wbr>Based<wbr>Access<wbr>Control<wbr>Azure<wbr>Active<wbr>Directory</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetKubernetesClusterRoleBasedAccessControlAzureActiveDirectory">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/containerservice?tab=doc#GetKubernetesClusterRoleBasedAccessControlAzureActiveDirectory">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Client ID of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Server ID of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Tenant ID used for Azure Active Directory Application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Client ID of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Server ID of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Tenant ID used for Azure Active Directory Application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Client ID of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server<wbr>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Server ID of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Tenant ID used for Azure Active Directory Application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Client ID of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>server<wbr>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Server ID of an Azure Active Directory Application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Tenant ID used for Azure Active Directory Application.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getkubernetesclusterserviceprincipal">Get<wbr>Kubernetes<wbr>Cluster<wbr>Service<wbr>Principal</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetKubernetesClusterServicePrincipal">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/containerservice?tab=doc#GetKubernetesClusterServicePrincipal">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Client ID of the Service Principal used by this Managed Kubernetes Cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Client ID of the Service Principal used by this Managed Kubernetes Cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Client ID of the Service Principal used by this Managed Kubernetes Cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Client ID of the Service Principal used by this Managed Kubernetes Cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getkubernetesclusterwindowsprofile">Get<wbr>Kubernetes<wbr>Cluster<wbr>Windows<wbr>Profile</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetKubernetesClusterWindowsProfile">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/containerservice?tab=doc#GetKubernetesClusterWindowsProfile">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The username associated with the administrator account of the Windows VMs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The username associated with the administrator account of the Windows VMs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The username associated with the administrator account of the Windows VMs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>admin_<wbr>username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The username associated with the administrator account of the Windows VMs.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







