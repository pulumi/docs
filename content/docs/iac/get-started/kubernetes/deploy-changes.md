---
title_tag: Deploy the Changes | Kubernetes
title: Deploy the changes
h1: "Deploy the changes"
meta_desc: Learn how to deploy changes to a Kubernetes + Pulumi project in this guide.
weight: 8
menu:
    iac:
        name: Deploy the changes
        identifier: kubernetes-get-started.deploy-changes
        parent: kubernetes-get-started
        weight: 8
aliases:
    - /docs/get-started/kubernetes/deploy-changes/
    - /docs/quickstart/kubernetes/deploy-changes/
    - /docs/clouds/kubernetes/get-started/deploy-changes/
---

Now deploy the changes with `pulumi up`. Pulumi computes the minimal set of changes needed to reach your program's new desired state, leaving unchanged resources as-is:

```bash
$ pulumi up
```

As before, you'll see a preview of the changes to be made:

```
Previewing update (dev):

     Type                           Name            Plan
     pulumi:pulumi:Stack            quickstart-dev
 +   └─ kubernetes:core/v1:Service  nginx           create

Outputs:
  + ip  : "10.96.0.0"
  - name: "nginx-bec13562"

Resources:
    + 1 to create
    2 unchanged

Do you want to perform this update?
> yes
  no
  details
```

Choose `yes` to proceed with the update. Pulumi creates the new service and prints the `ip` [stack output](/docs/iac/concepts/stacks/#outputs), which you can also retrieve directly:

```bash
$ pulumi stack output ip
```

{{% notes type="info" %}}
If you're using Minikube, a `LoadBalancer` service won't receive an external IP on its own. You have two options:

- Run `minikube tunnel` in a separate terminal (it may require sudo), then set `isMinikube` to `false` and reach the service at its external IP.
- Set `isMinikube` to `true` and forward a local port to the service instead. Find its name with `kubectl get service`, then run `kubectl port-forward service/<name> 8080:80` and reach it at `http://localhost:8080`.
{{% /notes %}}

Once the service is reachable, `curl` it to verify NGINX is running:

```bash
$ curl $(pulumi stack output ip)
```

```html
<!DOCTYPE html>
<html>
<head><title>Welcome to nginx!</title></head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and working.</p>
</body>
</html>
```

Next you'll finish up by destroying the resources you created.

{{< get-started-stepper >}}
