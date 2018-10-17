---
title: Module ssm
---

<a href="../index.html">@pulumi/aws</a> &gt; ssm

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Activation">class Activation</a>
* <a href="#Association">class Association</a>
* <a href="#Document">class Document</a>
* <a href="#MaintenanceWindow">class MaintenanceWindow</a>
* <a href="#MaintenanceWindowTarget">class MaintenanceWindowTarget</a>
* <a href="#MaintenanceWindowTask">class MaintenanceWindowTask</a>
* <a href="#Parameter">class Parameter</a>
* <a href="#PatchBaseline">class PatchBaseline</a>
* <a href="#PatchGroup">class PatchGroup</a>
* <a href="#ResourceDataSync">class ResourceDataSync</a>
* <a href="#getParameter">function getParameter</a>
* <a href="#ActivationArgs">interface ActivationArgs</a>
* <a href="#ActivationState">interface ActivationState</a>
* <a href="#AssociationArgs">interface AssociationArgs</a>
* <a href="#AssociationState">interface AssociationState</a>
* <a href="#DocumentArgs">interface DocumentArgs</a>
* <a href="#DocumentState">interface DocumentState</a>
* <a href="#GetParameterArgs">interface GetParameterArgs</a>
* <a href="#GetParameterResult">interface GetParameterResult</a>
* <a href="#MaintenanceWindowArgs">interface MaintenanceWindowArgs</a>
* <a href="#MaintenanceWindowState">interface MaintenanceWindowState</a>
* <a href="#MaintenanceWindowTargetArgs">interface MaintenanceWindowTargetArgs</a>
* <a href="#MaintenanceWindowTargetState">interface MaintenanceWindowTargetState</a>
* <a href="#MaintenanceWindowTaskArgs">interface MaintenanceWindowTaskArgs</a>
* <a href="#MaintenanceWindowTaskState">interface MaintenanceWindowTaskState</a>
* <a href="#ParameterArgs">interface ParameterArgs</a>
* <a href="#ParameterState">interface ParameterState</a>
* <a href="#PatchBaselineArgs">interface PatchBaselineArgs</a>
* <a href="#PatchBaselineState">interface PatchBaselineState</a>
* <a href="#PatchGroupArgs">interface PatchGroupArgs</a>
* <a href="#PatchGroupState">interface PatchGroupState</a>
* <a href="#ResourceDataSyncArgs">interface ResourceDataSyncArgs</a>
* <a href="#ResourceDataSyncState">interface ResourceDataSyncState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts">ssm/activation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts">ssm/association.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts">ssm/document.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/getParameter.ts">ssm/getParameter.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts">ssm/maintenanceWindow.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts">ssm/maintenanceWindowTarget.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts">ssm/maintenanceWindowTask.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts">ssm/parameter.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts">ssm/patchBaseline.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchGroup.ts">ssm/patchGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/resourceDataSync.ts">ssm/resourceDataSync.ts</a> 


<h2 class="pdoc-module-header" id="Activation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L10">class Activation</a>
</h2>

Registers an on-premises server or virtual machine with Amazon EC2 so that it can be managed using Run Command.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L54">constructor</a>
</h3>

```typescript
new Activation(name: string, args: ActivationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Activation resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ActivationState): Activation
```


Get an existing Activation resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L26">property activationCode</a>
</h3>

```typescript
public activationCode: pulumi.Output<string>;
```


The code the system generates when it processes the activation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L30">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the resource that you want to register.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L34">property expirationDate</a>
</h3>

```typescript
public expirationDate: pulumi.Output<string | undefined>;
```


A timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) by which this activation request should expire. The default value is 24 hours from resource creation time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L38">property expired</a>
</h3>

```typescript
public expired: pulumi.Output<string>;
```


If the current activation has expired.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L42">property iamRole</a>
</h3>

```typescript
public iamRole: pulumi.Output<string>;
```


The IAM Role to attach to the managed instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L46">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The default name of the registered managed instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L50">property registrationCount</a>
</h3>

```typescript
public registrationCount: pulumi.Output<number>;
```


The number of managed instances that are currently registered using this activation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L54">property registrationLimit</a>
</h3>

```typescript
public registrationLimit: pulumi.Output<number | undefined>;
```


The maximum number of managed instances you want to register. The default value is 1 instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Association">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L10">class Association</a>
</h2>

Associates an SSM Document to an instance or EC2 tag.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L55">constructor</a>
</h3>

```typescript
new Association(name: string, args?: AssociationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Association resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AssociationState): Association
```


Get an existing Association resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L23">property associationId</a>
</h3>

```typescript
public associationId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L27">property associationName</a>
</h3>

```typescript
public associationName: pulumi.Output<string | undefined>;
```


The descriptive name for the association.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L31">property documentVersion</a>
</h3>

```typescript
public documentVersion: pulumi.Output<string>;
```


The document version you want to associate with the target(s). Can be a specific version or the default version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L35">property instanceId</a>
</h3>

```typescript
public instanceId: pulumi.Output<string | undefined>;
```


The instance ID to apply an SSM document to. Use `targets` with key `InstanceIds` for document schema versions 2.0 and above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L39">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the SSM document to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L43">property outputLocation</a>
</h3>

```typescript
public outputLocation: pulumi.Output<{ ... } | undefined>;
```


An output location block. Output Location is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L47">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... }>;
```


A block of arbitrary string parameters to pass to the SSM document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L51">property scheduleExpression</a>
</h3>

```typescript
public scheduleExpression: pulumi.Output<string | undefined>;
```


A cron expression when the association will be applied to the target(s).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L55">property targets</a>
</h3>

```typescript
public targets: pulumi.Output<{ ... }[]>;
```


A block containing the targets of the SSM association. Targets are documented below. AWS currently supports a maximum of 5 targets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Document">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L16">class Document</a>
</h2>

Provides an SSM Document resource

~> **NOTE on updating SSM documents:** Only documents with a schema version of 2.0
or greater can update their content once created, see [SSM Schema Features][1]. To update a document with an older
schema version you must recreate the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L97">constructor</a>
</h3>

```typescript
new Document(name: string, args: DocumentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Document resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DocumentState): Document
```


Get an existing Document resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L29">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L33">property content</a>
</h3>

```typescript
public content: pulumi.Output<string>;
```


The JSON or YAML content of the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L37">property createdDate</a>
</h3>

```typescript
public createdDate: pulumi.Output<string>;
```


The date the document was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L41">property defaultVersion</a>
</h3>

```typescript
public defaultVersion: pulumi.Output<string>;
```


The default version of the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L45">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


The description of the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L49">property documentFormat</a>
</h3>

```typescript
public documentFormat: pulumi.Output<string | undefined>;
```


The format of the document. Valid document types include: `JSON` and `YAML`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L53">property documentType</a>
</h3>

```typescript
public documentType: pulumi.Output<string>;
```


The type of the document. Valid document types include: `Command`, `Policy`, `Automation` and `Session`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L57">property hash</a>
</h3>

```typescript
public hash: pulumi.Output<string>;
```


The sha1 or sha256 of the document content

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L61">property hashType</a>
</h3>

```typescript
public hashType: pulumi.Output<string>;
```


"Sha1" "Sha256". The hashing algorithm used when hashing the content.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L65">property latestVersion</a>
</h3>

```typescript
public latestVersion: pulumi.Output<string>;
```


The latest version of the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L69">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L73">property owner</a>
</h3>

```typescript
public owner: pulumi.Output<string>;
```


The AWS user account of the person who created the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L77">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... }[]>;
```


The parameters that are available to this document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L81">property permissions</a>
</h3>

```typescript
public permissions: pulumi.Output<{ ... } | undefined>;
```


Additional Permissions to attach to the document. See Permissions below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L85">property platformTypes</a>
</h3>

```typescript
public platformTypes: pulumi.Output<string[]>;
```


A list of OS platforms compatible with this SSM document, either "Windows" or "Linux".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L89">property schemaVersion</a>
</h3>

```typescript
public schemaVersion: pulumi.Output<string>;
```


The schema version of the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L93">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```


"Creating", "Active" or "Deleting". The current status of the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L97">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="MaintenanceWindow">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L10">class MaintenanceWindow</a>
</h2>

Provides an SSM Maintenance Window resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L43">constructor</a>
</h3>

```typescript
new MaintenanceWindow(name: string, args: MaintenanceWindowArgs, opts?: pulumi.CustomResourceOptions)
```


Create a MaintenanceWindow resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MaintenanceWindowState): MaintenanceWindow
```


Get an existing MaintenanceWindow resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L26">property allowUnassociatedTargets</a>
</h3>

```typescript
public allowUnassociatedTargets: pulumi.Output<boolean | undefined>;
```


Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L30">property cutoff</a>
</h3>

```typescript
public cutoff: pulumi.Output<number>;
```


The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L34">property duration</a>
</h3>

```typescript
public duration: pulumi.Output<number>;
```


The duration of the Maintenance Window in hours.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L35">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L39">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the maintenance window.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L43">property schedule</a>
</h3>

```typescript
public schedule: pulumi.Output<string>;
```


The schedule of the Maintenance Window in the form of a [cron](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-cron.html) or rate expression.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="MaintenanceWindowTarget">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts#L10">class MaintenanceWindowTarget</a>
</h2>

Provides an SSM Maintenance Window Target resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts#L38">constructor</a>
</h3>

```typescript
new MaintenanceWindowTarget(name: string, args: MaintenanceWindowTargetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a MaintenanceWindowTarget resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MaintenanceWindowTargetState): MaintenanceWindowTarget
```


Get an existing MaintenanceWindowTarget resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts#L26">property ownerInformation</a>
</h3>

```typescript
public ownerInformation: pulumi.Output<string | undefined>;
```


User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts#L30">property resourceType</a>
</h3>

```typescript
public resourceType: pulumi.Output<string>;
```


The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts#L34">property targets</a>
</h3>

```typescript
public targets: pulumi.Output<{ ... }[]>;
```


The targets (either instances or tags). Instances are specified using Key=instanceids,Values=instanceid1,instanceid2. Tags are specified using Key=tag name,Values=tag value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts#L38">property windowId</a>
</h3>

```typescript
public windowId: pulumi.Output<string>;
```


The Id of the maintenance window to register the target with.

<h2 class="pdoc-module-header" id="MaintenanceWindowTask">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L10">class MaintenanceWindowTask</a>
</h2>

Provides an SSM Maintenance Window Task resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L62">constructor</a>
</h3>

```typescript
new MaintenanceWindowTask(name: string, args: MaintenanceWindowTaskArgs, opts?: pulumi.CustomResourceOptions)
```


Create a MaintenanceWindowTask resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MaintenanceWindowTaskState): MaintenanceWindowTask
```


Get an existing MaintenanceWindowTask resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L26">property loggingInfo</a>
</h3>

```typescript
public loggingInfo: pulumi.Output<{ ... } | undefined>;
```


A structure containing information about an Amazon S3 bucket to write instance-level logs to. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L30">property maxConcurrency</a>
</h3>

```typescript
public maxConcurrency: pulumi.Output<string>;
```


The maximum number of targets this task can be run for in parallel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L34">property maxErrors</a>
</h3>

```typescript
public maxErrors: pulumi.Output<string>;
```


The maximum number of errors allowed before this task stops being scheduled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L38">property priority</a>
</h3>

```typescript
public priority: pulumi.Output<number | undefined>;
```


The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L42">property serviceRoleArn</a>
</h3>

```typescript
public serviceRoleArn: pulumi.Output<string>;
```


The role that should be assumed when executing the task.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L46">property targets</a>
</h3>

```typescript
public targets: pulumi.Output<{ ... }[]>;
```


The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L50">property taskArn</a>
</h3>

```typescript
public taskArn: pulumi.Output<string>;
```


The ARN of the task to execute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L54">property taskParameters</a>
</h3>

```typescript
public taskParameters: pulumi.Output<{ ... }[] | undefined>;
```


A structure containing information about parameters required by the particular `task_arn`. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L58">property taskType</a>
</h3>

```typescript
public taskType: pulumi.Output<string>;
```


The type of task being registered. The only allowed value is `RUN_COMMAND`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L62">property windowId</a>
</h3>

```typescript
public windowId: pulumi.Output<string>;
```


The Id of the maintenance window to register the task with.

<h2 class="pdoc-module-header" id="Parameter">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L12">class Parameter</a>
</h2>

Provides an SSM Parameter resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L60">constructor</a>
</h3>

```typescript
new Parameter(name: string, args: ParameterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Parameter resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ParameterState): Parameter
```


Get an existing Parameter resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L28">property allowedPattern</a>
</h3>

```typescript
public allowedPattern: pulumi.Output<string | undefined>;
```


A regular expression used to validate the parameter value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L32">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L36">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L40">property keyId</a>
</h3>

```typescript
public keyId: pulumi.Output<string>;
```


The KMS key id or arn for encrypting a SecureString.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L48">property overwrite</a>
</h3>

```typescript
public overwrite: pulumi.Output<boolean | undefined>;
```


Overwrite an existing parameter. If not specified, will default to `false` if the resource has not been created by terraform to avoid overwrite of existing resource and will default to `true` otherwise (terraform lifecycle rules should then be used to manage the update behavior).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L52">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L56">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of the parameter. Valid types are `String`, `StringList` and `SecureString`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L60">property value</a>
</h3>

```typescript
public value: pulumi.Output<string>;
```


The value of the parameter.

<h2 class="pdoc-module-header" id="PatchBaseline">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L14">class PatchBaseline</a>
</h2>

Provides an SSM Patch Baseline resource

~> **NOTE on Patch Baselines:** The `approved_patches` and `approval_rule` are
both marked as optional fields, but the Patch Baseline requires that at least one
of them is specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L58">constructor</a>
</h3>

```typescript
new PatchBaseline(name: string, args?: PatchBaselineArgs, opts?: pulumi.CustomResourceOptions)
```


Create a PatchBaseline resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PatchBaselineState): PatchBaseline
```


Get an existing PatchBaseline resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L30">property approvalRules</a>
</h3>

```typescript
public approvalRules: pulumi.Output<{ ... }[] | undefined>;
```


A set of rules used to include patches in the baseline. up to 10 approval rules can be specified. Each approval_rule block requires the fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L34">property approvedPatches</a>
</h3>

```typescript
public approvedPatches: pulumi.Output<string[] | undefined>;
```


A list of explicitly approved patches for the baseline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L38">property approvedPatchesComplianceLevel</a>
</h3>

```typescript
public approvedPatchesComplianceLevel: pulumi.Output<string | undefined>;
```


Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. Valid compliance levels include the following: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFORMATIONAL`, `UNSPECIFIED`. The default value is `UNSPECIFIED`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L42">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the patch baseline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L46">property globalFilters</a>
</h3>

```typescript
public globalFilters: pulumi.Output<{ ... }[] | undefined>;
```


A set of global filters used to exclude patches from the baseline. Up to 4 global filters can be specified using Key/Value pairs. Valid Keys are `PRODUCT | CLASSIFICATION | MSRC_SEVERITY | PATCH_ID`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L50">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the patch baseline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L54">property operatingSystem</a>
</h3>

```typescript
public operatingSystem: pulumi.Output<string | undefined>;
```


Defines the operating system the patch baseline applies to. Supported operating systems include `WINDOWS`, `AMAZON_LINUX`, `AMAZON_LINUX_2`, `SUSE`, `UBUNTU`, `CENTOS`, and `REDHAT_ENTERPRISE_LINUX`. The Default value is `WINDOWS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L58">property rejectedPatches</a>
</h3>

```typescript
public rejectedPatches: pulumi.Output<string[] | undefined>;
```


A list of rejected patches.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="PatchGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchGroup.ts#L10">class PatchGroup</a>
</h2>

Provides an SSM Patch Group resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchGroup.ts#L30">constructor</a>
</h3>

```typescript
new PatchGroup(name: string, args: PatchGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a PatchGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchGroup.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PatchGroupState): PatchGroup
```


Get an existing PatchGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchGroup.ts#L26">property baselineId</a>
</h3>

```typescript
public baselineId: pulumi.Output<string>;
```


The ID of the patch baseline to register the patch group with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchGroup.ts#L30">property patchGroup</a>
</h3>

```typescript
public patchGroup: pulumi.Output<string>;
```


The name of the patch group that should be registered with the patch baseline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ResourceDataSync">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/resourceDataSync.ts#L10">class ResourceDataSync</a>
</h2>

Provides a SSM resource data sync.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/resourceDataSync.ts#L30">constructor</a>
</h3>

```typescript
new ResourceDataSync(name: string, args: ResourceDataSyncArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ResourceDataSync resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/resourceDataSync.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ResourceDataSyncState): ResourceDataSync
```


Get an existing ResourceDataSync resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/resourceDataSync.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name for the configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/resourceDataSync.ts#L30">property s3Destination</a>
</h3>

```typescript
public s3Destination: pulumi.Output<{ ... }>;
```


Amazon S3 configuration details for the sync.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getParameter">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/getParameter.ts#L10">function getParameter</a>
</h2>

```typescript
getParameter(args: GetParameterArgs, opts?: pulumi.InvokeOptions): Promise<GetParameterResult>
```


Provides an SSM Parameter data source.

<h2 class="pdoc-module-header" id="ActivationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L135">interface ActivationArgs</a>
</h2>

The set of arguments for constructing a Activation resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L139">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the resource that you want to register.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L143">property expirationDate</a>
</h3>

```typescript
expirationDate?: pulumi.Input<string>;
```


A timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) by which this activation request should expire. The default value is 24 hours from resource creation time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L147">property iamRole</a>
</h3>

```typescript
iamRole: pulumi.Input<string>;
```


The IAM Role to attach to the managed instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L151">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The default name of the registered managed instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L155">property registrationLimit</a>
</h3>

```typescript
registrationLimit?: pulumi.Input<number>;
```


The maximum number of managed instances you want to register. The default value is 1 instance.

<h2 class="pdoc-module-header" id="ActivationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L97">interface ActivationState</a>
</h2>

Input properties used for looking up and filtering Activation resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L101">property activationCode</a>
</h3>

```typescript
activationCode?: pulumi.Input<string>;
```


The code the system generates when it processes the activation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L105">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the resource that you want to register.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L109">property expirationDate</a>
</h3>

```typescript
expirationDate?: pulumi.Input<string>;
```


A timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) by which this activation request should expire. The default value is 24 hours from resource creation time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L113">property expired</a>
</h3>

```typescript
expired?: pulumi.Input<string>;
```


If the current activation has expired.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L117">property iamRole</a>
</h3>

```typescript
iamRole?: pulumi.Input<string>;
```


The IAM Role to attach to the managed instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L121">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The default name of the registered managed instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L125">property registrationCount</a>
</h3>

```typescript
registrationCount?: pulumi.Input<number>;
```


The number of managed instances that are currently registered using this activation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/activation.ts#L129">property registrationLimit</a>
</h3>

```typescript
registrationLimit?: pulumi.Input<number>;
```


The maximum number of managed instances you want to register. The default value is 1 instance.

<h2 class="pdoc-module-header" id="AssociationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L136">interface AssociationArgs</a>
</h2>

The set of arguments for constructing a Association resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L140">property associationName</a>
</h3>

```typescript
associationName?: pulumi.Input<string>;
```


The descriptive name for the association.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L144">property documentVersion</a>
</h3>

```typescript
documentVersion?: pulumi.Input<string>;
```


The document version you want to associate with the target(s). Can be a specific version or the default version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L148">property instanceId</a>
</h3>

```typescript
instanceId?: pulumi.Input<string>;
```


The instance ID to apply an SSM document to. Use `targets` with key `InstanceIds` for document schema versions 2.0 and above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L152">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the SSM document to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L156">property outputLocation</a>
</h3>

```typescript
outputLocation?: pulumi.Input<{ ... }>;
```


An output location block. Output Location is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L160">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


A block of arbitrary string parameters to pass to the SSM document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L164">property scheduleExpression</a>
</h3>

```typescript
scheduleExpression?: pulumi.Input<string>;
```


A cron expression when the association will be applied to the target(s).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L168">property targets</a>
</h3>

```typescript
targets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A block containing the targets of the SSM association. Targets are documented below. AWS currently supports a maximum of 5 targets.

<h2 class="pdoc-module-header" id="AssociationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L97">interface AssociationState</a>
</h2>

Input properties used for looking up and filtering Association resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L98">property associationId</a>
</h3>

```typescript
associationId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L102">property associationName</a>
</h3>

```typescript
associationName?: pulumi.Input<string>;
```


The descriptive name for the association.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L106">property documentVersion</a>
</h3>

```typescript
documentVersion?: pulumi.Input<string>;
```


The document version you want to associate with the target(s). Can be a specific version or the default version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L110">property instanceId</a>
</h3>

```typescript
instanceId?: pulumi.Input<string>;
```


The instance ID to apply an SSM document to. Use `targets` with key `InstanceIds` for document schema versions 2.0 and above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L114">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the SSM document to apply.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L118">property outputLocation</a>
</h3>

```typescript
outputLocation?: pulumi.Input<{ ... }>;
```


An output location block. Output Location is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L122">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


A block of arbitrary string parameters to pass to the SSM document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L126">property scheduleExpression</a>
</h3>

```typescript
scheduleExpression?: pulumi.Input<string>;
```


A cron expression when the association will be applied to the target(s).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/association.ts#L130">property targets</a>
</h3>

```typescript
targets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A block containing the targets of the SSM association. Targets are documented below. AWS currently supports a maximum of 5 targets.

<h2 class="pdoc-module-header" id="DocumentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L238">interface DocumentArgs</a>
</h2>

The set of arguments for constructing a Document resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L242">property content</a>
</h3>

```typescript
content: pulumi.Input<string>;
```


The JSON or YAML content of the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L246">property documentFormat</a>
</h3>

```typescript
documentFormat?: pulumi.Input<string>;
```


The format of the document. Valid document types include: `JSON` and `YAML`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L250">property documentType</a>
</h3>

```typescript
documentType: pulumi.Input<string>;
```


The type of the document. Valid document types include: `Command`, `Policy`, `Automation` and `Session`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L254">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L258">property permissions</a>
</h3>

```typescript
permissions?: pulumi.Input<{ ... }>;
```


Additional Permissions to attach to the document. See Permissions below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L262">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the object.

<h2 class="pdoc-module-header" id="DocumentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L163">interface DocumentState</a>
</h2>

Input properties used for looking up and filtering Document resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L164">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L168">property content</a>
</h3>

```typescript
content?: pulumi.Input<string>;
```


The JSON or YAML content of the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L172">property createdDate</a>
</h3>

```typescript
createdDate?: pulumi.Input<string>;
```


The date the document was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L176">property defaultVersion</a>
</h3>

```typescript
defaultVersion?: pulumi.Input<string>;
```


The default version of the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L180">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L184">property documentFormat</a>
</h3>

```typescript
documentFormat?: pulumi.Input<string>;
```


The format of the document. Valid document types include: `JSON` and `YAML`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L188">property documentType</a>
</h3>

```typescript
documentType?: pulumi.Input<string>;
```


The type of the document. Valid document types include: `Command`, `Policy`, `Automation` and `Session`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L192">property hash</a>
</h3>

```typescript
hash?: pulumi.Input<string>;
```


The sha1 or sha256 of the document content

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L196">property hashType</a>
</h3>

```typescript
hashType?: pulumi.Input<string>;
```


"Sha1" "Sha256". The hashing algorithm used when hashing the content.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L200">property latestVersion</a>
</h3>

```typescript
latestVersion?: pulumi.Input<string>;
```


The latest version of the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L204">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L208">property owner</a>
</h3>

```typescript
owner?: pulumi.Input<string>;
```


The AWS user account of the person who created the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L212">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The parameters that are available to this document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L216">property permissions</a>
</h3>

```typescript
permissions?: pulumi.Input<{ ... }>;
```


Additional Permissions to attach to the document. See Permissions below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L220">property platformTypes</a>
</h3>

```typescript
platformTypes?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of OS platforms compatible with this SSM document, either "Windows" or "Linux".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L224">property schemaVersion</a>
</h3>

```typescript
schemaVersion?: pulumi.Input<string>;
```


The schema version of the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L228">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


"Creating", "Active" or "Deleting". The current status of the document.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/document.ts#L232">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the object.

<h2 class="pdoc-module-header" id="GetParameterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/getParameter.ts#L20">interface GetParameterArgs</a>
</h2>

A collection of arguments for invoking getParameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/getParameter.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


The name of the parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/getParameter.ts#L28">property withDecryption</a>
</h3>

```typescript
withDecryption?: boolean;
```


Whether to return decrypted `SecureString` value. Defaults to `true`.

<h2 class="pdoc-module-header" id="GetParameterResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/getParameter.ts#L34">interface GetParameterResult</a>
</h2>

A collection of values returned by getParameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/getParameter.ts#L35">property arn</a>
</h3>

```typescript
arn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/getParameter.ts#L41">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/getParameter.ts#L36">property type</a>
</h3>

```typescript
type: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/getParameter.ts#L37">property value</a>
</h3>

```typescript
value: string;
```

<h2 class="pdoc-module-header" id="MaintenanceWindowArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L115">interface MaintenanceWindowArgs</a>
</h2>

The set of arguments for constructing a MaintenanceWindow resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L119">property allowUnassociatedTargets</a>
</h3>

```typescript
allowUnassociatedTargets?: pulumi.Input<boolean>;
```


Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L123">property cutoff</a>
</h3>

```typescript
cutoff: pulumi.Input<number>;
```


The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L127">property duration</a>
</h3>

```typescript
duration: pulumi.Input<number>;
```


The duration of the Maintenance Window in hours.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L128">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L132">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the maintenance window.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L136">property schedule</a>
</h3>

```typescript
schedule: pulumi.Input<string>;
```


The schedule of the Maintenance Window in the form of a [cron](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-cron.html) or rate expression.

<h2 class="pdoc-module-header" id="MaintenanceWindowState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L88">interface MaintenanceWindowState</a>
</h2>

Input properties used for looking up and filtering MaintenanceWindow resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L92">property allowUnassociatedTargets</a>
</h3>

```typescript
allowUnassociatedTargets?: pulumi.Input<boolean>;
```


Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L96">property cutoff</a>
</h3>

```typescript
cutoff?: pulumi.Input<number>;
```


The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L100">property duration</a>
</h3>

```typescript
duration?: pulumi.Input<number>;
```


The duration of the Maintenance Window in hours.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L101">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L105">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the maintenance window.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindow.ts#L109">property schedule</a>
</h3>

```typescript
schedule?: pulumi.Input<string>;
```


The schedule of the Maintenance Window in the form of a [cron](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-cron.html) or rate expression.

<h2 class="pdoc-module-header" id="MaintenanceWindowTargetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts#L101">interface MaintenanceWindowTargetArgs</a>
</h2>

The set of arguments for constructing a MaintenanceWindowTarget resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts#L105">property ownerInformation</a>
</h3>

```typescript
ownerInformation?: pulumi.Input<string>;
```


User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts#L109">property resourceType</a>
</h3>

```typescript
resourceType: pulumi.Input<string>;
```


The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts#L113">property targets</a>
</h3>

```typescript
targets: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The targets (either instances or tags). Instances are specified using Key=instanceids,Values=instanceid1,instanceid2. Tags are specified using Key=tag name,Values=tag value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts#L117">property windowId</a>
</h3>

```typescript
windowId: pulumi.Input<string>;
```


The Id of the maintenance window to register the target with.

<h2 class="pdoc-module-header" id="MaintenanceWindowTargetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts#L79">interface MaintenanceWindowTargetState</a>
</h2>

Input properties used for looking up and filtering MaintenanceWindowTarget resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts#L83">property ownerInformation</a>
</h3>

```typescript
ownerInformation?: pulumi.Input<string>;
```


User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts#L87">property resourceType</a>
</h3>

```typescript
resourceType?: pulumi.Input<string>;
```


The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts#L91">property targets</a>
</h3>

```typescript
targets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The targets (either instances or tags). Instances are specified using Key=instanceids,Values=instanceid1,instanceid2. Tags are specified using Key=tag name,Values=tag value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTarget.ts#L95">property windowId</a>
</h3>

```typescript
windowId?: pulumi.Input<string>;
```


The Id of the maintenance window to register the target with.

<h2 class="pdoc-module-header" id="MaintenanceWindowTaskArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L173">interface MaintenanceWindowTaskArgs</a>
</h2>

The set of arguments for constructing a MaintenanceWindowTask resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L177">property loggingInfo</a>
</h3>

```typescript
loggingInfo?: pulumi.Input<{ ... }>;
```


A structure containing information about an Amazon S3 bucket to write instance-level logs to. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L181">property maxConcurrency</a>
</h3>

```typescript
maxConcurrency: pulumi.Input<string>;
```


The maximum number of targets this task can be run for in parallel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L185">property maxErrors</a>
</h3>

```typescript
maxErrors: pulumi.Input<string>;
```


The maximum number of errors allowed before this task stops being scheduled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L189">property priority</a>
</h3>

```typescript
priority?: pulumi.Input<number>;
```


The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L193">property serviceRoleArn</a>
</h3>

```typescript
serviceRoleArn: pulumi.Input<string>;
```


The role that should be assumed when executing the task.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L197">property targets</a>
</h3>

```typescript
targets: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L201">property taskArn</a>
</h3>

```typescript
taskArn: pulumi.Input<string>;
```


The ARN of the task to execute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L205">property taskParameters</a>
</h3>

```typescript
taskParameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A structure containing information about parameters required by the particular `task_arn`. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L209">property taskType</a>
</h3>

```typescript
taskType: pulumi.Input<string>;
```


The type of task being registered. The only allowed value is `RUN_COMMAND`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L213">property windowId</a>
</h3>

```typescript
windowId: pulumi.Input<string>;
```


The Id of the maintenance window to register the task with.

<h2 class="pdoc-module-header" id="MaintenanceWindowTaskState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L127">interface MaintenanceWindowTaskState</a>
</h2>

Input properties used for looking up and filtering MaintenanceWindowTask resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L131">property loggingInfo</a>
</h3>

```typescript
loggingInfo?: pulumi.Input<{ ... }>;
```


A structure containing information about an Amazon S3 bucket to write instance-level logs to. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L135">property maxConcurrency</a>
</h3>

```typescript
maxConcurrency?: pulumi.Input<string>;
```


The maximum number of targets this task can be run for in parallel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L139">property maxErrors</a>
</h3>

```typescript
maxErrors?: pulumi.Input<string>;
```


The maximum number of errors allowed before this task stops being scheduled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L143">property priority</a>
</h3>

```typescript
priority?: pulumi.Input<number>;
```


The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L147">property serviceRoleArn</a>
</h3>

```typescript
serviceRoleArn?: pulumi.Input<string>;
```


The role that should be assumed when executing the task.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L151">property targets</a>
</h3>

```typescript
targets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L155">property taskArn</a>
</h3>

```typescript
taskArn?: pulumi.Input<string>;
```


The ARN of the task to execute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L159">property taskParameters</a>
</h3>

```typescript
taskParameters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A structure containing information about parameters required by the particular `task_arn`. Documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L163">property taskType</a>
</h3>

```typescript
taskType?: pulumi.Input<string>;
```


The type of task being registered. The only allowed value is `RUN_COMMAND`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/maintenanceWindowTask.ts#L167">property windowId</a>
</h3>

```typescript
windowId?: pulumi.Input<string>;
```


The Id of the maintenance window to register the task with.

<h2 class="pdoc-module-header" id="ParameterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L150">interface ParameterArgs</a>
</h2>

The set of arguments for constructing a Parameter resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L154">property allowedPattern</a>
</h3>

```typescript
allowedPattern?: pulumi.Input<string>;
```


A regular expression used to validate the parameter value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L158">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L162">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L166">property keyId</a>
</h3>

```typescript
keyId?: pulumi.Input<string>;
```


The KMS key id or arn for encrypting a SecureString.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L170">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L174">property overwrite</a>
</h3>

```typescript
overwrite?: pulumi.Input<boolean>;
```


Overwrite an existing parameter. If not specified, will default to `false` if the resource has not been created by terraform to avoid overwrite of existing resource and will default to `true` otherwise (terraform lifecycle rules should then be used to manage the update behavior).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L178">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L182">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of the parameter. Valid types are `String`, `StringList` and `SecureString`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L186">property value</a>
</h3>

```typescript
value: pulumi.Input<string>;
```


The value of the parameter.

<h2 class="pdoc-module-header" id="ParameterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L108">interface ParameterState</a>
</h2>

Input properties used for looking up and filtering Parameter resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L112">property allowedPattern</a>
</h3>

```typescript
allowedPattern?: pulumi.Input<string>;
```


A regular expression used to validate the parameter value.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L116">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L120">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L124">property keyId</a>
</h3>

```typescript
keyId?: pulumi.Input<string>;
```


The KMS key id or arn for encrypting a SecureString.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L128">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the parameter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L132">property overwrite</a>
</h3>

```typescript
overwrite?: pulumi.Input<boolean>;
```


Overwrite an existing parameter. If not specified, will default to `false` if the resource has not been created by terraform to avoid overwrite of existing resource and will default to `true` otherwise (terraform lifecycle rules should then be used to manage the update behavior).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L136">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L140">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the parameter. Valid types are `String`, `StringList` and `SecureString`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/parameter.ts#L144">property value</a>
</h3>

```typescript
value?: pulumi.Input<string>;
```


The value of the parameter.

<h2 class="pdoc-module-header" id="PatchBaselineArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L136">interface PatchBaselineArgs</a>
</h2>

The set of arguments for constructing a PatchBaseline resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L140">property approvalRules</a>
</h3>

```typescript
approvalRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A set of rules used to include patches in the baseline. up to 10 approval rules can be specified. Each approval_rule block requires the fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L144">property approvedPatches</a>
</h3>

```typescript
approvedPatches?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of explicitly approved patches for the baseline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L148">property approvedPatchesComplianceLevel</a>
</h3>

```typescript
approvedPatchesComplianceLevel?: pulumi.Input<string>;
```


Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. Valid compliance levels include the following: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFORMATIONAL`, `UNSPECIFIED`. The default value is `UNSPECIFIED`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L152">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the patch baseline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L156">property globalFilters</a>
</h3>

```typescript
globalFilters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A set of global filters used to exclude patches from the baseline. Up to 4 global filters can be specified using Key/Value pairs. Valid Keys are `PRODUCT | CLASSIFICATION | MSRC_SEVERITY | PATCH_ID`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L160">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the patch baseline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L164">property operatingSystem</a>
</h3>

```typescript
operatingSystem?: pulumi.Input<string>;
```


Defines the operating system the patch baseline applies to. Supported operating systems include `WINDOWS`, `AMAZON_LINUX`, `AMAZON_LINUX_2`, `SUSE`, `UBUNTU`, `CENTOS`, and `REDHAT_ENTERPRISE_LINUX`. The Default value is `WINDOWS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L168">property rejectedPatches</a>
</h3>

```typescript
rejectedPatches?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of rejected patches.

<h2 class="pdoc-module-header" id="PatchBaselineState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L98">interface PatchBaselineState</a>
</h2>

Input properties used for looking up and filtering PatchBaseline resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L102">property approvalRules</a>
</h3>

```typescript
approvalRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A set of rules used to include patches in the baseline. up to 10 approval rules can be specified. Each approval_rule block requires the fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L106">property approvedPatches</a>
</h3>

```typescript
approvedPatches?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of explicitly approved patches for the baseline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L110">property approvedPatchesComplianceLevel</a>
</h3>

```typescript
approvedPatchesComplianceLevel?: pulumi.Input<string>;
```


Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. Valid compliance levels include the following: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFORMATIONAL`, `UNSPECIFIED`. The default value is `UNSPECIFIED`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L114">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the patch baseline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L118">property globalFilters</a>
</h3>

```typescript
globalFilters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A set of global filters used to exclude patches from the baseline. Up to 4 global filters can be specified using Key/Value pairs. Valid Keys are `PRODUCT | CLASSIFICATION | MSRC_SEVERITY | PATCH_ID`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L122">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the patch baseline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L126">property operatingSystem</a>
</h3>

```typescript
operatingSystem?: pulumi.Input<string>;
```


Defines the operating system the patch baseline applies to. Supported operating systems include `WINDOWS`, `AMAZON_LINUX`, `AMAZON_LINUX_2`, `SUSE`, `UBUNTU`, `CENTOS`, and `REDHAT_ENTERPRISE_LINUX`. The Default value is `WINDOWS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchBaseline.ts#L130">property rejectedPatches</a>
</h3>

```typescript
rejectedPatches?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of rejected patches.

<h2 class="pdoc-module-header" id="PatchGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchGroup.ts#L78">interface PatchGroupArgs</a>
</h2>

The set of arguments for constructing a PatchGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchGroup.ts#L82">property baselineId</a>
</h3>

```typescript
baselineId: pulumi.Input<string>;
```


The ID of the patch baseline to register the patch group with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchGroup.ts#L86">property patchGroup</a>
</h3>

```typescript
patchGroup: pulumi.Input<string>;
```


The name of the patch group that should be registered with the patch baseline.

<h2 class="pdoc-module-header" id="PatchGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchGroup.ts#L64">interface PatchGroupState</a>
</h2>

Input properties used for looking up and filtering PatchGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchGroup.ts#L68">property baselineId</a>
</h3>

```typescript
baselineId?: pulumi.Input<string>;
```


The ID of the patch baseline to register the patch group with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/patchGroup.ts#L72">property patchGroup</a>
</h3>

```typescript
patchGroup?: pulumi.Input<string>;
```


The name of the patch group that should be registered with the patch baseline.

<h2 class="pdoc-module-header" id="ResourceDataSyncArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/resourceDataSync.ts#L75">interface ResourceDataSyncArgs</a>
</h2>

The set of arguments for constructing a ResourceDataSync resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/resourceDataSync.ts#L79">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name for the configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/resourceDataSync.ts#L83">property s3Destination</a>
</h3>

```typescript
s3Destination: pulumi.Input<{ ... }>;
```


Amazon S3 configuration details for the sync.

<h2 class="pdoc-module-header" id="ResourceDataSyncState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/resourceDataSync.ts#L61">interface ResourceDataSyncState</a>
</h2>

Input properties used for looking up and filtering ResourceDataSync resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/resourceDataSync.ts#L65">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name for the configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ssm/resourceDataSync.ts#L69">property s3Destination</a>
</h3>

```typescript
s3Destination?: pulumi.Input<{ ... }>;
```


Amazon S3 configuration details for the sync.

