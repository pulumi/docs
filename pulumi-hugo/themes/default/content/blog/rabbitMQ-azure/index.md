---
title: "Deploy a Serverless RabbitMQ Cluster on Azure with .NET"
date: 2020-07-16
meta_desc: "Deploying a Geo-Redundant Serverless RabbitMQ Cluster on Azure Using Pulumi for .NET"
meta_image: 1.png
authors:
    - itay-podhajcer
tags:
    - Azure
    - .NET
    - rabbitmq

---

Itay Podhajcer is Chief Architect at Velocity Career Labs and a highly experienced software development and technology professional, consultant, architect & project manager. He shared his article on building an Azure serverless cluster for deploying RabbitMQ with C#. The original article was published [here](https://medium.com/microsoftazure/deploying-a-geo-redundant-serverless-rabbitmq-cluster-on-azure-using-pulumi-for-net-71e6b417378d).

<!--more-->

![Graphic](1.png)
<br>

Pulumi, an open source cloud development platform that supports multiple languages and platforms, allows programming and managing cloud environments using a consistent model and the power of full programming languages.

One of those supported languages is C#, which we will be using to deploy a geo-redundant serverless cluster of the well-known messaging solution RabbitMQ. To run the cluster, we will be using three regions, in which we will be deploying:

- Two peered virtual networks, one internal for the containers, and one external for connecting to the other regions. Two networks are required because (at least at the writing of this article) Azure Container Instances only support one peered network, so to overcome that, we will be peering the network with the containers with an additional network in the region, which in turn, connects with the external networks from the other regions.
- A RabbitMQ node using Azure Container Instances that will be deployed in the internal virtual network.
- An Azure Firewall, which will be deployed in the external virtual network, acting as a network virtual appliance (NVA) with rules for forwarding traffic between the internal node and the other regions.
- Route tables with routes that will enable the inter-network transfer of data.
- A storage account with file shares for maintaining the node’s state.

Additionally, as we will be using RabbitMQ’s DNS based cluster peer discovery mechanism, we will also be deploying at the global level:

- DNS zone for the node’s A records and the discovery record required by RabbitMQ.
- A reverse DNS zone for the PTR records of the nodes required by RabbitMQ.

{{< figure src="2.png" title="Geo-redundant serverless RabbitMQ cluster" >}}

## Prerequisites

As we will be using Pulumi for .NET to deploy to Azure, we will need the following installed on our workstation:

- Azure CLI: installation guide is available [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).
- .N ET Core SDK: download is available [here](https://dotnet.microsoft.com/download).
- Pulumi: installation guide is available [here](https://www.pulumi.com/docs/get-started/install/).

## Example Repository

The complete example of deploying the RabbitMQ cluster can be downloaded or cloned for the following GitHub repository:

[![Github link](repo.png)](https://github.com/cladular/pulumi-rabbitmq-azure)
<br>

When running `pulumi up` you will be asked to create a stack (you can use whatever you here like `Example`) and set a passphrase (you can leave it empty and press enter as there are no stored secrets in this stack).

## Setup the Project

After all the required tools are installed, we can start by creating the empty Pulumi project running `pulumi new azure-csharp` inside an empty folder. Set a name for the project (like `Example`), a description (like `RabbitMQ Serverless Cluster`), a stack name (like `Example`), a passphrase (you can use an empty one and just press enter as we won’t be storing secrets in the stack) and an Azure location (just use the default).

Now that we have an initial project, we will also add the `Pulumi.Random` package to the project by running the command `dotnet add package Pulumi.Random`, as we will be using it to generate the cluster sec, And rename the `MyStack` class and file to `ExampleStack` (it also needs to be changed inside `Program.cs` which holds the code that triggers the deployment of the stack).

Lastly, we call `dotnet restore` to also download the `Pulumi.Azure` package that was included in the project when it was created.

## Writing the Stack

We will start by defining a few constants, the constructor, an empty method called `Stack()`, which will be called by the constructor to start creating the resources and a property named `Cookie`, which will hold the cluster’s secret, decorated with the `Output` attribute to let Pulumi know that the value needs to be printed out once the deployment is complete:

{{< gist ItayPodhajcer 7552af98323ce6685e85b07ba67b1598 >}}

Now that we have our initial class, we can start writing methods for the resources we will be creating:

- Resource groups:
<br>
{{< gist ItayPodhajcer 4c57e537f0d9cc15b801035d556c2504 >}}
<br>
- Private DNS zone:

{{< gist ItayPodhajcer 52af6ba0a8f1a92d5352c3218505eefa >}}
<br>

- Private reverse DNS zone:

{{< gist ItayPodhajcer dbb6e125fe7d55ba79a2d09f4a13cfa2 >}}
<br>

- Random string for the RabbitMQ cluster secret:

{{< gist ItayPodhajcer f737d38ea91e446233d295ebb3b80766 >}}
<br>

- DNS zone links:

{{< gist ItayPodhajcer dba947cdec61f910166ea5e74073c13f >}}
<br>

- RabbitMQ node container:

{{< gist ItayPodhajcer 5deb5c83cc5568046d5a39c81f201d2c >}}

<br>
Note that we are overriding RabbitMQ docker image’s default command with `{ “/bin/bash”, “-c”, $”(sleep {ContainerStartupDelay} && docker-entrypoint.sh rabbitmq-server) & wait” }` to delay the startup of the container, but still keep it responsive. More on this later.
<br><br>

- Container mounted volumes:

{{< gist ItayPodhajcer b0ea32b39923904c7d9ffd34b148c535 >}}
<br>

- Storage accounts:

{{< gist ItayPodhajcer bde8bda973a6b1240f16edf1f800e2ea >}}
<br>

- File shares:

{{< gist ItayPodhajcer ddfdca26483c2b0643d01c06e2174fc3 >}}
<br>

- Container ports:

{{< gist ItayPodhajcer 4eb8ae91fe2897dc85af31876097c7f1 >}}
<br>

- Virtual networks:

{{< gist ItayPodhajcer 88576747f1f7a38b6f6203d8cd95e2c4 >}}
<br>

- Internal virtual network subnets:

{{< gist ItayPodhajcer 91de7123a929efe5658119d5ace1ff96 >}}
<br>

Note that we are creating it with the Microsoft.Storage service endpoint to allow access to storage accounts and the `Microsoft.ContainerInstance/containerGroups` delegation, which is required for deploying containers into virtual networks.
<br><br>

- Network profiles, also required for deploying containers into virtual networks:

{{< gist ItayPodhajcer c1eb8c3c31e468e508ed3221eb2718d8 >}}
<br>

- External virtual network subnets:

{{< gist ItayPodhajcer 408e58ffb4b50035085e23c24a56fb81 >}}
<br>

- Internal and external virtual networks peering:

{{< gist ItayPodhajcer db16c583aff0e1f6f0341582dcaab273 >}}
<br>

- External virtual network firewalls:

{{< gist ItayPodhajcer 2e29cbf1a225e41f959318069565c959 >}}
<br>

- Internal and external virtual networks routing:

{{< gist ItayPodhajcer 2bf4513f6b04f9f7849ed67e346a62c5 >}}
<br>

- RabbitMQ nodes DNS records:

{{< gist ItayPodhajcer 52302a51601ccf79d5c3752ad3c18aed >}}
<br>

- RabbitMQ nodes reverse DNS records:

{{< gist ItayPodhajcer 43a386db10e9e2d7ace1285b7097676e >}}
<br>

- Reversing the IP address as required by a reverse PTR record:

{{< gist ItayPodhajcer 09ea2238eca195165be2a02f0442e5f2 >}}
<br>

- Firewall IP forwarding rules:

{{< gist ItayPodhajcer 1bd2098ee4a0430367e3e82ef439b2db >}}
<br>

- RabbitMQ’s discovery DNS record:

{{< gist ItayPodhajcer 0b0a892a76284951e150c04edb24a45f >}}
<br>

- Global peering of the external virtual networks:

{{< gist ItayPodhajcer 6954cd03fb2cb5fce759627635198c60 >}}
<br>

- Global routes for the virtual networks:

{{< gist ItayPodhajcer a2e2016ac2a9db7908c5ac6006f19976 >}}
<br>

- Firewall virtual appliance routes:

{{< gist ItayPodhajcer 6f98ab784eb3fc2e579dea9ec90a46ab >}}
<br>

- Internet outbound routes:

{{< gist ItayPodhajcer f1da19e3eb4561cd0fd662eaa3633302 >}}
<br>

Now that we can create all the necessary resources, it is time to put it all together inside the empty `Stack()` method we created earlier:
<br><br>

{{< gist ItayPodhajcer 31067831e46aac84701661c2dadab99a >}}
<br>

Note that we are using two loops to create the required resources. The first one creates most of the resources (storage, firewall, networks, container, etc.) and the second one creates the DNS A records of the nodes. The second loop combined with the custom container startup command helps us ensure that the nodes will start without failing only when the entire infrastructure is ready.

This workaround is required because (at the writing of the article) Azure Container Instances do not allow manual allocation of private IP address, and because RabibtMQ’s discovery record requires those IPs which are available only after the containers are created, we end up in a chicken-and-the-egg situation. To overcome that, we need to allow the containers to start, but delay the execution of RabbitMQ’s startup script without blocking the container and use to our advantage the fact that RabbitMQ doesn’t start when it can‘t resolve its own hostname (that is why we create those DNS records last).

## Deploying the Stack

Once the script is complete, we can call `pulumi up --yes` to deploy it, where the `--yes` argument just skips the question whether to deploy or not once Pulumi has built the deployment app and discovered all the resources.

Remember that you need to call Azure CLI to login to your subscription, so that Pulumi can execute the deployment. You can call `az login` to login to the Azure portal in an interactive manner.
Checking the Cluster

## Checking the Cluster

To check that all nodes have managed to join the cluster we will connect to one of the nodes using `az container exec` to stream a shell from within that container (see more on the exec command [here](https://docs.microsoft.com/en-us/cli/azure/container?view=azure-cli-latest#az-container-exec)).

Once the shell is connected, you can call `rabbitmqctl cluster_status` and you should see all three nodes in the printed information.

## Conclusion

The example in this article can be used as a base for a complete solution, which includes additional containers and managed services provided by Azure. Also, the code for deploying the example, in a real-world scenario, would be better split off to smaller files, as looking at all the code in one large file is overwhelming, therefore harder to maintain.
