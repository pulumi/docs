---
title: Pulumi vs. Serverless Framework
meta_desc: Pulumi allows for a more holistic approach than the Serverless Framework, writing entire applications using an infrastructure-as-code approach.
linktitle: Serverless
menu:
  intro:
    parent: vs
    weight: 5

aliases: ["/docs/reference/vs/serverless/"]
---

The Serverless Framework is a tool that makes programming AWS Lambda, Azure Functions, and Google Cloud Functions
easier, by removing much of the boilerplate out of the native cloud providers' development experiences. It generates
the YAML and configuration required for functions, and simplifies uploading code packs to the cloud. The Serverless Framework relies on
the cloud provider's APIs or templating solutions for any provisioning or management beyond the functions themselves.

Pulumi is more holistic than the Serverless Framework in its focus. In [Pulumi] ({{< relref "/" >}}), you write entire applications -- some parts of which may be serverless
functions -- but this might also include containers, databases, cloud services, or even virtual machines. It then uses
an infrastructure-as-code approach to deploy, update, and generally manage these constellations of resources.

Where Serverless Framework treats each function as a configurable entity, Pulumi views the entire program as a cloud native
program. This means in practice that most Serverless Framework solutions also need to involve other solutions -- like
AWS CloudFormation -- and that you as a user are left orchestrating changes in multiple systems.
This often leads to the very "pile of bash scripts" problems that you had sought to solve in the first place.

For a good specific comparison of Pulumi and the Serverless Framework, refer to this example: [the before code using
the Serverless Framework](
https://serverless.com/blog/serverless-application-for-long-running-process-fargate-lambda/) takes about 38 pages
of explanation, including manual steps and AWS CloudFormation; [the after code using Pulumi](
https://github.com/pulumi/examples/tree/master/cloud-js-thumbnailer) is only about 38 lines of code.

Follow our blog for updates on [new features] (https://www.pulumi.com/blog/tag/new-features/), and if you have any questions about Pulumi, feel free to [contact us] (https://www.pulumi.com/contact/) any time.
