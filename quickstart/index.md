---
title: Quickstart tutorials
---

<!-- LINKS: -->
[Pulumi examples repo]: https://github.com/pulumi/examples
<!-- END LINKS: -->

Pulumi is a open-source tool and service that makes it easier to build modern cloud applications on AWS, Azure, GCP, and Kubernetes. Instead of using a configuration language, you use JavaScript or Python to define your desired cloud resources. 

Resources are declared with syntax like `new aws.ec2.Instance` in JavaScript or `ec2.Instance(...)` in Python. Pulumi is based on the concept of _immutable infrastructure_. Unlike Boto scripts that mutate infrastructure when they are run, Pulumi runs your program to determine the desired set of resources. Then, Pulumi makes only the minimal required changes to your infrastructure, without disrupting existing resources.

## 5-minute quickstarts

- [Create a serverless REST API](./aws-rest-api.html)
- [Host a static site on S3](./aws-s3-website.html)
- [Create EC2 instances on AWS](./aws-ec2.html)
- Provision containers on AWS (coming soon!)

## Examples

We have a number of code examples available in the [Pulumi examples repo] on GitHub. If you don't have access to the GitHub repo, please email [support@pulumi.com](mailto:support@pulumi.com) to get access, or download the [Pulumi examples zipfile](/examples/pulumi-examples.zip).

To learn more, check out the [featured example list](./examples).