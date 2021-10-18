---
title: "Getting Started with ECS Anywhere"
date: 2021-05-27
draft: false
meta_desc: Amazon Web Services' ECS Anywhere lets you run your ECS workload on any cloud provider, in any data center of your choosing.
meta_image: ecs_anywhere.png
authors:
    - piers-karsenbarg
tags:
    - aws
    - ecs
    - containers
---

When Amazon’s Elastic Container Service (ECS) first launched in 2014, it enabled an easy and convenient way of deploying and scheduling containers in the AWS ecosystem. Back then, you would run a set of EC2 instances, and ECS would deploy containers to instances based on the size, resources, and placement requirements you specified.

<!--more-->

In 2018, AWS released Fargate, bringing a serverless feel to the platform. You could have ECS run your container without having to manage any infrastructure.

The next iteration is [ECS Anywhere](https://aws.amazon.com/blogs/containers/introducing-amazon-ecs-anywhere/), which allows you to deploy your containers to almost any server. You can deploy to an EC2 instance inside AWS, a virtual machine (VM) in another cloud provider, or even a bare metal server in your private data center. Best of all, you can control the deployments in the same way you would with EC2 or Fargate.

## Why would I want to use this?

As we’ve seen over the past few years, the ECS system makes it a convenient service to use. There are several reasons why you might want to use ECS as a control plane for your container-based applications but not run the actual applications within your AWS infrastructure. These include:

* **Latency requirements:** You have systems on another network, and you need your containers to be running on that same network to give you the low latency required.
* **Regulatory requirements:** There may be legal, security, or privacy needs that can only be satisfied by running your application in your own data center.
* **Operational requirements:** you don’t want to manage a complex container cluster yourself on another network and are already running workloads on ECS.

## Behind the scenes

The crucial part of understanding how ECS Anywhere works is that you’re using ECS to manage the deployment of the containers to your VMs (which we’ll call nodes going forward). The actual interaction between your application and whatever network traffic or instructions it receives is separate. You’ll see this shown in the example below where we deploy two VMs and a load balancer. Once the application is up and running, ECS takes a back seat and waits for the instructions to deploy a new version or stop the application from running altogether.

There are three parts to getting this to work:

### 1. Setting up the AWS infrastructure

AWS’ Systems Manager has a feature called “Hybrid Activations.” We’ll use it to link the external nodes to the ECS cluster using an activation code and an activation id. We’ll also create various IAM roles necessary to activate the nodes and assign them to the ECS cluster. In our example, we’ll also set up IAM roles so that our application can send logs to CloudWatch as well.

### 2. Deploying the nodes

During the node setup process, we’re going to download and run a custom script from AWS that performs several tasks:

1. It installs the docker engine.
1. It installs the SSM agent and registers it with the Systems Manager’s Fleet manager (which keeps track of the nodes and assigns an IAM role)
1. It installs the ECS agent, which connects to the ECS cluster and listens for instructions.

### 3. Deploying the application

There are very few differences between deploying an application to ECS internally on AWS infrastructure here. We set up a Task Definition and a Service within the ECS infrastructure, and the only difference is that we’ll use the new launch type of `EXTERNAL` instead of `EC2` or `FARGATE`, which tells the cluster to push the instructions for running the application to our nodes.

## Deploying a Node.js application using ECS Anywhere

In this example, we will be deploying a basic Node.js application within a container to a pair of virtual machines (VMs) behind a load balancer. You’ll need multiple VMs because ECS won’t deploy the multiple task definitions with the same open network port to the same node (this also happens within the EC2 flavor of ECS).

### Let's be constant

Before setting up our cloud resources, we begin by setting some variables that we’ll use later on throughout our Pulumi program.

We'll first set up our configuration settings in our command line:

```bash
pulumi config set aws:region us-east-1
pulumi config set numberNodes 2
```

The first tells Pulumi which region to deploy the resources to (and we’ll also use it when setting up our nodes and CloudWatch logging). The second tells us how many nodes to create, and we’ll need at least two to allow ECS to perform a rolling deployment.

Since we’re using a third-party compute provider to prove that ECS can deploy the containers to non-AWS infrastructure, we need to provide an API token. In this example, we’ll add it to the config, but you should read our [Setup Guide](https://www.pulumi.com/registry/packages/digitalocean/installation-configuration/) for more information on how to deploy.

To add your token to the config (as a secret), you should run the following command:

```bash
pulumi config set digitalocean:token XXXXXXXXXXXX --secret
```

Exchange `XXXXXXXXXXXX` for a personal access token located in the [Control Panel](https://cloud.digitalocean.com/account/api/tokens).

We'll use these to set variables in our code:

```typescript
import * as pulumi from "@pulumi/pulumi";

const awsConfig = new pulumi.Config("aws");
const awsRegion = awsConfig.get("region");

const projectConfig = new pulumi.Config();
const numberNodes = projectConfig.getNumber("numberNodes") || 2;
```

(notice that for the number of nodes, we’re setting a default value in case this configuration setting does not exist)

### Setting up IAM roles

We're going to need three IAM roles:

1. The first is for the AWS Systems manager. We’re going to attach two managed policies to this: one to enable its core functionality (`AmazonSSMManagedInstanceCore`) and the default EC2 role for ECS (`AmazonEC2ContainerServiceforEC2Role`).
1. The second is the ECS execution role, and to that, we’re going to attach the managed policy to allow other AWS services to run ECS tasks (`AmazonECSTaskExecutionRolePolicy`)
1. The final one is the Task role, and we’re going to add a custom policy to that role to allow us to push logs from the nodes to CloudWatch.

```typescript
const ssmRole = new aws.iam.Role("ssmRole", {
  assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal(
    aws.iam.Principals.SsmPrincipal
  ),
});

new aws.iam.RolePolicyAttachment("rpa-ssmrole-ssminstancecore", {
  policyArn: aws.iam.ManagedPolicy.AmazonSSMManagedInstanceCore,
  role: ssmRole,
});

new aws.iam.RolePolicyAttachment("rpa-ssmrole-ec2containerservice", {
  policyArn: aws.iam.ManagedPolicy.AmazonEC2ContainerServiceforEC2Role,
  role: ssmRole,
});

const executionRole = new aws.iam.Role("taskExecutionRole", {
  assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal(
    aws.iam.Principals.EcsTasksPrincipal
  ),
});

new aws.iam.RolePolicyAttachment("rpa-ecsanywhere-ecstaskexecution", {
  role: executionRole,
  policyArn: aws.iam.ManagedPolicy.AmazonECSTaskExecutionRolePolicy,
});

const taskRole = new aws.iam.Role("taskRole", {
  assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal(
    aws.iam.Principals.EcsTasksPrincipal
  ),
});

new aws.iam.RolePolicy("taskRolePolicy", {
  role: taskRole.id,
  policy: {
    Version: "2012-10-17",
    Statement: [
      {
        Effect: "Allow",
        Action: [
          "ssmmessages:CreateControlChannel",
          "ssmmessages:CreateDataChannel",
          "ssmmessages:OpenControlChannel",
          "ssmmessages:OpenDataChannel",
        ],
        Resource: "*",
      },
      {
        Effect: "Allow",
        Action: ["logs:DescribeLogGroups"],
        Resource: "*",
      },
      {
        Effect: "Allow",
        Action: [
          "logs:CreateLogStream",
          "logs:CreateLogGroup",
          "logs:DescribeLogStreams",
          "logs:PutLogEvents",
        ],
        Resource: "*",
      },
    ],
  }
});
```

### Deploying the ECS cluster and node infrastructure

Next, we’re going to set up the System Manager activation, which provides an Id and a code that lets our nodes connect to the cluster. We’ll set them up at the same time as the CloudWatch log group that we’ll push application logs to later on:

```typescript
const ssmActivation = new aws.ssm.Activation("ecsanywhere-ssmactivation", {
  iamRole: ssmRole.name,
  registrationLimit: numberNodes,
});

const cluster = new aws.ecs.Cluster("cluster");

export const clusterName = cluster.name;

const logGroup = new aws.cloudwatch.LogGroup("logGroup");
```

We’re using the `ssmRole` we created earlier to allow the Systems Manager to do this. You’ll also notice we’re exporting the clusterName here. We will use this to tidy up later on when we tear down our infrastructure.

When we create the nodes, we will run an AWS bash script provided as part of the setup and pass it into the resource as userData. In this script, we pass in the cluster name, the activation id, the activation code, and the AWS region where the cluster will be deployed.

```typescript
const userData = pulumi
  .all([ssmActivation.activationCode, ssmActivation.id, cluster.name])
  .apply(
    ([activationCode, activationId, clusterName]) => `#!/bin/bash
# Download the ecs-anywhere install Script
curl -o "ecs-anywhere-install.sh" "https://amazon-ecs-agent.s3.amazonaws.com/ecs-anywhere-install-latest.sh" && sudo chmod +x ecs-anywhere-install.sh

# (Optional) Check integrity of the shell script
curl -o "ecs-anywhere-install.sh.sha256" "https://amazon-ecs-agent.s3.amazonaws.com/ecs-anywhere-install-latest.sh.sha256" && sha256sum -c ecs-anywhere-install.sh.sha256

# Run the install script
sudo ./ecs-anywhere-install.sh \
    --cluster ${clusterName} \
    --activation-id ${activationId} \
    --activation-code ${activationCode} \
    --region ${awsRegion}
`
  );
```

This next section of code deploys the VMs.

We’re going to create a tag that attaches the nodes to a load balancer. Next, we’ll create the VMs and assign the tag. Finally, we’ll deploy the load balancer and assign the same tag to route traffic to the nodes. We'll also take the IP address of the load balancer and mark it as an output so we have something we can either use in a browser or call with curl to ensure that our deployment has worked.

In the end, we’re going to output the load balancer IP address so we have something we can either use in a browser or call with curl to ensure that our deployment has worked.

```typescript
const loadBalancerTag = new digitalocean.Tag("lb");

for(let i = 1; i <= numberNodes; i++) {
  new digitalocean.Droplet(`droplet-${i}`, {
    region: digitalocean.Regions.NYC1,
    size: "s-1vcpu-2gb",
    image: "ubuntu-20-04-x64",
    userData: userData,
    tags: [loadBalancerTag.id]
  });
}

const lb = new digitalocean.LoadBalancer("lb", {
  region: digitalocean.Regions.NYC1,
  forwardingRules: [{
    entryPort: 80,
    entryProtocol: digitalocean.Protocols.HTTP,
    targetPort: 80,
    targetProtocol: digitalocean.Protocols.HTTP
  }],
  healthcheck: {
    port: 80,
    protocol: digitalocean.Protocols.HTTP,
    path: "/"
  },
  dropletTag: loadBalancerTag.name
});

export const ip = lb.ip;
```

The last part of the example will be familiar to anyone using ECS as a container scheduler: setting up the container repository, describing the task definition, and creating the service. The difference is that we use new compatibility in the task definition and a new launch type in the service - `EXTERNAL`. This tells ECS to push the container and start them on the external nodes.

```typescript
const repo = new awsx.ecr.Repository("app");

const image = repo.buildAndPushImage("./app");

const taskDefinition = pulumi.all([image, logGroup.name, logGroup.namePrefix]).apply(
  ([img, logGroupName, nameprefix]) =>
    new aws.ecs.TaskDefinition("taskdefinition", {
      family: "ecs-anywhere",
      requiresCompatibilities: ["EXTERNAL"],
      taskRoleArn: taskRole.arn,
      executionRoleArn: executionRole.arn,
      containerDefinitions: JSON.stringify([
        {
          name: "app",
          image: img,
          cpu: 256,
          memory: 256,
          essential: true,
          portMappings: [
            {
              containerPort: 80,
              hostPort: 80
            },
          ],
          logConfiguration: {
            logDriver: "awslogs",
            options: {
              "awslogs-group": logGroupName,
              "awslogs-region": awsRegion,
              "awslogs-stream-prefixs": nameprefix
            }
          }
        },
      ]),
    })
);

const service = new aws.ecs.Service("service", {
    launchType: "EXTERNAL",
    taskDefinition: taskDefinition.arn,
    cluster: cluster.id,
    desiredCount: numberNodes - 1,
  }
);
```

Now you can run `pulumi up`, and once it’s all deployed, run `curl ${pulumi stack output ip}`.

If you want to update the Dockerfile or the Node.js application, run `pulumi up` again. You’ll see the new container deployed. Then you can run `curl ${pulumi stack output ip}` again to see the new response.

Finally, when you want to destroy the infrastructure, there is an additional step before running the usual `pulumi destroy`. This is because the nodes are registered to AWS Systems Manager and the ECS cluster as part of the node setup and happen outside of the Pulumi stack.

Run the following in your command line (you’ll need to install [jq](https://stedolan.github.io/jq/) for this to work):

```bash
aws ssm describe-instance-information | jq ".InstanceInformationList | .[] | .InstanceId" | grep "mi-" | xargs -L 1 aws ssm deregister-managed-instance --instance-id

# Cleanup ECS resources
aws ecs list-container-instances --cluster ${pulumi stack output clusterName} | jq ".containerInstanceArns | .[]" | xargs -L 1 aws ecs deregister-container-instance --cluster ${pulumi stack output clusterName} --force --container-instance

# Refresh Pulumi stack
pulumi refresh -y
```

And then you can tear down all your infrastructure with the usual `pulumi destroy`.

You can see this code in its entirety in our [examples repository on GitHub](https://github.com/pulumi/examples/tree/master/aws-ts-ecs-anywhere).

## Summary

ECS Anywhere is an excellent addition to Amazon Web Services’ suite of container orchestration services. I can see many companies using it to run containers in their private infrastructure but don’t necessarily have the means, know-how, or drive to set up and run their Kubernetes cluster or another such tool.

We’ve shown you how to set up your ECS cluster to use external nodes, build and deploy the cluster and application and see for yourself how easy it is to deploy subsequent changes. Pulumi makes it simple to create container images and provision and manage cloud infrastructure on any cloud using familiar programming languages, including TypeScript, Python, Go, and .NET. Cloud engineers can manage container images, ECR registries, and multi-cloud deployments within the same infrastructure definition.
