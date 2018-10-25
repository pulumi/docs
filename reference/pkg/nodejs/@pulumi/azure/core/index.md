---
title: Module core
---

<a href="../index.html">@pulumi/azure</a> &gt; core

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ResourceGroup">class ResourceGroup</a>
* <a href="#TemplateDeployment">class TemplateDeployment</a>
* <a href="#getClientConfig">function getClientConfig</a>
* <a href="#getResourceGroup">function getResourceGroup</a>
* <a href="#getSubscription">function getSubscription</a>
* <a href="#getSubscriptions">function getSubscriptions</a>
* <a href="#GetClientConfigResult">interface GetClientConfigResult</a>
* <a href="#GetResourceGroupArgs">interface GetResourceGroupArgs</a>
* <a href="#GetResourceGroupResult">interface GetResourceGroupResult</a>
* <a href="#GetSubscriptionArgs">interface GetSubscriptionArgs</a>
* <a href="#GetSubscriptionResult">interface GetSubscriptionResult</a>
* <a href="#GetSubscriptionsResult">interface GetSubscriptionsResult</a>
* <a href="#ResourceGroupArgs">interface ResourceGroupArgs</a>
* <a href="#ResourceGroupState">interface ResourceGroupState</a>
* <a href="#TemplateDeploymentArgs">interface TemplateDeploymentArgs</a>
* <a href="#TemplateDeploymentState">interface TemplateDeploymentState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getClientConfig.ts">core/getClientConfig.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getResourceGroup.ts">core/getResourceGroup.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getSubscription.ts">core/getSubscription.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getSubscriptions.ts">core/getSubscriptions.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/resourceGroup.ts">core/resourceGroup.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts">core/templateDeployment.ts</a> 


<h2 class="pdoc-module-header" id="ResourceGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/resourceGroup.ts#L10">class ResourceGroup</a>
</h2>

Manages a resource group on Azure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/resourceGroup.ts#L36">constructor</a>
</h3>

```typescript
new ResourceGroup(name: string, args: ResourceGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ResourceGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/resourceGroup.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ResourceGroupState): ResourceGroup
```


Get an existing ResourceGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/resourceGroup.ts#L27">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location where the resource group should be created.
For a list of all Azure locations, please consult [this link](http://azure.microsoft.com/en-us/regions/) or run `az account list-locations --output table`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/resourceGroup.ts#L32">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the resource group. Must be unique on your
Azure subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/resourceGroup.ts#L36">property tags</a>
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

<h2 class="pdoc-module-header" id="TemplateDeployment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L14">class TemplateDeployment</a>
</h2>

Manage a template deployment of resources

~> **Note on ARM Template Deployments:** Due to the way the underlying Azure API is designed, Terraform can only manage the deployment of the ARM Template - and not any resources which are created by it.
This means that when deleting the `azurerm_template_deployment` resource, Terraform will only remove the reference to the deployment, whilst leaving any resources created by that ARM Template Deployment.
One workaround for this is to use a unique Resource Group for each ARM Template Deployment, which means deleting the Resource Group would contain any resources created within it - however this isn't ideal. [More information](https://docs.microsoft.com/en-us/rest/api/resources/deployments#Deployments_Delete).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L58">constructor</a>
</h3>

```typescript
new TemplateDeployment(name: string, args: TemplateDeploymentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TemplateDeployment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TemplateDeploymentState): TemplateDeployment
```


Get an existing TemplateDeployment resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L32">property deploymentMode</a>
</h3>

```typescript
public deploymentMode: pulumi.Output<string>;
```


Specifies the mode that is used to deploy resources. This value could be either `Incremental` or `Complete`.
Note that you will almost *always* want this to be set to `Incremental` otherwise the deployment will destroy all infrastructure not
specified within the template, and Terraform will not be aware of this.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the template deployment. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L41">property outputs</a>
</h3>

```typescript
public outputs: pulumi.Output<{ ... }>;
```


A map of supported scalar output types returned from the deployment (currently, Azure Template Deployment outputs of type String, Int and Bool are supported, and are converted to strings - others will be ignored) and can be accessed using `.outputs["name"]`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L45">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... } | undefined>;
```


Specifies the name and value pairs that define the deployment parameters for the template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L49">property parametersBody</a>
</h3>

```typescript
public parametersBody: pulumi.Output<string | undefined>;
```


Specifies a valid Azure JSON parameters file that define the deployment parameters. It can contain KeyVault references

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L54">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the template deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L58">property templateBody</a>
</h3>

```typescript
public templateBody: pulumi.Output<string>;
```


Specifies the JSON definition for the template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getClientConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getClientConfig.ts#L10">function getClientConfig</a>
</h2>

```typescript
getClientConfig(opts?: pulumi.InvokeOptions): Promise<GetClientConfigResult>
```


Use this data source to access the configuration of the AzureRM provider.

<h2 class="pdoc-module-header" id="getResourceGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getResourceGroup.ts#L10">function getResourceGroup</a>
</h2>

```typescript
getResourceGroup(args: GetResourceGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetResourceGroupResult>
```


Use this data source to access information about an existing Resource Group.

<h2 class="pdoc-module-header" id="getSubscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getSubscription.ts#L10">function getSubscription</a>
</h2>

```typescript
getSubscription(args?: GetSubscriptionArgs, opts?: pulumi.InvokeOptions): Promise<GetSubscriptionResult>
```


Use this data source to access information about an existing Subscription.

<h2 class="pdoc-module-header" id="getSubscriptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getSubscriptions.ts#L10">function getSubscriptions</a>
</h2>

```typescript
getSubscriptions(opts?: pulumi.InvokeOptions): Promise<GetSubscriptionsResult>
```


Use this data source to access information about all the Subscriptions currently available.

<h2 class="pdoc-module-header" id="GetClientConfigResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getClientConfig.ts#L18">interface GetClientConfigResult</a>
</h2>

A collection of values returned by getClientConfig.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getClientConfig.ts#L19">property clientId</a>
</h3>

```typescript
clientId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getClientConfig.ts#L27">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getClientConfig.ts#L20">property servicePrincipalApplicationId</a>
</h3>

```typescript
servicePrincipalApplicationId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getClientConfig.ts#L21">property servicePrincipalObjectId</a>
</h3>

```typescript
servicePrincipalObjectId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getClientConfig.ts#L22">property subscriptionId</a>
</h3>

```typescript
subscriptionId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getClientConfig.ts#L23">property tenantId</a>
</h3>

```typescript
tenantId: string;
```

<h2 class="pdoc-module-header" id="GetResourceGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getResourceGroup.ts#L19">interface GetResourceGroupArgs</a>
</h2>

A collection of arguments for invoking getResourceGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getResourceGroup.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the resource group.

<h2 class="pdoc-module-header" id="GetResourceGroupResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getResourceGroup.ts#L29">interface GetResourceGroupResult</a>
</h2>

A collection of values returned by getResourceGroup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getResourceGroup.ts#L41">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getResourceGroup.ts#L33">property location</a>
</h3>

```typescript
location: string;
```


The location of the resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getResourceGroup.ts#L37">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource group.

<h2 class="pdoc-module-header" id="GetSubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getSubscription.ts#L20">interface GetSubscriptionArgs</a>
</h2>

A collection of arguments for invoking getSubscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getSubscription.ts#L24">property subscriptionId</a>
</h3>

```typescript
subscriptionId?: string;
```


Specifies the ID of the subscription. If this argument is omitted, the subscription ID of the current Azure Resource Manager provider is used.

<h2 class="pdoc-module-header" id="GetSubscriptionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getSubscription.ts#L30">interface GetSubscriptionResult</a>
</h2>

A collection of values returned by getSubscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getSubscription.ts#L34">property displayName</a>
</h3>

```typescript
displayName: string;
```


The subscription display name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getSubscription.ts#L55">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getSubscription.ts#L38">property locationPlacementId</a>
</h3>

```typescript
locationPlacementId: string;
```


The subscription location placement ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getSubscription.ts#L42">property quotaId</a>
</h3>

```typescript
quotaId: string;
```


The subscription quota ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getSubscription.ts#L46">property spendingLimit</a>
</h3>

```typescript
spendingLimit: string;
```


The subscription spending limit.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getSubscription.ts#L50">property state</a>
</h3>

```typescript
state: string;
```


The subscription state. Possible values are Enabled, Warned, PastDue, Disabled, and Deleted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getSubscription.ts#L51">property subscriptionId</a>
</h3>

```typescript
subscriptionId: string;
```

<h2 class="pdoc-module-header" id="GetSubscriptionsResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getSubscriptions.ts#L18">interface GetSubscriptionsResult</a>
</h2>

A collection of values returned by getSubscriptions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getSubscriptions.ts#L26">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/getSubscriptions.ts#L22">property subscriptions</a>
</h3>

```typescript
subscriptions: { ... }[];
```


One or more `subscription` blocks as defined below.

<h2 class="pdoc-module-header" id="ResourceGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/resourceGroup.ts#L89">interface ResourceGroupArgs</a>
</h2>

The set of arguments for constructing a ResourceGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/resourceGroup.ts#L94">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location where the resource group should be created.
For a list of all Azure locations, please consult [this link](http://azure.microsoft.com/en-us/regions/) or run `az account list-locations --output table`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/resourceGroup.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the resource group. Must be unique on your
Azure subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/resourceGroup.ts#L103">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ResourceGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/resourceGroup.ts#L69">interface ResourceGroupState</a>
</h2>

Input properties used for looking up and filtering ResourceGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/resourceGroup.ts#L74">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location where the resource group should be created.
For a list of all Azure locations, please consult [this link](http://azure.microsoft.com/en-us/regions/) or run `az account list-locations --output table`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/resourceGroup.ts#L79">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the resource group. Must be unique on your
Azure subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/resourceGroup.ts#L83">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="TemplateDeploymentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L140">interface TemplateDeploymentArgs</a>
</h2>

The set of arguments for constructing a TemplateDeployment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L146">property deploymentMode</a>
</h3>

```typescript
deploymentMode: pulumi.Input<string>;
```


Specifies the mode that is used to deploy resources. This value could be either `Incremental` or `Complete`.
Note that you will almost *always* want this to be set to `Incremental` otherwise the deployment will destroy all infrastructure not
specified within the template, and Terraform will not be aware of this.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L151">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the template deployment. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L155">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


Specifies the name and value pairs that define the deployment parameters for the template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L159">property parametersBody</a>
</h3>

```typescript
parametersBody?: pulumi.Input<string>;
```


Specifies a valid Azure JSON parameters file that define the deployment parameters. It can contain KeyVault references

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L164">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the template deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L168">property templateBody</a>
</h3>

```typescript
templateBody?: pulumi.Input<string>;
```


Specifies the JSON definition for the template.

<h2 class="pdoc-module-header" id="TemplateDeploymentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L102">interface TemplateDeploymentState</a>
</h2>

Input properties used for looking up and filtering TemplateDeployment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L108">property deploymentMode</a>
</h3>

```typescript
deploymentMode?: pulumi.Input<string>;
```


Specifies the mode that is used to deploy resources. This value could be either `Incremental` or `Complete`.
Note that you will almost *always* want this to be set to `Incremental` otherwise the deployment will destroy all infrastructure not
specified within the template, and Terraform will not be aware of this.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L113">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the template deployment. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L117">property outputs</a>
</h3>

```typescript
outputs?: pulumi.Input<{ ... }>;
```


A map of supported scalar output types returned from the deployment (currently, Azure Template Deployment outputs of type String, Int and Bool are supported, and are converted to strings - others will be ignored) and can be accessed using `.outputs["name"]`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L121">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


Specifies the name and value pairs that define the deployment parameters for the template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L125">property parametersBody</a>
</h3>

```typescript
parametersBody?: pulumi.Input<string>;
```


Specifies a valid Azure JSON parameters file that define the deployment parameters. It can contain KeyVault references

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L130">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the template deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/core/templateDeployment.ts#L134">property templateBody</a>
</h3>

```typescript
templateBody?: pulumi.Input<string>;
```


Specifies the JSON definition for the template.

