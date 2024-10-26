---
title: write a blog post about pulumi esc
description: # Managing AWS Secrets with Pulumi ESC
language: TypeScript
---
    # Managing Secrets and Configuration with Pulumi ESC

In modern cloud-native applications, managing secrets and configuration securely is crucial. Pulumi provides a robust solution for this with its Encrypted Secrets Configuration (ESC). In this blog post, we'll explore how to use Pulumi ESC to manage secrets and configuration in a secure and efficient manner.

## What is Pulumi ESC?

Pulumi ESC is a feature that allows you to store secrets and configuration in a secure, encrypted format. This ensures that sensitive information, such as API keys, passwords, and other secrets, is not exposed in your infrastructure code or configuration files.

### Key Benefits of Pulumi ESC:
1. **Security**: Secrets are encrypted both at rest and in transit.
2. **Ease of Use**: Seamlessly integrates with Pulumi's infrastructure as code approach.
3. **Flexibility**: Supports various cloud providers and services.

## Setting Up Pulumi ESC

To demonstrate how to use Pulumi ESC, we'll create a simple AWS Secrets Manager secret using Pulumi. AWS Secrets Manager is a service that helps you protect access to your applications, services, and IT resources without the upfront cost and complexity of managing your own hardware security modules (HSMs).

### Prerequisites:
1. [Pulumi CLI](https://www.pulumi.com/docs/get-started/install/)
2. An AWS account
3. Node.js installed

### Step-by-Step Guide

1. **Initialize a New Pulumi Project**:
   ```sh
   mkdir pulumi-esc-demo
   cd pulumi-esc-demo
   pulumi new aws-typescript
   ```

2. **Install the AWS Pulumi Package**:
   ```sh
   npm install @pulumi/aws
   ```

3. **Create a Secret in AWS Secrets Manager**:
   In your `index.ts` file, add the following code:

   ```typescript
   import * as pulumi from "@pulumi/pulumi";
   import * as aws from "@pulumi/aws";

   // Create a new secret in AWS Secrets Manager
   const mySecret = new aws.secretsmanager.Secret("mySecret", {
       description: "My secret managed by Pulumi",
   });

   // Store a secret value
   const secretValue = new aws.secretsmanager.SecretVersion("mySecretValue", {
       secretId: mySecret.id,
       secretString: pulumi.secret("mySuperSecretValue"),
   });

   // Export the secret ARN
   export const secretArn = mySecret.arn;
   ```

   ### Explanation:
   - We import the necessary Pulumi and AWS packages.
   - We create a new secret in AWS Secrets Manager using `aws.secretsmanager.Secret`.
   - We store a secret value using `aws.secretsmanager.SecretVersion` and encrypt it using `pulumi.secret`.
   - Finally, we export the ARN of the secret for reference.

4. **Run Pulumi Up**:
   ```sh
   pulumi up
   ```

   Pulumi will show you a preview of the changes that will be made. Confirm the changes, and Pulumi will create the secret in AWS Secrets Manager.

5. **Verify the Secret in AWS Console**:
   Navigate to the AWS Secrets Manager console to verify that the secret has been created and the value is stored securely.

## Conclusion

Pulumi ESC provides a powerful way to manage secrets and configuration securely. By leveraging Pulumi's infrastructure as code capabilities, you can ensure that your sensitive information is protected while maintaining the flexibility and ease of use that Pulumi offers.

### Additional Resources:
- [Pulumi Documentation on Secrets](https://www.pulumi.com/docs/intro/concepts/secrets/)
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)

This blog post should give you a good starting point for managing secrets with Pulumi ESC. Happy coding!