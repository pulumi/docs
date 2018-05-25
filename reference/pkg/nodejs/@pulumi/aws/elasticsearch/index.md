---
title: Module elasticsearch
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Domain">class Domain</a>
* <a href="#DomainPolicy">class DomainPolicy</a>
* <a href="#DomainArgs">interface DomainArgs</a>
* <a href="#DomainPolicyArgs">interface DomainPolicyArgs</a>
* <a href="#DomainPolicyState">interface DomainPolicyState</a>
* <a href="#DomainState">interface DomainState</a>

<a href="/elasticsearch/domain.ts">elasticsearch/domain.ts</a> <a href="/elasticsearch/domainPolicy.ts">elasticsearch/domainPolicy.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Domain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L6">class Domain</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L80">constructor</a>
</h3>

```typescript
new Domain(name: string, args?: DomainArgs, opts?: pulumi.ResourceOptions)
```


Create a Domain resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Domain(name: string, state?: DomainState, opts?: pulumi.ResourceOptions)
```


Create a Domain resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L15">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DomainState): Domain
```


Get an existing Domain resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L22">property accessPolicies</a>
</h3>

```typescript
public accessPolicies: pulumi.Output<string>;
```


IAM policy document specifying the access policies for the domain

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L26">property advancedOptions</a>
</h3>

```typescript
public advancedOptions: pulumi.Output<{ ... }>;
```


Key-value string pairs to specify advanced configuration options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L30">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L34">property clusterConfig</a>
</h3>

```typescript
public clusterConfig: pulumi.Output<{ ... }>;
```


Cluster configuration of the domain, see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L38">property domainId</a>
</h3>

```typescript
public domainId: pulumi.Output<string>;
```


Unique identifier for the domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L42">property domainName</a>
</h3>

```typescript
public domainName: pulumi.Output<string>;
```


Name of the domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L46">property ebsOptions</a>
</h3>

```typescript
public ebsOptions: pulumi.Output<{ ... }>;
```


EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L50">property elasticsearchVersion</a>
</h3>

```typescript
public elasticsearchVersion: pulumi.Output<string | undefined>;
```


The version of ElasticSearch to deploy. Defaults to `1.5`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L54">property encryptAtRest</a>
</h3>

```typescript
public encryptAtRest: pulumi.Output<{ ... }>;
```


Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L58">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


Domain-specific endpoint used to submit index, search, and data upload requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L64">property kibanaEndpoint</a>
</h3>

```typescript
public kibanaEndpoint: pulumi.Output<string>;
```


Domain-specific endpoint for kibana without https scheme.
* `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
* `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L68">property logPublishingOptions</a>
</h3>

```typescript
public logPublishingOptions: pulumi.Output<{ ... }[] | undefined>;
```


Options for publishing slow logs to CloudWatch Logs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L72">property snapshotOptions</a>
</h3>

```typescript
public snapshotOptions: pulumi.Output<{ ... } | undefined>;
```


Snapshot related options, see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L76">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


A mapping of tags to assign to the resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L80">property vpcOptions</a>
</h3>

```typescript
public vpcOptions: pulumi.Output<{ ... } | undefined>;
```


VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).

<h2 class="pdoc-module-header" id="DomainPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domainPolicy.ts#L9">class DomainPolicy</a>
</h2>

Allows setting policy to an ElasticSearch domain while referencing domain attributes (e.g. ARN)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domainPolicy.ts#L29">constructor</a>
</h3>

```typescript
new DomainPolicy(name: string, args: DomainPolicyArgs, opts?: pulumi.ResourceOptions)
```


Create a DomainPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new DomainPolicy(name: string, state?: DomainPolicyState, opts?: pulumi.ResourceOptions)
```


Create a DomainPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domainPolicy.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DomainPolicyState): DomainPolicy
```


Get an existing DomainPolicy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domainPolicy.ts#L25">property accessPolicies</a>
</h3>

```typescript
public accessPolicies: pulumi.Output<string>;
```


IAM policy document specifying the access policies for the domain

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domainPolicy.ts#L29">property domainName</a>
</h3>

```typescript
public domainName: pulumi.Output<string>;
```


Name of the domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DomainArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L204">interface DomainArgs</a>
</h2>

The set of arguments for constructing a Domain resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L208">property accessPolicies</a>
</h3>

```typescript
accessPolicies?: pulumi.Input<string>;
```


IAM policy document specifying the access policies for the domain

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L212">property advancedOptions</a>
</h3>

```typescript
advancedOptions?: pulumi.Input<{ ... }>;
```


Key-value string pairs to specify advanced configuration options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L216">property clusterConfig</a>
</h3>

```typescript
clusterConfig?: pulumi.Input<{ ... }>;
```


Cluster configuration of the domain, see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L220">property domainName</a>
</h3>

```typescript
domainName?: pulumi.Input<string>;
```


Name of the domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L224">property ebsOptions</a>
</h3>

```typescript
ebsOptions?: pulumi.Input<{ ... }>;
```


EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L228">property elasticsearchVersion</a>
</h3>

```typescript
elasticsearchVersion?: pulumi.Input<string>;
```


The version of ElasticSearch to deploy. Defaults to `1.5`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L232">property encryptAtRest</a>
</h3>

```typescript
encryptAtRest?: pulumi.Input<{ ... }>;
```


Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L236">property logPublishingOptions</a>
</h3>

```typescript
logPublishingOptions?: pulumi.Input<{ ... }[]>;
```


Options for publishing slow logs to CloudWatch Logs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L240">property snapshotOptions</a>
</h3>

```typescript
snapshotOptions?: pulumi.Input<{ ... }>;
```


Snapshot related options, see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L244">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L248">property vpcOptions</a>
</h3>

```typescript
vpcOptions?: pulumi.Input<{ ... }>;
```


VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).

<h2 class="pdoc-module-header" id="DomainPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domainPolicy.ts#L79">interface DomainPolicyArgs</a>
</h2>

The set of arguments for constructing a DomainPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domainPolicy.ts#L83">property accessPolicies</a>
</h3>

```typescript
accessPolicies: pulumi.Input<string>;
```


IAM policy document specifying the access policies for the domain

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domainPolicy.ts#L87">property domainName</a>
</h3>

```typescript
domainName: pulumi.Input<string>;
```


Name of the domain.

<h2 class="pdoc-module-header" id="DomainPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domainPolicy.ts#L65">interface DomainPolicyState</a>
</h2>

Input properties used for looking up and filtering DomainPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domainPolicy.ts#L69">property accessPolicies</a>
</h3>

```typescript
accessPolicies?: pulumi.Input<string>;
```


IAM policy document specifying the access policies for the domain

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domainPolicy.ts#L73">property domainName</a>
</h3>

```typescript
domainName?: pulumi.Input<string>;
```


Name of the domain.

<h2 class="pdoc-module-header" id="DomainState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L136">interface DomainState</a>
</h2>

Input properties used for looking up and filtering Domain resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L140">property accessPolicies</a>
</h3>

```typescript
accessPolicies?: pulumi.Input<string>;
```


IAM policy document specifying the access policies for the domain

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L144">property advancedOptions</a>
</h3>

```typescript
advancedOptions?: pulumi.Input<{ ... }>;
```


Key-value string pairs to specify advanced configuration options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L148">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L152">property clusterConfig</a>
</h3>

```typescript
clusterConfig?: pulumi.Input<{ ... }>;
```


Cluster configuration of the domain, see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L156">property domainId</a>
</h3>

```typescript
domainId?: pulumi.Input<string>;
```


Unique identifier for the domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L160">property domainName</a>
</h3>

```typescript
domainName?: pulumi.Input<string>;
```


Name of the domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L164">property ebsOptions</a>
</h3>

```typescript
ebsOptions?: pulumi.Input<{ ... }>;
```


EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L168">property elasticsearchVersion</a>
</h3>

```typescript
elasticsearchVersion?: pulumi.Input<string>;
```


The version of ElasticSearch to deploy. Defaults to `1.5`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L172">property encryptAtRest</a>
</h3>

```typescript
encryptAtRest?: pulumi.Input<{ ... }>;
```


Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L176">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


Domain-specific endpoint used to submit index, search, and data upload requests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L182">property kibanaEndpoint</a>
</h3>

```typescript
kibanaEndpoint?: pulumi.Input<string>;
```


Domain-specific endpoint for kibana without https scheme.
* `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
* `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L186">property logPublishingOptions</a>
</h3>

```typescript
logPublishingOptions?: pulumi.Input<{ ... }[]>;
```


Options for publishing slow logs to CloudWatch Logs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L190">property snapshotOptions</a>
</h3>

```typescript
snapshotOptions?: pulumi.Input<{ ... }>;
```


Snapshot related options, see below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L194">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticsearch/domain.ts#L198">property vpcOptions</a>
</h3>

```typescript
vpcOptions?: pulumi.Input<{ ... }>;
```


VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).

