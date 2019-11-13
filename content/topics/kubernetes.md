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
    - id: code
      label: Code
    - id: get-started
      label: Get Started
    - id: contact
      label: Contact Us

examples:
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
          url: /docs/get-started
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

          const engineVersion = gcp.container.getEngineVersions().then(v => v.latestMasterVersion);
          export const k8sCluster = new gcp.container.Cluster("gke-cluster", {
              initialNodeCount: nodeCount,
              minMasterVersion: engineVersion,
              nodeVersion: engineVersion,
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
          url: /docs/get-started
          label: GET STARTED
---
