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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L10">class Group</a>
</h2>

Manage as an Azure Container Group instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L67">constructor</a>
</h3>

```typescript
new Group(name: string, args: GroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Group resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L26">property containers</a>
</h3>

```typescript
public containers: pulumi.Output<{ ... }[]>;
```


The definition of a container that is part of the group as documented in the `container` block below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L30">property dnsNameLabel</a>
</h3>

```typescript
public dnsNameLabel: pulumi.Output<string | undefined>;
```


The DNS label/name for the container groups IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L34">property fqdn</a>
</h3>

```typescript
public fqdn: pulumi.Output<string>;
```


The FQDN of the container group derived from `dns_name_label`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L38">property imageRegistryCredentials</a>
</h3>

```typescript
public imageRegistryCredentials: pulumi.Output<{ ... }[] | undefined>;
```


Set image registry credentials for the group as documented in the `image_registry_credential` block below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L42">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string>;
```


The IP address allocated to the container group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L46">property ipAddressType</a>
</h3>

```typescript
public ipAddressType: pulumi.Output<string | undefined>;
```


Specifies the ip address type of the container. `Public` is the only acceptable value at this time. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L50">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L54">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Container Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L58">property osType</a>
</h3>

```typescript
public osType: pulumi.Output<string>;
```


The OS for the container group. Allowed values are `Linux` and `Windows`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L62">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Container Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L66">property restartPolicy</a>
</h3>

```typescript
public restartPolicy: pulumi.Output<string | undefined>;
```


Restart policy for the container group. Allowed values are `Always`, `Never`, `OnFailure`. Defaults to `Always`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L67">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L12">class KubernetesCluster</a>
</h2>

Manages a Managed Kubernetes Cluster (also known as AKS / Azure Kubernetes Service)

~> **Note:** All arguments including the client secret will be stored in the raw state as plain-text. [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L88">constructor</a>
</h3>

```typescript
new KubernetesCluster(name: string, args: KubernetesClusterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a KubernetesCluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L21">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L28">property addonProfile</a>
</h3>

```typescript
public addonProfile: pulumi.Output<{ ... }>;
```


A `addon_profile` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L32">property agentPoolProfile</a>
</h3>

```typescript
public agentPoolProfile: pulumi.Output<{ ... }>;
```


One or more `agent_pool_profile` blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L36">property dnsPrefix</a>
</h3>

```typescript
public dnsPrefix: pulumi.Output<string>;
```


DNS prefix specified when creating the managed cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L40">property fqdn</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L44">property kubeConfig</a>
</h3>

```typescript
public kubeConfig: pulumi.Output<{ ... }>;
```


A `kube_config` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L48">property kubeConfigRaw</a>
</h3>

```typescript
public kubeConfigRaw: pulumi.Output<string>;
```


Raw Kubernetes config to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L52">property kubernetesVersion</a>
</h3>

```typescript
public kubernetesVersion: pulumi.Output<string>;
```


Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L56">property linuxProfile</a>
</h3>

```typescript
public linuxProfile: pulumi.Output<{ ... } | undefined>;
```


A `linux_profile` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L60">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L64">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L68">property networkProfile</a>
</h3>

```typescript
public networkProfile: pulumi.Output<{ ... }>;
```


A `network_profile` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L72">property nodeResourceGroup</a>
</h3>

```typescript
public nodeResourceGroup: pulumi.Output<string>;
```


The auto-generated Resource Group which contains the resources for this Managed Kubernetes Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L76">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L80">property roleBasedAccessControl</a>
</h3>

```typescript
public roleBasedAccessControl: pulumi.Output<{ ... } | undefined>;
```


A `role_based_access_control` block. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L84">property servicePrincipal</a>
</h3>

```typescript
public servicePrincipal: pulumi.Output<{ ... }>;
```


A `service_principal` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L88">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L59">class Service</a>
</h2>

Manages an Azure Container Service Instance

~> **NOTE:** All arguments including the client secret will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

~> **NOTE:** You may wish to consider using Azure Kubernetes Service (AKS) for new deployments.

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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L111">constructor</a>
</h3>

```typescript
new Service(name: string, args: ServiceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Service resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L68">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L75">property agentPoolProfile</a>
</h3>

```typescript
public agentPoolProfile: pulumi.Output<{ ... }>;
```


One or more Agent Pool Profile's block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L79">property diagnosticsProfile</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L83">property linuxProfile</a>
</h3>

```typescript
public linuxProfile: pulumi.Output<{ ... }>;
```


A Linux Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L87">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location where the Container Service instance should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L91">property masterProfile</a>
</h3>

```typescript
public masterProfile: pulumi.Output<{ ... }>;
```


A Master Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L95">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Unique name of the agent pool profile in the context of the subscription and resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L99">property orchestrationPlatform</a>
</h3>

```typescript
public orchestrationPlatform: pulumi.Output<string>;
```


Specifies the Container Orchestration Platform to use. Currently can be either `DCOS`, `Kubernetes` or `Swarm`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L103">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L107">property servicePrincipal</a>
</h3>

```typescript
public servicePrincipal: pulumi.Output<{ ... } | undefined>;
```


A Service Principal block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L111">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L13">function getKubernetesCluster</a>
</h2>

```typescript
getKubernetesCluster(args: GetKubernetesClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetKubernetesClusterResult>
```


Use this data source to access information about an existing Managed Kubernetes Cluster (AKS).

~> **Note:** All arguments including the client secret will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

<h2 class="pdoc-module-header" id="getRegistry">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getRegistry.ts#L10">function getRegistry</a>
</h2>

```typescript
getRegistry(args: GetRegistryArgs, opts?: pulumi.InvokeOptions): Promise<GetRegistryResult>
```


Use this data source to access information about an existing Container Registry.

<h2 class="pdoc-module-header" id="GetKubernetesClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L23">interface GetKubernetesClusterArgs</a>
</h2>

A collection of arguments for invoking getKubernetesCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L27">property name</a>
</h3>

```typescript
name: string;
```


The name of the managed Kubernetes Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L31">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The name of the Resource Group in which the managed Kubernetes Cluster exists.

<h2 class="pdoc-module-header" id="GetKubernetesClusterResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L37">interface GetKubernetesClusterResult</a>
</h2>

A collection of values returned by getKubernetesCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L41">property addonProfiles</a>
</h3>

```typescript
addonProfiles: { ... }[];
```


A `addon_profile` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L45">property agentPoolProfiles</a>
</h3>

```typescript
agentPoolProfiles: { ... }[];
```


One or more `agent_profile_pool` blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L49">property dnsPrefix</a>
</h3>

```typescript
dnsPrefix: string;
```


The DNS Prefix of the managed Kubernetes cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L53">property fqdn</a>
</h3>

```typescript
fqdn: string;
```


The FQDN of the Azure Kubernetes Managed Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L97">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L61">property kubeConfigRaw</a>
</h3>

```typescript
kubeConfigRaw: string;
```


Base64 encoded Kubernetes configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L57">property kubeConfigs</a>
</h3>

```typescript
kubeConfigs: { ... }[];
```


A `kube_config` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L65">property kubernetesVersion</a>
</h3>

```typescript
kubernetesVersion: string;
```


The version of Kubernetes used on the managed Kubernetes Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L69">property linuxProfiles</a>
</h3>

```typescript
linuxProfiles: { ... }[];
```


A `linux_profile` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L73">property location</a>
</h3>

```typescript
location: string;
```


The Azure Region in which the managed Kubernetes Cluster exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L77">property networkProfiles</a>
</h3>

```typescript
networkProfiles: { ... }[];
```


A `network_profile` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L81">property nodeResourceGroup</a>
</h3>

```typescript
nodeResourceGroup: string;
```


Auto-generated Resource Group containing AKS Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L85">property roleBasedAccessControls</a>
</h3>

```typescript
roleBasedAccessControls: { ... }[];
```


A `role_based_access_control` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L89">property servicePrincipals</a>
</h3>

```typescript
servicePrincipals: { ... }[];
```


A `service_principal` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L93">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L178">interface GroupArgs</a>
</h2>

The set of arguments for constructing a Group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L182">property containers</a>
</h3>

```typescript
containers: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The definition of a container that is part of the group as documented in the `container` block below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L186">property dnsNameLabel</a>
</h3>

```typescript
dnsNameLabel?: pulumi.Input<string>;
```


The DNS label/name for the container groups IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L190">property imageRegistryCredentials</a>
</h3>

```typescript
imageRegistryCredentials?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Set image registry credentials for the group as documented in the `image_registry_credential` block below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L194">property ipAddressType</a>
</h3>

```typescript
ipAddressType?: pulumi.Input<string>;
```


Specifies the ip address type of the container. `Public` is the only acceptable value at this time. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L198">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L202">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Container Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L206">property osType</a>
</h3>

```typescript
osType: pulumi.Input<string>;
```


The OS for the container group. Allowed values are `Linux` and `Windows`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L210">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Container Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L214">property restartPolicy</a>
</h3>

```typescript
restartPolicy?: pulumi.Input<string>;
```


Restart policy for the container group. Allowed values are `Always`, `Never`, `OnFailure`. Defaults to `Always`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L215">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="GroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L127">interface GroupState</a>
</h2>

Input properties used for looking up and filtering Group resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L131">property containers</a>
</h3>

```typescript
containers?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The definition of a container that is part of the group as documented in the `container` block below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L135">property dnsNameLabel</a>
</h3>

```typescript
dnsNameLabel?: pulumi.Input<string>;
```


The DNS label/name for the container groups IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L139">property fqdn</a>
</h3>

```typescript
fqdn?: pulumi.Input<string>;
```


The FQDN of the container group derived from `dns_name_label`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L143">property imageRegistryCredentials</a>
</h3>

```typescript
imageRegistryCredentials?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Set image registry credentials for the group as documented in the `image_registry_credential` block below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L147">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The IP address allocated to the container group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L151">property ipAddressType</a>
</h3>

```typescript
ipAddressType?: pulumi.Input<string>;
```


Specifies the ip address type of the container. `Public` is the only acceptable value at this time. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L155">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L159">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Container Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L163">property osType</a>
</h3>

```typescript
osType?: pulumi.Input<string>;
```


The OS for the container group. Allowed values are `Linux` and `Windows`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L167">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Container Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L171">property restartPolicy</a>
</h3>

```typescript
restartPolicy?: pulumi.Input<string>;
```


Restart policy for the container group. Allowed values are `Always`, `Never`, `OnFailure`. Defaults to `Always`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L172">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="KubernetesClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L229">interface KubernetesClusterArgs</a>
</h2>

The set of arguments for constructing a KubernetesCluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L233">property addonProfile</a>
</h3>

```typescript
addonProfile?: pulumi.Input<{ ... }>;
```


A `addon_profile` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L237">property agentPoolProfile</a>
</h3>

```typescript
agentPoolProfile: pulumi.Input<{ ... }>;
```


One or more `agent_pool_profile` blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L241">property dnsPrefix</a>
</h3>

```typescript
dnsPrefix: pulumi.Input<string>;
```


DNS prefix specified when creating the managed cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L245">property kubernetesVersion</a>
</h3>

```typescript
kubernetesVersion?: pulumi.Input<string>;
```


Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L249">property linuxProfile</a>
</h3>

```typescript
linuxProfile?: pulumi.Input<{ ... }>;
```


A `linux_profile` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L253">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L257">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L261">property networkProfile</a>
</h3>

```typescript
networkProfile?: pulumi.Input<{ ... }>;
```


A `network_profile` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L265">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L269">property roleBasedAccessControl</a>
</h3>

```typescript
roleBasedAccessControl?: pulumi.Input<{ ... }>;
```


A `role_based_access_control` block. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L273">property servicePrincipal</a>
</h3>

```typescript
servicePrincipal: pulumi.Input<{ ... }>;
```


A `service_principal` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L277">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="KubernetesClusterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L159">interface KubernetesClusterState</a>
</h2>

Input properties used for looking up and filtering KubernetesCluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L163">property addonProfile</a>
</h3>

```typescript
addonProfile?: pulumi.Input<{ ... }>;
```


A `addon_profile` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L167">property agentPoolProfile</a>
</h3>

```typescript
agentPoolProfile?: pulumi.Input<{ ... }>;
```


One or more `agent_pool_profile` blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L171">property dnsPrefix</a>
</h3>

```typescript
dnsPrefix?: pulumi.Input<string>;
```


DNS prefix specified when creating the managed cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L175">property fqdn</a>
</h3>

```typescript
fqdn?: pulumi.Input<string>;
```


The FQDN of the Azure Kubernetes Managed Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L179">property kubeConfig</a>
</h3>

```typescript
kubeConfig?: pulumi.Input<{ ... }>;
```


A `kube_config` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L183">property kubeConfigRaw</a>
</h3>

```typescript
kubeConfigRaw?: pulumi.Input<string>;
```


Raw Kubernetes config to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L187">property kubernetesVersion</a>
</h3>

```typescript
kubernetesVersion?: pulumi.Input<string>;
```


Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L191">property linuxProfile</a>
</h3>

```typescript
linuxProfile?: pulumi.Input<{ ... }>;
```


A `linux_profile` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L195">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L199">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L203">property networkProfile</a>
</h3>

```typescript
networkProfile?: pulumi.Input<{ ... }>;
```


A `network_profile` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L207">property nodeResourceGroup</a>
</h3>

```typescript
nodeResourceGroup?: pulumi.Input<string>;
```


The auto-generated Resource Group which contains the resources for this Managed Kubernetes Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L211">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L215">property roleBasedAccessControl</a>
</h3>

```typescript
roleBasedAccessControl?: pulumi.Input<{ ... }>;
```


A `role_based_access_control` block. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L219">property servicePrincipal</a>
</h3>

```typescript
servicePrincipal?: pulumi.Input<{ ... }>;
```


A `service_principal` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L223">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L222">interface ServiceArgs</a>
</h2>

The set of arguments for constructing a Service resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L226">property agentPoolProfile</a>
</h3>

```typescript
agentPoolProfile: pulumi.Input<{ ... }>;
```


One or more Agent Pool Profile's block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L230">property diagnosticsProfile</a>
</h3>

```typescript
diagnosticsProfile: pulumi.Input<{ ... }>;
```


A VM Diagnostics Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L234">property linuxProfile</a>
</h3>

```typescript
linuxProfile: pulumi.Input<{ ... }>;
```


A Linux Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L238">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location where the Container Service instance should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L242">property masterProfile</a>
</h3>

```typescript
masterProfile: pulumi.Input<{ ... }>;
```


A Master Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L246">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Unique name of the agent pool profile in the context of the subscription and resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L250">property orchestrationPlatform</a>
</h3>

```typescript
orchestrationPlatform: pulumi.Input<string>;
```


Specifies the Container Orchestration Platform to use. Currently can be either `DCOS`, `Kubernetes` or `Swarm`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L254">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L258">property servicePrincipal</a>
</h3>

```typescript
servicePrincipal?: pulumi.Input<{ ... }>;
```


A Service Principal block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L262">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ServiceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L176">interface ServiceState</a>
</h2>

Input properties used for looking up and filtering Service resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L180">property agentPoolProfile</a>
</h3>

```typescript
agentPoolProfile?: pulumi.Input<{ ... }>;
```


One or more Agent Pool Profile's block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L184">property diagnosticsProfile</a>
</h3>

```typescript
diagnosticsProfile?: pulumi.Input<{ ... }>;
```


A VM Diagnostics Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L188">property linuxProfile</a>
</h3>

```typescript
linuxProfile?: pulumi.Input<{ ... }>;
```


A Linux Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L192">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location where the Container Service instance should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L196">property masterProfile</a>
</h3>

```typescript
masterProfile?: pulumi.Input<{ ... }>;
```


A Master Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L200">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Unique name of the agent pool profile in the context of the subscription and resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L204">property orchestrationPlatform</a>
</h3>

```typescript
orchestrationPlatform?: pulumi.Input<string>;
```


Specifies the Container Orchestration Platform to use. Currently can be either `DCOS`, `Kubernetes` or `Swarm`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L208">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L212">property servicePrincipal</a>
</h3>

```typescript
servicePrincipal?: pulumi.Input<{ ... }>;
```


A Service Principal block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L216">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

