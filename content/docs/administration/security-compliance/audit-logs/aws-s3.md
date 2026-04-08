---
title_tag: "Export Audit Logs to AWS S3"
meta_desc: Learn how to configure automated export of Pulumi Cloud audit logs to an Amazon S3 bucket.
title: "Export to AWS S3"
h1: Export audit logs to AWS S3
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
        name: Export to AWS S3
        parent: administration-security-compliance
        weight: 4
---

{{% notes "info" %}}
Automated export is only available on the Pulumi Business Critical Edition. If you don't see it in your organization, [contact sales](/contact?form=sales).
{{% /notes %}}

Pulumi Cloud can continuously export audit log events to an Amazon S3 bucket. Once configured, new events are delivered automatically — no manual downloads or API polling required.

## Configure export using the console

1. Navigate to the organization's **Settings**.
1. Navigate to **Audit Logs**.
1. Use the three dot menu and select **Configure Audit Logs to S3**.

   <img src="/images/docs/reference/console/ale-menu.png">

1. Follow the instructions to create an AWS S3 bucket.
1. Provide bucket name and a filepath where Pulumi audit logs will be exported eg: 'Pulumi-audit-logs'.
1. Copy the provided policy.
1. In the AWS console create an IAM role.
1. Select **Another AWS Account** and check **Require external ID**.
1. Provide the Account ID and External ID, then attach the policy you created.
1. Provide the arn of the IAM role.
1. Test your configuration.

   <img src="/images/docs/reference/console/test-ale-configuration.png">

1. After a successful test, select **Save and Apply**.
1. After an hour, verify that logs have successfully started exporting.

   <img src="/images/docs/reference/console/ale-success.png">
