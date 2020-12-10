---
title: Migrate to Pulumi from Terraform
layout: terraform
url: /terraform
meta_desc: How to migrate to Pulumi from Terraform for huge productivity gains, and a unified programming model for Devs and DevOps.

hero:
    title: Modern Infrastructure as Code
    description: |
        Pulumi and Terraform are both able to declaratively create, deploy, and manage
        infrastructure but the similarities end there. Unlike Terraform, Pulumi allows
        you to use a general purpose programming language instead of a custom
        domain-specific-language.
    ide:
        tabs:
            - title: index.ts
              language: typescript
              code: |
                import * as pulumi from "@pulumi/pulumi";
                import * as kubernetes from "@pulumi/kubernetes";

                // Create a K8s namespace.
                const devNamespace = new kubernetes.core.v1.Namespace("devNamespace", {
                    metadata: {
                        name: "dev",
                    },
                });

                // Deploy the K8s nginx-ingress Helm chart into the created namespace.
                const nginxIngress = new kubernetes.helm.v3.Chart("nginx-ingress", {
                    chart: "nginx-ingress",
                    namespace: devNamespace.metadata.name,
                    fetchOpts:{
                        repo: "https://kubernetes-charts.storage.googleapis.com/",
                    },
                });
            - title: __main__.py
              language: python
              code: |
                import pulumi_kubernetes as kubernetes

                # Create a K8s namespace.
                dev_namespace = kubernetes.core.v1.Namespace(
                    "devNamespace",
                    metadata={
                        "name": "dev",
                    })

                # Deploy the K8s nginx-ingress Helm chart into the created namespace.
                nginx_ingress = kubernetes.helm.v3.Chart(
                    "nginx-ingress",
                    kubernetes.helm.v3.ChartOpts(
                        chart="nginx-ingress",
                        namespace=dev_namespace.metadata["name"],
                        fetch_opts=kubernetes.helm.v3.FetchOpts(
                            repo="https://kubernetes-charts.storage.googleapis.com/",
                        ),
                    ),
                )
            - title: main.go
              language: go
              code: |
                    package main

                    import (
                        corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/core/v1"
                        "github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/helm/v3"
                        metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/meta/v1"
                        "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
                    )

                    func main() {
                        pulumi.Run(func(ctx *pulumi.Context) error {

                            // Create a K8s namespace.
                            ns, err := corev1.NewNamespace(ctx, "devNamespace", &corev1.NamespaceArgs{
                                Metadata: &metav1.ObjectMetaArgs{
                                    Name: pulumi.String("dev"),
                                },
                            })
                            if err != nil {
                                return err
                            }

                            // Deploy the K8s nginx-ingress Helm chart into the created namespace.
                            _, err = helm.NewChart(ctx, "nginx-ingress", helm.ChartArgs{
                                Chart: pulumi.String("nginx-ingress"),
                                Namespace: ns.Metadata.ApplyT(func(metadata interface{}) string {
                                    return *metadata.(*metav1.ObjectMeta).Name
                                }).(pulumi.StringOutput),
                                FetchArgs: helm.FetchArgs{
                                    Repo: pulumi.String("https://kubernetes-charts.storage.googleapis.com/"),
                                },
                            })
                            if err != nil {
                                return err
                            }

                            return nil
                        })
                    }
            - title: MyStack.cs
              language: csharp
              code: |
                using Pulumi;
                using Kubernetes = Pulumi.Kubernetes;

                class MyStack : Stack
                {
                    public MyStack()
                    {
                        // Create a K8s namespace.
                        var devNamespace = new Kubernetes.Core.V1.Namespace("devNamespace", new Kubernetes.Types.Inputs.Core.V1.NamespaceArgs
                        {
                            Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
                            {
                                Name = "dev",
                            },
                        });

                        // Deploy the K8s nginx-ingress Helm chart into the created namespace.
                        var nginx = new Kubernetes.Helm.V3.Chart("nginx-ingress", new Kubernetes.Helm.ChartArgs
                        {
                            Chart = "nginx-ingress",
                            Namespace = devNamespace.Metadata.Apply(x => x.Name),
                            FetchOptions = new Kubernetes.Helm.ChartFetchArgs
                            {
                                Repo = "https://kubernetes-charts.storage.googleapis.com/"
                            },
                        });
                    }
                }

awsx_code: |
    import * as awsx from "@pulumi/awsx";

    // Allocate a new VPC with the default settings:
    const vpc = new awsx.ec2.Vpc("custom");

    // Export a few resulting fields to make them easy to use:
    export const vpcId = vpc.id;
    export const vpcPrivateSubnetIds = vpc.privateSubnetIds;
    export const vpcPublicSubnetIds = vpc.publicSubnetIds;

examples:
    - name: AWS EC2 Instance
      filename: main.tf
      description: Provisions an AWS EC2 instance running Ubuntu.
      code: |
        data "aws_ami" "ubuntu" {
            most_recent = true

            filter {
                name   = "name"
                values = ["ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-*"]
            }

            filter {
                name   = "virtualization-type"
                values = ["hvm"]
            }

            owners = ["099720109477"] # Canonical
        }

        resource "aws_instance" "web" {
            ami           = "${data.aws_ami.ubuntu.id}"
            instance_type = "t2.micro"

            tags = {
                Name = "HelloWorld"
            }
        }

    - name: Azure VM
      filename: main.tf
      description: Provisions an Azure Virtual Machine running Ubuntu.
      code: |
        resource "azurerm_resource_group" "example" {
            name = "example-resources"
            location = "West Europe"
        }

        resource "azurerm_virtual_network" "example" {
            name = "example-network"
            address_space = ["10.0.0.0/16"]
            location = azurerm_resource_group.example.location
            resource_group_name = azurerm_resource_group.example.name
        }

        resource "azurerm_subnet" "example" {
            name = "internal"
            resource_group_name = azurerm_resource_group.example.name
            virtual_network_name = azurerm_virtual_network.example.name
            address_prefix = "10.0.2.0/24"
        }

        resource "azurerm_network_interface" "example" {
            name = "example-nic"
            location = azurerm_resource_group.example.location
            resource_group_name = azurerm_resource_group.example.name

            ip_configuration {
                name = "internal"
                subnet_id = azurerm_subnet.example.id
                private_ip_address_allocation = "Dynamic"
            }
        }

        resource "azurerm_linux_virtual_machine" "example" {
            name = "example-machine"
            resource_group_name = azurerm_resource_group.example.name
            location = azurerm_resource_group.example.location
            size = "Standard_F2"
            admin_username = "adminuser"

            network_interface_ids = [
                azurerm_network_interface.example.id,
            ]

            os_disk {
                caching = "ReadWrite"
                storage_account_type = "Standard_LRS"
            }

            source_image_reference {
                publisher = "Canonical"
                offer = "UbuntuServer"
                sku = "16.04-LTS"
                version = "latest"
            }
        }

    - name: GKE Cluster
      filename: main.tf
      description: Provisions a Google Kubernetes Engine (GKE) cluster.
      code: |
        resource "google_container_cluster" "primary" {
            name = "my-gke-cluster"
            location = "us-central1"

            # We can't create a cluster with no node pool defined, but we want to only use
            # separately managed node pools. So we create the smallest possible default
            # node pool and immediately delete it.
            remove_default_node_pool = true
            initial_node_count = 1

            master_auth {
                username = ""
                password = ""

                client_certificate_config {
                    issue_client_certificate = false
                }
            }
        }

        resource "google_container_node_pool" "primary_preemptible_nodes" {
            name = "my-node-pool"
            location = "us-central1"
            cluster = google_container_cluster.primary.name
            node_count = 1

            node_config {
                preemptible  = true
                machine_type = "e2-medium"

                metadata = {
                    disable-legacy-endpoints = "true"
                }

                oauth_scopes = [
                    "https://www.googleapis.com/auth/logging.write",
                    "https://www.googleapis.com/auth/monitoring",
                ]
            }
        }

contact_us_form:
    section_id: contact-us
    hubspot_form_id: 123cfbdb-9ce4-4d33-a9b7-c30302463d7a
    headline: Need assistance?
    quote:
        title: See how top engineering teams enable developers and operators to work better together with Pulumi.
        name: Kim Hamilton
        name_title: CTO, Learning Machine
        content: |
            Pulumi has given our team the tools and framework to achieve a unified development and DevOps model,
            boosting productivity and taking our business to any cloud environment that our customers need. We
            retired 25,000 lines of complex code that few team members understood and replaced it with 100s of
            lines in a familiar programming language.
---
