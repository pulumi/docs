---
title_tag: Templates for Deploying Serverless Applications
title: Serverless Templates
layout: overview
schema_type: faq
description: Pulumi templates for serverless applications on AWS, Azure, and Google Cloud, in your language of choice.
meta_desc: Deploy serverless applications on AWS, Azure, or Google Cloud with Pulumi Serverless Application templates.
meta_image: meta.png
weight: 1
---

## About these templates

### What is a serverless application?

A [serverless](/serverless/) application runs on managed cloud services that scale automatically, are highly available by default, and bill only for what you use. You write the application code (typically as a function) and the cloud provider handles the runtime, capacity, and underlying servers.

### Which serverless services should I use on each cloud?

The major clouds expose comparable building blocks for serverless web and event-driven applications:

- **AWS**: [AWS Lambda](/registry/packages/aws/api-docs/lambda/function/) for the function runtime, [Amazon API Gateway](/registry/packages/aws/api-docs/apigateway/restapi/) for HTTP routing, and [Amazon S3](/registry/packages/aws/api-docs/s3/bucket/) for static assets.
- **Azure**: [Azure Functions](/registry/packages/azure-native/api-docs/web/webappfunction/) for the function runtime and [Azure Blob Storage](/registry/packages/azure-native/api-docs/storage/storageaccount/) configured for [static website hosting](/registry/packages/azure-native/api-docs/storage/storageaccountstaticwebsite/).
- **Google Cloud**: [Cloud Functions Gen 2](/registry/packages/gcp/api-docs/cloudfunctionsv2/function/) for the function runtime and [Cloud Storage](/registry/packages/gcp/api-docs/storage/bucket/) for static assets.

### How do I deploy a serverless application with Pulumi?

Use one of the Serverless Application templates above to scaffold a Pulumi project that provisions both the function runtime and the surrounding infrastructure (storage, routing, IAM). Each template ships placeholder web and function content so the project deploys end to end with `pulumi new` followed by `pulumi up`.

### Can I manage my function code in the same project as my infrastructure?

Yes. Each template includes the function source alongside the Pulumi program, so you can deploy infrastructure and application changes together as a single unit, version them in the same repository, and roll them back with one `pulumi destroy`.
