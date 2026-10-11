import pulumi
import pulumi_azure_native as azure_native

client_config = azure_native.authorization.get_client_config()
subscription_id = client_config.subscription_id
resource_group_name = pulumi.Config().get("resourceGroupName") # REPLACE
lookup_prop = f"/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}"

imported_resource_group = azure_native.resources.ResourceGroup("imported-rg",
    opts = pulumi.ResourceOptions(import_= lookup_prop)
)