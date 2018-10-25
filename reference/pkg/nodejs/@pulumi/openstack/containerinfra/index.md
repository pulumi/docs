---
title: Module containerinfra
---

<a href="../index.html">@pulumi/openstack</a> &gt; containerinfra

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Cluster">class Cluster</a>
* <a href="#ClusterTemplate">class ClusterTemplate</a>
* <a href="#getClusterTemplate">function getClusterTemplate</a>
* <a href="#ClusterArgs">interface ClusterArgs</a>
* <a href="#ClusterState">interface ClusterState</a>
* <a href="#ClusterTemplateArgs">interface ClusterTemplateArgs</a>
* <a href="#ClusterTemplateState">interface ClusterTemplateState</a>
* <a href="#GetClusterTemplateArgs">interface GetClusterTemplateArgs</a>
* <a href="#GetClusterTemplateResult">interface GetClusterTemplateResult</a>

<a href="/containerinfra/cluster.ts">containerinfra/cluster.ts</a> <a href="/containerinfra/clusterTemplate.ts">containerinfra/clusterTemplate.ts</a> <a href="/containerinfra/getClusterTemplate.ts">containerinfra/getClusterTemplate.ts</a> 


<h2 class="pdoc-module-header" id="Cluster">
<a class="pdoc-member-name" href="/containerinfra/cluster.ts#L10">class Cluster</a>
</h2>

Manages a V1 Magnum cluster resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L44">constructor</a>
</h3>

```typescript
new Cluster(name: string, args: ClusterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Cluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterState): Cluster
```


Get an existing Cluster resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L23">property apiAddress</a>
</h3>

```typescript
public apiAddress: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L24">property clusterTemplateId</a>
</h3>

```typescript
public clusterTemplateId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L25">property coeVersion</a>
</h3>

```typescript
public coeVersion: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L26">property containerVersion</a>
</h3>

```typescript
public containerVersion: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L27">property createTimeout</a>
</h3>

```typescript
public createTimeout: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L28">property createdAt</a>
</h3>

```typescript
public createdAt: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L29">property discoveryUrl</a>
</h3>

```typescript
public discoveryUrl: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L30">property dockerVolumeSize</a>
</h3>

```typescript
public dockerVolumeSize: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L31">property flavor</a>
</h3>

```typescript
public flavor: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L32">property keypair</a>
</h3>

```typescript
public keypair: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L33">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L34">property masterAddresses</a>
</h3>

```typescript
public masterAddresses: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L35">property masterCount</a>
</h3>

```typescript
public masterCount: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L36">property masterFlavor</a>
</h3>

```typescript
public masterFlavor: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L38">property nodeAddresses</a>
</h3>

```typescript
public nodeAddresses: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L39">property nodeCount</a>
</h3>

```typescript
public nodeCount: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L40">property projectId</a>
</h3>

```typescript
public projectId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L41">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L42">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L43">property updatedAt</a>
</h3>

```typescript
public updatedAt: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L44">property userId</a>
</h3>

```typescript
public userId: pulumi.Output<string>;
```

<h2 class="pdoc-module-header" id="ClusterTemplate">
<a class="pdoc-member-name" href="/containerinfra/clusterTemplate.ts#L10">class ClusterTemplate</a>
</h2>

Manages a V1 Magnum cluster template resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L54">constructor</a>
</h3>

```typescript
new ClusterTemplate(name: string, args: ClusterTemplateArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ClusterTemplate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterTemplateState): ClusterTemplate
```


Get an existing ClusterTemplate resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L23">property apiserverPort</a>
</h3>

```typescript
public apiserverPort: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L24">property clusterDistro</a>
</h3>

```typescript
public clusterDistro: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L25">property coe</a>
</h3>

```typescript
public coe: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L26">property createdAt</a>
</h3>

```typescript
public createdAt: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L27">property dnsNameserver</a>
</h3>

```typescript
public dnsNameserver: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L28">property dockerStorageDriver</a>
</h3>

```typescript
public dockerStorageDriver: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L29">property dockerVolumeSize</a>
</h3>

```typescript
public dockerVolumeSize: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L30">property externalNetworkId</a>
</h3>

```typescript
public externalNetworkId: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L31">property fixedNetwork</a>
</h3>

```typescript
public fixedNetwork: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L32">property fixedSubnet</a>
</h3>

```typescript
public fixedSubnet: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L33">property flavor</a>
</h3>

```typescript
public flavor: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L34">property floatingIpEnabled</a>
</h3>

```typescript
public floatingIpEnabled: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L35">property httpProxy</a>
</h3>

```typescript
public httpProxy: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L36">property httpsProxy</a>
</h3>

```typescript
public httpsProxy: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L37">property image</a>
</h3>

```typescript
public image: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L38">property insecureRegistry</a>
</h3>

```typescript
public insecureRegistry: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L39">property keypairId</a>
</h3>

```typescript
public keypairId: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L40">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L41">property masterFlavor</a>
</h3>

```typescript
public masterFlavor: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L42">property masterLbEnabled</a>
</h3>

```typescript
public masterLbEnabled: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L43">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L44">property networkDriver</a>
</h3>

```typescript
public networkDriver: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L45">property noProxy</a>
</h3>

```typescript
public noProxy: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L46">property projectId</a>
</h3>

```typescript
public projectId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L47">property public</a>
</h3>

```typescript
public public: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L48">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L49">property registryEnabled</a>
</h3>

```typescript
public registryEnabled: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L50">property serverType</a>
</h3>

```typescript
public serverType: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L51">property tlsDisabled</a>
</h3>

```typescript
public tlsDisabled: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L52">property updatedAt</a>
</h3>

```typescript
public updatedAt: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L53">property userId</a>
</h3>

```typescript
public userId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L54">property volumeDriver</a>
</h3>

```typescript
public volumeDriver: pulumi.Output<string | undefined>;
```

<h2 class="pdoc-module-header" id="getClusterTemplate">
<a class="pdoc-member-name" href="/containerinfra/getClusterTemplate.ts#L11">function getClusterTemplate</a>
</h2>

```typescript
getClusterTemplate(args: GetClusterTemplateArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterTemplateResult>
```


Use this data source to get the ID of an available OpenStack Magnum cluster
template.

<h2 class="pdoc-module-header" id="ClusterArgs">
<a class="pdoc-member-name" href="/containerinfra/cluster.ts#L143">interface ClusterArgs</a>
</h2>

The set of arguments for constructing a Cluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L144">property clusterTemplateId</a>
</h3>

```typescript
clusterTemplateId: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L145">property createTimeout</a>
</h3>

```typescript
createTimeout?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L146">property discoveryUrl</a>
</h3>

```typescript
discoveryUrl?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L147">property dockerVolumeSize</a>
</h3>

```typescript
dockerVolumeSize?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L148">property flavor</a>
</h3>

```typescript
flavor?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L149">property keypair</a>
</h3>

```typescript
keypair?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L150">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L151">property masterCount</a>
</h3>

```typescript
masterCount?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L152">property masterFlavor</a>
</h3>

```typescript
masterFlavor?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L153">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L154">property nodeCount</a>
</h3>

```typescript
nodeCount?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L155">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="ClusterState">
<a class="pdoc-member-name" href="/containerinfra/cluster.ts#L115">interface ClusterState</a>
</h2>

Input properties used for looking up and filtering Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L116">property apiAddress</a>
</h3>

```typescript
apiAddress?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L117">property clusterTemplateId</a>
</h3>

```typescript
clusterTemplateId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L118">property coeVersion</a>
</h3>

```typescript
coeVersion?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L119">property containerVersion</a>
</h3>

```typescript
containerVersion?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L120">property createTimeout</a>
</h3>

```typescript
createTimeout?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L121">property createdAt</a>
</h3>

```typescript
createdAt?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L122">property discoveryUrl</a>
</h3>

```typescript
discoveryUrl?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L123">property dockerVolumeSize</a>
</h3>

```typescript
dockerVolumeSize?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L124">property flavor</a>
</h3>

```typescript
flavor?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L125">property keypair</a>
</h3>

```typescript
keypair?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L126">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L127">property masterAddresses</a>
</h3>

```typescript
masterAddresses?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L128">property masterCount</a>
</h3>

```typescript
masterCount?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L129">property masterFlavor</a>
</h3>

```typescript
masterFlavor?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L130">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L131">property nodeAddresses</a>
</h3>

```typescript
nodeAddresses?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L132">property nodeCount</a>
</h3>

```typescript
nodeCount?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L133">property projectId</a>
</h3>

```typescript
projectId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L134">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L135">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L136">property updatedAt</a>
</h3>

```typescript
updatedAt?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/cluster.ts#L137">property userId</a>
</h3>

```typescript
userId?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="ClusterTemplateArgs">
<a class="pdoc-member-name" href="/containerinfra/clusterTemplate.ts#L186">interface ClusterTemplateArgs</a>
</h2>

The set of arguments for constructing a ClusterTemplate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L187">property apiserverPort</a>
</h3>

```typescript
apiserverPort?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L188">property clusterDistro</a>
</h3>

```typescript
clusterDistro?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L189">property coe</a>
</h3>

```typescript
coe: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L190">property dnsNameserver</a>
</h3>

```typescript
dnsNameserver?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L191">property dockerStorageDriver</a>
</h3>

```typescript
dockerStorageDriver?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L192">property dockerVolumeSize</a>
</h3>

```typescript
dockerVolumeSize?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L193">property externalNetworkId</a>
</h3>

```typescript
externalNetworkId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L194">property fixedNetwork</a>
</h3>

```typescript
fixedNetwork?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L195">property fixedSubnet</a>
</h3>

```typescript
fixedSubnet?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L196">property flavor</a>
</h3>

```typescript
flavor?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L197">property floatingIpEnabled</a>
</h3>

```typescript
floatingIpEnabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L198">property httpProxy</a>
</h3>

```typescript
httpProxy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L199">property httpsProxy</a>
</h3>

```typescript
httpsProxy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L200">property image</a>
</h3>

```typescript
image: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L201">property insecureRegistry</a>
</h3>

```typescript
insecureRegistry?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L202">property keypairId</a>
</h3>

```typescript
keypairId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L203">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L204">property masterFlavor</a>
</h3>

```typescript
masterFlavor?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L205">property masterLbEnabled</a>
</h3>

```typescript
masterLbEnabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L206">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L207">property networkDriver</a>
</h3>

```typescript
networkDriver?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L208">property noProxy</a>
</h3>

```typescript
noProxy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L209">property public</a>
</h3>

```typescript
public?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L210">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L211">property registryEnabled</a>
</h3>

```typescript
registryEnabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L212">property serverType</a>
</h3>

```typescript
serverType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L213">property tlsDisabled</a>
</h3>

```typescript
tlsDisabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L214">property volumeDriver</a>
</h3>

```typescript
volumeDriver?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="ClusterTemplateState">
<a class="pdoc-member-name" href="/containerinfra/clusterTemplate.ts#L148">interface ClusterTemplateState</a>
</h2>

Input properties used for looking up and filtering ClusterTemplate resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L149">property apiserverPort</a>
</h3>

```typescript
apiserverPort?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L150">property clusterDistro</a>
</h3>

```typescript
clusterDistro?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L151">property coe</a>
</h3>

```typescript
coe?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L152">property createdAt</a>
</h3>

```typescript
createdAt?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L153">property dnsNameserver</a>
</h3>

```typescript
dnsNameserver?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L154">property dockerStorageDriver</a>
</h3>

```typescript
dockerStorageDriver?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L155">property dockerVolumeSize</a>
</h3>

```typescript
dockerVolumeSize?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L156">property externalNetworkId</a>
</h3>

```typescript
externalNetworkId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L157">property fixedNetwork</a>
</h3>

```typescript
fixedNetwork?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L158">property fixedSubnet</a>
</h3>

```typescript
fixedSubnet?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L159">property flavor</a>
</h3>

```typescript
flavor?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L160">property floatingIpEnabled</a>
</h3>

```typescript
floatingIpEnabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L161">property httpProxy</a>
</h3>

```typescript
httpProxy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L162">property httpsProxy</a>
</h3>

```typescript
httpsProxy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L163">property image</a>
</h3>

```typescript
image?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L164">property insecureRegistry</a>
</h3>

```typescript
insecureRegistry?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L165">property keypairId</a>
</h3>

```typescript
keypairId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L166">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L167">property masterFlavor</a>
</h3>

```typescript
masterFlavor?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L168">property masterLbEnabled</a>
</h3>

```typescript
masterLbEnabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L169">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L170">property networkDriver</a>
</h3>

```typescript
networkDriver?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L171">property noProxy</a>
</h3>

```typescript
noProxy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L172">property projectId</a>
</h3>

```typescript
projectId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L173">property public</a>
</h3>

```typescript
public?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L174">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L175">property registryEnabled</a>
</h3>

```typescript
registryEnabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L176">property serverType</a>
</h3>

```typescript
serverType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L177">property tlsDisabled</a>
</h3>

```typescript
tlsDisabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L178">property updatedAt</a>
</h3>

```typescript
updatedAt?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L179">property userId</a>
</h3>

```typescript
userId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/clusterTemplate.ts#L180">property volumeDriver</a>
</h3>

```typescript
volumeDriver?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="GetClusterTemplateArgs">
<a class="pdoc-member-name" href="/containerinfra/getClusterTemplate.ts#L21">interface GetClusterTemplateArgs</a>
</h2>

A collection of arguments for invoking getClusterTemplate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L25">property name</a>
</h3>

```typescript
name: string;
```


The name of the cluster template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L31">property region</a>
</h3>

```typescript
region?: string;
```


The region in which to obtain the V1 Container Infra
client.
If omitted, the `region` argument of the provider is used.

<h2 class="pdoc-module-header" id="GetClusterTemplateResult">
<a class="pdoc-member-name" href="/containerinfra/getClusterTemplate.ts#L37">interface GetClusterTemplateResult</a>
</h2>

A collection of values returned by getClusterTemplate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L42">property apiserverPort</a>
</h3>

```typescript
apiserverPort: number;
```


The API server port for the Container Orchestration
Engine for this cluster template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L46">property clusterDistro</a>
</h3>

```typescript
clusterDistro: string;
```


The distro for the cluster (fedora-atomic, coreos, etc.).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L50">property coe</a>
</h3>

```typescript
coe: string;
```


The Container Orchestration Engine for this cluster template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L54">property createdAt</a>
</h3>

```typescript
createdAt: string;
```


The time at which cluster template was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L59">property dnsNameserver</a>
</h3>

```typescript
dnsNameserver: string;
```


Address of the DNS nameserver that is used in nodes of the
cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L64">property dockerStorageDriver</a>
</h3>

```typescript
dockerStorageDriver: string;
```


Docker storage driver. Changing this updates the
Docker storage driver of the existing cluster template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L68">property dockerVolumeSize</a>
</h3>

```typescript
dockerVolumeSize: number;
```


The size (in GB) of the Docker volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L73">property externalNetworkId</a>
</h3>

```typescript
externalNetworkId: string;
```


The ID of the external network that will be used for
the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L77">property fixedNetwork</a>
</h3>

```typescript
fixedNetwork: string;
```


The fixed network that will be attached to the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L81">property fixedSubnet</a>
</h3>

```typescript
fixedSubnet: string;
```


=The fixed subnet that will be attached to the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L85">property flavor</a>
</h3>

```typescript
flavor: string;
```


The flavor for the nodes of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L90">property floatingIpEnabled</a>
</h3>

```typescript
floatingIpEnabled: boolean;
```


Indicates whether created cluster should create IP
floating IP for every node or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L95">property httpProxy</a>
</h3>

```typescript
httpProxy: string;
```


The address of a proxy for receiving all HTTP requests and
relay them.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L100">property httpsProxy</a>
</h3>

```typescript
httpsProxy: string;
```


The address of a proxy for receiving all HTTPS requests and
relay them.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L177">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L104">property image</a>
</h3>

```typescript
image: string;
```


The reference to an image that is used for nodes of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L108">property insecureRegistry</a>
</h3>

```typescript
insecureRegistry: string;
```


The insecure registry URL for the cluster template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L112">property keypairId</a>
</h3>

```typescript
keypairId: string;
```


The name of the Compute service SSH keypair.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L117">property labels</a>
</h3>

```typescript
labels: { ... };
```


The list of key value pairs representing additional properties
of the cluster template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L121">property masterFlavor</a>
</h3>

```typescript
masterFlavor: string;
```


The flavor for the master nodes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L126">property masterLbEnabled</a>
</h3>

```typescript
masterLbEnabled: boolean;
```


Indicates whether created cluster should has a
loadbalancer for master nodes or not.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L130">property networkDriver</a>
</h3>

```typescript
networkDriver: string;
```


The name of the driver for the container network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L135">property noProxy</a>
</h3>

```typescript
noProxy: string;
```


A comma-separated list of IP addresses that shouldn't be used in
the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L139">property projectId</a>
</h3>

```typescript
projectId: string;
```


The project of the cluster template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L143">property public</a>
</h3>

```typescript
public: boolean;
```


Indicates whether cluster template should be public.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L147">property region</a>
</h3>

```typescript
region: string;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L152">property registryEnabled</a>
</h3>

```typescript
registryEnabled: boolean;
```


Indicates whether Docker registry is enabled in the
cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L156">property serverType</a>
</h3>

```typescript
serverType: string;
```


The server type for the cluster template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L160">property tlsDisabled</a>
</h3>

```typescript
tlsDisabled: boolean;
```


Indicates whether the TLS should be disabled in the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L164">property updatedAt</a>
</h3>

```typescript
updatedAt: string;
```


The time at which cluster template was updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L168">property userId</a>
</h3>

```typescript
userId: string;
```


The user of the cluster template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/containerinfra/getClusterTemplate.ts#L173">property volumeDriver</a>
</h3>

```typescript
volumeDriver: string;
```


The name of the driver that is used for the volumes of the
cluster nodes.

