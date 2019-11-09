--- title: Try Out the Cluster
menu:
  userguides:
    parent: crosswalk-kubernetes
    identifier: crosswalk-kubernetes-use-cluster
    weight: 3
---

{{< cloudchoose >}}

After the cluster is created with a Pulumi update, there will be
[outputs][pulumi-outputs] with fields like the cluster's `kubeconfig` file
contents, and its cluster name for reference.

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

The full code for this stack is on [GitHub][gh-repo-stack].

[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/aws/03-cluster-configuration
{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

The full code for this stack is on [GitHub][gh-repo-stack].

[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/azure/03-cluster-configuration
{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

The full code for this stack is on [GitHub][gh-repo-stack].

[gh-repo-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/gcp/03-cluster-configuration

{{% /md %}}
</div>

## Overview

We'll explore how to:

  * [Access the Cluster](#access-the-cluster)
  * [Query the Cluster](#query-the-cluster)
  * [Deploy a Workload](#deploy-a-workload)
  * [Learn More](#learn-more)

### Access the Cluster

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}
In EKS, the account caller will be placed into the
`system:masters` Kubernetes RBAC group by default. The `kubeconfig`
generated will cater to this primary cluster creator use-case, and it must be
copied, and reconfigured to use with other IAM roles the caller assumes, as
demonstrated in [Configure Access Control][crosswalk-configure-access].

#### As an Admin

##### Authentication

Authenticate as the `admins` role from the [Identity][aws-admin-identity-stack] stack.

```bash
$ aws sts assume-role --role-arn `pulumi stack output adminsIamRoleArn` --role-session-name k8s-admin
```

##### Kubeconfig Setup

To access your new Kubernetes cluster using `kubectl`, we need to setup the
`kubeconfig` file, and export the environment variable for `kubectl` usage
from the [Cluster Configuration][aws-cluster-config-stack] stack.

Setup the kubeconfig environment variable.

```bash
$ export KUBECONFIG=`pwd`/kubeconfig-admin.json
```

Get the Admins IAM Role ARN.

```bash
$ pulumi stack output adminsIamRoleArn
arn:aws:iam::000000000000:role/admins-eksClusterAdmin-0627674
```

Make a copy of the kubeconfig that will be edited for the `admins` to use the
`adminsIamRoleArn` output.

```bash
$ pulumi stack output kubeconfig > kubeconfig-admin.json
```

Edit `kubeconfig-admin.json` to use a role for authentication in the
`args` of the [`aws-iam-authenticator`][aws-iam-auth], e.g.

```bash
...
"users": [
  {
    "name": "aws",
    "user": {
      "exec": {
        "apiVersion": "client.authentication.k8s.io/v1alpha1",
        "args": [
          "token",
          "-i",
          "k8s-aws-cluster-eksCluster-1ef1afe",
          "-r",
          "arn:aws:iam::000000000000:role/admins-eksClusterAdmin-0627674"
        ],
        "command": "aws-iam-authenticator"
      }
    }
  }
]
```

#### As a Developer

##### Authentication

Authenticate as the `devs` role from the [Identity][aws-devs-identity-stack] stack.

```bash
$ aws sts assume-role --role-arn `pulumi stack output devsIamRoleArn` --role-session-name k8s-devs
```

##### Kubeconfig Setup

To access your new Kubernetes cluster using `kubectl`, we need to setup the
`kubeconfig` file, and export the environment variable for `kubectl` usage
from the [Cluster Configuration][aws-cluster-config-stack] stack.

Setup the kubeconfig environment variable.

```bash
$ export KUBECONFIG=`pwd`/kubeconfig-devs.json
```

Get the Devs IAM Role ARN.

```bash
$ pulumi stack output devsIamRoleArn
arn:aws:iam::000000000000:role/devs-eksClusterDeveloper-e332028
```

Make a copy of the kubeconfig that will be edited for the `devs` to use the
`devsIamRoleArn` output.

```bash
$ pulumi stack output kubeconfig > kubeconfig-devs.json
```

Edit `kubeconfig-devs.json` to use a role for authentication in the
`args` of the [`aws-iam-authenticator`][aws-iam-auth], e.g.

```bash
...
"users": [
  {
    "name": "aws",
    "user": {
      "exec": {
        "apiVersion": "client.authentication.k8s.io/v1alpha1",
        "args": [
          "token",
          "-i",
          "k8s-aws-cluster-eksCluster-1ef1afe",
          "-r",
          "arn:aws:iam::000000000000:role/devs-eksClusterDeveloper-e332028"
        ],
        "command": "aws-iam-authenticator"
      }
    }
  }
]
```

[aws-iam-auth]: https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html
[aws-admin-identity-stack]: {{< relref "/docs/guides/crosswalk/kubernetes/identity#create-an-iam-role-for-admins" >}}
[aws-devs-identity-stack]: {{< relref "/docs/guides/crosswalk/kubernetes/identity#create-an-iam-role-for-developers" >}}
[aws-cluster-config-stack]: https://github.com/pulumi/kubernetes-the-prod-way/tree/crosswalk/aws/03-cluster-configuration
[crosswalk-configure-access]: {{< relref "/docs/guides/crosswalk/kubernetes/configure-access-control" >}}
{{% /md %}}
</div>
<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}
In AKS, the account caller will be placed into the
`system:masters` Kubernetes RBAC group by default. Two `kubeconfig` files will
be generated that will cater to the admin and cluster user [use-cases][aks-cluster-roles].

To configure the cluster for use with IAM roles, check out
[Configure Access Control][crosswalk-configure-access].

#### Authentication

Authenticate as the ServicePrincipal from the [Identity][azure-identity-stack] stack.

```bash
$ az login --service-principal --username $ARM_CLIENT_ID --password $ARM_CLIENT_SECRET --tenant $ARM_TENANT_ID
```

#### Admin Kubeconfig Setup

To access your new Kubernetes cluster using `kubectl`, we need to setup the
`kubeconfig` file.

```bash
$ pulumi stack output kubeconfigAdmin > kubeconfig-admin.json
$ export KUBECONFIG=`pwd`/kubeconfig-admin.json
```

#### Developers Kubeconfig Setup

To access your new Kubernetes cluster using `kubectl`, we need to setup the
`kubeconfig` file.

```bash
$ pulumi stack output kubeconfig > kubeconfig-devs.json
$ export KUBECONFIG=`pwd`/kubeconfig-devs.json
```
[azure-identity-stack]: {{< relref "/docs/guides/crosswalk/kubernetes/identity#prerequisites" >}}
[aks-cluster-roles]: https://docs.microsoft.com/en-us/azure/aks/control-kubeconfig-access#available-cluster-roles-permissions
[crosswalk-configure-access]: {{< relref "/docs/guides/crosswalk/kubernetes/configure-access-control" >}}
{{% /md %}}
</div>
<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}
In GCP, the account caller will be placed into the
`system:masters` Kubernetes RBAC group by default. The `kubeconfig`
generated will cater to this primary cluster creator use-case.

GCP authentication will use tokens to operate as Members such as Users or ServiceAccounts,
and with certain permissions as detailed in [Configure Access Control][crosswalk-configure-access].

#### Admin Authentication

Authenticate as the `admins` ServiceAccount from the [Identity][gcp-admin-identity-stack] stack.

```bash
$ pulumi stack output adminsIamServiceAccountSecret > k8s-admin-sa-key.json
$ gcloud auth activate-service-account --key-file k8s-admin-sa-key.json
```

#### Developer Authentication

Authenticate as the `devs` ServiceAccount from the [Identity][gcp-devs-identity-stack] stack.

```bash
$ pulumi stack output devsIamServiceAccountSecret > k8s-devs-sa-key.json
$ gcloud auth activate-service-account --key-file k8s-devs-sa-key.json
```

#### Kubeconfig Setup

To access your new Kubernetes cluster using `kubectl`, we need to setup the
`kubeconfig` file, and export the environment variable for `kubectl` usage.

```bash
$ pulumi stack output --show-secrets kubeconfig > kubeconfig.json
$ export KUBECONFIG=`pwd`/kubeconfig.json
```

[gcp-admin-identity-stack]: {{< relref "/docs/guides/crosswalk/kubernetes/identity#create-an-iam-role-and-serviceaccount-for-admins" >}}
[gcp-devs-identity-stack]: {{< relref "/docs/guides/crosswalk/kubernetes/identity#create-an-iam-role-and-serviceaccount-for-developers" >}}
[crosswalk-configure-access]: {{< relref "/docs/guides/crosswalk/kubernetes/configure-access-control" >}}
{{% /md %}}
</div>

### Query the Cluster

Get cluster information.

```bash
$ kubectl version
$ kubectl cluster-info
```

Get the Nodes.

```bash
$ kubectl get nodes -o wide --show-labels
```

Get all Pods in the cluster, and show output attributes.

```bash
$ kubectl get pods --all-namespaces -o wide --show-labels
```

Get all Pods in the designated developer Namespace, and show output attributes.

```bash
$ kubectl get pods -n `pulumi stack output appsNamespaceName` -o wide --show-labels
```

Get the ConfigMaps of the `kube-system` Namespace.

```bash
$ kubectl get cm -n kube-system
```

### Deploy a Workload

{{< k8s-language nokx >}}

<div class="k8s-language-prologue-yaml"></div>
<div class="mt">
{{% md %}}
Imperatively deploy a NGINX Pod and public load-balanced service:

```bash
$ kubectl run --generator=run-pod/v1 nginx --image=nginx --port=80 --expose --service-overrides='{"spec":{"type":"LoadBalancer"}}'
```

After a few moments, visit the load balancer URL.

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}

```bash
$ if ING_LB=$((kubectl get svc nginx -o template --template='{{(index .status.loadBalancer.ingress 0).hostname}}') 2>&1) ; then echo "http://$ING_LB"; else echo "LB is not ready yet."; fi
```

{{% /md %}}
</div>

<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}

```bash
$ if ING_LB=$((kubectl get svc nginx -o template --template='{{(index .status.loadBalancer.ingress 0).ip}}') 2>&1) ; then echo "http://$ING_LB"; else echo "LB is not ready yet."; fi
```

{{% /md %}}
</div>

<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}

```bash
$ if ING_LB=$((kubectl get svc nginx -o template --template='{{(index .status.loadBalancer.ingress 0).ip}}') 2>&1) ; then echo "http://$ING_LB"; else echo "LB is not ready yet."; fi
```

{{% /md %}}
</div>

Delete the pod and service.

```bash
$ kubectl delete pod/nginx svc/nginx
```
{{% /md %}}
</div>

<div class="k8s-language-prologue-typescript"></div>
<div class="mt">
{{% md %}}
Declaratively deploy a NGINX Pod and public load-balanced service:

```ts
import * as k8s from "@pulumi/kubernetes";

// Expose a k8s provider instance of the cluster.
const provider = new k8s.Provider("provider", {kubeconfig: kubeconfig });

// Create a NGINX Pod
const nginx = new k8s.core.v1.Pod(name,
    {
        metadata: {labels: {app: "nginx"}},
        spec: {
            containers: [
                {
                    name: name,
                    image: "nginx:latest",
                    ports: [{ name: "http", containerPort: 80 }]
                }
            ],
        }
    }, {provider: provider}
);

// Create a LoadBalancer Service for the NGINX Deployment
const service = new k8s.core.v1.Service(name,
    {
        metadata: {labels: {app: "nginx"}},
        spec: {
            type: "LoadBalancer",
            ports: [{ port: 80, targetPort: "http" }],
            selector: {app: "nginx"},
        },
    }, {provider: provider}
);
```

<div class="cloud-prologue-aws"></div>
<div class="mt">
{{% md %}}
```ts
// Export the Service name and public LoadBalancer Endpoint
export const serviceName = service.metadata.name;
export const serviceHostname = service.status.loadBalancer.ingress[0].hostname;
```

After a few moments, visit the load balancer listed in the `serviceHostname`.

```bash
$ curl `pulumi stack output serviceHostname`
```

{{% /md %}}
</div>
<div class="cloud-prologue-azure"></div>
<div class="mt">
{{% md %}}
```ts
// Export the Service name and public LoadBalancer Endpoint
export const serviceName = service.metadata.name;
export const serviceIp = service.status.loadBalancer.ingress[0].ip;
```

After a few moments, visit the load balancer listed in the `serviceIp`.

```bash
$ curl `pulumi stack output serviceIp`
```

{{% /md %}}
</div>
<div class="cloud-prologue-gcp"></div>
<div class="mt">
{{% md %}}
```ts
// Export the Service name and public LoadBalancer Endpoint
export const serviceName = service.metadata.name;
export const serviceIp = service.status.loadBalancer.ingress[0].ip;
```

After a few moments, visit the load balancer listed in the `serviceIp`.

```bash
$ curl `pulumi stack output serviceIp`
```

{{% /md %}}
</div>
To tear down NGINX, delete its definition in the Pulumi program and run a Pulumi update.
{{% /md %}}
</div>

### Learn More

See the official [Kubernetes Basics][k8s-basics] tutorial for more details.

[pulumi-outputs]: https://www.pulumi.com/docs/intro/concepts/programming-model/#outputs
[k8s-basics]: https://kubernetes.io/docs/tutorials/kubernetes-basics/
