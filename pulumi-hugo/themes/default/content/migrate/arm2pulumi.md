---
title: Convert Your Azure ARM Template to a Modern Language
url: /arm2pulumi
layout: arm2pulumi
linktitle: ARM to Pulumi
menu:
  converters:
    identifier: arm2pulumi
    weight: 1
    
meta_desc: See what your Azure ARM Template would look like in a modern language thanks to Pulumi.

examples:
    - name: Storage Account
      filename: azuredeploy.json
      description:
      code: |
        {
            "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
            "contentVersion": "1.0.0.0",
            "parameters": {
                "storageAccountType": {
                    "type": "string",
                    "defaultValue": "Standard_LRS",
                    "allowedValues": [
                        "Standard_LRS",
                        "Standard_GRS",
                        "Standard_ZRS",
                        "Premium_LRS"
                    ],
                    "metadata": {
                        "description": "Storage Account type"
                    }
                },
                "location": {
                    "type": "string",
                    "defaultValue": "[resourceGroup().location]",
                    "metadata": {
                        "description": "Location for all resources."
                    }
                },
                "storageAccountName": {
                    "type": "string"
                }
            },
            "resources": [
                {
                    "type": "Microsoft.Storage/storageAccounts",
                    "apiVersion": "2019-04-01",
                    "name": "[parameters('storageAccountName')]",
                    "location": "[parameters('location')]",
                    "sku": {
                        "name": "[parameters('storageAccountType')]"
                    },
                    "properties": {
                        "sku": {
                            "name": "[parameters('storageAccountType')]"
                        },
                        "kind": "StorageV2"
                    }
                }
            ],
            "outputs": {
                "storageAccountName": {
                    "type": "string",
                    "value": "[reference(parameters('storageAccountName')).name]"
                }
            }
        }

    - name: AKS Cluster
      filename: azuredeploy.json
      description:
      code: |
        {
            "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
            "contentVersion": "1.0.0.1",
            "parameters": {
                "clusterName": {
                    "type": "string",
                    "defaultValue": "aks101cluster",
                    "metadata": {
                        "description": "The name of the Managed Cluster resource."
                    }
                },
                "location": {
                    "type": "string",
                    "defaultValue": "[resourceGroup().location]",
                    "metadata": {
                        "description": "The location of the Managed Cluster resource."
                    }
                },
                "dnsPrefix": {
                    "type": "string",
                    "metadata": {
                        "description": "Optional DNS prefix to use with hosted Kubernetes API server FQDN."
                    }
                },
                "osDiskSizeGB": {
                    "type": "int",
                    "defaultValue": 0,
                    "metadata": {
                        "description": "Disk size (in GB) to provision for each of the agent pool nodes. This value ranges from 0 to 1023. Specifying 0 will apply the default disk size for that agentVMSize."
                    },
                    "minValue": 0,
                    "maxValue": 1023
                },
                "agentCount": {
                    "type": "int",
                    "defaultValue": 3,
                    "metadata": {
                        "description": "The number of nodes for the cluster."
                    },
                    "minValue": 1,
                    "maxValue": 50
                },
                "agentVMSize": {
                    "type": "string",
                    "defaultValue": "Standard_DS2_v2",
                    "metadata": {
                        "description": "The size of the Virtual Machine."
                    }
                },
                "linuxAdminUsername": {
                    "type": "string",
                    "metadata": {
                        "description": "User name for the Linux Virtual Machines."
                    }
                },
                "sshRSAPublicKey": {
                    "type": "string",
                    "metadata": {
                        "description": "Configure all linux machines with the SSH RSA public key string. Your key should include three parts, for example 'ssh-rsa AAAAB...snip...UcyupgH azureuser@linuxvm'"
                    }
                },
                "servicePrincipalClientId": {
                    "metadata": {
                        "description": "Client ID (used by cloudprovider)"
                    },
                    "type": "securestring"
                },
                "servicePrincipalClientSecret": {
                    "metadata": {
                        "description": "The Service Principal Client Secret."
                    },
                    "type": "securestring"
                },
                "osType": {
                    "type": "string",
                    "defaultValue": "Linux",
                    "allowedValues": [
                        "Linux"
                    ],
                    "metadata": {
                        "description": "The type of operating system."
                    }
                }
            },
            "resources": [
                {
                    "apiVersion": "2020-03-01",
                    "type": "Microsoft.ContainerService/managedClusters",
                    "location": "[parameters('location')]",
                    "name": "[parameters('clusterName')]",
                    "properties": {
                        "dnsPrefix": "[parameters('dnsPrefix')]",
                        "agentPoolProfiles": [
                            {
                                "name": "agentpool",
                                "osDiskSizeGB": "[parameters('osDiskSizeGB')]",
                                "count": "[parameters('agentCount')]",
                                "vmSize": "[parameters('agentVMSize')]",
                                "osType": "[parameters('osType')]",
                                "storageProfile": "ManagedDisks"
                            }
                        ],
                        "linuxProfile": {
                            "adminUsername": "[parameters('linuxAdminUsername')]",
                            "ssh": {
                                "publicKeys": [
                                    {
                                        "keyData": "[parameters('sshRSAPublicKey')]"
                                    }
                                ]
                            }
                        },
                        "servicePrincipalProfile": {
                            "clientId": "[parameters('servicePrincipalClientId')]",
                            "secret": "[parameters('servicePrincipalClientSecret')]"
                        }
                    }
                }
            ],
            "outputs": {
                "controlPlaneFQDN": {
                    "type": "string",
                    "value": "[reference(parameters('clusterName')).fqdn]"
                }
            }
        }

    - name: Container Registry
      filename: azuredeploy.json
      description:
      code: |
        {
            "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
            "contentVersion": "1.0.0.0",
            "parameters": {
                "acrName": {
                    "type": "string",
                    "minLength": 5,
                    "maxLength": 50,
                    "metadata": {
                        "description": "Name of your Azure Container Registry"
                    }
                },
                "acrAdminUserEnabled": {
                    "type": "bool",
                    "defaultValue": false,
                    "metadata": {
                        "description": "Enable admin user that have push / pull permission to the registry."
                    }
                },
                "location": {
                    "type": "string",
                    "defaultValue": "[resourceGroup().location]",
                    "metadata": {
                        "description": "Location for all resources."
                    }
                },
                "acrSku": {
                    "type": "string",
                    "metadata": {
                        "description": "Tier of your Azure Container Registry."
                    },
                    "defaultValue": "Basic",
                    "allowedValues": [
                        "Basic",
                        "Standard",
                        "Premium"
                    ]
                }
            },
            "resources": [
                {
                    "name": "[parameters('acrName')]",
                    "type": "Microsoft.ContainerRegistry/registries",
                    "apiVersion": "2019-12-01-preview",
                    "location": "[parameters('location')]",
                    "comments": "Container registry for storing docker images",
                    "tags": {
                        "displayName": "Container Registry",
                        "container.registry": "[parameters('acrName')]"
                    },
                    "properties": {
                        "adminUserEnabled": "[parameters('acrAdminUserEnabled')]",
                        "sku": {
                            "name": "[parameters('acrSku')]"
                        }
                    }
                }
            ],
            "outputs": {
                "acrLoginServer": {
                    "value": "[reference(parameters('acrName'),'2019-12-01-preview').loginServer]",
                    "type": "string"
                }
            }
        }

form:
    hubspot_form_id: 8381e562-5fdf-4736-bb10-86096705e4ee
---
