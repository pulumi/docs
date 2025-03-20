---
title: "Kubernetes Best Practices I Wish I Had Known Before"
date: 2025-01-20
updated: 2025-03-20
draft: false

meta_desc: |
  Discover essential Kubernetes best practices I wish I had known earlier. Avoid pitfalls, optimize your setup, and streamline deployments with expert insights.

meta_image: meta.png

authors:
- engin-diri

tags:
- kubernetes
- best-practices
- k8s
- devops
social:
  twitter: |
    Learn best practices for Kubernetes that I wish I had known earlier. Avoid common pitfalls and save time, money, and headaches.
    <link>
  linkedin: |
    Kubernetes Best Practices I Wish I Had Known Before

    Embarking on your Kubernetes journey? Trust me, it can feel like climbing Mount Everest in flip-flops! Through years of hands-on experience in production environments, I've compiled a list of essential Kubernetes best practices that can save you time, money, and countless headaches.
    
    Whether you're just starting or looking to refine your Kubernetes setup, these insights will help you navigate the complexities and harness the full power of Kubernetes.
    <link>
---

Kubernetes has undeniably transformed the way we build, ship, and run applications. But let’s be honest, getting started with Kubernetes can feel like climbing Mount Everest in flip-flops.

As a cloud-native citizen and Kubernetes enthusiast, I’ve learned the hard way that there are a bunch of "wish I had known that earlier" best practices. They could have saved me time, money, and headaches.

<!--more-->

{{< figure alt="The 'Kubernetes is easy'-iceberg meme is a classic example of how Kubernetes can be deceivingly complex" src="img.png" caption="The 'Kubernetes is easy'-iceberg meme is a classic example of how Kubernetes can be deceivingly complex" width=100% >}}

In this post, I will highlight some crucial Kubernetes best practices. They are from my years of experience with Kubernetes in production. Think of this as the curated “Kubernetes cheat sheet” you wish you had from Day 1. Buckle up; it’s going to be an exciting ride.

1. [Don’t Skimp on Resource Requests and Limits](/blog/kubernetes-best-practices-i-wish-i-had-known-before/#1-dont-skimp-on-resource-requests-and-limits)
2. [Namespace Like Your Life Depends on It](/blog/kubernetes-best-practices-i-wish-i-had-known-before/#2-namespace-like-your-life-depends-on-it)
3. [Avoid Running Multiple Containers in One Pod Unless Necessary](/blog/kubernetes-best-practices-i-wish-i-had-known-before/#3-avoid-running-multiple-containers-in-one-pod-unless-necessary)
4. [Use a Package Manager for Your YAML Files](/blog/kubernetes-best-practices-i-wish-i-had-known-before/#4-use-a-package-manager-for-your-yaml-files)
5. [Ingress and Networking Best Practices](/blog/kubernetes-best-practices-i-wish-i-had-known-before/#5-ingress-and-networking-best-practices)
6. [Lean On Liveness, Readiness, and Startup Probes](/blog/kubernetes-best-practices-i-wish-i-had-known-before/#6-lean-on-liveness-readiness-and-startup-probes)
7. [Mind Your Security: RBAC, Pod Security, and Secrets](/blog/kubernetes-best-practices-i-wish-i-had-known-before/#7-mind-your-security-rbac-pod-security-and-secrets)
8. [Monitor Everything (And Then Monitor Some More)](/blog/kubernetes-best-practices-i-wish-i-had-known-before/#8-monitor-everything-and-then-monitor-some-more)
9. [Automate Deployments with CI/CD](/blog/kubernetes-best-practices-i-wish-i-had-known-before/#9-automate-deployments-with-cicd)
10. [Keep Your Kubernetes Cluster and Components Updated](/blog/kubernetes-best-practices-i-wish-i-had-known-before/#10-keep-your-kubernetes-cluster-and-components-updated)
11. [Use Labels and Annotations Wisely](/blog/kubernetes-best-practices-i-wish-i-had-known-before/#11-use-labels-and-annotations-wisely)
12. [Adopt a Multi-Environment Approach](/blog/kubernetes-best-practices-i-wish-i-had-known-before/#12-adopt-a-multi-environment-approach)
13. [Optimize Your Container Images](/blog/kubernetes-best-practices-i-wish-i-had-known-before/#13-optimize-your-container-images)
14. [Implement a Reliable Logging Strategy](/blog/kubernetes-best-practices-i-wish-i-had-known-before/#14-implement-a-reliable-logging-strategy)
15. [Treat Kubernetes Like Cattle, Not a Pet](/blog/kubernetes-best-practices-i-wish-i-had-known-before/#15-treat-kubernetes-like-cattle-not-a-pet)
16. [Consider a Higher-Level Approach for Complex Deployments](/blog/kubernetes-best-practices-i-wish-i-had-known-before/#16-consider-a-higher-level-approach-for-complex-deployments)
17. [Final Thoughts](/blog/kubernetes-best-practices-i-wish-i-had-known-before/#final-thoughts)

## 1. Don’t Skimp on Resource Requests and Limits

One of the first “aha!” moments in Kubernetes is realizing you can define how much CPU and memory your containers request (guaranteed resources) versus limit (the maximum they’re allowed). Here’s the tricky part: skipping these settings can get you in trouble.

- **Resource Requests:** This is basically your container’s baseline. If your container requests 200m CPU and 512Mi of memory, the Kubernetes scheduler will place your Pod on a node with at least that much capacity available.
- **Resource Limits:** This is the upper bound. If your container tries to exceed the limit, it might get throttled (CPU) or even evicted (memory).

{{% notes type="info" %}}
Pro Tip:

- Start with some baseline, maybe 100–200m CPU, 128–512Mi memory, then tweak as you gather more data.
- Utilise monitoring tools such as Prometheus or Datadog to analyse actual usage and make adjustments as needed.
{{% /notes %}}

## 2. Namespace Like Your Life Depends on It

If you’re deploying everything into the default namespace, oh boy, it’s time for an intervention. Namespaces are a simple yet powerful mechanism to organize (and isolate) resources in your cluster.

- **Team-based namespaces**: Dev, QA, Prod, or per microservice if that makes sense.
- **Access Control**: Combine namespaces with RBAC (Role-Based Access Control) policies to ensure that only the right people (and services) can mess with your stuff.
- **Resource Quotas**: You can set quotas (e.g., CPU, memory) per namespace, preventing one rogue microservice from hogging all resources.

Take a step back and design your namespace strategy; future you will say thanks.

## 3. Avoid Running Multiple Containers in One Pod Unless Necessary

Yes, a Pod can contain multiple containers. But should it? Typically, you only want multiple containers in the same Pod when they’re tightly coupled and must share resources like volumes or network namespaces (e.g., sidecar patterns for logging or security proxies).

Why avoid multi-container Pods?

- **Complexity**: Troubleshooting multiple containers within a single Pod can be a pain.
- **Coupling**: You lose the advantage of scaling containers independently. If you need to scale one container, you end up scaling everything in that Pod.

Follow the “one-container-per-Pod” rule of thumb unless you have a compelling reason (like a sidecar pattern).

{{< related-posts >}}

## 4. Use a Package Manager for Your YAML Files

Manually wrangling a hundred YAML files across multiple microservices is about as fun as debugging spaghetti code at 3 a.m. That’s where tools like Helm, Kustomize, or Timoni come in.

- [Helm](https://helm.sh/): The “package manager for Kubernetes.” It uses charts (templates) that you can customize via values.
- [Kustomize](https://kustomize.io/): A native Kubernetes tool that lets you overlay changes on base YAML manifests.
- [Timoni](https://timoni.sh/): Timoni is a package manager for Kubernetes, powered by CUE and inspired by Helm.

{{% notes type="info" %}}
Pro Tip: If you’re new to Helm, start with an official chart from the Helm Hub or Artifact Hub. Then customize to your heart’s content. You’ll save yourself from YAML duplication mania.

Or, test-drive [Pulumi](/docs/get-started/) and use real programming languages to manage your Kubernetes infrastructure.
{{% /notes %}}

## 5. Ingress and Networking Best Practices

In Kubernetes, networking can get complicated fast. Between Services, Ingress Controllers, and Load Balancers, it’s easy to get tangled. Keep these in mind:

- Use an Ingress Controller / [Gateway API](https://gateway-api.sigs.k8s.io/) (NGINX, Traefik, HAProxy, Istio Gateway, etc.) to manage external access.
- Leverage path-based and subdomain-based routing to simplify your network topology.
- TLS Termination: Terminate SSL/TLS at your ingress layer. You can offload certificate management (e.g., via cert-manager) and keep your cluster traffic secure and efficient.
- Ingress is a powerful concept in Kubernetes, spend time setting it up properly. A messy Ingress config is like a pothole-filled driveway leading to a beautiful mansion.

<div style="display: flex; align-items: center; justify-content: center; height: 100%;">
    <img src="img_1.png" alt="A meme featuring two side-by-side images of Mr. Incredible. The left side shows a normal, happy face labeled “I’M LEARNING KUBERNETES”, while the right side is a dark, distorted version of his face with the same caption, humorously implying the increasing complexity and challenges of learning Kubernetes." style="width: 80%; height: 100%">
</div>

## 6. Lean On Liveness, Readiness, and Startup Probes

Kubernetes is a bit like a personal assistant, but it needs clear instructions. Without properly configured [liveness, readiness, and startup probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/), your cluster will be left guessing about the health of your containers.

- **Liveness Probe**: Checks if your container is alive. If it fails, Kubernetes restarts the container.
- **Readiness Probe**: Checks if your container is ready to serve traffic. Until it’s ready, it doesn’t get traffic.
- **Startup Probe**: Useful for applications that take a while to start up. It prevents the container from being killed prematurely during initial loading.

Pro Tip: Start with readiness probes before liveness probes. You don’t want your containers to get killed simply because they’re not ready yet. Fine-tune the threshold, period, and timeout parameters.

## 7. Mind Your Security: RBAC, Pod Security, and Secrets

Security isn’t just a nice-to-have in Kubernetes—it’s critical. If your cluster is compromised, it’s game over.

1. **RBAC (Role-Based Access Control)**:
    - Implement it from Day 1.
    - Use the Principle of Least Privilege. Give each user, service account, or application only the access they need.

1. **Pod Security**:
    - Use [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) features to enforce standards (e.g., not allowing privileged containers).
    - Ensure you’re not running containers as root unless absolutely necessary.

1. **Manage Secrets Properly**:
    - Don’t store credentials or API keys in plain text inside your container images or environment variables.
    - Do not use Kubernetes Secrets, instead use [External Secret Operator](/docs/esc/integrations/kubernetes/external-secrets-operator/) or [Secret Store CSI Driver](/docs/esc/integrations/kubernetes/secret-store-csi-driver/) to store secrets in external secret stores like [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/), [Pulumi ESC](/docs/esc/), or [HashiCorp Vault](https://www.vaultproject.io/).

## 8. Monitor Everything (And Then Monitor Some More)

Monitoring in Kubernetes isn’t optional—it’s mandatory. With containers popping in and out of existence, you need robust observability to see what’s happening behind the scenes.

- [Prometheus + Grafana](https://github.com/prometheus-operator/kube-prometheus): A classic combo for metrics and dashboards.
- ELK / EFK / [Grafana Loki](https://grafana.com/oss/loki/) Stack: Elastic (or OpenSearch) for logs, plus Kibana and Fluentd/Fluent Bit for log collection or Grafana Loki for logs.
- Jaeger / Zipkin / Tempo: For distributed tracing if you have microservices that call each other.

Set up alerts early. You don’t want your first sign of trouble to be “why is the app so slow?” from an angry user at midnight.

## 9. Automate Deployments with CI/CD

One of the biggest advantages of Kubernetes is that it becomes easier to automate your entire release process. If you’re still doing manual deploys, now’s the time to move to a CI/CD pipeline.

- Jenkins, [GitLab](https://docs.gitlab.com/ee/ci/), GitHub Actions, the choice is yours.
- Embrace [GitOps](https://opengitops.dev/): store all manifests in Git, and let a tool like [Flux](https://fluxcd.io/) or [Argo CD](https://argoproj.github.io/cd/) synchronize them to your cluster.
- Automated rollbacks if a deployment fails.
- Automation not only speeds up delivery but also drastically reduces the room for human error.

## 10. Keep Your Kubernetes Cluster and Components Updated

Running an outdated Kubernetes version is like using a phone running iOS 6 in 2025. Not advisable.

- **Kubernetes Release Cycle**: Minor versions come out roughly [every three months](https://kubernetes.io/releases/release/), with patches more frequently.
- **Upgrade Strategies**:
    - Test in a dev environment first.
    - Backup your etcd (the key-value store).
    - Upgrade the control plane, then worker nodes, or use managed services that handle part of this for you (e.g., EKS, GKE, AKS).

Keep your dependencies updated (e.g., container runtime, CNI plugins, etc.) to benefit from the latest security and performance improvements.

## 11. Use Labels and Annotations Wisely

[Labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) and [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) might seem trivial at first, but they’re game-changers for a well-organized cluster.

- **Labels**: Key-value pairs used for grouping and selecting Kubernetes objects. For instance, app=my-app, env=staging, team=payments.
- **Annotations**: Key-value pairs for attaching non-identifying metadata (e.g., version info, contact email, or last-deployed timestamp).

A consistent labeling strategy helps you filter resources quickly and maintain a clear mental map of your cluster.

## 12. Adopt a Multi-Environment Approach

If your dev, staging, and prod environments share a single cluster, you’re playing with fire. While it can be done, best practice is to isolate production workloads from the playground.

- **Separate Clusters**: Have at least one cluster for dev/staging and one for production. There are create tools like [vCluster](https://www.vcluster.com/) to create virtual clusters within a single cluster.
- **Namespace Segregation**: If you must run them in the same cluster, use strict namespace-based isolation and RBAC rules.

Keeping environments separate reduces risk and makes it easier to test new features in a sandbox.

## 13. Optimize Your Container Images

Don’t ship monstrous container images with half of Ubuntu plus random leftovers. This leads to slow deployments and wasted resources.

- Use lightweight base images like [distroless](https://github.com/GoogleContainerTools/distroless), alpine, or minimal OS-based images.
- Clean up temporary files and dependencies within Dockerfiles.
- Scan your images regularly for vulnerabilities using tools like [Trivy](https://trivy.dev/latest/) or [Anchore](https://anchore.com/).

{{% notes type="info" %}}

Smaller images = faster pull times = less time to scale your app = better user experience.

{{% /notes %}}

## 14. Implement a Reliable Logging Strategy

Logs are your go-to for troubleshooting—and in Kubernetes, you need a solution that can handle ephemeral Pods.

- **Centralized Logging**: Whether it’s ELK/EFK, Splunk, or a managed service, make sure logs aren’t just sitting in ephemeral container storage.
- **Structured Logging**: JSON or another structured format helps your logging system parse and filter logs more effectively.
- **Log Retention and Rotation**: Define clear policies to prevent your log storage from ballooning.

Trust me, you don’t want to scramble for logs in the midst of a production incident.

{{< related-posts >}}

## 15. Treat Kubernetes Like Cattle, Not a Pet

The old adage for servers—“treat them like cattle, not pets”—applies to Kubernetes too. Don’t rely on manual fixes or human intervention. Strive for immutable infrastructure where possible:

- If something is wrong with a Pod, fix it in the YAML, [Code](/product/infrastructure-as-code/) or container image, redeploy, and let the old one go away.
- Avoid sneaky “quick fixes” on a running container—those changes will vanish the moment Kubernetes restarts the Pod.
- Embrace ephemeral environments and dynamic scaling. That’s what Kubernetes does best!

## 16. Consider a Higher-Level Approach for Complex Deployments  

While native YAML manifests can work for smaller Kubernetes deployments, they often become unwieldy as your projects and teams grow. [Pulumi](/blog/yaml-terraform-pulumi-whats-the-smart-choice-for-deployment-automation-with-kubernetes/) provides a powerful alternative for deployment automation, offering:

- **Real Programming Languages**: Use TypeScript, JavaScript, Python, Go, Java, or C# [for type-safe, testable infrastructure code](/docs/iac/languages-sdks/).
- **Cross-Cloud Flexibility**: Manage resources across [multiple cloud providers](/docs/iac/clouds/) and Kubernetes with a single tool.
- **Reusable Modules**: Abstract common patterns into [reusable components](/docs/iac/using-pulumi/pulumi-packages/), reducing boilerplate and preventing drift.
- **Strong Tooling & Ecosystem**: Benefit from package managers, [IDE integration](/docs/iac/concepts/testing/), and a rich library of shared Pulumi components.

By adopting Pulumi, you can avoid the complexity of juggling endless YAML files and gain a more streamlined, maintainable workflow for your Kubernetes infrastructure.

## Final Thoughts

<div style="display: flex; align-items: center; justify-content: center; height: 100%;">
    <img src="img_2.png" alt="A meme featuring a man slamming a card on a table, labeled “ME”, using “KUBERNETES” to solve “ANY PROBLEM TO SOLVE”, humorously depicting overuse of Kubernetes." style="width: 60%; height: 100%">
</div>

Kubernetes is like a Swiss Army knife: powerful, versatile, but also easy to misuse if you’re not careful. By adopting these best practices, declarative configuration, sensible resource allocations, strong security, robust observability, and automated deployments, you’ll keep your cluster humming smoothly.

If you’ve already learned some lessons the hard way, you’re not alone. But the beauty of Kubernetes is that with each setback, you gain more experience to fine-tune your approach.

Let’s learn (and unlearn) together, so we can keep taming this Kubernetes beast like the pros we are. Or at least, like the pros we will be!

{{< blog/cta-button "Try Pulumi for Free" "/docs/get-started/" >}}

> [!INFO]
> Let's talk about Kubernetes and all you can do! Meet us at:
>
> - **KubeCon Europe Booth S450** - [Request a 1:1 Demo](https://www.pulumi.com/kubecon-europe/)
> - **Google Next'25 booth 1589** - [Join us for a Happy House and/or Request your 1:1 Demo](https://www.pulumi.com/google-next/)
>
> Don’t miss the chance to see Pulumi in action, ask questions, and explore why Kubernetes + Pulumi go better together. 🚀
