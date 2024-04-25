---
title: "Creating a Python AWS Application Using Flask and Redis"
date: 2020-08-13T15:06:26-07:00
meta_desc: A tutorial on how to create a Python AWS application using Flask, Redis, and Pulumi.
meta_image: meta.png
authors: ["vova-ivanov"]
tags: ["aws", "python", "containers", "docker", "ecs"]
---

*Meet Vova Ivanov---one of the Pulumi summer interns. He'll be writing about his experiences learning Pulumi while modernizing a web app and its underlying infrastructure.*

<!--more-->

I've recently started developing with Pulumi, and have begun to explore its inner workings and mechanisms. I decided to construct a production-level application and to document each step that I take and my progress as I go along.

This blog post recreates the existing [Typescript voting app example](https://www.pulumi.com/docs/tutorials/aws/aws-ts-voting-app/) step by step in Python with Flask as the frontend and Redis as the backend. In future blog posts, we will explore how to change the front and backends, how to upgrade the app with additional AWS services, and migrating from one cloud provider to another.

The first step is to clone the [Typescript voting app example](https://www.pulumi.com/docs/tutorials/aws/aws-ts-voting-app/). We'll use a sparse clone to copy only the `aws-ts-voting-app` directory.

```bash
$ mkdir examples && cd examples
$ git init
$ git remote add origin -f https://github.com/pulumi/examples/
$ git config core.sparseCheckout true
$ echo aws-ts-voting-app >> .git/info/sparse-checkout
$ git pull origin master
```

The next step is to create a new directory and initialize a Pulumi project with `pulumi new aws-python`.

```bash
$ mkdir aws-py-voting-app && cd aws-py-voting-app
$ pulumi new aws-python
```

Since we won't be modifying the application's frontend, we simply copy the frontend/ folder from the example into our directory.

```bash
$ cp -r aws-ts-voting-app/frontend/ aws-py-voting-app/frontend
```

The `requirements.txt` file lists the libraries that the project depends on. We will need to add the following:

```
pulumi-docker>=2.0.0,<3.0.0
```

The biggest difference between our project and the example is the code describing the cloud infrastructure we want to create. Instead of an `index.ts` file, the project uses a `__main__.py` file. The first few lines of the file will indicate which libraries to import and describe a pair of configuration options used by the application.

```python
import json
import pulumi
import pulumi_aws as aws
import pulumi_docker as docker

config = pulumi.Config()
redis_password = config.require("redis-password")
redis_port = 6379
```

After setting up the imports and configurations, we create an Elastic Container Service Cluster.
A Cluster represents a group of tasks and services that work together for a certain purpose. In
this instance, the purpose is to provide users with a voting application.

```python
app_cluster = aws.ecs.Cluster("app-cluster")
```

To allow different tasks within our cluster to communicate, we create a Virtual Private
Cloud and an associated subnet.

```python
app_vpc = aws.ec2.Vpc("app-vpc",
    cidr_block="172.31.0.0/16",
    enable_dns_hostnames=True)

app_vpc_subnet = aws.ec2.Subnet("app-vpc-subnet",
    cidr_block="172.31.32.0/20",
    vpc_id=app_vpc)
```

A gateway and routing table are needed to allow the VPC to communicate with the Internet.
Once created, we associate the routing table with our VPC.

```python
app_gateway = aws.ec2.InternetGateway("app-gateway",
    vpc_id=app_vpc.id)

app_routetable = aws.ec2.RouteTable("app-routetable",
    routes=[
        {
            "cidr_block": "0.0.0.0/0",
            "gateway_id": app_gateway.id,
        }
    ],
    vpc_id=app_vpc.id)

app_routetable_association = aws.ec2.MainRouteTableAssociation("app_routetable_association",
    route_table_id=app_routetable.id,
    vpc_id=app_vpc)
```

To control traffic flow between applications running inside our VPC, we create a security group.

```python
app_security_group = aws.ec2.SecurityGroup("security-group",
	vpc_id=app_vpc.id,
	description="Enables HTTP access",
    ingress=[{
		'protocol': 'tcp',
		'from_port': 0,
		'to_port': 65535,
		'cidr_blocks': ['0.0.0.0/0'],
    }],
    egress=[{
		'protocol': '-1',
		'from_port': 0,
		'to_port': 0,
		'cidr_blocks': ['0.0.0.0/0'],
    }])
```

To start our services, we need to create an Identity and Access Management (IAM) role,
and attach execution permissions to it.

```python
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

exec_policy_attachment = aws.iam.RolePolicyAttachment("app-exec-policy", role=app_exec_role.name,
	policy_arn=aws.iam.ManagedPolicy.AMAZON_ECS_TASK_EXECUTION_ROLE_POLICY)
```

Likewise, our ECS service will need to have a task role to manage it, along with its own set
of permissions.

```python
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

task_policy_attachment = aws.iam.RolePolicyAttachment("app-access-policy", role=app_task_role.name,
	policy_arn=aws.iam.ManagedPolicy.AMAZON_ECS_FULL_ACCESS)
```

An Elastic Container Registry Repository stores the application Docker images that we want
to run. The life cycle policy automatically removes the oldest untagged image that we uploaded.

```python
app_ecr_repo = aws.ecr.Repository("app-ecr-repo",
    image_tag_mutability="MUTABLE")

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

With the basic infrastructure in place, we can begin to set up the application itself. First,
we will start with the Redis backend.

We need to create a target
group, a balancer, and a listener to allow Redis to communicate with the other services in our VPC, w

```python
redis_targetgroup = aws.lb.TargetGroup("redis-targetgroup",
	port=redis_port,
	protocol="TCP",
	target_type="ip",
    stickiness= {
        "enabled": False,
        "type": "lb_cookie",
    },
	vpc_id=app_vpc.id)

redis_balancer = aws.lb.LoadBalancer("redis-balancer",
    load_balancer_type="network",
    internal= False,
    security_groups=[],
	subnets=[app_vpc_subnet.id])

redis_listener = aws.lb.Listener("redis-listener",
	load_balancer_arn=redis_balancer.arn,
	port=redis_port,
    protocol="TCP",
	default_actions=[{
		"type": "forward",
		"target_group_arn": redis_targetgroup.arn
	}])
```

Every service running within ECS requires a task definition, specifying what hardware, internet,
and container settings it will use.

```python
redis_task_definition = aws.ecs.TaskDefinition("redis-task-definition",
    family="redis-task-definition-family",
    cpu="256",
    memory="512",
    network_mode="awsvpc",
    requires_compatibilities=["FARGATE"],
    execution_role_arn=app_exec_role.arn,
    task_role_arn=app_task_role.arn,
    container_definitions=json.dumps([{
        "name": "redis-container",
        "image": "redis:alpine",
        "memory": 512,
        "essential": True,
        "portMappings": [{
            "containerPort": redis_port,
            "hostPort": redis_port,
            "protocol": "tcp"
        }],
        "command": ["redis-server", "--requirepass", redis_password],
	}]))
```

Now that we have our task definition blueprint ready, we can launch a service using it. An
endpoint is created to hold information needed to connect the backend with the frontend.

```python
redis_service = aws.ecs.Service("redis-service",
	cluster=app_cluster.arn,
    desired_count=1,
    launch_type="FARGATE",
    task_definition=redis_task_definition.arn,
    wait_for_steady_state=False,
    network_configuration={
		"assign_public_ip": "true",
		"subnets": [app_vpc_subnet.id],
		"security_groups": [app_security_group.id]
	},
    load_balancers=[{
		"target_group_arn": redis_targetgroup.arn,
		"container_name": "redis-container",
		"container_port": redis_port,
	}],
    opts=pulumi.ResourceOptions(depends_on=[redis_listener]),
)

redis_endpoint = {"host": redis_balancer.dns_name, "port": redis_port}
```

The Redis backend is complete, and now all that's left is to create the Flask frontend.

A similar set of a target group, balancer, and listener is created for the frontend. Unlike
Redis, Flask will serve as the webpage and, as such, needs to receive its data from port 80.

```python
flask_targetgroup = aws.lb.TargetGroup("flask-targetgroup",
	port=80,
	protocol="TCP",
	target_type="ip",
    stickiness= {
        "enabled": False,
        "type": "lb_cookie",
    },
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
	default_actions=[{
		"type": "forward",
		"target_group_arn": flask_targetgroup.arn
	}])
```

The application is built into a Docker image and pushed to our ECR repository we created
earlier.

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
    build="./frontend",
    skip_push=False,
    registry=app_registry
)
```

A task definition is created for the frontend; this time, using the flask image that we
built. The redis endpoint is passed in as a group of environment variables, informing our
app of our database's host and port values.

```python
flask_task_definition = aws.ecs.TaskDefinition("flask-task-definition",
    family="frontend-task-definition-family",
    cpu="256",
    memory="512",
    network_mode="awsvpc",
    requires_compatibilities=["FARGATE"],
    execution_role_arn=app_exec_role.arn,
    task_role_arn=app_task_role.arn,
    container_definitions=pulumi.Output.all(flask_image.image_name, redis_endpoint).apply(lambda args: json.dumps([{
        "name": "flask-container",
        "image": args[0],
        "memory": 512,
        "essential": True,
        "portMappings": [{
            "containerPort": 80,
            "hostPort": 80,
            "protocol": "tcp"
        }],
        "environment": [
            { "name": "REDIS", "value": args[1]["host"] },
            { "name": "REDIS_PORT", "value": str(args[1]["port"]) },
            { "name": "REDIS_PWD", "value": redis_password },
        ],
    }])))
```

The service for our Flask frontend is launched. It can receive requests from the Internet,
process them, and change the Redis database accordingly.

```python
flask_service = aws.ecs.Service("flask-service",
	cluster=app_cluster.arn,
    desired_count=1,
    launch_type="FARGATE",
    task_definition=flask_task_definition.arn,
    wait_for_steady_state=False,
    network_configuration={
		"assign_public_ip": "true",
		"subnets": [app_vpc_subnet.id],
		"security_groups": [app_security_group.id]
	},
    load_balancers=[{
		"target_group_arn": flask_targetgroup.arn,
		"container_name": "flask-container",
		"container_port": 80,
	}],
    opts=pulumi.ResourceOptions(depends_on=[flask_listener]),
)
```

To connect to our application, we export the DNS name of the Flask balancer, and
open it in a browser window.

```python
pulumi.export("app-url", flask_balancer.dns_name)
```

In this example, I showed how straightforward it is to convert infrastructure code defined in TypeScript to one defined in Python. Teams often choose to standardize on one language and Pulumi expands that choice, allowing them to standardize on one language for the frontend, the backend, and the infrastructure.

Next week, I'll show how to modernize the application by changing the frontend from Flask to Django, and swapping out the database from Redis to Amazon RDS---using Pulumi to stand up new resources as I go.

The full code for the blog post can be [found on github.](https://github.com/pulumi/examples/tree/master/aws-py-voting-app)
