---
title: Module securitycenter
---

<a href="../index.html">@pulumi/azure</a> &gt; securitycenter

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Contact">class Contact</a>
* <a href="#SubscriptionPricing">class SubscriptionPricing</a>
* <a href="#Workspace">class Workspace</a>
* <a href="#ContactArgs">interface ContactArgs</a>
* <a href="#ContactState">interface ContactState</a>
* <a href="#SubscriptionPricingArgs">interface SubscriptionPricingArgs</a>
* <a href="#SubscriptionPricingState">interface SubscriptionPricingState</a>
* <a href="#WorkspaceArgs">interface WorkspaceArgs</a>
* <a href="#WorkspaceState">interface WorkspaceState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts">securitycenter/contact.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/subscriptionPricing.ts">securitycenter/subscriptionPricing.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/workspace.ts">securitycenter/workspace.ts</a> 


<h2 class="pdoc-module-header" id="Contact">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts#L12">class Contact</a>
</h2>

Manages the subscription's Security Center Contact.

~> **NOTE:** Owner access permission is required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts#L40">constructor</a>
</h3>

```typescript
new Contact(name: string, args: ContactArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Contact resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ContactState): Contact
```


Get an existing Contact resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts#L28">property alertNotifications</a>
</h3>

```typescript
public alertNotifications: pulumi.Output<boolean>;
```


Whether to send security alerts notifications to the security contact.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts#L32">property alertsToAdmins</a>
</h3>

```typescript
public alertsToAdmins: pulumi.Output<boolean>;
```


Whether to send security alerts notifications to subscription admins.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts#L36">property email</a>
</h3>

```typescript
public email: pulumi.Output<string>;
```


The email of the Security Center Contact.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts#L40">property phone</a>
</h3>

```typescript
public phone: pulumi.Output<string>;
```


The phone number of the Security Center Contact.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SubscriptionPricing">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/subscriptionPricing.ts#L14">class SubscriptionPricing</a>
</h2>

Manages the Pricing Tier for Azure Security Center in the current subscription.

~> **NOTE:** This resource requires the `Owner` permission on the Subscription.

~> **NOTE:** Deletion of this resource does not change or reset the pricing tier to `Free`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/subscriptionPricing.ts#L30">constructor</a>
</h3>

```typescript
new SubscriptionPricing(name: string, args: SubscriptionPricingArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SubscriptionPricing resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/subscriptionPricing.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubscriptionPricingState): SubscriptionPricing
```


Get an existing SubscriptionPricing resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/subscriptionPricing.ts#L30">property tier</a>
</h3>

```typescript
public tier: pulumi.Output<string>;
```


The pricing tier to use. Possible values are `Free` and `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Workspace">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/workspace.ts#L14">class Workspace</a>
</h2>

Manages the subscription's Security Center Workspace.

~> **NOTE:** Owner access permission is required.

~> **NOTE:** The subscription's pricing model can not be `Free` for this to have any affect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/workspace.ts#L34">constructor</a>
</h3>

```typescript
new Workspace(name: string, args: WorkspaceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Workspace resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/workspace.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WorkspaceState): Workspace
```


Get an existing Workspace resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/workspace.ts#L30">property scope</a>
</h3>

```typescript
public scope: pulumi.Output<string>;
```


The scope of VMs to send their security data to the desired workspace, unless overridden by a setting with more specific scope.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/workspace.ts#L34">property workspaceId</a>
</h3>

```typescript
public workspaceId: pulumi.Output<string>;
```


The ID of the Log Analytics Workspace to save the data in.

<h2 class="pdoc-module-header" id="ContactArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts#L106">interface ContactArgs</a>
</h2>

The set of arguments for constructing a Contact resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts#L110">property alertNotifications</a>
</h3>

```typescript
alertNotifications: pulumi.Input<boolean>;
```


Whether to send security alerts notifications to the security contact.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts#L114">property alertsToAdmins</a>
</h3>

```typescript
alertsToAdmins: pulumi.Input<boolean>;
```


Whether to send security alerts notifications to subscription admins.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts#L118">property email</a>
</h3>

```typescript
email: pulumi.Input<string>;
```


The email of the Security Center Contact.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts#L122">property phone</a>
</h3>

```typescript
phone: pulumi.Input<string>;
```


The phone number of the Security Center Contact.

<h2 class="pdoc-module-header" id="ContactState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts#L84">interface ContactState</a>
</h2>

Input properties used for looking up and filtering Contact resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts#L88">property alertNotifications</a>
</h3>

```typescript
alertNotifications?: pulumi.Input<boolean>;
```


Whether to send security alerts notifications to the security contact.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts#L92">property alertsToAdmins</a>
</h3>

```typescript
alertsToAdmins?: pulumi.Input<boolean>;
```


Whether to send security alerts notifications to subscription admins.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts#L96">property email</a>
</h3>

```typescript
email?: pulumi.Input<string>;
```


The email of the Security Center Contact.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/contact.ts#L100">property phone</a>
</h3>

```typescript
phone?: pulumi.Input<string>;
```


The phone number of the Security Center Contact.

<h2 class="pdoc-module-header" id="SubscriptionPricingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/subscriptionPricing.ts#L69">interface SubscriptionPricingArgs</a>
</h2>

The set of arguments for constructing a SubscriptionPricing resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/subscriptionPricing.ts#L73">property tier</a>
</h3>

```typescript
tier: pulumi.Input<string>;
```


The pricing tier to use. Possible values are `Free` and `Standard`.

<h2 class="pdoc-module-header" id="SubscriptionPricingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/subscriptionPricing.ts#L59">interface SubscriptionPricingState</a>
</h2>

Input properties used for looking up and filtering SubscriptionPricing resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/subscriptionPricing.ts#L63">property tier</a>
</h3>

```typescript
tier?: pulumi.Input<string>;
```


The pricing tier to use. Possible values are `Free` and `Standard`.

<h2 class="pdoc-module-header" id="WorkspaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/workspace.ts#L82">interface WorkspaceArgs</a>
</h2>

The set of arguments for constructing a Workspace resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/workspace.ts#L86">property scope</a>
</h3>

```typescript
scope: pulumi.Input<string>;
```


The scope of VMs to send their security data to the desired workspace, unless overridden by a setting with more specific scope.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/workspace.ts#L90">property workspaceId</a>
</h3>

```typescript
workspaceId: pulumi.Input<string>;
```


The ID of the Log Analytics Workspace to save the data in.

<h2 class="pdoc-module-header" id="WorkspaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/workspace.ts#L68">interface WorkspaceState</a>
</h2>

Input properties used for looking up and filtering Workspace resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/workspace.ts#L72">property scope</a>
</h3>

```typescript
scope?: pulumi.Input<string>;
```


The scope of VMs to send their security data to the desired workspace, unless overridden by a setting with more specific scope.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/securitycenter/workspace.ts#L76">property workspaceId</a>
</h3>

```typescript
workspaceId?: pulumi.Input<string>;
```


The ID of the Log Analytics Workspace to save the data in.

