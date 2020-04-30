---
title: Azure Kubernetes Service (AKS) - Hello World!
meta_desc: How to launch a new Managed Kubernetes Cluster on Azure Kubernetes Service (AKS).
aliases: ["/docs/reference/tutorials/kubernetes/tutorial-aks/"]
---

In this tutorial, we'll use Python to deploy an instance of Azure Kubernetes Service (AKS). You can find this code on the in the [examples repo](https://github.com/pulumi/examples/tree/master/azure-py-aks).

{{< azure-aks-prereqs >}}

## Create a new AKS cluster {#new-aks-cluster}

1. In a new folder `aks-hello-world`, create an empty project with `pulumi new`.

    This will create a base Pulumi program in Python, and is great
    recommendation to begin your journey.

    ```bash
    $ mkdir aks-hello-world && cd aks-hello-world
    $ pulumi new azure-python
    ```

    * Enter in a Pulumi project name, and description to detail what this
      Pulumi program does
    * Enter in a name for the [Pulumi stack]({{< prelref "/docs/intro/concepts/stack" >}}), which is an instance of our Pulumi program, and is used to distinguish amongst different development phases and environments of your work streams.
    * Enter in the Azure environment to use.
    * Follow the instructions presented to change directories to the newly created Pulumi project and install the dependencies.

1. Add the required dependencies:

    This installs the dependent packages [needed]({{< prelref "/docs/intro/concepts/how-pulumi-works" >}}) for our Pulumi program.

	```bash
	$ pip install pulumi pulumi_azure pulumi_kubernetes
	```

1. Configure the Pulumi settings for the project:

	```bash
    pulumi config set azure-py-aks:prefix <YOUR_PREFIX>
    pulumi config set --secret azure-py-aks:password <YOUR_NEW_CLUSTER_PRINCIPAL_PASSWORD>
    cat $HOME/.ssh/id_rsa.pub | pulumi config set azure-py-aks:sshkey
    pulumi config set azure-py-aks:location <YOUR_AZURE_LOCATION>
	```

1. Open the existing file `__main__.py`, and replace the contents with the following:

    The `__main__.py` occupies the role as the *main* entrypoint in our Pulumi
    program. In it, we are going to declare:

	* The resources we want in Azure to provision the AKS cluster based on our
      cluster configuration settings,
	* The `kubeconfig` file to access the cluster, and
	* The initialization of a Pulumi Kubernetes provider with the
	`kubeconfig`, so that we can deploy Kubernetes resources to the cluster
    once its ready in the next steps.

    ```python
    import pulumi
    from pulumi import ResourceOptions
    from pulumi_azure.core import ResourceGroup
    from pulumi_azure.role import Assignment
    from pulumi_azure.ad import Application, ServicePrincipal, ServicePrincipalPassword
    from pulumi_azure.containerservice import KubernetesCluster, Registry
    from pulumi_azure.network import VirtualNetwork, Subnet
    from pulumi_kubernetes import Provider
    from pulumi_kubernetes.apps.v1 import Deployment
    from pulumi_kubernetes.core.v1 import Service
    from pulumi_kubernetes.core.v1 import Namespace

    config = pulumi.Config('azure-py-aks')
    PREFIX = config.require('prefix')
    PASSWORD = config.require('password')
    SSHKEY = config.require('sshkey')
    LOCATION = config.get('location') or 'east us'

    # create Azure AD Application for AKS
    app = Application(
        'aks-app',
        name=PREFIX + 'aks-app'
    )

    # create service principal for the application so AKS can act on behalf of the application
    sp = ServicePrincipal(
        'aks-sp',
        application_id=app.application_id
    )

    # create service principal password
    sppwd = ServicePrincipalPassword(
        'aks-sp-pwd',
        service_principal_id=sp.id,
        end_date='2025-01-01T01:02:03Z',
        value=PASSWORD
    )

    rg = ResourceGroup(
        'rg',
        name=PREFIX + 'rg',
        location=LOCATION
    )

    vnet = VirtualNetwork(
        'vnet',
        name=PREFIX + 'vnet',
        location=rg.location,
        resource_group_name=rg.name,
        address_spaces=['10.0.0.0/16']
    )

    subnet = Subnet(
        'subnet',
        name=PREFIX + 'subnet',
        resource_group_name=rg.name,
        address_prefix='10.0.0.0/24',
        virtual_network_name=vnet.name
    )

    # create Azure Container Registry to store images in
    acr = Registry(
        'acr',
        name=PREFIX + 'acr',
        location=rg.location,
        resource_group_name=rg.name,
        sku="basic"
    )

    # assignments are needed for AKS to be able to interact with those resources
    acr_assignment = Assignment(
        'acr-permissions',
        principal_id=sp.id,
        role_definition_name='AcrPull',
        scope=acr.id
    )

    subnet_assignment = Assignment(
        'subnet-permissions',
        principal_id=sp.id,
        role_definition_name='Network Contributor',
        scope=subnet.id
    )

    aks = KubernetesCluster(
        'aks',
        name=PREFIX + 'aks',
        location=rg.location,
        resource_group_name=rg.name,
        kubernetes_version="1.13.5",
        dns_prefix="dns",
        agent_pool_profile=(
            {
                "name": "type1",
                "count": 2,
                "vmSize": "Standard_B2ms",
                "osType": "Linux",
                "maxPods": 110,
                "vnet_subnet_id": subnet.id
            }
        ),
        linux_profile=(
            {
                "adminUsername": "azureuser",
                "ssh_key": {
                    "keyData": SSHKEY
                }
            }
        ),
        service_principal={
            "clientId": app.application_id,
            "clientSecret": sppwd.value
        },
        role_based_access_control={
            "enabled": "true"
        },
        network_profile=(
            {
                "networkPlugin": "azure",
                "serviceCidr": "10.10.0.0/16",
                "dns_service_ip": "10.10.0.10",
                "dockerBridgeCidr": "172.17.0.1/16"
            }
        ), __opts__=ResourceOptions(depends_on=[acr_assignment, subnet_assignment])
    )

    custom_provider = Provider(
        "inflation_provider", kubeconfig=aks.kube_config_raw
    )

    pulumi.export('kubeconfig', aks.kube_config_raw)
    ```

    This example uses the [@pulumi_azure]({{< prelref "/docs/reference/pkg/python/pulumi_azure" >}}) package to create and manage several Azure resources including: a [KubernetesCluster]({{< prelref "/docs/reference/pkg/python/pulumi_azure/containerservice#pulumi_azure.containerservice.KubernetesCluster" >}}), [Registry]({{< prelref "/docs/reference/pkg/python/pulumi_azure/containerservice#pulumi_azure.containerservice.Registry" >}}) which will store Docker images and [VirtualNetwork]({{< prelref "/docs/reference/pkg/python/pulumi_azure/network#pulumi_azure.network.VirtualNetwork" >}}) that will contain AKS worker nodes and several others. We are using implicit and explicit dependencies in this configuration. For example, resource outputs can be used as inputs to imply dependency between resources, but you can also declare dependency using [ResourceOptions]({{< prelref "/docs/intro/concepts/programming-model#resources" >}}) passed to the resource as additional arguments.

1. To preview and deploy changes, run `pulumi up` and select "yes."

    The `up` sub-command shows a preview of the resources that will be created
    and prompts on whether to proceed with the deployment. Note that the stack
    itself is counted as a resource, though it does not correspond
    to a physical cloud resource.

    You can also run `pulumi up --diff` to see and inspect the diffs of the
    overall changes expected to take place.

    Running `pulumi up` will deploy the AKS cluster. Note, provisioning a
    new AKS cluster takes between 10-15 minutes.

        $ pulumi up
        Previewing update (dev):

            Type                                         Name                Plan       Info
        +   pulumi:pulumi:Stack                          aks-dev             create
        +   ├─ azure:core:ResourceGroup                  rg                  create
        +   ├─ azure:ad:Application                      aks-app             create
        +   ├─ azure:network:VirtualNetwork              vnet                create
        +   ├─ azure:containerservice:Registry           acr                 create
        +   ├─ azure:ad:ServicePrincipal                 aks-sp              create
        +   ├─ azure:network:Subnet                      subnet              create
        +   ├─ azure:ad:ServicePrincipalPassword         aks-sp-pwd          create
        +   ├─ azure:role:Assignment                     acr-permissions     create
        +   ├─ azure:containerservice:KubernetesCluster  aks                 create
        +   └─ azure:role:Assignment                     subnet-permissions  create

        Resources:
            + 11 to create

## Access the Kubernetes Cluster using Pulumi Providers

Now that we have an instance of Kubernetes running, we may want to create API resources in Kubernetes to manage our workloads through Pulumi.

We can do this by configuring a Pulumi provider for our newly created cluster, and instantiating a new Kubernetes resource object in our Pulumi program. The concept of a provider allows us to abstract away Kubernetes clusters in Pulumi that are indendent of their underyling cloud provider, so that you can operate on and work with your Kubernetes clusters in a standard manner.

1. Add the `pulumi/kubernetes` dependency to `requirements.txt` and install it:

    ```bash
    echo "pulumi_kubernetes>=v0.22.2" >> requirements.txt
    pip install -r requirements.txt
    ```

1. Create a new Kubernetes Namespace and Deployment:

	This declares a new Kubernetes Namespace, Deployment and Service to be
	created using the Pulumi Kubernetes provider to our cluster.

    Open the existing file `__main__.py`, and append the following:

    ```python
    name = 'replaceme'

    # Create a Kubernetes Namespace
    namespace = Namespace(name,
        metadata={},
        __opts__=ResourceOptions(provider=custom_provider)
    )

    # Create a NGINX Deployment
    appLabels = { "appClass": name }
    deployment = Deployment(name,
                metadata={
                    "labels": appLabels
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
                                    "name": name,
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
                __opts__=ResourceOptions(provider=custom_provider)
                )

    # Create nginx service
    service = Service(name,
        metadata={
            "labels": appLabels
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
        __opts__=ResourceOptions(provider=custom_provider)
    )

    pulumi.export('namespace_name', namespace.metadata.apply(lambda resource: resource['name']))
    pulumi.export('deployment_name', deployment.metadata.apply(lambda resource: resource['name']))
    pulumi.export('service_name', service.metadata.apply(lambda resource: resource['name']))
    pulumi.export('service_public_endpoint', service.status.apply(lambda status: status['load_balancer']['ingress'][0]['ip']))
    ```

    If you visit the ip address listed in `service_public_endpoint` you should land on the NGINX welcome page. Note, that it may take a minute or so for the LoadBalancer to become active on Azure.

## Access the Kubernetes Cluster using `kubectl`

To access your new Kubernetes cluster using `kubectl`, we need to setup the
`kubeconfig` file and download `kubectl`. We can leverage the Pulumi stack
output in the CLI, as Pulumi faciliates exporting these objects for us.

```bash
$ pulumi stack output kubeconfig > kubeconfig
$ export KUBECONFIG=`pwd`/kubeconfig
$ export KUBERNETES_VERSION=1.11.5 && sudo curl -s -o /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v${KUBERNETES_VERSION}/bin/linux/amd64/kubectl && sudo chmod +x /usr/local/bin/kubectl

$ kubectl version
$ kubectl cluster-info
$ kubectl get nodes
```

We can also use the stack output to query the cluster for our newly created Deployment:

```bash
$ kubectl get deployment $(pulumi stack output deploymentName) --namespace=$(pulumi stack output namespaceName)
$ kubectl get service $(pulumi stack output serviceName) --namespace=$(pulumi stack output namespaceName)
```

We can also create another NGINX Deployment into the `default` namespace using
`kubectl` natively:

```bash
$ kubectl create deployment my-nginx --image=nginx
$ kubectl get pods
$ kubectl delete deployment my-nginx
```

Of course, by doing so, resources are outside of Pulumi's purview, but this simply
demonstrates that all the `kubectl` commands you're used to will work.

## Clean up

Before moving on, let's tear down the resources that are part of our stack.

1. Run `pulumi destroy` to tear down all resources.  You'll be prompted to make sure you really want to delete these resources. This takes some time; Pulumi waits for all the resources to be removed before it considers the destroy operation to be complete.

1. To delete the stack itself, run `pulumi stack rm`. Note that this command deletes all deployment history from the Pulumi Console.

## Summary

In this tutorial, we saw how to use Pulumi programs to create and manage cloud resources in Microsoft Azure, using Python and pypi packages. To preview and update infrastructure, use `pulumi up`. To clean up resources, run `pulumi destroy`.

For a follow-up example on how to use Pulumi programs to create a Kubernetes
apps on your new cluster, see [Kubernetes Tutorial: Getting Started With Pulumi]({{< prelref "configmap-rollout" >}}).

We also encourage you to watch Joe Beda, co-founder of Kubernetes and Heptio,
take Pulumi for a spin in an episode of [TGIK8s](https://github.com/heptio/tgik).

<iframe width="560" height="315" src="https://www.youtube.com/embed/ILMK65YVSKw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
