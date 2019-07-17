---
title: Kubernetes with Pulumi
layout: kubernetes
url: /kubernetes

meta_desc: Pulumi provides a cloud native programming model for Kubernetes deployments and orchestration. Any code, any cloud, any app.

hero:
    title: Kubernetes with Pulumi
    body: >
        Pulumi provides a cloud native programming model for kubernetes
        deployments and orchestration: from on-premises to AWS EKS, Microsoft
        AKS, and Google GKE.


        Any code, any cloud, any language.
    code: |
        import * as k8sjs from "./k8sjs";

        let redis = new k8sjs.ServiceDeployment("redis", {
            image: "k8s.gcr.io/redis:e2e",
            ports: [ 6379 ]
        });

        let web = new k8sjs.ServiceDeployment("web", {
            replicas: 3,
            image: "gcr.io/google-samples/gb-frontend:v4",
            ports: [ 80 ],
            loadBalancer: true,
        });

        export let frontendIp = web.ipAddress;

sections:
    - id: what-is-kubernetes
      label: What is Kubernetes?
    - id: kubernetes-everywhere
      label: Kubernetes Everywhere
    - id: code
      label: Code
    - id: get-started
      label: Get Started
    - id: contact
      label: Contact Us

examples:
    - title: Define Kubernetes apps
      body: >
          In this example, we use TypeScript to define a trivial app - an nginx image - and
          deploy 1 replica. Using a real language to define your app enables great IDE support &mdash;
          compile time checking for instance.
      code: |
          import * as k8s from "@pulumi/kubernetes";

          const appLabels = { app: "nginx" };

          const deployment = new k8s.apps.v1.Deployment("nginx", {
              spec: {
                  replicas: 1,
                  selector: { matchLabels: appLabels },
                  template: {
                      metadata: { labels: appLabels },
                      spec: {
                          containers: [{
                              name: "nginx", image: "nginx"
                          }]
                      }
                  }
              }
          });
      cta:
          url: /docs/quickstart
          label: GET STARTED

    - title: Improve expressiveness, reduce boilerplate
      body: >
          Using real languages means being able to recognize patterns, and abstract them to reusable
          componenents.

          In this example we take a typical Deployment and Service pattern to create a ServiceDeployment
          class, simplifying the implementation of the canonical Guestbook app.
      code: |
          import * as k8sjs from "./k8sjs";

          let redisMaster = new k8sjs.ServiceDeployment("redis-master", {
              image: "k8s.gcr.io/redis:e2e",
              ports: [ 6379 ]
          });

          let redisSlave = new k8sjs.ServiceDeployment("redis-slave", {
              image: "gcr.io/google_samples/gb-redisslave:v1",
              ports: [ 6379 ]
          });

          let frontend = new k8sjs.ServiceDeployment("frontend", {
              replicas: 3,
              image: "gcr.io/google-samples/gb-frontend:v4",
              ports: [ 80 ],
              loadBalancer: true,
          });

          export let frontendIp = frontend.ipAddress;
      cta:
          url: /docs/quickstart
          label: GET STARTED

    - title: Injecting sidecars using abstraction
      body: >
          Abstraction also allows us to do powerful work to simplify more complex configuration.
          An example of this is the sidecar microservices pattern where a container runs
          alongside other containers to add some functional value &mdash; logging, proxying etc.

          In this case we define a simple EnvoyDeployment class that adds an Envoy sidecar to our Kubernetes app.
      code: |
          export class EnvoyDeployment extends k8s.apps.v1.Deployment {
              constructor(name: string, args: k8stypes.apps.v1.Deployment, opts?: pulumi.CustomResourceOptions) {
                  const pod = args.spec.template.spec;

                  // Add an Envoy sidecar container.
                  pod.containers = pod.containers || [];
                  pod.containers.push({
                      name: "envoy",
                      // `lyft/envoy` does not tag releases. Use a SHA.
                      image: "lyft/envoy:4640fc028d65a6e2ee18858ebefcaeed24dffa81",
                      command: ["/usr/local/bin/envoy"],
                      args: [
                          "--concurrency 4",
                          "--config-path /etc/envoy/envoy.json",
                          "--mode serve"
                      ],
                      ports: [{ containerPort: 80, protocol: "TCP" }],
                      resources: {
                          limits: { cpu: "1000m", memory: "512Mi" },
                          requests: { cpu: "100m", memory: "64Mi" }
                      },
                      volumeMounts: [{
                          name: "envoy-conf", mountPath: "/etc/envoy"
                      }]
                  });

                  // Add a Volume for Envoy's config, as a ConfigMap.
                  pod.volumes = pod.volumes || [];
                  pod.volumes.push({
                      name: "envoy-conf", configMap: { name: "envoy" },
                  });

                  super(name, args, opts);
              }
          }
      cta:
          url: /docs/quickstart
          label: GET STARTED

    - title: Use existing YAML and Helm Charts
      body: >
          Pulumi can also process YAML and Helm Charts, adding them to Pulumi programs which unlocks multi-cloud and advanced delivery scenarios.

          These examples use YAML and Helm to deploy the Kubernetes Guestbook app and Wordpress.
      code: |
          // Use YAML.
          import * as k8s from "@pulumi/kubernetes";

          const guestbook = new k8s.yaml.ConfigGroup(
              "guestbook", { files: "guestbook/*.yaml" });

          export const frontendIp =
              guestbook.getResource("v1/Service", "frontend").
              spec.apply(spec => spec.clusterIP);

          // Use Helm.
          import * as k8s from "@pulumi/kubernetes";

          const wordpress = new k8s.helm.v2.Chart("wordpress", {
              repo: "stable",
              version: "2.1.3",
              chart: "wordpress"
          });

          export const frontendIp = wordpress
              .getResource("v1/Service", "wpdev-wordpress")
              .status.apply(status => status.loadBalancer.ingress[0].ip);
      cta:
          url: /docs/quickstart
          label: GET STARTED

    - title: Declare managed services alongside Kubernetes
      body: >
          Pulumi can be used to combine services. For instance, a Kubernetes cluster and an associated database (such as RDS).

          In this example, we provision and use an AWS S3 bucket from a Kubernetes service.
      code: |
          import * as k8s from "@pulumi/kubernetes";
          import * as aws from "@pulumi/aws";

          const appName = "nginx";

          // nginx config stored in an S3 bucket.
          const config = new aws.s3.Bucket(`${appName}-config`);

          // nginx container, replicated 1 time.
          const appLabels = { app: appName };
          const nginx = new k8s.apps.v1beta1.Deployment(appName, {
              spec: {
                  selector: { matchLabels: appLabels },
                  replicas: 1,
                  template: {
                      metadata: { labels: appLabels },
                      spec: {
                          initContainers: [
                              nginxConfigPuller(config.bucketDomainName)
                          ],
                          containers: [{
                              name: appName, image: "nginx:1.15-alpine"
                          }]
                      }
                  }
              }
          });
      cta:
          url: /docs/quickstart
          label: GET STARTED

    - title: Provision Kubernetes clusters in any cloud
      body: >
          Kubernetes can be used in many environments &mdash; local dev, in the data center, self-hosted
          in the cloud, and as a managed cloud service. Pulumi supports all of those options.

          In this example, we show how to deploy a GKE cluster with configurable settings, which
          can then be used to deploy apps to.
      code: |
          import * as gcp from "@pulumi/gcp";
          import { nodeCount, nodeMachineType, password, username } from "./config";

          export const k8sCluster = new gcp.container.Cluster("gke-cluster", {
              initialNodeCount: nodeCount,
              nodeVersion: "latest",
              minMasterVersion: "latest",
              masterAuth: { username, password },
              nodeConfig: {
                  machineType: nodeMachineType,
                  oauthScopes: [
                      "https://www.googleapis.com/auth/compute",
                      "https://www.googleapis.com/auth/devstorage.read_only",
                      "https://www.googleapis.com/auth/logging.write",
                      "https://www.googleapis.com/auth/monitoring"
                  ],
              },
          });

      cta:
          url: /docs/quickstart
          label: GET STARTED
---
