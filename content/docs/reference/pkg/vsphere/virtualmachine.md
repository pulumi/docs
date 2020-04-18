
---
title: "VirtualMachine"
block_external_search_index: true
---






## Create a VirtualMachine Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#VirtualMachine">VirtualMachine</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#VirtualMachineArgs">VirtualMachineArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">VirtualMachine</span><span class="p">(resource_name, opts=None, </span>alternate_guest_name=None<span class="p">, </span>annotation=None<span class="p">, </span>boot_delay=None<span class="p">, </span>boot_retry_delay=None<span class="p">, </span>boot_retry_enabled=None<span class="p">, </span>cdrom=None<span class="p">, </span>clone=None<span class="p">, </span>cpu_hot_add_enabled=None<span class="p">, </span>cpu_hot_remove_enabled=None<span class="p">, </span>cpu_limit=None<span class="p">, </span>cpu_performance_counters_enabled=None<span class="p">, </span>cpu_reservation=None<span class="p">, </span>cpu_share_count=None<span class="p">, </span>cpu_share_level=None<span class="p">, </span>custom_attributes=None<span class="p">, </span>datastore_cluster_id=None<span class="p">, </span>datastore_id=None<span class="p">, </span>disks=None<span class="p">, </span>efi_secure_boot_enabled=None<span class="p">, </span>enable_disk_uuid=None<span class="p">, </span>enable_logging=None<span class="p">, </span>ept_rvi_mode=None<span class="p">, </span>extra_config=None<span class="p">, </span>firmware=None<span class="p">, </span>folder=None<span class="p">, </span>force_power_off=None<span class="p">, </span>guest_id=None<span class="p">, </span>hardware_version=None<span class="p">, </span>host_system_id=None<span class="p">, </span>hv_mode=None<span class="p">, </span>ignored_guest_ips=None<span class="p">, </span>latency_sensitivity=None<span class="p">, </span>memory=None<span class="p">, </span>memory_hot_add_enabled=None<span class="p">, </span>memory_limit=None<span class="p">, </span>memory_reservation=None<span class="p">, </span>memory_share_count=None<span class="p">, </span>memory_share_level=None<span class="p">, </span>migrate_wait_timeout=None<span class="p">, </span>name=None<span class="p">, </span>nested_hv_enabled=None<span class="p">, </span>network_interfaces=None<span class="p">, </span>num_cores_per_socket=None<span class="p">, </span>num_cpus=None<span class="p">, </span>poweron_timeout=None<span class="p">, </span>resource_pool_id=None<span class="p">, </span>run_tools_scripts_after_power_on=None<span class="p">, </span>run_tools_scripts_after_resume=None<span class="p">, </span>run_tools_scripts_before_guest_reboot=None<span class="p">, </span>run_tools_scripts_before_guest_shutdown=None<span class="p">, </span>run_tools_scripts_before_guest_standby=None<span class="p">, </span>scsi_bus_sharing=None<span class="p">, </span>scsi_controller_count=None<span class="p">, </span>scsi_type=None<span class="p">, </span>shutdown_wait_timeout=None<span class="p">, </span>storage_policy_id=None<span class="p">, </span>swap_placement_policy=None<span class="p">, </span>sync_time_with_host=None<span class="p">, </span>tags=None<span class="p">, </span>vapp=None<span class="p">, </span>wait_for_guest_ip_timeout=None<span class="p">, </span>wait_for_guest_net_routable=None<span class="p">, </span>wait_for_guest_net_timeout=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewVirtualMachine<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineArgs">VirtualMachineArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachine">VirtualMachine</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere.VirtualMachine.html">VirtualMachine</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.VSphere.VirtualMachineArgs.html">VirtualMachineArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinenetworkinterface">List&lt;Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Virtual<wbr>Machine<wbr>Network<wbr>Interface<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual NIC on this
virtual machine. See network interface options
below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the resource pool to put this virtual machine in.
See the section on virtual machine migration
for details on changing this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alternate<wbr>Guest<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The guest name for the operating system
when `guest_id` is `other` or `other-64`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Annotation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A user-provided description of the virtual machine.
The default is no annotation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of milliseconds to wait before starting
the boot sequence. The default is no delay.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Retry<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of milliseconds to wait before
retrying the boot sequence. This only valid if `boot_retry_enabled` is true.
Default: `10000` (10 seconds).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Retry<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to true, a virtual machine that
fails to boot will try again after the delay defined in `boot_retry_delay`.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cdrom</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinecdrom">Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Virtual<wbr>Machine<wbr>Cdrom<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A specification for a CDROM device on this virtual
machine. See CDROM options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Clone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclone">Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Virtual<wbr>Machine<wbr>Clone<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}When specified, the VM will be created as a clone of a
specified template. Optional customization options can be submitted as well.
See creating a virtual machine from a
template for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Hot<wbr>Add<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow CPUs to be added to this virtual
machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Hot<wbr>Remove<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow CPUs to be removed to this
virtual machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum amount of CPU (in MHz) that this virtual
machine can consume, regardless of available resources. The default is no
limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Performance<wbr>Counters<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable CPU performance
counters on this virtual machine. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of CPU (in MHz) that this virtual
machine is guaranteed. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of CPU shares allocated to the
virtual machine when the `cpu_share_level` is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The allocation level for CPU resources. Can be
one of `high`, `low`, `normal`, or `custom`. Default: `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual machine. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datastore cluster ID to use. This setting
applies to entire virtual machine and implies that you wish to use Storage
DRS with this virtual machine. See the section on virtual machine
migration for details on changing this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datastore<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinedisk">List&lt;Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Virtual<wbr>Machine<wbr>Disk<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual disk device on this virtual
machine. See disk options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Efi<wbr>Secure<wbr>Boot<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}When the `firmware` type is set to is
`efi`, this enables EFI secure boot. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Disk<wbr>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Expose the UUIDs of attached virtual disks to
the virtual machine, allowing access to them in the guest. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable logging of virtual machine events to a
log file stored in the virtual machine directory. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ept<wbr>Rvi<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The EPT/RVI (hardware memory virtualization)
setting for this virtual machine. Can be one of `automatic`, `on`, or `off`.
Default: `automatic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Extra<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}Extra configuration data for this virtual
machine. Can be used to supply advanced parameters not normally in
configuration, such as instance metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Firmware</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The firmware interface to use on the virtual machine.
Can be one of `bios` or `EFI`. Default: `bios`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The path to the folder to put this virtual machine in,
relative to the datacenter that the resource pool is in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Power<wbr>Off</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}If a guest shutdown failed or timed out while
updating or destroying (see
`shutdown_wait_timeout`), force the power-off of
the virtual machine. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The guest ID for the operating system type. For a
full list of possible values, see [here][vmware-docs-guest-ids]. Default: `other-64`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hardware<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The hardware version number. Valid range
is from 4 to 15. The hardware version cannot be downgraded. See [virtual
machine hardware compatibility][virtual-machine-hardware-compatibility] for
more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>System<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}An optional [managed object reference
ID][docs-about-morefs] of a host to put this virtual machine on. See the
section on virtual machine migration for
details on changing this value. If a `host_system_id` is not supplied,
vSphere will select a host in the resource pool to place the virtual machine,
according to any defaults or DRS policies in place.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hv<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The (non-nested) hardware virtualization setting for
this virtual machine. Can be one of `hvAuto`, `hvOn`, or `hvOff`. Default:
`hvAuto`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ignored<wbr>Guest<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}List of IP addresses and CIDR networks to
ignore while waiting for an available IP address using either of the waiters.
Any IP addresses in this list will be ignored if they show up so that the
waiter will continue to wait for a real IP address. Default: [].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Latency<wbr>Sensitivity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the scheduling delay of the
virtual machine. Use a higher sensitivity for applications that require lower
latency, such as VOIP, media player applications, or applications that
require frequent access to mouse or keyboard devices. Can be one of `low`,
`normal`, `medium`, or `high`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The size of the virtual machine's memory, in MB.
Default: `1024` (1 GB).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Hot<wbr>Add<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow memory to be added to this
virtual machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum amount of memory (in MB) that this
virtual machine can consume, regardless of available resources. The default
is no limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of memory (in MB) that this
virtual machine is guaranteed. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of memory shares allocated to
the virtual machine when the `memory_share_level` is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The allocation level for memory resources.
Can be one of `high`, `low`, `normal`, or `custom`. Default: `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Migrate<wbr>Wait<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to wait
for a virtual machine migration to complete before failing. Default: 10
minutes. Also see the section on virtual machine
migration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}An alias for both `label` and `path`, the latter when
using `attach`. Required if not using `label`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nested<wbr>Hv<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable nested hardware virtualization on
this virtual machine, facilitating nested virtualization in the guest.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Cores<wbr>Per<wbr>Socket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of cores per socket in this
virtual machine. The number of vCPUs on the virtual machine will be
`num_cpus` divided by `num_cores_per_socket`. If specified, the value
supplied to `num_cpus` must be evenly divisible by this value. Default: `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Cpus</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The total number of virtual processor cores to assign
to this virtual machine. Default: `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Poweron<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, that we will be trying to power on a VM
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>After<wbr>Power<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
post-power-on scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>After<wbr>Resume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
post-resume scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Reboot</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
pre-reboot scripts when VMware tools is installed. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Shutdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution
of pre-shutdown scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Standby</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
pre-standby scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scsi<wbr>Bus<wbr>Sharing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Mode for sharing the SCSI bus. The modes are
physicalSharing, virtualSharing, and noSharing. Default: `noSharing`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scsi<wbr>Controller<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of SCSI controllers that Terraform manages on this virtual machine. This directly affects the amount of disks
you can add to the virtual machine and the maximum disk unit number. Note that lowering this value does not remove
controllers.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scsi<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of SCSI bus this virtual machine will have.
Can be one of lsilogic (LSI Logic Parallel), lsilogic-sas (LSI Logic SAS) or
pvscsi (VMware Paravirtual). Defualt: `pvscsi`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shutdown<wbr>Wait<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to wait
for a graceful guest shutdown when making necessary updates to the virtual
machine. If `force_power_off` is set to true, the VM will be force powered-off
after this timeout, otherwise an error is returned. Default: 3 minutes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the storage policy to assign to this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Swap<wbr>Placement<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The swap file placement policy for this
virtual machine. Can be one of `inherit`, `hostLocal`, or `vmDirectory`.
Default: `inherit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sync<wbr>Time<wbr>With<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable guest clock synchronization with
the host. Requires VMware tools to be installed. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vapp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinevapp">Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Virtual<wbr>Machine<wbr>Vapp<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Optional vApp configuration. The only sub-key available
is `properties`, which is a key/value map of properties for virtual machines
imported from OVF or OVA files. See Using vApp properties to supply OVF/OVA
configuration for
more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait<wbr>For<wbr>Guest<wbr>Ip<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to
wait for an available guest IP address on this virtual machine. This should
only be used if your version of VMware Tools does not allow the
`wait_for_guest_net_timeout` waiter to be
used. A value less than 1 disables the waiter. Default: 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait<wbr>For<wbr>Guest<wbr>Net<wbr>Routable</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Controls whether or not the guest
network waiter waits for a routable address. When `false`, the waiter does
not wait for a default gateway, nor are IP addresses checked against any
discovered default gateways as part of its success criteria. This property is
ignored if the `wait_for_guest_ip_timeout`
waiter is used. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait<wbr>For<wbr>Guest<wbr>Net<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to
wait for an available IP address on this virtual machine's NICs. Older
versions of VMware Tools do not populate this property. In those cases, this
waiter can be disabled and the
`wait_for_guest_ip_timeout` waiter can be used
instead. A value less than 1 disables the waiter. Default: 5 minutes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinenetworkinterface">[]Virtual<wbr>Machine<wbr>Network<wbr>Interface</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual NIC on this
virtual machine. See network interface options
below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the resource pool to put this virtual machine in.
See the section on virtual machine migration
for details on changing this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alternate<wbr>Guest<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The guest name for the operating system
when `guest_id` is `other` or `other-64`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Annotation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A user-provided description of the virtual machine.
The default is no annotation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of milliseconds to wait before starting
the boot sequence. The default is no delay.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Retry<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of milliseconds to wait before
retrying the boot sequence. This only valid if `boot_retry_enabled` is true.
Default: `10000` (10 seconds).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Retry<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to true, a virtual machine that
fails to boot will try again after the delay defined in `boot_retry_delay`.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cdrom</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinecdrom">Virtual<wbr>Machine<wbr>Cdrom</a></span>
    </dt>
    <dd>{{% md %}}A specification for a CDROM device on this virtual
machine. See CDROM options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Clone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclone">Virtual<wbr>Machine<wbr>Clone</a></span>
    </dt>
    <dd>{{% md %}}When specified, the VM will be created as a clone of a
specified template. Optional customization options can be submitted as well.
See creating a virtual machine from a
template for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Hot<wbr>Add<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow CPUs to be added to this virtual
machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Hot<wbr>Remove<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow CPUs to be removed to this
virtual machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum amount of CPU (in MHz) that this virtual
machine can consume, regardless of available resources. The default is no
limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Performance<wbr>Counters<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable CPU performance
counters on this virtual machine. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of CPU (in MHz) that this virtual
machine is guaranteed. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of CPU shares allocated to the
virtual machine when the `cpu_share_level` is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The allocation level for CPU resources. Can be
one of `high`, `low`, `normal`, or `custom`. Default: `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual machine. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datastore cluster ID to use. This setting
applies to entire virtual machine and implies that you wish to use Storage
DRS with this virtual machine. See the section on virtual machine
migration for details on changing this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datastore<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinedisk">[]Virtual<wbr>Machine<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual disk device on this virtual
machine. See disk options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Efi<wbr>Secure<wbr>Boot<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}When the `firmware` type is set to is
`efi`, this enables EFI secure boot. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Disk<wbr>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Expose the UUIDs of attached virtual disks to
the virtual machine, allowing access to them in the guest. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable logging of virtual machine events to a
log file stored in the virtual machine directory. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ept<wbr>Rvi<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The EPT/RVI (hardware memory virtualization)
setting for this virtual machine. Can be one of `automatic`, `on`, or `off`.
Default: `automatic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Extra<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Extra configuration data for this virtual
machine. Can be used to supply advanced parameters not normally in
configuration, such as instance metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Firmware</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The firmware interface to use on the virtual machine.
Can be one of `bios` or `EFI`. Default: `bios`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The path to the folder to put this virtual machine in,
relative to the datacenter that the resource pool is in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Power<wbr>Off</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}If a guest shutdown failed or timed out while
updating or destroying (see
`shutdown_wait_timeout`), force the power-off of
the virtual machine. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The guest ID for the operating system type. For a
full list of possible values, see [here][vmware-docs-guest-ids]. Default: `other-64`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hardware<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The hardware version number. Valid range
is from 4 to 15. The hardware version cannot be downgraded. See [virtual
machine hardware compatibility][virtual-machine-hardware-compatibility] for
more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>System<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional [managed object reference
ID][docs-about-morefs] of a host to put this virtual machine on. See the
section on virtual machine migration for
details on changing this value. If a `host_system_id` is not supplied,
vSphere will select a host in the resource pool to place the virtual machine,
according to any defaults or DRS policies in place.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hv<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The (non-nested) hardware virtualization setting for
this virtual machine. Can be one of `hvAuto`, `hvOn`, or `hvOff`. Default:
`hvAuto`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ignored<wbr>Guest<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}List of IP addresses and CIDR networks to
ignore while waiting for an available IP address using either of the waiters.
Any IP addresses in this list will be ignored if they show up so that the
waiter will continue to wait for a real IP address. Default: [].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Latency<wbr>Sensitivity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the scheduling delay of the
virtual machine. Use a higher sensitivity for applications that require lower
latency, such as VOIP, media player applications, or applications that
require frequent access to mouse or keyboard devices. Can be one of `low`,
`normal`, `medium`, or `high`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The size of the virtual machine's memory, in MB.
Default: `1024` (1 GB).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Hot<wbr>Add<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow memory to be added to this
virtual machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum amount of memory (in MB) that this
virtual machine can consume, regardless of available resources. The default
is no limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of memory (in MB) that this
virtual machine is guaranteed. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of memory shares allocated to
the virtual machine when the `memory_share_level` is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The allocation level for memory resources.
Can be one of `high`, `low`, `normal`, or `custom`. Default: `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Migrate<wbr>Wait<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to wait
for a virtual machine migration to complete before failing. Default: 10
minutes. Also see the section on virtual machine
migration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}An alias for both `label` and `path`, the latter when
using `attach`. Required if not using `label`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nested<wbr>Hv<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable nested hardware virtualization on
this virtual machine, facilitating nested virtualization in the guest.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Cores<wbr>Per<wbr>Socket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of cores per socket in this
virtual machine. The number of vCPUs on the virtual machine will be
`num_cpus` divided by `num_cores_per_socket`. If specified, the value
supplied to `num_cpus` must be evenly divisible by this value. Default: `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Cpus</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The total number of virtual processor cores to assign
to this virtual machine. Default: `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Poweron<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, that we will be trying to power on a VM
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>After<wbr>Power<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
post-power-on scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>After<wbr>Resume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
post-resume scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Reboot</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
pre-reboot scripts when VMware tools is installed. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Shutdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution
of pre-shutdown scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Standby</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
pre-standby scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scsi<wbr>Bus<wbr>Sharing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Mode for sharing the SCSI bus. The modes are
physicalSharing, virtualSharing, and noSharing. Default: `noSharing`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scsi<wbr>Controller<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of SCSI controllers that Terraform manages on this virtual machine. This directly affects the amount of disks
you can add to the virtual machine and the maximum disk unit number. Note that lowering this value does not remove
controllers.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scsi<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of SCSI bus this virtual machine will have.
Can be one of lsilogic (LSI Logic Parallel), lsilogic-sas (LSI Logic SAS) or
pvscsi (VMware Paravirtual). Defualt: `pvscsi`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shutdown<wbr>Wait<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to wait
for a graceful guest shutdown when making necessary updates to the virtual
machine. If `force_power_off` is set to true, the VM will be force powered-off
after this timeout, otherwise an error is returned. Default: 3 minutes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the storage policy to assign to this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Swap<wbr>Placement<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The swap file placement policy for this
virtual machine. Can be one of `inherit`, `hostLocal`, or `vmDirectory`.
Default: `inherit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sync<wbr>Time<wbr>With<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable guest clock synchronization with
the host. Requires VMware tools to be installed. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vapp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinevapp">Virtual<wbr>Machine<wbr>Vapp</a></span>
    </dt>
    <dd>{{% md %}}Optional vApp configuration. The only sub-key available
is `properties`, which is a key/value map of properties for virtual machines
imported from OVF or OVA files. See Using vApp properties to supply OVF/OVA
configuration for
more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait<wbr>For<wbr>Guest<wbr>Ip<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to
wait for an available guest IP address on this virtual machine. This should
only be used if your version of VMware Tools does not allow the
`wait_for_guest_net_timeout` waiter to be
used. A value less than 1 disables the waiter. Default: 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait<wbr>For<wbr>Guest<wbr>Net<wbr>Routable</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Controls whether or not the guest
network waiter waits for a routable address. When `false`, the waiter does
not wait for a default gateway, nor are IP addresses checked against any
discovered default gateways as part of its success criteria. This property is
ignored if the `wait_for_guest_ip_timeout`
waiter is used. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait<wbr>For<wbr>Guest<wbr>Net<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to
wait for an available IP address on this virtual machine's NICs. Older
versions of VMware Tools do not populate this property. In those cases, this
waiter can be disabled and the
`wait_for_guest_ip_timeout` waiter can be used
instead. A value less than 1 disables the waiter. Default: 5 minutes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinenetworkinterface">Virtual<wbr>Machine<wbr>Network<wbr>Interface[]</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual NIC on this
virtual machine. See network interface options
below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the resource pool to put this virtual machine in.
See the section on virtual machine migration
for details on changing this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alternate<wbr>Guest<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The guest name for the operating system
when `guest_id` is `other` or `other-64`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>annotation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A user-provided description of the virtual machine.
The default is no annotation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of milliseconds to wait before starting
the boot sequence. The default is no delay.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Retry<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of milliseconds to wait before
retrying the boot sequence. This only valid if `boot_retry_enabled` is true.
Default: `10000` (10 seconds).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Retry<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}If set to true, a virtual machine that
fails to boot will try again after the delay defined in `boot_retry_delay`.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cdrom</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinecdrom">Virtual<wbr>Machine<wbr>Cdrom</a></span>
    </dt>
    <dd>{{% md %}}A specification for a CDROM device on this virtual
machine. See CDROM options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>clone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclone">Virtual<wbr>Machine<wbr>Clone</a></span>
    </dt>
    <dd>{{% md %}}When specified, the VM will be created as a clone of a
specified template. Optional customization options can be submitted as well.
See creating a virtual machine from a
template for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu<wbr>Hot<wbr>Add<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Allow CPUs to be added to this virtual
machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu<wbr>Hot<wbr>Remove<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Allow CPUs to be removed to this
virtual machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The maximum amount of CPU (in MHz) that this virtual
machine can consume, regardless of available resources. The default is no
limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu<wbr>Performance<wbr>Counters<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable CPU performance
counters on this virtual machine. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The amount of CPU (in MHz) that this virtual
machine is guaranteed. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of CPU shares allocated to the
virtual machine when the `cpu_share_level` is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The allocation level for CPU resources. Can be
one of `high`, `low`, `normal`, or `custom`. Default: `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual machine. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datastore cluster ID to use. This setting
applies to entire virtual machine and implies that you wish to use Storage
DRS with this virtual machine. See the section on virtual machine
migration for details on changing this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datastore<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinedisk">Virtual<wbr>Machine<wbr>Disk[]</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual disk device on this virtual
machine. See disk options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>efi<wbr>Secure<wbr>Boot<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}When the `firmware` type is set to is
`efi`, this enables EFI secure boot. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Disk<wbr>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Expose the UUIDs of attached virtual disks to
the virtual machine, allowing access to them in the guest. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable logging of virtual machine events to a
log file stored in the virtual machine directory. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ept<wbr>Rvi<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The EPT/RVI (hardware memory virtualization)
setting for this virtual machine. Can be one of `automatic`, `on`, or `off`.
Default: `automatic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>extra<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}Extra configuration data for this virtual
machine. Can be used to supply advanced parameters not normally in
configuration, such as instance metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>firmware</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The firmware interface to use on the virtual machine.
Can be one of `bios` or `EFI`. Default: `bios`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The path to the folder to put this virtual machine in,
relative to the datacenter that the resource pool is in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force<wbr>Power<wbr>Off</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}If a guest shutdown failed or timed out while
updating or destroying (see
`shutdown_wait_timeout`), force the power-off of
the virtual machine. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The guest ID for the operating system type. For a
full list of possible values, see [here][vmware-docs-guest-ids]. Default: `other-64`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hardware<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The hardware version number. Valid range
is from 4 to 15. The hardware version cannot be downgraded. See [virtual
machine hardware compatibility][virtual-machine-hardware-compatibility] for
more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>System<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional [managed object reference
ID][docs-about-morefs] of a host to put this virtual machine on. See the
section on virtual machine migration for
details on changing this value. If a `host_system_id` is not supplied,
vSphere will select a host in the resource pool to place the virtual machine,
according to any defaults or DRS policies in place.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hv<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The (non-nested) hardware virtualization setting for
this virtual machine. Can be one of `hvAuto`, `hvOn`, or `hvOff`. Default:
`hvAuto`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ignored<wbr>Guest<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}List of IP addresses and CIDR networks to
ignore while waiting for an available IP address using either of the waiters.
Any IP addresses in this list will be ignored if they show up so that the
waiter will continue to wait for a real IP address. Default: [].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>latency<wbr>Sensitivity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the scheduling delay of the
virtual machine. Use a higher sensitivity for applications that require lower
latency, such as VOIP, media player applications, or applications that
require frequent access to mouse or keyboard devices. Can be one of `low`,
`normal`, `medium`, or `high`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The size of the virtual machine's memory, in MB.
Default: `1024` (1 GB).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory<wbr>Hot<wbr>Add<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Allow memory to be added to this
virtual machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The maximum amount of memory (in MB) that this
virtual machine can consume, regardless of available resources. The default
is no limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The amount of memory (in MB) that this
virtual machine is guaranteed. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of memory shares allocated to
the virtual machine when the `memory_share_level` is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The allocation level for memory resources.
Can be one of `high`, `low`, `normal`, or `custom`. Default: `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>migrate<wbr>Wait<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to wait
for a virtual machine migration to complete before failing. Default: 10
minutes. Also see the section on virtual machine
migration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}An alias for both `label` and `path`, the latter when
using `attach`. Required if not using `label`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nested<wbr>Hv<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable nested hardware virtualization on
this virtual machine, facilitating nested virtualization in the guest.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Cores<wbr>Per<wbr>Socket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of cores per socket in this
virtual machine. The number of vCPUs on the virtual machine will be
`num_cpus` divided by `num_cores_per_socket`. If specified, the value
supplied to `num_cpus` must be evenly divisible by this value. Default: `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Cpus</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The total number of virtual processor cores to assign
to this virtual machine. Default: `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>poweron<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, that we will be trying to power on a VM
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>Tools<wbr>Scripts<wbr>After<wbr>Power<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
post-power-on scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>Tools<wbr>Scripts<wbr>After<wbr>Resume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
post-resume scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Reboot</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
pre-reboot scripts when VMware tools is installed. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Shutdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution
of pre-shutdown scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Standby</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
pre-standby scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scsi<wbr>Bus<wbr>Sharing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Mode for sharing the SCSI bus. The modes are
physicalSharing, virtualSharing, and noSharing. Default: `noSharing`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scsi<wbr>Controller<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of SCSI controllers that Terraform manages on this virtual machine. This directly affects the amount of disks
you can add to the virtual machine and the maximum disk unit number. Note that lowering this value does not remove
controllers.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scsi<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of SCSI bus this virtual machine will have.
Can be one of lsilogic (LSI Logic Parallel), lsilogic-sas (LSI Logic SAS) or
pvscsi (VMware Paravirtual). Defualt: `pvscsi`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shutdown<wbr>Wait<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to wait
for a graceful guest shutdown when making necessary updates to the virtual
machine. If `force_power_off` is set to true, the VM will be force powered-off
after this timeout, otherwise an error is returned. Default: 3 minutes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the storage policy to assign to this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>swap<wbr>Placement<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The swap file placement policy for this
virtual machine. Can be one of `inherit`, `hostLocal`, or `vmDirectory`.
Default: `inherit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sync<wbr>Time<wbr>With<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable guest clock synchronization with
the host. Requires VMware tools to be installed. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vapp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinevapp">Virtual<wbr>Machine<wbr>Vapp</a></span>
    </dt>
    <dd>{{% md %}}Optional vApp configuration. The only sub-key available
is `properties`, which is a key/value map of properties for virtual machines
imported from OVF or OVA files. See Using vApp properties to supply OVF/OVA
configuration for
more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait<wbr>For<wbr>Guest<wbr>Ip<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to
wait for an available guest IP address on this virtual machine. This should
only be used if your version of VMware Tools does not allow the
`wait_for_guest_net_timeout` waiter to be
used. A value less than 1 disables the waiter. Default: 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait<wbr>For<wbr>Guest<wbr>Net<wbr>Routable</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Controls whether or not the guest
network waiter waits for a routable address. When `false`, the waiter does
not wait for a default gateway, nor are IP addresses checked against any
discovered default gateways as part of its success criteria. This property is
ignored if the `wait_for_guest_ip_timeout`
waiter is used. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait<wbr>For<wbr>Guest<wbr>Net<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to
wait for an available IP address on this virtual machine's NICs. Older
versions of VMware Tools do not populate this property. In those cases, this
waiter can be disabled and the
`wait_for_guest_ip_timeout` waiter can be used
instead. A value less than 1 disables the waiter. Default: 5 minutes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>network_<wbr>interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinenetworkinterface">List[Virtual<wbr>Machine<wbr>Network<wbr>Interface]</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual NIC on this
virtual machine. See network interface options
below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>pool_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the resource pool to put this virtual machine in.
See the section on virtual machine migration
for details on changing this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alternate_<wbr>guest_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The guest name for the operating system
when `guest_id` is `other` or `other-64`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>annotation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A user-provided description of the virtual machine.
The default is no annotation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot_<wbr>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of milliseconds to wait before starting
the boot sequence. The default is no delay.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot_<wbr>retry_<wbr>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of milliseconds to wait before
retrying the boot sequence. This only valid if `boot_retry_enabled` is true.
Default: `10000` (10 seconds).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot_<wbr>retry_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to true, a virtual machine that
fails to boot will try again after the delay defined in `boot_retry_delay`.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cdrom</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinecdrom">Dict[Virtual<wbr>Machine<wbr>Cdrom]</a></span>
    </dt>
    <dd>{{% md %}}A specification for a CDROM device on this virtual
machine. See CDROM options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>clone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclone">Dict[Virtual<wbr>Machine<wbr>Clone]</a></span>
    </dt>
    <dd>{{% md %}}When specified, the VM will be created as a clone of a
specified template. Optional customization options can be submitted as well.
See creating a virtual machine from a
template for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu_<wbr>hot_<wbr>add_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow CPUs to be added to this virtual
machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu_<wbr>hot_<wbr>remove_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow CPUs to be removed to this
virtual machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The maximum amount of CPU (in MHz) that this virtual
machine can consume, regardless of available resources. The default is no
limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu_<wbr>performance_<wbr>counters_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable CPU performance
counters on this virtual machine. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu_<wbr>reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The amount of CPU (in MHz) that this virtual
machine is guaranteed. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of CPU shares allocated to the
virtual machine when the `cpu_share_level` is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The allocation level for CPU resources. Can be
one of `high`, `low`, `normal`, or `custom`. Default: `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual machine. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datastore_<wbr>cluster_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datastore cluster ID to use. This setting
applies to entire virtual machine and implies that you wish to use Storage
DRS with this virtual machine. See the section on virtual machine
migration for details on changing this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datastore_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinedisk">List[Virtual<wbr>Machine<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual disk device on this virtual
machine. See disk options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>efi_<wbr>secure_<wbr>boot_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}When the `firmware` type is set to is
`efi`, this enables EFI secure boot. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>disk_<wbr>uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Expose the UUIDs of attached virtual disks to
the virtual machine, allowing access to them in the guest. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable logging of virtual machine events to a
log file stored in the virtual machine directory. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ept_<wbr>rvi_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The EPT/RVI (hardware memory virtualization)
setting for this virtual machine. Can be one of `automatic`, `on`, or `off`.
Default: `automatic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>extra_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Extra configuration data for this virtual
machine. Can be used to supply advanced parameters not normally in
configuration, such as instance metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>firmware</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The firmware interface to use on the virtual machine.
Can be one of `bios` or `EFI`. Default: `bios`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The path to the folder to put this virtual machine in,
relative to the datacenter that the resource pool is in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force_<wbr>power_<wbr>off</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}If a guest shutdown failed or timed out while
updating or destroying (see
`shutdown_wait_timeout`), force the power-off of
the virtual machine. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The guest ID for the operating system type. For a
full list of possible values, see [here][vmware-docs-guest-ids]. Default: `other-64`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hardware_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The hardware version number. Valid range
is from 4 to 15. The hardware version cannot be downgraded. See [virtual
machine hardware compatibility][virtual-machine-hardware-compatibility] for
more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host_<wbr>system_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}An optional [managed object reference
ID][docs-about-morefs] of a host to put this virtual machine on. See the
section on virtual machine migration for
details on changing this value. If a `host_system_id` is not supplied,
vSphere will select a host in the resource pool to place the virtual machine,
according to any defaults or DRS policies in place.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hv_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The (non-nested) hardware virtualization setting for
this virtual machine. Can be one of `hvAuto`, `hvOn`, or `hvOff`. Default:
`hvAuto`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ignored_<wbr>guest_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}List of IP addresses and CIDR networks to
ignore while waiting for an available IP address using either of the waiters.
Any IP addresses in this list will be ignored if they show up so that the
waiter will continue to wait for a real IP address. Default: [].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>latency_<wbr>sensitivity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Controls the scheduling delay of the
virtual machine. Use a higher sensitivity for applications that require lower
latency, such as VOIP, media player applications, or applications that
require frequent access to mouse or keyboard devices. Can be one of `low`,
`normal`, `medium`, or `high`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The size of the virtual machine's memory, in MB.
Default: `1024` (1 GB).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory_<wbr>hot_<wbr>add_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow memory to be added to this
virtual machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The maximum amount of memory (in MB) that this
virtual machine can consume, regardless of available resources. The default
is no limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory_<wbr>reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The amount of memory (in MB) that this
virtual machine is guaranteed. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of memory shares allocated to
the virtual machine when the `memory_share_level` is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The allocation level for memory resources.
Can be one of `high`, `low`, `normal`, or `custom`. Default: `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>migrate_<wbr>wait_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to wait
for a virtual machine migration to complete before failing. Default: 10
minutes. Also see the section on virtual machine
migration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}An alias for both `label` and `path`, the latter when
using `attach`. Required if not using `label`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nested_<wbr>hv_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable nested hardware virtualization on
this virtual machine, facilitating nested virtualization in the guest.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num_<wbr>cores_<wbr>per_<wbr>socket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of cores per socket in this
virtual machine. The number of vCPUs on the virtual machine will be
`num_cpus` divided by `num_cores_per_socket`. If specified, the value
supplied to `num_cpus` must be evenly divisible by this value. Default: `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num_<wbr>cpus</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The total number of virtual processor cores to assign
to this virtual machine. Default: `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>poweron_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, that we will be trying to power on a VM
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run_<wbr>tools_<wbr>scripts_<wbr>after_<wbr>power_<wbr>on</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
post-power-on scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run_<wbr>tools_<wbr>scripts_<wbr>after_<wbr>resume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
post-resume scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run_<wbr>tools_<wbr>scripts_<wbr>before_<wbr>guest_<wbr>reboot</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
pre-reboot scripts when VMware tools is installed. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run_<wbr>tools_<wbr>scripts_<wbr>before_<wbr>guest_<wbr>shutdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution
of pre-shutdown scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run_<wbr>tools_<wbr>scripts_<wbr>before_<wbr>guest_<wbr>standby</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
pre-standby scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scsi_<wbr>bus_<wbr>sharing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Mode for sharing the SCSI bus. The modes are
physicalSharing, virtualSharing, and noSharing. Default: `noSharing`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scsi_<wbr>controller_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of SCSI controllers that Terraform manages on this virtual machine. This directly affects the amount of disks
you can add to the virtual machine and the maximum disk unit number. Note that lowering this value does not remove
controllers.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scsi_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of SCSI bus this virtual machine will have.
Can be one of lsilogic (LSI Logic Parallel), lsilogic-sas (LSI Logic SAS) or
pvscsi (VMware Paravirtual). Defualt: `pvscsi`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shutdown_<wbr>wait_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to wait
for a graceful guest shutdown when making necessary updates to the virtual
machine. If `force_power_off` is set to true, the VM will be force powered-off
after this timeout, otherwise an error is returned. Default: 3 minutes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>policy_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the storage policy to assign to this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>swap_<wbr>placement_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The swap file placement policy for this
virtual machine. Can be one of `inherit`, `hostLocal`, or `vmDirectory`.
Default: `inherit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sync_<wbr>time_<wbr>with_<wbr>host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable guest clock synchronization with
the host. Requires VMware tools to be installed. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vapp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinevapp">Dict[Virtual<wbr>Machine<wbr>Vapp]</a></span>
    </dt>
    <dd>{{% md %}}Optional vApp configuration. The only sub-key available
is `properties`, which is a key/value map of properties for virtual machines
imported from OVF or OVA files. See Using vApp properties to supply OVF/OVA
configuration for
more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait_<wbr>for_<wbr>guest_<wbr>ip_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to
wait for an available guest IP address on this virtual machine. This should
only be used if your version of VMware Tools does not allow the
`wait_for_guest_net_timeout` waiter to be
used. A value less than 1 disables the waiter. Default: 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait_<wbr>for_<wbr>guest_<wbr>net_<wbr>routable</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Controls whether or not the guest
network waiter waits for a routable address. When `false`, the waiter does
not wait for a default gateway, nor are IP addresses checked against any
discovered default gateways as part of its success criteria. This property is
ignored if the `wait_for_guest_ip_timeout`
waiter is used. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait_<wbr>for_<wbr>guest_<wbr>net_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to
wait for an available IP address on this virtual machine's NICs. Older
versions of VMware Tools do not populate this property. In those cases, this
waiter can be disabled and the
`wait_for_guest_ip_timeout` waiter can be used
instead. A value less than 1 disables the waiter. Default: 5 minutes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## VirtualMachine Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Change<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A unique identifier for a given version of the last
configuration applied, such the timestamp of the last update to the
configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The IP address selected by Terraform to be used for the provisioner.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Guest<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The current list of IP addresses on this machine,
including the value of `default_ip_address`. If VMware tools is not running
on the virtual machine, or if the VM is powered off, this list will be empty.
* `moid`: The [managed object reference ID][docs-about-morefs] of the created
virtual machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Imported</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}This is flagged if the virtual machine has been imported, or the
state has been migrated from a previous version of the resource. It
influences the behavior of the first post-import apply operation. See the
section on importing below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Moid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The machine object ID from VMWare
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Reboot<wbr>Required</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Value internal to Terraform used to determine if a configuration set change requires a reboot.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual disk's VMDK file. This is used to track the
virtual disk on the virtual machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vapp<wbr>Transports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}Computed value which is only valid for cloned virtual
machines. A list of vApp transport methods supported by the source virtual
machine or template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vmware<wbr>Tools<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The state of VMware tools in the guest. This will
determine the proper course of action for some device operations.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vmx<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The path of the virtual machine's configuration file in the VM's
datastore.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Change<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A unique identifier for a given version of the last
configuration applied, such the timestamp of the last update to the
configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The IP address selected by Terraform to be used for the provisioner.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Guest<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The current list of IP addresses on this machine,
including the value of `default_ip_address`. If VMware tools is not running
on the virtual machine, or if the VM is powered off, this list will be empty.
* `moid`: The [managed object reference ID][docs-about-morefs] of the created
virtual machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Imported</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}This is flagged if the virtual machine has been imported, or the
state has been migrated from a previous version of the resource. It
influences the behavior of the first post-import apply operation. See the
section on importing below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Moid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The machine object ID from VMWare
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Reboot<wbr>Required</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Value internal to Terraform used to determine if a configuration set change requires a reboot.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual disk's VMDK file. This is used to track the
virtual disk on the virtual machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vapp<wbr>Transports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}Computed value which is only valid for cloned virtual
machines. A list of vApp transport methods supported by the source virtual
machine or template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vmware<wbr>Tools<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The state of VMware tools in the guest. This will
determine the proper course of action for some device operations.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vmx<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The path of the virtual machine's configuration file in the VM's
datastore.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>change<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A unique identifier for a given version of the last
configuration applied, such the timestamp of the last update to the
configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The IP address selected by Terraform to be used for the provisioner.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>guest<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The current list of IP addresses on this machine,
including the value of `default_ip_address`. If VMware tools is not running
on the virtual machine, or if the VM is powered off, this list will be empty.
* `moid`: The [managed object reference ID][docs-about-morefs] of the created
virtual machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>imported</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}This is flagged if the virtual machine has been imported, or the
state has been migrated from a previous version of the resource. It
influences the behavior of the first post-import apply operation. See the
section on importing below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>moid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The machine object ID from VMWare
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>reboot<wbr>Required</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Value internal to Terraform used to determine if a configuration set change requires a reboot.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual disk's VMDK file. This is used to track the
virtual disk on the virtual machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vapp<wbr>Transports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}Computed value which is only valid for cloned virtual
machines. A list of vApp transport methods supported by the source virtual
machine or template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vmware<wbr>Tools<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The state of VMware tools in the guest. This will
determine the proper course of action for some device operations.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vmx<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The path of the virtual machine's configuration file in the VM's
datastore.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>change_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A unique identifier for a given version of the last
configuration applied, such the timestamp of the last update to the
configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The IP address selected by Terraform to be used for the provisioner.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>guest_<wbr>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The current list of IP addresses on this machine,
including the value of `default_ip_address`. If VMware tools is not running
on the virtual machine, or if the VM is powered off, this list will be empty.
* `moid`: The [managed object reference ID][docs-about-morefs] of the created
virtual machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>imported</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}This is flagged if the virtual machine has been imported, or the
state has been migrated from a previous version of the resource. It
influences the behavior of the first post-import apply operation. See the
section on importing below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>moid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The machine object ID from VMWare
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>reboot_<wbr>required</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Value internal to Terraform used to determine if a configuration set change requires a reboot.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual disk's VMDK file. This is used to track the
virtual disk on the virtual machine.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vapp_<wbr>transports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}Computed value which is only valid for cloned virtual
machines. A list of vApp transport methods supported by the source virtual
machine or template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vmware_<wbr>tools_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The state of VMware tools in the guest. This will
determine the proper course of action for some device operations.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vmx_<wbr>path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The path of the virtual machine's configuration file in the VM's
datastore.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing VirtualMachine Resource

Get an existing VirtualMachine resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#VirtualMachineState">VirtualMachineState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#VirtualMachine">VirtualMachine</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>alternate_guest_name=None<span class="p">, </span>annotation=None<span class="p">, </span>boot_delay=None<span class="p">, </span>boot_retry_delay=None<span class="p">, </span>boot_retry_enabled=None<span class="p">, </span>cdrom=None<span class="p">, </span>change_version=None<span class="p">, </span>clone=None<span class="p">, </span>cpu_hot_add_enabled=None<span class="p">, </span>cpu_hot_remove_enabled=None<span class="p">, </span>cpu_limit=None<span class="p">, </span>cpu_performance_counters_enabled=None<span class="p">, </span>cpu_reservation=None<span class="p">, </span>cpu_share_count=None<span class="p">, </span>cpu_share_level=None<span class="p">, </span>custom_attributes=None<span class="p">, </span>datastore_cluster_id=None<span class="p">, </span>datastore_id=None<span class="p">, </span>default_ip_address=None<span class="p">, </span>disks=None<span class="p">, </span>efi_secure_boot_enabled=None<span class="p">, </span>enable_disk_uuid=None<span class="p">, </span>enable_logging=None<span class="p">, </span>ept_rvi_mode=None<span class="p">, </span>extra_config=None<span class="p">, </span>firmware=None<span class="p">, </span>folder=None<span class="p">, </span>force_power_off=None<span class="p">, </span>guest_id=None<span class="p">, </span>guest_ip_addresses=None<span class="p">, </span>hardware_version=None<span class="p">, </span>host_system_id=None<span class="p">, </span>hv_mode=None<span class="p">, </span>ignored_guest_ips=None<span class="p">, </span>imported=None<span class="p">, </span>latency_sensitivity=None<span class="p">, </span>memory=None<span class="p">, </span>memory_hot_add_enabled=None<span class="p">, </span>memory_limit=None<span class="p">, </span>memory_reservation=None<span class="p">, </span>memory_share_count=None<span class="p">, </span>memory_share_level=None<span class="p">, </span>migrate_wait_timeout=None<span class="p">, </span>moid=None<span class="p">, </span>name=None<span class="p">, </span>nested_hv_enabled=None<span class="p">, </span>network_interfaces=None<span class="p">, </span>num_cores_per_socket=None<span class="p">, </span>num_cpus=None<span class="p">, </span>poweron_timeout=None<span class="p">, </span>reboot_required=None<span class="p">, </span>resource_pool_id=None<span class="p">, </span>run_tools_scripts_after_power_on=None<span class="p">, </span>run_tools_scripts_after_resume=None<span class="p">, </span>run_tools_scripts_before_guest_reboot=None<span class="p">, </span>run_tools_scripts_before_guest_shutdown=None<span class="p">, </span>run_tools_scripts_before_guest_standby=None<span class="p">, </span>scsi_bus_sharing=None<span class="p">, </span>scsi_controller_count=None<span class="p">, </span>scsi_type=None<span class="p">, </span>shutdown_wait_timeout=None<span class="p">, </span>storage_policy_id=None<span class="p">, </span>swap_placement_policy=None<span class="p">, </span>sync_time_with_host=None<span class="p">, </span>tags=None<span class="p">, </span>uuid=None<span class="p">, </span>vapp=None<span class="p">, </span>vapp_transports=None<span class="p">, </span>vmware_tools_status=None<span class="p">, </span>vmx_path=None<span class="p">, </span>wait_for_guest_ip_timeout=None<span class="p">, </span>wait_for_guest_net_routable=None<span class="p">, </span>wait_for_guest_net_timeout=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetVirtualMachine<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineState">VirtualMachineState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachine">VirtualMachine</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere.VirtualMachine.html">VirtualMachine</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere..VirtualMachineState.html">VirtualMachineState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Alternate<wbr>Guest<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The guest name for the operating system
when `guest_id` is `other` or `other-64`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Annotation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A user-provided description of the virtual machine.
The default is no annotation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of milliseconds to wait before starting
the boot sequence. The default is no delay.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Retry<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of milliseconds to wait before
retrying the boot sequence. This only valid if `boot_retry_enabled` is true.
Default: `10000` (10 seconds).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Retry<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to true, a virtual machine that
fails to boot will try again after the delay defined in `boot_retry_delay`.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cdrom</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinecdrom">Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Virtual<wbr>Machine<wbr>Cdrom<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A specification for a CDROM device on this virtual
machine. See CDROM options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Change<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A unique identifier for a given version of the last
configuration applied, such the timestamp of the last update to the
configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Clone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclone">Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Virtual<wbr>Machine<wbr>Clone<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}When specified, the VM will be created as a clone of a
specified template. Optional customization options can be submitted as well.
See creating a virtual machine from a
template for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Hot<wbr>Add<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow CPUs to be added to this virtual
machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Hot<wbr>Remove<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow CPUs to be removed to this
virtual machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum amount of CPU (in MHz) that this virtual
machine can consume, regardless of available resources. The default is no
limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Performance<wbr>Counters<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable CPU performance
counters on this virtual machine. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of CPU (in MHz) that this virtual
machine is guaranteed. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of CPU shares allocated to the
virtual machine when the `cpu_share_level` is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The allocation level for CPU resources. Can be
one of `high`, `low`, `normal`, or `custom`. Default: `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual machine. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datastore cluster ID to use. This setting
applies to entire virtual machine and implies that you wish to use Storage
DRS with this virtual machine. See the section on virtual machine
migration for details on changing this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datastore<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The IP address selected by Terraform to be used for the provisioner.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinedisk">List&lt;Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Virtual<wbr>Machine<wbr>Disk<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual disk device on this virtual
machine. See disk options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Efi<wbr>Secure<wbr>Boot<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}When the `firmware` type is set to is
`efi`, this enables EFI secure boot. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Disk<wbr>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Expose the UUIDs of attached virtual disks to
the virtual machine, allowing access to them in the guest. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable logging of virtual machine events to a
log file stored in the virtual machine directory. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ept<wbr>Rvi<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The EPT/RVI (hardware memory virtualization)
setting for this virtual machine. Can be one of `automatic`, `on`, or `off`.
Default: `automatic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Extra<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}Extra configuration data for this virtual
machine. Can be used to supply advanced parameters not normally in
configuration, such as instance metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Firmware</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The firmware interface to use on the virtual machine.
Can be one of `bios` or `EFI`. Default: `bios`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The path to the folder to put this virtual machine in,
relative to the datacenter that the resource pool is in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Power<wbr>Off</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}If a guest shutdown failed or timed out while
updating or destroying (see
`shutdown_wait_timeout`), force the power-off of
the virtual machine. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The guest ID for the operating system type. For a
full list of possible values, see [here][vmware-docs-guest-ids]. Default: `other-64`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The current list of IP addresses on this machine,
including the value of `default_ip_address`. If VMware tools is not running
on the virtual machine, or if the VM is powered off, this list will be empty.
* `moid`: The [managed object reference ID][docs-about-morefs] of the created
virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hardware<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The hardware version number. Valid range
is from 4 to 15. The hardware version cannot be downgraded. See [virtual
machine hardware compatibility][virtual-machine-hardware-compatibility] for
more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>System<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}An optional [managed object reference
ID][docs-about-morefs] of a host to put this virtual machine on. See the
section on virtual machine migration for
details on changing this value. If a `host_system_id` is not supplied,
vSphere will select a host in the resource pool to place the virtual machine,
according to any defaults or DRS policies in place.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hv<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The (non-nested) hardware virtualization setting for
this virtual machine. Can be one of `hvAuto`, `hvOn`, or `hvOff`. Default:
`hvAuto`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ignored<wbr>Guest<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}List of IP addresses and CIDR networks to
ignore while waiting for an available IP address using either of the waiters.
Any IP addresses in this list will be ignored if they show up so that the
waiter will continue to wait for a real IP address. Default: [].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Imported</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}This is flagged if the virtual machine has been imported, or the
state has been migrated from a previous version of the resource. It
influences the behavior of the first post-import apply operation. See the
section on importing below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Latency<wbr>Sensitivity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the scheduling delay of the
virtual machine. Use a higher sensitivity for applications that require lower
latency, such as VOIP, media player applications, or applications that
require frequent access to mouse or keyboard devices. Can be one of `low`,
`normal`, `medium`, or `high`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The size of the virtual machine's memory, in MB.
Default: `1024` (1 GB).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Hot<wbr>Add<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow memory to be added to this
virtual machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum amount of memory (in MB) that this
virtual machine can consume, regardless of available resources. The default
is no limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of memory (in MB) that this
virtual machine is guaranteed. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of memory shares allocated to
the virtual machine when the `memory_share_level` is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The allocation level for memory resources.
Can be one of `high`, `low`, `normal`, or `custom`. Default: `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Migrate<wbr>Wait<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to wait
for a virtual machine migration to complete before failing. Default: 10
minutes. Also see the section on virtual machine
migration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Moid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The machine object ID from VMWare
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}An alias for both `label` and `path`, the latter when
using `attach`. Required if not using `label`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nested<wbr>Hv<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable nested hardware virtualization on
this virtual machine, facilitating nested virtualization in the guest.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinenetworkinterface">List&lt;Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Virtual<wbr>Machine<wbr>Network<wbr>Interface<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual NIC on this
virtual machine. See network interface options
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Cores<wbr>Per<wbr>Socket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of cores per socket in this
virtual machine. The number of vCPUs on the virtual machine will be
`num_cpus` divided by `num_cores_per_socket`. If specified, the value
supplied to `num_cpus` must be evenly divisible by this value. Default: `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Cpus</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The total number of virtual processor cores to assign
to this virtual machine. Default: `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Poweron<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, that we will be trying to power on a VM
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reboot<wbr>Required</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Value internal to Terraform used to determine if a configuration set change requires a reboot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the resource pool to put this virtual machine in.
See the section on virtual machine migration
for details on changing this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>After<wbr>Power<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
post-power-on scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>After<wbr>Resume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
post-resume scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Reboot</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
pre-reboot scripts when VMware tools is installed. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Shutdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution
of pre-shutdown scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Standby</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
pre-standby scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scsi<wbr>Bus<wbr>Sharing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Mode for sharing the SCSI bus. The modes are
physicalSharing, virtualSharing, and noSharing. Default: `noSharing`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scsi<wbr>Controller<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of SCSI controllers that Terraform manages on this virtual machine. This directly affects the amount of disks
you can add to the virtual machine and the maximum disk unit number. Note that lowering this value does not remove
controllers.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scsi<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of SCSI bus this virtual machine will have.
Can be one of lsilogic (LSI Logic Parallel), lsilogic-sas (LSI Logic SAS) or
pvscsi (VMware Paravirtual). Defualt: `pvscsi`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shutdown<wbr>Wait<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to wait
for a graceful guest shutdown when making necessary updates to the virtual
machine. If `force_power_off` is set to true, the VM will be force powered-off
after this timeout, otherwise an error is returned. Default: 3 minutes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the storage policy to assign to this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Swap<wbr>Placement<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The swap file placement policy for this
virtual machine. Can be one of `inherit`, `hostLocal`, or `vmDirectory`.
Default: `inherit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sync<wbr>Time<wbr>With<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable guest clock synchronization with
the host. Requires VMware tools to be installed. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual disk's VMDK file. This is used to track the
virtual disk on the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vapp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinevapp">Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Virtual<wbr>Machine<wbr>Vapp<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Optional vApp configuration. The only sub-key available
is `properties`, which is a key/value map of properties for virtual machines
imported from OVF or OVA files. See Using vApp properties to supply OVF/OVA
configuration for
more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vapp<wbr>Transports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}Computed value which is only valid for cloned virtual
machines. A list of vApp transport methods supported by the source virtual
machine or template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmware<wbr>Tools<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The state of VMware tools in the guest. This will
determine the proper course of action for some device operations.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmx<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The path of the virtual machine's configuration file in the VM's
datastore.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait<wbr>For<wbr>Guest<wbr>Ip<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to
wait for an available guest IP address on this virtual machine. This should
only be used if your version of VMware Tools does not allow the
`wait_for_guest_net_timeout` waiter to be
used. A value less than 1 disables the waiter. Default: 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait<wbr>For<wbr>Guest<wbr>Net<wbr>Routable</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Controls whether or not the guest
network waiter waits for a routable address. When `false`, the waiter does
not wait for a default gateway, nor are IP addresses checked against any
discovered default gateways as part of its success criteria. This property is
ignored if the `wait_for_guest_ip_timeout`
waiter is used. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait<wbr>For<wbr>Guest<wbr>Net<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to
wait for an available IP address on this virtual machine's NICs. Older
versions of VMware Tools do not populate this property. In those cases, this
waiter can be disabled and the
`wait_for_guest_ip_timeout` waiter can be used
instead. A value less than 1 disables the waiter. Default: 5 minutes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Alternate<wbr>Guest<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The guest name for the operating system
when `guest_id` is `other` or `other-64`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Annotation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A user-provided description of the virtual machine.
The default is no annotation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of milliseconds to wait before starting
the boot sequence. The default is no delay.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Retry<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of milliseconds to wait before
retrying the boot sequence. This only valid if `boot_retry_enabled` is true.
Default: `10000` (10 seconds).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Retry<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to true, a virtual machine that
fails to boot will try again after the delay defined in `boot_retry_delay`.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cdrom</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinecdrom">Virtual<wbr>Machine<wbr>Cdrom</a></span>
    </dt>
    <dd>{{% md %}}A specification for a CDROM device on this virtual
machine. See CDROM options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Change<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A unique identifier for a given version of the last
configuration applied, such the timestamp of the last update to the
configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Clone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclone">Virtual<wbr>Machine<wbr>Clone</a></span>
    </dt>
    <dd>{{% md %}}When specified, the VM will be created as a clone of a
specified template. Optional customization options can be submitted as well.
See creating a virtual machine from a
template for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Hot<wbr>Add<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow CPUs to be added to this virtual
machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Hot<wbr>Remove<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow CPUs to be removed to this
virtual machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum amount of CPU (in MHz) that this virtual
machine can consume, regardless of available resources. The default is no
limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Performance<wbr>Counters<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable CPU performance
counters on this virtual machine. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of CPU (in MHz) that this virtual
machine is guaranteed. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of CPU shares allocated to the
virtual machine when the `cpu_share_level` is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The allocation level for CPU resources. Can be
one of `high`, `low`, `normal`, or `custom`. Default: `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual machine. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datastore cluster ID to use. This setting
applies to entire virtual machine and implies that you wish to use Storage
DRS with this virtual machine. See the section on virtual machine
migration for details on changing this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datastore<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The IP address selected by Terraform to be used for the provisioner.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinedisk">[]Virtual<wbr>Machine<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual disk device on this virtual
machine. See disk options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Efi<wbr>Secure<wbr>Boot<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}When the `firmware` type is set to is
`efi`, this enables EFI secure boot. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Disk<wbr>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Expose the UUIDs of attached virtual disks to
the virtual machine, allowing access to them in the guest. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable logging of virtual machine events to a
log file stored in the virtual machine directory. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ept<wbr>Rvi<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The EPT/RVI (hardware memory virtualization)
setting for this virtual machine. Can be one of `automatic`, `on`, or `off`.
Default: `automatic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Extra<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Extra configuration data for this virtual
machine. Can be used to supply advanced parameters not normally in
configuration, such as instance metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Firmware</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The firmware interface to use on the virtual machine.
Can be one of `bios` or `EFI`. Default: `bios`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The path to the folder to put this virtual machine in,
relative to the datacenter that the resource pool is in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Power<wbr>Off</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}If a guest shutdown failed or timed out while
updating or destroying (see
`shutdown_wait_timeout`), force the power-off of
the virtual machine. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The guest ID for the operating system type. For a
full list of possible values, see [here][vmware-docs-guest-ids]. Default: `other-64`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The current list of IP addresses on this machine,
including the value of `default_ip_address`. If VMware tools is not running
on the virtual machine, or if the VM is powered off, this list will be empty.
* `moid`: The [managed object reference ID][docs-about-morefs] of the created
virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hardware<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The hardware version number. Valid range
is from 4 to 15. The hardware version cannot be downgraded. See [virtual
machine hardware compatibility][virtual-machine-hardware-compatibility] for
more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host<wbr>System<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional [managed object reference
ID][docs-about-morefs] of a host to put this virtual machine on. See the
section on virtual machine migration for
details on changing this value. If a `host_system_id` is not supplied,
vSphere will select a host in the resource pool to place the virtual machine,
according to any defaults or DRS policies in place.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hv<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The (non-nested) hardware virtualization setting for
this virtual machine. Can be one of `hvAuto`, `hvOn`, or `hvOff`. Default:
`hvAuto`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ignored<wbr>Guest<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}List of IP addresses and CIDR networks to
ignore while waiting for an available IP address using either of the waiters.
Any IP addresses in this list will be ignored if they show up so that the
waiter will continue to wait for a real IP address. Default: [].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Imported</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}This is flagged if the virtual machine has been imported, or the
state has been migrated from a previous version of the resource. It
influences the behavior of the first post-import apply operation. See the
section on importing below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Latency<wbr>Sensitivity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the scheduling delay of the
virtual machine. Use a higher sensitivity for applications that require lower
latency, such as VOIP, media player applications, or applications that
require frequent access to mouse or keyboard devices. Can be one of `low`,
`normal`, `medium`, or `high`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The size of the virtual machine's memory, in MB.
Default: `1024` (1 GB).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Hot<wbr>Add<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow memory to be added to this
virtual machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum amount of memory (in MB) that this
virtual machine can consume, regardless of available resources. The default
is no limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of memory (in MB) that this
virtual machine is guaranteed. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of memory shares allocated to
the virtual machine when the `memory_share_level` is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The allocation level for memory resources.
Can be one of `high`, `low`, `normal`, or `custom`. Default: `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Migrate<wbr>Wait<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to wait
for a virtual machine migration to complete before failing. Default: 10
minutes. Also see the section on virtual machine
migration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Moid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The machine object ID from VMWare
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}An alias for both `label` and `path`, the latter when
using `attach`. Required if not using `label`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nested<wbr>Hv<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable nested hardware virtualization on
this virtual machine, facilitating nested virtualization in the guest.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinenetworkinterface">[]Virtual<wbr>Machine<wbr>Network<wbr>Interface</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual NIC on this
virtual machine. See network interface options
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Cores<wbr>Per<wbr>Socket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of cores per socket in this
virtual machine. The number of vCPUs on the virtual machine will be
`num_cpus` divided by `num_cores_per_socket`. If specified, the value
supplied to `num_cpus` must be evenly divisible by this value. Default: `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Cpus</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The total number of virtual processor cores to assign
to this virtual machine. Default: `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Poweron<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, that we will be trying to power on a VM
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reboot<wbr>Required</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Value internal to Terraform used to determine if a configuration set change requires a reboot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the resource pool to put this virtual machine in.
See the section on virtual machine migration
for details on changing this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>After<wbr>Power<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
post-power-on scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>After<wbr>Resume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
post-resume scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Reboot</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
pre-reboot scripts when VMware tools is installed. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Shutdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution
of pre-shutdown scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Standby</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
pre-standby scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scsi<wbr>Bus<wbr>Sharing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Mode for sharing the SCSI bus. The modes are
physicalSharing, virtualSharing, and noSharing. Default: `noSharing`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scsi<wbr>Controller<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of SCSI controllers that Terraform manages on this virtual machine. This directly affects the amount of disks
you can add to the virtual machine and the maximum disk unit number. Note that lowering this value does not remove
controllers.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scsi<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of SCSI bus this virtual machine will have.
Can be one of lsilogic (LSI Logic Parallel), lsilogic-sas (LSI Logic SAS) or
pvscsi (VMware Paravirtual). Defualt: `pvscsi`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shutdown<wbr>Wait<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to wait
for a graceful guest shutdown when making necessary updates to the virtual
machine. If `force_power_off` is set to true, the VM will be force powered-off
after this timeout, otherwise an error is returned. Default: 3 minutes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the storage policy to assign to this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Swap<wbr>Placement<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The swap file placement policy for this
virtual machine. Can be one of `inherit`, `hostLocal`, or `vmDirectory`.
Default: `inherit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sync<wbr>Time<wbr>With<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable guest clock synchronization with
the host. Requires VMware tools to be installed. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual disk's VMDK file. This is used to track the
virtual disk on the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vapp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinevapp">Virtual<wbr>Machine<wbr>Vapp</a></span>
    </dt>
    <dd>{{% md %}}Optional vApp configuration. The only sub-key available
is `properties`, which is a key/value map of properties for virtual machines
imported from OVF or OVA files. See Using vApp properties to supply OVF/OVA
configuration for
more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vapp<wbr>Transports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}Computed value which is only valid for cloned virtual
machines. A list of vApp transport methods supported by the source virtual
machine or template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmware<wbr>Tools<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The state of VMware tools in the guest. This will
determine the proper course of action for some device operations.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmx<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The path of the virtual machine's configuration file in the VM's
datastore.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait<wbr>For<wbr>Guest<wbr>Ip<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to
wait for an available guest IP address on this virtual machine. This should
only be used if your version of VMware Tools does not allow the
`wait_for_guest_net_timeout` waiter to be
used. A value less than 1 disables the waiter. Default: 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait<wbr>For<wbr>Guest<wbr>Net<wbr>Routable</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Controls whether or not the guest
network waiter waits for a routable address. When `false`, the waiter does
not wait for a default gateway, nor are IP addresses checked against any
discovered default gateways as part of its success criteria. This property is
ignored if the `wait_for_guest_ip_timeout`
waiter is used. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Wait<wbr>For<wbr>Guest<wbr>Net<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to
wait for an available IP address on this virtual machine's NICs. Older
versions of VMware Tools do not populate this property. In those cases, this
waiter can be disabled and the
`wait_for_guest_ip_timeout` waiter can be used
instead. A value less than 1 disables the waiter. Default: 5 minutes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alternate<wbr>Guest<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The guest name for the operating system
when `guest_id` is `other` or `other-64`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>annotation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A user-provided description of the virtual machine.
The default is no annotation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of milliseconds to wait before starting
the boot sequence. The default is no delay.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Retry<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of milliseconds to wait before
retrying the boot sequence. This only valid if `boot_retry_enabled` is true.
Default: `10000` (10 seconds).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Retry<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}If set to true, a virtual machine that
fails to boot will try again after the delay defined in `boot_retry_delay`.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cdrom</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinecdrom">Virtual<wbr>Machine<wbr>Cdrom</a></span>
    </dt>
    <dd>{{% md %}}A specification for a CDROM device on this virtual
machine. See CDROM options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>change<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A unique identifier for a given version of the last
configuration applied, such the timestamp of the last update to the
configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>clone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclone">Virtual<wbr>Machine<wbr>Clone</a></span>
    </dt>
    <dd>{{% md %}}When specified, the VM will be created as a clone of a
specified template. Optional customization options can be submitted as well.
See creating a virtual machine from a
template for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu<wbr>Hot<wbr>Add<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Allow CPUs to be added to this virtual
machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu<wbr>Hot<wbr>Remove<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Allow CPUs to be removed to this
virtual machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The maximum amount of CPU (in MHz) that this virtual
machine can consume, regardless of available resources. The default is no
limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu<wbr>Performance<wbr>Counters<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable CPU performance
counters on this virtual machine. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The amount of CPU (in MHz) that this virtual
machine is guaranteed. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of CPU shares allocated to the
virtual machine when the `cpu_share_level` is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The allocation level for CPU resources. Can be
one of `high`, `low`, `normal`, or `custom`. Default: `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual machine. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datastore<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datastore cluster ID to use. This setting
applies to entire virtual machine and implies that you wish to use Storage
DRS with this virtual machine. See the section on virtual machine
migration for details on changing this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datastore<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The IP address selected by Terraform to be used for the provisioner.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinedisk">Virtual<wbr>Machine<wbr>Disk[]</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual disk device on this virtual
machine. See disk options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>efi<wbr>Secure<wbr>Boot<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}When the `firmware` type is set to is
`efi`, this enables EFI secure boot. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Disk<wbr>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Expose the UUIDs of attached virtual disks to
the virtual machine, allowing access to them in the guest. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable logging of virtual machine events to a
log file stored in the virtual machine directory. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ept<wbr>Rvi<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The EPT/RVI (hardware memory virtualization)
setting for this virtual machine. Can be one of `automatic`, `on`, or `off`.
Default: `automatic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>extra<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}Extra configuration data for this virtual
machine. Can be used to supply advanced parameters not normally in
configuration, such as instance metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>firmware</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The firmware interface to use on the virtual machine.
Can be one of `bios` or `EFI`. Default: `bios`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The path to the folder to put this virtual machine in,
relative to the datacenter that the resource pool is in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force<wbr>Power<wbr>Off</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}If a guest shutdown failed or timed out while
updating or destroying (see
`shutdown_wait_timeout`), force the power-off of
the virtual machine. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The guest ID for the operating system type. For a
full list of possible values, see [here][vmware-docs-guest-ids]. Default: `other-64`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The current list of IP addresses on this machine,
including the value of `default_ip_address`. If VMware tools is not running
on the virtual machine, or if the VM is powered off, this list will be empty.
* `moid`: The [managed object reference ID][docs-about-morefs] of the created
virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hardware<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The hardware version number. Valid range
is from 4 to 15. The hardware version cannot be downgraded. See [virtual
machine hardware compatibility][virtual-machine-hardware-compatibility] for
more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host<wbr>System<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional [managed object reference
ID][docs-about-morefs] of a host to put this virtual machine on. See the
section on virtual machine migration for
details on changing this value. If a `host_system_id` is not supplied,
vSphere will select a host in the resource pool to place the virtual machine,
according to any defaults or DRS policies in place.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hv<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The (non-nested) hardware virtualization setting for
this virtual machine. Can be one of `hvAuto`, `hvOn`, or `hvOff`. Default:
`hvAuto`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ignored<wbr>Guest<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}List of IP addresses and CIDR networks to
ignore while waiting for an available IP address using either of the waiters.
Any IP addresses in this list will be ignored if they show up so that the
waiter will continue to wait for a real IP address. Default: [].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>imported</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}This is flagged if the virtual machine has been imported, or the
state has been migrated from a previous version of the resource. It
influences the behavior of the first post-import apply operation. See the
section on importing below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>latency<wbr>Sensitivity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the scheduling delay of the
virtual machine. Use a higher sensitivity for applications that require lower
latency, such as VOIP, media player applications, or applications that
require frequent access to mouse or keyboard devices. Can be one of `low`,
`normal`, `medium`, or `high`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The size of the virtual machine's memory, in MB.
Default: `1024` (1 GB).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory<wbr>Hot<wbr>Add<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Allow memory to be added to this
virtual machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The maximum amount of memory (in MB) that this
virtual machine can consume, regardless of available resources. The default
is no limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The amount of memory (in MB) that this
virtual machine is guaranteed. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of memory shares allocated to
the virtual machine when the `memory_share_level` is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The allocation level for memory resources.
Can be one of `high`, `low`, `normal`, or `custom`. Default: `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>migrate<wbr>Wait<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to wait
for a virtual machine migration to complete before failing. Default: 10
minutes. Also see the section on virtual machine
migration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>moid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The machine object ID from VMWare
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}An alias for both `label` and `path`, the latter when
using `attach`. Required if not using `label`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nested<wbr>Hv<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable nested hardware virtualization on
this virtual machine, facilitating nested virtualization in the guest.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinenetworkinterface">Virtual<wbr>Machine<wbr>Network<wbr>Interface[]</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual NIC on this
virtual machine. See network interface options
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Cores<wbr>Per<wbr>Socket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of cores per socket in this
virtual machine. The number of vCPUs on the virtual machine will be
`num_cpus` divided by `num_cores_per_socket`. If specified, the value
supplied to `num_cpus` must be evenly divisible by this value. Default: `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Cpus</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The total number of virtual processor cores to assign
to this virtual machine. Default: `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>poweron<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, that we will be trying to power on a VM
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reboot<wbr>Required</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Value internal to Terraform used to determine if a configuration set change requires a reboot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the resource pool to put this virtual machine in.
See the section on virtual machine migration
for details on changing this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>Tools<wbr>Scripts<wbr>After<wbr>Power<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
post-power-on scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>Tools<wbr>Scripts<wbr>After<wbr>Resume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
post-resume scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Reboot</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
pre-reboot scripts when VMware tools is installed. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Shutdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution
of pre-shutdown scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>Tools<wbr>Scripts<wbr>Before<wbr>Guest<wbr>Standby</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
pre-standby scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scsi<wbr>Bus<wbr>Sharing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Mode for sharing the SCSI bus. The modes are
physicalSharing, virtualSharing, and noSharing. Default: `noSharing`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scsi<wbr>Controller<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of SCSI controllers that Terraform manages on this virtual machine. This directly affects the amount of disks
you can add to the virtual machine and the maximum disk unit number. Note that lowering this value does not remove
controllers.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scsi<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of SCSI bus this virtual machine will have.
Can be one of lsilogic (LSI Logic Parallel), lsilogic-sas (LSI Logic SAS) or
pvscsi (VMware Paravirtual). Defualt: `pvscsi`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shutdown<wbr>Wait<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to wait
for a graceful guest shutdown when making necessary updates to the virtual
machine. If `force_power_off` is set to true, the VM will be force powered-off
after this timeout, otherwise an error is returned. Default: 3 minutes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the storage policy to assign to this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>swap<wbr>Placement<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The swap file placement policy for this
virtual machine. Can be one of `inherit`, `hostLocal`, or `vmDirectory`.
Default: `inherit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sync<wbr>Time<wbr>With<wbr>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Enable guest clock synchronization with
the host. Requires VMware tools to be installed. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual disk's VMDK file. This is used to track the
virtual disk on the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vapp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinevapp">Virtual<wbr>Machine<wbr>Vapp</a></span>
    </dt>
    <dd>{{% md %}}Optional vApp configuration. The only sub-key available
is `properties`, which is a key/value map of properties for virtual machines
imported from OVF or OVA files. See Using vApp properties to supply OVF/OVA
configuration for
more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vapp<wbr>Transports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}Computed value which is only valid for cloned virtual
machines. A list of vApp transport methods supported by the source virtual
machine or template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmware<wbr>Tools<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The state of VMware tools in the guest. This will
determine the proper course of action for some device operations.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmx<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The path of the virtual machine's configuration file in the VM's
datastore.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait<wbr>For<wbr>Guest<wbr>Ip<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to
wait for an available guest IP address on this virtual machine. This should
only be used if your version of VMware Tools does not allow the
`wait_for_guest_net_timeout` waiter to be
used. A value less than 1 disables the waiter. Default: 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait<wbr>For<wbr>Guest<wbr>Net<wbr>Routable</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Controls whether or not the guest
network waiter waits for a routable address. When `false`, the waiter does
not wait for a default gateway, nor are IP addresses checked against any
discovered default gateways as part of its success criteria. This property is
ignored if the `wait_for_guest_ip_timeout`
waiter is used. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait<wbr>For<wbr>Guest<wbr>Net<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to
wait for an available IP address on this virtual machine's NICs. Older
versions of VMware Tools do not populate this property. In those cases, this
waiter can be disabled and the
`wait_for_guest_ip_timeout` waiter can be used
instead. A value less than 1 disables the waiter. Default: 5 minutes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alternate_<wbr>guest_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The guest name for the operating system
when `guest_id` is `other` or `other-64`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>annotation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A user-provided description of the virtual machine.
The default is no annotation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot_<wbr>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of milliseconds to wait before starting
the boot sequence. The default is no delay.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot_<wbr>retry_<wbr>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of milliseconds to wait before
retrying the boot sequence. This only valid if `boot_retry_enabled` is true.
Default: `10000` (10 seconds).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot_<wbr>retry_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to true, a virtual machine that
fails to boot will try again after the delay defined in `boot_retry_delay`.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cdrom</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinecdrom">Dict[Virtual<wbr>Machine<wbr>Cdrom]</a></span>
    </dt>
    <dd>{{% md %}}A specification for a CDROM device on this virtual
machine. See CDROM options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>change_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A unique identifier for a given version of the last
configuration applied, such the timestamp of the last update to the
configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>clone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclone">Dict[Virtual<wbr>Machine<wbr>Clone]</a></span>
    </dt>
    <dd>{{% md %}}When specified, the VM will be created as a clone of a
specified template. Optional customization options can be submitted as well.
See creating a virtual machine from a
template for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu_<wbr>hot_<wbr>add_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow CPUs to be added to this virtual
machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu_<wbr>hot_<wbr>remove_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow CPUs to be removed to this
virtual machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The maximum amount of CPU (in MHz) that this virtual
machine can consume, regardless of available resources. The default is no
limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu_<wbr>performance_<wbr>counters_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable CPU performance
counters on this virtual machine. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu_<wbr>reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The amount of CPU (in MHz) that this virtual
machine is guaranteed. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of CPU shares allocated to the
virtual machine when the `cpu_share_level` is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cpu_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The allocation level for CPU resources. Can be
one of `high`, `low`, `normal`, or `custom`. Default: `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual machine. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datastore_<wbr>cluster_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datastore cluster ID to use. This setting
applies to entire virtual machine and implies that you wish to use Storage
DRS with this virtual machine. See the section on virtual machine
migration for details on changing this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datastore_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The IP address selected by Terraform to be used for the provisioner.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinedisk">List[Virtual<wbr>Machine<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual disk device on this virtual
machine. See disk options below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>efi_<wbr>secure_<wbr>boot_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}When the `firmware` type is set to is
`efi`, this enables EFI secure boot. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>disk_<wbr>uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Expose the UUIDs of attached virtual disks to
the virtual machine, allowing access to them in the guest. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>logging</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable logging of virtual machine events to a
log file stored in the virtual machine directory. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ept_<wbr>rvi_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The EPT/RVI (hardware memory virtualization)
setting for this virtual machine. Can be one of `automatic`, `on`, or `off`.
Default: `automatic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>extra_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Extra configuration data for this virtual
machine. Can be used to supply advanced parameters not normally in
configuration, such as instance metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>firmware</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The firmware interface to use on the virtual machine.
Can be one of `bios` or `EFI`. Default: `bios`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The path to the folder to put this virtual machine in,
relative to the datacenter that the resource pool is in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force_<wbr>power_<wbr>off</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}If a guest shutdown failed or timed out while
updating or destroying (see
`shutdown_wait_timeout`), force the power-off of
the virtual machine. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The guest ID for the operating system type. For a
full list of possible values, see [here][vmware-docs-guest-ids]. Default: `other-64`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest_<wbr>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The current list of IP addresses on this machine,
including the value of `default_ip_address`. If VMware tools is not running
on the virtual machine, or if the VM is powered off, this list will be empty.
* `moid`: The [managed object reference ID][docs-about-morefs] of the created
virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hardware_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The hardware version number. Valid range
is from 4 to 15. The hardware version cannot be downgraded. See [virtual
machine hardware compatibility][virtual-machine-hardware-compatibility] for
more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host_<wbr>system_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}An optional [managed object reference
ID][docs-about-morefs] of a host to put this virtual machine on. See the
section on virtual machine migration for
details on changing this value. If a `host_system_id` is not supplied,
vSphere will select a host in the resource pool to place the virtual machine,
according to any defaults or DRS policies in place.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hv_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The (non-nested) hardware virtualization setting for
this virtual machine. Can be one of `hvAuto`, `hvOn`, or `hvOff`. Default:
`hvAuto`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ignored_<wbr>guest_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}List of IP addresses and CIDR networks to
ignore while waiting for an available IP address using either of the waiters.
Any IP addresses in this list will be ignored if they show up so that the
waiter will continue to wait for a real IP address. Default: [].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>imported</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}This is flagged if the virtual machine has been imported, or the
state has been migrated from a previous version of the resource. It
influences the behavior of the first post-import apply operation. See the
section on importing below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>latency_<wbr>sensitivity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Controls the scheduling delay of the
virtual machine. Use a higher sensitivity for applications that require lower
latency, such as VOIP, media player applications, or applications that
require frequent access to mouse or keyboard devices. Can be one of `low`,
`normal`, `medium`, or `high`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The size of the virtual machine's memory, in MB.
Default: `1024` (1 GB).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory_<wbr>hot_<wbr>add_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Allow memory to be added to this
virtual machine while it is running.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The maximum amount of memory (in MB) that this
virtual machine can consume, regardless of available resources. The default
is no limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory_<wbr>reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The amount of memory (in MB) that this
virtual machine is guaranteed. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of memory shares allocated to
the virtual machine when the `memory_share_level` is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The allocation level for memory resources.
Can be one of `high`, `low`, `normal`, or `custom`. Default: `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>migrate_<wbr>wait_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to wait
for a virtual machine migration to complete before failing. Default: 10
minutes. Also see the section on virtual machine
migration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>moid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The machine object ID from VMWare
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}An alias for both `label` and `path`, the latter when
using `attach`. Required if not using `label`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nested_<wbr>hv_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable nested hardware virtualization on
this virtual machine, facilitating nested virtualization in the guest.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinenetworkinterface">List[Virtual<wbr>Machine<wbr>Network<wbr>Interface]</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual NIC on this
virtual machine. See network interface options
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num_<wbr>cores_<wbr>per_<wbr>socket</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of cores per socket in this
virtual machine. The number of vCPUs on the virtual machine will be
`num_cpus` divided by `num_cores_per_socket`. If specified, the value
supplied to `num_cpus` must be evenly divisible by this value. Default: `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num_<wbr>cpus</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The total number of virtual processor cores to assign
to this virtual machine. Default: `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>poweron_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, that we will be trying to power on a VM
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reboot_<wbr>required</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Value internal to Terraform used to determine if a configuration set change requires a reboot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>pool_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the resource pool to put this virtual machine in.
See the section on virtual machine migration
for details on changing this value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run_<wbr>tools_<wbr>scripts_<wbr>after_<wbr>power_<wbr>on</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
post-power-on scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run_<wbr>tools_<wbr>scripts_<wbr>after_<wbr>resume</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
post-resume scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run_<wbr>tools_<wbr>scripts_<wbr>before_<wbr>guest_<wbr>reboot</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
pre-reboot scripts when VMware tools is installed. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run_<wbr>tools_<wbr>scripts_<wbr>before_<wbr>guest_<wbr>shutdown</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution
of pre-shutdown scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run_<wbr>tools_<wbr>scripts_<wbr>before_<wbr>guest_<wbr>standby</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable the execution of
pre-standby scripts when VMware tools is installed. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scsi_<wbr>bus_<wbr>sharing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Mode for sharing the SCSI bus. The modes are
physicalSharing, virtualSharing, and noSharing. Default: `noSharing`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scsi_<wbr>controller_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of SCSI controllers that Terraform manages on this virtual machine. This directly affects the amount of disks
you can add to the virtual machine and the maximum disk unit number. Note that lowering this value does not remove
controllers.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scsi_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of SCSI bus this virtual machine will have.
Can be one of lsilogic (LSI Logic Parallel), lsilogic-sas (LSI Logic SAS) or
pvscsi (VMware Paravirtual). Defualt: `pvscsi`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shutdown_<wbr>wait_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to wait
for a graceful guest shutdown when making necessary updates to the virtual
machine. If `force_power_off` is set to true, the VM will be force powered-off
after this timeout, otherwise an error is returned. Default: 3 minutes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>policy_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the storage policy to assign to this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>swap_<wbr>placement_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The swap file placement policy for this
virtual machine. Can be one of `inherit`, `hostLocal`, or `vmDirectory`.
Default: `inherit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sync_<wbr>time_<wbr>with_<wbr>host</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Enable guest clock synchronization with
the host. Requires VMware tools to be installed. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual disk's VMDK file. This is used to track the
virtual disk on the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vapp</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachinevapp">Dict[Virtual<wbr>Machine<wbr>Vapp]</a></span>
    </dt>
    <dd>{{% md %}}Optional vApp configuration. The only sub-key available
is `properties`, which is a key/value map of properties for virtual machines
imported from OVF or OVA files. See Using vApp properties to supply OVF/OVA
configuration for
more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vapp_<wbr>transports</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}Computed value which is only valid for cloned virtual
machines. A list of vApp transport methods supported by the source virtual
machine or template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmware_<wbr>tools_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The state of VMware tools in the guest. This will
determine the proper course of action for some device operations.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmx_<wbr>path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The path of the virtual machine's configuration file in the VM's
datastore.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait_<wbr>for_<wbr>guest_<wbr>ip_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to
wait for an available guest IP address on this virtual machine. This should
only be used if your version of VMware Tools does not allow the
`wait_for_guest_net_timeout` waiter to be
used. A value less than 1 disables the waiter. Default: 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait_<wbr>for_<wbr>guest_<wbr>net_<wbr>routable</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Controls whether or not the guest
network waiter waits for a routable address. When `false`, the waiter does
not wait for a default gateway, nor are IP addresses checked against any
discovered default gateways as part of its success criteria. This property is
ignored if the `wait_for_guest_ip_timeout`
waiter is used. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>wait_<wbr>for_<wbr>guest_<wbr>net_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The amount of time, in minutes, to
wait for an available IP address on this virtual machine's NICs. Older
versions of VMware Tools do not populate this property. In those cases, this
waiter can be disabled and the
`wait_for_guest_ip_timeout` waiter can be used
instead. A value less than 1 disables the waiter. Default: 5 minutes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Virtual<wbr>Machine<wbr>Cdrom</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/input/#VirtualMachineCdrom">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/output/#VirtualMachineCdrom">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineCdromArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineCdromOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Device</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether the device should be backed by
remote client device. Conflicts with `datastore_id` and `path`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datastore<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Device<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The ID of the device within the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The path to the ISO file. Required for using a datastore
ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Device</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether the device should be backed by
remote client device. Conflicts with `datastore_id` and `path`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datastore<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Device<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The ID of the device within the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The path to the ISO file. Required for using a datastore
ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Device</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether the device should be backed by
remote client device. Conflicts with `datastore_id` and `path`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datastore<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>device<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The ID of the device within the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The path to the ISO file. Required for using a datastore
ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Device</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether the device should be backed by
remote client device. Conflicts with `datastore_id` and `path`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datastore_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>device<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The ID of the device within the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The path to the ISO file. Required for using a datastore
ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Virtual<wbr>Machine<wbr>Clone</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/input/#VirtualMachineClone">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/output/#VirtualMachineClone">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineCloneArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineCloneOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Template<wbr>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Customize</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclonecustomize">Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Virtual<wbr>Machine<wbr>Clone<wbr>Customize<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Linked<wbr>Clone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ovf<wbr>Network<wbr>Map</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ovf<wbr>Storage<wbr>Map</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Template<wbr>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Customize</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclonecustomize">Virtual<wbr>Machine<wbr>Clone<wbr>Customize</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Linked<wbr>Clone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ovf<wbr>Network<wbr>Map</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ovf<wbr>Storage<wbr>Map</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>template<wbr>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>customize</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclonecustomize">Virtual<wbr>Machine<wbr>Clone<wbr>Customize</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>linked<wbr>Clone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ovf<wbr>Network<wbr>Map</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ovf<wbr>Storage<wbr>Map</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>template<wbr>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>customize</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclonecustomize">Dict[Virtual<wbr>Machine<wbr>Clone<wbr>Customize]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>linked<wbr>Clone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ovf<wbr>Network<wbr>Map</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ovf<wbr>Storage<wbr>Map</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Virtual<wbr>Machine<wbr>Clone<wbr>Customize</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/input/#VirtualMachineCloneCustomize">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/output/#VirtualMachineCloneCustomize">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineCloneCustomizeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineCloneCustomizeOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Server<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Suffix<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv4Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Linux<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclonecustomizelinuxoptions">Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Virtual<wbr>Machine<wbr>Clone<wbr>Customize<wbr>Linux<wbr>Options<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclonecustomizenetworkinterface">List&lt;Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Virtual<wbr>Machine<wbr>Clone<wbr>Customize<wbr>Network<wbr>Interface<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual NIC on this
virtual machine. See network interface options
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Windows<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclonecustomizewindowsoptions">Pulumi.<wbr>VSphere.<wbr>Inputs.<wbr>Virtual<wbr>Machine<wbr>Clone<wbr>Customize<wbr>Windows<wbr>Options<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Windows<wbr>Sysprep<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Server<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Suffix<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv4Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Linux<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclonecustomizelinuxoptions">Virtual<wbr>Machine<wbr>Clone<wbr>Customize<wbr>Linux<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclonecustomizenetworkinterface">[]Virtual<wbr>Machine<wbr>Clone<wbr>Customize<wbr>Network<wbr>Interface</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual NIC on this
virtual machine. See network interface options
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Windows<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclonecustomizewindowsoptions">Virtual<wbr>Machine<wbr>Clone<wbr>Customize<wbr>Windows<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Windows<wbr>Sysprep<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Server<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Suffix<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv4Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>linux<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclonecustomizelinuxoptions">Virtual<wbr>Machine<wbr>Clone<wbr>Customize<wbr>Linux<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclonecustomizenetworkinterface">Virtual<wbr>Machine<wbr>Clone<wbr>Customize<wbr>Network<wbr>Interface[]</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual NIC on this
virtual machine. See network interface options
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>windows<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclonecustomizewindowsoptions">Virtual<wbr>Machine<wbr>Clone<wbr>Customize<wbr>Windows<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>windows<wbr>Sysprep<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Server<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Suffix<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv4Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>linux<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclonecustomizelinuxoptions">Dict[Virtual<wbr>Machine<wbr>Clone<wbr>Customize<wbr>Linux<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclonecustomizenetworkinterface">List[Virtual<wbr>Machine<wbr>Clone<wbr>Customize<wbr>Network<wbr>Interface]</a></span>
    </dt>
    <dd>{{% md %}}A specification for a virtual NIC on this
virtual machine. See network interface options
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>windows<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualmachineclonecustomizewindowsoptions">Dict[Virtual<wbr>Machine<wbr>Clone<wbr>Customize<wbr>Windows<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>windows<wbr>Sysprep<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Virtual<wbr>Machine<wbr>Clone<wbr>Customize<wbr>Linux<wbr>Options</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/input/#VirtualMachineCloneCustomizeLinuxOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/output/#VirtualMachineCloneCustomizeLinuxOptions">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineCloneCustomizeLinuxOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineCloneCustomizeLinuxOptionsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hw<wbr>Clock<wbr>Utc</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hw<wbr>Clock<wbr>Utc</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hw<wbr>Clock<wbr>Utc</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hw<wbr>Clock<wbr>Utc</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Virtual<wbr>Machine<wbr>Clone<wbr>Customize<wbr>Network<wbr>Interface</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/input/#VirtualMachineCloneCustomizeNetworkInterface">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/output/#VirtualMachineCloneCustomizeNetworkInterface">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineCloneCustomizeNetworkInterfaceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineCloneCustomizeNetworkInterfaceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Server<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv4Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv4Netmask</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Netmask</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Server<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv4Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv4Netmask</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Netmask</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Server<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv4Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv4Netmask</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6Netmask</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Server<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv4_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv4Netmask</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6Netmask</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Virtual<wbr>Machine<wbr>Clone<wbr>Customize<wbr>Windows<wbr>Options</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/input/#VirtualMachineCloneCustomizeWindowsOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/output/#VirtualMachineCloneCustomizeWindowsOptions">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineCloneCustomizeWindowsOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineCloneCustomizeWindowsOptionsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Computer<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Logon</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Logon<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Domain<wbr>Admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Domain<wbr>Admin<wbr>User</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Full<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Join<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Organization<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Product<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Once<wbr>Command<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Workgroup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Computer<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Logon</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Logon<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Domain<wbr>Admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Domain<wbr>Admin<wbr>User</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Full<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Join<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Organization<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Product<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Run<wbr>Once<wbr>Command<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Workgroup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>computer<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Logon</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Logon<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>domain<wbr>Admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>domain<wbr>Admin<wbr>User</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>full<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>join<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>organization<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>product<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>Once<wbr>Command<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>workgroup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>computer<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Logon</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Logon<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>domain<wbr>Admin<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>domain<wbr>Admin<wbr>User</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>full<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>join<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>organization<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>product<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>run<wbr>Once<wbr>Command<wbr>Lists</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>workgroup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Virtual<wbr>Machine<wbr>Disk</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/input/#VirtualMachineDisk">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/output/#VirtualMachineDisk">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineDiskArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineDiskOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Attach</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Attach an external disk instead of creating a new one.
Implies and conflicts with `keep_on_remove`. If set, you cannot set `size`,
`eagerly_scrub`, or `thin_provisioned`. Must set `path` if used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datastore<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Device<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The mode of this this virtual disk for purposes of
writes and snapshotting. Can be one of `append`, `independent_nonpersistent`,
`independent_persistent`, `nonpersistent`, `persistent`, or `undoable`.
Default: `persistent`. For an explanation of options, click
[here][vmware-docs-disk-mode].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Sharing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The sharing mode of this virtual disk. Can be one
of `sharingMultiWriter` or `sharingNone`. Default: `sharingNone`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eagerly<wbr>Scrub</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to `true`, the disk space is zeroed out
on VM creation. This will delay the creation of the disk or virtual machine.
Cannot be set to `true` when `thin_provisioned` is `true`.  See the section
on picking a disk type.  Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Io<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The upper limit of IOPS that this disk can use. The
default is no limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Io<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The I/O reservation (guarantee) that this disk
has, in IOPS.  The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Io<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The share count for this disk when the share
level is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Io<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The share allocation level for this disk. Can
be one of `low`, `normal`, `high`, or `custom`. Default: `normal`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Keep<wbr>On<wbr>Remove</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Keep this disk when removing the device or
destroying the virtual machine. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The ID of the device within the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A label for the disk. Forces a new disk if changed.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}An alias for both `label` and `path`, the latter when
using `attach`. Required if not using `label`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}
The name attribute for virtual disks will be removed in favor of &#34;label&#34; in
future releases. To transition existing disks, rename the &#34;name&#34; attribute to
&#34;label&#34;. When doing so, ensure the value of the attribute stays the same.

Note that &#34;label&#34; does not control the name of a VMDK and does not need to bear
the name of one on new disks or virtual machines. For more information, see the
documentation for the label attribute at: 

https://www.terraform.io/docs/providers/vsphere/r/virtual_machine.html#label
{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The path to the ISO file. Required for using a datastore
ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The size of the disk, in GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the storage policy to assign to this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thin<wbr>Provisioned</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}If `true`, this disk is thin provisioned,
with space for the file being allocated on an as-needed basis. Cannot be set
to `true` when `eagerly_scrub` is `true`. See the section on picking a disk
type. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unit<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The disk number on the SCSI bus. The maximum value
for this setting is the value of
`scsi_controller_count` times 15, minus 1 (so `14`,
`29`, `44`, and `59`, for 1-4 controllers respectively). The default is `0`,
for which one disk must be set to. Duplicate unit numbers are not allowed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual disk's VMDK file. This is used to track the
virtual disk on the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Write<wbr>Through</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}If `true`, writes for this disk are sent
directly to the filesystem immediately instead of being buffered. Default:
`false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Attach</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Attach an external disk instead of creating a new one.
Implies and conflicts with `keep_on_remove`. If set, you cannot set `size`,
`eagerly_scrub`, or `thin_provisioned`. Must set `path` if used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datastore<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Device<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The mode of this this virtual disk for purposes of
writes and snapshotting. Can be one of `append`, `independent_nonpersistent`,
`independent_persistent`, `nonpersistent`, `persistent`, or `undoable`.
Default: `persistent`. For an explanation of options, click
[here][vmware-docs-disk-mode].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Sharing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The sharing mode of this virtual disk. Can be one
of `sharingMultiWriter` or `sharingNone`. Default: `sharingNone`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eagerly<wbr>Scrub</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to `true`, the disk space is zeroed out
on VM creation. This will delay the creation of the disk or virtual machine.
Cannot be set to `true` when `thin_provisioned` is `true`.  See the section
on picking a disk type.  Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Io<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The upper limit of IOPS that this disk can use. The
default is no limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Io<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The I/O reservation (guarantee) that this disk
has, in IOPS.  The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Io<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The share count for this disk when the share
level is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Io<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The share allocation level for this disk. Can
be one of `low`, `normal`, `high`, or `custom`. Default: `normal`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Keep<wbr>On<wbr>Remove</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Keep this disk when removing the device or
destroying the virtual machine. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The ID of the device within the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A label for the disk. Forces a new disk if changed.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}An alias for both `label` and `path`, the latter when
using `attach`. Required if not using `label`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}
The name attribute for virtual disks will be removed in favor of &#34;label&#34; in
future releases. To transition existing disks, rename the &#34;name&#34; attribute to
&#34;label&#34;. When doing so, ensure the value of the attribute stays the same.

Note that &#34;label&#34; does not control the name of a VMDK and does not need to bear
the name of one on new disks or virtual machines. For more information, see the
documentation for the label attribute at: 

https://www.terraform.io/docs/providers/vsphere/r/virtual_machine.html#label
{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The path to the ISO file. Required for using a datastore
ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The size of the disk, in GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the storage policy to assign to this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Thin<wbr>Provisioned</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}If `true`, this disk is thin provisioned,
with space for the file being allocated on an as-needed basis. Cannot be set
to `true` when `eagerly_scrub` is `true`. See the section on picking a disk
type. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unit<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The disk number on the SCSI bus. The maximum value
for this setting is the value of
`scsi_controller_count` times 15, minus 1 (so `14`,
`29`, `44`, and `59`, for 1-4 controllers respectively). The default is `0`,
for which one disk must be set to. Duplicate unit numbers are not allowed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual disk's VMDK file. This is used to track the
virtual disk on the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Write<wbr>Through</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}If `true`, writes for this disk are sent
directly to the filesystem immediately instead of being buffered. Default:
`false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>attach</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Attach an external disk instead of creating a new one.
Implies and conflicts with `keep_on_remove`. If set, you cannot set `size`,
`eagerly_scrub`, or `thin_provisioned`. Must set `path` if used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datastore<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>device<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The mode of this this virtual disk for purposes of
writes and snapshotting. Can be one of `append`, `independent_nonpersistent`,
`independent_persistent`, `nonpersistent`, `persistent`, or `undoable`.
Default: `persistent`. For an explanation of options, click
[here][vmware-docs-disk-mode].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Sharing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The sharing mode of this virtual disk. Can be one
of `sharingMultiWriter` or `sharingNone`. Default: `sharingNone`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eagerly<wbr>Scrub</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}If set to `true`, the disk space is zeroed out
on VM creation. This will delay the creation of the disk or virtual machine.
Cannot be set to `true` when `thin_provisioned` is `true`.  See the section
on picking a disk type.  Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>io<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The upper limit of IOPS that this disk can use. The
default is no limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>io<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The I/O reservation (guarantee) that this disk
has, in IOPS.  The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>io<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The share count for this disk when the share
level is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>io<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The share allocation level for this disk. Can
be one of `low`, `normal`, `high`, or `custom`. Default: `normal`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>keep<wbr>On<wbr>Remove</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Keep this disk when removing the device or
destroying the virtual machine. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The ID of the device within the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A label for the disk. Forces a new disk if changed.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}An alias for both `label` and `path`, the latter when
using `attach`. Required if not using `label`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}
The name attribute for virtual disks will be removed in favor of &#34;label&#34; in
future releases. To transition existing disks, rename the &#34;name&#34; attribute to
&#34;label&#34;. When doing so, ensure the value of the attribute stays the same.

Note that &#34;label&#34; does not control the name of a VMDK and does not need to bear
the name of one on new disks or virtual machines. For more information, see the
documentation for the label attribute at: 

https://www.terraform.io/docs/providers/vsphere/r/virtual_machine.html#label
{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The path to the ISO file. Required for using a datastore
ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The size of the disk, in GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the storage policy to assign to this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thin<wbr>Provisioned</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}If `true`, this disk is thin provisioned,
with space for the file being allocated on an as-needed basis. Cannot be set
to `true` when `eagerly_scrub` is `true`. See the section on picking a disk
type. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unit<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The disk number on the SCSI bus. The maximum value
for this setting is the value of
`scsi_controller_count` times 15, minus 1 (so `14`,
`29`, `44`, and `59`, for 1-4 controllers respectively). The default is `0`,
for which one disk must be set to. Duplicate unit numbers are not allowed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual disk's VMDK file. This is used to track the
virtual disk on the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>write<wbr>Through</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}If `true`, writes for this disk are sent
directly to the filesystem immediately instead of being buffered. Default:
`false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>attach</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Attach an external disk instead of creating a new one.
Implies and conflicts with `keep_on_remove`. If set, you cannot set `size`,
`eagerly_scrub`, or `thin_provisioned`. Must set `path` if used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datastore_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>device<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The mode of this this virtual disk for purposes of
writes and snapshotting. Can be one of `append`, `independent_nonpersistent`,
`independent_persistent`, `nonpersistent`, `persistent`, or `undoable`.
Default: `persistent`. For an explanation of options, click
[here][vmware-docs-disk-mode].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Sharing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The sharing mode of this virtual disk. Can be one
of `sharingMultiWriter` or `sharingNone`. Default: `sharingNone`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eagerly<wbr>Scrub</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to `true`, the disk space is zeroed out
on VM creation. This will delay the creation of the disk or virtual machine.
Cannot be set to `true` when `thin_provisioned` is `true`.  See the section
on picking a disk type.  Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>io<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The upper limit of IOPS that this disk can use. The
default is no limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>io<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The I/O reservation (guarantee) that this disk
has, in IOPS.  The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>io<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The share count for this disk when the share
level is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>io<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The share allocation level for this disk. Can
be one of `low`, `normal`, `high`, or `custom`. Default: `normal`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>keep<wbr>On<wbr>Remove</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Keep this disk when removing the device or
destroying the virtual machine. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The ID of the device within the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A label for the disk. Forces a new disk if changed.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}An alias for both `label` and `path`, the latter when
using `attach`. Required if not using `label`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}
The name attribute for virtual disks will be removed in favor of &#34;label&#34; in
future releases. To transition existing disks, rename the &#34;name&#34; attribute to
&#34;label&#34;. When doing so, ensure the value of the attribute stays the same.

Note that &#34;label&#34; does not control the name of a VMDK and does not need to bear
the name of one on new disks or virtual machines. For more information, see the
documentation for the label attribute at: 

https://www.terraform.io/docs/providers/vsphere/r/virtual_machine.html#label
{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The path to the ISO file. Required for using a datastore
ISO. Conflicts with `client_device`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The size of the disk, in GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>policy_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the storage policy to assign to this disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>thin<wbr>Provisioned</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}If `true`, this disk is thin provisioned,
with space for the file being allocated on an as-needed basis. Cannot be set
to `true` when `eagerly_scrub` is `true`. See the section on picking a disk
type. Default: `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unit<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The disk number on the SCSI bus. The maximum value
for this setting is the value of
`scsi_controller_count` times 15, minus 1 (so `14`,
`29`, `44`, and `59`, for 1-4 controllers respectively). The default is `0`,
for which one disk must be set to. Duplicate unit numbers are not allowed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uuid</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual disk's VMDK file. This is used to track the
virtual disk on the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>write<wbr>Through</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}If `true`, writes for this disk are sent
directly to the filesystem immediately instead of being buffered. Default:
`false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Virtual<wbr>Machine<wbr>Network<wbr>Interface</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/input/#VirtualMachineNetworkInterface">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/output/#VirtualMachineNetworkInterface">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineNetworkInterfaceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineNetworkInterfaceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the network to connect this interface to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Adapter<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The network interface type. Can be one of
`e1000`, `e1000e`, or `vmxnet3`. Default: `vmxnet3`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bandwidth<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The upper bandwidth limit of this network
interface, in Mbits/sec. The default is no limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bandwidth<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The bandwidth reservation of this
network interface, in Mbits/sec. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bandwidth<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The share count for this network
interface when the share level is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bandwidth<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The bandwidth share allocation level for
this interface. Can be one of `low`, `normal`, `high`, or `custom`. Default:
`normal`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Device<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The ID of the device within the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mac<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The MAC address of this network interface. Can
only be manually set if `use_static_mac` is true, otherwise this is a
computed value that gives the current MAC address of this interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ovf<wbr>Mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies which OVF NIC the `network_interface`
should be associated with. Only applies at creation and only when deploying
from an OVF source.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Static<wbr>Mac</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}If true, the `mac_address` field is treated as
a static MAC address and set accordingly. Setting this to `true` requires
`mac_address` to be set. Default: `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the network to connect this interface to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Adapter<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The network interface type. Can be one of
`e1000`, `e1000e`, or `vmxnet3`. Default: `vmxnet3`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bandwidth<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The upper bandwidth limit of this network
interface, in Mbits/sec. The default is no limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bandwidth<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The bandwidth reservation of this
network interface, in Mbits/sec. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bandwidth<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The share count for this network
interface when the share level is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bandwidth<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The bandwidth share allocation level for
this interface. Can be one of `low`, `normal`, `high`, or `custom`. Default:
`normal`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Device<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The ID of the device within the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mac<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The MAC address of this network interface. Can
only be manually set if `use_static_mac` is true, otherwise this is a
computed value that gives the current MAC address of this interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ovf<wbr>Mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies which OVF NIC the `network_interface`
should be associated with. Only applies at creation and only when deploying
from an OVF source.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Static<wbr>Mac</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}If true, the `mac_address` field is treated as
a static MAC address and set accordingly. Setting this to `true` requires
`mac_address` to be set. Default: `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the network to connect this interface to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>adapter<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The network interface type. Can be one of
`e1000`, `e1000e`, or `vmxnet3`. Default: `vmxnet3`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bandwidth<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The upper bandwidth limit of this network
interface, in Mbits/sec. The default is no limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bandwidth<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The bandwidth reservation of this
network interface, in Mbits/sec. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bandwidth<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The share count for this network
interface when the share level is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bandwidth<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The bandwidth share allocation level for
this interface. Can be one of `low`, `normal`, `high`, or `custom`. Default:
`normal`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>device<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The ID of the device within the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mac<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The MAC address of this network interface. Can
only be manually set if `use_static_mac` is true, otherwise this is a
computed value that gives the current MAC address of this interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ovf<wbr>Mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies which OVF NIC the `network_interface`
should be associated with. Only applies at creation and only when deploying
from an OVF source.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Static<wbr>Mac</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}If true, the `mac_address` field is treated as
a static MAC address and set accordingly. Setting this to `true` requires
`mac_address` to be set. Default: `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the network to connect this interface to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>adapter_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The network interface type. Can be one of
`e1000`, `e1000e`, or `vmxnet3`. Default: `vmxnet3`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bandwidth<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The upper bandwidth limit of this network
interface, in Mbits/sec. The default is no limit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bandwidth<wbr>Reservation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The bandwidth reservation of this
network interface, in Mbits/sec. The default is no reservation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bandwidth<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The share count for this network
interface when the share level is `custom`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bandwidth<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The bandwidth share allocation level for
this interface. Can be one of `low`, `normal`, `high`, or `custom`. Default:
`normal`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>device<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The ID of the device within the virtual machine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mac<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The MAC address of this network interface. Can
only be manually set if `use_static_mac` is true, otherwise this is a
computed value that gives the current MAC address of this interface.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ovf<wbr>Mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies which OVF NIC the `network_interface`
should be associated with. Only applies at creation and only when deploying
from an OVF source.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Static<wbr>Mac</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}If true, the `mac_address` field is treated as
a static MAC address and set accordingly. Setting this to `true` requires
`mac_address` to be set. Default: `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Virtual<wbr>Machine<wbr>Vapp</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/input/#VirtualMachineVapp">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/output/#VirtualMachineVapp">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineVappArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#VirtualMachineVappOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-vsphere">https://github.com/pulumi/pulumi-vsphere</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`vsphere` Terraform Provider](https://github.com/terraform-providers/terraform-provider-vsphere).</dd>
</dl>

