---
title: "Reduce Cloud Costs with EC2 ARM Instances"
date: 2021-01-26
meta_desc: "The cost of running cloud based infrastructure can make or break a deployment. You can use ARM instances to decrease the cloud spend and remain in budget."
meta_image: arm.png
authors:
    - sophia-parafina
tags:
    - AWS
    - ec2
    - virtual-machines
---

Whether you're migrating to the cloud or have existing infrastructure, cloud spend can be a significant barrier to your success. Too small of a budget could prevent your organization from meeting your performance metrics. You can use different strategies to reduce cloud spend, such as using [Spot Instances](https://aws.amazon.com/ec2/spot/), which cost less than On-Demand Instances or scaling your infrastructure based on peak usage times.

With the addition of Graviton2 based EC2 Instances, AWS offers an on-demand alternative for decreasing cloud spend. Both Amazon and [independent testing](https://www.anandtech.com/show/15578/cloud-clash-amazon-graviton2-arm-against-intel-and-amd/9) demonstrated that the general-purpose [M6g instance](https://aws.amazon.com/ec2/instance-types/m6/) delivered up to a 40% gain of price/performance compared to Intel m5.large instances. In addition to the M6g general-purpose instance, AWS offers instances general-purpose burstable (T4g), compute-optimized (C6g), and memory-optimized (R6g) EC2 instances.

<!--more-->

## Deploying Infrastructure with ARM

Building infrastructure with ARM instances is straightforward. You can reuse code and substitute ARM instances and containers for Intel-based components. Check out this example that deploys a VPC with EC2 container instances. To get started, you can clone the repository with the Pulumi CLI.

```bash
$ pulumi new https://github.com/pulumi/examples/tree/master/aws-py-ecs-instances-autoapi/py-ecs-instance

This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name: (aws-py-ecs-instances-autoapi)
project description: (A container running in AWS ECS Container Instance, using Python infrastructure as code)
Created project 'aws-py-ecs-instances-autoapi'

Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
stack name: (dev)
Created stack 'dev'

Creating virtual environment...
Finished creating virtual environment
Updating pip, setuptools, and wheel in virtual environment...
…
Successfully installed arpeggio-1.10.1 attrs-20.3.0 dill-0.3.3 grpcio-1.35.0 parver-0.3.1 protobuf-3.14.0 pulumi-2.18.1 pulumi-aws-3.24.0 pyyaml-5.4.1 semver-2.13.0 six-1.15.0
Finished installing dependencies
Your new project is ready to go! ✨

To perform an initial deployment, run 'pulumi up'
```

Because this example is written in Python, the CLI will automatically configure your virtual environment and install the Python packages listed in `requirements.txt.` You can now edit __main__.py to use the M6g instance and an ARM version of the nginx container. Dockerhub has many [ARM images](https://hub.docker.com/search?type=image&architecture=arm%2Carm64) for popular applications, as well as for base images. We'll use the [arm64v8/nginx](https://hub.docker.com/r/arm64v8/nginx/) image in this example.

Edit this parts of __main__.py to use an ARM AMI

```python
# Find an "ECS optimized" AMI to use for the EC2 container instances.
ecs_instance_ami = aws.get_ami(
    most_recent="true",
    owners=["amazon"],
    filters=[
        {
            "name": "name",
            "values": ["amzn2-ami-ecs-hvm-*-arm64-*"]
        }
    ]
)
```

and this part to specify the instance type:

```python
# create launch configuration
launch_config = aws.ec2.LaunchConfiguration(
    "launch-config",
    image_id=ecs_instance_ami.id,
    instance_type="m6g.medium",
    iam_instance_profile=ecs_instance_profile.name, # needed to give instance authority to join the ECS cluster.
    user_data=user_data, # Required so instance knows to connect to the cluster created below.
)
```

Finally, replace the image with the ARM image from Dockerhub:

```python
# Task definition for creating our containers.
task_def = aws.ecs.TaskDefinition(
    "my-app",
    family="ec2-task-definition",
    cpu="256",
    memory="512",
    network_mode="awsvpc",
    requires_compatibilities=["EC2"],
    execution_role_arn=task_execution_role.arn,  # Needed so it has permission to launch tasks on the cluster.
    container_definitions=json.dumps([{
		"name": "my-app",
		"image": "arm64v8/nginx", # a simple nginx example
		"portMappings": [{
			"containerPort": 80,
			"hostPort": 80,
			"protocol": "tcp"
		}]
	}]),
    opts=pulumi.ResourceOptions(depends_on=[cluster])
)
```

Save your changes, and we're ready to go to the next step.

Before spinning up our example, we need to set the AWS region we want to use and the `autoscalingGroupSize` to limit the number of instances.

```bash
$ pulumi config set aws:region us-west-2
$ pulumi config set cfg:autoscalingGroupSize 1
```

Once those are configured, run `pulumi up` to bring up your infrastructure. You'll see similar output, including the URL for your deployment.

```bash
View Live: https://app.pulumi.com/spara/aws-py-ecs-instances-autoapi/dev/updates/1

     Type                             Name                              Status
 +   pulumi:pulumi:Stack              aws-py-ecs-instances-autoapi-dev  created
 +   ├─ aws:iam:Role                  task-execution-role               created
 +   ├─ aws:ec2:SecurityGroup         nginx-sg                          created
 +   ├─ aws:iam:Role                  ecs-instance-role                 created
 +   ├─ aws:lb:TargetGroup            app-tg                            created
 +   ├─ aws:iam:RolePolicyAttachment  task-excution-policy-attach       created
 +   ├─ aws:iam:RolePolicyAttachment  ecs-instance-policy-attach        created
 +   ├─ aws:iam:InstanceProfile       ecs-iam-instance-profile          created
 +   ├─ aws:ec2:LaunchConfiguration   launch-config                     created
 +   ├─ aws:lb:LoadBalancer           load-balancer                     created
 +   ├─ aws:autoscaling:Group         auto-scaling                      created
 +   ├─ aws:ecs:CapacityProvider      capacity-provider                 created
 +   ├─ aws:ecs:Cluster               cluster                           created
 +   ├─ aws:ecs:TaskDefinition        my-app                            created
 +   ├─ aws:lb:Listener               web                               created
 +   └─ aws:ecs:Service               my-task-runner                    created

Outputs:
    NOTE: "You may have to wait a minute for AWS to spin up the service. So if the URL throws a 503 error, try again after a bit."
    app_url: "http://load-balancer-7aedaa4-1557043631.us-west-2.elb.amazonaws.com"

Resources:
    + 16 created

Duration: 2m30s
```

## What's Next?

Before jumping to the next thing, let's review what we've done. Using infrastructure as code enables changing your infrastructure as new technology becomes available. You can experiment rapidly to see if this configuration can meet your performance metrics and remain within your cloud spend budget. Blue/green deployment is straightforward because you are just swapping components on a known and proven infrastructure. These are just some of the advantages of using infrastructure as code.

So what is the next step? In a future article, well demonstrate how to build your own ARM-based container images using Docker's `buildx` CLI plugin. Until then, you can learn more about Pulumi and infrastructure as code with our [Getting Started]({{< relref "/docs/get-started" >}}) tutorials.
