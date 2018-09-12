---
title: Module logicapps
---

<a href="../index.html">@pulumi/azure</a> &gt; logicapps

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ActionCustom">class ActionCustom</a>
* <a href="#ActionHttp">class ActionHttp</a>
* <a href="#TriggerCustom">class TriggerCustom</a>
* <a href="#TriggerHttpRequest">class TriggerHttpRequest</a>
* <a href="#TriggerRecurrence">class TriggerRecurrence</a>
* <a href="#Workflow">class Workflow</a>
* <a href="#getWorkflow">function getWorkflow</a>
* <a href="#ActionCustomArgs">interface ActionCustomArgs</a>
* <a href="#ActionCustomState">interface ActionCustomState</a>
* <a href="#ActionHttpArgs">interface ActionHttpArgs</a>
* <a href="#ActionHttpState">interface ActionHttpState</a>
* <a href="#GetWorkflowArgs">interface GetWorkflowArgs</a>
* <a href="#GetWorkflowResult">interface GetWorkflowResult</a>
* <a href="#TriggerCustomArgs">interface TriggerCustomArgs</a>
* <a href="#TriggerCustomState">interface TriggerCustomState</a>
* <a href="#TriggerHttpRequestArgs">interface TriggerHttpRequestArgs</a>
* <a href="#TriggerHttpRequestState">interface TriggerHttpRequestState</a>
* <a href="#TriggerRecurrenceArgs">interface TriggerRecurrenceArgs</a>
* <a href="#TriggerRecurrenceState">interface TriggerRecurrenceState</a>
* <a href="#WorkflowArgs">interface WorkflowArgs</a>
* <a href="#WorkflowState">interface WorkflowState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts">logicapps/actionCustom.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts">logicapps/actionHttp.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts">logicapps/getWorkflow.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts">logicapps/triggerCustom.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts">logicapps/triggerHttpRequest.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts">logicapps/triggerRecurrence.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts">logicapps/workflow.ts</a> 


<h2 class="pdoc-module-header" id="ActionCustom">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L10">class ActionCustom</a>
</h2>

Manages a Custom Action within a Logic App Workflow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L34">constructor</a>
</h3>

```typescript
new ActionCustom(name: string, args: ActionCustomArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ActionCustom resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ActionCustomState): ActionCustom
```


Get an existing ActionCustom resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L26">property body</a>
</h3>

```typescript
public body: pulumi.Output<string>;
```


Specifies the JSON Blob defining the Body of this Custom Action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L30">property logicAppId</a>
</h3>

```typescript
public logicAppId: pulumi.Output<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ActionHttp">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L10">class ActionHttp</a>
</h2>

Manages an HTTP Action within a Logic App Workflow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L46">constructor</a>
</h3>

```typescript
new ActionHttp(name: string, args: ActionHttpArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ActionHttp resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ActionHttpState): ActionHttp
```


Get an existing ActionHttp resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L26">property body</a>
</h3>

```typescript
public body: pulumi.Output<string | undefined>;
```


Specifies the HTTP Body that should be sent to the `uri` when this HTTP Action is triggered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L30">property headers</a>
</h3>

```typescript
public headers: pulumi.Output<{ ... } | undefined>;
```


Specifies a Map of Key-Value Pairs that should be sent to the `uri` when this HTTP Action is triggered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L34">property logicAppId</a>
</h3>

```typescript
public logicAppId: pulumi.Output<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L38">property method</a>
</h3>

```typescript
public method: pulumi.Output<string>;
```


Specifies the HTTP Method which should be used for this HTTP Action. Possible values include `DELETE`, `GET`, `PATCH`, `POST` and `PUT`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L46">property uri</a>
</h3>

```typescript
public uri: pulumi.Output<string>;
```


Specifies the URI which will be called when this HTTP Action is triggered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TriggerCustom">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L10">class TriggerCustom</a>
</h2>

Manages a Custom Trigger within a Logic App Workflow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L34">constructor</a>
</h3>

```typescript
new TriggerCustom(name: string, args: TriggerCustomArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TriggerCustom resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TriggerCustomState): TriggerCustom
```


Get an existing TriggerCustom resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L26">property body</a>
</h3>

```typescript
public body: pulumi.Output<string>;
```


Specifies the JSON Blob defining the Body of this Custom Trigger.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L30">property logicAppId</a>
</h3>

```typescript
public logicAppId: pulumi.Output<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the HTTP Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TriggerHttpRequest">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L10">class TriggerHttpRequest</a>
</h2>

Manages a HTTP Request Trigger within a Logic App Workflow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L42">constructor</a>
</h3>

```typescript
new TriggerHttpRequest(name: string, args: TriggerHttpRequestArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TriggerHttpRequest resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TriggerHttpRequestState): TriggerHttpRequest
```


Get an existing TriggerHttpRequest resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L26">property logicAppId</a>
</h3>

```typescript
public logicAppId: pulumi.Output<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L30">property method</a>
</h3>

```typescript
public method: pulumi.Output<string | undefined>;
```


Specifies the HTTP Method which the request be using. Possible values include `DELETE`, `GET`, `PATCH`, `POST` or `PUT`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the HTTP Request Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L38">property relativePath</a>
</h3>

```typescript
public relativePath: pulumi.Output<string | undefined>;
```


Specifies the Relative Path used for this Request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L42">property schema</a>
</h3>

```typescript
public schema: pulumi.Output<string>;
```


A JSON Blob defining the Schema of the incoming request. This needs to be valid JSON.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TriggerRecurrence">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L10">class TriggerRecurrence</a>
</h2>

Manages a Recurrence Trigger within a Logic App Workflow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L38">constructor</a>
</h3>

```typescript
new TriggerRecurrence(name: string, args: TriggerRecurrenceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TriggerRecurrence resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TriggerRecurrenceState): TriggerRecurrence
```


Get an existing TriggerRecurrence resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L26">property frequency</a>
</h3>

```typescript
public frequency: pulumi.Output<string>;
```


Specifies the Frequency at which this Trigger should be run. Possible values include `Month`, `Week`, `Day`, `Hour`, `Minute` and `Second`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L30">property interval</a>
</h3>

```typescript
public interval: pulumi.Output<number>;
```


Specifies interval used for the Frequency, for example a value of `4` for `interval` and `hour` for `frequency` would run the Trigger every 4 hours.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L34">property logicAppId</a>
</h3>

```typescript
public logicAppId: pulumi.Output<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Recurrence Triggers to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Workflow">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L10">class Workflow</a>
</h2>

Manages a Logic App Workflow.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L54">constructor</a>
</h3>

```typescript
new Workflow(name: string, args: WorkflowArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Workflow resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WorkflowState): Workflow
```


Get an existing Workflow resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L26">property accessEndpoint</a>
</h3>

```typescript
public accessEndpoint: pulumi.Output<string>;
```


The Access Endpoint for the Logic App Workflow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L30">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the Logic App Workflow exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L38">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... } | undefined>;
```


A map of Key-Value pairs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L42">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the Resource Group in which the Logic App Workflow should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L46">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L50">property workflowSchema</a>
</h3>

```typescript
public workflowSchema: pulumi.Output<string | undefined>;
```


Specifies the Schema to use for this Logic App Workflow. Defaults to `https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L54">property workflowVersion</a>
</h3>

```typescript
public workflowVersion: pulumi.Output<string | undefined>;
```


Specifies the version of the Schema used for this Logic App Workflow. Defaults to `1.0.0.0`. Changing this forces a new resource to be create.d

<h2 class="pdoc-module-header" id="getWorkflow">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L10">function getWorkflow</a>
</h2>

```typescript
getWorkflow(args: GetWorkflowArgs, opts?: pulumi.InvokeOptions): Promise<GetWorkflowResult>
```


Gets information about a Logic App Workflow.

<h2 class="pdoc-module-header" id="ActionCustomArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L88">interface ActionCustomArgs</a>
</h2>

The set of arguments for constructing a ActionCustom resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L92">property body</a>
</h3>

```typescript
body: pulumi.Input<string>;
```


Specifies the JSON Blob defining the Body of this Custom Action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L96">property logicAppId</a>
</h3>

```typescript
logicAppId: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L100">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ActionCustomState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L70">interface ActionCustomState</a>
</h2>

Input properties used for looking up and filtering ActionCustom resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L74">property body</a>
</h3>

```typescript
body?: pulumi.Input<string>;
```


Specifies the JSON Blob defining the Body of this Custom Action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L78">property logicAppId</a>
</h3>

```typescript
logicAppId?: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L82">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ActionHttpArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L121">interface ActionHttpArgs</a>
</h2>

The set of arguments for constructing a ActionHttp resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L125">property body</a>
</h3>

```typescript
body?: pulumi.Input<string>;
```


Specifies the HTTP Body that should be sent to the `uri` when this HTTP Action is triggered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L129">property headers</a>
</h3>

```typescript
headers?: pulumi.Input<{ ... }>;
```


Specifies a Map of Key-Value Pairs that should be sent to the `uri` when this HTTP Action is triggered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L133">property logicAppId</a>
</h3>

```typescript
logicAppId: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L137">property method</a>
</h3>

```typescript
method: pulumi.Input<string>;
```


Specifies the HTTP Method which should be used for this HTTP Action. Possible values include `DELETE`, `GET`, `PATCH`, `POST` and `PUT`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L141">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L145">property uri</a>
</h3>

```typescript
uri: pulumi.Input<string>;
```


Specifies the URI which will be called when this HTTP Action is triggered.

<h2 class="pdoc-module-header" id="ActionHttpState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L91">interface ActionHttpState</a>
</h2>

Input properties used for looking up and filtering ActionHttp resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L95">property body</a>
</h3>

```typescript
body?: pulumi.Input<string>;
```


Specifies the HTTP Body that should be sent to the `uri` when this HTTP Action is triggered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L99">property headers</a>
</h3>

```typescript
headers?: pulumi.Input<{ ... }>;
```


Specifies a Map of Key-Value Pairs that should be sent to the `uri` when this HTTP Action is triggered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L103">property logicAppId</a>
</h3>

```typescript
logicAppId?: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L107">property method</a>
</h3>

```typescript
method?: pulumi.Input<string>;
```


Specifies the HTTP Method which should be used for this HTTP Action. Possible values include `DELETE`, `GET`, `PATCH`, `POST` and `PUT`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L111">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L115">property uri</a>
</h3>

```typescript
uri?: pulumi.Input<string>;
```


Specifies the URI which will be called when this HTTP Action is triggered.

<h2 class="pdoc-module-header" id="GetWorkflowArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L20">interface GetWorkflowArgs</a>
</h2>

A collection of arguments for invoking getWorkflow.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


The name of the Logic App Workflow.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The name of the Resource Group in which the Logic App Workflow exists.

<h2 class="pdoc-module-header" id="GetWorkflowResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L34">interface GetWorkflowResult</a>
</h2>

A collection of values returned by getWorkflow.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L38">property accessEndpoint</a>
</h3>

```typescript
accessEndpoint: string;
```


The Access Endpoint for the Logic App Workflow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L62">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L42">property location</a>
</h3>

```typescript
location: string;
```


The Azure location where the Logic App Workflow exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L46">property parameters</a>
</h3>

```typescript
parameters: { ... };
```


A map of Key-Value pairs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L50">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L54">property workflowSchema</a>
</h3>

```typescript
workflowSchema: string;
```


The Schema used for this Logic App Workflow.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L58">property workflowVersion</a>
</h3>

```typescript
workflowVersion: string;
```


The version of the Schema used for this Logic App Workflow. Defaults to `1.0.0.0`.

<h2 class="pdoc-module-header" id="TriggerCustomArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L88">interface TriggerCustomArgs</a>
</h2>

The set of arguments for constructing a TriggerCustom resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L92">property body</a>
</h3>

```typescript
body: pulumi.Input<string>;
```


Specifies the JSON Blob defining the Body of this Custom Trigger.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L96">property logicAppId</a>
</h3>

```typescript
logicAppId: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L100">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the HTTP Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TriggerCustomState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L70">interface TriggerCustomState</a>
</h2>

Input properties used for looking up and filtering TriggerCustom resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L74">property body</a>
</h3>

```typescript
body?: pulumi.Input<string>;
```


Specifies the JSON Blob defining the Body of this Custom Trigger.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L78">property logicAppId</a>
</h3>

```typescript
logicAppId?: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L82">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the HTTP Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TriggerHttpRequestArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L108">interface TriggerHttpRequestArgs</a>
</h2>

The set of arguments for constructing a TriggerHttpRequest resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L112">property logicAppId</a>
</h3>

```typescript
logicAppId: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L116">property method</a>
</h3>

```typescript
method?: pulumi.Input<string>;
```


Specifies the HTTP Method which the request be using. Possible values include `DELETE`, `GET`, `PATCH`, `POST` or `PUT`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L120">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the HTTP Request Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L124">property relativePath</a>
</h3>

```typescript
relativePath?: pulumi.Input<string>;
```


Specifies the Relative Path used for this Request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L128">property schema</a>
</h3>

```typescript
schema: pulumi.Input<string>;
```


A JSON Blob defining the Schema of the incoming request. This needs to be valid JSON.

<h2 class="pdoc-module-header" id="TriggerHttpRequestState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L82">interface TriggerHttpRequestState</a>
</h2>

Input properties used for looking up and filtering TriggerHttpRequest resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L86">property logicAppId</a>
</h3>

```typescript
logicAppId?: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L90">property method</a>
</h3>

```typescript
method?: pulumi.Input<string>;
```


Specifies the HTTP Method which the request be using. Possible values include `DELETE`, `GET`, `PATCH`, `POST` or `PUT`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L94">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the HTTP Request Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L98">property relativePath</a>
</h3>

```typescript
relativePath?: pulumi.Input<string>;
```


Specifies the Relative Path used for this Request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L102">property schema</a>
</h3>

```typescript
schema?: pulumi.Input<string>;
```


A JSON Blob defining the Schema of the incoming request. This needs to be valid JSON.

<h2 class="pdoc-module-header" id="TriggerRecurrenceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L101">interface TriggerRecurrenceArgs</a>
</h2>

The set of arguments for constructing a TriggerRecurrence resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L105">property frequency</a>
</h3>

```typescript
frequency: pulumi.Input<string>;
```


Specifies the Frequency at which this Trigger should be run. Possible values include `Month`, `Week`, `Day`, `Hour`, `Minute` and `Second`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L109">property interval</a>
</h3>

```typescript
interval: pulumi.Input<number>;
```


Specifies interval used for the Frequency, for example a value of `4` for `interval` and `hour` for `frequency` would run the Trigger every 4 hours.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L113">property logicAppId</a>
</h3>

```typescript
logicAppId: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L117">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Recurrence Triggers to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TriggerRecurrenceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L79">interface TriggerRecurrenceState</a>
</h2>

Input properties used for looking up and filtering TriggerRecurrence resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L83">property frequency</a>
</h3>

```typescript
frequency?: pulumi.Input<string>;
```


Specifies the Frequency at which this Trigger should be run. Possible values include `Month`, `Week`, `Day`, `Hour`, `Minute` and `Second`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L87">property interval</a>
</h3>

```typescript
interval?: pulumi.Input<number>;
```


Specifies interval used for the Frequency, for example a value of `4` for `interval` and `hour` for `frequency` would run the Trigger every 4 hours.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L91">property logicAppId</a>
</h3>

```typescript
logicAppId?: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L95">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Recurrence Triggers to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="WorkflowArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L138">interface WorkflowArgs</a>
</h2>

The set of arguments for constructing a Workflow resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L142">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the Logic App Workflow exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L146">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L150">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


A map of Key-Value pairs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L154">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the Resource Group in which the Logic App Workflow should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L158">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L162">property workflowSchema</a>
</h3>

```typescript
workflowSchema?: pulumi.Input<string>;
```


Specifies the Schema to use for this Logic App Workflow. Defaults to `https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L166">property workflowVersion</a>
</h3>

```typescript
workflowVersion?: pulumi.Input<string>;
```


Specifies the version of the Schema used for this Logic App Workflow. Defaults to `1.0.0.0`. Changing this forces a new resource to be create.d

<h2 class="pdoc-module-header" id="WorkflowState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L100">interface WorkflowState</a>
</h2>

Input properties used for looking up and filtering Workflow resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L104">property accessEndpoint</a>
</h3>

```typescript
accessEndpoint?: pulumi.Input<string>;
```


The Access Endpoint for the Logic App Workflow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L108">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the Logic App Workflow exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L112">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L116">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


A map of Key-Value pairs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L120">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the Resource Group in which the Logic App Workflow should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L124">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L128">property workflowSchema</a>
</h3>

```typescript
workflowSchema?: pulumi.Input<string>;
```


Specifies the Schema to use for this Logic App Workflow. Defaults to `https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L132">property workflowVersion</a>
</h3>

```typescript
workflowVersion?: pulumi.Input<string>;
```


Specifies the version of the Schema used for this Logic App Workflow. Defaults to `1.0.0.0`. Changing this forces a new resource to be create.d

