---
title_tag: "Export Audit Logs to AWS S3"
meta_desc: Learn how to configure automated export of Pulumi Cloud audit logs to an Amazon S3 bucket.
title: "Export to AWS S3 (or S3-compatible)"
h1: Export audit logs to AWS S3
menu:
  administration:
        name: Export to AWS S3 (or S3-compatible)
        parent: administration-guides-audit-logs
        weight: 2
pulumi_cloud_feature: audit-log-export
aliases:
  - /docs/administration/security-compliance/audit-logs/aws-s3/
  - /docs/administration/guides/export-audit-logs/aws-s3/
---

Pulumi Cloud can continuously export audit log events to an Amazon S3 bucket. Once configured, new events are delivered automatically — no manual downloads or API polling required.

## Configure export using the console

### AWS S3

1. Navigate to the organization's **Settings**.
1. Navigate to **Audit Logs**.
1. Use the three-dot menu and select **Configure export to Amazon S3 / S3-compatible**.

   <img src="/images/docs/reference/console/ale-menu.png" alt="Audit log export menu showing the Configure Audit Logs to S3 option">

1. Select **Amazon S3**.
1. Follow the instructions to create an AWS S3 bucket.
1. Provide a bucket name and a filepath where Pulumi audit logs will be exported, e.g., `Pulumi-audit-logs`.
1. Copy the provided policy.
1. In the AWS console create an IAM role.
1. Select **Another AWS Account** and check **Require external ID**.
1. Provide the Account ID and External ID, then attach the policy you created.
1. Provide the ARN of the IAM role.
1. Test your configuration.

   <img src="/images/docs/reference/console/test-ale-configuration.png" alt="Testing the audit log export configuration">

1. After a successful test, select **Save and apply configuration**.
1. After an hour, verify that logs have successfully started exporting.

   <img src="/images/docs/reference/console/ale-success.png" alt="Successful audit log export configuration">

### S3-compatible service

Pulumi Cloud can also export audit logs to a storage service that implements the Amazon S3 API. Pulumi Cloud authenticates to the service with an access key instead of an IAM role.

1. Navigate to the organization's **Settings**.
1. Navigate to **Audit Logs**.
1. Use the three-dot menu and select **Configure export to Amazon S3 / S3-compatible**.
1. Select **S3-compatible service**.
1. Provide the **Endpoint URL** of the service. The endpoint must use `https` and must be reachable from Pulumi Cloud.
1. Optionally, provide the **Region** that the service uses to sign requests. If you leave it empty, Pulumi Cloud uses `us-east-1`.
1. Provide a **Bucket name** and a **File path prefix** where Pulumi audit logs will be exported.
1. Create an access key that can write objects under the file path prefix, then provide its **Access key ID** and **Secret access key**.
1. Test your configuration.
1. After a successful test, select **Save and apply configuration**.
1. After an hour, verify that logs have successfully started exporting.

Pulumi Cloud encrypts the secret access key and never shows it again. To change other settings later, leave **Secret access key** empty and Pulumi Cloud keeps the saved secret. If you change the endpoint URL or the access key ID, you must provide the secret access key again.

{{% notes type="info" %}}
On a self-hosted installation, to export to a service on a private network, list `AUDIT_LOG_EXPORT` in `PULUMI_DISABLE_SSRF_PROTECTION`. See [SSRF protection](/docs/administration/self-hosting/components/api/#ssrf-protection).
{{% /notes %}}
