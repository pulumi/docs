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
**If using Minikube:** You have two options to access your service:

### Option 1: Use `minikube tunnel` (recommended)

Minikube can provide LoadBalancer support via the `minikube tunnel` command. In a separate terminal, run:

```bash
$ minikube tunnel
```

This assigns an external IP to LoadBalancer services. With the tunnel running, you can set `isMinikube` to `false` and access your service via the external IP. Note that `minikube tunnel` may require administrator/sudo privileges.

### Option 2: Use port forwarding

Alternatively, set `isMinikube` to `true` and use port forwarding:

```bash
$ kubectl get service
NAME             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
kubernetes       ClusterIP   10.96.0.1        <none>        443/TCP   44h
nginx-9e5d5cd4   ClusterIP   10.103.199.118   <none>        80/TCP    6m47s
```

The assigned name for this particular nginx service is `nginx-9e5d5cd4`; yours will be different. In a new terminal window, run:

```bash
$ kubectl port-forward service/nginx-9e5d5cd4 8080:80
Forwarding from 127.0.0.1:8080 -> 80
Forwarding from [::1]:8080 -> 80
```

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
