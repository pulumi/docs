---
title: Quickstart tutorials
---

<!-- LINKS: -->
[Pulumi examples repo]: https://github.com/pulumi/examples
<!-- END LINKS: -->

Pulumi is a open-source tool and service that makes it easier to build modern cloud applications on AWS, Azure, GCP, and Kubernetes. With Pulumi, you can use JavaScript or Python to build serverless applications, manage low-level infrastructure, orchestrate containers --- or anything in between. You can use raw cloud resources, higher-level components built on top of them, or a combination of both.

Because Pulumi supports general-purpose programming languages, you don’t have to learn a custom configuration language. You can bring software engineering to the task of defining cloud infrastructure, with reusable libraries, type checking, IDE tooling, and testing.

## Getting started

Follow these steps deploy a simple serverless app to AWS. 

```bash
# Step 1. Install Pulumi
curl -fsSL https://get.pulumi.com | sh

# Step 2. Create a new project
pulumi new hello-aws-javascript

# Step 3. Deploy to the cloud
pulumi update
```

If you're using Windows, follow [these steps to install Pulumi](../install#windows).

If you haven't already configured the AWS CLI, [follow these steps](../install/aws.html). Make sure you also have [Node.js](https://nodejs.org/en/download/
) installed. 

## 5-minute quickstarts

- [Create a serverless REST API](./aws-rest-api.html)
- [Host a static site on S3](./aws-s3-website.html)
- [Create EC2 instances on AWS](./aws-ec2.html)
- Provision containers on AWS (coming soon!)

## Examples

We have a number of code examples available in the [Pulumi examples repo] on GitHub. If you don't have access to the GitHub repo, please email [support@pulumi.com](mailto:support@pulumi.com) to get access, or download the [Pulumi examples zipfile](/examples/pulumi-examples.zip).

To learn more, check out the [featured example list](./examples.html).