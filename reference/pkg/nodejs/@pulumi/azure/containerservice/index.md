---
title: Module containerservice
---

<a href="../index.html">@pulumi/azure</a> &gt; containerservice

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Group">class Group</a>
* <a href="#KubernetesCluster">class KubernetesCluster</a>
* <a href="#Registry">class Registry</a>
* <a href="#Service">class Service</a>
* <a href="#getKubernetesCluster">function getKubernetesCluster</a>
* <a href="#getRegistry">function getRegistry</a>
* <a href="#GetKubernetesClusterArgs">interface GetKubernetesClusterArgs</a>
* <a href="#GetKubernetesClusterResult">interface GetKubernetesClusterResult</a>
* <a href="#GetRegistryArgs">interface GetRegistryArgs</a>
* <a href="#GetRegistryResult">interface GetRegistryResult</a>
* <a href="#GroupArgs">interface GroupArgs</a>
* <a href="#GroupState">interface GroupState</a>
* <a href="#KubernetesClusterArgs">interface KubernetesClusterArgs</a>
* <a href="#KubernetesClusterState">interface KubernetesClusterState</a>
* <a href="#RegistryArgs">interface RegistryArgs</a>
* <a href="#RegistryState">interface RegistryState</a>
* <a href="#ServiceArgs">interface ServiceArgs</a>
* <a href="#ServiceState">interface ServiceState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts">containerservice/getKubernetesCluster.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getRegistry.ts">containerservice/getRegistry.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts">containerservice/group.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts">containerservice/kubernetesCluster.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts">containerservice/registry.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts">containerservice/service.ts</a> 


<h2 class="pdoc-module-header" id="Group">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L7">class Group</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L31">constructor</a>
</h3>

```typescript
new Group(name: string, args: GroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Group resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L16">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupState): Group
```


Get an existing Group resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L20">property containers</a>
</h3>

```typescript
public containers: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L21">property dnsNameLabel</a>
</h3>

```typescript
public dnsNameLabel: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L22">property fqdn</a>
</h3>

```typescript
public fqdn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L23">property imageRegistryCredentials</a>
</h3>

```typescript
public imageRegistryCredentials: pulumi.Output<{ ... }[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L24">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L25">property ipAddressType</a>
</h3>

```typescript
public ipAddressType: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L26">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L27">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L28">property osType</a>
</h3>

```typescript
public osType: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L29">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L30">property restartPolicy</a>
</h3>

```typescript
public restartPolicy: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L31">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="KubernetesCluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L13">class KubernetesCluster</a>
</h2>

Manages a managed Kubernetes Cluster (AKS)

~> **Note:** All arguments including the client secret will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L92">constructor</a>
</h3>

```typescript
new KubernetesCluster(name: string, args: KubernetesClusterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a KubernetesCluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KubernetesClusterState): KubernetesCluster
```


Get an existing KubernetesCluster resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L29">property addonProfile</a>
</h3>

```typescript
public addonProfile: pulumi.Output<{ ... }>;
```


A `addon_profile` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L33">property agentPoolProfile</a>
</h3>

```typescript
public agentPoolProfile: pulumi.Output<{ ... }>;
```


One or more Agent Pool Profile's block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L37">property dnsPrefix</a>
</h3>

```typescript
public dnsPrefix: pulumi.Output<string>;
```


DNS prefix specified when creating the managed cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L41">property enableRbac</a>
</h3>

```typescript
public enableRbac: pulumi.Output<boolean | undefined>;
```


True or False. Enables or Disables Kubernetes Role Based Access Control (RBAC). Defaults to True. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L45">property fqdn</a>
</h3>

```typescript
public fqdn: pulumi.Output<string>;
```


The FQDN of the Azure Kubernetes Managed Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L49">property kubeConfig</a>
</h3>

```typescript
public kubeConfig: pulumi.Output<{ ... }>;
```


A `kube_config` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L55">property kubeConfigRaw</a>
</h3>

```typescript
public kubeConfigRaw: pulumi.Output<string>;
```


Raw Kubernetes config to be used by
[kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and
other compatible tools

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L59">property kubernetesVersion</a>
</h3>

```typescript
public kubernetesVersion: pulumi.Output<string>;
```


Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L63">property linuxProfile</a>
</h3>

```typescript
public linuxProfile: pulumi.Output<{ ... } | undefined>;
```


A Linux Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L67">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location where the AKS Managed Cluster instance should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L71">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the AKS Managed Cluster instance to create. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L76">property networkProfile</a>
</h3>

```typescript
public networkProfile: pulumi.Output<{ ... }>;
```


A Network Profile block as documented below.
-> **NOTE:** If `network_profile` is not defined, `kubenet` profile will be used by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L80">property nodeResourceGroup</a>
</h3>

```typescript
public nodeResourceGroup: pulumi.Output<string>;
```


Auto-generated Resource Group containing AKS Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L84">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L88">property servicePrincipal</a>
</h3>

```typescript
public servicePrincipal: pulumi.Output<{ ... }>;
```


A Service Principal block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L92">property tags</a>
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

<h2 class="pdoc-module-header" id="Registry">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L13">class Registry</a>
</h2>

Manages an Azure Container Registry.

~> **Note:** All arguments including the access key will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L66">constructor</a>
</h3>

```typescript
new Registry(name: string, args: RegistryArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Registry resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RegistryState): Registry
```


Get an existing Registry resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L29">property adminEnabled</a>
</h3>

```typescript
public adminEnabled: pulumi.Output<boolean | undefined>;
```


Specifies whether the admin user is enabled. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L33">property adminPassword</a>
</h3>

```typescript
public adminPassword: pulumi.Output<string>;
```


The Password associated with the Container Registry Admin account - if the admin account is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L37">property adminUsername</a>
</h3>

```typescript
public adminUsername: pulumi.Output<string>;
```


The Username associated with the Container Registry Admin account - if the admin account is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L41">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L45">property loginServer</a>
</h3>

```typescript
public loginServer: pulumi.Output<string>;
```


The URL that can be used to log into the container registry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L49">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Container Registry. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L53">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L57">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string | undefined>;
```


The SKU name of the the container registry. Possible values are `Classic` (which was previously `Basic`), `Basic`, `Standard` and `Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L58">property storageAccount</a>
</h3>

```typescript
public storageAccount: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L62">property storageAccountId</a>
</h3>

```typescript
public storageAccountId: pulumi.Output<string | undefined>;
```


The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L66">property tags</a>
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

<h2 class="pdoc-module-header" id="Service">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L57">class Service</a>
</h2>

Manages an Azure Container Service Instance

~> **Note:** All arguments including the client secret will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

## Example Usage (DCOS)

```hcl
resource "azurerm_resource_group" "test" {
  name     = "acctestRG1"
  location = "West US"
}

resource "azurerm_container_service" "test" {
  name                   = "acctestcontservice1"
  location               = "${azurerm_resource_group.test.location}"
  resource_group_name    = "${azurerm_resource_group.test.name}"
  orchestration_platform = "DCOS"

  master_profile {
    count      = 1
    dns_prefix = "acctestmaster1"
  }

  linux_profile {
    admin_username = "acctestuser1"

    ssh_key {
      key_data = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqaZoyiz1qbdOQ8xEf6uEu1cCwYowo5FHtsBhqLoDnnp7KUTEBN+L2NxRIfQ781rxV6Iq5jSav6b2Q8z5KiseOlvKA/RF2wqU0UPYqQviQhLmW6THTpmrv/YkUCuzxDpsH7DUDhZcwySLKVVe0Qm3+5N2Ta6UYH3lsDf9R9wTP2K/+vAnflKebuypNlmocIvakFWoZda18FOmsOoIVXQ8HWFNCuw9ZCunMSN62QGamCe3dL5cXlkgHYv7ekJE15IA9aOJcM7e90oeTqo+7HTcWfdu0qQqPWY5ujyMw/llas8tsXY85LFqRnr3gJ02bAscjc477+X+j/gkpFoN1QEmt terraform@demo.tld"
    }
  }

  agent_pool_profile {
    name       = "default"
    count      = 1
    dns_prefix = "acctestagent1"
    vm_size    = "Standard_F2"
  }

  diagnostics_profile {
    enabled = false
  }

  tags {
    Environment = "Production"
  }
}
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L109">constructor</a>
</h3>

```typescript
new Service(name: string, args: ServiceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Service resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L66">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServiceState): Service
```


Get an existing Service resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L73">property agentPoolProfile</a>
</h3>

```typescript
public agentPoolProfile: pulumi.Output<{ ... }>;
```


One or more Agent Pool Profile's block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L77">property diagnosticsProfile</a>
</h3>

```typescript
public diagnosticsProfile: pulumi.Output<{ ... }>;
```


A VM Diagnostics Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L81">property linuxProfile</a>
</h3>

```typescript
public linuxProfile: pulumi.Output<{ ... }>;
```


A Linux Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L85">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location where the Container Service instance should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L89">property masterProfile</a>
</h3>

```typescript
public masterProfile: pulumi.Output<{ ... }>;
```


A Master Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L93">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Unique name of the agent pool profile in the context of the subscription and resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L97">property orchestrationPlatform</a>
</h3>

```typescript
public orchestrationPlatform: pulumi.Output<string>;
```


Specifies the Container Orchestration Platform to use. Currently can be either `DCOS`, `Kubernetes` or `Swarm`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L101">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L105">property servicePrincipal</a>
</h3>

```typescript
public servicePrincipal: pulumi.Output<{ ... } | undefined>;
```


A Service Principal block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L109">property tags</a>
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

<h2 class="pdoc-module-header" id="getKubernetesCluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L14">function getKubernetesCluster</a>
</h2>

```typescript
getKubernetesCluster(args: GetKubernetesClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetKubernetesClusterResult>
```


Gets information about a managed Kubernetes Cluster (AKS)

~> **Note:** All arguments including the client secret will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).


<h2 class="pdoc-module-header" id="getRegistry">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getRegistry.ts#L10">function getRegistry</a>
</h2>

```typescript
getRegistry(args: GetRegistryArgs, opts?: pulumi.InvokeOptions): Promise<GetRegistryResult>
```


Use this data source to access information about a Container Registry

<h2 class="pdoc-module-header" id="GetKubernetesClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L24">interface GetKubernetesClusterArgs</a>
</h2>

A collection of arguments for invoking getKubernetesCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L28">property name</a>
</h3>

```typescript
name: string;
```


The name of the managed Kubernetes Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L32">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The name of the Resource Group in which the managed Kubernetes Cluster exists.

<h2 class="pdoc-module-header" id="GetKubernetesClusterResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L38">interface GetKubernetesClusterResult</a>
</h2>

A collection of values returned by getKubernetesCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L42">property addonProfiles</a>
</h3>

```typescript
addonProfiles: { ... }[];
```


A `addon_profile` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L46">property agentPoolProfiles</a>
</h3>

```typescript
agentPoolProfiles: { ... }[];
```


One or more `agent_profile_pool` blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L50">property dnsPrefix</a>
</h3>

```typescript
dnsPrefix: string;
```


The DNS Prefix of the managed Kubernetes cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L54">property fqdn</a>
</h3>

```typescript
fqdn: string;
```


The FQDN of the Azure Kubernetes Managed Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L94">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L62">property kubeConfigRaw</a>
</h3>

```typescript
kubeConfigRaw: string;
```


Base64 encoded Kubernetes configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L58">property kubeConfigs</a>
</h3>

```typescript
kubeConfigs: { ... }[];
```


A `kube_config` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L66">property kubernetesVersion</a>
</h3>

```typescript
kubernetesVersion: string;
```


The version of Kubernetes used on the managed Kubernetes Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L70">property linuxProfiles</a>
</h3>

```typescript
linuxProfiles: { ... }[];
```


A `linux_profile` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L74">property location</a>
</h3>

```typescript
location: string;
```


The Azure Region in which the managed Kubernetes Cluster exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L78">property networkProfiles</a>
</h3>

```typescript
networkProfiles: { ... }[];
```


A `network_profile` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L82">property nodeResourceGroup</a>
</h3>

```typescript
nodeResourceGroup: string;
```


Auto-generated Resource Group containing AKS Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L86">property servicePrincipals</a>
</h3>

```typescript
servicePrincipals: { ... }[];
```


A `service_principal` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L90">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to this resource.

<h2 class="pdoc-module-header" id="GetRegistryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getRegistry.ts#L20">interface GetRegistryArgs</a>
</h2>

A collection of arguments for invoking getRegistry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getRegistry.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


The name of the Container Registry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getRegistry.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The Name of the Resource Group where this Container Registry exists.

<h2 class="pdoc-module-header" id="GetRegistryResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getRegistry.ts#L34">interface GetRegistryResult</a>
</h2>

A collection of values returned by getRegistry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getRegistry.ts#L38">property adminEnabled</a>
</h3>

```typescript
adminEnabled: boolean;
```


Is the Administrator account enabled for this Container Registry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getRegistry.ts#L42">property adminPassword</a>
</h3>

```typescript
adminPassword: string;
```


The Password associated with the Container Registry Admin account - if the admin account is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getRegistry.ts#L46">property adminUsername</a>
</h3>

```typescript
adminUsername: string;
```


The Username associated with the Container Registry Admin account - if the admin account is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getRegistry.ts#L66">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getRegistry.ts#L50">property location</a>
</h3>

```typescript
location: string;
```


The Azure Region in which this Container Registry exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getRegistry.ts#L54">property loginServer</a>
</h3>

```typescript
loginServer: string;
```


The URL that can be used to log into the container registry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getRegistry.ts#L58">property sku</a>
</h3>

```typescript
sku: string;
```


The SKU of this Container Registry, such as `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getRegistry.ts#L62">property storageAccountId</a>
</h3>

```typescript
storageAccountId: string;
```


The ID of the Storage Account used for this Container Registry. This is only returned for `Classic` SKU's.

<h2 class="pdoc-module-header" id="GroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L109">interface GroupArgs</a>
</h2>

The set of arguments for constructing a Group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L110">property containers</a>
</h3>

```typescript
containers: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L111">property dnsNameLabel</a>
</h3>

```typescript
dnsNameLabel?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L112">property imageRegistryCredentials</a>
</h3>

```typescript
imageRegistryCredentials?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L113">property ipAddressType</a>
</h3>

```typescript
ipAddressType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L114">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L115">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L116">property osType</a>
</h3>

```typescript
osType: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L117">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L118">property restartPolicy</a>
</h3>

```typescript
restartPolicy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L119">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="GroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L91">interface GroupState</a>
</h2>

Input properties used for looking up and filtering Group resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L92">property containers</a>
</h3>

```typescript
containers?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L93">property dnsNameLabel</a>
</h3>

```typescript
dnsNameLabel?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L94">property fqdn</a>
</h3>

```typescript
fqdn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L95">property imageRegistryCredentials</a>
</h3>

```typescript
imageRegistryCredentials?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L96">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L97">property ipAddressType</a>
</h3>

```typescript
ipAddressType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L98">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L100">property osType</a>
</h3>

```typescript
osType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L101">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L102">property restartPolicy</a>
</h3>

```typescript
restartPolicy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L103">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="KubernetesClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L236">interface KubernetesClusterArgs</a>
</h2>

The set of arguments for constructing a KubernetesCluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L240">property addonProfile</a>
</h3>

```typescript
addonProfile?: pulumi.Input<{ ... }>;
```


A `addon_profile` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L244">property agentPoolProfile</a>
</h3>

```typescript
agentPoolProfile: pulumi.Input<{ ... }>;
```


One or more Agent Pool Profile's block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L248">property dnsPrefix</a>
</h3>

```typescript
dnsPrefix: pulumi.Input<string>;
```


DNS prefix specified when creating the managed cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L252">property enableRbac</a>
</h3>

```typescript
enableRbac?: pulumi.Input<boolean>;
```


True or False. Enables or Disables Kubernetes Role Based Access Control (RBAC). Defaults to True. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L256">property kubernetesVersion</a>
</h3>

```typescript
kubernetesVersion?: pulumi.Input<string>;
```


Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L260">property linuxProfile</a>
</h3>

```typescript
linuxProfile?: pulumi.Input<{ ... }>;
```


A Linux Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L264">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location where the AKS Managed Cluster instance should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L268">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the AKS Managed Cluster instance to create. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L273">property networkProfile</a>
</h3>

```typescript
networkProfile?: pulumi.Input<{ ... }>;
```


A Network Profile block as documented below.
-> **NOTE:** If `network_profile` is not defined, `kubenet` profile will be used by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L277">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L281">property servicePrincipal</a>
</h3>

```typescript
servicePrincipal: pulumi.Input<{ ... }>;
```


A Service Principal block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L285">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="KubernetesClusterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L163">interface KubernetesClusterState</a>
</h2>

Input properties used for looking up and filtering KubernetesCluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L167">property addonProfile</a>
</h3>

```typescript
addonProfile?: pulumi.Input<{ ... }>;
```


A `addon_profile` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L171">property agentPoolProfile</a>
</h3>

```typescript
agentPoolProfile?: pulumi.Input<{ ... }>;
```


One or more Agent Pool Profile's block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L175">property dnsPrefix</a>
</h3>

```typescript
dnsPrefix?: pulumi.Input<string>;
```


DNS prefix specified when creating the managed cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L179">property enableRbac</a>
</h3>

```typescript
enableRbac?: pulumi.Input<boolean>;
```


True or False. Enables or Disables Kubernetes Role Based Access Control (RBAC). Defaults to True. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L183">property fqdn</a>
</h3>

```typescript
fqdn?: pulumi.Input<string>;
```


The FQDN of the Azure Kubernetes Managed Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L187">property kubeConfig</a>
</h3>

```typescript
kubeConfig?: pulumi.Input<{ ... }>;
```


A `kube_config` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L193">property kubeConfigRaw</a>
</h3>

```typescript
kubeConfigRaw?: pulumi.Input<string>;
```


Raw Kubernetes config to be used by
[kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and
other compatible tools

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L197">property kubernetesVersion</a>
</h3>

```typescript
kubernetesVersion?: pulumi.Input<string>;
```


Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L201">property linuxProfile</a>
</h3>

```typescript
linuxProfile?: pulumi.Input<{ ... }>;
```


A Linux Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L205">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location where the AKS Managed Cluster instance should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L209">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the AKS Managed Cluster instance to create. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L214">property networkProfile</a>
</h3>

```typescript
networkProfile?: pulumi.Input<{ ... }>;
```


A Network Profile block as documented below.
-> **NOTE:** If `network_profile` is not defined, `kubenet` profile will be used by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L218">property nodeResourceGroup</a>
</h3>

```typescript
nodeResourceGroup?: pulumi.Input<string>;
```


Auto-generated Resource Group containing AKS Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L222">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L226">property servicePrincipal</a>
</h3>

```typescript
servicePrincipal?: pulumi.Input<{ ... }>;
```


A Service Principal block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L230">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="RegistryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L165">interface RegistryArgs</a>
</h2>

The set of arguments for constructing a Registry resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L169">property adminEnabled</a>
</h3>

```typescript
adminEnabled?: pulumi.Input<boolean>;
```


Specifies whether the admin user is enabled. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L173">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L177">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Container Registry. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L181">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L185">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


The SKU name of the the container registry. Possible values are `Classic` (which was previously `Basic`), `Basic`, `Standard` and `Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L186">property storageAccount</a>
</h3>

```typescript
storageAccount?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L190">property storageAccountId</a>
</h3>

```typescript
storageAccountId?: pulumi.Input<string>;
```


The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L194">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="RegistryState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L118">interface RegistryState</a>
</h2>

Input properties used for looking up and filtering Registry resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L122">property adminEnabled</a>
</h3>

```typescript
adminEnabled?: pulumi.Input<boolean>;
```


Specifies whether the admin user is enabled. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L126">property adminPassword</a>
</h3>

```typescript
adminPassword?: pulumi.Input<string>;
```


The Password associated with the Container Registry Admin account - if the admin account is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L130">property adminUsername</a>
</h3>

```typescript
adminUsername?: pulumi.Input<string>;
```


The Username associated with the Container Registry Admin account - if the admin account is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L134">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L138">property loginServer</a>
</h3>

```typescript
loginServer?: pulumi.Input<string>;
```


The URL that can be used to log into the container registry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L142">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Container Registry. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L146">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L150">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


The SKU name of the the container registry. Possible values are `Classic` (which was previously `Basic`), `Basic`, `Standard` and `Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L151">property storageAccount</a>
</h3>

```typescript
storageAccount?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L155">property storageAccountId</a>
</h3>

```typescript
storageAccountId?: pulumi.Input<string>;
```


The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L159">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ServiceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L220">interface ServiceArgs</a>
</h2>

The set of arguments for constructing a Service resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L224">property agentPoolProfile</a>
</h3>

```typescript
agentPoolProfile: pulumi.Input<{ ... }>;
```


One or more Agent Pool Profile's block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L228">property diagnosticsProfile</a>
</h3>

```typescript
diagnosticsProfile: pulumi.Input<{ ... }>;
```


A VM Diagnostics Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L232">property linuxProfile</a>
</h3>

```typescript
linuxProfile: pulumi.Input<{ ... }>;
```


A Linux Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L236">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location where the Container Service instance should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L240">property masterProfile</a>
</h3>

```typescript
masterProfile: pulumi.Input<{ ... }>;
```


A Master Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L244">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Unique name of the agent pool profile in the context of the subscription and resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L248">property orchestrationPlatform</a>
</h3>

```typescript
orchestrationPlatform: pulumi.Input<string>;
```


Specifies the Container Orchestration Platform to use. Currently can be either `DCOS`, `Kubernetes` or `Swarm`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L252">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L256">property servicePrincipal</a>
</h3>

```typescript
servicePrincipal?: pulumi.Input<{ ... }>;
```


A Service Principal block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L260">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ServiceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L174">interface ServiceState</a>
</h2>

Input properties used for looking up and filtering Service resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L178">property agentPoolProfile</a>
</h3>

```typescript
agentPoolProfile?: pulumi.Input<{ ... }>;
```


One or more Agent Pool Profile's block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L182">property diagnosticsProfile</a>
</h3>

```typescript
diagnosticsProfile?: pulumi.Input<{ ... }>;
```


A VM Diagnostics Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L186">property linuxProfile</a>
</h3>

```typescript
linuxProfile?: pulumi.Input<{ ... }>;
```


A Linux Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L190">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location where the Container Service instance should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L194">property masterProfile</a>
</h3>

```typescript
masterProfile?: pulumi.Input<{ ... }>;
```


A Master Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L198">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Unique name of the agent pool profile in the context of the subscription and resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L202">property orchestrationPlatform</a>
</h3>

```typescript
orchestrationPlatform?: pulumi.Input<string>;
```


Specifies the Container Orchestration Platform to use. Currently can be either `DCOS`, `Kubernetes` or `Swarm`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L206">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L210">property servicePrincipal</a>
</h3>

```typescript
servicePrincipal?: pulumi.Input<{ ... }>;
```


A Service Principal block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L214">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

