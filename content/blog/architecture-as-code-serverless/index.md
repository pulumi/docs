---
title: "Architecture as Code: Serverless"
date: 2020-04-28
meta_desc: "Serverless can benefit from reusable resources created by infrastructure as code."
meta_image: serverless.png
authors:
    - sophia-parafina
tags:
    - serverless
---

In this fourth installment of Architecture as Code series, we’ll take a look at serverless, an architectural pattern that has quickly gained popularity among cloud practitioners. There are two reasons why serverless usage has proliferated: a cost-saving pay as you go model and elasticity that goes from zero to as many as needed to complete the task without managing servers.

<!--more-->

## Overview

Serverless is a pattern for building services without having to manage servers. You write a service and deploy it on infrastructure managed by a cloud service provider. Serverless apps can be either a simple function invoked by an event or an application in a container. They are typically ephemeral, where the application runs within a fixed time or until it completes the task. Managed implementations such as AWS Lambda and Fargate, Azure Functions, and Google Cloud Run and Cloud Functions charge for the service only when it’s invoked and create instances, or workers, based on demand.

Developers can write the application in any language that the service provider supports. That means developers can choose the language that best meets the needs of their application. For example, a compiled application may respond more quickly than a scripting language. Serverless applications can be either synchronous or asynchronous, depending on the task.

A common feature of serverless architecture is a REST interface which maps HTTP operations such as GET, PUT, POST, and DELETE to functions. A REST interface simplifies implementing REST interfaces for functions and applications. AWS offers API Gateway for building REST interfaces, while Azure and Google Cloud have out of the box solutions.

Let’s take a look at examples where we can apply Architecture as Code to serverless.

## Reusing resources

While serverless simplifies and reduces management overhead for deploying functions and containers, ancillary services also need to be configured. For example, a production deployment requires creating clusters, security groups, load balancers, and IAM policies. The following Python script creates resources that can be imported into `__main__.py`, which deploys the function or container. It ensures that each serverless application uses a vetted set of resources that can be replicated for every deployment.

```python
from pulumi import export, ResourceOptions
import pulumi_aws as aws
import json

# Create an ECS cluster to run a container-based service.
cluster = aws.ecs.Cluster('cluster')

# Read back the default VPC and public subnets, which we will use.
default_vpc = aws.ec2.get_vpc(default='true')
default_vpc_subnets = aws.ec2.get_subnet_ids(vpc_id=default_vpc.id)

# Create a SecurityGroup that permits HTTP ingress and unrestricted egress.
group = aws.ec2.SecurityGroup('web-secgrp',
	vpc_id=default_vpc.id,
	description='Enable HTTP access',
	ingress=[{
		'protocol': 'tcp',
		'from_port': 80,
		'to_port': 80,
		'cidr_blocks': ['0.0.0.0/0'],
	}],
  	egress=[{
		'protocol': '-1',
		'from_port': 0,
		'to_port': 0,
		'cidr_blocks': ['0.0.0.0/0'],
	}]
)

# Create a load balancer to listen for HTTP traffic on port 80.
alb = aws.lb.LoadBalancer('app-lb',
	security_groups=[group.id],
	subnets=default_vpc_subnets.ids
)

atg = aws.lb.TargetGroup('app-tg',
	port=80,
	protocol='HTTP',
	target_type='ip',
	vpc_id=default_vpc.id
)

wl = aws.lb.Listener('web',
	load_balancer_arn=alb.arn,
	port=80,
	default_actions=[{
		'type': 'forward',
		'target_group_arn': atg.arn
	}]
)

# Create an IAM role that can be used by our service's task.
role = aws.iam.Role('task-exec-role',
	assume_role_policy=json.dumps({
		'Version': '2008-10-17',
		'Statement': [{
			'Sid': '',
			'Effect': 'Allow',
			'Principal': {
				'Service': 'ecs-tasks.amazonaws.com'
			},
			'Action': 'sts:AssumeRole',
		}]
	})
)

rpa = aws.iam.RolePolicyAttachment('task-exec-policy',
	role=role.name,
	policy_arn='arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy'
)
```

To learn more about creating [reusable components]({{< prelref "/docs/intro/concepts/programming-model#components" >}}), read about Pulumi's programming model, which shows how to author components.

## Polyglot applications

This example shows how to deploy multiple functions in Google Cloud Functions. Note that we have one function written in Python and another in Go. The code that deploys the function is written in python and creates a Bucket to hold the function code and deploys both functions in the same script.

```python
from pulumi_gcp import storage, cloudfunctions
from pulumi import export, asset

bucket = storage.Bucket("bucket")

py_bucket_object = storage.BucketObject(
    "python-zip",
    bucket=bucket.name,
    source=asset.AssetArchive({
        ".": asset.FileArchive("./pythonfunc")
    }))

py_function = cloudfunctions.Function(
    "python-func",
    source_archive_bucket=bucket.name,
    runtime="python37",
    source_archive_object=py_bucket_object.name,
    entry_point="handler",
    trigger_http="true",
    available_memory_mb=128,
)

export("python_endpoint", py_function.https_trigger_url)

go_bucket_object = storage.BucketObject(
    "go-zip",
    bucket=bucket.name,
    source=asset.AssetArchive({
        ".": asset.FileArchive("./gofunc")
    }))

go_function = cloudfunctions.Function(
    "go-func",
    source_archive_bucket=bucket.name,
    runtime="go111",
    source_archive_object=go_bucket_object.name,
    entry_point="Handler",
    trigger_http="true",
    available_memory_mb=128,
)

export("go_endpoint", go_function.https_trigger_url)
```

The [full example](https://github.com/pulumi/examples/tree/master/gcp-ts-serverless-raw) is available on Github.

## Cold Starts

Despite the many advantages of serverless, one of the challenges of serverless is latency, more commonly known as “cold starts.” There are several ways to lessen the impact of cold starts, including:

- Invoking a pool of workers - a process known as 'warming'.
- Provisioned concurrency - workers that are always warm and dedicated to a specific function.
- Dynamic concurrency - workers configured to autoscale as needed.
- Scheduled profile - warming is applied during peak use.
- Autoscaling-based utilization - adds workers as service utilization increases.

Deploying infrastructure with code lets you implement these [strategies]({{< prelref "/blog/aws-lambda-provisioned-concurrency-no-cold-starts" >}}) based on your application requirements. The code snippet below is an example of provisioned concurrency; a fully [worked example](https://github.com/pulumi/examples/tree/master/aws-ts-serverless-raw) is available on Github.

```ts
// Read the config of whether to provision fixed concurrency for Lambda
const config = new pulumi.Config();
const provisionedConcurrentExecutions = config.getNumber("provisionedConcurrency");

// Create a Lambda function, using code from the `./app` folder.
const lambda = new aws.lambda.Function("mylambda", {
    runtime: aws.lambda.DotnetCore2d1Runtime,
    code: new pulumi.asset.AssetArchive({
        ".": new pulumi.asset.FileArchive(dotNetApplicationPublishFolder),
    }),
    timeout: 300,
    handler: dotNetApplicationEntryPoint,
    role: role.arn,
    publish: !!provisionedConcurrentExecutions, // Versioning required for provisioned concurrency
    environment: {
        variables: {
            "COUNTER_TABLE": counterTable.name,
        },
    },
}, { dependsOn: [policy] });

if (provisionedConcurrentExecutions) {
    const concurrency = new aws.lambda.ProvisionedConcurrencyConfig("concurrency", {
        functionName: lambda.name,
        qualifier: lambda.version,
        provisionedConcurrentExecutions,
    });
}
```

## Conclusion

Serverless is an attractive alternative to architectures that require hands-on management of servers. Despite this, it does not relieve you of the tasks needed to create and manage the ancillary resources needed for a modern application in production. Architecture as code enables you to declare resources and reuse them to ensure a standard and reproducible infrastructure. Also, you can deploy multiple functions and applications with a single Pulumi project, saving time and effort required to deploy them individually. Finally, you can tune your deployment strategies to overcome cold-start issues. [Pulumi tutorials]({{< prelref "/docs/tutorials" >}}) can get you started with serverless deployments.
