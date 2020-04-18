
---
title: "HaVmOverride"
block_external_search_index: true
---



The `vsphere..HaVmOverride` resource can be used to add an override for
vSphere HA settings on a cluster for a specific virtual machine. With this
resource, one can control specific HA settings so that they are different than
the cluster default, accommodating the needs of that specific virtual machine,
while not affecting the rest of the cluster.

For more information on vSphere HA, see [this page][ref-vsphere-ha-clusters].

[ref-vsphere-ha-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.avail.doc/GUID-5432CA24-14F1-44E3-87FB-61D937831CF6.html

> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

{{% examples %}}
## Example Usage
{{% example %}}

The example below creates a virtual machine in a cluster using the
[`vsphere..VirtualMachine`][tf-vsphere-vm-resource] resource, creating the
virtual machine in the cluster looked up by the
[`vsphere..ComputeCluster`][tf-vsphere-cluster-data-source] data source.

Considering a scenario where this virtual machine is of high value to the
application or organization for which it does its work, it's been determined in
the event of a host failure, that this should be one of the first virtual
machines to be started by vSphere HA during recovery. Hence, its
`ha_vm_restart_priority` as been set to `highest`,
which, assuming that the default restart priority is `medium` and no other
virtual machine has been assigned the `highest` priority, will mean that this
VM will be started before any other virtual machine in the event of host
failure.

[tf-vsphere-vm-resource]: /docs/providers/vsphere/r/virtual_machine.html
[tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as vsphere from "@pulumi/vsphere";

const dc = vsphere.getDatacenter({
    name: "dc1",
});
const datastore = vsphere.getDatastore({
    datacenterId: dc.id,
    name: "datastore1",
});
const cluster = vsphere.getComputeCluster({
    datacenterId: dc.id,
    name: "cluster1",
});
const network = vsphere.getNetwork({
    datacenterId: dc.id,
    name: "network1",
});
const vm = new vsphere.VirtualMachine("vm", {
    datastoreId: datastore.id,
    disks: [{
        label: "disk0",
        size: 20,
    }],
    guestId: "other3xLinux64Guest",
    memory: 2048,
    networkInterfaces: [{
        networkId: network.id,
    }],
    numCpus: 2,
    resourcePoolId: cluster.resourcePoolId,
});
const haVmOverride = new vsphere.HaVmOverride("ha_vm_override", {
    computeClusterId: cluster.id,
    haVmRestartPriority: "highest",
    virtualMachineId: vm.id,
});
```

{{% /example %}}
{{% /examples %}}



## Create a HaVmOverride Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#HaVmOverride">HaVmOverride</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#HaVmOverrideArgs">HaVmOverrideArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">HaVmOverride</span><span class="p">(resource_name, opts=None, </span>compute_cluster_id=None<span class="p">, </span>ha_datastore_apd_recovery_action=None<span class="p">, </span>ha_datastore_apd_response=None<span class="p">, </span>ha_datastore_apd_response_delay=None<span class="p">, </span>ha_datastore_pdl_response=None<span class="p">, </span>ha_host_isolation_response=None<span class="p">, </span>ha_vm_failure_interval=None<span class="p">, </span>ha_vm_maximum_failure_window=None<span class="p">, </span>ha_vm_maximum_resets=None<span class="p">, </span>ha_vm_minimum_uptime=None<span class="p">, </span>ha_vm_monitoring=None<span class="p">, </span>ha_vm_monitoring_use_cluster_defaults=None<span class="p">, </span>ha_vm_restart_priority=None<span class="p">, </span>ha_vm_restart_timeout=None<span class="p">, </span>virtual_machine_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewHaVmOverride<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#HaVmOverrideArgs">HaVmOverrideArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#HaVmOverride">HaVmOverride</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere.HaVmOverride.html">HaVmOverride</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.VSphere.HaVmOverrideArgs.html">HaVmOverrideArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Compute<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Datastore<wbr>Apd<wbr>Recovery<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take
on this virtual machine if an APD status on an affected datastore clears in
the middle of an APD event. Can be one of `useClusterDefault`, `none` or
`reset`.  Default: `useClusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Datastore<wbr>Apd<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take on this
virtual machine when the cluster has detected loss to all paths to a relevant
datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
`restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Datastore<wbr>Apd<wbr>Response<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Controls the delay in minutes
to wait after an APD timeout event to execute the response action defined in
`ha_datastore_apd_response`. Use `-1` to use
the cluster default. Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Datastore<wbr>Pdl<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take on this
virtual machine when the cluster has detected a permanent device loss to a
relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
`restartAggressive`. Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Host<wbr>Isolation<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The action to take on this virtual
machine when a host has detected that it has been isolated from the rest of
the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
`shutdown`. Default: `clusterIsolationResponse`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Failure<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}If a heartbeat from this virtual
machine is not received within this configured interval, the virtual machine
is marked as failed. The value is in seconds. Default: `30`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Maximum<wbr>Failure<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The length of the reset window in
which `ha_vm_maximum_resets` can operate. When this
window expires, no more resets are attempted regardless of the setting
configured in `ha_vm_maximum_resets`. `-1` means no window, meaning an
unlimited reset time is allotted. The value is specified in seconds. Default:
`-1` (no window).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Maximum<wbr>Resets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum number of resets that HA will
perform to this virtual machine when responding to a failure event. Default:
`3`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Minimum<wbr>Uptime</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The time, in seconds, that HA waits after
powering on this virtual machine before monitoring for heartbeats. Default:
`120` (2 minutes).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of virtual machine monitoring to use
when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
`vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Monitoring<wbr>Use<wbr>Cluster<wbr>Defaults</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether or
not the cluster's default settings or the VM override settings specified in
this resource are used for virtual machine monitoring. The default is `true`
(use cluster defaults) - set to `false` to have overrides take effect.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Restart<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The restart priority for the virtual
machine when vSphere detects a host failure. Can be one of
`clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
Default: `clusterRestartPriority`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Restart<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum time, in seconds, that
vSphere HA will wait for this virtual machine to be ready. Use `-1` to
specify the cluster default.  Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Compute<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Datastore<wbr>Apd<wbr>Recovery<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take
on this virtual machine if an APD status on an affected datastore clears in
the middle of an APD event. Can be one of `useClusterDefault`, `none` or
`reset`.  Default: `useClusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Datastore<wbr>Apd<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take on this
virtual machine when the cluster has detected loss to all paths to a relevant
datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
`restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Datastore<wbr>Apd<wbr>Response<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Controls the delay in minutes
to wait after an APD timeout event to execute the response action defined in
`ha_datastore_apd_response`. Use `-1` to use
the cluster default. Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Datastore<wbr>Pdl<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take on this
virtual machine when the cluster has detected a permanent device loss to a
relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
`restartAggressive`. Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Host<wbr>Isolation<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The action to take on this virtual
machine when a host has detected that it has been isolated from the rest of
the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
`shutdown`. Default: `clusterIsolationResponse`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Failure<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}If a heartbeat from this virtual
machine is not received within this configured interval, the virtual machine
is marked as failed. The value is in seconds. Default: `30`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Maximum<wbr>Failure<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The length of the reset window in
which `ha_vm_maximum_resets` can operate. When this
window expires, no more resets are attempted regardless of the setting
configured in `ha_vm_maximum_resets`. `-1` means no window, meaning an
unlimited reset time is allotted. The value is specified in seconds. Default:
`-1` (no window).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Maximum<wbr>Resets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum number of resets that HA will
perform to this virtual machine when responding to a failure event. Default:
`3`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Minimum<wbr>Uptime</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The time, in seconds, that HA waits after
powering on this virtual machine before monitoring for heartbeats. Default:
`120` (2 minutes).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of virtual machine monitoring to use
when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
`vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Monitoring<wbr>Use<wbr>Cluster<wbr>Defaults</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether or
not the cluster's default settings or the VM override settings specified in
this resource are used for virtual machine monitoring. The default is `true`
(use cluster defaults) - set to `false` to have overrides take effect.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Restart<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The restart priority for the virtual
machine when vSphere detects a host failure. Can be one of
`clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
Default: `clusterRestartPriority`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Restart<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum time, in seconds, that
vSphere HA will wait for this virtual machine to be ready. Use `-1` to
specify the cluster default.  Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>compute<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Datastore<wbr>Apd<wbr>Recovery<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take
on this virtual machine if an APD status on an affected datastore clears in
the middle of an APD event. Can be one of `useClusterDefault`, `none` or
`reset`.  Default: `useClusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Datastore<wbr>Apd<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take on this
virtual machine when the cluster has detected loss to all paths to a relevant
datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
`restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Datastore<wbr>Apd<wbr>Response<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Controls the delay in minutes
to wait after an APD timeout event to execute the response action defined in
`ha_datastore_apd_response`. Use `-1` to use
the cluster default. Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Datastore<wbr>Pdl<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take on this
virtual machine when the cluster has detected a permanent device loss to a
relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
`restartAggressive`. Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Host<wbr>Isolation<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The action to take on this virtual
machine when a host has detected that it has been isolated from the rest of
the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
`shutdown`. Default: `clusterIsolationResponse`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Vm<wbr>Failure<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}If a heartbeat from this virtual
machine is not received within this configured interval, the virtual machine
is marked as failed. The value is in seconds. Default: `30`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Vm<wbr>Maximum<wbr>Failure<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The length of the reset window in
which `ha_vm_maximum_resets` can operate. When this
window expires, no more resets are attempted regardless of the setting
configured in `ha_vm_maximum_resets`. `-1` means no window, meaning an
unlimited reset time is allotted. The value is specified in seconds. Default:
`-1` (no window).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Vm<wbr>Maximum<wbr>Resets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The maximum number of resets that HA will
perform to this virtual machine when responding to a failure event. Default:
`3`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Vm<wbr>Minimum<wbr>Uptime</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The time, in seconds, that HA waits after
powering on this virtual machine before monitoring for heartbeats. Default:
`120` (2 minutes).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Vm<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of virtual machine monitoring to use
when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
`vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Vm<wbr>Monitoring<wbr>Use<wbr>Cluster<wbr>Defaults</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Determines whether or
not the cluster's default settings or the VM override settings specified in
this resource are used for virtual machine monitoring. The default is `true`
(use cluster defaults) - set to `false` to have overrides take effect.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Vm<wbr>Restart<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The restart priority for the virtual
machine when vSphere detects a host failure. Can be one of
`clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
Default: `clusterRestartPriority`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Vm<wbr>Restart<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The maximum time, in seconds, that
vSphere HA will wait for this virtual machine to be ready. Use `-1` to
specify the cluster default.  Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>compute_<wbr>cluster_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>virtual_<wbr>machine_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>datastore_<wbr>apd_<wbr>recovery_<wbr>action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take
on this virtual machine if an APD status on an affected datastore clears in
the middle of an APD event. Can be one of `useClusterDefault`, `none` or
`reset`.  Default: `useClusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>datastore_<wbr>apd_<wbr>response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take on this
virtual machine when the cluster has detected loss to all paths to a relevant
datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
`restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>datastore_<wbr>apd_<wbr>response_<wbr>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Controls the delay in minutes
to wait after an APD timeout event to execute the response action defined in
`ha_datastore_apd_response`. Use `-1` to use
the cluster default. Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>datastore_<wbr>pdl_<wbr>response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take on this
virtual machine when the cluster has detected a permanent device loss to a
relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
`restartAggressive`. Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>host_<wbr>isolation_<wbr>response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The action to take on this virtual
machine when a host has detected that it has been isolated from the rest of
the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
`shutdown`. Default: `clusterIsolationResponse`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>vm_<wbr>failure_<wbr>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}If a heartbeat from this virtual
machine is not received within this configured interval, the virtual machine
is marked as failed. The value is in seconds. Default: `30`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>vm_<wbr>maximum_<wbr>failure_<wbr>window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The length of the reset window in
which `ha_vm_maximum_resets` can operate. When this
window expires, no more resets are attempted regardless of the setting
configured in `ha_vm_maximum_resets`. `-1` means no window, meaning an
unlimited reset time is allotted. The value is specified in seconds. Default:
`-1` (no window).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>vm_<wbr>maximum_<wbr>resets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The maximum number of resets that HA will
perform to this virtual machine when responding to a failure event. Default:
`3`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>vm_<wbr>minimum_<wbr>uptime</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The time, in seconds, that HA waits after
powering on this virtual machine before monitoring for heartbeats. Default:
`120` (2 minutes).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>vm_<wbr>monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of virtual machine monitoring to use
when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
`vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>vm_<wbr>monitoring_<wbr>use_<wbr>cluster_<wbr>defaults</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether or
not the cluster's default settings or the VM override settings specified in
this resource are used for virtual machine monitoring. The default is `true`
(use cluster defaults) - set to `false` to have overrides take effect.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>vm_<wbr>restart_<wbr>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The restart priority for the virtual
machine when vSphere detects a host failure. Can be one of
`clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
Default: `clusterRestartPriority`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>vm_<wbr>restart_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The maximum time, in seconds, that
vSphere HA will wait for this virtual machine to be ready. Use `-1` to
specify the cluster default.  Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Look up an Existing HaVmOverride Resource

Get an existing HaVmOverride resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#HaVmOverrideState">HaVmOverrideState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/vsphere/#HaVmOverride">HaVmOverride</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>compute_cluster_id=None<span class="p">, </span>ha_datastore_apd_recovery_action=None<span class="p">, </span>ha_datastore_apd_response=None<span class="p">, </span>ha_datastore_apd_response_delay=None<span class="p">, </span>ha_datastore_pdl_response=None<span class="p">, </span>ha_host_isolation_response=None<span class="p">, </span>ha_vm_failure_interval=None<span class="p">, </span>ha_vm_maximum_failure_window=None<span class="p">, </span>ha_vm_maximum_resets=None<span class="p">, </span>ha_vm_minimum_uptime=None<span class="p">, </span>ha_vm_monitoring=None<span class="p">, </span>ha_vm_monitoring_use_cluster_defaults=None<span class="p">, </span>ha_vm_restart_priority=None<span class="p">, </span>ha_vm_restart_timeout=None<span class="p">, </span>virtual_machine_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetHaVmOverride<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#HaVmOverrideState">HaVmOverrideState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere/?tab=doc#HaVmOverride">HaVmOverride</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere.HaVmOverride.html">HaVmOverride</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Vsphere/Pulumi.Vsphere..HaVmOverrideState.html">HaVmOverrideState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Compute<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Datastore<wbr>Apd<wbr>Recovery<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take
on this virtual machine if an APD status on an affected datastore clears in
the middle of an APD event. Can be one of `useClusterDefault`, `none` or
`reset`.  Default: `useClusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Datastore<wbr>Apd<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take on this
virtual machine when the cluster has detected loss to all paths to a relevant
datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
`restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Datastore<wbr>Apd<wbr>Response<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Controls the delay in minutes
to wait after an APD timeout event to execute the response action defined in
`ha_datastore_apd_response`. Use `-1` to use
the cluster default. Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Datastore<wbr>Pdl<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take on this
virtual machine when the cluster has detected a permanent device loss to a
relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
`restartAggressive`. Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Host<wbr>Isolation<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The action to take on this virtual
machine when a host has detected that it has been isolated from the rest of
the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
`shutdown`. Default: `clusterIsolationResponse`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Failure<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}If a heartbeat from this virtual
machine is not received within this configured interval, the virtual machine
is marked as failed. The value is in seconds. Default: `30`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Maximum<wbr>Failure<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The length of the reset window in
which `ha_vm_maximum_resets` can operate. When this
window expires, no more resets are attempted regardless of the setting
configured in `ha_vm_maximum_resets`. `-1` means no window, meaning an
unlimited reset time is allotted. The value is specified in seconds. Default:
`-1` (no window).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Maximum<wbr>Resets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum number of resets that HA will
perform to this virtual machine when responding to a failure event. Default:
`3`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Minimum<wbr>Uptime</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The time, in seconds, that HA waits after
powering on this virtual machine before monitoring for heartbeats. Default:
`120` (2 minutes).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of virtual machine monitoring to use
when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
`vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Monitoring<wbr>Use<wbr>Cluster<wbr>Defaults</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether or
not the cluster's default settings or the VM override settings specified in
this resource are used for virtual machine monitoring. The default is `true`
(use cluster defaults) - set to `false` to have overrides take effect.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Restart<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The restart priority for the virtual
machine when vSphere detects a host failure. Can be one of
`clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
Default: `clusterRestartPriority`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Restart<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum time, in seconds, that
vSphere HA will wait for this virtual machine to be ready. Use `-1` to
specify the cluster default.  Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Compute<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Datastore<wbr>Apd<wbr>Recovery<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take
on this virtual machine if an APD status on an affected datastore clears in
the middle of an APD event. Can be one of `useClusterDefault`, `none` or
`reset`.  Default: `useClusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Datastore<wbr>Apd<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take on this
virtual machine when the cluster has detected loss to all paths to a relevant
datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
`restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Datastore<wbr>Apd<wbr>Response<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Controls the delay in minutes
to wait after an APD timeout event to execute the response action defined in
`ha_datastore_apd_response`. Use `-1` to use
the cluster default. Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Datastore<wbr>Pdl<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take on this
virtual machine when the cluster has detected a permanent device loss to a
relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
`restartAggressive`. Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Host<wbr>Isolation<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The action to take on this virtual
machine when a host has detected that it has been isolated from the rest of
the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
`shutdown`. Default: `clusterIsolationResponse`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Failure<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}If a heartbeat from this virtual
machine is not received within this configured interval, the virtual machine
is marked as failed. The value is in seconds. Default: `30`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Maximum<wbr>Failure<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The length of the reset window in
which `ha_vm_maximum_resets` can operate. When this
window expires, no more resets are attempted regardless of the setting
configured in `ha_vm_maximum_resets`. `-1` means no window, meaning an
unlimited reset time is allotted. The value is specified in seconds. Default:
`-1` (no window).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Maximum<wbr>Resets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum number of resets that HA will
perform to this virtual machine when responding to a failure event. Default:
`3`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Minimum<wbr>Uptime</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The time, in seconds, that HA waits after
powering on this virtual machine before monitoring for heartbeats. Default:
`120` (2 minutes).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of virtual machine monitoring to use
when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
`vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Monitoring<wbr>Use<wbr>Cluster<wbr>Defaults</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether or
not the cluster's default settings or the VM override settings specified in
this resource are used for virtual machine monitoring. The default is `true`
(use cluster defaults) - set to `false` to have overrides take effect.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Restart<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The restart priority for the virtual
machine when vSphere detects a host failure. Can be one of
`clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
Default: `clusterRestartPriority`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ha<wbr>Vm<wbr>Restart<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum time, in seconds, that
vSphere HA will wait for this virtual machine to be ready. Use `-1` to
specify the cluster default.  Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>compute<wbr>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Datastore<wbr>Apd<wbr>Recovery<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take
on this virtual machine if an APD status on an affected datastore clears in
the middle of an APD event. Can be one of `useClusterDefault`, `none` or
`reset`.  Default: `useClusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Datastore<wbr>Apd<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take on this
virtual machine when the cluster has detected loss to all paths to a relevant
datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
`restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Datastore<wbr>Apd<wbr>Response<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Controls the delay in minutes
to wait after an APD timeout event to execute the response action defined in
`ha_datastore_apd_response`. Use `-1` to use
the cluster default. Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Datastore<wbr>Pdl<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take on this
virtual machine when the cluster has detected a permanent device loss to a
relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
`restartAggressive`. Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Host<wbr>Isolation<wbr>Response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The action to take on this virtual
machine when a host has detected that it has been isolated from the rest of
the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
`shutdown`. Default: `clusterIsolationResponse`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Vm<wbr>Failure<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}If a heartbeat from this virtual
machine is not received within this configured interval, the virtual machine
is marked as failed. The value is in seconds. Default: `30`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Vm<wbr>Maximum<wbr>Failure<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The length of the reset window in
which `ha_vm_maximum_resets` can operate. When this
window expires, no more resets are attempted regardless of the setting
configured in `ha_vm_maximum_resets`. `-1` means no window, meaning an
unlimited reset time is allotted. The value is specified in seconds. Default:
`-1` (no window).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Vm<wbr>Maximum<wbr>Resets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The maximum number of resets that HA will
perform to this virtual machine when responding to a failure event. Default:
`3`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Vm<wbr>Minimum<wbr>Uptime</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The time, in seconds, that HA waits after
powering on this virtual machine before monitoring for heartbeats. Default:
`120` (2 minutes).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Vm<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of virtual machine monitoring to use
when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
`vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Vm<wbr>Monitoring<wbr>Use<wbr>Cluster<wbr>Defaults</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Determines whether or
not the cluster's default settings or the VM override settings specified in
this resource are used for virtual machine monitoring. The default is `true`
(use cluster defaults) - set to `false` to have overrides take effect.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Vm<wbr>Restart<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The restart priority for the virtual
machine when vSphere detects a host failure. Can be one of
`clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
Default: `clusterRestartPriority`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha<wbr>Vm<wbr>Restart<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The maximum time, in seconds, that
vSphere HA will wait for this virtual machine to be ready. Use `-1` to
specify the cluster default.  Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtual<wbr>Machine<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>compute_<wbr>cluster_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>datastore_<wbr>apd_<wbr>recovery_<wbr>action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take
on this virtual machine if an APD status on an affected datastore clears in
the middle of an APD event. Can be one of `useClusterDefault`, `none` or
`reset`.  Default: `useClusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>datastore_<wbr>apd_<wbr>response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take on this
virtual machine when the cluster has detected loss to all paths to a relevant
datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
`restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>datastore_<wbr>apd_<wbr>response_<wbr>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Controls the delay in minutes
to wait after an APD timeout event to execute the response action defined in
`ha_datastore_apd_response`. Use `-1` to use
the cluster default. Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>datastore_<wbr>pdl_<wbr>response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Controls the action to take on this
virtual machine when the cluster has detected a permanent device loss to a
relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
`restartAggressive`. Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>host_<wbr>isolation_<wbr>response</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The action to take on this virtual
machine when a host has detected that it has been isolated from the rest of
the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
`shutdown`. Default: `clusterIsolationResponse`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>vm_<wbr>failure_<wbr>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}If a heartbeat from this virtual
machine is not received within this configured interval, the virtual machine
is marked as failed. The value is in seconds. Default: `30`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>vm_<wbr>maximum_<wbr>failure_<wbr>window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The length of the reset window in
which `ha_vm_maximum_resets` can operate. When this
window expires, no more resets are attempted regardless of the setting
configured in `ha_vm_maximum_resets`. `-1` means no window, meaning an
unlimited reset time is allotted. The value is specified in seconds. Default:
`-1` (no window).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>vm_<wbr>maximum_<wbr>resets</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The maximum number of resets that HA will
perform to this virtual machine when responding to a failure event. Default:
`3`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>vm_<wbr>minimum_<wbr>uptime</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The time, in seconds, that HA waits after
powering on this virtual machine before monitoring for heartbeats. Default:
`120` (2 minutes).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>vm_<wbr>monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of virtual machine monitoring to use
when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
`vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>vm_<wbr>monitoring_<wbr>use_<wbr>cluster_<wbr>defaults</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Determines whether or
not the cluster's default settings or the VM override settings specified in
this resource are used for virtual machine monitoring. The default is `true`
(use cluster defaults) - set to `false` to have overrides take effect.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>vm_<wbr>restart_<wbr>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The restart priority for the virtual
machine when vSphere detects a host failure. Can be one of
`clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
Default: `clusterRestartPriority`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ha_<wbr>vm_<wbr>restart_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The maximum time, in seconds, that
vSphere HA will wait for this virtual machine to be ready. Use `-1` to
specify the cluster default.  Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtual_<wbr>machine_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.
{{% /md %}}</dd>

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

