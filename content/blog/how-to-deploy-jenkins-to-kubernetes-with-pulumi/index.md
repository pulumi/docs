---
title: "How to deploy Jenkins to Kubernetes with Pulumi"
date: "2018-06-27"
authors: ["sean-gillespie"]
tags: ["Kubernetes"]
meta_desc: "In this blog, we'll see how to run Jenkins on Kubernetes with Pulumi, based on adapting a Helm template."
---

In this blog post, we'll see how to run
[Jenkins on Kubernetes with Pulumi](https://github.com/pulumi/examples/tree/master/kubernetes-ts-jenkins).
We abstract away the complexity of the configuration into a reusable
component to enable it to be reused by team mates. Our example is based
on adapting a Helm template.
<!--more-->

## Reusing the Jenkins component

Once the component is created, it can be reused with just a few lines of
implementation code.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as jenkins from "./jenkins";

const config = new pulumi.Config("jenkins");
const instance = new jenkins.Instance("jenkins", {
    name: "jenkins",
    credentials: {
        username: config.require("username"),
        password: config.require("password"),
    },
    resources: {
        memory: "512Mi",
        cpu: "100m",
    }
});
```

We could take the component code and prepare a fully reusable NPM
package, but as this is just an example, we've simply maintained the
code as an included class.

## Running the App

Follow the steps in
[Pulumi Installation and Setup]({{< relref "/docs/get-started/install" >}}) and
[Configuring Pulumi Kubernetes]({{< relref "/docs/get-started/kubernetes" >}})
to get setup with Pulumi and Kubernetes.

> *Note*: The code in this repo assumes you are deploying to a cluster
> that supports the `LoadBalancer` service type. This includes most
> cloud providers as well as [Docker for Mac Edge w/ Kubernetes](https://docs.docker.com/docker-for-mac/kubernetes/). If
> not (for example if you are targeting `minikube` or your own custom
> Kubernetes cluster), replace `type: "LoadBalancer"` with
> `type: "ClusterIP"` in `jenkins.ts`. See the Kubernetes [Services docs](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services---service-types)
> for more details.

Clone the repo and navigate to the Jenkins example:

    $ git clone https://github.com/pulumi/examples.git
    $ cd kubernetes-ts-jenkins

Install dependencies:

    $ npm install

Create a new stack:

    $ pulumi stack init
    Enter a stack name: kubernetes-ts-jenkins-dev

Create configuration keys for the root username and password for the
Jenkins instance we are about to create:

    $ pulumi config set jenkins:username <your desired username>
    $ pulumi config set jenkins:password <your desired password> --secret

Preview the deployment of the application:

    $ pulumi preview
    Previewing update of stack 'kubernetes-ts-jenkins-dev'
         Type    Name    Status        Info
     *   global  global  unchanged
    Previewing changes:

         Type                                            Name                                             Status        Info
     *   global                                          global                                           no change
     +   pulumi:pulumi:Stack                             kubernetes-ts-jenkins-kubernetes-ts-jenkins-dev  create
     +   └─ jenkins:jenkins:Instance                     jenkins                                          create
     +      ├─ kubernetes:core:v1:Secret                 jenkins-secret                                   create
     +      ├─ kubernetes:core:v1:PersistentVolumeClaim  jenkins-pvc                                      create
     +      ├─ kubernetes:core:v1:Service                jenkins-service                                  create
     +      └─ kubernetes:extensions:v1beta1:Deployment  jenkins-deploy                                   create

    info: 6 changes previewed:
        + 6 resources to create

Perform the deployment:

    $ pulumi update --skip-preview
    Updating stack 'kubernetes-ts-jenkins-dev'
         Type    Name    Status        Info
     *   global  global  unchanged
    Performing changes:

         Type                                            Name                                             Status        Info
     *   global                                          global                                           unchanged
     +   pulumi:pulumi:Stack                             kubernetes-ts-jenkins-kubernetes-ts-jenkins-dev  created
     +   └─ jenkins:jenkins:Instance                     jenkins                                          created
     +      ├─ kubernetes:core:v1:Secret                 jenkins-secret                                   created
     +      ├─ kubernetes:core:v1:PersistentVolumeClaim  jenkins-pvc                                      created
     +      ├─ kubernetes:core:v1:Service                jenkins-service                                  created
     +      └─ kubernetes:extensions:v1beta1:Deployment  jenkins-deploy                                   created

    info: 6 changes performed:
        + 6 resources created
    Update duration: 2m30.397621136s

The deployment is complete! Use `kubectl` to see the Service that we
just deployed:

    $ kubectl get services
    NAME         TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                      AGE
    jenkins      LoadBalancer   10.43.241.251   35.230.56.127   80:30638/TCP,443:30204/TCP   3m

The Jenkins instance we just deployed is reachable through port 80 of
the external IP address. You can now visit
`http://35.230.56.127/jenkins/login` in a Web browser to begin the
first-install flow for your new Jenkins instance. You can use the
username and password that you saved in your Pulumi config to log in to
your new Jenkins instance.

> *Note*: If you are deploying to a cluster that does not support
> `type: "LoadBalancer"`, and deployed the example using
> `type: "ClusterIP"` instead, run
> `kubectl port-forward svc/jenkins 8080:80` to forward the cluster port
> to the local machine and access the service via `localhost:8080`.

When you're ready to be done with Jenkins, you can destroy the
instance:

    $ pulumi destroy
    Do you want to perform this destroy? yes
    Destroying stack 'kubernetes-ts-jenkins-dev'
    Performing changes:

         Type                                            Name                                             Status      Info
     -   pulumi:pulumi:Stack                             kubernetes-ts-jenkins-kubernetes-ts-jenkins-dev  deleted
     -   └─ jenkins:jenkins:Instance                     jenkins                                          deleted
     -      ├─ kubernetes:extensions:v1beta1:Deployment  jenkins-deploy                                   deleted
     -      ├─ kubernetes:core:v1:Service                jenkins-service                                  deleted
     -      ├─ kubernetes:core:v1:PersistentVolumeClaim  jenkins-pvc                                      deleted
     -      └─ kubernetes:core:v1:Secret                 jenkins-secret                                   deleted

    info: 6 changes performed:
        - 6 resources deleted
    Update duration: 18.202009282s

## Next Steps

This example showed just a little of the potential of reusing components
and code, instead of copy and pasting config, to improve productivity
and comprehension for building cloud stacks.

Find out more:

- Get the [example code on GitHub](https://github.com/pulumi/examples/tree/master/kubernetes-ts-jenkins)
- Read the docs on [Kubernetes]({{< relref "/docs/reference/pkg/kubernetes/" >}})
- See the tutorial on [building components]({{< relref "/docs/tutorials/aws/s3-folder-component" >}})
