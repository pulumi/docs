---
title: "Building Kubernetes PR Previews with Shared Pulumi Components"
date: 2026-10-01
draft: false
allow_long_title: true
feature_image: feature.png
meta_desc: "A pattern for ephemeral PR preview environments alongside persistent Dev, Stage, and Prod stacks, with lessons from operating them at scale."
authors:
    - sangharsh-agarwal
tags:
    - pulumi
    - kubernetes
    - preview-environments
    - ephemeral-environments
    - python
    - best-practices
category: best-practices
resource_links:
    - type: documentation
      url: /docs/iac/concepts/components/
      text: "Learn more about Pulumi components"
      icon: cube
    - type: documentation
      url: /docs/iac/guides/building-extending/components/when-to-build-a-component/
      text: "Learn when to build a component"
      icon: compass
    - type: documentation
      url: /docs/iac/guides/building-extending/components/build-a-component/
      text: "Build a Pulumi component"
      icon: wrench
    - type: documentation
      url: /docs/deployments/concepts/review-stacks/
      text: "Automate previews with Review Stacks"
      icon: git-pull-request
    - type: documentation
      url: /docs/get-started/
      text: "Get started with Pulumi"
      icon: rocket-launch
---

My team develops a microservices application on Kubernetes, with hundreds of PRs opened each day. To let engineers test and review those changes in isolation before they're merged, we give every pull request its own ephemeral environment.

We use Pulumi to define those short-lived PR environments from a [component resource](/docs/iac/concepts/components/) that's shared with our long-lived Dev, Stage, Prod environments. Each PR gets its own Pulumi stack and Kubernetes namespace, which we tear down once the PR is merged or closed.

In this post, I'll walk through how we've implemented this pattern and what we've learned from running it at scale.

<!--more-->

{{% notes %}}
We use a self-managed Pulumi backend, so we manage the end-to-end lifecycle of PR environments ourselves. Pulumi Cloud users can instead use [review stacks](/docs/deployments/concepts/review-stacks/) to automate the lifecycle of ephemeral environments tied to pull requests.
{{% /notes %}}

## How our ephemeral environments work

A Kubernetes namespace gives each PR its own place to run, but to get to a working preview environment we need to do quite a bit on top of that. We still need to deploy the application into that namespace, make it reachable to reviewers, update it as new commits arrive, and remove it when the PR closes. And while a namespace separates the Kubernetes resources for each preview, things like database isolation, access controls, and network policies depend on the application and cluster.

Pulumi gives us a way to define these environments once while managing each one independently. Dev, Stage, Prod, and each PR run the same Pulumi program in separate stacks. The program defines the infrastructure for an environment, while each stack maintains its own configuration and state. For each PR, our CI creates or updates its Pulumi stack as new commits arrive, then destroys it when the PR closes.

## Defining the environment

Our implementation uses a single custom Pulumi component, but for the simplified example below, we’ve split it into two components to make the pattern easier to follow.

* `StackInstance` represents one environment, whether that’s Dev, Stage, Prod, or a PR preview. It creates a namespace within our existing Kubernetes cluster, along with resources shared by the services in that environment, including the Secret used to pull images from the container registry.

* `K8Instance` represents one microservice within that environment. It creates the Kubernetes resources needed to run the service and make it reachable through its preview URL, including a Deployment, Service, and Ingress. Each `K8Instance` uses the namespace and image pull `Secret` created by `StackInstance`, so an environment can contain multiple microservices without each one recreating those shared resources.

The following example assumes that shared infrastructure such as the Kubernetes cluster, ingress controller, and routing is already in place:

```python
import pulumi
import pulumi_kubernetes as k8s


class StackInstance(pulumi.ComponentResource):
    def __init__(self, name: str, namespace_name: str,
                 registry_config: pulumi.Input[str], opts=None):
        super().__init__("example:app:StackInstance", name, {}, opts)

        self.namespace = k8s.core.v1.Namespace(
            f"{name}-namespace",
            metadata={"name": namespace_name},
            opts=pulumi.ResourceOptions(parent=self),
        )
        self.pull_secret = k8s.core.v1.Secret(
            f"{name}-registry",
            metadata={"name": "registry-auth", "namespace": namespace_name},
            type="kubernetes.io/dockerconfigjson",
            string_data={".dockerconfigjson": registry_config},
            opts=pulumi.ResourceOptions(
                parent=self, depends_on=[self.namespace]
            ),
        )
        self.namespace_name = pulumi.Output.from_input(namespace_name)
        self.register_outputs({"namespace": self.namespace_name})


class K8Instance(pulumi.ComponentResource):
    def __init__(self, name: str, stack: StackInstance,
                 image: pulumi.Input[str], host: str, opts=None):
        super().__init__("example:app:K8Instance", name, {}, opts)
        labels = {"app": name}

        deployment = k8s.apps.v1.Deployment(
            f"{name}-deployment",
            metadata={"namespace": stack.namespace_name},
            spec={
                "replicas": 1,
                "selector": {"match_labels": labels},
                "template": {
                    "metadata": {"labels": labels},
                    "spec": {
                        "image_pull_secrets": [{"name": "registry-auth"}],
                        "containers": [{
                            "name": name,
                            "image": image,
                            "ports": [{"container_port": 8080}],
                        }],
                    },
                },
            },
            opts=pulumi.ResourceOptions(
                parent=self, depends_on=[stack.namespace, stack.pull_secret]
            ),
        )
        service = k8s.core.v1.Service(
            f"{name}-service",
            metadata={"name": name, "namespace": stack.namespace_name},
            spec={
                "selector": labels,
                "ports": [{"port": 80, "target_port": 8080}],
            },
            opts=pulumi.ResourceOptions(parent=self, depends_on=[deployment]),
        )
        k8s.networking.v1.Ingress(
            f"{name}-ingress",
            metadata={"namespace": stack.namespace_name},
            spec={
                "rules": [{
                    "host": host,
                    "http": {"paths": [{
                        "path": "/",
                        "path_type": "Prefix",
                        "backend": {"service": {
                            "name": name,
                            "port": {"number": 80},
                        }},
                    }]},
                }],
            },
            opts=pulumi.ResourceOptions(parent=self, depends_on=[service]),
        )
        self.url = pulumi.Output.from_input(f"https://{host}")
        self.register_outputs({"url": self.url})


config = pulumi.Config()
stack = StackInstance(
    "environment",
    namespace_name=config.require("namespace"),
    registry_config=config.require_secret("registryDockerConfig"),
)
web = K8Instance(
    "web",
    stack=stack,
    image=config.require("webImage"),
    host=config.require("webHost"),
    opts=pulumi.ResourceOptions(parent=stack),
)
pulumi.export("namespace", stack.namespace_name)
pulumi.export("web_url", web.url)
```

For a PR environment, we might configure the stack with a namespace such as `pr-1042`, a host such as `pr-1042.preview.example.com`, and the container image built for that PR. Dev, Stage, and Prod use the same program and components with configuration for their own environments. Our example creates the namespace as part of `StackInstance`, but if the namespace already exists outside the stack, we’d pass it into the component instead of creating another one.

Because we destroy the entire PR stack when the PR closes, it should only own resources that are safe to delete with the preview. Shared, long-lived infrastructure stays outside the stack and is passed in where the environment needs it.

## Managing the PR lifecycle

Our CI and cleanup workflow follows three stages for PR stacks:

* **Create**: When a PR is opened, CI creates a Pulumi stack for the preview and runs `pulumi up` to deploy the environment. Pulumi creates the Ingress for the configured preview URL and exports that URL so CI can retrieve it. Once the application is ready and reachable, CI shares the URL with reviewers.

* **Update**: When a new commit is pushed, CI runs `pulumi up` on the same stack with the new container image, updating the existing preview environment to reflect the latest version of the PR. Because `pulumi up` reconciles the entire stack, we review the preview after each update to make sure everything is working as expected.

* **Reconcile and remove**: A scheduled job compares the PR stacks with the current state of their corresponding pull requests. Once a PR is closed and any configured grace period has passed, the job destroys the stack’s resources and removes the empty stack record. (The grace period can give reviewers a little time before the environment disappears.)

To tear down a PR stack, we run:

```bash
pulumi destroy --stack pr-1042 --yes
pulumi stack rm pr-1042 --yes
```

`pulumi destroy` removes the resources managed by the stack, but leaves the stack record in place. We run `pulumi stack rm` only after the destroy succeeds.

The scheduled pass matters even if CI tries to delete a preview as soon as its PR closes. Webhooks and jobs can fail; reconciliation gives missed deletions another chance. The grace period is a team decision, not a universal constant.

## Lessons from running PR previews at scale

From running hundreds of PR environments per day, we’ve learned a few things about keeping them reliable.

### Serialize updates to the same PR stack

Developers sometimes push several commits to a PR in quick succession, which can cause two CI jobs to try to update the same Pulumi stack at once. We encountered stack operation conflicts when this happened.

We now serialize updates for each PR stack, while still allowing different PR stacks to update in parallel. If a CI job is interrupted, we also check the stack for an active operation before starting another update.

### Build cleanup to recover from failures

Cleanup failures can leave behind orphaned PR environments, which become more of a problem as the number of PR stacks grows. Even if CI tries to remove an environment when its PR closes, jobs and webhooks can fail. We run a scheduled reconciliation job to compare existing PR stacks with the current state of their pull requests and retry cleanup for environments that should no longer exist.

Cleanup also needs to account for infrastructure drift. If a resource has been changed or removed outside Pulumi, the stack state may no longer match what’s actually running in Kubernetes. If that causes a destroy to fail, we run `pulumi refresh` to reconcile the state before retrying. We also verify that resources have actually been deleted when the provider can’t confirm their removal.

## The result

On average, it takes about four minutes from the start of `pulumi up` until the PR environment is ready and reachable at its preview URL. That includes deploying the Kubernetes resources, waiting for the application to become ready, and configuring routing (the container image is built beforehand).

This approach lets us use the same Pulumi program and components for PR previews as we do for Dev, Stage, and Prod, while giving each environment its own configuration, state, and lifecycle. It keeps the infrastructure consistent across environments without requiring us to maintain a separate implementation for PR previews.
