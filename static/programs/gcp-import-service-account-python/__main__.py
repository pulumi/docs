import pulumi
from pulumi_gcp import serviceaccount, config

project_id = config.project
service_acct_email_suffix = f"@{project_id}.iam.gserviceaccount.com"
service_acct_display_name = "pulumi-tutorial-service-account" # REPLACE
service_acct_email_prefix = "pulumi-tutorial-service-accoun" # REPLACE

imported_tutorial_service_account = serviceaccount.Account("imported-tutorial-service-account",
    account_id=service_acct_email_prefix,
    display_name=service_acct_display_name, 
    project=project_id,
    opts = pulumi.ResourceOptions(
        import_= f"{service_acct_email_prefix}{service_acct_email_suffix}"
    )
)