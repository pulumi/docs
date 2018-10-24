---
title: Module servicefabric
---

<a href="../index.html">@pulumi/azure</a> &gt; servicefabric

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Cluster">class Cluster</a>
* <a href="#ClusterArgs">interface ClusterArgs</a>
* <a href="#ClusterState">interface ClusterState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts">servicefabric/cluster.ts</a> 


<h2 class="pdoc-module-header" id="Cluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L10">class Cluster</a>
</h2>

Manage a Service Fabric Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L86">constructor</a>
</h3>

```typescript
new Cluster(name: string, args: ClusterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Cluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterState): Cluster
```


Get an existing Cluster resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L26">property addOnFeatures</a>
</h3>

```typescript
public addOnFeatures: pulumi.Output<string[] | undefined>;
```


A List of one or more features which should be enabled, such as `DnsService`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L30">property certificate</a>
</h3>

```typescript
public certificate: pulumi.Output<{ ... } | undefined>;
```


A `certificate` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L34">property clientCertificateThumbprints</a>
</h3>

```typescript
public clientCertificateThumbprints: pulumi.Output<{ ... }[] | undefined>;
```


One or two `client_certificate_thumbprint` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L38">property clusterCodeVersion</a>
</h3>

```typescript
public clusterCodeVersion: pulumi.Output<string>;
```


Required if Upgrade Mode set to `Manual`, Specifies the Version of the Cluster Code of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L42">property clusterEndpoint</a>
</h3>

```typescript
public clusterEndpoint: pulumi.Output<string>;
```


The Cluster Endpoint for this Service Fabric Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L46">property diagnosticsConfig</a>
</h3>

```typescript
public diagnosticsConfig: pulumi.Output<{ ... } | undefined>;
```


A `diagnostics_config` block as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L50">property fabricSettings</a>
</h3>

```typescript
public fabricSettings: pulumi.Output<{ ... }[] | undefined>;
```


One or more `fabric_settings` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L54">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L58">property managementEndpoint</a>
</h3>

```typescript
public managementEndpoint: pulumi.Output<string>;
```


Specifies the Management Endpoint of the cluster such as `http://example.com`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L62">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Service Fabric Cluster. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L66">property nodeTypes</a>
</h3>

```typescript
public nodeTypes: pulumi.Output<{ ... }[]>;
```


One or more `node_type` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L70">property reliabilityLevel</a>
</h3>

```typescript
public reliabilityLevel: pulumi.Output<string>;
```


Specifies the Reliability Level of the Cluster. Possible values include `None`, `Bronze`, `Silver`, `Gold` and `Platinum`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L74">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L78">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L82">property upgradeMode</a>
</h3>

```typescript
public upgradeMode: pulumi.Output<string>;
```


Specifies the Upgrade Mode of the cluster. Possible values are `Automatic` or `Manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L86">property vmImage</a>
</h3>

```typescript
public vmImage: pulumi.Output<string>;
```


Specifies the Image expected for the Service Fabric Cluster, such as `Windows`. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L233">interface ClusterArgs</a>
</h2>

The set of arguments for constructing a Cluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L237">property addOnFeatures</a>
</h3>

```typescript
addOnFeatures?: pulumi.Input<pulumi.Input<string>[]>;
```


A List of one or more features which should be enabled, such as `DnsService`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L241">property certificate</a>
</h3>

```typescript
certificate?: pulumi.Input<{ ... }>;
```


A `certificate` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L245">property clientCertificateThumbprints</a>
</h3>

```typescript
clientCertificateThumbprints?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or two `client_certificate_thumbprint` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L249">property clusterCodeVersion</a>
</h3>

```typescript
clusterCodeVersion?: pulumi.Input<string>;
```


Required if Upgrade Mode set to `Manual`, Specifies the Version of the Cluster Code of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L253">property diagnosticsConfig</a>
</h3>

```typescript
diagnosticsConfig?: pulumi.Input<{ ... }>;
```


A `diagnostics_config` block as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L257">property fabricSettings</a>
</h3>

```typescript
fabricSettings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `fabric_settings` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L261">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L265">property managementEndpoint</a>
</h3>

```typescript
managementEndpoint: pulumi.Input<string>;
```


Specifies the Management Endpoint of the cluster such as `http://example.com`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L269">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Service Fabric Cluster. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L273">property nodeTypes</a>
</h3>

```typescript
nodeTypes: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `node_type` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L277">property reliabilityLevel</a>
</h3>

```typescript
reliabilityLevel: pulumi.Input<string>;
```


Specifies the Reliability Level of the Cluster. Possible values include `None`, `Bronze`, `Silver`, `Gold` and `Platinum`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L281">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L285">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L289">property upgradeMode</a>
</h3>

```typescript
upgradeMode: pulumi.Input<string>;
```


Specifies the Upgrade Mode of the cluster. Possible values are `Automatic` or `Manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L293">property vmImage</a>
</h3>

```typescript
vmImage: pulumi.Input<string>;
```


Specifies the Image expected for the Service Fabric Cluster, such as `Windows`. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ClusterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L163">interface ClusterState</a>
</h2>

Input properties used for looking up and filtering Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L167">property addOnFeatures</a>
</h3>

```typescript
addOnFeatures?: pulumi.Input<pulumi.Input<string>[]>;
```


A List of one or more features which should be enabled, such as `DnsService`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L171">property certificate</a>
</h3>

```typescript
certificate?: pulumi.Input<{ ... }>;
```


A `certificate` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L175">property clientCertificateThumbprints</a>
</h3>

```typescript
clientCertificateThumbprints?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or two `client_certificate_thumbprint` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L179">property clusterCodeVersion</a>
</h3>

```typescript
clusterCodeVersion?: pulumi.Input<string>;
```


Required if Upgrade Mode set to `Manual`, Specifies the Version of the Cluster Code of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L183">property clusterEndpoint</a>
</h3>

```typescript
clusterEndpoint?: pulumi.Input<string>;
```


The Cluster Endpoint for this Service Fabric Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L187">property diagnosticsConfig</a>
</h3>

```typescript
diagnosticsConfig?: pulumi.Input<{ ... }>;
```


A `diagnostics_config` block as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L191">property fabricSettings</a>
</h3>

```typescript
fabricSettings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `fabric_settings` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L195">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L199">property managementEndpoint</a>
</h3>

```typescript
managementEndpoint?: pulumi.Input<string>;
```


Specifies the Management Endpoint of the cluster such as `http://example.com`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L203">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Service Fabric Cluster. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L207">property nodeTypes</a>
</h3>

```typescript
nodeTypes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `node_type` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L211">property reliabilityLevel</a>
</h3>

```typescript
reliabilityLevel?: pulumi.Input<string>;
```


Specifies the Reliability Level of the Cluster. Possible values include `None`, `Bronze`, `Silver`, `Gold` and `Platinum`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L215">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L219">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L223">property upgradeMode</a>
</h3>

```typescript
upgradeMode?: pulumi.Input<string>;
```


Specifies the Upgrade Mode of the cluster. Possible values are `Automatic` or `Manual`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/servicefabric/cluster.ts#L227">property vmImage</a>
</h3>

```typescript
vmImage?: pulumi.Input<string>;
```


Specifies the Image expected for the Service Fabric Cluster, such as `Windows`. Changing this forces a new resource to be created.

