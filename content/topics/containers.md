---
title: Container Management with Pulumi
layout: containers
url: /containers

meta_desc: Pulumi provides a cloud native programming model for container management. Any code, any cloud, any app.

hero:
    title: Container Management with Pulumi
    body: >
        Pulumi provides a cloud native programming model for container
        management: deploy Docker to AWS Fargate, Microsoft ACI, and
        Kubernetes.


        Any code, any cloud, any language.
    code: |
        // Deploy Nginx to AWS Fargate
        import * as cloud from "@pulumi/cloud";

        let nginx = new cloud.Service("nginx", {
            image: "nginx",
            ports: [{ port: 80 }],
            replicas: 2,
        });

        export let url = nginx.defaultEndpoint;

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
          In this example, Pulumi uses a multi-cloud <code>cloud.Service</code> object to pull the nginx
          image from Docker Hub, and deploy it in a load-balanced way to AWS Fargate. Pulumi can
          pull from any container registry.
      code: |
          // In Pulumi configuration
          pulumi config set cloud-aws:useFargate true

          // Deploy Nginx to AWS Fargate
          import * as cloud from "@pulumi/cloud";

          let nginx = new cloud.Service("nginx", {
              image: "nginx",
              ports: [{ port: 80 }],
              replicas: 2,
          });

          export let url = nginx.defaultEndpoint;
      cta:
          url: /docs/quickstart/cloudfx/tutorial-service
          label: GET STARTED

    - title: Deploying with a custom build
      body: >
          This example uses a trivial Dockerfile that derives from the <code>nginx</code> base image and copies the
          <code>./www</code> directory into the nginx HTML target so that it will be served up.
      code: |
          // Using a custom build based on Nginx
          import * as cloud from "@pulumi/cloud";

          let nginx = new cloud.Service("nginx", {
              build: ".",
              ports: [{ port: 80 }],
              replicas: 2,
          });

          export let url = nginx.defaultEndpoint;

          // Dockerfile
          FROM nginx
          COPY ./www /usr/share/nginx/html
      cta:
          url: /docs/quickstart/cloudfx/tutorial-service
          label: GET STARTED

    - title: Connecting containers
      body: >
          This example shows how we can connect containers using Pulumi &mdash; in this case Redis for a data store,
          and a Python flask app for a front end. Using Pulumi, it is easy to obtain a reference to the container
          objects, and connect them using code.
      code: |
          import * as pulumi from "@pulumi/pulumi";
          import * as cloud from "@pulumi/cloud";

          // The data layer for the application
          let redisCache = new cloud.Service("voting-app-cache", {
              containers: {
                  redis: {
                      image: "redis:alpine",
                      memory: 512,
                      ports: [{ port: redisPort }],
                      command: ["redis-server", "--requirepass", redisPassword],
                  },
              },
          });

          let redisEndpoint = redisCache.endpoints.apply(endpoints => endpoints.redis[redisPort]);

          // A custom container for the frontend, which is a Python Flask app
          let frontend = new cloud.Service("voting-app-frontend", {
              containers: {
                  votingAppFrontend: {
                      build: "./frontend",   // path to Dockerfile folder
                      memory: 512,
                      ports: [{ port: 80 }],
                      environment: {
                          // pass the Redis container info in environment variables
                          "REDIS":      redisEndpoint.apply(e => e.hostname),
                          "REDIS_PORT": redisEndpoint.apply(e => e.port.toString()),
                          "REDIS_PWD":  redisPassword
                      }
                  },
              },
          });

          export let frontendURL = frontend.endpoints.apply(e => e["votingAppFrontend"][80].hostname);
      cta:
          url: /docs/quickstart/cloudfx/tutorial-service
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
          url: /docs/quickstart/cloudfx/tutorial-service
          label: GET STARTED

    - title: Invoke a long-running container as a task
      body: >
          This example shows a container used for executing a long-running task. Here, we use a container to
          perform a thumbnail extraction on a piece of video uploaded to an S3 bucket.
      code: |
          let cloud = require("@pulumi/cloud-aws");

          // A bucket to store videos and thumbnails.
          let videos = new cloud.Bucket("bucket");

          // A task which runs an FFMPEG transform to extract a thumbnail image.
          let ffmpegThumbnailTask = new cloud.Task("ffmpegThumbTask", {
              build: ".",
              memoryReservation: 512,
          });

          // When a new video is uploaded, run the FFMPEG task on the video file.
          videos.onPut("onNewVideo", args => {
              let file = args.key;
              ffmpegThumbnailTask.run({
                  environment: {
                      "S3_BUCKET":   videos.bucket.name.get(),
                      "INPUT_VIDEO": file,
                      "TIME_OFFSET": file.substring(file.indexOf('_')+1, file.indexOf('.')).replace('-',':'),
                      "OUTPUT_FILE": file.substring(0, file.indexOf('_')) + '.jpg',
                  },
              });
          }, { keySuffix: ".mp4" });

          exports.bucketName = videos.bucket.name;
      cta:
          url: /docs/quickstart/cloudfx/tutorial-service
          label: GET STARTED

---
