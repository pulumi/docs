---
title: "Introducing Pulumi ESC SDK: Streamline Your Application Secrets Management"
allow_long_title: true
date: 2024-06-05T00:00:00-07:01
draft: false
meta_desc: "The new Pulumi ESC SDK allows developers to seamlessly integrate Pulumi ESC with their applications for secrets management"
meta_image: "meta.png"
authors:
  - arun-loganathan
  - cleve-littlefield
tags:
  - esc
  - secrets
  - features
---

Managing secrets and application configurations effectively is crucial for building secure and maintainable software. However, developers often face challenges such as hardcoded credentials, configuration inconsistencies, and security risks. [Pulumi Environments Secrets and Configuration](/product/esc) (ESC) simplifies the management of sensitive data and configuration across your entire application lifecycle. Today, we're thrilled to introduce the official Pulumi ESC SDK in Typescript, Go, and Python, making it even easier to integrate ESC directly into your applications.

<!--more-->

## Primer on Pulumi ESC

Pulumi ESC (Environments, Secrets, and Configuration) provides a developer-first solution to simplify how you manage sensitive data and configuration across your entire application lifecycle. It's a fully managed solution allowing teams to generate [dynamic cloud provider](/docs/esc/providers/) credentials, aggregate secrets and configuration from multiple sources, and manage them through composable collections called "[environments](/docs/esc/environments/)." These environments can be consumed from anywhere, making Pulumi ESC ideal for any [application and development workflow](docs/esc/other-integrations/). Additionally, while Pulumi ESC works independently to eliminate duplication and reduce drift and sprawl of secrets and configuration for all your applications, it also [integrates](/docs/esc/get-started/integrate-with-pulumi-iac/) smoothly with Pulumi Infrastructure as Code (IaC) to enhance these capabilities within the Pulumi ecosystem.

## Introducing the Pulumi ESC SDK

We're excited to unveil the official Pulumi ESC SDK, making it even easier to harness the power of ESC directly within your applications using your favorite programming languages. The SDK provides a simple programmatic interface to all of Pulumi ESC's robust features, allowing you to:

- **Manage the Entire Lifecycle of Your Environments:** Create new environments, list existing ones, and easily update or delete them as your needs evolve. You can even add version tags to your environments, making it simple to track changes and roll back to previous states if needed.
- **Seamlessly Integrate Secrets and Configurations:** Securely access and utilize secrets and configurations within your applications, ensuring consistency of configuration across environments. The SDK provides a streamlined way to fetch the information you need, whether it's dynamic cloud credentials, database connection strings, feature flags, or any other sensitive data.

The Pulumi ESC SDK streamlines secret and configuration management, promoting secure handling best practices. It handles the secure storage and retrieval of your sensitive data at runtime, eliminating the need to store credentials long-term and minimizing the risk of accidental exposure. The SDK is a natural extension of your development workflow, offering familiar objects and methods, smooth integration with your IDE, and the benefits of type safety such as compile-time checks and helpful code suggestions that reduce errors and accelerate development.

## How to Get Started

Here are a few examples of how to use the ESC SDK for various languages:

{{< chooser language "typescript,python,go" />}}

{{% choosable language typescript %}}

```typescript

```

{{% /choosable %}}

{{% choosable language python %}}

```python

```

{{% /choosable %}}

{{% choosable language go %}}

```go

```
{{% /choosable %}}

## Real-World Examples: Pulumi ESC SDK in Action

Here are some real-world scenarios showcasing how you can leverage the Pulumi ESC SDK:

- **Secure Serverless Deployments**: Access your AWS S3 buckets securely from your Lambda functions. The ESC SDK lets you retrieve temporary AWS credentials at runtime:
```python
  aws_creds = esc_sdk.get_secret("aws-credentials")
  s3_client = boto3.client('s3', **aws_creds)
```
- **Microservices Configuration**:  Keep your microservices configuration consistent across environments. Fetch the correct values for each service at runtime using the SDK:
```python
api_endpoint = esc_sdk.get_config("service-a", "api_endpoint")
```
- **Database Connection String Management**: Securely connect to your database without embedding sensitive credentials in your code. The ESC SDK retrieves the appropriate connection string based on your environment:
```csharp
string dbConnectionString = escSdk.GetSecret("prod-database-connection");
```
- **Secure Third-Party Service Integrations**: Manage API keys and access tokens for external services like Stripe or Twilio with ease. The SDK ensures these credentials are securely stored and accessed:
```typescript
const stripeSecretKey = escSdk.getSecret("stripe-secret-key");
```

## Get Started Today!

The Pulumi ESC SDK is available now! To learn more and start simplifying your application secrets workflow, check out the Pulumi ESC SDK Documentation. We're confident that this powerful new tool will streamline your development process, enhance your application security, and empower you to build innovative solutions with confidence. Join us on this journey towards a more secure and manageable future for application secrets and configurations!
