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
* <a href="#GetKubernetesClusterArgs">interface GetKubernetesClusterArgs</a>
* <a href="#GetKubernetesClusterResult">interface GetKubernetesClusterResult</a>
* <a href="#GroupArgs">interface GroupArgs</a>
* <a href="#GroupState">interface GroupState</a>
* <a href="#KubernetesClusterArgs">interface KubernetesClusterArgs</a>
* <a href="#KubernetesClusterState">interface KubernetesClusterState</a>
* <a href="#RegistryArgs">interface RegistryArgs</a>
* <a href="#RegistryState">interface RegistryState</a>
* <a href="#ServiceArgs">interface ServiceArgs</a>
* <a href="#ServiceState">interface ServiceState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts">containerservice/getKubernetesCluster.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts">containerservice/group.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts">containerservice/kubernetesCluster.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts">containerservice/registry.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts">containerservice/service.ts</a> 


<h2 class="pdoc-module-header" id="Group">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L6">class Group</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L29">constructor</a>
</h3>

```typescript
new Group(name: string, args: GroupArgs, opts?: pulumi.ResourceOptions)
```


Create a Group resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L15">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupState): Group
```


Get an existing Group resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L19">property containers</a>
</h3>

```typescript
public containers: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L20">property dnsNameLabel</a>
</h3>

```typescript
public dnsNameLabel: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L21">property fqdn</a>
</h3>

```typescript
public fqdn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L22">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L23">property ipAddressType</a>
</h3>

```typescript
public ipAddressType: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L24">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L25">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L26">property osType</a>
</h3>

```typescript
public osType: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L27">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L28">property restartPolicy</a>
</h3>

```typescript
public restartPolicy: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L29">property tags</a>
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
[Read more about sensitive data in state](/docs/state/sensitive-data.html).


<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L73">constructor</a>
</h3>

```typescript
new KubernetesCluster(name: string, args: KubernetesClusterArgs, opts?: pulumi.ResourceOptions)
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L29">property agentPoolProfile</a>
</h3>

```typescript
public agentPoolProfile: pulumi.Output<{ ... }>;
```


One or more Agent Pool Profile's block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L33">property dnsPrefix</a>
</h3>

```typescript
public dnsPrefix: pulumi.Output<string>;
```


DNS prefix specified when creating the managed cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L37">property fqdn</a>
</h3>

```typescript
public fqdn: pulumi.Output<string>;
```


The FQDN of the Azure Kubernetes Managed Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L41">property kubeConfig</a>
</h3>

```typescript
public kubeConfig: pulumi.Output<{ ... }>;
```


Kubernetes configuration, sub-attributes defined below:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L45">property kubeConfigRaw</a>
</h3>

```typescript
public kubeConfigRaw: pulumi.Output<string>;
```


Base64 encoded Kubernetes configuration

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L49">property kubernetesVersion</a>
</h3>

```typescript
public kubernetesVersion: pulumi.Output<string>;
```


Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L53">property linuxProfile</a>
</h3>

```typescript
public linuxProfile: pulumi.Output<{ ... }>;
```


A Linux Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L57">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location where the AKS Managed Cluster instance should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L61">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Unique name of the Agent Pool Profile in the context of the Subscription and Resource Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L65">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L69">property servicePrincipal</a>
</h3>

```typescript
public servicePrincipal: pulumi.Output<{ ... }>;
```


A Service Principal block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L73">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L12">class Registry</a>
</h2>

Manages an Azure Container Registry.

~> **Note:** All arguments including the access key will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L65">constructor</a>
</h3>

```typescript
new Registry(name: string, args: RegistryArgs, opts?: pulumi.ResourceOptions)
```


Create a Registry resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RegistryState): Registry
```


Get an existing Registry resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L28">property adminEnabled</a>
</h3>

```typescript
public adminEnabled: pulumi.Output<boolean | undefined>;
```


Specifies whether the admin user is enabled. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L32">property adminPassword</a>
</h3>

```typescript
public adminPassword: pulumi.Output<string>;
```


The Password associated with the Container Registry Admin account - if the admin account is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L36">property adminUsername</a>
</h3>

```typescript
public adminUsername: pulumi.Output<string>;
```


The Username associated with the Container Registry Admin account - if the admin account is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L40">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L44">property loginServer</a>
</h3>

```typescript
public loginServer: pulumi.Output<string>;
```


The URL that can be used to log into the container registry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L48">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Container Registry. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L52">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L56">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string | undefined>;
```


The SKU name of the the container registry. Possible values are `Classic` (which was previously `Basic`), `Basic`, `Standard` and `Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L57">property storageAccount</a>
</h3>

```typescript
public storageAccount: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L61">property storageAccountId</a>
</h3>

```typescript
public storageAccountId: pulumi.Output<string | undefined>;
```


The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L65">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L56">class Service</a>
</h2>

Manages an Azure Container Service Instance

~> **Note:** All arguments including the client secret will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

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
    vm_size    = "Standard_A0"
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L108">constructor</a>
</h3>

```typescript
new Service(name: string, args: ServiceArgs, opts?: pulumi.ResourceOptions)
```


Create a Service resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L65">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServiceState): Service
```


Get an existing Service resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L72">property agentPoolProfile</a>
</h3>

```typescript
public agentPoolProfile: pulumi.Output<{ ... }>;
```


One or more Agent Pool Profile's block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L76">property diagnosticsProfile</a>
</h3>

```typescript
public diagnosticsProfile: pulumi.Output<{ ... }>;
```


A VM Diagnostics Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L80">property linuxProfile</a>
</h3>

```typescript
public linuxProfile: pulumi.Output<{ ... }>;
```


A Linux Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L84">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location where the Container Service instance should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L88">property masterProfile</a>
</h3>

```typescript
public masterProfile: pulumi.Output<{ ... }>;
```


A Master Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L92">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Unique name of the agent pool profile in the context of the subscription and resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L96">property orchestrationPlatform</a>
</h3>

```typescript
public orchestrationPlatform: pulumi.Output<string>;
```


Specifies the Container Orchestration Platform to use. Currently can be either `DCOS`, `Kubernetes` or `Swarm`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L100">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L104">property servicePrincipal</a>
</h3>

```typescript
public servicePrincipal: pulumi.Output<{ ... } | undefined>;
```


A Service Principal block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L108">property tags</a>
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
getKubernetesCluster(args: GetKubernetesClusterArgs): Promise<GetKubernetesClusterResult>
```


Gets information about a managed Kubernetes Cluster (AKS)

~> **Note:** All arguments including the client secret will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).


<h2 class="pdoc-module-header" id="GetKubernetesClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L23">interface GetKubernetesClusterArgs</a>
</h2>

A collection of arguments for invoking getKubernetesCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L27">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The name of the managed Kubernetes Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L31">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the Resource Group in which the managed Kubernetes Cluster exists.

<h2 class="pdoc-module-header" id="GetKubernetesClusterResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L37">interface GetKubernetesClusterResult</a>
</h2>

A collection of values returned by getKubernetesCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L41">property agentPoolProfiles</a>
</h3>

```typescript
agentPoolProfiles: { ... }[];
```


One or more `agent_profile_pool` blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L45">property dnsPrefix</a>
</h3>

```typescript
dnsPrefix: string;
```


The DNS Prefix of the managed Kubernetes cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L49">property fqdn</a>
</h3>

```typescript
fqdn: string;
```


The FQDN of the Azure Kubernetes Managed Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L81">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L57">property kubeConfigRaw</a>
</h3>

```typescript
kubeConfigRaw: string;
```


Base64 encoded Kubernetes configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L53">property kubeConfigs</a>
</h3>

```typescript
kubeConfigs: { ... }[];
```


A `kube_config` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L61">property kubernetesVersion</a>
</h3>

```typescript
kubernetesVersion: string;
```


The version of Kubernetes used on the managed Kubernetes Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L65">property linuxProfiles</a>
</h3>

```typescript
linuxProfiles: { ... }[];
```


A `linux_profile` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L69">property location</a>
</h3>

```typescript
location: string;
```


The Azure Region in which the managed Kubernetes Cluster exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L73">property servicePrincipals</a>
</h3>

```typescript
servicePrincipals: { ... }[];
```


A `service_principal` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/getKubernetesCluster.ts#L77">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to this resource.

<h2 class="pdoc-module-header" id="GroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L104">interface GroupArgs</a>
</h2>

The set of arguments for constructing a Group resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L105">property containers</a>
</h3>

```typescript
containers: pulumi.Input<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L106">property dnsNameLabel</a>
</h3>

```typescript
dnsNameLabel?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L107">property ipAddressType</a>
</h3>

```typescript
ipAddressType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L108">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L109">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L110">property osType</a>
</h3>

```typescript
osType: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L111">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L112">property restartPolicy</a>
</h3>

```typescript
restartPolicy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L113">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="GroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L87">interface GroupState</a>
</h2>

Input properties used for looking up and filtering Group resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L88">property containers</a>
</h3>

```typescript
containers?: pulumi.Input<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L89">property dnsNameLabel</a>
</h3>

```typescript
dnsNameLabel?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L90">property fqdn</a>
</h3>

```typescript
fqdn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L91">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L92">property ipAddressType</a>
</h3>

```typescript
ipAddressType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L93">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L94">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L95">property osType</a>
</h3>

```typescript
osType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L96">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L97">property restartPolicy</a>
</h3>

```typescript
restartPolicy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/group.ts#L98">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="KubernetesClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L190">interface KubernetesClusterArgs</a>
</h2>

The set of arguments for constructing a KubernetesCluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L194">property agentPoolProfile</a>
</h3>

```typescript
agentPoolProfile: pulumi.Input<{ ... }>;
```


One or more Agent Pool Profile's block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L198">property dnsPrefix</a>
</h3>

```typescript
dnsPrefix?: pulumi.Input<string>;
```


DNS prefix specified when creating the managed cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L202">property kubernetesVersion</a>
</h3>

```typescript
kubernetesVersion?: pulumi.Input<string>;
```


Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L206">property linuxProfile</a>
</h3>

```typescript
linuxProfile: pulumi.Input<{ ... }>;
```


A Linux Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L210">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location where the AKS Managed Cluster instance should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L214">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Unique name of the Agent Pool Profile in the context of the Subscription and Resource Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L218">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L222">property servicePrincipal</a>
</h3>

```typescript
servicePrincipal: pulumi.Input<{ ... }>;
```


A Service Principal block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L226">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="KubernetesClusterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L136">interface KubernetesClusterState</a>
</h2>

Input properties used for looking up and filtering KubernetesCluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L140">property agentPoolProfile</a>
</h3>

```typescript
agentPoolProfile?: pulumi.Input<{ ... }>;
```


One or more Agent Pool Profile's block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L144">property dnsPrefix</a>
</h3>

```typescript
dnsPrefix?: pulumi.Input<string>;
```


DNS prefix specified when creating the managed cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L148">property fqdn</a>
</h3>

```typescript
fqdn?: pulumi.Input<string>;
```


The FQDN of the Azure Kubernetes Managed Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L152">property kubeConfig</a>
</h3>

```typescript
kubeConfig?: pulumi.Input<{ ... }>;
```


Kubernetes configuration, sub-attributes defined below:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L156">property kubeConfigRaw</a>
</h3>

```typescript
kubeConfigRaw?: pulumi.Input<string>;
```


Base64 encoded Kubernetes configuration

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L160">property kubernetesVersion</a>
</h3>

```typescript
kubernetesVersion?: pulumi.Input<string>;
```


Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won't auto-upgrade).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L164">property linuxProfile</a>
</h3>

```typescript
linuxProfile?: pulumi.Input<{ ... }>;
```


A Linux Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L168">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location where the AKS Managed Cluster instance should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L172">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Unique name of the Agent Pool Profile in the context of the Subscription and Resource Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L176">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L180">property servicePrincipal</a>
</h3>

```typescript
servicePrincipal?: pulumi.Input<{ ... }>;
```


A Service Principal block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/kubernetesCluster.ts#L184">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="RegistryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L164">interface RegistryArgs</a>
</h2>

The set of arguments for constructing a Registry resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L168">property adminEnabled</a>
</h3>

```typescript
adminEnabled?: pulumi.Input<boolean>;
```


Specifies whether the admin user is enabled. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L172">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L176">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Container Registry. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L180">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L184">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


The SKU name of the the container registry. Possible values are `Classic` (which was previously `Basic`), `Basic`, `Standard` and `Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L185">property storageAccount</a>
</h3>

```typescript
storageAccount?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L189">property storageAccountId</a>
</h3>

```typescript
storageAccountId?: pulumi.Input<string>;
```


The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L193">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="RegistryState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L117">interface RegistryState</a>
</h2>

Input properties used for looking up and filtering Registry resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L121">property adminEnabled</a>
</h3>

```typescript
adminEnabled?: pulumi.Input<boolean>;
```


Specifies whether the admin user is enabled. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L125">property adminPassword</a>
</h3>

```typescript
adminPassword?: pulumi.Input<string>;
```


The Password associated with the Container Registry Admin account - if the admin account is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L129">property adminUsername</a>
</h3>

```typescript
adminUsername?: pulumi.Input<string>;
```


The Username associated with the Container Registry Admin account - if the admin account is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L133">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L137">property loginServer</a>
</h3>

```typescript
loginServer?: pulumi.Input<string>;
```


The URL that can be used to log into the container registry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L141">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Container Registry. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L145">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L149">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


The SKU name of the the container registry. Possible values are `Classic` (which was previously `Basic`), `Basic`, `Standard` and `Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L150">property storageAccount</a>
</h3>

```typescript
storageAccount?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L154">property storageAccountId</a>
</h3>

```typescript
storageAccountId?: pulumi.Input<string>;
```


The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/registry.ts#L158">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ServiceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L219">interface ServiceArgs</a>
</h2>

The set of arguments for constructing a Service resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L223">property agentPoolProfile</a>
</h3>

```typescript
agentPoolProfile: pulumi.Input<{ ... }>;
```


One or more Agent Pool Profile's block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L227">property diagnosticsProfile</a>
</h3>

```typescript
diagnosticsProfile: pulumi.Input<{ ... }>;
```


A VM Diagnostics Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L231">property linuxProfile</a>
</h3>

```typescript
linuxProfile: pulumi.Input<{ ... }>;
```


A Linux Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L235">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location where the Container Service instance should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L239">property masterProfile</a>
</h3>

```typescript
masterProfile: pulumi.Input<{ ... }>;
```


A Master Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L243">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Unique name of the agent pool profile in the context of the subscription and resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L247">property orchestrationPlatform</a>
</h3>

```typescript
orchestrationPlatform: pulumi.Input<string>;
```


Specifies the Container Orchestration Platform to use. Currently can be either `DCOS`, `Kubernetes` or `Swarm`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L251">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L255">property servicePrincipal</a>
</h3>

```typescript
servicePrincipal?: pulumi.Input<{ ... }>;
```


A Service Principal block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L259">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ServiceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L173">interface ServiceState</a>
</h2>

Input properties used for looking up and filtering Service resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L177">property agentPoolProfile</a>
</h3>

```typescript
agentPoolProfile?: pulumi.Input<{ ... }>;
```


One or more Agent Pool Profile's block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L181">property diagnosticsProfile</a>
</h3>

```typescript
diagnosticsProfile?: pulumi.Input<{ ... }>;
```


A VM Diagnostics Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L185">property linuxProfile</a>
</h3>

```typescript
linuxProfile?: pulumi.Input<{ ... }>;
```


A Linux Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L189">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location where the Container Service instance should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L193">property masterProfile</a>
</h3>

```typescript
masterProfile?: pulumi.Input<{ ... }>;
```


A Master Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L197">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Unique name of the agent pool profile in the context of the subscription and resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L201">property orchestrationPlatform</a>
</h3>

```typescript
orchestrationPlatform?: pulumi.Input<string>;
```


Specifies the Container Orchestration Platform to use. Currently can be either `DCOS`, `Kubernetes` or `Swarm`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L205">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L209">property servicePrincipal</a>
</h3>

```typescript
servicePrincipal?: pulumi.Input<{ ... }>;
```


A Service Principal block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/containerservice/service.ts#L213">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

