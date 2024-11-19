import pulumi
import pulumi_azure_native as azure_native

subscription_id = "0282681f-7a9e-424b-80b2-96babd57a8a1" # your subscription ID
resource_group_name = "pulumi-tutorial-resource-group2" # name of the virtual machine resource group
lookup_prop = f"/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}"

imported_resource_group = azure_native.resources.ResourceGroup("imported-rg",
    opts = pulumi.ResourceOptions(import_= lookup_prop)
)