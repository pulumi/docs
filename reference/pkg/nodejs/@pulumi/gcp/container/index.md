---
title: Module container
---

<a href="../index.html">@pulumi/gcp</a> &gt; container

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Cluster">class Cluster</a>
* <a href="#NodePool">class NodePool</a>
* <a href="#getCluster">function getCluster</a>
* <a href="#getEngineVersions">function getEngineVersions</a>
* <a href="#getRegistryImage">function getRegistryImage</a>
* <a href="#getRegistryRepository">function getRegistryRepository</a>
* <a href="#ClusterArgs">interface ClusterArgs</a>
* <a href="#ClusterState">interface ClusterState</a>
* <a href="#GetClusterArgs">interface GetClusterArgs</a>
* <a href="#GetClusterResult">interface GetClusterResult</a>
* <a href="#GetEngineVersionsArgs">interface GetEngineVersionsArgs</a>
* <a href="#GetEngineVersionsResult">interface GetEngineVersionsResult</a>
* <a href="#GetRegistryImageArgs">interface GetRegistryImageArgs</a>
* <a href="#GetRegistryImageResult">interface GetRegistryImageResult</a>
* <a href="#GetRegistryRepositoryArgs">interface GetRegistryRepositoryArgs</a>
* <a href="#GetRegistryRepositoryResult">interface GetRegistryRepositoryResult</a>
* <a href="#NodePoolArgs">interface NodePoolArgs</a>
* <a href="#NodePoolState">interface NodePoolState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts">container/cluster.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts">container/getCluster.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts">container/getEngineVersions.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts">container/getRegistryImage.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryRepository.ts">container/getRegistryRepository.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts">container/nodePool.ts</a> 


<h2 class="pdoc-module-header" id="Cluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L15">class Cluster</a>
</h2>

Creates a Google Kubernetes Engine (GKE) cluster. For more information see
[the official documentation](https://cloud.google.com/container-engine/docs/clusters)
and
[API](https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters).

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L204">constructor</a>
</h3>

```typescript
new Cluster(name: string, args?: ClusterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Cluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterState): Cluster
```


Get an existing Cluster resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L34">property additionalZones</a>
</h3>

```typescript
public additionalZones: pulumi.Output<string[]>;
```


The list of additional Google Compute Engine
locations in which the cluster's nodes should be located. If additional zones are
configured, the number of nodes specified in `initial_node_count` is created in
all specified zones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L39">property addonsConfig</a>
</h3>

```typescript
public addonsConfig: pulumi.Output<{ ... }>;
```


The configuration for addons supported by GKE.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L44">property clusterIpv4Cidr</a>
</h3>

```typescript
public clusterIpv4Cidr: pulumi.Output<string>;
```


The IP address range of the kubernetes pods in
this cluster. Default is an automatically assigned CIDR.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L48">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L54">property enableKubernetesAlpha</a>
</h3>

```typescript
public enableKubernetesAlpha: pulumi.Output<boolean | undefined>;
```


Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L61">property enableLegacyAbac</a>
</h3>

```typescript
public enableLegacyAbac: pulumi.Output<boolean | undefined>;
```


Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L65">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The IP address of this cluster's Kubernetes master.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L70">property initialNodeCount</a>
</h3>

```typescript
public initialNodeCount: pulumi.Output<number | undefined>;
```


The number of nodes to create in this
cluster (not including the Kubernetes master). Must be set if `node_pool` is not set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L75">property instanceGroupUrls</a>
</h3>

```typescript
public instanceGroupUrls: pulumi.Output<string[]>;
```


List of instance group URLs which have been assigned
to the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L81">property ipAllocationPolicy</a>
</h3>

```typescript
public ipAllocationPolicy: pulumi.Output<{ ... } | undefined>;
```


Configuration for cluster IP allocation. As of now, only pre-allocated subnetworks (custom type with secondary ranges) are supported.
This will activate IP aliases. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases)
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L87">property loggingService</a>
</h3>

```typescript
public loggingService: pulumi.Output<string>;
```


The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`,
`logging.googleapis.com/kubernetes` (beta), and `none`. Defaults to `logging.googleapis.com`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L92">property maintenancePolicy</a>
</h3>

```typescript
public maintenancePolicy: pulumi.Output<{ ... } | undefined>;
```


The maintenance policy to use for the cluster. Structure is
documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L97">property masterAuth</a>
</h3>

```typescript
public masterAuth: pulumi.Output<{ ... }>;
```


The authentication information for accessing the
Kubernetes master. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L103">property masterAuthorizedNetworksConfig</a>
</h3>

```typescript
public masterAuthorizedNetworksConfig: pulumi.Output<{ ... } | undefined>;
```


The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L109">property masterIpv4CidrBlock</a>
</h3>

```typescript
public masterIpv4CidrBlock: pulumi.Output<string | undefined>;
```


) Specifies a private
[RFC1918](https://tools.ietf.org/html/rfc1918) block for the master's VPC. The master range must not overlap with any subnet in your cluster's VPC.
The master and your cluster use VPC peering. Must be specified in CIDR notation and must be `/28` subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L115">property masterVersion</a>
</h3>

```typescript
public masterVersion: pulumi.Output<string>;
```


The current version of the master in the cluster. This may
be different than the `min_master_version` set in the config if the master
has been updated by GKE.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L123">property minMasterVersion</a>
</h3>

```typescript
public minMasterVersion: pulumi.Output<string | undefined>;
```


The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version--use the read-only `master_version` field to obtain that.
If unset, the cluster's version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L133">property monitoringService</a>
</h3>

```typescript
public monitoringService: pulumi.Output<string>;
```


The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
`monitoring.googleapis.com`, `monitoring.googleapis.com/kubernetes` (beta) and `none`.
Defaults to `monitoring.googleapis.com`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L138">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the cluster, unique within the project and
zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L144">property network</a>
</h3>

```typescript
public network: pulumi.Output<string | undefined>;
```


The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L150">property networkPolicy</a>
</h3>

```typescript
public networkPolicy: pulumi.Output<{ ... }>;
```


Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L155">property nodeConfig</a>
</h3>

```typescript
public nodeConfig: pulumi.Output<{ ... }>;
```


Parameters used in creating the cluster's nodes.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L160">property nodePools</a>
</h3>

```typescript
public nodePools: pulumi.Output<{ ... }[]>;
```


List of node pools associated with this cluster.
See [google_container_node_pool](container_node_pool.html) for schema.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L166">property nodeVersion</a>
</h3>

```typescript
public nodeVersion: pulumi.Output<string>;
```


The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L172">property podSecurityPolicyConfig</a>
</h3>

```typescript
public podSecurityPolicyConfig: pulumi.Output<{ ... } | undefined>;
```


) Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L179">property privateCluster</a>
</h3>

```typescript
public privateCluster: pulumi.Output<boolean | undefined>;
```


) If true, a
[private cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters) will be created, meaning
nodes do not get public IP addresses. It is mandatory to specify `master_ipv4_cidr_block` and
`ip_allocation_policy` with this option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L184">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L185">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L189">property removeDefaultNodePool</a>
</h3>

```typescript
public removeDefaultNodePool: pulumi.Output<boolean | undefined>;
```


If true, deletes the default node pool upon cluster creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L193">property resourceLabels</a>
</h3>

```typescript
public resourceLabels: pulumi.Output<{ ... } | undefined>;
```


The GCE resource labels (a map of key/value pairs) to be applied to the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L198">property subnetwork</a>
</h3>

```typescript
public subnetwork: pulumi.Output<string>;
```


The name or self_link of the Google Compute Engine subnetwork in
which the cluster's instances are launched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L204">property zone</a>
</h3>

```typescript
public zone: pulumi.Output<string>;
```


The zone that the master and the number of nodes specified
in `initial_node_count` should be created in. Only one of `zone` and `region`
may be set. If neither zone nor region are set, the provider zone is used.

<h2 class="pdoc-module-header" id="NodePool">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L12">class NodePool</a>
</h2>

Manages a Node Pool resource within GKE. For more information see
[the official documentation](https://cloud.google.com/container-engine/docs/node-pools)
and
[API](https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters.nodePools).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L83">constructor</a>
</h3>

```typescript
new NodePool(name: string, args: NodePoolArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NodePool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NodePoolState): NodePool
```


Get an existing NodePool resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L29">property autoscaling</a>
</h3>

```typescript
public autoscaling: pulumi.Output<{ ... } | undefined>;
```


Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L33">property cluster</a>
</h3>

```typescript
public cluster: pulumi.Output<string>;
```


The cluster to create the node pool for.  Cluster must be present in `zone` provided for zonal clusters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L38">property initialNodeCount</a>
</h3>

```typescript
public initialNodeCount: pulumi.Output<number>;
```


The initial node count for the pool. Changing this will force
recreation of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L39">property instanceGroupUrls</a>
</h3>

```typescript
public instanceGroupUrls: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L44">property management</a>
</h3>

```typescript
public management: pulumi.Output<{ ... }>;
```


Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L49">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the node pool. If left blank, Terraform will
auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L54">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string>;
```


Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L59">property nodeConfig</a>
</h3>

```typescript
public nodeConfig: pulumi.Output<{ ... }>;
```


The node configuration of the pool. See
[google_container_cluster](container_cluster.html) for schema.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L64">property nodeCount</a>
</h3>

```typescript
public nodeCount: pulumi.Output<number>;
```


The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L69">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L73">property region</a>
</h3>

```typescript
public region: pulumi.Output<string | undefined>;
```


The region in which the cluster resides (for regional clusters).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L79">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L83">property zone</a>
</h3>

```typescript
public zone: pulumi.Output<string>;
```


The zone in which the cluster resides.

<h2 class="pdoc-module-header" id="getCluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L9">function getCluster</a>
</h2>

```typescript
getCluster(args: GetClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterResult>
```


Get info about a cluster within GKE from its name and zone.

<h2 class="pdoc-module-header" id="getEngineVersions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L27">function getEngineVersions</a>
</h2>

```typescript
getEngineVersions(args?: GetEngineVersionsArgs, opts?: pulumi.InvokeOptions): Promise<GetEngineVersionsResult>
```


Provides access to available Google Container Engine versions in a zone for a given project.

```hcl
data "google_container_engine_versions" "central1b" {
  zone = "us-central1-b"
}

resource "google_container_cluster" "foo" {
  name               = "terraform-test-cluster"
  zone               = "us-central1-b"
  node_version       = "${data.google_container_engine_versions.central1b.latest_node_version}"
  initial_node_count = 1

  master_auth {
    username = "mr.yoda"
    password = "adoy.rm"
  }
}
```

<h2 class="pdoc-module-header" id="getRegistryImage">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L11">function getRegistryImage</a>
</h2>

```typescript
getRegistryImage(args: GetRegistryImageArgs, opts?: pulumi.InvokeOptions): Promise<GetRegistryImageResult>
```


This data source fetches the project name, and provides the appropriate URLs to use for container registry for this project.

The URLs are computed entirely offline - as long as the project exists, they will be valid, but this data source does not contact Google Container Registry (GCR) at any point.

<h2 class="pdoc-module-header" id="getRegistryRepository">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryRepository.ts#L11">function getRegistryRepository</a>
</h2>

```typescript
getRegistryRepository(args?: GetRegistryRepositoryArgs, opts?: pulumi.InvokeOptions): Promise<GetRegistryRepositoryResult>
```


This data source fetches the project name, and provides the appropriate URLs to use for container registry for this project.

The URLs are computed entirely offline - as long as the project exists, they will be valid, but this data source does not contact Google Container Registry (GCR) at any point.

<h2 class="pdoc-module-header" id="ClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L475">interface ClusterArgs</a>
</h2>

The set of arguments for constructing a Cluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L482">property additionalZones</a>
</h3>

```typescript
additionalZones?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of additional Google Compute Engine
locations in which the cluster's nodes should be located. If additional zones are
configured, the number of nodes specified in `initial_node_count` is created in
all specified zones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L487">property addonsConfig</a>
</h3>

```typescript
addonsConfig?: pulumi.Input<{ ... }>;
```


The configuration for addons supported by GKE.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L492">property clusterIpv4Cidr</a>
</h3>

```typescript
clusterIpv4Cidr?: pulumi.Input<string>;
```


The IP address range of the kubernetes pods in
this cluster. Default is an automatically assigned CIDR.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L496">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L502">property enableKubernetesAlpha</a>
</h3>

```typescript
enableKubernetesAlpha?: pulumi.Input<boolean>;
```


Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L509">property enableLegacyAbac</a>
</h3>

```typescript
enableLegacyAbac?: pulumi.Input<boolean>;
```


Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L514">property initialNodeCount</a>
</h3>

```typescript
initialNodeCount?: pulumi.Input<number>;
```


The number of nodes to create in this
cluster (not including the Kubernetes master). Must be set if `node_pool` is not set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L520">property ipAllocationPolicy</a>
</h3>

```typescript
ipAllocationPolicy?: pulumi.Input<{ ... }>;
```


Configuration for cluster IP allocation. As of now, only pre-allocated subnetworks (custom type with secondary ranges) are supported.
This will activate IP aliases. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases)
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L526">property loggingService</a>
</h3>

```typescript
loggingService?: pulumi.Input<string>;
```


The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`,
`logging.googleapis.com/kubernetes` (beta), and `none`. Defaults to `logging.googleapis.com`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L531">property maintenancePolicy</a>
</h3>

```typescript
maintenancePolicy?: pulumi.Input<{ ... }>;
```


The maintenance policy to use for the cluster. Structure is
documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L536">property masterAuth</a>
</h3>

```typescript
masterAuth?: pulumi.Input<{ ... }>;
```


The authentication information for accessing the
Kubernetes master. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L542">property masterAuthorizedNetworksConfig</a>
</h3>

```typescript
masterAuthorizedNetworksConfig?: pulumi.Input<{ ... }>;
```


The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L548">property masterIpv4CidrBlock</a>
</h3>

```typescript
masterIpv4CidrBlock?: pulumi.Input<string>;
```


) Specifies a private
[RFC1918](https://tools.ietf.org/html/rfc1918) block for the master's VPC. The master range must not overlap with any subnet in your cluster's VPC.
The master and your cluster use VPC peering. Must be specified in CIDR notation and must be `/28` subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L556">property minMasterVersion</a>
</h3>

```typescript
minMasterVersion?: pulumi.Input<string>;
```


The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version--use the read-only `master_version` field to obtain that.
If unset, the cluster's version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L566">property monitoringService</a>
</h3>

```typescript
monitoringService?: pulumi.Input<string>;
```


The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
`monitoring.googleapis.com`, `monitoring.googleapis.com/kubernetes` (beta) and `none`.
Defaults to `monitoring.googleapis.com`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L571">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the cluster, unique within the project and
zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L577">property network</a>
</h3>

```typescript
network?: pulumi.Input<string>;
```


The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L583">property networkPolicy</a>
</h3>

```typescript
networkPolicy?: pulumi.Input<{ ... }>;
```


Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L588">property nodeConfig</a>
</h3>

```typescript
nodeConfig?: pulumi.Input<{ ... }>;
```


Parameters used in creating the cluster's nodes.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L593">property nodePools</a>
</h3>

```typescript
nodePools?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


List of node pools associated with this cluster.
See [google_container_node_pool](container_node_pool.html) for schema.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L599">property nodeVersion</a>
</h3>

```typescript
nodeVersion?: pulumi.Input<string>;
```


The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L605">property podSecurityPolicyConfig</a>
</h3>

```typescript
podSecurityPolicyConfig?: pulumi.Input<{ ... }>;
```


) Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L612">property privateCluster</a>
</h3>

```typescript
privateCluster?: pulumi.Input<boolean>;
```


) If true, a
[private cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters) will be created, meaning
nodes do not get public IP addresses. It is mandatory to specify `master_ipv4_cidr_block` and
`ip_allocation_policy` with this option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L617">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L618">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L622">property removeDefaultNodePool</a>
</h3>

```typescript
removeDefaultNodePool?: pulumi.Input<boolean>;
```


If true, deletes the default node pool upon cluster creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L626">property resourceLabels</a>
</h3>

```typescript
resourceLabels?: pulumi.Input<{ ... }>;
```


The GCE resource labels (a map of key/value pairs) to be applied to the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L631">property subnetwork</a>
</h3>

```typescript
subnetwork?: pulumi.Input<string>;
```


The name or self_link of the Google Compute Engine subnetwork in
which the cluster's instances are launched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L637">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone that the master and the number of nodes specified
in `initial_node_count` should be created in. Only one of `zone` and `region`
may be set. If neither zone nor region are set, the provider zone is used.

<h2 class="pdoc-module-header" id="ClusterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L292">interface ClusterState</a>
</h2>

Input properties used for looking up and filtering Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L299">property additionalZones</a>
</h3>

```typescript
additionalZones?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of additional Google Compute Engine
locations in which the cluster's nodes should be located. If additional zones are
configured, the number of nodes specified in `initial_node_count` is created in
all specified zones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L304">property addonsConfig</a>
</h3>

```typescript
addonsConfig?: pulumi.Input<{ ... }>;
```


The configuration for addons supported by GKE.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L309">property clusterIpv4Cidr</a>
</h3>

```typescript
clusterIpv4Cidr?: pulumi.Input<string>;
```


The IP address range of the kubernetes pods in
this cluster. Default is an automatically assigned CIDR.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L313">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L319">property enableKubernetesAlpha</a>
</h3>

```typescript
enableKubernetesAlpha?: pulumi.Input<boolean>;
```


Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L326">property enableLegacyAbac</a>
</h3>

```typescript
enableLegacyAbac?: pulumi.Input<boolean>;
```


Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L330">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The IP address of this cluster's Kubernetes master.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L335">property initialNodeCount</a>
</h3>

```typescript
initialNodeCount?: pulumi.Input<number>;
```


The number of nodes to create in this
cluster (not including the Kubernetes master). Must be set if `node_pool` is not set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L340">property instanceGroupUrls</a>
</h3>

```typescript
instanceGroupUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


List of instance group URLs which have been assigned
to the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L346">property ipAllocationPolicy</a>
</h3>

```typescript
ipAllocationPolicy?: pulumi.Input<{ ... }>;
```


Configuration for cluster IP allocation. As of now, only pre-allocated subnetworks (custom type with secondary ranges) are supported.
This will activate IP aliases. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases)
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L352">property loggingService</a>
</h3>

```typescript
loggingService?: pulumi.Input<string>;
```


The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`,
`logging.googleapis.com/kubernetes` (beta), and `none`. Defaults to `logging.googleapis.com`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L357">property maintenancePolicy</a>
</h3>

```typescript
maintenancePolicy?: pulumi.Input<{ ... }>;
```


The maintenance policy to use for the cluster. Structure is
documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L362">property masterAuth</a>
</h3>

```typescript
masterAuth?: pulumi.Input<{ ... }>;
```


The authentication information for accessing the
Kubernetes master. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L368">property masterAuthorizedNetworksConfig</a>
</h3>

```typescript
masterAuthorizedNetworksConfig?: pulumi.Input<{ ... }>;
```


The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L374">property masterIpv4CidrBlock</a>
</h3>

```typescript
masterIpv4CidrBlock?: pulumi.Input<string>;
```


) Specifies a private
[RFC1918](https://tools.ietf.org/html/rfc1918) block for the master's VPC. The master range must not overlap with any subnet in your cluster's VPC.
The master and your cluster use VPC peering. Must be specified in CIDR notation and must be `/28` subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L380">property masterVersion</a>
</h3>

```typescript
masterVersion?: pulumi.Input<string>;
```


The current version of the master in the cluster. This may
be different than the `min_master_version` set in the config if the master
has been updated by GKE.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L388">property minMasterVersion</a>
</h3>

```typescript
minMasterVersion?: pulumi.Input<string>;
```


The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version--use the read-only `master_version` field to obtain that.
If unset, the cluster's version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L398">property monitoringService</a>
</h3>

```typescript
monitoringService?: pulumi.Input<string>;
```


The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
`monitoring.googleapis.com`, `monitoring.googleapis.com/kubernetes` (beta) and `none`.
Defaults to `monitoring.googleapis.com`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L403">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the cluster, unique within the project and
zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L409">property network</a>
</h3>

```typescript
network?: pulumi.Input<string>;
```


The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L415">property networkPolicy</a>
</h3>

```typescript
networkPolicy?: pulumi.Input<{ ... }>;
```


Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L420">property nodeConfig</a>
</h3>

```typescript
nodeConfig?: pulumi.Input<{ ... }>;
```


Parameters used in creating the cluster's nodes.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L425">property nodePools</a>
</h3>

```typescript
nodePools?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


List of node pools associated with this cluster.
See [google_container_node_pool](container_node_pool.html) for schema.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L431">property nodeVersion</a>
</h3>

```typescript
nodeVersion?: pulumi.Input<string>;
```


The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L437">property podSecurityPolicyConfig</a>
</h3>

```typescript
podSecurityPolicyConfig?: pulumi.Input<{ ... }>;
```


) Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L444">property privateCluster</a>
</h3>

```typescript
privateCluster?: pulumi.Input<boolean>;
```


) If true, a
[private cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters) will be created, meaning
nodes do not get public IP addresses. It is mandatory to specify `master_ipv4_cidr_block` and
`ip_allocation_policy` with this option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L449">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L450">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L454">property removeDefaultNodePool</a>
</h3>

```typescript
removeDefaultNodePool?: pulumi.Input<boolean>;
```


If true, deletes the default node pool upon cluster creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L458">property resourceLabels</a>
</h3>

```typescript
resourceLabels?: pulumi.Input<{ ... }>;
```


The GCE resource labels (a map of key/value pairs) to be applied to the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L463">property subnetwork</a>
</h3>

```typescript
subnetwork?: pulumi.Input<string>;
```


The name or self_link of the Google Compute Engine subnetwork in
which the cluster's instances are launched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L469">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone that the master and the number of nodes specified
in `initial_node_count` should be created in. Only one of `zone` and `region`
may be set. If neither zone nor region are set, the provider zone is used.

<h2 class="pdoc-module-header" id="GetClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L21">interface GetClusterArgs</a>
</h2>

A collection of arguments for invoking getCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L25">property name</a>
</h3>

```typescript
name: string;
```


The name of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L30">property project</a>
</h3>

```typescript
project?: string;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L31">property region</a>
</h3>

```typescript
region?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L32">property zone</a>
</h3>

```typescript
zone?: string;
```

<h2 class="pdoc-module-header" id="GetClusterResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L38">interface GetClusterResult</a>
</h2>

A collection of values returned by getCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L39">property additionalZones</a>
</h3>

```typescript
additionalZones: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L40">property addonsConfigs</a>
</h3>

```typescript
addonsConfigs: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L41">property clusterIpv4Cidr</a>
</h3>

```typescript
clusterIpv4Cidr: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L42">property description</a>
</h3>

```typescript
description: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L43">property enableKubernetesAlpha</a>
</h3>

```typescript
enableKubernetesAlpha: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L44">property enableLegacyAbac</a>
</h3>

```typescript
enableLegacyAbac: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L45">property endpoint</a>
</h3>

```typescript
endpoint: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L70">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L46">property initialNodeCount</a>
</h3>

```typescript
initialNodeCount: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L47">property instanceGroupUrls</a>
</h3>

```typescript
instanceGroupUrls: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L48">property ipAllocationPolicies</a>
</h3>

```typescript
ipAllocationPolicies: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L49">property loggingService</a>
</h3>

```typescript
loggingService: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L50">property maintenancePolicies</a>
</h3>

```typescript
maintenancePolicies: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L52">property masterAuthorizedNetworksConfigs</a>
</h3>

```typescript
masterAuthorizedNetworksConfigs: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L51">property masterAuths</a>
</h3>

```typescript
masterAuths: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L53">property masterIpv4CidrBlock</a>
</h3>

```typescript
masterIpv4CidrBlock: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L54">property masterVersion</a>
</h3>

```typescript
masterVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L55">property minMasterVersion</a>
</h3>

```typescript
minMasterVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L56">property monitoringService</a>
</h3>

```typescript
monitoringService: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L57">property network</a>
</h3>

```typescript
network: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L58">property networkPolicies</a>
</h3>

```typescript
networkPolicies: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L59">property nodeConfigs</a>
</h3>

```typescript
nodeConfigs: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L60">property nodePools</a>
</h3>

```typescript
nodePools: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L61">property nodeVersion</a>
</h3>

```typescript
nodeVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L62">property podSecurityPolicyConfigs</a>
</h3>

```typescript
podSecurityPolicyConfigs: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L63">property privateCluster</a>
</h3>

```typescript
privateCluster: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L64">property removeDefaultNodePool</a>
</h3>

```typescript
removeDefaultNodePool: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L65">property resourceLabels</a>
</h3>

```typescript
resourceLabels: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L66">property subnetwork</a>
</h3>

```typescript
subnetwork: string;
```

<h2 class="pdoc-module-header" id="GetEngineVersionsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L38">interface GetEngineVersionsArgs</a>
</h2>

A collection of arguments for invoking getEngineVersions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L43">property project</a>
</h3>

```typescript
project?: string;
```


ID of the project to list available cluster versions for. Should match the project the cluster will be deployed to.
Defaults to the project that the provider is authenticated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L47">property zone</a>
</h3>

```typescript
zone?: string;
```


Zone to list available cluster versions for. Should match the zone the cluster will be deployed in.

<h2 class="pdoc-module-header" id="GetEngineVersionsResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L53">interface GetEngineVersionsResult</a>
</h2>

A collection of values returned by getEngineVersions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L57">property defaultClusterVersion</a>
</h3>

```typescript
defaultClusterVersion: string;
```


Version of Kubernetes the service deploys by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L77">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L61">property latestMasterVersion</a>
</h3>

```typescript
latestMasterVersion: string;
```


The latest version available in the given zone for use with master instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L65">property latestNodeVersion</a>
</h3>

```typescript
latestNodeVersion: string;
```


The latest version available in the given zone for use with node instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L69">property validMasterVersions</a>
</h3>

```typescript
validMasterVersions: string[];
```


A list of versions available in the given zone for use with master instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L73">property validNodeVersions</a>
</h3>

```typescript
validNodeVersions: string[];
```


A list of versions available in the given zone for use with node instances.

<h2 class="pdoc-module-header" id="GetRegistryImageArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L24">interface GetRegistryImageArgs</a>
</h2>

A collection of arguments for invoking getRegistryImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L25">property digest</a>
</h3>

```typescript
digest?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L26">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L27">property project</a>
</h3>

```typescript
project?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L28">property region</a>
</h3>

```typescript
region?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L29">property tag</a>
</h3>

```typescript
tag?: string;
```

<h2 class="pdoc-module-header" id="GetRegistryImageResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L35">interface GetRegistryImageResult</a>
</h2>

A collection of values returned by getRegistryImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L41">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L36">property imageUrl</a>
</h3>

```typescript
imageUrl: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L37">property project</a>
</h3>

```typescript
project: string;
```

<h2 class="pdoc-module-header" id="GetRegistryRepositoryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryRepository.ts#L22">interface GetRegistryRepositoryArgs</a>
</h2>

A collection of arguments for invoking getRegistryRepository.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryRepository.ts#L23">property project</a>
</h3>

```typescript
project?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryRepository.ts#L24">property region</a>
</h3>

```typescript
region?: string;
```

<h2 class="pdoc-module-header" id="GetRegistryRepositoryResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryRepository.ts#L30">interface GetRegistryRepositoryResult</a>
</h2>

A collection of values returned by getRegistryRepository.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryRepository.ts#L36">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryRepository.ts#L31">property project</a>
</h3>

```typescript
project: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryRepository.ts#L32">property repositoryUrl</a>
</h3>

```typescript
repositoryUrl: string;
```

<h2 class="pdoc-module-header" id="NodePoolArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L201">interface NodePoolArgs</a>
</h2>

The set of arguments for constructing a NodePool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L206">property autoscaling</a>
</h3>

```typescript
autoscaling?: pulumi.Input<{ ... }>;
```


Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L210">property cluster</a>
</h3>

```typescript
cluster: pulumi.Input<string>;
```


The cluster to create the node pool for.  Cluster must be present in `zone` provided for zonal clusters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L215">property initialNodeCount</a>
</h3>

```typescript
initialNodeCount?: pulumi.Input<number>;
```


The initial node count for the pool. Changing this will force
recreation of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L220">property management</a>
</h3>

```typescript
management?: pulumi.Input<{ ... }>;
```


Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L225">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the node pool. If left blank, Terraform will
auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L230">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L235">property nodeConfig</a>
</h3>

```typescript
nodeConfig?: pulumi.Input<{ ... }>;
```


The node configuration of the pool. See
[google_container_cluster](container_cluster.html) for schema.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L240">property nodeCount</a>
</h3>

```typescript
nodeCount?: pulumi.Input<number>;
```


The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L245">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L249">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which the cluster resides (for regional clusters).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L255">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L259">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone in which the cluster resides.

<h2 class="pdoc-module-header" id="NodePoolState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L136">interface NodePoolState</a>
</h2>

Input properties used for looking up and filtering NodePool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L141">property autoscaling</a>
</h3>

```typescript
autoscaling?: pulumi.Input<{ ... }>;
```


Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L145">property cluster</a>
</h3>

```typescript
cluster?: pulumi.Input<string>;
```


The cluster to create the node pool for.  Cluster must be present in `zone` provided for zonal clusters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L150">property initialNodeCount</a>
</h3>

```typescript
initialNodeCount?: pulumi.Input<number>;
```


The initial node count for the pool. Changing this will force
recreation of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L151">property instanceGroupUrls</a>
</h3>

```typescript
instanceGroupUrls?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L156">property management</a>
</h3>

```typescript
management?: pulumi.Input<{ ... }>;
```


Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L161">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the node pool. If left blank, Terraform will
auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L166">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L171">property nodeConfig</a>
</h3>

```typescript
nodeConfig?: pulumi.Input<{ ... }>;
```


The node configuration of the pool. See
[google_container_cluster](container_cluster.html) for schema.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L176">property nodeCount</a>
</h3>

```typescript
nodeCount?: pulumi.Input<number>;
```


The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L181">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L185">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which the cluster resides (for regional clusters).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L191">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L195">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone in which the cluster resides.

