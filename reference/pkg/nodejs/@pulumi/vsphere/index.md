---
title: Package @pulumi/vsphere
---


Node.js:

```javascript
var vsphere = require("@pulumi/vsphere");
```

ES6 modules:

```typescript
import * as vsphere from "@pulumi/vsphere";
```

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ComputeCluster">class ComputeCluster</a>
* <a href="#ComputeClusterHostGroup">class ComputeClusterHostGroup</a>
* <a href="#ComputeClusterVmAffinityRule">class ComputeClusterVmAffinityRule</a>
* <a href="#ComputeClusterVmAntiAffinityRule">class ComputeClusterVmAntiAffinityRule</a>
* <a href="#ComputeClusterVmDependencyRule">class ComputeClusterVmDependencyRule</a>
* <a href="#ComputeClusterVmGroup">class ComputeClusterVmGroup</a>
* <a href="#ComputeClusterVmHostRule">class ComputeClusterVmHostRule</a>
* <a href="#CustomAttribute">class CustomAttribute</a>
* <a href="#Datacenter">class Datacenter</a>
* <a href="#DatastoreCluster">class DatastoreCluster</a>
* <a href="#DatastoreClusterVmAntiAffinityRule">class DatastoreClusterVmAntiAffinityRule</a>
* <a href="#DistributedPortGroup">class DistributedPortGroup</a>
* <a href="#DistributedVirtualSwitch">class DistributedVirtualSwitch</a>
* <a href="#DpmHostOverride">class DpmHostOverride</a>
* <a href="#DrsVmOverride">class DrsVmOverride</a>
* <a href="#File">class File</a>
* <a href="#Folder">class Folder</a>
* <a href="#HaVmOverride">class HaVmOverride</a>
* <a href="#HostPortGroup">class HostPortGroup</a>
* <a href="#HostVirtualSwitch">class HostVirtualSwitch</a>
* <a href="#License">class License</a>
* <a href="#NasDatastore">class NasDatastore</a>
* <a href="#Provider">class Provider</a>
* <a href="#ResourcePool">class ResourcePool</a>
* <a href="#StorageDrsVmOverride">class StorageDrsVmOverride</a>
* <a href="#Tag">class Tag</a>
* <a href="#TagCategory">class TagCategory</a>
* <a href="#VappContainer">class VappContainer</a>
* <a href="#VirtualDisk">class VirtualDisk</a>
* <a href="#VirtualMachine">class VirtualMachine</a>
* <a href="#VirtualMachineSnapshot">class VirtualMachineSnapshot</a>
* <a href="#VmfsDatastore">class VmfsDatastore</a>
* <a href="#getComputeCluster">function getComputeCluster</a>
* <a href="#getCustomAttribute">function getCustomAttribute</a>
* <a href="#getDatacenter">function getDatacenter</a>
* <a href="#getDatastore">function getDatastore</a>
* <a href="#getDatastoreCluster">function getDatastoreCluster</a>
* <a href="#getDistributedVirtualSwitch">function getDistributedVirtualSwitch</a>
* <a href="#getHost">function getHost</a>
* <a href="#getNetwork">function getNetwork</a>
* <a href="#getResourcePool">function getResourcePool</a>
* <a href="#getTag">function getTag</a>
* <a href="#getTagCategory">function getTagCategory</a>
* <a href="#getVirtualMachine">function getVirtualMachine</a>
* <a href="#getVmfsDisks">function getVmfsDisks</a>
* <a href="#ComputeClusterArgs">interface ComputeClusterArgs</a>
* <a href="#ComputeClusterHostGroupArgs">interface ComputeClusterHostGroupArgs</a>
* <a href="#ComputeClusterHostGroupState">interface ComputeClusterHostGroupState</a>
* <a href="#ComputeClusterState">interface ComputeClusterState</a>
* <a href="#ComputeClusterVmAffinityRuleArgs">interface ComputeClusterVmAffinityRuleArgs</a>
* <a href="#ComputeClusterVmAffinityRuleState">interface ComputeClusterVmAffinityRuleState</a>
* <a href="#ComputeClusterVmAntiAffinityRuleArgs">interface ComputeClusterVmAntiAffinityRuleArgs</a>
* <a href="#ComputeClusterVmAntiAffinityRuleState">interface ComputeClusterVmAntiAffinityRuleState</a>
* <a href="#ComputeClusterVmDependencyRuleArgs">interface ComputeClusterVmDependencyRuleArgs</a>
* <a href="#ComputeClusterVmDependencyRuleState">interface ComputeClusterVmDependencyRuleState</a>
* <a href="#ComputeClusterVmGroupArgs">interface ComputeClusterVmGroupArgs</a>
* <a href="#ComputeClusterVmGroupState">interface ComputeClusterVmGroupState</a>
* <a href="#ComputeClusterVmHostRuleArgs">interface ComputeClusterVmHostRuleArgs</a>
* <a href="#ComputeClusterVmHostRuleState">interface ComputeClusterVmHostRuleState</a>
* <a href="#CustomAttributeArgs">interface CustomAttributeArgs</a>
* <a href="#CustomAttributeState">interface CustomAttributeState</a>
* <a href="#DatacenterArgs">interface DatacenterArgs</a>
* <a href="#DatacenterState">interface DatacenterState</a>
* <a href="#DatastoreClusterArgs">interface DatastoreClusterArgs</a>
* <a href="#DatastoreClusterState">interface DatastoreClusterState</a>
* <a href="#DatastoreClusterVmAntiAffinityRuleArgs">interface DatastoreClusterVmAntiAffinityRuleArgs</a>
* <a href="#DatastoreClusterVmAntiAffinityRuleState">interface DatastoreClusterVmAntiAffinityRuleState</a>
* <a href="#DistributedPortGroupArgs">interface DistributedPortGroupArgs</a>
* <a href="#DistributedPortGroupState">interface DistributedPortGroupState</a>
* <a href="#DistributedVirtualSwitchArgs">interface DistributedVirtualSwitchArgs</a>
* <a href="#DistributedVirtualSwitchState">interface DistributedVirtualSwitchState</a>
* <a href="#DpmHostOverrideArgs">interface DpmHostOverrideArgs</a>
* <a href="#DpmHostOverrideState">interface DpmHostOverrideState</a>
* <a href="#DrsVmOverrideArgs">interface DrsVmOverrideArgs</a>
* <a href="#DrsVmOverrideState">interface DrsVmOverrideState</a>
* <a href="#FileArgs">interface FileArgs</a>
* <a href="#FileState">interface FileState</a>
* <a href="#FolderArgs">interface FolderArgs</a>
* <a href="#FolderState">interface FolderState</a>
* <a href="#GetComputeClusterArgs">interface GetComputeClusterArgs</a>
* <a href="#GetComputeClusterResult">interface GetComputeClusterResult</a>
* <a href="#GetCustomAttributeArgs">interface GetCustomAttributeArgs</a>
* <a href="#GetCustomAttributeResult">interface GetCustomAttributeResult</a>
* <a href="#GetDatacenterArgs">interface GetDatacenterArgs</a>
* <a href="#GetDatacenterResult">interface GetDatacenterResult</a>
* <a href="#GetDatastoreArgs">interface GetDatastoreArgs</a>
* <a href="#GetDatastoreClusterArgs">interface GetDatastoreClusterArgs</a>
* <a href="#GetDatastoreClusterResult">interface GetDatastoreClusterResult</a>
* <a href="#GetDatastoreResult">interface GetDatastoreResult</a>
* <a href="#GetDistributedVirtualSwitchArgs">interface GetDistributedVirtualSwitchArgs</a>
* <a href="#GetDistributedVirtualSwitchResult">interface GetDistributedVirtualSwitchResult</a>
* <a href="#GetHostArgs">interface GetHostArgs</a>
* <a href="#GetHostResult">interface GetHostResult</a>
* <a href="#GetNetworkArgs">interface GetNetworkArgs</a>
* <a href="#GetNetworkResult">interface GetNetworkResult</a>
* <a href="#GetResourcePoolArgs">interface GetResourcePoolArgs</a>
* <a href="#GetResourcePoolResult">interface GetResourcePoolResult</a>
* <a href="#GetTagArgs">interface GetTagArgs</a>
* <a href="#GetTagCategoryArgs">interface GetTagCategoryArgs</a>
* <a href="#GetTagCategoryResult">interface GetTagCategoryResult</a>
* <a href="#GetTagResult">interface GetTagResult</a>
* <a href="#GetVirtualMachineArgs">interface GetVirtualMachineArgs</a>
* <a href="#GetVirtualMachineResult">interface GetVirtualMachineResult</a>
* <a href="#GetVmfsDisksArgs">interface GetVmfsDisksArgs</a>
* <a href="#GetVmfsDisksResult">interface GetVmfsDisksResult</a>
* <a href="#HaVmOverrideArgs">interface HaVmOverrideArgs</a>
* <a href="#HaVmOverrideState">interface HaVmOverrideState</a>
* <a href="#HostPortGroupArgs">interface HostPortGroupArgs</a>
* <a href="#HostPortGroupState">interface HostPortGroupState</a>
* <a href="#HostVirtualSwitchArgs">interface HostVirtualSwitchArgs</a>
* <a href="#HostVirtualSwitchState">interface HostVirtualSwitchState</a>
* <a href="#LicenseArgs">interface LicenseArgs</a>
* <a href="#LicenseState">interface LicenseState</a>
* <a href="#NasDatastoreArgs">interface NasDatastoreArgs</a>
* <a href="#NasDatastoreState">interface NasDatastoreState</a>
* <a href="#ProviderArgs">interface ProviderArgs</a>
* <a href="#ResourcePoolArgs">interface ResourcePoolArgs</a>
* <a href="#ResourcePoolState">interface ResourcePoolState</a>
* <a href="#StorageDrsVmOverrideArgs">interface StorageDrsVmOverrideArgs</a>
* <a href="#StorageDrsVmOverrideState">interface StorageDrsVmOverrideState</a>
* <a href="#TagArgs">interface TagArgs</a>
* <a href="#TagCategoryArgs">interface TagCategoryArgs</a>
* <a href="#TagCategoryState">interface TagCategoryState</a>
* <a href="#TagState">interface TagState</a>
* <a href="#VappContainerArgs">interface VappContainerArgs</a>
* <a href="#VappContainerState">interface VappContainerState</a>
* <a href="#VirtualDiskArgs">interface VirtualDiskArgs</a>
* <a href="#VirtualDiskState">interface VirtualDiskState</a>
* <a href="#VirtualMachineArgs">interface VirtualMachineArgs</a>
* <a href="#VirtualMachineSnapshotArgs">interface VirtualMachineSnapshotArgs</a>
* <a href="#VirtualMachineSnapshotState">interface VirtualMachineSnapshotState</a>
* <a href="#VirtualMachineState">interface VirtualMachineState</a>
* <a href="#VmfsDatastoreArgs">interface VmfsDatastoreArgs</a>
* <a href="#VmfsDatastoreState">interface VmfsDatastoreState</a>

<a href="/computeCluster.ts">computeCluster.ts</a> <a href="/computeClusterHostGroup.ts">computeClusterHostGroup.ts</a> <a href="/computeClusterVmAffinityRule.ts">computeClusterVmAffinityRule.ts</a> <a href="/computeClusterVmAntiAffinityRule.ts">computeClusterVmAntiAffinityRule.ts</a> <a href="/computeClusterVmDependencyRule.ts">computeClusterVmDependencyRule.ts</a> <a href="/computeClusterVmGroup.ts">computeClusterVmGroup.ts</a> <a href="/computeClusterVmHostRule.ts">computeClusterVmHostRule.ts</a> <a href="/customAttribute.ts">customAttribute.ts</a> <a href="/datacenter.ts">datacenter.ts</a> <a href="/datastoreCluster.ts">datastoreCluster.ts</a> <a href="/datastoreClusterVmAntiAffinityRule.ts">datastoreClusterVmAntiAffinityRule.ts</a> <a href="/distributedPortGroup.ts">distributedPortGroup.ts</a> <a href="/distributedVirtualSwitch.ts">distributedVirtualSwitch.ts</a> <a href="/dpmHostOverride.ts">dpmHostOverride.ts</a> <a href="/drsVmOverride.ts">drsVmOverride.ts</a> <a href="/file.ts">file.ts</a> <a href="/folder.ts">folder.ts</a> <a href="/getComputeCluster.ts">getComputeCluster.ts</a> <a href="/getCustomAttribute.ts">getCustomAttribute.ts</a> <a href="/getDatacenter.ts">getDatacenter.ts</a> <a href="/getDatastore.ts">getDatastore.ts</a> <a href="/getDatastoreCluster.ts">getDatastoreCluster.ts</a> <a href="/getDistributedVirtualSwitch.ts">getDistributedVirtualSwitch.ts</a> <a href="/getHost.ts">getHost.ts</a> <a href="/getNetwork.ts">getNetwork.ts</a> <a href="/getResourcePool.ts">getResourcePool.ts</a> <a href="/getTag.ts">getTag.ts</a> <a href="/getTagCategory.ts">getTagCategory.ts</a> <a href="/getVirtualMachine.ts">getVirtualMachine.ts</a> <a href="/getVmfsDisks.ts">getVmfsDisks.ts</a> <a href="/haVmOverride.ts">haVmOverride.ts</a> <a href="/hostPortGroup.ts">hostPortGroup.ts</a> <a href="/hostVirtualSwitch.ts">hostVirtualSwitch.ts</a> <a href="/license.ts">license.ts</a> <a href="/nasDatastore.ts">nasDatastore.ts</a> <a href="/provider.ts">provider.ts</a> <a href="/resourcePool.ts">resourcePool.ts</a> <a href="/storageDrsVmOverride.ts">storageDrsVmOverride.ts</a> <a href="/tag.ts">tag.ts</a> <a href="/tagCategory.ts">tagCategory.ts</a> <a href="/vappContainer.ts">vappContainer.ts</a> <a href="/virtualDisk.ts">virtualDisk.ts</a> <a href="/virtualMachine.ts">virtualMachine.ts</a> <a href="/virtualMachineSnapshot.ts">virtualMachineSnapshot.ts</a> <a href="/vmfsDatastore.ts">vmfsDatastore.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>

* <a href="config">config</a>

<h2 class="pdoc-module-header" id="ComputeCluster">
<a class="pdoc-member-name" href="/computeCluster.ts#L35">class ComputeCluster</a>
</h2>

-> **A note on the naming of this resource:** VMware refers to clusters of
hosts in the UI and documentation as _clusters_, _HA clusters_, or _DRS
clusters_. All of these refer to the same kind of resource (with the latter two
referring to specific features of clustering). In Terraform, we use
`vsphere_compute_cluster` to differentiate host clusters from _datastore
clusters_, which are clusters of datastores that can be used to distribute load
and ensure fault tolerance via distribution of virtual machines. Datastore
clusters can also be managed through Terraform, via the
[`vsphere_datastore_cluster` resource][docs-r-vsphere-datastore-cluster].

[docs-r-vsphere-datastore-cluster]: /docs/providers/vsphere/r/datastore_cluster.html

The `vsphere_compute_cluster` resource can be used to create and manage
clusters of hosts allowing for resource control of compute resources, load
balancing through DRS, and high availability through vSphere HA.

For more information on vSphere clusters and DRS, see [this
page][ref-vsphere-drs-clusters]. For more information on vSphere HA, see [this
page][ref-vsphere-ha-clusters].

[ref-vsphere-drs-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-8ACF3502-5314-469F-8CC9-4A9BD5925BC2.html
[ref-vsphere-ha-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.avail.doc/GUID-5432CA24-14F1-44E3-87FB-61D937831CF6.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L391">constructor</a>
</h3>

```typescript
new ComputeCluster(name: string, args: ComputeClusterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ComputeCluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L44">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ComputeClusterState): ComputeCluster
```


Get an existing ComputeCluster resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L54">property customAttributes</a>
</h3>

```typescript
public customAttributes: pulumi.Output<{ ... } | undefined>;
```


A map of custom attribute ids to attribute
value strings to set for the datastore cluster. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L59">property datacenterId</a>
</h3>

```typescript
public datacenterId: pulumi.Output<string>;
```


The [managed object ID][docs-about-morefs] of
the datacenter to create the cluster in. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L65">property dpmAutomationLevel</a>
</h3>

```typescript
public dpmAutomationLevel: pulumi.Output<string | undefined>;
```


The automation level for host power
operations in this cluster. Can be one of `manual` or `automated`. Default:
`manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L71">property dpmEnabled</a>
</h3>

```typescript
public dpmEnabled: pulumi.Output<boolean | undefined>;
```


Enable DPM support for DRS in this cluster.
Requires `drs_enabled` to be `true` in order to be effective.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L78">property dpmThreshold</a>
</h3>

```typescript
public dpmThreshold: pulumi.Output<number | undefined>;
```


A value between `1` and `5` indicating the
threshold of load within the cluster that influences host power operations.
This affects both power on and power off operations - a lower setting will
tolerate more of a surplus/deficit than a higher setting. Default: `3`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L83">property drsAdvancedOptions</a>
</h3>

```typescript
public drsAdvancedOptions: pulumi.Output<{ ... } | undefined>;
```


A key/value map that specifies advanced
options for DRS and DPM.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L89">property drsAutomationLevel</a>
</h3>

```typescript
public drsAutomationLevel: pulumi.Output<string | undefined>;
```


The default automation level for all
virtual machines in this cluster. Can be one of `manual`,
`partiallyAutomated`, or `fullyAutomated`. Default: `manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L95">property drsEnablePredictiveDrs</a>
</h3>

```typescript
public drsEnablePredictiveDrs: pulumi.Output<boolean | undefined>;
```


When `true`, enables DRS to use data
from [vRealize Operations Manager][ref-vsphere-vro] to make proactive DRS
recommendations. <sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L100">property drsEnableVmOverrides</a>
</h3>

```typescript
public drsEnableVmOverrides: pulumi.Output<boolean | undefined>;
```


Allow individual DRS overrides to be
set for virtual machines in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L104">property drsEnabled</a>
</h3>

```typescript
public drsEnabled: pulumi.Output<boolean | undefined>;
```


Enable DRS for this cluster. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L111">property drsMigrationThreshold</a>
</h3>

```typescript
public drsMigrationThreshold: pulumi.Output<number | undefined>;
```


A value between `1` and `5` indicating
the threshold of imbalance tolerated between hosts. A lower setting will
tolerate more imbalance while a higher setting will tolerate less. Default:
`3`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L120">property folder</a>
</h3>

```typescript
public folder: pulumi.Output<string | undefined>;
```


The relative path to a folder to put this cluster in.
This is a path relative to the datacenter you are deploying the cluster to.
Example: for the `dc1` datacenter, and a provided `folder` of `foo/bar`,
Terraform will place a cluster named `terraform-compute-cluster-test` in a
host folder located at `/dc1/host/foo/bar`, with the final inventory path
being `/dc1/host/foo/bar/terraform-datastore-cluster-test`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L128">property forceEvacuateOnDestroy</a>
</h3>

```typescript
public forceEvacuateOnDestroy: pulumi.Output<boolean | undefined>;
```


When destroying the resource, setting this to
`true` will auto-remove any hosts that are currently a member of the cluster,
as if they were removed by taking their entry out of `host_system_ids` (see
below). This is an advanced
option and should only be used for testing. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L136">property haAdmissionControlFailoverHostSystemIds</a>
</h3>

```typescript
public haAdmissionControlFailoverHostSystemIds: pulumi.Output<string[] | undefined>;
```


Defines the
[managed object IDs][docs-about-morefs] of hosts to use as dedicated failover
hosts. These hosts are kept as available as possible - admission control will
block access to the host, and DRS will ignore the host when making
recommendations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L144">property haAdmissionControlHostFailureTolerance</a>
</h3>

```typescript
public haAdmissionControlHostFailureTolerance: pulumi.Output<number | undefined>;
```


The maximum number
of failed hosts that admission control tolerates when making decisions on
whether to permit virtual machine operations. The maximum is one less than
the number of hosts in the cluster. Default: `1`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L151">property haAdmissionControlPerformanceTolerance</a>
</h3>

```typescript
public haAdmissionControlPerformanceTolerance: pulumi.Output<number | undefined>;
```


The percentage of
resource reduction that a cluster of virtual machines can tolerate in case of
a failover. A value of 0 produces warnings only, whereas a value of 100
disables the setting. Default: `100` (disabled).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L157">property haAdmissionControlPolicy</a>
</h3>

```typescript
public haAdmissionControlPolicy: pulumi.Output<string | undefined>;
```


The type of admission control
policy to use with vSphere HA. Can be one of `resourcePercentage`,
`slotPolicy`, `failoverHosts`, or `disabled`. Default: `resourcePercentage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L167">property haAdmissionControlResourcePercentageAutoCompute</a>
</h3>

```typescript
public haAdmissionControlResourcePercentageAutoCompute: pulumi.Output<boolean | undefined>;
```


Automatically determine available resource percentages by subtracting the
average number of host resources represented by the
`ha_admission_control_host_failure_tolerance`
setting from the total amount of resources in the cluster. Disable to supply
user-defined values. Default: `true`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L173">property haAdmissionControlResourcePercentageCpu</a>
</h3>

```typescript
public haAdmissionControlResourcePercentageCpu: pulumi.Output<number | undefined>;
```


Controls the
user-defined percentage of CPU resources in the cluster to reserve for
failover. Default: `100`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L179">property haAdmissionControlResourcePercentageMemory</a>
</h3>

```typescript
public haAdmissionControlResourcePercentageMemory: pulumi.Output<number | undefined>;
```


Controls the
user-defined percentage of memory resources in the cluster to reserve for
failover. Default: `100`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L184">property haAdmissionControlSlotPolicyExplicitCpu</a>
</h3>

```typescript
public haAdmissionControlSlotPolicyExplicitCpu: pulumi.Output<number | undefined>;
```


Controls the
user-defined CPU slot size, in MHz. Default: `32`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L189">property haAdmissionControlSlotPolicyExplicitMemory</a>
</h3>

```typescript
public haAdmissionControlSlotPolicyExplicitMemory: pulumi.Output<number | undefined>;
```


Controls the
user-defined memory slot size, in MB. Default: `100`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L196">property haAdmissionControlSlotPolicyUseExplicitSize</a>
</h3>

```typescript
public haAdmissionControlSlotPolicyUseExplicitSize: pulumi.Output<boolean | undefined>;
```


Controls
whether or not you wish to supply explicit values to CPU and memory slot
sizes. The default is `false`, which tells vSphere to gather a automatic
average based on all powered-on virtual machines currently in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L201">property haAdvancedOptions</a>
</h3>

```typescript
public haAdvancedOptions: pulumi.Output<{ ... } | undefined>;
```


A key/value map that specifies advanced
options for vSphere HA.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L208">property haDatastoreApdRecoveryAction</a>
</h3>

```typescript
public haDatastoreApdRecoveryAction: pulumi.Output<string | undefined>;
```


Controls the action to take
on virtual machines if an APD status on an affected datastore clears in the
middle of an APD event. Can be one of `none` or `reset`. Default: `none`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L216">property haDatastoreApdResponse</a>
</h3>

```typescript
public haDatastoreApdResponse: pulumi.Output<string | undefined>;
```


Controls the action to take on
virtual machines when the cluster has detected loss to all paths to a
relevant datastore. Can be one of `disabled`, `warning`,
`restartConservative`, or `restartAggressive`.  Default: `disabled`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L223">property haDatastoreApdResponseDelay</a>
</h3>

```typescript
public haDatastoreApdResponseDelay: pulumi.Output<number | undefined>;
```


Controls the delay in minutes
to wait after an APD timeout event to execute the response action defined in
`ha_datastore_apd_response`. Default: `3`
minutes. <sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L231">property haDatastorePdlResponse</a>
</h3>

```typescript
public haDatastorePdlResponse: pulumi.Output<string | undefined>;
```


Controls the action to take on
virtual machines when the cluster has detected a permanent device loss to a
relevant datastore. Can be one of `disabled`, `warning`, or
`restartAggressive`. Default: `disabled`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L236">property haEnabled</a>
</h3>

```typescript
public haEnabled: pulumi.Output<boolean | undefined>;
```


Enable vSphere HA for this cluster. Default:
`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L243">property haHeartbeatDatastoreIds</a>
</h3>

```typescript
public haHeartbeatDatastoreIds: pulumi.Output<string[] | undefined>;
```


The list of managed object IDs for
preferred datastores to use for HA heartbeating. This setting is only useful
when `ha_heartbeat_datastore_policy` is set
to either `userSelectedDs` or `allFeasibleDsWithUserPreference`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L250">property haHeartbeatDatastorePolicy</a>
</h3>

```typescript
public haHeartbeatDatastorePolicy: pulumi.Output<string | undefined>;
```


The selection policy for HA
heartbeat datastores. Can be one of `allFeasibleDs`, `userSelectedDs`, or
`allFeasibleDsWithUserPreference`. Default:
`allFeasibleDsWithUserPreference`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L257">property haHostIsolationResponse</a>
</h3>

```typescript
public haHostIsolationResponse: pulumi.Output<string | undefined>;
```


The action to take on virtual
machines when a host has detected that it has been isolated from the rest of
the cluster. Can be one of `none`, `powerOff`, or `shutdown`. Default:
`none`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L263">property haHostMonitoring</a>
</h3>

```typescript
public haHostMonitoring: pulumi.Output<string | undefined>;
```


Global setting that controls whether
vSphere HA remediates virtual machines on host failure. Can be one of `enabled`
or `disabled`. Default: `enabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L270">property haVmComponentProtection</a>
</h3>

```typescript
public haVmComponentProtection: pulumi.Output<string | undefined>;
```


Controls vSphere VM component
protection for virtual machines in this cluster. Can be one of `enabled` or
`disabled`. Default: `enabled`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L280">property haVmDependencyRestartCondition</a>
</h3>

```typescript
public haVmDependencyRestartCondition: pulumi.Output<string | undefined>;
```


The condition used to
determine whether or not virtual machines in a certain restart priority class
are online, allowing HA to move on to restarting virtual machines on the next
priority. Can be one of `none`, `poweredOn`, `guestHbStatusGreen`, or
`appHbStatusGreen`. The default is `none`, which means that a virtual machine
is considered ready immediately after a host is found to start it on.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L286">property haVmFailureInterval</a>
</h3>

```typescript
public haVmFailureInterval: pulumi.Output<number | undefined>;
```


If a heartbeat from a virtual machine
is not received within this configured interval, the virtual machine is
marked as failed. The value is in seconds. Default: `30`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L295">property haVmMaximumFailureWindow</a>
</h3>

```typescript
public haVmMaximumFailureWindow: pulumi.Output<number | undefined>;
```


The length of the reset window in
which `ha_vm_maximum_resets` can operate. When this
window expires, no more resets are attempted regardless of the setting
configured in `ha_vm_maximum_resets`. `-1` means no window, meaning an
unlimited reset time is allotted. The value is specified in seconds. Default:
`-1` (no window).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L300">property haVmMaximumResets</a>
</h3>

```typescript
public haVmMaximumResets: pulumi.Output<number | undefined>;
```


The maximum number of resets that HA will
perform to a virtual machine when responding to a failure event. Default: `3`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L306">property haVmMinimumUptime</a>
</h3>

```typescript
public haVmMinimumUptime: pulumi.Output<number | undefined>;
```


The time, in seconds, that HA waits after
powering on a virtual machine before monitoring for heartbeats. Default:
`120` (2 minutes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L312">property haVmMonitoring</a>
</h3>

```typescript
public haVmMonitoring: pulumi.Output<string | undefined>;
```


The type of virtual machine monitoring to use
when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
`vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L318">property haVmRestartAdditionalDelay</a>
</h3>

```typescript
public haVmRestartAdditionalDelay: pulumi.Output<number | undefined>;
```


Additional delay in seconds
after ready condition is met. A VM is considered ready at this point.
Default: `0` (no delay). <sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L324">property haVmRestartPriority</a>
</h3>

```typescript
public haVmRestartPriority: pulumi.Output<string | undefined>;
```


The default restart priority
for affected virtual machines when vSphere detects a host failure. Can be one
of `lowest`, `low`, `medium`, `high`, or `highest`. Default: `medium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L331">property haVmRestartTimeout</a>
</h3>

```typescript
public haVmRestartTimeout: pulumi.Output<number | undefined>;
```


The maximum time, in seconds,
that vSphere HA will wait for virtual machines in one priority to be ready
before proceeding with the next priority. Default: `600` (10 minutes).
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L337">property hostClusterExitTimeout</a>
</h3>

```typescript
public hostClusterExitTimeout: pulumi.Output<number | undefined>;
```


The timeout for each host maintenance mode
operation when removing hosts from a cluster. The value is specified in
seconds. Default: `3600` (1 hour).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L342">property hostSystemIds</a>
</h3>

```typescript
public hostSystemIds: pulumi.Output<string[] | undefined>;
```


The [managed object IDs][docs-about-morefs] of
the hosts to put in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L346">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L353">property proactiveHaAutomationLevel</a>
</h3>

```typescript
public proactiveHaAutomationLevel: pulumi.Output<string | undefined>;
```


Determines how the host
quarantine, maintenance mode, or virtual machine migration recommendations
made by proactive HA are to be handled. Can be one of `Automated` or
`Manual`. Default: `Manual`. <sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L358">property proactiveHaEnabled</a>
</h3>

```typescript
public proactiveHaEnabled: pulumi.Output<boolean | undefined>;
```


Enables Proactive HA. Default: `false`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L367">property proactiveHaModerateRemediation</a>
</h3>

```typescript
public proactiveHaModerateRemediation: pulumi.Output<string | undefined>;
```


The configured remediation
for moderately degraded hosts. Can be one of `MaintenanceMode` or
`QuarantineMode`. Note that this cannot be set to `MaintenanceMode` when
`proactive_ha_severe_remediation` is set
to `QuarantineMode`. Default: `QuarantineMode`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L373">property proactiveHaProviderIds</a>
</h3>

```typescript
public proactiveHaProviderIds: pulumi.Output<string[] | undefined>;
```


The list of IDs for health update
providers configured for this cluster.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L382">property proactiveHaSevereRemediation</a>
</h3>

```typescript
public proactiveHaSevereRemediation: pulumi.Output<string | undefined>;
```


The configured remediation for
severely degraded hosts. Can be one of `MaintenanceMode` or `QuarantineMode`.
Note that this cannot be set to `QuarantineMode` when
`proactive_ha_moderate_remediation` is
set to `MaintenanceMode`. Default: `QuarantineMode`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L386">property resourcePoolId</a>
</h3>

```typescript
public resourcePoolId: pulumi.Output<string>;
```


The managed object ID of the cluster's root resource pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L391">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<string[] | undefined>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ComputeClusterHostGroup">
<a class="pdoc-member-name" href="/computeClusterHostGroup.ts#L27">class ComputeClusterHostGroup</a>
</h2>

The `vsphere_compute_cluster_host_group` resource can be used to manage groups
of hosts in a cluster, either created by the
[`vsphere_compute_cluster`][tf-vsphere-cluster-resource] resource or looked up
by the [`vsphere_compute_cluster`][tf-vsphere-cluster-data-source] data source.

[tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
[tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html

This resource mainly serves as an input to the
[`vsphere_compute_cluster_vm_host_rule`][tf-vsphere-cluster-vm-host-rule-resource]
resource - see the documentation for that resource for further details on how
to use host groups.

[tf-vsphere-cluster-vm-host-rule-resource]: /docs/providers/vsphere/r/compute_cluster_vm_host_rule.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterHostGroup.ts#L55">constructor</a>
</h3>

```typescript
new ComputeClusterHostGroup(name: string, args: ComputeClusterHostGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ComputeClusterHostGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterHostGroup.ts#L36">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ComputeClusterHostGroupState): ComputeClusterHostGroup
```


Get an existing ComputeClusterHostGroup resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterHostGroup.ts#L45">property computeClusterId</a>
</h3>

```typescript
public computeClusterId: pulumi.Output<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterHostGroup.ts#L50">property hostSystemIds</a>
</h3>

```typescript
public hostSystemIds: pulumi.Output<string[] | undefined>;
```


The [managed object IDs][docs-about-morefs] of
the hosts to put in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterHostGroup.ts#L55">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the host group. This must be unique in the
cluster. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ComputeClusterVmAffinityRule">
<a class="pdoc-member-name" href="/computeClusterVmAffinityRule.ts#L34">class ComputeClusterVmAffinityRule</a>
</h2>

The `vsphere_compute_cluster_vm_affinity_rule` resource can be used to manage
VM affinity rules in a cluster, either created by the
[`vsphere_compute_cluster`][tf-vsphere-cluster-resource] resource or looked up
by the [`vsphere_compute_cluster`][tf-vsphere-cluster-data-source] data source.

[tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
[tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html

This rule can be used to tell a set to virtual machines to run together on a
single host within a cluster. When configured, DRS will make a best effort to
ensure that the virtual machines run on the same host, or prevent any operation
that would keep that from happening, depending on the value of the
`mandatory` flag.

-> Keep in mind that this rule can only be used to tell VMs to run together on
a _non-specific_ host - it can't be used to pin VMs to a host. For that, see
the
[`vsphere_compute_cluster_vm_host_rule`][tf-vsphere-cluster-vm-host-rule-resource]
resource.

[tf-vsphere-cluster-vm-host-rule-resource]: /docs/providers/vsphere/r/compute_cluster_vm_host_rule.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAffinityRule.ts#L70">constructor</a>
</h3>

```typescript
new ComputeClusterVmAffinityRule(name: string, args: ComputeClusterVmAffinityRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ComputeClusterVmAffinityRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAffinityRule.ts#L43">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ComputeClusterVmAffinityRuleState): ComputeClusterVmAffinityRule
```


Get an existing ComputeClusterVmAffinityRule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAffinityRule.ts#L52">property computeClusterId</a>
</h3>

```typescript
public computeClusterId: pulumi.Output<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAffinityRule.ts#L56">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Enable this rule in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAffinityRule.ts#L61">property mandatory</a>
</h3>

```typescript
public mandatory: pulumi.Output<boolean | undefined>;
```


When this value is `true`, prevents any virtual
machine operations that may violate this rule. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAffinityRule.ts#L65">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the rule. This must be unique in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAffinityRule.ts#L70">property virtualMachineIds</a>
</h3>

```typescript
public virtualMachineIds: pulumi.Output<string[]>;
```


The UUIDs of the virtual machines to run
on the same host together.

<h2 class="pdoc-module-header" id="ComputeClusterVmAntiAffinityRule">
<a class="pdoc-member-name" href="/computeClusterVmAntiAffinityRule.ts#L35">class ComputeClusterVmAntiAffinityRule</a>
</h2>

The `vsphere_compute_cluster_vm_anti_affinity_rule` resource can be used to
manage VM anti-affinity rules in a cluster, either created by the
[`vsphere_compute_cluster`][tf-vsphere-cluster-resource] resource or looked up
by the [`vsphere_compute_cluster`][tf-vsphere-cluster-data-source] data source.

[tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
[tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html

This rule can be used to tell a set to virtual machines to run on different
hosts within a cluster, useful for preventing single points of failure in
application cluster scenarios. When configured, DRS will make a best effort to
ensure that the virtual machines run on different hosts, or prevent any
operation that would keep that from happening, depending on the value of the
`mandatory` flag.

-> Keep in mind that this rule can only be used to tell VMs to run separately
on _non-specific_ hosts - specific hosts cannot be specified with this rule.
For that, see the
[`vsphere_compute_cluster_vm_host_rule`][tf-vsphere-cluster-vm-host-rule-resource]
resource.

[tf-vsphere-cluster-vm-host-rule-resource]: /docs/providers/vsphere/r/compute_cluster_vm_host_rule.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAntiAffinityRule.ts#L71">constructor</a>
</h3>

```typescript
new ComputeClusterVmAntiAffinityRule(name: string, args: ComputeClusterVmAntiAffinityRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ComputeClusterVmAntiAffinityRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAntiAffinityRule.ts#L44">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ComputeClusterVmAntiAffinityRuleState): ComputeClusterVmAntiAffinityRule
```


Get an existing ComputeClusterVmAntiAffinityRule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAntiAffinityRule.ts#L53">property computeClusterId</a>
</h3>

```typescript
public computeClusterId: pulumi.Output<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAntiAffinityRule.ts#L57">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Enable this rule in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAntiAffinityRule.ts#L62">property mandatory</a>
</h3>

```typescript
public mandatory: pulumi.Output<boolean | undefined>;
```


When this value is `true`, prevents any virtual
machine operations that may violate this rule. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAntiAffinityRule.ts#L66">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the rule. This must be unique in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAntiAffinityRule.ts#L71">property virtualMachineIds</a>
</h3>

```typescript
public virtualMachineIds: pulumi.Output<string[]>;
```


The UUIDs of the virtual machines to run
on hosts different from each other.

<h2 class="pdoc-module-header" id="ComputeClusterVmDependencyRule">
<a class="pdoc-member-name" href="/computeClusterVmDependencyRule.ts#L26">class ComputeClusterVmDependencyRule</a>
</h2>

The `vsphere_compute_cluster_vm_dependency_rule` resource can be used to manage
VM dependency rules in a cluster, either created by the
[`vsphere_compute_cluster`][tf-vsphere-cluster-resource] resource or looked up
by the [`vsphere_compute_cluster`][tf-vsphere-cluster-data-source] data source.

[tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
[tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html

A virtual machine dependency rule applies to vSphere HA, and allows
user-defined startup orders for virtual machines in the case of host failure.
Virtual machines are supplied via groups, which can be managed via the
[`vsphere_compute_cluster_vm_group`][tf-vsphere-cluster-vm-group-resource]
resource.

[tf-vsphere-cluster-vm-group-resource]: /docs/providers/vsphere/r/compute_cluster_vm_group.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L72">constructor</a>
</h3>

```typescript
new ComputeClusterVmDependencyRule(name: string, args: ComputeClusterVmDependencyRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ComputeClusterVmDependencyRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L35">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ComputeClusterVmDependencyRuleState): ComputeClusterVmDependencyRule
```


Get an existing ComputeClusterVmDependencyRule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L44">property computeClusterId</a>
</h3>

```typescript
public computeClusterId: pulumi.Output<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L51">property dependencyVmGroupName</a>
</h3>

```typescript
public dependencyVmGroupName: pulumi.Output<string>;
```


The name of the VM group that this
rule depends on. The VMs defined in the group specified by
`vm_group_name` will not be started until the VMs in this
group are started.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L55">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Enable this rule in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L60">property mandatory</a>
</h3>

```typescript
public mandatory: pulumi.Output<boolean | undefined>;
```


When this value is `true`, prevents any virtual
machine operations that may violate this rule. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L65">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the rule. This must be unique in the
cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L72">property vmGroupName</a>
</h3>

```typescript
public vmGroupName: pulumi.Output<string>;
```


The name of the VM group that is the subject of
this rule. The VMs defined in this group will not be started until the VMs in
the group specified by
`dependency_vm_group_name` are started.

<h2 class="pdoc-module-header" id="ComputeClusterVmGroup">
<a class="pdoc-member-name" href="/computeClusterVmGroup.ts#L29">class ComputeClusterVmGroup</a>
</h2>

The `vsphere_compute_cluster_vm_group` resource can be used to manage groups of
virtual machines in a cluster, either created by the
[`vsphere_compute_cluster`][tf-vsphere-cluster-resource] resource or looked up
by the [`vsphere_compute_cluster`][tf-vsphere-cluster-data-source] data source.

[tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
[tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html

This resource mainly serves as an input to the
[`vsphere_compute_cluster_vm_dependency_rule`][tf-vsphere-cluster-vm-dependency-rule-resource]
and
[`vsphere_compute_cluster_vm_host_rule`][tf-vsphere-cluster-vm-host-rule-resource]
resources. See the individual resource documentation pages for more information.

[tf-vsphere-cluster-vm-dependency-rule-resource]: /docs/providers/vsphere/r/compute_cluster_vm_dependency_rule.html
[tf-vsphere-cluster-vm-host-rule-resource]: /docs/providers/vsphere/r/compute_cluster_vm_host_rule.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmGroup.ts#L57">constructor</a>
</h3>

```typescript
new ComputeClusterVmGroup(name: string, args: ComputeClusterVmGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ComputeClusterVmGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmGroup.ts#L38">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ComputeClusterVmGroupState): ComputeClusterVmGroup
```


Get an existing ComputeClusterVmGroup resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmGroup.ts#L47">property computeClusterId</a>
</h3>

```typescript
public computeClusterId: pulumi.Output<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmGroup.ts#L52">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the VM group. This must be unique in the
cluster. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmGroup.ts#L57">property virtualMachineIds</a>
</h3>

```typescript
public virtualMachineIds: pulumi.Output<string[] | undefined>;
```


The UUIDs of the virtual machines in this
group.

<h2 class="pdoc-module-header" id="ComputeClusterVmHostRule">
<a class="pdoc-member-name" href="/computeClusterVmHostRule.ts#L31">class ComputeClusterVmHostRule</a>
</h2>

The `vsphere_compute_cluster_vm_host_rule` resource can be used to manage
VM-to-host rules in a cluster, either created by the
[`vsphere_compute_cluster`][tf-vsphere-cluster-resource] resource or looked up
by the [`vsphere_compute_cluster`][tf-vsphere-cluster-data-source] data source.

[tf-vsphere-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html
[tf-vsphere-cluster-data-source]: /docs/providers/vsphere/d/compute_cluster.html

This resource can create both _affinity rules_, where virtual machines run on
specified hosts, or _anti-affinity_ rules, where virtual machines run on hosts
outside of the ones specified in the rule. Virtual machines and hosts are
supplied via groups, which can be managed via the
[`vsphere_compute_cluster_vm_group`][tf-vsphere-cluster-vm-group-resource] and
[`vsphere_compute_cluster_host_group`][tf-vsphere-cluster-host-group-resource]
resources.

[tf-vsphere-cluster-vm-group-resource]: /docs/providers/vsphere/r/compute_cluster_vm_group.html
[tf-vsphere-cluster-host-group-resource]: /docs/providers/vsphere/r/compute_cluster_host_group.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L80">constructor</a>
</h3>

```typescript
new ComputeClusterVmHostRule(name: string, args: ComputeClusterVmHostRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ComputeClusterVmHostRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L40">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ComputeClusterVmHostRuleState): ComputeClusterVmHostRule
```


Get an existing ComputeClusterVmHostRule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L49">property affinityHostGroupName</a>
</h3>

```typescript
public affinityHostGroupName: pulumi.Output<string | undefined>;
```


When this field is used, the virtual
machines defined in `vm_group_name` will be run on the
hosts defined in this host group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L55">property antiAffinityHostGroupName</a>
</h3>

```typescript
public antiAffinityHostGroupName: pulumi.Output<string | undefined>;
```


When this field is used, the
virtual machines defined in `vm_group_name` will _not_ be
run on the hosts defined in this host group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L61">property computeClusterId</a>
</h3>

```typescript
public computeClusterId: pulumi.Output<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L65">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Enable this rule in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L70">property mandatory</a>
</h3>

```typescript
public mandatory: pulumi.Output<boolean | undefined>;
```


When this value is `true`, prevents any virtual
machine operations that may violate this rule. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L75">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the rule. This must be unique in the
cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L80">property vmGroupName</a>
</h3>

```typescript
public vmGroupName: pulumi.Output<string>;
```


The name of the virtual machine group to use
with this rule.

<h2 class="pdoc-module-header" id="CustomAttribute">
<a class="pdoc-member-name" href="/customAttribute.ts#L19">class CustomAttribute</a>
</h2>

The `vsphere_custom_attribute` resource can be used to create and manage custom
attributes, which allow users to associate user-specific meta-information with
vSphere managed objects. Custom attribute values must be strings and are stored
on the vCenter Server and not the managed object.

For more information about custom attributes, click [here][ext-custom-attributes].

[ext-custom-attributes]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vcenterhost.doc/GUID-73606C4C-763C-4E27-A1DA-032E4C46219D.html

~> **NOTE:** Custom attributes are unsupported on direct ESXi connections
and require vCenter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/customAttribute.ts#L42">constructor</a>
</h3>

```typescript
new CustomAttribute(name: string, args?: CustomAttributeArgs, opts?: pulumi.CustomResourceOptions)
```


Create a CustomAttribute resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/customAttribute.ts#L28">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CustomAttributeState): CustomAttribute
```


Get an existing CustomAttribute resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/customAttribute.ts#L38">property managedObjectType</a>
</h3>

```typescript
public managedObjectType: pulumi.Output<string | undefined>;
```


The object type that this attribute may be
applied to. If not set, the custom attribute may be applied to any object
type. For a full list, click here. Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/customAttribute.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the custom attribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Datacenter">
<a class="pdoc-member-name" href="/datacenter.ts#L10">class Datacenter</a>
</h2>

Provides a VMware vSphere datacenter resource. This can be used as the primary
container of inventory objects such as hosts and virtual machines.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datacenter.ts#L48">constructor</a>
</h3>

```typescript
new Datacenter(name: string, args?: DatacenterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Datacenter resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datacenter.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatacenterState): Datacenter
```


Get an existing Datacenter resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datacenter.ts#L29">property customAttributes</a>
</h3>

```typescript
public customAttributes: pulumi.Output<{ ... } | undefined>;
```


Map of custom attribute ids to value
strings to set for datacenter resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datacenter.ts#L34">property folder</a>
</h3>

```typescript
public folder: pulumi.Output<string | undefined>;
```


The folder where the datacenter should be created.
Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datacenter.ts#L38">property moid</a>
</h3>

```typescript
public moid: pulumi.Output<string>;
```


[Managed object ID][docs-about-morefs] of this datacenter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datacenter.ts#L43">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the datacenter. This name needs to be unique
within the folder. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datacenter.ts#L48">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<string[] | undefined>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DatastoreCluster">
<a class="pdoc-member-name" href="/datastoreCluster.ts#L22">class DatastoreCluster</a>
</h2>

The `vsphere_datastore_cluster` resource can be used to create and manage
datastore clusters. This can be used to create groups of datastores with a
shared management interface, allowing for resource control and load balancing
through Storage DRS.

For more information on vSphere datastore clusters and Storage DRS, see [this
page][ref-vsphere-datastore-clusters].

[ref-vsphere-datastore-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-598DF695-107E-406B-9C95-0AF961FC227A.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** Storage DRS requires a vSphere Enterprise Plus license.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L178">constructor</a>
</h3>

```typescript
new DatastoreCluster(name: string, args: DatastoreClusterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DatastoreCluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L31">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatastoreClusterState): DatastoreCluster
```


Get an existing DatastoreCluster resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L41">property customAttributes</a>
</h3>

```typescript
public customAttributes: pulumi.Output<{ ... } | undefined>;
```


A map of custom attribute ids to attribute
value strings to set for the datastore cluster. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L47">property datacenterId</a>
</h3>

```typescript
public datacenterId: pulumi.Output<string>;
```


The [managed object ID][docs-about-morefs] of
the datacenter to create the datastore cluster in. Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L57">property folder</a>
</h3>

```typescript
public folder: pulumi.Output<string | undefined>;
```


The relative path to a folder to put this datastore
cluster in.  This is a path relative to the datacenter you are deploying the
datastore to.  Example: for the `dc1` datacenter, and a provided `folder` of
`foo/bar`, Terraform will place a datastore cluster named
`terraform-datastore-cluster-test` in a datastore folder located at
`/dc1/datastore/foo/bar`, with the final inventory path being
`/dc1/datastore/foo/bar/terraform-datastore-cluster-test`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L61">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the datastore cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L66">property sdrsAdvancedOptions</a>
</h3>

```typescript
public sdrsAdvancedOptions: pulumi.Output<{ ... } | undefined>;
```


A key/value map of advanced Storage DRS
settings that are not exposed via Terraform or the vSphere client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L71">property sdrsAutomationLevel</a>
</h3>

```typescript
public sdrsAutomationLevel: pulumi.Output<string | undefined>;
```


The global automation level for all
virtual machines in this datastore cluster. Default: `manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L76">property sdrsDefaultIntraVmAffinity</a>
</h3>

```typescript
public sdrsDefaultIntraVmAffinity: pulumi.Output<boolean | undefined>;
```


When `true`, all disks in a
single virtual machine will be kept on the same datastore. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L81">property sdrsEnabled</a>
</h3>

```typescript
public sdrsEnabled: pulumi.Output<boolean | undefined>;
```


Enable Storage DRS for this datastore cluster.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L88">property sdrsFreeSpaceThreshold</a>
</h3>

```typescript
public sdrsFreeSpaceThreshold: pulumi.Output<number | undefined>;
```


The free space threshold to use.
When set to `utilization`, `drs_space_utilization_threshold` is used, and
when set to `freeSpace`, `drs_free_space_threshold` is used. Default:
`utilization`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L93">property sdrsFreeSpaceThresholdMode</a>
</h3>

```typescript
public sdrsFreeSpaceThresholdMode: pulumi.Output<string | undefined>;
```


The free space threshold to use. When set to utilization, drs_space_utilization_threshold is used, and when set to
freeSpace, drs_free_space_threshold is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L99">property sdrsFreeSpaceUtilizationDifference</a>
</h3>

```typescript
public sdrsFreeSpaceUtilizationDifference: pulumi.Output<number | undefined>;
```


The threshold, in
percent, of difference between space utilization in datastores before storage
DRS makes decisions to balance the space. Default: `5` percent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L104">property sdrsIoBalanceAutomationLevel</a>
</h3>

```typescript
public sdrsIoBalanceAutomationLevel: pulumi.Output<string | undefined>;
```


Overrides the default
automation settings when correcting I/O load imbalances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L110">property sdrsIoLatencyThreshold</a>
</h3>

```typescript
public sdrsIoLatencyThreshold: pulumi.Output<number | undefined>;
```


The I/O latency threshold, in
milliseconds, that storage DRS uses to make recommendations to move disks
from this datastore. Default: `15` seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L115">property sdrsIoLoadBalanceEnabled</a>
</h3>

```typescript
public sdrsIoLoadBalanceEnabled: pulumi.Output<boolean | undefined>;
```


Enable I/O load balancing for
this datastore cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L121">property sdrsIoLoadImbalanceThreshold</a>
</h3>

```typescript
public sdrsIoLoadImbalanceThreshold: pulumi.Output<number | undefined>;
```


The difference between load
in datastores in the cluster before storage DRS makes recommendations to
balance the load. Default: `5` percent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L130">property sdrsIoReservableIopsThreshold</a>
</h3>

```typescript
public sdrsIoReservableIopsThreshold: pulumi.Output<number | undefined>;
```


The threshold of reservable
IOPS of all virtual machines on the datastore before storage DRS makes
recommendations to move VMs off of a datastore. Note that this setting should
only be set if `sdrs_io_reservable_percent_threshold` cannot make an accurate
estimate of the capacity of the datastores in your cluster, and should be set
to roughly 50-60% of the worst case peak performance of the backing LUNs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L137">property sdrsIoReservablePercentThreshold</a>
</h3>

```typescript
public sdrsIoReservablePercentThreshold: pulumi.Output<number | undefined>;
```


The threshold, in
percent, of actual estimated performance of the datastore (in IOPS) that
storage DRS uses to make recommendations to move VMs off of a datastore when
the total reservable IOPS exceeds the threshold. Default: `60` percent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L144">property sdrsIoReservableThresholdMode</a>
</h3>

```typescript
public sdrsIoReservableThresholdMode: pulumi.Output<string | undefined>;
```


The reservable IOPS
threshold setting to use, `sdrs_io_reservable_percent_threshold` in the event
of `automatic`, or `sdrs_io_reservable_iops_threshold` in the event of
`manual`. Default: `automatic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L149">property sdrsLoadBalanceInterval</a>
</h3>

```typescript
public sdrsLoadBalanceInterval: pulumi.Output<number | undefined>;
```


The storage DRS poll interval, in
minutes. Default: `480` minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L154">property sdrsPolicyEnforcementAutomationLevel</a>
</h3>

```typescript
public sdrsPolicyEnforcementAutomationLevel: pulumi.Output<string | undefined>;
```


Overrides the default
automation settings when correcting storage and VM policy violations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L159">property sdrsRuleEnforcementAutomationLevel</a>
</h3>

```typescript
public sdrsRuleEnforcementAutomationLevel: pulumi.Output<string | undefined>;
```


Overrides the default
automation settings when correcting affinity rule violations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L164">property sdrsSpaceBalanceAutomationLevel</a>
</h3>

```typescript
public sdrsSpaceBalanceAutomationLevel: pulumi.Output<string | undefined>;
```


Overrides the default
automation settings when correcting disk space imbalances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L168">property sdrsSpaceUtilizationThreshold</a>
</h3>

```typescript
public sdrsSpaceUtilizationThreshold: pulumi.Output<number | undefined>;
```


The threshold, in percent of used space, that storage DRS uses to make decisions to migrate VMs out of a datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L173">property sdrsVmEvacuationAutomationLevel</a>
</h3>

```typescript
public sdrsVmEvacuationAutomationLevel: pulumi.Output<string | undefined>;
```


Overrides the default
automation settings when generating recommendations for datastore evacuation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L178">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<string[] | undefined>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DatastoreClusterVmAntiAffinityRule">
<a class="pdoc-member-name" href="/datastoreClusterVmAntiAffinityRule.ts#L27">class DatastoreClusterVmAntiAffinityRule</a>
</h2>

The `vsphere_datastore_cluster_vm_anti_affinity_rule` resource can be used to
manage VM anti-affinity rules in a datastore cluster, either created by the
[`vsphere_datastore_cluster`][tf-vsphere-datastore-cluster-resource] resource or looked up
by the [`vsphere_datastore_cluster`][tf-vsphere-datastore-cluster-data-source] data source.

[tf-vsphere-datastore-cluster-resource]: /docs/providers/vsphere/r/datastore_cluster.html
[tf-vsphere-datastore-cluster-data-source]: /docs/providers/vsphere/d/datastore_cluster.html

This rule can be used to tell a set to virtual machines to run on different
datastores within a cluster, useful for preventing single points of failure in
application cluster scenarios. When configured, Storage DRS will make a best effort to
ensure that the virtual machines run on different datastores, or prevent any
operation that would keep that from happening, depending on the value of the
`mandatory` flag.

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** Storage DRS requires a vSphere Enterprise Plus license.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreClusterVmAntiAffinityRule.ts#L63">constructor</a>
</h3>

```typescript
new DatastoreClusterVmAntiAffinityRule(name: string, args: DatastoreClusterVmAntiAffinityRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DatastoreClusterVmAntiAffinityRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreClusterVmAntiAffinityRule.ts#L36">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatastoreClusterVmAntiAffinityRuleState): DatastoreClusterVmAntiAffinityRule
```


Get an existing DatastoreClusterVmAntiAffinityRule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreClusterVmAntiAffinityRule.ts#L45">property datastoreClusterId</a>
</h3>

```typescript
public datastoreClusterId: pulumi.Output<string>;
```


The [managed object reference
ID][docs-about-morefs] of the datastore cluster to put the group in.  Forces
a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreClusterVmAntiAffinityRule.ts#L49">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Enable this rule in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreClusterVmAntiAffinityRule.ts#L54">property mandatory</a>
</h3>

```typescript
public mandatory: pulumi.Output<boolean | undefined>;
```


When this value is `true`, prevents any virtual
machine operations that may violate this rule. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreClusterVmAntiAffinityRule.ts#L58">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the rule. This must be unique in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreClusterVmAntiAffinityRule.ts#L63">property virtualMachineIds</a>
</h3>

```typescript
public virtualMachineIds: pulumi.Output<string[]>;
```


The UUIDs of the virtual machines to run
on different datastores from each other.

<h2 class="pdoc-module-header" id="DistributedPortGroup">
<a class="pdoc-member-name" href="/distributedPortGroup.ts#L27">class DistributedPortGroup</a>
</h2>

The `vsphere_distributed_port_group` resource can be used to manage vSphere
distributed virtual port groups. These port groups are connected to distributed
virtual switches, which can be managed by the
[`vsphere_distributed_virtual_switch`][distributed-virtual-switch] resource.

Distributed port groups can be used as networks for virtual machines, allowing
VMs to use the networking supplied by a distributed virtual switch (DVS), with
a set of policies that apply to that individual newtork, if desired.

For an overview on vSphere networking concepts, see [this
page][ref-vsphere-net-concepts]. For more information on vSphere DVS
portgroups, see [this page][ref-vsphere-dvportgroup].

[distributed-virtual-switch]: /docs/providers/vsphere/r/distributed_virtual_switch.html
[ref-vsphere-net-concepts]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html
[ref-vsphere-dvportgroup]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-69933F6E-2442-46CF-AA17-1196CB9A0A09.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L258">constructor</a>
</h3>

```typescript
new DistributedPortGroup(name: string, args: DistributedPortGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DistributedPortGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L36">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DistributedPortGroupState): DistributedPortGroup
```


Get an existing DistributedPortGroup resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L43">property activeUplinks</a>
</h3>

```typescript
public activeUplinks: pulumi.Output<string[]>;
```


List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L48">property allowForgedTransmits</a>
</h3>

```typescript
public allowForgedTransmits: pulumi.Output<boolean>;
```


Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address
than that of its own.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L52">property allowMacChanges</a>
</h3>

```typescript
public allowMacChanges: pulumi.Output<boolean>;
```


Controls whether or not the Media Access Control (MAC) address can be changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L56">property allowPromiscuous</a>
</h3>

```typescript
public allowPromiscuous: pulumi.Output<boolean>;
```


Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L61">property autoExpand</a>
</h3>

```typescript
public autoExpand: pulumi.Output<boolean | undefined>;
```


Allows the port group to create additional ports
past the limit specified in `number_of_ports` if necessary. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L65">property blockAllPorts</a>
</h3>

```typescript
public blockAllPorts: pulumi.Output<boolean>;
```


Indicates whether to block all ports by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L70">property blockOverrideAllowed</a>
</h3>

```typescript
public blockOverrideAllowed: pulumi.Output<boolean | undefined>;
```


Allow the [port shutdown
policy][port-shutdown-policy] to be overridden on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L74">property checkBeacon</a>
</h3>

```typescript
public checkBeacon: pulumi.Output<boolean>;
```


Enable beacon probing on the ports this policy applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L78">property configVersion</a>
</h3>

```typescript
public configVersion: pulumi.Output<string>;
```


Version string of the configuration that this spec is trying to change.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L84">property customAttributes</a>
</h3>

```typescript
public customAttributes: pulumi.Output<{ ... } | undefined>;
```


Map of custom attribute ids to attribute
value string to set for port group. See [here][docs-setting-custom-attributes]
for a reference on how to set values for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L88">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


An optional description for the port group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L92">property directpathGen2Allowed</a>
</h3>

```typescript
public directpathGen2Allowed: pulumi.Output<boolean>;
```


Allow VMDirectPath Gen2 on the ports this policy applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L97">property distributedVirtualSwitchUuid</a>
</h3>

```typescript
public distributedVirtualSwitchUuid: pulumi.Output<string>;
```


The ID of the DVS to add the
port group to. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L101">property egressShapingAverageBandwidth</a>
</h3>

```typescript
public egressShapingAverageBandwidth: pulumi.Output<number>;
```


The average egress bandwidth in bits per second if egress shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L105">property egressShapingBurstSize</a>
</h3>

```typescript
public egressShapingBurstSize: pulumi.Output<number>;
```


The maximum egress burst size allowed in bytes if egress shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L109">property egressShapingEnabled</a>
</h3>

```typescript
public egressShapingEnabled: pulumi.Output<boolean>;
```


True if the traffic shaper is enabled for egress traffic on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L113">property egressShapingPeakBandwidth</a>
</h3>

```typescript
public egressShapingPeakBandwidth: pulumi.Output<number>;
```


The peak egress bandwidth during bursts in bits per second if egress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L117">property failback</a>
</h3>

```typescript
public failback: pulumi.Output<boolean>;
```


If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L121">property ingressShapingAverageBandwidth</a>
</h3>

```typescript
public ingressShapingAverageBandwidth: pulumi.Output<number>;
```


The average ingress bandwidth in bits per second if ingress shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L125">property ingressShapingBurstSize</a>
</h3>

```typescript
public ingressShapingBurstSize: pulumi.Output<number>;
```


The maximum ingress burst size allowed in bytes if ingress shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L129">property ingressShapingEnabled</a>
</h3>

```typescript
public ingressShapingEnabled: pulumi.Output<boolean>;
```


True if the traffic shaper is enabled for ingress traffic on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L133">property ingressShapingPeakBandwidth</a>
</h3>

```typescript
public ingressShapingPeakBandwidth: pulumi.Output<number>;
```


The peak ingress bandwidth during bursts in bits per second if ingress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L137">property key</a>
</h3>

```typescript
public key: pulumi.Output<string>;
```


The generated UUID of the portgroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L141">property lacpEnabled</a>
</h3>

```typescript
public lacpEnabled: pulumi.Output<boolean>;
```


Whether or not to enable LACP on all uplink ports.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L145">property lacpMode</a>
</h3>

```typescript
public lacpMode: pulumi.Output<string>;
```


The uplink LACP mode to use. Can be one of active or passive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L150">property livePortMovingAllowed</a>
</h3>

```typescript
public livePortMovingAllowed: pulumi.Output<boolean | undefined>;
```


Allow a port in this port group to be
moved to another port group while it is connected.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L154">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the port group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L158">property netflowEnabled</a>
</h3>

```typescript
public netflowEnabled: pulumi.Output<boolean>;
```


Indicates whether to enable netflow on all ports.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L164">property netflowOverrideAllowed</a>
</h3>

```typescript
public netflowOverrideAllowed: pulumi.Output<boolean | undefined>;
```


Allow the [Netflow
policy][netflow-policy] on this port group to be overridden on an individual
port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L170">property networkResourcePoolKey</a>
</h3>

```typescript
public networkResourcePoolKey: pulumi.Output<string | undefined>;
```


The key of a network resource pool
to associate with this port group. The default is `-1`, which implies no
association.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L175">property networkResourcePoolOverrideAllowed</a>
</h3>

```typescript
public networkResourcePoolOverrideAllowed: pulumi.Output<boolean | undefined>;
```


Allow the network
resource pool set on this port group to be overridden on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L179">property notifySwitches</a>
</h3>

```typescript
public notifySwitches: pulumi.Output<boolean>;
```


If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L184">property numberOfPorts</a>
</h3>

```typescript
public numberOfPorts: pulumi.Output<number>;
```


The number of ports available on this port
group. Cannot be decreased below the amount of used ports on the port group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L189">property portConfigResetAtDisconnect</a>
</h3>

```typescript
public portConfigResetAtDisconnect: pulumi.Output<boolean | undefined>;
```


Reset a port's settings to the
settings defined on this port group policy when the port disconnects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L195">property portNameFormat</a>
</h3>

```typescript
public portNameFormat: pulumi.Output<string | undefined>;
```


An optional formatting policy for naming of
the ports in this port group. See the `portNameFormat` attribute listed
[here][ext-vsphere-portname-format] for details on the format syntax.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L199">property portPrivateSecondaryVlanId</a>
</h3>

```typescript
public portPrivateSecondaryVlanId: pulumi.Output<number>;
```


The secondary VLAN ID for this port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L205">property securityPolicyOverrideAllowed</a>
</h3>

```typescript
public securityPolicyOverrideAllowed: pulumi.Output<boolean | undefined>;
```


Allow the [security policy
settings][sec-policy-settings] defined in this port group policy to be
overridden on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L211">property shapingOverrideAllowed</a>
</h3>

```typescript
public shapingOverrideAllowed: pulumi.Output<boolean | undefined>;
```


Allow the [traffic shaping
options][traffic-shaping-settings] on this port group policy to be overridden
on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L215">property standbyUplinks</a>
</h3>

```typescript
public standbyUplinks: pulumi.Output<string[]>;
```


List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L219">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<string[] | undefined>;
```


A list of tag IDs to apply to this object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L224">property teamingPolicy</a>
</h3>

```typescript
public teamingPolicy: pulumi.Output<string>;
```


The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid,
failover_explicit, or loadbalance_loadbased.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L229">property trafficFilterOverrideAllowed</a>
</h3>

```typescript
public trafficFilterOverrideAllowed: pulumi.Output<boolean | undefined>;
```


Allow any traffic filters on
this port group to be overridden on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L234">property txUplink</a>
</h3>

```typescript
public txUplink: pulumi.Output<boolean>;
```


If true, a copy of packets sent to the switch will always be forwarded to an uplink in addition to the regular
packet forwarded done by the switch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L239">property type</a>
</h3>

```typescript
public type: pulumi.Output<string | undefined>;
```


The port group type. Can be one of `earlyBinding` (static
binding) or `ephemeral`. Default: `earlyBinding`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L245">property uplinkTeamingOverrideAllowed</a>
</h3>

```typescript
public uplinkTeamingOverrideAllowed: pulumi.Output<boolean | undefined>;
```


Allow the [uplink teaming
options][uplink-teaming-settings] on this port group to be overridden on an
individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L249">property vlanId</a>
</h3>

```typescript
public vlanId: pulumi.Output<number>;
```


The VLAN ID for single VLAN mode. 0 denotes no VLAN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L254">property vlanOverrideAllowed</a>
</h3>

```typescript
public vlanOverrideAllowed: pulumi.Output<boolean | undefined>;
```


Allow the [VLAN settings][vlan-settings]
on this port group to be overridden on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L258">property vlanRanges</a>
</h3>

```typescript
public vlanRanges: pulumi.Output<{ ... }[]>;
```


The VLAN ID for single VLAN mode. 0 denotes no VLAN.

<h2 class="pdoc-module-header" id="DistributedVirtualSwitch">
<a class="pdoc-member-name" href="/distributedVirtualSwitch.ts#L29">class DistributedVirtualSwitch</a>
</h2>

The `vsphere_distributed_virtual_switch` resource can be used to manage VMware
Distributed Virtual Switches.

An essential component of a distributed, scalable VMware datacenter, the
vSphere Distributed Virtual Switch (DVS) provides centralized management and
monitoring of the networking configuration of all the hosts that are associated
with the switch. In addition to adding port groups (see the
[`vsphere_distributed_port_group`][distributed-port-group] resource) that can
be used as networks for virtual machines, a DVS can be configured to perform
advanced high availability, traffic shaping, network monitoring, and more.

For an overview on vSphere networking concepts, see [this
page][ref-vsphere-net-concepts]. For more information on vSphere DVS, see [this
page][ref-vsphere-dvs].

[distributed-port-group]: /docs/providers/vsphere/r/distributed_port_group.html
[ref-vsphere-net-concepts]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html
[ref-vsphere-dvs]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-375B45C7-684C-4C51-BA3C-70E48DFABF04.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L469">constructor</a>
</h3>

```typescript
new DistributedVirtualSwitch(name: string, args: DistributedVirtualSwitchArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DistributedVirtualSwitch resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L38">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DistributedVirtualSwitchState): DistributedVirtualSwitch
```


Get an existing DistributedVirtualSwitch resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L48">property activeUplinks</a>
</h3>

```typescript
public activeUplinks: pulumi.Output<string[]>;
```


A list of active uplinks to be used in load
balancing. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L54">property allowForgedTransmits</a>
</h3>

```typescript
public allowForgedTransmits: pulumi.Output<boolean>;
```


Controls whether or not a virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L59">property allowMacChanges</a>
</h3>

```typescript
public allowMacChanges: pulumi.Output<boolean>;
```


Controls whether or not the Media Access
Control (MAC) address can be changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L64">property allowPromiscuous</a>
</h3>

```typescript
public allowPromiscuous: pulumi.Output<boolean>;
```


Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L70">property blockAllPorts</a>
</h3>

```typescript
public blockAllPorts: pulumi.Output<boolean>;
```


Shuts down all ports in the port groups that
this policy applies to, effectively blocking all network access to connected
virtual devices.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L75">property checkBeacon</a>
</h3>

```typescript
public checkBeacon: pulumi.Output<boolean>;
```


Enables beacon probing as an additional measure
to detect NIC failure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L79">property configVersion</a>
</h3>

```typescript
public configVersion: pulumi.Output<string>;
```


The version string of the configuration that this spec is trying to change.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L84">property contactDetail</a>
</h3>

```typescript
public contactDetail: pulumi.Output<string | undefined>;
```


The detailed contact information for the person
who is responsible for the DVS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L89">property contactName</a>
</h3>

```typescript
public contactName: pulumi.Output<string | undefined>;
```


The name of the person who is responsible for the
DVS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L96">property customAttributes</a>
</h3>

```typescript
public customAttributes: pulumi.Output<{ ... } | undefined>;
```


Map of custom attribute ids to attribute
value strings to set for virtual switch. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L101">property datacenterId</a>
</h3>

```typescript
public datacenterId: pulumi.Output<string>;
```


The ID of the datacenter where the distributed
virtual switch will be created. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L105">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A detailed description for the DVS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L110">property directpathGen2Allowed</a>
</h3>

```typescript
public directpathGen2Allowed: pulumi.Output<boolean>;
```


Allow VMDirectPath Gen2 for the ports
for which this policy applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L115">property egressShapingAverageBandwidth</a>
</h3>

```typescript
public egressShapingAverageBandwidth: pulumi.Output<number>;
```


The average bandwidth in bits
per second if egress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L120">property egressShapingBurstSize</a>
</h3>

```typescript
public egressShapingBurstSize: pulumi.Output<number>;
```


The maximum burst size allowed in
bytes if egress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L125">property egressShapingEnabled</a>
</h3>

```typescript
public egressShapingEnabled: pulumi.Output<boolean>;
```


`true` if the traffic shaper is enabled
on the port for egress traffic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L130">property egressShapingPeakBandwidth</a>
</h3>

```typescript
public egressShapingPeakBandwidth: pulumi.Output<number>;
```


The peak bandwidth during bursts
in bits per second if egress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L135">property failback</a>
</h3>

```typescript
public failback: pulumi.Output<boolean>;
```


If `true`, the teaming policy will re-activate failed
uplinks higher in precedence when they come back up.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L139">property faulttoleranceMaximumMbit</a>
</h3>

```typescript
public faulttoleranceMaximumMbit: pulumi.Output<number>;
```


The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L143">property faulttoleranceReservationMbit</a>
</h3>

```typescript
public faulttoleranceReservationMbit: pulumi.Output<number>;
```


The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L147">property faulttoleranceShareCount</a>
</h3>

```typescript
public faulttoleranceShareCount: pulumi.Output<number>;
```


The amount of shares to allocate to the faultTolerance traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L151">property faulttoleranceShareLevel</a>
</h3>

```typescript
public faulttoleranceShareLevel: pulumi.Output<string>;
```


The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L156">property folder</a>
</h3>

```typescript
public folder: pulumi.Output<string | undefined>;
```


The folder to create the DVS in. Forces a new resource
if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L160">property hbrMaximumMbit</a>
</h3>

```typescript
public hbrMaximumMbit: pulumi.Output<number>;
```


The maximum allowed usage for the hbr traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L164">property hbrReservationMbit</a>
</h3>

```typescript
public hbrReservationMbit: pulumi.Output<number>;
```


The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L168">property hbrShareCount</a>
</h3>

```typescript
public hbrShareCount: pulumi.Output<number>;
```


The amount of shares to allocate to the hbr traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L172">property hbrShareLevel</a>
</h3>

```typescript
public hbrShareLevel: pulumi.Output<string>;
```


The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L177">property hosts</a>
</h3>

```typescript
public hosts: pulumi.Output<{ ... }[] | undefined>;
```


Use the `host` block to declare a host specification. The
options are:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L182">property ingressShapingAverageBandwidth</a>
</h3>

```typescript
public ingressShapingAverageBandwidth: pulumi.Output<number>;
```


The average bandwidth in
bits per second if ingress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L187">property ingressShapingBurstSize</a>
</h3>

```typescript
public ingressShapingBurstSize: pulumi.Output<number>;
```


The maximum burst size allowed in
bytes if ingress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L192">property ingressShapingEnabled</a>
</h3>

```typescript
public ingressShapingEnabled: pulumi.Output<boolean>;
```


`true` if the traffic shaper is
enabled on the port for ingress traffic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L197">property ingressShapingPeakBandwidth</a>
</h3>

```typescript
public ingressShapingPeakBandwidth: pulumi.Output<number>;
```


The peak bandwidth during
bursts in bits per second if ingress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L203">property ipv4Address</a>
</h3>

```typescript
public ipv4Address: pulumi.Output<string | undefined>;
```


An IPv4 address to identify the switch. This is
mostly useful when used with the Netflow arguments found
below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L207">property iscsiMaximumMbit</a>
</h3>

```typescript
public iscsiMaximumMbit: pulumi.Output<number>;
```


The maximum allowed usage for the iSCSI traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L211">property iscsiReservationMbit</a>
</h3>

```typescript
public iscsiReservationMbit: pulumi.Output<number>;
```


The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L215">property iscsiShareCount</a>
</h3>

```typescript
public iscsiShareCount: pulumi.Output<number>;
```


The amount of shares to allocate to the iSCSI traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L219">property iscsiShareLevel</a>
</h3>

```typescript
public iscsiShareLevel: pulumi.Output<string>;
```


The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L225">property lacpApiVersion</a>
</h3>

```typescript
public lacpApiVersion: pulumi.Output<string>;
```


The Link Aggregation Control Protocol group
version to use with the switch. Possible values are `singleLag` and
`multipleLag`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L230">property lacpEnabled</a>
</h3>

```typescript
public lacpEnabled: pulumi.Output<boolean>;
```


Enables LACP for the ports that this policy
applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L234">property lacpMode</a>
</h3>

```typescript
public lacpMode: pulumi.Output<string>;
```


The LACP mode. Can be one of `active` or `passive`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L239">property linkDiscoveryOperation</a>
</h3>

```typescript
public linkDiscoveryOperation: pulumi.Output<string | undefined>;
```


Whether to `advertise` or `listen`
for link discovery traffic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L244">property linkDiscoveryProtocol</a>
</h3>

```typescript
public linkDiscoveryProtocol: pulumi.Output<string | undefined>;
```


The discovery protocol type. Valid
types are `cdp` and `lldp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L248">property managementMaximumMbit</a>
</h3>

```typescript
public managementMaximumMbit: pulumi.Output<number>;
```


The maximum allowed usage for the management traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L252">property managementReservationMbit</a>
</h3>

```typescript
public managementReservationMbit: pulumi.Output<number>;
```


The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L256">property managementShareCount</a>
</h3>

```typescript
public managementShareCount: pulumi.Output<number>;
```


The amount of shares to allocate to the management traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L260">property managementShareLevel</a>
</h3>

```typescript
public managementShareLevel: pulumi.Output<string>;
```


The allocation level for the management traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L265">property maxMtu</a>
</h3>

```typescript
public maxMtu: pulumi.Output<number>;
```


The maximum transmission unit (MTU) for the virtual
switch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L270">property multicastFilteringMode</a>
</h3>

```typescript
public multicastFilteringMode: pulumi.Output<string>;
```


The multicast filtering mode to use
with the switch. Can be one of `legacyFiltering` or `snooping`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L274">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the distributed virtual switch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L280">property netflowActiveFlowTimeout</a>
</h3>

```typescript
public netflowActiveFlowTimeout: pulumi.Output<number | undefined>;
```


The number of seconds after which
active flows are forced to be exported to the collector. Allowed range is
`60` to `3600`. Default: `60`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L286">property netflowCollectorIpAddress</a>
</h3>

```typescript
public netflowCollectorIpAddress: pulumi.Output<string | undefined>;
```


IP address for the Netflow
collector, using IPv4 or IPv6. IPv6 is supported in vSphere Distributed
Switch Version 6.0 or later. Must be set before Netflow can be enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L291">property netflowCollectorPort</a>
</h3>

```typescript
public netflowCollectorPort: pulumi.Output<number | undefined>;
```


Port for the Netflow collector. This
must be set before Netflow can be enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L296">property netflowEnabled</a>
</h3>

```typescript
public netflowEnabled: pulumi.Output<boolean>;
```


Enables Netflow on all ports that this policy
applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L302">property netflowIdleFlowTimeout</a>
</h3>

```typescript
public netflowIdleFlowTimeout: pulumi.Output<number | undefined>;
```


The number of seconds after which
idle flows are forced to be exported to the collector. Allowed range is `10`
to `600`. Default: `15`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L308">property netflowInternalFlowsOnly</a>
</h3>

```typescript
public netflowInternalFlowsOnly: pulumi.Output<boolean | undefined>;
```


Whether to limit analysis to
traffic that has both source and destination served by the same host.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L313">property netflowObservationDomainId</a>
</h3>

```typescript
public netflowObservationDomainId: pulumi.Output<number | undefined>;
```


The observation domain ID for
the Netflow collector.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L320">property netflowSamplingRate</a>
</h3>

```typescript
public netflowSamplingRate: pulumi.Output<number | undefined>;
```


The ratio of total number of packets to
the number of packets analyzed. The default is `0`, which indicates that the
switch should analyze all packets. The maximum value is `1000`, which
indicates an analysis rate of 0.001%.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L325">property networkResourceControlEnabled</a>
</h3>

```typescript
public networkResourceControlEnabled: pulumi.Output<boolean | undefined>;
```


Set to `true` to enable
network I/O control. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L330">property networkResourceControlVersion</a>
</h3>

```typescript
public networkResourceControlVersion: pulumi.Output<string>;
```


The version of network I/O
control to use. Can be one of `version2` or `version3`. Default: `version2`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L334">property nfsMaximumMbit</a>
</h3>

```typescript
public nfsMaximumMbit: pulumi.Output<number>;
```


The maximum allowed usage for the nfs traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L338">property nfsReservationMbit</a>
</h3>

```typescript
public nfsReservationMbit: pulumi.Output<number>;
```


The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L342">property nfsShareCount</a>
</h3>

```typescript
public nfsShareCount: pulumi.Output<number>;
```


The amount of shares to allocate to the nfs traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L346">property nfsShareLevel</a>
</h3>

```typescript
public nfsShareLevel: pulumi.Output<string>;
```


The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L351">property notifySwitches</a>
</h3>

```typescript
public notifySwitches: pulumi.Output<boolean>;
```


If `true`, the teaming policy will notify the
broadcast network of an uplink failover, triggering cache updates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L356">property portPrivateSecondaryVlanId</a>
</h3>

```typescript
public portPrivateSecondaryVlanId: pulumi.Output<number>;
```


Used to define a secondary VLAN
ID when using private VLANs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L363">property standbyUplinks</a>
</h3>

```typescript
public standbyUplinks: pulumi.Output<string[]>;
```


A list of standby uplinks to be used in
failover. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L368">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<string[] | undefined>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L374">property teamingPolicy</a>
</h3>

```typescript
public teamingPolicy: pulumi.Output<string>;
```


The uplink teaming policy. Can be one of
`loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L379">property txUplink</a>
</h3>

```typescript
public txUplink: pulumi.Output<boolean>;
```


Forward all traffic transmitted by ports for which
this policy applies to its DVS uplinks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L387">property uplinks</a>
</h3>

```typescript
public uplinks: pulumi.Output<string[]>;
```


A list of strings that uniquely identifies the names
of the uplinks on the DVS across hosts. The number of items in this list
controls the number of uplinks that exist on the DVS, in addition to the
names.  See here for an example on how to
use this option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L391">property vdpMaximumMbit</a>
</h3>

```typescript
public vdpMaximumMbit: pulumi.Output<number>;
```


The maximum allowed usage for the vdp traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L395">property vdpReservationMbit</a>
</h3>

```typescript
public vdpReservationMbit: pulumi.Output<number>;
```


The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L399">property vdpShareCount</a>
</h3>

```typescript
public vdpShareCount: pulumi.Output<number>;
```


The amount of shares to allocate to the vdp traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L403">property vdpShareLevel</a>
</h3>

```typescript
public vdpShareLevel: pulumi.Output<string>;
```


The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L410">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


- The version of the DVS to create. The default is to
create the DVS at the latest version supported by the version of vSphere
being used. A DVS can be upgraded to another version, but cannot be
downgraded.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L414">property virtualmachineMaximumMbit</a>
</h3>

```typescript
public virtualmachineMaximumMbit: pulumi.Output<number>;
```


The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L418">property virtualmachineReservationMbit</a>
</h3>

```typescript
public virtualmachineReservationMbit: pulumi.Output<number>;
```


The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L422">property virtualmachineShareCount</a>
</h3>

```typescript
public virtualmachineShareCount: pulumi.Output<number>;
```


The amount of shares to allocate to the virtualMachine traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L426">property virtualmachineShareLevel</a>
</h3>

```typescript
public virtualmachineShareLevel: pulumi.Output<string>;
```


The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L430">property vlanId</a>
</h3>

```typescript
public vlanId: pulumi.Output<number>;
```


The VLAN ID for single VLAN mode. 0 denotes no VLAN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L437">property vlanRanges</a>
</h3>

```typescript
public vlanRanges: pulumi.Output<{ ... }[]>;
```


Used to denote VLAN trunking. Use the `min_vlan`
and `max_vlan` sub-arguments to define the tagged VLAN range. Multiple
`vlan_range` definitions are allowed, but they must not overlap. Example
below:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L441">property vmotionMaximumMbit</a>
</h3>

```typescript
public vmotionMaximumMbit: pulumi.Output<number>;
```


The maximum allowed usage for the vmotion traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L445">property vmotionReservationMbit</a>
</h3>

```typescript
public vmotionReservationMbit: pulumi.Output<number>;
```


The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L449">property vmotionShareCount</a>
</h3>

```typescript
public vmotionShareCount: pulumi.Output<number>;
```


The amount of shares to allocate to the vmotion traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L453">property vmotionShareLevel</a>
</h3>

```typescript
public vmotionShareLevel: pulumi.Output<string>;
```


The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L457">property vsanMaximumMbit</a>
</h3>

```typescript
public vsanMaximumMbit: pulumi.Output<number>;
```


The maximum allowed usage for the vsan traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L461">property vsanReservationMbit</a>
</h3>

```typescript
public vsanReservationMbit: pulumi.Output<number>;
```


The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L465">property vsanShareCount</a>
</h3>

```typescript
public vsanShareCount: pulumi.Output<number>;
```


The amount of shares to allocate to the vsan traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L469">property vsanShareLevel</a>
</h3>

```typescript
public vsanShareLevel: pulumi.Output<string>;
```


The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom.

<h2 class="pdoc-module-header" id="DpmHostOverride">
<a class="pdoc-member-name" href="/dpmHostOverride.ts#L22">class DpmHostOverride</a>
</h2>

The `vsphere_dpm_host_override` resource can be used to add a DPM override to a
cluster for a particular host. This allows you to control the power management
settings for individual hosts in the cluster while leaving any unspecified ones
at the default power management settings.

For more information on DPM within vSphere clusters, see [this
page][ref-vsphere-cluster-dpm].

[ref-vsphere-cluster-dpm]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-5E5E349A-4644-4C9C-B434-1C0243EBDC80.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dpmHostOverride.ts#L55">constructor</a>
</h3>

```typescript
new DpmHostOverride(name: string, args: DpmHostOverrideArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DpmHostOverride resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dpmHostOverride.ts#L31">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DpmHostOverrideState): DpmHostOverride
```


Get an existing DpmHostOverride resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dpmHostOverride.ts#L40">property computeClusterId</a>
</h3>

```typescript
public computeClusterId: pulumi.Output<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dpmHostOverride.ts#L46">property dpmAutomationLevel</a>
</h3>

```typescript
public dpmAutomationLevel: pulumi.Output<string | undefined>;
```


The automation level for host power
operations on this host. Can be one of `manual` or `automated`. Default:
`manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dpmHostOverride.ts#L51">property dpmEnabled</a>
</h3>

```typescript
public dpmEnabled: pulumi.Output<boolean | undefined>;
```


Enable DPM support for this host. Default:
`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dpmHostOverride.ts#L55">property hostSystemId</a>
</h3>

```typescript
public hostSystemId: pulumi.Output<string>;
```


The managed object ID of the host.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DrsVmOverride">
<a class="pdoc-member-name" href="/drsVmOverride.ts#L22">class DrsVmOverride</a>
</h2>

The `vsphere_drs_vm_override` resource can be used to add a DRS override to a
cluster for a specific virtual machine. With this resource, one can enable or
disable DRS and control the automation level for a single virtual machine
without affecting the rest of the cluster.

For more information on vSphere clusters and DRS, see [this
page][ref-vsphere-drs-clusters].

[ref-vsphere-drs-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-8ACF3502-5314-469F-8CC9-4A9BD5925BC2.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/drsVmOverride.ts#L56">constructor</a>
</h3>

```typescript
new DrsVmOverride(name: string, args: DrsVmOverrideArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DrsVmOverride resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/drsVmOverride.ts#L31">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DrsVmOverrideState): DrsVmOverride
```


Get an existing DrsVmOverride resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/drsVmOverride.ts#L40">property computeClusterId</a>
</h3>

```typescript
public computeClusterId: pulumi.Output<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/drsVmOverride.ts#L46">property drsAutomationLevel</a>
</h3>

```typescript
public drsAutomationLevel: pulumi.Output<string | undefined>;
```


Overrides the automation level for this virtual
machine in the cluster. Can be one of `manual`, `partiallyAutomated`, or
`fullyAutomated`. Default: `manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/drsVmOverride.ts#L51">property drsEnabled</a>
</h3>

```typescript
public drsEnabled: pulumi.Output<boolean | undefined>;
```


Overrides the default DRS setting for this virtual
machine. Can be either `true` or `false`. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/drsVmOverride.ts#L56">property virtualMachineId</a>
</h3>

```typescript
public virtualMachineId: pulumi.Output<string>;
```


The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.

<h2 class="pdoc-module-header" id="File">
<a class="pdoc-member-name" href="/file.ts#L20">class File</a>
</h2>

The `vsphere_file` resource can be used to upload files (such as virtual disk
files) from the host machine that Terraform is running on to a target
datastore.  The resource can also be used to copy files between datastores, or
from one location to another on the same datastore.

Updates to destination parameters such as `datacenter`, `datastore`, or
`destination_file` will move the managed file a new destination based on the
values of the new settings.  If any source parameter is changed, such as
`source_datastore`, `source_datacenter` or `source_file`), the resource will be
re-created. Depending on if destination parameters are being changed as well,
this may result in the destination file either being overwritten or deleted at
the old location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L68">constructor</a>
</h3>

```typescript
new File(name: string, args: FileArgs, opts?: pulumi.CustomResourceOptions)
```


Create a File resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L29">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FileState): File
```


Get an existing File resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L37">property createDirectories</a>
</h3>

```typescript
public createDirectories: pulumi.Output<boolean | undefined>;
```


Create directories in `destination_file`
path parameter if any missing for copy operation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L42">property datacenter</a>
</h3>

```typescript
public datacenter: pulumi.Output<string | undefined>;
```


The name of a datacenter in which the file will be
uploaded to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L47">property datastore</a>
</h3>

```typescript
public datastore: pulumi.Output<string>;
```


The name of the datastore in which to upload the
file to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L52">property destinationFile</a>
</h3>

```typescript
public destinationFile: pulumi.Output<string>;
```


The path to where the file should be uploaded
or copied to on vSphere.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L57">property sourceDatacenter</a>
</h3>

```typescript
public sourceDatacenter: pulumi.Output<string | undefined>;
```


The name of a datacenter in which the file
will be copied from. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L62">property sourceDatastore</a>
</h3>

```typescript
public sourceDatastore: pulumi.Output<string | undefined>;
```


The name of the datastore in which file will
be copied from. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L68">property sourceFile</a>
</h3>

```typescript
public sourceFile: pulumi.Output<string>;
```


The path to the file being uploaded from the
Terraform host to vSphere or copied within vSphere. Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Folder">
<a class="pdoc-member-name" href="/folder.ts#L17">class Folder</a>
</h2>

The `vsphere_folder` resource can be used to manage vSphere inventory folders.
The resource supports creating folders of the 5 major types - datacenter
folders, host and cluster folders, virtual machine folders, datastore folders,
and network folders.

Paths are always relative to the specific type of folder you are creating.
Subfolders are discovered by parsing the relative path specified in `path`, so
`foo/bar` will create a folder named `bar` in the parent folder `foo`, as long
as that folder exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/folder.ts#L62">constructor</a>
</h3>

```typescript
new Folder(name: string, args: FolderArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Folder resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/folder.ts#L26">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FolderState): Folder
```


Get an existing Folder resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/folder.ts#L35">property customAttributes</a>
</h3>

```typescript
public customAttributes: pulumi.Output<{ ... } | undefined>;
```


Map of custom attribute ids to attribute
value strings to set for folder. See [here][docs-setting-custom-attributes]
for a reference on how to set values for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/folder.ts#L41">property datacenterId</a>
</h3>

```typescript
public datacenterId: pulumi.Output<string | undefined>;
```


The ID of the datacenter the folder will be created in.
Required for all folder types except for datacenter folders. Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/folder.ts#L50">property path</a>
</h3>

```typescript
public path: pulumi.Output<string>;
```


The path of the folder to be created. This is relative to
the root of the type of folder you are creating, and the supplied datacenter.
For example, given a default datacenter of `default-dc`, a folder of type
`vm` (denoting a virtual machine folder), and a supplied folder of
`terraform-test-folder`, the resulting path would be
`/default-dc/vm/terraform-test-folder`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/folder.ts#L55">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<string[] | undefined>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/folder.ts#L62">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of folder to create. Allowed options are
`datacenter` for datacenter folders, `host` for host and cluster folders,
`vm` for virtual machine folders, `datastore` for datastore folders, and
`network` for network folders. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="HaVmOverride">
<a class="pdoc-member-name" href="/haVmOverride.ts#L20">class HaVmOverride</a>
</h2>

The `vsphere_ha_vm_override` resource can be used to add an override for
vSphere HA settings on a cluster for a specific virtual machine. With this
resource, one can control specific HA settings so that they are different than
the cluster default, accommodating the needs of that specific virtual machine,
while not affecting the rest of the cluster.

For more information on vSphere HA, see [this page][ref-vsphere-ha-clusters].

[ref-vsphere-ha-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.avail.doc/GUID-5432CA24-14F1-44E3-87FB-61D937831CF6.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L136">constructor</a>
</h3>

```typescript
new HaVmOverride(name: string, args: HaVmOverrideArgs, opts?: pulumi.CustomResourceOptions)
```


Create a HaVmOverride resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L29">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HaVmOverrideState): HaVmOverride
```


Get an existing HaVmOverride resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L38">property computeClusterId</a>
</h3>

```typescript
public computeClusterId: pulumi.Output<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L46">property haDatastoreApdRecoveryAction</a>
</h3>

```typescript
public haDatastoreApdRecoveryAction: pulumi.Output<string | undefined>;
```


Controls the action to take
on this virtual machine if an APD status on an affected datastore clears in
the middle of an APD event. Can be one of `useClusterDefault`, `none` or
`reset`.  Default: `useClusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L54">property haDatastoreApdResponse</a>
</h3>

```typescript
public haDatastoreApdResponse: pulumi.Output<string | undefined>;
```


Controls the action to take on this
virtual machine when the cluster has detected loss to all paths to a relevant
datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
`restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L62">property haDatastoreApdResponseDelay</a>
</h3>

```typescript
public haDatastoreApdResponseDelay: pulumi.Output<number | undefined>;
```


Controls the delay in minutes
to wait after an APD timeout event to execute the response action defined in
`ha_datastore_apd_response`. Use `-1` to use
the cluster default. Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L70">property haDatastorePdlResponse</a>
</h3>

```typescript
public haDatastorePdlResponse: pulumi.Output<string | undefined>;
```


Controls the action to take on this
virtual machine when the cluster has detected a permanent device loss to a
relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
`restartAggressive`. Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L77">property haHostIsolationResponse</a>
</h3>

```typescript
public haHostIsolationResponse: pulumi.Output<string | undefined>;
```


The action to take on this virtual
machine when a host has detected that it has been isolated from the rest of
the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
`shutdown`. Default: `clusterIsolationResponse`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L83">property haVmFailureInterval</a>
</h3>

```typescript
public haVmFailureInterval: pulumi.Output<number | undefined>;
```


If a heartbeat from this virtual
machine is not received within this configured interval, the virtual machine
is marked as failed. The value is in seconds. Default: `30`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L92">property haVmMaximumFailureWindow</a>
</h3>

```typescript
public haVmMaximumFailureWindow: pulumi.Output<number | undefined>;
```


The length of the reset window in
which `ha_vm_maximum_resets` can operate. When this
window expires, no more resets are attempted regardless of the setting
configured in `ha_vm_maximum_resets`. `-1` means no window, meaning an
unlimited reset time is allotted. The value is specified in seconds. Default:
`-1` (no window).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L98">property haVmMaximumResets</a>
</h3>

```typescript
public haVmMaximumResets: pulumi.Output<number | undefined>;
```


The maximum number of resets that HA will
perform to this virtual machine when responding to a failure event. Default:
`3`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L104">property haVmMinimumUptime</a>
</h3>

```typescript
public haVmMinimumUptime: pulumi.Output<number | undefined>;
```


The time, in seconds, that HA waits after
powering on this virtual machine before monitoring for heartbeats. Default:
`120` (2 minutes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L110">property haVmMonitoring</a>
</h3>

```typescript
public haVmMonitoring: pulumi.Output<string | undefined>;
```


The type of virtual machine monitoring to use
when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
`vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L117">property haVmMonitoringUseClusterDefaults</a>
</h3>

```typescript
public haVmMonitoringUseClusterDefaults: pulumi.Output<boolean | undefined>;
```


Determines whether or
not the cluster's default settings or the VM override settings specified in
this resource are used for virtual machine monitoring. The default is `true`
(use cluster defaults) - set to `false` to have overrides take effect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L124">property haVmRestartPriority</a>
</h3>

```typescript
public haVmRestartPriority: pulumi.Output<string | undefined>;
```


The restart priority for the virtual
machine when vSphere detects a host failure. Can be one of
`clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
Default: `clusterRestartPriority`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L131">property haVmRestartTimeout</a>
</h3>

```typescript
public haVmRestartTimeout: pulumi.Output<number | undefined>;
```


The maximum time, in seconds, that
vSphere HA will wait for this virtual machine to be ready. Use `-1` to
specify the cluster default.  Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L136">property virtualMachineId</a>
</h3>

```typescript
public virtualMachineId: pulumi.Output<string>;
```


The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.

<h2 class="pdoc-module-header" id="HostPortGroup">
<a class="pdoc-member-name" href="/hostPortGroup.ts#L17">class HostPortGroup</a>
</h2>

The `vsphere_host_port_group` resource can be used to manage vSphere standard
port groups on an ESXi host. These port groups are connected to standard
virtual switches, which can be managed by the
[`vsphere_host_virtual_switch`][host-virtual-switch] resource.

For an overview on vSphere networking concepts, see [this page][ref-vsphere-net-concepts].

[host-virtual-switch]: /docs/providers/vsphere/r/host_virtual_switch.html
[ref-vsphere-net-concepts]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L120">constructor</a>
</h3>

```typescript
new HostPortGroup(name: string, args: HostPortGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a HostPortGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L26">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HostPortGroupState): HostPortGroup
```


Get an existing HostPortGroup resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L33">property activeNics</a>
</h3>

```typescript
public activeNics: pulumi.Output<string[] | undefined>;
```


List of active network adapters used for load balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L38">property allowForgedTransmits</a>
</h3>

```typescript
public allowForgedTransmits: pulumi.Output<boolean | undefined>;
```


Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address
than that of its own.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L42">property allowMacChanges</a>
</h3>

```typescript
public allowMacChanges: pulumi.Output<boolean | undefined>;
```


Controls whether or not the Media Access Control (MAC) address can be changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L46">property allowPromiscuous</a>
</h3>

```typescript
public allowPromiscuous: pulumi.Output<boolean | undefined>;
```


Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L51">property checkBeacon</a>
</h3>

```typescript
public checkBeacon: pulumi.Output<boolean | undefined>;
```


Enable beacon probing. Requires that the vSwitch has been configured to use a beacon. If disabled, link status is
used only.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L57">property computedPolicy</a>
</h3>

```typescript
public computedPolicy: pulumi.Output<{ ... }>;
```


A map with a full set of the [policy
options][host-vswitch-policy-options] computed from defaults and overrides,
explaining the effective policy for this port group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L61">property failback</a>
</h3>

```typescript
public failback: pulumi.Output<boolean | undefined>;
```


If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L66">property hostSystemId</a>
</h3>

```typescript
public hostSystemId: pulumi.Output<string>;
```


The [managed object ID][docs-about-morefs] of
the host to set the port group up on. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L70">property key</a>
</h3>

```typescript
public key: pulumi.Output<string>;
```


The key for this port group as returned from the vSphere API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L75">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the port group.  Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L79">property notifySwitches</a>
</h3>

```typescript
public notifySwitches: pulumi.Output<boolean | undefined>;
```


If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L83">property ports</a>
</h3>

```typescript
public ports: pulumi.Output<{ ... }>;
```


A list of ports that currently exist and are used on this port group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L87">property shapingAverageBandwidth</a>
</h3>

```typescript
public shapingAverageBandwidth: pulumi.Output<number | undefined>;
```


The average bandwidth in bits per second if traffic shaping is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L91">property shapingBurstSize</a>
</h3>

```typescript
public shapingBurstSize: pulumi.Output<number | undefined>;
```


The maximum burst size allowed in bytes if traffic shaping is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L95">property shapingEnabled</a>
</h3>

```typescript
public shapingEnabled: pulumi.Output<boolean | undefined>;
```


Enable traffic shaping on this virtual switch or port group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L99">property shapingPeakBandwidth</a>
</h3>

```typescript
public shapingPeakBandwidth: pulumi.Output<number | undefined>;
```


The peak bandwidth during bursts in bits per second if traffic shaping is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L103">property standbyNics</a>
</h3>

```typescript
public standbyNics: pulumi.Output<string[] | undefined>;
```


List of standby network adapters used for failover.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L108">property teamingPolicy</a>
</h3>

```typescript
public teamingPolicy: pulumi.Output<string | undefined>;
```


The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, or
failover_explicit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L113">property virtualSwitchName</a>
</h3>

```typescript
public virtualSwitchName: pulumi.Output<string>;
```


The name of the virtual switch to bind
this port group to. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L120">property vlanId</a>
</h3>

```typescript
public vlanId: pulumi.Output<number | undefined>;
```


The VLAN ID/trunk mode for this port group.  An ID of
`0` denotes no tagging, an ID of `1`-`4094` tags with the specific ID, and an
ID of `4095` enables trunk mode, allowing the guest to manage its own
tagging. Default: `0`.

<h2 class="pdoc-module-header" id="HostVirtualSwitch">
<a class="pdoc-member-name" href="/hostVirtualSwitch.ts#L18">class HostVirtualSwitch</a>
</h2>

The `vsphere_host_virtual_switch` resource can be used to manage vSphere
standard switches on an ESXi host. These switches can be used as a backing for
standard port groups, which can be managed by the
[`vsphere_host_port_group`][host-port-group] resource.

For an overview on vSphere networking concepts, see [this
page][ref-vsphere-net-concepts].

[host-port-group]: /docs/providers/vsphere/r/host_port_group.html
[ref-vsphere-net-concepts]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L142">constructor</a>
</h3>

```typescript
new HostVirtualSwitch(name: string, args: HostVirtualSwitchArgs, opts?: pulumi.CustomResourceOptions)
```


Create a HostVirtualSwitch resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L27">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HostVirtualSwitchState): HostVirtualSwitch
```


Get an existing HostVirtualSwitch resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L35">property activeNics</a>
</h3>

```typescript
public activeNics: pulumi.Output<string[]>;
```


The list of active network adapters used for load
balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L41">property allowForgedTransmits</a>
</h3>

```typescript
public allowForgedTransmits: pulumi.Output<boolean | undefined>;
```


Controls whether or not the virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L46">property allowMacChanges</a>
</h3>

```typescript
public allowMacChanges: pulumi.Output<boolean | undefined>;
```


Controls whether or not the Media Access
Control (MAC) address can be changed. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L52">property allowPromiscuous</a>
</h3>

```typescript
public allowPromiscuous: pulumi.Output<boolean | undefined>;
```


Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port. Default:
`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L58">property beaconInterval</a>
</h3>

```typescript
public beaconInterval: pulumi.Output<number | undefined>;
```


The interval, in seconds, that a NIC beacon
packet is sent out. This can be used with `check_beacon` to
offer link failure capability beyond link status only. Default: `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L65">property checkBeacon</a>
</h3>

```typescript
public checkBeacon: pulumi.Output<boolean | undefined>;
```


Enable beacon probing - this requires that the
`beacon_interval` option has been set in the bridge
options. If this is set to `false`, only link status is used to check for
failed NICs.  Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L71">property failback</a>
</h3>

```typescript
public failback: pulumi.Output<boolean | undefined>;
```


If set to `true`, the teaming policy will re-activate
failed interfaces higher in precedence when they come back up.  Default:
`true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L76">property hostSystemId</a>
</h3>

```typescript
public hostSystemId: pulumi.Output<string>;
```


The [managed object ID][docs-about-morefs] of
the host to set the virtual switch up on. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L81">property linkDiscoveryOperation</a>
</h3>

```typescript
public linkDiscoveryOperation: pulumi.Output<string | undefined>;
```


Whether to `advertise` or `listen`
for link discovery traffic. Default: `listen`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L86">property linkDiscoveryProtocol</a>
</h3>

```typescript
public linkDiscoveryProtocol: pulumi.Output<string | undefined>;
```


The discovery protocol type.  Valid
types are `cpd` and `lldp`. Default: `cdp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L91">property mtu</a>
</h3>

```typescript
public mtu: pulumi.Output<number | undefined>;
```


The maximum transmission unit (MTU) for the virtual
switch. Default: `1500`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L96">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the virtual switch. Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L100">property networkAdapters</a>
</h3>

```typescript
public networkAdapters: pulumi.Output<string[]>;
```


The network interfaces to bind to the bridge.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L106">property notifySwitches</a>
</h3>

```typescript
public notifySwitches: pulumi.Output<boolean | undefined>;
```


If set to `true`, the teaming policy will
notify the broadcast network of a NIC failover, triggering cache updates.
Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L111">property numberOfPorts</a>
</h3>

```typescript
public numberOfPorts: pulumi.Output<number | undefined>;
```


The number of ports to create with this
virtual switch. Default: `128`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L116">property shapingAverageBandwidth</a>
</h3>

```typescript
public shapingAverageBandwidth: pulumi.Output<number | undefined>;
```


The average bandwidth in bits per
second if traffic shaping is enabled. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L121">property shapingBurstSize</a>
</h3>

```typescript
public shapingBurstSize: pulumi.Output<number | undefined>;
```


The maximum burst size allowed in bytes if
shaping is enabled. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L126">property shapingEnabled</a>
</h3>

```typescript
public shapingEnabled: pulumi.Output<boolean | undefined>;
```


Set to `true` to enable the traffic shaper for
ports managed by this virtual switch. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L131">property shapingPeakBandwidth</a>
</h3>

```typescript
public shapingPeakBandwidth: pulumi.Output<number | undefined>;
```


The peak bandwidth during bursts in
bits per second if traffic shaping is enabled. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L136">property standbyNics</a>
</h3>

```typescript
public standbyNics: pulumi.Output<string[]>;
```


The list of standby network adapters used for
failover.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L142">property teamingPolicy</a>
</h3>

```typescript
public teamingPolicy: pulumi.Output<string | undefined>;
```


The network adapter teaming policy. Can be one
of `loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`. Default: `loadbalance_srcid`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="License">
<a class="pdoc-member-name" href="/license.ts#L9">class License</a>
</h2>

Provides a VMware vSphere license resource. This can be used to add and remove license keys.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/license.ts#L45">constructor</a>
</h3>

```typescript
new License(name: string, args: LicenseArgs, opts?: pulumi.CustomResourceOptions)
```


Create a License resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/license.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LicenseState): License
```


Get an existing License resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/license.ts#L25">property editionKey</a>
</h3>

```typescript
public editionKey: pulumi.Output<string>;
```


The product edition of the license key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/license.ts#L29">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


A map of key/value pairs to be attached as labels (tags) to the license key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/license.ts#L33">property licenseKey</a>
</h3>

```typescript
public licenseKey: pulumi.Output<string>;
```


The license key to add.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/license.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The display name for the license.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/license.ts#L41">property total</a>
</h3>

```typescript
public total: pulumi.Output<number>;
```


Total number of units (example: CPUs) contained in the license.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/license.ts#L45">property used</a>
</h3>

```typescript
public used: pulumi.Output<number>;
```


The number of units (example: CPUs) assigned to this license.

<h2 class="pdoc-module-header" id="NasDatastore">
<a class="pdoc-member-name" href="/nasDatastore.ts#L18">class NasDatastore</a>
</h2>

The `vsphere_nas_datastore` resource can be used to create and manage NAS
datastores on an ESXi host or a set of hosts. The resource supports mounting
NFS v3 and v4.1 shares to be used as datastores.

~> **NOTE:** Unlike [`vsphere_vmfs_datastore`][resource-vmfs-datastore], a NAS
datastore is only mounted on the hosts you choose to mount it on. To mount on
multiple hosts, you must specify each host that you want to add in the
`host_system_ids` argument.

[resource-vmfs-datastore]: /docs/providers/vsphere/r/vmfs_datastore.html

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L134">constructor</a>
</h3>

```typescript
new NasDatastore(name: string, args: NasDatastoreArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NasDatastore resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L27">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NasDatastoreState): NasDatastore
```


Get an existing NasDatastore resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L37">property accessMode</a>
</h3>

```typescript
public accessMode: pulumi.Output<string | undefined>;
```


Access mode for the mount point. Can be one of
`readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
that the datastore will be read-write depending on the permissions of the
actual share. Default: `readWrite`. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L42">property accessible</a>
</h3>

```typescript
public accessible: pulumi.Output<boolean>;
```


The connectivity status of the datastore. If this is `false`,
some other computed attributes may be out of date.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L46">property capacity</a>
</h3>

```typescript
public capacity: pulumi.Output<number>;
```


Maximum capacity of the datastore, in megabytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L53">property customAttributes</a>
</h3>

```typescript
public customAttributes: pulumi.Output<{ ... } | undefined>;
```


Map of custom attribute ids to attribute
value strings to set on datasource resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L59">property datastoreClusterId</a>
</h3>

```typescript
public datastoreClusterId: pulumi.Output<string | undefined>;
```


The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L69">property folder</a>
</h3>

```typescript
public folder: pulumi.Output<string | undefined>;
```


The relative path to a folder to put this datastore in.
This is a path relative to the datacenter you are deploying the datastore to.
Example: for the `dc1` datacenter, and a provided `folder` of `foo/bar`,
Terraform will place a datastore named `terraform-test` in a datastore folder
located at `/dc1/datastore/foo/bar`, with the final inventory path being
`/dc1/datastore/foo/bar/terraform-test`. Conflicts with
`datastore_cluster_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L73">property freeSpace</a>
</h3>

```typescript
public freeSpace: pulumi.Output<number>;
```


Available space of this datastore, in megabytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L78">property hostSystemIds</a>
</h3>

```typescript
public hostSystemIds: pulumi.Output<string[]>;
```


The [managed object IDs][docs-about-morefs] of
the hosts to mount the datastore on.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L82">property maintenanceMode</a>
</h3>

```typescript
public maintenanceMode: pulumi.Output<string>;
```


The current maintenance mode state of the datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L87">property multipleHostAccess</a>
</h3>

```typescript
public multipleHostAccess: pulumi.Output<boolean>;
```


If `true`, more than one host in the datacenter has
been configured with access to the datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L92">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the datastore. Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L97">property protocolEndpoint</a>
</h3>

```typescript
public protocolEndpoint: pulumi.Output<string>;
```


Indicates that this NAS volume is a protocol endpoint.
This field is only populated if the host supports virtual datastores.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L103">property remoteHosts</a>
</h3>

```typescript
public remoteHosts: pulumi.Output<string[]>;
```


The hostnames or IP addresses of the remote
server or servers. Only one element should be present for NFS v3 but multiple
can be present for NFS v4.1. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L108">property remotePath</a>
</h3>

```typescript
public remotePath: pulumi.Output<string>;
```


The remote path of the mount point. Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L114">property securityType</a>
</h3>

```typescript
public securityType: pulumi.Output<string | undefined>;
```


The security type to use when using NFS v4.1.
Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L119">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<string[] | undefined>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L125">property type</a>
</h3>

```typescript
public type: pulumi.Output<string | undefined>;
```


The type of NAS volume. Can be one of `NFS` (to denote
v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L130">property uncommittedSpace</a>
</h3>

```typescript
public uncommittedSpace: pulumi.Output<number>;
```


Total additional storage space, in megabytes,
potentially used by all virtual machines on this datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L134">property url</a>
</h3>

```typescript
public url: pulumi.Output<string>;
```


The unique locator for the datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Provider">
<a class="pdoc-member-name" href="/provider.ts#L9">class Provider</a>
</h2>

The provider type for the vsphere package

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L9">constructor</a>
</h3>

```typescript
new Provider(name: string, args: ProviderArgs, opts?: pulumi.ResourceOptions)
```


Create a Provider resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ResourcePool">
<a class="pdoc-member-name" href="/resourcePool.ts#L15">class ResourcePool</a>
</h2>

The `vsphere_resource_pool` resource can be used to create and manage
resource pools in standalone hosts or on compute clusters.

For more information on vSphere resource pools, see [this
page][ref-vsphere-resource_pools].

[ref-vsphere-resource_pools]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-60077B40-66FF-4625-934A-641703ED7601.html

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L110">constructor</a>
</h3>

```typescript
new ResourcePool(name: string, args: ResourcePoolArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ResourcePool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ResourcePoolState): ResourcePool
```


Get an existing ResourcePool resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L33">property cpuExpandable</a>
</h3>

```typescript
public cpuExpandable: pulumi.Output<boolean | undefined>;
```


Determines if the reservation on a resource
pool can grow beyond the specified value if the parent resource pool has
unreserved resources. Default: `true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L39">property cpuLimit</a>
</h3>

```typescript
public cpuLimit: pulumi.Output<number | undefined>;
```


The CPU utilization of a resource pool will not exceed
this limit, even if there are available resources. Set to `-1` for unlimited.
Default: `-1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L44">property cpuReservation</a>
</h3>

```typescript
public cpuReservation: pulumi.Output<number | undefined>;
```


Amount of CPU (MHz) that is guaranteed
available to the resource pool. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L52">property cpuShareLevel</a>
</h3>

```typescript
public cpuShareLevel: pulumi.Output<string | undefined>;
```


The CPU allocation level. The level is a
simplified view of shares. Levels map to a pre-determined set of numeric
values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
`low`, `normal`, or `high` are specified values in `cpu_shares` will be
ignored.  Default: `normal`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L58">property cpuShares</a>
</h3>

```typescript
public cpuShares: pulumi.Output<number>;
```


The number of shares allocated for CPU. Used to
determine resource allocation in case of resource contention. If this is set,
`cpu_share_level` must be `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L62">property customAttributes</a>
</h3>

```typescript
public customAttributes: pulumi.Output<{ ... } | undefined>;
```


A list of custom attributes to set on this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L68">property memoryExpandable</a>
</h3>

```typescript
public memoryExpandable: pulumi.Output<boolean | undefined>;
```


Determines if the reservation on a resource
pool can grow beyond the specified value if the parent resource pool has
unreserved resources. Default: `true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L74">property memoryLimit</a>
</h3>

```typescript
public memoryLimit: pulumi.Output<number | undefined>;
```


The CPU utilization of a resource pool will not exceed
this limit, even if there are available resources. Set to `-1` for unlimited.
Default: `-1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L79">property memoryReservation</a>
</h3>

```typescript
public memoryReservation: pulumi.Output<number | undefined>;
```


Amount of CPU (MHz) that is guaranteed
available to the resource pool. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L87">property memoryShareLevel</a>
</h3>

```typescript
public memoryShareLevel: pulumi.Output<string | undefined>;
```


The CPU allocation level. The level is a
simplified view of shares. Levels map to a pre-determined set of numeric
values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
`low`, `normal`, or `high` are specified values in `memory_shares` will be
ignored.  Default: `normal`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L93">property memoryShares</a>
</h3>

```typescript
public memoryShares: pulumi.Output<number>;
```


The number of shares allocated for CPU. Used to
determine resource allocation in case of resource contention. If this is set,
`memory_share_level` must be `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L97">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the resource pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L105">property parentResourcePoolId</a>
</h3>

```typescript
public parentResourcePoolId: pulumi.Output<string>;
```


The [managed object ID][docs-about-morefs]
of the parent resource pool. This can be the root resource pool for a cluster
or standalone host, or a resource pool itself. When moving a resource pool
from one parent resource pool to another, both must share a common root
resource pool or the move will fail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L110">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<string[] | undefined>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="StorageDrsVmOverride">
<a class="pdoc-member-name" href="/storageDrsVmOverride.ts#L18">class StorageDrsVmOverride</a>
</h2>

The `vsphere_storage_drs_vm_override` resource can be used to add a Storage DRS
override to a datastore cluster for a specific virtual machine. With this
resource, one can enable or disable Storage DRS, and control the automation
level and disk affinity for a single virtual machine without affecting the rest
of the datastore cluster.

For more information on vSphere datastore clusters and Storage DRS, see [this
page][ref-vsphere-datastore-clusters].

[ref-vsphere-datastore-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-598DF695-107E-406B-9C95-0AF961FC227A.html

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageDrsVmOverride.ts#L62">constructor</a>
</h3>

```typescript
new StorageDrsVmOverride(name: string, args: StorageDrsVmOverrideArgs, opts?: pulumi.CustomResourceOptions)
```


Create a StorageDrsVmOverride resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageDrsVmOverride.ts#L27">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StorageDrsVmOverrideState): StorageDrsVmOverride
```


Get an existing StorageDrsVmOverride resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageDrsVmOverride.ts#L36">property datastoreClusterId</a>
</h3>

```typescript
public datastoreClusterId: pulumi.Output<string>;
```


The [managed object reference
ID][docs-about-morefs] of the datastore cluster to put the override in.
Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageDrsVmOverride.ts#L43">property sdrsAutomationLevel</a>
</h3>

```typescript
public sdrsAutomationLevel: pulumi.Output<string | undefined>;
```


Overrides any Storage DRS automation
levels for this virtual machine. Can be one of `automated` or `manual`. When
not specified, the datastore cluster's settings are used according to the
[specific SDRS subsystem][tf-vsphere-datastore-cluster-sdrs-levels].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageDrsVmOverride.ts#L49">property sdrsEnabled</a>
</h3>

```typescript
public sdrsEnabled: pulumi.Output<string | undefined>;
```


Overrides the default Storage DRS setting for
this virtual machine. When not specified, the datastore cluster setting is
used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageDrsVmOverride.ts#L57">property sdrsIntraVmAffinity</a>
</h3>

```typescript
public sdrsIntraVmAffinity: pulumi.Output<string | undefined>;
```


Overrides the intra-VM affinity setting
for this virtual machine. When `true`, all disks for this virtual machine
will be kept on the same datastore. When `false`, Storage DRS may locate
individual disks on different datastores if it helps satisfy cluster
requirements. When not specified, the datastore cluster's settings are used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageDrsVmOverride.ts#L62">property virtualMachineId</a>
</h3>

```typescript
public virtualMachineId: pulumi.Output<string>;
```


The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.

<h2 class="pdoc-module-header" id="Tag">
<a class="pdoc-member-name" href="/tag.ts#L18">class Tag</a>
</h2>

The `vsphere_tag` resource can be used to create and manage tags, which allow
you to attach metadata to objects in the vSphere inventory to make these
objects more sortable and searchable.

For more information about tags, click [here][ext-tags-general].

[ext-tags-general]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vcenterhost.doc/GUID-E8E854DD-AA97-4E0C-8419-CE84F93C4058.html

~> **NOTE:** Tagging support is unsupported on direct ESXi connections and
requires vCenter 6.0 or higher.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tag.ts#L44">constructor</a>
</h3>

```typescript
new Tag(name: string, args: TagArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Tag resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tag.ts#L27">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TagState): Tag
```


Get an existing Tag resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tag.ts#L35">property categoryId</a>
</h3>

```typescript
public categoryId: pulumi.Output<string>;
```


The unique identifier of the parent category in
which this tag will be created. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tag.ts#L39">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description for the tag.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tag.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The display name of the tag. The name must be unique
within its category.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TagCategory">
<a class="pdoc-member-name" href="/tagCategory.ts#L21">class TagCategory</a>
</h2>

The `vsphere_tag_category` resource can be used to create and manage tag
categories, which determine how tags are grouped together and applied to
specific objects.

For more information about tags, click [here][ext-tags-general]. For more
information about tag categories specifically, click
[here][ext-tag-categories].

[ext-tags-general]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vcenterhost.doc/GUID-E8E854DD-AA97-4E0C-8419-CE84F93C4058.html
[ext-tag-categories]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vcenterhost.doc/GUID-BA3D1794-28F2-43F3-BCE9-3964CB207FB6.html

~> **NOTE:** Tagging support is unsupported on direct ESXi connections and
requires vCenter 6.0 or higher.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tagCategory.ts#L54">constructor</a>
</h3>

```typescript
new TagCategory(name: string, args: TagCategoryArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TagCategory resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tagCategory.ts#L30">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TagCategoryState): TagCategory
```


Get an existing TagCategory resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tagCategory.ts#L39">property associableTypes</a>
</h3>

```typescript
public associableTypes: pulumi.Output<string[]>;
```


A list object types that this category is
valid to be assigned to. For a full list, click
here.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tagCategory.ts#L46">property cardinality</a>
</h3>

```typescript
public cardinality: pulumi.Output<string>;
```


The number of tags that can be assigned from this
category to a single object at once. Can be one of `SINGLE` (object can only
be assigned one tag in this category), to `MULTIPLE` (object can be assigned
multiple tags in this category). Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tagCategory.ts#L50">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description for the category.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tagCategory.ts#L54">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the category.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="VappContainer">
<a class="pdoc-member-name" href="/vappContainer.ts#L15">class VappContainer</a>
</h2>

The `vsphere_vapp_container` resource can be used to create and manage
vApps.

For more information on vSphere vApps, see [this
page][ref-vsphere-vapp].

[ref-vsphere-vapp]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-2A95EBB8-1779-40FA-B4FB-4D0845750879.html

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L117">constructor</a>
</h3>

```typescript
new VappContainer(name: string, args: VappContainerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VappContainer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VappContainerState): VappContainer
```


Get an existing VappContainer resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L33">property cpuExpandable</a>
</h3>

```typescript
public cpuExpandable: pulumi.Output<boolean | undefined>;
```


Determines if the reservation on a vApp
container can grow beyond the specified value if the parent resource pool has
unreserved resources. Default: `true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L40">property cpuLimit</a>
</h3>

```typescript
public cpuLimit: pulumi.Output<number | undefined>;
```


The CPU utilization of a vApp container will not
exceed this limit, even if there are available resources. Set to `-1` for
unlimited.
Default: `-1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L45">property cpuReservation</a>
</h3>

```typescript
public cpuReservation: pulumi.Output<number | undefined>;
```


Amount of CPU (MHz) that is guaranteed
available to the vApp container. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L53">property cpuShareLevel</a>
</h3>

```typescript
public cpuShareLevel: pulumi.Output<string | undefined>;
```


The CPU allocation level. The level is a
simplified view of shares. Levels map to a pre-determined set of numeric
values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
`low`, `normal`, or `high` are specified values in `cpu_shares` will be
ignored.  Default: `normal`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L59">property cpuShares</a>
</h3>

```typescript
public cpuShares: pulumi.Output<number>;
```


The number of shares allocated for CPU. Used to
determine resource allocation in case of resource contention. If this is set,
`cpu_share_level` must be `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L63">property customAttributes</a>
</h3>

```typescript
public customAttributes: pulumi.Output<{ ... } | undefined>;
```


A list of custom attributes to set on this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L69">property memoryExpandable</a>
</h3>

```typescript
public memoryExpandable: pulumi.Output<boolean | undefined>;
```


Determines if the reservation on a vApp
container can grow beyond the specified value if the parent resource pool has
unreserved resources. Default: `true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L76">property memoryLimit</a>
</h3>

```typescript
public memoryLimit: pulumi.Output<number | undefined>;
```


The CPU utilization of a vApp container will not
exceed this limit, even if there are available resources. Set to `-1` for
unlimited.
Default: `-1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L81">property memoryReservation</a>
</h3>

```typescript
public memoryReservation: pulumi.Output<number | undefined>;
```


Amount of CPU (MHz) that is guaranteed
available to the vApp container. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L89">property memoryShareLevel</a>
</h3>

```typescript
public memoryShareLevel: pulumi.Output<string | undefined>;
```


The CPU allocation level. The level is a
simplified view of shares. Levels map to a pre-determined set of numeric
values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
`low`, `normal`, or `high` are specified values in `memory_shares` will be
ignored.  Default: `normal`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L95">property memoryShares</a>
</h3>

```typescript
public memoryShares: pulumi.Output<number>;
```


The number of shares allocated for CPU. Used to
determine resource allocation in case of resource contention. If this is set,
`memory_share_level` must be `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L99">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the vApp container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L104">property parentFolderId</a>
</h3>

```typescript
public parentFolderId: pulumi.Output<string | undefined>;
```


The [managed object ID][docs-about-morefs] of
the vApp container's parent folder.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L112">property parentResourcePoolId</a>
</h3>

```typescript
public parentResourcePoolId: pulumi.Output<string>;
```


The [managed object ID][docs-about-morefs]
of the parent resource pool. This can be the root resource pool for a cluster
or standalone host, or a resource pool itself. When moving a vApp container
from one parent resource pool to another, both must share a common root
resource pool or the move will fail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L117">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<string[] | undefined>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="VirtualDisk">
<a class="pdoc-member-name" href="/virtualDisk.ts#L15">class VirtualDisk</a>
</h2>

The `vsphere_virtual_disk` resource can be used to create virtual disks outside
of any given [`vsphere_virtual_machine`][docs-vsphere-virtual-machine]
resource. These disks can be attached to a virtual machine by creating a disk
block with the [`attach`][docs-vsphere-virtual-machine-disk-attach] parameter.

[docs-vsphere-virtual-machine]: /docs/providers/vsphere/r/virtual_machine.html
[docs-vsphere-virtual-machine-disk-attach]: /docs/providers/vsphere/r/virtual_machine.html#attach

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L65">constructor</a>
</h3>

```typescript
new VirtualDisk(name: string, args: VirtualDiskArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VirtualDisk resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VirtualDiskState): VirtualDisk
```


Get an existing VirtualDisk resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L32">property adapterType</a>
</h3>

```typescript
public adapterType: pulumi.Output<string | undefined>;
```


The adapter type for this virtual disk. Can be
one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L38">property createDirectories</a>
</h3>

```typescript
public createDirectories: pulumi.Output<boolean | undefined>;
```


Tells the resource to create any
directories that are a part of the `vmdk_path` parameter if they are missing.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L44">property datacenter</a>
</h3>

```typescript
public datacenter: pulumi.Output<string | undefined>;
```


The name of the datacenter in which to create the
disk. Can be omitted when when ESXi or if there is only one datacenter in
your infrastructure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L49">property datastore</a>
</h3>

```typescript
public datastore: pulumi.Output<string>;
```


The name of the datastore in which to create the
disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L53">property size</a>
</h3>

```typescript
public size: pulumi.Output<number>;
```


Size of the disk (in GB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L60">property type</a>
</h3>

```typescript
public type: pulumi.Output<string | undefined>;
```


The type of disk to create. Can be one of
`eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
information on what each kind of disk provisioning policy means, click
[here][docs-vmware-vm-disk-provisioning].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L65">property vmdkPath</a>
</h3>

```typescript
public vmdkPath: pulumi.Output<string>;
```


The path, including filename, of the virtual disk to
be created.  This needs to end in `.vmdk`.

<h2 class="pdoc-module-header" id="VirtualMachine">
<a class="pdoc-member-name" href="/virtualMachine.ts#L17">class VirtualMachine</a>
</h2>

The `vsphere_virtual_machine` resource can be used to manage the complex
lifecycle of a virtual machine. It supports management of disk, network
interface, and CDROM devices, creation from scratch or cloning from template,
and migration through both host and storage vMotion.

For more details on working with virtual machines in vSphere, see [this
page][vmware-docs-vm-management].

[vmware-docs-vm-management]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-55238059-912E-411F-A0E9-A7A536972A91.html

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L423">constructor</a>
</h3>

```typescript
new VirtualMachine(name: string, args: VirtualMachineArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VirtualMachine resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L26">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VirtualMachineState): VirtualMachine
```


Get an existing VirtualMachine resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L34">property alternateGuestName</a>
</h3>

```typescript
public alternateGuestName: pulumi.Output<string | undefined>;
```


The guest name for the operating system
when `guest_id` is `other` or `other-64`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L39">property annotation</a>
</h3>

```typescript
public annotation: pulumi.Output<string | undefined>;
```


A user-provided description of the virtual machine.
The default is no annotation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L44">property bootDelay</a>
</h3>

```typescript
public bootDelay: pulumi.Output<number | undefined>;
```


The number of milliseconds to wait before starting
the boot sequence. The default is no delay.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L50">property bootRetryDelay</a>
</h3>

```typescript
public bootRetryDelay: pulumi.Output<number | undefined>;
```


The number of milliseconds to wait before
retrying the boot sequence. This only valid if `boot_retry_enabled` is true.
Default: `10000` (10 seconds).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L56">property bootRetryEnabled</a>
</h3>

```typescript
public bootRetryEnabled: pulumi.Output<boolean | undefined>;
```


If set to true, a virtual machine that
fails to boot will try again after the delay defined in `boot_retry_delay`.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L61">property cdrom</a>
</h3>

```typescript
public cdrom: pulumi.Output<{ ... } | undefined>;
```


A specification for a CDROM device on this virtual
machine. See CDROM options below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L67">property changeVersion</a>
</h3>

```typescript
public changeVersion: pulumi.Output<string>;
```


A unique identifier for a given version of the last
configuration applied, such the timestamp of the last update to the
configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L74">property clone</a>
</h3>

```typescript
public clone: pulumi.Output<{ ... } | undefined>;
```


When specified, the VM will be created as a clone of a
specified template. Optional customization options can be submitted as well.
See creating a virtual machine from a
template for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L79">property cpuHotAddEnabled</a>
</h3>

```typescript
public cpuHotAddEnabled: pulumi.Output<boolean | undefined>;
```


Allow CPUs to be added to this virtual
machine while it is running.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L84">property cpuHotRemoveEnabled</a>
</h3>

```typescript
public cpuHotRemoveEnabled: pulumi.Output<boolean | undefined>;
```


Allow CPUs to be removed to this
virtual machine while it is running.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L90">property cpuLimit</a>
</h3>

```typescript
public cpuLimit: pulumi.Output<number | undefined>;
```


The maximum amount of CPU (in MHz) that this virtual
machine can consume, regardless of available resources. The default is no
limit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L95">property cpuPerformanceCountersEnabled</a>
</h3>

```typescript
public cpuPerformanceCountersEnabled: pulumi.Output<boolean | undefined>;
```


Enable CPU performance
counters on this virtual machine. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L100">property cpuReservation</a>
</h3>

```typescript
public cpuReservation: pulumi.Output<number | undefined>;
```


The amount of CPU (in MHz) that this virtual
machine is guaranteed. The default is no reservation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L105">property cpuShareCount</a>
</h3>

```typescript
public cpuShareCount: pulumi.Output<number>;
```


The number of CPU shares allocated to the
virtual machine when the `cpu_share_level` is `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L110">property cpuShareLevel</a>
</h3>

```typescript
public cpuShareLevel: pulumi.Output<string | undefined>;
```


The allocation level for CPU resources. Can be
one of `high`, `low`, `normal`, or `custom`. Default: `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L117">property customAttributes</a>
</h3>

```typescript
public customAttributes: pulumi.Output<{ ... } | undefined>;
```


Map of custom attribute ids to attribute
value strings to set for virtual machine. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L125">property datastoreClusterId</a>
</h3>

```typescript
public datastoreClusterId: pulumi.Output<string | undefined>;
```


The [managed object reference
ID][docs-about-morefs] of the datastore cluster ID to use. This setting
applies to entire virtual machine and implies that you wish to use Storage
DRS with this virtual machine. See the section on virtual machine
migration for details on changing this value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L130">property datastoreId</a>
</h3>

```typescript
public datastoreId: pulumi.Output<string>;
```


The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L140">property defaultIpAddress</a>
</h3>

```typescript
public defaultIpAddress: pulumi.Output<string>;
```


The IP address selected by Terraform to be used with
any [provisioners][tf-docs-provisioners] configured on this resource.
Whenever possible, this is the first IPv4 address that is reachable through
the default gateway configured on the machine, then the first reachable IPv6
address, and then the first general discovered address if neither exist. If
VMware tools is not running on the virtual machine, or if the VM is powered
off, this value will be blank.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L145">property disks</a>
</h3>

```typescript
public disks: pulumi.Output<{ ... }[]>;
```


A specification for a virtual disk device on this virtual
machine. See disk options below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L150">property efiSecureBootEnabled</a>
</h3>

```typescript
public efiSecureBootEnabled: pulumi.Output<boolean | undefined>;
```


When the `firmware` type is set to is
`efi`, this enables EFI secure boot. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L155">property enableDiskUuid</a>
</h3>

```typescript
public enableDiskUuid: pulumi.Output<boolean | undefined>;
```


Expose the UUIDs of attached virtual disks to
the virtual machine, allowing access to them in the guest. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L160">property enableLogging</a>
</h3>

```typescript
public enableLogging: pulumi.Output<boolean | undefined>;
```


Enable logging of virtual machine events to a
log file stored in the virtual machine directory. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L166">property eptRviMode</a>
</h3>

```typescript
public eptRviMode: pulumi.Output<string | undefined>;
```


The EPT/RVI (hardware memory virtualization)
setting for this virtual machine. Can be one of `automatic`, `on`, or `off`.
Default: `automatic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L172">property extraConfig</a>
</h3>

```typescript
public extraConfig: pulumi.Output<{ ... } | undefined>;
```


Extra configuration data for this virtual
machine. Can be used to supply advanced parameters not normally in
configuration, such as data for cloud-config (under the guestinfo namespace).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L177">property firmware</a>
</h3>

```typescript
public firmware: pulumi.Output<string | undefined>;
```


The firmware interface to use on the virtual machine.
Can be one of `bios` or `EFI`. Default: `bios`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L182">property folder</a>
</h3>

```typescript
public folder: pulumi.Output<string | undefined>;
```


The path to the folder to put this virtual machine in,
relative to the datacenter that the resource pool is in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L189">property forcePowerOff</a>
</h3>

```typescript
public forcePowerOff: pulumi.Output<boolean | undefined>;
```


If a guest shutdown failed or timed out while
updating or destroying (see
`shutdown_wait_timeout`), force the power-off of
the virtual machine. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L194">property guestId</a>
</h3>

```typescript
public guestId: pulumi.Output<string | undefined>;
```


The guest ID for the operating system type. For a
full list of possible values, see [here][vmware-docs-guest-ids]. Default: `other-64`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L202">property guestIpAddresses</a>
</h3>

```typescript
public guestIpAddresses: pulumi.Output<string[]>;
```


The current list of IP addresses on this machine,
including the value of `default_ip_address`. If VMware tools is not running
on the virtual machine, or if the VM is powered off, this list will be empty.
* `moid`: The [managed object reference ID][docs-about-morefs] of the created
virtual machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L211">property hostSystemId</a>
</h3>

```typescript
public hostSystemId: pulumi.Output<string>;
```


An optional [managed object reference
ID][docs-about-morefs] of a host to put this virtual machine on. See the
section on virtual machine migration for
details on changing this value. If a `host_system_id` is not supplied,
vSphere will select a host in the resource pool to place the virtual machine,
according to any defaults or DRS policies in place.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L217">property hvMode</a>
</h3>

```typescript
public hvMode: pulumi.Output<string | undefined>;
```


The (non-nested) hardware virtualization setting for
this virtual machine. Can be one of `hvAuto`, `hvOn`, or `hvOff`. Default:
`hvAuto`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L224">property imported</a>
</h3>

```typescript
public imported: pulumi.Output<boolean>;
```


This is flagged if the virtual machine has been imported, or the
state has been migrated from a previous version of the resource. It
influences the behavior of the first post-import apply operation. See the
section on importing below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L232">property latencySensitivity</a>
</h3>

```typescript
public latencySensitivity: pulumi.Output<string | undefined>;
```


Controls the scheduling delay of the
virtual machine. Use a higher sensitivity for applications that require lower
latency, such as VOIP, media player applications, or applications that
require frequent access to mouse or keyboard devices. Can be one of `low`,
`normal`, `medium`, or `high`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L237">property memory</a>
</h3>

```typescript
public memory: pulumi.Output<number | undefined>;
```


The size of the virtual machine's memory, in MB.
Default: `1024` (1 GB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L242">property memoryHotAddEnabled</a>
</h3>

```typescript
public memoryHotAddEnabled: pulumi.Output<boolean | undefined>;
```


Allow memory to be added to this
virtual machine while it is running.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L248">property memoryLimit</a>
</h3>

```typescript
public memoryLimit: pulumi.Output<number | undefined>;
```


The maximum amount of memory (in MB) that this
virtual machine can consume, regardless of available resources. The default
is no limit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L253">property memoryReservation</a>
</h3>

```typescript
public memoryReservation: pulumi.Output<number | undefined>;
```


The amount of memory (in MB) that this
virtual machine is guaranteed. The default is no reservation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L258">property memoryShareCount</a>
</h3>

```typescript
public memoryShareCount: pulumi.Output<number>;
```


The number of memory shares allocated to
the virtual machine when the `memory_share_level` is `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L263">property memoryShareLevel</a>
</h3>

```typescript
public memoryShareLevel: pulumi.Output<string | undefined>;
```


The allocation level for memory resources.
Can be one of `high`, `low`, `normal`, or `custom`. Default: `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L270">property migrateWaitTimeout</a>
</h3>

```typescript
public migrateWaitTimeout: pulumi.Output<number | undefined>;
```


The amount of time, in minutes, to wait
for a virtual machine migration to complete before failing. Default: 10
minutes. Also see the section on virtual machine
migration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L274">property moid</a>
</h3>

```typescript
public moid: pulumi.Output<string>;
```


The machine object ID from VMWare

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L279">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


An alias for both `label` and `path`, the latter when
using `attach`. Required if not using `label`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L285">property nestedHvEnabled</a>
</h3>

```typescript
public nestedHvEnabled: pulumi.Output<boolean | undefined>;
```


Enable nested hardware virtualization on
this virtual machine, facilitating nested virtualization in the guest.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L291">property networkInterfaces</a>
</h3>

```typescript
public networkInterfaces: pulumi.Output<{ ... }[]>;
```


A specification for a virtual NIC on this
virtual machine. See network interface options
below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L297">property numCoresPerSocket</a>
</h3>

```typescript
public numCoresPerSocket: pulumi.Output<number | undefined>;
```


The number of cores to distribute among
the CPUs in this virtual machine. If specified, the value supplied to
`num_cpus` must be evenly divisible by this value. Default: `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L302">property numCpus</a>
</h3>

```typescript
public numCpus: pulumi.Output<number | undefined>;
```


The number of virtual processors to assign to this
virtual machine. Default: `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L308">property rebootRequired</a>
</h3>

```typescript
public rebootRequired: pulumi.Output<boolean>;
```


Value internal to Terraform used to determine if a
configuration set change requires a reboot. This value is only useful during
an update process and gets reset on refresh.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L315">property resourcePoolId</a>
</h3>

```typescript
public resourcePoolId: pulumi.Output<string>;
```


The [managed object reference
ID][docs-about-morefs] of the resource pool to put this virtual machine in.
See the section on virtual machine migration
for details on changing this value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L320">property runToolsScriptsAfterPowerOn</a>
</h3>

```typescript
public runToolsScriptsAfterPowerOn: pulumi.Output<boolean | undefined>;
```


Enable the execution of
post-power-on scripts when VMware tools is installed. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L325">property runToolsScriptsAfterResume</a>
</h3>

```typescript
public runToolsScriptsAfterResume: pulumi.Output<boolean | undefined>;
```


Enable the execution of
post-resume scripts when VMware tools is installed. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L330">property runToolsScriptsBeforeGuestReboot</a>
</h3>

```typescript
public runToolsScriptsBeforeGuestReboot: pulumi.Output<boolean | undefined>;
```


Enable the execution of
pre-reboot scripts when VMware tools is installed. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L335">property runToolsScriptsBeforeGuestShutdown</a>
</h3>

```typescript
public runToolsScriptsBeforeGuestShutdown: pulumi.Output<boolean | undefined>;
```


Enable the execution
of pre-shutdown scripts when VMware tools is installed. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L340">property runToolsScriptsBeforeGuestStandby</a>
</h3>

```typescript
public runToolsScriptsBeforeGuestStandby: pulumi.Output<boolean | undefined>;
```


Enable the execution of
pre-standby scripts when VMware tools is installed. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L345">property scsiBusSharing</a>
</h3>

```typescript
public scsiBusSharing: pulumi.Output<string | undefined>;
```


Mode for sharing the SCSI bus. The modes are
physicalSharing, virtualSharing, and noSharing. Default: `noSharing`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L352">property scsiControllerCount</a>
</h3>

```typescript
public scsiControllerCount: pulumi.Output<number | undefined>;
```


The number of SCSI controllers that
Terraform manages on this virtual machine. This directly affects the amount
of disks you can add to the virtual machine and the maximum disk unit number.
Note that lowering this value does not remove controllers. Default: `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L358">property scsiType</a>
</h3>

```typescript
public scsiType: pulumi.Output<string | undefined>;
```


The type of SCSI bus this virtual machine will have.
Can be one of lsilogic (LSI Logic Parallel), lsilogic-sas (LSI Logic SAS) or
pvscsi (VMware Paravirtual). Defualt: `pvscsi`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L365">property shutdownWaitTimeout</a>
</h3>

```typescript
public shutdownWaitTimeout: pulumi.Output<number | undefined>;
```


The amount of time, in minutes, to wait
for a graceful guest shutdown when making necessary updates to the virtual
machine. If `force_power_off` is set to true, the VM will be force powered-off
after this timeout, otherwise an error is returned. Default: 3 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L371">property swapPlacementPolicy</a>
</h3>

```typescript
public swapPlacementPolicy: pulumi.Output<string | undefined>;
```


The swap file placement policy for this
virtual machine. Can be one of `inherit`, `hostLocal`, or `vmDirectory`.
Default: `inherit`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L376">property syncTimeWithHost</a>
</h3>

```typescript
public syncTimeWithHost: pulumi.Output<boolean | undefined>;
```


Enable guest clock synchronization with
the host. Requires VMware tools to be installed. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L381">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<string[] | undefined>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L386">property uuid</a>
</h3>

```typescript
public uuid: pulumi.Output<string>;
```


The UUID of the virtual disk's VMDK file. This is used to track the
virtual disk on the virtual machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L394">property vapp</a>
</h3>

```typescript
public vapp: pulumi.Output<{ ... } | undefined>;
```


Optional vApp configuration. The only sub-key available
is `properties`, which is a key/value map of properties for virtual machines
imported from OVF or OVA files. See Using vApp properties to supply OVF/OVA
configuration for
more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L400">property vappTransports</a>
</h3>

```typescript
public vappTransports: pulumi.Output<string[]>;
```


Computed value which is only valid for cloned virtual
machines. A list of vApp transport methods supported by the source virtual
machine or template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L405">property vmwareToolsStatus</a>
</h3>

```typescript
public vmwareToolsStatus: pulumi.Output<string>;
```


The state of VMware tools in the guest. This will
determine the proper course of action for some device operations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L410">property vmxPath</a>
</h3>

```typescript
public vmxPath: pulumi.Output<string>;
```


The path of the virtual machine's configuration file in the VM's
datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L417">property waitForGuestNetRoutable</a>
</h3>

```typescript
public waitForGuestNetRoutable: pulumi.Output<boolean | undefined>;
```


Controls whether or not the guest
network waiter waits for a routable address. When `false`, the waiter does
not wait for a default gateway, nor are IP addresses checked against any
discovered default gateways as part of its success criteria. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L423">property waitForGuestNetTimeout</a>
</h3>

```typescript
public waitForGuestNetTimeout: pulumi.Output<number | undefined>;
```


The amount of time, in minutes, to
wait for an available IP address on this virtual machine. A value less than 1
disables the waiter. Default: 5 minutes.

<h2 class="pdoc-module-header" id="VirtualMachineSnapshot">
<a class="pdoc-member-name" href="/virtualMachineSnapshot.ts#L30">class VirtualMachineSnapshot</a>
</h2>

The `vsphere_virtual_machine_snapshot` resource can be used to manage snapshots
for a virtual machine.

For more information on managing snapshots and how they work in VMware, see
[here][ext-vm-snapshot-management].

[ext-vm-snapshot-management]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-CA948C69-7F58-4519-AEB1-739545EA94E5.html

~> **NOTE:** A snapshot in VMware differs from traditional disk snapshots, and
can contain the actual running state of the virtual machine, data for all disks
that have not been set to be independent from the snapshot (including ones that
have been attached via the [attach][docs-vsphere-virtual-machine-disk-attach]
parameter to the `vsphere_virtual_machine` `disk` block), and even the
configuration of the virtual machine at the time of the snapshot. Virtual
machine, disk activity, and configuration changes post-snapshot are not
included in the original state. Use this resource with care! Neither VMware nor
HashiCorp recommends retaining snapshots for a extended period of time and does
NOT recommend using them as as backup feature. For more information on the
limitation of virtual machine snapshots, see [here][ext-vm-snap-limitations].

[docs-vsphere-virtual-machine-disk-attach]: /docs/providers/vsphere/r/virtual_machine.html#attach
[ext-vm-snap-limitations]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-53F65726-A23B-4CF0-A7D5-48E584B88613.html

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L76">constructor</a>
</h3>

```typescript
new VirtualMachineSnapshot(name: string, args: VirtualMachineSnapshotArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VirtualMachineSnapshot resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L39">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VirtualMachineSnapshotState): VirtualMachineSnapshot
```


Get an existing VirtualMachineSnapshot resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L48">property consolidate</a>
</h3>

```typescript
public consolidate: pulumi.Output<boolean | undefined>;
```


If set to `true`, the delta disks involved in this
snapshot will be consolidated into the parent when this resource is
destroyed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L52">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


A description for the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L57">property memory</a>
</h3>

```typescript
public memory: pulumi.Output<boolean>;
```


If set to `true`, a dump of the internal state of the
virtual machine is included in the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L63">property quiesce</a>
</h3>

```typescript
public quiesce: pulumi.Output<boolean>;
```


If set to `true`, and the virtual machine is powered
on when the snapshot is taken, VMware Tools is used to quiesce the file
system in the virtual machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L68">property removeChildren</a>
</h3>

```typescript
public removeChildren: pulumi.Output<boolean | undefined>;
```


If set to `true`, the entire snapshot subtree
is removed when this resource is destroyed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L72">property snapshotName</a>
</h3>

```typescript
public snapshotName: pulumi.Output<string>;
```


The name of the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L76">property virtualMachineUuid</a>
</h3>

```typescript
public virtualMachineUuid: pulumi.Output<string>;
```


The virtual machine UUID.

<h2 class="pdoc-module-header" id="VmfsDatastore">
<a class="pdoc-member-name" href="/vmfsDatastore.ts#L16">class VmfsDatastore</a>
</h2>

The `vsphere_vmfs_datastore` resource can be used to create and manage VMFS
datastores on an ESXi host or a set of hosts. The resource supports using any
SCSI device that can generally be used in a datastore, such as local disks, or
disks presented to a host or multiple hosts over Fibre Channel or iSCSI.
Devices can be specified manually, or discovered using the
[`vsphere_vmfs_disks`][data-source-vmfs-disks] data source.

[data-source-vmfs-disks]: /docs/providers/vsphere/d/vmfs_disks.html

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L104">constructor</a>
</h3>

```typescript
new VmfsDatastore(name: string, args: VmfsDatastoreArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VmfsDatastore resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VmfsDatastoreState): VmfsDatastore
```


Get an existing VmfsDatastore resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L33">property accessible</a>
</h3>

```typescript
public accessible: pulumi.Output<boolean>;
```


The connectivity status of the datastore. If this is `false`,
some other computed attributes may be out of date.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L37">property capacity</a>
</h3>

```typescript
public capacity: pulumi.Output<number>;
```


Maximum capacity of the datastore, in megabytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L44">property customAttributes</a>
</h3>

```typescript
public customAttributes: pulumi.Output<{ ... } | undefined>;
```


Map of custom attribute ids to attribute
value string to set on datastore resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L50">property datastoreClusterId</a>
</h3>

```typescript
public datastoreClusterId: pulumi.Output<string | undefined>;
```


The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L54">property disks</a>
</h3>

```typescript
public disks: pulumi.Output<string[]>;
```


The disks to use with the datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L64">property folder</a>
</h3>

```typescript
public folder: pulumi.Output<string | undefined>;
```


The relative path to a folder to put this datastore in.
This is a path relative to the datacenter you are deploying the datastore to.
Example: for the `dc1` datacenter, and a provided `folder` of `foo/bar`,
Terraform will place a datastore named `terraform-test` in a datastore folder
located at `/dc1/datastore/foo/bar`, with the final inventory path being
`/dc1/datastore/foo/bar/terraform-test`. Conflicts with
`datastore_cluster_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L68">property freeSpace</a>
</h3>

```typescript
public freeSpace: pulumi.Output<number>;
```


Available space of this datastore, in megabytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L76">property hostSystemId</a>
</h3>

```typescript
public hostSystemId: pulumi.Output<string>;
```


The [managed object ID][docs-about-morefs] of
the host to set the datastore up on. Note that this is not necessarily the
only host that the datastore will be set up on - see
here for more info. Forces a
new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L80">property maintenanceMode</a>
</h3>

```typescript
public maintenanceMode: pulumi.Output<string>;
```


The current maintenance mode state of the datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L85">property multipleHostAccess</a>
</h3>

```typescript
public multipleHostAccess: pulumi.Output<boolean>;
```


If `true`, more than one host in the datacenter has
been configured with access to the datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L90">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the datastore. Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L95">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<string[] | undefined>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L100">property uncommittedSpace</a>
</h3>

```typescript
public uncommittedSpace: pulumi.Output<number>;
```


Total additional storage space, in megabytes,
potentially used by all virtual machines on this datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L104">property url</a>
</h3>

```typescript
public url: pulumi.Output<string>;
```


The unique locator for the datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getComputeCluster">
<a class="pdoc-member-name" href="/getComputeCluster.ts#L24">function getComputeCluster</a>
</h2>

```typescript
getComputeCluster(args: GetComputeClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetComputeClusterResult>
```


The `vsphere_compute_cluster` data source can be used to discover the ID of a
cluster in vSphere. This is useful to fetch the ID of a cluster that you want
to use for virtual machine placement via the
[`vsphere_virtual_machine`][docs-virtual-machine-resource] resource, allowing
you to specify the cluster's root resource pool directly versus using the alias
available through the [`vsphere_resource_pool`][docs-resource-pool-data-source]
data source.

[docs-virtual-machine-resource]: /docs/providers/vsphere/r/virtual_machine.html
[docs-resource-pool-data-source]: /docs/providers/vsphere/d/resource_pool.html

-> You may also wish to see the
[`vsphere_compute_cluster`][docs-compute-cluster-resource] resource for further
details about clusters or how to work with them in Terraform.

[docs-compute-cluster-resource]: /docs/providers/vsphere/r/compute_cluster.html

<h2 class="pdoc-module-header" id="getCustomAttribute">
<a class="pdoc-member-name" href="/getCustomAttribute.ts#L18">function getCustomAttribute</a>
</h2>

```typescript
getCustomAttribute(args: GetCustomAttributeArgs, opts?: pulumi.InvokeOptions): Promise<GetCustomAttributeResult>
```


The `vsphere_custom_attribute` data source can be used to reference custom
attributes that are not managed by Terraform. Its attributes are exactly the
same as the [`vsphere_custom_attribute` resource][resource-custom-attribute],
and, like importing, the data source takes a name to search on. The `id` and
other attributes are then populated with the data found by the search.

[resource-custom-attribute]: /docs/providers/vsphere/r/custom_attribute.html

~> **NOTE:** Custom attributes are unsupported on direct ESXi connections
and require vCenter.

<h2 class="pdoc-module-header" id="getDatacenter">
<a class="pdoc-member-name" href="/getDatacenter.ts#L14">function getDatacenter</a>
</h2>

```typescript
getDatacenter(args?: GetDatacenterArgs, opts?: pulumi.InvokeOptions): Promise<GetDatacenterResult>
```


The `vsphere_datacenter` data source can be used to discover the ID of a
vSphere datacenter. This can then be used with resources or data sources that
require a datacenter, such as the [`vsphere_host`][data-source-vsphere-host]
data source.

[data-source-vsphere-host]: /docs/providers/vsphere/d/host.html

<h2 class="pdoc-module-header" id="getDatastore">
<a class="pdoc-member-name" href="/getDatastore.ts#L14">function getDatastore</a>
</h2>

```typescript
getDatastore(args: GetDatastoreArgs, opts?: pulumi.InvokeOptions): Promise<GetDatastoreResult>
```


The `vsphere_datastore` data source can be used to discover the ID of a
datastore in vSphere. This is useful to fetch the ID of a datastore that you
want to use to create virtual machines in using the
[`vsphere_virtual_machine`][docs-virtual-machine-resource] resource.

[docs-virtual-machine-resource]: /docs/providers/vsphere/r/virtual_machine.html

<h2 class="pdoc-module-header" id="getDatastoreCluster">
<a class="pdoc-member-name" href="/getDatastoreCluster.ts#L19">function getDatastoreCluster</a>
</h2>

```typescript
getDatastoreCluster(args: GetDatastoreClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetDatastoreClusterResult>
```


The `vsphere_datastore_cluster` data source can be used to discover the ID of a
datastore cluster in vSphere. This is useful to fetch the ID of a datastore
cluster that you want to use to assign datastores to using the
[`vsphere_nas_datastore`][docs-nas-datastore-resource] or
[`vsphere_vmfs_datastore`][docs-vmfs-datastore-resource] resources, or create
virtual machines in using the
[`vsphere_virtual_machine`][docs-virtual-machine-resource] resource.

[docs-nas-datastore-resource]: /docs/providers/vsphere/r/nas_datastore.html
[docs-vmfs-datastore-resource]: /docs/providers/vsphere/r/vmfs_datastore.html
[docs-virtual-machine-resource]: /docs/providers/vsphere/r/virtual_machine.html

<h2 class="pdoc-module-header" id="getDistributedVirtualSwitch">
<a class="pdoc-member-name" href="/getDistributedVirtualSwitch.ts#L18">function getDistributedVirtualSwitch</a>
</h2>

```typescript
getDistributedVirtualSwitch(args: GetDistributedVirtualSwitchArgs, opts?: pulumi.InvokeOptions): Promise<GetDistributedVirtualSwitchResult>
```


The `vsphere_distributed_virtual_switch` data source can be used to discover
the ID and uplink data of a of a vSphere distributed virtual switch (DVS). This
can then be used with resources or data sources that require a DVS, such as the
[`vsphere_distributed_port_group`][distributed-port-group] resource, for which
an example is shown below.

[distributed-port-group]: /docs/providers/vsphere/r/distributed_port_group.html

~> **NOTE:** This data source requires vCenter and is not available on direct
ESXi connections.

<h2 class="pdoc-module-header" id="getHost">
<a class="pdoc-member-name" href="/getHost.ts#L11">function getHost</a>
</h2>

```typescript
getHost(args: GetHostArgs, opts?: pulumi.InvokeOptions): Promise<GetHostResult>
```


The `vsphere_host` data source can be used to discover the ID of a vSphere
host. This can then be used with resources or data sources that require a host
managed object reference ID.

<h2 class="pdoc-module-header" id="getNetwork">
<a class="pdoc-member-name" href="/getNetwork.ts#L13">function getNetwork</a>
</h2>

```typescript
getNetwork(args: GetNetworkArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkResult>
```


The `vsphere_network` data source can be used to discover the ID of a network
in vSphere. This can be any network that can be used as the backing for a
network interface for `vsphere_virtual_machine` or any other vSphere resource
that requires a network. This includes standard (host-based) port groups, DVS
port groups, or opaque networks such as those managed by NSX.

<h2 class="pdoc-module-header" id="getResourcePool">
<a class="pdoc-member-name" href="/getResourcePool.ts#L14">function getResourcePool</a>
</h2>

```typescript
getResourcePool(args?: GetResourcePoolArgs, opts?: pulumi.InvokeOptions): Promise<GetResourcePoolResult>
```


The `vsphere_resource_pool` data source can be used to discover the ID of a
resource pool in vSphere. This is useful to fetch the ID of a resource pool
that you want to use to create virtual machines in using the
[`vsphere_virtual_machine`][docs-virtual-machine-resource] resource.

[docs-virtual-machine-resource]: /docs/providers/vsphere/r/virtual_machine.html

<h2 class="pdoc-module-header" id="getTag">
<a class="pdoc-member-name" href="/getTag.ts#L18">function getTag</a>
</h2>

```typescript
getTag(args: GetTagArgs, opts?: pulumi.InvokeOptions): Promise<GetTagResult>
```


The `vsphere_tag` data source can be used to reference tags that are not
managed by Terraform. Its attributes are exactly the same as the [`vsphere_tag`
resource][resource-tag], and, like importing, the data source takes a name and
category to search on. The `id` and other attributes are then populated with
the data found by the search.

[resource-tag]: /docs/providers/vsphere/r/tag.html

~> **NOTE:** Tagging support is unsupported on direct ESXi connections and
requires vCenter 6.0 or higher.

<h2 class="pdoc-module-header" id="getTagCategory">
<a class="pdoc-member-name" href="/getTagCategory.ts#L18">function getTagCategory</a>
</h2>

```typescript
getTagCategory(args: GetTagCategoryArgs, opts?: pulumi.InvokeOptions): Promise<GetTagCategoryResult>
```


The `vsphere_tag_category` data source can be used to reference tag categories
that are not managed by Terraform. Its attributes are exactly the same as the
[`vsphere_tag_category` resource][resource-tag-category], and, like importing,
the data source takes a name to search on. The `id` and other attributes are
then populated with the data found by the search.

[resource-tag-category]: /docs/providers/vsphere/r/tag_category.html

~> **NOTE:** Tagging support is unsupported on direct ESXi connections and
requires vCenter 6.0 or higher.

<h2 class="pdoc-module-header" id="getVirtualMachine">
<a class="pdoc-member-name" href="/getVirtualMachine.ts#L15">function getVirtualMachine</a>
</h2>

```typescript
getVirtualMachine(args: GetVirtualMachineArgs, opts?: pulumi.InvokeOptions): Promise<GetVirtualMachineResult>
```


The `vsphere_virtual_machine` data source can be used to find the UUID of an
existing virtual machine or template. Its most relevant purpose is for finding
the UUID of a template to be used as the source for cloning into a new
[`vsphere_virtual_machine`][docs-virtual-machine-resource] resource. It also
reads the guest ID so that can be supplied as well.

[docs-virtual-machine-resource]: /docs/providers/vsphere/r/virtual_machine.html

<h2 class="pdoc-module-header" id="getVmfsDisks">
<a class="pdoc-member-name" href="/getVmfsDisks.ts#L14">function getVmfsDisks</a>
</h2>

```typescript
getVmfsDisks(args: GetVmfsDisksArgs, opts?: pulumi.InvokeOptions): Promise<GetVmfsDisksResult>
```


The `vsphere_vmfs_disks` data source can be used to discover the storage
devices available on an ESXi host. This data source can be combined with the
[`vsphere_vmfs_datastore`][data-source-vmfs-datastore] resource to create VMFS
datastores based off a set of discovered disks.

[data-source-vmfs-datastore]: /docs/providers/vsphere/r/vmfs_datastore.html

<h2 class="pdoc-module-header" id="ComputeClusterArgs">
<a class="pdoc-member-name" href="/computeCluster.ts#L874">interface ComputeClusterArgs</a>
</h2>

The set of arguments for constructing a ComputeCluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L881">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


A map of custom attribute ids to attribute
value strings to set for the datastore cluster. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L886">property datacenterId</a>
</h3>

```typescript
datacenterId: pulumi.Input<string>;
```


The [managed object ID][docs-about-morefs] of
the datacenter to create the cluster in. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L892">property dpmAutomationLevel</a>
</h3>

```typescript
dpmAutomationLevel?: pulumi.Input<string>;
```


The automation level for host power
operations in this cluster. Can be one of `manual` or `automated`. Default:
`manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L898">property dpmEnabled</a>
</h3>

```typescript
dpmEnabled?: pulumi.Input<boolean>;
```


Enable DPM support for DRS in this cluster.
Requires `drs_enabled` to be `true` in order to be effective.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L905">property dpmThreshold</a>
</h3>

```typescript
dpmThreshold?: pulumi.Input<number>;
```


A value between `1` and `5` indicating the
threshold of load within the cluster that influences host power operations.
This affects both power on and power off operations - a lower setting will
tolerate more of a surplus/deficit than a higher setting. Default: `3`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L910">property drsAdvancedOptions</a>
</h3>

```typescript
drsAdvancedOptions?: pulumi.Input<{ ... }>;
```


A key/value map that specifies advanced
options for DRS and DPM.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L916">property drsAutomationLevel</a>
</h3>

```typescript
drsAutomationLevel?: pulumi.Input<string>;
```


The default automation level for all
virtual machines in this cluster. Can be one of `manual`,
`partiallyAutomated`, or `fullyAutomated`. Default: `manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L922">property drsEnablePredictiveDrs</a>
</h3>

```typescript
drsEnablePredictiveDrs?: pulumi.Input<boolean>;
```


When `true`, enables DRS to use data
from [vRealize Operations Manager][ref-vsphere-vro] to make proactive DRS
recommendations. <sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L927">property drsEnableVmOverrides</a>
</h3>

```typescript
drsEnableVmOverrides?: pulumi.Input<boolean>;
```


Allow individual DRS overrides to be
set for virtual machines in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L931">property drsEnabled</a>
</h3>

```typescript
drsEnabled?: pulumi.Input<boolean>;
```


Enable DRS for this cluster. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L938">property drsMigrationThreshold</a>
</h3>

```typescript
drsMigrationThreshold?: pulumi.Input<number>;
```


A value between `1` and `5` indicating
the threshold of imbalance tolerated between hosts. A lower setting will
tolerate more imbalance while a higher setting will tolerate less. Default:
`3`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L947">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The relative path to a folder to put this cluster in.
This is a path relative to the datacenter you are deploying the cluster to.
Example: for the `dc1` datacenter, and a provided `folder` of `foo/bar`,
Terraform will place a cluster named `terraform-compute-cluster-test` in a
host folder located at `/dc1/host/foo/bar`, with the final inventory path
being `/dc1/host/foo/bar/terraform-datastore-cluster-test`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L955">property forceEvacuateOnDestroy</a>
</h3>

```typescript
forceEvacuateOnDestroy?: pulumi.Input<boolean>;
```


When destroying the resource, setting this to
`true` will auto-remove any hosts that are currently a member of the cluster,
as if they were removed by taking their entry out of `host_system_ids` (see
below). This is an advanced
option and should only be used for testing. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L963">property haAdmissionControlFailoverHostSystemIds</a>
</h3>

```typescript
haAdmissionControlFailoverHostSystemIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Defines the
[managed object IDs][docs-about-morefs] of hosts to use as dedicated failover
hosts. These hosts are kept as available as possible - admission control will
block access to the host, and DRS will ignore the host when making
recommendations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L971">property haAdmissionControlHostFailureTolerance</a>
</h3>

```typescript
haAdmissionControlHostFailureTolerance?: pulumi.Input<number>;
```


The maximum number
of failed hosts that admission control tolerates when making decisions on
whether to permit virtual machine operations. The maximum is one less than
the number of hosts in the cluster. Default: `1`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L978">property haAdmissionControlPerformanceTolerance</a>
</h3>

```typescript
haAdmissionControlPerformanceTolerance?: pulumi.Input<number>;
```


The percentage of
resource reduction that a cluster of virtual machines can tolerate in case of
a failover. A value of 0 produces warnings only, whereas a value of 100
disables the setting. Default: `100` (disabled).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L984">property haAdmissionControlPolicy</a>
</h3>

```typescript
haAdmissionControlPolicy?: pulumi.Input<string>;
```


The type of admission control
policy to use with vSphere HA. Can be one of `resourcePercentage`,
`slotPolicy`, `failoverHosts`, or `disabled`. Default: `resourcePercentage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L994">property haAdmissionControlResourcePercentageAutoCompute</a>
</h3>

```typescript
haAdmissionControlResourcePercentageAutoCompute?: pulumi.Input<boolean>;
```


Automatically determine available resource percentages by subtracting the
average number of host resources represented by the
`ha_admission_control_host_failure_tolerance`
setting from the total amount of resources in the cluster. Disable to supply
user-defined values. Default: `true`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1000">property haAdmissionControlResourcePercentageCpu</a>
</h3>

```typescript
haAdmissionControlResourcePercentageCpu?: pulumi.Input<number>;
```


Controls the
user-defined percentage of CPU resources in the cluster to reserve for
failover. Default: `100`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1006">property haAdmissionControlResourcePercentageMemory</a>
</h3>

```typescript
haAdmissionControlResourcePercentageMemory?: pulumi.Input<number>;
```


Controls the
user-defined percentage of memory resources in the cluster to reserve for
failover. Default: `100`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1011">property haAdmissionControlSlotPolicyExplicitCpu</a>
</h3>

```typescript
haAdmissionControlSlotPolicyExplicitCpu?: pulumi.Input<number>;
```


Controls the
user-defined CPU slot size, in MHz. Default: `32`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1016">property haAdmissionControlSlotPolicyExplicitMemory</a>
</h3>

```typescript
haAdmissionControlSlotPolicyExplicitMemory?: pulumi.Input<number>;
```


Controls the
user-defined memory slot size, in MB. Default: `100`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1023">property haAdmissionControlSlotPolicyUseExplicitSize</a>
</h3>

```typescript
haAdmissionControlSlotPolicyUseExplicitSize?: pulumi.Input<boolean>;
```


Controls
whether or not you wish to supply explicit values to CPU and memory slot
sizes. The default is `false`, which tells vSphere to gather a automatic
average based on all powered-on virtual machines currently in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1028">property haAdvancedOptions</a>
</h3>

```typescript
haAdvancedOptions?: pulumi.Input<{ ... }>;
```


A key/value map that specifies advanced
options for vSphere HA.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1035">property haDatastoreApdRecoveryAction</a>
</h3>

```typescript
haDatastoreApdRecoveryAction?: pulumi.Input<string>;
```


Controls the action to take
on virtual machines if an APD status on an affected datastore clears in the
middle of an APD event. Can be one of `none` or `reset`. Default: `none`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1043">property haDatastoreApdResponse</a>
</h3>

```typescript
haDatastoreApdResponse?: pulumi.Input<string>;
```


Controls the action to take on
virtual machines when the cluster has detected loss to all paths to a
relevant datastore. Can be one of `disabled`, `warning`,
`restartConservative`, or `restartAggressive`.  Default: `disabled`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1050">property haDatastoreApdResponseDelay</a>
</h3>

```typescript
haDatastoreApdResponseDelay?: pulumi.Input<number>;
```


Controls the delay in minutes
to wait after an APD timeout event to execute the response action defined in
`ha_datastore_apd_response`. Default: `3`
minutes. <sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1058">property haDatastorePdlResponse</a>
</h3>

```typescript
haDatastorePdlResponse?: pulumi.Input<string>;
```


Controls the action to take on
virtual machines when the cluster has detected a permanent device loss to a
relevant datastore. Can be one of `disabled`, `warning`, or
`restartAggressive`. Default: `disabled`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1063">property haEnabled</a>
</h3>

```typescript
haEnabled?: pulumi.Input<boolean>;
```


Enable vSphere HA for this cluster. Default:
`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1070">property haHeartbeatDatastoreIds</a>
</h3>

```typescript
haHeartbeatDatastoreIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of managed object IDs for
preferred datastores to use for HA heartbeating. This setting is only useful
when `ha_heartbeat_datastore_policy` is set
to either `userSelectedDs` or `allFeasibleDsWithUserPreference`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1077">property haHeartbeatDatastorePolicy</a>
</h3>

```typescript
haHeartbeatDatastorePolicy?: pulumi.Input<string>;
```


The selection policy for HA
heartbeat datastores. Can be one of `allFeasibleDs`, `userSelectedDs`, or
`allFeasibleDsWithUserPreference`. Default:
`allFeasibleDsWithUserPreference`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1084">property haHostIsolationResponse</a>
</h3>

```typescript
haHostIsolationResponse?: pulumi.Input<string>;
```


The action to take on virtual
machines when a host has detected that it has been isolated from the rest of
the cluster. Can be one of `none`, `powerOff`, or `shutdown`. Default:
`none`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1090">property haHostMonitoring</a>
</h3>

```typescript
haHostMonitoring?: pulumi.Input<string>;
```


Global setting that controls whether
vSphere HA remediates virtual machines on host failure. Can be one of `enabled`
or `disabled`. Default: `enabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1097">property haVmComponentProtection</a>
</h3>

```typescript
haVmComponentProtection?: pulumi.Input<string>;
```


Controls vSphere VM component
protection for virtual machines in this cluster. Can be one of `enabled` or
`disabled`. Default: `enabled`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1107">property haVmDependencyRestartCondition</a>
</h3>

```typescript
haVmDependencyRestartCondition?: pulumi.Input<string>;
```


The condition used to
determine whether or not virtual machines in a certain restart priority class
are online, allowing HA to move on to restarting virtual machines on the next
priority. Can be one of `none`, `poweredOn`, `guestHbStatusGreen`, or
`appHbStatusGreen`. The default is `none`, which means that a virtual machine
is considered ready immediately after a host is found to start it on.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1113">property haVmFailureInterval</a>
</h3>

```typescript
haVmFailureInterval?: pulumi.Input<number>;
```


If a heartbeat from a virtual machine
is not received within this configured interval, the virtual machine is
marked as failed. The value is in seconds. Default: `30`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1122">property haVmMaximumFailureWindow</a>
</h3>

```typescript
haVmMaximumFailureWindow?: pulumi.Input<number>;
```


The length of the reset window in
which `ha_vm_maximum_resets` can operate. When this
window expires, no more resets are attempted regardless of the setting
configured in `ha_vm_maximum_resets`. `-1` means no window, meaning an
unlimited reset time is allotted. The value is specified in seconds. Default:
`-1` (no window).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1127">property haVmMaximumResets</a>
</h3>

```typescript
haVmMaximumResets?: pulumi.Input<number>;
```


The maximum number of resets that HA will
perform to a virtual machine when responding to a failure event. Default: `3`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1133">property haVmMinimumUptime</a>
</h3>

```typescript
haVmMinimumUptime?: pulumi.Input<number>;
```


The time, in seconds, that HA waits after
powering on a virtual machine before monitoring for heartbeats. Default:
`120` (2 minutes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1139">property haVmMonitoring</a>
</h3>

```typescript
haVmMonitoring?: pulumi.Input<string>;
```


The type of virtual machine monitoring to use
when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
`vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1145">property haVmRestartAdditionalDelay</a>
</h3>

```typescript
haVmRestartAdditionalDelay?: pulumi.Input<number>;
```


Additional delay in seconds
after ready condition is met. A VM is considered ready at this point.
Default: `0` (no delay). <sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1151">property haVmRestartPriority</a>
</h3>

```typescript
haVmRestartPriority?: pulumi.Input<string>;
```


The default restart priority
for affected virtual machines when vSphere detects a host failure. Can be one
of `lowest`, `low`, `medium`, `high`, or `highest`. Default: `medium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1158">property haVmRestartTimeout</a>
</h3>

```typescript
haVmRestartTimeout?: pulumi.Input<number>;
```


The maximum time, in seconds,
that vSphere HA will wait for virtual machines in one priority to be ready
before proceeding with the next priority. Default: `600` (10 minutes).
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1164">property hostClusterExitTimeout</a>
</h3>

```typescript
hostClusterExitTimeout?: pulumi.Input<number>;
```


The timeout for each host maintenance mode
operation when removing hosts from a cluster. The value is specified in
seconds. Default: `3600` (1 hour).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1169">property hostSystemIds</a>
</h3>

```typescript
hostSystemIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The [managed object IDs][docs-about-morefs] of
the hosts to put in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1173">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1180">property proactiveHaAutomationLevel</a>
</h3>

```typescript
proactiveHaAutomationLevel?: pulumi.Input<string>;
```


Determines how the host
quarantine, maintenance mode, or virtual machine migration recommendations
made by proactive HA are to be handled. Can be one of `Automated` or
`Manual`. Default: `Manual`. <sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1185">property proactiveHaEnabled</a>
</h3>

```typescript
proactiveHaEnabled?: pulumi.Input<boolean>;
```


Enables Proactive HA. Default: `false`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1194">property proactiveHaModerateRemediation</a>
</h3>

```typescript
proactiveHaModerateRemediation?: pulumi.Input<string>;
```


The configured remediation
for moderately degraded hosts. Can be one of `MaintenanceMode` or
`QuarantineMode`. Note that this cannot be set to `MaintenanceMode` when
`proactive_ha_severe_remediation` is set
to `QuarantineMode`. Default: `QuarantineMode`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1200">property proactiveHaProviderIds</a>
</h3>

```typescript
proactiveHaProviderIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of IDs for health update
providers configured for this cluster.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1209">property proactiveHaSevereRemediation</a>
</h3>

```typescript
proactiveHaSevereRemediation?: pulumi.Input<string>;
```


The configured remediation for
severely degraded hosts. Can be one of `MaintenanceMode` or `QuarantineMode`.
Note that this cannot be set to `QuarantineMode` when
`proactive_ha_moderate_remediation` is
set to `MaintenanceMode`. Default: `QuarantineMode`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L1214">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h2 class="pdoc-module-header" id="ComputeClusterHostGroupArgs">
<a class="pdoc-member-name" href="/computeClusterHostGroup.ts#L110">interface ComputeClusterHostGroupArgs</a>
</h2>

The set of arguments for constructing a ComputeClusterHostGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterHostGroup.ts#L116">property computeClusterId</a>
</h3>

```typescript
computeClusterId: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterHostGroup.ts#L121">property hostSystemIds</a>
</h3>

```typescript
hostSystemIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The [managed object IDs][docs-about-morefs] of
the hosts to put in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterHostGroup.ts#L126">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the host group. This must be unique in the
cluster. Forces a new resource if changed.

<h2 class="pdoc-module-header" id="ComputeClusterHostGroupState">
<a class="pdoc-member-name" href="/computeClusterHostGroup.ts#L88">interface ComputeClusterHostGroupState</a>
</h2>

Input properties used for looking up and filtering ComputeClusterHostGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterHostGroup.ts#L94">property computeClusterId</a>
</h3>

```typescript
computeClusterId?: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterHostGroup.ts#L99">property hostSystemIds</a>
</h3>

```typescript
hostSystemIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The [managed object IDs][docs-about-morefs] of
the hosts to put in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterHostGroup.ts#L104">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the host group. This must be unique in the
cluster. Forces a new resource if changed.

<h2 class="pdoc-module-header" id="ComputeClusterState">
<a class="pdoc-member-name" href="/computeCluster.ts#L524">interface ComputeClusterState</a>
</h2>

Input properties used for looking up and filtering ComputeCluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L531">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


A map of custom attribute ids to attribute
value strings to set for the datastore cluster. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L536">property datacenterId</a>
</h3>

```typescript
datacenterId?: pulumi.Input<string>;
```


The [managed object ID][docs-about-morefs] of
the datacenter to create the cluster in. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L542">property dpmAutomationLevel</a>
</h3>

```typescript
dpmAutomationLevel?: pulumi.Input<string>;
```


The automation level for host power
operations in this cluster. Can be one of `manual` or `automated`. Default:
`manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L548">property dpmEnabled</a>
</h3>

```typescript
dpmEnabled?: pulumi.Input<boolean>;
```


Enable DPM support for DRS in this cluster.
Requires `drs_enabled` to be `true` in order to be effective.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L555">property dpmThreshold</a>
</h3>

```typescript
dpmThreshold?: pulumi.Input<number>;
```


A value between `1` and `5` indicating the
threshold of load within the cluster that influences host power operations.
This affects both power on and power off operations - a lower setting will
tolerate more of a surplus/deficit than a higher setting. Default: `3`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L560">property drsAdvancedOptions</a>
</h3>

```typescript
drsAdvancedOptions?: pulumi.Input<{ ... }>;
```


A key/value map that specifies advanced
options for DRS and DPM.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L566">property drsAutomationLevel</a>
</h3>

```typescript
drsAutomationLevel?: pulumi.Input<string>;
```


The default automation level for all
virtual machines in this cluster. Can be one of `manual`,
`partiallyAutomated`, or `fullyAutomated`. Default: `manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L572">property drsEnablePredictiveDrs</a>
</h3>

```typescript
drsEnablePredictiveDrs?: pulumi.Input<boolean>;
```


When `true`, enables DRS to use data
from [vRealize Operations Manager][ref-vsphere-vro] to make proactive DRS
recommendations. <sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L577">property drsEnableVmOverrides</a>
</h3>

```typescript
drsEnableVmOverrides?: pulumi.Input<boolean>;
```


Allow individual DRS overrides to be
set for virtual machines in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L581">property drsEnabled</a>
</h3>

```typescript
drsEnabled?: pulumi.Input<boolean>;
```


Enable DRS for this cluster. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L588">property drsMigrationThreshold</a>
</h3>

```typescript
drsMigrationThreshold?: pulumi.Input<number>;
```


A value between `1` and `5` indicating
the threshold of imbalance tolerated between hosts. A lower setting will
tolerate more imbalance while a higher setting will tolerate less. Default:
`3`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L597">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The relative path to a folder to put this cluster in.
This is a path relative to the datacenter you are deploying the cluster to.
Example: for the `dc1` datacenter, and a provided `folder` of `foo/bar`,
Terraform will place a cluster named `terraform-compute-cluster-test` in a
host folder located at `/dc1/host/foo/bar`, with the final inventory path
being `/dc1/host/foo/bar/terraform-datastore-cluster-test`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L605">property forceEvacuateOnDestroy</a>
</h3>

```typescript
forceEvacuateOnDestroy?: pulumi.Input<boolean>;
```


When destroying the resource, setting this to
`true` will auto-remove any hosts that are currently a member of the cluster,
as if they were removed by taking their entry out of `host_system_ids` (see
below). This is an advanced
option and should only be used for testing. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L613">property haAdmissionControlFailoverHostSystemIds</a>
</h3>

```typescript
haAdmissionControlFailoverHostSystemIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Defines the
[managed object IDs][docs-about-morefs] of hosts to use as dedicated failover
hosts. These hosts are kept as available as possible - admission control will
block access to the host, and DRS will ignore the host when making
recommendations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L621">property haAdmissionControlHostFailureTolerance</a>
</h3>

```typescript
haAdmissionControlHostFailureTolerance?: pulumi.Input<number>;
```


The maximum number
of failed hosts that admission control tolerates when making decisions on
whether to permit virtual machine operations. The maximum is one less than
the number of hosts in the cluster. Default: `1`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L628">property haAdmissionControlPerformanceTolerance</a>
</h3>

```typescript
haAdmissionControlPerformanceTolerance?: pulumi.Input<number>;
```


The percentage of
resource reduction that a cluster of virtual machines can tolerate in case of
a failover. A value of 0 produces warnings only, whereas a value of 100
disables the setting. Default: `100` (disabled).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L634">property haAdmissionControlPolicy</a>
</h3>

```typescript
haAdmissionControlPolicy?: pulumi.Input<string>;
```


The type of admission control
policy to use with vSphere HA. Can be one of `resourcePercentage`,
`slotPolicy`, `failoverHosts`, or `disabled`. Default: `resourcePercentage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L644">property haAdmissionControlResourcePercentageAutoCompute</a>
</h3>

```typescript
haAdmissionControlResourcePercentageAutoCompute?: pulumi.Input<boolean>;
```


Automatically determine available resource percentages by subtracting the
average number of host resources represented by the
`ha_admission_control_host_failure_tolerance`
setting from the total amount of resources in the cluster. Disable to supply
user-defined values. Default: `true`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L650">property haAdmissionControlResourcePercentageCpu</a>
</h3>

```typescript
haAdmissionControlResourcePercentageCpu?: pulumi.Input<number>;
```


Controls the
user-defined percentage of CPU resources in the cluster to reserve for
failover. Default: `100`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L656">property haAdmissionControlResourcePercentageMemory</a>
</h3>

```typescript
haAdmissionControlResourcePercentageMemory?: pulumi.Input<number>;
```


Controls the
user-defined percentage of memory resources in the cluster to reserve for
failover. Default: `100`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L661">property haAdmissionControlSlotPolicyExplicitCpu</a>
</h3>

```typescript
haAdmissionControlSlotPolicyExplicitCpu?: pulumi.Input<number>;
```


Controls the
user-defined CPU slot size, in MHz. Default: `32`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L666">property haAdmissionControlSlotPolicyExplicitMemory</a>
</h3>

```typescript
haAdmissionControlSlotPolicyExplicitMemory?: pulumi.Input<number>;
```


Controls the
user-defined memory slot size, in MB. Default: `100`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L673">property haAdmissionControlSlotPolicyUseExplicitSize</a>
</h3>

```typescript
haAdmissionControlSlotPolicyUseExplicitSize?: pulumi.Input<boolean>;
```


Controls
whether or not you wish to supply explicit values to CPU and memory slot
sizes. The default is `false`, which tells vSphere to gather a automatic
average based on all powered-on virtual machines currently in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L678">property haAdvancedOptions</a>
</h3>

```typescript
haAdvancedOptions?: pulumi.Input<{ ... }>;
```


A key/value map that specifies advanced
options for vSphere HA.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L685">property haDatastoreApdRecoveryAction</a>
</h3>

```typescript
haDatastoreApdRecoveryAction?: pulumi.Input<string>;
```


Controls the action to take
on virtual machines if an APD status on an affected datastore clears in the
middle of an APD event. Can be one of `none` or `reset`. Default: `none`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L693">property haDatastoreApdResponse</a>
</h3>

```typescript
haDatastoreApdResponse?: pulumi.Input<string>;
```


Controls the action to take on
virtual machines when the cluster has detected loss to all paths to a
relevant datastore. Can be one of `disabled`, `warning`,
`restartConservative`, or `restartAggressive`.  Default: `disabled`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L700">property haDatastoreApdResponseDelay</a>
</h3>

```typescript
haDatastoreApdResponseDelay?: pulumi.Input<number>;
```


Controls the delay in minutes
to wait after an APD timeout event to execute the response action defined in
`ha_datastore_apd_response`. Default: `3`
minutes. <sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L708">property haDatastorePdlResponse</a>
</h3>

```typescript
haDatastorePdlResponse?: pulumi.Input<string>;
```


Controls the action to take on
virtual machines when the cluster has detected a permanent device loss to a
relevant datastore. Can be one of `disabled`, `warning`, or
`restartAggressive`. Default: `disabled`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L713">property haEnabled</a>
</h3>

```typescript
haEnabled?: pulumi.Input<boolean>;
```


Enable vSphere HA for this cluster. Default:
`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L720">property haHeartbeatDatastoreIds</a>
</h3>

```typescript
haHeartbeatDatastoreIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of managed object IDs for
preferred datastores to use for HA heartbeating. This setting is only useful
when `ha_heartbeat_datastore_policy` is set
to either `userSelectedDs` or `allFeasibleDsWithUserPreference`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L727">property haHeartbeatDatastorePolicy</a>
</h3>

```typescript
haHeartbeatDatastorePolicy?: pulumi.Input<string>;
```


The selection policy for HA
heartbeat datastores. Can be one of `allFeasibleDs`, `userSelectedDs`, or
`allFeasibleDsWithUserPreference`. Default:
`allFeasibleDsWithUserPreference`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L734">property haHostIsolationResponse</a>
</h3>

```typescript
haHostIsolationResponse?: pulumi.Input<string>;
```


The action to take on virtual
machines when a host has detected that it has been isolated from the rest of
the cluster. Can be one of `none`, `powerOff`, or `shutdown`. Default:
`none`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L740">property haHostMonitoring</a>
</h3>

```typescript
haHostMonitoring?: pulumi.Input<string>;
```


Global setting that controls whether
vSphere HA remediates virtual machines on host failure. Can be one of `enabled`
or `disabled`. Default: `enabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L747">property haVmComponentProtection</a>
</h3>

```typescript
haVmComponentProtection?: pulumi.Input<string>;
```


Controls vSphere VM component
protection for virtual machines in this cluster. Can be one of `enabled` or
`disabled`. Default: `enabled`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L757">property haVmDependencyRestartCondition</a>
</h3>

```typescript
haVmDependencyRestartCondition?: pulumi.Input<string>;
```


The condition used to
determine whether or not virtual machines in a certain restart priority class
are online, allowing HA to move on to restarting virtual machines on the next
priority. Can be one of `none`, `poweredOn`, `guestHbStatusGreen`, or
`appHbStatusGreen`. The default is `none`, which means that a virtual machine
is considered ready immediately after a host is found to start it on.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L763">property haVmFailureInterval</a>
</h3>

```typescript
haVmFailureInterval?: pulumi.Input<number>;
```


If a heartbeat from a virtual machine
is not received within this configured interval, the virtual machine is
marked as failed. The value is in seconds. Default: `30`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L772">property haVmMaximumFailureWindow</a>
</h3>

```typescript
haVmMaximumFailureWindow?: pulumi.Input<number>;
```


The length of the reset window in
which `ha_vm_maximum_resets` can operate. When this
window expires, no more resets are attempted regardless of the setting
configured in `ha_vm_maximum_resets`. `-1` means no window, meaning an
unlimited reset time is allotted. The value is specified in seconds. Default:
`-1` (no window).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L777">property haVmMaximumResets</a>
</h3>

```typescript
haVmMaximumResets?: pulumi.Input<number>;
```


The maximum number of resets that HA will
perform to a virtual machine when responding to a failure event. Default: `3`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L783">property haVmMinimumUptime</a>
</h3>

```typescript
haVmMinimumUptime?: pulumi.Input<number>;
```


The time, in seconds, that HA waits after
powering on a virtual machine before monitoring for heartbeats. Default:
`120` (2 minutes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L789">property haVmMonitoring</a>
</h3>

```typescript
haVmMonitoring?: pulumi.Input<string>;
```


The type of virtual machine monitoring to use
when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
`vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L795">property haVmRestartAdditionalDelay</a>
</h3>

```typescript
haVmRestartAdditionalDelay?: pulumi.Input<number>;
```


Additional delay in seconds
after ready condition is met. A VM is considered ready at this point.
Default: `0` (no delay). <sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L801">property haVmRestartPriority</a>
</h3>

```typescript
haVmRestartPriority?: pulumi.Input<string>;
```


The default restart priority
for affected virtual machines when vSphere detects a host failure. Can be one
of `lowest`, `low`, `medium`, `high`, or `highest`. Default: `medium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L808">property haVmRestartTimeout</a>
</h3>

```typescript
haVmRestartTimeout?: pulumi.Input<number>;
```


The maximum time, in seconds,
that vSphere HA will wait for virtual machines in one priority to be ready
before proceeding with the next priority. Default: `600` (10 minutes).
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L814">property hostClusterExitTimeout</a>
</h3>

```typescript
hostClusterExitTimeout?: pulumi.Input<number>;
```


The timeout for each host maintenance mode
operation when removing hosts from a cluster. The value is specified in
seconds. Default: `3600` (1 hour).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L819">property hostSystemIds</a>
</h3>

```typescript
hostSystemIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The [managed object IDs][docs-about-morefs] of
the hosts to put in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L823">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L830">property proactiveHaAutomationLevel</a>
</h3>

```typescript
proactiveHaAutomationLevel?: pulumi.Input<string>;
```


Determines how the host
quarantine, maintenance mode, or virtual machine migration recommendations
made by proactive HA are to be handled. Can be one of `Automated` or
`Manual`. Default: `Manual`. <sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L835">property proactiveHaEnabled</a>
</h3>

```typescript
proactiveHaEnabled?: pulumi.Input<boolean>;
```


Enables Proactive HA. Default: `false`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L844">property proactiveHaModerateRemediation</a>
</h3>

```typescript
proactiveHaModerateRemediation?: pulumi.Input<string>;
```


The configured remediation
for moderately degraded hosts. Can be one of `MaintenanceMode` or
`QuarantineMode`. Note that this cannot be set to `MaintenanceMode` when
`proactive_ha_severe_remediation` is set
to `QuarantineMode`. Default: `QuarantineMode`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L850">property proactiveHaProviderIds</a>
</h3>

```typescript
proactiveHaProviderIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of IDs for health update
providers configured for this cluster.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L859">property proactiveHaSevereRemediation</a>
</h3>

```typescript
proactiveHaSevereRemediation?: pulumi.Input<string>;
```


The configured remediation for
severely degraded hosts. Can be one of `MaintenanceMode` or `QuarantineMode`.
Note that this cannot be set to `QuarantineMode` when
`proactive_ha_moderate_remediation` is
set to `MaintenanceMode`. Default: `QuarantineMode`.
<sup>\*</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L863">property resourcePoolId</a>
</h3>

```typescript
resourcePoolId?: pulumi.Input<string>;
```


The managed object ID of the cluster's root resource pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeCluster.ts#L868">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h2 class="pdoc-module-header" id="ComputeClusterVmAffinityRuleArgs">
<a class="pdoc-member-name" href="/computeClusterVmAffinityRule.ts#L140">interface ComputeClusterVmAffinityRuleArgs</a>
</h2>

The set of arguments for constructing a ComputeClusterVmAffinityRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAffinityRule.ts#L146">property computeClusterId</a>
</h3>

```typescript
computeClusterId: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAffinityRule.ts#L150">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Enable this rule in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAffinityRule.ts#L155">property mandatory</a>
</h3>

```typescript
mandatory?: pulumi.Input<boolean>;
```


When this value is `true`, prevents any virtual
machine operations that may violate this rule. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAffinityRule.ts#L159">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule. This must be unique in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAffinityRule.ts#L164">property virtualMachineIds</a>
</h3>

```typescript
virtualMachineIds: pulumi.Input<pulumi.Input<string>[]>;
```


The UUIDs of the virtual machines to run
on the same host together.

<h2 class="pdoc-module-header" id="ComputeClusterVmAffinityRuleState">
<a class="pdoc-member-name" href="/computeClusterVmAffinityRule.ts#L110">interface ComputeClusterVmAffinityRuleState</a>
</h2>

Input properties used for looking up and filtering ComputeClusterVmAffinityRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAffinityRule.ts#L116">property computeClusterId</a>
</h3>

```typescript
computeClusterId?: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAffinityRule.ts#L120">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Enable this rule in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAffinityRule.ts#L125">property mandatory</a>
</h3>

```typescript
mandatory?: pulumi.Input<boolean>;
```


When this value is `true`, prevents any virtual
machine operations that may violate this rule. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAffinityRule.ts#L129">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule. This must be unique in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAffinityRule.ts#L134">property virtualMachineIds</a>
</h3>

```typescript
virtualMachineIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The UUIDs of the virtual machines to run
on the same host together.

<h2 class="pdoc-module-header" id="ComputeClusterVmAntiAffinityRuleArgs">
<a class="pdoc-member-name" href="/computeClusterVmAntiAffinityRule.ts#L141">interface ComputeClusterVmAntiAffinityRuleArgs</a>
</h2>

The set of arguments for constructing a ComputeClusterVmAntiAffinityRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAntiAffinityRule.ts#L147">property computeClusterId</a>
</h3>

```typescript
computeClusterId: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAntiAffinityRule.ts#L151">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Enable this rule in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAntiAffinityRule.ts#L156">property mandatory</a>
</h3>

```typescript
mandatory?: pulumi.Input<boolean>;
```


When this value is `true`, prevents any virtual
machine operations that may violate this rule. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAntiAffinityRule.ts#L160">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule. This must be unique in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAntiAffinityRule.ts#L165">property virtualMachineIds</a>
</h3>

```typescript
virtualMachineIds: pulumi.Input<pulumi.Input<string>[]>;
```


The UUIDs of the virtual machines to run
on hosts different from each other.

<h2 class="pdoc-module-header" id="ComputeClusterVmAntiAffinityRuleState">
<a class="pdoc-member-name" href="/computeClusterVmAntiAffinityRule.ts#L111">interface ComputeClusterVmAntiAffinityRuleState</a>
</h2>

Input properties used for looking up and filtering ComputeClusterVmAntiAffinityRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAntiAffinityRule.ts#L117">property computeClusterId</a>
</h3>

```typescript
computeClusterId?: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAntiAffinityRule.ts#L121">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Enable this rule in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAntiAffinityRule.ts#L126">property mandatory</a>
</h3>

```typescript
mandatory?: pulumi.Input<boolean>;
```


When this value is `true`, prevents any virtual
machine operations that may violate this rule. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAntiAffinityRule.ts#L130">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule. This must be unique in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmAntiAffinityRule.ts#L135">property virtualMachineIds</a>
</h3>

```typescript
virtualMachineIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The UUIDs of the virtual machines to run
on hosts different from each other.

<h2 class="pdoc-module-header" id="ComputeClusterVmDependencyRuleArgs">
<a class="pdoc-member-name" href="/computeClusterVmDependencyRule.ts#L157">interface ComputeClusterVmDependencyRuleArgs</a>
</h2>

The set of arguments for constructing a ComputeClusterVmDependencyRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L163">property computeClusterId</a>
</h3>

```typescript
computeClusterId: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L170">property dependencyVmGroupName</a>
</h3>

```typescript
dependencyVmGroupName: pulumi.Input<string>;
```


The name of the VM group that this
rule depends on. The VMs defined in the group specified by
`vm_group_name` will not be started until the VMs in this
group are started.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L174">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Enable this rule in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L179">property mandatory</a>
</h3>

```typescript
mandatory?: pulumi.Input<boolean>;
```


When this value is `true`, prevents any virtual
machine operations that may violate this rule. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L184">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule. This must be unique in the
cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L191">property vmGroupName</a>
</h3>

```typescript
vmGroupName: pulumi.Input<string>;
```


The name of the VM group that is the subject of
this rule. The VMs defined in this group will not be started until the VMs in
the group specified by
`dependency_vm_group_name` are started.

<h2 class="pdoc-module-header" id="ComputeClusterVmDependencyRuleState">
<a class="pdoc-member-name" href="/computeClusterVmDependencyRule.ts#L117">interface ComputeClusterVmDependencyRuleState</a>
</h2>

Input properties used for looking up and filtering ComputeClusterVmDependencyRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L123">property computeClusterId</a>
</h3>

```typescript
computeClusterId?: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L130">property dependencyVmGroupName</a>
</h3>

```typescript
dependencyVmGroupName?: pulumi.Input<string>;
```


The name of the VM group that this
rule depends on. The VMs defined in the group specified by
`vm_group_name` will not be started until the VMs in this
group are started.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L134">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Enable this rule in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L139">property mandatory</a>
</h3>

```typescript
mandatory?: pulumi.Input<boolean>;
```


When this value is `true`, prevents any virtual
machine operations that may violate this rule. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L144">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule. This must be unique in the
cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmDependencyRule.ts#L151">property vmGroupName</a>
</h3>

```typescript
vmGroupName?: pulumi.Input<string>;
```


The name of the VM group that is the subject of
this rule. The VMs defined in this group will not be started until the VMs in
the group specified by
`dependency_vm_group_name` are started.

<h2 class="pdoc-module-header" id="ComputeClusterVmGroupArgs">
<a class="pdoc-member-name" href="/computeClusterVmGroup.ts#L112">interface ComputeClusterVmGroupArgs</a>
</h2>

The set of arguments for constructing a ComputeClusterVmGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmGroup.ts#L118">property computeClusterId</a>
</h3>

```typescript
computeClusterId: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmGroup.ts#L123">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the VM group. This must be unique in the
cluster. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmGroup.ts#L128">property virtualMachineIds</a>
</h3>

```typescript
virtualMachineIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The UUIDs of the virtual machines in this
group.

<h2 class="pdoc-module-header" id="ComputeClusterVmGroupState">
<a class="pdoc-member-name" href="/computeClusterVmGroup.ts#L90">interface ComputeClusterVmGroupState</a>
</h2>

Input properties used for looking up and filtering ComputeClusterVmGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmGroup.ts#L96">property computeClusterId</a>
</h3>

```typescript
computeClusterId?: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmGroup.ts#L101">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the VM group. This must be unique in the
cluster. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmGroup.ts#L106">property virtualMachineIds</a>
</h3>

```typescript
virtualMachineIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The UUIDs of the virtual machines in this
group.

<h2 class="pdoc-module-header" id="ComputeClusterVmHostRuleArgs">
<a class="pdoc-member-name" href="/computeClusterVmHostRule.ts#L167">interface ComputeClusterVmHostRuleArgs</a>
</h2>

The set of arguments for constructing a ComputeClusterVmHostRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L173">property affinityHostGroupName</a>
</h3>

```typescript
affinityHostGroupName?: pulumi.Input<string>;
```


When this field is used, the virtual
machines defined in `vm_group_name` will be run on the
hosts defined in this host group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L179">property antiAffinityHostGroupName</a>
</h3>

```typescript
antiAffinityHostGroupName?: pulumi.Input<string>;
```


When this field is used, the
virtual machines defined in `vm_group_name` will _not_ be
run on the hosts defined in this host group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L185">property computeClusterId</a>
</h3>

```typescript
computeClusterId: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L189">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Enable this rule in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L194">property mandatory</a>
</h3>

```typescript
mandatory?: pulumi.Input<boolean>;
```


When this value is `true`, prevents any virtual
machine operations that may violate this rule. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L199">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule. This must be unique in the
cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L204">property vmGroupName</a>
</h3>

```typescript
vmGroupName: pulumi.Input<string>;
```


The name of the virtual machine group to use
with this rule.

<h2 class="pdoc-module-header" id="ComputeClusterVmHostRuleState">
<a class="pdoc-member-name" href="/computeClusterVmHostRule.ts#L124">interface ComputeClusterVmHostRuleState</a>
</h2>

Input properties used for looking up and filtering ComputeClusterVmHostRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L130">property affinityHostGroupName</a>
</h3>

```typescript
affinityHostGroupName?: pulumi.Input<string>;
```


When this field is used, the virtual
machines defined in `vm_group_name` will be run on the
hosts defined in this host group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L136">property antiAffinityHostGroupName</a>
</h3>

```typescript
antiAffinityHostGroupName?: pulumi.Input<string>;
```


When this field is used, the
virtual machines defined in `vm_group_name` will _not_ be
run on the hosts defined in this host group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L142">property computeClusterId</a>
</h3>

```typescript
computeClusterId?: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the group in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L146">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Enable this rule in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L151">property mandatory</a>
</h3>

```typescript
mandatory?: pulumi.Input<boolean>;
```


When this value is `true`, prevents any virtual
machine operations that may violate this rule. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L156">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule. This must be unique in the
cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/computeClusterVmHostRule.ts#L161">property vmGroupName</a>
</h3>

```typescript
vmGroupName?: pulumi.Input<string>;
```


The name of the virtual machine group to use
with this rule.

<h2 class="pdoc-module-header" id="CustomAttributeArgs">
<a class="pdoc-member-name" href="/customAttribute.ts#L87">interface CustomAttributeArgs</a>
</h2>

The set of arguments for constructing a CustomAttribute resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/customAttribute.ts#L94">property managedObjectType</a>
</h3>

```typescript
managedObjectType?: pulumi.Input<string>;
```


The object type that this attribute may be
applied to. If not set, the custom attribute may be applied to any object
type. For a full list, click here. Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/customAttribute.ts#L98">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the custom attribute.

<h2 class="pdoc-module-header" id="CustomAttributeState">
<a class="pdoc-member-name" href="/customAttribute.ts#L70">interface CustomAttributeState</a>
</h2>

Input properties used for looking up and filtering CustomAttribute resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/customAttribute.ts#L77">property managedObjectType</a>
</h3>

```typescript
managedObjectType?: pulumi.Input<string>;
```


The object type that this attribute may be
applied to. If not set, the custom attribute may be applied to any object
type. For a full list, click here. Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/customAttribute.ts#L81">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the custom attribute.

<h2 class="pdoc-module-header" id="DatacenterArgs">
<a class="pdoc-member-name" href="/datacenter.ts#L114">interface DatacenterArgs</a>
</h2>

The set of arguments for constructing a Datacenter resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datacenter.ts#L121">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


Map of custom attribute ids to value
strings to set for datacenter resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datacenter.ts#L126">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The folder where the datacenter should be created.
Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datacenter.ts#L131">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the datacenter. This name needs to be unique
within the folder. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datacenter.ts#L136">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h2 class="pdoc-module-header" id="DatacenterState">
<a class="pdoc-member-name" href="/datacenter.ts#L82">interface DatacenterState</a>
</h2>

Input properties used for looking up and filtering Datacenter resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datacenter.ts#L89">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


Map of custom attribute ids to value
strings to set for datacenter resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datacenter.ts#L94">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The folder where the datacenter should be created.
Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datacenter.ts#L98">property moid</a>
</h3>

```typescript
moid?: pulumi.Input<string>;
```


[Managed object ID][docs-about-morefs] of this datacenter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datacenter.ts#L103">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the datacenter. This name needs to be unique
within the folder. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datacenter.ts#L108">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h2 class="pdoc-module-header" id="DatastoreClusterArgs">
<a class="pdoc-member-name" href="/datastoreCluster.ts#L405">interface DatastoreClusterArgs</a>
</h2>

The set of arguments for constructing a DatastoreCluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L412">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


A map of custom attribute ids to attribute
value strings to set for the datastore cluster. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L418">property datacenterId</a>
</h3>

```typescript
datacenterId: pulumi.Input<string>;
```


The [managed object ID][docs-about-morefs] of
the datacenter to create the datastore cluster in. Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L428">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The relative path to a folder to put this datastore
cluster in.  This is a path relative to the datacenter you are deploying the
datastore to.  Example: for the `dc1` datacenter, and a provided `folder` of
`foo/bar`, Terraform will place a datastore cluster named
`terraform-datastore-cluster-test` in a datastore folder located at
`/dc1/datastore/foo/bar`, with the final inventory path being
`/dc1/datastore/foo/bar/terraform-datastore-cluster-test`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L432">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the datastore cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L437">property sdrsAdvancedOptions</a>
</h3>

```typescript
sdrsAdvancedOptions?: pulumi.Input<{ ... }>;
```


A key/value map of advanced Storage DRS
settings that are not exposed via Terraform or the vSphere client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L442">property sdrsAutomationLevel</a>
</h3>

```typescript
sdrsAutomationLevel?: pulumi.Input<string>;
```


The global automation level for all
virtual machines in this datastore cluster. Default: `manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L447">property sdrsDefaultIntraVmAffinity</a>
</h3>

```typescript
sdrsDefaultIntraVmAffinity?: pulumi.Input<boolean>;
```


When `true`, all disks in a
single virtual machine will be kept on the same datastore. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L452">property sdrsEnabled</a>
</h3>

```typescript
sdrsEnabled?: pulumi.Input<boolean>;
```


Enable Storage DRS for this datastore cluster.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L459">property sdrsFreeSpaceThreshold</a>
</h3>

```typescript
sdrsFreeSpaceThreshold?: pulumi.Input<number>;
```


The free space threshold to use.
When set to `utilization`, `drs_space_utilization_threshold` is used, and
when set to `freeSpace`, `drs_free_space_threshold` is used. Default:
`utilization`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L464">property sdrsFreeSpaceThresholdMode</a>
</h3>

```typescript
sdrsFreeSpaceThresholdMode?: pulumi.Input<string>;
```


The free space threshold to use. When set to utilization, drs_space_utilization_threshold is used, and when set to
freeSpace, drs_free_space_threshold is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L470">property sdrsFreeSpaceUtilizationDifference</a>
</h3>

```typescript
sdrsFreeSpaceUtilizationDifference?: pulumi.Input<number>;
```


The threshold, in
percent, of difference between space utilization in datastores before storage
DRS makes decisions to balance the space. Default: `5` percent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L475">property sdrsIoBalanceAutomationLevel</a>
</h3>

```typescript
sdrsIoBalanceAutomationLevel?: pulumi.Input<string>;
```


Overrides the default
automation settings when correcting I/O load imbalances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L481">property sdrsIoLatencyThreshold</a>
</h3>

```typescript
sdrsIoLatencyThreshold?: pulumi.Input<number>;
```


The I/O latency threshold, in
milliseconds, that storage DRS uses to make recommendations to move disks
from this datastore. Default: `15` seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L486">property sdrsIoLoadBalanceEnabled</a>
</h3>

```typescript
sdrsIoLoadBalanceEnabled?: pulumi.Input<boolean>;
```


Enable I/O load balancing for
this datastore cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L492">property sdrsIoLoadImbalanceThreshold</a>
</h3>

```typescript
sdrsIoLoadImbalanceThreshold?: pulumi.Input<number>;
```


The difference between load
in datastores in the cluster before storage DRS makes recommendations to
balance the load. Default: `5` percent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L501">property sdrsIoReservableIopsThreshold</a>
</h3>

```typescript
sdrsIoReservableIopsThreshold?: pulumi.Input<number>;
```


The threshold of reservable
IOPS of all virtual machines on the datastore before storage DRS makes
recommendations to move VMs off of a datastore. Note that this setting should
only be set if `sdrs_io_reservable_percent_threshold` cannot make an accurate
estimate of the capacity of the datastores in your cluster, and should be set
to roughly 50-60% of the worst case peak performance of the backing LUNs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L508">property sdrsIoReservablePercentThreshold</a>
</h3>

```typescript
sdrsIoReservablePercentThreshold?: pulumi.Input<number>;
```


The threshold, in
percent, of actual estimated performance of the datastore (in IOPS) that
storage DRS uses to make recommendations to move VMs off of a datastore when
the total reservable IOPS exceeds the threshold. Default: `60` percent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L515">property sdrsIoReservableThresholdMode</a>
</h3>

```typescript
sdrsIoReservableThresholdMode?: pulumi.Input<string>;
```


The reservable IOPS
threshold setting to use, `sdrs_io_reservable_percent_threshold` in the event
of `automatic`, or `sdrs_io_reservable_iops_threshold` in the event of
`manual`. Default: `automatic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L520">property sdrsLoadBalanceInterval</a>
</h3>

```typescript
sdrsLoadBalanceInterval?: pulumi.Input<number>;
```


The storage DRS poll interval, in
minutes. Default: `480` minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L525">property sdrsPolicyEnforcementAutomationLevel</a>
</h3>

```typescript
sdrsPolicyEnforcementAutomationLevel?: pulumi.Input<string>;
```


Overrides the default
automation settings when correcting storage and VM policy violations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L530">property sdrsRuleEnforcementAutomationLevel</a>
</h3>

```typescript
sdrsRuleEnforcementAutomationLevel?: pulumi.Input<string>;
```


Overrides the default
automation settings when correcting affinity rule violations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L535">property sdrsSpaceBalanceAutomationLevel</a>
</h3>

```typescript
sdrsSpaceBalanceAutomationLevel?: pulumi.Input<string>;
```


Overrides the default
automation settings when correcting disk space imbalances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L539">property sdrsSpaceUtilizationThreshold</a>
</h3>

```typescript
sdrsSpaceUtilizationThreshold?: pulumi.Input<number>;
```


The threshold, in percent of used space, that storage DRS uses to make decisions to migrate VMs out of a datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L544">property sdrsVmEvacuationAutomationLevel</a>
</h3>

```typescript
sdrsVmEvacuationAutomationLevel?: pulumi.Input<string>;
```


Overrides the default
automation settings when generating recommendations for datastore evacuation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L549">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h2 class="pdoc-module-header" id="DatastoreClusterState">
<a class="pdoc-member-name" href="/datastoreCluster.ts#L255">interface DatastoreClusterState</a>
</h2>

Input properties used for looking up and filtering DatastoreCluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L262">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


A map of custom attribute ids to attribute
value strings to set for the datastore cluster. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L268">property datacenterId</a>
</h3>

```typescript
datacenterId?: pulumi.Input<string>;
```


The [managed object ID][docs-about-morefs] of
the datacenter to create the datastore cluster in. Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L278">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The relative path to a folder to put this datastore
cluster in.  This is a path relative to the datacenter you are deploying the
datastore to.  Example: for the `dc1` datacenter, and a provided `folder` of
`foo/bar`, Terraform will place a datastore cluster named
`terraform-datastore-cluster-test` in a datastore folder located at
`/dc1/datastore/foo/bar`, with the final inventory path being
`/dc1/datastore/foo/bar/terraform-datastore-cluster-test`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L282">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the datastore cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L287">property sdrsAdvancedOptions</a>
</h3>

```typescript
sdrsAdvancedOptions?: pulumi.Input<{ ... }>;
```


A key/value map of advanced Storage DRS
settings that are not exposed via Terraform or the vSphere client.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L292">property sdrsAutomationLevel</a>
</h3>

```typescript
sdrsAutomationLevel?: pulumi.Input<string>;
```


The global automation level for all
virtual machines in this datastore cluster. Default: `manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L297">property sdrsDefaultIntraVmAffinity</a>
</h3>

```typescript
sdrsDefaultIntraVmAffinity?: pulumi.Input<boolean>;
```


When `true`, all disks in a
single virtual machine will be kept on the same datastore. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L302">property sdrsEnabled</a>
</h3>

```typescript
sdrsEnabled?: pulumi.Input<boolean>;
```


Enable Storage DRS for this datastore cluster.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L309">property sdrsFreeSpaceThreshold</a>
</h3>

```typescript
sdrsFreeSpaceThreshold?: pulumi.Input<number>;
```


The free space threshold to use.
When set to `utilization`, `drs_space_utilization_threshold` is used, and
when set to `freeSpace`, `drs_free_space_threshold` is used. Default:
`utilization`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L314">property sdrsFreeSpaceThresholdMode</a>
</h3>

```typescript
sdrsFreeSpaceThresholdMode?: pulumi.Input<string>;
```


The free space threshold to use. When set to utilization, drs_space_utilization_threshold is used, and when set to
freeSpace, drs_free_space_threshold is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L320">property sdrsFreeSpaceUtilizationDifference</a>
</h3>

```typescript
sdrsFreeSpaceUtilizationDifference?: pulumi.Input<number>;
```


The threshold, in
percent, of difference between space utilization in datastores before storage
DRS makes decisions to balance the space. Default: `5` percent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L325">property sdrsIoBalanceAutomationLevel</a>
</h3>

```typescript
sdrsIoBalanceAutomationLevel?: pulumi.Input<string>;
```


Overrides the default
automation settings when correcting I/O load imbalances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L331">property sdrsIoLatencyThreshold</a>
</h3>

```typescript
sdrsIoLatencyThreshold?: pulumi.Input<number>;
```


The I/O latency threshold, in
milliseconds, that storage DRS uses to make recommendations to move disks
from this datastore. Default: `15` seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L336">property sdrsIoLoadBalanceEnabled</a>
</h3>

```typescript
sdrsIoLoadBalanceEnabled?: pulumi.Input<boolean>;
```


Enable I/O load balancing for
this datastore cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L342">property sdrsIoLoadImbalanceThreshold</a>
</h3>

```typescript
sdrsIoLoadImbalanceThreshold?: pulumi.Input<number>;
```


The difference between load
in datastores in the cluster before storage DRS makes recommendations to
balance the load. Default: `5` percent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L351">property sdrsIoReservableIopsThreshold</a>
</h3>

```typescript
sdrsIoReservableIopsThreshold?: pulumi.Input<number>;
```


The threshold of reservable
IOPS of all virtual machines on the datastore before storage DRS makes
recommendations to move VMs off of a datastore. Note that this setting should
only be set if `sdrs_io_reservable_percent_threshold` cannot make an accurate
estimate of the capacity of the datastores in your cluster, and should be set
to roughly 50-60% of the worst case peak performance of the backing LUNs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L358">property sdrsIoReservablePercentThreshold</a>
</h3>

```typescript
sdrsIoReservablePercentThreshold?: pulumi.Input<number>;
```


The threshold, in
percent, of actual estimated performance of the datastore (in IOPS) that
storage DRS uses to make recommendations to move VMs off of a datastore when
the total reservable IOPS exceeds the threshold. Default: `60` percent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L365">property sdrsIoReservableThresholdMode</a>
</h3>

```typescript
sdrsIoReservableThresholdMode?: pulumi.Input<string>;
```


The reservable IOPS
threshold setting to use, `sdrs_io_reservable_percent_threshold` in the event
of `automatic`, or `sdrs_io_reservable_iops_threshold` in the event of
`manual`. Default: `automatic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L370">property sdrsLoadBalanceInterval</a>
</h3>

```typescript
sdrsLoadBalanceInterval?: pulumi.Input<number>;
```


The storage DRS poll interval, in
minutes. Default: `480` minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L375">property sdrsPolicyEnforcementAutomationLevel</a>
</h3>

```typescript
sdrsPolicyEnforcementAutomationLevel?: pulumi.Input<string>;
```


Overrides the default
automation settings when correcting storage and VM policy violations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L380">property sdrsRuleEnforcementAutomationLevel</a>
</h3>

```typescript
sdrsRuleEnforcementAutomationLevel?: pulumi.Input<string>;
```


Overrides the default
automation settings when correcting affinity rule violations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L385">property sdrsSpaceBalanceAutomationLevel</a>
</h3>

```typescript
sdrsSpaceBalanceAutomationLevel?: pulumi.Input<string>;
```


Overrides the default
automation settings when correcting disk space imbalances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L389">property sdrsSpaceUtilizationThreshold</a>
</h3>

```typescript
sdrsSpaceUtilizationThreshold?: pulumi.Input<number>;
```


The threshold, in percent of used space, that storage DRS uses to make decisions to migrate VMs out of a datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L394">property sdrsVmEvacuationAutomationLevel</a>
</h3>

```typescript
sdrsVmEvacuationAutomationLevel?: pulumi.Input<string>;
```


Overrides the default
automation settings when generating recommendations for datastore evacuation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreCluster.ts#L399">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h2 class="pdoc-module-header" id="DatastoreClusterVmAntiAffinityRuleArgs">
<a class="pdoc-member-name" href="/datastoreClusterVmAntiAffinityRule.ts#L133">interface DatastoreClusterVmAntiAffinityRuleArgs</a>
</h2>

The set of arguments for constructing a DatastoreClusterVmAntiAffinityRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreClusterVmAntiAffinityRule.ts#L139">property datastoreClusterId</a>
</h3>

```typescript
datastoreClusterId: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the datastore cluster to put the group in.  Forces
a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreClusterVmAntiAffinityRule.ts#L143">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Enable this rule in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreClusterVmAntiAffinityRule.ts#L148">property mandatory</a>
</h3>

```typescript
mandatory?: pulumi.Input<boolean>;
```


When this value is `true`, prevents any virtual
machine operations that may violate this rule. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreClusterVmAntiAffinityRule.ts#L152">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule. This must be unique in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreClusterVmAntiAffinityRule.ts#L157">property virtualMachineIds</a>
</h3>

```typescript
virtualMachineIds: pulumi.Input<pulumi.Input<string>[]>;
```


The UUIDs of the virtual machines to run
on different datastores from each other.

<h2 class="pdoc-module-header" id="DatastoreClusterVmAntiAffinityRuleState">
<a class="pdoc-member-name" href="/datastoreClusterVmAntiAffinityRule.ts#L103">interface DatastoreClusterVmAntiAffinityRuleState</a>
</h2>

Input properties used for looking up and filtering DatastoreClusterVmAntiAffinityRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreClusterVmAntiAffinityRule.ts#L109">property datastoreClusterId</a>
</h3>

```typescript
datastoreClusterId?: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the datastore cluster to put the group in.  Forces
a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreClusterVmAntiAffinityRule.ts#L113">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Enable this rule in the cluster. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreClusterVmAntiAffinityRule.ts#L118">property mandatory</a>
</h3>

```typescript
mandatory?: pulumi.Input<boolean>;
```


When this value is `true`, prevents any virtual
machine operations that may violate this rule. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreClusterVmAntiAffinityRule.ts#L122">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the rule. This must be unique in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/datastoreClusterVmAntiAffinityRule.ts#L127">property virtualMachineIds</a>
</h3>

```typescript
virtualMachineIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The UUIDs of the virtual machines to run
on different datastores from each other.

<h2 class="pdoc-module-header" id="DistributedPortGroupArgs">
<a class="pdoc-member-name" href="/distributedPortGroup.ts#L606">interface DistributedPortGroupArgs</a>
</h2>

The set of arguments for constructing a DistributedPortGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L610">property activeUplinks</a>
</h3>

```typescript
activeUplinks?: pulumi.Input<pulumi.Input<string>[]>;
```


List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L615">property allowForgedTransmits</a>
</h3>

```typescript
allowForgedTransmits?: pulumi.Input<boolean>;
```


Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address
than that of its own.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L619">property allowMacChanges</a>
</h3>

```typescript
allowMacChanges?: pulumi.Input<boolean>;
```


Controls whether or not the Media Access Control (MAC) address can be changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L623">property allowPromiscuous</a>
</h3>

```typescript
allowPromiscuous?: pulumi.Input<boolean>;
```


Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L628">property autoExpand</a>
</h3>

```typescript
autoExpand?: pulumi.Input<boolean>;
```


Allows the port group to create additional ports
past the limit specified in `number_of_ports` if necessary. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L632">property blockAllPorts</a>
</h3>

```typescript
blockAllPorts?: pulumi.Input<boolean>;
```


Indicates whether to block all ports by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L637">property blockOverrideAllowed</a>
</h3>

```typescript
blockOverrideAllowed?: pulumi.Input<boolean>;
```


Allow the [port shutdown
policy][port-shutdown-policy] to be overridden on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L641">property checkBeacon</a>
</h3>

```typescript
checkBeacon?: pulumi.Input<boolean>;
```


Enable beacon probing on the ports this policy applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L647">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


Map of custom attribute ids to attribute
value string to set for port group. See [here][docs-setting-custom-attributes]
for a reference on how to set values for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L651">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


An optional description for the port group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L655">property directpathGen2Allowed</a>
</h3>

```typescript
directpathGen2Allowed?: pulumi.Input<boolean>;
```


Allow VMDirectPath Gen2 on the ports this policy applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L660">property distributedVirtualSwitchUuid</a>
</h3>

```typescript
distributedVirtualSwitchUuid: pulumi.Input<string>;
```


The ID of the DVS to add the
port group to. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L664">property egressShapingAverageBandwidth</a>
</h3>

```typescript
egressShapingAverageBandwidth?: pulumi.Input<number>;
```


The average egress bandwidth in bits per second if egress shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L668">property egressShapingBurstSize</a>
</h3>

```typescript
egressShapingBurstSize?: pulumi.Input<number>;
```


The maximum egress burst size allowed in bytes if egress shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L672">property egressShapingEnabled</a>
</h3>

```typescript
egressShapingEnabled?: pulumi.Input<boolean>;
```


True if the traffic shaper is enabled for egress traffic on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L676">property egressShapingPeakBandwidth</a>
</h3>

```typescript
egressShapingPeakBandwidth?: pulumi.Input<number>;
```


The peak egress bandwidth during bursts in bits per second if egress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L680">property failback</a>
</h3>

```typescript
failback?: pulumi.Input<boolean>;
```


If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L684">property ingressShapingAverageBandwidth</a>
</h3>

```typescript
ingressShapingAverageBandwidth?: pulumi.Input<number>;
```


The average ingress bandwidth in bits per second if ingress shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L688">property ingressShapingBurstSize</a>
</h3>

```typescript
ingressShapingBurstSize?: pulumi.Input<number>;
```


The maximum ingress burst size allowed in bytes if ingress shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L692">property ingressShapingEnabled</a>
</h3>

```typescript
ingressShapingEnabled?: pulumi.Input<boolean>;
```


True if the traffic shaper is enabled for ingress traffic on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L696">property ingressShapingPeakBandwidth</a>
</h3>

```typescript
ingressShapingPeakBandwidth?: pulumi.Input<number>;
```


The peak ingress bandwidth during bursts in bits per second if ingress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L700">property lacpEnabled</a>
</h3>

```typescript
lacpEnabled?: pulumi.Input<boolean>;
```


Whether or not to enable LACP on all uplink ports.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L704">property lacpMode</a>
</h3>

```typescript
lacpMode?: pulumi.Input<string>;
```


The uplink LACP mode to use. Can be one of active or passive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L709">property livePortMovingAllowed</a>
</h3>

```typescript
livePortMovingAllowed?: pulumi.Input<boolean>;
```


Allow a port in this port group to be
moved to another port group while it is connected.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L713">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the port group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L717">property netflowEnabled</a>
</h3>

```typescript
netflowEnabled?: pulumi.Input<boolean>;
```


Indicates whether to enable netflow on all ports.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L723">property netflowOverrideAllowed</a>
</h3>

```typescript
netflowOverrideAllowed?: pulumi.Input<boolean>;
```


Allow the [Netflow
policy][netflow-policy] on this port group to be overridden on an individual
port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L729">property networkResourcePoolKey</a>
</h3>

```typescript
networkResourcePoolKey?: pulumi.Input<string>;
```


The key of a network resource pool
to associate with this port group. The default is `-1`, which implies no
association.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L734">property networkResourcePoolOverrideAllowed</a>
</h3>

```typescript
networkResourcePoolOverrideAllowed?: pulumi.Input<boolean>;
```


Allow the network
resource pool set on this port group to be overridden on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L738">property notifySwitches</a>
</h3>

```typescript
notifySwitches?: pulumi.Input<boolean>;
```


If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L743">property numberOfPorts</a>
</h3>

```typescript
numberOfPorts?: pulumi.Input<number>;
```


The number of ports available on this port
group. Cannot be decreased below the amount of used ports on the port group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L748">property portConfigResetAtDisconnect</a>
</h3>

```typescript
portConfigResetAtDisconnect?: pulumi.Input<boolean>;
```


Reset a port's settings to the
settings defined on this port group policy when the port disconnects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L754">property portNameFormat</a>
</h3>

```typescript
portNameFormat?: pulumi.Input<string>;
```


An optional formatting policy for naming of
the ports in this port group. See the `portNameFormat` attribute listed
[here][ext-vsphere-portname-format] for details on the format syntax.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L758">property portPrivateSecondaryVlanId</a>
</h3>

```typescript
portPrivateSecondaryVlanId?: pulumi.Input<number>;
```


The secondary VLAN ID for this port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L764">property securityPolicyOverrideAllowed</a>
</h3>

```typescript
securityPolicyOverrideAllowed?: pulumi.Input<boolean>;
```


Allow the [security policy
settings][sec-policy-settings] defined in this port group policy to be
overridden on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L770">property shapingOverrideAllowed</a>
</h3>

```typescript
shapingOverrideAllowed?: pulumi.Input<boolean>;
```


Allow the [traffic shaping
options][traffic-shaping-settings] on this port group policy to be overridden
on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L774">property standbyUplinks</a>
</h3>

```typescript
standbyUplinks?: pulumi.Input<pulumi.Input<string>[]>;
```


List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L778">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of tag IDs to apply to this object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L783">property teamingPolicy</a>
</h3>

```typescript
teamingPolicy?: pulumi.Input<string>;
```


The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid,
failover_explicit, or loadbalance_loadbased.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L788">property trafficFilterOverrideAllowed</a>
</h3>

```typescript
trafficFilterOverrideAllowed?: pulumi.Input<boolean>;
```


Allow any traffic filters on
this port group to be overridden on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L793">property txUplink</a>
</h3>

```typescript
txUplink?: pulumi.Input<boolean>;
```


If true, a copy of packets sent to the switch will always be forwarded to an uplink in addition to the regular
packet forwarded done by the switch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L798">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The port group type. Can be one of `earlyBinding` (static
binding) or `ephemeral`. Default: `earlyBinding`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L804">property uplinkTeamingOverrideAllowed</a>
</h3>

```typescript
uplinkTeamingOverrideAllowed?: pulumi.Input<boolean>;
```


Allow the [uplink teaming
options][uplink-teaming-settings] on this port group to be overridden on an
individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L808">property vlanId</a>
</h3>

```typescript
vlanId?: pulumi.Input<number>;
```


The VLAN ID for single VLAN mode. 0 denotes no VLAN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L813">property vlanOverrideAllowed</a>
</h3>

```typescript
vlanOverrideAllowed?: pulumi.Input<boolean>;
```


Allow the [VLAN settings][vlan-settings]
on this port group to be overridden on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L817">property vlanRanges</a>
</h3>

```typescript
vlanRanges?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The VLAN ID for single VLAN mode. 0 denotes no VLAN.

<h2 class="pdoc-module-header" id="DistributedPortGroupState">
<a class="pdoc-member-name" href="/distributedPortGroup.ts#L381">interface DistributedPortGroupState</a>
</h2>

Input properties used for looking up and filtering DistributedPortGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L385">property activeUplinks</a>
</h3>

```typescript
activeUplinks?: pulumi.Input<pulumi.Input<string>[]>;
```


List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L390">property allowForgedTransmits</a>
</h3>

```typescript
allowForgedTransmits?: pulumi.Input<boolean>;
```


Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address
than that of its own.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L394">property allowMacChanges</a>
</h3>

```typescript
allowMacChanges?: pulumi.Input<boolean>;
```


Controls whether or not the Media Access Control (MAC) address can be changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L398">property allowPromiscuous</a>
</h3>

```typescript
allowPromiscuous?: pulumi.Input<boolean>;
```


Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L403">property autoExpand</a>
</h3>

```typescript
autoExpand?: pulumi.Input<boolean>;
```


Allows the port group to create additional ports
past the limit specified in `number_of_ports` if necessary. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L407">property blockAllPorts</a>
</h3>

```typescript
blockAllPorts?: pulumi.Input<boolean>;
```


Indicates whether to block all ports by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L412">property blockOverrideAllowed</a>
</h3>

```typescript
blockOverrideAllowed?: pulumi.Input<boolean>;
```


Allow the [port shutdown
policy][port-shutdown-policy] to be overridden on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L416">property checkBeacon</a>
</h3>

```typescript
checkBeacon?: pulumi.Input<boolean>;
```


Enable beacon probing on the ports this policy applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L420">property configVersion</a>
</h3>

```typescript
configVersion?: pulumi.Input<string>;
```


Version string of the configuration that this spec is trying to change.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L426">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


Map of custom attribute ids to attribute
value string to set for port group. See [here][docs-setting-custom-attributes]
for a reference on how to set values for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L430">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


An optional description for the port group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L434">property directpathGen2Allowed</a>
</h3>

```typescript
directpathGen2Allowed?: pulumi.Input<boolean>;
```


Allow VMDirectPath Gen2 on the ports this policy applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L439">property distributedVirtualSwitchUuid</a>
</h3>

```typescript
distributedVirtualSwitchUuid?: pulumi.Input<string>;
```


The ID of the DVS to add the
port group to. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L443">property egressShapingAverageBandwidth</a>
</h3>

```typescript
egressShapingAverageBandwidth?: pulumi.Input<number>;
```


The average egress bandwidth in bits per second if egress shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L447">property egressShapingBurstSize</a>
</h3>

```typescript
egressShapingBurstSize?: pulumi.Input<number>;
```


The maximum egress burst size allowed in bytes if egress shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L451">property egressShapingEnabled</a>
</h3>

```typescript
egressShapingEnabled?: pulumi.Input<boolean>;
```


True if the traffic shaper is enabled for egress traffic on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L455">property egressShapingPeakBandwidth</a>
</h3>

```typescript
egressShapingPeakBandwidth?: pulumi.Input<number>;
```


The peak egress bandwidth during bursts in bits per second if egress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L459">property failback</a>
</h3>

```typescript
failback?: pulumi.Input<boolean>;
```


If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L463">property ingressShapingAverageBandwidth</a>
</h3>

```typescript
ingressShapingAverageBandwidth?: pulumi.Input<number>;
```


The average ingress bandwidth in bits per second if ingress shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L467">property ingressShapingBurstSize</a>
</h3>

```typescript
ingressShapingBurstSize?: pulumi.Input<number>;
```


The maximum ingress burst size allowed in bytes if ingress shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L471">property ingressShapingEnabled</a>
</h3>

```typescript
ingressShapingEnabled?: pulumi.Input<boolean>;
```


True if the traffic shaper is enabled for ingress traffic on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L475">property ingressShapingPeakBandwidth</a>
</h3>

```typescript
ingressShapingPeakBandwidth?: pulumi.Input<number>;
```


The peak ingress bandwidth during bursts in bits per second if ingress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L479">property key</a>
</h3>

```typescript
key?: pulumi.Input<string>;
```


The generated UUID of the portgroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L483">property lacpEnabled</a>
</h3>

```typescript
lacpEnabled?: pulumi.Input<boolean>;
```


Whether or not to enable LACP on all uplink ports.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L487">property lacpMode</a>
</h3>

```typescript
lacpMode?: pulumi.Input<string>;
```


The uplink LACP mode to use. Can be one of active or passive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L492">property livePortMovingAllowed</a>
</h3>

```typescript
livePortMovingAllowed?: pulumi.Input<boolean>;
```


Allow a port in this port group to be
moved to another port group while it is connected.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L496">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the port group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L500">property netflowEnabled</a>
</h3>

```typescript
netflowEnabled?: pulumi.Input<boolean>;
```


Indicates whether to enable netflow on all ports.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L506">property netflowOverrideAllowed</a>
</h3>

```typescript
netflowOverrideAllowed?: pulumi.Input<boolean>;
```


Allow the [Netflow
policy][netflow-policy] on this port group to be overridden on an individual
port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L512">property networkResourcePoolKey</a>
</h3>

```typescript
networkResourcePoolKey?: pulumi.Input<string>;
```


The key of a network resource pool
to associate with this port group. The default is `-1`, which implies no
association.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L517">property networkResourcePoolOverrideAllowed</a>
</h3>

```typescript
networkResourcePoolOverrideAllowed?: pulumi.Input<boolean>;
```


Allow the network
resource pool set on this port group to be overridden on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L521">property notifySwitches</a>
</h3>

```typescript
notifySwitches?: pulumi.Input<boolean>;
```


If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L526">property numberOfPorts</a>
</h3>

```typescript
numberOfPorts?: pulumi.Input<number>;
```


The number of ports available on this port
group. Cannot be decreased below the amount of used ports on the port group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L531">property portConfigResetAtDisconnect</a>
</h3>

```typescript
portConfigResetAtDisconnect?: pulumi.Input<boolean>;
```


Reset a port's settings to the
settings defined on this port group policy when the port disconnects.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L537">property portNameFormat</a>
</h3>

```typescript
portNameFormat?: pulumi.Input<string>;
```


An optional formatting policy for naming of
the ports in this port group. See the `portNameFormat` attribute listed
[here][ext-vsphere-portname-format] for details on the format syntax.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L541">property portPrivateSecondaryVlanId</a>
</h3>

```typescript
portPrivateSecondaryVlanId?: pulumi.Input<number>;
```


The secondary VLAN ID for this port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L547">property securityPolicyOverrideAllowed</a>
</h3>

```typescript
securityPolicyOverrideAllowed?: pulumi.Input<boolean>;
```


Allow the [security policy
settings][sec-policy-settings] defined in this port group policy to be
overridden on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L553">property shapingOverrideAllowed</a>
</h3>

```typescript
shapingOverrideAllowed?: pulumi.Input<boolean>;
```


Allow the [traffic shaping
options][traffic-shaping-settings] on this port group policy to be overridden
on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L557">property standbyUplinks</a>
</h3>

```typescript
standbyUplinks?: pulumi.Input<pulumi.Input<string>[]>;
```


List of active uplinks used for load balancing, matching the names of the uplinks assigned in the DVS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L561">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of tag IDs to apply to this object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L566">property teamingPolicy</a>
</h3>

```typescript
teamingPolicy?: pulumi.Input<string>;
```


The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid,
failover_explicit, or loadbalance_loadbased.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L571">property trafficFilterOverrideAllowed</a>
</h3>

```typescript
trafficFilterOverrideAllowed?: pulumi.Input<boolean>;
```


Allow any traffic filters on
this port group to be overridden on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L576">property txUplink</a>
</h3>

```typescript
txUplink?: pulumi.Input<boolean>;
```


If true, a copy of packets sent to the switch will always be forwarded to an uplink in addition to the regular
packet forwarded done by the switch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L581">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The port group type. Can be one of `earlyBinding` (static
binding) or `ephemeral`. Default: `earlyBinding`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L587">property uplinkTeamingOverrideAllowed</a>
</h3>

```typescript
uplinkTeamingOverrideAllowed?: pulumi.Input<boolean>;
```


Allow the [uplink teaming
options][uplink-teaming-settings] on this port group to be overridden on an
individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L591">property vlanId</a>
</h3>

```typescript
vlanId?: pulumi.Input<number>;
```


The VLAN ID for single VLAN mode. 0 denotes no VLAN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L596">property vlanOverrideAllowed</a>
</h3>

```typescript
vlanOverrideAllowed?: pulumi.Input<boolean>;
```


Allow the [VLAN settings][vlan-settings]
on this port group to be overridden on an individual port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedPortGroup.ts#L600">property vlanRanges</a>
</h3>

```typescript
vlanRanges?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The VLAN ID for single VLAN mode. 0 denotes no VLAN.

<h2 class="pdoc-module-header" id="DistributedVirtualSwitchArgs">
<a class="pdoc-member-name" href="/distributedVirtualSwitch.ts#L1108">interface DistributedVirtualSwitchArgs</a>
</h2>

The set of arguments for constructing a DistributedVirtualSwitch resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1115">property activeUplinks</a>
</h3>

```typescript
activeUplinks?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of active uplinks to be used in load
balancing. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1121">property allowForgedTransmits</a>
</h3>

```typescript
allowForgedTransmits?: pulumi.Input<boolean>;
```


Controls whether or not a virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1126">property allowMacChanges</a>
</h3>

```typescript
allowMacChanges?: pulumi.Input<boolean>;
```


Controls whether or not the Media Access
Control (MAC) address can be changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1131">property allowPromiscuous</a>
</h3>

```typescript
allowPromiscuous?: pulumi.Input<boolean>;
```


Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1137">property blockAllPorts</a>
</h3>

```typescript
blockAllPorts?: pulumi.Input<boolean>;
```


Shuts down all ports in the port groups that
this policy applies to, effectively blocking all network access to connected
virtual devices.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1142">property checkBeacon</a>
</h3>

```typescript
checkBeacon?: pulumi.Input<boolean>;
```


Enables beacon probing as an additional measure
to detect NIC failure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1147">property contactDetail</a>
</h3>

```typescript
contactDetail?: pulumi.Input<string>;
```


The detailed contact information for the person
who is responsible for the DVS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1152">property contactName</a>
</h3>

```typescript
contactName?: pulumi.Input<string>;
```


The name of the person who is responsible for the
DVS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1159">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


Map of custom attribute ids to attribute
value strings to set for virtual switch. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1164">property datacenterId</a>
</h3>

```typescript
datacenterId: pulumi.Input<string>;
```


The ID of the datacenter where the distributed
virtual switch will be created. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1168">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A detailed description for the DVS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1173">property directpathGen2Allowed</a>
</h3>

```typescript
directpathGen2Allowed?: pulumi.Input<boolean>;
```


Allow VMDirectPath Gen2 for the ports
for which this policy applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1178">property egressShapingAverageBandwidth</a>
</h3>

```typescript
egressShapingAverageBandwidth?: pulumi.Input<number>;
```


The average bandwidth in bits
per second if egress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1183">property egressShapingBurstSize</a>
</h3>

```typescript
egressShapingBurstSize?: pulumi.Input<number>;
```


The maximum burst size allowed in
bytes if egress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1188">property egressShapingEnabled</a>
</h3>

```typescript
egressShapingEnabled?: pulumi.Input<boolean>;
```


`true` if the traffic shaper is enabled
on the port for egress traffic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1193">property egressShapingPeakBandwidth</a>
</h3>

```typescript
egressShapingPeakBandwidth?: pulumi.Input<number>;
```


The peak bandwidth during bursts
in bits per second if egress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1198">property failback</a>
</h3>

```typescript
failback?: pulumi.Input<boolean>;
```


If `true`, the teaming policy will re-activate failed
uplinks higher in precedence when they come back up.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1202">property faulttoleranceMaximumMbit</a>
</h3>

```typescript
faulttoleranceMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1206">property faulttoleranceReservationMbit</a>
</h3>

```typescript
faulttoleranceReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1210">property faulttoleranceShareCount</a>
</h3>

```typescript
faulttoleranceShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the faultTolerance traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1214">property faulttoleranceShareLevel</a>
</h3>

```typescript
faulttoleranceShareLevel?: pulumi.Input<string>;
```


The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1219">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The folder to create the DVS in. Forces a new resource
if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1223">property hbrMaximumMbit</a>
</h3>

```typescript
hbrMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the hbr traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1227">property hbrReservationMbit</a>
</h3>

```typescript
hbrReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1231">property hbrShareCount</a>
</h3>

```typescript
hbrShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the hbr traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1235">property hbrShareLevel</a>
</h3>

```typescript
hbrShareLevel?: pulumi.Input<string>;
```


The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1240">property hosts</a>
</h3>

```typescript
hosts?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Use the `host` block to declare a host specification. The
options are:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1245">property ingressShapingAverageBandwidth</a>
</h3>

```typescript
ingressShapingAverageBandwidth?: pulumi.Input<number>;
```


The average bandwidth in
bits per second if ingress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1250">property ingressShapingBurstSize</a>
</h3>

```typescript
ingressShapingBurstSize?: pulumi.Input<number>;
```


The maximum burst size allowed in
bytes if ingress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1255">property ingressShapingEnabled</a>
</h3>

```typescript
ingressShapingEnabled?: pulumi.Input<boolean>;
```


`true` if the traffic shaper is
enabled on the port for ingress traffic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1260">property ingressShapingPeakBandwidth</a>
</h3>

```typescript
ingressShapingPeakBandwidth?: pulumi.Input<number>;
```


The peak bandwidth during
bursts in bits per second if ingress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1266">property ipv4Address</a>
</h3>

```typescript
ipv4Address?: pulumi.Input<string>;
```


An IPv4 address to identify the switch. This is
mostly useful when used with the Netflow arguments found
below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1270">property iscsiMaximumMbit</a>
</h3>

```typescript
iscsiMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the iSCSI traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1274">property iscsiReservationMbit</a>
</h3>

```typescript
iscsiReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1278">property iscsiShareCount</a>
</h3>

```typescript
iscsiShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the iSCSI traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1282">property iscsiShareLevel</a>
</h3>

```typescript
iscsiShareLevel?: pulumi.Input<string>;
```


The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1288">property lacpApiVersion</a>
</h3>

```typescript
lacpApiVersion?: pulumi.Input<string>;
```


The Link Aggregation Control Protocol group
version to use with the switch. Possible values are `singleLag` and
`multipleLag`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1293">property lacpEnabled</a>
</h3>

```typescript
lacpEnabled?: pulumi.Input<boolean>;
```


Enables LACP for the ports that this policy
applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1297">property lacpMode</a>
</h3>

```typescript
lacpMode?: pulumi.Input<string>;
```


The LACP mode. Can be one of `active` or `passive`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1302">property linkDiscoveryOperation</a>
</h3>

```typescript
linkDiscoveryOperation?: pulumi.Input<string>;
```


Whether to `advertise` or `listen`
for link discovery traffic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1307">property linkDiscoveryProtocol</a>
</h3>

```typescript
linkDiscoveryProtocol?: pulumi.Input<string>;
```


The discovery protocol type. Valid
types are `cdp` and `lldp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1311">property managementMaximumMbit</a>
</h3>

```typescript
managementMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the management traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1315">property managementReservationMbit</a>
</h3>

```typescript
managementReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1319">property managementShareCount</a>
</h3>

```typescript
managementShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the management traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1323">property managementShareLevel</a>
</h3>

```typescript
managementShareLevel?: pulumi.Input<string>;
```


The allocation level for the management traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1328">property maxMtu</a>
</h3>

```typescript
maxMtu?: pulumi.Input<number>;
```


The maximum transmission unit (MTU) for the virtual
switch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1333">property multicastFilteringMode</a>
</h3>

```typescript
multicastFilteringMode?: pulumi.Input<string>;
```


The multicast filtering mode to use
with the switch. Can be one of `legacyFiltering` or `snooping`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1337">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the distributed virtual switch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1343">property netflowActiveFlowTimeout</a>
</h3>

```typescript
netflowActiveFlowTimeout?: pulumi.Input<number>;
```


The number of seconds after which
active flows are forced to be exported to the collector. Allowed range is
`60` to `3600`. Default: `60`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1349">property netflowCollectorIpAddress</a>
</h3>

```typescript
netflowCollectorIpAddress?: pulumi.Input<string>;
```


IP address for the Netflow
collector, using IPv4 or IPv6. IPv6 is supported in vSphere Distributed
Switch Version 6.0 or later. Must be set before Netflow can be enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1354">property netflowCollectorPort</a>
</h3>

```typescript
netflowCollectorPort?: pulumi.Input<number>;
```


Port for the Netflow collector. This
must be set before Netflow can be enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1359">property netflowEnabled</a>
</h3>

```typescript
netflowEnabled?: pulumi.Input<boolean>;
```


Enables Netflow on all ports that this policy
applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1365">property netflowIdleFlowTimeout</a>
</h3>

```typescript
netflowIdleFlowTimeout?: pulumi.Input<number>;
```


The number of seconds after which
idle flows are forced to be exported to the collector. Allowed range is `10`
to `600`. Default: `15`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1371">property netflowInternalFlowsOnly</a>
</h3>

```typescript
netflowInternalFlowsOnly?: pulumi.Input<boolean>;
```


Whether to limit analysis to
traffic that has both source and destination served by the same host.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1376">property netflowObservationDomainId</a>
</h3>

```typescript
netflowObservationDomainId?: pulumi.Input<number>;
```


The observation domain ID for
the Netflow collector.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1383">property netflowSamplingRate</a>
</h3>

```typescript
netflowSamplingRate?: pulumi.Input<number>;
```


The ratio of total number of packets to
the number of packets analyzed. The default is `0`, which indicates that the
switch should analyze all packets. The maximum value is `1000`, which
indicates an analysis rate of 0.001%.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1388">property networkResourceControlEnabled</a>
</h3>

```typescript
networkResourceControlEnabled?: pulumi.Input<boolean>;
```


Set to `true` to enable
network I/O control. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1393">property networkResourceControlVersion</a>
</h3>

```typescript
networkResourceControlVersion?: pulumi.Input<string>;
```


The version of network I/O
control to use. Can be one of `version2` or `version3`. Default: `version2`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1397">property nfsMaximumMbit</a>
</h3>

```typescript
nfsMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the nfs traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1401">property nfsReservationMbit</a>
</h3>

```typescript
nfsReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1405">property nfsShareCount</a>
</h3>

```typescript
nfsShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the nfs traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1409">property nfsShareLevel</a>
</h3>

```typescript
nfsShareLevel?: pulumi.Input<string>;
```


The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1414">property notifySwitches</a>
</h3>

```typescript
notifySwitches?: pulumi.Input<boolean>;
```


If `true`, the teaming policy will notify the
broadcast network of an uplink failover, triggering cache updates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1419">property portPrivateSecondaryVlanId</a>
</h3>

```typescript
portPrivateSecondaryVlanId?: pulumi.Input<number>;
```


Used to define a secondary VLAN
ID when using private VLANs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1426">property standbyUplinks</a>
</h3>

```typescript
standbyUplinks?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of standby uplinks to be used in
failover. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1431">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1437">property teamingPolicy</a>
</h3>

```typescript
teamingPolicy?: pulumi.Input<string>;
```


The uplink teaming policy. Can be one of
`loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1442">property txUplink</a>
</h3>

```typescript
txUplink?: pulumi.Input<boolean>;
```


Forward all traffic transmitted by ports for which
this policy applies to its DVS uplinks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1450">property uplinks</a>
</h3>

```typescript
uplinks?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of strings that uniquely identifies the names
of the uplinks on the DVS across hosts. The number of items in this list
controls the number of uplinks that exist on the DVS, in addition to the
names.  See here for an example on how to
use this option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1454">property vdpMaximumMbit</a>
</h3>

```typescript
vdpMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the vdp traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1458">property vdpReservationMbit</a>
</h3>

```typescript
vdpReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1462">property vdpShareCount</a>
</h3>

```typescript
vdpShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the vdp traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1466">property vdpShareLevel</a>
</h3>

```typescript
vdpShareLevel?: pulumi.Input<string>;
```


The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1473">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


- The version of the DVS to create. The default is to
create the DVS at the latest version supported by the version of vSphere
being used. A DVS can be upgraded to another version, but cannot be
downgraded.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1477">property virtualmachineMaximumMbit</a>
</h3>

```typescript
virtualmachineMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1481">property virtualmachineReservationMbit</a>
</h3>

```typescript
virtualmachineReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1485">property virtualmachineShareCount</a>
</h3>

```typescript
virtualmachineShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the virtualMachine traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1489">property virtualmachineShareLevel</a>
</h3>

```typescript
virtualmachineShareLevel?: pulumi.Input<string>;
```


The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1493">property vlanId</a>
</h3>

```typescript
vlanId?: pulumi.Input<number>;
```


The VLAN ID for single VLAN mode. 0 denotes no VLAN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1500">property vlanRanges</a>
</h3>

```typescript
vlanRanges?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Used to denote VLAN trunking. Use the `min_vlan`
and `max_vlan` sub-arguments to define the tagged VLAN range. Multiple
`vlan_range` definitions are allowed, but they must not overlap. Example
below:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1504">property vmotionMaximumMbit</a>
</h3>

```typescript
vmotionMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the vmotion traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1508">property vmotionReservationMbit</a>
</h3>

```typescript
vmotionReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1512">property vmotionShareCount</a>
</h3>

```typescript
vmotionShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the vmotion traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1516">property vmotionShareLevel</a>
</h3>

```typescript
vmotionShareLevel?: pulumi.Input<string>;
```


The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1520">property vsanMaximumMbit</a>
</h3>

```typescript
vsanMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the vsan traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1524">property vsanReservationMbit</a>
</h3>

```typescript
vsanReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1528">property vsanShareCount</a>
</h3>

```typescript
vsanShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the vsan traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1532">property vsanShareLevel</a>
</h3>

```typescript
vsanShareLevel?: pulumi.Input<string>;
```


The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom.

<h2 class="pdoc-module-header" id="DistributedVirtualSwitchState">
<a class="pdoc-member-name" href="/distributedVirtualSwitch.ts#L674">interface DistributedVirtualSwitchState</a>
</h2>

Input properties used for looking up and filtering DistributedVirtualSwitch resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L681">property activeUplinks</a>
</h3>

```typescript
activeUplinks?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of active uplinks to be used in load
balancing. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L687">property allowForgedTransmits</a>
</h3>

```typescript
allowForgedTransmits?: pulumi.Input<boolean>;
```


Controls whether or not a virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L692">property allowMacChanges</a>
</h3>

```typescript
allowMacChanges?: pulumi.Input<boolean>;
```


Controls whether or not the Media Access
Control (MAC) address can be changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L697">property allowPromiscuous</a>
</h3>

```typescript
allowPromiscuous?: pulumi.Input<boolean>;
```


Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L703">property blockAllPorts</a>
</h3>

```typescript
blockAllPorts?: pulumi.Input<boolean>;
```


Shuts down all ports in the port groups that
this policy applies to, effectively blocking all network access to connected
virtual devices.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L708">property checkBeacon</a>
</h3>

```typescript
checkBeacon?: pulumi.Input<boolean>;
```


Enables beacon probing as an additional measure
to detect NIC failure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L712">property configVersion</a>
</h3>

```typescript
configVersion?: pulumi.Input<string>;
```


The version string of the configuration that this spec is trying to change.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L717">property contactDetail</a>
</h3>

```typescript
contactDetail?: pulumi.Input<string>;
```


The detailed contact information for the person
who is responsible for the DVS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L722">property contactName</a>
</h3>

```typescript
contactName?: pulumi.Input<string>;
```


The name of the person who is responsible for the
DVS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L729">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


Map of custom attribute ids to attribute
value strings to set for virtual switch. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L734">property datacenterId</a>
</h3>

```typescript
datacenterId?: pulumi.Input<string>;
```


The ID of the datacenter where the distributed
virtual switch will be created. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L738">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A detailed description for the DVS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L743">property directpathGen2Allowed</a>
</h3>

```typescript
directpathGen2Allowed?: pulumi.Input<boolean>;
```


Allow VMDirectPath Gen2 for the ports
for which this policy applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L748">property egressShapingAverageBandwidth</a>
</h3>

```typescript
egressShapingAverageBandwidth?: pulumi.Input<number>;
```


The average bandwidth in bits
per second if egress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L753">property egressShapingBurstSize</a>
</h3>

```typescript
egressShapingBurstSize?: pulumi.Input<number>;
```


The maximum burst size allowed in
bytes if egress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L758">property egressShapingEnabled</a>
</h3>

```typescript
egressShapingEnabled?: pulumi.Input<boolean>;
```


`true` if the traffic shaper is enabled
on the port for egress traffic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L763">property egressShapingPeakBandwidth</a>
</h3>

```typescript
egressShapingPeakBandwidth?: pulumi.Input<number>;
```


The peak bandwidth during bursts
in bits per second if egress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L768">property failback</a>
</h3>

```typescript
failback?: pulumi.Input<boolean>;
```


If `true`, the teaming policy will re-activate failed
uplinks higher in precedence when they come back up.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L772">property faulttoleranceMaximumMbit</a>
</h3>

```typescript
faulttoleranceMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the faultTolerance traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L776">property faulttoleranceReservationMbit</a>
</h3>

```typescript
faulttoleranceReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the faultTolerance traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L780">property faulttoleranceShareCount</a>
</h3>

```typescript
faulttoleranceShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the faultTolerance traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L784">property faulttoleranceShareLevel</a>
</h3>

```typescript
faulttoleranceShareLevel?: pulumi.Input<string>;
```


The allocation level for the faultTolerance traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L789">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The folder to create the DVS in. Forces a new resource
if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L793">property hbrMaximumMbit</a>
</h3>

```typescript
hbrMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the hbr traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L797">property hbrReservationMbit</a>
</h3>

```typescript
hbrReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the hbr traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L801">property hbrShareCount</a>
</h3>

```typescript
hbrShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the hbr traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L805">property hbrShareLevel</a>
</h3>

```typescript
hbrShareLevel?: pulumi.Input<string>;
```


The allocation level for the hbr traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L810">property hosts</a>
</h3>

```typescript
hosts?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Use the `host` block to declare a host specification. The
options are:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L815">property ingressShapingAverageBandwidth</a>
</h3>

```typescript
ingressShapingAverageBandwidth?: pulumi.Input<number>;
```


The average bandwidth in
bits per second if ingress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L820">property ingressShapingBurstSize</a>
</h3>

```typescript
ingressShapingBurstSize?: pulumi.Input<number>;
```


The maximum burst size allowed in
bytes if ingress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L825">property ingressShapingEnabled</a>
</h3>

```typescript
ingressShapingEnabled?: pulumi.Input<boolean>;
```


`true` if the traffic shaper is
enabled on the port for ingress traffic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L830">property ingressShapingPeakBandwidth</a>
</h3>

```typescript
ingressShapingPeakBandwidth?: pulumi.Input<number>;
```


The peak bandwidth during
bursts in bits per second if ingress traffic shaping is enabled on the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L836">property ipv4Address</a>
</h3>

```typescript
ipv4Address?: pulumi.Input<string>;
```


An IPv4 address to identify the switch. This is
mostly useful when used with the Netflow arguments found
below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L840">property iscsiMaximumMbit</a>
</h3>

```typescript
iscsiMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the iSCSI traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L844">property iscsiReservationMbit</a>
</h3>

```typescript
iscsiReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the iSCSI traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L848">property iscsiShareCount</a>
</h3>

```typescript
iscsiShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the iSCSI traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L852">property iscsiShareLevel</a>
</h3>

```typescript
iscsiShareLevel?: pulumi.Input<string>;
```


The allocation level for the iSCSI traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L858">property lacpApiVersion</a>
</h3>

```typescript
lacpApiVersion?: pulumi.Input<string>;
```


The Link Aggregation Control Protocol group
version to use with the switch. Possible values are `singleLag` and
`multipleLag`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L863">property lacpEnabled</a>
</h3>

```typescript
lacpEnabled?: pulumi.Input<boolean>;
```


Enables LACP for the ports that this policy
applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L867">property lacpMode</a>
</h3>

```typescript
lacpMode?: pulumi.Input<string>;
```


The LACP mode. Can be one of `active` or `passive`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L872">property linkDiscoveryOperation</a>
</h3>

```typescript
linkDiscoveryOperation?: pulumi.Input<string>;
```


Whether to `advertise` or `listen`
for link discovery traffic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L877">property linkDiscoveryProtocol</a>
</h3>

```typescript
linkDiscoveryProtocol?: pulumi.Input<string>;
```


The discovery protocol type. Valid
types are `cdp` and `lldp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L881">property managementMaximumMbit</a>
</h3>

```typescript
managementMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the management traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L885">property managementReservationMbit</a>
</h3>

```typescript
managementReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the management traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L889">property managementShareCount</a>
</h3>

```typescript
managementShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the management traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L893">property managementShareLevel</a>
</h3>

```typescript
managementShareLevel?: pulumi.Input<string>;
```


The allocation level for the management traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L898">property maxMtu</a>
</h3>

```typescript
maxMtu?: pulumi.Input<number>;
```


The maximum transmission unit (MTU) for the virtual
switch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L903">property multicastFilteringMode</a>
</h3>

```typescript
multicastFilteringMode?: pulumi.Input<string>;
```


The multicast filtering mode to use
with the switch. Can be one of `legacyFiltering` or `snooping`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L907">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the distributed virtual switch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L913">property netflowActiveFlowTimeout</a>
</h3>

```typescript
netflowActiveFlowTimeout?: pulumi.Input<number>;
```


The number of seconds after which
active flows are forced to be exported to the collector. Allowed range is
`60` to `3600`. Default: `60`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L919">property netflowCollectorIpAddress</a>
</h3>

```typescript
netflowCollectorIpAddress?: pulumi.Input<string>;
```


IP address for the Netflow
collector, using IPv4 or IPv6. IPv6 is supported in vSphere Distributed
Switch Version 6.0 or later. Must be set before Netflow can be enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L924">property netflowCollectorPort</a>
</h3>

```typescript
netflowCollectorPort?: pulumi.Input<number>;
```


Port for the Netflow collector. This
must be set before Netflow can be enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L929">property netflowEnabled</a>
</h3>

```typescript
netflowEnabled?: pulumi.Input<boolean>;
```


Enables Netflow on all ports that this policy
applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L935">property netflowIdleFlowTimeout</a>
</h3>

```typescript
netflowIdleFlowTimeout?: pulumi.Input<number>;
```


The number of seconds after which
idle flows are forced to be exported to the collector. Allowed range is `10`
to `600`. Default: `15`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L941">property netflowInternalFlowsOnly</a>
</h3>

```typescript
netflowInternalFlowsOnly?: pulumi.Input<boolean>;
```


Whether to limit analysis to
traffic that has both source and destination served by the same host.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L946">property netflowObservationDomainId</a>
</h3>

```typescript
netflowObservationDomainId?: pulumi.Input<number>;
```


The observation domain ID for
the Netflow collector.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L953">property netflowSamplingRate</a>
</h3>

```typescript
netflowSamplingRate?: pulumi.Input<number>;
```


The ratio of total number of packets to
the number of packets analyzed. The default is `0`, which indicates that the
switch should analyze all packets. The maximum value is `1000`, which
indicates an analysis rate of 0.001%.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L958">property networkResourceControlEnabled</a>
</h3>

```typescript
networkResourceControlEnabled?: pulumi.Input<boolean>;
```


Set to `true` to enable
network I/O control. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L963">property networkResourceControlVersion</a>
</h3>

```typescript
networkResourceControlVersion?: pulumi.Input<string>;
```


The version of network I/O
control to use. Can be one of `version2` or `version3`. Default: `version2`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L967">property nfsMaximumMbit</a>
</h3>

```typescript
nfsMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the nfs traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L971">property nfsReservationMbit</a>
</h3>

```typescript
nfsReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the nfs traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L975">property nfsShareCount</a>
</h3>

```typescript
nfsShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the nfs traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L979">property nfsShareLevel</a>
</h3>

```typescript
nfsShareLevel?: pulumi.Input<string>;
```


The allocation level for the nfs traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L984">property notifySwitches</a>
</h3>

```typescript
notifySwitches?: pulumi.Input<boolean>;
```


If `true`, the teaming policy will notify the
broadcast network of an uplink failover, triggering cache updates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L989">property portPrivateSecondaryVlanId</a>
</h3>

```typescript
portPrivateSecondaryVlanId?: pulumi.Input<number>;
```


Used to define a secondary VLAN
ID when using private VLANs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L996">property standbyUplinks</a>
</h3>

```typescript
standbyUplinks?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of standby uplinks to be used in
failover. These uplinks need to match the definitions in the
`uplinks` DVS argument. See
here for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1001">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1007">property teamingPolicy</a>
</h3>

```typescript
teamingPolicy?: pulumi.Input<string>;
```


The uplink teaming policy. Can be one of
`loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1012">property txUplink</a>
</h3>

```typescript
txUplink?: pulumi.Input<boolean>;
```


Forward all traffic transmitted by ports for which
this policy applies to its DVS uplinks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1020">property uplinks</a>
</h3>

```typescript
uplinks?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of strings that uniquely identifies the names
of the uplinks on the DVS across hosts. The number of items in this list
controls the number of uplinks that exist on the DVS, in addition to the
names.  See here for an example on how to
use this option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1024">property vdpMaximumMbit</a>
</h3>

```typescript
vdpMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the vdp traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1028">property vdpReservationMbit</a>
</h3>

```typescript
vdpReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the vdp traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1032">property vdpShareCount</a>
</h3>

```typescript
vdpShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the vdp traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1036">property vdpShareLevel</a>
</h3>

```typescript
vdpShareLevel?: pulumi.Input<string>;
```


The allocation level for the vdp traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1043">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


- The version of the DVS to create. The default is to
create the DVS at the latest version supported by the version of vSphere
being used. A DVS can be upgraded to another version, but cannot be
downgraded.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1047">property virtualmachineMaximumMbit</a>
</h3>

```typescript
virtualmachineMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the virtualMachine traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1051">property virtualmachineReservationMbit</a>
</h3>

```typescript
virtualmachineReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the virtualMachine traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1055">property virtualmachineShareCount</a>
</h3>

```typescript
virtualmachineShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the virtualMachine traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1059">property virtualmachineShareLevel</a>
</h3>

```typescript
virtualmachineShareLevel?: pulumi.Input<string>;
```


The allocation level for the virtualMachine traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1063">property vlanId</a>
</h3>

```typescript
vlanId?: pulumi.Input<number>;
```


The VLAN ID for single VLAN mode. 0 denotes no VLAN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1070">property vlanRanges</a>
</h3>

```typescript
vlanRanges?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Used to denote VLAN trunking. Use the `min_vlan`
and `max_vlan` sub-arguments to define the tagged VLAN range. Multiple
`vlan_range` definitions are allowed, but they must not overlap. Example
below:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1074">property vmotionMaximumMbit</a>
</h3>

```typescript
vmotionMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the vmotion traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1078">property vmotionReservationMbit</a>
</h3>

```typescript
vmotionReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the vmotion traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1082">property vmotionShareCount</a>
</h3>

```typescript
vmotionShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the vmotion traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1086">property vmotionShareLevel</a>
</h3>

```typescript
vmotionShareLevel?: pulumi.Input<string>;
```


The allocation level for the vmotion traffic class. Can be one of high, low, normal, or custom.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1090">property vsanMaximumMbit</a>
</h3>

```typescript
vsanMaximumMbit?: pulumi.Input<number>;
```


The maximum allowed usage for the vsan traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1094">property vsanReservationMbit</a>
</h3>

```typescript
vsanReservationMbit?: pulumi.Input<number>;
```


The amount of guaranteed bandwidth for the vsan traffic class, in Mbits/sec.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1098">property vsanShareCount</a>
</h3>

```typescript
vsanShareCount?: pulumi.Input<number>;
```


The amount of shares to allocate to the vsan traffic class for a custom share level.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/distributedVirtualSwitch.ts#L1102">property vsanShareLevel</a>
</h3>

```typescript
vsanShareLevel?: pulumi.Input<string>;
```


The allocation level for the vsan traffic class. Can be one of high, low, normal, or custom.

<h2 class="pdoc-module-header" id="DpmHostOverrideArgs">
<a class="pdoc-member-name" href="/dpmHostOverride.ts#L120">interface DpmHostOverrideArgs</a>
</h2>

The set of arguments for constructing a DpmHostOverride resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dpmHostOverride.ts#L126">property computeClusterId</a>
</h3>

```typescript
computeClusterId: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dpmHostOverride.ts#L132">property dpmAutomationLevel</a>
</h3>

```typescript
dpmAutomationLevel?: pulumi.Input<string>;
```


The automation level for host power
operations on this host. Can be one of `manual` or `automated`. Default:
`manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dpmHostOverride.ts#L137">property dpmEnabled</a>
</h3>

```typescript
dpmEnabled?: pulumi.Input<boolean>;
```


Enable DPM support for this host. Default:
`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dpmHostOverride.ts#L141">property hostSystemId</a>
</h3>

```typescript
hostSystemId: pulumi.Input<string>;
```


The managed object ID of the host.

<h2 class="pdoc-module-header" id="DpmHostOverrideState">
<a class="pdoc-member-name" href="/dpmHostOverride.ts#L93">interface DpmHostOverrideState</a>
</h2>

Input properties used for looking up and filtering DpmHostOverride resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dpmHostOverride.ts#L99">property computeClusterId</a>
</h3>

```typescript
computeClusterId?: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dpmHostOverride.ts#L105">property dpmAutomationLevel</a>
</h3>

```typescript
dpmAutomationLevel?: pulumi.Input<string>;
```


The automation level for host power
operations on this host. Can be one of `manual` or `automated`. Default:
`manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dpmHostOverride.ts#L110">property dpmEnabled</a>
</h3>

```typescript
dpmEnabled?: pulumi.Input<boolean>;
```


Enable DPM support for this host. Default:
`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dpmHostOverride.ts#L114">property hostSystemId</a>
</h3>

```typescript
hostSystemId?: pulumi.Input<string>;
```


The managed object ID of the host.

<h2 class="pdoc-module-header" id="DrsVmOverrideArgs">
<a class="pdoc-member-name" href="/drsVmOverride.ts#L122">interface DrsVmOverrideArgs</a>
</h2>

The set of arguments for constructing a DrsVmOverride resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/drsVmOverride.ts#L128">property computeClusterId</a>
</h3>

```typescript
computeClusterId: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/drsVmOverride.ts#L134">property drsAutomationLevel</a>
</h3>

```typescript
drsAutomationLevel?: pulumi.Input<string>;
```


Overrides the automation level for this virtual
machine in the cluster. Can be one of `manual`, `partiallyAutomated`, or
`fullyAutomated`. Default: `manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/drsVmOverride.ts#L139">property drsEnabled</a>
</h3>

```typescript
drsEnabled?: pulumi.Input<boolean>;
```


Overrides the default DRS setting for this virtual
machine. Can be either `true` or `false`. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/drsVmOverride.ts#L144">property virtualMachineId</a>
</h3>

```typescript
virtualMachineId: pulumi.Input<string>;
```


The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.

<h2 class="pdoc-module-header" id="DrsVmOverrideState">
<a class="pdoc-member-name" href="/drsVmOverride.ts#L94">interface DrsVmOverrideState</a>
</h2>

Input properties used for looking up and filtering DrsVmOverride resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/drsVmOverride.ts#L100">property computeClusterId</a>
</h3>

```typescript
computeClusterId?: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/drsVmOverride.ts#L106">property drsAutomationLevel</a>
</h3>

```typescript
drsAutomationLevel?: pulumi.Input<string>;
```


Overrides the automation level for this virtual
machine in the cluster. Can be one of `manual`, `partiallyAutomated`, or
`fullyAutomated`. Default: `manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/drsVmOverride.ts#L111">property drsEnabled</a>
</h3>

```typescript
drsEnabled?: pulumi.Input<boolean>;
```


Overrides the default DRS setting for this virtual
machine. Can be either `true` or `false`. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/drsVmOverride.ts#L116">property virtualMachineId</a>
</h3>

```typescript
virtualMachineId?: pulumi.Input<string>;
```


The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.

<h2 class="pdoc-module-header" id="FileArgs">
<a class="pdoc-member-name" href="/file.ts#L157">interface FileArgs</a>
</h2>

The set of arguments for constructing a File resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L162">property createDirectories</a>
</h3>

```typescript
createDirectories?: pulumi.Input<boolean>;
```


Create directories in `destination_file`
path parameter if any missing for copy operation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L167">property datacenter</a>
</h3>

```typescript
datacenter?: pulumi.Input<string>;
```


The name of a datacenter in which the file will be
uploaded to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L172">property datastore</a>
</h3>

```typescript
datastore: pulumi.Input<string>;
```


The name of the datastore in which to upload the
file to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L177">property destinationFile</a>
</h3>

```typescript
destinationFile: pulumi.Input<string>;
```


The path to where the file should be uploaded
or copied to on vSphere.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L182">property sourceDatacenter</a>
</h3>

```typescript
sourceDatacenter?: pulumi.Input<string>;
```


The name of a datacenter in which the file
will be copied from. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L187">property sourceDatastore</a>
</h3>

```typescript
sourceDatastore?: pulumi.Input<string>;
```


The name of the datastore in which file will
be copied from. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L193">property sourceFile</a>
</h3>

```typescript
sourceFile: pulumi.Input<string>;
```


The path to the file being uploaded from the
Terraform host to vSphere or copied within vSphere. Forces a new resource if
changed.

<h2 class="pdoc-module-header" id="FileState">
<a class="pdoc-member-name" href="/file.ts#L115">interface FileState</a>
</h2>

Input properties used for looking up and filtering File resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L120">property createDirectories</a>
</h3>

```typescript
createDirectories?: pulumi.Input<boolean>;
```


Create directories in `destination_file`
path parameter if any missing for copy operation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L125">property datacenter</a>
</h3>

```typescript
datacenter?: pulumi.Input<string>;
```


The name of a datacenter in which the file will be
uploaded to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L130">property datastore</a>
</h3>

```typescript
datastore?: pulumi.Input<string>;
```


The name of the datastore in which to upload the
file to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L135">property destinationFile</a>
</h3>

```typescript
destinationFile?: pulumi.Input<string>;
```


The path to where the file should be uploaded
or copied to on vSphere.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L140">property sourceDatacenter</a>
</h3>

```typescript
sourceDatacenter?: pulumi.Input<string>;
```


The name of a datacenter in which the file
will be copied from. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L145">property sourceDatastore</a>
</h3>

```typescript
sourceDatastore?: pulumi.Input<string>;
```


The name of the datastore in which file will
be copied from. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/file.ts#L151">property sourceFile</a>
</h3>

```typescript
sourceFile?: pulumi.Input<string>;
```


The path to the file being uploaded from the
Terraform host to vSphere or copied within vSphere. Forces a new resource if
changed.

<h2 class="pdoc-module-header" id="FolderArgs">
<a class="pdoc-member-name" href="/folder.ts#L141">interface FolderArgs</a>
</h2>

The set of arguments for constructing a Folder resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/folder.ts#L147">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


Map of custom attribute ids to attribute
value strings to set for folder. See [here][docs-setting-custom-attributes]
for a reference on how to set values for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/folder.ts#L153">property datacenterId</a>
</h3>

```typescript
datacenterId?: pulumi.Input<string>;
```


The ID of the datacenter the folder will be created in.
Required for all folder types except for datacenter folders. Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/folder.ts#L162">property path</a>
</h3>

```typescript
path: pulumi.Input<string>;
```


The path of the folder to be created. This is relative to
the root of the type of folder you are creating, and the supplied datacenter.
For example, given a default datacenter of `default-dc`, a folder of type
`vm` (denoting a virtual machine folder), and a supplied folder of
`terraform-test-folder`, the resulting path would be
`/default-dc/vm/terraform-test-folder`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/folder.ts#L167">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/folder.ts#L174">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of folder to create. Allowed options are
`datacenter` for datacenter folders, `host` for host and cluster folders,
`vm` for virtual machine folders, `datastore` for datastore folders, and
`network` for network folders. Forces a new resource if changed.

<h2 class="pdoc-module-header" id="FolderState">
<a class="pdoc-member-name" href="/folder.ts#L102">interface FolderState</a>
</h2>

Input properties used for looking up and filtering Folder resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/folder.ts#L108">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


Map of custom attribute ids to attribute
value strings to set for folder. See [here][docs-setting-custom-attributes]
for a reference on how to set values for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/folder.ts#L114">property datacenterId</a>
</h3>

```typescript
datacenterId?: pulumi.Input<string>;
```


The ID of the datacenter the folder will be created in.
Required for all folder types except for datacenter folders. Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/folder.ts#L123">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


The path of the folder to be created. This is relative to
the root of the type of folder you are creating, and the supplied datacenter.
For example, given a default datacenter of `default-dc`, a folder of type
`vm` (denoting a virtual machine folder), and a supplied folder of
`terraform-test-folder`, the resulting path would be
`/default-dc/vm/terraform-test-folder`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/folder.ts#L128">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/folder.ts#L135">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of folder to create. Allowed options are
`datacenter` for datacenter folders, `host` for host and cluster folders,
`vm` for virtual machine folders, `datastore` for datastore folders, and
`network` for network folders. Forces a new resource if changed.

<h2 class="pdoc-module-header" id="GetComputeClusterArgs">
<a class="pdoc-member-name" href="/getComputeCluster.ts#L34">interface GetComputeClusterArgs</a>
</h2>

A collection of arguments for invoking getComputeCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getComputeCluster.ts#L42">property datacenterId</a>
</h3>

```typescript
datacenterId?: string;
```


The [managed object reference
ID][docs-about-morefs] of the datacenter the cluster is located in.  This can
be omitted if the search path used in `name` is an absolute path.  For
default datacenters, use the id attribute from an empty `vsphere_datacenter`
data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getComputeCluster.ts#L46">property name</a>
</h3>

```typescript
name: string;
```


The name or absolute path to the cluster.

<h2 class="pdoc-module-header" id="GetComputeClusterResult">
<a class="pdoc-member-name" href="/getComputeCluster.ts#L52">interface GetComputeClusterResult</a>
</h2>

A collection of values returned by getComputeCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getComputeCluster.ts#L57">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getComputeCluster.ts#L53">property resourcePoolId</a>
</h3>

```typescript
resourcePoolId: string;
```

<h2 class="pdoc-module-header" id="GetCustomAttributeArgs">
<a class="pdoc-member-name" href="/getCustomAttribute.ts#L27">interface GetCustomAttributeArgs</a>
</h2>

A collection of arguments for invoking getCustomAttribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getCustomAttribute.ts#L31">property name</a>
</h3>

```typescript
name: string;
```


The name of the custom attribute.

<h2 class="pdoc-module-header" id="GetCustomAttributeResult">
<a class="pdoc-member-name" href="/getCustomAttribute.ts#L37">interface GetCustomAttributeResult</a>
</h2>

A collection of values returned by getCustomAttribute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getCustomAttribute.ts#L42">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getCustomAttribute.ts#L38">property managedObjectType</a>
</h3>

```typescript
managedObjectType: string;
```

<h2 class="pdoc-module-header" id="GetDatacenterArgs">
<a class="pdoc-member-name" href="/getDatacenter.ts#L24">interface GetDatacenterArgs</a>
</h2>

A collection of arguments for invoking getDatacenter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getDatacenter.ts#L29">property name</a>
</h3>

```typescript
name?: string;
```


The name of the datacenter. This can be a name or path.
Can be omitted if there is only one datacenter in your inventory.

<h2 class="pdoc-module-header" id="GetDatacenterResult">
<a class="pdoc-member-name" href="/getDatacenter.ts#L35">interface GetDatacenterResult</a>
</h2>

A collection of values returned by getDatacenter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getDatacenter.ts#L39">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="GetDatastoreArgs">
<a class="pdoc-member-name" href="/getDatastore.ts#L24">interface GetDatastoreArgs</a>
</h2>

A collection of arguments for invoking getDatastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getDatastore.ts#L32">property datacenterId</a>
</h3>

```typescript
datacenterId?: string;
```


The [managed object reference
ID][docs-about-morefs] of the datacenter the datastore is located in. This
can be omitted if the search path used in `name` is an absolute path. For
default datacenters, use the id attribute from an empty `vsphere_datacenter`
data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getDatastore.ts#L36">property name</a>
</h3>

```typescript
name: string;
```


The name of the datastore. This can be a name or path.

<h2 class="pdoc-module-header" id="GetDatastoreClusterArgs">
<a class="pdoc-member-name" href="/getDatastoreCluster.ts#L29">interface GetDatastoreClusterArgs</a>
</h2>

A collection of arguments for invoking getDatastoreCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getDatastoreCluster.ts#L37">property datacenterId</a>
</h3>

```typescript
datacenterId?: string;
```


The [managed object reference
ID][docs-about-morefs] of the datacenter the datastore cluster is located in.
This can be omitted if the search path used in `name` is an absolute path.
For default datacenters, use the id attribute from an empty
`vsphere_datacenter` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getDatastoreCluster.ts#L41">property name</a>
</h3>

```typescript
name: string;
```


The name or absolute path to the datastore cluster.

<h2 class="pdoc-module-header" id="GetDatastoreClusterResult">
<a class="pdoc-member-name" href="/getDatastoreCluster.ts#L47">interface GetDatastoreClusterResult</a>
</h2>

A collection of values returned by getDatastoreCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getDatastoreCluster.ts#L51">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="GetDatastoreResult">
<a class="pdoc-member-name" href="/getDatastore.ts#L42">interface GetDatastoreResult</a>
</h2>

A collection of values returned by getDatastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getDatastore.ts#L46">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="GetDistributedVirtualSwitchArgs">
<a class="pdoc-member-name" href="/getDistributedVirtualSwitch.ts#L28">interface GetDistributedVirtualSwitchArgs</a>
</h2>

A collection of arguments for invoking getDistributedVirtualSwitch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getDistributedVirtualSwitch.ts#L36">property datacenterId</a>
</h3>

```typescript
datacenterId?: string;
```


The [managed object reference
ID][docs-about-morefs] of the datacenter the DVS is located in. This can be
omitted if the search path used in `name` is an absolute path. For default
datacenters, use the id attribute from an empty `vsphere_datacenter` data
source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getDistributedVirtualSwitch.ts#L41">property name</a>
</h3>

```typescript
name: string;
```


The name of the distributed virtual switch. This can be a
name or path.

<h2 class="pdoc-module-header" id="GetDistributedVirtualSwitchResult">
<a class="pdoc-member-name" href="/getDistributedVirtualSwitch.ts#L47">interface GetDistributedVirtualSwitchResult</a>
</h2>

A collection of values returned by getDistributedVirtualSwitch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getDistributedVirtualSwitch.ts#L52">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getDistributedVirtualSwitch.ts#L48">property uplinks</a>
</h3>

```typescript
uplinks: string[];
```

<h2 class="pdoc-module-header" id="GetHostArgs">
<a class="pdoc-member-name" href="/getHost.ts#L21">interface GetHostArgs</a>
</h2>

A collection of arguments for invoking getHost.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getHost.ts#L26">property datacenterId</a>
</h3>

```typescript
datacenterId: string;
```


The [managed object reference
ID][docs-about-morefs] of a datacenter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getHost.ts#L31">property name</a>
</h3>

```typescript
name?: string;
```


The name of the host. This can be a name or path. Can be
omitted if there is only one host in your inventory.

<h2 class="pdoc-module-header" id="GetHostResult">
<a class="pdoc-member-name" href="/getHost.ts#L37">interface GetHostResult</a>
</h2>

A collection of values returned by getHost.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getHost.ts#L46">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getHost.ts#L42">property resourcePoolId</a>
</h3>

```typescript
resourcePoolId: string;
```


The [managed object ID][docs-about-morefs] of the host's
root resource pool.

<h2 class="pdoc-module-header" id="GetNetworkArgs">
<a class="pdoc-member-name" href="/getNetwork.ts#L23">interface GetNetworkArgs</a>
</h2>

A collection of arguments for invoking getNetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getNetwork.ts#L31">property datacenterId</a>
</h3>

```typescript
datacenterId?: string;
```


The [managed object reference
ID][docs-about-morefs] of the datacenter the network is located in. This can
be omitted if the search path used in `name` is an absolute path. For default
datacenters, use the id attribute from an empty `vsphere_datacenter` data
source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getNetwork.ts#L35">property name</a>
</h3>

```typescript
name: string;
```


The name of the network. This can be a name or path.

<h2 class="pdoc-module-header" id="GetNetworkResult">
<a class="pdoc-member-name" href="/getNetwork.ts#L41">interface GetNetworkResult</a>
</h2>

A collection of values returned by getNetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getNetwork.ts#L46">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getNetwork.ts#L42">property type</a>
</h3>

```typescript
type: string;
```

<h2 class="pdoc-module-header" id="GetResourcePoolArgs">
<a class="pdoc-member-name" href="/getResourcePool.ts#L25">interface GetResourcePoolArgs</a>
</h2>

A collection of arguments for invoking getResourcePool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getResourcePool.ts#L33">property datacenterId</a>
</h3>

```typescript
datacenterId?: string;
```


The [managed object reference
ID][docs-about-morefs] of the datacenter the resource pool is located in.
This can be omitted if the search path used in `name` is an absolute path.
For default datacenters, use the id attribute from an empty
`vsphere_datacenter` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getResourcePool.ts#L38">property name</a>
</h3>

```typescript
name?: string;
```


The name of the resource pool. This can be a name or
path. This is required when using vCenter.

<h2 class="pdoc-module-header" id="GetResourcePoolResult">
<a class="pdoc-member-name" href="/getResourcePool.ts#L44">interface GetResourcePoolResult</a>
</h2>

A collection of values returned by getResourcePool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getResourcePool.ts#L48">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="GetTagArgs">
<a class="pdoc-member-name" href="/getTag.ts#L28">interface GetTagArgs</a>
</h2>

A collection of arguments for invoking getTag.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getTag.ts#L32">property categoryId</a>
</h3>

```typescript
categoryId: string;
```


The ID of the tag category the tag is located in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getTag.ts#L36">property name</a>
</h3>

```typescript
name: string;
```


The name of the tag.

<h2 class="pdoc-module-header" id="GetTagCategoryArgs">
<a class="pdoc-member-name" href="/getTagCategory.ts#L27">interface GetTagCategoryArgs</a>
</h2>

A collection of arguments for invoking getTagCategory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getTagCategory.ts#L31">property name</a>
</h3>

```typescript
name: string;
```


The name of the tag category.

<h2 class="pdoc-module-header" id="GetTagCategoryResult">
<a class="pdoc-member-name" href="/getTagCategory.ts#L37">interface GetTagCategoryResult</a>
</h2>

A collection of values returned by getTagCategory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getTagCategory.ts#L38">property associableTypes</a>
</h3>

```typescript
associableTypes: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getTagCategory.ts#L39">property cardinality</a>
</h3>

```typescript
cardinality: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getTagCategory.ts#L40">property description</a>
</h3>

```typescript
description: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getTagCategory.ts#L44">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="GetTagResult">
<a class="pdoc-member-name" href="/getTag.ts#L42">interface GetTagResult</a>
</h2>

A collection of values returned by getTag.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getTag.ts#L43">property description</a>
</h3>

```typescript
description: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getTag.ts#L47">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="GetVirtualMachineArgs">
<a class="pdoc-member-name" href="/getVirtualMachine.ts#L26">interface GetVirtualMachineArgs</a>
</h2>

A collection of arguments for invoking getVirtualMachine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getVirtualMachine.ts#L34">property datacenterId</a>
</h3>

```typescript
datacenterId?: string;
```


The [managed object reference
ID][docs-about-morefs] of the datacenter the virtual machine is located in.
This can be omitted if the search path used in `name` is an absolute path.
For default datacenters, use the `id` attribute from an empty
`vsphere_datacenter` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getVirtualMachine.ts#L39">property name</a>
</h3>

```typescript
name: string;
```


The name of the virtual machine. This can be a name or
path.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getVirtualMachine.ts#L44">property scsiControllerScanCount</a>
</h3>

```typescript
scsiControllerScanCount?: number;
```


The number of SCSI controllers to
scan for disk attributes and controller types on. Default: `1`.

<h2 class="pdoc-module-header" id="GetVirtualMachineResult">
<a class="pdoc-member-name" href="/getVirtualMachine.ts#L50">interface GetVirtualMachineResult</a>
</h2>

A collection of values returned by getVirtualMachine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getVirtualMachine.ts#L55">property alternateGuestName</a>
</h3>

```typescript
alternateGuestName: string;
```


The alternate guest name of the virtual machine when
guest_id is a non-specific operating system, like `otherGuest`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getVirtualMachine.ts#L66">property disks</a>
</h3>

```typescript
disks: { ... }[];
```


Information about each of the disks on this virtual machine or
template. These are sorted by bus and unit number so that they can be applied
to a `vsphere_virtual_machine` resource in the order the resource expects
while cloning. This is useful for discovering certain disk settings while
performing a linked clone, as all settings that are output by this data
source must be the same on the destination virtual machine as the source.
Only the first number of controllers defined by `scsi_controller_scan_count`
are scanned for disks. The sub-attributes are:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getVirtualMachine.ts#L70">property firmware</a>
</h3>

```typescript
firmware: string;
```


The firmware type for this virtual machine. Can be `bios` or `efi`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getVirtualMachine.ts#L74">property guestId</a>
</h3>

```typescript
guestId: string;
```


The guest ID of the virtual machine or template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getVirtualMachine.ts#L98">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getVirtualMachine.ts#L80">property networkInterfaceTypes</a>
</h3>

```typescript
networkInterfaceTypes: string[];
```


The network interface types for each network
interface found on the virtual machine, in device bus order. Will be one of
`e1000`, `e1000e`, `pcnet32`, `sriov`, `vmxnet2`, or `vmxnet3`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getVirtualMachine.ts#L86">property scsiBusSharing</a>
</h3>

```typescript
scsiBusSharing: string;
```


Mode for sharing the SCSI bus. The modes are
physicalSharing, virtualSharing, and noSharing. Only the first number of
controllers defined by `scsi_controller_scan_count` are scanned.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getVirtualMachine.ts#L94">property scsiType</a>
</h3>

```typescript
scsiType: string;
```


The common type of all SCSI controllers on this virtual machine.
Will be one of `lsilogic` (LSI Logic Parallel), `lsilogic-sas` (LSI Logic
SAS), `pvscsi` (VMware Paravirtual), `buslogic` (BusLogic), or `mixed` when
there are multiple controller types. Only the first number of controllers
defined by `scsi_controller_scan_count` are scanned.

<h2 class="pdoc-module-header" id="GetVmfsDisksArgs">
<a class="pdoc-member-name" href="/getVmfsDisks.ts#L25">interface GetVmfsDisksArgs</a>
</h2>

A collection of arguments for invoking getVmfsDisks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getVmfsDisks.ts#L30">property filter</a>
</h3>

```typescript
filter?: string;
```


A regular expression to filter the disks against. Only
disks with canonical names that match will be included.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getVmfsDisks.ts#L35">property hostSystemId</a>
</h3>

```typescript
hostSystemId: string;
```


The [managed object ID][docs-about-morefs] of
the host to look for disks on.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getVmfsDisks.ts#L41">property rescan</a>
</h3>

```typescript
rescan?: boolean;
```


Whether or not to rescan storage adapters before
searching for disks. This may lengthen the time it takes to perform the
search. Default: `false`.

<h2 class="pdoc-module-header" id="GetVmfsDisksResult">
<a class="pdoc-member-name" href="/getVmfsDisks.ts#L47">interface GetVmfsDisksResult</a>
</h2>

A collection of values returned by getVmfsDisks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getVmfsDisks.ts#L52">property disks</a>
</h3>

```typescript
disks: string[];
```


A lexicographically sorted list of devices discovered by the
operation, matching the supplied `filter`, if provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/getVmfsDisks.ts#L56">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="HaVmOverrideArgs">
<a class="pdoc-member-name" href="/haVmOverride.ts#L306">interface HaVmOverrideArgs</a>
</h2>

The set of arguments for constructing a HaVmOverride resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L312">property computeClusterId</a>
</h3>

```typescript
computeClusterId: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L320">property haDatastoreApdRecoveryAction</a>
</h3>

```typescript
haDatastoreApdRecoveryAction?: pulumi.Input<string>;
```


Controls the action to take
on this virtual machine if an APD status on an affected datastore clears in
the middle of an APD event. Can be one of `useClusterDefault`, `none` or
`reset`.  Default: `useClusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L328">property haDatastoreApdResponse</a>
</h3>

```typescript
haDatastoreApdResponse?: pulumi.Input<string>;
```


Controls the action to take on this
virtual machine when the cluster has detected loss to all paths to a relevant
datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
`restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L336">property haDatastoreApdResponseDelay</a>
</h3>

```typescript
haDatastoreApdResponseDelay?: pulumi.Input<number>;
```


Controls the delay in minutes
to wait after an APD timeout event to execute the response action defined in
`ha_datastore_apd_response`. Use `-1` to use
the cluster default. Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L344">property haDatastorePdlResponse</a>
</h3>

```typescript
haDatastorePdlResponse?: pulumi.Input<string>;
```


Controls the action to take on this
virtual machine when the cluster has detected a permanent device loss to a
relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
`restartAggressive`. Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L351">property haHostIsolationResponse</a>
</h3>

```typescript
haHostIsolationResponse?: pulumi.Input<string>;
```


The action to take on this virtual
machine when a host has detected that it has been isolated from the rest of
the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
`shutdown`. Default: `clusterIsolationResponse`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L357">property haVmFailureInterval</a>
</h3>

```typescript
haVmFailureInterval?: pulumi.Input<number>;
```


If a heartbeat from this virtual
machine is not received within this configured interval, the virtual machine
is marked as failed. The value is in seconds. Default: `30`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L366">property haVmMaximumFailureWindow</a>
</h3>

```typescript
haVmMaximumFailureWindow?: pulumi.Input<number>;
```


The length of the reset window in
which `ha_vm_maximum_resets` can operate. When this
window expires, no more resets are attempted regardless of the setting
configured in `ha_vm_maximum_resets`. `-1` means no window, meaning an
unlimited reset time is allotted. The value is specified in seconds. Default:
`-1` (no window).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L372">property haVmMaximumResets</a>
</h3>

```typescript
haVmMaximumResets?: pulumi.Input<number>;
```


The maximum number of resets that HA will
perform to this virtual machine when responding to a failure event. Default:
`3`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L378">property haVmMinimumUptime</a>
</h3>

```typescript
haVmMinimumUptime?: pulumi.Input<number>;
```


The time, in seconds, that HA waits after
powering on this virtual machine before monitoring for heartbeats. Default:
`120` (2 minutes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L384">property haVmMonitoring</a>
</h3>

```typescript
haVmMonitoring?: pulumi.Input<string>;
```


The type of virtual machine monitoring to use
when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
`vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L391">property haVmMonitoringUseClusterDefaults</a>
</h3>

```typescript
haVmMonitoringUseClusterDefaults?: pulumi.Input<boolean>;
```


Determines whether or
not the cluster's default settings or the VM override settings specified in
this resource are used for virtual machine monitoring. The default is `true`
(use cluster defaults) - set to `false` to have overrides take effect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L398">property haVmRestartPriority</a>
</h3>

```typescript
haVmRestartPriority?: pulumi.Input<string>;
```


The restart priority for the virtual
machine when vSphere detects a host failure. Can be one of
`clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
Default: `clusterRestartPriority`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L405">property haVmRestartTimeout</a>
</h3>

```typescript
haVmRestartTimeout?: pulumi.Input<number>;
```


The maximum time, in seconds, that
vSphere HA will wait for this virtual machine to be ready. Use `-1` to
specify the cluster default.  Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L410">property virtualMachineId</a>
</h3>

```typescript
virtualMachineId: pulumi.Input<string>;
```


The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.

<h2 class="pdoc-module-header" id="HaVmOverrideState">
<a class="pdoc-member-name" href="/haVmOverride.ts#L196">interface HaVmOverrideState</a>
</h2>

Input properties used for looking up and filtering HaVmOverride resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L202">property computeClusterId</a>
</h3>

```typescript
computeClusterId?: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the cluster to put the override in.  Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L210">property haDatastoreApdRecoveryAction</a>
</h3>

```typescript
haDatastoreApdRecoveryAction?: pulumi.Input<string>;
```


Controls the action to take
on this virtual machine if an APD status on an affected datastore clears in
the middle of an APD event. Can be one of `useClusterDefault`, `none` or
`reset`.  Default: `useClusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L218">property haDatastoreApdResponse</a>
</h3>

```typescript
haDatastoreApdResponse?: pulumi.Input<string>;
```


Controls the action to take on this
virtual machine when the cluster has detected loss to all paths to a relevant
datastore. Can be one of `clusterDefault`, `disabled`, `warning`,
`restartConservative`, or `restartAggressive`.  Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L226">property haDatastoreApdResponseDelay</a>
</h3>

```typescript
haDatastoreApdResponseDelay?: pulumi.Input<number>;
```


Controls the delay in minutes
to wait after an APD timeout event to execute the response action defined in
`ha_datastore_apd_response`. Use `-1` to use
the cluster default. Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L234">property haDatastorePdlResponse</a>
</h3>

```typescript
haDatastorePdlResponse?: pulumi.Input<string>;
```


Controls the action to take on this
virtual machine when the cluster has detected a permanent device loss to a
relevant datastore. Can be one of `clusterDefault`, `disabled`, `warning`, or
`restartAggressive`. Default: `clusterDefault`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L241">property haHostIsolationResponse</a>
</h3>

```typescript
haHostIsolationResponse?: pulumi.Input<string>;
```


The action to take on this virtual
machine when a host has detected that it has been isolated from the rest of
the cluster. Can be one of `clusterIsolationResponse`, `none`, `powerOff`, or
`shutdown`. Default: `clusterIsolationResponse`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L247">property haVmFailureInterval</a>
</h3>

```typescript
haVmFailureInterval?: pulumi.Input<number>;
```


If a heartbeat from this virtual
machine is not received within this configured interval, the virtual machine
is marked as failed. The value is in seconds. Default: `30`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L256">property haVmMaximumFailureWindow</a>
</h3>

```typescript
haVmMaximumFailureWindow?: pulumi.Input<number>;
```


The length of the reset window in
which `ha_vm_maximum_resets` can operate. When this
window expires, no more resets are attempted regardless of the setting
configured in `ha_vm_maximum_resets`. `-1` means no window, meaning an
unlimited reset time is allotted. The value is specified in seconds. Default:
`-1` (no window).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L262">property haVmMaximumResets</a>
</h3>

```typescript
haVmMaximumResets?: pulumi.Input<number>;
```


The maximum number of resets that HA will
perform to this virtual machine when responding to a failure event. Default:
`3`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L268">property haVmMinimumUptime</a>
</h3>

```typescript
haVmMinimumUptime?: pulumi.Input<number>;
```


The time, in seconds, that HA waits after
powering on this virtual machine before monitoring for heartbeats. Default:
`120` (2 minutes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L274">property haVmMonitoring</a>
</h3>

```typescript
haVmMonitoring?: pulumi.Input<string>;
```


The type of virtual machine monitoring to use
when HA is enabled in the cluster. Can be one of `vmMonitoringDisabled`,
`vmMonitoringOnly`, or `vmAndAppMonitoring`. Default: `vmMonitoringDisabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L281">property haVmMonitoringUseClusterDefaults</a>
</h3>

```typescript
haVmMonitoringUseClusterDefaults?: pulumi.Input<boolean>;
```


Determines whether or
not the cluster's default settings or the VM override settings specified in
this resource are used for virtual machine monitoring. The default is `true`
(use cluster defaults) - set to `false` to have overrides take effect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L288">property haVmRestartPriority</a>
</h3>

```typescript
haVmRestartPriority?: pulumi.Input<string>;
```


The restart priority for the virtual
machine when vSphere detects a host failure. Can be one of
`clusterRestartPriority`, `lowest`, `low`, `medium`, `high`, or `highest`.
Default: `clusterRestartPriority`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L295">property haVmRestartTimeout</a>
</h3>

```typescript
haVmRestartTimeout?: pulumi.Input<number>;
```


The maximum time, in seconds, that
vSphere HA will wait for this virtual machine to be ready. Use `-1` to
specify the cluster default.  Default: `-1`.
<sup>[\*][tf-vsphere-cluster-resource-version-restrictions]</sup>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/haVmOverride.ts#L300">property virtualMachineId</a>
</h3>

```typescript
virtualMachineId?: pulumi.Input<string>;
```


The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.

<h2 class="pdoc-module-header" id="HostPortGroupArgs">
<a class="pdoc-member-name" href="/hostPortGroup.ts#L287">interface HostPortGroupArgs</a>
</h2>

The set of arguments for constructing a HostPortGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L291">property activeNics</a>
</h3>

```typescript
activeNics?: pulumi.Input<pulumi.Input<string>[]>;
```


List of active network adapters used for load balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L296">property allowForgedTransmits</a>
</h3>

```typescript
allowForgedTransmits?: pulumi.Input<boolean>;
```


Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address
than that of its own.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L300">property allowMacChanges</a>
</h3>

```typescript
allowMacChanges?: pulumi.Input<boolean>;
```


Controls whether or not the Media Access Control (MAC) address can be changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L304">property allowPromiscuous</a>
</h3>

```typescript
allowPromiscuous?: pulumi.Input<boolean>;
```


Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L309">property checkBeacon</a>
</h3>

```typescript
checkBeacon?: pulumi.Input<boolean>;
```


Enable beacon probing. Requires that the vSwitch has been configured to use a beacon. If disabled, link status is
used only.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L313">property failback</a>
</h3>

```typescript
failback?: pulumi.Input<boolean>;
```


If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L318">property hostSystemId</a>
</h3>

```typescript
hostSystemId: pulumi.Input<string>;
```


The [managed object ID][docs-about-morefs] of
the host to set the port group up on. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L323">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the port group.  Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L327">property notifySwitches</a>
</h3>

```typescript
notifySwitches?: pulumi.Input<boolean>;
```


If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L331">property shapingAverageBandwidth</a>
</h3>

```typescript
shapingAverageBandwidth?: pulumi.Input<number>;
```


The average bandwidth in bits per second if traffic shaping is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L335">property shapingBurstSize</a>
</h3>

```typescript
shapingBurstSize?: pulumi.Input<number>;
```


The maximum burst size allowed in bytes if traffic shaping is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L339">property shapingEnabled</a>
</h3>

```typescript
shapingEnabled?: pulumi.Input<boolean>;
```


Enable traffic shaping on this virtual switch or port group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L343">property shapingPeakBandwidth</a>
</h3>

```typescript
shapingPeakBandwidth?: pulumi.Input<number>;
```


The peak bandwidth during bursts in bits per second if traffic shaping is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L347">property standbyNics</a>
</h3>

```typescript
standbyNics?: pulumi.Input<pulumi.Input<string>[]>;
```


List of standby network adapters used for failover.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L352">property teamingPolicy</a>
</h3>

```typescript
teamingPolicy?: pulumi.Input<string>;
```


The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, or
failover_explicit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L357">property virtualSwitchName</a>
</h3>

```typescript
virtualSwitchName: pulumi.Input<string>;
```


The name of the virtual switch to bind
this port group to. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L364">property vlanId</a>
</h3>

```typescript
vlanId?: pulumi.Input<number>;
```


The VLAN ID/trunk mode for this port group.  An ID of
`0` denotes no tagging, an ID of `1`-`4094` tags with the specific ID, and an
ID of `4095` enables trunk mode, allowing the guest to manage its own
tagging. Default: `0`.

<h2 class="pdoc-module-header" id="HostPortGroupState">
<a class="pdoc-member-name" href="/hostPortGroup.ts#L190">interface HostPortGroupState</a>
</h2>

Input properties used for looking up and filtering HostPortGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L194">property activeNics</a>
</h3>

```typescript
activeNics?: pulumi.Input<pulumi.Input<string>[]>;
```


List of active network adapters used for load balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L199">property allowForgedTransmits</a>
</h3>

```typescript
allowForgedTransmits?: pulumi.Input<boolean>;
```


Controls whether or not the virtual network adapter is allowed to send network traffic with a different MAC address
than that of its own.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L203">property allowMacChanges</a>
</h3>

```typescript
allowMacChanges?: pulumi.Input<boolean>;
```


Controls whether or not the Media Access Control (MAC) address can be changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L207">property allowPromiscuous</a>
</h3>

```typescript
allowPromiscuous?: pulumi.Input<boolean>;
```


Enable promiscuous mode on the network. This flag indicates whether or not all traffic is seen on a given port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L212">property checkBeacon</a>
</h3>

```typescript
checkBeacon?: pulumi.Input<boolean>;
```


Enable beacon probing. Requires that the vSwitch has been configured to use a beacon. If disabled, link status is
used only.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L218">property computedPolicy</a>
</h3>

```typescript
computedPolicy?: pulumi.Input<{ ... }>;
```


A map with a full set of the [policy
options][host-vswitch-policy-options] computed from defaults and overrides,
explaining the effective policy for this port group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L222">property failback</a>
</h3>

```typescript
failback?: pulumi.Input<boolean>;
```


If true, the teaming policy will re-activate failed interfaces higher in precedence when they come back up.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L227">property hostSystemId</a>
</h3>

```typescript
hostSystemId?: pulumi.Input<string>;
```


The [managed object ID][docs-about-morefs] of
the host to set the port group up on. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L231">property key</a>
</h3>

```typescript
key?: pulumi.Input<string>;
```


The key for this port group as returned from the vSphere API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L236">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the port group.  Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L240">property notifySwitches</a>
</h3>

```typescript
notifySwitches?: pulumi.Input<boolean>;
```


If true, the teaming policy will notify the broadcast network of a NIC failover, triggering cache updates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L244">property ports</a>
</h3>

```typescript
ports?: pulumi.Input<{ ... }>;
```


A list of ports that currently exist and are used on this port group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L248">property shapingAverageBandwidth</a>
</h3>

```typescript
shapingAverageBandwidth?: pulumi.Input<number>;
```


The average bandwidth in bits per second if traffic shaping is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L252">property shapingBurstSize</a>
</h3>

```typescript
shapingBurstSize?: pulumi.Input<number>;
```


The maximum burst size allowed in bytes if traffic shaping is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L256">property shapingEnabled</a>
</h3>

```typescript
shapingEnabled?: pulumi.Input<boolean>;
```


Enable traffic shaping on this virtual switch or port group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L260">property shapingPeakBandwidth</a>
</h3>

```typescript
shapingPeakBandwidth?: pulumi.Input<number>;
```


The peak bandwidth during bursts in bits per second if traffic shaping is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L264">property standbyNics</a>
</h3>

```typescript
standbyNics?: pulumi.Input<pulumi.Input<string>[]>;
```


List of standby network adapters used for failover.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L269">property teamingPolicy</a>
</h3>

```typescript
teamingPolicy?: pulumi.Input<string>;
```


The network adapter teaming policy. Can be one of loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, or
failover_explicit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L274">property virtualSwitchName</a>
</h3>

```typescript
virtualSwitchName?: pulumi.Input<string>;
```


The name of the virtual switch to bind
this port group to. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostPortGroup.ts#L281">property vlanId</a>
</h3>

```typescript
vlanId?: pulumi.Input<number>;
```


The VLAN ID/trunk mode for this port group.  An ID of
`0` denotes no tagging, an ID of `1`-`4094` tags with the specific ID, and an
ID of `4095` enables trunk mode, allowing the guest to manage its own
tagging. Default: `0`.

<h2 class="pdoc-module-header" id="HostVirtualSwitchArgs">
<a class="pdoc-member-name" href="/hostVirtualSwitch.ts#L338">interface HostVirtualSwitchArgs</a>
</h2>

The set of arguments for constructing a HostVirtualSwitch resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L343">property activeNics</a>
</h3>

```typescript
activeNics: pulumi.Input<pulumi.Input<string>[]>;
```


The list of active network adapters used for load
balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L349">property allowForgedTransmits</a>
</h3>

```typescript
allowForgedTransmits?: pulumi.Input<boolean>;
```


Controls whether or not the virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L354">property allowMacChanges</a>
</h3>

```typescript
allowMacChanges?: pulumi.Input<boolean>;
```


Controls whether or not the Media Access
Control (MAC) address can be changed. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L360">property allowPromiscuous</a>
</h3>

```typescript
allowPromiscuous?: pulumi.Input<boolean>;
```


Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port. Default:
`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L366">property beaconInterval</a>
</h3>

```typescript
beaconInterval?: pulumi.Input<number>;
```


The interval, in seconds, that a NIC beacon
packet is sent out. This can be used with `check_beacon` to
offer link failure capability beyond link status only. Default: `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L373">property checkBeacon</a>
</h3>

```typescript
checkBeacon?: pulumi.Input<boolean>;
```


Enable beacon probing - this requires that the
`beacon_interval` option has been set in the bridge
options. If this is set to `false`, only link status is used to check for
failed NICs.  Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L379">property failback</a>
</h3>

```typescript
failback?: pulumi.Input<boolean>;
```


If set to `true`, the teaming policy will re-activate
failed interfaces higher in precedence when they come back up.  Default:
`true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L384">property hostSystemId</a>
</h3>

```typescript
hostSystemId: pulumi.Input<string>;
```


The [managed object ID][docs-about-morefs] of
the host to set the virtual switch up on. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L389">property linkDiscoveryOperation</a>
</h3>

```typescript
linkDiscoveryOperation?: pulumi.Input<string>;
```


Whether to `advertise` or `listen`
for link discovery traffic. Default: `listen`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L394">property linkDiscoveryProtocol</a>
</h3>

```typescript
linkDiscoveryProtocol?: pulumi.Input<string>;
```


The discovery protocol type.  Valid
types are `cpd` and `lldp`. Default: `cdp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L399">property mtu</a>
</h3>

```typescript
mtu?: pulumi.Input<number>;
```


The maximum transmission unit (MTU) for the virtual
switch. Default: `1500`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L404">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the virtual switch. Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L408">property networkAdapters</a>
</h3>

```typescript
networkAdapters: pulumi.Input<pulumi.Input<string>[]>;
```


The network interfaces to bind to the bridge.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L414">property notifySwitches</a>
</h3>

```typescript
notifySwitches?: pulumi.Input<boolean>;
```


If set to `true`, the teaming policy will
notify the broadcast network of a NIC failover, triggering cache updates.
Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L419">property numberOfPorts</a>
</h3>

```typescript
numberOfPorts?: pulumi.Input<number>;
```


The number of ports to create with this
virtual switch. Default: `128`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L424">property shapingAverageBandwidth</a>
</h3>

```typescript
shapingAverageBandwidth?: pulumi.Input<number>;
```


The average bandwidth in bits per
second if traffic shaping is enabled. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L429">property shapingBurstSize</a>
</h3>

```typescript
shapingBurstSize?: pulumi.Input<number>;
```


The maximum burst size allowed in bytes if
shaping is enabled. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L434">property shapingEnabled</a>
</h3>

```typescript
shapingEnabled?: pulumi.Input<boolean>;
```


Set to `true` to enable the traffic shaper for
ports managed by this virtual switch. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L439">property shapingPeakBandwidth</a>
</h3>

```typescript
shapingPeakBandwidth?: pulumi.Input<number>;
```


The peak bandwidth during bursts in
bits per second if traffic shaping is enabled. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L444">property standbyNics</a>
</h3>

```typescript
standbyNics: pulumi.Input<pulumi.Input<string>[]>;
```


The list of standby network adapters used for
failover.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L450">property teamingPolicy</a>
</h3>

```typescript
teamingPolicy?: pulumi.Input<string>;
```


The network adapter teaming policy. Can be one
of `loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`. Default: `loadbalance_srcid`.

<h2 class="pdoc-module-header" id="HostVirtualSwitchState">
<a class="pdoc-member-name" href="/hostVirtualSwitch.ts#L220">interface HostVirtualSwitchState</a>
</h2>

Input properties used for looking up and filtering HostVirtualSwitch resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L225">property activeNics</a>
</h3>

```typescript
activeNics?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of active network adapters used for load
balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L231">property allowForgedTransmits</a>
</h3>

```typescript
allowForgedTransmits?: pulumi.Input<boolean>;
```


Controls whether or not the virtual
network adapter is allowed to send network traffic with a different MAC
address than that of its own. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L236">property allowMacChanges</a>
</h3>

```typescript
allowMacChanges?: pulumi.Input<boolean>;
```


Controls whether or not the Media Access
Control (MAC) address can be changed. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L242">property allowPromiscuous</a>
</h3>

```typescript
allowPromiscuous?: pulumi.Input<boolean>;
```


Enable promiscuous mode on the network. This
flag indicates whether or not all traffic is seen on a given port. Default:
`false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L248">property beaconInterval</a>
</h3>

```typescript
beaconInterval?: pulumi.Input<number>;
```


The interval, in seconds, that a NIC beacon
packet is sent out. This can be used with `check_beacon` to
offer link failure capability beyond link status only. Default: `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L255">property checkBeacon</a>
</h3>

```typescript
checkBeacon?: pulumi.Input<boolean>;
```


Enable beacon probing - this requires that the
`beacon_interval` option has been set in the bridge
options. If this is set to `false`, only link status is used to check for
failed NICs.  Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L261">property failback</a>
</h3>

```typescript
failback?: pulumi.Input<boolean>;
```


If set to `true`, the teaming policy will re-activate
failed interfaces higher in precedence when they come back up.  Default:
`true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L266">property hostSystemId</a>
</h3>

```typescript
hostSystemId?: pulumi.Input<string>;
```


The [managed object ID][docs-about-morefs] of
the host to set the virtual switch up on. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L271">property linkDiscoveryOperation</a>
</h3>

```typescript
linkDiscoveryOperation?: pulumi.Input<string>;
```


Whether to `advertise` or `listen`
for link discovery traffic. Default: `listen`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L276">property linkDiscoveryProtocol</a>
</h3>

```typescript
linkDiscoveryProtocol?: pulumi.Input<string>;
```


The discovery protocol type.  Valid
types are `cpd` and `lldp`. Default: `cdp`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L281">property mtu</a>
</h3>

```typescript
mtu?: pulumi.Input<number>;
```


The maximum transmission unit (MTU) for the virtual
switch. Default: `1500`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L286">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the virtual switch. Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L290">property networkAdapters</a>
</h3>

```typescript
networkAdapters?: pulumi.Input<pulumi.Input<string>[]>;
```


The network interfaces to bind to the bridge.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L296">property notifySwitches</a>
</h3>

```typescript
notifySwitches?: pulumi.Input<boolean>;
```


If set to `true`, the teaming policy will
notify the broadcast network of a NIC failover, triggering cache updates.
Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L301">property numberOfPorts</a>
</h3>

```typescript
numberOfPorts?: pulumi.Input<number>;
```


The number of ports to create with this
virtual switch. Default: `128`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L306">property shapingAverageBandwidth</a>
</h3>

```typescript
shapingAverageBandwidth?: pulumi.Input<number>;
```


The average bandwidth in bits per
second if traffic shaping is enabled. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L311">property shapingBurstSize</a>
</h3>

```typescript
shapingBurstSize?: pulumi.Input<number>;
```


The maximum burst size allowed in bytes if
shaping is enabled. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L316">property shapingEnabled</a>
</h3>

```typescript
shapingEnabled?: pulumi.Input<boolean>;
```


Set to `true` to enable the traffic shaper for
ports managed by this virtual switch. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L321">property shapingPeakBandwidth</a>
</h3>

```typescript
shapingPeakBandwidth?: pulumi.Input<number>;
```


The peak bandwidth during bursts in
bits per second if traffic shaping is enabled. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L326">property standbyNics</a>
</h3>

```typescript
standbyNics?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of standby network adapters used for
failover.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/hostVirtualSwitch.ts#L332">property teamingPolicy</a>
</h3>

```typescript
teamingPolicy?: pulumi.Input<string>;
```


The network adapter teaming policy. Can be one
of `loadbalance_ip`, `loadbalance_srcmac`, `loadbalance_srcid`, or
`failover_explicit`. Default: `loadbalance_srcid`.

<h2 class="pdoc-module-header" id="LicenseArgs">
<a class="pdoc-member-name" href="/license.ts#L114">interface LicenseArgs</a>
</h2>

The set of arguments for constructing a License resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/license.ts#L118">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A map of key/value pairs to be attached as labels (tags) to the license key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/license.ts#L122">property licenseKey</a>
</h3>

```typescript
licenseKey: pulumi.Input<string>;
```


The license key to add.

<h2 class="pdoc-module-header" id="LicenseState">
<a class="pdoc-member-name" href="/license.ts#L84">interface LicenseState</a>
</h2>

Input properties used for looking up and filtering License resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/license.ts#L88">property editionKey</a>
</h3>

```typescript
editionKey?: pulumi.Input<string>;
```


The product edition of the license key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/license.ts#L92">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A map of key/value pairs to be attached as labels (tags) to the license key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/license.ts#L96">property licenseKey</a>
</h3>

```typescript
licenseKey?: pulumi.Input<string>;
```


The license key to add.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/license.ts#L100">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The display name for the license.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/license.ts#L104">property total</a>
</h3>

```typescript
total?: pulumi.Input<number>;
```


Total number of units (example: CPUs) contained in the license.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/license.ts#L108">property used</a>
</h3>

```typescript
used?: pulumi.Input<number>;
```


The number of units (example: CPUs) assigned to this license.

<h2 class="pdoc-module-header" id="NasDatastoreArgs">
<a class="pdoc-member-name" href="/nasDatastore.ts#L315">interface NasDatastoreArgs</a>
</h2>

The set of arguments for constructing a NasDatastore resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L322">property accessMode</a>
</h3>

```typescript
accessMode?: pulumi.Input<string>;
```


Access mode for the mount point. Can be one of
`readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
that the datastore will be read-write depending on the permissions of the
actual share. Default: `readWrite`. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L329">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


Map of custom attribute ids to attribute
value strings to set on datasource resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L335">property datastoreClusterId</a>
</h3>

```typescript
datastoreClusterId?: pulumi.Input<string>;
```


The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L345">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The relative path to a folder to put this datastore in.
This is a path relative to the datacenter you are deploying the datastore to.
Example: for the `dc1` datacenter, and a provided `folder` of `foo/bar`,
Terraform will place a datastore named `terraform-test` in a datastore folder
located at `/dc1/datastore/foo/bar`, with the final inventory path being
`/dc1/datastore/foo/bar/terraform-test`. Conflicts with
`datastore_cluster_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L350">property hostSystemIds</a>
</h3>

```typescript
hostSystemIds: pulumi.Input<pulumi.Input<string>[]>;
```


The [managed object IDs][docs-about-morefs] of
the hosts to mount the datastore on.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L355">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the datastore. Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L361">property remoteHosts</a>
</h3>

```typescript
remoteHosts: pulumi.Input<pulumi.Input<string>[]>;
```


The hostnames or IP addresses of the remote
server or servers. Only one element should be present for NFS v3 but multiple
can be present for NFS v4.1. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L366">property remotePath</a>
</h3>

```typescript
remotePath: pulumi.Input<string>;
```


The remote path of the mount point. Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L372">property securityType</a>
</h3>

```typescript
securityType?: pulumi.Input<string>;
```


The security type to use when using NFS v4.1.
Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L377">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L383">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of NAS volume. Can be one of `NFS` (to denote
v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
changed.

<h2 class="pdoc-module-header" id="NasDatastoreState">
<a class="pdoc-member-name" href="/nasDatastore.ts#L205">interface NasDatastoreState</a>
</h2>

Input properties used for looking up and filtering NasDatastore resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L212">property accessMode</a>
</h3>

```typescript
accessMode?: pulumi.Input<string>;
```


Access mode for the mount point. Can be one of
`readOnly` or `readWrite`. Note that `readWrite` does not necessarily mean
that the datastore will be read-write depending on the permissions of the
actual share. Default: `readWrite`. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L217">property accessible</a>
</h3>

```typescript
accessible?: pulumi.Input<boolean>;
```


The connectivity status of the datastore. If this is `false`,
some other computed attributes may be out of date.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L221">property capacity</a>
</h3>

```typescript
capacity?: pulumi.Input<number>;
```


Maximum capacity of the datastore, in megabytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L228">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


Map of custom attribute ids to attribute
value strings to set on datasource resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L234">property datastoreClusterId</a>
</h3>

```typescript
datastoreClusterId?: pulumi.Input<string>;
```


The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L244">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The relative path to a folder to put this datastore in.
This is a path relative to the datacenter you are deploying the datastore to.
Example: for the `dc1` datacenter, and a provided `folder` of `foo/bar`,
Terraform will place a datastore named `terraform-test` in a datastore folder
located at `/dc1/datastore/foo/bar`, with the final inventory path being
`/dc1/datastore/foo/bar/terraform-test`. Conflicts with
`datastore_cluster_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L248">property freeSpace</a>
</h3>

```typescript
freeSpace?: pulumi.Input<number>;
```


Available space of this datastore, in megabytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L253">property hostSystemIds</a>
</h3>

```typescript
hostSystemIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The [managed object IDs][docs-about-morefs] of
the hosts to mount the datastore on.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L257">property maintenanceMode</a>
</h3>

```typescript
maintenanceMode?: pulumi.Input<string>;
```


The current maintenance mode state of the datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L262">property multipleHostAccess</a>
</h3>

```typescript
multipleHostAccess?: pulumi.Input<boolean>;
```


If `true`, more than one host in the datacenter has
been configured with access to the datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L267">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the datastore. Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L272">property protocolEndpoint</a>
</h3>

```typescript
protocolEndpoint?: pulumi.Input<string>;
```


Indicates that this NAS volume is a protocol endpoint.
This field is only populated if the host supports virtual datastores.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L278">property remoteHosts</a>
</h3>

```typescript
remoteHosts?: pulumi.Input<pulumi.Input<string>[]>;
```


The hostnames or IP addresses of the remote
server or servers. Only one element should be present for NFS v3 but multiple
can be present for NFS v4.1. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L283">property remotePath</a>
</h3>

```typescript
remotePath?: pulumi.Input<string>;
```


The remote path of the mount point. Forces a new
resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L289">property securityType</a>
</h3>

```typescript
securityType?: pulumi.Input<string>;
```


The security type to use when using NFS v4.1.
Can be one of `AUTH_SYS`, `SEC_KRB5`, or `SEC_KRB5I`. Forces a new resource
if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L294">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L300">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of NAS volume. Can be one of `NFS` (to denote
v3) or `NFS41` (to denote NFS v4.1). Default: `NFS`. Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L305">property uncommittedSpace</a>
</h3>

```typescript
uncommittedSpace?: pulumi.Input<number>;
```


Total additional storage space, in megabytes,
potentially used by all virtual machines on this datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/nasDatastore.ts#L309">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```


The unique locator for the datastore.

<h2 class="pdoc-module-header" id="ProviderArgs">
<a class="pdoc-member-name" href="/provider.ts#L46">interface ProviderArgs</a>
</h2>

The set of arguments for constructing a Provider resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L50">property allowUnverifiedSsl</a>
</h3>

```typescript
allowUnverifiedSsl?: pulumi.Input<boolean>;
```


If set, VMware vSphere client will permit unverifiable SSL certificates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L54">property clientDebug</a>
</h3>

```typescript
clientDebug?: pulumi.Input<boolean>;
```


govmomi debug

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L58">property clientDebugPath</a>
</h3>

```typescript
clientDebugPath?: pulumi.Input<string>;
```


govmomi debug path for debug

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L62">property clientDebugPathRun</a>
</h3>

```typescript
clientDebugPathRun?: pulumi.Input<string>;
```


govmomi debug path for a single run

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L66">property password</a>
</h3>

```typescript
password: pulumi.Input<string>;
```


The user password for vSphere API operations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L70">property persistSession</a>
</h3>

```typescript
persistSession?: pulumi.Input<boolean>;
```


Persist vSphere client sessions to disk

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L74">property restSessionPath</a>
</h3>

```typescript
restSessionPath?: pulumi.Input<string>;
```


The directory to save vSphere REST API sessions to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L78">property user</a>
</h3>

```typescript
user: pulumi.Input<string>;
```


The user name for vSphere API operations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L79">property vcenterServer</a>
</h3>

```typescript
vcenterServer?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L83">property vimSessionPath</a>
</h3>

```typescript
vimSessionPath?: pulumi.Input<string>;
```


The directory to save vSphere SOAP API sessions to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L87">property vsphereServer</a>
</h3>

```typescript
vsphereServer?: pulumi.Input<string>;
```


The vSphere Server name for vSphere API operations.

<h2 class="pdoc-module-header" id="ResourcePoolArgs">
<a class="pdoc-member-name" href="/resourcePool.ts#L254">interface ResourcePoolArgs</a>
</h2>

The set of arguments for constructing a ResourcePool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L260">property cpuExpandable</a>
</h3>

```typescript
cpuExpandable?: pulumi.Input<boolean>;
```


Determines if the reservation on a resource
pool can grow beyond the specified value if the parent resource pool has
unreserved resources. Default: `true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L266">property cpuLimit</a>
</h3>

```typescript
cpuLimit?: pulumi.Input<number>;
```


The CPU utilization of a resource pool will not exceed
this limit, even if there are available resources. Set to `-1` for unlimited.
Default: `-1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L271">property cpuReservation</a>
</h3>

```typescript
cpuReservation?: pulumi.Input<number>;
```


Amount of CPU (MHz) that is guaranteed
available to the resource pool. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L279">property cpuShareLevel</a>
</h3>

```typescript
cpuShareLevel?: pulumi.Input<string>;
```


The CPU allocation level. The level is a
simplified view of shares. Levels map to a pre-determined set of numeric
values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
`low`, `normal`, or `high` are specified values in `cpu_shares` will be
ignored.  Default: `normal`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L285">property cpuShares</a>
</h3>

```typescript
cpuShares?: pulumi.Input<number>;
```


The number of shares allocated for CPU. Used to
determine resource allocation in case of resource contention. If this is set,
`cpu_share_level` must be `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L289">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


A list of custom attributes to set on this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L295">property memoryExpandable</a>
</h3>

```typescript
memoryExpandable?: pulumi.Input<boolean>;
```


Determines if the reservation on a resource
pool can grow beyond the specified value if the parent resource pool has
unreserved resources. Default: `true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L301">property memoryLimit</a>
</h3>

```typescript
memoryLimit?: pulumi.Input<number>;
```


The CPU utilization of a resource pool will not exceed
this limit, even if there are available resources. Set to `-1` for unlimited.
Default: `-1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L306">property memoryReservation</a>
</h3>

```typescript
memoryReservation?: pulumi.Input<number>;
```


Amount of CPU (MHz) that is guaranteed
available to the resource pool. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L314">property memoryShareLevel</a>
</h3>

```typescript
memoryShareLevel?: pulumi.Input<string>;
```


The CPU allocation level. The level is a
simplified view of shares. Levels map to a pre-determined set of numeric
values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
`low`, `normal`, or `high` are specified values in `memory_shares` will be
ignored.  Default: `normal`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L320">property memoryShares</a>
</h3>

```typescript
memoryShares?: pulumi.Input<number>;
```


The number of shares allocated for CPU. Used to
determine resource allocation in case of resource contention. If this is set,
`memory_share_level` must be `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L324">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the resource pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L332">property parentResourcePoolId</a>
</h3>

```typescript
parentResourcePoolId: pulumi.Input<string>;
```


The [managed object ID][docs-about-morefs]
of the parent resource pool. This can be the root resource pool for a cluster
or standalone host, or a resource pool itself. When moving a resource pool
from one parent resource pool to another, both must share a common root
resource pool or the move will fail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L337">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h2 class="pdoc-module-header" id="ResourcePoolState">
<a class="pdoc-member-name" href="/resourcePool.ts#L165">interface ResourcePoolState</a>
</h2>

Input properties used for looking up and filtering ResourcePool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L171">property cpuExpandable</a>
</h3>

```typescript
cpuExpandable?: pulumi.Input<boolean>;
```


Determines if the reservation on a resource
pool can grow beyond the specified value if the parent resource pool has
unreserved resources. Default: `true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L177">property cpuLimit</a>
</h3>

```typescript
cpuLimit?: pulumi.Input<number>;
```


The CPU utilization of a resource pool will not exceed
this limit, even if there are available resources. Set to `-1` for unlimited.
Default: `-1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L182">property cpuReservation</a>
</h3>

```typescript
cpuReservation?: pulumi.Input<number>;
```


Amount of CPU (MHz) that is guaranteed
available to the resource pool. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L190">property cpuShareLevel</a>
</h3>

```typescript
cpuShareLevel?: pulumi.Input<string>;
```


The CPU allocation level. The level is a
simplified view of shares. Levels map to a pre-determined set of numeric
values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
`low`, `normal`, or `high` are specified values in `cpu_shares` will be
ignored.  Default: `normal`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L196">property cpuShares</a>
</h3>

```typescript
cpuShares?: pulumi.Input<number>;
```


The number of shares allocated for CPU. Used to
determine resource allocation in case of resource contention. If this is set,
`cpu_share_level` must be `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L200">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


A list of custom attributes to set on this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L206">property memoryExpandable</a>
</h3>

```typescript
memoryExpandable?: pulumi.Input<boolean>;
```


Determines if the reservation on a resource
pool can grow beyond the specified value if the parent resource pool has
unreserved resources. Default: `true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L212">property memoryLimit</a>
</h3>

```typescript
memoryLimit?: pulumi.Input<number>;
```


The CPU utilization of a resource pool will not exceed
this limit, even if there are available resources. Set to `-1` for unlimited.
Default: `-1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L217">property memoryReservation</a>
</h3>

```typescript
memoryReservation?: pulumi.Input<number>;
```


Amount of CPU (MHz) that is guaranteed
available to the resource pool. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L225">property memoryShareLevel</a>
</h3>

```typescript
memoryShareLevel?: pulumi.Input<string>;
```


The CPU allocation level. The level is a
simplified view of shares. Levels map to a pre-determined set of numeric
values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
`low`, `normal`, or `high` are specified values in `memory_shares` will be
ignored.  Default: `normal`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L231">property memoryShares</a>
</h3>

```typescript
memoryShares?: pulumi.Input<number>;
```


The number of shares allocated for CPU. Used to
determine resource allocation in case of resource contention. If this is set,
`memory_share_level` must be `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L235">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the resource pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L243">property parentResourcePoolId</a>
</h3>

```typescript
parentResourcePoolId?: pulumi.Input<string>;
```


The [managed object ID][docs-about-morefs]
of the parent resource pool. This can be the root resource pool for a cluster
or standalone host, or a resource pool itself. When moving a resource pool
from one parent resource pool to another, both must share a common root
resource pool or the move will fail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/resourcePool.ts#L248">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h2 class="pdoc-module-header" id="StorageDrsVmOverrideArgs">
<a class="pdoc-member-name" href="/storageDrsVmOverride.ts#L140">interface StorageDrsVmOverrideArgs</a>
</h2>

The set of arguments for constructing a StorageDrsVmOverride resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageDrsVmOverride.ts#L146">property datastoreClusterId</a>
</h3>

```typescript
datastoreClusterId: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the datastore cluster to put the override in.
Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageDrsVmOverride.ts#L153">property sdrsAutomationLevel</a>
</h3>

```typescript
sdrsAutomationLevel?: pulumi.Input<string>;
```


Overrides any Storage DRS automation
levels for this virtual machine. Can be one of `automated` or `manual`. When
not specified, the datastore cluster's settings are used according to the
[specific SDRS subsystem][tf-vsphere-datastore-cluster-sdrs-levels].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageDrsVmOverride.ts#L159">property sdrsEnabled</a>
</h3>

```typescript
sdrsEnabled?: pulumi.Input<string>;
```


Overrides the default Storage DRS setting for
this virtual machine. When not specified, the datastore cluster setting is
used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageDrsVmOverride.ts#L167">property sdrsIntraVmAffinity</a>
</h3>

```typescript
sdrsIntraVmAffinity?: pulumi.Input<string>;
```


Overrides the intra-VM affinity setting
for this virtual machine. When `true`, all disks for this virtual machine
will be kept on the same datastore. When `false`, Storage DRS may locate
individual disks on different datastores if it helps satisfy cluster
requirements. When not specified, the datastore cluster's settings are used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageDrsVmOverride.ts#L172">property virtualMachineId</a>
</h3>

```typescript
virtualMachineId: pulumi.Input<string>;
```


The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.

<h2 class="pdoc-module-header" id="StorageDrsVmOverrideState">
<a class="pdoc-member-name" href="/storageDrsVmOverride.ts#L102">interface StorageDrsVmOverrideState</a>
</h2>

Input properties used for looking up and filtering StorageDrsVmOverride resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageDrsVmOverride.ts#L108">property datastoreClusterId</a>
</h3>

```typescript
datastoreClusterId?: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the datastore cluster to put the override in.
Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageDrsVmOverride.ts#L115">property sdrsAutomationLevel</a>
</h3>

```typescript
sdrsAutomationLevel?: pulumi.Input<string>;
```


Overrides any Storage DRS automation
levels for this virtual machine. Can be one of `automated` or `manual`. When
not specified, the datastore cluster's settings are used according to the
[specific SDRS subsystem][tf-vsphere-datastore-cluster-sdrs-levels].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageDrsVmOverride.ts#L121">property sdrsEnabled</a>
</h3>

```typescript
sdrsEnabled?: pulumi.Input<string>;
```


Overrides the default Storage DRS setting for
this virtual machine. When not specified, the datastore cluster setting is
used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageDrsVmOverride.ts#L129">property sdrsIntraVmAffinity</a>
</h3>

```typescript
sdrsIntraVmAffinity?: pulumi.Input<string>;
```


Overrides the intra-VM affinity setting
for this virtual machine. When `true`, all disks for this virtual machine
will be kept on the same datastore. When `false`, Storage DRS may locate
individual disks on different datastores if it helps satisfy cluster
requirements. When not specified, the datastore cluster's settings are used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageDrsVmOverride.ts#L134">property virtualMachineId</a>
</h3>

```typescript
virtualMachineId?: pulumi.Input<string>;
```


The UUID of the virtual machine to create
the override for.  Forces a new resource if changed.

<h2 class="pdoc-module-header" id="TagArgs">
<a class="pdoc-member-name" href="/tag.ts#L97">interface TagArgs</a>
</h2>

The set of arguments for constructing a Tag resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tag.ts#L102">property categoryId</a>
</h3>

```typescript
categoryId: pulumi.Input<string>;
```


The unique identifier of the parent category in
which this tag will be created. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tag.ts#L106">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the tag.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tag.ts#L111">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The display name of the tag. The name must be unique
within its category.

<h2 class="pdoc-module-header" id="TagCategoryArgs">
<a class="pdoc-member-name" href="/tagCategory.ts#L119">interface TagCategoryArgs</a>
</h2>

The set of arguments for constructing a TagCategory resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tagCategory.ts#L125">property associableTypes</a>
</h3>

```typescript
associableTypes: pulumi.Input<pulumi.Input<string>[]>;
```


A list object types that this category is
valid to be assigned to. For a full list, click
here.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tagCategory.ts#L132">property cardinality</a>
</h3>

```typescript
cardinality: pulumi.Input<string>;
```


The number of tags that can be assigned from this
category to a single object at once. Can be one of `SINGLE` (object can only
be assigned one tag in this category), to `MULTIPLE` (object can be assigned
multiple tags in this category). Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tagCategory.ts#L136">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the category.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tagCategory.ts#L140">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the category.

<h2 class="pdoc-module-header" id="TagCategoryState">
<a class="pdoc-member-name" href="/tagCategory.ts#L92">interface TagCategoryState</a>
</h2>

Input properties used for looking up and filtering TagCategory resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tagCategory.ts#L98">property associableTypes</a>
</h3>

```typescript
associableTypes?: pulumi.Input<pulumi.Input<string>[]>;
```


A list object types that this category is
valid to be assigned to. For a full list, click
here.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tagCategory.ts#L105">property cardinality</a>
</h3>

```typescript
cardinality?: pulumi.Input<string>;
```


The number of tags that can be assigned from this
category to a single object at once. Can be one of `SINGLE` (object can only
be assigned one tag in this category), to `MULTIPLE` (object can be assigned
multiple tags in this category). Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tagCategory.ts#L109">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the category.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tagCategory.ts#L113">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the category.

<h2 class="pdoc-module-header" id="TagState">
<a class="pdoc-member-name" href="/tag.ts#L77">interface TagState</a>
</h2>

Input properties used for looking up and filtering Tag resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tag.ts#L82">property categoryId</a>
</h3>

```typescript
categoryId?: pulumi.Input<string>;
```


The unique identifier of the parent category in
which this tag will be created. Forces a new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tag.ts#L86">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the tag.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/tag.ts#L91">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The display name of the tag. The name must be unique
within its category.

<h2 class="pdoc-module-header" id="VappContainerArgs">
<a class="pdoc-member-name" href="/vappContainer.ts#L270">interface VappContainerArgs</a>
</h2>

The set of arguments for constructing a VappContainer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L276">property cpuExpandable</a>
</h3>

```typescript
cpuExpandable?: pulumi.Input<boolean>;
```


Determines if the reservation on a vApp
container can grow beyond the specified value if the parent resource pool has
unreserved resources. Default: `true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L283">property cpuLimit</a>
</h3>

```typescript
cpuLimit?: pulumi.Input<number>;
```


The CPU utilization of a vApp container will not
exceed this limit, even if there are available resources. Set to `-1` for
unlimited.
Default: `-1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L288">property cpuReservation</a>
</h3>

```typescript
cpuReservation?: pulumi.Input<number>;
```


Amount of CPU (MHz) that is guaranteed
available to the vApp container. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L296">property cpuShareLevel</a>
</h3>

```typescript
cpuShareLevel?: pulumi.Input<string>;
```


The CPU allocation level. The level is a
simplified view of shares. Levels map to a pre-determined set of numeric
values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
`low`, `normal`, or `high` are specified values in `cpu_shares` will be
ignored.  Default: `normal`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L302">property cpuShares</a>
</h3>

```typescript
cpuShares?: pulumi.Input<number>;
```


The number of shares allocated for CPU. Used to
determine resource allocation in case of resource contention. If this is set,
`cpu_share_level` must be `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L306">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


A list of custom attributes to set on this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L312">property memoryExpandable</a>
</h3>

```typescript
memoryExpandable?: pulumi.Input<boolean>;
```


Determines if the reservation on a vApp
container can grow beyond the specified value if the parent resource pool has
unreserved resources. Default: `true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L319">property memoryLimit</a>
</h3>

```typescript
memoryLimit?: pulumi.Input<number>;
```


The CPU utilization of a vApp container will not
exceed this limit, even if there are available resources. Set to `-1` for
unlimited.
Default: `-1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L324">property memoryReservation</a>
</h3>

```typescript
memoryReservation?: pulumi.Input<number>;
```


Amount of CPU (MHz) that is guaranteed
available to the vApp container. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L332">property memoryShareLevel</a>
</h3>

```typescript
memoryShareLevel?: pulumi.Input<string>;
```


The CPU allocation level. The level is a
simplified view of shares. Levels map to a pre-determined set of numeric
values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
`low`, `normal`, or `high` are specified values in `memory_shares` will be
ignored.  Default: `normal`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L338">property memoryShares</a>
</h3>

```typescript
memoryShares?: pulumi.Input<number>;
```


The number of shares allocated for CPU. Used to
determine resource allocation in case of resource contention. If this is set,
`memory_share_level` must be `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L342">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the vApp container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L347">property parentFolderId</a>
</h3>

```typescript
parentFolderId?: pulumi.Input<string>;
```


The [managed object ID][docs-about-morefs] of
the vApp container's parent folder.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L355">property parentResourcePoolId</a>
</h3>

```typescript
parentResourcePoolId: pulumi.Input<string>;
```


The [managed object ID][docs-about-morefs]
of the parent resource pool. This can be the root resource pool for a cluster
or standalone host, or a resource pool itself. When moving a vApp container
from one parent resource pool to another, both must share a common root
resource pool or the move will fail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L360">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h2 class="pdoc-module-header" id="VappContainerState">
<a class="pdoc-member-name" href="/vappContainer.ts#L174">interface VappContainerState</a>
</h2>

Input properties used for looking up and filtering VappContainer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L180">property cpuExpandable</a>
</h3>

```typescript
cpuExpandable?: pulumi.Input<boolean>;
```


Determines if the reservation on a vApp
container can grow beyond the specified value if the parent resource pool has
unreserved resources. Default: `true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L187">property cpuLimit</a>
</h3>

```typescript
cpuLimit?: pulumi.Input<number>;
```


The CPU utilization of a vApp container will not
exceed this limit, even if there are available resources. Set to `-1` for
unlimited.
Default: `-1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L192">property cpuReservation</a>
</h3>

```typescript
cpuReservation?: pulumi.Input<number>;
```


Amount of CPU (MHz) that is guaranteed
available to the vApp container. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L200">property cpuShareLevel</a>
</h3>

```typescript
cpuShareLevel?: pulumi.Input<string>;
```


The CPU allocation level. The level is a
simplified view of shares. Levels map to a pre-determined set of numeric
values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
`low`, `normal`, or `high` are specified values in `cpu_shares` will be
ignored.  Default: `normal`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L206">property cpuShares</a>
</h3>

```typescript
cpuShares?: pulumi.Input<number>;
```


The number of shares allocated for CPU. Used to
determine resource allocation in case of resource contention. If this is set,
`cpu_share_level` must be `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L210">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


A list of custom attributes to set on this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L216">property memoryExpandable</a>
</h3>

```typescript
memoryExpandable?: pulumi.Input<boolean>;
```


Determines if the reservation on a vApp
container can grow beyond the specified value if the parent resource pool has
unreserved resources. Default: `true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L223">property memoryLimit</a>
</h3>

```typescript
memoryLimit?: pulumi.Input<number>;
```


The CPU utilization of a vApp container will not
exceed this limit, even if there are available resources. Set to `-1` for
unlimited.
Default: `-1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L228">property memoryReservation</a>
</h3>

```typescript
memoryReservation?: pulumi.Input<number>;
```


Amount of CPU (MHz) that is guaranteed
available to the vApp container. Default: `0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L236">property memoryShareLevel</a>
</h3>

```typescript
memoryShareLevel?: pulumi.Input<string>;
```


The CPU allocation level. The level is a
simplified view of shares. Levels map to a pre-determined set of numeric
values for shares. Can be one of `low`, `normal`, `high`, or `custom`. When
`low`, `normal`, or `high` are specified values in `memory_shares` will be
ignored.  Default: `normal`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L242">property memoryShares</a>
</h3>

```typescript
memoryShares?: pulumi.Input<number>;
```


The number of shares allocated for CPU. Used to
determine resource allocation in case of resource contention. If this is set,
`memory_share_level` must be `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L246">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the vApp container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L251">property parentFolderId</a>
</h3>

```typescript
parentFolderId?: pulumi.Input<string>;
```


The [managed object ID][docs-about-morefs] of
the vApp container's parent folder.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L259">property parentResourcePoolId</a>
</h3>

```typescript
parentResourcePoolId?: pulumi.Input<string>;
```


The [managed object ID][docs-about-morefs]
of the parent resource pool. This can be the root resource pool for a cluster
or standalone host, or a resource pool itself. When moving a vApp container
from one parent resource pool to another, both must share a common root
resource pool or the move will fail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vappContainer.ts#L264">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h2 class="pdoc-module-header" id="VirtualDiskArgs">
<a class="pdoc-member-name" href="/virtualDisk.ts#L156">interface VirtualDiskArgs</a>
</h2>

The set of arguments for constructing a VirtualDisk resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L161">property adapterType</a>
</h3>

```typescript
adapterType?: pulumi.Input<string>;
```


The adapter type for this virtual disk. Can be
one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L167">property createDirectories</a>
</h3>

```typescript
createDirectories?: pulumi.Input<boolean>;
```


Tells the resource to create any
directories that are a part of the `vmdk_path` parameter if they are missing.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L173">property datacenter</a>
</h3>

```typescript
datacenter?: pulumi.Input<string>;
```


The name of the datacenter in which to create the
disk. Can be omitted when when ESXi or if there is only one datacenter in
your infrastructure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L178">property datastore</a>
</h3>

```typescript
datastore: pulumi.Input<string>;
```


The name of the datastore in which to create the
disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L182">property size</a>
</h3>

```typescript
size: pulumi.Input<number>;
```


Size of the disk (in GB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L189">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of disk to create. Can be one of
`eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
information on what each kind of disk provisioning policy means, click
[here][docs-vmware-vm-disk-provisioning].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L194">property vmdkPath</a>
</h3>

```typescript
vmdkPath: pulumi.Input<string>;
```


The path, including filename, of the virtual disk to
be created.  This needs to end in `.vmdk`.

<h2 class="pdoc-module-header" id="VirtualDiskState">
<a class="pdoc-member-name" href="/virtualDisk.ts#L112">interface VirtualDiskState</a>
</h2>

Input properties used for looking up and filtering VirtualDisk resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L117">property adapterType</a>
</h3>

```typescript
adapterType?: pulumi.Input<string>;
```


The adapter type for this virtual disk. Can be
one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L123">property createDirectories</a>
</h3>

```typescript
createDirectories?: pulumi.Input<boolean>;
```


Tells the resource to create any
directories that are a part of the `vmdk_path` parameter if they are missing.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L129">property datacenter</a>
</h3>

```typescript
datacenter?: pulumi.Input<string>;
```


The name of the datacenter in which to create the
disk. Can be omitted when when ESXi or if there is only one datacenter in
your infrastructure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L134">property datastore</a>
</h3>

```typescript
datastore?: pulumi.Input<string>;
```


The name of the datastore in which to create the
disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L138">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```


Size of the disk (in GB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L145">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of disk to create. Can be one of
`eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
information on what each kind of disk provisioning policy means, click
[here][docs-vmware-vm-disk-provisioning].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualDisk.ts#L150">property vmdkPath</a>
</h3>

```typescript
vmdkPath?: pulumi.Input<string>;
```


The path, including filename, of the virtual disk to
be created.  This needs to end in `.vmdk`.

<h2 class="pdoc-module-header" id="VirtualMachineArgs">
<a class="pdoc-member-name" href="/virtualMachine.ts#L989">interface VirtualMachineArgs</a>
</h2>

The set of arguments for constructing a VirtualMachine resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L994">property alternateGuestName</a>
</h3>

```typescript
alternateGuestName?: pulumi.Input<string>;
```


The guest name for the operating system
when `guest_id` is `other` or `other-64`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L999">property annotation</a>
</h3>

```typescript
annotation?: pulumi.Input<string>;
```


A user-provided description of the virtual machine.
The default is no annotation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1004">property bootDelay</a>
</h3>

```typescript
bootDelay?: pulumi.Input<number>;
```


The number of milliseconds to wait before starting
the boot sequence. The default is no delay.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1010">property bootRetryDelay</a>
</h3>

```typescript
bootRetryDelay?: pulumi.Input<number>;
```


The number of milliseconds to wait before
retrying the boot sequence. This only valid if `boot_retry_enabled` is true.
Default: `10000` (10 seconds).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1016">property bootRetryEnabled</a>
</h3>

```typescript
bootRetryEnabled?: pulumi.Input<boolean>;
```


If set to true, a virtual machine that
fails to boot will try again after the delay defined in `boot_retry_delay`.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1021">property cdrom</a>
</h3>

```typescript
cdrom?: pulumi.Input<{ ... }>;
```


A specification for a CDROM device on this virtual
machine. See CDROM options below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1028">property clone</a>
</h3>

```typescript
clone?: pulumi.Input<{ ... }>;
```


When specified, the VM will be created as a clone of a
specified template. Optional customization options can be submitted as well.
See creating a virtual machine from a
template for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1033">property cpuHotAddEnabled</a>
</h3>

```typescript
cpuHotAddEnabled?: pulumi.Input<boolean>;
```


Allow CPUs to be added to this virtual
machine while it is running.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1038">property cpuHotRemoveEnabled</a>
</h3>

```typescript
cpuHotRemoveEnabled?: pulumi.Input<boolean>;
```


Allow CPUs to be removed to this
virtual machine while it is running.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1044">property cpuLimit</a>
</h3>

```typescript
cpuLimit?: pulumi.Input<number>;
```


The maximum amount of CPU (in MHz) that this virtual
machine can consume, regardless of available resources. The default is no
limit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1049">property cpuPerformanceCountersEnabled</a>
</h3>

```typescript
cpuPerformanceCountersEnabled?: pulumi.Input<boolean>;
```


Enable CPU performance
counters on this virtual machine. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1054">property cpuReservation</a>
</h3>

```typescript
cpuReservation?: pulumi.Input<number>;
```


The amount of CPU (in MHz) that this virtual
machine is guaranteed. The default is no reservation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1059">property cpuShareCount</a>
</h3>

```typescript
cpuShareCount?: pulumi.Input<number>;
```


The number of CPU shares allocated to the
virtual machine when the `cpu_share_level` is `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1064">property cpuShareLevel</a>
</h3>

```typescript
cpuShareLevel?: pulumi.Input<string>;
```


The allocation level for CPU resources. Can be
one of `high`, `low`, `normal`, or `custom`. Default: `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1071">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


Map of custom attribute ids to attribute
value strings to set for virtual machine. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1079">property datastoreClusterId</a>
</h3>

```typescript
datastoreClusterId?: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the datastore cluster ID to use. This setting
applies to entire virtual machine and implies that you wish to use Storage
DRS with this virtual machine. See the section on virtual machine
migration for details on changing this value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1084">property datastoreId</a>
</h3>

```typescript
datastoreId?: pulumi.Input<string>;
```


The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1089">property disks</a>
</h3>

```typescript
disks?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A specification for a virtual disk device on this virtual
machine. See disk options below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1094">property efiSecureBootEnabled</a>
</h3>

```typescript
efiSecureBootEnabled?: pulumi.Input<boolean>;
```


When the `firmware` type is set to is
`efi`, this enables EFI secure boot. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1099">property enableDiskUuid</a>
</h3>

```typescript
enableDiskUuid?: pulumi.Input<boolean>;
```


Expose the UUIDs of attached virtual disks to
the virtual machine, allowing access to them in the guest. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1104">property enableLogging</a>
</h3>

```typescript
enableLogging?: pulumi.Input<boolean>;
```


Enable logging of virtual machine events to a
log file stored in the virtual machine directory. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1110">property eptRviMode</a>
</h3>

```typescript
eptRviMode?: pulumi.Input<string>;
```


The EPT/RVI (hardware memory virtualization)
setting for this virtual machine. Can be one of `automatic`, `on`, or `off`.
Default: `automatic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1116">property extraConfig</a>
</h3>

```typescript
extraConfig?: pulumi.Input<{ ... }>;
```


Extra configuration data for this virtual
machine. Can be used to supply advanced parameters not normally in
configuration, such as data for cloud-config (under the guestinfo namespace).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1121">property firmware</a>
</h3>

```typescript
firmware?: pulumi.Input<string>;
```


The firmware interface to use on the virtual machine.
Can be one of `bios` or `EFI`. Default: `bios`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1126">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The path to the folder to put this virtual machine in,
relative to the datacenter that the resource pool is in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1133">property forcePowerOff</a>
</h3>

```typescript
forcePowerOff?: pulumi.Input<boolean>;
```


If a guest shutdown failed or timed out while
updating or destroying (see
`shutdown_wait_timeout`), force the power-off of
the virtual machine. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1138">property guestId</a>
</h3>

```typescript
guestId?: pulumi.Input<string>;
```


The guest ID for the operating system type. For a
full list of possible values, see [here][vmware-docs-guest-ids]. Default: `other-64`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1147">property hostSystemId</a>
</h3>

```typescript
hostSystemId?: pulumi.Input<string>;
```


An optional [managed object reference
ID][docs-about-morefs] of a host to put this virtual machine on. See the
section on virtual machine migration for
details on changing this value. If a `host_system_id` is not supplied,
vSphere will select a host in the resource pool to place the virtual machine,
according to any defaults or DRS policies in place.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1153">property hvMode</a>
</h3>

```typescript
hvMode?: pulumi.Input<string>;
```


The (non-nested) hardware virtualization setting for
this virtual machine. Can be one of `hvAuto`, `hvOn`, or `hvOff`. Default:
`hvAuto`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1161">property latencySensitivity</a>
</h3>

```typescript
latencySensitivity?: pulumi.Input<string>;
```


Controls the scheduling delay of the
virtual machine. Use a higher sensitivity for applications that require lower
latency, such as VOIP, media player applications, or applications that
require frequent access to mouse or keyboard devices. Can be one of `low`,
`normal`, `medium`, or `high`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1166">property memory</a>
</h3>

```typescript
memory?: pulumi.Input<number>;
```


The size of the virtual machine's memory, in MB.
Default: `1024` (1 GB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1171">property memoryHotAddEnabled</a>
</h3>

```typescript
memoryHotAddEnabled?: pulumi.Input<boolean>;
```


Allow memory to be added to this
virtual machine while it is running.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1177">property memoryLimit</a>
</h3>

```typescript
memoryLimit?: pulumi.Input<number>;
```


The maximum amount of memory (in MB) that this
virtual machine can consume, regardless of available resources. The default
is no limit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1182">property memoryReservation</a>
</h3>

```typescript
memoryReservation?: pulumi.Input<number>;
```


The amount of memory (in MB) that this
virtual machine is guaranteed. The default is no reservation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1187">property memoryShareCount</a>
</h3>

```typescript
memoryShareCount?: pulumi.Input<number>;
```


The number of memory shares allocated to
the virtual machine when the `memory_share_level` is `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1192">property memoryShareLevel</a>
</h3>

```typescript
memoryShareLevel?: pulumi.Input<string>;
```


The allocation level for memory resources.
Can be one of `high`, `low`, `normal`, or `custom`. Default: `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1199">property migrateWaitTimeout</a>
</h3>

```typescript
migrateWaitTimeout?: pulumi.Input<number>;
```


The amount of time, in minutes, to wait
for a virtual machine migration to complete before failing. Default: 10
minutes. Also see the section on virtual machine
migration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1204">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


An alias for both `label` and `path`, the latter when
using `attach`. Required if not using `label`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1210">property nestedHvEnabled</a>
</h3>

```typescript
nestedHvEnabled?: pulumi.Input<boolean>;
```


Enable nested hardware virtualization on
this virtual machine, facilitating nested virtualization in the guest.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1216">property networkInterfaces</a>
</h3>

```typescript
networkInterfaces: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A specification for a virtual NIC on this
virtual machine. See network interface options
below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1222">property numCoresPerSocket</a>
</h3>

```typescript
numCoresPerSocket?: pulumi.Input<number>;
```


The number of cores to distribute among
the CPUs in this virtual machine. If specified, the value supplied to
`num_cpus` must be evenly divisible by this value. Default: `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1227">property numCpus</a>
</h3>

```typescript
numCpus?: pulumi.Input<number>;
```


The number of virtual processors to assign to this
virtual machine. Default: `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1234">property resourcePoolId</a>
</h3>

```typescript
resourcePoolId: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the resource pool to put this virtual machine in.
See the section on virtual machine migration
for details on changing this value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1239">property runToolsScriptsAfterPowerOn</a>
</h3>

```typescript
runToolsScriptsAfterPowerOn?: pulumi.Input<boolean>;
```


Enable the execution of
post-power-on scripts when VMware tools is installed. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1244">property runToolsScriptsAfterResume</a>
</h3>

```typescript
runToolsScriptsAfterResume?: pulumi.Input<boolean>;
```


Enable the execution of
post-resume scripts when VMware tools is installed. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1249">property runToolsScriptsBeforeGuestReboot</a>
</h3>

```typescript
runToolsScriptsBeforeGuestReboot?: pulumi.Input<boolean>;
```


Enable the execution of
pre-reboot scripts when VMware tools is installed. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1254">property runToolsScriptsBeforeGuestShutdown</a>
</h3>

```typescript
runToolsScriptsBeforeGuestShutdown?: pulumi.Input<boolean>;
```


Enable the execution
of pre-shutdown scripts when VMware tools is installed. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1259">property runToolsScriptsBeforeGuestStandby</a>
</h3>

```typescript
runToolsScriptsBeforeGuestStandby?: pulumi.Input<boolean>;
```


Enable the execution of
pre-standby scripts when VMware tools is installed. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1264">property scsiBusSharing</a>
</h3>

```typescript
scsiBusSharing?: pulumi.Input<string>;
```


Mode for sharing the SCSI bus. The modes are
physicalSharing, virtualSharing, and noSharing. Default: `noSharing`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1271">property scsiControllerCount</a>
</h3>

```typescript
scsiControllerCount?: pulumi.Input<number>;
```


The number of SCSI controllers that
Terraform manages on this virtual machine. This directly affects the amount
of disks you can add to the virtual machine and the maximum disk unit number.
Note that lowering this value does not remove controllers. Default: `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1277">property scsiType</a>
</h3>

```typescript
scsiType?: pulumi.Input<string>;
```


The type of SCSI bus this virtual machine will have.
Can be one of lsilogic (LSI Logic Parallel), lsilogic-sas (LSI Logic SAS) or
pvscsi (VMware Paravirtual). Defualt: `pvscsi`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1284">property shutdownWaitTimeout</a>
</h3>

```typescript
shutdownWaitTimeout?: pulumi.Input<number>;
```


The amount of time, in minutes, to wait
for a graceful guest shutdown when making necessary updates to the virtual
machine. If `force_power_off` is set to true, the VM will be force powered-off
after this timeout, otherwise an error is returned. Default: 3 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1290">property swapPlacementPolicy</a>
</h3>

```typescript
swapPlacementPolicy?: pulumi.Input<string>;
```


The swap file placement policy for this
virtual machine. Can be one of `inherit`, `hostLocal`, or `vmDirectory`.
Default: `inherit`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1295">property syncTimeWithHost</a>
</h3>

```typescript
syncTimeWithHost?: pulumi.Input<boolean>;
```


Enable guest clock synchronization with
the host. Requires VMware tools to be installed. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1300">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1308">property vapp</a>
</h3>

```typescript
vapp?: pulumi.Input<{ ... }>;
```


Optional vApp configuration. The only sub-key available
is `properties`, which is a key/value map of properties for virtual machines
imported from OVF or OVA files. See Using vApp properties to supply OVF/OVA
configuration for
more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1315">property waitForGuestNetRoutable</a>
</h3>

```typescript
waitForGuestNetRoutable?: pulumi.Input<boolean>;
```


Controls whether or not the guest
network waiter waits for a routable address. When `false`, the waiter does
not wait for a default gateway, nor are IP addresses checked against any
discovered default gateways as part of its success criteria. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L1321">property waitForGuestNetTimeout</a>
</h3>

```typescript
waitForGuestNetTimeout?: pulumi.Input<number>;
```


The amount of time, in minutes, to
wait for an available IP address on this virtual machine. A value less than 1
disables the waiter. Default: 5 minutes.

<h2 class="pdoc-module-header" id="VirtualMachineSnapshotArgs">
<a class="pdoc-member-name" href="/virtualMachineSnapshot.ts#L169">interface VirtualMachineSnapshotArgs</a>
</h2>

The set of arguments for constructing a VirtualMachineSnapshot resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L175">property consolidate</a>
</h3>

```typescript
consolidate?: pulumi.Input<boolean>;
```


If set to `true`, the delta disks involved in this
snapshot will be consolidated into the parent when this resource is
destroyed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L179">property description</a>
</h3>

```typescript
description: pulumi.Input<string>;
```


A description for the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L184">property memory</a>
</h3>

```typescript
memory: pulumi.Input<boolean>;
```


If set to `true`, a dump of the internal state of the
virtual machine is included in the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L190">property quiesce</a>
</h3>

```typescript
quiesce: pulumi.Input<boolean>;
```


If set to `true`, and the virtual machine is powered
on when the snapshot is taken, VMware Tools is used to quiesce the file
system in the virtual machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L195">property removeChildren</a>
</h3>

```typescript
removeChildren?: pulumi.Input<boolean>;
```


If set to `true`, the entire snapshot subtree
is removed when this resource is destroyed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L199">property snapshotName</a>
</h3>

```typescript
snapshotName: pulumi.Input<string>;
```


The name of the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L203">property virtualMachineUuid</a>
</h3>

```typescript
virtualMachineUuid: pulumi.Input<string>;
```


The virtual machine UUID.

<h2 class="pdoc-module-header" id="VirtualMachineSnapshotState">
<a class="pdoc-member-name" href="/virtualMachineSnapshot.ts#L129">interface VirtualMachineSnapshotState</a>
</h2>

Input properties used for looking up and filtering VirtualMachineSnapshot resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L135">property consolidate</a>
</h3>

```typescript
consolidate?: pulumi.Input<boolean>;
```


If set to `true`, the delta disks involved in this
snapshot will be consolidated into the parent when this resource is
destroyed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L139">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L144">property memory</a>
</h3>

```typescript
memory?: pulumi.Input<boolean>;
```


If set to `true`, a dump of the internal state of the
virtual machine is included in the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L150">property quiesce</a>
</h3>

```typescript
quiesce?: pulumi.Input<boolean>;
```


If set to `true`, and the virtual machine is powered
on when the snapshot is taken, VMware Tools is used to quiesce the file
system in the virtual machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L155">property removeChildren</a>
</h3>

```typescript
removeChildren?: pulumi.Input<boolean>;
```


If set to `true`, the entire snapshot subtree
is removed when this resource is destroyed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L159">property snapshotName</a>
</h3>

```typescript
snapshotName?: pulumi.Input<string>;
```


The name of the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachineSnapshot.ts#L163">property virtualMachineUuid</a>
</h3>

```typescript
virtualMachineUuid?: pulumi.Input<string>;
```


The virtual machine UUID.

<h2 class="pdoc-module-header" id="VirtualMachineState">
<a class="pdoc-member-name" href="/virtualMachine.ts#L589">interface VirtualMachineState</a>
</h2>

Input properties used for looking up and filtering VirtualMachine resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L594">property alternateGuestName</a>
</h3>

```typescript
alternateGuestName?: pulumi.Input<string>;
```


The guest name for the operating system
when `guest_id` is `other` or `other-64`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L599">property annotation</a>
</h3>

```typescript
annotation?: pulumi.Input<string>;
```


A user-provided description of the virtual machine.
The default is no annotation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L604">property bootDelay</a>
</h3>

```typescript
bootDelay?: pulumi.Input<number>;
```


The number of milliseconds to wait before starting
the boot sequence. The default is no delay.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L610">property bootRetryDelay</a>
</h3>

```typescript
bootRetryDelay?: pulumi.Input<number>;
```


The number of milliseconds to wait before
retrying the boot sequence. This only valid if `boot_retry_enabled` is true.
Default: `10000` (10 seconds).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L616">property bootRetryEnabled</a>
</h3>

```typescript
bootRetryEnabled?: pulumi.Input<boolean>;
```


If set to true, a virtual machine that
fails to boot will try again after the delay defined in `boot_retry_delay`.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L621">property cdrom</a>
</h3>

```typescript
cdrom?: pulumi.Input<{ ... }>;
```


A specification for a CDROM device on this virtual
machine. See CDROM options below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L627">property changeVersion</a>
</h3>

```typescript
changeVersion?: pulumi.Input<string>;
```


A unique identifier for a given version of the last
configuration applied, such the timestamp of the last update to the
configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L634">property clone</a>
</h3>

```typescript
clone?: pulumi.Input<{ ... }>;
```


When specified, the VM will be created as a clone of a
specified template. Optional customization options can be submitted as well.
See creating a virtual machine from a
template for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L639">property cpuHotAddEnabled</a>
</h3>

```typescript
cpuHotAddEnabled?: pulumi.Input<boolean>;
```


Allow CPUs to be added to this virtual
machine while it is running.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L644">property cpuHotRemoveEnabled</a>
</h3>

```typescript
cpuHotRemoveEnabled?: pulumi.Input<boolean>;
```


Allow CPUs to be removed to this
virtual machine while it is running.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L650">property cpuLimit</a>
</h3>

```typescript
cpuLimit?: pulumi.Input<number>;
```


The maximum amount of CPU (in MHz) that this virtual
machine can consume, regardless of available resources. The default is no
limit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L655">property cpuPerformanceCountersEnabled</a>
</h3>

```typescript
cpuPerformanceCountersEnabled?: pulumi.Input<boolean>;
```


Enable CPU performance
counters on this virtual machine. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L660">property cpuReservation</a>
</h3>

```typescript
cpuReservation?: pulumi.Input<number>;
```


The amount of CPU (in MHz) that this virtual
machine is guaranteed. The default is no reservation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L665">property cpuShareCount</a>
</h3>

```typescript
cpuShareCount?: pulumi.Input<number>;
```


The number of CPU shares allocated to the
virtual machine when the `cpu_share_level` is `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L670">property cpuShareLevel</a>
</h3>

```typescript
cpuShareLevel?: pulumi.Input<string>;
```


The allocation level for CPU resources. Can be
one of `high`, `low`, `normal`, or `custom`. Default: `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L677">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


Map of custom attribute ids to attribute
value strings to set for virtual machine. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L685">property datastoreClusterId</a>
</h3>

```typescript
datastoreClusterId?: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the datastore cluster ID to use. This setting
applies to entire virtual machine and implies that you wish to use Storage
DRS with this virtual machine. See the section on virtual machine
migration for details on changing this value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L690">property datastoreId</a>
</h3>

```typescript
datastoreId?: pulumi.Input<string>;
```


The datastore ID that the ISO is located in.
Requried for using a datastore ISO. Conflicts with `client_device`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L700">property defaultIpAddress</a>
</h3>

```typescript
defaultIpAddress?: pulumi.Input<string>;
```


The IP address selected by Terraform to be used with
any [provisioners][tf-docs-provisioners] configured on this resource.
Whenever possible, this is the first IPv4 address that is reachable through
the default gateway configured on the machine, then the first reachable IPv6
address, and then the first general discovered address if neither exist. If
VMware tools is not running on the virtual machine, or if the VM is powered
off, this value will be blank.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L705">property disks</a>
</h3>

```typescript
disks?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A specification for a virtual disk device on this virtual
machine. See disk options below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L710">property efiSecureBootEnabled</a>
</h3>

```typescript
efiSecureBootEnabled?: pulumi.Input<boolean>;
```


When the `firmware` type is set to is
`efi`, this enables EFI secure boot. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L715">property enableDiskUuid</a>
</h3>

```typescript
enableDiskUuid?: pulumi.Input<boolean>;
```


Expose the UUIDs of attached virtual disks to
the virtual machine, allowing access to them in the guest. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L720">property enableLogging</a>
</h3>

```typescript
enableLogging?: pulumi.Input<boolean>;
```


Enable logging of virtual machine events to a
log file stored in the virtual machine directory. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L726">property eptRviMode</a>
</h3>

```typescript
eptRviMode?: pulumi.Input<string>;
```


The EPT/RVI (hardware memory virtualization)
setting for this virtual machine. Can be one of `automatic`, `on`, or `off`.
Default: `automatic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L732">property extraConfig</a>
</h3>

```typescript
extraConfig?: pulumi.Input<{ ... }>;
```


Extra configuration data for this virtual
machine. Can be used to supply advanced parameters not normally in
configuration, such as data for cloud-config (under the guestinfo namespace).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L737">property firmware</a>
</h3>

```typescript
firmware?: pulumi.Input<string>;
```


The firmware interface to use on the virtual machine.
Can be one of `bios` or `EFI`. Default: `bios`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L742">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The path to the folder to put this virtual machine in,
relative to the datacenter that the resource pool is in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L749">property forcePowerOff</a>
</h3>

```typescript
forcePowerOff?: pulumi.Input<boolean>;
```


If a guest shutdown failed or timed out while
updating or destroying (see
`shutdown_wait_timeout`), force the power-off of
the virtual machine. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L754">property guestId</a>
</h3>

```typescript
guestId?: pulumi.Input<string>;
```


The guest ID for the operating system type. For a
full list of possible values, see [here][vmware-docs-guest-ids]. Default: `other-64`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L762">property guestIpAddresses</a>
</h3>

```typescript
guestIpAddresses?: pulumi.Input<pulumi.Input<string>[]>;
```


The current list of IP addresses on this machine,
including the value of `default_ip_address`. If VMware tools is not running
on the virtual machine, or if the VM is powered off, this list will be empty.
* `moid`: The [managed object reference ID][docs-about-morefs] of the created
virtual machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L771">property hostSystemId</a>
</h3>

```typescript
hostSystemId?: pulumi.Input<string>;
```


An optional [managed object reference
ID][docs-about-morefs] of a host to put this virtual machine on. See the
section on virtual machine migration for
details on changing this value. If a `host_system_id` is not supplied,
vSphere will select a host in the resource pool to place the virtual machine,
according to any defaults or DRS policies in place.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L777">property hvMode</a>
</h3>

```typescript
hvMode?: pulumi.Input<string>;
```


The (non-nested) hardware virtualization setting for
this virtual machine. Can be one of `hvAuto`, `hvOn`, or `hvOff`. Default:
`hvAuto`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L784">property imported</a>
</h3>

```typescript
imported?: pulumi.Input<boolean>;
```


This is flagged if the virtual machine has been imported, or the
state has been migrated from a previous version of the resource. It
influences the behavior of the first post-import apply operation. See the
section on importing below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L792">property latencySensitivity</a>
</h3>

```typescript
latencySensitivity?: pulumi.Input<string>;
```


Controls the scheduling delay of the
virtual machine. Use a higher sensitivity for applications that require lower
latency, such as VOIP, media player applications, or applications that
require frequent access to mouse or keyboard devices. Can be one of `low`,
`normal`, `medium`, or `high`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L797">property memory</a>
</h3>

```typescript
memory?: pulumi.Input<number>;
```


The size of the virtual machine's memory, in MB.
Default: `1024` (1 GB).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L802">property memoryHotAddEnabled</a>
</h3>

```typescript
memoryHotAddEnabled?: pulumi.Input<boolean>;
```


Allow memory to be added to this
virtual machine while it is running.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L808">property memoryLimit</a>
</h3>

```typescript
memoryLimit?: pulumi.Input<number>;
```


The maximum amount of memory (in MB) that this
virtual machine can consume, regardless of available resources. The default
is no limit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L813">property memoryReservation</a>
</h3>

```typescript
memoryReservation?: pulumi.Input<number>;
```


The amount of memory (in MB) that this
virtual machine is guaranteed. The default is no reservation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L818">property memoryShareCount</a>
</h3>

```typescript
memoryShareCount?: pulumi.Input<number>;
```


The number of memory shares allocated to
the virtual machine when the `memory_share_level` is `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L823">property memoryShareLevel</a>
</h3>

```typescript
memoryShareLevel?: pulumi.Input<string>;
```


The allocation level for memory resources.
Can be one of `high`, `low`, `normal`, or `custom`. Default: `custom`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L830">property migrateWaitTimeout</a>
</h3>

```typescript
migrateWaitTimeout?: pulumi.Input<number>;
```


The amount of time, in minutes, to wait
for a virtual machine migration to complete before failing. Default: 10
minutes. Also see the section on virtual machine
migration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L834">property moid</a>
</h3>

```typescript
moid?: pulumi.Input<string>;
```


The machine object ID from VMWare

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L839">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


An alias for both `label` and `path`, the latter when
using `attach`. Required if not using `label`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L845">property nestedHvEnabled</a>
</h3>

```typescript
nestedHvEnabled?: pulumi.Input<boolean>;
```


Enable nested hardware virtualization on
this virtual machine, facilitating nested virtualization in the guest.
Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L851">property networkInterfaces</a>
</h3>

```typescript
networkInterfaces?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A specification for a virtual NIC on this
virtual machine. See network interface options
below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L857">property numCoresPerSocket</a>
</h3>

```typescript
numCoresPerSocket?: pulumi.Input<number>;
```


The number of cores to distribute among
the CPUs in this virtual machine. If specified, the value supplied to
`num_cpus` must be evenly divisible by this value. Default: `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L862">property numCpus</a>
</h3>

```typescript
numCpus?: pulumi.Input<number>;
```


The number of virtual processors to assign to this
virtual machine. Default: `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L868">property rebootRequired</a>
</h3>

```typescript
rebootRequired?: pulumi.Input<boolean>;
```


Value internal to Terraform used to determine if a
configuration set change requires a reboot. This value is only useful during
an update process and gets reset on refresh.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L875">property resourcePoolId</a>
</h3>

```typescript
resourcePoolId?: pulumi.Input<string>;
```


The [managed object reference
ID][docs-about-morefs] of the resource pool to put this virtual machine in.
See the section on virtual machine migration
for details on changing this value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L880">property runToolsScriptsAfterPowerOn</a>
</h3>

```typescript
runToolsScriptsAfterPowerOn?: pulumi.Input<boolean>;
```


Enable the execution of
post-power-on scripts when VMware tools is installed. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L885">property runToolsScriptsAfterResume</a>
</h3>

```typescript
runToolsScriptsAfterResume?: pulumi.Input<boolean>;
```


Enable the execution of
post-resume scripts when VMware tools is installed. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L890">property runToolsScriptsBeforeGuestReboot</a>
</h3>

```typescript
runToolsScriptsBeforeGuestReboot?: pulumi.Input<boolean>;
```


Enable the execution of
pre-reboot scripts when VMware tools is installed. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L895">property runToolsScriptsBeforeGuestShutdown</a>
</h3>

```typescript
runToolsScriptsBeforeGuestShutdown?: pulumi.Input<boolean>;
```


Enable the execution
of pre-shutdown scripts when VMware tools is installed. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L900">property runToolsScriptsBeforeGuestStandby</a>
</h3>

```typescript
runToolsScriptsBeforeGuestStandby?: pulumi.Input<boolean>;
```


Enable the execution of
pre-standby scripts when VMware tools is installed. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L905">property scsiBusSharing</a>
</h3>

```typescript
scsiBusSharing?: pulumi.Input<string>;
```


Mode for sharing the SCSI bus. The modes are
physicalSharing, virtualSharing, and noSharing. Default: `noSharing`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L912">property scsiControllerCount</a>
</h3>

```typescript
scsiControllerCount?: pulumi.Input<number>;
```


The number of SCSI controllers that
Terraform manages on this virtual machine. This directly affects the amount
of disks you can add to the virtual machine and the maximum disk unit number.
Note that lowering this value does not remove controllers. Default: `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L918">property scsiType</a>
</h3>

```typescript
scsiType?: pulumi.Input<string>;
```


The type of SCSI bus this virtual machine will have.
Can be one of lsilogic (LSI Logic Parallel), lsilogic-sas (LSI Logic SAS) or
pvscsi (VMware Paravirtual). Defualt: `pvscsi`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L925">property shutdownWaitTimeout</a>
</h3>

```typescript
shutdownWaitTimeout?: pulumi.Input<number>;
```


The amount of time, in minutes, to wait
for a graceful guest shutdown when making necessary updates to the virtual
machine. If `force_power_off` is set to true, the VM will be force powered-off
after this timeout, otherwise an error is returned. Default: 3 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L931">property swapPlacementPolicy</a>
</h3>

```typescript
swapPlacementPolicy?: pulumi.Input<string>;
```


The swap file placement policy for this
virtual machine. Can be one of `inherit`, `hostLocal`, or `vmDirectory`.
Default: `inherit`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L936">property syncTimeWithHost</a>
</h3>

```typescript
syncTimeWithHost?: pulumi.Input<boolean>;
```


Enable guest clock synchronization with
the host. Requires VMware tools to be installed. Default: `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L941">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L946">property uuid</a>
</h3>

```typescript
uuid?: pulumi.Input<string>;
```


The UUID of the virtual disk's VMDK file. This is used to track the
virtual disk on the virtual machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L954">property vapp</a>
</h3>

```typescript
vapp?: pulumi.Input<{ ... }>;
```


Optional vApp configuration. The only sub-key available
is `properties`, which is a key/value map of properties for virtual machines
imported from OVF or OVA files. See Using vApp properties to supply OVF/OVA
configuration for
more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L960">property vappTransports</a>
</h3>

```typescript
vappTransports?: pulumi.Input<pulumi.Input<string>[]>;
```


Computed value which is only valid for cloned virtual
machines. A list of vApp transport methods supported by the source virtual
machine or template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L965">property vmwareToolsStatus</a>
</h3>

```typescript
vmwareToolsStatus?: pulumi.Input<string>;
```


The state of VMware tools in the guest. This will
determine the proper course of action for some device operations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L970">property vmxPath</a>
</h3>

```typescript
vmxPath?: pulumi.Input<string>;
```


The path of the virtual machine's configuration file in the VM's
datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L977">property waitForGuestNetRoutable</a>
</h3>

```typescript
waitForGuestNetRoutable?: pulumi.Input<boolean>;
```


Controls whether or not the guest
network waiter waits for a routable address. When `false`, the waiter does
not wait for a default gateway, nor are IP addresses checked against any
discovered default gateways as part of its success criteria. Default: `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/virtualMachine.ts#L983">property waitForGuestNetTimeout</a>
</h3>

```typescript
waitForGuestNetTimeout?: pulumi.Input<number>;
```


The amount of time, in minutes, to
wait for an available IP address on this virtual machine. A value less than 1
disables the waiter. Default: 5 minutes.

<h2 class="pdoc-module-header" id="VmfsDatastoreArgs">
<a class="pdoc-member-name" href="/vmfsDatastore.ts#L244">interface VmfsDatastoreArgs</a>
</h2>

The set of arguments for constructing a VmfsDatastore resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L251">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


Map of custom attribute ids to attribute
value string to set on datastore resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L257">property datastoreClusterId</a>
</h3>

```typescript
datastoreClusterId?: pulumi.Input<string>;
```


The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L261">property disks</a>
</h3>

```typescript
disks: pulumi.Input<pulumi.Input<string>[]>;
```


The disks to use with the datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L271">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The relative path to a folder to put this datastore in.
This is a path relative to the datacenter you are deploying the datastore to.
Example: for the `dc1` datacenter, and a provided `folder` of `foo/bar`,
Terraform will place a datastore named `terraform-test` in a datastore folder
located at `/dc1/datastore/foo/bar`, with the final inventory path being
`/dc1/datastore/foo/bar/terraform-test`. Conflicts with
`datastore_cluster_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L279">property hostSystemId</a>
</h3>

```typescript
hostSystemId: pulumi.Input<string>;
```


The [managed object ID][docs-about-morefs] of
the host to set the datastore up on. Note that this is not necessarily the
only host that the datastore will be set up on - see
here for more info. Forces a
new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L284">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the datastore. Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L289">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h2 class="pdoc-module-header" id="VmfsDatastoreState">
<a class="pdoc-member-name" href="/vmfsDatastore.ts#L162">interface VmfsDatastoreState</a>
</h2>

Input properties used for looking up and filtering VmfsDatastore resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L167">property accessible</a>
</h3>

```typescript
accessible?: pulumi.Input<boolean>;
```


The connectivity status of the datastore. If this is `false`,
some other computed attributes may be out of date.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L171">property capacity</a>
</h3>

```typescript
capacity?: pulumi.Input<number>;
```


Maximum capacity of the datastore, in megabytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L178">property customAttributes</a>
</h3>

```typescript
customAttributes?: pulumi.Input<{ ... }>;
```


Map of custom attribute ids to attribute
value string to set on datastore resource. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L184">property datastoreClusterId</a>
</h3>

```typescript
datastoreClusterId?: pulumi.Input<string>;
```


The [managed object
ID][docs-about-morefs] of a datastore cluster to put this datastore in.
Conflicts with `folder`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L188">property disks</a>
</h3>

```typescript
disks?: pulumi.Input<pulumi.Input<string>[]>;
```


The disks to use with the datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L198">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The relative path to a folder to put this datastore in.
This is a path relative to the datacenter you are deploying the datastore to.
Example: for the `dc1` datacenter, and a provided `folder` of `foo/bar`,
Terraform will place a datastore named `terraform-test` in a datastore folder
located at `/dc1/datastore/foo/bar`, with the final inventory path being
`/dc1/datastore/foo/bar/terraform-test`. Conflicts with
`datastore_cluster_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L202">property freeSpace</a>
</h3>

```typescript
freeSpace?: pulumi.Input<number>;
```


Available space of this datastore, in megabytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L210">property hostSystemId</a>
</h3>

```typescript
hostSystemId?: pulumi.Input<string>;
```


The [managed object ID][docs-about-morefs] of
the host to set the datastore up on. Note that this is not necessarily the
only host that the datastore will be set up on - see
here for more info. Forces a
new resource if changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L214">property maintenanceMode</a>
</h3>

```typescript
maintenanceMode?: pulumi.Input<string>;
```


The current maintenance mode state of the datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L219">property multipleHostAccess</a>
</h3>

```typescript
multipleHostAccess?: pulumi.Input<boolean>;
```


If `true`, more than one host in the datacenter has
been configured with access to the datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L224">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the datastore. Forces a new resource if
changed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L229">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L234">property uncommittedSpace</a>
</h3>

```typescript
uncommittedSpace?: pulumi.Input<number>;
```


Total additional storage space, in megabytes,
potentially used by all virtual machines on this datastore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/vmfsDatastore.ts#L238">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```


The unique locator for the datastore.

