---
title: "Cloud Systems Part Three: Deploying to Amazon ECS"

date: 2021-12-28T14:52:42Z

draft: false

meta_desc: In this series, learn modern cloud engineering practices and tooling, continuing with deploying our containerized website to AWS Elastic Container Service!

authors:
    - kat-cosgrove

tags:
    - cloud-systems
    - aws
    - tutorials
    - docker
---

Cloud engineering is taking over software development. In a lot of ways, this is great; it allows us to build and deploy more complicated applications with less difficulty, and maintaining those applications becomes less troublesome too. We can release smaller updates more quickly than ever, ensuring that we can stay on top of feature requests and security issues. That said, the rise of cloud engineering has also introduced a lot of complexity in the form of dozens of services even within just one cloud provider. Figuring out where to start can be tough, so let’s take a practical tour! In this series, I’ll walk you through building a personal website and deploying it using modern cloud engineering practices.

<!--more-->

## Elastic Container Service

In the previous tutorial, we extended our personal website to use the Flask web framework, add server-side routing, and package everything up into a Docker container. It's still only running locally, though, and we want to deploy it. To do that, today we'll be learning to use Pulumi to deploy to Amazon's Elastic Container Service. If you completed part two of this series, we'll be picking up right where we left off. If you're just now joining me, you can get the completed code by forking and cloning [this repository](https://github.com/katcosgrove/cloud-systems-101).

## Prerequisites:

- An AWS Account

- [Pulumi account](https://app.pulumi.com)

- [Pulumi installed and configured for AWS](https://www.pulumi.com/docs/get-started/aws/begin/)

- [Docker](https://www.docker.com/products/docker-desktop)

- Python3

## Configuring Amazon ECS

[Amazon’s ECS (Elastic Container Service)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) is a tool used for container orchestration. It allows you to deploy containerized applications into a cluster, defined as tasks. We’re going to use Pulumi to define all of the necessary rules and settings to do this in a secure manner, then create our infrastructure and deploy the containerized website.

First, run `pulumi new python -y` to start a new Pulumi project if you don't already have one for this tutorial. From now on, we'll be working within `__main__.py`

```python
import json
import base64
import pulumi
import pulumi_aws as aws
import pulumi_docker as docker
```

First, we have our imports. We’re working with both AWS and Docker, so we need both of those Pulumi providers. Launch the virtual environment set up for you by Pulumi with `source venv/bin/activate` and run `pip3 install pulumi-aws pulumi-docker` to get both. If you want to make sure your dependencies are saved for later, you can run `pip3 freeze > requirements.txt` .

```python
app_cluster = aws.ecs.Cluster("app-cluster")

app_vpc = aws.ec2.Vpc("app-vpc",
    cidr_block="172.31.0.0/16",
    enable_dns_hostnames=True)

app_vpc_subnet = aws.ec2.Subnet("app-vpc-subnet",
    cidr_block="172.31.32.0/20",
    vpc_id=app_vpc.id)
```

In this codeblock, we're first creating our ECS cluster and naming it `app-cluster`. Then create a VPC (Virtual Private Cloud), and a subnet for it. VPCs are like miniature local networks, with subnets providing the addressing within that mini network. Using a VPC means you can wire up your system as you like it without worrying about how that network setup might collide with other AWS resources, since you define how that network can connect outward. If you've ever used Docker networking, you'll be familiar with the idea that an internal network is different than the external interface.

It is possible to use the default VPC here rather than defining one, but AWS networking is complex, so it's worth knowing that it is possible to define a custom VPC.

```python
app_gateway = aws.ec2.InternetGateway("app-gateway",
    vpc_id=app_vpc.id)

app_routetable = aws.ec2.RouteTable("app-routetable",
    routes=[
        aws.ec2.RouteTableRouteArgs(
            cidr_block="0.0.0.0/0",
            gateway_id=app_gateway.id,
        )
    ],
    vpc_id=app_vpc.id)

app_routetable_association = aws.ec2.MainRouteTableAssociation("app_routetable_association",
    route_table_id=app_routetable.id,
    vpc_id=app_vpc.id)
```

Next, we need a gateway and a route table. The gateway's job is to provide a target in that route table we just created and associated with our VPC. This allows our VPC to communicate with the public internet.

```python
app_security_group = aws.ec2.SecurityGroup("security-group",
    vpc_id=app_vpc.id,
    description="Enables HTTP access",
    ingress=[aws.ec2.SecurityGroupIngressArgs(
        protocol='tcp',
        from_port=80,
        to_port=80,
        cidr_blocks=['0.0.0.0/0'],
    )],
    egress=[aws.ec2.SecurityGroupEgressArgs(
        protocol='-1',
        from_port=0,
        to_port=0,
        cidr_blocks=['0.0.0.0/0'],
    )])
```

Just about everything you do in AWS requires a security group. The purpose of a security group is to control traffic, both inbound and outbound. This one enables HTTP access.

```python
# Creating an IAM role used by Fargate to execute all our services
app_exec_role = aws.iam.Role("app-exec-role",
    assume_role_policy="""{
        "Version": "2012-10-17",
        "Statement": [
        {
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": "ecs-tasks.amazonaws.com"
            },
            "Effect": "Allow",
            "Sid": ""
        }]
    }""")

# Attaching execution permissions to the exec role
exec_policy_attachment = aws.iam.RolePolicyAttachment("app-exec-policy", role=app_exec_role.name,
    policy_arn="arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy")

# Creating an IAM role used by Fargate to manage tasks
app_task_role = aws.iam.Role("app-task-role",
    assume_role_policy="""{
        "Version": "2012-10-17",
        "Statement": [
        {
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": "ecs-tasks.amazonaws.com"
            },
            "Effect": "Allow",
            "Sid": ""
        }]
    }""")

# Attaching execution permissions to the task role
task_policy_attachment = aws.iam.RolePolicyAttachment("app-access-policy", role=app_task_role.name,
    policy_arn=aws.iam.ManagedPolicy.AMAZON_ECS_FULL_ACCESS)
```

We're going to be using [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) to actually run our container. Fargate is a serverless compute platform designed for running containers without requiring you to provision and manage clusters of EC2 (Elastic Compute Cloud) instances. Since our website is containerized and very small, it's perfect for us. Services also require IAM roles, and in this case, we need to allow Fargate to execute our services and manage our tasks, so we create new roles for both and apply execution permissions to them.

In the context of Fargate, a task is a collection of containers, and a task definition tells AWS what needs to be running all at once in order to make an application run. The task definitions will be written later onm but first we need to define policies. It's important that these policies be created first, or the task definitions won't create correctly later on.

```python
# Creating storage space to upload a docker image of our app to
app_ecr_repo = aws.ecr.Repository("app-ecr-repo",
    image_tag_mutability="MUTABLE")

# Attaching an application life cycle policy to the storage
app_lifecycle_policy = aws.ecr.LifecyclePolicy("app-lifecycle-policy",
    repository=app_ecr_repo.name,
    policy="""{
        "rules": [
            {
                "rulePriority": 10,
                "description": "Remove untagged images",
                "selection": {
                    "tagStatus": "untagged",
                    "countType": "imageCountMoreThan",
                    "countNumber": 1
                },
                "action": {
                    "type": "expire"
                }
            }
        ]
    }""")
```

The last thing we need to do for our infrastructure before we can start deploying to it is create a repository on [Amazon ECR (Elastic Container Registry)](https://aws.amazon.com/ecr/) where our Docker image will live, then attach an application lifecycle policy to that repository. This makes sure that we expire and remove any untagged images in the repository, keeping things from geting clogged up.

## Deploying a Dockerized Flask Application to ECS

We're now ready to deploy our website and wire all of this up!

```python
flask_targetgroup = aws.lb.TargetGroup("flask-targetgroup",
    port=80,
    protocol="TCP",
    target_type="ip",
    vpc_id=app_vpc.id)

flask_balancer = aws.lb.LoadBalancer("flask-balancer",
    load_balancer_type="network",
    internal=False,
    security_groups=[],
    subnets=[app_vpc_subnet.id])

flask_listener = aws.lb.Listener("flask-listener",
    load_balancer_arn=flask_balancer.arn,
    port=80,
    protocol="TCP",
    default_actions=[aws.lb.ListenerDefaultActionArgs(
        type="forward",
        target_group_arn=flask_targetgroup.arn
    )])
```

First, we need to make it possible for our Flask application to communicate with the internet. That requires three pieces of configuration: a target group for port 80, a load balancer to spread out incoming requests and make sure our website doesn't get overwhelmed as easily, and a listener to forward public traffic to the defined target group. The target group is directed at the endpoint for the VPC we created earlier, defining the port as it is unknown until runtime.

```python
def get_registry_info(rid):
    creds = aws.ecr.get_credentials(registry_id=rid)
    decoded = base64.b64decode(creds.authorization_token).decode()
    parts = decoded.split(':')
    if len(parts) != 2:
        raise Exception("Invalid credentials")
    return docker.ImageRegistry(creds.proxy_endpoint, parts[0], parts[1])

app_registry = app_ecr_repo.registry_id.apply(get_registry_info)

flask_image = docker.Image("flask-dockerimage",
    image_name=app_ecr_repo.repository_url,
    build="./website",
    skip_push=False,
    registry=app_registry
)
```

A small helper function is required here. It's grabbing some of our AWS credentials, specificaly an authorization token, so that we can talk to the registry. Next, we build the Docker image for our website and push it to the repository we created in Amazon ECR earlier. Remember, the Dockerfile is in `./website`.

```python
flask_task_definition = aws.ecs.TaskDefinition("flask-task-definition",
    family="frontend-task-definition-family",
    cpu="256",
    memory="512",
    network_mode="awsvpc",
    requires_compatibilities=["FARGATE"],
    execution_role_arn=app_exec_role.arn,
    task_role_arn=app_task_role.arn,
    container_definitions=pulumi.Output.all(flask_image.image_name).apply(lambda args: json.dumps([{
        "name": "flask-container",
        "image": args[0],
        "memory": 512,
        "essential": True,
        "portMappings": [{
            "containerPort": 80,
            "hostPort": 80,
            "protocol": "tcp"
        }],
    }])))
```

We need a task definition for the Flask instance. AWS Fargate will be managing this for us, using the roles we defined earlier. We're also handing it a container definition, including the image name and a little bit of information about it, like the container and host ports.

```python
flask_service = aws.ecs.Service("flask-service",
    cluster=app_cluster.arn,
    desired_count=1,
    launch_type="FARGATE",
    task_definition=flask_task_definition.arn,
    wait_for_steady_state=False,
    network_configuration=aws.ecs.ServiceNetworkConfigurationArgs(
        assign_public_ip=True,
        subnets=[app_vpc_subnet.id],
        security_groups=[app_security_group.id]
    ),
    load_balancers=[aws.ecs.ServiceLoadBalancerArgs(
        target_group_arn=flask_targetgroup.arn,
        container_name="flask-container",
        container_port=80,
    )],
    opts=pulumi.ResourceOptions(depends_on=[flask_listener]),
)
```

Finally, we actually launch our website. We need to create a new service definition and hand it all of the resources we created earlier, beginning with the ECS cluster itself. It has the task definition, our network configurations, and our load balancers, and we make sure that this particular piece of code isn't executed until the listener we created to watch for traffic is online.

As a shortcut to finding our website, export the DNS name of our load balancer as an output from Pulumi as the last part of the program:

```python
pulumi.export("app-url", flask_balancer.dns_name)
```

We're ready to go! Set your AWS region in your terminal:

```bash
pulumi config set aws:region us-west-2
```

Then run `pulumi up` to watch it go! This time, we're going to see *way* more services created than before.

```bash
     Type                                  Name                        Status      Info
 +   pulumi:pulumi:Stack                   part-three-dev              created
 +   ├─ docker:image:Image                 flask-dockerimage           created
 +   ├─ aws:ec2:Vpc                        app-vpc                     created
 +   ├─ aws:ecs:Cluster                    app-cluster                 created
 +   ├─ aws:iam:Role                       app-exec-role               created
 +   ├─ aws:iam:Role                       app-task-role               created
 +   ├─ aws:ecr:Repository                 app-ecr-repo                created
 +   ├─ aws:iam:RolePolicyAttachment       app-exec-policy             created
 +   ├─ aws:iam:RolePolicyAttachment       app-access-policy           created
 +   ├─ aws:ecr:LifecyclePolicy            app-lifecycle-policy        created
 +   ├─ aws:ec2:Subnet                     app-vpc-subnet              created
 +   ├─ aws:ec2:InternetGateway            app-gateway                 created
 +   ├─ aws:ec2:SecurityGroup              security-group              created
 +   ├─ aws:lb:TargetGroup                 flask-targetgroup           created
 +   ├─ aws:ecs:TaskDefinition             flask-task-definition       created
 +   ├─ aws:lb:LoadBalancer                flask-balancer              created
 +   ├─ aws:ec2:RouteTable                 app-routetable              created
 +   ├─ aws:ec2:MainRouteTableAssociation  app_routetable_association  created
 +   ├─ aws:lb:Listener                    flask-listener              created
 +   └─ aws:ecs:Service                    flask-service               created

Outputs:
    app-url: "flask-balancer-a90d260-057e5a40e0267b63.elb.us-west-2.amazonaws.com"

Resources:
    + 20 created

Duration: 3m36s
```

Pulumi has created 20 resources for you, and helpfully returned the DNS address of your load balancer. I've snipped out the `diagnostics` section of this output for the sake of keeping things brief, but you will also see the step-by-step process Docker goes through building and running your image. Go to that URL after a couple of minutes, and your website is online!

We now have a functional, multi-page website with server-side routing, packaged up into a Docker container and deployed to a fully-configured AWS ECS cluster in just a couple hundred lines of Python, all without leaving the same repository our website is stored in. What if we want to be able to scale really large, though? Some resiliency would be nice. Stay tuned for the next blog for an introduction to Kubernetes, where we'll learn to deploy our website to Amazon's Elastic Kubermetes Service!
