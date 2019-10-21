---
title: "Deploying with Octopus and Pulumi"
authors: ["sophia-parafina"]
tags: ["CI"]
meta_image: "octopus-pulumi.png"
meta_desc: "Continuous deployment"
date: "2019-10-15"
---

Continuous delivery is about making changes in your application and getting them into production securely, quickly in a consistent way. Pulumi's infrastructure as code approach uses source code to model cloud resources, making it ideal for continuous delivery. Your infrastructure code can go through the same process as your application code including running unit and integration tests, perform code reviews via Pull Requests, and examining your infrastructure using lingers or static analysis tools.  Like your application, your cloud infrastructure can be validated and tested before deploying to production. Pulumi can integrate into any CI/CD system (Jenkins, Azure DevOps, CircleCI, Spinnaker, TravisCI, GitLab CI, Codeship, NodeJS in Google Cloud, DigitalOcean, Codefresh and npm), so let's take a look at how to implement a deployment server.

[Octopus Deploy](https://octopus.com) is a deployment automation server that integrates with your existing build pipeline such as Jenkins, Azure DevOps or through a REST API. You can choose the environments for deploying your software and who can deploy them. For example, the QA team can only deploy to the Test environment but not to Development or Production. Different team members can trigger deployments but the deployment process is always consistent.

## Continuous Delivery with Octopus Deploy

Deployment targets are grouped in **environments** in Octopus. Environments represent different stages of the deployment pipeline that your software passes through on it's way to a release. A common practice is to create Development, Test, and Production environments which lets you define you deployment process. Octopus Deploy lets you deploy the correct versions of you software, with the right configuration and to the appropriate environment.

Pulumi's [guide](https://www.pulumi.com/docs/guides/continuous-delivery/octopus-deploy/) to implementing Octopus Deploy walks you through the process of implementing a environment for deploying a Python flask application on [AWS Fargate](https://aws.amazon.com/fargate/). Before starting, make sure you have met the [prerequisites](https://www.pulumi.com/docs/guides/continuous-delivery/octopus-deploy/#prerequisites).

Octopus environments are analogous to Pulumi stacks. If you have Development, Test, and Production Octopus environments, you would create a Pulumi stack for each environment. The application being deployed is a Pulumi project. Octopus uses packages which contain the source code bundled in a supported format such as .zip files, gzip or bzip tar files,  Java archive formats such as .jar or .war, and Docker images. Pulumi apps can be packaged in the desired format and extracted onto a Octopus worker that the Pulumi CLI can access.

Try deploying Pulumi applications with Octopus Deploy with our [continuous delivery guide](https://www.pulumi.com/docs/guides/continuous-delivery/octopus-deploy/).
