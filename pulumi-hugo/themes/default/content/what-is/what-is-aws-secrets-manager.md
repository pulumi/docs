---
title: What is AWS Secrets Manager?
meta_desc: |
     Learn more about what AWS Secrets Manager is and how to use it.

type: what-is
page_title: "What is AWS Secrets Manager?"
---

Amazon Web Services (AWS) is a leader in cloud computing, transforming the way organizations manage their digital infrastructure. A critical aspect of this landscape is the management of sensitive data, commonly known as "[secrets](/what-is/what-is-secrets-management/)". AWS Secrets Manager is a service designed for the secure handling of these secrets, offering tools for storing, accessing, and managing confidential information in the cloud. 

## What is AWS Secrets Manager?

AWS Secrets Manager is a cloud service for managing, retrieving, and storing sensitive information such as database credentials, API keys, and other secrets. It helps in securing access to applications, services, and IT resources without hard-coding sensitive information in plain text.

### Key features

- **Secure and Encrypted Storage**: Secrets in AWS Secrets Manager are encrypted during transit and at rest, ensuring a high level of security.
- **Secrets Lifecycle Management**: AWS Secrets Manager allows you to rotate, manage, and retrieve secrets throughout their lifecycle without disrupting the applications.
- **Fine-grained Access Control**: You can control access to secrets using AWS Identity and Access Management (IAM) policies.

## Creating AWS Secrets Manager secrets

AWS Secrets Manager secrets can be created via the AWS CLI. Before creating secrets in AWS, you must first make sure you have the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) installed. Once you have installed the AWS CLI, run the `aws configure` command to [set up your AWS credentials](https://docs.aws.amazon.com/cli/latest/reference/configure/).

```bash
$ aws configure

AWS Access Key ID [None]: ********
AWS Secret Access Key [None]:  ********
Default region name [None]:  ********
Default output format [None]:  ********
```

### Create a secret via the CLI

You can create a secret by running the `aws secretsmanager create-secret` command:

```bash
$ aws secretsmanager create-secret --name MySecretName --secret-string "MySecretValue"

{
    "ARN": "arn:aws:secretsmanager:eu-central-1:111111111111:secret:MySecretName-86zArI",
    "Name": "MySecretName",
    "VersionId": "41c3c47e-4542-438c-929f-92f02d3261e4"
}
```

Verify the secret was created with the `aws secretsmanager list-secrets` command.

```bash
$ aws secretsmanager list-secrets
{
    "SecretList": [
        {
            "ARN": "arn:aws:secretsmanager:eu-central-1:111111111111:secret:MySecretName-86zArI",
            "Name": "MySecretName",
            "LastChangedDate": "2023-11-28T17:16:05.840000+00:00",
            "SecretVersionsToStages": {
                "41c3c47e-4542-438c-929f-92f02d3261e4": [
                    "AWSCURRENT"
                ]
            },
            "CreatedDate": "2023-11-28T17:16:05.791000+00:00"
        }
    ]
}
```

## Accessing Secrets Manager secrets

Now that you have created a Secrets Manager secret, you can access the value via the AWS CLI using the `aws secretsmanager get-secret-value` command.

```bash
$ aws secretsmanager get-secret-value --secret-id MySecretName
{
    "ARN": "arn:aws:secretsmanager:eu-central-1:111111111111:secret:MySecretName-86zArI",
    "Name": "MySecretName",
    "VersionId": "41c3c47e-4542-438c-929f-92f02d3261e4",
    "SecretString": "MySecretValue",
    "VersionStages": [
        "AWSCURRENT"
    ],
    "CreatedDate": "2023-11-28T17:16:05.836000+00:00"
}
```

## Challenges and considerations

AWS Secrets Manager is a powerful tool for managing secrets and cryptographic keys, but  it does come with its own set of challenges, considerations, and limitations. Some of the key aspects to be aware of include:

- **Compatibility and Integration**: AWS Secrets Manager primarily integrates with AWS services and applications. Integrating it with on-premises applications might require additional configurations.
- **Cost Management**: While AWS Secrets Manager offers robust features, it is important to manage costs associated with the number of API calls and secret versions.
- **API Request Quotas and Throttling**: AWS Secrets Manager has quotas on the rate of API requests. For example, the combined rate of certain API requests like DescribeSecret and GetSecretValue is limited to 10,000 transactions per second per region. Exceeding these limits can result in throttling, where valid requests are rejected and a throttling error is returned.

Understanding the limitations of AWS Secrets Manager and effectively planning its usage are crucial for seamless integration into your AWS infrastructure. Properly addressing these challenges and considerations is key to leveraging the full benefits of the service.
Best Practices
Rotate Secrets Regularly: Implement a routine for regularly rotating secrets to enhance security.
Provide Least-Privilege Access: Employ IAM policies for granular access control to secrets.
Audit and Monitor Secret Access: Use AWS CloudTrail and other monitoring tools to track access and modifications to your secrets.

## Conclusion

AWS Secrets Manager is an essential tool for secure secret management in cloud environments, particularly for applications running on AWS. Properly utilizing AWS Secrets Manager can significantly strengthen the security and management of sensitive data in cloud applications. Consider exploring more AWS services and tools to enhance your cloud infrastructure's security and management efficiency.

Now that you’re equipped with the knowledge of AWS Secrets Manager, take your cloud infrastructure management to the next level with Pulumi. Explore these key resources to deepen your understanding and enhance your implementation strategies:

- **Provision Infrastructure as Code**: Learn about deploying and managing AWS Secrets Manager secrets as well as other AWS resources using Pulumi's Infrastructure as Code capabilities. For comprehensive insights, refer to [Pulumi's AWS Provider documentation](/registry/packages/aws/).
- **Advanced Secrets Management**: Explore Pulumi’s detailed guides on the centralized management of secrets in cloud applications, particularly with Pulumi ESC (Environments, Secrets, and Configurations). For more information, visit the [Pulumi ESC documentation for the AWS Secrets provider](/docs/pulumi-cloud/esc/providers/aws-secrets/).

Our [community on Slack](https://slack.pulumi.com/) is always open for discussions, questions, and sharing experiences. Join us there and become part of our growing community of cloud professionals!
