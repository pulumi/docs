---
title_tag: "Export Audit Logs to AWS S3"
meta_desc: Learn how to configure automated export of Pulumi Cloud audit logs to an Amazon S3 bucket.
title: "Export to AWS S3"
h1: Export audit logs to AWS S3
menu:
  administration:
        name: Export to AWS S3
        parent: administration-security-compliance-audit-logs
        weight: 1
---

{{% notes "info" %}}
Automated export is only available on the Pulumi Business Critical Edition. If you don't see it in your organization, [contact sales](/contact?form=sales).
{{% /notes %}}

Pulumi Cloud can continuously export audit log events to an Amazon S3 bucket. Once configured, new events are delivered automatically — no manual downloads or API polling required.

## Configure export using the console

1. Navigate to the organization's **Settings**.
1. Navigate to **Audit Logs**.
1. Use the three-dot menu and select **Configure Audit Logs to S3**.

   <img src="/images/docs/reference/console/ale-menu.png" alt="Audit log export menu showing the Configure Audit Logs to S3 option">

1. Follow the instructions to create an AWS S3 bucket.
1. Provide a bucket name and a filepath where Pulumi audit logs will be exported, e.g., `Pulumi-audit-logs`.
1. Copy the provided policy.
1. In the AWS console create an IAM role.
1. Select **Another AWS Account** and check **Require external ID**.
1. Provide the Account ID and External ID, then attach the policy you created.
1. Provide the ARN of the IAM role.
1. Test your configuration.

   <img src="/images/docs/reference/console/test-ale-configuration.png" alt="Testing the audit log export configuration">

1. After a successful test, select **Save and Apply**.
1. After an hour, verify that logs have successfully started exporting.

   <img src="/images/docs/reference/console/ale-success.png" alt="Successful audit log export configuration">
