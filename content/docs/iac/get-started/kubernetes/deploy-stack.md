---
title_tag: Deploy the Stack | Kubernetes
meta_desc: Learn how to deploy your stack to a Kubernetes project in this guide.
title: Deploy to Kubernetes
h1: "Get started with Pulumi and Kubernetes"
weight: 5
menu:
    iac:
        name: Deploy
        identifier: kubernetes-get-started.deploy-stack
        parent: kubernetes-get-started
        weight: 5

aliases:
    - /docs/quickstart/kubernetes/deploy-stack/
---

## Deploy to Kubernetes

Now run `pulumi up` to start deploying your NGINX deployment:

{{% choosable "os" "macos,linux" %}}

```bash
$ pulumi up
```

{{% /choosable %}}
{{% choosable "os" "windows" %}}

```powershell
> pulumi up
```

{{% /choosable %}}

This command first shows you a **preview** of the changes that will be made:

```
Previewing update (dev):

     Type                              Name            Plan
 +   pulumi:pulumi:Stack               quickstart-dev  create
 +   └─ kubernetes:apps/v1:Deployment  nginx           create

Resources:
    + 2 to create

Do you want to perform this update?
> yes
  no
  details
```

No changes have been made yet. You may decline to proceed by selecting `no` or choose `details` to see more information about the proposed update like your deployment's properties.

### Performing the update

To proceed and deploy your NGINX deployment, select `yes`. This begins an **update**:

```
Do you want to perform this update? yes
Updating (dev):

     Type                              Name            Status
 +   pulumi:pulumi:Stack               quickstart-dev  created (3s)
 +   └─ kubernetes:apps/v1:Deployment  nginx           created (2s)

Outputs:
    name: "nginx-bec13562"

Resources:
    + 2 created

Duration: 4s
```

Updates can take some time since they wait for the Kubernetes resources to finish being created. The deployment will finish in just a few seconds.

{{< auto-naming-note resource="deployment" suffix="bec13562" >}}

{{% notes type="warning" %}}
If you get the error `configured Kubernetes cluster is unreachable` or
`unable to load schema information from the API server`, verify your cluster access:

1. Check your kubeconfig: `kubectl config view`
2. Test cluster connectivity: `kubectl cluster-info`
3. Verify authentication: `kubectl auth can-i get pods`

If these commands fail, return to the [Configure access](/docs/iac/get-started/kubernetes/configure/)
step to set up your Kubernetes cluster and kubectl.
{{% /notes %}}

### View your update on Pulumi Cloud

If you are logged into [Pulumi Cloud](/docs/pulumi-cloud), you'll see "View Live" hyperlinks in the CLI output during your update. These go to [a page](https://app.pulumi.com) with detailed information about your stack including resources, configuration, a full history of updates, and more. Navigate to it to review the details of your update:

<a href="/images/getting-started/console-update.png" target="_blank">
    <img src="/images/getting-started/console-update.png" alt="A stack update with console output, as shown in the Pulumi Service" />
</a>

Now that the NGINX deployment has been provisioned, you'll update it to do something more interesting.

{{< get-started-stepper >}}
