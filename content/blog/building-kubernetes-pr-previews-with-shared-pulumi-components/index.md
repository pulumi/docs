---
title: "Building Kubernetes PR Previews with Shared Pulumi Components"
date: 2026-09-24
draft: false
allow_long_title: true
meta_desc: "A StackInstance and K8Instance pattern for separate Dev, Stage, Prod, and PR stacks, with lessons from operating PR previews at scale."
authors:
    - sangharsh-agarwal
tags:
    - pulumi
    - kubernetes
    - preview-environments
    - python
    - best-practices
category: tutorials
---

On my team, Dev, Stage, Prod, and pull-request preview environments each have their own Pulumi stack while sharing the same code path. PR stacks are short-lived; the other stacks are long-lived. This post shows a component pattern for those different lifecycles and some lessons from operating PR previews at scale.

<!--more-->

Our implementation uses a shared `Instance(pulumi.ComponentResource)` class. The example below separates its stack-level and service-level responsibilities into two components to make the pattern easier to follow. It uses example resource names and assumes a cluster, ingress controller, and routing are already in place.

## The problem is the whole lifecycle

A namespace gives a PR a place to run, but it does not answer who creates the deployment and Service, how reviewers find the preview, or what removes those resources after the PR closes. A separate PR-only implementation would also need to track changes to the longer-lived environments. Separate stacks give each environment its own state and lifecycle; the shared component keeps resource declarations consistent.

There is also a boundary question: a preview may use shared infrastructure such as a cluster, container registry, or database server. Deleting its stack must not delete those shared resources. Database isolation, access controls, and network policy need to be designed for the actual application and cluster; a Kubernetes namespace alone does not provide them.

The useful unit of ownership is therefore *one environment's managed resources*, with its dependencies kept explicit. The PR's stack owns disposable resources; Dev, Stage, and Prod stacks instantiate the same component with different settings.

## Compose stack-level and service-level components

A Pulumi [stack](/docs/iac/concepts/stacks/) runs a program with its own configuration and state. Dev, Stage, Prod, and each PR have separate stacks but use the same code. In this example, `StackInstance` owns the namespace and image pull Secret; each `K8Instance` owns the resources for one microservice. This decomposition illustrates the ownership pattern without reproducing our internal code.

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

For example, a PR stack might receive `namespace=pr-1042` and `webHost=pr-1042.preview.example.com`. Dev, Stage, and Prod stacks receive their own namespace, host, image, and registry configuration. Each stack runs the same program and creates the same component types. The `web` service shown here is one `K8Instance`; the program can instantiate additional `K8Instance` components for other microservices.

The image pull Secret comes from Pulumi secret configuration. The example omits application secrets, ingress-specific settings, DNS, and TLS. The exported URL is an address; CI checks that the application is ready before sharing it with reviewers. Where a namespace is already managed outside the stack, pass it into the component instead of creating another one.

## Keep ownership aligned with lifetime

The division follows the resources' lifetimes:

| Component | Resources it owns | Lifetime |
| --- | --- | --- |
| `StackInstance` | Namespace and resources shared by services in that namespace, such as an image pull Secret | The environment's stack |
| `K8Instance` | One microservice's Deployment, Service, and routing resources | A child of that environment's stack |

The program creates one `StackInstance`, then a `K8Instance` for each microservice. Each service receives the namespace and shared image pull Secret from the stack-level component. That way, several services can use the Secret without each declaring its own copy.

The same composition runs in Dev, Stage, Prod, and PR stacks with different configuration. Destroying a PR stack removes its managed namespace and service resources; the shared cluster and other stacks have separate lifecycles.

## Give each stack the right lifecycle

Dev, Stage, and Prod are persistent stacks. Each PR has a separate, disposable stack. Our CI and cleanup workflow follows three stages for PR stacks:

1. **Create:** When a PR is opened, select or initialize its stack and run `pulumi up` with that PR's image. Publish the resulting URL for reviewers once application readiness and routing checks pass.
2. **Update:** On a new commit, run `pulumi up` on the **same** stack with the new image reference. Stable resource names and unchanged inputs let Pulumi plan the appropriate update; always review the preview because other changed inputs can still cause replacements.
3. **Reconcile and remove:** A scheduled job compares PR stacks with source-control state. Once a PR is closed and any configured grace period has passed, the job destroys its stack, removes the empty stack record, and retries failed cleanup on a later run.

For a stack selected for teardown, the normal path is:

```bash
pulumi destroy --stack pr-1042 --yes
pulumi stack rm pr-1042 --yes
```

Run `stack rm` after a successful destroy. Pulumi's [`destroy`](/docs/iac/cli/commands/pulumi_destroy/) removes managed resources but leaves the stack record unless it is removed separately.

The scheduled pass matters even if CI tries to delete a preview as soon as its PR closes. Webhooks and jobs can fail; reconciliation gives missed deletions another chance. The grace period is a team decision, not a universal constant.

## Plan for overlapping updates and cleanup failures

Fast follow-up commits can start two updates against one PR stack. We encountered stack-operation conflicts while building this workflow. CI can serialize updates **per PR stack** while allowing different PR stacks to deploy in parallel. If a job is interrupted, check the active operation and stack state before retrying.

Cleanup has its own edge cases. A resource may have been changed or removed outside Pulumi, leaving stack state out of sync with Kubernetes. [`pulumi refresh`](/docs/iac/cli/commands/pulumi_refresh/) can reconcile that state before another destroy attempt. A failed destroy should be retried, with resource deletion verified when the provider cannot confirm it.

The scheduled cleanup job provides another chance if a PR-close event, CI job, or first destroy attempt fails. This matters more as the number of PR stacks grows.

## Measure the outcome

We deploy **hundreds of PR environments each day**. From the start of `pulumi up` to an application that is ready and reachable through its preview URL, deployment takes **about four minutes on average**. That includes deploying the Kubernetes resources, application readiness, and routing. **Container image build time is excluded**; the image is available before this measurement starts.

At that volume, cleanup cannot depend on someone noticing an abandoned environment. A scheduled pass makes it part of the normal workflow and gives failures a clear path to retry.

One code path and separate stacks keep Dev, Stage, Prod, and PR environments consistent while giving each its own lifecycle. The `StackInstance` and `K8Instance` example makes the ownership boundary visible: the stack owns shared namespace resources, and each service owns its deployment and routing. For PR environments, that boundary works alongside repeatable updates and scheduled cleanup.

{{< blog/cta-button "Try Pulumi for Free" "/docs/get-started/" >}}
