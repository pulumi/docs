---
title: What is Google Cloud Secret Manager?
meta_desc: |
     Learn more about what Google Cloud Secret Manager is and how to use it.

meta_image: /images/what-is/what-is-google-cloud-secret-manager-meta.png
type: what-is
page_title: "What is Google Cloud Secret Manager?"
authors: ["torian-crane"]
---

Google Cloud is a leader in cloud computing, transforming the way organizations manage their digital infrastructure. An important aspect of Google Cloud’s security framework is the management of sensitive data, commonly known as "[secrets](/what-is/what-is-secrets-management/)". [Google Cloud Secret Manager](https://cloud.google.com/secret-manager) is a service designed for the secure handling of these secrets, offering tools for storing, accessing, and managing confidential information in the cloud.

## What is Google Cloud Secret Manager?

Google Cloud Secret Manager is a cloud service provided by Google Cloud for managing, securing, and accessing sensitive data such as API keys, passwords, and certificates. It offers a centralized solution for storing and controlling access to private information, ensuring a high level of security within the Google Cloud environment.

### Key features

- **Centralized and secure storage**: Secret Manager provides a central place to store and manage secrets, with built-in encryption at rest.
- **Fine-grained access control**: It integrates with Google Cloud’s Identity and Access Management (IAM) to control access to secrets.
- **Versioning and audit logging**: Secret Manager supports versioning of secrets and provides audit logs, enabling tracking of secret access and changes over time. Note that data access activities are not logged by default and must be [explicitly enabled](https://cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable).

## Creating Google Cloud Secret Manager secrets

Google Cloud Secret Manager secrets can be created via the gcloud CLI. Before creating secrets in Google Cloud, you must first make sure you have [created a Google Cloud project with the Secret Manager API enabled](https://cloud.google.com/secret-manager/docs/configuring-secret-manager).

You will then need to install the [gcloud CLI](https://cloud.google.com/cli). Once you have installed the gcloud CLI, run the `gcloud auth login` command to [authenticate to your Google Cloud account](https://cloud.google.com/sdk/gcloud/reference/auth/login).

```bash
# Example gcloud auth login interaction and output
$ gcloud auth login
Go to the following link in your browser:

    https://accounts.google.com/o/oauth2/auth?...

Enter authorization code: 4/0A....

You are now logged in as [your@email.com].
Your current project is [your-project].  You can change this setting by running:
  $ gcloud config set project PROJECT_ID
```

### Create a secret via the CLI

You can create a secret by running the `gcloud secrets create` command:

```bash
$ gcloud secrets create my-secret

Created secret [my-secret].
```

Now add your secret data to the secret as shown below:

```bash
$ echo -n "my-secret-data" | gcloud secrets versions add my-secret --data-file=-

Created version [1] of the secret [my-secret].
```

Verify the secret was created with the `gcloud secrets list` command.

```bash
$ gcloud secrets list

NAME         CREATED              REPLICATION_POLICY  LOCATIONS
api-key      2023-10-09T09:04:30  automatic           -
my-secret    2023-11-30T14:05:58  automatic           -
test-secret  2023-11-10T09:40:29  automatic           -
```

{{< notes type="info" >}}

Many infrastructure as code platforms, including Pulumi, have support for creating secrets. You can learn more about how to create and manage secrets in Pulumi by taking a look at [Pulumi Secrets documentation](/docs/concepts/secrets/).

{{< /notes >}}

## Accessing Google Cloud Secret Manager secrets

Now that you have created a Google Cloud Secret Manager secret, you can access the value via the gcloud CLI using the `gcloud secrets versions access` command.

```bash
$ gcloud secrets versions access latest --secret="my-secret"

my-secret-data
```

## Best practices

- **Regularly rotate secrets**: Implement a strategy for the regular rotation of secrets.
- **Provide least-privilege access**: Minimize the number of entities with access to the secret.
- **Monitor access and usage**: Utilize Google Cloud’s audit logs to monitor and track access to secrets.

## Challenges and considerations

Google Cloud Secret Manager, while a powerful tool for managing secrets and cryptographic keys, does come with its own set of challenges, considerations, and limitations. Some of the key aspects to be aware of include:

- **Quotas and limits on secret access**: When retrieving secrets frequently, such as in SaaS applications that make API calls, it's important to ensure that project-level quotas are sufficient. Secret Manager has a limit of 90,000 access requests per minute per project, which can be increased via a Google Cloud support ticket. Additionally, there are limits on the size of the secret value (64 KiB) and the number of aliases a secret can have (50 aliases).
- **Lack of auto-rotation for secrets**: Currently, Google Cloud Secret Manager does not have the capability to auto-rotate secrets. This means organizations need to implement their own mechanisms to ensure secrets are rotated in compliance with their security policies.
- **Logging and audit considerations**: Accessing a secret in Google Cloud Secret Manager is not logged by default. However, users can enable granular access logs on secrets and retrieve this data through Google Cloud’s Logs Explorer. This requires activation of relevant data access logs in the Cloud Audit Logs service. Additionally, frequent access logging can lead to large bills, so it’s important to evaluate the necessity of logging every secret request and configure custom retention policies accordingly.

Understanding and addressing these challenges and considerations is key to effectively leveraging Google Cloud Secret Manager in a cloud infrastructure, ensuring that the management of secrets aligns with the organization's security and compliance requirements.

## Conclusion

Secret Manager solves storage and access control, but it deliberately leaves the operational hard parts to you: it does not rotate secrets on its own, and it does not log secret access until you turn that logging on and pay for it. The security of your setup therefore lives less in the service itself than in the rotation policies, IAM scoping, and audit configuration you build around it. Treat Secret Manager as the secure vault, and treat those surrounding practices as the part you actually own.

To manage Secret Manager secrets as code alongside the rest of your Google Cloud infrastructure, see [deploying and managing Google Secret Manager secrets](/registry/packages/gcp/api-docs/secretmanager/secret/) with Pulumi.

The [Pulumi community on Slack](https://slack.pulumi.com/) is open for questions and discussion.
