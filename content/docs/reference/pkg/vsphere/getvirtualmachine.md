
---
title: "GetVirtualMachine"
block_external_search_index: true
---



The `vsphere..VirtualMachine` data source can be used to find the UUID of an
existing virtual machine or template. Its most relevant purpose is for finding
the UUID of a template to be used as the source for cloning into a new
[`vsphere..VirtualMachine`][docs-virtual-machine-resource] resource. It also
reads the guest ID so that can be supplied as well.

[docs-virtual-machine-resource]: /docs/providers/vsphere/r/virtual_machine.html

{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as vsphere from "@pulumi/vsphere";

const datacenter = vsphere.getDatacenter({
    name: "dc1",
});
const template = vsphere.getVirtualMachine({
    datacenterId: datacenter.id,
    name: "test-vm-template",
});
```

{{% /example %}}
{{% /examples %}}





## Using GetVirtualMachine

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getVirtualMachine<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#GetVirtualMachineArgs">GetVirtualMachineArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#GetVirtualMachineResult">GetVirtualMachineResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_virtual_machine(</span>datacenter_id=None<span class="p">, </span>name=None<span class="p">, </span>scsi_controller_scan_count=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupVirtualMachine<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#GetVirtualMachineArgs">GetVirtualMachineArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#LookupVirtualMachineResult">LookupVirtualMachineResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetVirtualMachine </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere.GetVirtualMachineResult.html">GetVirtualMachineResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.VSphere.GetVirtualMachineArgs.html">GetVirtualMachineArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
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
    <dd>{{% md %}}The name of the virtual machine. This can be a name or
path.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datacenter<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datacenter the virtual machine is located in.
This can be omitted if the search path used in `name` is an absolute path.
For default datacenters, use the `id` attribute from an empty
`vsphere..Datacenter` data source.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scsi<wbr>Controller<wbr>Scan<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of SCSI controllers to
scan for disk attributes and controller types on. Default: `1`.
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
    <dd>{{% md %}}The name of the virtual machine. This can be a name or
path.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datacenter<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datacenter the virtual machine is located in.
This can be omitted if the search path used in `name` is an absolute path.
For default datacenters, use the `id` attribute from an empty
`vsphere..Datacenter` data source.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scsi<wbr>Controller<wbr>Scan<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of SCSI controllers to
scan for disk attributes and controller types on. Default: `1`.
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
    <dd>{{% md %}}The name of the virtual machine. This can be a name or
path.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datacenter<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datacenter the virtual machine is located in.
This can be omitted if the search path used in `name` is an absolute path.
For default datacenters, use the `id` attribute from an empty
`vsphere..Datacenter` data source.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scsi<wbr>Controller<wbr>Scan<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of SCSI controllers to
scan for disk attributes and controller types on. Default: `1`.
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
    <dd>{{% md %}}The name of the virtual machine. This can be a name or
path.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datacenter_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the datacenter the virtual machine is located in.
This can be omitted if the search path used in `name` is an absolute path.
For default datacenters, use the `id` attribute from an empty
`vsphere..Datacenter` data source.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scsi_<wbr>controller_<wbr>scan_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of SCSI controllers to
scan for disk attributes and controller types on. Default: `1`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetVirtualMachine Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Alternate<wbr>Guest<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The alternate guest name of the virtual machine when
guest_id is a non-specific operating system, like `otherGuest`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getvirtualmachinedisk">List&lt;Pulumi.<wbr>VSphere.<wbr>Outputs.<wbr>Get<wbr>Virtual<wbr>Machine<wbr>Disk&gt;</a></span>
    </dt>
    <dd>{{% md %}}Information about each of the disks on this virtual machine or
template. These are sorted by bus and unit number so that they can be applied
to a `vsphere..VirtualMachine` resource in the order the resource expects
while cloning. This is useful for discovering certain disk settings while
performing a linked clone, as all settings that are output by this data
source must be the same on the destination virtual machine as the source.
Only the first number of controllers defined by `scsi_controller_scan_count`
are scanned for disks. The sub-attributes are:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Firmware</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The firmware type for this virtual machine. Can be `bios` or `efi`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Guest<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The guest ID of the virtual machine or template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Guest<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of IP addresses as reported by VMWare tools.
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
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interface<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The network interface types for each network
interface found on the virtual machine, in device bus order. Will be one of
`e1000`, `e1000e`, `pcnet32`, `sriov`, `vmxnet2`, or `vmxnet3`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scsi<wbr>Bus<wbr>Sharing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Mode for sharing the SCSI bus. The modes are
physicalSharing, virtualSharing, and noSharing. Only the first number of
controllers defined by `scsi_controller_scan_count` are scanned.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scsi<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The common type of all SCSI controllers on this virtual machine.
Will be one of `lsilogic` (LSI Logic Parallel), `lsilogic-sas` (LSI Logic
SAS), `pvscsi` (VMware Paravirtual), `buslogic` (BusLogic), or `mixed` when
there are multiple controller types. Only the first number of controllers
defined by `scsi_controller_scan_count` are scanned.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Datacenter<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scsi<wbr>Controller<wbr>Scan<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Alternate<wbr>Guest<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The alternate guest name of the virtual machine when
guest_id is a non-specific operating system, like `otherGuest`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getvirtualmachinedisk">[]Get<wbr>Virtual<wbr>Machine<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}Information about each of the disks on this virtual machine or
template. These are sorted by bus and unit number so that they can be applied
to a `vsphere..VirtualMachine` resource in the order the resource expects
while cloning. This is useful for discovering certain disk settings while
performing a linked clone, as all settings that are output by this data
source must be the same on the destination virtual machine as the source.
Only the first number of controllers defined by `scsi_controller_scan_count`
are scanned for disks. The sub-attributes are:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Firmware</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The firmware type for this virtual machine. Can be `bios` or `efi`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Guest<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The guest ID of the virtual machine or template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Guest<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}A list of IP addresses as reported by VMWare tools.
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
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interface<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The network interface types for each network
interface found on the virtual machine, in device bus order. Will be one of
`e1000`, `e1000e`, `pcnet32`, `sriov`, `vmxnet2`, or `vmxnet3`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scsi<wbr>Bus<wbr>Sharing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Mode for sharing the SCSI bus. The modes are
physicalSharing, virtualSharing, and noSharing. Only the first number of
controllers defined by `scsi_controller_scan_count` are scanned.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scsi<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The common type of all SCSI controllers on this virtual machine.
Will be one of `lsilogic` (LSI Logic Parallel), `lsilogic-sas` (LSI Logic
SAS), `pvscsi` (VMware Paravirtual), `buslogic` (BusLogic), or `mixed` when
there are multiple controller types. Only the first number of controllers
defined by `scsi_controller_scan_count` are scanned.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Datacenter<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scsi<wbr>Controller<wbr>Scan<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>alternate<wbr>Guest<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The alternate guest name of the virtual machine when
guest_id is a non-specific operating system, like `otherGuest`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getvirtualmachinedisk">Get<wbr>Virtual<wbr>Machine<wbr>Disk[]</a></span>
    </dt>
    <dd>{{% md %}}Information about each of the disks on this virtual machine or
template. These are sorted by bus and unit number so that they can be applied
to a `vsphere..VirtualMachine` resource in the order the resource expects
while cloning. This is useful for discovering certain disk settings while
performing a linked clone, as all settings that are output by this data
source must be the same on the destination virtual machine as the source.
Only the first number of controllers defined by `scsi_controller_scan_count`
are scanned for disks. The sub-attributes are:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>firmware</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The firmware type for this virtual machine. Can be `bios` or `efi`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>guest<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The guest ID of the virtual machine or template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>guest<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}A list of IP addresses as reported by VMWare tools.
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
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Interface<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The network interface types for each network
interface found on the virtual machine, in device bus order. Will be one of
`e1000`, `e1000e`, `pcnet32`, `sriov`, `vmxnet2`, or `vmxnet3`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scsi<wbr>Bus<wbr>Sharing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Mode for sharing the SCSI bus. The modes are
physicalSharing, virtualSharing, and noSharing. Only the first number of
controllers defined by `scsi_controller_scan_count` are scanned.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scsi<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The common type of all SCSI controllers on this virtual machine.
Will be one of `lsilogic` (LSI Logic Parallel), `lsilogic-sas` (LSI Logic
SAS), `pvscsi` (VMware Paravirtual), `buslogic` (BusLogic), or `mixed` when
there are multiple controller types. Only the first number of controllers
defined by `scsi_controller_scan_count` are scanned.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>datacenter<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scsi<wbr>Controller<wbr>Scan<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>alternate_<wbr>guest_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The alternate guest name of the virtual machine when
guest_id is a non-specific operating system, like `otherGuest`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getvirtualmachinedisk">List[Get<wbr>Virtual<wbr>Machine<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}Information about each of the disks on this virtual machine or
template. These are sorted by bus and unit number so that they can be applied
to a `vsphere..VirtualMachine` resource in the order the resource expects
while cloning. This is useful for discovering certain disk settings while
performing a linked clone, as all settings that are output by this data
source must be the same on the destination virtual machine as the source.
Only the first number of controllers defined by `scsi_controller_scan_count`
are scanned for disks. The sub-attributes are:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>firmware</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The firmware type for this virtual machine. Can be `bios` or `efi`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>guest_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The guest ID of the virtual machine or template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>guest_<wbr>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}A list of IP addresses as reported by VMWare tools.
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
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>interface_<wbr>types</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The network interface types for each network
interface found on the virtual machine, in device bus order. Will be one of
`e1000`, `e1000e`, `pcnet32`, `sriov`, `vmxnet2`, or `vmxnet3`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scsi_<wbr>bus_<wbr>sharing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Mode for sharing the SCSI bus. The modes are
physicalSharing, virtualSharing, and noSharing. Only the first number of
controllers defined by `scsi_controller_scan_count` are scanned.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scsi_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The common type of all SCSI controllers on this virtual machine.
Will be one of `lsilogic` (LSI Logic Parallel), `lsilogic-sas` (LSI Logic
SAS), `pvscsi` (VMware Paravirtual), `buslogic` (BusLogic), or `mixed` when
there are multiple controller types. Only the first number of controllers
defined by `scsi_controller_scan_count` are scanned.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>datacenter_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scsi_<wbr>controller_<wbr>scan_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Virtual<wbr>Machine<wbr>Disk</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/output/#GetVirtualMachineDisk">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#GetVirtualMachineDisk">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Eagerly<wbr>Scrub</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Set to `true` if the disk has been eager zeroed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The size of the disk, in GIB.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Thin<wbr>Provisioned</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Set to `true` if the disk has been thin provisioned.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Eagerly<wbr>Scrub</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Set to `true` if the disk has been eager zeroed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The size of the disk, in GIB.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Thin<wbr>Provisioned</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Set to `true` if the disk has been thin provisioned.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>eagerly<wbr>Scrub</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Set to `true` if the disk has been eager zeroed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The size of the disk, in GIB.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>thin<wbr>Provisioned</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Set to `true` if the disk has been thin provisioned.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>eagerly<wbr>Scrub</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Set to `true` if the disk has been eager zeroed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The size of the disk, in GIB.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>thin<wbr>Provisioned</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Set to `true` if the disk has been thin provisioned.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







