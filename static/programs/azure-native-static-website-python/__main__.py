import pulumi
import pulumi_azure_native as azure_native
import pulumi_synced_folder as synced_folder

path = "./wwwroot"
index_document = "index.html"
error_document = "error.html"

#### Steps:
# [1] Create a resource group.
# [2] Create a blob storage account.
# [3] Configure the storage account as a website.

# [1] Create a resource group.
resource_group = azure_native.resources.ResourceGroup( "website-resource-group",
    location="eastus"
)

# [2] Create a blob storage account.
storage_account = azure_native.storage.StorageAccount(
    "websiteblob",
    resource_group_name=resource_group.name,
    kind="StorageV2",
    sku={
        "name": "Standard_LRS",
    }
)

# [3] Configure the storage account as a website.
website = azure_native.storage.StorageAccountStaticWebsite(
    "website",
    account_name=storage_account.name,
    resource_group_name=resource_group.name,
    index_document=index_document,
    error404_document=error_document,
)

# Upload the website files.
synced_folder = synced_folder.AzureBlobFolder(
    "synced-folder",
    path=path,
    resource_group_name=resource_group.name,
    storage_account_name=storage_account.name,
    container_name=website.container_name,
)

# Export the URL of the website.
pulumi.export("staticEndpoint", storage_account.primary_endpoints.web)