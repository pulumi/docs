---
title: Getting Started with Pulumi on AWS using TypeScript
meta_desc: Learn how to build and deploy AWS infrastructure using TypeScript and Pulumi
layout: tutorial
---

# Getting Started with Pulumi on AWS using TypeScript

Welcome! This guide will walk you through creating your first AWS infrastructure using Pulumi and TypeScript. By the end of this tutorial, you'll have deployed a real application to AWS and understand the core concepts of infrastructure as code with Pulumi.

## What We'll Build

Instead of just creating a simple S3 bucket, we'll build something more exciting: a **containerized web application** with:
- A Docker container running your application
- AWS Fargate for serverless container hosting
- Application Load Balancer for high availability
- Auto-scaling based on CPU usage
- CloudWatch logging for monitoring

## Prerequisites

Before we begin, make sure you have:

1. **An AWS account** - [Sign up for free](https://aws.amazon.com/free)
2. **Node.js 18+** - [Download here](https://nodejs.org/)
3. **Pulumi CLI** - Install with:
   ```bash
   curl -fsSL https://get.pulumi.com | sh
   ```
4. **AWS CLI** - [Installation guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
5. **Docker** - [Get Docker](https://docs.docker.com/get-docker/)

## Step 1: Configure AWS Access

First, configure your AWS credentials so Pulumi can manage resources in your account:

```bash
aws configure
```

Enter your AWS Access Key ID, Secret Access Key, and preferred region when prompted.

## Step 2: Create a New Pulumi Project

Create a new directory for your project and initialize a Pulumi program:

```bash
mkdir my-first-pulumi-app && cd my-first-pulumi-app
pulumi new aws-typescript
```

Follow the prompts:
- **Project name**: Accept the default or choose your own
- **Project description**: Optional description
- **Stack name**: Use `dev` for development

This creates:
- `Pulumi.yaml` - Project configuration
- `Pulumi.dev.yaml` - Stack-specific configuration
- `index.ts` - Your infrastructure code
- `package.json` - Node.js dependencies

## Step 3: Understanding Pulumi Concepts

Before we write code, let's understand three key Pulumi concepts:

### Resources
Resources are the building blocks of your infrastructure (like EC2 instances, S3 buckets, or databases). In Pulumi, you declare resources using your programming language.

### Stacks
Stacks are isolated, independently configurable instances of your infrastructure. You might have `dev`, `staging`, and `production` stacks.

### State
Pulumi stores the state of your infrastructure to track what resources exist. By default, this is stored in Pulumi Cloud (free for individual use).

## Step 4: Write Your Infrastructure Code

Replace the contents of `index.ts` with:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Create a VPC for our application
const vpc = new awsx.ec2.Vpc("app-vpc", {
    numberOfAvailabilityZones: 2,
});

// Create an ECS cluster
const cluster = new aws.ecs.Cluster("app-cluster");

// Create a load balancer
const loadBalancer = new awsx.lb.ApplicationLoadBalancer("app-lb", {
    defaultTargetGroup: {
        port: 80,
        protocol: "HTTP",
        healthCheck: {
            path: "/",
            interval: 30,
        },
    },
});

// Build and publish a Docker image to ECR
const image = new awsx.ecr.Image("app-image", {
    repositoryUrl: new aws.ecr.Repository("app-repo").repositoryUrl,
    context: "./app",
    dockerfile: "./app/Dockerfile",
});

// Create a Fargate service
const service = new awsx.ecs.FargateService("app-service", {
    cluster: cluster.arn,
    taskDefinitionArgs: {
        container: {
            name: "app-container",
            image: image.imageUri,
            cpu: 128,
            memory: 512,
            essential: true,
            portMappings: [{
                containerPort: 80,
                targetGroup: loadBalancer.defaultTargetGroup,
            }],
        },
    },
    desiredCount: 2,
});

// Enable auto-scaling
const autoScaling = new aws.appautoscaling.Target("app-scaling", {
    maxCapacity: 10,
    minCapacity: 2,
    resourceId: pulumi.interpolate`service/${cluster.name}/${service.service.name}`,
    scalableDimension: "ecs:service:DesiredCount",
    serviceNamespace: "ecs",
});

const autoScalingPolicy = new aws.appautoscaling.Policy("app-scaling-policy", {
    policyType: "TargetTrackingScaling",
    resourceId: autoScaling.resourceId,
    scalableDimension: autoScaling.scalableDimension,
    serviceNamespace: autoScaling.serviceNamespace,
    targetTrackingScalingPolicyConfiguration: {
        predefinedMetricSpecification: {
            predefinedMetricType: "ECSServiceAverageCPUUtilization",
        },
        targetValue: 70,
    },
});

// Export the load balancer URL
export const url = loadBalancer.loadBalancer.dnsName;
```

## Step 5: Create Your Application

Create a simple Node.js application to deploy. Make a directory called `app`:

```bash
mkdir app
```

Create `app/index.js`:

```javascript
const express = require('express');
const app = express();
const port = 80;

app.get('/', (req, res) => {
    res.send(`
        <html>
            <head>
                <title>My First Pulumi App</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 50px; }
                    h1 { color: #7c3aed; }
                </style>
            </head>
            <body>
                <h1>🎉 Congratulations!</h1>
                <p>You've successfully deployed your first application with Pulumi!</p>
                <p>This app is running on AWS Fargate with auto-scaling enabled.</p>
                <p>Instance: ${process.env.HOSTNAME || 'unknown'}</p>
            </body>
        </html>
    `);
});

app.listen(port, () => {
    console.log(`App listening at http://localhost:${port}`);
});
```

Create `app/package.json`:

```json
{
  "name": "pulumi-app",
  "version": "1.0.0",
  "main": "index.js",
  "dependencies": {
    "express": "^4.18.0"
  },
  "scripts": {
    "start": "node index.js"
  }
}
```

Create `app/Dockerfile`:

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 80
CMD ["npm", "start"]
```

## Step 6: Install Dependencies

Install the required Pulumi packages:

```bash
npm install @pulumi/awsx
```

## Step 7: Deploy Your Infrastructure

Now for the exciting part - deploying to AWS:

```bash
pulumi up
```

Pulumi will show you a preview of what it's going to create. Review the changes and select **yes** to deploy.

This will:
1. Create a VPC with public and private subnets
2. Build your Docker image
3. Push it to Amazon ECR
4. Create an ECS cluster and Fargate service
5. Set up load balancing and auto-scaling
6. Output the URL of your application

The deployment takes about 5-7 minutes. Once complete, you'll see:

```
Outputs:
    url: "app-lb-xxxxxxx.us-west-2.elb.amazonaws.com"
```

## Step 8: Access Your Application

Open the URL in your browser. You should see your congratulations message! 

Try refreshing the page multiple times - you'll notice the instance ID changes as the load balancer distributes traffic across your containers.

## Step 9: Make Changes

Let's update the application. Edit `app/index.js` and change the message:

```javascript
<h1>🚀 My Pulumi App - Updated!</h1>
<p>This is version 2 of my application.</p>
```

Deploy the changes:

```bash
pulumi up
```

Pulumi will:
1. Rebuild your Docker image
2. Push the new version to ECR
3. Perform a rolling update of your service
4. Maintain availability during the deployment

## Step 10: Monitor Your Application

View logs from your application:

```bash
pulumi logs --follow
```

Check the status of your resources:

```bash
pulumi stack
```

## Understanding the Magic

What makes Pulumi powerful:

1. **Real Programming Languages**: Use TypeScript's type safety, IDE support, and debugging tools
2. **State Management**: Pulumi tracks your infrastructure state automatically
3. **Secrets Encryption**: Sensitive values are encrypted by default
4. **Preview Changes**: Always see what will change before deploying
5. **Rollback Capability**: Easy to revert changes if something goes wrong

## Clean Up

To avoid AWS charges, destroy your resources when done:

```bash
pulumi destroy
```

This removes all resources created by Pulumi.

## Next Steps

Congratulations! You've deployed a real application to AWS with Pulumi. Here's what to explore next:

1. **[Pulumi ESC](https://www.pulumi.com/docs/esc/)** - Manage secrets and configuration
2. **[Pulumi Insights](https://www.pulumi.com/docs/insights/)** - Search and analyze your infrastructure
3. **[Stack References](https://www.pulumi.com/docs/concepts/stack/#stack-references)** - Share outputs between stacks
4. **[Policy as Code](https://www.pulumi.com/docs/using-pulumi/crossguard/)** - Enforce security and compliance rules

## Get Help

- 💬 [Join our Slack community](https://slack.pulumi.com)
- 📚 [Browse the documentation](https://www.pulumi.com/docs/)
- 🎓 [Explore more tutorials](https://www.pulumi.com/learn/)
- 🐛 [Report issues on GitHub](https://github.com/pulumi/pulumi)

Welcome to the Pulumi community! We're excited to see what you'll build.