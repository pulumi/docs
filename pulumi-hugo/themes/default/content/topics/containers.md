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
        programming model.


        Any code, any cloud, any language.
    code: |
        // Deploy Nginx to AWS Fargate
        import * as awsx from "@pulumi/awsx";

        let web = new awsx.elb.ApplicationLoadBalancer(
            "net-lb", { external: true }).
            createListener("web", { port: 80, external: true });

        let appService = new awsx.ecs.FargateService("nginx-svc", {
            taskDefinitionArgs: {
                container: {
                    image: "nginx",
                    portMappings: [ web ],
                },
            },
            desiredCount: 5,
        });

        export let url = web.endpoint.hostname;

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
      label: Contact Us

examples:
    - title: Deploy Nginx to AWS Fargate
      body: >
          In this example, Pulumi defines and uses a new Amazon ECS Fargate cluster, and creates
          a load balanced service running the standard Nginx image from the Docker Hub. The same
          experience is available on other clouds and Pulumi can pull from any container registry.
      code: |
          // Deploy Nginx to AWS Fargate
          import * as awsx from "@pulumi/awsx";

          let web = new awsx.elb.ApplicationLoadBalancer(
              "net-lb", { external: true }).
              createListener("web", { port: 80, external: true });

          let appService = new awsx.ecs.FargateService("nginx-svc", {
              taskDefinitionArgs: {
                  container: {
                      image: "nginx",
                      portMappings: [ web ],
                  },
              },
              desiredCount: 5,
          });

          export let url = web.endpoint.hostname;
      cta:
          url: /docs/get-started
          label: GET STARTED

    - title: Deploying with a custom build
      body: >
          This example uses a trivial Dockerfile that derives from the <code>nginx</code> base image and copies the
          <code>./www</code> directory into the nginx HTML target so that it will be served up.
      code: |
          // Using a custom build based on Nginx
          import * as awsx from "@pulumi/awsx";

          let web = new awsx.elb.ApplicationLoadBalancer(
              "net-lb", { external: true }).
              createListener("web", { port: 80, external: true });

          const appService = new awsx.ecs.FargateService("nginx-svc", {
              taskDefinitionArgs: {
                  container: {
                      image: awsx.ecs.Image.fromPath("app-img", "./www");
                      portMappings: [ web ],
                  },
              },
              desiredCount: 5,
          });

          export const url = web.endpoint.hostname;

          // Dockerfile
          FROM nginx
          COPY ./www /usr/share/nginx/html
      cta:
          url: /docs/get-started
          label: GET STARTED

    - title: Creating a Kubernetes cluster
      body: >
          Pulumi can provision Kubernetes clusters &mdash; in this example, an AWS EKS cluster &mdash;
          in addition to deploying application-level configuration, using a standard set of languages,
          abstractions, and tools.
      code: |
          import * as awsx from "@pulumi/awsx";
          import * as eks from "@pulumi/eks";

          // Create a VPC for our cluster.
          const vpc = new awsx.ec2.Vpc("vpc", {});

          // Create the EKS cluster itself.
          const cluster = new eks.Cluster("cluster", {
              vpcId: vpc.id,
              subnetIds: vpc.publicSubnetIds,
              instanceType: "t2.medium",
              desiredCapacity: 4,
              minSize: 3,
              maxSize: 5,
              storageClasses: "gp2",
              deployDashboard: true,
          });

          // Export the cluster's kubeconfig.
          export const kubeconfig = cluster.kubeconfig;
      cta:
          url: /docs/get-started
          label: GET STARTED

    - title: Deploy containers to Microsoft ACI
      body: >
          The <code>@pulumi/azure</code> library provides fine-grained control of Azure resources. In this example,
          we deploy a simple linux container to Microsoft ACI, in the West US zone.
      code: |
          import * as azure from "@pulumi/azure";

          const resourceGroup = new azure.core.ResourceGroup("resourcegroup", {
              location: "West US",
          });

          const containerGroup = new azure.containerservice.Group("containergroup", {
              location: resourceGroup.location,
              resourceGroupName: resourceGroup.name,
              ipAddressType: "public",
              osType: "linux",
              containers: [
                  {
                      name: "hw",
                      image: "microsoft/aci-helloworld:latest",
                      cpu: 0.5,
                      memory: 1.5,
                      port: 80
                  },
              ],
              tags: {
                  "environment": "testing",
              },
          });
      cta:
          url: /docs/get-started
          label: GET STARTED

    - title: Invoke a long-running container as a task
      body: >
          This example shows a container used for executing a long-running task. Here, we use a container to
          perform a thumbnail extraction on a piece of video uploaded to an S3 bucket.
      code: |
          import * as aws from "@pulumi/aws";
          import * as awsx from "@pulumi/awsx";

          // A bucket to store videos and thumbnails.
          const videos = new aws.s3.Bucket("bucket");

          // A task which runs a containerized FFMPEG job to extract a thumbnail image.
          const ffmpegThumbnailTask = new awsx.ecs.FargateTaskDefinition("ffmpegThumbTask", {
              container: {
                  image: awsx.ecs.Image.fromPath("ffmpegThumbTask", "./docker-ffmpeg-thumb"),
                  memoryReservation: 512,
              },
          });

          // When a new video is uploaded, run the FFMPEG task on the video file.
          videos.onObjectCreated("onNewVideo",
              new aws.lambda.CallbackFunction<aws.s3.BucketEvent, void>("onNewVideo", {
                  // Specify appropriate policies so that this AWS lambda can run EC2 tasks.
                  policies: [
                      aws.iam.AWSLambdaFullAccess,
                      aws.iam.AmazonEC2ContainerServiceFullAccess,
                  ],
                  callback: async bucketArgs => {
                      for (const record of bucketArgs.Records) {
                          const file = record.s3.object.key;
                          const thumbnailFile = file.substring(0, file.indexOf('_')) + '.jpg';
                          const framePos = file.substring(file.indexOf('_')+1, file.indexOf('.')).replace('-',':');
                          await ffmpegThumbnailTask.run({
                              overrides: {
                                  containerOverrides: [{
                                      name: "container",
                                      environment: [
                                          { name: "S3_BUCKET", value: bucketName.get() },
                                          { name: "INPUT_VIDEO", value: file },
                                          { name: "TIME_OFFSET", value: framePos },
                                          { name: "OUTPUT_FILE", value: thumbnailFile },
                                      ],
                                  }],
                              },
                          });
                      }
                  },
              }), { filterSuffix: ".mp4" });

          exports.bucketName = videos.bucket;
      cta:
          url: /docs/get-started
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
            public clouds including GCP, AWS and others. Pulumi's declarative model, the support for real programming
            languages, and the uniform workflow on any cloud make our SRE team much more efficient.
---
