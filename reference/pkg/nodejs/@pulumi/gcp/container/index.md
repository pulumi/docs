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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L16">class Cluster</a>
</h2>

Creates a Google Kubernetes Engine (GKE) cluster. For more information see
[the official documentation](https://cloud.google.com/container-engine/docs/clusters)
and
[API](https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters).

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L205">constructor</a>
</h3>

```typescript
new Cluster(name: string, args?: ClusterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Cluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L25">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L35">property additionalZones</a>
</h3>

```typescript
public additionalZones: pulumi.Output<string[]>;
```


The list of additional Google Compute Engine
locations in which the cluster's nodes should be located. If additional zones are
configured, the number of nodes specified in `initial_node_count` is created in
all specified zones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L40">property addonsConfig</a>
</h3>

```typescript
public addonsConfig: pulumi.Output<{ ... }>;
```


The configuration for addons supported by GKE.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L45">property clusterIpv4Cidr</a>
</h3>

```typescript
public clusterIpv4Cidr: pulumi.Output<string>;
```


The IP address range of the kubernetes pods in
this cluster. Default is an automatically assigned CIDR.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L49">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L55">property enableKubernetesAlpha</a>
</h3>

```typescript
public enableKubernetesAlpha: pulumi.Output<boolean | undefined>;
```


Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L62">property enableLegacyAbac</a>
</h3>

```typescript
public enableLegacyAbac: pulumi.Output<boolean | undefined>;
```


Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L66">property endpoint</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L71">property initialNodeCount</a>
</h3>

```typescript
public initialNodeCount: pulumi.Output<number | undefined>;
```


The number of nodes to create in this
cluster (not including the Kubernetes master). Must be set if `node_pool` is not set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L76">property instanceGroupUrls</a>
</h3>

```typescript
public instanceGroupUrls: pulumi.Output<string[]>;
```


List of instance group URLs which have been assigned
to the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L82">property ipAllocationPolicy</a>
</h3>

```typescript
public ipAllocationPolicy: pulumi.Output<{ ... } | undefined>;
```


Configuration for cluster IP allocation. As of now, only pre-allocated subnetworks (custom type with secondary ranges) are supported.
This will activate IP aliases. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases)
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L88">property loggingService</a>
</h3>

```typescript
public loggingService: pulumi.Output<string>;
```


The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`,
`logging.googleapis.com/kubernetes` (beta), and `none`. Defaults to `logging.googleapis.com`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L93">property maintenancePolicy</a>
</h3>

```typescript
public maintenancePolicy: pulumi.Output<{ ... } | undefined>;
```


The maintenance policy to use for the cluster. Structure is
documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L98">property masterAuth</a>
</h3>

```typescript
public masterAuth: pulumi.Output<{ ... }>;
```


The authentication information for accessing the
Kubernetes master. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L104">property masterAuthorizedNetworksConfig</a>
</h3>

```typescript
public masterAuthorizedNetworksConfig: pulumi.Output<{ ... } | undefined>;
```


The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L110">property masterIpv4CidrBlock</a>
</h3>

```typescript
public masterIpv4CidrBlock: pulumi.Output<string | undefined>;
```


) Specifies a private
[RFC1918](https://tools.ietf.org/html/rfc1918) block for the master's VPC. The master range must not overlap with any subnet in your cluster's VPC.
The master and your cluster use VPC peering. Must be specified in CIDR notation and must be `/28` subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L116">property masterVersion</a>
</h3>

```typescript
public masterVersion: pulumi.Output<string>;
```


The current version of the master in the cluster. This may
be different than the `min_master_version` set in the config if the master
has been updated by GKE.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L124">property minMasterVersion</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L134">property monitoringService</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L139">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the cluster, unique within the project and
zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L145">property network</a>
</h3>

```typescript
public network: pulumi.Output<string | undefined>;
```


The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L151">property networkPolicy</a>
</h3>

```typescript
public networkPolicy: pulumi.Output<{ ... }>;
```


Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L156">property nodeConfig</a>
</h3>

```typescript
public nodeConfig: pulumi.Output<{ ... }>;
```


Parameters used in creating the cluster's nodes.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L161">property nodePools</a>
</h3>

```typescript
public nodePools: pulumi.Output<{ ... }[]>;
```


List of node pools associated with this cluster.
See google_container_node_pool for schema.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L167">property nodeVersion</a>
</h3>

```typescript
public nodeVersion: pulumi.Output<string>;
```


The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L173">property podSecurityPolicyConfig</a>
</h3>

```typescript
public podSecurityPolicyConfig: pulumi.Output<{ ... } | undefined>;
```


) Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L180">property privateCluster</a>
</h3>

```typescript
public privateCluster: pulumi.Output<boolean | undefined>;
```


) If true, a
[private cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters) will be created, meaning
nodes do not get public IP addresses. It is mandatory to specify `master_ipv4_cidr_block` and
`ip_allocation_policy` with this option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L185">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L186">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L190">property removeDefaultNodePool</a>
</h3>

```typescript
public removeDefaultNodePool: pulumi.Output<boolean | undefined>;
```


If true, deletes the default node pool upon cluster creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L194">property resourceLabels</a>
</h3>

```typescript
public resourceLabels: pulumi.Output<{ ... } | undefined>;
```


The GCE resource labels (a map of key/value pairs) to be applied to the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L199">property subnetwork</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L205">property zone</a>
</h3>

```typescript
public zone: pulumi.Output<string>;
```


The zone that the master and the number of nodes specified
in `initial_node_count` should be created in. Only one of `zone` and `region`
may be set. If neither zone nor region are set, the provider zone is used.

<h2 class="pdoc-module-header" id="NodePool">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L13">class NodePool</a>
</h2>

Manages a Node Pool resource within GKE. For more information see
[the official documentation](https://cloud.google.com/container-engine/docs/node-pools)
and
[API](https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters.nodePools).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L84">constructor</a>
</h3>

```typescript
new NodePool(name: string, args: NodePoolArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NodePool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L22">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L30">property autoscaling</a>
</h3>

```typescript
public autoscaling: pulumi.Output<{ ... } | undefined>;
```


Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L34">property cluster</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L39">property initialNodeCount</a>
</h3>

```typescript
public initialNodeCount: pulumi.Output<number>;
```


The initial node count for the pool. Changing this will force
recreation of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L40">property instanceGroupUrls</a>
</h3>

```typescript
public instanceGroupUrls: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L45">property management</a>
</h3>

```typescript
public management: pulumi.Output<{ ... }>;
```


Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L50">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the node pool. If left blank, Terraform will
auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L55">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string>;
```


Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L60">property nodeConfig</a>
</h3>

```typescript
public nodeConfig: pulumi.Output<{ ... }>;
```


The node configuration of the pool. See
google_container_cluster for schema.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L65">property nodeCount</a>
</h3>

```typescript
public nodeCount: pulumi.Output<number>;
```


The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L70">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L74">property region</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L80">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L84">property zone</a>
</h3>

```typescript
public zone: pulumi.Output<string>;
```


The zone in which the cluster resides.

<h2 class="pdoc-module-header" id="getCluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L10">function getCluster</a>
</h2>

```typescript
getCluster(args: GetClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterResult>
```


Get info about a cluster within GKE from its name and zone.

<h2 class="pdoc-module-header" id="getEngineVersions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L28">function getEngineVersions</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L12">function getRegistryImage</a>
</h2>

```typescript
getRegistryImage(args: GetRegistryImageArgs, opts?: pulumi.InvokeOptions): Promise<GetRegistryImageResult>
```


This data source fetches the project name, and provides the appropriate URLs to use for container registry for this project.

The URLs are computed entirely offline - as long as the project exists, they will be valid, but this data source does not contact Google Container Registry (GCR) at any point.

<h2 class="pdoc-module-header" id="getRegistryRepository">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryRepository.ts#L12">function getRegistryRepository</a>
</h2>

```typescript
getRegistryRepository(args?: GetRegistryRepositoryArgs, opts?: pulumi.InvokeOptions): Promise<GetRegistryRepositoryResult>
```


This data source fetches the project name, and provides the appropriate URLs to use for container registry for this project.

The URLs are computed entirely offline - as long as the project exists, they will be valid, but this data source does not contact Google Container Registry (GCR) at any point.

<h2 class="pdoc-module-header" id="ClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L476">interface ClusterArgs</a>
</h2>

The set of arguments for constructing a Cluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L483">property additionalZones</a>
</h3>

```typescript
additionalZones?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of additional Google Compute Engine
locations in which the cluster's nodes should be located. If additional zones are
configured, the number of nodes specified in `initial_node_count` is created in
all specified zones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L488">property addonsConfig</a>
</h3>

```typescript
addonsConfig?: pulumi.Input<{ ... }>;
```


The configuration for addons supported by GKE.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L493">property clusterIpv4Cidr</a>
</h3>

```typescript
clusterIpv4Cidr?: pulumi.Input<string>;
```


The IP address range of the kubernetes pods in
this cluster. Default is an automatically assigned CIDR.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L497">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L503">property enableKubernetesAlpha</a>
</h3>

```typescript
enableKubernetesAlpha?: pulumi.Input<boolean>;
```


Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L510">property enableLegacyAbac</a>
</h3>

```typescript
enableLegacyAbac?: pulumi.Input<boolean>;
```


Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L515">property initialNodeCount</a>
</h3>

```typescript
initialNodeCount?: pulumi.Input<number>;
```


The number of nodes to create in this
cluster (not including the Kubernetes master). Must be set if `node_pool` is not set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L521">property ipAllocationPolicy</a>
</h3>

```typescript
ipAllocationPolicy?: pulumi.Input<{ ... }>;
```


Configuration for cluster IP allocation. As of now, only pre-allocated subnetworks (custom type with secondary ranges) are supported.
This will activate IP aliases. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases)
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L527">property loggingService</a>
</h3>

```typescript
loggingService?: pulumi.Input<string>;
```


The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`,
`logging.googleapis.com/kubernetes` (beta), and `none`. Defaults to `logging.googleapis.com`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L532">property maintenancePolicy</a>
</h3>

```typescript
maintenancePolicy?: pulumi.Input<{ ... }>;
```


The maintenance policy to use for the cluster. Structure is
documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L537">property masterAuth</a>
</h3>

```typescript
masterAuth?: pulumi.Input<{ ... }>;
```


The authentication information for accessing the
Kubernetes master. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L543">property masterAuthorizedNetworksConfig</a>
</h3>

```typescript
masterAuthorizedNetworksConfig?: pulumi.Input<{ ... }>;
```


The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L549">property masterIpv4CidrBlock</a>
</h3>

```typescript
masterIpv4CidrBlock?: pulumi.Input<string>;
```


) Specifies a private
[RFC1918](https://tools.ietf.org/html/rfc1918) block for the master's VPC. The master range must not overlap with any subnet in your cluster's VPC.
The master and your cluster use VPC peering. Must be specified in CIDR notation and must be `/28` subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L557">property minMasterVersion</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L567">property monitoringService</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L572">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the cluster, unique within the project and
zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L578">property network</a>
</h3>

```typescript
network?: pulumi.Input<string>;
```


The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L584">property networkPolicy</a>
</h3>

```typescript
networkPolicy?: pulumi.Input<{ ... }>;
```


Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L589">property nodeConfig</a>
</h3>

```typescript
nodeConfig?: pulumi.Input<{ ... }>;
```


Parameters used in creating the cluster's nodes.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L594">property nodePools</a>
</h3>

```typescript
nodePools?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


List of node pools associated with this cluster.
See google_container_node_pool for schema.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L600">property nodeVersion</a>
</h3>

```typescript
nodeVersion?: pulumi.Input<string>;
```


The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L606">property podSecurityPolicyConfig</a>
</h3>

```typescript
podSecurityPolicyConfig?: pulumi.Input<{ ... }>;
```


) Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L613">property privateCluster</a>
</h3>

```typescript
privateCluster?: pulumi.Input<boolean>;
```


) If true, a
[private cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters) will be created, meaning
nodes do not get public IP addresses. It is mandatory to specify `master_ipv4_cidr_block` and
`ip_allocation_policy` with this option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L618">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L619">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L623">property removeDefaultNodePool</a>
</h3>

```typescript
removeDefaultNodePool?: pulumi.Input<boolean>;
```


If true, deletes the default node pool upon cluster creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L627">property resourceLabels</a>
</h3>

```typescript
resourceLabels?: pulumi.Input<{ ... }>;
```


The GCE resource labels (a map of key/value pairs) to be applied to the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L632">property subnetwork</a>
</h3>

```typescript
subnetwork?: pulumi.Input<string>;
```


The name or self_link of the Google Compute Engine subnetwork in
which the cluster's instances are launched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L638">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone that the master and the number of nodes specified
in `initial_node_count` should be created in. Only one of `zone` and `region`
may be set. If neither zone nor region are set, the provider zone is used.

<h2 class="pdoc-module-header" id="ClusterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L293">interface ClusterState</a>
</h2>

Input properties used for looking up and filtering Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L300">property additionalZones</a>
</h3>

```typescript
additionalZones?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of additional Google Compute Engine
locations in which the cluster's nodes should be located. If additional zones are
configured, the number of nodes specified in `initial_node_count` is created in
all specified zones.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L305">property addonsConfig</a>
</h3>

```typescript
addonsConfig?: pulumi.Input<{ ... }>;
```


The configuration for addons supported by GKE.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L310">property clusterIpv4Cidr</a>
</h3>

```typescript
clusterIpv4Cidr?: pulumi.Input<string>;
```


The IP address range of the kubernetes pods in
this cluster. Default is an automatically assigned CIDR.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L314">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L320">property enableKubernetesAlpha</a>
</h3>

```typescript
enableKubernetesAlpha?: pulumi.Input<boolean>;
```


Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L327">property enableLegacyAbac</a>
</h3>

```typescript
enableLegacyAbac?: pulumi.Input<boolean>;
```


Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L331">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The IP address of this cluster's Kubernetes master.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L336">property initialNodeCount</a>
</h3>

```typescript
initialNodeCount?: pulumi.Input<number>;
```


The number of nodes to create in this
cluster (not including the Kubernetes master). Must be set if `node_pool` is not set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L341">property instanceGroupUrls</a>
</h3>

```typescript
instanceGroupUrls?: pulumi.Input<pulumi.Input<string>[]>;
```


List of instance group URLs which have been assigned
to the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L347">property ipAllocationPolicy</a>
</h3>

```typescript
ipAllocationPolicy?: pulumi.Input<{ ... }>;
```


Configuration for cluster IP allocation. As of now, only pre-allocated subnetworks (custom type with secondary ranges) are supported.
This will activate IP aliases. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases)
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L353">property loggingService</a>
</h3>

```typescript
loggingService?: pulumi.Input<string>;
```


The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`,
`logging.googleapis.com/kubernetes` (beta), and `none`. Defaults to `logging.googleapis.com`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L358">property maintenancePolicy</a>
</h3>

```typescript
maintenancePolicy?: pulumi.Input<{ ... }>;
```


The maintenance policy to use for the cluster. Structure is
documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L363">property masterAuth</a>
</h3>

```typescript
masterAuth?: pulumi.Input<{ ... }>;
```


The authentication information for accessing the
Kubernetes master. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L369">property masterAuthorizedNetworksConfig</a>
</h3>

```typescript
masterAuthorizedNetworksConfig?: pulumi.Input<{ ... }>;
```


The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L375">property masterIpv4CidrBlock</a>
</h3>

```typescript
masterIpv4CidrBlock?: pulumi.Input<string>;
```


) Specifies a private
[RFC1918](https://tools.ietf.org/html/rfc1918) block for the master's VPC. The master range must not overlap with any subnet in your cluster's VPC.
The master and your cluster use VPC peering. Must be specified in CIDR notation and must be `/28` subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L381">property masterVersion</a>
</h3>

```typescript
masterVersion?: pulumi.Input<string>;
```


The current version of the master in the cluster. This may
be different than the `min_master_version` set in the config if the master
has been updated by GKE.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L389">property minMasterVersion</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L399">property monitoringService</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L404">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the cluster, unique within the project and
zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L410">property network</a>
</h3>

```typescript
network?: pulumi.Input<string>;
```


The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L416">property networkPolicy</a>
</h3>

```typescript
networkPolicy?: pulumi.Input<{ ... }>;
```


Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L421">property nodeConfig</a>
</h3>

```typescript
nodeConfig?: pulumi.Input<{ ... }>;
```


Parameters used in creating the cluster's nodes.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L426">property nodePools</a>
</h3>

```typescript
nodePools?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


List of node pools associated with this cluster.
See google_container_node_pool for schema.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L432">property nodeVersion</a>
</h3>

```typescript
nodeVersion?: pulumi.Input<string>;
```


The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L438">property podSecurityPolicyConfig</a>
</h3>

```typescript
podSecurityPolicyConfig?: pulumi.Input<{ ... }>;
```


) Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L445">property privateCluster</a>
</h3>

```typescript
privateCluster?: pulumi.Input<boolean>;
```


) If true, a
[private cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters) will be created, meaning
nodes do not get public IP addresses. It is mandatory to specify `master_ipv4_cidr_block` and
`ip_allocation_policy` with this option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L450">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L451">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L455">property removeDefaultNodePool</a>
</h3>

```typescript
removeDefaultNodePool?: pulumi.Input<boolean>;
```


If true, deletes the default node pool upon cluster creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L459">property resourceLabels</a>
</h3>

```typescript
resourceLabels?: pulumi.Input<{ ... }>;
```


The GCE resource labels (a map of key/value pairs) to be applied to the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L464">property subnetwork</a>
</h3>

```typescript
subnetwork?: pulumi.Input<string>;
```


The name or self_link of the Google Compute Engine subnetwork in
which the cluster's instances are launched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/cluster.ts#L470">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone that the master and the number of nodes specified
in `initial_node_count` should be created in. Only one of `zone` and `region`
may be set. If neither zone nor region are set, the provider zone is used.

<h2 class="pdoc-module-header" id="GetClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L22">interface GetClusterArgs</a>
</h2>

A collection of arguments for invoking getCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L26">property name</a>
</h3>

```typescript
name: string;
```


The name of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L31">property project</a>
</h3>

```typescript
project?: string;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L32">property region</a>
</h3>

```typescript
region?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L33">property zone</a>
</h3>

```typescript
zone?: string;
```

<h2 class="pdoc-module-header" id="GetClusterResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L39">interface GetClusterResult</a>
</h2>

A collection of values returned by getCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L40">property additionalZones</a>
</h3>

```typescript
additionalZones: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L41">property addonsConfigs</a>
</h3>

```typescript
addonsConfigs: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L42">property clusterIpv4Cidr</a>
</h3>

```typescript
clusterIpv4Cidr: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L43">property description</a>
</h3>

```typescript
description: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L44">property enableKubernetesAlpha</a>
</h3>

```typescript
enableKubernetesAlpha: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L45">property enableLegacyAbac</a>
</h3>

```typescript
enableLegacyAbac: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L46">property endpoint</a>
</h3>

```typescript
endpoint: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L71">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L47">property initialNodeCount</a>
</h3>

```typescript
initialNodeCount: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L48">property instanceGroupUrls</a>
</h3>

```typescript
instanceGroupUrls: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L49">property ipAllocationPolicies</a>
</h3>

```typescript
ipAllocationPolicies: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L50">property loggingService</a>
</h3>

```typescript
loggingService: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L51">property maintenancePolicies</a>
</h3>

```typescript
maintenancePolicies: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L53">property masterAuthorizedNetworksConfigs</a>
</h3>

```typescript
masterAuthorizedNetworksConfigs: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L52">property masterAuths</a>
</h3>

```typescript
masterAuths: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L54">property masterIpv4CidrBlock</a>
</h3>

```typescript
masterIpv4CidrBlock: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L55">property masterVersion</a>
</h3>

```typescript
masterVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L56">property minMasterVersion</a>
</h3>

```typescript
minMasterVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L57">property monitoringService</a>
</h3>

```typescript
monitoringService: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L58">property network</a>
</h3>

```typescript
network: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L59">property networkPolicies</a>
</h3>

```typescript
networkPolicies: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L60">property nodeConfigs</a>
</h3>

```typescript
nodeConfigs: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L61">property nodePools</a>
</h3>

```typescript
nodePools: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L62">property nodeVersion</a>
</h3>

```typescript
nodeVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L63">property podSecurityPolicyConfigs</a>
</h3>

```typescript
podSecurityPolicyConfigs: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L64">property privateCluster</a>
</h3>

```typescript
privateCluster: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L65">property removeDefaultNodePool</a>
</h3>

```typescript
removeDefaultNodePool: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L66">property resourceLabels</a>
</h3>

```typescript
resourceLabels: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getCluster.ts#L67">property subnetwork</a>
</h3>

```typescript
subnetwork: string;
```

<h2 class="pdoc-module-header" id="GetEngineVersionsArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L39">interface GetEngineVersionsArgs</a>
</h2>

A collection of arguments for invoking getEngineVersions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L44">property project</a>
</h3>

```typescript
project?: string;
```


ID of the project to list available cluster versions for. Should match the project the cluster will be deployed to.
Defaults to the project that the provider is authenticated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L48">property zone</a>
</h3>

```typescript
zone?: string;
```


Zone to list available cluster versions for. Should match the zone the cluster will be deployed in.

<h2 class="pdoc-module-header" id="GetEngineVersionsResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L54">interface GetEngineVersionsResult</a>
</h2>

A collection of values returned by getEngineVersions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L58">property defaultClusterVersion</a>
</h3>

```typescript
defaultClusterVersion: string;
```


Version of Kubernetes the service deploys by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L78">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L62">property latestMasterVersion</a>
</h3>

```typescript
latestMasterVersion: string;
```


The latest version available in the given zone for use with master instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L66">property latestNodeVersion</a>
</h3>

```typescript
latestNodeVersion: string;
```


The latest version available in the given zone for use with node instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L70">property validMasterVersions</a>
</h3>

```typescript
validMasterVersions: string[];
```


A list of versions available in the given zone for use with master instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getEngineVersions.ts#L74">property validNodeVersions</a>
</h3>

```typescript
validNodeVersions: string[];
```


A list of versions available in the given zone for use with node instances.

<h2 class="pdoc-module-header" id="GetRegistryImageArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L25">interface GetRegistryImageArgs</a>
</h2>

A collection of arguments for invoking getRegistryImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L26">property digest</a>
</h3>

```typescript
digest?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L27">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L28">property project</a>
</h3>

```typescript
project?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L29">property region</a>
</h3>

```typescript
region?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L30">property tag</a>
</h3>

```typescript
tag?: string;
```

<h2 class="pdoc-module-header" id="GetRegistryImageResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L36">interface GetRegistryImageResult</a>
</h2>

A collection of values returned by getRegistryImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L42">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L37">property imageUrl</a>
</h3>

```typescript
imageUrl: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryImage.ts#L38">property project</a>
</h3>

```typescript
project: string;
```

<h2 class="pdoc-module-header" id="GetRegistryRepositoryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryRepository.ts#L23">interface GetRegistryRepositoryArgs</a>
</h2>

A collection of arguments for invoking getRegistryRepository.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryRepository.ts#L24">property project</a>
</h3>

```typescript
project?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryRepository.ts#L25">property region</a>
</h3>

```typescript
region?: string;
```

<h2 class="pdoc-module-header" id="GetRegistryRepositoryResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryRepository.ts#L31">interface GetRegistryRepositoryResult</a>
</h2>

A collection of values returned by getRegistryRepository.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryRepository.ts#L37">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryRepository.ts#L32">property project</a>
</h3>

```typescript
project: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/getRegistryRepository.ts#L33">property repositoryUrl</a>
</h3>

```typescript
repositoryUrl: string;
```

<h2 class="pdoc-module-header" id="NodePoolArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L202">interface NodePoolArgs</a>
</h2>

The set of arguments for constructing a NodePool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L207">property autoscaling</a>
</h3>

```typescript
autoscaling?: pulumi.Input<{ ... }>;
```


Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L211">property cluster</a>
</h3>

```typescript
cluster: pulumi.Input<string>;
```


The cluster to create the node pool for.  Cluster must be present in `zone` provided for zonal clusters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L216">property initialNodeCount</a>
</h3>

```typescript
initialNodeCount?: pulumi.Input<number>;
```


The initial node count for the pool. Changing this will force
recreation of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L221">property management</a>
</h3>

```typescript
management?: pulumi.Input<{ ... }>;
```


Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L226">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the node pool. If left blank, Terraform will
auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L231">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L236">property nodeConfig</a>
</h3>

```typescript
nodeConfig?: pulumi.Input<{ ... }>;
```


The node configuration of the pool. See
google_container_cluster for schema.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L241">property nodeCount</a>
</h3>

```typescript
nodeCount?: pulumi.Input<number>;
```


The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L246">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L250">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which the cluster resides (for regional clusters).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L256">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L260">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone in which the cluster resides.

<h2 class="pdoc-module-header" id="NodePoolState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L137">interface NodePoolState</a>
</h2>

Input properties used for looking up and filtering NodePool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L142">property autoscaling</a>
</h3>

```typescript
autoscaling?: pulumi.Input<{ ... }>;
```


Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L146">property cluster</a>
</h3>

```typescript
cluster?: pulumi.Input<string>;
```


The cluster to create the node pool for.  Cluster must be present in `zone` provided for zonal clusters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L151">property initialNodeCount</a>
</h3>

```typescript
initialNodeCount?: pulumi.Input<number>;
```


The initial node count for the pool. Changing this will force
recreation of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L152">property instanceGroupUrls</a>
</h3>

```typescript
instanceGroupUrls?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L157">property management</a>
</h3>

```typescript
management?: pulumi.Input<{ ... }>;
```


Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L162">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the node pool. If left blank, Terraform will
auto-generate a unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L167">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L172">property nodeConfig</a>
</h3>

```typescript
nodeConfig?: pulumi.Input<{ ... }>;
```


The node configuration of the pool. See
google_container_cluster for schema.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L177">property nodeCount</a>
</h3>

```typescript
nodeCount?: pulumi.Input<number>;
```


The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L182">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L186">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which the cluster resides (for regional clusters).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L192">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/container/nodePool.ts#L196">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone in which the cluster resides.

