---
title: "#4: Graceful App Rollout"
menu:
  reference:
    parent: tutorials-kubernetes
---

This tutorial shows you how to use Pulumi to write and manage a Kubernetes application through it's
lifecycle. We will use the Pulumi Kubernetes [TypeScript][ts] SDK to write the Kubernetes
applications, and the Pulumi CLI to create, update, and destroy resources on the Kubernetes cluster.

Along the way, we will get a taste for several of Pulumi's features for visualizing and
understanding how an update will impact the application running in the cluster.

For example, in the gif below, we can see how updating one resource (in this case, a `ConfigMap`) "ripples through" the rest of the application, causing other resources to be updated, as well.

**Topics:**

-   [Prerequisites](#prerequisites)
-   [Provisioning a Kubernetes application](#provisioning-a-Kubernetes-application)
-   [Using Pulumi's notion of "stack outputs"](#using-pulumis-notion-of-stack-outputs)
-   [Using Pulumi's diff facilities to understand how a change affects an application](#using-pulumis-diff-facilities-to-understand-how-a-change-affects-an-application)
-   [Updating an application](#updating-an-application)
-   [Deleting resources safely](#deleting-resources-safely)

![configmapRollout](/images/docs/quickstart/kubernetes/cm-rollout.gif "ConfigMap-induced Rollout")

## Prerequisites

> **IMPORTANT:** This tutorial expects that you have provisioned a Kubernetes cluster and have an
> active kubeconfig file. If you don't, please follow instructions [here]({{< relref "/docs/reference/clouds/kubernetes" >}}).

1.  Install [Node.js][nodejs] version 8 or later.
1.  Install a package manager for Node.js, such as [npm] or [Yarn].
1.  Follow the directions [here][install] to install the Pulumi CLI.

## Provisioning a Kubernetes application

We're going to provision one of Pulumi's [example applications][pulumi-test]. We'll dig into the
code when we modify it later.

This application will:

-   Create a container running [nginx](https://nginx.org/) (an open source web server).
-   Create a `ConfigMap` with an configuration file that configures nginx to proxy traffic to
    `pulumi.github.io`.
-   Mount that configuration data into the nginx container.
-   Expose the nginx container to the internet using a `Service`.

To provision the application, we need to:

1. **Run** `pulumi new`**.**

    ```sh
    $ mkdir test-pulumi && cd test-pulumi
    # Clones the application into the current directory, and begins provisioning it in the active
    # context of your kubeconfig file.
    $ pulumi new https://github.com/pulumi/examples/tree/master/kubernetes-ts-configmap-rollout
    ```

1. **Answer the questions prompted by** `pulumi new`**.** This will bring up a CLI prompt that looks
   like the following, asking you questions to get you started. It is ok to accept default values
   for all questions except `isMinikube`, where it is important to answer `false`.

    > **IMPORTANT:** If you are using minikube, Docker for Mac, or any other compute provider that
    > can't allocate a load balancer, you can answer `true`, but you won't be able to bring up the
    > service in your browser without using something like `kubectl port-forward`.

    ![Pulumi CLI questions](/images/docs/quickstart/kubernetes/questions.png "Pulumi CLI questions prompt")

1. **Accept the update.** After all the questions are answered, you should see a prompt like the
   following, asking if you'd like to proceed with the update. You can opt to view the diff, if you like, but we'll also do this later when we update the application.

    ```
    Resources:
        + 4 to create

    Do you want to perform this update?
      yes
    > no
      details
    ```

Once all this is complete, Pulumi will begin provisioning the application. It should look something
like the following gif, though it will be slightly different, depending on the name you've given
your stack.

There are several things to notice here:

-   **Resources are provisioned in a specific order.** We can see from the output that the
    `ConfigMap` is provisioned first, the `Deployment` second, and the `Service` third.

    As we will see in the following sections, Pulumi keeps track of resources as a _graph_. We will
    also see that this allows Pulumi to tell us how a change to one resource will affect other
    resources.

-   **We get intermediate status updates as resources provision.** As the `Service` rolls out, for
    example, we can see distinct stages in the initialization.

These two things will be important in the next sections.

![Allocating a public IP to a Deployment](/images/docs/quickstart/kubernetes/exposed-deploy.gif "Allocating a public IP to a Deployment")

## Using Pulumi's notion of "stack outputs"

It's worth noting briefly that Pulumi provides convenient tooling for "exporting" values of
initialized resources.

This application exports `frontendIp`, which is the IP address of the load balancer that the
underlying compute provider provisioned when you started the service. You can view it with the following command:

```sh
$ pulumi stack output frontendIp
35.247.60.31
```

If you paste this IP into your browser, you should see that it's redirected you to the [Pulumi
homepage](http://www.pulumi.com). Alternatively, you can run this:

```sh
$ curl -sL $(pulumi stack output frontendIp):80 | grep -C 1 "<title>"

    <title>Pulumi. Serverless // Containers // Infrastructure // Cloud // DevOps</title>
```

## Using Pulumi's diff facilities to understand how a change affects an application

In this section, we'll re-configure nginx to point at google.com by changing the data in the
`ConfigMap`.

This is one of the "gotchas" of Kubernetes -- by default `kubectl` will not trigger a rollout among
the containers that reference a `ConfigMap` when its data will change. Instead, the kubelet silently, transparently syncs the data to the containers after the TTL expires.

In this section, we will see that Pulumi plans a _safe_ update of the `ConfigMap`. It will:

1. Create a new `ConfigMap` with a new name and the new data.
1. Update the `PodTemplate` of the `Deployment` to point at the new `ConfigMap`. This update
   triggers the `Deployment` controller to try to roll out a new set of containers with mounts
   that contain this new data.
1. Only once that succeeds, delete the old `ConfigMap`.

Here are the steps to make this change:

1. **Find the configuration data we need to change.** In [index.ts] we can see the definition of the
   `ConfigMap`:

    ```typescript
    // nginx Configuration data to proxy traffic to `pulumi.github.io`. Read from
    // `default.conf` file.
    const nginxConfig = new k8s.core.v1.ConfigMap(appName, {
        metadata: { labels: appLabels },
        data: { "default.conf": fs.readFileSync("default.conf").toString() },
    });
    ```

    This indicates that the `ConfigMap` is reading the `default.conf` file using `fs.readFileSync`.

1. **Change the configuration file.** If you're on macOS, you can run:

    ```sh
    $ sed -i bak "s/pulumi.github.io/google.com/g" default.conf
    ```

    If you're running a platform that does not support `sed`, paste the following into your
    `default.conf` file:

    ```conf
    upstream node {
      server google.com;
    }
    server {
      listen                  80;
      server_name             _;
      root                    /usr/share/nginx/html;
      location / {
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header Host google.com;
        proxy_pass http://node;
        proxy_redirect off;
        port_in_redirect off;
      }
    }
    ```

1. **Get a high-level view of the changes with** `pulumi preview`**.** It should look something like
   the picture below. As we mentioned before, we can see that Pulumi plans to explicitly trigger a
   rollout in the `Deployment` by replacing the `ConfigMap`. This is in contrast to `kubectl`, which
   will silently sync the new version of the file to the containers.

    ![Preview](/images/docs/quickstart/kubernetes/preview.png "Preview")

1. **Get a more detailed view of the changes with** `pulumi preview --diff`**.**. It will look
   conceptually something like the following gif (though this gif is a different app).

    ![diff](/images/docs/quickstart/kubernetes/diff.gif "Diff")

## Updating an application

Once we're confident this is what we want, we can run the update:

1. **Run** `pulumi up`**.**

    ```sh
    $ pulumi up
    ```

    The output should look something like this.

    ![configmapRollout](/images/docs/quickstart/kubernetes/cm-rollout.gif)

2. **Verify the rollout worked.** You can do this by pasting the URL into the browser (be sure to
   disable the cache), or by running the following:
    ```sh
    $ curl -sL $(pulumi stack output frontendIp) | grep -o "<title>Google</title>"
    <title>Google</title>
    ```

## Destroying an application

Once we're done with the application, it's possible to destroy it using:

```sh
$ pulumi destroy
```

[ts]: https://www.typescriptlang.org/
[nodejs]: https://nodejs.org/en/
[npm]: https://www.npmjs.com/get-npm
[yarn]: https://yarnpkg.com/en/docs/install
[install]: {{< relref "/docs/reference/install.md" >}}
[pulumi-test]: https://github.com/pulumi/examples/tree/master/kubernetes-ts-configmap-rollout
[index.ts]: https://github.com/pulumi/examples/blob/master/kubernetes-ts-configmap-rollout/index.ts
