
---
title: "LinuxVirtualMachineScaleSet"
block_external_search_index: true
---



Manages a Linux Virtual Machine Scale Set.

## Disclaimers

> **Note** This provider will automatically update & reimage the nodes in the Scale Set (if Required) during an Update - this behaviour can be configured using the `features` configuration within the Provider configuration block.

> **Note:** This resource does not support Unmanaged Disks. If you need to use Unmanaged Disks you can continue to use the `azure.compute.ScaleSet` resource instead

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/linux_virtual_machine_scale_set.html.markdown.



## Create a LinuxVirtualMachineScaleSet Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/compute/#LinuxVirtualMachineScaleSet">LinuxVirtualMachineScaleSet</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/compute/#LinuxVirtualMachineScaleSetArgs">LinuxVirtualMachineScaleSetArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">LinuxVirtualMachineScaleSet</span><span class="p">(resource_name, opts=None, </span>additional_capabilities=None<span class="p">, </span>admin_password=None<span class="p">, </span>admin_ssh_keys=None<span class="p">, </span>admin_username=None<span class="p">, </span>automatic_os_upgrade_policy=None<span class="p">, </span>boot_diagnostics=None<span class="p">, </span>computer_name_prefix=None<span class="p">, </span>custom_data=None<span class="p">, </span>data_disks=None<span class="p">, </span>disable_password_authentication=None<span class="p">, </span>do_not_run_extensions_on_overprovisioned_machines=None<span class="p">, </span>eviction_policy=None<span class="p">, </span>health_probe_id=None<span class="p">, </span>identity=None<span class="p">, </span>instances=None<span class="p">, </span>location=None<span class="p">, </span>max_bid_price=None<span class="p">, </span>name=None<span class="p">, </span>network_interfaces=None<span class="p">, </span>os_disk=None<span class="p">, </span>overprovision=None<span class="p">, </span>plan=None<span class="p">, </span>priority=None<span class="p">, </span>provision_vm_agent=None<span class="p">, </span>proximity_placement_group_id=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>rolling_upgrade_policy=None<span class="p">, </span>scale_in_policy=None<span class="p">, </span>secrets=None<span class="p">, </span>single_placement_group=None<span class="p">, </span>sku=None<span class="p">, </span>source_image_id=None<span class="p">, </span>source_image_reference=None<span class="p">, </span>tags=None<span class="p">, </span>terminate_notification=None<span class="p">, </span>upgrade_mode=None<span class="p">, </span>zone_balance=None<span class="p">, </span>zones=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewLinuxVirtualMachineScaleSet<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetArgs">LinuxVirtualMachineScaleSetArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSet">LinuxVirtualMachineScaleSet</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Compute.LinuxVirtualMachineScaleSet.html">LinuxVirtualMachineScaleSet</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Compute.LinuxVirtualMachineScaleSetArgs.html">LinuxVirtualMachineScaleSetArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadditionalcapabilities">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Additional<wbr>Capabilities<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
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
        <span>Admin<wbr>Ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadminsshkey">List&lt;Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Admin<wbr>Ssh<wbr>Key<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `admin_ssh_key` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetautomaticosupgradepolicy">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `automatic_os_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetbootdiagnostics">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Boot<wbr>Diagnostics<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Computer<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the `name` field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Data<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetdatadisk">List&lt;Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Data<wbr>Disk<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `data_disk` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Password<wbr>Authentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should Password Authentication be disabled on this Virtual Machine Scale Set? Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Do<wbr>Not<wbr>Run<wbr>Extensions<wbr>On<wbr>Overprovisioned<wbr>Machines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Probe<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetidentity">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Identity<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of Virtual Machines in the Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Linux Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the `eviction_policy`. Defaults to `-1`, which means that each Virtual Machine in this Scale Set should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterface">List&lt;Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `network_interface` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetosdisk">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}An `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Overprovision</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You're not billed for these over-provisioned VM's and they don't count towards the Subscription Quota. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetplan">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Plan<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Priority of this Virtual Machine Scale Set. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this value forces a new resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to `true`. Changing this value forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Linux Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rolling<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetrollingupgradepolicy">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Rolling<wbr>Upgrade<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `rolling_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scale<wbr>In<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are `Default`, `NewestVM` and `OldestVM`, defaults to `Default`. For more information about scale in policy, please [refer to this doc](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsecret">List&lt;Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Single<wbr>Placement<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Virtual Machine SKU for the Scale Set, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of an Image which each Virtual Machine in this Scale Set should be based on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsourceimagereference">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Source<wbr>Image<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Terminate<wbr>Notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetterminatenotification">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Terminate<wbr>Notification<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `terminate_notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are `Automatic`, `Manual` and `Rolling`. Defaults to `Manual`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone<wbr>Balance</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to `false`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadditionalcapabilities">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Additional<wbr>Capabilities</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
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
        <span>Admin<wbr>Ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadminsshkey">[]Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Admin<wbr>Ssh<wbr>Key</a></span>
    </dt>
    <dd>{{% md %}}One or more `admin_ssh_key` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetautomaticosupgradepolicy">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `automatic_os_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetbootdiagnostics">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Boot<wbr>Diagnostics</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Computer<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the `name` field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Data<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetdatadisk">[]Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Data<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}One or more `data_disk` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Password<wbr>Authentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should Password Authentication be disabled on this Virtual Machine Scale Set? Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Do<wbr>Not<wbr>Run<wbr>Extensions<wbr>On<wbr>Overprovisioned<wbr>Machines</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Probe<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetidentity">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Identity</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of Virtual Machines in the Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Linux Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the `eviction_policy`. Defaults to `-1`, which means that each Virtual Machine in this Scale Set should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterface">[]Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface</a></span>
    </dt>
    <dd>{{% md %}}One or more `network_interface` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetosdisk">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}An `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Overprovision</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You're not billed for these over-provisioned VM's and they don't count towards the Subscription Quota. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetplan">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Plan</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Priority of this Virtual Machine Scale Set. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this value forces a new resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to `true`. Changing this value forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Linux Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rolling<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetrollingupgradepolicy">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Rolling<wbr>Upgrade<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `rolling_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scale<wbr>In<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are `Default`, `NewestVM` and `OldestVM`, defaults to `Default`. For more information about scale in policy, please [refer to this doc](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsecret">[]Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Single<wbr>Placement<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Virtual Machine SKU for the Scale Set, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of an Image which each Virtual Machine in this Scale Set should be based on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsourceimagereference">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Source<wbr>Image<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Terminate<wbr>Notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetterminatenotification">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Terminate<wbr>Notification</a></span>
    </dt>
    <dd>{{% md %}}A `terminate_notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are `Automatic`, `Manual` and `Rolling`. Defaults to `Manual`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone<wbr>Balance</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to `false`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>additional<wbr>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadditionalcapabilities">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Additional<wbr>Capabilities?</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
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
        <span>admin<wbr>Ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadminsshkey">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Admin<wbr>Ssh<wbr>Key[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `admin_ssh_key` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>automatic<wbr>Os<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetautomaticosupgradepolicy">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `automatic_os_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetbootdiagnostics">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Boot<wbr>Diagnostics?</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>computer<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the `name` field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>data<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetdatadisk">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Data<wbr>Disk[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `data_disk` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable<wbr>Password<wbr>Authentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should Password Authentication be disabled on this Virtual Machine Scale Set? Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>do<wbr>Not<wbr>Run<wbr>Extensions<wbr>On<wbr>Overprovisioned<wbr>Machines</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health<wbr>Probe<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetidentity">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Identity?</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of Virtual Machines in the Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Linux Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the `eviction_policy`. Defaults to `-1`, which means that each Virtual Machine in this Scale Set should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterface">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `network_interface` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetosdisk">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}An `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>overprovision</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You're not billed for these over-provisioned VM's and they don't count towards the Subscription Quota. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetplan">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Plan?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Priority of this Virtual Machine Scale Set. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this value forces a new resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to `true`. Changing this value forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Linux Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rolling<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetrollingupgradepolicy">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Rolling<wbr>Upgrade<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `rolling_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scale<wbr>In<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are `Default`, `NewestVM` and `OldestVM`, defaults to `Default`. For more information about scale in policy, please [refer to this doc](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsecret">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>single<wbr>Placement<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Virtual Machine SKU for the Scale Set, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of an Image which each Virtual Machine in this Scale Set should be based on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsourceimagereference">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Source<wbr>Image<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>terminate<wbr>Notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetterminatenotification">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Terminate<wbr>Notification?</a></span>
    </dt>
    <dd>{{% md %}}A `terminate_notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are `Automatic`, `Manual` and `Rolling`. Defaults to `Manual`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone<wbr>Balance</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to `false`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>additional_<wbr>capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadditionalcapabilities">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Additional<wbr>Capabilities]</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
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
        <span>admin_<wbr>ssh_<wbr>keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadminsshkey">List[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Admin<wbr>Ssh<wbr>Key]</a></span>
    </dt>
    <dd>{{% md %}}One or more `admin_ssh_key` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>admin_<wbr>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>automatic_<wbr>os_<wbr>upgrade_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetautomaticosupgradepolicy">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A `automatic_os_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot_<wbr>diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetbootdiagnostics">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Boot<wbr>Diagnostics]</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>computer_<wbr>name_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the `name` field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>data_<wbr>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetdatadisk">List[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Data<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}One or more `data_disk` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable_<wbr>password_<wbr>authentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Password Authentication be disabled on this Virtual Machine Scale Set? Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>do_<wbr>not_<wbr>run_<wbr>extensions_<wbr>on_<wbr>overprovisioned_<wbr>machines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eviction_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health_<wbr>probe_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetidentity">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Identity]</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of Virtual Machines in the Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Linux Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>bid_<wbr>price</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the `eviction_policy`. Defaults to `-1`, which means that each Virtual Machine in this Scale Set should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network_<wbr>interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterface">List[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface]</a></span>
    </dt>
    <dd>{{% md %}}One or more `network_interface` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>os_<wbr>disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetosdisk">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}An `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>overprovision</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You're not billed for these over-provisioned VM's and they don't count towards the Subscription Quota. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetplan">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Plan]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Priority of this Virtual Machine Scale Set. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this value forces a new resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provision_<wbr>vm_<wbr>agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to `true`. Changing this value forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proximity_<wbr>placement_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Linux Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rolling_<wbr>upgrade_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetrollingupgradepolicy">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Rolling<wbr>Upgrade<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A `rolling_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scale_<wbr>in_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are `Default`, `NewestVM` and `OldestVM`, defaults to `Default`. For more information about scale in policy, please [refer to this doc](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsecret">List[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret]</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>single_<wbr>placement_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Virtual Machine SKU for the Scale Set, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>image_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of an Image which each Virtual Machine in this Scale Set should be based on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>image_<wbr>reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsourceimagereference">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Source<wbr>Image<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>terminate_<wbr>notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetterminatenotification">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Terminate<wbr>Notification]</a></span>
    </dt>
    <dd>{{% md %}}A `terminate_notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>upgrade_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are `Automatic`, `Manual` and `Rolling`. Defaults to `Manual`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone_<wbr>balance</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to `false`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## LinuxVirtualMachineScaleSet Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Additional<wbr>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadditionalcapabilities">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Additional<wbr>Capabilities?</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Admin<wbr>Ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadminsshkey">List&lt;Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Admin<wbr>Ssh<wbr>Key&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `admin_ssh_key` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetautomaticosupgradepolicy">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `automatic_os_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetbootdiagnostics">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Boot<wbr>Diagnostics?</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Computer<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the `name` field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Data<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetdatadisk">List&lt;Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Data<wbr>Disk&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `data_disk` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disable<wbr>Password<wbr>Authentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should Password Authentication be disabled on this Virtual Machine Scale Set? Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Do<wbr>Not<wbr>Run<wbr>Extensions<wbr>On<wbr>Overprovisioned<wbr>Machines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Health<wbr>Probe<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetidentity">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Identity?</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of Virtual Machines in the Scale Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Linux Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the `eviction_policy`. Defaults to `-1`, which means that each Virtual Machine in this Scale Set should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterface">List&lt;Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `network_interface` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetosdisk">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}An `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Overprovision</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You're not billed for these over-provisioned VM's and they don't count towards the Subscription Quota. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetplan">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Plan?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Priority of this Virtual Machine Scale Set. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this value forces a new resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to `true`. Changing this value forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Linux Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Rolling<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetrollingupgradepolicy">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Rolling<wbr>Upgrade<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `rolling_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scale<wbr>In<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are `Default`, `NewestVM` and `OldestVM`, defaults to `Default`. For more information about scale in policy, please [refer to this doc](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsecret">List&lt;Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Single<wbr>Placement<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Virtual Machine SKU for the Scale Set, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of an Image which each Virtual Machine in this Scale Set should be based on.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsourceimagereference">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Source<wbr>Image<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Terminate<wbr>Notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetterminatenotification">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Terminate<wbr>Notification</a></span>
    </dt>
    <dd>{{% md %}}A `terminate_notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Unique<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Unique ID for this Linux Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are `Automatic`, `Manual` and `Rolling`. Defaults to `Manual`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone<wbr>Balance</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to `false`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Additional<wbr>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadditionalcapabilities">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Additional<wbr>Capabilities</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Admin<wbr>Ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadminsshkey">[]Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Admin<wbr>Ssh<wbr>Key</a></span>
    </dt>
    <dd>{{% md %}}One or more `admin_ssh_key` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetautomaticosupgradepolicy">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `automatic_os_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetbootdiagnostics">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Boot<wbr>Diagnostics</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Computer<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the `name` field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Data<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetdatadisk">[]Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Data<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}One or more `data_disk` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disable<wbr>Password<wbr>Authentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should Password Authentication be disabled on this Virtual Machine Scale Set? Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Do<wbr>Not<wbr>Run<wbr>Extensions<wbr>On<wbr>Overprovisioned<wbr>Machines</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Health<wbr>Probe<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetidentity">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Identity</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of Virtual Machines in the Scale Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Linux Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the `eviction_policy`. Defaults to `-1`, which means that each Virtual Machine in this Scale Set should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterface">[]Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface</a></span>
    </dt>
    <dd>{{% md %}}One or more `network_interface` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetosdisk">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}An `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Overprovision</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You're not billed for these over-provisioned VM's and they don't count towards the Subscription Quota. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetplan">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Plan</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Priority of this Virtual Machine Scale Set. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this value forces a new resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to `true`. Changing this value forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Linux Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Rolling<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetrollingupgradepolicy">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Rolling<wbr>Upgrade<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `rolling_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scale<wbr>In<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are `Default`, `NewestVM` and `OldestVM`, defaults to `Default`. For more information about scale in policy, please [refer to this doc](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsecret">[]Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Single<wbr>Placement<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Virtual Machine SKU for the Scale Set, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of an Image which each Virtual Machine in this Scale Set should be based on.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsourceimagereference">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Source<wbr>Image<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Terminate<wbr>Notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetterminatenotification">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Terminate<wbr>Notification</a></span>
    </dt>
    <dd>{{% md %}}A `terminate_notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Unique<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Unique ID for this Linux Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are `Automatic`, `Manual` and `Rolling`. Defaults to `Manual`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone<wbr>Balance</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to `false`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>additional<wbr>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadditionalcapabilities">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Additional<wbr>Capabilities?</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>admin<wbr>Ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadminsshkey">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Admin<wbr>Ssh<wbr>Key[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `admin_ssh_key` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>automatic<wbr>Os<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetautomaticosupgradepolicy">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `automatic_os_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetbootdiagnostics">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Boot<wbr>Diagnostics?</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>computer<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the `name` field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>data<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetdatadisk">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Data<wbr>Disk[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `data_disk` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disable<wbr>Password<wbr>Authentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should Password Authentication be disabled on this Virtual Machine Scale Set? Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>do<wbr>Not<wbr>Run<wbr>Extensions<wbr>On<wbr>Overprovisioned<wbr>Machines</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>health<wbr>Probe<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetidentity">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Identity?</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of Virtual Machines in the Scale Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Linux Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the `eviction_policy`. Defaults to `-1`, which means that each Virtual Machine in this Scale Set should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterface">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `network_interface` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetosdisk">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}An `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>overprovision</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You're not billed for these over-provisioned VM's and they don't count towards the Subscription Quota. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetplan">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Plan?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Priority of this Virtual Machine Scale Set. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this value forces a new resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to `true`. Changing this value forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Linux Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>rolling<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetrollingupgradepolicy">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Rolling<wbr>Upgrade<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `rolling_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scale<wbr>In<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are `Default`, `NewestVM` and `OldestVM`, defaults to `Default`. For more information about scale in policy, please [refer to this doc](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsecret">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>single<wbr>Placement<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Virtual Machine SKU for the Scale Set, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of an Image which each Virtual Machine in this Scale Set should be based on.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsourceimagereference">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Source<wbr>Image<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>terminate<wbr>Notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetterminatenotification">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Terminate<wbr>Notification</a></span>
    </dt>
    <dd>{{% md %}}A `terminate_notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>unique<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Unique ID for this Linux Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are `Automatic`, `Manual` and `Rolling`. Defaults to `Manual`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone<wbr>Balance</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to `false`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>additional_<wbr>capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadditionalcapabilities">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Additional<wbr>Capabilities]</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
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
        <span>admin_<wbr>ssh_<wbr>keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadminsshkey">List[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Admin<wbr>Ssh<wbr>Key]</a></span>
    </dt>
    <dd>{{% md %}}One or more `admin_ssh_key` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>admin_<wbr>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>automatic_<wbr>os_<wbr>upgrade_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetautomaticosupgradepolicy">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A `automatic_os_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>boot_<wbr>diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetbootdiagnostics">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Boot<wbr>Diagnostics]</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>computer_<wbr>name_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the `name` field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>data_<wbr>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetdatadisk">List[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Data<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}One or more `data_disk` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disable_<wbr>password_<wbr>authentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Password Authentication be disabled on this Virtual Machine Scale Set? Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>do_<wbr>not_<wbr>run_<wbr>extensions_<wbr>on_<wbr>overprovisioned_<wbr>machines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>eviction_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>health_<wbr>probe_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetidentity">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Identity]</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of Virtual Machines in the Scale Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Linux Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max_<wbr>bid_<wbr>price</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the `eviction_policy`. Defaults to `-1`, which means that each Virtual Machine in this Scale Set should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterface">List[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface]</a></span>
    </dt>
    <dd>{{% md %}}One or more `network_interface` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>os_<wbr>disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetosdisk">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}An `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>overprovision</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You're not billed for these over-provisioned VM's and they don't count towards the Subscription Quota. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetplan">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Plan]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Priority of this Virtual Machine Scale Set. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this value forces a new resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>provision_<wbr>vm_<wbr>agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to `true`. Changing this value forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>proximity_<wbr>placement_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Linux Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>rolling_<wbr>upgrade_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetrollingupgradepolicy">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Rolling<wbr>Upgrade<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A `rolling_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scale_<wbr>in_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are `Default`, `NewestVM` and `OldestVM`, defaults to `Default`. For more information about scale in policy, please [refer to this doc](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsecret">List[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret]</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>single_<wbr>placement_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Virtual Machine SKU for the Scale Set, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source_<wbr>image_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of an Image which each Virtual Machine in this Scale Set should be based on.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source_<wbr>image_<wbr>reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsourceimagereference">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Source<wbr>Image<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>terminate_<wbr>notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetterminatenotification">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Terminate<wbr>Notification]</a></span>
    </dt>
    <dd>{{% md %}}A `terminate_notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>unique_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Unique ID for this Linux Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>upgrade_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are `Automatic`, `Manual` and `Rolling`. Defaults to `Manual`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone_<wbr>balance</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to `false`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing LinuxVirtualMachineScaleSet Resource

Get an existing LinuxVirtualMachineScaleSet resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/compute/#LinuxVirtualMachineScaleSetState">LinuxVirtualMachineScaleSetState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/compute/#LinuxVirtualMachineScaleSet">LinuxVirtualMachineScaleSet</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>additional_capabilities=None<span class="p">, </span>admin_password=None<span class="p">, </span>admin_ssh_keys=None<span class="p">, </span>admin_username=None<span class="p">, </span>automatic_os_upgrade_policy=None<span class="p">, </span>boot_diagnostics=None<span class="p">, </span>computer_name_prefix=None<span class="p">, </span>custom_data=None<span class="p">, </span>data_disks=None<span class="p">, </span>disable_password_authentication=None<span class="p">, </span>do_not_run_extensions_on_overprovisioned_machines=None<span class="p">, </span>eviction_policy=None<span class="p">, </span>health_probe_id=None<span class="p">, </span>identity=None<span class="p">, </span>instances=None<span class="p">, </span>location=None<span class="p">, </span>max_bid_price=None<span class="p">, </span>name=None<span class="p">, </span>network_interfaces=None<span class="p">, </span>os_disk=None<span class="p">, </span>overprovision=None<span class="p">, </span>plan=None<span class="p">, </span>priority=None<span class="p">, </span>provision_vm_agent=None<span class="p">, </span>proximity_placement_group_id=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>rolling_upgrade_policy=None<span class="p">, </span>scale_in_policy=None<span class="p">, </span>secrets=None<span class="p">, </span>single_placement_group=None<span class="p">, </span>sku=None<span class="p">, </span>source_image_id=None<span class="p">, </span>source_image_reference=None<span class="p">, </span>tags=None<span class="p">, </span>terminate_notification=None<span class="p">, </span>unique_id=None<span class="p">, </span>upgrade_mode=None<span class="p">, </span>zone_balance=None<span class="p">, </span>zones=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetLinuxVirtualMachineScaleSet<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetState">LinuxVirtualMachineScaleSetState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSet">LinuxVirtualMachineScaleSet</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Compute.LinuxVirtualMachineScaleSet.html">LinuxVirtualMachineScaleSet</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Compute.LinuxVirtualMachineScaleSetState.html">LinuxVirtualMachineScaleSetState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadditionalcapabilities">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Additional<wbr>Capabilities<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
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
        <span>Admin<wbr>Ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadminsshkey">List&lt;Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Admin<wbr>Ssh<wbr>Key<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `admin_ssh_key` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetautomaticosupgradepolicy">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `automatic_os_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetbootdiagnostics">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Boot<wbr>Diagnostics<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Computer<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the `name` field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Data<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetdatadisk">List&lt;Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Data<wbr>Disk<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `data_disk` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Password<wbr>Authentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should Password Authentication be disabled on this Virtual Machine Scale Set? Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Do<wbr>Not<wbr>Run<wbr>Extensions<wbr>On<wbr>Overprovisioned<wbr>Machines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Probe<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetidentity">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Identity<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of Virtual Machines in the Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Linux Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the `eviction_policy`. Defaults to `-1`, which means that each Virtual Machine in this Scale Set should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterface">List&lt;Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `network_interface` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetosdisk">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}An `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Overprovision</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You're not billed for these over-provisioned VM's and they don't count towards the Subscription Quota. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetplan">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Plan<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Priority of this Virtual Machine Scale Set. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this value forces a new resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to `true`. Changing this value forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Linux Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rolling<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetrollingupgradepolicy">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Rolling<wbr>Upgrade<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `rolling_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scale<wbr>In<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are `Default`, `NewestVM` and `OldestVM`, defaults to `Default`. For more information about scale in policy, please [refer to this doc](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsecret">List&lt;Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Single<wbr>Placement<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Virtual Machine SKU for the Scale Set, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of an Image which each Virtual Machine in this Scale Set should be based on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsourceimagereference">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Source<wbr>Image<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Terminate<wbr>Notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetterminatenotification">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Terminate<wbr>Notification<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `terminate_notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unique<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Unique ID for this Linux Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are `Automatic`, `Manual` and `Rolling`. Defaults to `Manual`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone<wbr>Balance</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to `false`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadditionalcapabilities">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Additional<wbr>Capabilities</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
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
        <span>Admin<wbr>Ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadminsshkey">[]Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Admin<wbr>Ssh<wbr>Key</a></span>
    </dt>
    <dd>{{% md %}}One or more `admin_ssh_key` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetautomaticosupgradepolicy">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `automatic_os_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetbootdiagnostics">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Boot<wbr>Diagnostics</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Computer<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the `name` field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Data<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetdatadisk">[]Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Data<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}One or more `data_disk` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Password<wbr>Authentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should Password Authentication be disabled on this Virtual Machine Scale Set? Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Do<wbr>Not<wbr>Run<wbr>Extensions<wbr>On<wbr>Overprovisioned<wbr>Machines</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Probe<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetidentity">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Identity</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of Virtual Machines in the Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Linux Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the `eviction_policy`. Defaults to `-1`, which means that each Virtual Machine in this Scale Set should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterface">[]Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface</a></span>
    </dt>
    <dd>{{% md %}}One or more `network_interface` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetosdisk">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}An `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Overprovision</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You're not billed for these over-provisioned VM's and they don't count towards the Subscription Quota. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetplan">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Plan</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Priority of this Virtual Machine Scale Set. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this value forces a new resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to `true`. Changing this value forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Linux Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rolling<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetrollingupgradepolicy">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Rolling<wbr>Upgrade<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `rolling_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scale<wbr>In<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are `Default`, `NewestVM` and `OldestVM`, defaults to `Default`. For more information about scale in policy, please [refer to this doc](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsecret">[]Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Single<wbr>Placement<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Virtual Machine SKU for the Scale Set, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of an Image which each Virtual Machine in this Scale Set should be based on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsourceimagereference">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Source<wbr>Image<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Terminate<wbr>Notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetterminatenotification">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Terminate<wbr>Notification</a></span>
    </dt>
    <dd>{{% md %}}A `terminate_notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unique<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Unique ID for this Linux Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are `Automatic`, `Manual` and `Rolling`. Defaults to `Manual`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone<wbr>Balance</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to `false`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>additional<wbr>Capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadditionalcapabilities">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Additional<wbr>Capabilities?</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
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
        <span>admin<wbr>Ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadminsshkey">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Admin<wbr>Ssh<wbr>Key[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `admin_ssh_key` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>automatic<wbr>Os<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetautomaticosupgradepolicy">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `automatic_os_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetbootdiagnostics">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Boot<wbr>Diagnostics?</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>computer<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the `name` field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>data<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetdatadisk">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Data<wbr>Disk[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `data_disk` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable<wbr>Password<wbr>Authentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should Password Authentication be disabled on this Virtual Machine Scale Set? Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>do<wbr>Not<wbr>Run<wbr>Extensions<wbr>On<wbr>Overprovisioned<wbr>Machines</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eviction<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health<wbr>Probe<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetidentity">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Identity?</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of Virtual Machines in the Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Linux Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Bid<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the `eviction_policy`. Defaults to `-1`, which means that each Virtual Machine in this Scale Set should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterface">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `network_interface` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>os<wbr>Disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetosdisk">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk?</a></span>
    </dt>
    <dd>{{% md %}}An `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>overprovision</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You're not billed for these over-provisioned VM's and they don't count towards the Subscription Quota. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetplan">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Plan?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Priority of this Virtual Machine Scale Set. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this value forces a new resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provision<wbr>Vm<wbr>Agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to `true`. Changing this value forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proximity<wbr>Placement<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Linux Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rolling<wbr>Upgrade<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetrollingupgradepolicy">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Rolling<wbr>Upgrade<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `rolling_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scale<wbr>In<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are `Default`, `NewestVM` and `OldestVM`, defaults to `Default`. For more information about scale in policy, please [refer to this doc](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsecret">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>single<wbr>Placement<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Virtual Machine SKU for the Scale Set, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of an Image which each Virtual Machine in this Scale Set should be based on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Image<wbr>Reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsourceimagereference">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Source<wbr>Image<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>terminate<wbr>Notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetterminatenotification">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Terminate<wbr>Notification?</a></span>
    </dt>
    <dd>{{% md %}}A `terminate_notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unique<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Unique ID for this Linux Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>upgrade<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are `Automatic`, `Manual` and `Rolling`. Defaults to `Manual`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone<wbr>Balance</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to `false`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>additional_<wbr>capabilities</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadditionalcapabilities">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Additional<wbr>Capabilities]</a></span>
    </dt>
    <dd>{{% md %}}A `additional_capabilities` block as defined below.
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
        <span>admin_<wbr>ssh_<wbr>keys</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetadminsshkey">List[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Admin<wbr>Ssh<wbr>Key]</a></span>
    </dt>
    <dd>{{% md %}}One or more `admin_ssh_key` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>admin_<wbr>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>automatic_<wbr>os_<wbr>upgrade_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetautomaticosupgradepolicy">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A `automatic_os_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot_<wbr>diagnostics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetbootdiagnostics">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Boot<wbr>Diagnostics]</a></span>
    </dt>
    <dd>{{% md %}}A `boot_diagnostics` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>computer_<wbr>name_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the `name` field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>data_<wbr>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetdatadisk">List[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Data<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}One or more `data_disk` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable_<wbr>password_<wbr>authentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Password Authentication be disabled on this Virtual Machine Scale Set? Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>do_<wbr>not_<wbr>run_<wbr>extensions_<wbr>on_<wbr>overprovisioned_<wbr>machines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eviction_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health_<wbr>probe_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetidentity">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Identity]</a></span>
    </dt>
    <dd>{{% md %}}A `identity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of Virtual Machines in the Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Azure location where the Linux Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>bid_<wbr>price</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum price you're willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the `eviction_policy`. Defaults to `-1`, which means that each Virtual Machine in this Scale Set should not be evicted for price reasons.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterface">List[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface]</a></span>
    </dt>
    <dd>{{% md %}}One or more `network_interface` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>os_<wbr>disk</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetosdisk">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}An `os_disk` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>overprovision</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You're not billed for these over-provisioned VM's and they don't count towards the Subscription Quota. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetplan">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Plan]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Priority of this Virtual Machine Scale Set. Possible values are `Regular` and `Spot`. Defaults to `Regular`. Changing this value forces a new resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provision_<wbr>vm_<wbr>agent</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to `true`. Changing this value forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>proximity_<wbr>placement_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in which the Linux Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rolling_<wbr>upgrade_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetrollingupgradepolicy">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Rolling<wbr>Upgrade<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A `rolling_upgrade_policy` block as defined below. This is Required and can only be specified when `upgrade_mode` is set to `Automatic` or `Rolling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scale_<wbr>in_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are `Default`, `NewestVM` and `OldestVM`, defaults to `Default`. For more information about scale in policy, please [refer to this doc](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secrets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsecret">List[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret]</a></span>
    </dt>
    <dd>{{% md %}}One or more `secret` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>single_<wbr>placement_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Virtual Machine SKU for the Scale Set, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>image_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of an Image which each Virtual Machine in this Scale Set should be based on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>image_<wbr>reference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsourceimagereference">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Source<wbr>Image<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}A `source_image_reference` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags which should be assigned to this Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>terminate_<wbr>notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetterminatenotification">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Terminate<wbr>Notification]</a></span>
    </dt>
    <dd>{{% md %}}A `terminate_notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unique_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Unique ID for this Linux Virtual Machine Scale Set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>upgrade_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are `Automatic`, `Manual` and `Rolling`. Defaults to `Manual`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone_<wbr>balance</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to `false`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Additional<wbr>Capabilities</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetAdditionalCapabilities">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetAdditionalCapabilities">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetAdditionalCapabilitiesArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetAdditionalCapabilitiesOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ultra<wbr>Ssd<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should the capacity to enable Data Disks of the `UltraSSD_LRS` storage account type be supported on this Virtual Machine Scale Set? Defaults to `false`. Changing this forces a new resource to be created.
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
    <dd>{{% md %}}Should the capacity to enable Data Disks of the `UltraSSD_LRS` storage account type be supported on this Virtual Machine Scale Set? Defaults to `false`. Changing this forces a new resource to be created.
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
    <dd>{{% md %}}Should the capacity to enable Data Disks of the `UltraSSD_LRS` storage account type be supported on this Virtual Machine Scale Set? Defaults to `false`. Changing this forces a new resource to be created.
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
    <dd>{{% md %}}Should the capacity to enable Data Disks of the `UltraSSD_LRS` storage account type be supported on this Virtual Machine Scale Set? Defaults to `false`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Admin<wbr>Ssh<wbr>Key</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetAdminSshKey">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetAdminSshKey">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetAdminSshKeyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetAdminSshKeyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Public Key which should be used for authentication, which needs to be at least 2048-bit and in `ssh-rsa` format.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Username for which this Public SSH Key should be configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Public Key which should be used for authentication, which needs to be at least 2048-bit and in `ssh-rsa` format.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Username for which this Public SSH Key should be configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>public<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Public Key which should be used for authentication, which needs to be at least 2048-bit and in `ssh-rsa` format.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Username for which this Public SSH Key should be configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>public<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Public Key which should be used for authentication, which needs to be at least 2048-bit and in `ssh-rsa` format.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Username for which this Public SSH Key should be configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Automatic<wbr>Os<wbr>Upgrade<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Disable<wbr>Automatic<wbr>Rollback</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should automatic rollbacks be disabled? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enable<wbr>Automatic<wbr>Os<wbr>Upgrade</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should OS Upgrades automatically be applied to Scale Set instances in a rolling fashion when a newer version of the OS Image becomes available? Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Disable<wbr>Automatic<wbr>Rollback</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should automatic rollbacks be disabled? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enable<wbr>Automatic<wbr>Os<wbr>Upgrade</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should OS Upgrades automatically be applied to Scale Set instances in a rolling fashion when a newer version of the OS Image becomes available? Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>disable<wbr>Automatic<wbr>Rollback</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Should automatic rollbacks be disabled? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enable<wbr>Automatic<wbr>Os<wbr>Upgrade</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Should OS Upgrades automatically be applied to Scale Set instances in a rolling fashion when a newer version of the OS Image becomes available? Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>disable<wbr>Automatic<wbr>Rollback</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should automatic rollbacks be disabled? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enable<wbr>Automatic<wbr>Os<wbr>Upgrade</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should OS Upgrades automatically be applied to Scale Set instances in a rolling fashion when a newer version of the OS Image becomes available? Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Boot<wbr>Diagnostics</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetBootDiagnostics">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetBootDiagnostics">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetBootDiagnosticsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetBootDiagnosticsOutput">output</a> API doc for this type.
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





<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Data<wbr>Disk</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetDataDisk">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetDataDisk">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetDataDiskArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetDataDiskOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Caching</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of Caching which should be used for this Data Disk. Possible values are `None`, `ReadOnly` and `ReadWrite`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Encryption<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Disk Encryption Set which should be used to encrypt this Data Disk.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The size of the Data Disk which should be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Lun</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Logical Unit Number of the Data Disk, which must be unique within the Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Type of Storage Account which should back this Data Disk. Possible values include `Standard_LRS`, `StandardSSD_LRS`, `Premium_LRS` and `UltraSSD_LRS`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Write<wbr>Accelerator<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should Write Accelerator be enabled for this Data Disk? Defaults to `false`.
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
    <dd>{{% md %}}The type of Caching which should be used for this Data Disk. Possible values are `None`, `ReadOnly` and `ReadWrite`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Encryption<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Disk Encryption Set which should be used to encrypt this Data Disk.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The size of the Data Disk which should be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Lun</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Logical Unit Number of the Data Disk, which must be unique within the Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Type of Storage Account which should back this Data Disk. Possible values include `Standard_LRS`, `StandardSSD_LRS`, `Premium_LRS` and `UltraSSD_LRS`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Write<wbr>Accelerator<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should Write Accelerator be enabled for this Data Disk? Defaults to `false`.
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
    <dd>{{% md %}}The type of Caching which should be used for this Data Disk. Possible values are `None`, `ReadOnly` and `ReadWrite`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Encryption<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Disk Encryption Set which should be used to encrypt this Data Disk.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The size of the Data Disk which should be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>lun</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The Logical Unit Number of the Data Disk, which must be unique within the Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Account<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Type of Storage Account which should back this Data Disk. Possible values include `Standard_LRS`, `StandardSSD_LRS`, `Premium_LRS` and `UltraSSD_LRS`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>write<wbr>Accelerator<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should Write Accelerator be enabled for this Data Disk? Defaults to `false`.
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
    <dd>{{% md %}}The type of Caching which should be used for this Data Disk. Possible values are `None`, `ReadOnly` and `ReadWrite`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk_<wbr>encryption_<wbr>set_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Disk Encryption Set which should be used to encrypt this Data Disk.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disk_<wbr>size_<wbr>gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The size of the Data Disk which should be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>lun</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The Logical Unit Number of the Data Disk, which must be unique within the Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage_<wbr>account_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Type of Storage Account which should back this Data Disk. Possible values include `Standard_LRS`, `StandardSSD_LRS`, `Premium_LRS` and `UltraSSD_LRS`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>write_<wbr>accelerator_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should Write Accelerator be enabled for this Data Disk? Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Identity</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetIdentity">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetIdentity">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetIdentityArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetIdentityOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Identity<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of User Managed Identity ID's which should be assigned to the Linux Virtual Machine Scale Set.
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
    <dd>{{% md %}}The type of Managed Identity which should be assigned to the Linux Virtual Machine Scale Set. Possible values are `SystemAssigned`, `UserAssigned` and `SystemAssigned, UserAssigned`.
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
    <dd>{{% md %}}A list of User Managed Identity ID's which should be assigned to the Linux Virtual Machine Scale Set.
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
    <dd>{{% md %}}The type of Managed Identity which should be assigned to the Linux Virtual Machine Scale Set. Possible values are `SystemAssigned`, `UserAssigned` and `SystemAssigned, UserAssigned`.
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
    <dd>{{% md %}}A list of User Managed Identity ID's which should be assigned to the Linux Virtual Machine Scale Set.
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
    <dd>{{% md %}}The type of Managed Identity which should be assigned to the Linux Virtual Machine Scale Set. Possible values are `SystemAssigned`, `UserAssigned` and `SystemAssigned, UserAssigned`.
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
    <dd>{{% md %}}A list of User Managed Identity ID's which should be assigned to the Linux Virtual Machine Scale Set.
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
    <dd>{{% md %}}The type of Managed Identity which should be assigned to the Linux Virtual Machine Scale Set. Possible values are `SystemAssigned`, `UserAssigned` and `SystemAssigned, UserAssigned`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetNetworkInterface">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetNetworkInterface">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetNetworkInterfaceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetNetworkInterfaceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of IP Addresses of DNS Servers which should be assigned to the Network Interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Accelerated<wbr>Networking</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Does this Network Interface support Accelerated Networking? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Ip<wbr>Forwarding</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Does this Network Interface support IP Forwarding? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ip<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterfaceipconfiguration">List&lt;Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface<wbr>Ip<wbr>Configuration<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `ip_configuration` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this Network Interface. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of a Network Security Group which should be assigned to this Network Interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Primary</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Is this the Primary IP Configuration?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of IP Addresses of DNS Servers which should be assigned to the Network Interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Accelerated<wbr>Networking</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Does this Network Interface support Accelerated Networking? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Ip<wbr>Forwarding</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Does this Network Interface support IP Forwarding? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ip<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterfaceipconfiguration">[]Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface<wbr>Ip<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}One or more `ip_configuration` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this Network Interface. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of a Network Security Group which should be assigned to this Network Interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Primary</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Is this the Primary IP Configuration?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of IP Addresses of DNS Servers which should be assigned to the Network Interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Accelerated<wbr>Networking</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Does this Network Interface support Accelerated Networking? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Ip<wbr>Forwarding</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Does this Network Interface support IP Forwarding? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ip<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterfaceipconfiguration">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface<wbr>Ip<wbr>Configuration[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `ip_configuration` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this Network Interface. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of a Network Security Group which should be assigned to this Network Interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>primary</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Is this the Primary IP Configuration?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dns_<wbr>servers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of IP Addresses of DNS Servers which should be assigned to the Network Interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>accelerated_<wbr>networking</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Does this Network Interface support Accelerated Networking? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>ip_<wbr>forwarding</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Does this Network Interface support IP Forwarding? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ip_<wbr>configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterfaceipconfiguration">List[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface<wbr>Ip<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}One or more `ip_configuration` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this Network Interface. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>security_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of a Network Security Group which should be assigned to this Network Interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>primary</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is this the Primary IP Configuration?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface<wbr>Ip<wbr>Configuration</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Application<wbr>Gateway<wbr>Backend<wbr>Address<wbr>Pool<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of Backend Address Pools ID's from a Application Gateway which this Virtual Machine Scale Set should be connected to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Application<wbr>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of Application Security Group ID's which this Virtual Machine Scale Set should be connected to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancer<wbr>Backend<wbr>Address<wbr>Pool<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of Backend Address Pools ID's from a Load Balancer which this Virtual Machine Scale Set should be connected to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancer<wbr>Inbound<wbr>Nat<wbr>Rules<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of NAT Rule ID's from a Load Balancer which this Virtual Machine Scale Set should be connected to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this IP Configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Primary</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Is this the Primary IP Configuration for this Network Interface? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterfaceipconfigurationpublicipaddress">List&lt;Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface<wbr>Ip<wbr>Configuration<wbr>Public<wbr>Ip<wbr>Address<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A `public_ip_address` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet which this IP Configuration should be connected to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Internet Protocol Version which should be used for this IP Configuration. Possible values are `IPv4` and `IPv6`. Defaults to `IPv4`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Application<wbr>Gateway<wbr>Backend<wbr>Address<wbr>Pool<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of Backend Address Pools ID's from a Application Gateway which this Virtual Machine Scale Set should be connected to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Application<wbr>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of Application Security Group ID's which this Virtual Machine Scale Set should be connected to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancer<wbr>Backend<wbr>Address<wbr>Pool<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of Backend Address Pools ID's from a Load Balancer which this Virtual Machine Scale Set should be connected to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancer<wbr>Inbound<wbr>Nat<wbr>Rules<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of NAT Rule ID's from a Load Balancer which this Virtual Machine Scale Set should be connected to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this IP Configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Primary</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Is this the Primary IP Configuration for this Network Interface? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterfaceipconfigurationpublicipaddress">[]Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface<wbr>Ip<wbr>Configuration<wbr>Public<wbr>Ip<wbr>Address</a></span>
    </dt>
    <dd>{{% md %}}A `public_ip_address` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet which this IP Configuration should be connected to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Internet Protocol Version which should be used for this IP Configuration. Possible values are `IPv4` and `IPv6`. Defaults to `IPv4`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>application<wbr>Gateway<wbr>Backend<wbr>Address<wbr>Pool<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of Backend Address Pools ID's from a Application Gateway which this Virtual Machine Scale Set should be connected to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>application<wbr>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of Application Security Group ID's which this Virtual Machine Scale Set should be connected to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load<wbr>Balancer<wbr>Backend<wbr>Address<wbr>Pool<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of Backend Address Pools ID's from a Load Balancer which this Virtual Machine Scale Set should be connected to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load<wbr>Balancer<wbr>Inbound<wbr>Nat<wbr>Rules<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of NAT Rule ID's from a Load Balancer which this Virtual Machine Scale Set should be connected to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this IP Configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>primary</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Is this the Primary IP Configuration for this Network Interface? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterfaceipconfigurationpublicipaddress">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface<wbr>Ip<wbr>Configuration<wbr>Public<wbr>Ip<wbr>Address[]?</a></span>
    </dt>
    <dd>{{% md %}}A `public_ip_address` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet which this IP Configuration should be connected to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Internet Protocol Version which should be used for this IP Configuration. Possible values are `IPv4` and `IPv6`. Defaults to `IPv4`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>application<wbr>Gateway<wbr>Backend<wbr>Address<wbr>Pool<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of Backend Address Pools ID's from a Application Gateway which this Virtual Machine Scale Set should be connected to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>application<wbr>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of Application Security Group ID's which this Virtual Machine Scale Set should be connected to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load<wbr>Balancer<wbr>Backend<wbr>Address<wbr>Pool<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of Backend Address Pools ID's from a Load Balancer which this Virtual Machine Scale Set should be connected to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load<wbr>Balancer<wbr>Inbound<wbr>Nat<wbr>Rules<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of NAT Rule ID's from a Load Balancer which this Virtual Machine Scale Set should be connected to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name which should be used for this IP Configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>primary</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is this the Primary IP Configuration for this Network Interface? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public_<wbr>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterfaceipconfigurationpublicipaddress">List[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface<wbr>Ip<wbr>Configuration<wbr>Public<wbr>Ip<wbr>Address]</a></span>
    </dt>
    <dd>{{% md %}}A `public_ip_address` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet which this IP Configuration should be connected to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Internet Protocol Version which should be used for this IP Configuration. Possible values are `IPv4` and `IPv6`. Defaults to `IPv4`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface<wbr>Ip<wbr>Configuration<wbr>Public<wbr>Ip<wbr>Address</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationPublicIpAddress">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationPublicIpAddress">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationPublicIpAddressArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationPublicIpAddressOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Domain<wbr>Name<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Prefix which should be used for the Domain Name Label for each Virtual Machine Instance. Azure concatenates the Domain Name Label and Virtual Machine Index to create a unique Domain Name Label for each Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Idle<wbr>Timeout<wbr>In<wbr>Minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The Idle Timeout in Minutes for the Public IP Address. Possible values are in the range `4` to `32`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterfaceipconfigurationpublicipaddressiptag">List&lt;Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface<wbr>Ip<wbr>Configuration<wbr>Public<wbr>Ip<wbr>Address<wbr>Ip<wbr>Tag<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `ip_tag` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Public IP Address Configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ip<wbr>Prefix<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Public IP Address Prefix from where Public IP Addresses should be allocated. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Domain<wbr>Name<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Prefix which should be used for the Domain Name Label for each Virtual Machine Instance. Azure concatenates the Domain Name Label and Virtual Machine Index to create a unique Domain Name Label for each Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Idle<wbr>Timeout<wbr>In<wbr>Minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The Idle Timeout in Minutes for the Public IP Address. Possible values are in the range `4` to `32`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterfaceipconfigurationpublicipaddressiptag">[]Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface<wbr>Ip<wbr>Configuration<wbr>Public<wbr>Ip<wbr>Address<wbr>Ip<wbr>Tag</a></span>
    </dt>
    <dd>{{% md %}}One or more `ip_tag` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Public IP Address Configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ip<wbr>Prefix<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Public IP Address Prefix from where Public IP Addresses should be allocated. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>domain<wbr>Name<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Prefix which should be used for the Domain Name Label for each Virtual Machine Instance. Azure concatenates the Domain Name Label and Virtual Machine Index to create a unique Domain Name Label for each Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>idle<wbr>Timeout<wbr>In<wbr>Minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The Idle Timeout in Minutes for the Public IP Address. Possible values are in the range `4` to `32`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterfaceipconfigurationpublicipaddressiptag">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface<wbr>Ip<wbr>Configuration<wbr>Public<wbr>Ip<wbr>Address<wbr>Ip<wbr>Tag[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `ip_tag` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Name of the Public IP Address Configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public<wbr>Ip<wbr>Prefix<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Public IP Address Prefix from where Public IP Addresses should be allocated. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>domain_<wbr>name_<wbr>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Prefix which should be used for the Domain Name Label for each Virtual Machine Instance. Azure concatenates the Domain Name Label and Virtual Machine Index to create a unique Domain Name Label for each Virtual Machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>idle_<wbr>timeout_<wbr>in_<wbr>minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The Idle Timeout in Minutes for the Public IP Address. Possible values are in the range `4` to `32`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetnetworkinterfaceipconfigurationpublicipaddressiptag">List[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface<wbr>Ip<wbr>Configuration<wbr>Public<wbr>Ip<wbr>Address<wbr>Ip<wbr>Tag]</a></span>
    </dt>
    <dd>{{% md %}}One or more `ip_tag` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Name of the Public IP Address Configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public_<wbr>ip_<wbr>prefix_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Public IP Address Prefix from where Public IP Addresses should be allocated. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Network<wbr>Interface<wbr>Ip<wbr>Configuration<wbr>Public<wbr>Ip<wbr>Address<wbr>Ip<wbr>Tag</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationPublicIpAddressIpTag">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationPublicIpAddressIpTag">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationPublicIpAddressIpTagArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationPublicIpAddressIpTagOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP Tag associated with the Public IP, such as `SQL` or `Storage`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Type of IP Tag, such as `FirstPartyUsage`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP Tag associated with the Public IP, such as `SQL` or `Storage`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Type of IP Tag, such as `FirstPartyUsage`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP Tag associated with the Public IP, such as `SQL` or `Storage`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Type of IP Tag, such as `FirstPartyUsage`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>tag</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IP Tag associated with the Public IP, such as `SQL` or `Storage`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Type of IP Tag, such as `FirstPartyUsage`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetOsDisk">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetOsDisk">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetOsDiskArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetOsDiskOutput">output</a> API doc for this type.
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
        <span class="property-type"><a href="#linuxvirtualmachinescalesetosdiskdiffdisksettings">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk<wbr>Diff<wbr>Disk<wbr>Settings<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `diff_disk_settings` block as defined above. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Encryption<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Disk Encryption Set which should be used to encrypt this OS Disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine Scale Set is sourced from.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Type of Storage Account which should back this the Internal OS Disk. Possible values include `Standard_LRS`, `StandardSSD_LRS` and `Premium_LRS`.
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
        <span class="property-type"><a href="#linuxvirtualmachinescalesetosdiskdiffdisksettings">*Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk<wbr>Diff<wbr>Disk<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}A `diff_disk_settings` block as defined above. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Encryption<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Disk Encryption Set which should be used to encrypt this OS Disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine Scale Set is sourced from.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Type of Storage Account which should back this the Internal OS Disk. Possible values include `Standard_LRS`, `StandardSSD_LRS` and `Premium_LRS`.
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
        <span class="property-type"><a href="#linuxvirtualmachinescalesetosdiskdiffdisksettings">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk<wbr>Diff<wbr>Disk<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}A `diff_disk_settings` block as defined above. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Encryption<wbr>Set<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Disk Encryption Set which should be used to encrypt this OS Disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine Scale Set is sourced from.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Account<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Type of Storage Account which should back this the Internal OS Disk. Possible values include `Standard_LRS`, `StandardSSD_LRS` and `Premium_LRS`.
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
        <span class="property-type"><a href="#linuxvirtualmachinescalesetosdiskdiffdisksettings">Dict[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk<wbr>Diff<wbr>Disk<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}A `diff_disk_settings` block as defined above. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk_<wbr>encryption_<wbr>set_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Disk Encryption Set which should be used to encrypt this OS Disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk_<wbr>size_<wbr>gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine Scale Set is sourced from.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage_<wbr>account_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Type of Storage Account which should back this the Internal OS Disk. Possible values include `Standard_LRS`, `StandardSSD_LRS` and `Premium_LRS`.
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





<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Os<wbr>Disk<wbr>Diff<wbr>Disk<wbr>Settings</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetOsDiskDiffDiskSettingsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetOsDiskDiffDiskSettingsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Option</span>
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
        <span>Option</span>
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
        <span>option</span>
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
        <span>option</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Plan</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetPlan">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetPlan">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetPlanArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetPlanOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Product</span>
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
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Product</span>
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
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>product</span>
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
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>product</span>
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
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Rolling<wbr>Upgrade<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetRollingUpgradePolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetRollingUpgradePolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetRollingUpgradePolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetRollingUpgradePolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Batch<wbr>Instance<wbr>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum percent of total virtual machine instances that will be upgraded simultaneously by the rolling upgrade in one batch. As this is a maximum, unhealthy instances in previous or future batches can cause the percentage of instances in a batch to decrease to ensure higher reliability. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Unhealthy<wbr>Instance<wbr>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy, either as a result of being upgraded, or by being found in an unhealthy state by the virtual machine health checks before the rolling upgrade aborts. This constraint will be checked prior to starting any batch. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Unhealthy<wbr>Upgraded<wbr>Instance<wbr>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum percentage of upgraded virtual machine instances that can be found to be in an unhealthy state. This check will happen after each batch is upgraded. If this percentage is ever exceeded, the rolling update aborts. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Pause<wbr>Time<wbr>Between<wbr>Batches</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The wait time between completing the update for all virtual machines in one batch and starting the next batch. The time duration should be specified in ISO 8601 format. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Batch<wbr>Instance<wbr>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum percent of total virtual machine instances that will be upgraded simultaneously by the rolling upgrade in one batch. As this is a maximum, unhealthy instances in previous or future batches can cause the percentage of instances in a batch to decrease to ensure higher reliability. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Unhealthy<wbr>Instance<wbr>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy, either as a result of being upgraded, or by being found in an unhealthy state by the virtual machine health checks before the rolling upgrade aborts. This constraint will be checked prior to starting any batch. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Unhealthy<wbr>Upgraded<wbr>Instance<wbr>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum percentage of upgraded virtual machine instances that can be found to be in an unhealthy state. This check will happen after each batch is upgraded. If this percentage is ever exceeded, the rolling update aborts. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Pause<wbr>Time<wbr>Between<wbr>Batches</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The wait time between completing the update for all virtual machines in one batch and starting the next batch. The time duration should be specified in ISO 8601 format. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Batch<wbr>Instance<wbr>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum percent of total virtual machine instances that will be upgraded simultaneously by the rolling upgrade in one batch. As this is a maximum, unhealthy instances in previous or future batches can cause the percentage of instances in a batch to decrease to ensure higher reliability. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Unhealthy<wbr>Instance<wbr>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy, either as a result of being upgraded, or by being found in an unhealthy state by the virtual machine health checks before the rolling upgrade aborts. This constraint will be checked prior to starting any batch. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Unhealthy<wbr>Upgraded<wbr>Instance<wbr>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum percentage of upgraded virtual machine instances that can be found to be in an unhealthy state. This check will happen after each batch is upgraded. If this percentage is ever exceeded, the rolling update aborts. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>pause<wbr>Time<wbr>Between<wbr>Batches</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The wait time between completing the update for all virtual machines in one batch and starting the next batch. The time duration should be specified in ISO 8601 format. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Batch<wbr>Instance<wbr>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum percent of total virtual machine instances that will be upgraded simultaneously by the rolling upgrade in one batch. As this is a maximum, unhealthy instances in previous or future batches can cause the percentage of instances in a batch to decrease to ensure higher reliability. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Unhealthy<wbr>Instance<wbr>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy, either as a result of being upgraded, or by being found in an unhealthy state by the virtual machine health checks before the rolling upgrade aborts. This constraint will be checked prior to starting any batch. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Unhealthy<wbr>Upgraded<wbr>Instance<wbr>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum percentage of upgraded virtual machine instances that can be found to be in an unhealthy state. This check will happen after each batch is upgraded. If this percentage is ever exceeded, the rolling update aborts. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>pause<wbr>Time<wbr>Between<wbr>Batches</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The wait time between completing the update for all virtual machines in one batch and starting the next batch. The time duration should be specified in ISO 8601 format. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetSecret">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetSecret">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetSecretArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetSecretOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsecretcertificate">List&lt;Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret<wbr>Certificate<wbr>Args&gt;</a></span>
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
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsecretcertificate">[]Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret<wbr>Certificate</a></span>
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
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsecretcertificate">Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret<wbr>Certificate[]</a></span>
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
        <span class="property-type"><a href="#linuxvirtualmachinescalesetsecretcertificate">List[Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret<wbr>Certificate]</a></span>
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





<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Secret<wbr>Certificate</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetSecretCertificate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetSecretCertificate">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetSecretCertificateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetSecretCertificateOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

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
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Secret URL of a Key Vault Certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Source<wbr>Image<wbr>Reference</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetSourceImageReference">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetSourceImageReference">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetSourceImageReferenceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetSourceImageReferenceOutput">output</a> API doc for this type.
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
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Virtual Machine SKU for the Scale Set, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Internet Protocol Version which should be used for this IP Configuration. Possible values are `IPv4` and `IPv6`. Defaults to `IPv4`.
{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Virtual Machine SKU for the Scale Set, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Internet Protocol Version which should be used for this IP Configuration. Possible values are `IPv4` and `IPv6`. Defaults to `IPv4`.
{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Virtual Machine SKU for the Scale Set, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Internet Protocol Version which should be used for this IP Configuration. Possible values are `IPv4` and `IPv6`. Defaults to `IPv4`.
{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Virtual Machine SKU for the Scale Set, such as `Standard_F2`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Internet Protocol Version which should be used for this IP Configuration. Possible values are `IPv4` and `IPv6`. Defaults to `IPv4`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Linux<wbr>Virtual<wbr>Machine<wbr>Scale<wbr>Set<wbr>Terminate<wbr>Notification</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#LinuxVirtualMachineScaleSetTerminateNotification">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#LinuxVirtualMachineScaleSetTerminateNotification">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetTerminateNotificationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/compute?tab=doc#LinuxVirtualMachineScaleSetTerminateNotificationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should the terminate notification be enabled on this Virtual Machine Scale Set? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Length of time (in minutes, between 5 and 15) a notification to be sent to the VM on the instance metadata server till the VM gets deleted. The time duration should be specified in ISO 8601 format.
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
    <dd>{{% md %}}Should the terminate notification be enabled on this Virtual Machine Scale Set? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Length of time (in minutes, between 5 and 15) a notification to be sent to the VM on the instance metadata server till the VM gets deleted. The time duration should be specified in ISO 8601 format.
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
    <dd>{{% md %}}Should the terminate notification be enabled on this Virtual Machine Scale Set? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Length of time (in minutes, between 5 and 15) a notification to be sent to the VM on the instance metadata server till the VM gets deleted. The time duration should be specified in ISO 8601 format.
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
    <dd>{{% md %}}Should the terminate notification be enabled on this Virtual Machine Scale Set? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Length of time (in minutes, between 5 and 15) a notification to be sent to the VM on the instance metadata server till the VM gets deleted. The time duration should be specified in ISO 8601 format.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-azure">https://github.com/pulumi/pulumi-azure</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

