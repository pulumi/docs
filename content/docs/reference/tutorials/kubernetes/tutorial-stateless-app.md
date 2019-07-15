---
title: "#6: Run a Stateless App Deployment"
menu:
  reference:
    parent: tutorials-kubernetes
---

In this tutorial, we'll run an application using a [Kubernetes
Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) object. This results in an
automatically scaled out container running inside of a cluster.

This example is authored using Pulumi's programming model in TypeScript instead of YAML and using the `pulumi` CLI for
deployment rather than `kubectl`. This gives us the full power of real languages, combined with immutable
infrastructure, delivering a robust and repeatable update experience.

This example is based on
[this Kubernetes tutorial](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/), and
its full code is [available on GitHub](https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook).

## Objectives

* Create a Deployment using Pulumi that runs Nginx
* Use `pulumi` to deploy this application
* Use `kubectl` to list information about the resulting Kubernetes resources
* Update the deployment's number of replicas using `pulumi`
* Clean up

## Before you begin

You need to have the Pulumi CLI and a working Kubernetes cluster.
[Minikube](https://kubernetes.io/docs/getting-started-guides/minikube) is an easy way to get started.

1. [Install Pulumi]({{< relref "/docs/reference/install.md" >}})
2. [Connect Pulumi to a Kubernetes Cluster]({{< relref "/docs/reference/clouds/kubernetes/setup.md" >}})

## Creating and Running the Application

Normally we would write YAML files to configure them, and then run `kubectl` commands to create and manage the services.
Instead of doing that, we will author our program in code and deploy it with `pulumi`.

To start, we'll need to create a project and stack (a deployment target) for our new project:

### Create and Configure a Project

1.  To create a new Pulumi project, let's use a template:

    ```shell
    $ mkdir k8s-nginx && cd k8s-nginx
    $ pulumi new kubernetes-typescript
    ```

    This command will initialize a fresh project in the `k8s-nginx` newly-created directory.

2.  Next, replace the minimal contents of the template's `index.ts` file with the code for the deployment:

    ```typescript
    import * as pulumi from "@pulumi/pulumi";
    import * as k8s from "@pulumi/kubernetes";

    let config = new pulumi.Config();

    let nginxLabels = { app: "nginx" };
    let nginxDeployment = new k8s.apps.v1.Deployment("nginx-deployment", {
        spec: {
            selector: { matchLabels: nginxLabels },
            replicas: config.getNumber("replicas") || 2,
            template: {
                metadata: { labels: nginxLabels },
                spec: {
                    containers: [{
                        name: "nginx",
                        image: "nginx:1.7.9",
                        ports: [{ containerPort: 80 }]
                    }],
                },
            },
        },
    });

    export let nginx = nginxDeployment.metadata.apply(md => md.name);
    ```

    This code simply creates a Kubernetes Deployment object. The entire Kubernetes object model is
    available to us, giving us the full power of Kubernetes right away.

### Deploying

3.  Now we're ready to deploy our code. To do so, simply run `pulumi up`:

    ```shell
    $ pulumi up
    ```

    The command will first show us a complete preview of what will take place, with a confirmation prompt. No changes
    will have been made yet. It should look something like this:

        Previewing update of stack 'k8s-nginx-dev'
        Previewing changes:

            Type                           Name                     Plan       Info
        +   pulumi:pulumi:Stack            k8s-nginx-k8s-nginx-dev  create
        +   └─ kubernetes:apps:Deployment  nginx-deployment         create

        info: 2 changes previewed:
            + 2 resources to create

        Do you want to perform this update?
        > yes
        no
        details

    Let's select "yes" and hit enter. The deployment will proceed, and the output will look like this:

        Updating stack 'k8s-nginx-dev'
        Performing changes:

            Type                           Name                     Status      Info
        +   pulumi:pulumi:Stack            k8s-nginx-k8s-nginx-dev  created
        +   └─ kubernetes:apps:Deployment  nginx-deployment         created

        ---outputs:---
        nginx: "nginx-deployment-rlefbi4w"

        info: 2 changes performed:
            + 2 resources created
        Update duration: 8.127334048s

        Permalink: https://app.pulumi.com/joeduffy/k8s-nginx-dev/updates/1


    Note that Pulumi will wait until the deployment has succeeded (or failed), and it will print detailed
    status outputs as the deployment happens. This is in contrast to `kubectl` which returns immediately. The
    Pulumi CLI's approach ensures that you have more robust deployments that converge as expected.

4. Now that we've done the deployment, let's check some state with `kubectl`:

    ```shell
    $ kubectl describe deployment $(pulumi stack output nginx)
    ```

    Notice that we used the `pulumi stack output` command to fetch the auto-generated deployment name.

    The output will look similar to this:

    ```
    Name:     nginx-deployment-rlefbi4w
    Namespace:    default
    CreationTimestamp:  Tue, 30 Aug 2018 18:11:37 -0700
    Labels:     app=nginx
    Annotations:    deployment.kubernetes.io/revision=1
    Selector:   app=nginx
    Replicas:   2 desired | 2 updated | 2 total | 2 available | 0 unavailable
    StrategyType:   RollingUpdate
    MinReadySeconds:  0
    RollingUpdateStrategy:  1 max unavailable, 1 max surge
    Pod Template:
      Labels:       app=nginx
      Containers:
       nginx:
        Image:              nginx:1.7.9
        Port:               80/TCP
        Environment:        <none>
        Mounts:             <none>
      Volumes:              <none>
    Conditions:
      Type          Status  Reason
      ----          ------  ------
      Available     True    MinimumReplicasAvailable
      Progressing   True    NewReplicaSetAvailable
    OldReplicaSets:   <none>
    NewReplicaSet:    nginx-deployment-rlefbi4w-1771418926 (2/2 replicas created)
    No events.
    ```

    Let's also list the pods created by this deployment:

    ```shell
    $ kubectl get pods -l app=nginx
    ```

    The output will look something like this:

    ```
    NAME                                        READY     STATUS    RESTARTS   AGE
    nginx-deployment-rlefbi4w-1771418926-7o5ns   1/1       Running   0          1m
    nginx-deployment-rlefbi4w-1771418926-r18az   1/1       Running   0          1m
    ```

### Updating the Deployment

You can update your program by changing the source code and re-running `pulumi up`. Let's do two quick updates
to see what this looks like. After that, we'll clean up and we're done!

5. Let's update our version of Nginx from 1.7 to 1.8. Simply replace the line

    ```typescript
                        image: "nginx:1.7.9",
    ```

    with

    ```typescript
                        image: "nginx:1.8",
    ```

    and re-run `pulumi up`. We will see a preview that indicates just the spec changed:

        Previewing update of stack 'k8s-nginx-dev'
        Previewing changes:

            Type                           Name                     Plan          Info
        *   pulumi:pulumi:Stack            k8s-nginx-k8s-nginx-dev  no change
        ~   └─ kubernetes:apps:Deployment  nginx-deployment         update        changes: ~ spec

            ---outputs:---
            nginx: "nginx-deployment-rlefbi4w"

        info: 1 change previewed:
            ~ 1 resource to update
            1 resource unchanged

        Do you want to perform this update?
        yes
        no
        > details

    If we choose `details` and hit enter we will see a full diff of the changes:

        * pulumi:pulumi:Stack: (same)
            [urn=urn:pulumi:k8s-nginx-dev::k8s-nginx::pulumi:pulumi:Stack::k8s-nginx-k8s-nginx-dev]
            ---outputs:---
            nginx: "nginx-deployment-rlefbi4w"
            ~ kubernetes:apps/v1:Deployment: (update)
                [id=default/nginx-deployment-rlefbi4w]
                [urn=urn:pulumi:k8s-nginx-dev::k8s-nginx::kubernetes:apps/v1:Deployment::nginx-deployment]
            ~ spec      : {
                ~ template: {
                    ~ spec    : {
                        ~ containers: [
                            ~ [0]: {
                                    ~ image: "nginx:1.7.9" => "nginx:1.8"
                                    }
                            ]
                        }
                    }
                }


    If we select `yes` and hit enter to proceed with the update, the deployment will be updated in place.

6.  Next, let's scale our application by increasing the replica count. You may have noticed this example used
    the Pulumi configuration system so that the replica count can be easily changed. Simply run

    ```shell
    $ pulumi config set replicas 4
    ```

    and re-run `pulumi up`. Pulumi will figure out the minimal set of changes to make:

    ```shell
    $ pulumi up
    ```

    The output from running this command will look like the usual update, with a preview diff, prompt, and details.

### Cleaning Up

From here, feel free to experiment. As soon as you're done, let's clean up our stack:

```shell
$ pulumi destroy --yes
$ pulumi stack rm --yes
```

Afterwards, query the list of pods to verify that none are remaining:

```shell
$ kubectl get pods -l app=nginx
```

This should print out something along these lines:

```
No resources found.
```
