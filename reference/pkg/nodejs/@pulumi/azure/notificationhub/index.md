---
title: Module notificationhub
---

<a href="../index.html">@pulumi/azure</a> &gt; notificationhub

<h2 class="pdoc-module-header">Index</h2>

* <a href="#AuthorizationRule">class AuthorizationRule</a>
* <a href="#Hub">class Hub</a>
* <a href="#Namespace">class Namespace</a>
* <a href="#getHub">function getHub</a>
* <a href="#getNamespace">function getNamespace</a>
* <a href="#AuthorizationRuleArgs">interface AuthorizationRuleArgs</a>
* <a href="#AuthorizationRuleState">interface AuthorizationRuleState</a>
* <a href="#GetHubArgs">interface GetHubArgs</a>
* <a href="#GetHubResult">interface GetHubResult</a>
* <a href="#GetNamespaceArgs">interface GetNamespaceArgs</a>
* <a href="#GetNamespaceResult">interface GetNamespaceResult</a>
* <a href="#HubArgs">interface HubArgs</a>
* <a href="#HubState">interface HubState</a>
* <a href="#NamespaceArgs">interface NamespaceArgs</a>
* <a href="#NamespaceState">interface NamespaceState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts">notificationhub/authorizationRule.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getHub.ts">notificationhub/getHub.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getNamespace.ts">notificationhub/getNamespace.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts">notificationhub/hub.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts">notificationhub/namespace.ts</a> 


<h2 class="pdoc-module-header" id="AuthorizationRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L9">class AuthorizationRule</a>
</h2>

Manages an Authorization Rule associated with a Notification Hub within a Notification Hub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L57">constructor</a>
</h3>

```typescript
new AuthorizationRule(name: string, args: AuthorizationRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AuthorizationRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AuthorizationRuleState): AuthorizationRule
```


Get an existing AuthorizationRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L25">property listen</a>
</h3>

```typescript
public listen: pulumi.Output<boolean | undefined>;
```


Does this Authorization Rule have Listen access to the Notification Hub? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L29">property manage</a>
</h3>

```typescript
public manage: pulumi.Output<boolean | undefined>;
```


Does this Authorization Rule have Manage access to the Notification Hub? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name to use for this Authorization Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L37">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


The name of the Notification Hub Namespace in which the Notification Hub exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L41">property notificationHubName</a>
</h3>

```typescript
public notificationHubName: pulumi.Output<string>;
```


The name of the Notification Hub for which the Authorization Rule should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L45">property primaryAccessKey</a>
</h3>

```typescript
public primaryAccessKey: pulumi.Output<string>;
```


The Primary Access Key associated with this Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L49">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L53">property secondaryAccessKey</a>
</h3>

```typescript
public secondaryAccessKey: pulumi.Output<string>;
```


The Secondary Access Key associated with this Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L57">property send</a>
</h3>

```typescript
public send: pulumi.Output<boolean | undefined>;
```


Does this Authorization Rule have Send access to the Notification Hub? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Hub">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L9">class Hub</a>
</h2>

Manages a Notification Hub within a Notification Hub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L45">constructor</a>
</h3>

```typescript
new Hub(name: string, args: HubArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Hub resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HubState): Hub
```


Get an existing Hub resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L25">property apnsCredential</a>
</h3>

```typescript
public apnsCredential: pulumi.Output<{ ... } | undefined>;
```


A `apns_credential` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L29">property gcmCredential</a>
</h3>

```typescript
public gcmCredential: pulumi.Output<{ ... } | undefined>;
```


A `gcm_credential` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L33">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The Azure Region in which this Notification Hub Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name to use for this Notification Hub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L41">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


The name of the Notification Hub Namespace in which to create this Notification Hub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L45">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Namespace">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L9">class Namespace</a>
</h2>

Manages a Notification Hub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L49">constructor</a>
</h3>

```typescript
new Namespace(name: string, args: NamespaceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Namespace resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NamespaceState): Namespace
```


Get an existing Namespace resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L25">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Is this Notification Hub Namespace enabled? Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L29">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The Azure Region in which this Notification Hub Namespace should be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the SKU to use for this Notification Hub Namespace. Possible values are `Free`, `Basic` or `Standard`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L37">property namespaceType</a>
</h3>

```typescript
public namespaceType: pulumi.Output<string>;
```


The Type of Namespace - possible values are `Messaging` or `NotificationHub`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L41">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the Resource Group in which the Notification Hub Namespace should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L45">property servicebusEndpoint</a>
</h3>

```typescript
public servicebusEndpoint: pulumi.Output<string>;
```


The ServiceBus Endpoint for this Notification Hub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L49">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getHub">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getHub.ts#L9">function getHub</a>
</h2>

```typescript
getHub(args: GetHubArgs, opts?: pulumi.InvokeOptions): Promise<GetHubResult>
```


Gets information about the specified Notification Hub within a Notification Hub Namespace.

<h2 class="pdoc-module-header" id="getNamespace">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getNamespace.ts#L9">function getNamespace</a>
</h2>

```typescript
getNamespace(args: GetNamespaceArgs, opts?: pulumi.InvokeOptions): Promise<GetNamespaceResult>
```


Gets information about the specified Notification Hub Namespace.

<h2 class="pdoc-module-header" id="AuthorizationRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L150">interface AuthorizationRuleArgs</a>
</h2>

The set of arguments for constructing a AuthorizationRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L154">property listen</a>
</h3>

```typescript
listen?: pulumi.Input<boolean>;
```


Does this Authorization Rule have Listen access to the Notification Hub? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L158">property manage</a>
</h3>

```typescript
manage?: pulumi.Input<boolean>;
```


Does this Authorization Rule have Manage access to the Notification Hub? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L162">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to use for this Authorization Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L166">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


The name of the Notification Hub Namespace in which the Notification Hub exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L170">property notificationHubName</a>
</h3>

```typescript
notificationHubName: pulumi.Input<string>;
```


The name of the Notification Hub for which the Authorization Rule should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L174">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L178">property send</a>
</h3>

```typescript
send?: pulumi.Input<boolean>;
```


Does this Authorization Rule have Send access to the Notification Hub? Defaults to `false`.

<h2 class="pdoc-module-header" id="AuthorizationRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L108">interface AuthorizationRuleState</a>
</h2>

Input properties used for looking up and filtering AuthorizationRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L112">property listen</a>
</h3>

```typescript
listen?: pulumi.Input<boolean>;
```


Does this Authorization Rule have Listen access to the Notification Hub? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L116">property manage</a>
</h3>

```typescript
manage?: pulumi.Input<boolean>;
```


Does this Authorization Rule have Manage access to the Notification Hub? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L120">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to use for this Authorization Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L124">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


The name of the Notification Hub Namespace in which the Notification Hub exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L128">property notificationHubName</a>
</h3>

```typescript
notificationHubName?: pulumi.Input<string>;
```


The name of the Notification Hub for which the Authorization Rule should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L132">property primaryAccessKey</a>
</h3>

```typescript
primaryAccessKey?: pulumi.Input<string>;
```


The Primary Access Key associated with this Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L136">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L140">property secondaryAccessKey</a>
</h3>

```typescript
secondaryAccessKey?: pulumi.Input<string>;
```


The Secondary Access Key associated with this Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/authorizationRule.ts#L144">property send</a>
</h3>

```typescript
send?: pulumi.Input<boolean>;
```


Does this Authorization Rule have Send access to the Notification Hub? Defaults to `false`.

<h2 class="pdoc-module-header" id="GetHubArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getHub.ts#L20">interface GetHubArgs</a>
</h2>

A collection of arguments for invoking getHub.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getHub.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


Specifies the Name of the Notification Hub.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getHub.ts#L28">property namespaceName</a>
</h3>

```typescript
namespaceName: string;
```


Specifies the Name of the Notification Hub Namespace which contains the Notification Hub.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getHub.ts#L32">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the Name of the Resource Group within which the Notification Hub exists.

<h2 class="pdoc-module-header" id="GetHubResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getHub.ts#L38">interface GetHubResult</a>
</h2>

A collection of values returned by getHub.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getHub.ts#L42">property apnsCredentials</a>
</h3>

```typescript
apnsCredentials: { ... }[];
```


A `apns_credential` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getHub.ts#L46">property gcmCredentials</a>
</h3>

```typescript
gcmCredentials: { ... }[];
```


A `gcm_credential` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getHub.ts#L54">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getHub.ts#L50">property location</a>
</h3>

```typescript
location: string;
```


The Azure Region in which this Notification Hub exists.

<h2 class="pdoc-module-header" id="GetNamespaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getNamespace.ts#L19">interface GetNamespaceArgs</a>
</h2>

A collection of arguments for invoking getNamespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getNamespace.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


Specifies the Name of the Notification Hub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getNamespace.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the Name of the Resource Group within which the Notification Hub exists.

<h2 class="pdoc-module-header" id="GetNamespaceResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getNamespace.ts#L33">interface GetNamespaceResult</a>
</h2>

A collection of values returned by getNamespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getNamespace.ts#L37">property enabled</a>
</h3>

```typescript
enabled: boolean;
```


Is this Notification Hub Namespace enabled?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getNamespace.ts#L54">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getNamespace.ts#L41">property location</a>
</h3>

```typescript
location: string;
```


The Azure Region in which this Notification Hub Namespace exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getNamespace.ts#L45">property namespaceType</a>
</h3>

```typescript
namespaceType: string;
```


The Type of Namespace, such as `Messaging` or `NotificationHub`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getNamespace.ts#L46">property servicebusEndpoint</a>
</h3>

```typescript
servicebusEndpoint: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/getNamespace.ts#L50">property sku</a>
</h3>

```typescript
sku: { ... };
```


A `sku` block as defined below.

<h2 class="pdoc-module-header" id="HubArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L120">interface HubArgs</a>
</h2>

The set of arguments for constructing a Hub resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L124">property apnsCredential</a>
</h3>

```typescript
apnsCredential?: pulumi.Input<{ ... }>;
```


A `apns_credential` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L128">property gcmCredential</a>
</h3>

```typescript
gcmCredential?: pulumi.Input<{ ... }>;
```


A `gcm_credential` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L132">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The Azure Region in which this Notification Hub Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L136">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to use for this Notification Hub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L140">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


The name of the Notification Hub Namespace in which to create this Notification Hub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L144">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="HubState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L90">interface HubState</a>
</h2>

Input properties used for looking up and filtering Hub resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L94">property apnsCredential</a>
</h3>

```typescript
apnsCredential?: pulumi.Input<{ ... }>;
```


A `apns_credential` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L98">property gcmCredential</a>
</h3>

```typescript
gcmCredential?: pulumi.Input<{ ... }>;
```


A `gcm_credential` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L102">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The Azure Region in which this Notification Hub Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L106">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name to use for this Notification Hub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L110">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


The name of the Notification Hub Namespace in which to create this Notification Hub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/hub.ts#L114">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the Resource Group in which the Notification Hub Namespace exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="NamespaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L133">interface NamespaceArgs</a>
</h2>

The set of arguments for constructing a Namespace resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L137">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Is this Notification Hub Namespace enabled? Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L141">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The Azure Region in which this Notification Hub Namespace should be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L145">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the SKU to use for this Notification Hub Namespace. Possible values are `Free`, `Basic` or `Standard`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L149">property namespaceType</a>
</h3>

```typescript
namespaceType: pulumi.Input<string>;
```


The Type of Namespace - possible values are `Messaging` or `NotificationHub`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L153">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the Resource Group in which the Notification Hub Namespace should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L157">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

<h2 class="pdoc-module-header" id="NamespaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L99">interface NamespaceState</a>
</h2>

Input properties used for looking up and filtering Namespace resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L103">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Is this Notification Hub Namespace enabled? Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L107">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The Azure Region in which this Notification Hub Namespace should be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L111">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the SKU to use for this Notification Hub Namespace. Possible values are `Free`, `Basic` or `Standard`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L115">property namespaceType</a>
</h3>

```typescript
namespaceType?: pulumi.Input<string>;
```


The Type of Namespace - possible values are `Messaging` or `NotificationHub`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L119">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the Resource Group in which the Notification Hub Namespace should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L123">property servicebusEndpoint</a>
</h3>

```typescript
servicebusEndpoint?: pulumi.Input<string>;
```


The ServiceBus Endpoint for this Notification Hub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/notificationhub/namespace.ts#L127">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

