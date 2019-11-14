---
title: A Year of Helping Customers Build Production-Ready Kubernetes Infrastructure
authors: ["joe-duffy"]
tags: ["Pulumi-News", "Kubernetes"]
meta_desc: "Today we announced Pulumi Crosswalk for Kubernetes, a collection of open source technologies to help developers and operators bring Kubernetes into their organizations."
date: "2019-11-14"
---

Today we announced Pulumi Crosswalk for Kubernetes, a collection of open source technologies to help developers and operators work together to bring Kubernetes into their organizations &mdash; from the underlying cloud and cluster infrastructure to cloud native applications themselves. These tools, libraries, and playbooks capture the lessons we learned over the past year working with organizations to go from zero to Kubernetes in production for their infrastructure and application workloads.

If you want a synopsis of just what’s new, jump straight to the press release or [product documentation](/docs/guides/crosswalk/kubernetes/). Below is the backstory and why we’re so excited about this release.

## Applying infrastructure as code to Kubernetes

A little over a year ago, we launched support for managing Kubernetes resources using Pulumi’s open source infrastructure as code tools. The entire Kubernetes object model across all supported versions is available in your language of choice &mdash; including JavaScript, TypeScript, and Python &mdash; in addition to the entire ecosystem of Helm Charts. This offers 100% API resource compatibility, and same-day support for newly released Kubernetes releases.

By leveraging general purpose languages, you get rich capabilities like for loops, functions, and classes, the ability to share and reuse best practices &mdash; eliminating copy and paste &mdash; as well as access to your favorite tools, including editors, test frameworks, and static analysis tools.

This is exciting for any of us who have struggled with “walls of YAML or JSON” &mdash; but this alone isn’t the whole story.

A unified approach to infrastructure as code delivers a robust delivery workflow, and enables managing configuration across not only just Kubernetes resources, but also any of the cluster’s underlying public or private cloud infrastructure, including AWS, Azure, Google Cloud, vSphere, and others.

At the time, we didn’t realize how powerful this unified approach would turn out to be. For instance, properly provisioning an Amazon EKS cluster requires not only orchestrating deployments across AWS, but also going back and forth with Kubernetes resources. We designed  Pulumi to let you do this using a single consistent platform and workflow, replacing the “mountains of Bash” that are typically required to integrate multiple tools.

This was an exciting foundation to start from, and we had a number of end users and organizations who soon came to our doors to adopt Kubernetes, with our help.

## Why Kubernetes in production is hard

If I had to summarize the challenges that we faced and which we worked to help solve, they are:

* **Kubernetes infrastructure is not an island.** Although AWS, Azure, and GCP offer managed Kubernetes services, most organizations with existing infrastructure maturity find it difficult to provision and manage cluster infrastructure. This is often because going to production requires connecting a cluster to a lot of surrounding infrastructure &mdash; including IAM, networking, encryption services, private Docker registries, and more. Kubernetes-specific tools only help with a fraction of this problem and create silos.
* **Empowering an entire organization is tough.** Most organizations adopting Kubernetes are attempting to harmonize the “two sides of the house” -- developers and operators. The infrastructure operations team is responsible for managing the cluster and underlying infrastructure, while the developers are trying to deliver applications and services to the cluster (often also using other public cloud services, like object stores). Although the Kubernetes architecture is well-suited to this, teams struggle to standardize on tools, workflows, and practices around both infrastructure and application delivery.
* **Day Two is even harder than Day One.** Many teams decide to go “all in” on Kubernetes ... only to find out that securing, scaling, and operationalizing Kubernetes is far more of a full-time job than they imagined. Can you perform zero-downtime upgrades? How do you perform failover between regions? How fast can you promote new container images from dev, to staging, to dozens of production clusters?

Adding to the complexity, these challenges tend to differ depending on which cloud environment you’re targeting. Although Kubernetes has helped to standardize the container compute layer, and what it means to scale out a load balanced service, for example, it does not abstract away all of the infrastructure capabilities between the clouds, like IAM, container registries, and data services.

We experienced this first hand with many customers over the past year. There are three specific areas we’ve worked to develop into turnkey solutions for customers:

* Infrastructure playbooks
* Making Kubernetes more accessible to developers
* Operationalizing delivery at-scale

Let me tell you about each of these in turn.

## Developing playbooks for cluster infrastructures

Most practitioners are left to discover solutions to the hardest problems with Kubernetes infrastructure on their own. After helping dozens of customers go to production with AWS EKS, Azure AKS, Google Cloud GKE, and on-premises Kubernetes infrastructures, we decided to develop best practices into a set of playbooks. This helps organizations to avoid reinventing the wheel, in addition to mitigating potential pitfalls around security, reliability, and maintainability.

These playbooks cover a lot of ground, including topics like:

* **Control planes.** Each Kubernetes cluster has a control plane comprised of controllers, state management, and other centralized services. Each provider offers a distinct and unique way of creating, deploying, and managing the control plane.
Worker nodes. Each cluster also requires worker nodes to actually run compute. Depending on your compute, storage, and security needs, the provisioning and management of these nodes &mdash; often using multiple node pools &mdash; differs greatly. Getting this right is essential to attaining a good tradeoff between cost and performance.
* **Identity.** All of the above also needs to integrate with your team’s security policies, including Identity and Access Management (IAM) and Role Based Access Controls (RBAC). If you’re in AWS, you undoubtedly want to connect to AWS IAM; if you’re in Azure, you want to leverage existing ActiveDirectory settings; if you’re in GCP, you’ll want to use GCP IAM; and if you’re using a custom configuration, it can be even more complicated. This is an essential part of deploying Kubernetes within an organization. 
* **Cluster services.** Each cluster needs cluster-wide services deployed into the cluster, including performance and monitoring services (AWS CloudWatch, Azure Log Analytics and Monitoring, Datadog, Prometheus, etc.), service meshes, container registries, CRDs, and operators.
Application delivery. Applications need to be Dockerized, packaged up and deployed to private container registries, and rolled out to the cluster, often continuously.
* **Application services.** In addition to the applications themselves, often cloud native applications require additional services to come along for the ride. This includes ingress controllers, DNS and certificate management services, and more.
Upgrading clusters. Last but not least, cluster upgrades are an essential part of the overall playbook. Kubernetes is fast-moving, so upgrades are a regular occurrence, and yet it’s not always easy to deploy upgrades with confidence, especially when you are worried about zero downtime and persistent workloads.

This layer cake of concerns can be visualized using the following diagram:

![Kubernetes Infrastructue Architecture Layers](/images/docs/quickstart/kubernetes/cake.svg)

We are confident that anybody looking to create production-ready infrastructure in any of the public clouds, or even on-premises, will benefit from this material. It is also open source so we hope to improve and evolve it in partnership with the community in the weeks to come.

## Making Kubernetes more accessible to developers

Besides having to navigate walls of YAML, there is a significant amount of repetition on most idiomatic Kubernetes configurations. In fact, it often feels like hand-authoring Kubernetes YAML is akin to writing software in assembly language, rather than higher level languages.

Pulumi exposes 100% of the Kubernetes API, which means you can use modern language practices to start taming some of this low-level chaos. But new library constructs available in Crosswalk take this to another level by eliminating common boilerplate patterns.

For example, this wall of YAML:

```yaml
apiVersion: v1
kind: ConfigMap
data:
  config: very important data
metadata:
  name: app-config
---
apiVersion: v1
kind: Secret
data:
  app-password: JikkMz9mK2hIRDo3
  database-password: Y29uZmlnLmRhdGFiYXNlUGFzc3dvcmQ=
metadata:
  name: app-secrets
type: Opaque
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - env:
            - name: APP_CONFIG_PATH
              value: /app/config
            - name: APP_USER
              value: config.user
            - name: APP_PASSWORD
              valueFrom:
                secretKeyRef:
                  key: app-password
                  name: app-secrets
            - name: APP_DATABASE_PASSWORD
              valueFrom:
                secretKeyRef:
                  key: database-password
                  name: app-secrets
          image: nginx
          imagePullPolicy: Always
          name: nginx
          ports:
            - containerPort: 80
              name: http
          volumeMounts:
            - mountPath: /app/config
              name: app-config-rsg88x4g
      restartPolicy: Always
      volumes:
        - configMap:
            name: app-config
          name: app-config
---
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  ports:
    - name: http
      port: 80
      targetPort: 80
  selector:
    app: nginx
  type: LoadBalancer
```

Is distilled down to its essence, with far less ceremony and repetition

```typescript
// Define the application configuration and secrets.
const configs = new kx.ConfigMap("app-config", {
    data: { "config": "very important data" }
});

const secrets = new kx.Secret("app-secrets", {
    stringData: {
        "app-password": new kx.RandomPassword("app-password"),
        "database-password": config.databasePassword
    }
});

// Define the application Pod.
const appConfigPath = "/app/config";
const appPod = new kx.PodBuilder({
    containers: [{
        image: "app:1.0.0",
        env: {
            "APP_CONFIG_PATH": appConfigPath,
            "APP_USER": config.user,
            "APP_PASSWORD": secrets.asEnvValue("app-password"),
            "APP_DATABASE_PASSWORD": secrets.asEnvValue("database-password"),
        },
        volumeMounts: [
            configs.mount(appConfigPath)
        ],
    }],
});

// Create a Kubernetes Deployment using the previous Pod definition.
const deployment = new kx.Deployment("nginx", {
    spec: appPod.asDeploymentSpec({ replicas: 3 }),
});

// Expose the Deployment with a load balancer using a Kubernetes Service.
const service = deployment.createService({
    type: kx.types.ServiceType.LoadBalancer,
});
```

These library extensions have been designed to live alongside your existing Kubernetes configuration, so that you can gradually reduce complexity, while the result still feels familiar and integrated.

In addition to making Kubernetes configuration more accessible in these ways, there are other benefits to application configuration that we have seen emerge. This includes:

* **Data Services.** For many of us, managing persistent workloads in Kubernetes is not worth the hassle. Although it’s possible to manage the delicate dance of tainting, draining, and migration, many of our customers rely on hosted offerings for data stores &mdash; such as Amazon S3, RDS, Azure Cosmos DB or Google Cloud BigTable &mdash; and Kubernetes for stateless compute. Using managed services brings the advantage of intrinsic scaling, backups, and management, without the tedium. Pulumi lets you mix and match Kubernetes and public cloud infrastructure as code.
* **Container Registries.** Most end users need to use private container registries to host application images. Furthermore, most of us want to use our cloud provider’s native offering, such as Amazon Elastic Container Registry, Azure Container Registry, or Google Container Registry, because it integrates with IAM. Using Pulumi, you don’t need separate deployment pipelines for containers compared to the supporting application infrastructure.
* **Serverless.** If you want to use the best and most cost effective serverless capabilities, you likely want to use AWS Lambda, Azure Functions, or Google Cloud Functions. We see end users augmenting container-based applications with serverless extensions all the time.
* **Architecture as Code.** Thanks to Pulumi’s use of real languages for infrastructure as code, end users have been able to abstract and encapsulate complexity into reusable forms, such as functions and classes. This helps you go beyond even the basic Kubernetes configuration challenges that Kx solves, to codifying recurring patterns in your cloud native architectures.

In addition to all of that, we’ve been hard at work on a new experimental “watch mode” feature which, in conjunction with the above, brings all of Kubernetes to your fingertips in a radically new way. We’re excited to show this off at our booth at KubeCon next week!

## Operationalizing delivery at-scale

After you’ve mastered the infrastructure and application authoring challenges, the difficulties move to Day Two and beyond. At this stage, organizations need to figure out how to deliver changes continuously to an ever-increasing number of environments.

Since our initial launch last year, we have added many different CI/CD integrations, including support for GitLab, Codefresh, Azure DevOps, Octopus Deploy, GitHub Actions, and more. This enables delivery at global scale. In fact, one of our customers continuously deploys to 80 different environments across their development and infrastructure operations teams.

Finally, we are excited to release a new technology today, Cloud Query Language (CQL), that leverages the Pulumi object model to ask operational queries about your cluster and its applications. This includes queries like “How many distinct versions of MySQL are running in my cluster?”, “Which Pods are exposed to the Internet via a load-balanced Service?”, and so on.

For instance, this query shows the distinct versions of MySQL inside your cluster:

```typescript
import * as kq from "@pulumi/query-kubernetes";

// Find all distinct versions of MySQL running in your cluster.
const mySqlVersions = kq
    .list("v1", "Pod")
    .flatMap(pod => pod.spec.containers)
    .map(container => container.image)
    .filter(imageName => imageName.includes("mysql"))
    .distinct();

mySqlVersions.forEach(console.log);
```

CQL also supports live streaming queries, which the CLI will display results from in real time.

## Join a growing community

Everything above is open source and has been battle-tested with many end users and organizations over the last year &mdash; all the way from startups to ISVs to the largest enterprises in the world. We are excited to share these best practices in reusable forms, leveraging the foundation uniquely provided by Pulumi’s infrastructure as code platform using real languages.

To get started, check out the [documentation](/docs/guides/crosswalk/kubernetes/), or [get started with the open source SDK now](/docs/get-started/kubernetes/).

We sincerely hope that your team can be successful in your Kubernetes journey as a result of these lessons learned from others. Additionally, Pulumi offers training and services, so if we can help in any way, please [join our entire team and thousands of practitioners on our Community Slack](https://slack.pulumi.com) &mdash; or simply [contact us](/contact) and we’ll be in touch.
