---
title_tag: Deploy the Changes | Kubernetes
meta_desc: This page provides an overview of how deploy changes to a Kubernetes project.
title: Deploy changes
h1: "Pulumi & Kubernetes: Deploy changes"
block_external_search_index: true
---

Now let's deploy our changes.

```bash
$ pulumi up
```

Pulumi computes the minimally disruptive change to achieve the desired state described by the program.

```
Previewing update (dev):

     Type                        Name            Plan
     pulumi:pulumi:Stack         quickstart-dev
 +   └─ kubernetes:core:Service  nginx           create

 Outputs:
  + ip  : output<string>
  - name: "nginx-xw231xdt"

Resources:
    + 1 to create
    2 unchanged

Do you want to perform this update?
  yes
> no
  details
```

Pulumi will create the service since it is now defined in the program.

```
Do you want to perform this update? yes
Updating (dev):

     Type                        Name            Status
     pulumi:pulumi:Stack         quickstart-dev
 +   └─ kubernetes:core:Service  nginx           created

Outputs:
  + ip  : "10.100.249.54"
  - name: "nginx-xw231xdt"

Resources:
    + 1 created
    2 unchanged

Duration: 12s
```

You can see we now have an `ip` [stack output](/docs/concepts/stack#outputs) that we can `curl` to get the output from the service.

> **Using Minikube:** Note that Minikube does not support type `LoadBalancer`. If you are deploying to Minikube, see the following example to run the `kubectl port-forward service/YOUR_SERVICE_NAME 8080:80` command to forward the cluster port to the local machine. Then, the service can be accessed via `curl http://localhost:8080`, which will get the same result as `curl $(pulumi stack output ip)` as in the environment without using Minikube.
>
>
>  ```bash
>  $ kubectl get service
>  NAME             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
>  kubernetes       ClusterIP   10.96.0.1       <none>        443/TCP   26h
>  nginx-3hq3kux6   ClusterIP   10.96.185.206   <none>        80/TCP    15m
>  ```
>
> ```bash
> $ kubectl port-forward service/nginx-3hq3kux6 8080:80
> Forwarding from 127.0.0.1:8080 -> 80
> Forwarding from [::1]:8080 -> 80
> ```

```bash
$ curl $(pulumi stack output ip)
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

Next, we'll destroy the stack.

<div class="mt-6">
    <a data-track="previous-step" class="btn btn-secondary" href="/docs/clouds/kubernetes/get-started/modify-program-b/">&larr; Previous Step</a>
    <a data-track="next-step" class="btn" href="/docs/clouds/kubernetes/get-started/destroy-stack-b/">Destroy Stack &rarr;</a>
</div>
