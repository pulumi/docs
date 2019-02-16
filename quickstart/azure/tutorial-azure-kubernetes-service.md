---
title: "Tutorial: Azure Kubernetes Service"
---

In this tutorial, we'll use Python to deploy an instance of Azure Kubernetes Service (AKS).

## Prerequisites

1.  [Install Pulumi](../install.html)
1.  [Configure Azure credentials](./setup.html)

## Create AKS and supporting resources {#AKS}

1.  In a new folder `aks`, create an empty project with `pulumi new`. Make sure you have run `az login` or configured credentials for Azure.
    ```
    $ pulumi new azure-python --dir aks
    $ cd aks
    $ pip install -r requirements.txt
    ```

2.  Open `__main__.py` and replace the contents with the following:

    ```python
    import pulumi
    from pulumi import ResourceOptions
    from pulumi_azure.core import ResourceGroup
    from pulumi_azure.role import Assignment
    from pulumi_azure.ad import Application, ServicePrincipal, ServicePrincipalPassword
    from pulumi_azure.containerservice import KubernetesCluster, Registry
    from pulumi_azure.network import VirtualNetwork, Subnet
    from pulumi_kubernetes import Provider

    # replace these values
    PREFIX = 'replaceme'
    PASSWORD = 'replaceme'
    SSHKEY = 'replaceme'

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
        location='westeurope'
    )

    vnet = VirtualNetwork(
        'vnet',
        name=PREFIX + 'vnet',
        location=rg.location,
        resource_group_name=rg.name,
        address_spaces=['10.0.0.0/8']
    )

    subnet = Subnet(
        'subnet',
        name=PREFIX + 'subnet',
        resource_group_name=rg.name,
        address_prefix='10.0.0.0/23',
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
        kubernetes_version="1.12.5",
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
                "ssh_key": [
                    {
                        "keyData": SSHKEY
                    }
                ]
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

    pulumi.export('kubecfg', aks.kube_config_raw)
    ```

    This example uses the [@pulumi_azure](https://pulumi.io/reference/pkg/python/pulumi_azure/index.html) package to create and manage several Azure resources including: a [pulumi_azure.containerservice.KubernetesCluster](https://pulumi.io/reference/pkg/python/pulumi_azure/containerservice/#pulumi_azure.containerservice.KubernetesCluster), [pulumi_azure.containerservice.Registry](https://pulumi.io/reference/pkg/python/pulumi_azure/containerservice/#pulumi_azure.containerservice.Registry) which will store Docker images and [pulumi_azure.network.VirtualNetwork](https://pulumi.io/reference/pkg/python/pulumi_azure/network/#pulumi_azure.network.VirtualNetwork) that will contain AKS worker nodes and several others. We are using implicit and explicit dependencies in this configuration. For example, resource outputs can be used as inputs to imply dependency between resources, but you can also declare dependency using [ResourceOptions](/reference/programming-model.html#resources) passed to the resource as additional argumanets.

3.  To preview and deploy changes, run `pulumi update`. The command shows a preview of the resources that will be created and prompts on whether to proceed with the deployment.  Note that the stack itself is counted as a resource, though it does not correspond to an actual cloud resource.

    ```bash
    $ pulumi update
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
    ```

4.  Now, proceed with the deployment. 

    ```bash
    Do you want to perform this update?
    > yes
      no
      details

        Type                                         Name                Status      Info
    +   pulumi:pulumi:Stack                          aks-dev             created
    +   ├─ azure:core:ResourceGroup                  rg                  created
    +   ├─ azure:ad:Application                      aks-app             created
    +   ├─ azure:network:VirtualNetwork              vnet                created
    +   ├─ azure:containerservice:Registry           acr                 created
    +   ├─ azure:ad:ServicePrincipal                 aks-sp              created
    +   ├─ azure:ad:ServicePrincipalPassword         aks-sp-pwd          created
    +   ├─ azure:role:Assignment                     acr-permissions     created
    +   ├─ azure:network:Subnet                      subnet              created
    +   ├─ azure:containerservice:KubernetesCluster  aks                 created
    +   └─ azure:role:Assignment                     subnet-permissions  created

    Outputs:
        kubecfg: "omitted"

    Resources:
        + 11 created

    Duration: 7m30s

    Permalink: https://app.pulumi.com/4c74356b41/aks/dev/updates/10
    ```

    To see the full details of the deployment and the resources that are now part of the stack, open the update permalink in a browser.

5.  To view the provisioned resources on the command line, run `pulumi stack`. You'll also see a [stack output](/reference/stack.html#output) corresponding to the kubernetes config file you can use to access the AKS cluster we created.  

    ```
    $ pulumi stack
    ...
    Current stack resources (12):
        TYPE                                                        NAME
        pulumi:pulumi:Stack                                         aks-dev
        pulumi:providers:azure                                      default
        azure:core/resourceGroup:ResourceGroup                      rg
        azure:ad/application:Application                            aks-app
        azure:ad/servicePrincipal:ServicePrincipal                  aks-sp
        azure:ad/servicePrincipalPassword:ServicePrincipalPassword  aks-sp-pwd
        azure:containerservice/registry:Registry                    acr
        azure:network/virtualNetwork:VirtualNetwork                 vnet
        azure:network/subnet:Subnet                                 subnet
        azure:role/assignment:Assignment                            subnet-permissions
        azure:role/assignment:Assignment                            acr-permissions
        azure:containerservice/kubernetesCluster:KubernetesCluster  aks

    Current stack outputs (1):
        OUTPUT   VALUE
        kubecfg  ommited
    ```

6.  If you want to provision Kubernetes resources, you need to create a Kubernetes provider using the following:

    ```
    aks = KubernetesCluster(
        omitted
    )

    custom_provider = Provider(
        "inflation_provider", kubeconfig=aks.kube_config_raw
    )
    ```

    You are all set after this. There are alternative ways of setting up Kubernetes provider. We have [kubernetes tutotials](/quickstart/kubernetes/) which you can follow to get a better understanding of setting up and working with Kubernetes.

## Clean up

Before moving on, let's tear down the resources that are part of our stack.

1.  Run `pulumi destroy` to tear down all resources.  You'll be prompted to make sure you really want to delete these resources. This takes some time; Pulumi waits for all the resources to be removed before it considers the destroy operation to be complete.

2.  To delete the stack itself, run `pulumi stack rm`. Note that this command deletes all deployment history from the Pulumi Console.

## Summary

In this tutorial, we saw how to use Pulumi programs to create and manage cloud resources in Microsoft Azure, using Python and pypi packages. To preview and update infrastructure, use `pulumi update`. To clean up resources, run `pulumi destroy`.
