---
title: Module cloudhsmv2
---

<a href="../index.html">@pulumi/aws</a> &gt; cloudhsmv2

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Cluster">class Cluster</a>
* <a href="#Hsm">class Hsm</a>
* <a href="#getCluster">function getCluster</a>
* <a href="#ClusterArgs">interface ClusterArgs</a>
* <a href="#ClusterState">interface ClusterState</a>
* <a href="#GetClusterArgs">interface GetClusterArgs</a>
* <a href="#GetClusterResult">interface GetClusterResult</a>
* <a href="#HsmArgs">interface HsmArgs</a>
* <a href="#HsmState">interface HsmState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts">cloudhsmv2/cluster.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/getCluster.ts">cloudhsmv2/getCluster.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts">cloudhsmv2/hsm.ts</a> 


<h2 class="pdoc-module-header" id="Cluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L19">class Cluster</a>
</h2>

Creates an Amazon CloudHSM v2 cluster.

For information about CloudHSM v2, see the
[AWS CloudHSM User Guide][1] and the [Amazon
CloudHSM API Reference][2].

~> **NOTE:** CloudHSM can take up to several minutes to be set up.
Practically no single attribute can be updated except TAGS.
If you need to delete a cluster, you have to remove its HSM modules first.
To initialize cluster you have to sign CSR and upload it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L69">constructor</a>
</h3>

```typescript
new Cluster(name: string, args: ClusterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Cluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L28">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterState): Cluster
```


Get an existing Cluster resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L40">property clusterCertificates</a>
</h3>

```typescript
public clusterCertificates: pulumi.Output<{ ... }>;
```


The list of cluster certificates.
* `cluster_certificates.0.cluster_certificate` - The cluster certificate issued (signed) by the issuing certificate authority (CA) of the cluster's owner.
* `cluster_certificates.0.cluster_csr` - The certificate signing request (CSR). Available only in UNINITIALIZED state.
* `cluster_certificates.0.aws_hardware_certificate` - The HSM hardware certificate issued (signed) by AWS CloudHSM.
* `cluster_certificates.0.hsm_certificate` - The HSM certificate issued (signed) by the HSM hardware.
* `cluster_certificates.0.manufacturer_hardware_certificate` - The HSM hardware certificate issued (signed) by the hardware manufacturer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L44">property clusterId</a>
</h3>

```typescript
public clusterId: pulumi.Output<string>;
```


The id of the CloudHSM cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L48">property clusterState</a>
</h3>

```typescript
public clusterState: pulumi.Output<string>;
```


The state of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L52">property hsmType</a>
</h3>

```typescript
public hsmType: pulumi.Output<string>;
```


The type of HSM module in the cluster. Currently, only hsm1.medium is supported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L56">property securityGroupId</a>
</h3>

```typescript
public securityGroupId: pulumi.Output<string>;
```


The ID of the security group associated with the CloudHSM cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L60">property sourceBackupIdentifier</a>
</h3>

```typescript
public sourceBackupIdentifier: pulumi.Output<string | undefined>;
```


The id of Cloud HSM v2 cluster backup to be restored.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L64">property subnetIds</a>
</h3>

```typescript
public subnetIds: pulumi.Output<string[]>;
```


The IDs of subnets in which cluster will operate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L65">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L69">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The id of the VPC that the CloudHSM cluster resides in.

<h2 class="pdoc-module-header" id="Hsm">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L10">class Hsm</a>
</h2>

Creates an HSM module in Amazon CloudHSM v2 cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L50">constructor</a>
</h3>

```typescript
new Hsm(name: string, args: HsmArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Hsm resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HsmState): Hsm
```


Get an existing Hsm resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L26">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The IDs of AZ in which HSM module will be located. Do not use together with subnet_id.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L30">property clusterId</a>
</h3>

```typescript
public clusterId: pulumi.Output<string>;
```


The ID of Cloud HSM v2 cluster to which HSM will be added.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L34">property hsmEniId</a>
</h3>

```typescript
public hsmEniId: pulumi.Output<string>;
```


The id of the ENI interface allocated for HSM module.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L38">property hsmId</a>
</h3>

```typescript
public hsmId: pulumi.Output<string>;
```


The id of the HSM module.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L42">property hsmState</a>
</h3>

```typescript
public hsmState: pulumi.Output<string>;
```


The state of the HSM module.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L46">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string>;
```


The IP address of HSM module. Must be within the CIDR of selected subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L50">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


The ID of subnet in which HSM module will be located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getCluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/getCluster.ts#L10">function getCluster</a>
</h2>

```typescript
getCluster(args: GetClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterResult>
```


Use this data source to get information about a CloudHSM v2 cluster

<h2 class="pdoc-module-header" id="ClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L161">interface ClusterArgs</a>
</h2>

The set of arguments for constructing a Cluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L165">property hsmType</a>
</h3>

```typescript
hsmType: pulumi.Input<string>;
```


The type of HSM module in the cluster. Currently, only hsm1.medium is supported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L169">property sourceBackupIdentifier</a>
</h3>

```typescript
sourceBackupIdentifier?: pulumi.Input<string>;
```


The id of Cloud HSM v2 cluster backup to be restored.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L173">property subnetIds</a>
</h3>

```typescript
subnetIds: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of subnets in which cluster will operate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L174">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="ClusterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L117">interface ClusterState</a>
</h2>

Input properties used for looking up and filtering Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L126">property clusterCertificates</a>
</h3>

```typescript
clusterCertificates?: pulumi.Input<{ ... }>;
```


The list of cluster certificates.
* `cluster_certificates.0.cluster_certificate` - The cluster certificate issued (signed) by the issuing certificate authority (CA) of the cluster's owner.
* `cluster_certificates.0.cluster_csr` - The certificate signing request (CSR). Available only in UNINITIALIZED state.
* `cluster_certificates.0.aws_hardware_certificate` - The HSM hardware certificate issued (signed) by AWS CloudHSM.
* `cluster_certificates.0.hsm_certificate` - The HSM certificate issued (signed) by the HSM hardware.
* `cluster_certificates.0.manufacturer_hardware_certificate` - The HSM hardware certificate issued (signed) by the hardware manufacturer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L130">property clusterId</a>
</h3>

```typescript
clusterId?: pulumi.Input<string>;
```


The id of the CloudHSM cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L134">property clusterState</a>
</h3>

```typescript
clusterState?: pulumi.Input<string>;
```


The state of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L138">property hsmType</a>
</h3>

```typescript
hsmType?: pulumi.Input<string>;
```


The type of HSM module in the cluster. Currently, only hsm1.medium is supported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L142">property securityGroupId</a>
</h3>

```typescript
securityGroupId?: pulumi.Input<string>;
```


The ID of the security group associated with the CloudHSM cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L146">property sourceBackupIdentifier</a>
</h3>

```typescript
sourceBackupIdentifier?: pulumi.Input<string>;
```


The id of Cloud HSM v2 cluster backup to be restored.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L150">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The IDs of subnets in which cluster will operate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L151">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/cluster.ts#L155">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The id of the VPC that the CloudHSM cluster resides in.

<h2 class="pdoc-module-header" id="GetClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/getCluster.ts#L20">interface GetClusterArgs</a>
</h2>

A collection of arguments for invoking getCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/getCluster.ts#L24">property clusterId</a>
</h3>

```typescript
clusterId: string;
```


The id of Cloud HSM v2 cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/getCluster.ts#L28">property clusterState</a>
</h3>

```typescript
clusterState?: string;
```


The state of the cluster to be found.

<h2 class="pdoc-module-header" id="GetClusterResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/getCluster.ts#L34">interface GetClusterResult</a>
</h2>

A collection of values returned by getCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/getCluster.ts#L44">property clusterCertificates</a>
</h3>

```typescript
clusterCertificates: { ... };
```


The list of cluster certificates.
* `cluster_certificates.0.cluster_certificate` - The cluster certificate issued (signed) by the issuing certificate authority (CA) of the cluster's owner.
* `cluster_certificates.0.cluster_csr` - The certificate signing request (CSR). Available only in UNINITIALIZED state.
* `cluster_certificates.0.aws_hardware_certificate` - The HSM hardware certificate issued (signed) by AWS CloudHSM.
* `cluster_certificates.0.hsm_certificate` - The HSM certificate issued (signed) by the HSM hardware.
* `cluster_certificates.0.manufacturer_hardware_certificate` - The HSM hardware certificate issued (signed) by the hardware manufacturer.
The number of available cluster certificates may vary depending on state of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/getCluster.ts#L45">property clusterState</a>
</h3>

```typescript
clusterState: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/getCluster.ts#L61">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/getCluster.ts#L49">property securityGroupId</a>
</h3>

```typescript
securityGroupId: string;
```


The ID of the security group associated with the CloudHSM cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/getCluster.ts#L53">property subnetIds</a>
</h3>

```typescript
subnetIds: string[];
```


The IDs of subnets in which cluster operates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/getCluster.ts#L57">property vpcId</a>
</h3>

```typescript
vpcId: string;
```


The id of the VPC that the CloudHSM cluster resides in.

<h2 class="pdoc-module-header" id="HsmArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L125">interface HsmArgs</a>
</h2>

The set of arguments for constructing a Hsm resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L129">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The IDs of AZ in which HSM module will be located. Do not use together with subnet_id.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L133">property clusterId</a>
</h3>

```typescript
clusterId: pulumi.Input<string>;
```


The ID of Cloud HSM v2 cluster to which HSM will be added.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L137">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The IP address of HSM module. Must be within the CIDR of selected subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L141">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The ID of subnet in which HSM module will be located.

<h2 class="pdoc-module-header" id="HsmState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L91">interface HsmState</a>
</h2>

Input properties used for looking up and filtering Hsm resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L95">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The IDs of AZ in which HSM module will be located. Do not use together with subnet_id.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L99">property clusterId</a>
</h3>

```typescript
clusterId?: pulumi.Input<string>;
```


The ID of Cloud HSM v2 cluster to which HSM will be added.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L103">property hsmEniId</a>
</h3>

```typescript
hsmEniId?: pulumi.Input<string>;
```


The id of the ENI interface allocated for HSM module.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L107">property hsmId</a>
</h3>

```typescript
hsmId?: pulumi.Input<string>;
```


The id of the HSM module.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L111">property hsmState</a>
</h3>

```typescript
hsmState?: pulumi.Input<string>;
```


The state of the HSM module.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L115">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The IP address of HSM module. Must be within the CIDR of selected subnet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudhsmv2/hsm.ts#L119">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The ID of subnet in which HSM module will be located.

