---
title: Module inspector
---

<a href="../index.html">@pulumi/aws</a> &gt; inspector

<h2 class="pdoc-module-header">Index</h2>

* <a href="#AssessmentTarget">class AssessmentTarget</a>
* <a href="#AssessmentTemplate">class AssessmentTemplate</a>
* <a href="#ResourceGroup">class ResourceGroup</a>
* <a href="#getRulesPackages">function getRulesPackages</a>
* <a href="#AssessmentTargetArgs">interface AssessmentTargetArgs</a>
* <a href="#AssessmentTargetState">interface AssessmentTargetState</a>
* <a href="#AssessmentTemplateArgs">interface AssessmentTemplateArgs</a>
* <a href="#AssessmentTemplateState">interface AssessmentTemplateState</a>
* <a href="#GetRulesPackagesResult">interface GetRulesPackagesResult</a>
* <a href="#ResourceGroupArgs">interface ResourceGroupArgs</a>
* <a href="#ResourceGroupState">interface ResourceGroupState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTarget.ts">inspector/assessmentTarget.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts">inspector/assessmentTemplate.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/getRulesPackages.ts">inspector/getRulesPackages.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/resourceGroup.ts">inspector/resourceGroup.ts</a> 


<h2 class="pdoc-module-header" id="AssessmentTarget">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTarget.ts#L9">class AssessmentTarget</a>
</h2>

Provides a Inspector assessment target

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTarget.ts#L31">constructor</a>
</h3>

```typescript
new AssessmentTarget(name: string, args: AssessmentTargetArgs, opts?: pulumi.ResourceOptions)
```


Create a AssessmentTarget resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTarget.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AssessmentTargetState): AssessmentTarget
```


Get an existing AssessmentTarget resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTarget.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The target assessment ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTarget.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the assessment target.
* `resource_group_arn` (Required )- The resource group ARN stating tags for instance matching.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTarget.ts#L31">property resourceGroupArn</a>
</h3>

```typescript
public resourceGroupArn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AssessmentTemplate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L9">class AssessmentTemplate</a>
</h2>

Provides a Inspector assessment template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L41">constructor</a>
</h3>

```typescript
new AssessmentTemplate(name: string, args: AssessmentTemplateArgs, opts?: pulumi.ResourceOptions)
```


Create a AssessmentTemplate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AssessmentTemplateState): AssessmentTemplate
```


Get an existing AssessmentTemplate resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The template assessment ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L29">property duration</a>
</h3>

```typescript
public duration: pulumi.Output<number>;
```


The duration of the inspector run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the assessment template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L37">property rulesPackageArns</a>
</h3>

```typescript
public rulesPackageArns: pulumi.Output<string[]>;
```


The rules to be used during the run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L41">property targetArn</a>
</h3>

```typescript
public targetArn: pulumi.Output<string>;
```


The assessment target ARN to attach the template to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ResourceGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/resourceGroup.ts#L9">class ResourceGroup</a>
</h2>

Provides a Inspector resource group

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/resourceGroup.ts#L29">constructor</a>
</h3>

```typescript
new ResourceGroup(name: string, args: ResourceGroupArgs, opts?: pulumi.ResourceOptions)
```


Create a ResourceGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/resourceGroup.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ResourceGroupState): ResourceGroup
```


Get an existing ResourceGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/resourceGroup.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The resource group ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/resourceGroup.ts#L29">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


The tags on your EC2 Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getRulesPackages">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/getRulesPackages.ts#L11">function getRulesPackages</a>
</h2>

```typescript
getRulesPackages(): Promise<GetRulesPackagesResult>
```


The AWS Inspector Rules Packages data source allows access to the list of AWS
Inspector Rules Packages which can be used by AWS Inspector within the region
configured in the provider.

<h2 class="pdoc-module-header" id="AssessmentTargetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTarget.ts#L80">interface AssessmentTargetArgs</a>
</h2>

The set of arguments for constructing a AssessmentTarget resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTarget.ts#L85">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the assessment target.
* `resource_group_arn` (Required )- The resource group ARN stating tags for instance matching.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTarget.ts#L86">property resourceGroupArn</a>
</h3>

```typescript
resourceGroupArn: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="AssessmentTargetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTarget.ts#L64">interface AssessmentTargetState</a>
</h2>

Input properties used for looking up and filtering AssessmentTarget resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTarget.ts#L68">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The target assessment ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTarget.ts#L73">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the assessment target.
* `resource_group_arn` (Required )- The resource group ARN stating tags for instance matching.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTarget.ts#L74">property resourceGroupArn</a>
</h3>

```typescript
resourceGroupArn?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="AssessmentTemplateArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L110">interface AssessmentTemplateArgs</a>
</h2>

The set of arguments for constructing a AssessmentTemplate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L114">property duration</a>
</h3>

```typescript
duration: pulumi.Input<number>;
```


The duration of the inspector run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L118">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the assessment template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L122">property rulesPackageArns</a>
</h3>

```typescript
rulesPackageArns: pulumi.Input<pulumi.Input<string>[]>;
```


The rules to be used during the run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L126">property targetArn</a>
</h3>

```typescript
targetArn: pulumi.Input<string>;
```


The assessment target ARN to attach the template to.

<h2 class="pdoc-module-header" id="AssessmentTemplateState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L84">interface AssessmentTemplateState</a>
</h2>

Input properties used for looking up and filtering AssessmentTemplate resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L88">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The template assessment ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L92">property duration</a>
</h3>

```typescript
duration?: pulumi.Input<number>;
```


The duration of the inspector run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the assessment template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L100">property rulesPackageArns</a>
</h3>

```typescript
rulesPackageArns?: pulumi.Input<pulumi.Input<string>[]>;
```


The rules to be used during the run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/assessmentTemplate.ts#L104">property targetArn</a>
</h3>

```typescript
targetArn?: pulumi.Input<string>;
```


The assessment target ARN to attach the template to.

<h2 class="pdoc-module-header" id="GetRulesPackagesResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/getRulesPackages.ts#L19">interface GetRulesPackagesResult</a>
</h2>

A collection of values returned by getRulesPackages.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/getRulesPackages.ts#L23">property arns</a>
</h3>

```typescript
arns: string[];
```


A list of the AWS Inspector Rules Packages arns available in the AWS region.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/getRulesPackages.ts#L27">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="ResourceGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/resourceGroup.ts#L74">interface ResourceGroupArgs</a>
</h2>

The set of arguments for constructing a ResourceGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/resourceGroup.ts#L78">property tags</a>
</h3>

```typescript
tags: pulumi.Input<{ ... }>;
```


The tags on your EC2 Instance.

<h2 class="pdoc-module-header" id="ResourceGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/resourceGroup.ts#L60">interface ResourceGroupState</a>
</h2>

Input properties used for looking up and filtering ResourceGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/resourceGroup.ts#L64">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The resource group ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/inspector/resourceGroup.ts#L68">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


The tags on your EC2 Instance.

