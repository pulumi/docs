---
title_tag: Make an Update | Azure
title: Make an update
h1: "Get started with Pulumi and Azure"
meta_desc: This page provides an overview on how to update an Azure project from a Pulumi program.
weight: 6
menu:
    iac:
        name: Make an update
        identifier: azure-get-started.modify-program
        parent: azure-get-started
        weight: 6
aliases:
    - /docs/quickstart/azure/modify-program/
    - /docs/clouds/azure/get-started/modify-program/
    - /docs/quickstart/azure/deploy-changes/
    - /docs/clouds/azure/get-started/deploy-changes/
---

## Make an update

Now you will update your project to serve a static website out of your Azure storage account. You will change your code and then re-run `pulumi up` which will update your infrastructure.

### Add new resources

Pulumi knows how to evolve your current infrastructure to your project's new desired state, both for the first deployment as well as subsequent updates.

To turn your storage account into a static website, you will add two new Azure resources:

1. [`StorageAccountStaticWebsite`](/registry/packages/azure-native/api-docs/storage/storageaccountstaticwebsite/):
    enables static website support on your storage account
2. [`Blob`](/registry/packages/azure-native/api-docs/storage/blob/):
    uploads your website content to the storage container

### Add an index.html

First, from within your project directory, create a new `index.html` file with some content in it.

{{< chooser os "macos,linux,windows" / >}}

{{% choosable os macos %}}

```bash
cat <<EOT > index.html
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
EOT
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
cat <<EOT > index.html
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
EOT
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
@"
<html>
  <body>
    <h1>Hello, Pulumi!</h1>
  </body>
</html>
"@ | Out-File -FilePath index.html
```

{{% /choosable %}}

Now open {{< langfile >}} in your editor and enable static website support by adding a [`StorageAccountStaticWebsite`](/registry/packages/azure-native/api-docs/storage/storageaccountstaticwebsite/) resource right after the storage account is created:

{{% choosable language typescript %}}

```typescript
// Create an Azure resource (Storage Account)
const storageAccount = new storage.StorageAccount("sa", {
    /* existing storage account configuration */
});

// Enable static website support - add this code
const staticWebsite = new storage.StorageAccountStaticWebsite("staticWebsite", {
    accountName: storageAccount.name,
    resourceGroupName: resourceGroup.name,
    indexDocument: "index.html",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
# Create an Azure resource (Storage Account)
account = storage.StorageAccount(
    "sa",
    # existing storage account configuration
)

# Enable static website support - add this code
static_website = storage.StorageAccountStaticWebsite(
    "staticWebsite",
    account_name=account.name,
    resource_group_name=resource_group.name,
    index_document="index.html",
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// Create an Azure resource (Storage Account)
account, err := storage.NewStorageAccount(ctx, "sa", &storage.StorageAccountArgs{
    // existing storage account configuration
})
if err != nil {
    return err
}

// Enable static website support - add this code
staticWebsite, err := storage.NewStorageAccountStaticWebsite(ctx, "staticWebsite", &storage.StorageAccountStaticWebsiteArgs{
    AccountName:       account.Name,
    ResourceGroupName: resourceGroup.Name,
    IndexDocument:     pulumi.String("index.html"),
})
if err != nil {
    return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Create an Azure resource (Storage Account)
var storageAccount = new StorageAccount("sa", new StorageAccountArgs
{
    /* existing storage account configuration */
});

// Enable static website support - add this code
var staticWebsite = new StorageAccountStaticWebsite("staticWebsite", new StorageAccountStaticWebsiteArgs
{
    AccountName = storageAccount.Name,
    ResourceGroupName = resourceGroup.Name,
    IndexDocument = "index.html",
});
```

{{% /choosable %}}

{{% choosable language java %}}

First, add the following imports at the top of `App.java`:

```java
import com.pulumi.azurenative.storage.StorageAccountStaticWebsite;
import com.pulumi.azurenative.storage.StorageAccountStaticWebsiteArgs;
import com.pulumi.azurenative.storage.Blob;
import com.pulumi.azurenative.storage.BlobArgs;
import com.pulumi.azurenative.storage.outputs.EndpointsResponse;
import com.pulumi.asset.FileAsset;
```

Then add the following right after the storage account creation:

```java
// Create an Azure resource (Storage Account)
var storageAccount = new StorageAccount("sa", StorageAccountArgs.builder()
    // existing storage account configuration
    .build());

// Enable static website support - add this code
var staticWebsite = new StorageAccountStaticWebsite("staticWebsite",
                    StorageAccountStaticWebsiteArgs.builder()
                            .accountName(storageAccount.name())
                            .resourceGroupName(resourceGroup.name())
                            .indexDocument("index.html")
                            .build());
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  # Create an Azure resource (Storage Account)
  sa:
    type: azure-native:storage:StorageAccount
    # existing storage account configuration

  # Enable static website support - add this code
  staticWebsite:
    type: azure-native:storage:StorageAccountStaticWebsite
    properties:
      accountName: ${sa.name}
      resourceGroupName: ${resourceGroup.name}
      indexDocument: index.html
```

{{% /choosable %}}

Notice that resources can reference each other, which forms automatic dependencies between them.
Pulumi uses this information to parallelize deployments safely.

Now use all of these cloud resources and a local `FileAsset` resource to upload `index.html` into your storage container by adding a [`Blob`](/registry/packages/azure-native/api-docs/storage/blob/) at the end of the file (after enabling the static website support):
{{% choosable language typescript %}}

```typescript
// Upload the file
const indexHtml = new storage.Blob("index.html", {
    resourceGroupName: resourceGroup.name,
    accountName: storageAccount.name,
    containerName: staticWebsite.containerName,
    source: new pulumi.asset.FileAsset("index.html"),
    contentType: "text/html",
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# Upload the file
index_html = storage.Blob(
    "index.html",
    resource_group_name=resource_group.name,
    account_name=account.name,
    container_name=static_website.container_name,
    source=pulumi.FileAsset("index.html"),
    content_type="text/html",
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// Upload the file
_, err = storage.NewBlob(ctx, "index.html", &storage.BlobArgs{
    ResourceGroupName: resourceGroup.Name,
    AccountName:       account.Name,
    ContainerName:     staticWebsite.ContainerName,
    Source:            pulumi.NewFileAsset("index.html"),
    ContentType:       pulumi.String("text/html"),
})
if err != nil {
    return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Upload the file
var indexHtml = new Blob("index.html", new BlobArgs
{
    ResourceGroupName = resourceGroup.Name,
    AccountName = storageAccount.Name,
    ContainerName = staticWebsite.ContainerName,
    Source = new FileAsset("./index.html"),
    ContentType = "text/html",
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// Upload the file
var index_html = new Blob("index.html", BlobArgs.builder()
                    .resourceGroupName(resourceGroup.name())
                    .accountName(storageAccount.name())
                    .containerName(staticWebsite.containerName())
                    .source(new FileAsset("index.html"))
                    .contentType("text/html")
                    .build());
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  # ...
  # Upload the file
  index-html:
    type: azure-native:storage:Blob
    properties:
      resourceGroupName: ${resourceGroup.name}
      accountName: ${sa.name}
      containerName: ${staticWebsite.containerName}
      source:
        fn::fileAsset: ./index.html
      contentType: text/html
      blobName: index.html
      type: Block
```

{{% /choosable %}}

This uploads the `index.html` file to your storage container using a Pulumi concept called an [asset](/docs/iac/concepts/assets-archives/#assets).

### Export the website URL

Now to export the website's URL for easy access, add the `staticEndpoint` export to your return statement as shown in this example:

{{% choosable language typescript %}}

```typescript
// Export the primary key of the Storage Account
export const primaryStorageKey = pulumi.secret(storageAccountKeys.keys[0].value);
export const storageAccountName = storageAccount.name;

// Web endpoint to the website
export const staticEndpoint = storageAccount.primaryEndpoints.web;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# Export the primary key of the Storage Account
pulumi.export("primary_storage_key", primary_key)
pulumi.export("storage_account_name", account.name)

# Web endpoint to the website
pulumi.export("staticEndpoint", account.primary_endpoints.web)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Export the primary key of the Storage Account
ctx.Export("primaryStorageKey", pulumi.All(resourceGroup.Name, account.Name).ApplyT(
    func(args []interface{}) (string, error) {
        resourceGroupName := args[0].(string)
        accountName := args[1].(string)
        accountKeys, err := storage.ListStorageAccountKeys(ctx, &storage.ListStorageAccountKeysArgs{
            ResourceGroupName: resourceGroupName,
            AccountName:       accountName,
        })
        if err != nil {
            return "", err
        }

        return accountKeys.Keys[0].Value, nil
    },
))
ctx.Export("storageAccountName", account.Name)

// Web endpoint to the website
ctx.Export("staticEndpoint", account.PrimaryEndpoints.Web())
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
// Export outputs
return new Dictionary<string, object?>
{
    ["primaryStorageKey"] = primaryStorageKey,
    ["storageAccountName"] = storageAccount.Name,
    ["staticEndpoint"] = storageAccount.PrimaryEndpoints.Apply(primaryEndpoints => primaryEndpoints.Web)
};
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// Export the primary key of the Storage Account
ctx.export("primaryStorageKey", primaryStorageKey);
ctx.export("storageAccountName", storageAccount.name());

// Web endpoint to the website
ctx.export("staticEndpoint", storageAccount.primaryEndpoints()
        .applyValue(EndpointsResponse::web));
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
outputs:
  # Export the primary key of the Storage Account
  primaryStorageKey: ${storageAccountKeys.keys[0].value}
  storageAccountName: ${sa.name}

  # Web endpoint to the website
  staticEndpoint: ${sa.primaryEndpoints.web}
```

{{% /choosable %}}

The storage account's endpoint is [an output property](/docs/iac/concepts/inputs-outputs/#outputs)
that Azure assigns at deployment time, not a raw string, meaning its value is not known in advance.

### Deploy the changes

To deploy the changes, run `pulumi up` again and it will figure out the deltas:

{{% choosable "os" "macos,linux" %}}

```bash
$ pulumi up
```

{{% /choosable %}}
{{% choosable "os" "windows" %}}

```powershell
> pulumi up
```

{{% /choosable %}}

Just like the first time you will see a preview of the changes before they happen:

```
Previewing update (dev):

     Type                                                   Name                 Plan
     pulumi:pulumi:Stack                                    quickstart-dev
 +   ├─ azure-native:storage:StorageAccountStaticWebsite    staticWebsite        create
 +   └─ azure-native:storage:Blob                           index.html           create

Outputs:
  + staticEndpoint   : "https://sa8dd8af62.z22.web.core.windows.net/"

Resources:
    + 2 to create
    3 unchanged

Do you want to perform this update?
> yes
  no
  details
```

Choose `yes` to perform the deployment:

```
Do you want to perform this update? yes
Updating (dev):

     Type                                                   Name                Status
     pulumi:pulumi:Stack                                    quickstart-dev
 +   ├─ azure-native:storage:StorageAccountStaticWebsite    staticWebsite       created
 +   └─ azure-native:storage:Blob                           index.html          created

Outputs:
    primaryStorageKey: "<key_value>"
  + staticEndpoint   : "https://sa8dd8af62.z22.web.core.windows.net/"

Resources:
    + 2 created
    3 unchanged

Duration: 4s
```

In just a few seconds, your new website will be ready. Curl the endpoint to see it live:

{{% choosable os "linux,macos" %}}

```bash
$ curl $(pulumi stack output staticEndpoint)
```

{{% /choosable %}}

{{% choosable os "windows" %}}

```powershell
> curl (pulumi stack output staticEndpoint)
```

{{% /choosable %}}

This will reveal your new website!

```
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
```

Feel free to experiment, such as changing the contents of `index.html` and redeploying.

Next, wrap the website into an infrastructure abstraction.

{{< get-started-stepper >}}
