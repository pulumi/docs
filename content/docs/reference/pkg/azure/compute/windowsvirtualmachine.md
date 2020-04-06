
---
title: "WindowsVirtualMachine"
block_external_search_index: true
---



Manages a Windows Virtual Machine.

## Disclaimers

> **Note** This provider will automatically remove the OS Disk by default - this behaviour can be configured using the `features` configuration within the Provider configuration block.

> **Note** This resource does not support Unmanaged Disks. If you need to use Unmanaged Disks you can continue to use the `azure.compute.VirtualMachine` resource instead.

> **Note** This resource does not support attaching existing OS Disks. You can instead capture an image of the OS Disk or continue to use the `azure.compute.VirtualMachine` resource instead.

> In this release there's a known issue where the `public_ip_address` and `public_ip_addresses` fields may not be fully populated for Dynamic Public IP's.

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/windows_virtual_machine.html.markdown.



## Create a WindowsVirtualMachine Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/compute/#WindowsVirtualMachine">WindowsVirtualMachine</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/compute/#WindowsVirtualMachineArgs">WindowsVirtualMachineArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">WindowsVirtualMachine</span><span class="p">(resource_name, opts=None, </span>additional_capabilities=None<span class="p">, </span>additional_unattend_contents=None<span class="p">, </span>admin_password=None<span class="p">, </span>admin_username=None<span class="p">, </span>allow_extension_operations=None<span class="p">, </span>availability_set_id=None<span class="p">, </span>boot_diagnostics=None<span class="p">, </span>computer_name=None<span class="p">, </span>custom_data=None<span class="p">, </span>dedicated_host_id=None<span class="p">, </span>enable_automatic_updates=None<span class="p">, </span>eviction_policy=None<span class="p">, </span>identity=None<span class="p">, </span>license_type=None<span class="p">, </span>location=None<span class="p">, </span>max_bid_price=None<span class="p">, </span>name=None<span class="p">, </span>network_interface_ids=None<span class="p">, </span>os_disk=None<span class="p">, </span>plan=None<span class="p">, </span>priority=None<span class="p">, </span>provision_vm_agent=None<span class="p">, </span>proximity_placement_group_id=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>secrets=None<span class="p">, </span>size=None<span class="p">, </span>source_image_id=None<span class="p">, </span>source_image_reference=None<span class="p">, </span>tags=None<span class="p">, </span>timezone=None<span class="p">, </span>winrm_listeners=None<span class="p">, </span>zone=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewWindowsVirtualMachine<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineArgs">WindowsVirtualMachineArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachine">WindowsVirtualMachine</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Compute.WindowsVirtualMachine.html">WindowsVirtualMachine</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Compute.WindowsVirtualMachineArgs.html">WindowsVirtualMachineArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Additional<wbr>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalcapabilities">Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Capabilities<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Unattend<wbr>Contents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalunattendcontent">List&lt;Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Unattend<wbr>Content<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `additional_unattend_content` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Extension<wbr>Operations</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinebootdiagnostics">Windows<wbr>Virtual<wbr>Machine<wbr>Boot<wbr>Diagnostics<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Computer<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the `name` field. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dedicated<wbr>Host<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Automatic<wbr>Updates</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies if Automatic Updates are Enabled for the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is `Deallocate`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineidentity">Windows<wbr>Virtual<wbr>Machine<wbr>Identity<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}An `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>License<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of on-premise license (also known as [Azure Hybrid Use Benefit](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing)) which should be used for this Virtual Machine. Possible values are `None`, `Windows_Client` and `Windows_Server`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Windows Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the `eviction_policy`. Defaults to `-1`, which means that the Virtual Machine should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Interface<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}. A list of Network Interface ID's which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineosdisk">Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineplan">Windows<wbr>Virtual<wbr>Machine<wbr>Plan<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `plan` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to `true`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Windows Virtual Machine should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesecret">List&lt;Windows<wbr>Virtual<wbr>Machine<wbr>Secret<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SKU which should be used for this Virtual Machine, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesourceimagereference">Windows<wbr>Virtual<wbr>Machine<wbr>Source<wbr>Image<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Time Zone which should be used by the Virtual Machine, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Winrm<wbr>Listeners</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinewinrmlistener">List&lt;Windows<wbr>Virtual<wbr>Machine<wbr>Winrm<wbr>Listener<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `winrm_listener` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalcapabilities">*Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Capabilities</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Unattend<wbr>Contents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalunattendcontent">[]Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Unattend<wbr>Content</a></span>
    </dt>
    <dd>{{% md %}}One or more `additional_unattend_content` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Extension<wbr>Operations</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinebootdiagnostics">*Windows<wbr>Virtual<wbr>Machine<wbr>Boot<wbr>Diagnostics</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Computer<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the `name` field. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dedicated<wbr>Host<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Automatic<wbr>Updates</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies if Automatic Updates are Enabled for the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is `Deallocate`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineidentity">*Windows<wbr>Virtual<wbr>Machine<wbr>Identity</a></span>
    </dt>
    <dd>{{% md %}}An `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>License<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the type of on-premise license (also known as [Azure Hybrid Use Benefit](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing)) which should be used for this Virtual Machine. Possible values are `None`, `Windows_Client` and `Windows_Server`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Windows Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the `eviction_policy`. Defaults to `-1`, which means that the Virtual Machine should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Interface<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}. A list of Network Interface ID's which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineosdisk">Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}A `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineplan">*Windows<wbr>Virtual<wbr>Machine<wbr>Plan</a></span>
    </dt>
    <dd>{{% md %}}A `plan` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to `true`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Windows Virtual Machine should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesecret">[]Windows<wbr>Virtual<wbr>Machine<wbr>Secret</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SKU which should be used for this Virtual Machine, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesourceimagereference">*Windows<wbr>Virtual<wbr>Machine<wbr>Source<wbr>Image<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the Time Zone which should be used by the Virtual Machine, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Winrm<wbr>Listeners</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinewinrmlistener">[]Windows<wbr>Virtual<wbr>Machine<wbr>Winrm<wbr>Listener</a></span>
    </dt>
    <dd>{{% md %}}One or more `winrm_listener` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>additional<wbr>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalcapabilities">Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Capabilities?</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>additional<wbr>Unattend<wbr>Contents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalunattendcontent">Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Unattend<wbr>Content[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `additional_unattend_content` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Extension<wbr>Operations</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>availability<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinebootdiagnostics">Windows<wbr>Virtual<wbr>Machine<wbr>Boot<wbr>Diagnostics?</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>computer<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the `name` field. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dedicated<wbr>Host<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Automatic<wbr>Updates</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies if Automatic Updates are Enabled for the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is `Deallocate`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineidentity">Windows<wbr>Virtual<wbr>Machine<wbr>Identity?</a></span>
    </dt>
    <dd>{{% md %}}An `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>license<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of on-premise license (also known as [Azure Hybrid Use Benefit](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing)) which should be used for this Virtual Machine. Possible values are `None`, `Windows_Client` and `Windows_Server`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Windows Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the `eviction_policy`. Defaults to `-1`, which means that the Virtual Machine should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Interface<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}. A list of Network Interface ID's which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineosdisk">Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}A `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineplan">Windows<wbr>Virtual<wbr>Machine<wbr>Plan?</a></span>
    </dt>
    <dd>{{% md %}}A `plan` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to `true`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Windows Virtual Machine should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesecret">Windows<wbr>Virtual<wbr>Machine<wbr>Secret[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SKU which should be used for this Virtual Machine, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesourceimagereference">Windows<wbr>Virtual<wbr>Machine<wbr>Source<wbr>Image<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Time Zone which should be used by the Virtual Machine, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>winrm<wbr>Listeners</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinewinrmlistener">Windows<wbr>Virtual<wbr>Machine<wbr>Winrm<wbr>Listener[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `winrm_listener` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>additional_<wbr>capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalcapabilities">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Capabilities]</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>additional_<wbr>unattend_<wbr>contents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalunattendcontent">List[Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Unattend<wbr>Content]</a></span>
    </dt>
    <dd>{{% md %}}One or more `additional_unattend_content` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>admin_<wbr>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>admin_<wbr>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>extension_<wbr>operations</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>availability_<wbr>set_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot_<wbr>diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinebootdiagnostics">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Boot<wbr>Diagnostics]</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>computer_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the `name` field. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dedicated_<wbr>host_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>automatic_<wbr>updates</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies if Automatic Updates are Enabled for the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eviction_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is `Deallocate`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineidentity">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Identity]</a></span>
    </dt>
    <dd>{{% md %}}An `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>license_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the type of on-premise license (also known as [Azure Hybrid Use Benefit](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing)) which should be used for this Virtual Machine. Possible values are `None`, `Windows_Client` and `Windows_Server`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Windows Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>bid_<wbr>price</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the `eviction_policy`. Defaults to `-1`, which means that the Virtual Machine should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network_<wbr>interface_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}. A list of Network Interface ID's which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>os_<wbr>disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineosdisk">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}A `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineplan">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Plan]</a></span>
    </dt>
    <dd>{{% md %}}A `plan` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provision_<wbr>vm_<wbr>agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to `true`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proximity_<wbr>placement_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Windows Virtual Machine should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesecret">List[Windows<wbr>Virtual<wbr>Machine<wbr>Secret]</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The SKU which should be used for this Virtual Machine, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>image_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>image_<wbr>reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesourceimagereference">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Source<wbr>Image<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Time Zone which should be used by the Virtual Machine, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>winrm_<wbr>listeners</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinewinrmlistener">List[Windows<wbr>Virtual<wbr>Machine<wbr>Winrm<wbr>Listener]</a></span>
    </dt>
    <dd>{{% md %}}One or more `winrm_listener` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## WindowsVirtualMachine Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Additional<wbr>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalcapabilities">Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Capabilities?</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Additional<wbr>Unattend<wbr>Contents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalunattendcontent">List&lt;Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Unattend<wbr>Content&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `additional_unattend_content` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Extension<wbr>Operations</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Availability<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinebootdiagnostics">Windows<wbr>Virtual<wbr>Machine<wbr>Boot<wbr>Diagnostics?</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Computer<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the `name` field. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dedicated<wbr>Host<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Automatic<wbr>Updates</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies if Automatic Updates are Enabled for the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is `Deallocate`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineidentity">Windows<wbr>Virtual<wbr>Machine<wbr>Identity?</a></span>
    </dt>
    <dd>{{% md %}}An `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>License<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of on-premise license (also known as [Azure Hybrid Use Benefit](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing)) which should be used for this Virtual Machine. Possible values are `None`, `Windows_Client` and `Windows_Server`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Windows Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the `eviction_policy`. Defaults to `-1`, which means that the Virtual Machine should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interface<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}. A list of Network Interface ID's which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineosdisk">Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}A `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineplan">Windows<wbr>Virtual<wbr>Machine<wbr>Plan?</a></span>
    </dt>
    <dd>{{% md %}}A `plan` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary Private IP Address assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of Private IP Addresses assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to `true`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary Public IP Address assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of the Public IP Addresses assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Windows Virtual Machine should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesecret">List&lt;Windows<wbr>Virtual<wbr>Machine<wbr>Secret&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SKU which should be used for this Virtual Machine, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesourceimagereference">Windows<wbr>Virtual<wbr>Machine<wbr>Source<wbr>Image<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Time Zone which should be used by the Virtual Machine, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A 128-bit identifier which uniquely identifies this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Winrm<wbr>Listeners</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinewinrmlistener">List&lt;Windows<wbr>Virtual<wbr>Machine<wbr>Winrm<wbr>Listener&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `winrm_listener` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Additional<wbr>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalcapabilities">*Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Capabilities</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Additional<wbr>Unattend<wbr>Contents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalunattendcontent">[]Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Unattend<wbr>Content</a></span>
    </dt>
    <dd>{{% md %}}One or more `additional_unattend_content` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Extension<wbr>Operations</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Availability<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinebootdiagnostics">*Windows<wbr>Virtual<wbr>Machine<wbr>Boot<wbr>Diagnostics</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Computer<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the `name` field. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dedicated<wbr>Host<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Automatic<wbr>Updates</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies if Automatic Updates are Enabled for the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is `Deallocate`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineidentity">*Windows<wbr>Virtual<wbr>Machine<wbr>Identity</a></span>
    </dt>
    <dd>{{% md %}}An `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>License<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the type of on-premise license (also known as [Azure Hybrid Use Benefit](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing)) which should be used for this Virtual Machine. Possible values are `None`, `Windows_Client` and `Windows_Server`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Windows Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the `eviction_policy`. Defaults to `-1`, which means that the Virtual Machine should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interface<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}. A list of Network Interface ID's which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineosdisk">Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}A `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineplan">*Windows<wbr>Virtual<wbr>Machine<wbr>Plan</a></span>
    </dt>
    <dd>{{% md %}}A `plan` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary Private IP Address assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of Private IP Addresses assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to `true`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary Public IP Address assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of the Public IP Addresses assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Windows Virtual Machine should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesecret">[]Windows<wbr>Virtual<wbr>Machine<wbr>Secret</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SKU which should be used for this Virtual Machine, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesourceimagereference">*Windows<wbr>Virtual<wbr>Machine<wbr>Source<wbr>Image<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the Time Zone which should be used by the Virtual Machine, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A 128-bit identifier which uniquely identifies this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Winrm<wbr>Listeners</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinewinrmlistener">[]Windows<wbr>Virtual<wbr>Machine<wbr>Winrm<wbr>Listener</a></span>
    </dt>
    <dd>{{% md %}}One or more `winrm_listener` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>additional<wbr>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalcapabilities">Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Capabilities?</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>additional<wbr>Unattend<wbr>Contents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalunattendcontent">Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Unattend<wbr>Content[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `additional_unattend_content` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow<wbr>Extension<wbr>Operations</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>availability<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinebootdiagnostics">Windows<wbr>Virtual<wbr>Machine<wbr>Boot<wbr>Diagnostics?</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>computer<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the `name` field. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dedicated<wbr>Host<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Automatic<wbr>Updates</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies if Automatic Updates are Enabled for the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is `Deallocate`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineidentity">Windows<wbr>Virtual<wbr>Machine<wbr>Identity?</a></span>
    </dt>
    <dd>{{% md %}}An `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>license<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of on-premise license (also known as [Azure Hybrid Use Benefit](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing)) which should be used for this Virtual Machine. Possible values are `None`, `Windows_Client` and `Windows_Server`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Windows Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the `eviction_policy`. Defaults to `-1`, which means that the Virtual Machine should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Interface<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}. A list of Network Interface ID's which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineosdisk">Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}A `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineplan">Windows<wbr>Virtual<wbr>Machine<wbr>Plan?</a></span>
    </dt>
    <dd>{{% md %}}A `plan` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary Private IP Address assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of Private IP Addresses assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to `true`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary Public IP Address assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of the Public IP Addresses assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Windows Virtual Machine should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesecret">Windows<wbr>Virtual<wbr>Machine<wbr>Secret[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SKU which should be used for this Virtual Machine, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesourceimagereference">Windows<wbr>Virtual<wbr>Machine<wbr>Source<wbr>Image<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Time Zone which should be used by the Virtual Machine, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A 128-bit identifier which uniquely identifies this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>winrm<wbr>Listeners</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinewinrmlistener">Windows<wbr>Virtual<wbr>Machine<wbr>Winrm<wbr>Listener[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `winrm_listener` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>additional_<wbr>capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalcapabilities">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Capabilities]</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>additional_<wbr>unattend_<wbr>contents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalunattendcontent">List[Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Unattend<wbr>Content]</a></span>
    </dt>
    <dd>{{% md %}}One or more `additional_unattend_content` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>admin_<wbr>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>admin_<wbr>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow_<wbr>extension_<wbr>operations</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>availability_<wbr>set_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>boot_<wbr>diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinebootdiagnostics">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Boot<wbr>Diagnostics]</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>computer_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the `name` field. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dedicated_<wbr>host_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>automatic_<wbr>updates</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies if Automatic Updates are Enabled for the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>eviction_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is `Deallocate`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineidentity">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Identity]</a></span>
    </dt>
    <dd>{{% md %}}An `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>license_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the type of on-premise license (also known as [Azure Hybrid Use Benefit](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing)) which should be used for this Virtual Machine. Possible values are `None`, `Windows_Client` and `Windows_Server`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Windows Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max_<wbr>bid_<wbr>price</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the `eviction_policy`. Defaults to `-1`, which means that the Virtual Machine should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>interface_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}. A list of Network Interface ID's which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>os_<wbr>disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineosdisk">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}A `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineplan">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Plan]</a></span>
    </dt>
    <dd>{{% md %}}A `plan` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Primary Private IP Address assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private_<wbr>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of Private IP Addresses assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>provision_<wbr>vm_<wbr>agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to `true`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>proximity_<wbr>placement_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Primary Public IP Address assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public_<wbr>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of the Public IP Addresses assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Windows Virtual Machine should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesecret">List[Windows<wbr>Virtual<wbr>Machine<wbr>Secret]</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The SKU which should be used for this Virtual Machine, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source_<wbr>image_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source_<wbr>image_<wbr>reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesourceimagereference">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Source<wbr>Image<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Time Zone which should be used by the Virtual Machine, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>virtual_<wbr>machine_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A 128-bit identifier which uniquely identifies this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>winrm_<wbr>listeners</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinewinrmlistener">List[Windows<wbr>Virtual<wbr>Machine<wbr>Winrm<wbr>Listener]</a></span>
    </dt>
    <dd>{{% md %}}One or more `winrm_listener` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing WindowsVirtualMachine Resource

Get an existing WindowsVirtualMachine resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/compute/#WindowsVirtualMachineState">WindowsVirtualMachineState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/compute/#WindowsVirtualMachine">WindowsVirtualMachine</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>additional_capabilities=None<span class="p">, </span>additional_unattend_contents=None<span class="p">, </span>admin_password=None<span class="p">, </span>admin_username=None<span class="p">, </span>allow_extension_operations=None<span class="p">, </span>availability_set_id=None<span class="p">, </span>boot_diagnostics=None<span class="p">, </span>computer_name=None<span class="p">, </span>custom_data=None<span class="p">, </span>dedicated_host_id=None<span class="p">, </span>enable_automatic_updates=None<span class="p">, </span>eviction_policy=None<span class="p">, </span>identity=None<span class="p">, </span>license_type=None<span class="p">, </span>location=None<span class="p">, </span>max_bid_price=None<span class="p">, </span>name=None<span class="p">, </span>network_interface_ids=None<span class="p">, </span>os_disk=None<span class="p">, </span>plan=None<span class="p">, </span>priority=None<span class="p">, </span>private_ip_address=None<span class="p">, </span>private_ip_addresses=None<span class="p">, </span>provision_vm_agent=None<span class="p">, </span>proximity_placement_group_id=None<span class="p">, </span>public_ip_address=None<span class="p">, </span>public_ip_addresses=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>secrets=None<span class="p">, </span>size=None<span class="p">, </span>source_image_id=None<span class="p">, </span>source_image_reference=None<span class="p">, </span>tags=None<span class="p">, </span>timezone=None<span class="p">, </span>virtual_machine_id=None<span class="p">, </span>winrm_listeners=None<span class="p">, </span>zone=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetWindowsVirtualMachine<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineState">WindowsVirtualMachineState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachine">WindowsVirtualMachine</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Compute.WindowsVirtualMachine.html">WindowsVirtualMachine</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Compute.WindowsVirtualMachineState.html">WindowsVirtualMachineState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Additional<wbr>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalcapabilities">Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Capabilities<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Unattend<wbr>Contents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalunattendcontent">List&lt;Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Unattend<wbr>Content<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `additional_unattend_content` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Extension<wbr>Operations</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinebootdiagnostics">Windows<wbr>Virtual<wbr>Machine<wbr>Boot<wbr>Diagnostics<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Computer<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the `name` field. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dedicated<wbr>Host<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Automatic<wbr>Updates</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies if Automatic Updates are Enabled for the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is `Deallocate`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineidentity">Windows<wbr>Virtual<wbr>Machine<wbr>Identity<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}An `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>License<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of on-premise license (also known as [Azure Hybrid Use Benefit](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing)) which should be used for this Virtual Machine. Possible values are `None`, `Windows_Client` and `Windows_Server`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Windows Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the `eviction_policy`. Defaults to `-1`, which means that the Virtual Machine should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Interface<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}. A list of Network Interface ID's which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineosdisk">Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineplan">Windows<wbr>Virtual<wbr>Machine<wbr>Plan<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `plan` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Primary Private IP Address assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of Private IP Addresses assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to `true`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Primary Public IP Address assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of the Public IP Addresses assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Windows Virtual Machine should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesecret">List&lt;Windows<wbr>Virtual<wbr>Machine<wbr>Secret<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The SKU which should be used for this Virtual Machine, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesourceimagereference">Windows<wbr>Virtual<wbr>Machine<wbr>Source<wbr>Image<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Time Zone which should be used by the Virtual Machine, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A 128-bit identifier which uniquely identifies this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Winrm<wbr>Listeners</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinewinrmlistener">List&lt;Windows<wbr>Virtual<wbr>Machine<wbr>Winrm<wbr>Listener<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `winrm_listener` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalcapabilities">*Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Capabilities</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Unattend<wbr>Contents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalunattendcontent">[]Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Unattend<wbr>Content</a></span>
    </dt>
    <dd>{{% md %}}One or more `additional_unattend_content` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Extension<wbr>Operations</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinebootdiagnostics">*Windows<wbr>Virtual<wbr>Machine<wbr>Boot<wbr>Diagnostics</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Computer<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the `name` field. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dedicated<wbr>Host<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Automatic<wbr>Updates</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies if Automatic Updates are Enabled for the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is `Deallocate`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineidentity">*Windows<wbr>Virtual<wbr>Machine<wbr>Identity</a></span>
    </dt>
    <dd>{{% md %}}An `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>License<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the type of on-premise license (also known as [Azure Hybrid Use Benefit](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing)) which should be used for this Virtual Machine. Possible values are `None`, `Windows_Client` and `Windows_Server`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Windows Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the `eviction_policy`. Defaults to `-1`, which means that the Virtual Machine should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Interface<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}. A list of Network Interface ID's which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineosdisk">*Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}A `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineplan">*Windows<wbr>Virtual<wbr>Machine<wbr>Plan</a></span>
    </dt>
    <dd>{{% md %}}A `plan` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Primary Private IP Address assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of Private IP Addresses assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to `true`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Primary Public IP Address assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of the Public IP Addresses assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Windows Virtual Machine should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesecret">[]Windows<wbr>Virtual<wbr>Machine<wbr>Secret</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The SKU which should be used for this Virtual Machine, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesourceimagereference">*Windows<wbr>Virtual<wbr>Machine<wbr>Source<wbr>Image<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the Time Zone which should be used by the Virtual Machine, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A 128-bit identifier which uniquely identifies this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Winrm<wbr>Listeners</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinewinrmlistener">[]Windows<wbr>Virtual<wbr>Machine<wbr>Winrm<wbr>Listener</a></span>
    </dt>
    <dd>{{% md %}}One or more `winrm_listener` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>additional<wbr>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalcapabilities">Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Capabilities?</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>additional<wbr>Unattend<wbr>Contents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalunattendcontent">Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Unattend<wbr>Content[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `additional_unattend_content` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Extension<wbr>Operations</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>availability<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinebootdiagnostics">Windows<wbr>Virtual<wbr>Machine<wbr>Boot<wbr>Diagnostics?</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>computer<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the `name` field. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dedicated<wbr>Host<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Automatic<wbr>Updates</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies if Automatic Updates are Enabled for the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is `Deallocate`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineidentity">Windows<wbr>Virtual<wbr>Machine<wbr>Identity?</a></span>
    </dt>
    <dd>{{% md %}}An `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>license<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the type of on-premise license (also known as [Azure Hybrid Use Benefit](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing)) which should be used for this Virtual Machine. Possible values are `None`, `Windows_Client` and `Windows_Server`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Windows Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the `eviction_policy`. Defaults to `-1`, which means that the Virtual Machine should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Interface<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}. A list of Network Interface ID's which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineosdisk">Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk?</a></span>
    </dt>
    <dd>{{% md %}}A `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineplan">Windows<wbr>Virtual<wbr>Machine<wbr>Plan?</a></span>
    </dt>
    <dd>{{% md %}}A `plan` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Primary Private IP Address assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of Private IP Addresses assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to `true`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Primary Public IP Address assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of the Public IP Addresses assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Windows Virtual Machine should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesecret">Windows<wbr>Virtual<wbr>Machine<wbr>Secret[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The SKU which should be used for this Virtual Machine, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesourceimagereference">Windows<wbr>Virtual<wbr>Machine<wbr>Source<wbr>Image<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Time Zone which should be used by the Virtual Machine, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A 128-bit identifier which uniquely identifies this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>winrm<wbr>Listeners</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinewinrmlistener">Windows<wbr>Virtual<wbr>Machine<wbr>Winrm<wbr>Listener[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `winrm_listener` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>additional_<wbr>capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalcapabilities">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Capabilities]</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>additional_<wbr>unattend_<wbr>contents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineadditionalunattendcontent">List[Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Unattend<wbr>Content]</a></span>
    </dt>
    <dd>{{% md %}}One or more `additional_unattend_content` blocks as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>admin_<wbr>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>admin_<wbr>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>extension_<wbr>operations</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>availability_<wbr>set_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot_<wbr>diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinebootdiagnostics">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Boot<wbr>Diagnostics]</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>computer_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the `name` field. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dedicated_<wbr>host_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>automatic_<wbr>updates</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies if Automatic Updates are Enabled for the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eviction_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is `Deallocate`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineidentity">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Identity]</a></span>
    </dt>
    <dd>{{% md %}}An `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>license_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the type of on-premise license (also known as [Azure Hybrid Use Benefit](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing)) which should be used for this Virtual Machine. Possible values are `None`, `Windows_Client` and `Windows_Server`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Windows Virtual Machine should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>bid_<wbr>price</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the `eviction_policy`. Defaults to `-1`, which means that the Virtual Machine should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Windows Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>interface_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}. A list of Network Interface ID's which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>os_<wbr>disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineosdisk">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}A `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineplan">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Plan]</a></span>
    </dt>
    <dd>{{% md %}}A `plan` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Primary Private IP Address assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private_<wbr>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of Private IP Addresses assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provision_<wbr>vm_<wbr>agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to `true`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proximity_<wbr>placement_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Primary Public IP Address assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public_<wbr>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of the Public IP Addresses assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Windows Virtual Machine should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesecret">List[Windows<wbr>Virtual<wbr>Machine<wbr>Secret]</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The SKU which should be used for this Virtual Machine, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>image_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>image_<wbr>reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesourceimagereference">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Source<wbr>Image<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Time Zone which should be used by the Virtual Machine, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtual_<wbr>machine_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A 128-bit identifier which uniquely identifies this Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>winrm_<wbr>listeners</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinewinrmlistener">List[Windows<wbr>Virtual<wbr>Machine<wbr>Winrm<wbr>Listener]</a></span>
    </dt>
    <dd>{{% md %}}One or more `winrm_listener` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Capabilities</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#WindowsVirtualMachineAdditionalCapabilities">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#WindowsVirtualMachineAdditionalCapabilities">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineAdditionalCapabilitiesArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineAdditionalCapabilitiesOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ultra<wbr>Ssd<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should the capacity to enable Data Disks of the `UltraSSD_LRS` storage account type be supported on this Virtual Machine? Defaults to `false`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ultra<wbr>Ssd<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should the capacity to enable Data Disks of the `UltraSSD_LRS` storage account type be supported on this Virtual Machine? Defaults to `false`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ultra<wbr>Ssd<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should the capacity to enable Data Disks of the `UltraSSD_LRS` storage account type be supported on this Virtual Machine? Defaults to `false`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ultra<wbr>Ssd<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should the capacity to enable Data Disks of the `UltraSSD_LRS` storage account type be supported on this Virtual Machine? Defaults to `false`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Windows<wbr>Virtual<wbr>Machine<wbr>Additional<wbr>Unattend<wbr>Content</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#WindowsVirtualMachineAdditionalUnattendContent">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#WindowsVirtualMachineAdditionalUnattendContent">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineAdditionalUnattendContentArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineAdditionalUnattendContentOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The XML formatted content that is added to the unattend.xml file for the specified path and component. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Setting</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the setting to which the content applies. Possible values are `AutoLogon` and `FirstLogonCommands`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The XML formatted content that is added to the unattend.xml file for the specified path and component. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Setting</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the setting to which the content applies. Possible values are `AutoLogon` and `FirstLogonCommands`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The XML formatted content that is added to the unattend.xml file for the specified path and component. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>setting</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the setting to which the content applies. Possible values are `AutoLogon` and `FirstLogonCommands`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The XML formatted content that is added to the unattend.xml file for the specified path and component. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>setting</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the setting to which the content applies. Possible values are `AutoLogon` and `FirstLogonCommands`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Windows<wbr>Virtual<wbr>Machine<wbr>Boot<wbr>Diagnostics</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#WindowsVirtualMachineBootDiagnostics">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#WindowsVirtualMachineBootDiagnostics">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineBootDiagnosticsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineBootDiagnosticsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary/Secondary Endpoint for the Azure Storage Account which should be used to store Boot Diagnostics, including Console Output and Screenshots from the Hypervisor.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary/Secondary Endpoint for the Azure Storage Account which should be used to store Boot Diagnostics, including Console Output and Screenshots from the Hypervisor.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Account<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary/Secondary Endpoint for the Azure Storage Account which should be used to store Boot Diagnostics, including Console Output and Screenshots from the Hypervisor.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Account<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Primary/Secondary Endpoint for the Azure Storage Account which should be used to store Boot Diagnostics, including Console Output and Screenshots from the Hypervisor.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Windows<wbr>Virtual<wbr>Machine<wbr>Identity</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#WindowsVirtualMachineIdentity">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#WindowsVirtualMachineIdentity">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineIdentityArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineIdentityOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Identity<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of User Managed Identity ID's which should be assigned to the Windows Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Principal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the System Managed Service Principal.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of Managed Identity which should be assigned to the Windows Virtual Machine. Possible values are `SystemAssigned`, `UserAssigned` and `SystemAssigned, UserAssigned`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Identity<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of User Managed Identity ID's which should be assigned to the Windows Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Principal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the System Managed Service Principal.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of Managed Identity which should be assigned to the Windows Virtual Machine. Possible values are `SystemAssigned`, `UserAssigned` and `SystemAssigned, UserAssigned`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>identity<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of User Managed Identity ID's which should be assigned to the Windows Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>principal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the System Managed Service Principal.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of Managed Identity which should be assigned to the Windows Virtual Machine. Possible values are `SystemAssigned`, `UserAssigned` and `SystemAssigned, UserAssigned`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>identity<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of User Managed Identity ID's which should be assigned to the Windows Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>principal_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the System Managed Service Principal.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of Managed Identity which should be assigned to the Windows Virtual Machine. Possible values are `SystemAssigned`, `UserAssigned` and `SystemAssigned, UserAssigned`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#WindowsVirtualMachineOsDisk">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#WindowsVirtualMachineOsDisk">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineOsDiskArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineOsDiskOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Caching</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Type of Caching which should be used for the Internal OS Disk. Possible values are `None`, `ReadOnly` and `ReadWrite`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Diff<wbr>Disk<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineosdiskdiffdisksettings">Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk<wbr>Diff<wbr>Disk<wbr>Settings<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `diff_disk_settings` block as defined above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Encryption<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Disk Encryption Set which should be used to Encrypt this OS Disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine is sourced from.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name which should be used for the Internal OS Disk. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Type of Storage Account which should back this the Internal OS Disk. Possible values are `Standard_LRS`, `StandardSSD_LRS` and `Premium_LRS`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Write<wbr>Accelerator<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should Write Accelerator be Enabled for this OS Disk? Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Caching</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Type of Caching which should be used for the Internal OS Disk. Possible values are `None`, `ReadOnly` and `ReadWrite`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Diff<wbr>Disk<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineosdiskdiffdisksettings">*Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk<wbr>Diff<wbr>Disk<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}A `diff_disk_settings` block as defined above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Encryption<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Disk Encryption Set which should be used to Encrypt this OS Disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine is sourced from.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name which should be used for the Internal OS Disk. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Type of Storage Account which should back this the Internal OS Disk. Possible values are `Standard_LRS`, `StandardSSD_LRS` and `Premium_LRS`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Write<wbr>Accelerator<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should Write Accelerator be Enabled for this OS Disk? Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>caching</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Type of Caching which should be used for the Internal OS Disk. Possible values are `None`, `ReadOnly` and `ReadWrite`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>diff<wbr>Disk<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineosdiskdiffdisksettings">Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk<wbr>Diff<wbr>Disk<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}A `diff_disk_settings` block as defined above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Encryption<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Disk Encryption Set which should be used to Encrypt this OS Disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine is sourced from.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name which should be used for the Internal OS Disk. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Account<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Type of Storage Account which should back this the Internal OS Disk. Possible values are `Standard_LRS`, `StandardSSD_LRS` and `Premium_LRS`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>write<wbr>Accelerator<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should Write Accelerator be Enabled for this OS Disk? Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>caching</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Type of Caching which should be used for the Internal OS Disk. Possible values are `None`, `ReadOnly` and `ReadWrite`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>diff<wbr>Disk<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachineosdiskdiffdisksettings">Dict[Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk<wbr>Diff<wbr>Disk<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}A `diff_disk_settings` block as defined above.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk_<wbr>encryption_<wbr>set_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Disk Encryption Set which should be used to Encrypt this OS Disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk_<wbr>size_<wbr>gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine is sourced from.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name which should be used for the Internal OS Disk. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage_<wbr>account_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Type of Storage Account which should back this the Internal OS Disk. Possible values are `Standard_LRS`, `StandardSSD_LRS` and `Premium_LRS`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>write_<wbr>accelerator_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Write Accelerator be Enabled for this OS Disk? Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Windows<wbr>Virtual<wbr>Machine<wbr>Os<wbr>Disk<wbr>Diff<wbr>Disk<wbr>Settings</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#WindowsVirtualMachineOsDiskDiffDiskSettings">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#WindowsVirtualMachineOsDiskDiffDiskSettings">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineOsDiskDiffDiskSettingsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineOsDiskDiffDiskSettingsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Option</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Ephemeral Disk Settings for the OS Disk. At this time the only possible value is `Local`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Option</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Ephemeral Disk Settings for the OS Disk. At this time the only possible value is `Local`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>option</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Ephemeral Disk Settings for the OS Disk. At this time the only possible value is `Local`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>option</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Ephemeral Disk Settings for the OS Disk. At this time the only possible value is `Local`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Windows<wbr>Virtual<wbr>Machine<wbr>Plan</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#WindowsVirtualMachinePlan">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#WindowsVirtualMachinePlan">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachinePlanArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachinePlanOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Name of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Product</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Product of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Publisher</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.
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
    <dd>{{% md %}}Specifies the Name of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Product</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Product of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Publisher</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.
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
    <dd>{{% md %}}Specifies the Name of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>product</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Product of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>publisher</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.
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
    <dd>{{% md %}}Specifies the Name of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>product</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Product of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>publisher</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Windows<wbr>Virtual<wbr>Machine<wbr>Secret</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#WindowsVirtualMachineSecret">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#WindowsVirtualMachineSecret">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineSecretArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineSecretOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesecretcertificate">List&lt;Windows<wbr>Virtual<wbr>Machine<wbr>Secret<wbr>Certificate<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `certificate` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Vault<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault from which all Secrets should be sourced.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesecretcertificate">[]Windows<wbr>Virtual<wbr>Machine<wbr>Secret<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}One or more `certificate` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key<wbr>Vault<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault from which all Secrets should be sourced.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesecretcertificate">Windows<wbr>Virtual<wbr>Machine<wbr>Secret<wbr>Certificate[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `certificate` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key<wbr>Vault<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault from which all Secrets should be sourced.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsvirtualmachinesecretcertificate">List[Windows<wbr>Virtual<wbr>Machine<wbr>Secret<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}One or more `certificate` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key_<wbr>vault_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Key Vault from which all Secrets should be sourced.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Windows<wbr>Virtual<wbr>Machine<wbr>Secret<wbr>Certificate</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#WindowsVirtualMachineSecretCertificate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#WindowsVirtualMachineSecretCertificate">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineSecretCertificateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineSecretCertificateOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Store</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The certificate store on the Virtual Machine where the certificate should be added.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secret URL of a Key Vault Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Store</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The certificate store on the Virtual Machine where the certificate should be added.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secret URL of a Key Vault Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>store</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The certificate store on the Virtual Machine where the certificate should be added.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secret URL of a Key Vault Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>store</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The certificate store on the Virtual Machine where the certificate should be added.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Secret URL of a Key Vault Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Windows<wbr>Virtual<wbr>Machine<wbr>Source<wbr>Image<wbr>Reference</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#WindowsVirtualMachineSourceImageReference">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#WindowsVirtualMachineSourceImageReference">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineSourceImageReferenceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineSourceImageReferenceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Offer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Publisher</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Version</span>
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
        <span>Offer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Publisher</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Version</span>
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
        <span>offer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>publisher</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>version</span>
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
        <span>offer</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>publisher</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Windows<wbr>Virtual<wbr>Machine<wbr>Winrm<wbr>Listener</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#WindowsVirtualMachineWinrmListener">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#WindowsVirtualMachineWinrmListener">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineWinrmListenerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#WindowsVirtualMachineWinrmListenerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Certificate<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Secret URL of a Key Vault Certificate, which must be specified when `protocol` is set to `Https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Certificate<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Secret URL of a Key Vault Certificate, which must be specified when `protocol` is set to `Https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>certificate<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Secret URL of a Key Vault Certificate, which must be specified when `protocol` is set to `Https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>certificate<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Secret URL of a Key Vault Certificate, which must be specified when `protocol` is set to `Https`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-azure">https://github.com/pulumi/pulumi-azure</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

