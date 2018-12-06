---
title: Module datasync
---

<a href="../index.html">@pulumi/aws</a> &gt; datasync

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Agent">class Agent</a>
* <a href="#EfsLocation">class EfsLocation</a>
* <a href="#NfsLocation">class NfsLocation</a>
* <a href="#S3Location">class S3Location</a>
* <a href="#Task">class Task</a>
* <a href="#AgentArgs">interface AgentArgs</a>
* <a href="#AgentState">interface AgentState</a>
* <a href="#EfsLocationArgs">interface EfsLocationArgs</a>
* <a href="#EfsLocationState">interface EfsLocationState</a>
* <a href="#NfsLocationArgs">interface NfsLocationArgs</a>
* <a href="#NfsLocationState">interface NfsLocationState</a>
* <a href="#S3LocationArgs">interface S3LocationArgs</a>
* <a href="#S3LocationState">interface S3LocationState</a>
* <a href="#TaskArgs">interface TaskArgs</a>
* <a href="#TaskState">interface TaskState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts">datasync/agent.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts">datasync/efsLocation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts">datasync/nfsLocation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts">datasync/s3Location.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts">datasync/task.ts</a> 


<h2 class="pdoc-module-header" id="Agent">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L14">class Agent</a>
</h2>

Manages an AWS DataSync Agent deployed on premises.

~> **NOTE:** One of `activation_key` or `ip_address` must be provided for resource creation (agent activation). Neither is required for resource import. If using `ip_address`, Terraform must be able to make an HTTP (port 80) GET request to the specified IP address from where it is running. The agent will turn off that HTTP server after activation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L46">constructor</a>
</h3>

```typescript
new Agent(name: string, args?: AgentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Agent resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AgentState): Agent
```


Get an existing Agent resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L30">property activationKey</a>
</h3>

```typescript
public activationKey: pulumi.Output<string>;
```


DataSync Agent activation key during resource creation. Conflicts with `ip_address`. If an `ip_address` is provided instead, Terraform will retrieve the `activation_key` as part of the resource creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L34">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the DataSync Agent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L38">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string>;
```


DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. DataSync Agent must be accessible on port 80 from where Terraform is running.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name of the DataSync Agent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L46">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


Key-value pairs of resource tags to assign to the DataSync Agent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="EfsLocation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L14">class EfsLocation</a>
</h2>

Manages an AWS DataSync EFS Location.

~> **NOTE:** The EFS File System must have a mounted EFS Mount Target before creating this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L47">constructor</a>
</h3>

```typescript
new EfsLocation(name: string, args: EfsLocationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EfsLocation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EfsLocationState): EfsLocation
```


Get an existing EfsLocation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L30">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L34">property ec2Config</a>
</h3>

```typescript
public ec2Config: pulumi.Output<{ ... }>;
```


Configuration block containing EC2 configurations for connecting to the EFS File System.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L38">property efsFileSystemArn</a>
</h3>

```typescript
public efsFileSystemArn: pulumi.Output<ARN>;
```


Amazon Resource Name (ARN) of EFS File System.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L42">property subdirectory</a>
</h3>

```typescript
public subdirectory: pulumi.Output<string | undefined>;
```


Subdirectory to perform actions as source or destination. Default `/`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L46">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


Key-value pairs of resource tags to assign to the DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L47">property uri</a>
</h3>

```typescript
public uri: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="NfsLocation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L14">class NfsLocation</a>
</h2>

Manages an NFS Location within AWS DataSync.

~> **NOTE:** The DataSync Agents must be available before creating this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L47">constructor</a>
</h3>

```typescript
new NfsLocation(name: string, args: NfsLocationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NfsLocation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NfsLocationState): NfsLocation
```


Get an existing NfsLocation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L30">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L34">property onPremConfig</a>
</h3>

```typescript
public onPremConfig: pulumi.Output<{ ... }>;
```


Configuration block containing information for connecting to the NFS File System.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L38">property serverHostname</a>
</h3>

```typescript
public serverHostname: pulumi.Output<string>;
```


Specifies the IP address or DNS name of the NFS server. The DataSync Agent(s) use this to mount the NFS server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L42">property subdirectory</a>
</h3>

```typescript
public subdirectory: pulumi.Output<string>;
```


Subdirectory to perform actions as source or destination. Should be exported by the NFS server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L46">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


Key-value pairs of resource tags to assign to the DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L47">property uri</a>
</h3>

```typescript
public uri: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="S3Location">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L12">class S3Location</a>
</h2>

Manages an S3 Location within AWS DataSync.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L45">constructor</a>
</h3>

```typescript
new S3Location(name: string, args: S3LocationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a S3Location resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: S3LocationState): S3Location
```


Get an existing S3Location resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L32">property s3BucketArn</a>
</h3>

```typescript
public s3BucketArn: pulumi.Output<ARN>;
```


Amazon Resource Name (ARN) of the S3 Bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L36">property s3Config</a>
</h3>

```typescript
public s3Config: pulumi.Output<{ ... }>;
```


Configuration block containing information for connecting to S3.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L40">property subdirectory</a>
</h3>

```typescript
public subdirectory: pulumi.Output<string>;
```


Prefix to perform actions as source or destination.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L44">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


Key-value pairs of resource tags to assign to the DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L45">property uri</a>
</h3>

```typescript
public uri: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Task">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L12">class Task</a>
</h2>

Manages an AWS DataSync Task, which represents a configuration for synchronization. Starting an execution of these DataSync Tasks (actually synchronizing files) is performed outside of this Terraform resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L52">constructor</a>
</h3>

```typescript
new Task(name: string, args: TaskArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Task resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TaskState): Task
```


Get an existing Task resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the DataSync Task.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L32">property cloudwatchLogGroupArn</a>
</h3>

```typescript
public cloudwatchLogGroupArn: pulumi.Output<ARN | undefined>;
```


Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L36">property destinationLocationArn</a>
</h3>

```typescript
public destinationLocationArn: pulumi.Output<ARN>;
```


Amazon Resource Name (ARN) of destination DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L40">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name of the DataSync Task.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L44">property options</a>
</h3>

```typescript
public options: pulumi.Output<{ ... } | undefined>;
```


Configuration block containing option that controls the default behavior when you start an execution of this DataSync Task. For each individual task execution, you can override these options by specifying an overriding configuration in those executions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L48">property sourceLocationArn</a>
</h3>

```typescript
public sourceLocationArn: pulumi.Output<ARN>;
```


Amazon Resource Name (ARN) of source DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L52">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


Key-value pairs of resource tags to assign to the DataSync Task.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AgentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L106">interface AgentArgs</a>
</h2>

The set of arguments for constructing a Agent resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L110">property activationKey</a>
</h3>

```typescript
activationKey?: pulumi.Input<string>;
```


DataSync Agent activation key during resource creation. Conflicts with `ip_address`. If an `ip_address` is provided instead, Terraform will retrieve the `activation_key` as part of the resource creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L114">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. DataSync Agent must be accessible on port 80 from where Terraform is running.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L118">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the DataSync Agent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L122">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Key-value pairs of resource tags to assign to the DataSync Agent.

<h2 class="pdoc-module-header" id="AgentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L80">interface AgentState</a>
</h2>

Input properties used for looking up and filtering Agent resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L84">property activationKey</a>
</h3>

```typescript
activationKey?: pulumi.Input<string>;
```


DataSync Agent activation key during resource creation. Conflicts with `ip_address`. If an `ip_address` is provided instead, Terraform will retrieve the `activation_key` as part of the resource creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L88">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the DataSync Agent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L92">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. DataSync Agent must be accessible on port 80 from where Terraform is running.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the DataSync Agent.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/agent.ts#L100">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Key-value pairs of resource tags to assign to the DataSync Agent.

<h2 class="pdoc-module-header" id="EfsLocationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L116">interface EfsLocationArgs</a>
</h2>

The set of arguments for constructing a EfsLocation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L120">property ec2Config</a>
</h3>

```typescript
ec2Config: pulumi.Input<{ ... }>;
```


Configuration block containing EC2 configurations for connecting to the EFS File System.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L124">property efsFileSystemArn</a>
</h3>

```typescript
efsFileSystemArn: pulumi.Input<ARN>;
```


Amazon Resource Name (ARN) of EFS File System.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L128">property subdirectory</a>
</h3>

```typescript
subdirectory?: pulumi.Input<string>;
```


Subdirectory to perform actions as source or destination. Default `/`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L132">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Key-value pairs of resource tags to assign to the DataSync Location.

<h2 class="pdoc-module-header" id="EfsLocationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L89">interface EfsLocationState</a>
</h2>

Input properties used for looking up and filtering EfsLocation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L93">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L97">property ec2Config</a>
</h3>

```typescript
ec2Config?: pulumi.Input<{ ... }>;
```


Configuration block containing EC2 configurations for connecting to the EFS File System.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L101">property efsFileSystemArn</a>
</h3>

```typescript
efsFileSystemArn?: pulumi.Input<ARN>;
```


Amazon Resource Name (ARN) of EFS File System.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L105">property subdirectory</a>
</h3>

```typescript
subdirectory?: pulumi.Input<string>;
```


Subdirectory to perform actions as source or destination. Default `/`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L109">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Key-value pairs of resource tags to assign to the DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/efsLocation.ts#L110">property uri</a>
</h3>

```typescript
uri?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="NfsLocationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L119">interface NfsLocationArgs</a>
</h2>

The set of arguments for constructing a NfsLocation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L123">property onPremConfig</a>
</h3>

```typescript
onPremConfig: pulumi.Input<{ ... }>;
```


Configuration block containing information for connecting to the NFS File System.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L127">property serverHostname</a>
</h3>

```typescript
serverHostname: pulumi.Input<string>;
```


Specifies the IP address or DNS name of the NFS server. The DataSync Agent(s) use this to mount the NFS server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L131">property subdirectory</a>
</h3>

```typescript
subdirectory: pulumi.Input<string>;
```


Subdirectory to perform actions as source or destination. Should be exported by the NFS server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L135">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Key-value pairs of resource tags to assign to the DataSync Location.

<h2 class="pdoc-module-header" id="NfsLocationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L92">interface NfsLocationState</a>
</h2>

Input properties used for looking up and filtering NfsLocation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L96">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L100">property onPremConfig</a>
</h3>

```typescript
onPremConfig?: pulumi.Input<{ ... }>;
```


Configuration block containing information for connecting to the NFS File System.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L104">property serverHostname</a>
</h3>

```typescript
serverHostname?: pulumi.Input<string>;
```


Specifies the IP address or DNS name of the NFS server. The DataSync Agent(s) use this to mount the NFS server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L108">property subdirectory</a>
</h3>

```typescript
subdirectory?: pulumi.Input<string>;
```


Subdirectory to perform actions as source or destination. Should be exported by the NFS server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L112">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Key-value pairs of resource tags to assign to the DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/nfsLocation.ts#L113">property uri</a>
</h3>

```typescript
uri?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="S3LocationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L117">interface S3LocationArgs</a>
</h2>

The set of arguments for constructing a S3Location resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L121">property s3BucketArn</a>
</h3>

```typescript
s3BucketArn: pulumi.Input<ARN>;
```


Amazon Resource Name (ARN) of the S3 Bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L125">property s3Config</a>
</h3>

```typescript
s3Config: pulumi.Input<{ ... }>;
```


Configuration block containing information for connecting to S3.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L129">property subdirectory</a>
</h3>

```typescript
subdirectory: pulumi.Input<string>;
```


Prefix to perform actions as source or destination.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L133">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Key-value pairs of resource tags to assign to the DataSync Location.

<h2 class="pdoc-module-header" id="S3LocationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L90">interface S3LocationState</a>
</h2>

Input properties used for looking up and filtering S3Location resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L94">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L98">property s3BucketArn</a>
</h3>

```typescript
s3BucketArn?: pulumi.Input<ARN>;
```


Amazon Resource Name (ARN) of the S3 Bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L102">property s3Config</a>
</h3>

```typescript
s3Config?: pulumi.Input<{ ... }>;
```


Configuration block containing information for connecting to S3.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L106">property subdirectory</a>
</h3>

```typescript
subdirectory?: pulumi.Input<string>;
```


Prefix to perform actions as source or destination.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L110">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Key-value pairs of resource tags to assign to the DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/s3Location.ts#L111">property uri</a>
</h3>

```typescript
uri?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="TaskArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L130">interface TaskArgs</a>
</h2>

The set of arguments for constructing a Task resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L134">property cloudwatchLogGroupArn</a>
</h3>

```typescript
cloudwatchLogGroupArn?: pulumi.Input<ARN>;
```


Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L138">property destinationLocationArn</a>
</h3>

```typescript
destinationLocationArn: pulumi.Input<ARN>;
```


Amazon Resource Name (ARN) of destination DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L142">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the DataSync Task.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L146">property options</a>
</h3>

```typescript
options?: pulumi.Input<{ ... }>;
```


Configuration block containing option that controls the default behavior when you start an execution of this DataSync Task. For each individual task execution, you can override these options by specifying an overriding configuration in those executions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L150">property sourceLocationArn</a>
</h3>

```typescript
sourceLocationArn: pulumi.Input<ARN>;
```


Amazon Resource Name (ARN) of source DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L154">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Key-value pairs of resource tags to assign to the DataSync Task.

<h2 class="pdoc-module-header" id="TaskState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L96">interface TaskState</a>
</h2>

Input properties used for looking up and filtering Task resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L100">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the DataSync Task.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L104">property cloudwatchLogGroupArn</a>
</h3>

```typescript
cloudwatchLogGroupArn?: pulumi.Input<ARN>;
```


Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L108">property destinationLocationArn</a>
</h3>

```typescript
destinationLocationArn?: pulumi.Input<ARN>;
```


Amazon Resource Name (ARN) of destination DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L112">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the DataSync Task.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L116">property options</a>
</h3>

```typescript
options?: pulumi.Input<{ ... }>;
```


Configuration block containing option that controls the default behavior when you start an execution of this DataSync Task. For each individual task execution, you can override these options by specifying an overriding configuration in those executions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L120">property sourceLocationArn</a>
</h3>

```typescript
sourceLocationArn?: pulumi.Input<ARN>;
```


Amazon Resource Name (ARN) of source DataSync Location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/datasync/task.ts#L124">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


Key-value pairs of resource tags to assign to the DataSync Task.

