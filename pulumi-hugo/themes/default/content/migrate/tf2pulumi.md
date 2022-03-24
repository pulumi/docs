---
title: Convert Your Terraform to a Modern Language
url: /tf2pulumi
layout: tf2pulumi
linktitle: Terraform to Pulumi
menu:
  converters:
    identifier: tf2pulumi
    weight: 4
meta_desc: See what your Terraform HCL would look like in a modern language thanks to Pulumi.

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

form:
    hubspot_form_id: 8381e562-5fdf-4736-bb10-86096705e4ee
---
