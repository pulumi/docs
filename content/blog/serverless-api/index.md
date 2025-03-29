---
title: "Host your Python app for $1.28 a month"
date: 2025-01-29T00:00:00
updated: 2025-03-13
draft: false
meta_desc: Learn how to deploy a Flask API in an AWS Lambda container for just $1.28/month.
  Zero cost when idle, instant scaling – great for low-traffic apps.
meta_image: meta.png
authors:
  - adam-gordon-bell
tags:
  - python
  - serverless
social:
  twitter: >
    🚀 Transform your low-traffic Flask APIs into cost-efficient serverless apps! Package
    your entire REST API as a container, deploy to AWS Lambda, and pay $0 when idle.
    Simple local development, standard Flask patterns, and automatic scaling - all
    with minimal serverless expertise needed. 
  linkedin: >
    Ever wondered how to run web services for practically nothing? Adam shares an
    approach that's perfect for side projects and low-traffic applications.

    💡 The Challenge:
    Running services 24/7 that barely get used, but need to be reliable when called.
    🎯 The Solution:
    Package your entire web app as a container and run it on AWS Lambda!
    ✨ Why This Works:

    Zero cost when idle - literally $0!
    Instant activation when needed
    Pennies per month for low traffic
    Compatible with all web frameworks

    🛠️ The Beauty of Simplicity:
    No serverless expertise needed! Just:

    Write your code normally
    Containerize it
    Deploy to Lambda
    Add API Gateway
    You're live!

    💰 Real Cost Example:
    Flask app running with:

    512MB memory
    40,000 requests/month
    Total cost: $0.28/month (!!)
    Zero traffic = Zero cost
search:
  keywords:
    - Python
    - AWS
    - Lambda
    - AWS Lambda
    - Flask API
    - serverless apps
---

Most developers maintain at least one low-traffic service that still needs to be reliably available. It might be an internal reporting API that gets a few calls per hour or a side project with occasional use. While these services don't handle much load, they need to exist and remain responsive.

This creates an interesting hosting challenge: how do you maintain high availability for services that might only handle a few thousand requests per month? Traditional hosting approaches mean paying for 24/7 server time, even when your service sits idle.

These services present a unique challenge: they need to be reliable when called but get less than 500,000 requests a month.
<!--more-->
{{< youtube "cjLpOJn0B6g?rel=0" >}}

What if you could maintain these low-traffic services at zero cost when idle while ensuring they spring to life exactly when needed? This is where AWS Lambda's container support shines. While many developers think of Lambda primarily for individual functions, it's equally capable of hosting complete REST APIs that spring to life when needed.

Any web framework that can handle HTTP requests - Flask, FastAPI, Express, or something else - can be containerized and run on AWS Lambda at minimal cost. You pay only when your API is being called.

A Flask app on AWS Lambda with 512 MB memory and 40,000 requests per month would cost approximately **$0.28 per month** for the Lambda and another dollar total for egress and API gateway.

| **Provider**                   | **Approx. Cost / Month $**                   | **Notes**                                                                                                              |
|:-------------------------------|:--------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| AWS (Lambda + HTTP API)    | ~1.00–1.28                        | - 1–1.08 for ~12 GB data out (at $0.09/GB) + pennies for 40k requests. <br>- Free tier can cover Lambda itself. |
| Vercel (Pro Plan)          | 20–38 base plan                    | - 1M serverless function executions + generous bandwidth often included. <br>- 40k requests likely won’t add overages. |
| Railway                    | ~ 6.20 total                         | - 5 for a 512 MB container + 1.20 for 12 GB egress at 0.10/GB.                                              |
| Fly.io                     | ~5–6 total                        | - 5 for a small VM + 0.60–1.08 for 12 GB egress (typically 0.05–0.09/GB, region-dependent).             |

<div style="text-align: center; width: 100%; margin: 20px auto;">
    <figcaption>
       <i>Approximate Hosting Cost Numbers. <br/>Your use case may vary, but even 1 million requests/month is under $30 / month. Egress cost dominates</i>
    </figcaption>
</div>

What we'll cover:

1. [Why this approach is different](/blog/serverless-api/#why-this-approach-is-different)
2. [Building Flask application](/blog/serverless-api/#building-our-flask-application)
3. [Containerizing for Lambda](/blog/serverless-api/#containerizing-for-lambda)
4. [No special Lambda knowledge required](/blog/serverless-api/#no-special-lambda-knowledge-required)
5. [Infrastructure as code with Pulumi](/blog/serverless-api/#infrastructure-as-code-with-pulumi)
6. [Why I love this approach](/blog/serverless-api/#why-i-love-this-approach)
7. [Conclusion](/blog/serverless-api/#conclusion)

## **Why AWS Lambda is Ideal for Low-Traffic Python Apps**

"But Lambda means one function per REST endpoint, right?" While that's how serverless was initially positioned, the Lambda monolith approach here is a more straightforward pattern. Take any REST API service, package it as a container, put it in Lambda, and give it an entire HTTP route behind an IP, domain name, or API Gateway prefix. Done.

This approach gives you several benefits:

1. **Minimal Serverless Knowledge Required**: You don't need to be an expert in Lambda architecture or serverless patterns. If you can build a REST API and containerize it, you're ready to go.
2. **Standard Development Experience**: Write your API exactly as you would for any other hosting platform: no special frameworks, no Lambda-specific patterns to learn.
3. **Simple Local Development**: Run your container locally, and it will behave exactly like it will in production. No complex serverless emulation is needed.
4. **Zero Cost at Zero Usage**: Get all the cost benefits of serverless without restructuring your application.

The trade-off? Cold starts when Lambda spins up a new container instance. But this is often a worthwhile exchange for operational simplicity and zero-cost idle periods for low-traffic services.

Let me show you how to set this up. With some Pulumi Python code for setting up the Infra and some containerization code, you get an easy hosting solution.

{{< notes type="info" >}}

### Why containers?

Containers let us package everything—code, system dependencies, runtime—into one unit. Any HTTP service that fits in a container will work: Flask, Express, Rails, plus whatever system tools you need. Local testing? Just start the container. No Lambda-specific configuration is required.

{{< /notes >}}

## **Building our Flask application in Python**

Let's start with the fun part - writing some Python code, but I will keep it really simple. We'll build a simple Flask application that demonstrates why running a full web framework in Lambda makes sense.

Here's our starting point in `scripts/simple_server.py`

```python
from typing import Dict
from flask import flask, jsonify, request
from mangum import Mangum

# Create Flask app
app = Flask(__name__)

@app.route("/hello")
def hello() -> Dict[str, str]:
    return jsonify({"message": "Hello from Flask!"})

@app.route("/echo", methods=['POST'])
def echo() -> Dict[str, str]:
    data = request.get_json()
    return jsonify({"reversed": data['message'][::-1]})

# Create Lambda handler
lambda_handler = Mangum(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
```

Notice a few key things about this code:

1. **It's Just Flask**: No Lambda-specific code, no special frameworks. If you know Flask, you know how to modify this.
2. **Multiple Endpoints**: We have several routes demonstrating different HTTP methods and URL patterns.

## **Containerizing for Lambda**

To containerize our Flask app for Lambda, we'll start with a Dockerfile that meets AWS's requirements. The key is using the right base image and adapting our application to Lambda's runtime interface.

First, let's create our Dockerfile:

```dockerfile
FROM public.ecr.aws/lambda/python:3.12

# Set up working directory
WORKDIR /app
COPY scripts/simple_server.py scripts/
COPY scripts/simple_entrypoint.sh scripts/

# Install dependencies
RUN pip install --no-cache-dir \
    flask>=3.0.0 \
    mangum>=0.17.0

# Make entrypoint script executable
RUN chmod +x scripts/simple_entrypoint.sh

# Set environment variables
ENV FLASK_APP=scripts/simple_server.py
ENV PYTHONPATH=/app
ENV RUN_MODE=lambda
EXPOSE 3000

# Use our entrypoint script
ENTRYPOINT ["/app/scripts/simple_entrypoint.sh"]
```

Notice that:

1. We're using AWS's official Lambda Python base image. You can use your own base image and your Python package manager of choice, but starting with this base and `pip install` is the easiest.
2. The `${LAMBDA_TASK_ROOT}` is a special directory where Lambda expects to find your code
3. We're introducing a new file: `simple_entrypoint.sh`

## No special Lambda knowledge required

The beauty of everything covered so far is that it's just a container. You can work with it locally with Docker run, put it in Kubernetes, or run it in one of the [1000 places you can run containers](https://www.pulumi.com/blog/cursed-container-iceberg/). Lambda has some odd requirements about function calling that get in the way of this, but `simple_entrypoint.sh` saves the day:

```bash
#!/bin/bash

if [ "$RUN_MODE" = "local" ]; then
    echo "Starting in local mode..."
    exec python scripts/simple_server.py
else
    echo "Starting in Lambda mode..."
    exec python -m awslambdaric scripts.simple_server.lambda_handler
fi

```

All this means is that locally, you don't need to know about lambdas at all. If you supply `RUN_MODE=local` it runs the standard way you are used to:

```bash
#!/bin/bash

# Build the container
docker build -t simple-flask -f infra/Dockerfile .
docker run -d -p 3000:3000 -e RUN_MODE=local simple-flask

# Test the endpoints:
# 1. Test GET /hello
curl http://localhost:3000/hello

# 2. Test POST /echo with a message
curl -X POST "http://localhost:3000/echo" \
  -H "Content-Type: application/json" \
  -d '{"message": "hello world"}'
```

This local testing setup is crucial because it helps catch issues before deployment.

The beauty of this setup is that once it works locally, it'll work the same way in AWS.

And since this is just a standard Python application in a container, you can use all your favorite Python tools and patterns – your preferred package manager (pip, poetry, uv), pytest for testing, standard logging, type hints, linting, and pre-commit hooks.

( *I'm skipping those details here to focus on deployment, but the container approach means there are no serverless-specific limitations on your Python workflow.* )

## **Infrastructure as code with Pulumi**

Now let's get our containerized Flask app into AWS. While you could click around in the AWS console, we're going to do this properly with infrastructure as code. You are welcome to use [Cloudformation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or manual setup, but it's nice to be able to keep everything in Python, and this is the Pulumi blog. Using Python to define our AWS resources means we get type-checking and proper IDE support.

Here's our infrastructure code:

*Don't let the infrastructure code below intimidate you. It's just typed Python code, hooking up the Lambda, that you can version control and modify easily.*

```python
from typing import Any
import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx
import json

# First, create an API Gateway
api_gateway: aws.apigatewayv2.Api = aws.apigatewayv2.Api("flask-api",
    name="Flask Lambda API",
    protocol_type="HTTP",
    route_selection_expression="$request.method $request.path"
)

# Create IAM role for Lambda
lambda_role: aws.iam.Role = aws.iam.Role("flask-lambda-role",
    assume_role_policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Effect": "Allow",
            "Sid": ""
        }]
    })
)

# Attach basic execution policy - Lambda needs this to write logs
lambda_role_policy: aws.iam.RolePolicyAttachment = aws.iam.RolePolicyAttachment("lambda-role-policy",
    role=lambda_role.name,
    policy_arn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
)

# Create ECR repository for our container
repository: aws.ecr.Repository = aws.ecr.Repository("flask-app-repo",
    name="flask-app-repo",
    force_delete=True,  # Makes cleanup easier for testing
    image_scanning_configuration=aws.ecr.RepositoryImageScanningConfigurationArgs(
        scan_on_push=True,
    )
)

# Build and push the Docker image to ECR
image: awsx.ecr.Image = awsx.ecr.Image("flask-app-image",
    repository_url=repository.repository_url,
    path=".",  # Path to your Dockerfile
    platform="linux/amd64"  # Important for M1/M2 Mac users
)

# Create the Lambda function
lambda_function: aws.lambda_.Function = aws.lambda_.Function("flask-app",
    name="flask-app",
    package_type="Image",
    image_uri=image.image_uri,
    role=lambda_role.arn,
    timeout=30,
    memory_size=512,
    environment={
        "variables": {
            "FLASK_ENV": "production",
            "PYTHONUNBUFFERED": "1"
        }
    }
)

# Create API Gateway stage
stage: aws.apigatewayv2.Stage = aws.apigatewayv2.Stage("api-stage",
    api_id=api_gateway.id,
    name="$default",
    auto_deploy=True
)

# Connect API Gateway to Lambda
integration: aws.apigatewayv2.Integration = aws.apigatewayv2.Integration("lambda-integration",
    api_id=api_gateway.id,
    integration_type="AWS_PROXY",
    integration_uri=lambda_function.arn,
    integration_method="POST",
    payload_format_version="2.0"
)

# Create catch-all route
route: aws.apigatewayv2.Route = aws.apigatewayv2.Route("catch-all-route",
    api_id=api_gateway.id,
    route_key="ANY /{proxy+}",
    target=integration.id.apply(lambda id: f"integrations/{id}")
)

# Allow API Gateway to invoke Lambda
lambda_permission: aws.lambda_.Permission = aws.lambda_.Permission("api-lambda-permission",
    action="lambda:InvokeFunction",
    function=lambda_function.name,
    principal="apigateway.amazonaws.com",
    source_arn=api_gateway.execution_arn.apply(lambda arn: f"{arn}/*/*")
)

# Export the API Gateway URL
pulumi.export("url", api_gateway.api_endpoint)
```

Let's break down what's happening here:

1. **API Gateway**: We create an HTTP API (v2) that will receive all web requests and forward them to our Lambda.
2. **IAM Role**: Lambda needs permissions to execute and write logs. We create a role with the minimum necessary permissions.
3. **Container Registry**: We create an ECR repository and use Pulumi's `awsx` package to build and push our Docker image automatically.
4. **Lambda Function**: We create the Lambda function using our container image. Notice how we set memory and timeout - these are important for a web application.
5. **Integration**: We connect API Gateway to Lambda using the AWS\_PROXY integration type. `ANY /{proxy+}` means we route everything through with the full path.

Need a custom domain, that's easy to use as well. Setup some Route53 records, CNAME a domain name appropriately and you'll have a container backed by a custom domain name.

## Why I love this approach

The cool thing about using Pulumi and lambdas is that they make complex infrastructure changes safe and repeatable.

- Want to increase the Lambda memory? Change one number and run `pulumi up`.
- You get [complete AWS Lambda and API Gateway management](/registry/packages/aws/) for your low-traffic REST APIs
- And [Infrastructure testing capabilities](/docs/iac/concepts/testing/) mean you can validate your serverless configuration before deployment

You can find the full code in the [service status monitor repo](https://github.com/adamgordonbell/service-status-monitor) from my [Python devops article](https://www.pulumi.com/blog/python-for-devops/). A larger version with rolling updates is coming soon.

{{< notes type="info" >}}

### **Alternative approaches**

There are other ways to run containers that scale to zero. [Google Cloud Run](https://www.pulumi.com/registry/packages/gcp/api-docs/cloudrun/service/) offers similar functionality on GCP, and [AWS App Runner](https://www.pulumi.com/blog/deploy-applications-with-aws-app-runner/) is another AWS service that can do this. Both have similar pricing models—very cheap for low-volume services. And [SST](https://www.pulumi.com/blog/from-cdk-pulumi-evolution-of-sst/) is a similar solution for getting TypeScript / JavaScript solutions into an AWS Lambda.

The beauty of the container approach used here is that switching between these services is straightforward. Since we're just running a standard container with a REST endpoint, there's nothing AWS-specific in our application code. If you need to move to a different platform later, you can take your container with you.

{{< /notes >}}

## **Conclusion**

Running Flask applications in Lambda containers represents a sweet spot between development simplicity and operational efficiency. You get:

1. **True zero-cost periods** when your application isn't being used
2. **Familiar development patterns** - it's just Flask
3. **Infrastructure as code** with Pulumi
4. **Automatic scaling** without managing servers

The trade-offs - primarily cold starts and some AWS-specific configuration - are worth it for many applications, especially:

- APIs with sporadic traffic
- Cost-sensitive projects

The key is understanding that this isn't just about saving money - it's about reducing operational complexity. No more worrying about scaling policies, server maintenance, or capacity planning. Your application scales automatically, and you only pay for what you use.

Is this approach right for every application? No, but this combination of familiar local development with serverless operations is under utilized.

I'd love to hear about your experiences with monolithic serverless applications. What hosting solutions have you tried? What challenges have you encountered?
