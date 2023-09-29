---
title_tag: Deploy the Changes | Kubernetes
meta_desc: This page provides an overview of how deploy changes to a Kubernetes project.
title: Deploy changes
h1: "Pulumi & Kubernetes: Deploy changes"
weight: 7
menu:
  clouds:
    parent: kubernetes-get-started
    identifier: kubernetes-deploy-changes

aliases:
- /docs/quickstart/kubernetes/deploy-changes/
- /docs/get-started/kubernetes/deploy-changes/
---

Deploy the stack changes.

```bash
$ pulumi up
```

Pulumi computes the minimally disruptive change to achieve the desired state described by the program.

```bash
Previewing update (dev)

     Type                              Name            Plan
     pulumi:pulumi:Stack               quickstart-dev
 +   ├─ kubernetes:apps/v1:Deployment  nginx           create
 +   ├─ kubernetes:core/v1:Service     nginx           create
 -   └─ kubernetes:apps/v1:Deployment  app-dep         delete


Outputs:
  + ip  : "10.96.0.0"
  - name: "app-dep-b7413dae"

Resources:
    + 2 to create
    - 1 to delete
    3 changes. 1 unchanged

Do you want to perform this update?  [Use arrows to move, type to filter]
  yes
> no
  details
```

Select `yes` using the arrows and hit enter to update the resources in Kubernetes.

Pulumi will create the service since it is now defined in the program.

```bash
Do you want to perform this update? yes
Updating (dev)

     Type                              Name            Status
     pulumi:pulumi:Stack               quickstart-dev
 +   ├─ kubernetes:apps/v1:Deployment  nginx           created (3s)
 +   ├─ kubernetes:core/v1:Service     nginx           created (10s)
 -   └─ kubernetes:apps/v1:Deployment  app-dep         deleted (1s)


Outputs:
  + ip  : "10.103.199.118"
  - name: "app-dep-b7413dae"

Resources:
    + 2 created
    - 1 deleted
    3 changes. 1 unchanged

Duration: 23s
```

View the `ip` [stack output](/docs/concepts/stack#outputs) from the nginx service.

```bash
$ pulumi stack output ip
```

> **If using Minikube:** Minikube does not support type `LoadBalancer`. Instead, forward the nginx service:
>
>  ```bash
>  $ kubectl get service
>  NAME             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
>  kubernetes       ClusterIP   10.96.0.1        <none>        443/TCP   44h
>  nginx-9e5d5cd4   ClusterIP   10.103.199.118   <none>        80/TCP    6m47s
>  ```
>
> Note: The assigned name for this particular nginx service is `nginx-9e5d5cd4`. In a new terminal window, run:
>
> ```bash
>  $ kubectl port-forward service/nginx-9e5d5cd4 8080:80
>  Forwarding from 127.0.0.1:8080 -> 80
>  Forwarding from [::1]:8080 -> 80
> ```

Curl nginx to verify it is running.

```bash
$ $(pulumi config get isMinikube) && curl "http://localhost:8080" || curl $(pulumi stack output ip)
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

Next, we'll destroy the stack.

{{< get-started-stepper >}}
