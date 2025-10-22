import pulumi
import pulumi_azure_native as azure_native

resource_group = azure_native.resources.ResourceGroup("resource-group")

storage_account = azure_native.storage.StorageAccount(
    "storageaccount",
    resource_group_name=resource_group.name,
    kind="StorageV2",
    sku={
        "name": "Standard_LRS",
    },
)

blob_container = azure_native.storage.BlobContainer("blobcontainer",
    account_name=storage_account.name,
    resource_group_name=resource_group.name
)

resource_group_name = resource_group.name
storage_account_name = storage_account.name
blob_container_name = blob_container.name

blob_resource = azure_native.storage.Blob("blobresource",
    account_name=storage_account_name,
    container_name=blob_container_name,
    resource_group_name=resource_group_name,
    access_tier=azure_native.storage.BlobAccessTier.HOT,
    source=pulumi.StringAsset("content"),
    type=azure_native.storage.BlobType.BLOCK
)

pulumi.export("resourceGroupName", resource_group.name)
pulumi.export("storageAccountName", storage_account.name)
pulumi.export("blobContainerName", blob_container.name)
