---
title: Package @pulumi/eks
---


Node.js:

```javascript
var eks = require("@pulumi/eks");
```

ES6 modules:

```typescript
import * as eks from "@pulumi/eks";
```

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Cluster">class Cluster</a>
* <a href="#ServiceRole">class ServiceRole</a>
* <a href="#createStorageClass">function createStorageClass</a>
* <a href="#ClusterOptions">interface ClusterOptions</a>
* <a href="#ServiceRoleArgs">interface ServiceRoleArgs</a>
* <a href="#StorageClass">interface StorageClass</a>
* <a href="#EBSVolumeType">type EBSVolumeType</a>

<a href="/cluster.ts">cluster.ts</a> <a href="/servicerole.ts">servicerole.ts</a> <a href="/storageclass.ts">storageclass.ts</a> 


<h2 class="pdoc-module-header" id="Cluster">
<a class="pdoc-member-name" href="/cluster.ts#L108">class Cluster</a>
</h2>

Cluster is a component that wraps the AWS and Kubernetes resources necessary to run an EKS cluster, its worker
nodes, its optional StorageClasses, and an optional deployment of the Kubernetes Dashboard.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/cluster.ts#L133">constructor</a>
</h3>

```typescript
new Cluster(name: string, args?: ClusterOptions, opts?: pulumi.ComponentResourceOptions)
```


Create a new EKS cluster with worker nodes, optional storage classes, and deploy the Kubernetes Dashboard if
requested.

* `name` The _unique_ name of this component.
* `args` The arguments for this cluster.
* `opts` A bag of options that control this copmonent&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/cluster.ts#L128">property clusterSecurityGroup</a>
</h3>

```typescript
public clusterSecurityGroup: aws.ec2.SecurityGroup;
```


The security group for the EKS cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/cluster.ts#L113">property kubeconfig</a>
</h3>

```typescript
public kubeconfig: pulumi.Output<any>;
```


A kubeconfig that can be used to connect to the EKS cluster. This must be serialized as a string before passing
to the Kubernetes provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/cluster.ts#L133">property nodeSecurityGroup</a>
</h3>

```typescript
public nodeSecurityGroup: aws.ec2.SecurityGroup;
```


The security group for the cluster's nodes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/cluster.ts#L123">property provider</a>
</h3>

```typescript
public provider: k8s.Provider;
```


A Kubernetes resource provider that can be used to deploy into this cluster. For example, the code below will
create a new Pod in the EKS cluster.

    let eks = new Cluster("eks");
    let pod = new kubernetes.core.v1.Pod("pod", { ... }, { provider: eks.provider });


<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ServiceRole">
<a class="pdoc-member-name" href="/servicerole.ts#L49">class ServiceRole</a>
</h2>

The ServiceRole component creates an IAM role for a particular service and attaches to it a list of well-known
managed policies.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/servicerole.ts#L51">constructor</a>
</h3>

```typescript
new ServiceRole(name: string, args: ServiceRoleArgs, opts?: pulumi.ResourceOptions)
```


Create a new ServiceRole.

* `name` The _unique_ name of this component.
* `args` The arguments for this cluster.
* `opts` A bag of options that control this copmonent&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/servicerole.ts#L51">property role</a>
</h3>

```typescript
public role: pulumi.Output<aws.iam.Role>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="createStorageClass">
<a class="pdoc-member-name" href="/storageclass.ts#L98">function createStorageClass</a>
</h2>

```typescript
createStorageClass(name: string, storageClass: StorageClass, opts: pulumi.CustomResourceOptions): void
```

<h2 class="pdoc-module-header" id="ClusterOptions">
<a class="pdoc-member-name" href="/cluster.ts#L29">interface ClusterOptions</a>
</h2>

ClusterOptions describes the configuration options accepted by an EKSCluster component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/cluster.ts#L101">property deployDashboard</a>
</h3>

```typescript
deployDashboard?: undefined | false | true;
```


Whether or not to deploy the Kubernetes dashboard to the cluster. If the dashboard is deployed, it can be
accessed as follows:
1. Retrieve an authentication token for the dashboard by running the following and copying the value of `token`
  from the output of the last command:

    $ kubectl -n kube-system get secret | grep eks-admin | awk '{print $1}'
    $ kubectl -n kube-system describe secret <output from previous command>

2. Start the kubectl proxt:

    $ kubectl proxy

3. Open `http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/` in a
   web browser.
4. Choose `Token` authentication, paste the token retrieved earlier into the `Token` field, and sign in.

Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/cluster.ts#L62">property desiredCapacity</a>
</h3>

```typescript
desiredCapacity?: pulumi.Input<number>;
```


The number of worker nodes that should be running in the cluster. Defaults to 2.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/cluster.ts#L45">property instanceType</a>
</h3>

```typescript
instanceType?: pulumi.Input<aws.ec2.InstanceType>;
```


The instance type to use for the cluster's nodes. Defaults to "t2.medium".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/cluster.ts#L72">property maxSize</a>
</h3>

```typescript
maxSize?: pulumi.Input<number>;
```


The maximum number of worker nodes running in the cluster. Defaults to 2.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/cluster.ts#L67">property minSize</a>
</h3>

```typescript
minSize?: pulumi.Input<number>;
```


The minimum number of worker nodes running in the cluster. Defaults to 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/cluster.ts#L52">property nodePublicKey</a>
</h3>

```typescript
nodePublicKey?: pulumi.Input<string>;
```


Public key material for SSH access to worker nodes. See allowed formats at:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html
If not provided, no SSH access is enabled on VMs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/cluster.ts#L57">property nodeRootVolumeSize</a>
</h3>

```typescript
nodeRootVolumeSize?: pulumi.Input<number>;
```


The size in GiB of a cluster node's root volume. Defaults to 20.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/cluster.ts#L80">property storageClasses</a>
</h3>

```typescript
storageClasses?: { ... } | EBSVolumeType;
```


An optional set of StorageClasses to enable for the cluster. If this is a single volume type rather than a map,
a single StorageClass will be created for that volume type and made the cluster's default StorageClass.

Defaults to "gp2".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/cluster.ts#L40">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The subnets to attach to the EKS cluster. If either vpcId or subnetIds is unset, the cluster will use the
default VPC's subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/cluster.ts#L34">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The VPC in which to create the cluster and its worker nodes. If unset, the cluster will be created in the
default VPC.

<h2 class="pdoc-module-header" id="ServiceRoleArgs">
<a class="pdoc-member-name" href="/servicerole.ts#L30">interface ServiceRoleArgs</a>
</h2>

ServiceRoleArgs describe the parameters to a ServiceRole component.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/servicerole.ts#L38">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/servicerole.ts#L42">property managedPolicyArns</a>
</h3>

```typescript
managedPolicyArns?: string[];
```


One or more managed policy ARNs to attach to this role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/servicerole.ts#L34">property service</a>
</h3>

```typescript
service: pulumi.Input<string>;
```


The service associated with this role.

<h2 class="pdoc-module-header" id="StorageClass">
<a class="pdoc-member-name" href="/storageclass.ts#L30">interface StorageClass</a>
</h2>

StorageClass describes the inputs to a single Kubernetes StorageClass provisioned by AWS. Any number of storage
classes can be added to a cluster at creation time. One of these storage classes may be configured the default
storage class for the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageclass.ts#L68">property allowVolumeExpansion</a>
</h3>

```typescript
allowVolumeExpansion?: pulumi.Input<boolean>;
```


AllowVolumeExpansion shows whether the storage class allow volume expand

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageclass.ts#L63">property default</a>
</h3>

```typescript
default?: pulumi.Input<boolean>;
```


True if this storage class should be the default storage class for the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageclass.ts#L52">property encrypted</a>
</h3>

```typescript
encrypted?: pulumi.Input<boolean>;
```


Denotes whether the EBS volume should be encrypted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageclass.ts#L47">property iopsPerGb</a>
</h3>

```typescript
iopsPerGb?: pulumi.Input<number>;
```


I/O operations per second per GiB for "io1" volumes. The AWS volume plugin multiplies this with the size of a
requested volume to compute IOPS of the volume and caps the result at 20,000 IOPS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageclass.ts#L58">property kmsKeyId</a>
</h3>

```typescript
kmsKeyId?: pulumi.Input<string>;
```


The full Amazon Resource Name of the key to use when encrypting the volume. If none is supplied but encrypted is
true, a key is generated by AWS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageclass.ts#L74">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<k8sInputs.meta.v1.ObjectMeta>;
```


Standard object's metadata. More info:
https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageclass.ts#L81">property mountOptions</a>
</h3>

```typescript
mountOptions?: pulumi.Input<string[]>;
```


Dynamically provisioned PersistentVolumes of this storage class are created with these
mountOptions, e.g. ["ro", "soft"]. Not validated - mount of the PVs will simply fail if one
is invalid.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageclass.ts#L87">property reclaimPolicy</a>
</h3>

```typescript
reclaimPolicy?: pulumi.Input<string>;
```


Dynamically provisioned PersistentVolumes of this storage class are created with this
reclaimPolicy. Defaults to Delete.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageclass.ts#L34">property type</a>
</h3>

```typescript
type: pulumi.Input<EBSVolumeType>;
```


The EBS volume type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageclass.ts#L94">property volumeBindingMode</a>
</h3>

```typescript
volumeBindingMode?: pulumi.Input<string>;
```


VolumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.
When unset, VolumeBindingImmediate is used. This field is alpha-level and is only honored
by servers that enable the VolumeScheduling feature.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storageclass.ts#L41">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<pulumi.Input<string>[]>;
```


The AWS zone or zones for the EBS volume. If zones is not specified, volumes are generally round-robin-ed across
all active zones where Kubernetes cluster has a node. zone and zones parameters must not be used at the same
time.

<h2 class="pdoc-module-header" id="EBSVolumeType">
<a class="pdoc-member-name" href="/storageclass.ts#L23">type EBSVolumeType</a>
</h2>

```typescript
type EBSVolumeType = io1 | gp2 | sc1 | st1;
```


EBSVolumeType lists the set of volume types accepted by an EKS storage class.

