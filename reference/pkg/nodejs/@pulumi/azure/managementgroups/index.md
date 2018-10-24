---
title: Module managementgroups
---

<a href="../index.html">@pulumi/azure</a> &gt; managementgroups

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ManagementGroup">class ManagementGroup</a>
* <a href="#getManagementGroup">function getManagementGroup</a>
* <a href="#GetManagementGroupArgs">interface GetManagementGroupArgs</a>
* <a href="#GetManagementGroupResult">interface GetManagementGroupResult</a>
* <a href="#ManagementGroupArgs">interface ManagementGroupArgs</a>
* <a href="#ManagementGroupState">interface ManagementGroupState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/getManagementGroup.ts">managementgroups/getManagementGroup.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts">managementgroups/managementGroup.ts</a> 


<h2 class="pdoc-module-header" id="ManagementGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts#L10">class ManagementGroup</a>
</h2>

Manages a Management Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts#L38">constructor</a>
</h3>

```typescript
new ManagementGroup(name: string, args?: ManagementGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ManagementGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ManagementGroupState): ManagementGroup
```


Get an existing ManagementGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts#L26">property displayName</a>
</h3>

```typescript
public displayName: pulumi.Output<string>;
```


A friendly name for this Management Group. If not specified, this'll be the same as the `group_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts#L30">property groupId</a>
</h3>

```typescript
public groupId: pulumi.Output<string>;
```


The UUID for this Management Group, which needs to be unique across your tenant - which will be generated if not provided. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts#L34">property parentManagementGroupId</a>
</h3>

```typescript
public parentManagementGroupId: pulumi.Output<string>;
```


The ID of the Parent Management Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts#L38">property subscriptionIds</a>
</h3>

```typescript
public subscriptionIds: pulumi.Output<string[] | undefined>;
```


A list of Subscription ID's which should be assigned to the Management Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getManagementGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/getManagementGroup.ts#L10">function getManagementGroup</a>
</h2>

```typescript
getManagementGroup(args: GetManagementGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetManagementGroupResult>
```


Use this data source to access information about an existing Management Group.

<h2 class="pdoc-module-header" id="GetManagementGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/getManagementGroup.ts#L19">interface GetManagementGroupArgs</a>
</h2>

A collection of arguments for invoking getManagementGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/getManagementGroup.ts#L23">property groupId</a>
</h3>

```typescript
groupId: string;
```


Specifies the UUID of this Management Group.

<h2 class="pdoc-module-header" id="GetManagementGroupResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/getManagementGroup.ts#L29">interface GetManagementGroupResult</a>
</h2>

A collection of values returned by getManagementGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/getManagementGroup.ts#L33">property displayName</a>
</h3>

```typescript
displayName: string;
```


A friendly name for the Management Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/getManagementGroup.ts#L45">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/getManagementGroup.ts#L37">property parentManagementGroupId</a>
</h3>

```typescript
parentManagementGroupId: string;
```


The ID of any Parent Management Group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/getManagementGroup.ts#L41">property subscriptionIds</a>
</h3>

```typescript
subscriptionIds: string[];
```


A list of Subscription ID's which are assigned to the Management Group.

<h2 class="pdoc-module-header" id="ManagementGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts#L92">interface ManagementGroupArgs</a>
</h2>

The set of arguments for constructing a ManagementGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts#L96">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


A friendly name for this Management Group. If not specified, this'll be the same as the `group_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts#L100">property groupId</a>
</h3>

```typescript
groupId?: pulumi.Input<string>;
```


The UUID for this Management Group, which needs to be unique across your tenant - which will be generated if not provided. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts#L104">property parentManagementGroupId</a>
</h3>

```typescript
parentManagementGroupId?: pulumi.Input<string>;
```


The ID of the Parent Management Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts#L108">property subscriptionIds</a>
</h3>

```typescript
subscriptionIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Subscription ID's which should be assigned to the Management Group.

<h2 class="pdoc-module-header" id="ManagementGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts#L70">interface ManagementGroupState</a>
</h2>

Input properties used for looking up and filtering ManagementGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts#L74">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


A friendly name for this Management Group. If not specified, this'll be the same as the `group_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts#L78">property groupId</a>
</h3>

```typescript
groupId?: pulumi.Input<string>;
```


The UUID for this Management Group, which needs to be unique across your tenant - which will be generated if not provided. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts#L82">property parentManagementGroupId</a>
</h3>

```typescript
parentManagementGroupId?: pulumi.Input<string>;
```


The ID of the Parent Management Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/managementgroups/managementGroup.ts#L86">property subscriptionIds</a>
</h3>

```typescript
subscriptionIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Subscription ID's which should be assigned to the Management Group.

