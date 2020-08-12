---
title: Kubernetes with Pulumi
layout: kubernetes
url: /kubernetes

meta_desc: Pulumi provides a cloud native programming model for Kubernetes deployments and orchestration. Any code, any cloud, any app.

hero:
    title: Kubernetes with Pulumi
    body: >
        Pulumi provides a cloud native programming model for Kubernetes
        deployments and orchestration: from on-premises to AWS EKS, Microsoft
        AKS, and Google GKE.


        Any code, any cloud, any language.
    code: |
        import * as kx from "@pulumi/kubernetesx";

        const pb = new kx.PodBuilder({
            containers: [{
                image: "nginx",
                ports: { http: 80 }
            }]
        });

        const deployment = new kx.Deployment("nginx", {
            spec: pb.asDeploymentSpec({ replicas: 3 })
        });

        const service = deployment.createService({
            type: kx.types.ServiceType.LoadBalancer
        });

        export const serviceIP = service.ip;

sections:
    - id: code
      label: Code
    - id: get-started
      label: Get Started
    - id: contact
      label: Contact Us

kubernetes_crosswalk:
    code: |
        import * as gcp from "@pulumi/gcp";
        import * as k8s from "@pulumi/kubernetes";

        // Create a GKE cluster.
        const cluster = new gcp.container.Cluster("gke-cluster");

        // Create a performant node pool in the cluster.
        const performantNodes = new gcp.container.NodePool("performant-nodes", {
            cluster: cluster.name,
            nodeConfig: { machineType: "n1-standard-16"}
        });

        // Create an Apps namespace.
        const appsNamespace = new k8s.core.v1.Namespace("apps");

        // Create a quota.
        const quotaAppNamespace = new k8s.core.v1.ResourceQuota("apps", {
            spec: {hard: {cpu: "200", memory: "1Gi", pods: "10"}},
        })

        // Create a restrictive PodSecurityPolicy.
        const restrictivePSP = new k8s.policy.v1beta1.PodSecurityPolicy("restrictive", {
            spec: { privileged: false,
                runAsUser: { rule: "RunAsAny" }, fsGroup: { rule: "RunAsAny" },
                seLinux: { rule: "RunAsAny" }, supplementalGroups: { rule: "RunAsAny" },
            }
        });

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
          id: get-started-kubernetes-yaml-helm
          url: /docs/get-started/kubernetes/
          label: TRY IT NOW

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
          id: get-started-kubernetes-multi-cloud
          url: /docs/get-started/kubernetes/
          label: GET STARTED

contact_us_form:
    section_id: contact
    hubspot_form_id: 212ce93d-e081-4998-b14b-f26a974da4fb
    headline: Need help with Kubernetes?
    quote:
        title: Learn how top engineering teams are using Pulumi to manage and provision Kubernetes clusters in any cloud.
        name: Harrison Heck
        name_title: Head of DevOps, Linio
        content: |
            As the largest eCommerce platform in Latin America, our infrastructure has to be highly stable, well
            documented and agile. With Pulumi, we're able to develop new infrastructure, change existing infrastructure
            and more with greater speed and reliability than we've ever had before.
---
