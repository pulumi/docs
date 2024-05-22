---
title: Automate AWS Aurora Serverless v2 Deployment with Pulumi
meta_desc: A comprehensive guide to automate file expiration in AWS S3 using Pulumi.
description: A comprehensive guide to automate file expiration in AWS S3 using Pulumi.
layout: topic
estimated_time: 5
providers:
    - aws
collections:
    - serverless
---

## Overview

In this tutorial, you will learn how to automate the deployment of AWS Aurora Serverless v2 clusters using Pulumi. AWS Aurora Serverless v2 provides a cost-effective, scalable solution for running your relational databases without managing database servers. Pulumi allows you to define, deploy, and manage your cloud infrastructure using familiar programming languages.

## Prerequisites

Before you begin, ensure you have the following:

- An AWS account with appropriate permissions to create and manage Aurora Serverless v2 clusters.
- Pulumi CLI installed on your local machine. You can download it from the [Pulumi website](https://www.pulumi.com/docs/get-started/install/).
- Node.js and npm installed. You can download them from the [Node.js website](https://nodejs.org/).
- AWS CLI installed and configured with your AWS credentials. You can download it from the [AWS CLI website](https://aws.amazon.com/cli/).
- Pulumi ESC configured for managing secrets. Follow the setup guide on the [Pulumi ESC documentation](https://www.pulumi.com/docs/esc/).

## Define the Aurora Serverless v2 Cluster

1. Open the `index.ts` file in your project directory and add the following code:

    ```typescript
    import * as pulumi from "@pulumi/pulumi";
    import * as aws from "@pulumi/aws";

    // Create an RDS subnet group
    const subnetGroup = new aws.rds.SubnetGroup("aurora-subnet-group", {
        subnetIds: ["subnet-12345678", "subnet-87654321"], // Replace with your subnet IDs
        tags: {
            Name: "aurora-subnet-group",
        },
    });

    // Create a security group for the Aurora cluster
    const securityGroup = new aws.ec2.SecurityGroup("aurora-security-group", {
        description: "Allow access to Aurora Serverless v2 cluster",
        ingress: [
            {
                protocol: "tcp",
                fromPort: 3306,
                toPort: 3306,
                cidrBlocks: ["0.0.0.0/0"], // Replace with your IP range
            },
        ],
    });

    // Use Pulumi ESC to manage secrets securely
    const config = new pulumi.Config();
    const dbPassword = config.requireSecret("dbPassword");

    // Create an Aurora Serverless v2 cluster
    const cluster = new aws.rds.Cluster("aurora-cluster", {
        engine: "aurora-mysql", // or "aurora-postgresql" based on your preference
        engineMode: "serverless",
        scalingConfiguration: {
            autoPause: true,
            minCapacity: 2,
            maxCapacity: 64,
        },
        masterUsername: "admin",
        masterPassword: dbPassword,
        skipFinalSnapshot: true,
        dbSubnetGroupName: subnetGroup.name,
        vpcSecurityGroupIds: [securityGroup.id],
        backupRetentionPeriod: 7, // Retain backups for 7 days
        preferredBackupWindow: "07:00-09:00", // Backup window
        preferredMaintenanceWindow: "sun:23:00-mon:01:30", // Maintenance window
        // kmsKeyId: "your-kms-key-id", // Optional: Replace with your KMS key ID for encryption
    });

    // Output the cluster endpoint
    export const clusterEndpoint = cluster.endpoint;
    ```

This Pulumi TypeScript code creates an RDS subnet group named `aurora-subnet-group`, which includes the specified subnet IDs (`subnet-12345678` and `subnet-87654321`). This subnet group allows the Aurora cluster to span across multiple Availability Zones, ensuring high availability. Additionally, the code creates a security group named `aurora-security-group`, which allows inbound traffic on port 3306 (the default port for MySQL) from any IP address (`0.0.0.0/0`). This security group ensures that only specified traffic can access the Aurora cluster.

The code then creates an Aurora Serverless v2 cluster named `aurora-cluster`. The cluster is configured to use the MySQL engine (`aurora-mysql`) and the serverless engine mode. It is set up with automatic pause and scaling, with a minimum capacity of 2 ACUs and a maximum capacity of 64 ACUs.

Instead of using a static password, the tutorial now uses Pulumi ESC to securely manage the database password. This ensures that sensitive information is not hard-coded into your infrastructure code, enhancing security.

Finally, the code exports the endpoint of the Aurora cluster, allowing you to use it in other parts of your infrastructure or applications. This setup provides a scalable, serverless MySQL database cluster on AWS with essential networking and security configurations, along with automated backups and maintenance settings.

## Step 3: Configure Secrets with Pulumi ESC

1. Set the database password using Pulumi ESC:

    ```bash
    pulumi config set --secret dbPassword your-secure-password
    ```

    This command securely stores the database password in Pulumi ESC, ensuring it is not exposed in your code or version control.

## Step 4: Deploy the Infrastructure

1. Deploy your Pulumi stack:

    ```bash
    pulumi up
    ```

    Confirm the deployment and wait for the resources to be created.

## Step 5: Verify the Deployment

1. Log in to the [AWS Management Console](https://aws.amazon.com/console/).
2. Navigate to the RDS service.
3. Verify that the Aurora Serverless v2 cluster has been created and is in an available state.

## Conclusion

In this tutorial, you have successfully automated the deployment of an AWS Aurora Serverless v2 cluster using Pulumi. By leveraging Pulumi ESC, you securely managed sensitive information, enhancing the security of your infrastructure. You can now manage your cloud infrastructure with code, making deployments more consistent and repeatable.

For more information on Pulumi and AWS Aurora Serverless v2, refer to the [Pulumi documentation](https://www.pulumi.com/docs/) and [AWS Aurora Serverless v2 documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html).

## Learn more about Pulumi

Pulumi is free, [open source](https://github.com/pulumi/pulumi), and optionally pairs with the [Pulumi Cloud](/docs/pulumi-cloud/) to make managing infrastructure secure, reliable, and hassle-free.

- Follow the [Getting Started](/docs/get-started/) guide to give Pulumi a try.

- [Join our community on Slack](https://slack.pulumi.com/) to discuss this guide, and let us know what you think.
