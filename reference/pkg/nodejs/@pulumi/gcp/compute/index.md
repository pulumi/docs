---
title: Module compute
---

<a href="../index.html">@pulumi/gcp</a> &gt; compute

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Address">class Address</a>
* <a href="#Autoscalar">class Autoscalar</a>
* <a href="#BackendBucket">class BackendBucket</a>
* <a href="#BackendService">class BackendService</a>
* <a href="#Disk">class Disk</a>
* <a href="#Firewall">class Firewall</a>
* <a href="#ForwardingRule">class ForwardingRule</a>
* <a href="#GlobalAddress">class GlobalAddress</a>
* <a href="#GlobalForwardingRule">class GlobalForwardingRule</a>
* <a href="#HealthCheck">class HealthCheck</a>
* <a href="#HttpHealthCheck">class HttpHealthCheck</a>
* <a href="#HttpsHealthCheck">class HttpsHealthCheck</a>
* <a href="#Image">class Image</a>
* <a href="#Instance">class Instance</a>
* <a href="#InstanceGroup">class InstanceGroup</a>
* <a href="#InstanceGroupManager">class InstanceGroupManager</a>
* <a href="#InstanceTemplate">class InstanceTemplate</a>
* <a href="#Network">class Network</a>
* <a href="#NetworkPeering">class NetworkPeering</a>
* <a href="#ProjectMetadata">class ProjectMetadata</a>
* <a href="#ProjectMetadataItem">class ProjectMetadataItem</a>
* <a href="#RegionAutoscaler">class RegionAutoscaler</a>
* <a href="#RegionBackendService">class RegionBackendService</a>
* <a href="#RegionInstanceGroupManager">class RegionInstanceGroupManager</a>
* <a href="#Route">class Route</a>
* <a href="#Router">class Router</a>
* <a href="#RouterInterface">class RouterInterface</a>
* <a href="#RouterPeer">class RouterPeer</a>
* <a href="#SSLCertificate">class SSLCertificate</a>
* <a href="#SharedVPCHostProject">class SharedVPCHostProject</a>
* <a href="#SharedVPCServiceProject">class SharedVPCServiceProject</a>
* <a href="#Snapshot">class Snapshot</a>
* <a href="#Subnetwork">class Subnetwork</a>
* <a href="#TargetHttpProxy">class TargetHttpProxy</a>
* <a href="#TargetHttpsProxy">class TargetHttpsProxy</a>
* <a href="#TargetPool">class TargetPool</a>
* <a href="#TargetSSLProxy">class TargetSSLProxy</a>
* <a href="#TargetTCPProxy">class TargetTCPProxy</a>
* <a href="#URLMap">class URLMap</a>
* <a href="#VPNGateway">class VPNGateway</a>
* <a href="#VPNTunnel">class VPNTunnel</a>
* <a href="#getAddress">function getAddress</a>
* <a href="#getBackendService">function getBackendService</a>
* <a href="#getDefaultServiceAccount">function getDefaultServiceAccount</a>
* <a href="#getForwardingRule">function getForwardingRule</a>
* <a href="#getGlobalAddress">function getGlobalAddress</a>
* <a href="#getImage">function getImage</a>
* <a href="#getInstanceGroup">function getInstanceGroup</a>
* <a href="#getLBIPRanges">function getLBIPRanges</a>
* <a href="#getNetwork">function getNetwork</a>
* <a href="#getRegionInstanceGroup">function getRegionInstanceGroup</a>
* <a href="#getSubnetwork">function getSubnetwork</a>
* <a href="#getVPNGateway">function getVPNGateway</a>
* <a href="#getZones">function getZones</a>
* <a href="#AddressArgs">interface AddressArgs</a>
* <a href="#AddressState">interface AddressState</a>
* <a href="#AutoscalarArgs">interface AutoscalarArgs</a>
* <a href="#AutoscalarState">interface AutoscalarState</a>
* <a href="#BackendBucketArgs">interface BackendBucketArgs</a>
* <a href="#BackendBucketState">interface BackendBucketState</a>
* <a href="#BackendServiceArgs">interface BackendServiceArgs</a>
* <a href="#BackendServiceState">interface BackendServiceState</a>
* <a href="#DiskArgs">interface DiskArgs</a>
* <a href="#DiskState">interface DiskState</a>
* <a href="#FirewallArgs">interface FirewallArgs</a>
* <a href="#FirewallState">interface FirewallState</a>
* <a href="#ForwardingRuleArgs">interface ForwardingRuleArgs</a>
* <a href="#ForwardingRuleState">interface ForwardingRuleState</a>
* <a href="#GetAddressArgs">interface GetAddressArgs</a>
* <a href="#GetAddressResult">interface GetAddressResult</a>
* <a href="#GetBackendServiceArgs">interface GetBackendServiceArgs</a>
* <a href="#GetBackendServiceResult">interface GetBackendServiceResult</a>
* <a href="#GetDefaultServiceAccountArgs">interface GetDefaultServiceAccountArgs</a>
* <a href="#GetForwardingRuleArgs">interface GetForwardingRuleArgs</a>
* <a href="#GetForwardingRuleResult">interface GetForwardingRuleResult</a>
* <a href="#GetGlobalAddressArgs">interface GetGlobalAddressArgs</a>
* <a href="#GetGlobalAddressResult">interface GetGlobalAddressResult</a>
* <a href="#GetImageArgs">interface GetImageArgs</a>
* <a href="#GetImageResult">interface GetImageResult</a>
* <a href="#GetInstanceGroupArgs">interface GetInstanceGroupArgs</a>
* <a href="#GetInstanceGroupResult">interface GetInstanceGroupResult</a>
* <a href="#GetLBIPRangesResult">interface GetLBIPRangesResult</a>
* <a href="#GetNetworkArgs">interface GetNetworkArgs</a>
* <a href="#GetNetworkResult">interface GetNetworkResult</a>
* <a href="#GetRegionInstanceGroupArgs">interface GetRegionInstanceGroupArgs</a>
* <a href="#GetRegionInstanceGroupResult">interface GetRegionInstanceGroupResult</a>
* <a href="#GetSubnetworkArgs">interface GetSubnetworkArgs</a>
* <a href="#GetSubnetworkResult">interface GetSubnetworkResult</a>
* <a href="#GetVPNGatewayArgs">interface GetVPNGatewayArgs</a>
* <a href="#GetVPNGatewayResult">interface GetVPNGatewayResult</a>
* <a href="#GetZonesArgs">interface GetZonesArgs</a>
* <a href="#GetZonesResult">interface GetZonesResult</a>
* <a href="#GlobalAddressArgs">interface GlobalAddressArgs</a>
* <a href="#GlobalAddressState">interface GlobalAddressState</a>
* <a href="#GlobalForwardingRuleArgs">interface GlobalForwardingRuleArgs</a>
* <a href="#GlobalForwardingRuleState">interface GlobalForwardingRuleState</a>
* <a href="#HealthCheckArgs">interface HealthCheckArgs</a>
* <a href="#HealthCheckState">interface HealthCheckState</a>
* <a href="#HttpHealthCheckArgs">interface HttpHealthCheckArgs</a>
* <a href="#HttpHealthCheckState">interface HttpHealthCheckState</a>
* <a href="#HttpsHealthCheckArgs">interface HttpsHealthCheckArgs</a>
* <a href="#HttpsHealthCheckState">interface HttpsHealthCheckState</a>
* <a href="#ImageArgs">interface ImageArgs</a>
* <a href="#ImageState">interface ImageState</a>
* <a href="#InstanceArgs">interface InstanceArgs</a>
* <a href="#InstanceGroupArgs">interface InstanceGroupArgs</a>
* <a href="#InstanceGroupManagerArgs">interface InstanceGroupManagerArgs</a>
* <a href="#InstanceGroupManagerState">interface InstanceGroupManagerState</a>
* <a href="#InstanceGroupState">interface InstanceGroupState</a>
* <a href="#InstanceState">interface InstanceState</a>
* <a href="#InstanceTemplateArgs">interface InstanceTemplateArgs</a>
* <a href="#InstanceTemplateState">interface InstanceTemplateState</a>
* <a href="#NetworkArgs">interface NetworkArgs</a>
* <a href="#NetworkPeeringArgs">interface NetworkPeeringArgs</a>
* <a href="#NetworkPeeringState">interface NetworkPeeringState</a>
* <a href="#NetworkState">interface NetworkState</a>
* <a href="#ProjectMetadataArgs">interface ProjectMetadataArgs</a>
* <a href="#ProjectMetadataItemArgs">interface ProjectMetadataItemArgs</a>
* <a href="#ProjectMetadataItemState">interface ProjectMetadataItemState</a>
* <a href="#ProjectMetadataState">interface ProjectMetadataState</a>
* <a href="#RegionAutoscalerArgs">interface RegionAutoscalerArgs</a>
* <a href="#RegionAutoscalerState">interface RegionAutoscalerState</a>
* <a href="#RegionBackendServiceArgs">interface RegionBackendServiceArgs</a>
* <a href="#RegionBackendServiceState">interface RegionBackendServiceState</a>
* <a href="#RegionInstanceGroupManagerArgs">interface RegionInstanceGroupManagerArgs</a>
* <a href="#RegionInstanceGroupManagerState">interface RegionInstanceGroupManagerState</a>
* <a href="#RouteArgs">interface RouteArgs</a>
* <a href="#RouteState">interface RouteState</a>
* <a href="#RouterArgs">interface RouterArgs</a>
* <a href="#RouterInterfaceArgs">interface RouterInterfaceArgs</a>
* <a href="#RouterInterfaceState">interface RouterInterfaceState</a>
* <a href="#RouterPeerArgs">interface RouterPeerArgs</a>
* <a href="#RouterPeerState">interface RouterPeerState</a>
* <a href="#RouterState">interface RouterState</a>
* <a href="#SSLCertificateArgs">interface SSLCertificateArgs</a>
* <a href="#SSLCertificateState">interface SSLCertificateState</a>
* <a href="#SharedVPCHostProjectArgs">interface SharedVPCHostProjectArgs</a>
* <a href="#SharedVPCHostProjectState">interface SharedVPCHostProjectState</a>
* <a href="#SharedVPCServiceProjectArgs">interface SharedVPCServiceProjectArgs</a>
* <a href="#SharedVPCServiceProjectState">interface SharedVPCServiceProjectState</a>
* <a href="#SnapshotArgs">interface SnapshotArgs</a>
* <a href="#SnapshotState">interface SnapshotState</a>
* <a href="#SubnetworkArgs">interface SubnetworkArgs</a>
* <a href="#SubnetworkState">interface SubnetworkState</a>
* <a href="#TargetHttpProxyArgs">interface TargetHttpProxyArgs</a>
* <a href="#TargetHttpProxyState">interface TargetHttpProxyState</a>
* <a href="#TargetHttpsProxyArgs">interface TargetHttpsProxyArgs</a>
* <a href="#TargetHttpsProxyState">interface TargetHttpsProxyState</a>
* <a href="#TargetPoolArgs">interface TargetPoolArgs</a>
* <a href="#TargetPoolState">interface TargetPoolState</a>
* <a href="#TargetSSLProxyArgs">interface TargetSSLProxyArgs</a>
* <a href="#TargetSSLProxyState">interface TargetSSLProxyState</a>
* <a href="#TargetTCPProxyArgs">interface TargetTCPProxyArgs</a>
* <a href="#TargetTCPProxyState">interface TargetTCPProxyState</a>
* <a href="#URLMapArgs">interface URLMapArgs</a>
* <a href="#URLMapState">interface URLMapState</a>
* <a href="#VPNGatewayArgs">interface VPNGatewayArgs</a>
* <a href="#VPNGatewayState">interface VPNGatewayState</a>
* <a href="#VPNTunnelArgs">interface VPNTunnelArgs</a>
* <a href="#VPNTunnelState">interface VPNTunnelState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts">compute/address.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts">compute/autoscalar.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts">compute/backendBucket.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts">compute/backendService.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts">compute/disk.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts">compute/firewall.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts">compute/forwardingRule.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getAddress.ts">compute/getAddress.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts">compute/getBackendService.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getDefaultServiceAccount.ts">compute/getDefaultServiceAccount.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts">compute/getForwardingRule.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getGlobalAddress.ts">compute/getGlobalAddress.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts">compute/getImage.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getInstanceGroup.ts">compute/getInstanceGroup.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getLBIPRanges.ts">compute/getLBIPRanges.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getNetwork.ts">compute/getNetwork.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getRegionInstanceGroup.ts">compute/getRegionInstanceGroup.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getSubnetwork.ts">compute/getSubnetwork.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getVPNGateway.ts">compute/getVPNGateway.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getZones.ts">compute/getZones.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts">compute/globalAddress.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts">compute/globalForwardingRule.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts">compute/healthCheck.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts">compute/httpHealthCheck.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts">compute/httpsHealthCheck.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts">compute/image.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts">compute/instance.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts">compute/instanceGroup.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts">compute/instanceGroupManager.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts">compute/instanceTemplate.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts">compute/network.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts">compute/networkPeering.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadata.ts">compute/projectMetadata.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadataItem.ts">compute/projectMetadataItem.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts">compute/regionAutoscaler.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts">compute/regionBackendService.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts">compute/regionInstanceGroupManager.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts">compute/route.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts">compute/router.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts">compute/routerInterface.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts">compute/routerPeer.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts">compute/sSLCertificate.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCHostProject.ts">compute/sharedVPCHostProject.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCServiceProject.ts">compute/sharedVPCServiceProject.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts">compute/snapshot.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts">compute/subnetwork.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts">compute/targetHttpProxy.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts">compute/targetHttpsProxy.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts">compute/targetPool.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts">compute/targetSSLProxy.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts">compute/targetTCPProxy.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts">compute/uRLMap.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts">compute/vPNGateway.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts">compute/vPNTunnel.ts</a> 


<h2 class="pdoc-module-header" id="Address">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L15">class Address</a>
</h2>

Creates a static IP address resource for Google Compute Engine. For more information see
the official documentation for
[external](https://cloud.google.com/compute/docs/instances-and-network) and
[internal](https://cloud.google.com/compute/docs/ip-addresses/reserve-static-internal-ip-address)
static IP reservations, as well as the
[API](https://cloud.google.com/compute/docs/reference/beta/addresses/insert).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L64">constructor</a>
</h3>

```typescript
new Address(name: string, args?: AddressArgs, opts?: pulumi.ResourceOptions)
```


Create a Address resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AddressState): Address
```


Get an existing Address resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L33">property address</a>
</h3>

```typescript
public address: pulumi.Output<string>;
```


The IP address to reserve. An address may only be
specified for INTERNAL address types. The IP address must be inside the
specified subnetwork, if any.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L39">property addressType</a>
</h3>

```typescript
public addressType: pulumi.Output<string | undefined>;
```


The Address Type that should be configured.
Specify INTERNAL to reserve an internal static IP address EXTERNAL to
specify an external static IP address. Defaults to EXTERNAL if omitted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L49">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L54">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The Region in which the created address should reside.
If it is not provided, the provider region is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L58">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L64">property subnetwork</a>
</h3>

```typescript
public subnetwork: pulumi.Output<string>;
```


The self link URI of the subnetwork in which to
create the address. A subnetwork may only be specified for INTERNAL
address types.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Autoscalar">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L17">class Autoscalar</a>
</h2>

A Compute Engine Autoscaler automatically adds or removes virtual machines from
a managed instance group based on increases or decreases in load. This allows
your applications to gracefully handle increases in traffic and reduces cost
when the need for resources is lower. You just define the autoscaling policy and
the autoscaler performs automatic scaling based on the measured load. For more
information, see [the official
documentation](https://cloud.google.com/compute/docs/autoscaler/) and
[API](https://cloud.google.com/compute/docs/reference/latest/autoscalers)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L64">constructor</a>
</h3>

```typescript
new Autoscalar(name: string, args: AutoscalarArgs, opts?: pulumi.ResourceOptions)
```


Create a Autoscalar resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L26">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AutoscalarState): Autoscalar
```


Get an existing Autoscalar resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L34">property autoscalingPolicy</a>
</h3>

```typescript
public autoscalingPolicy: pulumi.Output<{ ... }>;
```


The parameters of the autoscaling
algorithm. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L39">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


An optional textual description of the instance
group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Google Cloud Monitoring metric to follow, e.g.
`compute.googleapis.com/instance/network/received_bytes_count`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L49">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L53">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URL of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L60">property target</a>
</h3>

```typescript
public target: pulumi.Output<string>;
```


The floating point threshold where load balancing utilization
should be. E.g. if the load balancer's `maxRatePerInstance` is 10 requests
per second (RPS) then setting this to 0.5 would cause the group to be scaled
such that each instance receives 5 RPS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L64">property zone</a>
</h3>

```typescript
public zone: pulumi.Output<string>;
```


The zone of the target.

<h2 class="pdoc-module-header" id="BackendBucket">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L6">class BackendBucket</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L32">constructor</a>
</h3>

```typescript
new BackendBucket(name: string, args: BackendBucketArgs, opts?: pulumi.ResourceOptions)
```


Create a BackendBucket resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L15">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BackendBucketState): BackendBucket
```


Get an existing BackendBucket resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L19">property bucketName</a>
</h3>

```typescript
public bucketName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L20">property creationTimestamp</a>
</h3>

```typescript
public creationTimestamp: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L21">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L22">property enableCdn</a>
</h3>

```typescript
public enableCdn: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L23">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L28">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L32">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="BackendService">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L13">class BackendService</a>
</h2>

A Backend Service defines a group of virtual machines that will serve traffic for load balancing. For more information
see [the official documentation](https://cloud.google.com/compute/docs/load-balancing/http/backend-service)
and the [API](https://cloud.google.com/compute/docs/reference/latest/backendServices).

For internal load balancing, use a [google_compute_region_backend_service](/docs/providers/google/r/compute_region_backend_service.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L99">constructor</a>
</h3>

```typescript
new BackendService(name: string, args: BackendServiceArgs, opts?: pulumi.ResourceOptions)
```


Create a BackendService resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BackendServiceState): BackendService
```


Get an existing BackendService resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L29">property backends</a>
</h3>

```typescript
public backends: pulumi.Output<{ ... }[] | undefined>;
```


The list of backends that serve this BackendService. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L33">property cdnPolicy</a>
</h3>

```typescript
public cdnPolicy: pulumi.Output<{ ... }>;
```


Cloud CDN configuration for this BackendService. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L38">property connectionDrainingTimeoutSec</a>
</h3>

```typescript
public connectionDrainingTimeoutSec: pulumi.Output<number | undefined>;
```


Time for which instance will be drained (not accept new connections,
but still work to finish started ones). Defaults to `300`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L42">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Textual description for the backend.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L46">property enableCdn</a>
</h3>

```typescript
public enableCdn: pulumi.Output<boolean | undefined>;
```


Whether or not to enable the Cloud CDN on the backend service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L50">property fingerprint</a>
</h3>

```typescript
public fingerprint: pulumi.Output<string>;
```


The fingerprint of the backend service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L56">property healthChecks</a>
</h3>

```typescript
public healthChecks: pulumi.Output<string>;
```


Specifies a list of HTTP/HTTPS health checks
for checking the health of the backend service. Currently at most one health
check can be specified, and a health check is required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L60">property iap</a>
</h3>

```typescript
public iap: pulumi.Output<{ ... } | undefined>;
```


Specification for the Identity-Aware proxy. Disabled if not specified. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L64">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the backend service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L69">property portName</a>
</h3>

```typescript
public portName: pulumi.Output<string>;
```


The name of a service that has been added to an
instance group in this backend. See [related docs](https://cloud.google.com/compute/docs/instance-groups/#specifying_service_endpoints) for details. Defaults to http.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L74">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L79">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The protocol for incoming requests. Defaults to
`HTTP`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L84">property securityPolicy</a>
</h3>

```typescript
public securityPolicy: pulumi.Output<string | undefined>;
```


) Name or URI of a
[security policy](https://cloud.google.com/armor/docs/security-policy-concepts) to add to the backend service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L88">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L94">property sessionAffinity</a>
</h3>

```typescript
public sessionAffinity: pulumi.Output<string>;
```


How to distribute load. Options are `NONE` (no
affinity), `CLIENT_IP` (hash of the source/dest addresses / ports), and
`GENERATED_COOKIE` (distribute load using a generated session cookie).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L99">property timeoutSec</a>
</h3>

```typescript
public timeoutSec: pulumi.Output<number>;
```


The number of secs to wait for a backend to respond
to a request before considering the request failed. Defaults to `30`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Disk">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L15">class Disk</a>
</h2>

Creates a new persistent disk within GCE, based on another disk. For more information see
[the official documentation](https://cloud.google.com/compute/docs/disks/add-persistent-disk)
and
[API](https://cloud.google.com/compute/docs/reference/latest/disks).

~> **Note:** All arguments including the disk encryption key will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L96">constructor</a>
</h3>

```typescript
new Disk(name: string, args?: DiskArgs, opts?: pulumi.ResourceOptions)
```


Create a Disk resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DiskState): Disk
```


Get an existing Disk resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L34">property diskEncryptionKeyRaw</a>
</h3>

```typescript
public diskEncryptionKeyRaw: pulumi.Output<string | undefined>;
```


A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L41">property diskEncryptionKeySha256</a>
</h3>

```typescript
public diskEncryptionKeySha256: pulumi.Output<string>;
```


The [RFC 4648 base64]
(https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the
[customer-supplied encryption key](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
that protects this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L53">property image</a>
</h3>

```typescript
public image: pulumi.Output<string | undefined>;
```


The image from which to initialize this disk. This can be
one of: the image's `self_link`, `projects/{project}/global/images/{image}`,
`projects/{project}/global/images/family/{family}`, `global/images/{image}`,
`global/images/family/{family}`, `family/{family}`, `{project}/{family}`,
`{project}/{image}`, `{family}`, or `{image}`. If referred by family, the
images names must include the family name. If they don't, use the
[google_compute_image data source](/docs/providers/google/d/datasource_compute_image.html).
For instance, the image `centos-6-v20180104` includes its family name `centos-6`.
These images can be referred by family name here.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L57">property labelFingerprint</a>
</h3>

```typescript
public labelFingerprint: pulumi.Output<string>;
```


The fingerprint of the assigned labels.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L61">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


A set of key/value label pairs to assign to the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L66">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L71">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L75">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L80">property size</a>
</h3>

```typescript
public size: pulumi.Output<number>;
```


The size of the image in gigabytes. If not specified, it
will inherit the size of its base image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L84">property snapshot</a>
</h3>

```typescript
public snapshot: pulumi.Output<string | undefined>;
```


Name of snapshot from which to initialize this disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L88">property type</a>
</h3>

```typescript
public type: pulumi.Output<string | undefined>;
```


The GCE disk type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L92">property users</a>
</h3>

```typescript
public users: pulumi.Output<string[]>;
```


The Users of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L96">property zone</a>
</h3>

```typescript
public zone: pulumi.Output<string>;
```


The zone where this disk will be available.

<h2 class="pdoc-module-header" id="Firewall">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L12">class Firewall</a>
</h2>

Manages a firewall resource within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/vpc/firewalls)
and
[API](https://cloud.google.com/compute/docs/reference/latest/firewalls).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L105">constructor</a>
</h3>

```typescript
new Firewall(name: string, args: FirewallArgs, opts?: pulumi.ResourceOptions)
```


Create a Firewall resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FirewallState): Firewall
```


Get an existing Firewall resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L29">property allows</a>
</h3>

```typescript
public allows: pulumi.Output<{ ... }[] | undefined>;
```


Can be specified multiple times for each allow
rule. Each allow block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L35">property denies</a>
</h3>

```typescript
public denies: pulumi.Output<{ ... }[] | undefined>;
```


Can be specified multiple times for each deny
rule. Each deny block supports fields documented below. Can be specified
instead of allow.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L39">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Textual description field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L44">property destinationRanges</a>
</h3>

```typescript
public destinationRanges: pulumi.Output<string[]>;
```


A list of destination CIDR ranges that this
firewall applies to. Can't be used for `INGRESS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L49">property direction</a>
</h3>

```typescript
public direction: pulumi.Output<string>;
```


Direction of traffic to which this firewall applies;
One of `INGRESS` or `EGRESS`. Defaults to `INGRESS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L54">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L58">property network</a>
</h3>

```typescript
public network: pulumi.Output<string>;
```


The name or self_link of the network to attach this firewall to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L64">property priority</a>
</h3>

```typescript
public priority: pulumi.Output<number | undefined>;
```


The priority for this firewall. Ranges from 0-65535, inclusive. Defaults to 1000. Firewall
resources with lower priority values have higher precedence (e.g. a firewall resource with a priority value of 0
takes effect over all other firewall rules with a non-zero priority).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L69">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L73">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L78">property sourceRanges</a>
</h3>

```typescript
public sourceRanges: pulumi.Output<string[]>;
```


A list of source CIDR ranges that this
firewall applies to. Can't be used for `EGRESS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L89">property sourceServiceAccounts</a>
</h3>

```typescript
public sourceServiceAccounts: pulumi.Output<string | undefined>;
```


A list of service accounts such that
the firewall will apply only to traffic originating from an instance with a service account in this list.  Note that as of May 2018,
this list can contain only one item, due to a change in the way that these firewall rules are handled.  Source service accounts
cannot be used to control traffic to an instance's external IP address because service accounts are associated with an instance, not
an IP address. `source_ranges` can be set at the same time as `source_service_accounts`. If both are set, the firewall will apply to
traffic that has source IP address within `source_ranges` OR the source IP belongs to an instance with service account listed in
`source_service_accounts`. The connection does not need to match both properties for the firewall to apply. `source_service_accounts`
cannot be used at the same time as `source_tags` or `target_tags`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L93">property sourceTags</a>
</h3>

```typescript
public sourceTags: pulumi.Output<string[] | undefined>;
```


A list of source tags for this firewall. Can't be used for `EGRESS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L101">property targetServiceAccounts</a>
</h3>

```typescript
public targetServiceAccounts: pulumi.Output<string | undefined>;
```


A list of service accounts indicating
sets of instances located in the network that may make network connections as specified in `allow`. `target_service_accounts` cannot
be used at the same time as `source_tags` or `target_tags`. If neither `target_service_accounts` nor `target_tags` are specified, the
firewall rule applies to all instances on the specified network.  Note that as of May 2018, this list can contain only one item, due
to a change in the way that these firewall rules are handled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L105">property targetTags</a>
</h3>

```typescript
public targetTags: pulumi.Output<string[] | undefined>;
```


A list of target tags for this firewall.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ForwardingRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L12">class ForwardingRule</a>
</h2>

Manages a Forwarding Rule within GCE. This binds an ip and port range to a target pool. For more
information see [the official
documentation](https://cloud.google.com/compute/docs/load-balancing/network/forwarding-rules) and
[API](https://cloud.google.com/compute/docs/reference/latest/forwardingRules).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L102">constructor</a>
</h3>

```typescript
new ForwardingRule(name: string, args?: ForwardingRuleArgs, opts?: pulumi.ResourceOptions)
```


Create a ForwardingRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ForwardingRuleState): ForwardingRule
```


Get an existing ForwardingRule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L29">property backendService</a>
</h3>

```typescript
public backendService: pulumi.Output<string | undefined>;
```


BackendService resource to receive the
matched traffic. Only used for internal load balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L33">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Textual description field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L38">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string>;
```


The static IP. (if not set, an ephemeral IP is
used).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L44">property ipProtocol</a>
</h3>

```typescript
public ipProtocol: pulumi.Output<string>;
```


The IP protocol to route, one of "TCP" "UDP" "AH"
"ESP" or "SCTP" for external load balancing, "TCP" or "UDP" for internal
(default "TCP").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L49">property loadBalancingScheme</a>
</h3>

```typescript
public loadBalancingScheme: pulumi.Output<string | undefined>;
```


Type of load balancing to use. Can be
set to "INTERNAL" or "EXTERNAL" (default "EXTERNAL").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L54">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L60">property network</a>
</h3>

```typescript
public network: pulumi.Output<string>;
```


Network name or self_link that the load balanced IP
should belong to. Only used for internal load balancing. If it is not
provided, the default network is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L71">property portRange</a>
</h3>

```typescript
public portRange: pulumi.Output<string | undefined>;
```


A range e.g. "1024-2048" or a single port "1024"
(defaults to all ports!). Only used for external load balancing.
Some types of forwarding targets have constraints on the acceptable ports:
* Target HTTP proxy: 80, 8080
* Target HTTPS proxy: 443
* Target TCP proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
* Target SSL proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
* Target VPN gateway: 500, 4500

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L77">property ports</a>
</h3>

```typescript
public ports: pulumi.Output<string[] | undefined>;
```


A list of ports (maximum of 5) to use for internal load
balancing. Packets addressed to these ports will be forwarded to the backends
configured with this forwarding rule. Required for internal load balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L82">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L87">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The Region in which the created address should reside.
If it is not provided, the provider region is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L91">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L97">property subnetwork</a>
</h3>

```typescript
public subnetwork: pulumi.Output<string>;
```


Subnetwork that the load balanced IP should belong
to. Only used for internal load balancing. Must be specified if the network
is in custom subnet mode.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L102">property target</a>
</h3>

```typescript
public target: pulumi.Output<string | undefined>;
```


URL of target pool. Required for external load
balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="GlobalAddress">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L6">class GlobalAddress</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L32">constructor</a>
</h3>

```typescript
new GlobalAddress(name: string, args?: GlobalAddressArgs, opts?: pulumi.ResourceOptions)
```


Create a GlobalAddress resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L15">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GlobalAddressState): GlobalAddress
```


Get an existing GlobalAddress resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L19">property address</a>
</h3>

```typescript
public address: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L20">property creationTimestamp</a>
</h3>

```typescript
public creationTimestamp: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L21">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L22">property ipVersion</a>
</h3>

```typescript
public ipVersion: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L23">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L28">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L32">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="GlobalForwardingRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L12">class GlobalForwardingRule</a>
</h2>

Manages a Global Forwarding Rule within GCE. This binds an ip and port to a target HTTP(s) proxy. For more
information see [the official
documentation](https://cloud.google.com/compute/docs/load-balancing/http/global-forwarding-rules) and
[API](https://cloud.google.com/compute/docs/reference/latest/globalForwardingRules).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L83">constructor</a>
</h3>

```typescript
new GlobalForwardingRule(name: string, args: GlobalForwardingRuleArgs, opts?: pulumi.ResourceOptions)
```


Create a GlobalForwardingRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GlobalForwardingRuleState): GlobalForwardingRule
```


Get an existing GlobalForwardingRule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L28">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Textual description field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L35">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string>;
```


The static IP. (if not set, an ephemeral IP is
used). This should be the literal IP address to be used, not the `self_link`
to a `google_compute_global_address` resource. (If using a `google_compute_global_address`
resource, use the `address` property instead of the `self_link` property.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L40">property ipProtocol</a>
</h3>

```typescript
public ipProtocol: pulumi.Output<string>;
```


The IP protocol to route, one of "TCP" "UDP" "AH"
"ESP" or "SCTP". (default "TCP").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L45">property ipVersion</a>
</h3>

```typescript
public ipVersion: pulumi.Output<string | undefined>;
```


The IP Version that will be used by this resource's address. One of `"IPV4"` or `"IPV6"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L49">property labelFingerprint</a>
</h3>

```typescript
public labelFingerprint: pulumi.Output<string>;
```


([Beta](/docs/providers/google/index.html#beta-features)) The current label fingerprint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L54">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


)
A set of key/value label pairs to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L59">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L70">property portRange</a>
</h3>

```typescript
public portRange: pulumi.Output<string | undefined>;
```


A range e.g. "1024-2048" or a single port "1024"
(defaults to all ports!).
Some types of forwarding targets have constraints on the acceptable ports:
* Target HTTP proxy: 80, 8080
* Target HTTPS proxy: 443
* Target TCP proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
* Target SSL proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
* Target VPN gateway: 500, 4500

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L75">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L79">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L83">property target</a>
</h3>

```typescript
public target: pulumi.Output<string>;
```


URL of target HTTP or HTTPS proxy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="HealthCheck">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L14">class HealthCheck</a>
</h2>

Manages a health check within GCE. This is used to monitor instances
behind load balancers. Timeouts or HTTP errors cause the instance to be
removed from the pool. For more information, see [the official
documentation](https://cloud.google.com/compute/docs/load-balancing/health-checks)
and
[API](https://cloud.google.com/compute/docs/reference/latest/healthChecks).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L82">constructor</a>
</h3>

```typescript
new HealthCheck(name: string, args?: HealthCheckArgs, opts?: pulumi.ResourceOptions)
```


Create a HealthCheck resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HealthCheckState): HealthCheck
```


Get an existing HealthCheck resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L31">property checkIntervalSec</a>
</h3>

```typescript
public checkIntervalSec: pulumi.Output<number | undefined>;
```


The number of seconds between each poll of
the instance instance (default 5).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L35">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Textual description field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L39">property healthyThreshold</a>
</h3>

```typescript
public healthyThreshold: pulumi.Output<number | undefined>;
```


Consecutive successes required (default 2).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L44">property httpHealthCheck</a>
</h3>

```typescript
public httpHealthCheck: pulumi.Output<{ ... } | undefined>;
```


An HTTP Health Check. Only one kind of Health Check can be added.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L49">property httpsHealthCheck</a>
</h3>

```typescript
public httpsHealthCheck: pulumi.Output<{ ... } | undefined>;
```


An HTTPS Health Check. Only one kind of Health Check can be added.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L54">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L59">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L63">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L68">property sslHealthCheck</a>
</h3>

```typescript
public sslHealthCheck: pulumi.Output<{ ... } | undefined>;
```


An SSL Health Check. Only one kind of Health Check can be added.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L73">property tcpHealthCheck</a>
</h3>

```typescript
public tcpHealthCheck: pulumi.Output<{ ... } | undefined>;
```


A TCP Health Check. Only one kind of Health Check can be added.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L78">property timeoutSec</a>
</h3>

```typescript
public timeoutSec: pulumi.Output<number | undefined>;
```


The number of seconds to wait before declaring
failure (default 5).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L82">property unhealthyThreshold</a>
</h3>

```typescript
public unhealthyThreshold: pulumi.Output<number | undefined>;
```


Consecutive failures required (default 2).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="HttpHealthCheck">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L6">class HttpHealthCheck</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L37">constructor</a>
</h3>

```typescript
new HttpHealthCheck(name: string, args?: HttpHealthCheckArgs, opts?: pulumi.ResourceOptions)
```


Create a HttpHealthCheck resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L15">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HttpHealthCheckState): HttpHealthCheck
```


Get an existing HttpHealthCheck resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L19">property checkIntervalSec</a>
</h3>

```typescript
public checkIntervalSec: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L20">property creationTimestamp</a>
</h3>

```typescript
public creationTimestamp: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L21">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L22">property healthyThreshold</a>
</h3>

```typescript
public healthyThreshold: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L23">property host</a>
</h3>

```typescript
public host: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L24">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L25">property port</a>
</h3>

```typescript
public port: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L30">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L31">property requestPath</a>
</h3>

```typescript
public requestPath: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L35">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L36">property timeoutSec</a>
</h3>

```typescript
public timeoutSec: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L37">property unhealthyThreshold</a>
</h3>

```typescript
public unhealthyThreshold: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="HttpsHealthCheck">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L6">class HttpsHealthCheck</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L37">constructor</a>
</h3>

```typescript
new HttpsHealthCheck(name: string, args?: HttpsHealthCheckArgs, opts?: pulumi.ResourceOptions)
```


Create a HttpsHealthCheck resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L15">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HttpsHealthCheckState): HttpsHealthCheck
```


Get an existing HttpsHealthCheck resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L19">property checkIntervalSec</a>
</h3>

```typescript
public checkIntervalSec: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L20">property creationTimestamp</a>
</h3>

```typescript
public creationTimestamp: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L21">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L22">property healthyThreshold</a>
</h3>

```typescript
public healthyThreshold: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L23">property host</a>
</h3>

```typescript
public host: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L24">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L25">property port</a>
</h3>

```typescript
public port: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L30">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L31">property requestPath</a>
</h3>

```typescript
public requestPath: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L35">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L36">property timeoutSec</a>
</h3>

```typescript
public timeoutSec: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L37">property unhealthyThreshold</a>
</h3>

```typescript
public unhealthyThreshold: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Image">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L12">class Image</a>
</h2>

Creates a bootable VM image resource for Google Compute Engine from an existing
tarball. For more information see [the official documentation](https://cloud.google.com/compute/docs/images) and
[API](https://cloud.google.com/compute/docs/reference/latest/images).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L69">constructor</a>
</h3>

```typescript
new Image(name: string, args?: ImageArgs, opts?: pulumi.ResourceOptions)
```


Create a Image resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ImageState): Image
```


Get an existing Image resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L28">property createTimeout</a>
</h3>

```typescript
public createTimeout: pulumi.Output<number | undefined>;
```


Configurable timeout in minutes for creating images. Default is 4 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L32">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the image to be created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L36">property family</a>
</h3>

```typescript
public family: pulumi.Output<string | undefined>;
```


The name of the image family to which this image belongs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L40">property labelFingerprint</a>
</h3>

```typescript
public labelFingerprint: pulumi.Output<string>;
```


The fingerprint of the assigned labels.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L44">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


A set of key/value label pairs to assign to the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L49">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L54">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L60">property rawDisk</a>
</h3>

```typescript
public rawDisk: pulumi.Output<{ ... } | undefined>;
```


The raw disk that will be used as the source of the image.
Changing this forces a new resource to be created. Structure is documented
below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L64">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L69">property sourceDisk</a>
</h3>

```typescript
public sourceDisk: pulumi.Output<string | undefined>;
```


The URL of a disk that will be used as the source of the
image. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Instance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L13">class Instance</a>
</h2>

Manages a VM instance resource within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/instances)
and
[API](https://cloud.google.com/compute/docs/reference/latest/instances).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L156">constructor</a>
</h3>

```typescript
new Instance(name: string, args: InstanceArgs, opts?: pulumi.ResourceOptions)
```


Create a Instance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceState): Instance
```


Get an existing Instance resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L30">property allowStoppingForUpdate</a>
</h3>

```typescript
public allowStoppingForUpdate: pulumi.Output<boolean | undefined>;
```


If true, allows Terraform to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L34">property attachedDisks</a>
</h3>

```typescript
public attachedDisks: pulumi.Output<{ ... }[] | undefined>;
```


List of disks to attach to the instance. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L39">property bootDisk</a>
</h3>

```typescript
public bootDisk: pulumi.Output<{ ... }>;
```


The boot disk for the instance.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L45">property canIpForward</a>
</h3>

```typescript
public canIpForward: pulumi.Output<boolean | undefined>;
```


Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L49">property cpuPlatform</a>
</h3>

```typescript
public cpuPlatform: pulumi.Output<string>;
```


The CPU platform used by this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L54">property createTimeout</a>
</h3>

```typescript
public createTimeout: pulumi.Output<number | undefined>;
```


Configurable timeout in minutes for creating instances. Default is 4 minutes.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L59">property deletionProtection</a>
</h3>

```typescript
public deletionProtection: pulumi.Output<boolean | undefined>;
```


Enable deletion protection on this instance. Defaults to false.
**Note:** you must disable deletion protection before removing the resource (e.g., via `terraform destroy`), or the instance cannot be deleted and the Terraform run will not complete successfully.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L63">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A brief description of this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L67">property guestAccelerators</a>
</h3>

```typescript
public guestAccelerators: pulumi.Output<{ ... }[]>;
```


List of the type and count of accelerator cards attached to the instance. Structure documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L71">property instanceId</a>
</h3>

```typescript
public instanceId: pulumi.Output<string>;
```


The server-assigned unique identifier of this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L75">property labelFingerprint</a>
</h3>

```typescript
public labelFingerprint: pulumi.Output<string>;
```


The unique fingerprint of the labels.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L79">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


A set of key/value label pairs to assign to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L86">property machineType</a>
</h3>

```typescript
public machineType: pulumi.Output<string>;
```


The machine type to create. To create a custom
machine type, value should be set as specified
[here](https://cloud.google.com/compute/docs/reference/latest/instances#machineType).
**Note**: [`allow_stopping_for_update`](#allow_stopping_for_update) must be set to true in order to update this field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L91">property metadata</a>
</h3>

```typescript
public metadata: pulumi.Output<{ ... } | undefined>;
```


Metadata key/value pairs to make available from
within the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L95">property metadataFingerprint</a>
</h3>

```typescript
public metadataFingerprint: pulumi.Output<string>;
```


The unique fingerprint of the metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L103">property metadataStartupScript</a>
</h3>

```typescript
public metadataStartupScript: pulumi.Output<string | undefined>;
```


An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L109">property minCpuPlatform</a>
</h3>

```typescript
public minCpuPlatform: pulumi.Output<string | undefined>;
```


Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
**Note**: [`allow_stopping_for_update`](#allow_stopping_for_update) must be set to true in order to update this field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L114">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L119">property networkInterfaces</a>
</h3>

```typescript
public networkInterfaces: pulumi.Output<{ ... }[]>;
```


Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L124">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L129">property scheduling</a>
</h3>

```typescript
public scheduling: pulumi.Output<{ ... }>;
```


The scheduling strategy to use. More details about
this configuration option are detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L134">property scratchDisks</a>
</h3>

```typescript
public scratchDisks: pulumi.Output<{ ... }[] | undefined>;
```


Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L138">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L144">property serviceAccount</a>
</h3>

```typescript
public serviceAccount: pulumi.Output<{ ... } | undefined>;
```


Service account to attach to the instance.
Structure is documented below.
**Note**: [`allow_stopping_for_update`](#allow_stopping_for_update) must be set to true in order to update this field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L148">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<string[] | undefined>;
```


A list of tags to attach to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L152">property tagsFingerprint</a>
</h3>

```typescript
public tagsFingerprint: pulumi.Output<string>;
```


The unique fingerprint of the tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L156">property zone</a>
</h3>

```typescript
public zone: pulumi.Output<string>;
```


The zone that the machine should be created in.

<h2 class="pdoc-module-header" id="InstanceGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L11">class InstanceGroup</a>
</h2>

Creates a group of dissimilar Compute Engine virtual machine instances.
For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/#unmanaged_instance_groups)
and [API](https://cloud.google.com/compute/docs/reference/latest/instanceGroups)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L67">constructor</a>
</h3>

```typescript
new InstanceGroup(name: string, args?: InstanceGroupArgs, opts?: pulumi.ResourceOptions)
```


Create a InstanceGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceGroupState): InstanceGroup
```


Get an existing InstanceGroup resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L28">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


An optional textual description of the instance
group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L34">property instances</a>
</h3>

```typescript
public instances: pulumi.Output<string[]>;
```


List of instances in the group. They should be given
as self_link URLs. When adding instances they must all be in the same
network and zone as the instance group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name which the port will be mapped to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L43">property namedPorts</a>
</h3>

```typescript
public namedPorts: pulumi.Output<{ ... }[] | undefined>;
```


The named port configuration. See the section below
for details on configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L50">property network</a>
</h3>

```typescript
public network: pulumi.Output<string>;
```


The URL of the network the instance group is in. If
this is different from the network where the instances are in, the creation
fails. Defaults to the network where the instances are in (if neither
`network` nor `instances` is specified, this field will be blank).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L55">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L59">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L63">property size</a>
</h3>

```typescript
public size: pulumi.Output<number>;
```


The number of instances in the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L67">property zone</a>
</h3>

```typescript
public zone: pulumi.Output<string>;
```


The zone that this instance group should be created in.

<h2 class="pdoc-module-header" id="InstanceGroupManager">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L14">class InstanceGroupManager</a>
</h2>

The Google Compute Engine Instance Group Manager API creates and manages pools
of homogeneous Compute Engine virtual machine instances from a common instance
template. For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/manager)
and [API](https://cloud.google.com/compute/docs/reference/latest/instanceGroupManagers)

~> **Note:** Use [google_compute_region_instance_group_manager](/docs/providers/google/r/compute_region_instance_group_manager.html) to create a regional (multi-zone) instance group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L112">constructor</a>
</h3>

```typescript
new InstanceGroupManager(name: string, args: InstanceGroupManagerArgs, opts?: pulumi.ResourceOptions)
```


Create a InstanceGroupManager resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceGroupManagerState): InstanceGroupManager
```


Get an existing InstanceGroupManager resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L31">property autoHealingPolicies</a>
</h3>

```typescript
public autoHealingPolicies: pulumi.Output<{ ... } | undefined>;
```


) The autohealing policies for this managed instance
group. You can specify only one value. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L40">property baseInstanceName</a>
</h3>

```typescript
public baseInstanceName: pulumi.Output<string>;
```


The base instance name to use for
instances in this group. The value must be a valid
[RFC1035](https://www.ietf.org/rfc/rfc1035.txt) name. Supported characters
are lowercase letters, numbers, and hyphens (-). Instances are named by
appending a hyphen and a random four-character string to the base instance
name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L45">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


An optional textual description of the instance
group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L49">property fingerprint</a>
</h3>

```typescript
public fingerprint: pulumi.Output<string>;
```


The fingerprint of the instance group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L53">property instanceGroup</a>
</h3>

```typescript
public instanceGroup: pulumi.Output<string>;
```


The full URL of the instance group created by the manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L58">property instanceTemplate</a>
</h3>

```typescript
public instanceTemplate: pulumi.Output<string>;
```


The full URL to an instance template from
which all new instances will be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L62">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L67">property namedPorts</a>
</h3>

```typescript
public namedPorts: pulumi.Output<{ ... }[] | undefined>;
```


The named port configuration. See the section below
for details on configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L72">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L77">property rollingUpdatePolicy</a>
</h3>

```typescript
public rollingUpdatePolicy: pulumi.Output<{ ... } | undefined>;
```


) The update policy for this managed instance group. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagers/patch)
- - -

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L81">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URL of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L87">property targetPools</a>
</h3>

```typescript
public targetPools: pulumi.Output<string[] | undefined>;
```


The full URL of all target pools to which new
instances in the group are added. Updating the target pools attribute does
not affect existing instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L93">property targetSize</a>
</h3>

```typescript
public targetSize: pulumi.Output<number>;
```


The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to `0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L101">property updateStrategy</a>
</h3>

```typescript
public updateStrategy: pulumi.Output<string | undefined>;
```


If the `instance_template`
resource is modified, a value of `"NONE"` will prevent any of the managed
instances from being restarted by Terraform. A value of `"RESTART"` will
restart all of the instances at once. `"ROLLING_UPDATE"` is supported as [Beta feature].
A value of `"ROLLING_UPDATE"` requires `rolling_update_policy` block to be set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L107">property waitForInstances</a>
</h3>

```typescript
public waitForInstances: pulumi.Output<boolean | undefined>;
```


Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, Terraform will
continue trying until it times out.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L112">property zone</a>
</h3>

```typescript
public zone: pulumi.Output<string>;
```


The zone that instances in this group should be created
in.

<h2 class="pdoc-module-header" id="InstanceTemplate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L13">class InstanceTemplate</a>
</h2>

Manages a VM instance template resource within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/instance-templates)
and
[API](https://cloud.google.com/compute/docs/reference/latest/instanceTemplates).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L130">constructor</a>
</h3>

```typescript
new InstanceTemplate(name: string, args: InstanceTemplateArgs, opts?: pulumi.ResourceOptions)
```


Create a InstanceTemplate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceTemplateState): InstanceTemplate
```


Get an existing InstanceTemplate resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L30">property canIpForward</a>
</h3>

```typescript
public canIpForward: pulumi.Output<boolean | undefined>;
```


Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L34">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A brief description of this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L40">property disks</a>
</h3>

```typescript
public disks: pulumi.Output<{ ... }[]>;
```


Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L44">property guestAccelerators</a>
</h3>

```typescript
public guestAccelerators: pulumi.Output<{ ... }[] | undefined>;
```


List of the type and count of accelerator cards attached to the instance. Structure documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L49">property instanceDescription</a>
</h3>

```typescript
public instanceDescription: pulumi.Output<string | undefined>;
```


A brief description to use for instances
created from this template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L54">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


A set of key/value label pairs to assign to instances
created from this template,

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L58">property machineType</a>
</h3>

```typescript
public machineType: pulumi.Output<string>;
```


The machine type to create.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L63">property metadata</a>
</h3>

```typescript
public metadata: pulumi.Output<{ ... } | undefined>;
```


Metadata key/value pairs to make available from
within instances created from this template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L67">property metadataFingerprint</a>
</h3>

```typescript
public metadataFingerprint: pulumi.Output<string>;
```


The unique fingerprint of the metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L74">property metadataStartupScript</a>
</h3>

```typescript
public metadataStartupScript: pulumi.Output<string | undefined>;
```


An alternative to using the
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L79">property minCpuPlatform</a>
</h3>

```typescript
public minCpuPlatform: pulumi.Output<string | undefined>;
```


Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L84">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the instance template. If you leave
this blank, Terraform will auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L89">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L95">property networkInterfaces</a>
</h3>

```typescript
public networkInterfaces: pulumi.Output<{ ... }[] | undefined>;
```


Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L100">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L109">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom `subnetwork`
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L114">property schedulings</a>
</h3>

```typescript
public schedulings: pulumi.Output<{ ... }[]>;
```


The scheduling strategy to use. More details about
this configuration option are detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L118">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L122">property serviceAccount</a>
</h3>

```typescript
public serviceAccount: pulumi.Output<{ ... } | undefined>;
```


Service account to attach to the instance. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L126">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<string[] | undefined>;
```


Tags to attach to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L130">property tagsFingerprint</a>
</h3>

```typescript
public tagsFingerprint: pulumi.Output<string>;
```


The unique fingerprint of the tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Network">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L12">class Network</a>
</h2>

Manages a network within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/vpc)
and
[API](https://cloud.google.com/compute/docs/reference/latest/networks).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L66">constructor</a>
</h3>

```typescript
new Network(name: string, args?: NetworkArgs, opts?: pulumi.ResourceOptions)
```


Create a Network resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkState): Network
```


Get an existing Network resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L31">property autoCreateSubnetworks</a>
</h3>

```typescript
public autoCreateSubnetworks: pulumi.Output<boolean | undefined>;
```


If set to true, this network will be
created in auto subnet mode, and Google will create a subnet for each region
automatically. If set to false, a custom subnetted network will be created that
can support `google_compute_subnetwork` resources. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L35">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A brief description of this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L39">property gatewayIpv4</a>
</h3>

```typescript
public gatewayIpv4: pulumi.Output<string>;
```


The IPv4 address of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L45">property ipv4Range</a>
</h3>

```typescript
public ipv4Range: pulumi.Output<string | undefined>;
```


If set to a CIDR block, uses the legacy VPC API with the
specified range. This API is deprecated. If set, `auto_create_subnetworks` must be
explicitly set to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L50">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L55">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L62">property routingMode</a>
</h3>

```typescript
public routingMode: pulumi.Output<string>;
```


Sets the network-wide routing mode for Cloud Routers
to use. Accepted values are `"GLOBAL"` or `"REGIONAL"`. Defaults to `"REGIONAL"`.
Refer to the [Cloud Router documentation](https://cloud.google.com/router/docs/concepts/overview#dynamic-routing-mode)
for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L66">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="NetworkPeering">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L16">class NetworkPeering</a>
</h2>

Manages a network peering within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/vpc/vpc-peering)
and
[API](https://cloud.google.com/compute/docs/reference/latest/networks).

~> **Note:** Both network must create a peering with each other for the peering to be functional.

~> **Note:** Subnets IP ranges across peered VPC networks cannot overlap.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L53">constructor</a>
</h3>

```typescript
new NetworkPeering(name: string, args: NetworkPeeringArgs, opts?: pulumi.ResourceOptions)
```


Create a NetworkPeering resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkPeeringState): NetworkPeering
```


Get an existing NetworkPeering resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L33">property autoCreateRoutes</a>
</h3>

```typescript
public autoCreateRoutes: pulumi.Output<boolean | undefined>;
```


If set to `true`, the routes between the two networks will
be created and managed automatically. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name of the peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L41">property network</a>
</h3>

```typescript
public network: pulumi.Output<string>;
```


Resource link of the network to add a peering to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L45">property peerNetwork</a>
</h3>

```typescript
public peerNetwork: pulumi.Output<string>;
```


Resource link of the peer network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L49">property state</a>
</h3>

```typescript
public state: pulumi.Output<string>;
```


State for the peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L53">property stateDetails</a>
</h3>

```typescript
public stateDetails: pulumi.Output<string>;
```


Details about the current state of the peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ProjectMetadata">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadata.ts#L16">class ProjectMetadata</a>
</h2>

Manages metadata common to all instances for a project in GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/storing-retrieving-metadata)
and
[API](https://cloud.google.com/compute/docs/reference/latest/projects/setCommonInstanceMetadata).

~> **Note:**  If you want to manage only single key/value pairs within the project metadata
rather than the entire set, then use
[google_compute_project_metadata_item](compute_project_metadata_item.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadata.ts#L38">constructor</a>
</h3>

```typescript
new ProjectMetadata(name: string, args: ProjectMetadataArgs, opts?: pulumi.ResourceOptions)
```


Create a ProjectMetadata resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadata.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProjectMetadataState): ProjectMetadata
```


Get an existing ProjectMetadata resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadata.ts#L33">property metadata</a>
</h3>

```typescript
public metadata: pulumi.Output<{ ... }>;
```


A series of key value pairs. Changing this resource
updates the GCE state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadata.ts#L38">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ProjectMetadataItem">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadataItem.ts#L12">class ProjectMetadataItem</a>
</h2>

Manages a single key/value pair on metadata common to all instances for
a project in GCE. Using `google_compute_project_metadata_item` lets you
manage a single key/value setting in Terraform rather than the entire
project metadata map.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadataItem.ts#L37">constructor</a>
</h3>

```typescript
new ProjectMetadataItem(name: string, args: ProjectMetadataItemArgs, opts?: pulumi.ResourceOptions)
```


Create a ProjectMetadataItem resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadataItem.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProjectMetadataItemState): ProjectMetadataItem
```


Get an existing ProjectMetadataItem resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadataItem.ts#L28">property key</a>
</h3>

```typescript
public key: pulumi.Output<string>;
```


The metadata key to set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadataItem.ts#L33">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadataItem.ts#L37">property value</a>
</h3>

```typescript
public value: pulumi.Output<string>;
```


The value to set for the given metadata key.

<h2 class="pdoc-module-header" id="RegionAutoscaler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L17">class RegionAutoscaler</a>
</h2>

A Compute Engine Regional Autoscaler automatically adds or removes virtual machines from
a managed instance group based on increases or decreases in load. This allows
your applications to gracefully handle increases in traffic and reduces cost
when the need for resources is lower. You just define the autoscaling policy and
the autoscaler performs automatic scaling based on the measured load. For more
information, see [the official
documentation](https://cloud.google.com/compute/docs/autoscaler/) and
[API](https://cloud.google.com/compute/docs/reference/latest/regionAutoscalers)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L64">constructor</a>
</h3>

```typescript
new RegionAutoscaler(name: string, args: RegionAutoscalerArgs, opts?: pulumi.ResourceOptions)
```


Create a RegionAutoscaler resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L26">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RegionAutoscalerState): RegionAutoscaler
```


Get an existing RegionAutoscaler resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L34">property autoscalingPolicy</a>
</h3>

```typescript
public autoscalingPolicy: pulumi.Output<{ ... }>;
```


The parameters of the autoscaling
algorithm. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L39">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


An optional textual description of the instance
group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Google Cloud Monitoring metric to follow, e.g.
`compute.googleapis.com/instance/network/received_bytes_count`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L49">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L53">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region of the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L57">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URL of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L64">property target</a>
</h3>

```typescript
public target: pulumi.Output<string>;
```


The floating point threshold where load balancing utilization
should be. E.g. if the load balancer's `maxRatePerInstance` is 10 requests
per second (RPS) then setting this to 0.5 would cause the group to be scaled
such that each instance receives 5 RPS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RegionBackendService">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L11">class RegionBackendService</a>
</h2>

A Region Backend Service defines a regionally-scoped group of virtual machines that will serve traffic for load balancing.
For more information see [the official documentation](https://cloud.google.com/compute/docs/load-balancing/internal/)
and [API](https://cloud.google.com/compute/docs/reference/latest/regionBackendServices).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L81">constructor</a>
</h3>

```typescript
new RegionBackendService(name: string, args: RegionBackendServiceArgs, opts?: pulumi.ResourceOptions)
```


Create a RegionBackendService resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RegionBackendServiceState): RegionBackendService
```


Get an existing RegionBackendService resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L28">property backends</a>
</h3>

```typescript
public backends: pulumi.Output<{ ... }[] | undefined>;
```


The list of backends that serve this BackendService.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L33">property connectionDrainingTimeoutSec</a>
</h3>

```typescript
public connectionDrainingTimeoutSec: pulumi.Output<number | undefined>;
```


Time for which instance will be drained
(not accept new connections, but still work to finish started ones). Defaults to `0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L37">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Textual description for the backend.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L41">property fingerprint</a>
</h3>

```typescript
public fingerprint: pulumi.Output<string>;
```


The fingerprint of the backend service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L47">property healthChecks</a>
</h3>

```typescript
public healthChecks: pulumi.Output<string>;
```


Specifies a list of health checks
for checking the health of the backend service. Currently at most
one health check can be specified, and a health check is required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L51">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the backend service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L56">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L61">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The protocol for incoming requests. Defaults to
`HTTP`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L66">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The Region in which the created address should reside.
If it is not provided, the provider region is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L70">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L76">property sessionAffinity</a>
</h3>

```typescript
public sessionAffinity: pulumi.Output<string>;
```


How to distribute load. Options are `NONE` (no
affinity), `CLIENT_IP`, `CLIENT_IP_PROTO`, or `CLIENT_IP_PORT_PROTO`.
Defaults to `NONE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L81">property timeoutSec</a>
</h3>

```typescript
public timeoutSec: pulumi.Output<number>;
```


The number of secs to wait for a backend to respond
to a request before considering the request failed. Defaults to `30`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RegionInstanceGroupManager">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L14">class RegionInstanceGroupManager</a>
</h2>

The Google Compute Engine Regional Instance Group Manager API creates and manages pools
of homogeneous Compute Engine virtual machine instances from a common instance
template. For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups)
and [API](https://cloud.google.com/compute/docs/reference/latest/regionInstanceGroupManagers)

~> **Note:** Use [google_compute_instance_group_manager](/docs/providers/google/r/compute_instance_group_manager.html) to create a single-zone instance group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L116">constructor</a>
</h3>

```typescript
new RegionInstanceGroupManager(name: string, args: RegionInstanceGroupManagerArgs, opts?: pulumi.ResourceOptions)
```


Create a RegionInstanceGroupManager resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RegionInstanceGroupManagerState): RegionInstanceGroupManager
```


Get an existing RegionInstanceGroupManager resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L31">property autoHealingPolicies</a>
</h3>

```typescript
public autoHealingPolicies: pulumi.Output<{ ... } | undefined>;
```


) The autohealing policies for this managed instance
group. You can specify only one value. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L40">property baseInstanceName</a>
</h3>

```typescript
public baseInstanceName: pulumi.Output<string>;
```


The base instance name to use for
instances in this group. The value must be a valid
[RFC1035](https://www.ietf.org/rfc/rfc1035.txt) name. Supported characters
are lowercase letters, numbers, and hyphens (-). Instances are named by
appending a hyphen and a random four-character string to the base instance
name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L45">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


An optional textual description of the instance
group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L51">property distributionPolicyZones</a>
</h3>

```typescript
public distributionPolicyZones: pulumi.Output<string[]>;
```


) The distribution policy for this managed instance
group. You can specify one or more values. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selectingzones).
- - -

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L55">property fingerprint</a>
</h3>

```typescript
public fingerprint: pulumi.Output<string>;
```


The fingerprint of the instance group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L59">property instanceGroup</a>
</h3>

```typescript
public instanceGroup: pulumi.Output<string>;
```


The full URL of the instance group created by the manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L64">property instanceTemplate</a>
</h3>

```typescript
public instanceTemplate: pulumi.Output<string>;
```


The full URL to an instance template from
which all new instances will be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L68">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L73">property namedPorts</a>
</h3>

```typescript
public namedPorts: pulumi.Output<{ ... }[] | undefined>;
```


The named port configuration. See the section below
for details on configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L78">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L82">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region where the managed instance group resides.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L86">property rollingUpdatePolicy</a>
</h3>

```typescript
public rollingUpdatePolicy: pulumi.Output<{ ... } | undefined>;
```


) The update policy for this managed instance group. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patch)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L90">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URL of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L96">property targetPools</a>
</h3>

```typescript
public targetPools: pulumi.Output<string[] | undefined>;
```


The full URL of all target pools to which new
instances in the group are added. Updating the target pools attribute does
not affect existing instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L102">property targetSize</a>
</h3>

```typescript
public targetSize: pulumi.Output<number>;
```


The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to `0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L110">property updateStrategy</a>
</h3>

```typescript
public updateStrategy: pulumi.Output<string | undefined>;
```


If the `instance_template`
resource is modified, a value of `"NONE"` will prevent any of the managed
instances from being restarted by Terraform. A value of `"ROLLING_UPDATE"`
is supported as [Beta feature]. A value of `"ROLLING_UPDATE"` requires
`rolling_update_policy` block to be set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L116">property waitForInstances</a>
</h3>

```typescript
public waitForInstances: pulumi.Output<boolean | undefined>;
```


Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, Terraform will
continue trying until it times out.

<h2 class="pdoc-module-header" id="Route">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L12">class Route</a>
</h2>

Manages a network route within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/vpc/routes)
and
[API](https://cloud.google.com/compute/docs/reference/latest/routes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L86">constructor</a>
</h3>

```typescript
new Route(name: string, args: RouteArgs, opts?: pulumi.ResourceOptions)
```


Create a Route resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouteState): Route
```


Get an existing Route resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L25">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L30">property destRange</a>
</h3>

```typescript
public destRange: pulumi.Output<string>;
```


The destination IPv4 address range that this
route applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L35">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L39">property network</a>
</h3>

```typescript
public network: pulumi.Output<string>;
```


The name or self_link of the network to attach this route to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L45">property nextHopGateway</a>
</h3>

```typescript
public nextHopGateway: pulumi.Output<string | undefined>;
```


The URL of the internet gateway to route
to if this route is matched. The alias "default-internet-gateway" can also
be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L50">property nextHopInstance</a>
</h3>

```typescript
public nextHopInstance: pulumi.Output<string | undefined>;
```


The name of the VM instance to route to
if this route is matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L55">property nextHopInstanceZone</a>
</h3>

```typescript
public nextHopInstanceZone: pulumi.Output<string | undefined>;
```


The zone of the instance specified in `next_hop_instance`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L60">property nextHopIp</a>
</h3>

```typescript
public nextHopIp: pulumi.Output<string | undefined>;
```


The IP address of the next hop if this route
is matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L64">property nextHopNetwork</a>
</h3>

```typescript
public nextHopNetwork: pulumi.Output<string>;
```


The name of the next hop network, if available.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L69">property nextHopVpnTunnel</a>
</h3>

```typescript
public nextHopVpnTunnel: pulumi.Output<string | undefined>;
```


The name of the VPN to route to if this
route is matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L73">property priority</a>
</h3>

```typescript
public priority: pulumi.Output<number | undefined>;
```


The priority of this route, used to break ties. Defaults to 1000.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L78">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L82">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L86">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<string[] | undefined>;
```


The tags that this route applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Router">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L12">class Router</a>
</h2>

Manages a Cloud Router resource. For more information see
[the official documentation](https://cloud.google.com/compute/docs/cloudrouter)
and
[API](https://cloud.google.com/compute/docs/reference/latest/routers).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L61">constructor</a>
</h3>

```typescript
new Router(name: string, args: RouterArgs, opts?: pulumi.ResourceOptions)
```


Create a Router resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouterState): Router
```


Get an existing Router resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L30">property bgp</a>
</h3>

```typescript
public bgp: pulumi.Output<{ ... }>;
```


BGP information specific to this router.
Changing this forces a new router to be created.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L35">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the resource.
Changing this forces a new router to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L40">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the router, required by GCE. Changing
this forces a new router to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L45">property network</a>
</h3>

```typescript
public network: pulumi.Output<string>;
```


The name or resource link to the network this Cloud Router
will use to learn and announce routes. Changing this forces a new router to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L51">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
Changing this forces a new router to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L57">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region this router should sit in. If not specified,
the project region will be used. Changing this forces a new router to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L61">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RouterInterface">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L12">class RouterInterface</a>
</h2>

Manages a Cloud Router interface. For more information see
[the official documentation](https://cloud.google.com/compute/docs/cloudrouter)
and
[API](https://cloud.google.com/compute/docs/reference/latest/routers).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L55">constructor</a>
</h3>

```typescript
new RouterInterface(name: string, args: RouterInterfaceArgs, opts?: pulumi.ResourceOptions)
```


Create a RouterInterface resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouterInterfaceState): RouterInterface
```


Get an existing RouterInterface resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L29">property ipRange</a>
</h3>

```typescript
public ipRange: pulumi.Output<string | undefined>;
```


IP address and range of the interface. The IP range must be
in the RFC3927 link-local IP space. Changing this forces a new interface to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the interface, required by GCE. Changing
this forces a new interface to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L39">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which this interface's router belongs. If it
is not provided, the provider project is used. Changing this forces a new interface to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L45">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region this interface's router sits in. If not specified,
the project region will be used. Changing this forces a new interface to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L50">property router</a>
</h3>

```typescript
public router: pulumi.Output<string>;
```


The name of the router this interface will be attached to.
Changing this forces a new interface to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L55">property vpnTunnel</a>
</h3>

```typescript
public vpnTunnel: pulumi.Output<string>;
```


The name or resource link to the VPN tunnel this
interface will be linked to. Changing this forces a new interface to be created.

<h2 class="pdoc-module-header" id="RouterPeer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L12">class RouterPeer</a>
</h2>

Manages a Cloud Router BGP peer. For more information see
[the official documentation](https://cloud.google.com/compute/docs/cloudrouter)
and
[API](https://cloud.google.com/compute/docs/reference/latest/routers).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L69">constructor</a>
</h3>

```typescript
new RouterPeer(name: string, args: RouterPeerArgs, opts?: pulumi.ResourceOptions)
```


Create a RouterPeer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouterPeerState): RouterPeer
```


Get an existing RouterPeer resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L29">property advertisedRoutePriority</a>
</h3>

```typescript
public advertisedRoutePriority: pulumi.Output<number | undefined>;
```


The priority of routes advertised to this BGP peer.
Changing this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L34">property interface</a>
</h3>

```typescript
public interface: pulumi.Output<string>;
```


The name of the interface the BGP peer is associated with.
Changing this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L38">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string>;
```


IP address of the interface inside Google Cloud Platform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L43">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for BGP peer, required by GCE. Changing
this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L48">property peerAsn</a>
</h3>

```typescript
public peerAsn: pulumi.Output<number>;
```


Peer BGP Autonomous System Number (ASN).
Changing this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L53">property peerIpAddress</a>
</h3>

```typescript
public peerIpAddress: pulumi.Output<string | undefined>;
```


IP address of the BGP interface outside Google Cloud.
Changing this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L58">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which this peer's router belongs. If it
is not provided, the provider project is used. Changing this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L64">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region this peer's router sits in. If not specified,
the project region will be used. Changing this forces a new peer to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L69">property router</a>
</h3>

```typescript
public router: pulumi.Output<string>;
```


The name of the router in which this BGP peer will be configured.
Changing this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SSLCertificate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L13">class SSLCertificate</a>
</h2>

Creates an SSL certificate resource necessary for HTTPS load balancing in GCE.
For more information see
[the official documentation](https://cloud.google.com/compute/docs/load-balancing/http/ssl-certificates) and
[API](https://cloud.google.com/compute/docs/reference/latest/sslCertificates).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L64">constructor</a>
</h3>

```typescript
new SSLCertificate(name: string, args: SSLCertificateArgs, opts?: pulumi.ResourceOptions)
```


Create a SSLCertificate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SSLCertificateState): SSLCertificate
```


Get an existing SSLCertificate resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L31">property certificate</a>
</h3>

```typescript
public certificate: pulumi.Output<string>;
```


A local certificate file in PEM format. The chain
may be at most 5 certs long, and must include at least one intermediate
cert. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L35">property certificateId</a>
</h3>

```typescript
public certificateId: pulumi.Output<string>;
```


A unique ID for the certificate, assigned by GCE.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L40">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


An optional description of this resource.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the SSL certificate. If you leave
this blank, Terraform will auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L50">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L55">property privateKey</a>
</h3>

```typescript
public privateKey: pulumi.Output<string>;
```


Write only private key in PEM format.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L60">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L64">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SharedVPCHostProject">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCHostProject.ts#L15">class SharedVPCHostProject</a>
</h2>

Enables the Google Compute Engine
[Shared VPC](https://cloud.google.com/compute/docs/shared-vpc)
feature for a project, assigning it as a Shared VPC host project.

For more information, see,
[the Project API documentation](https://cloud.google.com/compute/docs/reference/latest/projects),
where the Shared VPC feature is referred to by its former name "XPN".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCHostProject.ts#L31">constructor</a>
</h3>

```typescript
new SharedVPCHostProject(name: string, args: SharedVPCHostProjectArgs, opts?: pulumi.ResourceOptions)
```


Create a SharedVPCHostProject resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCHostProject.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SharedVPCHostProjectState): SharedVPCHostProject
```


Get an existing SharedVPCHostProject resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCHostProject.ts#L31">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project that will serve as a Shared VPC host project

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SharedVPCServiceProject">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCServiceProject.ts#L16">class SharedVPCServiceProject</a>
</h2>

Enables the Google Compute Engine
[Shared VPC](https://cloud.google.com/compute/docs/shared-vpc)
feature for a project, assigning it as a Shared VPC service project associated
with a given host project.

For more information, see,
[the Project API documentation](https://cloud.google.com/compute/docs/reference/latest/projects),
where the Shared VPC feature is referred to by its former name "XPN".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCServiceProject.ts#L36">constructor</a>
</h3>

```typescript
new SharedVPCServiceProject(name: string, args: SharedVPCServiceProjectArgs, opts?: pulumi.ResourceOptions)
```


Create a SharedVPCServiceProject resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCServiceProject.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SharedVPCServiceProjectState): SharedVPCServiceProject
```


Get an existing SharedVPCServiceProject resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCServiceProject.ts#L32">property hostProject</a>
</h3>

```typescript
public hostProject: pulumi.Output<string>;
```


The ID of a host project to associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCServiceProject.ts#L36">property serviceProject</a>
</h3>

```typescript
public serviceProject: pulumi.Output<string>;
```


The ID of the project that will serve as a Shared VPC service project.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Snapshot">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L12">class Snapshot</a>
</h2>

Creates a new snapshot of a disk within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/disks/create-snapshots)
and
[API](https://cloud.google.com/compute/docs/reference/latest/snapshots).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L86">constructor</a>
</h3>

```typescript
new Snapshot(name: string, args: SnapshotArgs, opts?: pulumi.ResourceOptions)
```


Create a Snapshot resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SnapshotState): Snapshot
```


Get an existing Snapshot resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L28">property labelFingerprint</a>
</h3>

```typescript
public labelFingerprint: pulumi.Output<string>;
```


The unique fingerprint of the labels.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L32">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


A set of key/value label pairs to assign to the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L42">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L46">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L53">property snapshotEncryptionKeyRaw</a>
</h3>

```typescript
public snapshotEncryptionKeyRaw: pulumi.Output<string | undefined>;
```


A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L60">property snapshotEncryptionKeySha256</a>
</h3>

```typescript
public snapshotEncryptionKeySha256: pulumi.Output<string>;
```


The [RFC 4648 base64]
(https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the
[customer-supplied encryption key](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
that protects this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L64">property sourceDisk</a>
</h3>

```typescript
public sourceDisk: pulumi.Output<string>;
```


The disk which will be used as the source of the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L71">property sourceDiskEncryptionKeyRaw</a>
</h3>

```typescript
public sourceDiskEncryptionKeyRaw: pulumi.Output<string | undefined>;
```


A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to decrypt the source disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L78">property sourceDiskEncryptionKeySha256</a>
</h3>

```typescript
public sourceDiskEncryptionKeySha256: pulumi.Output<string>;
```


The [RFC 4648 base64]
(https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the
[customer-supplied encryption key](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
that protects the source disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L82">property sourceDiskLink</a>
</h3>

```typescript
public sourceDiskLink: pulumi.Output<string>;
```


The URI of the source disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L86">property zone</a>
</h3>

```typescript
public zone: pulumi.Output<string>;
```


The zone where the source disk is located.

<h2 class="pdoc-module-header" id="Subnetwork">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L12">class Subnetwork</a>
</h2>

Manages a subnetwork within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/vpc/#vpc_networks_and_subnets)
and
[API](https://cloud.google.com/compute/docs/reference/latest/subnetworks).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L78">constructor</a>
</h3>

```typescript
new Subnetwork(name: string, args: SubnetworkArgs, opts?: pulumi.ResourceOptions)
```


Create a Subnetwork resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubnetworkState): Subnetwork
```


Get an existing Subnetwork resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L28">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of this subnetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L34">property enableFlowLogs</a>
</h3>

```typescript
public enableFlowLogs: pulumi.Output<boolean | undefined>;
```


)
Set to `true` to enable [flow logs](https://cloud.google.com/vpc/docs/using-flow-logs)
for this subnetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L35">property fingerprint</a>
</h3>

```typescript
public fingerprint: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L39">property gatewayAddress</a>
</h3>

```typescript
public gatewayAddress: pulumi.Output<string>;
```


The IP address of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L43">property ipCidrRange</a>
</h3>

```typescript
public ipCidrRange: pulumi.Output<string>;
```


The range of IP addresses belonging to this subnetwork secondary range. Ranges must be unique and non-overlapping with all primary and secondary IP ranges within a network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L48">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L54">property network</a>
</h3>

```typescript
public network: pulumi.Output<string>;
```


The network name or resource link to the parent
network of this subnetwork. The parent network must have been created
in custom subnet mode.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L60">property privateIpGoogleAccess</a>
</h3>

```typescript
public privateIpGoogleAccess: pulumi.Output<boolean | undefined>;
```


Whether the VMs in this subnet
can access Google services without assigned external IP
addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L65">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L70">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region this subnetwork will be created in. If
unspecified, this defaults to the region configured in the provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L74">property secondaryIpRanges</a>
</h3>

```typescript
public secondaryIpRanges: pulumi.Output<{ ... }[] | undefined>;
```


) An array of configurations for secondary IP ranges for VM instances contained in this subnetwork. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L78">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TargetHttpProxy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L6">class TargetHttpProxy</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L32">constructor</a>
</h3>

```typescript
new TargetHttpProxy(name: string, args: TargetHttpProxyArgs, opts?: pulumi.ResourceOptions)
```


Create a TargetHttpProxy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L15">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TargetHttpProxyState): TargetHttpProxy
```


Get an existing TargetHttpProxy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L19">property creationTimestamp</a>
</h3>

```typescript
public creationTimestamp: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L20">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L21">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L26">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L27">property proxyId</a>
</h3>

```typescript
public proxyId: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L31">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L32">property urlMap</a>
</h3>

```typescript
public urlMap: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TargetHttpsProxy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L6">class TargetHttpsProxy</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L34">constructor</a>
</h3>

```typescript
new TargetHttpsProxy(name: string, args: TargetHttpsProxyArgs, opts?: pulumi.ResourceOptions)
```


Create a TargetHttpsProxy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L15">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TargetHttpsProxyState): TargetHttpsProxy
```


Get an existing TargetHttpsProxy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L19">property creationTimestamp</a>
</h3>

```typescript
public creationTimestamp: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L20">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L21">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L26">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L27">property proxyId</a>
</h3>

```typescript
public proxyId: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L31">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L32">property sslCertificates</a>
</h3>

```typescript
public sslCertificates: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L33">property sslPolicy</a>
</h3>

```typescript
public sslPolicy: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L34">property urlMap</a>
</h3>

```typescript
public urlMap: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TargetPool">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L14">class TargetPool</a>
</h2>

Manages a Target Pool within GCE. This is a collection of instances used as
target of a network load balancer (Forwarding Rule). For more information see
[the official
documentation](https://cloud.google.com/compute/docs/load-balancing/network/target-pools)
and [API](https://cloud.google.com/compute/docs/reference/latest/targetPools).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L78">constructor</a>
</h3>

```typescript
new TargetPool(name: string, args?: TargetPoolArgs, opts?: pulumi.ResourceOptions)
```


Create a TargetPool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TargetPoolState): TargetPool
```


Get an existing TargetPool resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L31">property backupPool</a>
</h3>

```typescript
public backupPool: pulumi.Output<string | undefined>;
```


URL to the backup target pool. Must also set
failover\_ratio.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L35">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Textual description field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L40">property failoverRatio</a>
</h3>

```typescript
public failoverRatio: pulumi.Output<number | undefined>;
```


Ratio (0 to 1) of failed nodes before using the
backup pool (which must also be set).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L45">property healthChecks</a>
</h3>

```typescript
public healthChecks: pulumi.Output<string | undefined>;
```


List of zero or one health check name or self_link. Only
legacy `google_compute_http_health_check` is supported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L53">property instances</a>
</h3>

```typescript
public instances: pulumi.Output<string[]>;
```


List of instances in the pool. They can be given as
URLs, or in the form of "zone/name". Note that the instances need not exist
at the time of target pool creation, so there is no need to use the
Terraform interpolators to create a dependency on the instances from the
target pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L58">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L63">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L68">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


Where the target pool resides. Defaults to project
region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L72">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L78">property sessionAffinity</a>
</h3>

```typescript
public sessionAffinity: pulumi.Output<string | undefined>;
```


How to distribute load. Options are "NONE" (no
affinity). "CLIENT\_IP" (hash of the source/dest addresses / ports), and
"CLIENT\_IP\_PROTO" also includes the protocol (default "NONE").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TargetSSLProxy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L6">class TargetSSLProxy</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L34">constructor</a>
</h3>

```typescript
new TargetSSLProxy(name: string, args: TargetSSLProxyArgs, opts?: pulumi.ResourceOptions)
```


Create a TargetSSLProxy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L15">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TargetSSLProxyState): TargetSSLProxy
```


Get an existing TargetSSLProxy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L19">property backendService</a>
</h3>

```typescript
public backendService: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L20">property creationTimestamp</a>
</h3>

```typescript
public creationTimestamp: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L21">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L22">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L27">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L28">property proxyHeader</a>
</h3>

```typescript
public proxyHeader: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L29">property proxyId</a>
</h3>

```typescript
public proxyId: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L33">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L34">property sslCertificates</a>
</h3>

```typescript
public sslCertificates: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TargetTCPProxy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L6">class TargetTCPProxy</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L33">constructor</a>
</h3>

```typescript
new TargetTCPProxy(name: string, args: TargetTCPProxyArgs, opts?: pulumi.ResourceOptions)
```


Create a TargetTCPProxy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L15">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TargetTCPProxyState): TargetTCPProxy
```


Get an existing TargetTCPProxy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L19">property backendService</a>
</h3>

```typescript
public backendService: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L20">property creationTimestamp</a>
</h3>

```typescript
public creationTimestamp: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L21">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L22">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L27">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L28">property proxyHeader</a>
</h3>

```typescript
public proxyHeader: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L29">property proxyId</a>
</h3>

```typescript
public proxyId: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L33">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="URLMap">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L13">class URLMap</a>
</h2>

Manages a URL Map resource within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/load-balancing/http/url-map)
and
[API](https://cloud.google.com/compute/docs/reference/latest/urlMaps).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L66">constructor</a>
</h3>

```typescript
new URLMap(name: string, args: URLMapArgs, opts?: pulumi.ResourceOptions)
```


Create a URLMap resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: URLMapState): URLMap
```


Get an existing URLMap resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L29">property defaultService</a>
</h3>

```typescript
public defaultService: pulumi.Output<string>;
```


The backend service or backend bucket to use if none of the given paths match.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L33">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


An optional description of this test.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L37">property fingerprint</a>
</h3>

```typescript
public fingerprint: pulumi.Output<string>;
```


The unique fingerprint for this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L41">property hostRules</a>
</h3>

```typescript
public hostRules: pulumi.Output<{ ... }[] | undefined>;
```


A list of host rules. Multiple blocks of this type are permitted. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L45">property mapId</a>
</h3>

```typescript
public mapId: pulumi.Output<string>;
```


The GCE assigned ID of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L49">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the `path_matcher` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L53">property pathMatchers</a>
</h3>

```typescript
public pathMatchers: pulumi.Output<{ ... }[] | undefined>;
```


The name of the `path_matcher` to apply this host rule to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L58">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L62">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L66">property tests</a>
</h3>

```typescript
public tests: pulumi.Output<{ ... }[] | undefined>;
```


The test to perform.  Multiple blocks of this type are permitted. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="VPNGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L6">class VPNGateway</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L32">constructor</a>
</h3>

```typescript
new VPNGateway(name: string, args: VPNGatewayArgs, opts?: pulumi.ResourceOptions)
```


Create a VPNGateway resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L15">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VPNGatewayState): VPNGateway
```


Get an existing VPNGateway resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L19">property creationTimestamp</a>
</h3>

```typescript
public creationTimestamp: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L20">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L21">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L22">property network</a>
</h3>

```typescript
public network: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L27">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L28">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L32">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="VPNTunnel">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L13">class VPNTunnel</a>
</h2>

Manages a VPN Tunnel to the GCE network. For more info, read the
[documentation](https://cloud.google.com/compute/docs/vpn).

~> **Note:** All arguments including the `shared_secret` will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L94">constructor</a>
</h3>

```typescript
new VPNTunnel(name: string, args: VPNTunnelArgs, opts?: pulumi.ResourceOptions)
```


Create a VPNTunnel resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VPNTunnelState): VPNTunnel
```


Get an existing VPNTunnel resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L30">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the resource. Changing this forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L34">property detailedStatus</a>
</h3>

```typescript
public detailedStatus: pulumi.Output<string>;
```


Information about the status of the VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L39">property ikeVersion</a>
</h3>

```typescript
public ikeVersion: pulumi.Output<number | undefined>;
```


Either version 1 or 2. Default is 2. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L46">property localTrafficSelectors</a>
</h3>

```typescript
public localTrafficSelectors: pulumi.Output<string[]>;
```


Specifies which CIDR ranges are
announced to the VPN peer. Mandatory if the VPN gateway is attached to a
custom subnetted network. Refer to Google documentation for more
information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L51">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L56">property peerIp</a>
</h3>

```typescript
public peerIp: pulumi.Output<string>;
```


The VPN gateway sitting outside of GCE. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L61">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L67">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region this tunnel should sit in. If not specified,
the project region will be used. Changing this forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L74">property remoteTrafficSelectors</a>
</h3>

```typescript
public remoteTrafficSelectors: pulumi.Output<string[]>;
```


Specifies which CIDR ranges the VPN
tunnel can route to the remote side. Mandatory if the VPN gateway is attached to a
custom subnetted network. Refer to Google documentation for more
information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L80">property router</a>
</h3>

```typescript
public router: pulumi.Output<string | undefined>;
```


Name of a Cloud Router in the same region
to be used for dynamic routing. Refer to Google documentation for more
information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L84">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L89">property sharedSecret</a>
</h3>

```typescript
public sharedSecret: pulumi.Output<string>;
```


A passphrase shared between the two VPN gateways.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L94">property targetVpnGateway</a>
</h3>

```typescript
public targetVpnGateway: pulumi.Output<string>;
```


A link to the VPN gateway sitting inside
GCE. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getAddress">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getAddress.ts#L10">function getAddress</a>
</h2>

```typescript
getAddress(args: GetAddressArgs): Promise<GetAddressResult>
```


Get the IP address from a static address. For more information see
the official [API](https://cloud.google.com/compute/docs/reference/latest/addresses/get) documentation.

<h2 class="pdoc-module-header" id="getBackendService">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L11">function getBackendService</a>
</h2>

```typescript
getBackendService(args: GetBackendServiceArgs): Promise<GetBackendServiceResult>
```


Provide acces to a Backend Service's attribute. For more information
see [the official documentation](https://cloud.google.com/compute/docs/load-balancing/http/backend-service)
and the [API](https://cloud.google.com/compute/docs/reference/latest/backendServices).

<h2 class="pdoc-module-header" id="getDefaultServiceAccount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getDefaultServiceAccount.ts#L9">function getDefaultServiceAccount</a>
</h2>

```typescript
getDefaultServiceAccount(args?: GetDefaultServiceAccountArgs): Promise<void>
```


Use this data source to retrieve default service account for this project

<h2 class="pdoc-module-header" id="getForwardingRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L9">function getForwardingRule</a>
</h2>

```typescript
getForwardingRule(args: GetForwardingRuleArgs): Promise<GetForwardingRuleResult>
```


Get a forwarding rule within GCE from its name.

<h2 class="pdoc-module-header" id="getGlobalAddress">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getGlobalAddress.ts#L10">function getGlobalAddress</a>
</h2>

```typescript
getGlobalAddress(args: GetGlobalAddressArgs): Promise<GetGlobalAddressResult>
```


Get the IP address from a static address reserved for a Global Forwarding Rule which are only used for HTTP load balancing. For more information see
the official [API](https://cloud.google.com/compute/docs/reference/latest/globalAddresses) documentation.

<h2 class="pdoc-module-header" id="getImage">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L10">function getImage</a>
</h2>

```typescript
getImage(args?: GetImageArgs): Promise<GetImageResult>
```


Get information about a Google Compute Image. Check that your service account has the `compute.imageUser` role if you want to share [custom images](https://cloud.google.com/compute/docs/images/sharing-images-across-projects) from another project. If you want to use [public images][pubimg], do not forget to specify the dedicated project. For more information see
[the official documentation](https://cloud.google.com/compute/docs/images) and its [API](https://cloud.google.com/compute/docs/reference/latest/images).

<h2 class="pdoc-module-header" id="getInstanceGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getInstanceGroup.ts#L18">function getInstanceGroup</a>
</h2>

```typescript
getInstanceGroup(args?: GetInstanceGroupArgs): Promise<GetInstanceGroupResult>
```


Get a Compute Instance Group within GCE.
For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/#unmanaged_instance_groups)
and [API](https://cloud.google.com/compute/docs/reference/latest/instanceGroups)

```
data "google_compute_instance_group" "all" {
	name = "instance-group-name"
	zone = "us-central1-a"
}
```

<h2 class="pdoc-module-header" id="getLBIPRanges">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getLBIPRanges.ts#L11">function getLBIPRanges</a>
</h2>

```typescript
getLBIPRanges(): Promise<GetLBIPRangesResult>
```


Use this data source to access IP ranges in your firewall rules.

https://cloud.google.com/compute/docs/load-balancing/health-checks#health_check_source_ips_and_firewall_rules

<h2 class="pdoc-module-header" id="getNetwork">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getNetwork.ts#L9">function getNetwork</a>
</h2>

```typescript
getNetwork(args: GetNetworkArgs): Promise<GetNetworkResult>
```


Get a network within GCE from its name.

<h2 class="pdoc-module-header" id="getRegionInstanceGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getRegionInstanceGroup.ts#L35">function getRegionInstanceGroup</a>
</h2>

```typescript
getRegionInstanceGroup(args?: GetRegionInstanceGroupArgs): Promise<GetRegionInstanceGroupResult>
```


Get a Compute Region Instance Group within GCE.
For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/latest/regionInstanceGroups).

```
data "google_compute_region_instance_group" "group" {
	name = "instance-group-name"
}
```

The most common use of this datasource will be to fetch information about the instances inside regional managed instance groups, for instance:

```
resource "google_compute_region_instance_group_manager" "foo" {
	name = "some_name"
    ...
	base_instance_name = "foo"
    ...
	instance_template = "${google_compute_instance_template.foo.self_link}"
	target_pools = ["${google_compute_target_pool.foo.self_link}"]
    ...
}

data "google_compute_region_instance_group" "data_source" {
	self_link = "${google_compute_region_instance_group_manager.foo.instance_group}"
}

```

<h2 class="pdoc-module-header" id="getSubnetwork">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getSubnetwork.ts#L9">function getSubnetwork</a>
</h2>

```typescript
getSubnetwork(args: GetSubnetworkArgs): Promise<GetSubnetworkResult>
```


Get a subnetwork within GCE from its name and region.

<h2 class="pdoc-module-header" id="getVPNGateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getVPNGateway.ts#L9">function getVPNGateway</a>
</h2>

```typescript
getVPNGateway(args: GetVPNGatewayArgs): Promise<GetVPNGatewayResult>
```


Get a VPN gateway within GCE from its name.

<h2 class="pdoc-module-header" id="getZones">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getZones.ts#L24">function getZones</a>
</h2>

```typescript
getZones(args?: GetZonesArgs): Promise<GetZonesResult>
```


Provides access to available Google Compute zones in a region for a given project.
See more about [regions and zones](https://cloud.google.com/compute/docs/regions-zones/regions-zones) in the upstream docs.

```
data "google_compute_zones" "available" {}

resource "google_compute_instance_group_manager" "foo" {
  count = "${length(data.google_compute_zones.available.names)}"

  name               = "terraform-test-${count.index}"
  instance_template  = "${google_compute_instance_template.foobar.self_link}"
  base_instance_name = "foobar-${count.index}"
  zone               = "${data.google_compute_zones.available.names[count.index]}"
  target_size        = 1
}
```

<h2 class="pdoc-module-header" id="AddressArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L145">interface AddressArgs</a>
</h2>

The set of arguments for constructing a Address resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L151">property address</a>
</h3>

```typescript
address?: pulumi.Input<string>;
```


The IP address to reserve. An address may only be
specified for INTERNAL address types. The IP address must be inside the
specified subnetwork, if any.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L157">property addressType</a>
</h3>

```typescript
addressType?: pulumi.Input<string>;
```


The Address Type that should be configured.
Specify INTERNAL to reserve an internal static IP address EXTERNAL to
specify an external static IP address. Defaults to EXTERNAL if omitted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L162">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L167">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L172">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The Region in which the created address should reside.
If it is not provided, the provider region is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L178">property subnetwork</a>
</h3>

```typescript
subnetwork?: pulumi.Input<string>;
```


The self link URI of the subnetwork in which to
create the address. A subnetwork may only be specified for INTERNAL
address types.

<h2 class="pdoc-module-header" id="AddressState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L102">interface AddressState</a>
</h2>

Input properties used for looking up and filtering Address resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L108">property address</a>
</h3>

```typescript
address?: pulumi.Input<string>;
```


The IP address to reserve. An address may only be
specified for INTERNAL address types. The IP address must be inside the
specified subnetwork, if any.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L114">property addressType</a>
</h3>

```typescript
addressType?: pulumi.Input<string>;
```


The Address Type that should be configured.
Specify INTERNAL to reserve an internal static IP address EXTERNAL to
specify an external static IP address. Defaults to EXTERNAL if omitted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L119">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L124">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L129">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The Region in which the created address should reside.
If it is not provided, the provider region is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L133">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/address.ts#L139">property subnetwork</a>
</h3>

```typescript
subnetwork?: pulumi.Input<string>;
```


The self link URI of the subnetwork in which to
create the address. A subnetwork may only be specified for INTERNAL
address types.

<h2 class="pdoc-module-header" id="AutoscalarArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L149">interface AutoscalarArgs</a>
</h2>

The set of arguments for constructing a Autoscalar resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L154">property autoscalingPolicy</a>
</h3>

```typescript
autoscalingPolicy: pulumi.Input<{ ... }>;
```


The parameters of the autoscaling
algorithm. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L159">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


An optional textual description of the instance
group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L164">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Google Cloud Monitoring metric to follow, e.g.
`compute.googleapis.com/instance/network/received_bytes_count`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L169">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L176">property target</a>
</h3>

```typescript
target: pulumi.Input<string>;
```


The floating point threshold where load balancing utilization
should be. E.g. if the load balancer's `maxRatePerInstance` is 10 requests
per second (RPS) then setting this to 0.5 would cause the group to be scaled
such that each instance receives 5 RPS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L180">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone of the target.

<h2 class="pdoc-module-header" id="AutoscalarState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L108">interface AutoscalarState</a>
</h2>

Input properties used for looking up and filtering Autoscalar resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L113">property autoscalingPolicy</a>
</h3>

```typescript
autoscalingPolicy?: pulumi.Input<{ ... }>;
```


The parameters of the autoscaling
algorithm. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L118">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


An optional textual description of the instance
group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L123">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Google Cloud Monitoring metric to follow, e.g.
`compute.googleapis.com/instance/network/received_bytes_count`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L128">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L132">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URL of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L139">property target</a>
</h3>

```typescript
target?: pulumi.Input<string>;
```


The floating point threshold where load balancing utilization
should be. E.g. if the load balancer's `maxRatePerInstance` is 10 requests
per second (RPS) then setting this to 0.5 would cause the group to be scaled
such that each instance receives 5 RPS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/autoscalar.ts#L143">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone of the target.

<h2 class="pdoc-module-header" id="BackendBucketArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L93">interface BackendBucketArgs</a>
</h2>

The set of arguments for constructing a BackendBucket resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L94">property bucketName</a>
</h3>

```typescript
bucketName: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L95">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L96">property enableCdn</a>
</h3>

```typescript
enableCdn?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L97">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L102">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="BackendBucketState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L73">interface BackendBucketState</a>
</h2>

Input properties used for looking up and filtering BackendBucket resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L74">property bucketName</a>
</h3>

```typescript
bucketName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L75">property creationTimestamp</a>
</h3>

```typescript
creationTimestamp?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L76">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L77">property enableCdn</a>
</h3>

```typescript
enableCdn?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L78">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L83">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendBucket.ts#L87">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h2 class="pdoc-module-header" id="BackendServiceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L238">interface BackendServiceArgs</a>
</h2>

The set of arguments for constructing a BackendService resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L242">property backends</a>
</h3>

```typescript
backends?: pulumi.Input<{ ... }[]>;
```


The list of backends that serve this BackendService. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L246">property cdnPolicy</a>
</h3>

```typescript
cdnPolicy?: pulumi.Input<{ ... }>;
```


Cloud CDN configuration for this BackendService. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L251">property connectionDrainingTimeoutSec</a>
</h3>

```typescript
connectionDrainingTimeoutSec?: pulumi.Input<number>;
```


Time for which instance will be drained (not accept new connections,
but still work to finish started ones). Defaults to `300`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L255">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Textual description for the backend.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L259">property enableCdn</a>
</h3>

```typescript
enableCdn?: pulumi.Input<boolean>;
```


Whether or not to enable the Cloud CDN on the backend service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L265">property healthChecks</a>
</h3>

```typescript
healthChecks: pulumi.Input<pulumi.Input<string>>;
```


Specifies a list of HTTP/HTTPS health checks
for checking the health of the backend service. Currently at most one health
check can be specified, and a health check is required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L269">property iap</a>
</h3>

```typescript
iap?: pulumi.Input<{ ... }>;
```


Specification for the Identity-Aware proxy. Disabled if not specified. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L273">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the backend service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L278">property portName</a>
</h3>

```typescript
portName?: pulumi.Input<string>;
```


The name of a service that has been added to an
instance group in this backend. See [related docs](https://cloud.google.com/compute/docs/instance-groups/#specifying_service_endpoints) for details. Defaults to http.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L283">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L288">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The protocol for incoming requests. Defaults to
`HTTP`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L293">property securityPolicy</a>
</h3>

```typescript
securityPolicy?: pulumi.Input<string>;
```


) Name or URI of a
[security policy](https://cloud.google.com/armor/docs/security-policy-concepts) to add to the backend service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L299">property sessionAffinity</a>
</h3>

```typescript
sessionAffinity?: pulumi.Input<string>;
```


How to distribute load. Options are `NONE` (no
affinity), `CLIENT_IP` (hash of the source/dest addresses / ports), and
`GENERATED_COOKIE` (distribute load using a generated session cookie).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L304">property timeoutSec</a>
</h3>

```typescript
timeoutSec?: pulumi.Input<number>;
```


The number of secs to wait for a backend to respond
to a request before considering the request failed. Defaults to `30`.

<h2 class="pdoc-module-header" id="BackendServiceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L158">interface BackendServiceState</a>
</h2>

Input properties used for looking up and filtering BackendService resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L162">property backends</a>
</h3>

```typescript
backends?: pulumi.Input<{ ... }[]>;
```


The list of backends that serve this BackendService. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L166">property cdnPolicy</a>
</h3>

```typescript
cdnPolicy?: pulumi.Input<{ ... }>;
```


Cloud CDN configuration for this BackendService. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L171">property connectionDrainingTimeoutSec</a>
</h3>

```typescript
connectionDrainingTimeoutSec?: pulumi.Input<number>;
```


Time for which instance will be drained (not accept new connections,
but still work to finish started ones). Defaults to `300`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L175">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Textual description for the backend.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L179">property enableCdn</a>
</h3>

```typescript
enableCdn?: pulumi.Input<boolean>;
```


Whether or not to enable the Cloud CDN on the backend service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L183">property fingerprint</a>
</h3>

```typescript
fingerprint?: pulumi.Input<string>;
```


The fingerprint of the backend service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L189">property healthChecks</a>
</h3>

```typescript
healthChecks?: pulumi.Input<pulumi.Input<string>>;
```


Specifies a list of HTTP/HTTPS health checks
for checking the health of the backend service. Currently at most one health
check can be specified, and a health check is required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L193">property iap</a>
</h3>

```typescript
iap?: pulumi.Input<{ ... }>;
```


Specification for the Identity-Aware proxy. Disabled if not specified. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L197">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the backend service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L202">property portName</a>
</h3>

```typescript
portName?: pulumi.Input<string>;
```


The name of a service that has been added to an
instance group in this backend. See [related docs](https://cloud.google.com/compute/docs/instance-groups/#specifying_service_endpoints) for details. Defaults to http.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L207">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L212">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The protocol for incoming requests. Defaults to
`HTTP`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L217">property securityPolicy</a>
</h3>

```typescript
securityPolicy?: pulumi.Input<string>;
```


) Name or URI of a
[security policy](https://cloud.google.com/armor/docs/security-policy-concepts) to add to the backend service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L221">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L227">property sessionAffinity</a>
</h3>

```typescript
sessionAffinity?: pulumi.Input<string>;
```


How to distribute load. Options are `NONE` (no
affinity), `CLIENT_IP` (hash of the source/dest addresses / ports), and
`GENERATED_COOKIE` (distribute load using a generated session cookie).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/backendService.ts#L232">property timeoutSec</a>
</h3>

```typescript
timeoutSec?: pulumi.Input<number>;
```


The number of secs to wait for a backend to respond
to a request before considering the request failed. Defaults to `30`.

<h2 class="pdoc-module-header" id="DiskArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L221">interface DiskArgs</a>
</h2>

The set of arguments for constructing a Disk resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L228">property diskEncryptionKeyRaw</a>
</h3>

```typescript
diskEncryptionKeyRaw?: pulumi.Input<string>;
```


A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L240">property image</a>
</h3>

```typescript
image?: pulumi.Input<string>;
```


The image from which to initialize this disk. This can be
one of: the image's `self_link`, `projects/{project}/global/images/{image}`,
`projects/{project}/global/images/family/{family}`, `global/images/{image}`,
`global/images/family/{family}`, `family/{family}`, `{project}/{family}`,
`{project}/{image}`, `{family}`, or `{image}`. If referred by family, the
images names must include the family name. If they don't, use the
[google_compute_image data source](/docs/providers/google/d/datasource_compute_image.html).
For instance, the image `centos-6-v20180104` includes its family name `centos-6`.
These images can be referred by family name here.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L244">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A set of key/value label pairs to assign to the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L249">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L254">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L259">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```


The size of the image in gigabytes. If not specified, it
will inherit the size of its base image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L263">property snapshot</a>
</h3>

```typescript
snapshot?: pulumi.Input<string>;
```


Name of snapshot from which to initialize this disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L267">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The GCE disk type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L271">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone where this disk will be available.

<h2 class="pdoc-module-header" id="DiskState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L146">interface DiskState</a>
</h2>

Input properties used for looking up and filtering Disk resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L153">property diskEncryptionKeyRaw</a>
</h3>

```typescript
diskEncryptionKeyRaw?: pulumi.Input<string>;
```


A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L160">property diskEncryptionKeySha256</a>
</h3>

```typescript
diskEncryptionKeySha256?: pulumi.Input<string>;
```


The [RFC 4648 base64]
(https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the
[customer-supplied encryption key](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
that protects this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L172">property image</a>
</h3>

```typescript
image?: pulumi.Input<string>;
```


The image from which to initialize this disk. This can be
one of: the image's `self_link`, `projects/{project}/global/images/{image}`,
`projects/{project}/global/images/family/{family}`, `global/images/{image}`,
`global/images/family/{family}`, `family/{family}`, `{project}/{family}`,
`{project}/{image}`, `{family}`, or `{image}`. If referred by family, the
images names must include the family name. If they don't, use the
[google_compute_image data source](/docs/providers/google/d/datasource_compute_image.html).
For instance, the image `centos-6-v20180104` includes its family name `centos-6`.
These images can be referred by family name here.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L176">property labelFingerprint</a>
</h3>

```typescript
labelFingerprint?: pulumi.Input<string>;
```


The fingerprint of the assigned labels.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L180">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A set of key/value label pairs to assign to the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L185">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L190">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L194">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L199">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```


The size of the image in gigabytes. If not specified, it
will inherit the size of its base image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L203">property snapshot</a>
</h3>

```typescript
snapshot?: pulumi.Input<string>;
```


Name of snapshot from which to initialize this disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L207">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The GCE disk type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L211">property users</a>
</h3>

```typescript
users?: pulumi.Input<pulumi.Input<string>[]>;
```


The Users of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/disk.ts#L215">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone where this disk will be available.

<h2 class="pdoc-module-header" id="FirewallArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L249">interface FirewallArgs</a>
</h2>

The set of arguments for constructing a Firewall resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L254">property allows</a>
</h3>

```typescript
allows?: pulumi.Input<{ ... }[]>;
```


Can be specified multiple times for each allow
rule. Each allow block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L260">property denies</a>
</h3>

```typescript
denies?: pulumi.Input<{ ... }[]>;
```


Can be specified multiple times for each deny
rule. Each deny block supports fields documented below. Can be specified
instead of allow.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L264">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Textual description field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L269">property destinationRanges</a>
</h3>

```typescript
destinationRanges?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of destination CIDR ranges that this
firewall applies to. Can't be used for `INGRESS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L274">property direction</a>
</h3>

```typescript
direction?: pulumi.Input<string>;
```


Direction of traffic to which this firewall applies;
One of `INGRESS` or `EGRESS`. Defaults to `INGRESS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L279">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L283">property network</a>
</h3>

```typescript
network: pulumi.Input<string>;
```


The name or self_link of the network to attach this firewall to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L289">property priority</a>
</h3>

```typescript
priority?: pulumi.Input<number>;
```


The priority for this firewall. Ranges from 0-65535, inclusive. Defaults to 1000. Firewall
resources with lower priority values have higher precedence (e.g. a firewall resource with a priority value of 0
takes effect over all other firewall rules with a non-zero priority).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L294">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L299">property sourceRanges</a>
</h3>

```typescript
sourceRanges?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of source CIDR ranges that this
firewall applies to. Can't be used for `EGRESS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L310">property sourceServiceAccounts</a>
</h3>

```typescript
sourceServiceAccounts?: pulumi.Input<pulumi.Input<string>>;
```


A list of service accounts such that
the firewall will apply only to traffic originating from an instance with a service account in this list.  Note that as of May 2018,
this list can contain only one item, due to a change in the way that these firewall rules are handled.  Source service accounts
cannot be used to control traffic to an instance's external IP address because service accounts are associated with an instance, not
an IP address. `source_ranges` can be set at the same time as `source_service_accounts`. If both are set, the firewall will apply to
traffic that has source IP address within `source_ranges` OR the source IP belongs to an instance with service account listed in
`source_service_accounts`. The connection does not need to match both properties for the firewall to apply. `source_service_accounts`
cannot be used at the same time as `source_tags` or `target_tags`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L314">property sourceTags</a>
</h3>

```typescript
sourceTags?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of source tags for this firewall. Can't be used for `EGRESS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L322">property targetServiceAccounts</a>
</h3>

```typescript
targetServiceAccounts?: pulumi.Input<pulumi.Input<string>>;
```


A list of service accounts indicating
sets of instances located in the network that may make network connections as specified in `allow`. `target_service_accounts` cannot
be used at the same time as `source_tags` or `target_tags`. If neither `target_service_accounts` nor `target_tags` are specified, the
firewall rule applies to all instances on the specified network.  Note that as of May 2018, this list can contain only one item, due
to a change in the way that these firewall rules are handled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L326">property targetTags</a>
</h3>

```typescript
targetTags?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of target tags for this firewall.

<h2 class="pdoc-module-header" id="FirewallState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L162">interface FirewallState</a>
</h2>

Input properties used for looking up and filtering Firewall resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L167">property allows</a>
</h3>

```typescript
allows?: pulumi.Input<{ ... }[]>;
```


Can be specified multiple times for each allow
rule. Each allow block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L173">property denies</a>
</h3>

```typescript
denies?: pulumi.Input<{ ... }[]>;
```


Can be specified multiple times for each deny
rule. Each deny block supports fields documented below. Can be specified
instead of allow.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L177">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Textual description field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L182">property destinationRanges</a>
</h3>

```typescript
destinationRanges?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of destination CIDR ranges that this
firewall applies to. Can't be used for `INGRESS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L187">property direction</a>
</h3>

```typescript
direction?: pulumi.Input<string>;
```


Direction of traffic to which this firewall applies;
One of `INGRESS` or `EGRESS`. Defaults to `INGRESS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L192">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L196">property network</a>
</h3>

```typescript
network?: pulumi.Input<string>;
```


The name or self_link of the network to attach this firewall to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L202">property priority</a>
</h3>

```typescript
priority?: pulumi.Input<number>;
```


The priority for this firewall. Ranges from 0-65535, inclusive. Defaults to 1000. Firewall
resources with lower priority values have higher precedence (e.g. a firewall resource with a priority value of 0
takes effect over all other firewall rules with a non-zero priority).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L207">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L211">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L216">property sourceRanges</a>
</h3>

```typescript
sourceRanges?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of source CIDR ranges that this
firewall applies to. Can't be used for `EGRESS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L227">property sourceServiceAccounts</a>
</h3>

```typescript
sourceServiceAccounts?: pulumi.Input<pulumi.Input<string>>;
```


A list of service accounts such that
the firewall will apply only to traffic originating from an instance with a service account in this list.  Note that as of May 2018,
this list can contain only one item, due to a change in the way that these firewall rules are handled.  Source service accounts
cannot be used to control traffic to an instance's external IP address because service accounts are associated with an instance, not
an IP address. `source_ranges` can be set at the same time as `source_service_accounts`. If both are set, the firewall will apply to
traffic that has source IP address within `source_ranges` OR the source IP belongs to an instance with service account listed in
`source_service_accounts`. The connection does not need to match both properties for the firewall to apply. `source_service_accounts`
cannot be used at the same time as `source_tags` or `target_tags`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L231">property sourceTags</a>
</h3>

```typescript
sourceTags?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of source tags for this firewall. Can't be used for `EGRESS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L239">property targetServiceAccounts</a>
</h3>

```typescript
targetServiceAccounts?: pulumi.Input<pulumi.Input<string>>;
```


A list of service accounts indicating
sets of instances located in the network that may make network connections as specified in `allow`. `target_service_accounts` cannot
be used at the same time as `source_tags` or `target_tags`. If neither `target_service_accounts` nor `target_tags` are specified, the
firewall rule applies to all instances on the specified network.  Note that as of May 2018, this list can contain only one item, due
to a change in the way that these firewall rules are handled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/firewall.ts#L243">property targetTags</a>
</h3>

```typescript
targetTags?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of target tags for this firewall.

<h2 class="pdoc-module-header" id="ForwardingRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L238">interface ForwardingRuleArgs</a>
</h2>

The set of arguments for constructing a ForwardingRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L243">property backendService</a>
</h3>

```typescript
backendService?: pulumi.Input<string>;
```


BackendService resource to receive the
matched traffic. Only used for internal load balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L247">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Textual description field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L252">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The static IP. (if not set, an ephemeral IP is
used).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L258">property ipProtocol</a>
</h3>

```typescript
ipProtocol?: pulumi.Input<string>;
```


The IP protocol to route, one of "TCP" "UDP" "AH"
"ESP" or "SCTP" for external load balancing, "TCP" or "UDP" for internal
(default "TCP").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L263">property loadBalancingScheme</a>
</h3>

```typescript
loadBalancingScheme?: pulumi.Input<string>;
```


Type of load balancing to use. Can be
set to "INTERNAL" or "EXTERNAL" (default "EXTERNAL").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L268">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L274">property network</a>
</h3>

```typescript
network?: pulumi.Input<string>;
```


Network name or self_link that the load balanced IP
should belong to. Only used for internal load balancing. If it is not
provided, the default network is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L285">property portRange</a>
</h3>

```typescript
portRange?: pulumi.Input<string>;
```


A range e.g. "1024-2048" or a single port "1024"
(defaults to all ports!). Only used for external load balancing.
Some types of forwarding targets have constraints on the acceptable ports:
* Target HTTP proxy: 80, 8080
* Target HTTPS proxy: 443
* Target TCP proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
* Target SSL proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
* Target VPN gateway: 500, 4500

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L291">property ports</a>
</h3>

```typescript
ports?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of ports (maximum of 5) to use for internal load
balancing. Packets addressed to these ports will be forwarded to the backends
configured with this forwarding rule. Required for internal load balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L296">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L301">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The Region in which the created address should reside.
If it is not provided, the provider region is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L307">property subnetwork</a>
</h3>

```typescript
subnetwork?: pulumi.Input<string>;
```


Subnetwork that the load balanced IP should belong
to. Only used for internal load balancing. Must be specified if the network
is in custom subnet mode.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L312">property target</a>
</h3>

```typescript
target?: pulumi.Input<string>;
```


URL of target pool. Required for external load
balancing.

<h2 class="pdoc-module-header" id="ForwardingRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L154">interface ForwardingRuleState</a>
</h2>

Input properties used for looking up and filtering ForwardingRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L159">property backendService</a>
</h3>

```typescript
backendService?: pulumi.Input<string>;
```


BackendService resource to receive the
matched traffic. Only used for internal load balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L163">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Textual description field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L168">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The static IP. (if not set, an ephemeral IP is
used).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L174">property ipProtocol</a>
</h3>

```typescript
ipProtocol?: pulumi.Input<string>;
```


The IP protocol to route, one of "TCP" "UDP" "AH"
"ESP" or "SCTP" for external load balancing, "TCP" or "UDP" for internal
(default "TCP").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L179">property loadBalancingScheme</a>
</h3>

```typescript
loadBalancingScheme?: pulumi.Input<string>;
```


Type of load balancing to use. Can be
set to "INTERNAL" or "EXTERNAL" (default "EXTERNAL").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L184">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L190">property network</a>
</h3>

```typescript
network?: pulumi.Input<string>;
```


Network name or self_link that the load balanced IP
should belong to. Only used for internal load balancing. If it is not
provided, the default network is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L201">property portRange</a>
</h3>

```typescript
portRange?: pulumi.Input<string>;
```


A range e.g. "1024-2048" or a single port "1024"
(defaults to all ports!). Only used for external load balancing.
Some types of forwarding targets have constraints on the acceptable ports:
* Target HTTP proxy: 80, 8080
* Target HTTPS proxy: 443
* Target TCP proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
* Target SSL proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
* Target VPN gateway: 500, 4500

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L207">property ports</a>
</h3>

```typescript
ports?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of ports (maximum of 5) to use for internal load
balancing. Packets addressed to these ports will be forwarded to the backends
configured with this forwarding rule. Required for internal load balancing.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L212">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L217">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The Region in which the created address should reside.
If it is not provided, the provider region is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L221">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L227">property subnetwork</a>
</h3>

```typescript
subnetwork?: pulumi.Input<string>;
```


Subnetwork that the load balanced IP should belong
to. Only used for internal load balancing. Must be specified if the network
is in custom subnet mode.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/forwardingRule.ts#L232">property target</a>
</h3>

```typescript
target?: pulumi.Input<string>;
```


URL of target pool. Required for external load
balancing.

<h2 class="pdoc-module-header" id="GetAddressArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getAddress.ts#L21">interface GetAddressArgs</a>
</h2>

A collection of arguments for invoking getAddress.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getAddress.ts#L25">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getAddress.ts#L30">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getAddress.ts#L35">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The Region in which the created address reside.
If it is not provided, the provider region is used.

<h2 class="pdoc-module-header" id="GetAddressResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getAddress.ts#L41">interface GetAddressResult</a>
</h2>

A collection of values returned by getAddress.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getAddress.ts#L45">property address</a>
</h3>

```typescript
address: string;
```


The IP of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getAddress.ts#L46">property project</a>
</h3>

```typescript
project: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getAddress.ts#L47">property region</a>
</h3>

```typescript
region: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getAddress.ts#L51">property selfLink</a>
</h3>

```typescript
selfLink: string;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getAddress.ts#L55">property status</a>
</h3>

```typescript
status: string;
```


Indicates if the address is used. Possible values are: RESERVED or IN_USE.

<h2 class="pdoc-module-header" id="GetBackendServiceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L21">interface GetBackendServiceArgs</a>
</h2>

A collection of arguments for invoking getBackendService.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L25">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The name of the Backend Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L29">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="GetBackendServiceResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L35">interface GetBackendServiceResult</a>
</h2>

A collection of values returned by getBackendService.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L39">property backends</a>
</h3>

```typescript
backends: { ... }[];
```


The list of backends that serve this Backend Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L40">property cdnPolicies</a>
</h3>

```typescript
cdnPolicies: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L44">property connectionDrainingTimeoutSec</a>
</h3>

```typescript
connectionDrainingTimeoutSec: number;
```


Time for which instance will be drained (not accept new connections, but still work to finish started ones).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L48">property description</a>
</h3>

```typescript
description: string;
```


Textual description for the Backend Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L52">property enableCdn</a>
</h3>

```typescript
enableCdn: boolean;
```


Whether or not Cloud CDN is enabled on the Backend Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L56">property fingerprint</a>
</h3>

```typescript
fingerprint: string;
```


The fingerprint of the Backend Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L60">property healthChecks</a>
</h3>

```typescript
healthChecks: string[];
```


The list of HTTP/HTTPS health checks used by the Backend Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L61">property iaps</a>
</h3>

```typescript
iaps: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L65">property portName</a>
</h3>

```typescript
portName: string;
```


The name of a service that has been added to an instance group in this backend.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L69">property protocol</a>
</h3>

```typescript
protocol: string;
```


The protocol for incoming requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L70">property region</a>
</h3>

```typescript
region: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L71">property securityPolicy</a>
</h3>

```typescript
securityPolicy: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L75">property selfLink</a>
</h3>

```typescript
selfLink: string;
```


The URI of the Backend Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L79">property sessionAffinity</a>
</h3>

```typescript
sessionAffinity: string;
```


The Backend Service session stickyness configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getBackendService.ts#L83">property timeoutSec</a>
</h3>

```typescript
timeoutSec: number;
```


The number of seconds to wait for a backend to respond to a request before considering the request failed.

<h2 class="pdoc-module-header" id="GetDefaultServiceAccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getDefaultServiceAccount.ts#L20">interface GetDefaultServiceAccountArgs</a>
</h2>

A collection of arguments for invoking getDefaultServiceAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getDefaultServiceAccount.ts#L21">property email</a>
</h3>

```typescript
email?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getDefaultServiceAccount.ts#L25">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project ID. If it is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="GetForwardingRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L20">interface GetForwardingRuleArgs</a>
</h2>

A collection of arguments for invoking getForwardingRule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L24">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The name of the forwarding rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L29">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L34">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which the resource belongs. If it
is not provided, the project region is used.

<h2 class="pdoc-module-header" id="GetForwardingRuleResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L40">interface GetForwardingRuleResult</a>
</h2>

A collection of values returned by getForwardingRule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L44">property backendService</a>
</h3>

```typescript
backendService: string;
```


Backend service, if this forwarding rule has one.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L48">property description</a>
</h3>

```typescript
description: string;
```


Description of this forwarding rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L52">property ipAddress</a>
</h3>

```typescript
ipAddress: string;
```


IP address of this forwarding rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L56">property ipProtocol</a>
</h3>

```typescript
ipProtocol: string;
```


IP protocol of this forwarding rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L60">property loadBalancingScheme</a>
</h3>

```typescript
loadBalancingScheme: string;
```


Type of load balancing of this forwarding rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L64">property network</a>
</h3>

```typescript
network: string;
```


Network of this forwarding rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L68">property portRange</a>
</h3>

```typescript
portRange: string;
```


Port range, if this forwarding rule has one.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L72">property ports</a>
</h3>

```typescript
ports: string[];
```


List of ports to use for internal load balancing, if this forwarding rule has any.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L73">property project</a>
</h3>

```typescript
project: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L77">property region</a>
</h3>

```typescript
region: string;
```


Region of this forwarding rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L81">property selfLink</a>
</h3>

```typescript
selfLink: string;
```


The URI of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L85">property subnetwork</a>
</h3>

```typescript
subnetwork: string;
```


Subnetwork of this forwarding rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getForwardingRule.ts#L89">property target</a>
</h3>

```typescript
target: string;
```


URL of the target pool, if this forwarding rule has one.

<h2 class="pdoc-module-header" id="GetGlobalAddressArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getGlobalAddress.ts#L20">interface GetGlobalAddressArgs</a>
</h2>

A collection of arguments for invoking getGlobalAddress.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getGlobalAddress.ts#L24">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getGlobalAddress.ts#L29">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="GetGlobalAddressResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getGlobalAddress.ts#L35">interface GetGlobalAddressResult</a>
</h2>

A collection of values returned by getGlobalAddress.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getGlobalAddress.ts#L39">property address</a>
</h3>

```typescript
address: string;
```


The IP of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getGlobalAddress.ts#L40">property project</a>
</h3>

```typescript
project: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getGlobalAddress.ts#L44">property selfLink</a>
</h3>

```typescript
selfLink: string;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getGlobalAddress.ts#L48">property status</a>
</h3>

```typescript
status: string;
```


Indicates if the address is used. Possible values are: RESERVED or IN_USE.

<h2 class="pdoc-module-header" id="GetImageArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L22">interface GetImageArgs</a>
</h2>

A collection of arguments for invoking getImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L23">property family</a>
</h3>

```typescript
family?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L24">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L30">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it is not
provided, the provider project is used. If you are using a
[public base image][pubimg], be sure to specify the correct Image Project.

<h2 class="pdoc-module-header" id="GetImageResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L36">interface GetImageResult</a>
</h2>

A collection of values returned by getImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L40">property archiveSizeBytes</a>
</h3>

```typescript
archiveSizeBytes: number;
```


The size of the image tar.gz archive stored in Google Cloud Storage in bytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L44">property creationTimestamp</a>
</h3>

```typescript
creationTimestamp: string;
```


The creation timestamp in RFC3339 text format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L48">property description</a>
</h3>

```typescript
description: string;
```


An optional description of this image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L52">property diskSizeGb</a>
</h3>

```typescript
diskSizeGb: number;
```


The size of the image when restored onto a persistent disk in gigabytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L56">property family</a>
</h3>

```typescript
family: string;
```


The family name of the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L62">property imageEncryptionKeySha256</a>
</h3>

```typescript
imageEncryptionKeySha256: string;
```


The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
encoded SHA-256 hash of the [customer-supplied encryption key](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
that protects this image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L66">property imageId</a>
</h3>

```typescript
imageId: string;
```


The unique identifier for the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L70">property labelFingerprint</a>
</h3>

```typescript
labelFingerprint: string;
```


A fingerprint for the labels being applied to this image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L74">property labels</a>
</h3>

```typescript
labels: { ... };
```


A map of labels applied to this image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L78">property licenses</a>
</h3>

```typescript
licenses: string[];
```


A list of applicable license URI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L82">property name</a>
</h3>

```typescript
name: string;
```


The name of the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L83">property project</a>
</h3>

```typescript
project: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L87">property selfLink</a>
</h3>

```typescript
selfLink: string;
```


The URI of the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L91">property sourceDisk</a>
</h3>

```typescript
sourceDisk: string;
```


The URL of the source disk used to create this image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L97">property sourceDiskEncryptionKeySha256</a>
</h3>

```typescript
sourceDiskEncryptionKeySha256: string;
```


The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
encoded SHA-256 hash of the [customer-supplied encryption key](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
that protects this image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L101">property sourceDiskId</a>
</h3>

```typescript
sourceDiskId: string;
```


The ID value of the disk used to create this image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L105">property sourceImageId</a>
</h3>

```typescript
sourceImageId: string;
```


The ID value of the image used to create this image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getImage.ts#L109">property status</a>
</h3>

```typescript
status: string;
```


The status of the image. Possible values are **FAILED**, **PENDING**, or **READY**.

<h2 class="pdoc-module-header" id="GetInstanceGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getInstanceGroup.ts#L31">interface GetInstanceGroupArgs</a>
</h2>

A collection of arguments for invoking getInstanceGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getInstanceGroup.ts#L35">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the instance group. Either `name` or `self_link` must be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getInstanceGroup.ts#L40">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getInstanceGroup.ts#L44">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The self link of the instance group. Either `name` or `self_link` must be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getInstanceGroup.ts#L49">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone of the instance group. If referencing the instance group by name
and `zone` is not provided, the provider zone is used.

<h2 class="pdoc-module-header" id="GetInstanceGroupResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getInstanceGroup.ts#L55">interface GetInstanceGroupResult</a>
</h2>

A collection of values returned by getInstanceGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getInstanceGroup.ts#L59">property description</a>
</h3>

```typescript
description: string;
```


Textual description of the instance group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getInstanceGroup.ts#L63">property instances</a>
</h3>

```typescript
instances: string[];
```


List of instances in the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getInstanceGroup.ts#L67">property namedPorts</a>
</h3>

```typescript
namedPorts: { ... }[];
```


List of named ports in the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getInstanceGroup.ts#L71">property network</a>
</h3>

```typescript
network: string;
```


The URL of the network the instance group is in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getInstanceGroup.ts#L72">property project</a>
</h3>

```typescript
project: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getInstanceGroup.ts#L76">property selfLink</a>
</h3>

```typescript
selfLink: string;
```


The URI of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getInstanceGroup.ts#L80">property size</a>
</h3>

```typescript
size: number;
```


The number of instances in the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getInstanceGroup.ts#L81">property zone</a>
</h3>

```typescript
zone: string;
```

<h2 class="pdoc-module-header" id="GetLBIPRangesResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getLBIPRanges.ts#L19">interface GetLBIPRangesResult</a>
</h2>

A collection of values returned by getLBIPRanges.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getLBIPRanges.ts#L23">property httpSslTcpInternals</a>
</h3>

```typescript
httpSslTcpInternals: string[];
```


The IP ranges used for health checks when **HTTP(S), SSL proxy, TCP proxy, and Internal load balancing** is used

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getLBIPRanges.ts#L27">property networks</a>
</h3>

```typescript
networks: string[];
```


The IP ranges used for health checks when **Network load balancing** is used

<h2 class="pdoc-module-header" id="GetNetworkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getNetwork.ts#L19">interface GetNetworkArgs</a>
</h2>

A collection of arguments for invoking getNetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getNetwork.ts#L23">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The name of the network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getNetwork.ts#L28">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="GetNetworkResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getNetwork.ts#L34">interface GetNetworkResult</a>
</h2>

A collection of values returned by getNetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getNetwork.ts#L38">property description</a>
</h3>

```typescript
description: string;
```


Description of this network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getNetwork.ts#L42">property gatewayIpv4</a>
</h3>

```typescript
gatewayIpv4: string;
```


The IP address of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getNetwork.ts#L46">property selfLink</a>
</h3>

```typescript
selfLink: string;
```


The URI of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getNetwork.ts#L50">property subnetworksSelfLinks</a>
</h3>

```typescript
subnetworksSelfLinks: string[];
```


the list of subnetworks which belong to the network

<h2 class="pdoc-module-header" id="GetRegionInstanceGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getRegionInstanceGroup.ts#L48">interface GetRegionInstanceGroupArgs</a>
</h2>

A collection of arguments for invoking getRegionInstanceGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getRegionInstanceGroup.ts#L52">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the instance group.  One of `name` or `self_link` must be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getRegionInstanceGroup.ts#L57">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getRegionInstanceGroup.ts#L63">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which the resource belongs.  If `self_link`
is provided, this value is ignored.  If neither `self_link` nor `region` are
provided, the provider region is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getRegionInstanceGroup.ts#L67">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The link to the instance group.  One of `name` or `self_link` must be provided.

<h2 class="pdoc-module-header" id="GetRegionInstanceGroupResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getRegionInstanceGroup.ts#L73">interface GetRegionInstanceGroupResult</a>
</h2>

A collection of values returned by getRegionInstanceGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getRegionInstanceGroup.ts#L77">property instances</a>
</h3>

```typescript
instances: { ... }[];
```


List of instances in the group, as a list of resources, each containing:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getRegionInstanceGroup.ts#L81">property name</a>
</h3>

```typescript
name: string;
```


String port name

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getRegionInstanceGroup.ts#L82">property project</a>
</h3>

```typescript
project: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getRegionInstanceGroup.ts#L83">property region</a>
</h3>

```typescript
region: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getRegionInstanceGroup.ts#L84">property selfLink</a>
</h3>

```typescript
selfLink: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getRegionInstanceGroup.ts#L88">property size</a>
</h3>

```typescript
size: number;
```


The number of instances in the group.

<h2 class="pdoc-module-header" id="GetSubnetworkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getSubnetwork.ts#L20">interface GetSubnetworkArgs</a>
</h2>

A collection of arguments for invoking getSubnetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getSubnetwork.ts#L24">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The name of the subnetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getSubnetwork.ts#L29">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getSubnetwork.ts#L34">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region this subnetwork has been created in. If
unspecified, this defaults to the region configured in the provider.

<h2 class="pdoc-module-header" id="GetSubnetworkResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getSubnetwork.ts#L40">interface GetSubnetworkResult</a>
</h2>

A collection of values returned by getSubnetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getSubnetwork.ts#L44">property description</a>
</h3>

```typescript
description: string;
```


Description of this subnetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getSubnetwork.ts#L48">property gatewayAddress</a>
</h3>

```typescript
gatewayAddress: string;
```


The IP address of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getSubnetwork.ts#L53">property ipCidrRange</a>
</h3>

```typescript
ipCidrRange: string;
```


The range of IP addresses belonging to this subnetwork
secondary range.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getSubnetwork.ts#L58">property network</a>
</h3>

```typescript
network: string;
```


The network name or resource link to the parent
network of this subnetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getSubnetwork.ts#L64">property privateIpGoogleAccess</a>
</h3>

```typescript
privateIpGoogleAccess: boolean;
```


Whether the VMs in this subnet
can access Google services without assigned external IP
addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getSubnetwork.ts#L65">property project</a>
</h3>

```typescript
project: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getSubnetwork.ts#L66">property region</a>
</h3>

```typescript
region: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getSubnetwork.ts#L71">property secondaryIpRanges</a>
</h3>

```typescript
secondaryIpRanges: { ... }[];
```


An array of configurations for secondary IP ranges for
VM instances contained in this subnetwork. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getSubnetwork.ts#L75">property selfLink</a>
</h3>

```typescript
selfLink: string;
```


The URI of the created resource.

<h2 class="pdoc-module-header" id="GetVPNGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getVPNGateway.ts#L20">interface GetVPNGatewayArgs</a>
</h2>

A collection of arguments for invoking getVPNGateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getVPNGateway.ts#L24">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The name of the VPN gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getVPNGateway.ts#L29">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getVPNGateway.ts#L34">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which the resource belongs. If it
is not provided, the project region is used.

<h2 class="pdoc-module-header" id="GetVPNGatewayResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getVPNGateway.ts#L40">interface GetVPNGatewayResult</a>
</h2>

A collection of values returned by getVPNGateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getVPNGateway.ts#L44">property description</a>
</h3>

```typescript
description: string;
```


Description of this VPN gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getVPNGateway.ts#L48">property network</a>
</h3>

```typescript
network: string;
```


The network of this VPN gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getVPNGateway.ts#L49">property project</a>
</h3>

```typescript
project: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getVPNGateway.ts#L53">property region</a>
</h3>

```typescript
region: string;
```


Region of this VPN gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getVPNGateway.ts#L57">property selfLink</a>
</h3>

```typescript
selfLink: string;
```


The URI of the resource.

<h2 class="pdoc-module-header" id="GetZonesArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getZones.ts#L36">interface GetZonesArgs</a>
</h2>

A collection of arguments for invoking getZones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getZones.ts#L40">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


Project from which to list available zones. Defaults to project declared in the provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getZones.ts#L44">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


Region from which to list available zones. Defaults to region declared in the provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getZones.ts#L49">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


Allows to filter list of zones based on their current status. Status can be either `UP` or `DOWN`.
Defaults to no filtering (all available zones - both `UP` and `DOWN`).

<h2 class="pdoc-module-header" id="GetZonesResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getZones.ts#L55">interface GetZonesResult</a>
</h2>

A collection of values returned by getZones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getZones.ts#L59">property names</a>
</h3>

```typescript
names: string[];
```


A list of zones available in the given region

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/getZones.ts#L60">property project</a>
</h3>

```typescript
project: string;
```

<h2 class="pdoc-module-header" id="GlobalAddressArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L90">interface GlobalAddressArgs</a>
</h2>

The set of arguments for constructing a GlobalAddress resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L91">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L92">property ipVersion</a>
</h3>

```typescript
ipVersion?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L93">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L98">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="GlobalAddressState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L70">interface GlobalAddressState</a>
</h2>

Input properties used for looking up and filtering GlobalAddress resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L71">property address</a>
</h3>

```typescript
address?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L72">property creationTimestamp</a>
</h3>

```typescript
creationTimestamp?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L73">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L74">property ipVersion</a>
</h3>

```typescript
ipVersion?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L75">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L80">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalAddress.ts#L84">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h2 class="pdoc-module-header" id="GlobalForwardingRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L197">interface GlobalForwardingRuleArgs</a>
</h2>

The set of arguments for constructing a GlobalForwardingRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L201">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Textual description field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L208">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The static IP. (if not set, an ephemeral IP is
used). This should be the literal IP address to be used, not the `self_link`
to a `google_compute_global_address` resource. (If using a `google_compute_global_address`
resource, use the `address` property instead of the `self_link` property.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L213">property ipProtocol</a>
</h3>

```typescript
ipProtocol?: pulumi.Input<string>;
```


The IP protocol to route, one of "TCP" "UDP" "AH"
"ESP" or "SCTP". (default "TCP").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L218">property ipVersion</a>
</h3>

```typescript
ipVersion?: pulumi.Input<string>;
```


The IP Version that will be used by this resource's address. One of `"IPV4"` or `"IPV6"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L223">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


)
A set of key/value label pairs to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L228">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L239">property portRange</a>
</h3>

```typescript
portRange?: pulumi.Input<string>;
```


A range e.g. "1024-2048" or a single port "1024"
(defaults to all ports!).
Some types of forwarding targets have constraints on the acceptable ports:
* Target HTTP proxy: 80, 8080
* Target HTTPS proxy: 443
* Target TCP proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
* Target SSL proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
* Target VPN gateway: 500, 4500

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L244">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L248">property target</a>
</h3>

```typescript
target: pulumi.Input<string>;
```


URL of target HTTP or HTTPS proxy.

<h2 class="pdoc-module-header" id="GlobalForwardingRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L132">interface GlobalForwardingRuleState</a>
</h2>

Input properties used for looking up and filtering GlobalForwardingRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L136">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Textual description field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L143">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The static IP. (if not set, an ephemeral IP is
used). This should be the literal IP address to be used, not the `self_link`
to a `google_compute_global_address` resource. (If using a `google_compute_global_address`
resource, use the `address` property instead of the `self_link` property.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L148">property ipProtocol</a>
</h3>

```typescript
ipProtocol?: pulumi.Input<string>;
```


The IP protocol to route, one of "TCP" "UDP" "AH"
"ESP" or "SCTP". (default "TCP").

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L153">property ipVersion</a>
</h3>

```typescript
ipVersion?: pulumi.Input<string>;
```


The IP Version that will be used by this resource's address. One of `"IPV4"` or `"IPV6"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L157">property labelFingerprint</a>
</h3>

```typescript
labelFingerprint?: pulumi.Input<string>;
```


([Beta](/docs/providers/google/index.html#beta-features)) The current label fingerprint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L162">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


)
A set of key/value label pairs to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L167">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L178">property portRange</a>
</h3>

```typescript
portRange?: pulumi.Input<string>;
```


A range e.g. "1024-2048" or a single port "1024"
(defaults to all ports!).
Some types of forwarding targets have constraints on the acceptable ports:
* Target HTTP proxy: 80, 8080
* Target HTTPS proxy: 443
* Target TCP proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
* Target SSL proxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222
* Target VPN gateway: 500, 4500

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L183">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L187">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/globalForwardingRule.ts#L191">property target</a>
</h3>

```typescript
target?: pulumi.Input<string>;
```


URL of target HTTP or HTTPS proxy.

<h2 class="pdoc-module-header" id="HealthCheckArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L192">interface HealthCheckArgs</a>
</h2>

The set of arguments for constructing a HealthCheck resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L197">property checkIntervalSec</a>
</h3>

```typescript
checkIntervalSec?: pulumi.Input<number>;
```


The number of seconds between each poll of
the instance instance (default 5).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L201">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Textual description field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L205">property healthyThreshold</a>
</h3>

```typescript
healthyThreshold?: pulumi.Input<number>;
```


Consecutive successes required (default 2).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L210">property httpHealthCheck</a>
</h3>

```typescript
httpHealthCheck?: pulumi.Input<{ ... }>;
```


An HTTP Health Check. Only one kind of Health Check can be added.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L215">property httpsHealthCheck</a>
</h3>

```typescript
httpsHealthCheck?: pulumi.Input<{ ... }>;
```


An HTTPS Health Check. Only one kind of Health Check can be added.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L220">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L225">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L230">property sslHealthCheck</a>
</h3>

```typescript
sslHealthCheck?: pulumi.Input<{ ... }>;
```


An SSL Health Check. Only one kind of Health Check can be added.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L235">property tcpHealthCheck</a>
</h3>

```typescript
tcpHealthCheck?: pulumi.Input<{ ... }>;
```


A TCP Health Check. Only one kind of Health Check can be added.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L240">property timeoutSec</a>
</h3>

```typescript
timeoutSec?: pulumi.Input<number>;
```


The number of seconds to wait before declaring
failure (default 5).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L244">property unhealthyThreshold</a>
</h3>

```typescript
unhealthyThreshold?: pulumi.Input<number>;
```


Consecutive failures required (default 2).

<h2 class="pdoc-module-header" id="HealthCheckState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L130">interface HealthCheckState</a>
</h2>

Input properties used for looking up and filtering HealthCheck resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L135">property checkIntervalSec</a>
</h3>

```typescript
checkIntervalSec?: pulumi.Input<number>;
```


The number of seconds between each poll of
the instance instance (default 5).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L139">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Textual description field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L143">property healthyThreshold</a>
</h3>

```typescript
healthyThreshold?: pulumi.Input<number>;
```


Consecutive successes required (default 2).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L148">property httpHealthCheck</a>
</h3>

```typescript
httpHealthCheck?: pulumi.Input<{ ... }>;
```


An HTTP Health Check. Only one kind of Health Check can be added.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L153">property httpsHealthCheck</a>
</h3>

```typescript
httpsHealthCheck?: pulumi.Input<{ ... }>;
```


An HTTPS Health Check. Only one kind of Health Check can be added.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L158">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L163">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L167">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L172">property sslHealthCheck</a>
</h3>

```typescript
sslHealthCheck?: pulumi.Input<{ ... }>;
```


An SSL Health Check. Only one kind of Health Check can be added.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L177">property tcpHealthCheck</a>
</h3>

```typescript
tcpHealthCheck?: pulumi.Input<{ ... }>;
```


A TCP Health Check. Only one kind of Health Check can be added.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L182">property timeoutSec</a>
</h3>

```typescript
timeoutSec?: pulumi.Input<number>;
```


The number of seconds to wait before declaring
failure (default 5).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/healthCheck.ts#L186">property unhealthyThreshold</a>
</h3>

```typescript
unhealthyThreshold?: pulumi.Input<number>;
```


Consecutive failures required (default 2).

<h2 class="pdoc-module-header" id="HttpHealthCheckArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L110">interface HttpHealthCheckArgs</a>
</h2>

The set of arguments for constructing a HttpHealthCheck resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L111">property checkIntervalSec</a>
</h3>

```typescript
checkIntervalSec?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L112">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L113">property healthyThreshold</a>
</h3>

```typescript
healthyThreshold?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L114">property host</a>
</h3>

```typescript
host?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L115">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L116">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L121">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L122">property requestPath</a>
</h3>

```typescript
requestPath?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L123">property timeoutSec</a>
</h3>

```typescript
timeoutSec?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L124">property unhealthyThreshold</a>
</h3>

```typescript
unhealthyThreshold?: pulumi.Input<number>;
```

<h2 class="pdoc-module-header" id="HttpHealthCheckState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L85">interface HttpHealthCheckState</a>
</h2>

Input properties used for looking up and filtering HttpHealthCheck resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L86">property checkIntervalSec</a>
</h3>

```typescript
checkIntervalSec?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L87">property creationTimestamp</a>
</h3>

```typescript
creationTimestamp?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L88">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L89">property healthyThreshold</a>
</h3>

```typescript
healthyThreshold?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L90">property host</a>
</h3>

```typescript
host?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L91">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L92">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L97">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L98">property requestPath</a>
</h3>

```typescript
requestPath?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L102">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L103">property timeoutSec</a>
</h3>

```typescript
timeoutSec?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpHealthCheck.ts#L104">property unhealthyThreshold</a>
</h3>

```typescript
unhealthyThreshold?: pulumi.Input<number>;
```

<h2 class="pdoc-module-header" id="HttpsHealthCheckArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L110">interface HttpsHealthCheckArgs</a>
</h2>

The set of arguments for constructing a HttpsHealthCheck resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L111">property checkIntervalSec</a>
</h3>

```typescript
checkIntervalSec?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L112">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L113">property healthyThreshold</a>
</h3>

```typescript
healthyThreshold?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L114">property host</a>
</h3>

```typescript
host?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L115">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L116">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L121">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L122">property requestPath</a>
</h3>

```typescript
requestPath?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L123">property timeoutSec</a>
</h3>

```typescript
timeoutSec?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L124">property unhealthyThreshold</a>
</h3>

```typescript
unhealthyThreshold?: pulumi.Input<number>;
```

<h2 class="pdoc-module-header" id="HttpsHealthCheckState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L85">interface HttpsHealthCheckState</a>
</h2>

Input properties used for looking up and filtering HttpsHealthCheck resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L86">property checkIntervalSec</a>
</h3>

```typescript
checkIntervalSec?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L87">property creationTimestamp</a>
</h3>

```typescript
creationTimestamp?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L88">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L89">property healthyThreshold</a>
</h3>

```typescript
healthyThreshold?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L90">property host</a>
</h3>

```typescript
host?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L91">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L92">property port</a>
</h3>

```typescript
port?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L97">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L98">property requestPath</a>
</h3>

```typescript
requestPath?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L102">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L103">property timeoutSec</a>
</h3>

```typescript
timeoutSec?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/httpsHealthCheck.ts#L104">property unhealthyThreshold</a>
</h3>

```typescript
unhealthyThreshold?: pulumi.Input<number>;
```

<h2 class="pdoc-module-header" id="ImageArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L164">interface ImageArgs</a>
</h2>

The set of arguments for constructing a Image resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L168">property createTimeout</a>
</h3>

```typescript
createTimeout?: pulumi.Input<number>;
```


Configurable timeout in minutes for creating images. Default is 4 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L172">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the image to be created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L176">property family</a>
</h3>

```typescript
family?: pulumi.Input<string>;
```


The name of the image family to which this image belongs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L180">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A set of key/value label pairs to assign to the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L185">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L190">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L196">property rawDisk</a>
</h3>

```typescript
rawDisk?: pulumi.Input<{ ... }>;
```


The raw disk that will be used as the source of the image.
Changing this forces a new resource to be created. Structure is documented
below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L201">property sourceDisk</a>
</h3>

```typescript
sourceDisk?: pulumi.Input<string>;
```


The URL of a disk that will be used as the source of the
image. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ImageState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L113">interface ImageState</a>
</h2>

Input properties used for looking up and filtering Image resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L117">property createTimeout</a>
</h3>

```typescript
createTimeout?: pulumi.Input<number>;
```


Configurable timeout in minutes for creating images. Default is 4 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L121">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the image to be created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L125">property family</a>
</h3>

```typescript
family?: pulumi.Input<string>;
```


The name of the image family to which this image belongs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L129">property labelFingerprint</a>
</h3>

```typescript
labelFingerprint?: pulumi.Input<string>;
```


The fingerprint of the assigned labels.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L133">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A set of key/value label pairs to assign to the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L138">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L143">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L149">property rawDisk</a>
</h3>

```typescript
rawDisk?: pulumi.Input<{ ... }>;
```


The raw disk that will be used as the source of the image.
Changing this forces a new resource to be created. Structure is documented
below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L153">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/image.ts#L158">property sourceDisk</a>
</h3>

```typescript
sourceDisk?: pulumi.Input<string>;
```


The URL of a disk that will be used as the source of the
image. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="InstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L380">interface InstanceArgs</a>
</h2>

The set of arguments for constructing a Instance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L385">property allowStoppingForUpdate</a>
</h3>

```typescript
allowStoppingForUpdate?: pulumi.Input<boolean>;
```


If true, allows Terraform to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L389">property attachedDisks</a>
</h3>

```typescript
attachedDisks?: pulumi.Input<{ ... }[]>;
```


List of disks to attach to the instance. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L394">property bootDisk</a>
</h3>

```typescript
bootDisk: pulumi.Input<{ ... }>;
```


The boot disk for the instance.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L400">property canIpForward</a>
</h3>

```typescript
canIpForward?: pulumi.Input<boolean>;
```


Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L405">property createTimeout</a>
</h3>

```typescript
createTimeout?: pulumi.Input<number>;
```


Configurable timeout in minutes for creating instances. Default is 4 minutes.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L410">property deletionProtection</a>
</h3>

```typescript
deletionProtection?: pulumi.Input<boolean>;
```


Enable deletion protection on this instance. Defaults to false.
**Note:** you must disable deletion protection before removing the resource (e.g., via `terraform destroy`), or the instance cannot be deleted and the Terraform run will not complete successfully.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L414">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A brief description of this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L418">property guestAccelerators</a>
</h3>

```typescript
guestAccelerators?: pulumi.Input<{ ... }[]>;
```


List of the type and count of accelerator cards attached to the instance. Structure documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L422">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A set of key/value label pairs to assign to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L429">property machineType</a>
</h3>

```typescript
machineType: pulumi.Input<string>;
```


The machine type to create. To create a custom
machine type, value should be set as specified
[here](https://cloud.google.com/compute/docs/reference/latest/instances#machineType).
**Note**: [`allow_stopping_for_update`](#allow_stopping_for_update) must be set to true in order to update this field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L434">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to make available from
within the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L442">property metadataStartupScript</a>
</h3>

```typescript
metadataStartupScript?: pulumi.Input<string>;
```


An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L448">property minCpuPlatform</a>
</h3>

```typescript
minCpuPlatform?: pulumi.Input<string>;
```


Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
**Note**: [`allow_stopping_for_update`](#allow_stopping_for_update) must be set to true in order to update this field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L453">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L458">property networkInterfaces</a>
</h3>

```typescript
networkInterfaces: pulumi.Input<{ ... }[]>;
```


Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L463">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L468">property scheduling</a>
</h3>

```typescript
scheduling?: pulumi.Input<{ ... }>;
```


The scheduling strategy to use. More details about
this configuration option are detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L473">property scratchDisks</a>
</h3>

```typescript
scratchDisks?: pulumi.Input<{ ... }[]>;
```


Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L479">property serviceAccount</a>
</h3>

```typescript
serviceAccount?: pulumi.Input<{ ... }>;
```


Service account to attach to the instance.
Structure is documented below.
**Note**: [`allow_stopping_for_update`](#allow_stopping_for_update) must be set to true in order to update this field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L483">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of tags to attach to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L487">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone that the machine should be created in.

<h2 class="pdoc-module-header" id="InstanceGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L159">interface InstanceGroupArgs</a>
</h2>

The set of arguments for constructing a InstanceGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L164">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


An optional textual description of the instance
group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L170">property instances</a>
</h3>

```typescript
instances?: pulumi.Input<pulumi.Input<string>[]>;
```


List of instances in the group. They should be given
as self_link URLs. When adding instances they must all be in the same
network and zone as the instance group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L174">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name which the port will be mapped to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L179">property namedPorts</a>
</h3>

```typescript
namedPorts?: pulumi.Input<{ ... }[]>;
```


The named port configuration. See the section below
for details on configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L186">property network</a>
</h3>

```typescript
network?: pulumi.Input<string>;
```


The URL of the network the instance group is in. If
this is different from the network where the instances are in, the creation
fails. Defaults to the network where the instances are in (if neither
`network` nor `instances` is specified, this field will be blank).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L191">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L195">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone that this instance group should be created in.

<h2 class="pdoc-module-header" id="InstanceGroupManagerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L266">interface InstanceGroupManagerArgs</a>
</h2>

The set of arguments for constructing a InstanceGroupManager resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L271">property autoHealingPolicies</a>
</h3>

```typescript
autoHealingPolicies?: pulumi.Input<{ ... }>;
```


) The autohealing policies for this managed instance
group. You can specify only one value. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L280">property baseInstanceName</a>
</h3>

```typescript
baseInstanceName: pulumi.Input<string>;
```


The base instance name to use for
instances in this group. The value must be a valid
[RFC1035](https://www.ietf.org/rfc/rfc1035.txt) name. Supported characters
are lowercase letters, numbers, and hyphens (-). Instances are named by
appending a hyphen and a random four-character string to the base instance
name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L285">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


An optional textual description of the instance
group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L290">property instanceTemplate</a>
</h3>

```typescript
instanceTemplate: pulumi.Input<string>;
```


The full URL to an instance template from
which all new instances will be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L294">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L299">property namedPorts</a>
</h3>

```typescript
namedPorts?: pulumi.Input<{ ... }[]>;
```


The named port configuration. See the section below
for details on configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L304">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L309">property rollingUpdatePolicy</a>
</h3>

```typescript
rollingUpdatePolicy?: pulumi.Input<{ ... }>;
```


) The update policy for this managed instance group. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagers/patch)
- - -

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L315">property targetPools</a>
</h3>

```typescript
targetPools?: pulumi.Input<pulumi.Input<string>[]>;
```


The full URL of all target pools to which new
instances in the group are added. Updating the target pools attribute does
not affect existing instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L321">property targetSize</a>
</h3>

```typescript
targetSize?: pulumi.Input<number>;
```


The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to `0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L329">property updateStrategy</a>
</h3>

```typescript
updateStrategy?: pulumi.Input<string>;
```


If the `instance_template`
resource is modified, a value of `"NONE"` will prevent any of the managed
instances from being restarted by Terraform. A value of `"RESTART"` will
restart all of the instances at once. `"ROLLING_UPDATE"` is supported as [Beta feature].
A value of `"ROLLING_UPDATE"` requires `rolling_update_policy` block to be set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L335">property waitForInstances</a>
</h3>

```typescript
waitForInstances?: pulumi.Input<boolean>;
```


Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, Terraform will
continue trying until it times out.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L340">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone that instances in this group should be created
in.

<h2 class="pdoc-module-header" id="InstanceGroupManagerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L174">interface InstanceGroupManagerState</a>
</h2>

Input properties used for looking up and filtering InstanceGroupManager resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L179">property autoHealingPolicies</a>
</h3>

```typescript
autoHealingPolicies?: pulumi.Input<{ ... }>;
```


) The autohealing policies for this managed instance
group. You can specify only one value. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L188">property baseInstanceName</a>
</h3>

```typescript
baseInstanceName?: pulumi.Input<string>;
```


The base instance name to use for
instances in this group. The value must be a valid
[RFC1035](https://www.ietf.org/rfc/rfc1035.txt) name. Supported characters
are lowercase letters, numbers, and hyphens (-). Instances are named by
appending a hyphen and a random four-character string to the base instance
name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L193">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


An optional textual description of the instance
group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L197">property fingerprint</a>
</h3>

```typescript
fingerprint?: pulumi.Input<string>;
```


The fingerprint of the instance group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L201">property instanceGroup</a>
</h3>

```typescript
instanceGroup?: pulumi.Input<string>;
```


The full URL of the instance group created by the manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L206">property instanceTemplate</a>
</h3>

```typescript
instanceTemplate?: pulumi.Input<string>;
```


The full URL to an instance template from
which all new instances will be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L210">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L215">property namedPorts</a>
</h3>

```typescript
namedPorts?: pulumi.Input<{ ... }[]>;
```


The named port configuration. See the section below
for details on configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L220">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L225">property rollingUpdatePolicy</a>
</h3>

```typescript
rollingUpdatePolicy?: pulumi.Input<{ ... }>;
```


) The update policy for this managed instance group. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagers/patch)
- - -

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L229">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URL of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L235">property targetPools</a>
</h3>

```typescript
targetPools?: pulumi.Input<pulumi.Input<string>[]>;
```


The full URL of all target pools to which new
instances in the group are added. Updating the target pools attribute does
not affect existing instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L241">property targetSize</a>
</h3>

```typescript
targetSize?: pulumi.Input<number>;
```


The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to `0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L249">property updateStrategy</a>
</h3>

```typescript
updateStrategy?: pulumi.Input<string>;
```


If the `instance_template`
resource is modified, a value of `"NONE"` will prevent any of the managed
instances from being restarted by Terraform. A value of `"RESTART"` will
restart all of the instances at once. `"ROLLING_UPDATE"` is supported as [Beta feature].
A value of `"ROLLING_UPDATE"` requires `rolling_update_policy` block to be set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L255">property waitForInstances</a>
</h3>

```typescript
waitForInstances?: pulumi.Input<boolean>;
```


Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, Terraform will
continue trying until it times out.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroupManager.ts#L260">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone that instances in this group should be created
in.

<h2 class="pdoc-module-header" id="InstanceGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L109">interface InstanceGroupState</a>
</h2>

Input properties used for looking up and filtering InstanceGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L114">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


An optional textual description of the instance
group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L120">property instances</a>
</h3>

```typescript
instances?: pulumi.Input<pulumi.Input<string>[]>;
```


List of instances in the group. They should be given
as self_link URLs. When adding instances they must all be in the same
network and zone as the instance group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L124">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name which the port will be mapped to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L129">property namedPorts</a>
</h3>

```typescript
namedPorts?: pulumi.Input<{ ... }[]>;
```


The named port configuration. See the section below
for details on configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L136">property network</a>
</h3>

```typescript
network?: pulumi.Input<string>;
```


The URL of the network the instance group is in. If
this is different from the network where the instances are in, the creation
fails. Defaults to the network where the instances are in (if neither
`network` nor `instances` is specified, this field will be blank).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L141">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L145">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L149">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```


The number of instances in the group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceGroup.ts#L153">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone that this instance group should be created in.

<h2 class="pdoc-module-header" id="InstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L243">interface InstanceState</a>
</h2>

Input properties used for looking up and filtering Instance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L248">property allowStoppingForUpdate</a>
</h3>

```typescript
allowStoppingForUpdate?: pulumi.Input<boolean>;
```


If true, allows Terraform to stop the instance to update its properties.
If you try to update a property that requires stopping the instance without setting this field, the update will fail.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L252">property attachedDisks</a>
</h3>

```typescript
attachedDisks?: pulumi.Input<{ ... }[]>;
```


List of disks to attach to the instance. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L257">property bootDisk</a>
</h3>

```typescript
bootDisk?: pulumi.Input<{ ... }>;
```


The boot disk for the instance.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L263">property canIpForward</a>
</h3>

```typescript
canIpForward?: pulumi.Input<boolean>;
```


Whether to allow sending and receiving of
packets with non-matching source or destination IPs.
This defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L267">property cpuPlatform</a>
</h3>

```typescript
cpuPlatform?: pulumi.Input<string>;
```


The CPU platform used by this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L272">property createTimeout</a>
</h3>

```typescript
createTimeout?: pulumi.Input<number>;
```


Configurable timeout in minutes for creating instances. Default is 4 minutes.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L277">property deletionProtection</a>
</h3>

```typescript
deletionProtection?: pulumi.Input<boolean>;
```


Enable deletion protection on this instance. Defaults to false.
**Note:** you must disable deletion protection before removing the resource (e.g., via `terraform destroy`), or the instance cannot be deleted and the Terraform run will not complete successfully.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L281">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A brief description of this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L285">property guestAccelerators</a>
</h3>

```typescript
guestAccelerators?: pulumi.Input<{ ... }[]>;
```


List of the type and count of accelerator cards attached to the instance. Structure documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L289">property instanceId</a>
</h3>

```typescript
instanceId?: pulumi.Input<string>;
```


The server-assigned unique identifier of this instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L293">property labelFingerprint</a>
</h3>

```typescript
labelFingerprint?: pulumi.Input<string>;
```


The unique fingerprint of the labels.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L297">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A set of key/value label pairs to assign to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L304">property machineType</a>
</h3>

```typescript
machineType?: pulumi.Input<string>;
```


The machine type to create. To create a custom
machine type, value should be set as specified
[here](https://cloud.google.com/compute/docs/reference/latest/instances#machineType).
**Note**: [`allow_stopping_for_update`](#allow_stopping_for_update) must be set to true in order to update this field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L309">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to make available from
within the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L313">property metadataFingerprint</a>
</h3>

```typescript
metadataFingerprint?: pulumi.Input<string>;
```


The unique fingerprint of the metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L321">property metadataStartupScript</a>
</h3>

```typescript
metadataStartupScript?: pulumi.Input<string>;
```


An alternative to using the
startup-script metadata key, except this one forces the instance to be
recreated (thus re-running the script) if it is changed. This replaces the
startup-script metadata key on the created instance and thus the two
mechanisms are not allowed to be used simultaneously.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L327">property minCpuPlatform</a>
</h3>

```typescript
minCpuPlatform?: pulumi.Input<string>;
```


Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).
**Note**: [`allow_stopping_for_update`](#allow_stopping_for_update) must be set to true in order to update this field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L332">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L337">property networkInterfaces</a>
</h3>

```typescript
networkInterfaces?: pulumi.Input<{ ... }[]>;
```


Networks to attach to the instance. This can
be specified multiple times. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L342">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L347">property scheduling</a>
</h3>

```typescript
scheduling?: pulumi.Input<{ ... }>;
```


The scheduling strategy to use. More details about
this configuration option are detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L352">property scratchDisks</a>
</h3>

```typescript
scratchDisks?: pulumi.Input<{ ... }[]>;
```


Scratch disks to attach to the instance. This can be
specified multiple times for multiple scratch disks. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L356">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L362">property serviceAccount</a>
</h3>

```typescript
serviceAccount?: pulumi.Input<{ ... }>;
```


Service account to attach to the instance.
Structure is documented below.
**Note**: [`allow_stopping_for_update`](#allow_stopping_for_update) must be set to true in order to update this field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L366">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of tags to attach to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L370">property tagsFingerprint</a>
</h3>

```typescript
tagsFingerprint?: pulumi.Input<string>;
```


The unique fingerprint of the tags.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instance.ts#L374">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone that the machine should be created in.

<h2 class="pdoc-module-header" id="InstanceTemplateArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L313">interface InstanceTemplateArgs</a>
</h2>

The set of arguments for constructing a InstanceTemplate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L318">property canIpForward</a>
</h3>

```typescript
canIpForward?: pulumi.Input<boolean>;
```


Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L322">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A brief description of this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L328">property disks</a>
</h3>

```typescript
disks: pulumi.Input<{ ... }[]>;
```


Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L332">property guestAccelerators</a>
</h3>

```typescript
guestAccelerators?: pulumi.Input<{ ... }[]>;
```


List of the type and count of accelerator cards attached to the instance. Structure documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L337">property instanceDescription</a>
</h3>

```typescript
instanceDescription?: pulumi.Input<string>;
```


A brief description to use for instances
created from this template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L342">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A set of key/value label pairs to assign to instances
created from this template,

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L346">property machineType</a>
</h3>

```typescript
machineType: pulumi.Input<string>;
```


The machine type to create.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L351">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to make available from
within instances created from this template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L358">property metadataStartupScript</a>
</h3>

```typescript
metadataStartupScript?: pulumi.Input<string>;
```


An alternative to using the
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L363">property minCpuPlatform</a>
</h3>

```typescript
minCpuPlatform?: pulumi.Input<string>;
```


Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L368">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the instance template. If you leave
this blank, Terraform will auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L373">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L379">property networkInterfaces</a>
</h3>

```typescript
networkInterfaces?: pulumi.Input<{ ... }[]>;
```


Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L384">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L393">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom `subnetwork`
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L398">property schedulings</a>
</h3>

```typescript
schedulings?: pulumi.Input<{ ... }[]>;
```


The scheduling strategy to use. More details about
this configuration option are detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L402">property serviceAccount</a>
</h3>

```typescript
serviceAccount?: pulumi.Input<{ ... }>;
```


Service account to attach to the instance. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L406">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


Tags to attach to the instance.

<h2 class="pdoc-module-header" id="InstanceTemplateState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L202">interface InstanceTemplateState</a>
</h2>

Input properties used for looking up and filtering InstanceTemplate resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L207">property canIpForward</a>
</h3>

```typescript
canIpForward?: pulumi.Input<boolean>;
```


Whether to allow sending and receiving of
packets with non-matching source or destination IPs. This defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L211">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A brief description of this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L217">property disks</a>
</h3>

```typescript
disks?: pulumi.Input<{ ... }[]>;
```


Disks to attach to instances created from this template.
This can be specified multiple times for multiple disks. Structure is
documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L221">property guestAccelerators</a>
</h3>

```typescript
guestAccelerators?: pulumi.Input<{ ... }[]>;
```


List of the type and count of accelerator cards attached to the instance. Structure documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L226">property instanceDescription</a>
</h3>

```typescript
instanceDescription?: pulumi.Input<string>;
```


A brief description to use for instances
created from this template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L231">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A set of key/value label pairs to assign to instances
created from this template,

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L235">property machineType</a>
</h3>

```typescript
machineType?: pulumi.Input<string>;
```


The machine type to create.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L240">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to make available from
within instances created from this template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L244">property metadataFingerprint</a>
</h3>

```typescript
metadataFingerprint?: pulumi.Input<string>;
```


The unique fingerprint of the metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L251">property metadataStartupScript</a>
</h3>

```typescript
metadataStartupScript?: pulumi.Input<string>;
```


An alternative to using the
startup-script metadata key, mostly to match the compute_instance resource.
This replaces the startup-script metadata key on the created instance and
thus the two mechanisms are not allowed to be used simultaneously.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L256">property minCpuPlatform</a>
</h3>

```typescript
minCpuPlatform?: pulumi.Input<string>;
```


Specifies a minimum CPU platform. Applicable values are the friendly names of CPU platforms, such as
`Intel Haswell` or `Intel Skylake`. See the complete list [here](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L261">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the instance template. If you leave
this blank, Terraform will auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L266">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L272">property networkInterfaces</a>
</h3>

```typescript
networkInterfaces?: pulumi.Input<{ ... }[]>;
```


Networks to attach to instances created from
this template. This can be specified multiple times for multiple networks.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L277">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L286">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


An instance template is a global resource that is not
bound to a zone or a region. However, you can still specify some regional
resources in an instance template, which restricts the template to the
region where that resource resides. For example, a custom `subnetwork`
resource is tied to a specific region. Defaults to the region of the
Provider if no value is given.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L291">property schedulings</a>
</h3>

```typescript
schedulings?: pulumi.Input<{ ... }[]>;
```


The scheduling strategy to use. More details about
this configuration option are detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L295">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L299">property serviceAccount</a>
</h3>

```typescript
serviceAccount?: pulumi.Input<{ ... }>;
```


Service account to attach to the instance. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L303">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


Tags to attach to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/instanceTemplate.ts#L307">property tagsFingerprint</a>
</h3>

```typescript
tagsFingerprint?: pulumi.Input<string>;
```


The unique fingerprint of the tags.

<h2 class="pdoc-module-header" id="NetworkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L154">interface NetworkArgs</a>
</h2>

The set of arguments for constructing a Network resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L161">property autoCreateSubnetworks</a>
</h3>

```typescript
autoCreateSubnetworks?: pulumi.Input<boolean>;
```


If set to true, this network will be
created in auto subnet mode, and Google will create a subnet for each region
automatically. If set to false, a custom subnetted network will be created that
can support `google_compute_subnetwork` resources. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L165">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A brief description of this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L171">property ipv4Range</a>
</h3>

```typescript
ipv4Range?: pulumi.Input<string>;
```


If set to a CIDR block, uses the legacy VPC API with the
specified range. This API is deprecated. If set, `auto_create_subnetworks` must be
explicitly set to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L176">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L181">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L188">property routingMode</a>
</h3>

```typescript
routingMode?: pulumi.Input<string>;
```


Sets the network-wide routing mode for Cloud Routers
to use. Accepted values are `"GLOBAL"` or `"REGIONAL"`. Defaults to `"REGIONAL"`.
Refer to the [Cloud Router documentation](https://cloud.google.com/router/docs/concepts/overview#dynamic-routing-mode)
for more details.

<h2 class="pdoc-module-header" id="NetworkPeeringArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L126">interface NetworkPeeringArgs</a>
</h2>

The set of arguments for constructing a NetworkPeering resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L131">property autoCreateRoutes</a>
</h3>

```typescript
autoCreateRoutes?: pulumi.Input<boolean>;
```


If set to `true`, the routes between the two networks will
be created and managed automatically. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L135">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L139">property network</a>
</h3>

```typescript
network: pulumi.Input<string>;
```


Resource link of the network to add a peering to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L143">property peerNetwork</a>
</h3>

```typescript
peerNetwork: pulumi.Input<string>;
```


Resource link of the peer network.

<h2 class="pdoc-module-header" id="NetworkPeeringState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L95">interface NetworkPeeringState</a>
</h2>

Input properties used for looking up and filtering NetworkPeering resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L100">property autoCreateRoutes</a>
</h3>

```typescript
autoCreateRoutes?: pulumi.Input<boolean>;
```


If set to `true`, the routes between the two networks will
be created and managed automatically. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L104">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L108">property network</a>
</h3>

```typescript
network?: pulumi.Input<string>;
```


Resource link of the network to add a peering to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L112">property peerNetwork</a>
</h3>

```typescript
peerNetwork?: pulumi.Input<string>;
```


Resource link of the peer network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L116">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


State for the peering.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/networkPeering.ts#L120">property stateDetails</a>
</h3>

```typescript
stateDetails?: pulumi.Input<string>;
```


Details about the current state of the peering.

<h2 class="pdoc-module-header" id="NetworkState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L106">interface NetworkState</a>
</h2>

Input properties used for looking up and filtering Network resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L113">property autoCreateSubnetworks</a>
</h3>

```typescript
autoCreateSubnetworks?: pulumi.Input<boolean>;
```


If set to true, this network will be
created in auto subnet mode, and Google will create a subnet for each region
automatically. If set to false, a custom subnetted network will be created that
can support `google_compute_subnetwork` resources. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L117">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A brief description of this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L121">property gatewayIpv4</a>
</h3>

```typescript
gatewayIpv4?: pulumi.Input<string>;
```


The IPv4 address of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L127">property ipv4Range</a>
</h3>

```typescript
ipv4Range?: pulumi.Input<string>;
```


If set to a CIDR block, uses the legacy VPC API with the
specified range. This API is deprecated. If set, `auto_create_subnetworks` must be
explicitly set to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L132">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L137">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L144">property routingMode</a>
</h3>

```typescript
routingMode?: pulumi.Input<string>;
```


Sets the network-wide routing mode for Cloud Routers
to use. Accepted values are `"GLOBAL"` or `"REGIONAL"`. Defaults to `"REGIONAL"`.
Refer to the [Cloud Router documentation](https://cloud.google.com/router/docs/concepts/overview#dynamic-routing-mode)
for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/network.ts#L148">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h2 class="pdoc-module-header" id="ProjectMetadataArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadata.ts#L85">interface ProjectMetadataArgs</a>
</h2>

The set of arguments for constructing a ProjectMetadata resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadata.ts#L90">property metadata</a>
</h3>

```typescript
metadata: pulumi.Input<{ ... }>;
```


A series of key value pairs. Changing this resource
updates the GCE state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadata.ts#L95">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="ProjectMetadataItemArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadataItem.ts#L92">interface ProjectMetadataItemArgs</a>
</h2>

The set of arguments for constructing a ProjectMetadataItem resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadataItem.ts#L96">property key</a>
</h3>

```typescript
key: pulumi.Input<string>;
```


The metadata key to set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadataItem.ts#L101">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadataItem.ts#L105">property value</a>
</h3>

```typescript
value: pulumi.Input<string>;
```


The value to set for the given metadata key.

<h2 class="pdoc-module-header" id="ProjectMetadataItemState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadataItem.ts#L73">interface ProjectMetadataItemState</a>
</h2>

Input properties used for looking up and filtering ProjectMetadataItem resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadataItem.ts#L77">property key</a>
</h3>

```typescript
key?: pulumi.Input<string>;
```


The metadata key to set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadataItem.ts#L82">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadataItem.ts#L86">property value</a>
</h3>

```typescript
value?: pulumi.Input<string>;
```


The value to set for the given metadata key.

<h2 class="pdoc-module-header" id="ProjectMetadataState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadata.ts#L69">interface ProjectMetadataState</a>
</h2>

Input properties used for looking up and filtering ProjectMetadata resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadata.ts#L74">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


A series of key value pairs. Changing this resource
updates the GCE state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/projectMetadata.ts#L79">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="RegionAutoscalerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L152">interface RegionAutoscalerArgs</a>
</h2>

The set of arguments for constructing a RegionAutoscaler resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L157">property autoscalingPolicy</a>
</h3>

```typescript
autoscalingPolicy: pulumi.Input<{ ... }>;
```


The parameters of the autoscaling
algorithm. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L162">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


An optional textual description of the instance
group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L167">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Google Cloud Monitoring metric to follow, e.g.
`compute.googleapis.com/instance/network/received_bytes_count`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L172">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L176">property region</a>
</h3>

```typescript
region: pulumi.Input<string>;
```


The region of the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L183">property target</a>
</h3>

```typescript
target: pulumi.Input<string>;
```


The floating point threshold where load balancing utilization
should be. E.g. if the load balancer's `maxRatePerInstance` is 10 requests
per second (RPS) then setting this to 0.5 would cause the group to be scaled
such that each instance receives 5 RPS.

<h2 class="pdoc-module-header" id="RegionAutoscalerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L111">interface RegionAutoscalerState</a>
</h2>

Input properties used for looking up and filtering RegionAutoscaler resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L116">property autoscalingPolicy</a>
</h3>

```typescript
autoscalingPolicy?: pulumi.Input<{ ... }>;
```


The parameters of the autoscaling
algorithm. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L121">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


An optional textual description of the instance
group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L126">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Google Cloud Monitoring metric to follow, e.g.
`compute.googleapis.com/instance/network/received_bytes_count`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L131">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L135">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region of the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L139">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URL of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionAutoscaler.ts#L146">property target</a>
</h3>

```typescript
target?: pulumi.Input<string>;
```


The floating point threshold where load balancing utilization
should be. E.g. if the load balancer's `maxRatePerInstance` is 10 requests
per second (RPS) then setting this to 0.5 would cause the group to be scaled
such that each instance receives 5 RPS.

<h2 class="pdoc-module-header" id="RegionBackendServiceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L196">interface RegionBackendServiceArgs</a>
</h2>

The set of arguments for constructing a RegionBackendService resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L201">property backends</a>
</h3>

```typescript
backends?: pulumi.Input<{ ... }[]>;
```


The list of backends that serve this BackendService.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L206">property connectionDrainingTimeoutSec</a>
</h3>

```typescript
connectionDrainingTimeoutSec?: pulumi.Input<number>;
```


Time for which instance will be drained
(not accept new connections, but still work to finish started ones). Defaults to `0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L210">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Textual description for the backend.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L216">property healthChecks</a>
</h3>

```typescript
healthChecks: pulumi.Input<pulumi.Input<string>>;
```


Specifies a list of health checks
for checking the health of the backend service. Currently at most
one health check can be specified, and a health check is required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L220">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the backend service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L225">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L230">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The protocol for incoming requests. Defaults to
`HTTP`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L235">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The Region in which the created address should reside.
If it is not provided, the provider region is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L241">property sessionAffinity</a>
</h3>

```typescript
sessionAffinity?: pulumi.Input<string>;
```


How to distribute load. Options are `NONE` (no
affinity), `CLIENT_IP`, `CLIENT_IP_PROTO`, or `CLIENT_IP_PORT_PROTO`.
Defaults to `NONE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L246">property timeoutSec</a>
</h3>

```typescript
timeoutSec?: pulumi.Input<number>;
```


The number of secs to wait for a backend to respond
to a request before considering the request failed. Defaults to `30`.

<h2 class="pdoc-module-header" id="RegionBackendServiceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L132">interface RegionBackendServiceState</a>
</h2>

Input properties used for looking up and filtering RegionBackendService resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L137">property backends</a>
</h3>

```typescript
backends?: pulumi.Input<{ ... }[]>;
```


The list of backends that serve this BackendService.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L142">property connectionDrainingTimeoutSec</a>
</h3>

```typescript
connectionDrainingTimeoutSec?: pulumi.Input<number>;
```


Time for which instance will be drained
(not accept new connections, but still work to finish started ones). Defaults to `0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L146">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Textual description for the backend.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L150">property fingerprint</a>
</h3>

```typescript
fingerprint?: pulumi.Input<string>;
```


The fingerprint of the backend service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L156">property healthChecks</a>
</h3>

```typescript
healthChecks?: pulumi.Input<pulumi.Input<string>>;
```


Specifies a list of health checks
for checking the health of the backend service. Currently at most
one health check can be specified, and a health check is required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L160">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the backend service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L165">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L170">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The protocol for incoming requests. Defaults to
`HTTP`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L175">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The Region in which the created address should reside.
If it is not provided, the provider region is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L179">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L185">property sessionAffinity</a>
</h3>

```typescript
sessionAffinity?: pulumi.Input<string>;
```


How to distribute load. Options are `NONE` (no
affinity), `CLIENT_IP`, `CLIENT_IP_PROTO`, or `CLIENT_IP_PORT_PROTO`.
Defaults to `NONE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionBackendService.ts#L190">property timeoutSec</a>
</h3>

```typescript
timeoutSec?: pulumi.Input<number>;
```


The number of secs to wait for a backend to respond
to a request before considering the request failed. Defaults to `30`.

<h2 class="pdoc-module-header" id="RegionInstanceGroupManagerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L279">interface RegionInstanceGroupManagerArgs</a>
</h2>

The set of arguments for constructing a RegionInstanceGroupManager resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L284">property autoHealingPolicies</a>
</h3>

```typescript
autoHealingPolicies?: pulumi.Input<{ ... }>;
```


) The autohealing policies for this managed instance
group. You can specify only one value. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L293">property baseInstanceName</a>
</h3>

```typescript
baseInstanceName: pulumi.Input<string>;
```


The base instance name to use for
instances in this group. The value must be a valid
[RFC1035](https://www.ietf.org/rfc/rfc1035.txt) name. Supported characters
are lowercase letters, numbers, and hyphens (-). Instances are named by
appending a hyphen and a random four-character string to the base instance
name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L298">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


An optional textual description of the instance
group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L304">property distributionPolicyZones</a>
</h3>

```typescript
distributionPolicyZones?: pulumi.Input<pulumi.Input<string>[]>;
```


) The distribution policy for this managed instance
group. You can specify one or more values. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selectingzones).
- - -

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L309">property instanceTemplate</a>
</h3>

```typescript
instanceTemplate: pulumi.Input<string>;
```


The full URL to an instance template from
which all new instances will be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L313">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L318">property namedPorts</a>
</h3>

```typescript
namedPorts?: pulumi.Input<{ ... }[]>;
```


The named port configuration. See the section below
for details on configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L323">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L327">property region</a>
</h3>

```typescript
region: pulumi.Input<string>;
```


The region where the managed instance group resides.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L331">property rollingUpdatePolicy</a>
</h3>

```typescript
rollingUpdatePolicy?: pulumi.Input<{ ... }>;
```


) The update policy for this managed instance group. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patch)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L337">property targetPools</a>
</h3>

```typescript
targetPools?: pulumi.Input<pulumi.Input<string>[]>;
```


The full URL of all target pools to which new
instances in the group are added. Updating the target pools attribute does
not affect existing instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L343">property targetSize</a>
</h3>

```typescript
targetSize?: pulumi.Input<number>;
```


The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to `0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L351">property updateStrategy</a>
</h3>

```typescript
updateStrategy?: pulumi.Input<string>;
```


If the `instance_template`
resource is modified, a value of `"NONE"` will prevent any of the managed
instances from being restarted by Terraform. A value of `"ROLLING_UPDATE"`
is supported as [Beta feature]. A value of `"ROLLING_UPDATE"` requires
`rolling_update_policy` block to be set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L357">property waitForInstances</a>
</h3>

```typescript
waitForInstances?: pulumi.Input<boolean>;
```


Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, Terraform will
continue trying until it times out.

<h2 class="pdoc-module-header" id="RegionInstanceGroupManagerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L183">interface RegionInstanceGroupManagerState</a>
</h2>

Input properties used for looking up and filtering RegionInstanceGroupManager resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L188">property autoHealingPolicies</a>
</h3>

```typescript
autoHealingPolicies?: pulumi.Input<{ ... }>;
```


) The autohealing policies for this managed instance
group. You can specify only one value. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L197">property baseInstanceName</a>
</h3>

```typescript
baseInstanceName?: pulumi.Input<string>;
```


The base instance name to use for
instances in this group. The value must be a valid
[RFC1035](https://www.ietf.org/rfc/rfc1035.txt) name. Supported characters
are lowercase letters, numbers, and hyphens (-). Instances are named by
appending a hyphen and a random four-character string to the base instance
name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L202">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


An optional textual description of the instance
group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L208">property distributionPolicyZones</a>
</h3>

```typescript
distributionPolicyZones?: pulumi.Input<pulumi.Input<string>[]>;
```


) The distribution policy for this managed instance
group. You can specify one or more values. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selectingzones).
- - -

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L212">property fingerprint</a>
</h3>

```typescript
fingerprint?: pulumi.Input<string>;
```


The fingerprint of the instance group manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L216">property instanceGroup</a>
</h3>

```typescript
instanceGroup?: pulumi.Input<string>;
```


The full URL of the instance group created by the manager.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L221">property instanceTemplate</a>
</h3>

```typescript
instanceTemplate?: pulumi.Input<string>;
```


The full URL to an instance template from
which all new instances will be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L225">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the port.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L230">property namedPorts</a>
</h3>

```typescript
namedPorts?: pulumi.Input<{ ... }[]>;
```


The named port configuration. See the section below
for details on configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L235">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L239">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region where the managed instance group resides.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L243">property rollingUpdatePolicy</a>
</h3>

```typescript
rollingUpdatePolicy?: pulumi.Input<{ ... }>;
```


) The update policy for this managed instance group. Structure is documented below. For more information, see the [official documentation](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) and [API](https://cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patch)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L247">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URL of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L253">property targetPools</a>
</h3>

```typescript
targetPools?: pulumi.Input<pulumi.Input<string>[]>;
```


The full URL of all target pools to which new
instances in the group are added. Updating the target pools attribute does
not affect existing instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L259">property targetSize</a>
</h3>

```typescript
targetSize?: pulumi.Input<number>;
```


The target number of running instances for this managed
instance group. This value should always be explicitly set unless this resource is attached to
an autoscaler, in which case it should never be set. Defaults to `0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L267">property updateStrategy</a>
</h3>

```typescript
updateStrategy?: pulumi.Input<string>;
```


If the `instance_template`
resource is modified, a value of `"NONE"` will prevent any of the managed
instances from being restarted by Terraform. A value of `"ROLLING_UPDATE"`
is supported as [Beta feature]. A value of `"ROLLING_UPDATE"` requires
`rolling_update_policy` block to be set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/regionInstanceGroupManager.ts#L273">property waitForInstances</a>
</h3>

```typescript
waitForInstances?: pulumi.Input<boolean>;
```


Whether to wait for all instances to be created/updated before
returning. Note that if this is set to true and the operation does not succeed, Terraform will
continue trying until it times out.

<h2 class="pdoc-module-header" id="RouteArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L212">interface RouteArgs</a>
</h2>

The set of arguments for constructing a Route resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L213">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L218">property destRange</a>
</h3>

```typescript
destRange: pulumi.Input<string>;
```


The destination IPv4 address range that this
route applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L223">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L227">property network</a>
</h3>

```typescript
network: pulumi.Input<string>;
```


The name or self_link of the network to attach this route to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L233">property nextHopGateway</a>
</h3>

```typescript
nextHopGateway?: pulumi.Input<string>;
```


The URL of the internet gateway to route
to if this route is matched. The alias "default-internet-gateway" can also
be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L238">property nextHopInstance</a>
</h3>

```typescript
nextHopInstance?: pulumi.Input<string>;
```


The name of the VM instance to route to
if this route is matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L243">property nextHopInstanceZone</a>
</h3>

```typescript
nextHopInstanceZone?: pulumi.Input<string>;
```


The zone of the instance specified in `next_hop_instance`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L248">property nextHopIp</a>
</h3>

```typescript
nextHopIp?: pulumi.Input<string>;
```


The IP address of the next hop if this route
is matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L253">property nextHopVpnTunnel</a>
</h3>

```typescript
nextHopVpnTunnel?: pulumi.Input<string>;
```


The name of the VPN to route to if this
route is matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L257">property priority</a>
</h3>

```typescript
priority?: pulumi.Input<number>;
```


The priority of this route, used to break ties. Defaults to 1000.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L262">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L266">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The tags that this route applies to.

<h2 class="pdoc-module-header" id="RouteState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L144">interface RouteState</a>
</h2>

Input properties used for looking up and filtering Route resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L145">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L150">property destRange</a>
</h3>

```typescript
destRange?: pulumi.Input<string>;
```


The destination IPv4 address range that this
route applies to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L155">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L159">property network</a>
</h3>

```typescript
network?: pulumi.Input<string>;
```


The name or self_link of the network to attach this route to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L165">property nextHopGateway</a>
</h3>

```typescript
nextHopGateway?: pulumi.Input<string>;
```


The URL of the internet gateway to route
to if this route is matched. The alias "default-internet-gateway" can also
be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L170">property nextHopInstance</a>
</h3>

```typescript
nextHopInstance?: pulumi.Input<string>;
```


The name of the VM instance to route to
if this route is matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L175">property nextHopInstanceZone</a>
</h3>

```typescript
nextHopInstanceZone?: pulumi.Input<string>;
```


The zone of the instance specified in `next_hop_instance`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L180">property nextHopIp</a>
</h3>

```typescript
nextHopIp?: pulumi.Input<string>;
```


The IP address of the next hop if this route
is matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L184">property nextHopNetwork</a>
</h3>

```typescript
nextHopNetwork?: pulumi.Input<string>;
```


The name of the next hop network, if available.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L189">property nextHopVpnTunnel</a>
</h3>

```typescript
nextHopVpnTunnel?: pulumi.Input<string>;
```


The name of the VPN to route to if this
route is matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L193">property priority</a>
</h3>

```typescript
priority?: pulumi.Input<number>;
```


The priority of this route, used to break ties. Defaults to 1000.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L198">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L202">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/route.ts#L206">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The tags that this route applies to.

<h2 class="pdoc-module-header" id="RouterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L148">interface RouterArgs</a>
</h2>

The set of arguments for constructing a Router resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L154">property bgp</a>
</h3>

```typescript
bgp: pulumi.Input<{ ... }>;
```


BGP information specific to this router.
Changing this forces a new router to be created.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L159">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the resource.
Changing this forces a new router to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L164">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the router, required by GCE. Changing
this forces a new router to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L169">property network</a>
</h3>

```typescript
network: pulumi.Input<string>;
```


The name or resource link to the network this Cloud Router
will use to learn and announce routes. Changing this forces a new router to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L175">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
Changing this forces a new router to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L181">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region this router should sit in. If not specified,
the project region will be used. Changing this forces a new router to be
created.

<h2 class="pdoc-module-header" id="RouterInterfaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L134">interface RouterInterfaceArgs</a>
</h2>

The set of arguments for constructing a RouterInterface resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L139">property ipRange</a>
</h3>

```typescript
ipRange?: pulumi.Input<string>;
```


IP address and range of the interface. The IP range must be
in the RFC3927 link-local IP space. Changing this forces a new interface to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L144">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the interface, required by GCE. Changing
this forces a new interface to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L149">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which this interface's router belongs. If it
is not provided, the provider project is used. Changing this forces a new interface to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L155">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region this interface's router sits in. If not specified,
the project region will be used. Changing this forces a new interface to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L160">property router</a>
</h3>

```typescript
router: pulumi.Input<string>;
```


The name of the router this interface will be attached to.
Changing this forces a new interface to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L165">property vpnTunnel</a>
</h3>

```typescript
vpnTunnel: pulumi.Input<string>;
```


The name or resource link to the VPN tunnel this
interface will be linked to. Changing this forces a new interface to be created.

<h2 class="pdoc-module-header" id="RouterInterfaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L97">interface RouterInterfaceState</a>
</h2>

Input properties used for looking up and filtering RouterInterface resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L102">property ipRange</a>
</h3>

```typescript
ipRange?: pulumi.Input<string>;
```


IP address and range of the interface. The IP range must be
in the RFC3927 link-local IP space. Changing this forces a new interface to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L107">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the interface, required by GCE. Changing
this forces a new interface to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L112">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which this interface's router belongs. If it
is not provided, the provider project is used. Changing this forces a new interface to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L118">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region this interface's router sits in. If not specified,
the project region will be used. Changing this forces a new interface to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L123">property router</a>
</h3>

```typescript
router?: pulumi.Input<string>;
```


The name of the router this interface will be attached to.
Changing this forces a new interface to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerInterface.ts#L128">property vpnTunnel</a>
</h3>

```typescript
vpnTunnel?: pulumi.Input<string>;
```


The name or resource link to the VPN tunnel this
interface will be linked to. Changing this forces a new interface to be created.

<h2 class="pdoc-module-header" id="RouterPeerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L171">interface RouterPeerArgs</a>
</h2>

The set of arguments for constructing a RouterPeer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L176">property advertisedRoutePriority</a>
</h3>

```typescript
advertisedRoutePriority?: pulumi.Input<number>;
```


The priority of routes advertised to this BGP peer.
Changing this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L181">property interface</a>
</h3>

```typescript
interface: pulumi.Input<string>;
```


The name of the interface the BGP peer is associated with.
Changing this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L186">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for BGP peer, required by GCE. Changing
this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L191">property peerAsn</a>
</h3>

```typescript
peerAsn: pulumi.Input<number>;
```


Peer BGP Autonomous System Number (ASN).
Changing this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L196">property peerIpAddress</a>
</h3>

```typescript
peerIpAddress?: pulumi.Input<string>;
```


IP address of the BGP interface outside Google Cloud.
Changing this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L201">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which this peer's router belongs. If it
is not provided, the provider project is used. Changing this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L207">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region this peer's router sits in. If not specified,
the project region will be used. Changing this forces a new peer to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L212">property router</a>
</h3>

```typescript
router: pulumi.Input<string>;
```


The name of the router in which this BGP peer will be configured.
Changing this forces a new peer to be created.

<h2 class="pdoc-module-header" id="RouterPeerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L120">interface RouterPeerState</a>
</h2>

Input properties used for looking up and filtering RouterPeer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L125">property advertisedRoutePriority</a>
</h3>

```typescript
advertisedRoutePriority?: pulumi.Input<number>;
```


The priority of routes advertised to this BGP peer.
Changing this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L130">property interface</a>
</h3>

```typescript
interface?: pulumi.Input<string>;
```


The name of the interface the BGP peer is associated with.
Changing this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L134">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


IP address of the interface inside Google Cloud Platform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L139">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for BGP peer, required by GCE. Changing
this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L144">property peerAsn</a>
</h3>

```typescript
peerAsn?: pulumi.Input<number>;
```


Peer BGP Autonomous System Number (ASN).
Changing this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L149">property peerIpAddress</a>
</h3>

```typescript
peerIpAddress?: pulumi.Input<string>;
```


IP address of the BGP interface outside Google Cloud.
Changing this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L154">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which this peer's router belongs. If it
is not provided, the provider project is used. Changing this forces a new peer to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L160">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region this peer's router sits in. If not specified,
the project region will be used. Changing this forces a new peer to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/routerPeer.ts#L165">property router</a>
</h3>

```typescript
router?: pulumi.Input<string>;
```


The name of the router in which this BGP peer will be configured.
Changing this forces a new peer to be created.

<h2 class="pdoc-module-header" id="RouterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L105">interface RouterState</a>
</h2>

Input properties used for looking up and filtering Router resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L111">property bgp</a>
</h3>

```typescript
bgp?: pulumi.Input<{ ... }>;
```


BGP information specific to this router.
Changing this forces a new router to be created.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L116">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the resource.
Changing this forces a new router to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L121">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the router, required by GCE. Changing
this forces a new router to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L126">property network</a>
</h3>

```typescript
network?: pulumi.Input<string>;
```


The name or resource link to the network this Cloud Router
will use to learn and announce routes. Changing this forces a new router to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L132">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
Changing this forces a new router to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L138">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region this router should sit in. If not specified,
the project region will be used. Changing this forces a new router to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/router.ts#L142">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h2 class="pdoc-module-header" id="SSLCertificateArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L155">interface SSLCertificateArgs</a>
</h2>

The set of arguments for constructing a SSLCertificate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L161">property certificate</a>
</h3>

```typescript
certificate: pulumi.Input<string>;
```


A local certificate file in PEM format. The chain
may be at most 5 certs long, and must include at least one intermediate
cert. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L166">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


An optional description of this resource.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L171">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the SSL certificate. If you leave
this blank, Terraform will auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L176">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L181">property privateKey</a>
</h3>

```typescript
privateKey: pulumi.Input<string>;
```


Write only private key in PEM format.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L186">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="SSLCertificateState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L110">interface SSLCertificateState</a>
</h2>

Input properties used for looking up and filtering SSLCertificate resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L116">property certificate</a>
</h3>

```typescript
certificate?: pulumi.Input<string>;
```


A local certificate file in PEM format. The chain
may be at most 5 certs long, and must include at least one intermediate
cert. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L120">property certificateId</a>
</h3>

```typescript
certificateId?: pulumi.Input<string>;
```


A unique ID for the certificate, assigned by GCE.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L125">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


An optional description of this resource.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L130">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the SSL certificate. If you leave
this blank, Terraform will auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L135">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L140">property privateKey</a>
</h3>

```typescript
privateKey?: pulumi.Input<string>;
```


Write only private key in PEM format.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L145">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sSLCertificate.ts#L149">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h2 class="pdoc-module-header" id="SharedVPCHostProjectArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCHostProject.ts#L70">interface SharedVPCHostProjectArgs</a>
</h2>

The set of arguments for constructing a SharedVPCHostProject resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCHostProject.ts#L74">property project</a>
</h3>

```typescript
project: pulumi.Input<string>;
```


The ID of the project that will serve as a Shared VPC host project

<h2 class="pdoc-module-header" id="SharedVPCHostProjectState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCHostProject.ts#L60">interface SharedVPCHostProjectState</a>
</h2>

Input properties used for looking up and filtering SharedVPCHostProject resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCHostProject.ts#L64">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project that will serve as a Shared VPC host project

<h2 class="pdoc-module-header" id="SharedVPCServiceProjectArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCServiceProject.ts#L84">interface SharedVPCServiceProjectArgs</a>
</h2>

The set of arguments for constructing a SharedVPCServiceProject resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCServiceProject.ts#L88">property hostProject</a>
</h3>

```typescript
hostProject: pulumi.Input<string>;
```


The ID of a host project to associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCServiceProject.ts#L92">property serviceProject</a>
</h3>

```typescript
serviceProject: pulumi.Input<string>;
```


The ID of the project that will serve as a Shared VPC service project.

<h2 class="pdoc-module-header" id="SharedVPCServiceProjectState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCServiceProject.ts#L70">interface SharedVPCServiceProjectState</a>
</h2>

Input properties used for looking up and filtering SharedVPCServiceProject resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCServiceProject.ts#L74">property hostProject</a>
</h3>

```typescript
hostProject?: pulumi.Input<string>;
```


The ID of a host project to associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/sharedVPCServiceProject.ts#L78">property serviceProject</a>
</h3>

```typescript
serviceProject?: pulumi.Input<string>;
```


The ID of the project that will serve as a Shared VPC service project.

<h2 class="pdoc-module-header" id="SnapshotArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L205">interface SnapshotArgs</a>
</h2>

The set of arguments for constructing a Snapshot resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L209">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A set of key/value label pairs to assign to the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L214">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L219">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L226">property snapshotEncryptionKeyRaw</a>
</h3>

```typescript
snapshotEncryptionKeyRaw?: pulumi.Input<string>;
```


A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L230">property sourceDisk</a>
</h3>

```typescript
sourceDisk: pulumi.Input<string>;
```


The disk which will be used as the source of the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L237">property sourceDiskEncryptionKeyRaw</a>
</h3>

```typescript
sourceDiskEncryptionKeyRaw?: pulumi.Input<string>;
```


A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to decrypt the source disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L241">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone where the source disk is located.

<h2 class="pdoc-module-header" id="SnapshotState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L137">interface SnapshotState</a>
</h2>

Input properties used for looking up and filtering Snapshot resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L141">property labelFingerprint</a>
</h3>

```typescript
labelFingerprint?: pulumi.Input<string>;
```


The unique fingerprint of the labels.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L145">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A set of key/value label pairs to assign to the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L150">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L155">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L159">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L166">property snapshotEncryptionKeyRaw</a>
</h3>

```typescript
snapshotEncryptionKeyRaw?: pulumi.Input<string>;
```


A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L173">property snapshotEncryptionKeySha256</a>
</h3>

```typescript
snapshotEncryptionKeySha256?: pulumi.Input<string>;
```


The [RFC 4648 base64]
(https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the
[customer-supplied encryption key](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
that protects this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L177">property sourceDisk</a>
</h3>

```typescript
sourceDisk?: pulumi.Input<string>;
```


The disk which will be used as the source of the snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L184">property sourceDiskEncryptionKeyRaw</a>
</h3>

```typescript
sourceDiskEncryptionKeyRaw?: pulumi.Input<string>;
```


A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to decrypt the source disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L191">property sourceDiskEncryptionKeySha256</a>
</h3>

```typescript
sourceDiskEncryptionKeySha256?: pulumi.Input<string>;
```


The [RFC 4648 base64]
(https://tools.ietf.org/html/rfc4648#section-4) encoded SHA-256 hash of the
[customer-supplied encryption key](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
that protects the source disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L195">property sourceDiskLink</a>
</h3>

```typescript
sourceDiskLink?: pulumi.Input<string>;
```


The URI of the source disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/snapshot.ts#L199">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone where the source disk is located.

<h2 class="pdoc-module-header" id="SubnetworkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L192">interface SubnetworkArgs</a>
</h2>

The set of arguments for constructing a Subnetwork resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L196">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of this subnetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L202">property enableFlowLogs</a>
</h3>

```typescript
enableFlowLogs?: pulumi.Input<boolean>;
```


)
Set to `true` to enable [flow logs](https://cloud.google.com/vpc/docs/using-flow-logs)
for this subnetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L206">property ipCidrRange</a>
</h3>

```typescript
ipCidrRange: pulumi.Input<string>;
```


The range of IP addresses belonging to this subnetwork secondary range. Ranges must be unique and non-overlapping with all primary and secondary IP ranges within a network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L211">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L217">property network</a>
</h3>

```typescript
network: pulumi.Input<string>;
```


The network name or resource link to the parent
network of this subnetwork. The parent network must have been created
in custom subnet mode.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L223">property privateIpGoogleAccess</a>
</h3>

```typescript
privateIpGoogleAccess?: pulumi.Input<boolean>;
```


Whether the VMs in this subnet
can access Google services without assigned external IP
addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L228">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L233">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region this subnetwork will be created in. If
unspecified, this defaults to the region configured in the provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L237">property secondaryIpRanges</a>
</h3>

```typescript
secondaryIpRanges?: pulumi.Input<{ ... }[]>;
```


) An array of configurations for secondary IP ranges for VM instances contained in this subnetwork. Structure is documented below.

<h2 class="pdoc-module-header" id="SubnetworkState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L132">interface SubnetworkState</a>
</h2>

Input properties used for looking up and filtering Subnetwork resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L136">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of this subnetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L142">property enableFlowLogs</a>
</h3>

```typescript
enableFlowLogs?: pulumi.Input<boolean>;
```


)
Set to `true` to enable [flow logs](https://cloud.google.com/vpc/docs/using-flow-logs)
for this subnetwork.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L143">property fingerprint</a>
</h3>

```typescript
fingerprint?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L147">property gatewayAddress</a>
</h3>

```typescript
gatewayAddress?: pulumi.Input<string>;
```


The IP address of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L151">property ipCidrRange</a>
</h3>

```typescript
ipCidrRange?: pulumi.Input<string>;
```


The range of IP addresses belonging to this subnetwork secondary range. Ranges must be unique and non-overlapping with all primary and secondary IP ranges within a network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L156">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L162">property network</a>
</h3>

```typescript
network?: pulumi.Input<string>;
```


The network name or resource link to the parent
network of this subnetwork. The parent network must have been created
in custom subnet mode.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L168">property privateIpGoogleAccess</a>
</h3>

```typescript
privateIpGoogleAccess?: pulumi.Input<boolean>;
```


Whether the VMs in this subnet
can access Google services without assigned external IP
addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L173">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L178">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region this subnetwork will be created in. If
unspecified, this defaults to the region configured in the provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L182">property secondaryIpRanges</a>
</h3>

```typescript
secondaryIpRanges?: pulumi.Input<{ ... }[]>;
```


) An array of configurations for secondary IP ranges for VM instances contained in this subnetwork. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/subnetwork.ts#L186">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h2 class="pdoc-module-header" id="TargetHttpProxyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L93">interface TargetHttpProxyArgs</a>
</h2>

The set of arguments for constructing a TargetHttpProxy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L94">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L95">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L100">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L101">property urlMap</a>
</h3>

```typescript
urlMap: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="TargetHttpProxyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L73">interface TargetHttpProxyState</a>
</h2>

Input properties used for looking up and filtering TargetHttpProxy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L74">property creationTimestamp</a>
</h3>

```typescript
creationTimestamp?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L75">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L76">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L81">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L82">property proxyId</a>
</h3>

```typescript
proxyId?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L86">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpProxy.ts#L87">property urlMap</a>
</h3>

```typescript
urlMap?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="TargetHttpsProxyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L104">interface TargetHttpsProxyArgs</a>
</h2>

The set of arguments for constructing a TargetHttpsProxy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L105">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L106">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L111">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L112">property sslCertificates</a>
</h3>

```typescript
sslCertificates: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L113">property sslPolicy</a>
</h3>

```typescript
sslPolicy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L114">property urlMap</a>
</h3>

```typescript
urlMap: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="TargetHttpsProxyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L82">interface TargetHttpsProxyState</a>
</h2>

Input properties used for looking up and filtering TargetHttpsProxy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L83">property creationTimestamp</a>
</h3>

```typescript
creationTimestamp?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L84">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L85">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L90">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L91">property proxyId</a>
</h3>

```typescript
proxyId?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L95">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L96">property sslCertificates</a>
</h3>

```typescript
sslCertificates?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L97">property sslPolicy</a>
</h3>

```typescript
sslPolicy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetHttpsProxy.ts#L98">property urlMap</a>
</h3>

```typescript
urlMap?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="TargetPoolArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L180">interface TargetPoolArgs</a>
</h2>

The set of arguments for constructing a TargetPool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L185">property backupPool</a>
</h3>

```typescript
backupPool?: pulumi.Input<string>;
```


URL to the backup target pool. Must also set
failover\_ratio.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L189">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Textual description field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L194">property failoverRatio</a>
</h3>

```typescript
failoverRatio?: pulumi.Input<number>;
```


Ratio (0 to 1) of failed nodes before using the
backup pool (which must also be set).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L199">property healthChecks</a>
</h3>

```typescript
healthChecks?: pulumi.Input<pulumi.Input<string>>;
```


List of zero or one health check name or self_link. Only
legacy `google_compute_http_health_check` is supported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L207">property instances</a>
</h3>

```typescript
instances?: pulumi.Input<pulumi.Input<string>[]>;
```


List of instances in the pool. They can be given as
URLs, or in the form of "zone/name". Note that the instances need not exist
at the time of target pool creation, so there is no need to use the
Terraform interpolators to create a dependency on the instances from the
target pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L212">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L217">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L222">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


Where the target pool resides. Defaults to project
region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L228">property sessionAffinity</a>
</h3>

```typescript
sessionAffinity?: pulumi.Input<string>;
```


How to distribute load. Options are "NONE" (no
affinity). "CLIENT\_IP" (hash of the source/dest addresses / ports), and
"CLIENT\_IP\_PROTO" also includes the protocol (default "NONE").

<h2 class="pdoc-module-header" id="TargetPoolState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L122">interface TargetPoolState</a>
</h2>

Input properties used for looking up and filtering TargetPool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L127">property backupPool</a>
</h3>

```typescript
backupPool?: pulumi.Input<string>;
```


URL to the backup target pool. Must also set
failover\_ratio.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L131">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Textual description field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L136">property failoverRatio</a>
</h3>

```typescript
failoverRatio?: pulumi.Input<number>;
```


Ratio (0 to 1) of failed nodes before using the
backup pool (which must also be set).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L141">property healthChecks</a>
</h3>

```typescript
healthChecks?: pulumi.Input<pulumi.Input<string>>;
```


List of zero or one health check name or self_link. Only
legacy `google_compute_http_health_check` is supported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L149">property instances</a>
</h3>

```typescript
instances?: pulumi.Input<pulumi.Input<string>[]>;
```


List of instances in the pool. They can be given as
URLs, or in the form of "zone/name". Note that the instances need not exist
at the time of target pool creation, so there is no need to use the
Terraform interpolators to create a dependency on the instances from the
target pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L154">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L159">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L164">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


Where the target pool resides. Defaults to project
region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L168">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetPool.ts#L174">property sessionAffinity</a>
</h3>

```typescript
sessionAffinity?: pulumi.Input<string>;
```


How to distribute load. Options are "NONE" (no
affinity). "CLIENT\_IP" (hash of the source/dest addresses / ports), and
"CLIENT\_IP\_PROTO" also includes the protocol (default "NONE").

<h2 class="pdoc-module-header" id="TargetSSLProxyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L104">interface TargetSSLProxyArgs</a>
</h2>

The set of arguments for constructing a TargetSSLProxy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L105">property backendService</a>
</h3>

```typescript
backendService: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L106">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L107">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L112">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L113">property proxyHeader</a>
</h3>

```typescript
proxyHeader?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L114">property sslCertificates</a>
</h3>

```typescript
sslCertificates: pulumi.Input<pulumi.Input<string>>;
```

<h2 class="pdoc-module-header" id="TargetSSLProxyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L82">interface TargetSSLProxyState</a>
</h2>

Input properties used for looking up and filtering TargetSSLProxy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L83">property backendService</a>
</h3>

```typescript
backendService?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L84">property creationTimestamp</a>
</h3>

```typescript
creationTimestamp?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L85">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L86">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L91">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L92">property proxyHeader</a>
</h3>

```typescript
proxyHeader?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L93">property proxyId</a>
</h3>

```typescript
proxyId?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L97">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetSSLProxy.ts#L98">property sslCertificates</a>
</h3>

```typescript
sslCertificates?: pulumi.Input<pulumi.Input<string>>;
```

<h2 class="pdoc-module-header" id="TargetTCPProxyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L97">interface TargetTCPProxyArgs</a>
</h2>

The set of arguments for constructing a TargetTCPProxy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L98">property backendService</a>
</h3>

```typescript
backendService: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L99">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L100">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L105">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L106">property proxyHeader</a>
</h3>

```typescript
proxyHeader?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="TargetTCPProxyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L76">interface TargetTCPProxyState</a>
</h2>

Input properties used for looking up and filtering TargetTCPProxy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L77">property backendService</a>
</h3>

```typescript
backendService?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L78">property creationTimestamp</a>
</h3>

```typescript
creationTimestamp?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L79">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L80">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L85">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L86">property proxyHeader</a>
</h3>

```typescript
proxyHeader?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L87">property proxyId</a>
</h3>

```typescript
proxyId?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/targetTCPProxy.ts#L91">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h2 class="pdoc-module-header" id="URLMapArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L160">interface URLMapArgs</a>
</h2>

The set of arguments for constructing a URLMap resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L164">property defaultService</a>
</h3>

```typescript
defaultService: pulumi.Input<string>;
```


The backend service or backend bucket to use if none of the given paths match.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L168">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


An optional description of this test.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L172">property hostRules</a>
</h3>

```typescript
hostRules?: pulumi.Input<{ ... }[]>;
```


A list of host rules. Multiple blocks of this type are permitted. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L176">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the `path_matcher` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L180">property pathMatchers</a>
</h3>

```typescript
pathMatchers?: pulumi.Input<{ ... }[]>;
```


The name of the `path_matcher` to apply this host rule to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L185">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L189">property tests</a>
</h3>

```typescript
tests?: pulumi.Input<{ ... }[]>;
```


The test to perform.  Multiple blocks of this type are permitted. Structure is documented below.

<h2 class="pdoc-module-header" id="URLMapState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L113">interface URLMapState</a>
</h2>

Input properties used for looking up and filtering URLMap resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L117">property defaultService</a>
</h3>

```typescript
defaultService?: pulumi.Input<string>;
```


The backend service or backend bucket to use if none of the given paths match.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L121">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


An optional description of this test.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L125">property fingerprint</a>
</h3>

```typescript
fingerprint?: pulumi.Input<string>;
```


The unique fingerprint for this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L129">property hostRules</a>
</h3>

```typescript
hostRules?: pulumi.Input<{ ... }[]>;
```


A list of host rules. Multiple blocks of this type are permitted. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L133">property mapId</a>
</h3>

```typescript
mapId?: pulumi.Input<string>;
```


The GCE assigned ID of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L137">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the `path_matcher` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L141">property pathMatchers</a>
</h3>

```typescript
pathMatchers?: pulumi.Input<{ ... }[]>;
```


The name of the `path_matcher` to apply this host rule to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L146">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L150">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/uRLMap.ts#L154">property tests</a>
</h3>

```typescript
tests?: pulumi.Input<{ ... }[]>;
```


The test to perform.  Multiple blocks of this type are permitted. Structure is documented below.

<h2 class="pdoc-module-header" id="VPNGatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L93">interface VPNGatewayArgs</a>
</h2>

The set of arguments for constructing a VPNGateway resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L94">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L95">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L96">property network</a>
</h3>

```typescript
network: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L101">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L102">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="VPNGatewayState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L73">interface VPNGatewayState</a>
</h2>

Input properties used for looking up and filtering VPNGateway resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L74">property creationTimestamp</a>
</h3>

```typescript
creationTimestamp?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L75">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L76">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L77">property network</a>
</h3>

```typescript
network?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L82">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L83">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNGateway.ts#L87">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h2 class="pdoc-module-header" id="VPNTunnelArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L228">interface VPNTunnelArgs</a>
</h2>

The set of arguments for constructing a VPNTunnel resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L233">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the resource. Changing this forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L238">property ikeVersion</a>
</h3>

```typescript
ikeVersion?: pulumi.Input<number>;
```


Either version 1 or 2. Default is 2. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L245">property localTrafficSelectors</a>
</h3>

```typescript
localTrafficSelectors?: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies which CIDR ranges are
announced to the VPN peer. Mandatory if the VPN gateway is attached to a
custom subnetted network. Refer to Google documentation for more
information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L250">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L255">property peerIp</a>
</h3>

```typescript
peerIp: pulumi.Input<string>;
```


The VPN gateway sitting outside of GCE. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L260">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L266">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region this tunnel should sit in. If not specified,
the project region will be used. Changing this forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L273">property remoteTrafficSelectors</a>
</h3>

```typescript
remoteTrafficSelectors?: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies which CIDR ranges the VPN
tunnel can route to the remote side. Mandatory if the VPN gateway is attached to a
custom subnetted network. Refer to Google documentation for more
information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L279">property router</a>
</h3>

```typescript
router?: pulumi.Input<string>;
```


Name of a Cloud Router in the same region
to be used for dynamic routing. Refer to Google documentation for more
information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L284">property sharedSecret</a>
</h3>

```typescript
sharedSecret: pulumi.Input<string>;
```


A passphrase shared between the two VPN gateways.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L289">property targetVpnGateway</a>
</h3>

```typescript
targetVpnGateway: pulumi.Input<string>;
```


A link to the VPN gateway sitting inside
GCE. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="VPNTunnelState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L153">interface VPNTunnelState</a>
</h2>

Input properties used for looking up and filtering VPNTunnel resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L158">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the resource. Changing this forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L162">property detailedStatus</a>
</h3>

```typescript
detailedStatus?: pulumi.Input<string>;
```


Information about the status of the VPN tunnel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L167">property ikeVersion</a>
</h3>

```typescript
ikeVersion?: pulumi.Input<number>;
```


Either version 1 or 2. Default is 2. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L174">property localTrafficSelectors</a>
</h3>

```typescript
localTrafficSelectors?: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies which CIDR ranges are
announced to the VPN peer. Mandatory if the VPN gateway is attached to a
custom subnetted network. Refer to Google documentation for more
information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L179">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L184">property peerIp</a>
</h3>

```typescript
peerIp?: pulumi.Input<string>;
```


The VPN gateway sitting outside of GCE. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L189">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L195">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region this tunnel should sit in. If not specified,
the project region will be used. Changing this forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L202">property remoteTrafficSelectors</a>
</h3>

```typescript
remoteTrafficSelectors?: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies which CIDR ranges the VPN
tunnel can route to the remote side. Mandatory if the VPN gateway is attached to a
custom subnetted network. Refer to Google documentation for more
information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L208">property router</a>
</h3>

```typescript
router?: pulumi.Input<string>;
```


Name of a Cloud Router in the same region
to be used for dynamic routing. Refer to Google documentation for more
information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L212">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L217">property sharedSecret</a>
</h3>

```typescript
sharedSecret?: pulumi.Input<string>;
```


A passphrase shared between the two VPN gateways.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/compute/vPNTunnel.ts#L222">property targetVpnGateway</a>
</h3>

```typescript
targetVpnGateway?: pulumi.Input<string>;
```


A link to the VPN gateway sitting inside
GCE. Changing this forces a new resource to be created.

