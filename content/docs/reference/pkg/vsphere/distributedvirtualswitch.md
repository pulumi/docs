
---
title: "DistributedVirtualSwitch"
block_external_search_index: true
---



The `vsphere..DistributedVirtualSwitch` resource can be used to manage VMware
Distributed Virtual Switches.

An essential component of a distributed, scalable VMware datacenter, the
vSphere Distributed Virtual Switch (DVS) provides centralized management and
monitoring of the networking configuration of all the hosts that are associated
with the switch. In addition to adding port groups (see the
[`vsphere..DistributedPortGroup`][distributed-port-group] resource) that can
be used as networks for virtual machines, a DVS can be configured to perform
advanced high availability, traffic shaping, network monitoring, and more.

For an overview on vSphere networking concepts, see [this
page][ref-vsphere-net-concepts]. For more information on vSphere DVS, see [this
page][ref-vsphere-dvs].

[distributed-port-group]: /docs/providers/vsphere/r/distributed_port_group.html
[ref-vsphere-net-concepts]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html
[ref-vsphere-dvs]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-375B45C7-684C-4C51-BA3C-70E48DFABF04.html

> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

> This content is derived from https://github.com/terraform-providers/terraform-provider-vsphere/blob/master/website/docs/r/distributed_virtual_switch.html.markdown.



## Create a DistributedVirtualSwitch Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#DistributedVirtualSwitch">DistributedVirtualSwitch</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#DistributedVirtualSwitchArgs">DistributedVirtualSwitchArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">DistributedVirtualSwitch</span><span class="p">(resource_name, opts=None, </span>active_uplinks=None<span class="p">, </span>allow_forged_transmits=None<span class="p">, </span>allow_mac_changes=None<span class="p">, </span>allow_promiscuous=None<span class="p">, </span>block_all_ports=None<span class="p">, </span>check_beacon=None<span class="p">, </span>contact_detail=None<span class="p">, </span>contact_name=None<span class="p">, </span>custom_attributes=None<span class="p">, </span>datacenter_id=None<span class="p">, </span>description=None<span class="p">, </span>directpath_gen2_allowed=None<span class="p">, </span>egress_shaping_average_bandwidth=None<span class="p">, </span>egress_shaping_burst_size=None<span class="p">, </span>egress_shaping_enabled=None<span class="p">, </span>egress_shaping_peak_bandwidth=None<span class="p">, </span>failback=None<span class="p">, </span>faulttolerance_maximum_mbit=None<span class="p">, </span>faulttolerance_reservation_mbit=None<span class="p">, </span>faulttolerance_share_count=None<span class="p">, </span>faulttolerance_share_level=None<span class="p">, </span>folder=None<span class="p">, </span>hbr_maximum_mbit=None<span class="p">, </span>hbr_reservation_mbit=None<span class="p">, </span>hbr_share_count=None<span class="p">, </span>hbr_share_level=None<span class="p">, </span>hosts=None<span class="p">, </span>ingress_shaping_average_bandwidth=None<span class="p">, </span>ingress_shaping_burst_size=None<span class="p">, </span>ingress_shaping_enabled=None<span class="p">, </span>ingress_shaping_peak_bandwidth=None<span class="p">, </span>ipv4_address=None<span class="p">, </span>iscsi_maximum_mbit=None<span class="p">, </span>iscsi_reservation_mbit=None<span class="p">, </span>iscsi_share_count=None<span class="p">, </span>iscsi_share_level=None<span class="p">, </span>lacp_api_version=None<span class="p">, </span>lacp_enabled=None<span class="p">, </span>lacp_mode=None<span class="p">, </span>link_discovery_operation=None<span class="p">, </span>link_discovery_protocol=None<span class="p">, </span>management_maximum_mbit=None<span class="p">, </span>management_reservation_mbit=None<span class="p">, </span>management_share_count=None<span class="p">, </span>management_share_level=None<span class="p">, </span>max_mtu=None<span class="p">, </span>multicast_filtering_mode=None<span class="p">, </span>name=None<span class="p">, </span>netflow_active_flow_timeout=None<span class="p">, </span>netflow_collector_ip_address=None<span class="p">, </span>netflow_collector_port=None<span class="p">, </span>netflow_enabled=None<span class="p">, </span>netflow_idle_flow_timeout=None<span class="p">, </span>netflow_internal_flows_only=None<span class="p">, </span>netflow_observation_domain_id=None<span class="p">, </span>netflow_sampling_rate=None<span class="p">, </span>network_resource_control_enabled=None<span class="p">, </span>network_resource_control_version=None<span class="p">, </span>nfs_maximum_mbit=None<span class="p">, </span>nfs_reservation_mbit=None<span class="p">, </span>nfs_share_count=None<span class="p">, </span>nfs_share_level=None<span class="p">, </span>notify_switches=None<span class="p">, </span>port_private_secondary_vlan_id=None<span class="p">, </span>standby_uplinks=None<span class="p">, </span>tags=None<span class="p">, </span>teaming_policy=None<span class="p">, </span>tx_uplink=None<span class="p">, </span>uplinks=None<span class="p">, </span>vdp_maximum_mbit=None<span class="p">, </span>vdp_reservation_mbit=None<span class="p">, </span>vdp_share_count=None<span class="p">, </span>vdp_share_level=None<span class="p">, </span>version=None<span class="p">, </span>virtualmachine_maximum_mbit=None<span class="p">, </span>virtualmachine_reservation_mbit=None<span class="p">, </span>virtualmachine_share_count=None<span class="p">, </span>virtualmachine_share_level=None<span class="p">, </span>vlan_id=None<span class="p">, </span>vlan_ranges=None<span class="p">, </span>vmotion_maximum_mbit=None<span class="p">, </span>vmotion_reservation_mbit=None<span class="p">, </span>vmotion_share_count=None<span class="p">, </span>vmotion_share_level=None<span class="p">, </span>vsan_maximum_mbit=None<span class="p">, </span>vsan_reservation_mbit=None<span class="p">, </span>vsan_share_count=None<span class="p">, </span>vsan_share_level=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDistributedVirtualSwitch<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/go/vsphere/?tab=doc#DistributedVirtualSwitchArgs">DistributedVirtualSwitchArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/go/vsphere/?tab=doc#DistributedVirtualSwitch">DistributedVirtualSwitch</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere..DistributedVirtualSwitch.html">DistributedVirtualSwitch</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere.DistributedVirtualSwitchArgs.html">DistributedVirtualSwitchArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Active<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of active uplinks to be used in load
balancing. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Forged<wbr>Transmits</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Controls whether or not a virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Mac<wbr>Changes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Controls whether or not the Media Access
Control (MAC) address can be changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Promiscuous</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Block<wbr>All<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Shuts down all ports in the port groups that
this policy applies to, effectively blocking all network access to connected
virtual devices.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Check<wbr>Beacon</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enables beacon probing as an additional measure
to detect NIC failure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Contact<wbr>Detail</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The detailed contact information for the person
who is responsible for the DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Contact<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the person who is responsible for the
DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual switch. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Datacenter<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter where the distributed
virtual switch will be created. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A detailed description for the DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Directpath<wbr>Gen2Allowed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Allow VMDirectPath Gen2 for the ports
for which this policy applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in bits
per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is enabled
on the port for egress traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during bursts
in bits per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failback</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will re-activate failed
uplinks higher in precedence when they come back up.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Faulttolerance<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Faulttolerance<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Faulttolerance<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the faultTolerance traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Faulttolerance<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The folder to create the DVS in. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hbr<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hbr<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hbr<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the hbr traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hbr<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchhost">List&lt;Distributed<wbr>Virtual<wbr>Switch<wbr>Host<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Use the `host` block to declare a host specification. The
options are:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ingress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in
bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ingress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ingress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is
enabled on the port for ingress traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ingress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during
bursts in bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv4Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An IPv4 address to identify the switch. This is
mostly useful when used with the Netflow arguments found
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the iSCSI traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lacp<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Link Aggregation Control Protocol group
version to use with the switch. Possible values are `singleLag` and
`multipleLag`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lacp<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enables LACP for the ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lacp<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The LACP mode. Can be one of `active` or `passive`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Link<wbr>Discovery<wbr>Operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Whether to `advertise` or `listen`
for link discovery traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Link<wbr>Discovery<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The discovery protocol type. Valid
types are `cdp` and `lldp`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the management traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the management traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum transmission unit (MTU) for the virtual
switch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Multicast<wbr>Filtering<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The multicast filtering mode to use
with the switch. Can be one of `legacyFiltering` or `snooping`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the distributed virtual switch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Active<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
active flows are forced to be exported to the collector. Allowed range is
`60` to `3600`. Default: `60`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Collector<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IP address for the Netflow
collector, using IPv4 or IPv6. IPv6 is supported in vSphere Distributed
Switch Version 6.0 or later. Must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Collector<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Port for the Netflow collector. This
must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enables Netflow on all ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Idle<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
idle flows are forced to be exported to the collector. Allowed range is `10`
to `600`. Default: `15`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Internal<wbr>Flows<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to limit analysis to
traffic that has both source and destination served by the same host.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Observation<wbr>Domain<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The observation domain ID for
the Netflow collector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Sampling<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The ratio of total number of packets to
the number of packets analyzed. The default is `0`, which indicates that the
switch should analyze all packets. The maximum value is `1000`, which
indicates an analysis rate of 0.001%.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Resource<wbr>Control<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Set to `true` to enable
network I/O control. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Resource<wbr>Control<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version of network I/O
control to use. Can be one of `version2` or `version3`. Default: `version2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the nfs traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notify<wbr>Switches</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will notify the
broadcast network of an uplink failover, triggering cache updates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port<wbr>Private<wbr>Secondary<wbr>Vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Used to define a secondary VLAN
ID when using private VLANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Standby<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of standby uplinks to be used in
failover. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Teaming<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The uplink teaming policy. Can be one of
`loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tx<wbr>Uplink</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Forward all traffic transmitted by ports for which
this policy applies to its DVS uplinks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of strings that uniquely identifies the names
of the uplinks on the DVS across hosts. The number of items in this list
controls the number of uplinks that exist on the DVS, in addition to the
names.  See here for an example on how to
use this option.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vdp<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vdp<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vdp<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vdp traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vdp<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}- The version of the DVS to create. The default is to
create the DVS at the latest version supported by the version of vSphere
being used. A DVS can be upgraded to another version, but cannot be
downgraded.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtualmachine<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtualmachine<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtualmachine<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the virtualMachine traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtualmachine<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The VLAN ID for single VLAN mode. 0 denotes no VLAN.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vlan<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchvlanrange">List&lt;Distributed<wbr>Virtual<wbr>Switch<wbr>Vlan<wbr>Range<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Used to denote VLAN trunking. Use the `min_vlan`
and `max_vlan` sub-arguments to define the tagged VLAN range. Multiple
`vlan_range` definitions are allowed, but they must not overlap. Example
below:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmotion<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmotion<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmotion<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vmotion traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmotion<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsan<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsan<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsan<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vsan traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsan<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Active<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of active uplinks to be used in load
balancing. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Forged<wbr>Transmits</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Controls whether or not a virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Mac<wbr>Changes</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Controls whether or not the Media Access
Control (MAC) address can be changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Promiscuous</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Block<wbr>All<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Shuts down all ports in the port groups that
this policy applies to, effectively blocking all network access to connected
virtual devices.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Check<wbr>Beacon</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enables beacon probing as an additional measure
to detect NIC failure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Contact<wbr>Detail</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The detailed contact information for the person
who is responsible for the DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Contact<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the person who is responsible for the
DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual switch. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Datacenter<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter where the distributed
virtual switch will be created. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A detailed description for the DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Directpath<wbr>Gen2Allowed</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Allow VMDirectPath Gen2 for the ports
for which this policy applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in bits
per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is enabled
on the port for egress traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during bursts
in bits per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failback</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will re-activate failed
uplinks higher in precedence when they come back up.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Faulttolerance<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Faulttolerance<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Faulttolerance<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the faultTolerance traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Faulttolerance<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The folder to create the DVS in. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hbr<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hbr<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hbr<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the hbr traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hbr<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchhost">[]Distributed<wbr>Virtual<wbr>Switch<wbr>Host</a></span>
    </dt>
    <dd>{{% md %}}Use the `host` block to declare a host specification. The
options are:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ingress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in
bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ingress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ingress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is
enabled on the port for ingress traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ingress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during
bursts in bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv4Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An IPv4 address to identify the switch. This is
mostly useful when used with the Netflow arguments found
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the iSCSI traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lacp<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Link Aggregation Control Protocol group
version to use with the switch. Possible values are `singleLag` and
`multipleLag`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lacp<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enables LACP for the ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lacp<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The LACP mode. Can be one of `active` or `passive`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Link<wbr>Discovery<wbr>Operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Whether to `advertise` or `listen`
for link discovery traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Link<wbr>Discovery<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The discovery protocol type. Valid
types are `cdp` and `lldp`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the management traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the management traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum transmission unit (MTU) for the virtual
switch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Multicast<wbr>Filtering<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The multicast filtering mode to use
with the switch. Can be one of `legacyFiltering` or `snooping`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the distributed virtual switch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Active<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
active flows are forced to be exported to the collector. Allowed range is
`60` to `3600`. Default: `60`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Collector<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}IP address for the Netflow
collector, using IPv4 or IPv6. IPv6 is supported in vSphere Distributed
Switch Version 6.0 or later. Must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Collector<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Port for the Netflow collector. This
must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enables Netflow on all ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Idle<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
idle flows are forced to be exported to the collector. Allowed range is `10`
to `600`. Default: `15`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Internal<wbr>Flows<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to limit analysis to
traffic that has both source and destination served by the same host.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Observation<wbr>Domain<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The observation domain ID for
the Netflow collector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Sampling<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The ratio of total number of packets to
the number of packets analyzed. The default is `0`, which indicates that the
switch should analyze all packets. The maximum value is `1000`, which
indicates an analysis rate of 0.001%.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Resource<wbr>Control<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Set to `true` to enable
network I/O control. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Resource<wbr>Control<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The version of network I/O
control to use. Can be one of `version2` or `version3`. Default: `version2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the nfs traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notify<wbr>Switches</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will notify the
broadcast network of an uplink failover, triggering cache updates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port<wbr>Private<wbr>Secondary<wbr>Vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Used to define a secondary VLAN
ID when using private VLANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Standby<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of standby uplinks to be used in
failover. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Teaming<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The uplink teaming policy. Can be one of
`loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tx<wbr>Uplink</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Forward all traffic transmitted by ports for which
this policy applies to its DVS uplinks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of strings that uniquely identifies the names
of the uplinks on the DVS across hosts. The number of items in this list
controls the number of uplinks that exist on the DVS, in addition to the
names.  See here for an example on how to
use this option.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vdp<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vdp<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vdp<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vdp traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vdp<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}- The version of the DVS to create. The default is to
create the DVS at the latest version supported by the version of vSphere
being used. A DVS can be upgraded to another version, but cannot be
downgraded.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtualmachine<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtualmachine<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtualmachine<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the virtualMachine traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtualmachine<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The VLAN ID for single VLAN mode. 0 denotes no VLAN.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vlan<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchvlanrange">[]Distributed<wbr>Virtual<wbr>Switch<wbr>Vlan<wbr>Range</a></span>
    </dt>
    <dd>{{% md %}}Used to denote VLAN trunking. Use the `min_vlan`
and `max_vlan` sub-arguments to define the tagged VLAN range. Multiple
`vlan_range` definitions are allowed, but they must not overlap. Example
below:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmotion<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmotion<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmotion<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vmotion traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmotion<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsan<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsan<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsan<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vsan traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsan<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>active<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of active uplinks to be used in load
balancing. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Forged<wbr>Transmits</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Controls whether or not a virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Mac<wbr>Changes</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Controls whether or not the Media Access
Control (MAC) address can be changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Promiscuous</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>block<wbr>All<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Shuts down all ports in the port groups that
this policy applies to, effectively blocking all network access to connected
virtual devices.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>check<wbr>Beacon</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enables beacon probing as an additional measure
to detect NIC failure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>contact<wbr>Detail</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The detailed contact information for the person
who is responsible for the DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>contact<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the person who is responsible for the
DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual switch. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>datacenter<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter where the distributed
virtual switch will be created. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A detailed description for the DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>directpath<wbr>Gen2Allowed</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Allow VMDirectPath Gen2 for the ports
for which this policy applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in bits
per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is enabled
on the port for egress traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during bursts
in bits per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failback</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will re-activate failed
uplinks higher in precedence when they come back up.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>faulttolerance<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>faulttolerance<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>faulttolerance<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the faultTolerance traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>faulttolerance<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The folder to create the DVS in. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hbr<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hbr<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hbr<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the hbr traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hbr<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchhost">Distributed<wbr>Virtual<wbr>Switch<wbr>Host[]?</a></span>
    </dt>
    <dd>{{% md %}}Use the `host` block to declare a host specification. The
options are:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ingress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in
bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ingress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ingress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is
enabled on the port for ingress traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ingress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during
bursts in bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv4Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An IPv4 address to identify the switch. This is
mostly useful when used with the Netflow arguments found
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the iSCSI traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lacp<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Link Aggregation Control Protocol group
version to use with the switch. Possible values are `singleLag` and
`multipleLag`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lacp<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enables LACP for the ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lacp<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The LACP mode. Can be one of `active` or `passive`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>link<wbr>Discovery<wbr>Operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Whether to `advertise` or `listen`
for link discovery traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>link<wbr>Discovery<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The discovery protocol type. Valid
types are `cdp` and `lldp`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the management traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the management traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum transmission unit (MTU) for the virtual
switch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>multicast<wbr>Filtering<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The multicast filtering mode to use
with the switch. Can be one of `legacyFiltering` or `snooping`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the distributed virtual switch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow<wbr>Active<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
active flows are forced to be exported to the collector. Allowed range is
`60` to `3600`. Default: `60`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow<wbr>Collector<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IP address for the Netflow
collector, using IPv4 or IPv6. IPv6 is supported in vSphere Distributed
Switch Version 6.0 or later. Must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow<wbr>Collector<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Port for the Netflow collector. This
must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enables Netflow on all ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow<wbr>Idle<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
idle flows are forced to be exported to the collector. Allowed range is `10`
to `600`. Default: `15`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow<wbr>Internal<wbr>Flows<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to limit analysis to
traffic that has both source and destination served by the same host.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow<wbr>Observation<wbr>Domain<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The observation domain ID for
the Netflow collector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow<wbr>Sampling<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The ratio of total number of packets to
the number of packets analyzed. The default is `0`, which indicates that the
switch should analyze all packets. The maximum value is `1000`, which
indicates an analysis rate of 0.001%.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Resource<wbr>Control<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Set to `true` to enable
network I/O control. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Resource<wbr>Control<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version of network I/O
control to use. Can be one of `version2` or `version3`. Default: `version2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the nfs traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notify<wbr>Switches</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will notify the
broadcast network of an uplink failover, triggering cache updates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port<wbr>Private<wbr>Secondary<wbr>Vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Used to define a secondary VLAN
ID when using private VLANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>standby<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of standby uplinks to be used in
failover. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>teaming<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The uplink teaming policy. Can be one of
`loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tx<wbr>Uplink</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Forward all traffic transmitted by ports for which
this policy applies to its DVS uplinks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of strings that uniquely identifies the names
of the uplinks on the DVS across hosts. The number of items in this list
controls the number of uplinks that exist on the DVS, in addition to the
names.  See here for an example on how to
use this option.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vdp<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vdp<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vdp<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vdp traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vdp<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}- The version of the DVS to create. The default is to
create the DVS at the latest version supported by the version of vSphere
being used. A DVS can be upgraded to another version, but cannot be
downgraded.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtualmachine<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtualmachine<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtualmachine<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the virtualMachine traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtualmachine<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The VLAN ID for single VLAN mode. 0 denotes no VLAN.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vlan<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchvlanrange">Distributed<wbr>Virtual<wbr>Switch<wbr>Vlan<wbr>Range[]?</a></span>
    </dt>
    <dd>{{% md %}}Used to denote VLAN trunking. Use the `min_vlan`
and `max_vlan` sub-arguments to define the tagged VLAN range. Multiple
`vlan_range` definitions are allowed, but they must not overlap. Example
below:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmotion<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmotion<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmotion<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vmotion traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmotion<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsan<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsan<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsan<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vsan traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsan<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>active_<wbr>uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of active uplinks to be used in load
balancing. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>forged_<wbr>transmits</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Controls whether or not a virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>mac_<wbr>changes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Controls whether or not the Media Access
Control (MAC) address can be changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>promiscuous</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>block_<wbr>all_<wbr>ports</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Shuts down all ports in the port groups that
this policy applies to, effectively blocking all network access to connected
virtual devices.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>check_<wbr>beacon</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enables beacon probing as an additional measure
to detect NIC failure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>contact_<wbr>detail</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The detailed contact information for the person
who is responsible for the DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>contact_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the person who is responsible for the
DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual switch. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>datacenter_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter where the distributed
virtual switch will be created. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A detailed description for the DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>directpath_<wbr>gen2_<wbr>allowed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allow VMDirectPath Gen2 for the ports
for which this policy applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress_<wbr>shaping_<wbr>average_<wbr>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in bits
per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress_<wbr>shaping_<wbr>burst_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress_<wbr>shaping_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is enabled
on the port for egress traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress_<wbr>shaping_<wbr>peak_<wbr>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during bursts
in bits per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failback</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will re-activate failed
uplinks higher in precedence when they come back up.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>faulttolerance_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>faulttolerance_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>faulttolerance_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the faultTolerance traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>faulttolerance_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The folder to create the DVS in. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hbr_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hbr_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hbr_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the hbr traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hbr_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchhost">List[Distributed<wbr>Virtual<wbr>Switch<wbr>Host]</a></span>
    </dt>
    <dd>{{% md %}}Use the `host` block to declare a host specification. The
options are:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ingress_<wbr>shaping_<wbr>average_<wbr>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in
bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ingress_<wbr>shaping_<wbr>burst_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ingress_<wbr>shaping_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is
enabled on the port for ingress traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ingress_<wbr>shaping_<wbr>peak_<wbr>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during
bursts in bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv4_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An IPv4 address to identify the switch. This is
mostly useful when used with the Netflow arguments found
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the iSCSI traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lacp_<wbr>api_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Link Aggregation Control Protocol group
version to use with the switch. Possible values are `singleLag` and
`multipleLag`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lacp_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enables LACP for the ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lacp_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The LACP mode. Can be one of `active` or `passive`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>link_<wbr>discovery_<wbr>operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Whether to `advertise` or `listen`
for link discovery traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>link_<wbr>discovery_<wbr>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The discovery protocol type. Valid
types are `cdp` and `lldp`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the management traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the management traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum transmission unit (MTU) for the virtual
switch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>multicast_<wbr>filtering_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The multicast filtering mode to use
with the switch. Can be one of `legacyFiltering` or `snooping`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the distributed virtual switch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow_<wbr>active_<wbr>flow_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
active flows are forced to be exported to the collector. Allowed range is
`60` to `3600`. Default: `60`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow_<wbr>collector_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}IP address for the Netflow
collector, using IPv4 or IPv6. IPv6 is supported in vSphere Distributed
Switch Version 6.0 or later. Must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow_<wbr>collector_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Port for the Netflow collector. This
must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enables Netflow on all ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow_<wbr>idle_<wbr>flow_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
idle flows are forced to be exported to the collector. Allowed range is `10`
to `600`. Default: `15`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow_<wbr>internal_<wbr>flows_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to limit analysis to
traffic that has both source and destination served by the same host.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow_<wbr>observation_<wbr>domain_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The observation domain ID for
the Netflow collector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow_<wbr>sampling_<wbr>rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The ratio of total number of packets to
the number of packets analyzed. The default is `0`, which indicates that the
switch should analyze all packets. The maximum value is `1000`, which
indicates an analysis rate of 0.001%.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>resource_<wbr>control_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to `true` to enable
network I/O control. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>resource_<wbr>control_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The version of network I/O
control to use. Can be one of `version2` or `version3`. Default: `version2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the nfs traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notify_<wbr>switches</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will notify the
broadcast network of an uplink failover, triggering cache updates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port_<wbr>private_<wbr>secondary_<wbr>vlan_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Used to define a secondary VLAN
ID when using private VLANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>standby_<wbr>uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of standby uplinks to be used in
failover. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>teaming_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The uplink teaming policy. Can be one of
`loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tx_<wbr>uplink</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Forward all traffic transmitted by ports for which
this policy applies to its DVS uplinks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of strings that uniquely identifies the names
of the uplinks on the DVS across hosts. The number of items in this list
controls the number of uplinks that exist on the DVS, in addition to the
names.  See here for an example on how to
use this option.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vdp_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vdp_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vdp_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vdp traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vdp_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}- The version of the DVS to create. The default is to
create the DVS at the latest version supported by the version of vSphere
being used. A DVS can be upgraded to another version, but cannot be
downgraded.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtualmachine_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtualmachine_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtualmachine_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the virtualMachine traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtualmachine_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vlan_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The VLAN ID for single VLAN mode. 0 denotes no VLAN.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vlan_<wbr>ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchvlanrange">List[Distributed<wbr>Virtual<wbr>Switch<wbr>Vlan<wbr>Range]</a></span>
    </dt>
    <dd>{{% md %}}Used to denote VLAN trunking. Use the `min_vlan`
and `max_vlan` sub-arguments to define the tagged VLAN range. Multiple
`vlan_range` definitions are allowed, but they must not overlap. Example
below:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmotion_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmotion_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmotion_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vmotion traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmotion_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsan_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsan_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsan_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vsan traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsan_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## DistributedVirtualSwitch Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Active<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of active uplinks to be used in load
balancing. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Forged<wbr>Transmits</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Controls whether or not a virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Mac<wbr>Changes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Controls whether or not the Media Access
Control (MAC) address can be changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Promiscuous</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Block<wbr>All<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Shuts down all ports in the port groups that
this policy applies to, effectively blocking all network access to connected
virtual devices.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Check<wbr>Beacon</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enables beacon probing as an additional measure
to detect NIC failure.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Config<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version string of the configuration that this spec is trying to change.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Contact<wbr>Detail</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The detailed contact information for the person
who is responsible for the DVS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Contact<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the person who is responsible for the
DVS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual switch. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Datacenter<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter where the distributed
virtual switch will be created. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A detailed description for the DVS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Directpath<wbr>Gen2Allowed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allow VMDirectPath Gen2 for the ports
for which this policy applies to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Egress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in bits
per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Egress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Egress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is enabled
on the port for egress traffic.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Egress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during bursts
in bits per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Failback</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will re-activate failed
uplinks higher in precedence when they come back up.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Faulttolerance<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Faulttolerance<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Faulttolerance<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the faultTolerance traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Faulttolerance<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The folder to create the DVS in. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hbr<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hbr<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hbr<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the hbr traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hbr<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchhost">List&lt;Distributed<wbr>Virtual<wbr>Switch<wbr>Host&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Use the `host` block to declare a host specification. The
options are:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ingress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in
bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ingress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ingress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is
enabled on the port for ingress traffic.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ingress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during
bursts in bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ipv4Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An IPv4 address to identify the switch. This is
mostly useful when used with the Netflow arguments found
below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iscsi<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iscsi<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iscsi<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the iSCSI traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iscsi<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lacp<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Link Aggregation Control Protocol group
version to use with the switch. Possible values are `singleLag` and
`multipleLag`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lacp<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enables LACP for the ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lacp<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The LACP mode. Can be one of `active` or `passive`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Link<wbr>Discovery<wbr>Operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Whether to `advertise` or `listen`
for link discovery traffic.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Link<wbr>Discovery<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The discovery protocol type. Valid
types are `cdp` and `lldp`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Management<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Management<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Management<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the management traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Management<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the management traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum transmission unit (MTU) for the virtual
switch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Multicast<wbr>Filtering<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multicast filtering mode to use
with the switch. Can be one of `legacyFiltering` or `snooping`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the distributed virtual switch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Netflow<wbr>Active<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
active flows are forced to be exported to the collector. Allowed range is
`60` to `3600`. Default: `60`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Netflow<wbr>Collector<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IP address for the Netflow
collector, using IPv4 or IPv6. IPv6 is supported in vSphere Distributed
Switch Version 6.0 or later. Must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Netflow<wbr>Collector<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Port for the Netflow collector. This
must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Netflow<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enables Netflow on all ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Netflow<wbr>Idle<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
idle flows are forced to be exported to the collector. Allowed range is `10`
to `600`. Default: `15`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Netflow<wbr>Internal<wbr>Flows<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to limit analysis to
traffic that has both source and destination served by the same host.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Netflow<wbr>Observation<wbr>Domain<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The observation domain ID for
the Netflow collector.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Netflow<wbr>Sampling<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The ratio of total number of packets to
the number of packets analyzed. The default is `0`, which indicates that the
switch should analyze all packets. The maximum value is `1000`, which
indicates an analysis rate of 0.001%.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Resource<wbr>Control<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Set to `true` to enable
network I/O control. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Resource<wbr>Control<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version of network I/O
control to use. Can be one of `version2` or `version3`. Default: `version2`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Nfs<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Nfs<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Nfs<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the nfs traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Nfs<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Notify<wbr>Switches</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will notify the
broadcast network of an uplink failover, triggering cache updates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port<wbr>Private<wbr>Secondary<wbr>Vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Used to define a secondary VLAN
ID when using private VLANs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Standby<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of standby uplinks to be used in
failover. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Teaming<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The uplink teaming policy. Can be one of
`loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tx<wbr>Uplink</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Forward all traffic transmitted by ports for which
this policy applies to its DVS uplinks.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of strings that uniquely identifies the names
of the uplinks on the DVS across hosts. The number of items in this list
controls the number of uplinks that exist on the DVS, in addition to the
names.  See here for an example on how to
use this option.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vdp<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vdp<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vdp<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vdp traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vdp<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}- The version of the DVS to create. The default is to
create the DVS at the latest version supported by the version of vSphere
being used. A DVS can be upgraded to another version, but cannot be
downgraded.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Virtualmachine<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Virtualmachine<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Virtualmachine<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the virtualMachine traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Virtualmachine<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The VLAN ID for single VLAN mode. 0 denotes no VLAN.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vlan<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchvlanrange">List&lt;Distributed<wbr>Virtual<wbr>Switch<wbr>Vlan<wbr>Range&gt;</a></span>
    </dt>
    <dd>{{% md %}}Used to denote VLAN trunking. Use the `min_vlan`
and `max_vlan` sub-arguments to define the tagged VLAN range. Multiple
`vlan_range` definitions are allowed, but they must not overlap. Example
below:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vmotion<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vmotion<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vmotion<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vmotion traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vmotion<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vsan<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vsan<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vsan<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vsan traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vsan<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Active<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of active uplinks to be used in load
balancing. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Forged<wbr>Transmits</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Controls whether or not a virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Mac<wbr>Changes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Controls whether or not the Media Access
Control (MAC) address can be changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allow<wbr>Promiscuous</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Block<wbr>All<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Shuts down all ports in the port groups that
this policy applies to, effectively blocking all network access to connected
virtual devices.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Check<wbr>Beacon</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enables beacon probing as an additional measure
to detect NIC failure.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Config<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version string of the configuration that this spec is trying to change.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Contact<wbr>Detail</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The detailed contact information for the person
who is responsible for the DVS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Contact<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the person who is responsible for the
DVS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual switch. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Datacenter<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter where the distributed
virtual switch will be created. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A detailed description for the DVS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Directpath<wbr>Gen2Allowed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allow VMDirectPath Gen2 for the ports
for which this policy applies to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Egress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in bits
per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Egress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Egress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is enabled
on the port for egress traffic.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Egress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during bursts
in bits per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Failback</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will re-activate failed
uplinks higher in precedence when they come back up.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Faulttolerance<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Faulttolerance<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Faulttolerance<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the faultTolerance traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Faulttolerance<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The folder to create the DVS in. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hbr<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hbr<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hbr<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the hbr traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hbr<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchhost">[]Distributed<wbr>Virtual<wbr>Switch<wbr>Host</a></span>
    </dt>
    <dd>{{% md %}}Use the `host` block to declare a host specification. The
options are:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ingress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in
bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ingress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ingress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is
enabled on the port for ingress traffic.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ingress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during
bursts in bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ipv4Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An IPv4 address to identify the switch. This is
mostly useful when used with the Netflow arguments found
below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iscsi<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iscsi<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iscsi<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the iSCSI traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iscsi<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lacp<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Link Aggregation Control Protocol group
version to use with the switch. Possible values are `singleLag` and
`multipleLag`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lacp<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enables LACP for the ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lacp<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The LACP mode. Can be one of `active` or `passive`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Link<wbr>Discovery<wbr>Operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Whether to `advertise` or `listen`
for link discovery traffic.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Link<wbr>Discovery<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The discovery protocol type. Valid
types are `cdp` and `lldp`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Management<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Management<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Management<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the management traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Management<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the management traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum transmission unit (MTU) for the virtual
switch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Multicast<wbr>Filtering<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multicast filtering mode to use
with the switch. Can be one of `legacyFiltering` or `snooping`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the distributed virtual switch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Netflow<wbr>Active<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
active flows are forced to be exported to the collector. Allowed range is
`60` to `3600`. Default: `60`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Netflow<wbr>Collector<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}IP address for the Netflow
collector, using IPv4 or IPv6. IPv6 is supported in vSphere Distributed
Switch Version 6.0 or later. Must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Netflow<wbr>Collector<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Port for the Netflow collector. This
must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Netflow<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enables Netflow on all ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Netflow<wbr>Idle<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
idle flows are forced to be exported to the collector. Allowed range is `10`
to `600`. Default: `15`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Netflow<wbr>Internal<wbr>Flows<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to limit analysis to
traffic that has both source and destination served by the same host.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Netflow<wbr>Observation<wbr>Domain<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The observation domain ID for
the Netflow collector.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Netflow<wbr>Sampling<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The ratio of total number of packets to
the number of packets analyzed. The default is `0`, which indicates that the
switch should analyze all packets. The maximum value is `1000`, which
indicates an analysis rate of 0.001%.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Resource<wbr>Control<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Set to `true` to enable
network I/O control. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Resource<wbr>Control<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version of network I/O
control to use. Can be one of `version2` or `version3`. Default: `version2`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Nfs<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Nfs<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Nfs<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the nfs traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Nfs<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Notify<wbr>Switches</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will notify the
broadcast network of an uplink failover, triggering cache updates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port<wbr>Private<wbr>Secondary<wbr>Vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Used to define a secondary VLAN
ID when using private VLANs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Standby<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of standby uplinks to be used in
failover. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Teaming<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The uplink teaming policy. Can be one of
`loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tx<wbr>Uplink</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Forward all traffic transmitted by ports for which
this policy applies to its DVS uplinks.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of strings that uniquely identifies the names
of the uplinks on the DVS across hosts. The number of items in this list
controls the number of uplinks that exist on the DVS, in addition to the
names.  See here for an example on how to
use this option.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vdp<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vdp<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vdp<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vdp traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vdp<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}- The version of the DVS to create. The default is to
create the DVS at the latest version supported by the version of vSphere
being used. A DVS can be upgraded to another version, but cannot be
downgraded.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Virtualmachine<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Virtualmachine<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Virtualmachine<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the virtualMachine traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Virtualmachine<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The VLAN ID for single VLAN mode. 0 denotes no VLAN.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vlan<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchvlanrange">[]Distributed<wbr>Virtual<wbr>Switch<wbr>Vlan<wbr>Range</a></span>
    </dt>
    <dd>{{% md %}}Used to denote VLAN trunking. Use the `min_vlan`
and `max_vlan` sub-arguments to define the tagged VLAN range. Multiple
`vlan_range` definitions are allowed, but they must not overlap. Example
below:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vmotion<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vmotion<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vmotion<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vmotion traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vmotion<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vsan<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vsan<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vsan<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vsan traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vsan<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>active<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of active uplinks to be used in load
balancing. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow<wbr>Forged<wbr>Transmits</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Controls whether or not a virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow<wbr>Mac<wbr>Changes</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Controls whether or not the Media Access
Control (MAC) address can be changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow<wbr>Promiscuous</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>block<wbr>All<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Shuts down all ports in the port groups that
this policy applies to, effectively blocking all network access to connected
virtual devices.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>check<wbr>Beacon</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enables beacon probing as an additional measure
to detect NIC failure.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>config<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version string of the configuration that this spec is trying to change.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>contact<wbr>Detail</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The detailed contact information for the person
who is responsible for the DVS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>contact<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the person who is responsible for the
DVS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual switch. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>datacenter<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter where the distributed
virtual switch will be created. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A detailed description for the DVS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>directpath<wbr>Gen2Allowed</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Allow VMDirectPath Gen2 for the ports
for which this policy applies to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>egress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in bits
per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>egress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>egress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is enabled
on the port for egress traffic.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>egress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during bursts
in bits per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>failback</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will re-activate failed
uplinks higher in precedence when they come back up.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>faulttolerance<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>faulttolerance<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>faulttolerance<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the faultTolerance traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>faulttolerance<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The folder to create the DVS in. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hbr<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hbr<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hbr<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the hbr traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hbr<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchhost">Distributed<wbr>Virtual<wbr>Switch<wbr>Host[]?</a></span>
    </dt>
    <dd>{{% md %}}Use the `host` block to declare a host specification. The
options are:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ingress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in
bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ingress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ingress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is
enabled on the port for ingress traffic.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ingress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during
bursts in bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ipv4Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An IPv4 address to identify the switch. This is
mostly useful when used with the Netflow arguments found
below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iscsi<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iscsi<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iscsi<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the iSCSI traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iscsi<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lacp<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Link Aggregation Control Protocol group
version to use with the switch. Possible values are `singleLag` and
`multipleLag`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lacp<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enables LACP for the ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lacp<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The LACP mode. Can be one of `active` or `passive`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>link<wbr>Discovery<wbr>Operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Whether to `advertise` or `listen`
for link discovery traffic.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>link<wbr>Discovery<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The discovery protocol type. Valid
types are `cdp` and `lldp`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>management<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>management<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>management<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the management traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>management<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the management traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max<wbr>Mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum transmission unit (MTU) for the virtual
switch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>multicast<wbr>Filtering<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The multicast filtering mode to use
with the switch. Can be one of `legacyFiltering` or `snooping`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the distributed virtual switch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>netflow<wbr>Active<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
active flows are forced to be exported to the collector. Allowed range is
`60` to `3600`. Default: `60`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>netflow<wbr>Collector<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IP address for the Netflow
collector, using IPv4 or IPv6. IPv6 is supported in vSphere Distributed
Switch Version 6.0 or later. Must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>netflow<wbr>Collector<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Port for the Netflow collector. This
must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>netflow<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enables Netflow on all ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>netflow<wbr>Idle<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
idle flows are forced to be exported to the collector. Allowed range is `10`
to `600`. Default: `15`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>netflow<wbr>Internal<wbr>Flows<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to limit analysis to
traffic that has both source and destination served by the same host.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>netflow<wbr>Observation<wbr>Domain<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The observation domain ID for
the Netflow collector.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>netflow<wbr>Sampling<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The ratio of total number of packets to
the number of packets analyzed. The default is `0`, which indicates that the
switch should analyze all packets. The maximum value is `1000`, which
indicates an analysis rate of 0.001%.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Resource<wbr>Control<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Set to `true` to enable
network I/O control. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Resource<wbr>Control<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version of network I/O
control to use. Can be one of `version2` or `version3`. Default: `version2`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>nfs<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>nfs<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>nfs<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the nfs traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>nfs<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>notify<wbr>Switches</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will notify the
broadcast network of an uplink failover, triggering cache updates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port<wbr>Private<wbr>Secondary<wbr>Vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Used to define a secondary VLAN
ID when using private VLANs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>standby<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of standby uplinks to be used in
failover. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>teaming<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The uplink teaming policy. Can be one of
`loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tx<wbr>Uplink</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Forward all traffic transmitted by ports for which
this policy applies to its DVS uplinks.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of strings that uniquely identifies the names
of the uplinks on the DVS across hosts. The number of items in this list
controls the number of uplinks that exist on the DVS, in addition to the
names.  See here for an example on how to
use this option.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vdp<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vdp<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vdp<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vdp traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vdp<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}- The version of the DVS to create. The default is to
create the DVS at the latest version supported by the version of vSphere
being used. A DVS can be upgraded to another version, but cannot be
downgraded.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>virtualmachine<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>virtualmachine<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>virtualmachine<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the virtualMachine traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>virtualmachine<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The VLAN ID for single VLAN mode. 0 denotes no VLAN.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vlan<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchvlanrange">Distributed<wbr>Virtual<wbr>Switch<wbr>Vlan<wbr>Range[]</a></span>
    </dt>
    <dd>{{% md %}}Used to denote VLAN trunking. Use the `min_vlan`
and `max_vlan` sub-arguments to define the tagged VLAN range. Multiple
`vlan_range` definitions are allowed, but they must not overlap. Example
below:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vmotion<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vmotion<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vmotion<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vmotion traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vmotion<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vsan<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vsan<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vsan<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vsan traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vsan<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>active_<wbr>uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of active uplinks to be used in load
balancing. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow_<wbr>forged_<wbr>transmits</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Controls whether or not a virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow_<wbr>mac_<wbr>changes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Controls whether or not the Media Access
Control (MAC) address can be changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allow_<wbr>promiscuous</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>block_<wbr>all_<wbr>ports</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Shuts down all ports in the port groups that
this policy applies to, effectively blocking all network access to connected
virtual devices.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>check_<wbr>beacon</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enables beacon probing as an additional measure
to detect NIC failure.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>config_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The version string of the configuration that this spec is trying to change.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>contact_<wbr>detail</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The detailed contact information for the person
who is responsible for the DVS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>contact_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the person who is responsible for the
DVS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom_<wbr>attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual switch. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>datacenter_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter where the distributed
virtual switch will be created. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A detailed description for the DVS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>directpath_<wbr>gen2_<wbr>allowed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allow VMDirectPath Gen2 for the ports
for which this policy applies to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>egress_<wbr>shaping_<wbr>average_<wbr>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in bits
per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>egress_<wbr>shaping_<wbr>burst_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>egress_<wbr>shaping_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is enabled
on the port for egress traffic.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>egress_<wbr>shaping_<wbr>peak_<wbr>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during bursts
in bits per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>failback</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will re-activate failed
uplinks higher in precedence when they come back up.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>faulttolerance_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>faulttolerance_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>faulttolerance_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the faultTolerance traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>faulttolerance_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The folder to create the DVS in. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hbr_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hbr_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hbr_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the hbr traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hbr_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchhost">List[Distributed<wbr>Virtual<wbr>Switch<wbr>Host]</a></span>
    </dt>
    <dd>{{% md %}}Use the `host` block to declare a host specification. The
options are:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ingress_<wbr>shaping_<wbr>average_<wbr>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in
bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ingress_<wbr>shaping_<wbr>burst_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ingress_<wbr>shaping_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is
enabled on the port for ingress traffic.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ingress_<wbr>shaping_<wbr>peak_<wbr>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during
bursts in bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ipv4_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An IPv4 address to identify the switch. This is
mostly useful when used with the Netflow arguments found
below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iscsi_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iscsi_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iscsi_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the iSCSI traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iscsi_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lacp_<wbr>api_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Link Aggregation Control Protocol group
version to use with the switch. Possible values are `singleLag` and
`multipleLag`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lacp_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enables LACP for the ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lacp_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The LACP mode. Can be one of `active` or `passive`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>link_<wbr>discovery_<wbr>operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Whether to `advertise` or `listen`
for link discovery traffic.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>link_<wbr>discovery_<wbr>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The discovery protocol type. Valid
types are `cdp` and `lldp`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>management_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>management_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>management_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the management traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>management_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the management traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max_<wbr>mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum transmission unit (MTU) for the virtual
switch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>multicast_<wbr>filtering_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The multicast filtering mode to use
with the switch. Can be one of `legacyFiltering` or `snooping`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the distributed virtual switch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>netflow_<wbr>active_<wbr>flow_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
active flows are forced to be exported to the collector. Allowed range is
`60` to `3600`. Default: `60`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>netflow_<wbr>collector_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}IP address for the Netflow
collector, using IPv4 or IPv6. IPv6 is supported in vSphere Distributed
Switch Version 6.0 or later. Must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>netflow_<wbr>collector_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Port for the Netflow collector. This
must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>netflow_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enables Netflow on all ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>netflow_<wbr>idle_<wbr>flow_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
idle flows are forced to be exported to the collector. Allowed range is `10`
to `600`. Default: `15`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>netflow_<wbr>internal_<wbr>flows_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to limit analysis to
traffic that has both source and destination served by the same host.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>netflow_<wbr>observation_<wbr>domain_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The observation domain ID for
the Netflow collector.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>netflow_<wbr>sampling_<wbr>rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The ratio of total number of packets to
the number of packets analyzed. The default is `0`, which indicates that the
switch should analyze all packets. The maximum value is `1000`, which
indicates an analysis rate of 0.001%.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>resource_<wbr>control_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to `true` to enable
network I/O control. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>resource_<wbr>control_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The version of network I/O
control to use. Can be one of `version2` or `version3`. Default: `version2`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>nfs_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>nfs_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>nfs_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the nfs traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>nfs_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>notify_<wbr>switches</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will notify the
broadcast network of an uplink failover, triggering cache updates.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port_<wbr>private_<wbr>secondary_<wbr>vlan_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Used to define a secondary VLAN
ID when using private VLANs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>standby_<wbr>uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of standby uplinks to be used in
failover. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>teaming_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The uplink teaming policy. Can be one of
`loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tx_<wbr>uplink</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Forward all traffic transmitted by ports for which
this policy applies to its DVS uplinks.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of strings that uniquely identifies the names
of the uplinks on the DVS across hosts. The number of items in this list
controls the number of uplinks that exist on the DVS, in addition to the
names.  See here for an example on how to
use this option.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vdp_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vdp_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vdp_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vdp traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vdp_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}- The version of the DVS to create. The default is to
create the DVS at the latest version supported by the version of vSphere
being used. A DVS can be upgraded to another version, but cannot be
downgraded.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>virtualmachine_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>virtualmachine_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>virtualmachine_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the virtualMachine traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>virtualmachine_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vlan_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The VLAN ID for single VLAN mode. 0 denotes no VLAN.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vlan_<wbr>ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchvlanrange">List[Distributed<wbr>Virtual<wbr>Switch<wbr>Vlan<wbr>Range]</a></span>
    </dt>
    <dd>{{% md %}}Used to denote VLAN trunking. Use the `min_vlan`
and `max_vlan` sub-arguments to define the tagged VLAN range. Multiple
`vlan_range` definitions are allowed, but they must not overlap. Example
below:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vmotion_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vmotion_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vmotion_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vmotion traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vmotion_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vsan_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vsan_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vsan_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vsan traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vsan_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing DistributedVirtualSwitch Resource

Get an existing DistributedVirtualSwitch resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#DistributedVirtualSwitchState">DistributedVirtualSwitchState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#DistributedVirtualSwitch">DistributedVirtualSwitch</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>active_uplinks=None<span class="p">, </span>allow_forged_transmits=None<span class="p">, </span>allow_mac_changes=None<span class="p">, </span>allow_promiscuous=None<span class="p">, </span>block_all_ports=None<span class="p">, </span>check_beacon=None<span class="p">, </span>config_version=None<span class="p">, </span>contact_detail=None<span class="p">, </span>contact_name=None<span class="p">, </span>custom_attributes=None<span class="p">, </span>datacenter_id=None<span class="p">, </span>description=None<span class="p">, </span>directpath_gen2_allowed=None<span class="p">, </span>egress_shaping_average_bandwidth=None<span class="p">, </span>egress_shaping_burst_size=None<span class="p">, </span>egress_shaping_enabled=None<span class="p">, </span>egress_shaping_peak_bandwidth=None<span class="p">, </span>failback=None<span class="p">, </span>faulttolerance_maximum_mbit=None<span class="p">, </span>faulttolerance_reservation_mbit=None<span class="p">, </span>faulttolerance_share_count=None<span class="p">, </span>faulttolerance_share_level=None<span class="p">, </span>folder=None<span class="p">, </span>hbr_maximum_mbit=None<span class="p">, </span>hbr_reservation_mbit=None<span class="p">, </span>hbr_share_count=None<span class="p">, </span>hbr_share_level=None<span class="p">, </span>hosts=None<span class="p">, </span>ingress_shaping_average_bandwidth=None<span class="p">, </span>ingress_shaping_burst_size=None<span class="p">, </span>ingress_shaping_enabled=None<span class="p">, </span>ingress_shaping_peak_bandwidth=None<span class="p">, </span>ipv4_address=None<span class="p">, </span>iscsi_maximum_mbit=None<span class="p">, </span>iscsi_reservation_mbit=None<span class="p">, </span>iscsi_share_count=None<span class="p">, </span>iscsi_share_level=None<span class="p">, </span>lacp_api_version=None<span class="p">, </span>lacp_enabled=None<span class="p">, </span>lacp_mode=None<span class="p">, </span>link_discovery_operation=None<span class="p">, </span>link_discovery_protocol=None<span class="p">, </span>management_maximum_mbit=None<span class="p">, </span>management_reservation_mbit=None<span class="p">, </span>management_share_count=None<span class="p">, </span>management_share_level=None<span class="p">, </span>max_mtu=None<span class="p">, </span>multicast_filtering_mode=None<span class="p">, </span>name=None<span class="p">, </span>netflow_active_flow_timeout=None<span class="p">, </span>netflow_collector_ip_address=None<span class="p">, </span>netflow_collector_port=None<span class="p">, </span>netflow_enabled=None<span class="p">, </span>netflow_idle_flow_timeout=None<span class="p">, </span>netflow_internal_flows_only=None<span class="p">, </span>netflow_observation_domain_id=None<span class="p">, </span>netflow_sampling_rate=None<span class="p">, </span>network_resource_control_enabled=None<span class="p">, </span>network_resource_control_version=None<span class="p">, </span>nfs_maximum_mbit=None<span class="p">, </span>nfs_reservation_mbit=None<span class="p">, </span>nfs_share_count=None<span class="p">, </span>nfs_share_level=None<span class="p">, </span>notify_switches=None<span class="p">, </span>port_private_secondary_vlan_id=None<span class="p">, </span>standby_uplinks=None<span class="p">, </span>tags=None<span class="p">, </span>teaming_policy=None<span class="p">, </span>tx_uplink=None<span class="p">, </span>uplinks=None<span class="p">, </span>vdp_maximum_mbit=None<span class="p">, </span>vdp_reservation_mbit=None<span class="p">, </span>vdp_share_count=None<span class="p">, </span>vdp_share_level=None<span class="p">, </span>version=None<span class="p">, </span>virtualmachine_maximum_mbit=None<span class="p">, </span>virtualmachine_reservation_mbit=None<span class="p">, </span>virtualmachine_share_count=None<span class="p">, </span>virtualmachine_share_level=None<span class="p">, </span>vlan_id=None<span class="p">, </span>vlan_ranges=None<span class="p">, </span>vmotion_maximum_mbit=None<span class="p">, </span>vmotion_reservation_mbit=None<span class="p">, </span>vmotion_share_count=None<span class="p">, </span>vmotion_share_level=None<span class="p">, </span>vsan_maximum_mbit=None<span class="p">, </span>vsan_reservation_mbit=None<span class="p">, </span>vsan_share_count=None<span class="p">, </span>vsan_share_level=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetDistributedVirtualSwitch<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/go/vsphere/?tab=doc#DistributedVirtualSwitchState">DistributedVirtualSwitchState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/go/vsphere/?tab=doc#DistributedVirtualSwitch">DistributedVirtualSwitch</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere..DistributedVirtualSwitch.html">DistributedVirtualSwitch</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere..DistributedVirtualSwitchState.html">DistributedVirtualSwitchState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Active<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of active uplinks to be used in load
balancing. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Forged<wbr>Transmits</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Controls whether or not a virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Mac<wbr>Changes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Controls whether or not the Media Access
Control (MAC) address can be changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Promiscuous</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Block<wbr>All<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Shuts down all ports in the port groups that
this policy applies to, effectively blocking all network access to connected
virtual devices.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Check<wbr>Beacon</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enables beacon probing as an additional measure
to detect NIC failure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Config<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version string of the configuration that this spec is trying to change.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Contact<wbr>Detail</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The detailed contact information for the person
who is responsible for the DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Contact<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the person who is responsible for the
DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual switch. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datacenter<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter where the distributed
virtual switch will be created. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A detailed description for the DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Directpath<wbr>Gen2Allowed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Allow VMDirectPath Gen2 for the ports
for which this policy applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in bits
per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is enabled
on the port for egress traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during bursts
in bits per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failback</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will re-activate failed
uplinks higher in precedence when they come back up.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Faulttolerance<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Faulttolerance<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Faulttolerance<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the faultTolerance traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Faulttolerance<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The folder to create the DVS in. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hbr<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hbr<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hbr<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the hbr traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hbr<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchhost">List&lt;Distributed<wbr>Virtual<wbr>Switch<wbr>Host<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Use the `host` block to declare a host specification. The
options are:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ingress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in
bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ingress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ingress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is
enabled on the port for ingress traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ingress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during
bursts in bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv4Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An IPv4 address to identify the switch. This is
mostly useful when used with the Netflow arguments found
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the iSCSI traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lacp<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Link Aggregation Control Protocol group
version to use with the switch. Possible values are `singleLag` and
`multipleLag`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lacp<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enables LACP for the ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lacp<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The LACP mode. Can be one of `active` or `passive`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Link<wbr>Discovery<wbr>Operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Whether to `advertise` or `listen`
for link discovery traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Link<wbr>Discovery<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The discovery protocol type. Valid
types are `cdp` and `lldp`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the management traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the management traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum transmission unit (MTU) for the virtual
switch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Multicast<wbr>Filtering<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The multicast filtering mode to use
with the switch. Can be one of `legacyFiltering` or `snooping`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the distributed virtual switch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Active<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
active flows are forced to be exported to the collector. Allowed range is
`60` to `3600`. Default: `60`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Collector<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IP address for the Netflow
collector, using IPv4 or IPv6. IPv6 is supported in vSphere Distributed
Switch Version 6.0 or later. Must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Collector<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Port for the Netflow collector. This
must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enables Netflow on all ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Idle<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
idle flows are forced to be exported to the collector. Allowed range is `10`
to `600`. Default: `15`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Internal<wbr>Flows<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to limit analysis to
traffic that has both source and destination served by the same host.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Observation<wbr>Domain<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The observation domain ID for
the Netflow collector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Sampling<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The ratio of total number of packets to
the number of packets analyzed. The default is `0`, which indicates that the
switch should analyze all packets. The maximum value is `1000`, which
indicates an analysis rate of 0.001%.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Resource<wbr>Control<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Set to `true` to enable
network I/O control. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Resource<wbr>Control<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version of network I/O
control to use. Can be one of `version2` or `version3`. Default: `version2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the nfs traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notify<wbr>Switches</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will notify the
broadcast network of an uplink failover, triggering cache updates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port<wbr>Private<wbr>Secondary<wbr>Vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Used to define a secondary VLAN
ID when using private VLANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Standby<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of standby uplinks to be used in
failover. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Teaming<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The uplink teaming policy. Can be one of
`loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tx<wbr>Uplink</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Forward all traffic transmitted by ports for which
this policy applies to its DVS uplinks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of strings that uniquely identifies the names
of the uplinks on the DVS across hosts. The number of items in this list
controls the number of uplinks that exist on the DVS, in addition to the
names.  See here for an example on how to
use this option.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vdp<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vdp<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vdp<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vdp traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vdp<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}- The version of the DVS to create. The default is to
create the DVS at the latest version supported by the version of vSphere
being used. A DVS can be upgraded to another version, but cannot be
downgraded.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtualmachine<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtualmachine<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtualmachine<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the virtualMachine traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtualmachine<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The VLAN ID for single VLAN mode. 0 denotes no VLAN.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vlan<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchvlanrange">List&lt;Distributed<wbr>Virtual<wbr>Switch<wbr>Vlan<wbr>Range<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Used to denote VLAN trunking. Use the `min_vlan`
and `max_vlan` sub-arguments to define the tagged VLAN range. Multiple
`vlan_range` definitions are allowed, but they must not overlap. Example
below:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmotion<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmotion<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmotion<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vmotion traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmotion<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsan<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsan<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsan<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vsan traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsan<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Active<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of active uplinks to be used in load
balancing. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Forged<wbr>Transmits</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Controls whether or not a virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Mac<wbr>Changes</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Controls whether or not the Media Access
Control (MAC) address can be changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Promiscuous</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Block<wbr>All<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Shuts down all ports in the port groups that
this policy applies to, effectively blocking all network access to connected
virtual devices.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Check<wbr>Beacon</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enables beacon probing as an additional measure
to detect NIC failure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Config<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The version string of the configuration that this spec is trying to change.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Contact<wbr>Detail</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The detailed contact information for the person
who is responsible for the DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Contact<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the person who is responsible for the
DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual switch. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Datacenter<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter where the distributed
virtual switch will be created. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A detailed description for the DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Directpath<wbr>Gen2Allowed</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Allow VMDirectPath Gen2 for the ports
for which this policy applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in bits
per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is enabled
on the port for egress traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Egress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during bursts
in bits per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failback</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will re-activate failed
uplinks higher in precedence when they come back up.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Faulttolerance<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Faulttolerance<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Faulttolerance<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the faultTolerance traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Faulttolerance<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The folder to create the DVS in. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hbr<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hbr<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hbr<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the hbr traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hbr<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchhost">[]Distributed<wbr>Virtual<wbr>Switch<wbr>Host</a></span>
    </dt>
    <dd>{{% md %}}Use the `host` block to declare a host specification. The
options are:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ingress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in
bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ingress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ingress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is
enabled on the port for ingress traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ingress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during
bursts in bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv4Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An IPv4 address to identify the switch. This is
mostly useful when used with the Netflow arguments found
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the iSCSI traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iscsi<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lacp<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Link Aggregation Control Protocol group
version to use with the switch. Possible values are `singleLag` and
`multipleLag`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lacp<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enables LACP for the ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lacp<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The LACP mode. Can be one of `active` or `passive`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Link<wbr>Discovery<wbr>Operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Whether to `advertise` or `listen`
for link discovery traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Link<wbr>Discovery<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The discovery protocol type. Valid
types are `cdp` and `lldp`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the management traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the management traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum transmission unit (MTU) for the virtual
switch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Multicast<wbr>Filtering<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The multicast filtering mode to use
with the switch. Can be one of `legacyFiltering` or `snooping`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the distributed virtual switch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Active<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
active flows are forced to be exported to the collector. Allowed range is
`60` to `3600`. Default: `60`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Collector<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}IP address for the Netflow
collector, using IPv4 or IPv6. IPv6 is supported in vSphere Distributed
Switch Version 6.0 or later. Must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Collector<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Port for the Netflow collector. This
must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enables Netflow on all ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Idle<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
idle flows are forced to be exported to the collector. Allowed range is `10`
to `600`. Default: `15`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Internal<wbr>Flows<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to limit analysis to
traffic that has both source and destination served by the same host.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Observation<wbr>Domain<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The observation domain ID for
the Netflow collector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Netflow<wbr>Sampling<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The ratio of total number of packets to
the number of packets analyzed. The default is `0`, which indicates that the
switch should analyze all packets. The maximum value is `1000`, which
indicates an analysis rate of 0.001%.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Resource<wbr>Control<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Set to `true` to enable
network I/O control. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Resource<wbr>Control<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The version of network I/O
control to use. Can be one of `version2` or `version3`. Default: `version2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the nfs traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nfs<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notify<wbr>Switches</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will notify the
broadcast network of an uplink failover, triggering cache updates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port<wbr>Private<wbr>Secondary<wbr>Vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Used to define a secondary VLAN
ID when using private VLANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Standby<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of standby uplinks to be used in
failover. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Teaming<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The uplink teaming policy. Can be one of
`loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tx<wbr>Uplink</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Forward all traffic transmitted by ports for which
this policy applies to its DVS uplinks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of strings that uniquely identifies the names
of the uplinks on the DVS across hosts. The number of items in this list
controls the number of uplinks that exist on the DVS, in addition to the
names.  See here for an example on how to
use this option.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vdp<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vdp<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vdp<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vdp traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vdp<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}- The version of the DVS to create. The default is to
create the DVS at the latest version supported by the version of vSphere
being used. A DVS can be upgraded to another version, but cannot be
downgraded.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtualmachine<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtualmachine<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtualmachine<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the virtualMachine traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtualmachine<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The VLAN ID for single VLAN mode. 0 denotes no VLAN.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vlan<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchvlanrange">[]Distributed<wbr>Virtual<wbr>Switch<wbr>Vlan<wbr>Range</a></span>
    </dt>
    <dd>{{% md %}}Used to denote VLAN trunking. Use the `min_vlan`
and `max_vlan` sub-arguments to define the tagged VLAN range. Multiple
`vlan_range` definitions are allowed, but they must not overlap. Example
below:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmotion<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmotion<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmotion<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vmotion traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vmotion<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsan<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsan<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsan<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vsan traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsan<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>active<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of active uplinks to be used in load
balancing. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Forged<wbr>Transmits</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Controls whether or not a virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Mac<wbr>Changes</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Controls whether or not the Media Access
Control (MAC) address can be changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Promiscuous</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>block<wbr>All<wbr>Ports</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Shuts down all ports in the port groups that
this policy applies to, effectively blocking all network access to connected
virtual devices.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>check<wbr>Beacon</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enables beacon probing as an additional measure
to detect NIC failure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>config<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version string of the configuration that this spec is trying to change.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>contact<wbr>Detail</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The detailed contact information for the person
who is responsible for the DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>contact<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the person who is responsible for the
DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual switch. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datacenter<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter where the distributed
virtual switch will be created. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A detailed description for the DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>directpath<wbr>Gen2Allowed</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Allow VMDirectPath Gen2 for the ports
for which this policy applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in bits
per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is enabled
on the port for egress traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during bursts
in bits per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failback</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will re-activate failed
uplinks higher in precedence when they come back up.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>faulttolerance<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>faulttolerance<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>faulttolerance<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the faultTolerance traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>faulttolerance<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The folder to create the DVS in. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hbr<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hbr<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hbr<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the hbr traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hbr<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchhost">Distributed<wbr>Virtual<wbr>Switch<wbr>Host[]?</a></span>
    </dt>
    <dd>{{% md %}}Use the `host` block to declare a host specification. The
options are:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ingress<wbr>Shaping<wbr>Average<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in
bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ingress<wbr>Shaping<wbr>Burst<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ingress<wbr>Shaping<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is
enabled on the port for ingress traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ingress<wbr>Shaping<wbr>Peak<wbr>Bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during
bursts in bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv4Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An IPv4 address to identify the switch. This is
mostly useful when used with the Netflow arguments found
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the iSCSI traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lacp<wbr>Api<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Link Aggregation Control Protocol group
version to use with the switch. Possible values are `singleLag` and
`multipleLag`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lacp<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enables LACP for the ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lacp<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The LACP mode. Can be one of `active` or `passive`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>link<wbr>Discovery<wbr>Operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Whether to `advertise` or `listen`
for link discovery traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>link<wbr>Discovery<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The discovery protocol type. Valid
types are `cdp` and `lldp`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the management traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the management traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum transmission unit (MTU) for the virtual
switch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>multicast<wbr>Filtering<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The multicast filtering mode to use
with the switch. Can be one of `legacyFiltering` or `snooping`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the distributed virtual switch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow<wbr>Active<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
active flows are forced to be exported to the collector. Allowed range is
`60` to `3600`. Default: `60`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow<wbr>Collector<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IP address for the Netflow
collector, using IPv4 or IPv6. IPv6 is supported in vSphere Distributed
Switch Version 6.0 or later. Must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow<wbr>Collector<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Port for the Netflow collector. This
must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enables Netflow on all ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow<wbr>Idle<wbr>Flow<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
idle flows are forced to be exported to the collector. Allowed range is `10`
to `600`. Default: `15`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow<wbr>Internal<wbr>Flows<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to limit analysis to
traffic that has both source and destination served by the same host.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow<wbr>Observation<wbr>Domain<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The observation domain ID for
the Netflow collector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow<wbr>Sampling<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The ratio of total number of packets to
the number of packets analyzed. The default is `0`, which indicates that the
switch should analyze all packets. The maximum value is `1000`, which
indicates an analysis rate of 0.001%.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Resource<wbr>Control<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Set to `true` to enable
network I/O control. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Resource<wbr>Control<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version of network I/O
control to use. Can be one of `version2` or `version3`. Default: `version2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the nfs traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notify<wbr>Switches</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will notify the
broadcast network of an uplink failover, triggering cache updates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port<wbr>Private<wbr>Secondary<wbr>Vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Used to define a secondary VLAN
ID when using private VLANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>standby<wbr>Uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of standby uplinks to be used in
failover. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>teaming<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The uplink teaming policy. Can be one of
`loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tx<wbr>Uplink</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Forward all traffic transmitted by ports for which
this policy applies to its DVS uplinks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of strings that uniquely identifies the names
of the uplinks on the DVS across hosts. The number of items in this list
controls the number of uplinks that exist on the DVS, in addition to the
names.  See here for an example on how to
use this option.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vdp<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vdp<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vdp<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vdp traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vdp<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}- The version of the DVS to create. The default is to
create the DVS at the latest version supported by the version of vSphere
being used. A DVS can be upgraded to another version, but cannot be
downgraded.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtualmachine<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtualmachine<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtualmachine<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the virtualMachine traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtualmachine<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The VLAN ID for single VLAN mode. 0 denotes no VLAN.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vlan<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchvlanrange">Distributed<wbr>Virtual<wbr>Switch<wbr>Vlan<wbr>Range[]?</a></span>
    </dt>
    <dd>{{% md %}}Used to denote VLAN trunking. Use the `min_vlan`
and `max_vlan` sub-arguments to define the tagged VLAN range. Multiple
`vlan_range` definitions are allowed, but they must not overlap. Example
below:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmotion<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmotion<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmotion<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vmotion traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmotion<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsan<wbr>Maximum<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsan<wbr>Reservation<wbr>Mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsan<wbr>Share<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vsan traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsan<wbr>Share<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>active_<wbr>uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of active uplinks to be used in load
balancing. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>forged_<wbr>transmits</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Controls whether or not a virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>mac_<wbr>changes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Controls whether or not the Media Access
Control (MAC) address can be changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow_<wbr>promiscuous</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>block_<wbr>all_<wbr>ports</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Shuts down all ports in the port groups that
this policy applies to, effectively blocking all network access to connected
virtual devices.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>check_<wbr>beacon</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enables beacon probing as an additional measure
to detect NIC failure.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>config_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The version string of the configuration that this spec is trying to change.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>contact_<wbr>detail</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The detailed contact information for the person
who is responsible for the DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>contact_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the person who is responsible for the
DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Map of custom attribute ids to attribute
value strings to set for virtual switch. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>datacenter_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the datacenter where the distributed
virtual switch will be created. Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A detailed description for the DVS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>directpath_<wbr>gen2_<wbr>allowed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Allow VMDirectPath Gen2 for the ports
for which this policy applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress_<wbr>shaping_<wbr>average_<wbr>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in bits
per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress_<wbr>shaping_<wbr>burst_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress_<wbr>shaping_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is enabled
on the port for egress traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>egress_<wbr>shaping_<wbr>peak_<wbr>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during bursts
in bits per second if egress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failback</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will re-activate failed
uplinks higher in precedence when they come back up.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>faulttolerance_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>faulttolerance_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>faulttolerance_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the faultTolerance traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>faulttolerance_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The folder to create the DVS in. Forces a new resource
if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hbr_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hbr_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hbr_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the hbr traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hbr_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hosts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchhost">List[Distributed<wbr>Virtual<wbr>Switch<wbr>Host]</a></span>
    </dt>
    <dd>{{% md %}}Use the `host` block to declare a host specification. The
options are:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ingress_<wbr>shaping_<wbr>average_<wbr>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The average bandwidth in
bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ingress_<wbr>shaping_<wbr>burst_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum burst size allowed in
bytes if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ingress_<wbr>shaping_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}`true` if the traffic shaper is
enabled on the port for ingress traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ingress_<wbr>shaping_<wbr>peak_<wbr>bandwidth</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The peak bandwidth during
bursts in bits per second if ingress traffic shaping is enabled on the port.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv4_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An IPv4 address to identify the switch. This is
mostly useful when used with the Netflow arguments found
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the iSCSI traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iscsi_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lacp_<wbr>api_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Link Aggregation Control Protocol group
version to use with the switch. Possible values are `singleLag` and
`multipleLag`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lacp_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enables LACP for the ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lacp_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The LACP mode. Can be one of `active` or `passive`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>link_<wbr>discovery_<wbr>operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Whether to `advertise` or `listen`
for link discovery traffic.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>link_<wbr>discovery_<wbr>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The discovery protocol type. Valid
types are `cdp` and `lldp`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the management traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the management traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum transmission unit (MTU) for the virtual
switch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>multicast_<wbr>filtering_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The multicast filtering mode to use
with the switch. Can be one of `legacyFiltering` or `snooping`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the distributed virtual switch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow_<wbr>active_<wbr>flow_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
active flows are forced to be exported to the collector. Allowed range is
`60` to `3600`. Default: `60`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow_<wbr>collector_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}IP address for the Netflow
collector, using IPv4 or IPv6. IPv6 is supported in vSphere Distributed
Switch Version 6.0 or later. Must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow_<wbr>collector_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Port for the Netflow collector. This
must be set before Netflow can be enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enables Netflow on all ports that this policy
applies to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow_<wbr>idle_<wbr>flow_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of seconds after which
idle flows are forced to be exported to the collector. Allowed range is `10`
to `600`. Default: `15`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow_<wbr>internal_<wbr>flows_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to limit analysis to
traffic that has both source and destination served by the same host.
Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow_<wbr>observation_<wbr>domain_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The observation domain ID for
the Netflow collector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>netflow_<wbr>sampling_<wbr>rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The ratio of total number of packets to
the number of packets analyzed. The default is `0`, which indicates that the
switch should analyze all packets. The maximum value is `1000`, which
indicates an analysis rate of 0.001%.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>resource_<wbr>control_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to `true` to enable
network I/O control. Default: `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>resource_<wbr>control_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The version of network I/O
control to use. Can be one of `version2` or `version3`. Default: `version2`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the nfs traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nfs_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notify_<wbr>switches</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, the teaming policy will notify the
broadcast network of an uplink failover, triggering cache updates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port_<wbr>private_<wbr>secondary_<wbr>vlan_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Used to define a secondary VLAN
ID when using private VLANs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>standby_<wbr>uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of standby uplinks to be used in
failover. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>teaming_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The uplink teaming policy. Can be one of
`loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tx_<wbr>uplink</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Forward all traffic transmitted by ports for which
this policy applies to its DVS uplinks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uplinks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of strings that uniquely identifies the names
of the uplinks on the DVS across hosts. The number of items in this list
controls the number of uplinks that exist on the DVS, in addition to the
names.  See here for an example on how to
use this option.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vdp_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vdp_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vdp_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vdp traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vdp_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}- The version of the DVS to create. The default is to
create the DVS at the latest version supported by the version of vSphere
being used. A DVS can be upgraded to another version, but cannot be
downgraded.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtualmachine_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtualmachine_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtualmachine_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the virtualMachine traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtualmachine_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vlan_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The VLAN ID for single VLAN mode. 0 denotes no VLAN.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vlan_<wbr>ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#distributedvirtualswitchvlanrange">List[Distributed<wbr>Virtual<wbr>Switch<wbr>Vlan<wbr>Range]</a></span>
    </dt>
    <dd>{{% md %}}Used to denote VLAN trunking. Use the `min_vlan`
and `max_vlan` sub-arguments to define the tagged VLAN range. Multiple
`vlan_range` definitions are allowed, but they must not overlap. Example
below:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmotion_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmotion_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmotion_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vmotion traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vmotion_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsan_<wbr>maximum_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum allowed usage for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsan_<wbr>reservation_<wbr>mbit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsan_<wbr>share_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of shares to allocate to the vsan traffic class for a custom share level.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsan_<wbr>share_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Distributed<wbr>Virtual<wbr>Switch<wbr>Host</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/input/#DistributedVirtualSwitchHost">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/output/#DistributedVirtualSwitchHost">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/go/vsphere/?tab=doc#DistributedVirtualSwitchHostArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/go/vsphere/?tab=doc#DistributedVirtualSwitchHostOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The list of NIC devices to map to uplinks on the DVS,
added in order they are specified.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>System<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The host system ID of the host to add to the
DVS.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of NIC devices to map to uplinks on the DVS,
added in order they are specified.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>System<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The host system ID of the host to add to the
DVS.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>devices</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The list of NIC devices to map to uplinks on the DVS,
added in order they are specified.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host<wbr>System<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The host system ID of the host to add to the
DVS.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>devices</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of NIC devices to map to uplinks on the DVS,
added in order they are specified.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host_<wbr>system_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The host system ID of the host to add to the
DVS.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Distributed<wbr>Virtual<wbr>Switch<wbr>Vlan<wbr>Range</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/input/#DistributedVirtualSwitchVlanRange">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/vsphere/types/output/#DistributedVirtualSwitchVlanRange">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/go/vsphere/?tab=doc#DistributedVirtualSwitchVlanRangeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/go/vsphere/?tab=doc#DistributedVirtualSwitchVlanRangeOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Vlan</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Min<wbr>Vlan</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Vlan</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Min<wbr>Vlan</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Vlan</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>min<wbr>Vlan</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Vlan</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>min<wbr>Vlan</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
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
    
</dl>

