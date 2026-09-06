---
title_tag: "Pulumi Kubernetes Operator | Integrations"
meta_desc: Use the Pulumi Kubernetes Operator to manage Pulumi stacks from within Kubernetes, driven by commits in git, Kubernetes objects, or Flux sources.
title: Pulumi Kubernetes Operator
h1: Pulumi Kubernetes Operator
menu:
    integrations:
        name: Pulumi Kubernetes Operator
        parent: kubernetes-clouds
        identifier: kubernetes-clouds-operator
        weight: 5
aliases:
- /docs/iac/guides/continuous-delivery/pulumi-kubernetes-operator/
- /docs/iac/using-pulumi/continuous-delivery/pulumi-kubernetes-operator/
- /docs/guides/continuous-delivery/pulumi-kubernetes-operator/
- /docs/using-pulumi/continuous-delivery/pulumi-kubernetes-operator/
- /docs/iac/packages-and-automation/continuous-delivery/pulumi-kubernetes-operator/
---

The [Pulumi Kubernetes Operator](https://github.com/pulumi/pulumi-kubernetes-operator) automates the deployment of Pulumi [stacks][stack] from within Kubernetes. The Pulumi program for a stack can come from a [Program resource][], from a Git repository, or from a [Flux source][flux-source], and may be authored in any supported Pulumi language (TypeScript, Python, Go, .NET, Java, YAML).

[Program resource]: https://github.com/pulumi/pulumi-kubernetes-operator/blob/master/docs/programs.md
[flux-source]: https://fluxcd.io/flux/components/source/

## Overview

The Pulumi Kubernetes Operator provides [custom resources][k8s-ext-pattern] to:

- Provision a workspace (an execution environment) for a Pulumi project
- Keep a Pulumi stack up-to-date using gitops
- Write [Pulumi YAML][] programs as Kubernetes objects
- Run Pulumi deployment operations

Deploying Pulumi stacks using Kubernetes provides the capability to build out CI/CD and other automation systems, and to manage your infrastructure alongside your Kubernetes workloads or in dedicated control-plane clusters.

[k8s-ext-pattern]: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
[stack]: /docs/iac/concepts/stacks/
[Pulumi YAML]: /docs/iac/languages-sdks/yaml/

## In this section

- **[Installation](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/installation/)** — install the operator, create a service account, and configure Pulumi Cloud access and Pulumi ESC.
- **[Defining stacks](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/defining-stacks/)** — create a `Stack` resource from a Git repository, Flux source, or Program object, and set its configuration and environment variables.
- **[Stack operations](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/stack-operations/)** — drift detection, state refresh, cleanup, prerequisites, external triggers, and preview mode.
- **[Rolling out changes](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/rolling-out-changes/)** — approve changes upstream, preview before they reach the operator, and stage a rollout across environments with prerequisites.

Detailed documentation on the Stack API is available in the [operator repository][pko-stacks].

[pko-stacks]: https://github.com/pulumi/pulumi-kubernetes-operator/blob/master/docs/stacks.md

## Use with Argo CD

You can combine the operator with Argo CD to manage the lifecycle of your `Stack` resources using the GitOps paradigm, driving Pulumi deployments from the Argo CD UI or CLI. For comprehensive guidance—including a trunk-based GitOps workflow, preview environments, and sync waves—see the dedicated [Argo CD with Pulumi Kubernetes Operator](/docs/iac/operations/continuous-delivery/argocd/) documentation.

## More information

More examples are available in the [pulumi/pulumi-kubernetes-operator][pko-examples] repository.

Check out [troubleshooting](https://github.com/pulumi/pulumi-kubernetes-operator/blob/master/docs/troubleshooting.md) for more details, look at [known issues](https://github.com/pulumi/pulumi-kubernetes-operator/issues/), or open a [new issue](https://github.com/pulumi/pulumi-kubernetes-operator/issues/new) in GitHub.

[pko-examples]: https://github.com/pulumi/pulumi-kubernetes-operator/tree/master/examples
