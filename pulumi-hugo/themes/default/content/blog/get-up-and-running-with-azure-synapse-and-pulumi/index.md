---
title: "Get Up and Running with Azure Synapse and Pulumi"
date: 2020-12-04
draft: false
meta_desc: Use infrastructure as code to automate deployment of an Azure Synapse workspace
meta_image: synapse.png
authors:
   - mikhail-shilkov
tags:
   - azure

---

Azure Synapse is an integrated analytics service that combines enterprise data warehousing of Azure SQL Data Warehouse and Big Data analytics of Apache Spark. Azure Synapse is a managed service well integrated with other Azure services for data ingestion and business analytics.

You could use the Azure portal to get started with Azure Synapse, but it can be hard to define sophisticated infrastructure for your analytics pipeline using the portal alone, and many users need to apply version control to their cloud configurations.

The alternative is to use an [infrastructure as code]({{< relref "/what-is/what-is-infrastructure-as-code" >}}) tool to automate building and deploying cloud resources. This article demonstrates how to provision an Azure Synapse workspace using Pulumi and general-purpose programming languages like Python and C#.

<!--more-->

<div class="bg-purple-100 text-sm rounded-lg py-1 px-4">

##### Azure Synapse Quick Start

Ready to get up and running quickly right away?

1. Bootstrap a project `$ pulumi new https://github.com/pulumi/examples/tree/master/azure-py-synapse`.
2. Follow the steps outlined in [README](https://github.com/pulumi/examples/blob/master/azure-py-synapse/README.md).
3. Go to `https://web.azuresynapse.net` and sign in to your new workspace.

For additional information on how provisioning Azure Synapse with infrastructure as code, please read on.

</div>

## Azure Synapse Components

Let's start by introducing the components required to provision a basic Azure Synapse workspace. To follow along with the [Synapse Getting Started Guide](https://docs.microsoft.com/en-us/azure/synapse-analytics/get-started), you need the following key Azure infrastructure components:

- **Resource Group** to contain all other resources.
- **Storage Account** to store input data and analytics artifacts.
- **Azure Synapse Workspace**&mdash;a collaboration boundary for cloud-based analytics in Azure.
- **SQL Pool**&mdash;a dedicated Synapse SQL pool to run T-SQL based analytics.
- **Spark Pool** to use Apache Spark analytics.
- **IP Filters** and **Role Assignments** for secure access control.

## Infrastructure as Code

Let's walk through the steps to build a workspace with all the components mentioned above. We'll use Pulumi to provision the necessary resources. Feel free to pick the language of your choice that will apply to all code snippets.

You can check out the [full source code](https://github.com/pulumi/examples/tree/master/aws-ts-lambda-thumbnailer) in the Pulumi Examples.

### Resource Group

Let's start by defining a resource group to contain all other resources. Be sure to adjust its name and region to your preferred values.

{{< notes type="info" >}}
Choose the language below to adjust the contents of this blog. Your choice is applied throughout the article.
{{< /notes >}}

{{< chooser language "python,csharp,typescript" />}}

{{% choosable language python %}}

```python
resource_group = resources.ResourceGroup("resourceGroup",
    resource_group_name="synapse-rg",
    location="westus2")
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var resourceGroup = new ResourceGroup("resourceGroup", new ResourceGroupArgs
{
    ResourceGroupName = "synapse-rg",
    Location = "westus2
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const resourceGroup = new resources.ResourceGroup('resourceGroup', {
   resourceGroupName: 'synapse-rg',
   location: 'westus2',
});
```

{{% /choosable %}}

### Data Lake Storage Account

Synapse workspace will store data in a data lake storage account. We use a Standard Read-Access Geo-Redundant Storage account (SKU `Standard_RAGRS`) for this purpose. Make sure to change the `accountName` to your own globally unique name.

{{% choosable language python %}}

```python
storage_account = storage.StorageAccount("storageAccount",
    resource_group_name=resource_group.name,
    location=resource_group.location,
    account_name="yoursynapsesa",
    access_tier="Hot",
    enable_https_traffic_only=True,
    is_hns_enabled=True,
    kind="StorageV2",
    sku=storage.SkuArgs(
        name="Standard_RAGRS",
    ))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var storageAccount = new StorageAccount("storageAccount", new StorageAccountArgs
{
    ResourceGroupName = resourceGroup.Name,
    Location = resourceGroup.Location,
    AccountName = "synapsesa",
    AccessTier = "Hot",
    EnableHttpsTrafficOnly = true,
    IsHnsEnabled = true,
    Kind = "StorageV2",
    Sku = new SkuArgs
    {
        Name = "Standard_RAGRS"
    },
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const storageAccount = new storage.StorageAccount("storageAccount", {
   resourceGroupName: resourceGroup.name,
   location: resourceGroup.location,
   accountName: "yoursynapsesa",
   accessTier: "Hot",
   enableHttpsTrafficOnly: true,
   isHnsEnabled: true,
   kind: "StorageV2",
   sku: {
       name: "Standard_RAGRS",
   },
});
```

{{% /choosable %}}

Let's build a data lake URL for this storage account.

{{% choosable language python %}}

```python
data_lake_storage_account_url = storage_account.name.apply(lambda name: f"https://{name}.dfs.core.windows.net")
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var dataLakeStorageAccountUrl = Output.Format($"https://{storageAccount.Name}.dfs.core.windows.net");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const dataLakeStorageAccountUrl = pulumi.interpolate`https://${storageAccount.name}.dfs.core.windows.net`;
```

{{% /choosable %}}

We'll use the `users` blob container as the analytics file system.

{{% choosable language python %}}

```python
users = storage.BlobContainer("users",
    resource_group_name=resource_group.name,
    account_name=storage_account.name,
    container_name="users",
    public_access="None")
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var users = new BlobContainer("users", new BlobContainerArgs
{
    ResourceGroupName = resourceGroup.Name,
    AccountName = storageAccount.Name,
    ContainerName = "users",
    PublicAccess = "None"
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
new storage.BlobContainer("users", {
   resourceGroupName: resourceGroup.name,
   accountName: storageAccount.name,
   containerName: "users",
   publicAccess: "None",
});
```

{{% /choosable %}}

### Synapse Workspace

It's time to use all of the above to provision an Azure Synapse workspace! Adjust the name and the SQL credentials in the definition below.

{{% choosable language python %}}

```python
workspace = synapse.Workspace("workspace",
    resource_group_name=resource_group.name,
    location=resource_group.location,
    workspace_name="mysynapse",
    default_data_lake_storage=synapse.DataLakeStorageAccountDetailsArgs(
        account_url=data_lake_storage_account_url,
        filesystem="users",
    ),
    identity=synapse.ManagedIdentityArgs(
        type="SystemAssigned",
    ),
    sql_administrator_login="sqladminuser",
    sql_administrator_login_password=random.RandomPassword("workspacePwd", length=12).result)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var workspace = new Workspace("workspace", new WorkspaceArgs
{
    ResourceGroupName = resourceGroup.Name,
    Location = resourceGroup.Location,
    WorkspaceName = "my-workspace",
    DefaultDataLakeStorage = new DataLakeStorageAccountDetailsArgs
    {
        AccountUrl = dataLakeStorageAccountUrl,
        Filesystem = "users"
    },
    Identity = new ManagedIdentityArgs
    {
        Type = "SystemAssigned"
    },
    SqlAdministratorLogin = "sqladminuser",
    SqlAdministratorLoginPassword = "YourStrongPassword"
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const workspace = new synapse.Workspace("workspace", {
   resourceGroupName: resourceGroup.name,
   location: resourceGroup.location,
   workspaceName: "mysynapse",
   defaultDataLakeStorage: {
       accountUrl: dataLakeStorageAccountUrl,
       filesystem: "users",
   },
   identity: {
       type: "SystemAssigned",
   },
   sqlAdministratorLogin: "sqladminuser",
   sqlAdministratorLoginPassword: "YourSecurePassword",
});
```

{{% /choosable %}}

> Note that we also defined a system-assigned managed identity for the workspace.

### Security Setup

You need to allow access to the workspace with a firewall rule. The following is a blank access rule but feel free to restrict it to your target IP range.

{{% choosable language python %}}

```python
allow_all = synapse.IpFirewallRule("allowAll",
    resource_group_name=resource_group.name,
    workspace_name=workspace.name,
    rule_name="allowAll",
    end_ip_address="255.255.255.255",
    start_ip_address="0.0.0.0")
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var allowAll = new IpFirewallRule("allowAll", new IpFirewallRuleArgs
{
    ResourceGroupName = resourceGroup.Name,
    WorkspaceName = workspace.Name,
    RuleName = "allowAll",
    EndIpAddress = "255.255.255.255",
    StartIpAddress = "0.0.0.0"
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
new synapse.IpFirewallRule("allowAll", {
   resourceGroupName: resourceGroup.name,
   workspaceName: workspace.name,
   ruleName: "allowAll",
   endIpAddress: "255.255.255.255",
   startIpAddress: "0.0.0.0",
});
```

{{% /choosable %}}

The following snippet assigns the **Storage Blob Data Contributor** role to the workspace managed identity and your target user. If you use the Azure CLI, run `az ad signed-in-user show --query=objectId` to look up your user ID.

{{% choosable language python %}}

```python
subscription_id = resource_group.id.apply(lambda id: id.split('/')[2])
role_definition_id = subscription_id.apply(lambda id: f"/subscriptions/{id}/providers/Microsoft.Authorization/roleDefinitions/ba92f5b4-2d11-453d-a403-e96b0029c9fe")

authorization.RoleAssignment("storageAccess",
    role_assignment_name=random.RandomUuid("roleName").result,
    scope=storage_account.id,
    principal_id=workspace.identity.principal_id.apply(lambda v: v or "<preview>"),
    principal_type="ServicePrincipal",
    role_definition_id=role_definition_id)

authorization.RoleAssignment("userAccess",
    role_assignment_name=random.RandomUuid("userRoleName").result,
    scope=storage_account.id,
    principal_id=config.get("userObjectId"),
    principal_type="User",
    role_definition_id=role_definition_id)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var subscriptionId = resourceGroup.Id.Apply(id => id.Split('/')[2]);
var roleDefinitionId = $"/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/roleDefinitions/ba92f5b4-2d11-453d-a403-e96b0029c9fe";

new RoleAssignment("storageAccess", new RoleAssignmentArgs
{
    RoleAssignmentName = new RandomUuid("roleName").Result,
    Scope = storageAccount.Id,
    PrincipalId = workspace.Identity.Apply(identity => identity.PrincipalId).Apply(v => v ?? "<preview>"),
    PrincipalType = "ServicePrincipal",
    RoleDefinitionId = roleDefinitionId
});
new RoleAssignment("userAccess", new RoleAssignmentArgs
{
    RoleAssignmentName = new RandomUuid("userRoleName").Result,
    Scope = storageAccount.Id,
    PrincipalId = config.Require("userObjectId"),
    PrincipalType = "User",
    RoleDefinitionId = roleDefinitionId
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const subscriptionId = resourceGroup.id.apply(id => id.split('/')[2]);
const roleDefinitionId = pulumi.interpolate`/subscriptions/${subscriptionId}/providers/Microsoft.Authorization/roleDefinitions/ba92f5b4-2d11-453d-a403-e96b0029c9fe`;

new authorization.RoleAssignment("storageAccess", {
   roleAssignmentName: new random.RandomUuid("roleName").result,
   scope: storageAccount.id,
   principalId: workspace.identity.principalId,
   principalType: "ServicePrincipal",
   roleDefinitionId: roleDefinitionId,
});

new authorization.RoleAssignment("userAccess", {
 roleAssignmentName: new random.RandomUuid("userRoleName").result,
 scope: storageAccount.id,
 principalId: "your-synapse-user-object-uuid",
 principalType: "User",
 roleDefinitionId: roleDefinitionId,
});
```

{{% /choosable %}}

### SQL and Spark Pools

Finally, let's add two worker pools to the Synapse workspace. A SQL pool for T-SQL analytic queries...

{{% choosable language python %}}

```python
sql_pool = synapse.SqlPool("sqlPool",
    resource_group_name=resource_group.name,
    location=resource_group.location,
    workspace_name=workspace.name,
    sql_pool_name="SQLPOOL1",
    collation="SQL_Latin1_General_CP1_CI_AS",
    create_mode="Default",
    sku=synapse.SkuArgs(
        name="DW100c",
    ))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var sqlPool = new SqlPool("sqlPool", new SqlPoolArgs
{
    ResourceGroupName = resourceGroup.Name,
    Location = resourceGroup.Location,
    WorkspaceName = workspace.Name,
    SqlPoolName = "SQLPOOL1",
    Collation = "SQL_Latin1_General_CP1_CI_AS",
    CreateMode = "Default",
    Sku = new Pulumi.AzureNative.Synapse.Inputs.SkuArgs
    {
        Name = "DW100c"
    },
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const sqlPool = new synapse.SqlPool("sqlPool", {
   resourceGroupName: resourceGroup.name,
   location: resourceGroup.location,
   workspaceName: workspace.name,
   sqlPoolName: "SQLPOOL1",
   collation: "SQL_Latin1_General_CP1_CI_AS",
   createMode: "Default",
   sku: {
       name: "DW100c",
   },
});
```

{{% /choosable %}}

... and a Spark pool for Big Data analytics.

{{% choosable language python %}}

```python
spark_pool = synapse.BigDataPool("sparkPool",
    resource_group_name=resource_group.name,
    location=resource_group.location,
    workspace_name=workspace.name,
    big_data_pool_name="Spark1",
    auto_pause=synapse.AutoPausePropertiesArgs(
        delay_in_minutes=15,
        enabled=True,
    ),
    auto_scale=synapse.AutoScalePropertiesArgs(
        enabled=True,
        max_node_count=3,
        min_node_count=3,
    ),
    node_count=3,
    node_size="Small",
    node_size_family="MemoryOptimized",
    spark_version="2.4")
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var sparkPool = new BigDataPool("sparkPool", new BigDataPoolArgs
{
    ResourceGroupName = resourceGroup.Name,
    Location = resourceGroup.Location,
    WorkspaceName = workspace.Name,
    BigDataPoolName = "Spark1",
    AutoPause = new AutoPausePropertiesArgs
    {
        DelayInMinutes = 15,
        Enabled = true,
    },
    AutoScale = new AutoScalePropertiesArgs
    {
        Enabled = true,
        MaxNodeCount = 3,
        MinNodeCount = 3,
    },
    NodeCount = 3,
    NodeSize = "Small",
    NodeSizeFamily = "MemoryOptimized",
    SparkVersion = "2.4"
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const bigDataPoolResource = new synapse.BigDataPool("sparkPool", {
   resourceGroupName: resourceGroup.name,
   location: resourceGroup.location,
   workspaceName: workspace.name,
   bigDataPoolName: "Spark1",
   autoPause: {
       delayInMinutes: 15,
       enabled: true,
   },
   autoScale: {
       enabled: true,
       maxNodeCount: 3,
       minNodeCount: 3,
   },
   nodeCount: 3,
   nodeSize: "Small",
   nodeSizeFamily: "MemoryOptimized",
   sparkVersion: "2.4",
});
```

{{% /choosable %}}

## Ready to Dive into Analytics

Our resource definitions are ready. Run `pulumi up` to provision your Azure Synapse infrastructure.

```sh
$ pulumi up
...
Do you want to perform this update? yes
Updating (dev)

     Type                                          Name                  Plan
 +   pulumi:pulumi:Stack                           azure-py-synapse-dev  created
 +   ├─ azure-native:resources:ResourceGroup       resourceGroup         created
 +   ├─ azure-native:storage:StorageAccount        storageAccount        created
 +   ├─ azure-native:storage:BlobContainer         users                 created
 +   ├─ azure-native:synapse:Workspace             workspace             created
 +   ├─ random:index:RandomUuid                    roleName              created
 +   └─ azure-native:authorization:RoleAssignment  storageAccess         created
 +   ├─ random:index:RandomUuid                    userRoleName          created
 +   ├─ azure-native:authorization:RoleAssignment  userAccess            created
 +   ├─ azure-native:synapse:IpFirewallRule        allowAll              created
 +   ├─ azure-native:synapse:SqlPool               sqlPool               created
 +   ├─ azure-native:synapse:BigDataPool           sparkPool             created

 Resources:
    + 12 created

Duration: 10m51s
 ```

You can now navigate to the [Azure Synapse Quickstart, Step 2](https://docs.microsoft.com/en-us/azure/synapse-analytics/get-started-analyze-sql-pool), and follow along with the data analysis tutorial.

## Conclusion

Azure Synapse is a managed analytics service that accelerates time to insight across data warehouses and big data workloads. A Synapse workspace is a critical component of your cloud infrastructure that you should provision with infrastructure as code and other management best practices.

Pulumi and the native Azure provider open up full access to all types of Azure resources using your favorite programming languages, including Python, C#, and TypeScript. Navigate to the complete Azure Synapse example in [Python](https://github.com/pulumi/examples/tree/master/azure-py-synapse), [C#](https://github.com/pulumi/examples/tree/master/azure-cs-synapse), or [TypeScript](https://github.com/pulumi/examples/tree/master/azure-ts-synapse) and get started today.
