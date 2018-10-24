---
title: Module cloudformation
---

<a href="../index.html">@pulumi/aws</a> &gt; cloudformation

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Stack">class Stack</a>
* <a href="#getExport">function getExport</a>
* <a href="#getStack">function getStack</a>
* <a href="#GetExportArgs">interface GetExportArgs</a>
* <a href="#GetExportResult">interface GetExportResult</a>
* <a href="#GetStackArgs">interface GetStackArgs</a>
* <a href="#GetStackResult">interface GetStackResult</a>
* <a href="#StackArgs">interface StackArgs</a>
* <a href="#StackState">interface StackState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getExport.ts">cloudformation/getExport.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts">cloudformation/getStack.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts">cloudformation/stack.ts</a> 


<h2 class="pdoc-module-header" id="Stack">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L12">class Stack</a>
</h2>

Provides a CloudFormation Stack resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L85">constructor</a>
</h3>

```typescript
new Stack(name: string, args?: StackArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Stack resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StackState): Stack
```


Get an existing Stack resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L29">property capabilities</a>
</h3>

```typescript
public capabilities: pulumi.Output<string[] | undefined>;
```


A list of capabilities.
Valid values: `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L34">property disableRollback</a>
</h3>

```typescript
public disableRollback: pulumi.Output<boolean | undefined>;
```


Set to true to disable rollback of the stack if stack creation failed.
Conflicts with `on_failure`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L38">property iamRoleArn</a>
</h3>

```typescript
public iamRoleArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Stack name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L46">property notificationArns</a>
</h3>

```typescript
public notificationArns: pulumi.Output<string[] | undefined>;
```


A list of SNS topic ARNs to publish stack related events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L51">property onFailure</a>
</h3>

```typescript
public onFailure: pulumi.Output<string | undefined>;
```


Action to be taken if stack creation fails. This must be
one of: `DO_NOTHING`, `ROLLBACK`, or `DELETE`. Conflicts with `disable_rollback`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L55">property outputs</a>
</h3>

```typescript
public outputs: pulumi.Output<{ ... }>;
```


A map of outputs from the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L59">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... }>;
```


A map of Parameter structures that specify input parameters for the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L64">property policyBody</a>
</h3>

```typescript
public policyBody: pulumi.Output<string>;
```


Structure containing the stack policy body.
Conflicts w/ `policy_url`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L69">property policyUrl</a>
</h3>

```typescript
public policyUrl: pulumi.Output<string | undefined>;
```


Location of a file containing the stack policy.
Conflicts w/ `policy_body`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L73">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A list of tags to associate with this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L77">property templateBody</a>
</h3>

```typescript
public templateBody: pulumi.Output<string>;
```


Structure containing the template body (max size: 51,200 bytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L81">property templateUrl</a>
</h3>

```typescript
public templateUrl: pulumi.Output<string | undefined>;
```


Location of a file containing the template body (max size: 460,800 bytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L85">property timeoutInMinutes</a>
</h3>

```typescript
public timeoutInMinutes: pulumi.Output<number | undefined>;
```


The amount of time that can pass before the stack status becomes `CREATE_FAILED`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getExport">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getExport.ts#L13">function getExport</a>
</h2>

```typescript
getExport(args: GetExportArgs, opts?: pulumi.InvokeOptions): Promise<GetExportResult>
```


The CloudFormation Export data source allows access to stack
exports specified in the [Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html) section of the Cloudformation Template using the optional Export Property.

 -> Note: If you are trying to use a value from a Cloudformation Stack in the same Terraform run please use normal interpolation or Cloudformation Outputs.

<h2 class="pdoc-module-header" id="getStack">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L11">function getStack</a>
</h2>

```typescript
getStack(args: GetStackArgs, opts?: pulumi.InvokeOptions): Promise<GetStackResult>
```


The CloudFormation Stack data source allows access to stack
outputs and other useful data including the template body.

<h2 class="pdoc-module-header" id="GetExportArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getExport.ts#L22">interface GetExportArgs</a>
</h2>

A collection of arguments for invoking getExport.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getExport.ts#L26">property name</a>
</h3>

```typescript
name: string;
```


The name of the export as it appears in the console or from [list-exports](http://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-exports.html)

<h2 class="pdoc-module-header" id="GetExportResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getExport.ts#L32">interface GetExportResult</a>
</h2>

A collection of values returned by getExport.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getExport.ts#L36">property exportingStackId</a>
</h3>

```typescript
exportingStackId: string;
```


The exporting_stack_id (AWS ARNs) equivalent `ExportingStackId` from [list-exports](http://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-exports.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getExport.ts#L44">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getExport.ts#L40">property value</a>
</h3>

```typescript
value: string;
```


The value from Cloudformation export identified by the export name found from [list-exports](http://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-exports.html)

<h2 class="pdoc-module-header" id="GetStackArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L20">interface GetStackArgs</a>
</h2>

A collection of arguments for invoking getStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


The name of the stack

<h2 class="pdoc-module-header" id="GetStackResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L30">interface GetStackResult</a>
</h2>

A collection of values returned by getStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L34">property capabilities</a>
</h3>

```typescript
capabilities: string[];
```


A list of capabilities

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L38">property description</a>
</h3>

```typescript
description: string;
```


Description of the stack

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L42">property disableRollback</a>
</h3>

```typescript
disableRollback: boolean;
```


Whether the rollback of the stack is disabled when stack creation fails

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L46">property iamRoleArn</a>
</h3>

```typescript
iamRoleArn: string;
```


The ARN of the IAM role used to create the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L74">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L50">property notificationArns</a>
</h3>

```typescript
notificationArns: string[];
```


A list of SNS topic ARNs to publish stack related events

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L54">property outputs</a>
</h3>

```typescript
outputs: { ... };
```


A map of outputs from the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L58">property parameters</a>
</h3>

```typescript
parameters: { ... };
```


A map of parameters that specify input parameters for the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L62">property tags</a>
</h3>

```typescript
tags: { ... };
```


A map of tags associated with this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L66">property templateBody</a>
</h3>

```typescript
templateBody: string;
```


Structure containing the template body.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L70">property timeoutInMinutes</a>
</h3>

```typescript
timeoutInMinutes: number;
```


The amount of time that can pass before the stack status becomes `CREATE_FAILED`

<h2 class="pdoc-module-header" id="StackArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L204">interface StackArgs</a>
</h2>

The set of arguments for constructing a Stack resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L209">property capabilities</a>
</h3>

```typescript
capabilities?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of capabilities.
Valid values: `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L214">property disableRollback</a>
</h3>

```typescript
disableRollback?: pulumi.Input<boolean>;
```


Set to true to disable rollback of the stack if stack creation failed.
Conflicts with `on_failure`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L218">property iamRoleArn</a>
</h3>

```typescript
iamRoleArn?: pulumi.Input<string>;
```


The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L222">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Stack name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L226">property notificationArns</a>
</h3>

```typescript
notificationArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of SNS topic ARNs to publish stack related events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L231">property onFailure</a>
</h3>

```typescript
onFailure?: pulumi.Input<string>;
```


Action to be taken if stack creation fails. This must be
one of: `DO_NOTHING`, `ROLLBACK`, or `DELETE`. Conflicts with `disable_rollback`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L235">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


A map of Parameter structures that specify input parameters for the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L240">property policyBody</a>
</h3>

```typescript
policyBody?: pulumi.Input<string>;
```


Structure containing the stack policy body.
Conflicts w/ `policy_url`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L245">property policyUrl</a>
</h3>

```typescript
policyUrl?: pulumi.Input<string>;
```


Location of a file containing the stack policy.
Conflicts w/ `policy_body`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L249">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A list of tags to associate with this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L253">property templateBody</a>
</h3>

```typescript
templateBody?: pulumi.Input<string>;
```


Structure containing the template body (max size: 51,200 bytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L257">property templateUrl</a>
</h3>

```typescript
templateUrl?: pulumi.Input<string>;
```


Location of a file containing the template body (max size: 460,800 bytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L261">property timeoutInMinutes</a>
</h3>

```typescript
timeoutInMinutes?: pulumi.Input<number>;
```


The amount of time that can pass before the stack status becomes `CREATE_FAILED`.

<h2 class="pdoc-module-header" id="StackState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L137">interface StackState</a>
</h2>

Input properties used for looking up and filtering Stack resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L142">property capabilities</a>
</h3>

```typescript
capabilities?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of capabilities.
Valid values: `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L147">property disableRollback</a>
</h3>

```typescript
disableRollback?: pulumi.Input<boolean>;
```


Set to true to disable rollback of the stack if stack creation failed.
Conflicts with `on_failure`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L151">property iamRoleArn</a>
</h3>

```typescript
iamRoleArn?: pulumi.Input<string>;
```


The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L155">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Stack name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L159">property notificationArns</a>
</h3>

```typescript
notificationArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of SNS topic ARNs to publish stack related events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L164">property onFailure</a>
</h3>

```typescript
onFailure?: pulumi.Input<string>;
```


Action to be taken if stack creation fails. This must be
one of: `DO_NOTHING`, `ROLLBACK`, or `DELETE`. Conflicts with `disable_rollback`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L168">property outputs</a>
</h3>

```typescript
outputs?: pulumi.Input<{ ... }>;
```


A map of outputs from the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L172">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


A map of Parameter structures that specify input parameters for the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L177">property policyBody</a>
</h3>

```typescript
policyBody?: pulumi.Input<string>;
```


Structure containing the stack policy body.
Conflicts w/ `policy_url`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L182">property policyUrl</a>
</h3>

```typescript
policyUrl?: pulumi.Input<string>;
```


Location of a file containing the stack policy.
Conflicts w/ `policy_body`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L186">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A list of tags to associate with this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L190">property templateBody</a>
</h3>

```typescript
templateBody?: pulumi.Input<string>;
```


Structure containing the template body (max size: 51,200 bytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L194">property templateUrl</a>
</h3>

```typescript
templateUrl?: pulumi.Input<string>;
```


Location of a file containing the template body (max size: 460,800 bytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L198">property timeoutInMinutes</a>
</h3>

```typescript
timeoutInMinutes?: pulumi.Input<number>;
```


The amount of time that can pass before the stack status becomes `CREATE_FAILED`.

