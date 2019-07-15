---
title: "#3: Guestbook App with Redis and Nginx"
menu:
  reference:
    parent: tutorials-kubernetes
---

In this tutorial, we'll build and deploy
[the standard Kubernetes Guestbook example](https://github.com/kubernetes/examples/tree/master/guestbook) using Pulumi.

The guestbook is a simple, multi-tier web application that uses Redis and Nginx, powered by Docker containers and
Kubernetes. The primary difference between this example and the standard Kubernetes one is that we'll be authoring it in
TypeScript instead of YAML, and we'll deploy it using `pulumi` rather than `kubectl`. This gives us the full power of
real languages, combined with immutable infrastructure, delivering a robust and repeatable update experience.

The code for this tutorial is
[available on GitHub](https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook).

## Objectives

* Start up a Redis master
* Start up Redis slaves
* Start up the guestbook frontend
* Expose and view the frontend service
* Clean up

## Before you begin

You need to have the Pulumi CLI and a working Kubernetes cluster.
[Minikube](https://kubernetes.io/docs/getting-started-guides/minikube) is an easy way to get started.

1. [Install Pulumi]({{< relref "/docs/reference/install.md" >}})
2. [Connect Pulumi to a Kubernetes Cluster]({{< relref "/docs/reference/clouds/kubernetes/setup.md" >}})

## Running the Guestbook

The guestbook application uses Redis to store its data. It writes its data to a Redis master instance and reads data
from multiple Redis slave instances.

Normally we would write YAML files to configure them, and then run `kubectl` commands to create and manage the services.
Instead of doing that, we will author our program in code and deploy it with `pulumi`.

To start, we'll need to create a project and stack (a deployment target) for our new project:

### Create and Configure a Project

1.  To create a new Pulumi project, let's use a template:

    ```shell
    $ mkdir k8s-guestbook && cd k8s-guestbook
    $ pulumi new kubernetes-typescript
    ```

    This command will initialize a fresh project in the `k8s-guestbook` newly-created directory.

2.  Next, replace the minimal contents of the template's `index.ts` file with the full guestbook:

    ```javascript
    import * as k8s from "@pulumi/kubernetes";
    import * as pulumi from "@pulumi/pulumi";

    let config = new pulumi.Config();
    let useLoadBalancer = config.getBoolean("useLoadBalancer");

    // REDIS MASTER
    let redisMasterLabels = { app: "redis", tier: "backend", role: "master"};
    let redisMasterService = new k8s.core.v1.Service("redis-master", {
        metadata: {
            name: "redis-master",
            labels: redisMasterLabels,
        },
        spec: {
            ports: [{ port: 6379, targetPort: 6379 }],
            selector: redisMasterLabels,
        },
    });
    let redisMasterDeployment = new k8s.apps.v1.Deployment("redis-master", {
        metadata: { name: "redis-master" },
        spec: {
            selector: { matchLabels: redisMasterLabels },
            replicas: 1,
            template: {
                metadata: { labels: redisMasterLabels },
                spec: {
                    containers: [{
                        name: "master",
                        image: "k8s.gcr.io/redis:e2e",
                        resources: {
                            requests: {
                                cpu: "100m",
                                memory: "100Mi",
                            },
                        },
                        ports: [{ containerPort: 6379 }],
                    }],
                },
            },
        },
    });

    // REDIS SLAVE
    let redisSlaveLabels = { app: "redis", tier: "backend", role: "slave" };
    let redisSlaveService = new k8s.core.v1.Service("redis-slave", {
        metadata: {
            name: "redis-slave",
            labels: redisSlaveLabels,
        },
        spec: {
            ports: [{ port: 6379, targetPort: 6379 }],
            selector: redisSlaveLabels,
        },
    });
    let redisSlaveDeployment = new k8s.apps.v1.Deployment("redis-slave", {
        metadata: { name: "redis-slave" },
        spec: {
            selector: { matchLabels: redisSlaveLabels },
            replicas: 1,
            template: {
                metadata: { labels: redisSlaveLabels },
                spec: {
                    containers: [{
                        name: "slave",
                        image: "gcr.io/google_samples/gb-redisslave:v1",
                        resources: {
                            requests: {
                                cpu: "100m",
                                memory: "100Mi",
                            },
                        },
                        env: [{
                            name: "GET_HOSTS_FROM",
                            value: "dns",
                            // Using `GET_HOSTS_FROM=dns` requires your cluster to provide a dns service. As of
                            // Kubernetes 1.3, DNS is a built-in service launched automatically. However, if the
                            // cluster you are using does not have a built-in DNS service, you can instead access an
                            // environment variable to find the master service's host. To do so, comment out the
                            // 'value: "dns"' line above, and uncomment the line below:
                            // value: "env",
                        }],
                        ports: [{ containerPort: 6379 }],
                    }],
                },
            },
        },
    });

    // FRONTEND
    let frontendLabels = { app: "guestbook", tier: "frontend" };
    let frontendService = new k8s.core.v1.Service("frontend", {
        metadata: {
            name: "frontend",
            labels: frontendLabels,
        },
        spec: {
            type: useLoadBalancer ? "LoadBalancer" : "ClusterIP",
            ports: [{ port: 80 }],
            selector: frontendLabels,
        },
    });
    let frontendDeployment = new k8s.apps.v1.Deployment("frontend", {
        metadata: { name: "frontend" },
        spec: {
            selector: { matchLabels: frontendLabels },
            replicas: 3,
            template: {
                metadata: { labels: frontendLabels },
                spec: {
                    containers: [{
                        name: "php-redis",
                        image: "gcr.io/google-samples/gb-frontend:v4",
                        resources: {
                            requests: {
                                cpu: "100m",
                                memory: "100Mi",
                            },
                        },
                        env: [{
                            name: "GET_HOSTS_FROM",
                            value: "dns",
                            // Using `GET_HOSTS_FROM=dns` requires your cluster to provide a dns service. As of
                            // Kubernetes 1.3, DNS is a built-in service launched automatically. However, if the
                            // cluster you are using does not have a built-in DNS service, you can instead access an
                            // environment variable to find the master service's host. To do so, comment out the
                            // 'value: "dns"' line above, and uncomment the line below:
                            // value: "env",
                        }],
                        ports: [{ containerPort: 80 }],
                    }],
                },
            },
        },
    });

    export let frontendIP: pulumi.Output<string>;
    if (useLoadBalancer) {
        frontendIP = frontendService.status.apply(status => status.loadBalancer.ingress[0].ip);
    } else {
        frontendIP = frontendService.spec.apply(spec => spec.clusterIP);
    }
    ```

    This code creates three Kubernetes Services, each with an associated Deployment. The full Kubernetes object model is
    available to us, giving us the full power of Kubernetes right away.

3.  (Optional) By default, our frontend Service will be of type `ClusterIP`. This will work on Minikube, but for most
    production Kubernetes clusters, we will want it to be of type `LoadBalancer`, ensuring that a load balancer in your
    target cloud environment is allocated.

    The above code uses [configuration]({{< relref "/docs/reference/config.md" >}}) to make this parameterizable.
    If you'd like our program to use a load balancer, simply run:

    ```shell
    $ pulumi config set useLoadBalancer true
    ```

    If you're not sure, it's safe to skip this step.

### Deploying

4.  Now we're ready to deploy our code. To do so, simply run `pulumi up`:

    ```
    $ pulumi up
    ```

    The command will first show us a complete preview of what will take place, with a confirmation prompt. No changes
    will have been made yet. It should look something like this:


        Previewing update of stack 'k8s-guestbook-dev'
        Previewing changes:

            Type                           Name                             Plan       Info
        +   pulumi:pulumi:Stack            k8s-guestbook-k8s-guestbook-dev  create
        +   ├─ kubernetes:core:Service     redis-master                     create
        +   ├─ kubernetes:core:Service     redis-slave                      create
        +   ├─ kubernetes:core:Service     frontend                         create
        +   ├─ kubernetes:apps:Deployment  redis-master                     create
        +   ├─ kubernetes:apps:Deployment  redis-slave                      create
        +   └─ kubernetes:apps:Deployment  frontend                         create

        info: 7 changes previewed:
            + 7 resources to create

        Do you want to perform this update?
        > yes
        no
        details


    Let's select "yes" and hit enter. The deployment will proceed, and the output will look like this:


        Updating stack 'k8s-guestbook-dev'
        Performing changes:

            Type                           Name                             Status      Info
        +   pulumi:pulumi:Stack            k8s-guestbook-k8s-guestbook-dev  created
        +   ├─ kubernetes:core:Service     redis-slave                      created     1 info message
        +   ├─ kubernetes:core:Service     frontend                         created     1 info message
        +   ├─ kubernetes:core:Service     redis-master                     created     1 info message
        +   ├─ kubernetes:apps:Deployment  redis-master                     created
        +   ├─ kubernetes:apps:Deployment  redis-slave                      created
        +   └─ kubernetes:apps:Deployment  frontend                         created

        Diagnostics:
        kubernetes:core:Service: redis-slave
            info: ✅ Service 'redis-slave' successfully created endpoint objects

        kubernetes:core:Service: frontend
            info: ✅ Service 'frontend' successfully created endpoint objects

        kubernetes:core:Service: redis-master
            info: ✅ Service 'redis-master' successfully created endpoint objects

        ---outputs:---
        frontendIP: "10.102.193.86"

        info: 7 changes performed:
            + 7 resources created
        Update duration: 16.226520447s

        Permalink: https://app.pulumi.com/joeduffy/k8s-guestbook-dev/updates/1


### Viewing the Guestbook

5.  The application is now running in our cluster. Let's inspect our cluster state to validate the deployment.

    Use `kubectl` to see the deployed services:

    ```shell
    $ kubectl get services
    ```

    We should see entries for each of the four Services we've created in our program:

    ```
    NAME           TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
    frontend       ClusterIP   10.102.193.86   <none>        80/TCP     2m
    kubernetes     ClusterIP   10.96.0.1       <none>        443/TCP    1d
    redis-master   ClusterIP   10.98.205.37    <none>        6379/TCP   2m
    redis-slave    ClusterIP   10.96.9.70      <none>        6379/TCP   2m
    ```

    The `pulumi stack output` command prints exported program variables:

    ```shell
    $ pulumi stack output frontendIP
    ```

    The value of the `frontendIP` variable matches either `frontend`'s `CLUSTER-IP` (if you're
    deploying with `useLoadBalancer` set to `false`) or `frontend`'s `EXTERNAL-IP` (if you're
    deploying with `useLoadBalancer` set to `true`). For example:

    ```
    10.102.193.86
    ```

5.  Now let's see our guestbook application in action.

    ![Guestbook in browser](/images/docs/quickstart/kubernetes/guestbook.png)

    **No Load Balancer (Minikube):**

    Because Minikube doesn't support the `LoadBalancer` type, our example above uses `ClusterIP`. In order to
    browse to it, we will first need to forward a port on `localhost` to it. To do so, run:

    ```shell
    $ kubectl port-forward svc/frontend 8765:80
    ```

    At this point, we can view our running guestbook application:

    ```shell
    $ curl localhost:8765
    ```

    The HTML from the guestbook will be fetched and printed:

    ```
    <html ng-app="redis">
      <head>
      <title>Guestbook</title>
      ...
    </html>
    ```

    **Using a Load Balancer:**

    If you are instead running this program in a real cluster, and set `useLoadBalancer` to `true` in step 3,
    then you can simply access your guestbook application with:

    ```shell
    $ curl $(pulumi stack output frontendIP)
    ```

    The HTML from the guestbook will be fetched and printed:

    ```
    <html ng-app="redis">
      <head>
      <title>Guestbook</title>
      ...
    </html>
    ```

6.  We're almost done. To demonstrate incremental updates, however, Let's make an update to our program to scale
    the frontend from 3 replicas to 5. Find the line:

    ```typescript
            replicas: 3,
    ```

    and change it to:

    ```typescript
            replicas: 5,
    ```

    Or simply run `sed -i "s/replicas: 3/replicas: 5/g" index.ts`.

    Now all we need to do is run `pulumi up`, and Pulumi will figure out the minimal set of changes to make:

    ```shell
    $ pulumi up -y --skip-preview
    ```

    The output from running this command should look something like this:


        Updating stack 'k8s-guestbook-dev'
        Performing changes:

                Type                           Name                             Plan          Info
            *   pulumi:pulumi:Stack            k8s-guestbook-k8s-guestbook-dev  no change
            ~   └─ kubernetes:apps:Deployment  frontend                         updated       changes: ~ spec

        info: 1 change performed:
            ~ 1 resource updated
              6 resources unchanged


### Cleaning Up

7.  Feel free to experiment. As soon as you're done, let's clean up and destroy the resources and remove our stack:

    ```shell
    $ pulumi destroy --yes
    $ pulumi stack rm --yes
    ```

    Afterwards, query the list of pods to verify that none are remaining:

    ```shell
    $ kubectl get pods
    ```

    If your cluster is empty, you will see output along the following lines:

    ```
    No resources found.
    ```

    Of course, if you have other applications deployed, you should still see them, but not the guestbook.
