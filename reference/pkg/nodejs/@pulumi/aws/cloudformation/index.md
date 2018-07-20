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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L9">class Stack</a>
</h2>

Provides a CloudFormation Stack resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L82">constructor</a>
</h3>

```typescript
new Stack(name: string, args?: StackArgs, opts?: pulumi.ResourceOptions)
```


Create a Stack resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StackState): Stack
```


Get an existing Stack resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L26">property capabilities</a>
</h3>

```typescript
public capabilities: pulumi.Output<string[] | undefined>;
```


A list of capabilities.
Valid values: `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L31">property disableRollback</a>
</h3>

```typescript
public disableRollback: pulumi.Output<boolean | undefined>;
```


Set to true to disable rollback of the stack if stack creation failed.
Conflicts with `on_failure`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L35">property iamRoleArn</a>
</h3>

```typescript
public iamRoleArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L39">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Stack name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L43">property notificationArns</a>
</h3>

```typescript
public notificationArns: pulumi.Output<string[] | undefined>;
```


A list of SNS topic ARNs to publish stack related events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L48">property onFailure</a>
</h3>

```typescript
public onFailure: pulumi.Output<string | undefined>;
```


Action to be taken if stack creation fails. This must be
one of: `DO_NOTHING`, `ROLLBACK`, or `DELETE`. Conflicts with `disable_rollback`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L52">property outputs</a>
</h3>

```typescript
public outputs: pulumi.Output<{ ... }>;
```


A map of outputs from the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L56">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... }>;
```


A list of Parameter structures that specify input parameters for the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L61">property policyBody</a>
</h3>

```typescript
public policyBody: pulumi.Output<string>;
```


Structure containing the stack policy body.
Conflicts w/ `policy_url`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L66">property policyUrl</a>
</h3>

```typescript
public policyUrl: pulumi.Output<string | undefined>;
```


Location of a file containing the stack policy.
Conflicts w/ `policy_body`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L70">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


A list of tags to associate with this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L74">property templateBody</a>
</h3>

```typescript
public templateBody: pulumi.Output<string>;
```


Structure containing the template body (max size: 51,200 bytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L78">property templateUrl</a>
</h3>

```typescript
public templateUrl: pulumi.Output<string | undefined>;
```


Location of a file containing the template body (max size: 460,800 bytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L82">property timeoutInMinutes</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getExport.ts#L12">function getExport</a>
</h2>

```typescript
getExport(args: GetExportArgs): Promise<GetExportResult>
```


The CloudFormation Export data source allows access to stack
exports specified in the [Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html) section of the Cloudformation Template using the optional Export Property.

 -> Note: If you are trying to use a value from a Cloudformation Stack in the same Terraform run please use normal interpolation or Cloudformation Outputs.

<h2 class="pdoc-module-header" id="getStack">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L10">function getStack</a>
</h2>

```typescript
getStack(args: GetStackArgs): Promise<GetStackResult>
```


The CloudFormation Stack data source allows access to stack
outputs and other useful data including the template body.

<h2 class="pdoc-module-header" id="GetExportArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getExport.ts#L21">interface GetExportArgs</a>
</h2>

A collection of arguments for invoking getExport.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getExport.ts#L25">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The name of the cross stack reference

<h2 class="pdoc-module-header" id="GetExportResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getExport.ts#L31">interface GetExportResult</a>
</h2>

A collection of values returned by getExport.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getExport.ts#L35">property exportingStackId</a>
</h3>

```typescript
exportingStackId: string;
```


The exporting_stack_id (AWS ARNs) equivalent `ExportingStackId` from [list-exports](http://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-exports.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getExport.ts#L43">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getExport.ts#L39">property value</a>
</h3>

```typescript
value: string;
```


The value from Cloudformation export identified by the export name found from [list-exports](http://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-exports.html)

<h2 class="pdoc-module-header" id="GetStackArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L19">interface GetStackArgs</a>
</h2>

A collection of arguments for invoking getStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L23">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The name of the stack

<h2 class="pdoc-module-header" id="GetStackResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L29">interface GetStackResult</a>
</h2>

A collection of values returned by getStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L33">property capabilities</a>
</h3>

```typescript
capabilities: string[];
```


A list of capabilities

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L37">property description</a>
</h3>

```typescript
description: string;
```


Description of the stack

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L41">property disableRollback</a>
</h3>

```typescript
disableRollback: boolean;
```


Whether the rollback of the stack is disabled when stack creation fails

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L45">property iamRoleArn</a>
</h3>

```typescript
iamRoleArn: string;
```


The ARN of the IAM role used to create the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L73">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L49">property notificationArns</a>
</h3>

```typescript
notificationArns: string[];
```


A list of SNS topic ARNs to publish stack related events

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L53">property outputs</a>
</h3>

```typescript
outputs: { ... };
```


A map of outputs from the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L57">property parameters</a>
</h3>

```typescript
parameters: { ... };
```


A map of parameters that specify input parameters for the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L61">property tags</a>
</h3>

```typescript
tags: { ... };
```


A map of tags associated with this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L65">property templateBody</a>
</h3>

```typescript
templateBody: string;
```


Structure containing the template body.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/getStack.ts#L69">property timeoutInMinutes</a>
</h3>

```typescript
timeoutInMinutes: number;
```


The amount of time that can pass before the stack status becomes `CREATE_FAILED`

<h2 class="pdoc-module-header" id="StackArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L201">interface StackArgs</a>
</h2>

The set of arguments for constructing a Stack resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L206">property capabilities</a>
</h3>

```typescript
capabilities?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of capabilities.
Valid values: `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L211">property disableRollback</a>
</h3>

```typescript
disableRollback?: pulumi.Input<boolean>;
```


Set to true to disable rollback of the stack if stack creation failed.
Conflicts with `on_failure`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L215">property iamRoleArn</a>
</h3>

```typescript
iamRoleArn?: pulumi.Input<string>;
```


The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L219">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Stack name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L223">property notificationArns</a>
</h3>

```typescript
notificationArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of SNS topic ARNs to publish stack related events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L228">property onFailure</a>
</h3>

```typescript
onFailure?: pulumi.Input<string>;
```


Action to be taken if stack creation fails. This must be
one of: `DO_NOTHING`, `ROLLBACK`, or `DELETE`. Conflicts with `disable_rollback`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L232">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


A list of Parameter structures that specify input parameters for the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L237">property policyBody</a>
</h3>

```typescript
policyBody?: pulumi.Input<string>;
```


Structure containing the stack policy body.
Conflicts w/ `policy_url`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L242">property policyUrl</a>
</h3>

```typescript
policyUrl?: pulumi.Input<string>;
```


Location of a file containing the stack policy.
Conflicts w/ `policy_body`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L246">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A list of tags to associate with this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L250">property templateBody</a>
</h3>

```typescript
templateBody?: pulumi.Input<string>;
```


Structure containing the template body (max size: 51,200 bytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L254">property templateUrl</a>
</h3>

```typescript
templateUrl?: pulumi.Input<string>;
```


Location of a file containing the template body (max size: 460,800 bytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L258">property timeoutInMinutes</a>
</h3>

```typescript
timeoutInMinutes?: pulumi.Input<number>;
```


The amount of time that can pass before the stack status becomes `CREATE_FAILED`.

<h2 class="pdoc-module-header" id="StackState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L134">interface StackState</a>
</h2>

Input properties used for looking up and filtering Stack resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L139">property capabilities</a>
</h3>

```typescript
capabilities?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of capabilities.
Valid values: `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L144">property disableRollback</a>
</h3>

```typescript
disableRollback?: pulumi.Input<boolean>;
```


Set to true to disable rollback of the stack if stack creation failed.
Conflicts with `on_failure`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L148">property iamRoleArn</a>
</h3>

```typescript
iamRoleArn?: pulumi.Input<string>;
```


The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L152">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Stack name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L156">property notificationArns</a>
</h3>

```typescript
notificationArns?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of SNS topic ARNs to publish stack related events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L161">property onFailure</a>
</h3>

```typescript
onFailure?: pulumi.Input<string>;
```


Action to be taken if stack creation fails. This must be
one of: `DO_NOTHING`, `ROLLBACK`, or `DELETE`. Conflicts with `disable_rollback`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L165">property outputs</a>
</h3>

```typescript
outputs?: pulumi.Input<{ ... }>;
```


A map of outputs from the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L169">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


A list of Parameter structures that specify input parameters for the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L174">property policyBody</a>
</h3>

```typescript
policyBody?: pulumi.Input<string>;
```


Structure containing the stack policy body.
Conflicts w/ `policy_url`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L179">property policyUrl</a>
</h3>

```typescript
policyUrl?: pulumi.Input<string>;
```


Location of a file containing the stack policy.
Conflicts w/ `policy_body`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L183">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A list of tags to associate with this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L187">property templateBody</a>
</h3>

```typescript
templateBody?: pulumi.Input<string>;
```


Structure containing the template body (max size: 51,200 bytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L191">property templateUrl</a>
</h3>

```typescript
templateUrl?: pulumi.Input<string>;
```


Location of a file containing the template body (max size: 460,800 bytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudformation/stack.ts#L195">property timeoutInMinutes</a>
</h3>

```typescript
timeoutInMinutes?: pulumi.Input<number>;
```


The amount of time that can pass before the stack status becomes `CREATE_FAILED`.

