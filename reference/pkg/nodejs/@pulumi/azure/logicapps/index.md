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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L9">class ActionCustom</a>
</h2>

Manages a Custom Action within a Logic App Workflow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L33">constructor</a>
</h3>

```typescript
new ActionCustom(name: string, args: ActionCustomArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ActionCustom resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L25">property body</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L29">property logicAppId</a>
</h3>

```typescript
public logicAppId: pulumi.Output<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L33">property name</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L9">class ActionHttp</a>
</h2>

Manages an HTTP Action within a Logic App Workflow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L45">constructor</a>
</h3>

```typescript
new ActionHttp(name: string, args: ActionHttpArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ActionHttp resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L25">property body</a>
</h3>

```typescript
public body: pulumi.Output<string | undefined>;
```


Specifies the HTTP Body that should be sent to the `uri` when this HTTP Action is triggered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L29">property headers</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L33">property logicAppId</a>
</h3>

```typescript
public logicAppId: pulumi.Output<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L37">property method</a>
</h3>

```typescript
public method: pulumi.Output<string>;
```


Specifies the HTTP Method which should be used for this HTTP Action. Possible values include `DELETE`, `GET`, `PATCH`, `POST` and `PUT`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L41">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L45">property uri</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L9">class TriggerCustom</a>
</h2>

Manages a Custom Trigger within a Logic App Workflow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L33">constructor</a>
</h3>

```typescript
new TriggerCustom(name: string, args: TriggerCustomArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TriggerCustom resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L25">property body</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L29">property logicAppId</a>
</h3>

```typescript
public logicAppId: pulumi.Output<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L33">property name</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L9">class TriggerHttpRequest</a>
</h2>

Manages a HTTP Request Trigger within a Logic App Workflow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L41">constructor</a>
</h3>

```typescript
new TriggerHttpRequest(name: string, args: TriggerHttpRequestArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TriggerHttpRequest resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L25">property logicAppId</a>
</h3>

```typescript
public logicAppId: pulumi.Output<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L29">property method</a>
</h3>

```typescript
public method: pulumi.Output<string | undefined>;
```


Specifies the HTTP Method which the request be using. Possible values include `DELETE`, `GET`, `PATCH`, `POST` or `PUT`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the HTTP Request Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L37">property relativePath</a>
</h3>

```typescript
public relativePath: pulumi.Output<string | undefined>;
```


Specifies the Relative Path used for this Request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L41">property schema</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L9">class TriggerRecurrence</a>
</h2>

Manages a Recurrence Trigger within a Logic App Workflow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L37">constructor</a>
</h3>

```typescript
new TriggerRecurrence(name: string, args: TriggerRecurrenceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TriggerRecurrence resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L25">property frequency</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L29">property interval</a>
</h3>

```typescript
public interval: pulumi.Output<number>;
```


Specifies interval used for the Frequency, for example a value of `4` for `interval` and `hour` for `frequency` would run the Trigger every 4 hours.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L33">property logicAppId</a>
</h3>

```typescript
public logicAppId: pulumi.Output<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L37">property name</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L9">class Workflow</a>
</h2>

Manages a Logic App Workflow.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L53">constructor</a>
</h3>

```typescript
new Workflow(name: string, args: WorkflowArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Workflow resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L25">property accessEndpoint</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L29">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the Logic App Workflow exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L37">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... } | undefined>;
```


A map of Key-Value pairs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L41">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the Resource Group in which the Logic App Workflow should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L45">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L49">property workflowSchema</a>
</h3>

```typescript
public workflowSchema: pulumi.Output<string | undefined>;
```


Specifies the Schema to use for this Logic App Workflow. Defaults to `https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L53">property workflowVersion</a>
</h3>

```typescript
public workflowVersion: pulumi.Output<string | undefined>;
```


Specifies the version of the Schema used for this Logic App Workflow. Defaults to `1.0.0.0`. Changing this forces a new resource to be create.d

<h2 class="pdoc-module-header" id="getWorkflow">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L9">function getWorkflow</a>
</h2>

```typescript
getWorkflow(args: GetWorkflowArgs, opts?: pulumi.InvokeOptions): Promise<GetWorkflowResult>
```


Gets information about a Logic App Workflow.

<h2 class="pdoc-module-header" id="ActionCustomArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L87">interface ActionCustomArgs</a>
</h2>

The set of arguments for constructing a ActionCustom resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L91">property body</a>
</h3>

```typescript
body: pulumi.Input<string>;
```


Specifies the JSON Blob defining the Body of this Custom Action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L95">property logicAppId</a>
</h3>

```typescript
logicAppId: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ActionCustomState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L69">interface ActionCustomState</a>
</h2>

Input properties used for looking up and filtering ActionCustom resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L73">property body</a>
</h3>

```typescript
body?: pulumi.Input<string>;
```


Specifies the JSON Blob defining the Body of this Custom Action.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L77">property logicAppId</a>
</h3>

```typescript
logicAppId?: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionCustom.ts#L81">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ActionHttpArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L120">interface ActionHttpArgs</a>
</h2>

The set of arguments for constructing a ActionHttp resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L124">property body</a>
</h3>

```typescript
body?: pulumi.Input<string>;
```


Specifies the HTTP Body that should be sent to the `uri` when this HTTP Action is triggered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L128">property headers</a>
</h3>

```typescript
headers?: pulumi.Input<{ ... }>;
```


Specifies a Map of Key-Value Pairs that should be sent to the `uri` when this HTTP Action is triggered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L132">property logicAppId</a>
</h3>

```typescript
logicAppId: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L136">property method</a>
</h3>

```typescript
method: pulumi.Input<string>;
```


Specifies the HTTP Method which should be used for this HTTP Action. Possible values include `DELETE`, `GET`, `PATCH`, `POST` and `PUT`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L140">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L144">property uri</a>
</h3>

```typescript
uri: pulumi.Input<string>;
```


Specifies the URI which will be called when this HTTP Action is triggered.

<h2 class="pdoc-module-header" id="ActionHttpState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L90">interface ActionHttpState</a>
</h2>

Input properties used for looking up and filtering ActionHttp resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L94">property body</a>
</h3>

```typescript
body?: pulumi.Input<string>;
```


Specifies the HTTP Body that should be sent to the `uri` when this HTTP Action is triggered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L98">property headers</a>
</h3>

```typescript
headers?: pulumi.Input<{ ... }>;
```


Specifies a Map of Key-Value Pairs that should be sent to the `uri` when this HTTP Action is triggered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L102">property logicAppId</a>
</h3>

```typescript
logicAppId?: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L106">property method</a>
</h3>

```typescript
method?: pulumi.Input<string>;
```


Specifies the HTTP Method which should be used for this HTTP Action. Possible values include `DELETE`, `GET`, `PATCH`, `POST` and `PUT`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L110">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/actionHttp.ts#L114">property uri</a>
</h3>

```typescript
uri?: pulumi.Input<string>;
```


Specifies the URI which will be called when this HTTP Action is triggered.

<h2 class="pdoc-module-header" id="GetWorkflowArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L19">interface GetWorkflowArgs</a>
</h2>

A collection of arguments for invoking getWorkflow.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


The name of the Logic App Workflow.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The name of the Resource Group in which the Logic App Workflow exists.

<h2 class="pdoc-module-header" id="GetWorkflowResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L33">interface GetWorkflowResult</a>
</h2>

A collection of values returned by getWorkflow.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L37">property accessEndpoint</a>
</h3>

```typescript
accessEndpoint: string;
```


The Access Endpoint for the Logic App Workflow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L61">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L41">property location</a>
</h3>

```typescript
location: string;
```


The Azure location where the Logic App Workflow exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L45">property parameters</a>
</h3>

```typescript
parameters: { ... };
```


A map of Key-Value pairs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L49">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L53">property workflowSchema</a>
</h3>

```typescript
workflowSchema: string;
```


The Schema used for this Logic App Workflow.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/getWorkflow.ts#L57">property workflowVersion</a>
</h3>

```typescript
workflowVersion: string;
```


The version of the Schema used for this Logic App Workflow. Defaults to `1.0.0.0`.

<h2 class="pdoc-module-header" id="TriggerCustomArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L87">interface TriggerCustomArgs</a>
</h2>

The set of arguments for constructing a TriggerCustom resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L91">property body</a>
</h3>

```typescript
body: pulumi.Input<string>;
```


Specifies the JSON Blob defining the Body of this Custom Trigger.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L95">property logicAppId</a>
</h3>

```typescript
logicAppId: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the HTTP Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TriggerCustomState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L69">interface TriggerCustomState</a>
</h2>

Input properties used for looking up and filtering TriggerCustom resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L73">property body</a>
</h3>

```typescript
body?: pulumi.Input<string>;
```


Specifies the JSON Blob defining the Body of this Custom Trigger.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L77">property logicAppId</a>
</h3>

```typescript
logicAppId?: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerCustom.ts#L81">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the HTTP Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TriggerHttpRequestArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L107">interface TriggerHttpRequestArgs</a>
</h2>

The set of arguments for constructing a TriggerHttpRequest resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L111">property logicAppId</a>
</h3>

```typescript
logicAppId: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L115">property method</a>
</h3>

```typescript
method?: pulumi.Input<string>;
```


Specifies the HTTP Method which the request be using. Possible values include `DELETE`, `GET`, `PATCH`, `POST` or `PUT`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L119">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the HTTP Request Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L123">property relativePath</a>
</h3>

```typescript
relativePath?: pulumi.Input<string>;
```


Specifies the Relative Path used for this Request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L127">property schema</a>
</h3>

```typescript
schema: pulumi.Input<string>;
```


A JSON Blob defining the Schema of the incoming request. This needs to be valid JSON.

<h2 class="pdoc-module-header" id="TriggerHttpRequestState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L81">interface TriggerHttpRequestState</a>
</h2>

Input properties used for looking up and filtering TriggerHttpRequest resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L85">property logicAppId</a>
</h3>

```typescript
logicAppId?: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L89">property method</a>
</h3>

```typescript
method?: pulumi.Input<string>;
```


Specifies the HTTP Method which the request be using. Possible values include `DELETE`, `GET`, `PATCH`, `POST` or `PUT`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L93">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the HTTP Request Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L97">property relativePath</a>
</h3>

```typescript
relativePath?: pulumi.Input<string>;
```


Specifies the Relative Path used for this Request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerHttpRequest.ts#L101">property schema</a>
</h3>

```typescript
schema?: pulumi.Input<string>;
```


A JSON Blob defining the Schema of the incoming request. This needs to be valid JSON.

<h2 class="pdoc-module-header" id="TriggerRecurrenceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L100">interface TriggerRecurrenceArgs</a>
</h2>

The set of arguments for constructing a TriggerRecurrence resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L104">property frequency</a>
</h3>

```typescript
frequency: pulumi.Input<string>;
```


Specifies the Frequency at which this Trigger should be run. Possible values include `Month`, `Week`, `Day`, `Hour`, `Minute` and `Second`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L108">property interval</a>
</h3>

```typescript
interval: pulumi.Input<number>;
```


Specifies interval used for the Frequency, for example a value of `4` for `interval` and `hour` for `frequency` would run the Trigger every 4 hours.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L112">property logicAppId</a>
</h3>

```typescript
logicAppId: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L116">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Recurrence Triggers to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TriggerRecurrenceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L78">interface TriggerRecurrenceState</a>
</h2>

Input properties used for looking up and filtering TriggerRecurrence resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L82">property frequency</a>
</h3>

```typescript
frequency?: pulumi.Input<string>;
```


Specifies the Frequency at which this Trigger should be run. Possible values include `Month`, `Week`, `Day`, `Hour`, `Minute` and `Second`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L86">property interval</a>
</h3>

```typescript
interval?: pulumi.Input<number>;
```


Specifies interval used for the Frequency, for example a value of `4` for `interval` and `hour` for `frequency` would run the Trigger every 4 hours.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L90">property logicAppId</a>
</h3>

```typescript
logicAppId?: pulumi.Input<string>;
```


Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/triggerRecurrence.ts#L94">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Recurrence Triggers to be created within the Logic App Workflow. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="WorkflowArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L137">interface WorkflowArgs</a>
</h2>

The set of arguments for constructing a Workflow resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L141">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the Logic App Workflow exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L145">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L149">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


A map of Key-Value pairs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L153">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the Resource Group in which the Logic App Workflow should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L157">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L161">property workflowSchema</a>
</h3>

```typescript
workflowSchema?: pulumi.Input<string>;
```


Specifies the Schema to use for this Logic App Workflow. Defaults to `https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L165">property workflowVersion</a>
</h3>

```typescript
workflowVersion?: pulumi.Input<string>;
```


Specifies the version of the Schema used for this Logic App Workflow. Defaults to `1.0.0.0`. Changing this forces a new resource to be create.d

<h2 class="pdoc-module-header" id="WorkflowState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L99">interface WorkflowState</a>
</h2>

Input properties used for looking up and filtering Workflow resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L103">property accessEndpoint</a>
</h3>

```typescript
accessEndpoint?: pulumi.Input<string>;
```


The Access Endpoint for the Logic App Workflow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L107">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the Logic App Workflow exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L111">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Logic App Workflow. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L115">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


A map of Key-Value pairs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L119">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the Resource Group in which the Logic App Workflow should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L123">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L127">property workflowSchema</a>
</h3>

```typescript
workflowSchema?: pulumi.Input<string>;
```


Specifies the Schema to use for this Logic App Workflow. Defaults to `https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/logicapps/workflow.ts#L131">property workflowVersion</a>
</h3>

```typescript
workflowVersion?: pulumi.Input<string>;
```


Specifies the version of the Schema used for this Logic App Workflow. Defaults to `1.0.0.0`. Changing this forces a new resource to be create.d

