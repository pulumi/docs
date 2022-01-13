---
title: Azure Kubernetes Service (AKS) - Hello World!
meta_desc: How to launch a new Managed Kubernetes Cluster on Azure Kubernetes Service (AKS).
aliases: ["/docs/reference/tutorials/kubernetes/tutorial-aks/"]
layout: how-to-guide
---

In this tutorial, you'll use Python to deploy an instance of Azure Kubernetes Service (AKS). You can find a similar example in the [examples repo](https://github.com/pulumi/examples/tree/master/azure-py-aks).

{{< azure-aks-prereqs >}}

## Create a new AKS cluster {#new-aks-cluster}

1. In a new folder `aks-hello-world`, create an empty project with `pulumi new`.

    This will create a basic Pulumi program in Python and is great
    recommendation to begin your journey.

    ```bash
    $ mkdir aks-hello-world && cd aks-hello-world
    $ pulumi new azure-python
    ```

    * Enter in a Pulumi project name and description.
    * Enter in a name for the [Pulumi stack]({{< relref "/docs/intro/concepts/stack" >}}), which is an instance of our Pulumi program, and is used to distinguish amongst different development phases and environments of your work streams.
    * Enter in the Azure environment to use.
    * Follow the instructions presented to change directories to the newly created Pulumi project and install the dependencies.

1. In the root of your `aks-hello-world` project, add the following dependencies to `requirements.txt`:

    ```
    pulumi-azuread>=4.0.0,<5.0.0
    pulumi-kubernetes>=3.0.0,<4.0.0
    ```

1. Because `pulumi new` created a virtual environment to run your Pulumi program in, you must install these additional dependencies within that environment.

    ```bash
    $ venv/bin/pip install -r requirements.txt
    ```

1. Configure the Pulumi settings for the project:

    ```bash
    pulumi config set aks-hello-world:prefix <YOUR_prefix>
    pulumi config set --secret aks-hello-world:password <YOUR_NEW_CLUSTER_PRINCIPAL_PASSWORD>
    cat $HOME/.ssh/id_rsa.pub | pulumi config set aks-hello-world:sshkey
    pulumi config set aks-hello-world:location <YOUR_AZURE_LOCATION>
    ```

1. Open the existing file `__main__.py`, and replace the contents with the following:

    The `__main__.py` occupies the role as the *main* entrypoint in our Pulumi
    program. In it, you are going to declare:

	* The resources you want in Azure to provision the AKS cluster based on our
      cluster configuration settings,
	* The `kubeconfig` file to access the cluster, and
	* The initialization of a Pulumi Kubernetes provider with the
	`kubeconfig`, so that you can deploy Kubernetes resources to the cluster
    once its ready in the next steps.

    ```python
    import base64
    import pulumi
    from pulumi import ResourceOptions
    from pulumi_azure_native import resources, containerservice, network, authorization
    import pulumi_azuread as azuread
    from pulumi_kubernetes import Provider
    from pulumi_kubernetes.apps.v1 import Deployment
    from pulumi_kubernetes.core.v1 import Service, Namespace

    config = pulumi.Config("aks-hello-world")
    prefix = config.require("prefix")
    password = config.require("password")
    ssh_public_key = config.require("sshkey")
    location = config.get("location") or "east us"
    subscription_id = authorization.get_client_config().subscription_id

    # Create Azure AD Application for AKS
    app = azuread.Application(
        f"{prefix}-aks-app",
        display_name=f"{prefix}-aks-app"
    )

    # Create service principal for the application so AKS can act on behalf of the application
    sp = azuread.ServicePrincipal(
        "aks-sp",
        application_id=app.application_id
    )

    # Create the service principal password
    sppwd = azuread.ServicePrincipalPassword(
        "aks-sp-pwd",
        service_principal_id=sp.id,
        end_date="2099-01-01T00:00:00Z",
        value=password
    )

    rg = resources.ResourceGroup(
        f"{prefix}-rg",
        location=location
    )

    vnet = network.VirtualNetwork(
        f"{prefix}-vnet",
        location=rg.location,
        resource_group_name=rg.name,
        address_space={
            "address_prefixes": ["10.0.0.0/16"],
        }
    )

    subnet = network.Subnet(
        f"{prefix}-subnet",
        resource_group_name=rg.name,
        address_prefix="10.0.0.0/24",
        virtual_network_name=vnet.name
    )

    subnet_assignment = authorization.RoleAssignment(
        "subnet-permissions",
        principal_id=sp.id,
        principal_type=authorization.PrincipalType.SERVICE_PRINCIPAL,
        role_definition_id=f"/subscriptions/{subscription_id}/providers/Microsoft.Authorization/roleDefinitions/4d97b98b-1d4f-4787-a291-c67834d212e7", # ID for Network Contributor role
        scope=subnet.id
    )

    aks = containerservice.ManagedCluster(
        f"{prefix}-aks",
        location=rg.location,
        resource_group_name=rg.name,
        kubernetes_version="1.18.14",
        dns_prefix="dns",
        agent_pool_profiles=[{
            "name": "type1",
            "mode": "System",
            "count": 2,
            "vm_size": "Standard_B2ms",
            "os_type": containerservice.OSType.LINUX,
            "max_pods": 110,
            "vnet_subnet_id": subnet.id
        }],
        linux_profile={
            "admin_username": "azureuser",
            "ssh": {
                "public_keys": [{
                    "key_data": ssh_public_key
                }]
            }
        },
        service_principal_profile={
            "client_id": app.application_id,
            "secret": sppwd.value
        },
        enable_rbac=True,
        network_profile={
            "network_plugin": "azure",
            "service_cidr": "10.10.0.0/16",
            "dns_service_ip": "10.10.0.10",
            "docker_bridge_cidr": "172.17.0.1/16"
        }, opts=ResourceOptions(depends_on=[subnet_assignment])
    )

    kube_creds = pulumi.Output.all(rg.name, aks.name).apply(
        lambda args:
        containerservice.list_managed_cluster_user_credentials(
            resource_group_name=args[0],
            resource_name=args[1]))

    kube_config = kube_creds.kubeconfigs[0].value.apply(
        lambda enc: base64.b64decode(enc).decode())

    custom_provider = Provider(
        "inflation_provider", kubeconfig=kube_config
    )

    pulumi.export("kubeconfig", kube_config)
    ```

    This example uses the [@pulumi_azure_native]({{< relref "/registry/packages/azure-native" >}}) package to create and manage several Azure resources including a [ManagedCluster]({{< relref "/registry/packages/azure-native/api-docs/containerservice/managedcluster" >}}) resource, which defines your Kubernetes cluster, and a [VirtualNetwork]({{< relref "/registry/packages/azure-native/api-docs/network/virtualnetwork" >}}) resource that contains AKS worker nodes.

    In addition, this example uses implicit and explicit dependencies. For example, resource outputs can be used as inputs to imply dependency between resources, but resources like the subnet RoleAssignment are explicitly declared as dependencies using [ResourceOptions]({{< relref "/docs/intro/concepts/resources#options" >}}) and passed to the resource as additional arguments.

1. To preview and deploy changes, run `pulumi up` and select "yes."

    The `up` sub-command shows a preview of the resources that will be created
    and prompts on whether to proceed with the deployment. Note that the stack
    itself is counted as a resource, though it does not correspond
    to a physical cloud resource.

    You can also run `pulumi up --diff` to see and inspect the diffs of the
    overall changes expected to take place.

    Running `pulumi up` will deploy the AKS cluster. Note, provisioning a
    new AKS cluster can take several minutes.

    ```bash
    $ pulumi up
    Previewing update (dev):

        Type                                             Name                 Plan
    +   pulumi:pulumi:Stack                              aks-hello-world-dev  create
    +   ├─ azuread:index:Application                     my-aks-app           create
    +   ├─ azuread:index:ServicePrincipal                aks-sp               create
    +   ├─ azure-native:resources:ResourceGroup          my-rg                create
    +   ├─ azuread:index:ServicePrincipalPassword        aks-sp-pwd           create
    +   ├─ azure-native:network:VirtualNetwork           my-vnet              create
    +   ├─ azure-native:network:Subnet                   my-subnet            create
    +   ├─ azure-native:authorization:RoleAssignment     subnet-permissions   create
    +   ├─ azure-native:containerservice:ManagedCluster  my-aks               create
    +   └─ pulumi:providers:kubernetes                   inflation_provider   create

    Resources:
        + 10 to create
    ```

    {{% notes type="info" %}}
Due to an <a href="https://github.com/hashicorp/terraform-provider-azuread/issues/4" >issue</a> in the Azure AD Terraform Provider, the
creation of an Azure Service Principal, which is needed to create the Kubernetes cluster (see __main__.py), is delayed and may not
be available when the cluster is created. Because of this delay, if you get a Service Principal not found error, run `pulumi up`
again and it should successfully complete.
    {{% /notes %}}

## Access the Kubernetes Cluster using Pulumi Providers

Now that you have an instance of Kubernetes running, you may want to create API resources in Kubernetes to manage your workloads through Pulumi.

You can do this by configuring a Pulumi provider for your newly created cluster and instantiating a new Kubernetes resource object in your Pulumi program. The concept of a provider allows us to abstract away Kubernetes clusters in Pulumi that are independent of their underyling cloud provider, so that you can operate on and work with your Kubernetes clusters in a standard manner.

1. Create new Kubernetes Namespace, Deployment, and Service resources. This declares a new Kubernetes Namespace, Deployment, and Service to be
	created using the Pulumi Kubernetes provider.

    Open the existing file `__main__.py`, and append the following:

    ```python
    # Create a Kubernetes Namespace
    namespace = Namespace(f"{prefix}-k8s-namespace",
        metadata={},
        opts=ResourceOptions(provider=custom_provider)
    )

    # Create a NGINX Deployment
    appLabels = { "appClass": f"{prefix}" }
    deployment = Deployment(f"{prefix}-k8s-deployment",
        metadata={
            "labels": appLabels,
            "namespace": namespace.id
        },
        spec={
            "selector": {
                "match_labels": appLabels
            },
            "replicas": 1,
            "template": {
                "metadata": {
                    "labels": appLabels
                },
                "spec": {
                    "containers": [
                        {
                            "name": f"{prefix}-nginx",
                            "image": "nginx",
                            "ports": [
                                {
                                    "name": "http",
                                    "containerPort": 80
                                }
                            ]
                        }
                    ]
                }
            }
        },
        opts=ResourceOptions(provider=custom_provider)
    )

    # Create nginx service
    service = Service(f"{prefix}-nginx-service",
        metadata={
            "labels": appLabels,
            "namespace": namespace.id
        },
        spec={
            "ports": [
                {
                    "name": "http",
                    "port": 80
                }
            ],
            "selector": appLabels,
            "type": "LoadBalancer",
        },
        opts=ResourceOptions(provider=custom_provider)
    )

    pulumi.export('namespace_name', namespace.metadata.apply(lambda m: m.name))
    pulumi.export('deployment_name', deployment.metadata.apply(lambda m: m.name))
    pulumi.export('service_name', service.metadata.apply(lambda m: m.name))
    pulumi.export('service_public_endpoint', service.status.apply(lambda status: status.load_balancer.ingress[0].ip))
    ```

1. Run `pulumi up` again to deploy your new changes.

    ```bash
    $ pulumi up

        Type                              Name                 Plan
        pulumi:pulumi:Stack               aks-hello-world-dev
    +   ├─ kubernetes:core/v1:Namespace   my-k8s-namespace     create
    +   ├─ kubernetes:core/v1:Service     my-nginx-service     create
    +   └─ kubernetes:apps/v1:Deployment  my-k8s-deployment    create

    Outputs:
    + deployment_name        : "my-k8s-deployment-am0dnxwn"
    + namespace_name         : "my-k8s-namespace-aocurn1w"
    + service_name           : "my-nginx-service-sc1wmx95"
    + service_public_endpoint: output<string>

    Resources:
        + 3 to create
        10 unchanged
    ```

1. After the changes have been successfully deployed, access the NGINX welcome page using the IP address from the `service_public_endpoint` stack output.

    ```bash
    $ curl $(pulumi stack output service_public_endpoint)
    ```

    {{% notes type="info" %}}
Until the LoadBalancer is active, it may take a few minutes before you can retrieve the welcome page.
    {{% /notes %}}

## (Optional) Access the Kubernetes Cluster using `kubectl`

To access your new Kubernetes cluster using `kubectl`, you need to setup the
`kubeconfig` file. To do this, you can leverage the Pulumi stack output in the CLI, as Pulumi faciliates exporting these objects for you.

```bash
$ pulumi stack output kubeconfig > kubeconfig
$ export KUBECONFIG=`pwd`/kubeconfig
```

If you do not have `kubectl` installed, download a version of `kubectl` that matches the version you specified previously in `ManagedCluster`.

```bash
$ export KUBERNETES_VERSION=1.18.14 && sudo curl -Lo /usr/local/bin/kubectl "https://dl.k8s.io/release/v${KUBERNETES_VERSION}/bin/darwin/amd64/kubectl" && sudo chmod +x /usr/local/bin/kubectl
```

Verify that you successfully installed `kubectl` and use it to query your cluster for basic information.

```bash
$ kubectl version
$ kubectl cluster-info
$ kubectl get nodes
```

Once you have `kubectl` installed and configured, use the stack output to query the cluster for your newly created deployment:

```bash
$ kubectl get deployment $(pulumi stack output deployment_name) --namespace=$(pulumi stack output namespace_name)
$ kubectl get service $(pulumi stack output service_name) --namespace=$(pulumi stack output namespace_name)
```

You can also create another NGINX Deployment into your namespace using `kubectl` natively:

```bash
$ kubectl create deployment my-nginx --image=nginx --namespace=$(pulumi stack output namespace_name)
$ kubectl get pods --namespace=$(pulumi stack output namespace_name)
$ kubectl delete deployment my-nginx --namespace=$(pulumi stack output namespace_name)
```

When using `kubectl` directly to create additional deployments, Pulumi will not be aware of them to manage their state, but this simply
demonstrates that all the `kubectl` commands you're used to will work.

## Clean up

Before moving on, tear down the resources that are part of your stack.

1. Run `pulumi destroy` to tear down all resources.  You'll be prompted to make sure you really want to delete these resources. This takes some time; Pulumi waits for all the resources to be removed before it considers the destroy operation to be complete.

1. To delete the stack itself, run `pulumi stack rm`. Note that this command deletes all deployment history from the Pulumi Service.

## Summary

In this tutorial, you saw how to use Pulumi programs to create and manage cloud resources in Microsoft Azure, using Python and pypi packages. To preview and update infrastructure, use `pulumi up`. To clean up resources, run `pulumi destroy`.

For a follow-up example on how to use Pulumi programs to create a Kubernetes
apps on your new cluster, see [Kubernetes Tutorial: Getting Started With Pulumi]({{< relref "/registry/packages/kubernetes/how-to-guides/configmap-rollout" >}}).

We also encourage you to watch Joe Beda, co-founder of Kubernetes and Heptio,
take Pulumi for a spin in an episode of [TGIK8s](https://github.com/heptio/tgik).

<iframe width="560" height="315" src="https://www.youtube.com/embed/ILMK65YVSKw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
