---
title: Container Management with Pulumi
layout: containers
url: /containers

meta_desc: Pulumi provides a cloud native programming model for container management. Any code, any cloud, any app.

hero:
    title: Manage Clusters and Deploy Containers with Ease
    body: >
        Pulumi supports managing clusters and their associated infrastructure,
        whether it is Kubernetes, Amazon ECS, Azure ACI, or Google GKE. Build
        and deploy application containers to private registies, all in one
        programming model. Any code, any cloud, any language.

sections:
    - id: what-is-container-management
      label: What is Container Management?
    - id: deploying-containers
      label: Deploying Containers
    - id: code
      label: Code
    - id: get-started
      label: Get Started
    - id: contact
      label: Talk to a human

examples:
    - title: Deploy Nginx to AWS Fargate
      body: >
          In this example, Pulumi defines and uses a new Amazon ECS Fargate cluster, and creates
          a load balanced service running the standard Nginx image from the Docker Hub. The same
          experience is available on other clouds and Pulumi can pull from any container registry.
      path: awsx-load-balanced-fargate-nginx
      cta:
          url: /docs/quickstart
          label: GET STARTED

    - title: Deploying with a custom build
      body: >
          This example builds a container image from a Dockerfile at <code>./app</code> and deploys
          it behind a load balancer with ECS Fargate.
      path: awsx-load-balanced-fargate-ecr
      cta:
          url: /docs/quickstart
          label: GET STARTED

    - title: Creating a Kubernetes cluster
      body: >
          Pulumi can provision Kubernetes clusters &mdash; in this example, an AWS EKS cluster &mdash;
          in addition to deploying application-level configuration, using a standard set of languages,
          abstractions, and tools.
      path: aws-eks-cluster
      cta:
          url: /docs/quickstart
          label: GET STARTED

    - title: Deploy containers to Microsoft ACI
      body: >
          The <code>@pulumi/azure-native</code> library provides fine-grained control of Azure resources. In this example,
          we deploy a simple linux container to Microsoft ACI, in the West US zone.
      code: |
          import * as containerinstance from "@pulumi/azure-native/containerinstance";
          import * as resources from "@pulumi/azure-native/resources";

          const resourceGroup = new resources.ResourceGroup("resourcegroup", {
              location: "West US",
          });

          const imageName = "mcr.microsoft.com/azuredocs/aci-helloworld";
          const containerGroup = new containerinstance.ContainerGroup("containerGroup", {
              resourceGroupName: resourceGroup.name,
              osType: "Linux",
              containers: [{
                  name: "acilinuxpublicipcontainergroup",
                  image: imageName,
                  resources: {
                      requests: {
                          cpu: 1.0,
                          memoryInGB: 1.5,
                      },
                  },
                  ports: [{ port: 80 }],
              }],
              ipAddresses: [{
                  ports: [{
                    port: 80,
                    protocol: "Tcp",
                  }],
                  type: "Public",
              }],
              restartPolicy: "always",
          });
      cta:
          url: /docs/quickstart
          label: GET STARTED

    - title: Invoke a long-running container as a task
      body: >
          This example shows a container used for executing a long-running task. Here, we use a container to
          perform a thumbnail extraction on a piece of video uploaded to an S3 bucket.
      path: aws-lambda-container-thumbnailer
      languages: javascript,typescript
      cta:
          url: /docs/quickstart
          label: GET STARTED
contact_us_form:
    section_id: contact
    hubspot_form_id: abf0bd4b-5e71-44a9-aad1-b55b5cce561d
    headline: Need help with container management?
    quote:
        title: Learn how top engineering teams are using Pulumi to manage containers in any cloud.
        name: Josh Imhoff
        name_title: Site Reliability Engineer, Cockroach Labs
        content: |
            We are building a distributed-database-as-a-service product that runs on Kubernetes clusters across multiple
            public clouds including Google Cloud, AWS and others. Pulumi's declarative model, the support for familiar programming
            languages, and the uniform workflow on any cloud make our SRE team much more efficient.
---
