---
title: "Scale to Zero with Serverless APIs"
date: 2025-01-24T13:25:44-05:00
draft: false
meta_desc: How to run web services for practically nothing. AWS Lambda hosting for containers
meta_image: meta.png
authors:
    - adam-gordon-bell
tags:
    - python
    - serverless
social:
    twitter: >
            🚀 Transform your low-traffic Flask APIs into cost-efficient serverless apps! Package your entire REST API as a container, deploy to AWS Lambda, and pay $0 when idle. Simple local development, standard Flask patterns, and automatic scaling - all with minimal serverless expertise needed. 
    linkedin: >
            Ever wondered how to run web services for practically nothing? Adam shares an approach that's perfect for side projects and low-traffic applications.

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
---
Every developer has that service that needs to exist but barely gets used. Maybe it's an internal reporting API that get hourly requests but just from a handful of client, or maybe a side project you want hosted somewhere, but that is rarely used.

These services present a unique challenge: they need to be reliable when called, but actually keeping them always on and running seems like overkill.
<!--more-->
{{< youtube "cjLpOJn0B6g?rel=0" >}}

What if you could maintain these low-traffic services with zero cost when they're idle, while ensuring they spring to life exactly when needed? This is where AWS Lambda's container support shines. While many developers think of Lambda primarily for individual functions, it's equally capable of hosting complete REST APIs in containers.

Whether you're working with Flask, FastAPI, Express, or any other web framework, you can package your entire application as a container and let Lambda handle the scaling—including scaling to zero when there's no traffic. You pay only when your API is actually being called.

## **Why This Approach is Different**

"But Lambda means one function per REST endpoint, right?" I hear you say. While that's how serverless was originally positioned, the Lambda monolith approach has emerged as a simpler pattern. Take any REST API service, package it as a container, put it in Lambda, and give it a full HTTP route behind an IP, domain name, or API Gateway prefix. Done.

This approach gives you several benefits:

1. **Minimal Serverless Knowledge Required**: You don't need to be an expert in Lambda architecture or serverless patterns. If you can build a REST API and containerize it, you're ready to go.
2. **Standard Development Experience**: Write your API exactly as you would for any other hosting platform. No special frameworks, no Lambda-specific patterns to learn.
3. **Simple Local Development**: Run your container locally, and it behaves exactly like it will in production. No complex serverless emulation needed.
4. **Zero Cost at Zero Usage**: Get all the cost benefits of serverless without restructuring your application.

The trade-off? Cold starts when Lambda spins up a new container instance. But for low-traffic services, this is usually a worthwhile exchange for the operational simplicity and zero-cost idle periods.

My experience shows a Flask app on AWS Lambda with 512 MB memory and 40,000 requests per month would cost approximately **$0.28 per month**. A go service I created costs me even less, because memory usage and CPU usage is lower. And if your service is just a side project that gets no requests, your cost will be **~ $0 / month**.

{{< notes type="info" >}}

## Why containers?

Containers let us package everything—code, system dependencies, runtime—into one unit. Any HTTP service that fits in a container will work: Flask, Express, Rails, plus whatever system tools you need. Local testing? Just start the container. No Lambda-specific configuration needed.

{{< /notes >}}

## **Building Our Flask Application**

Let's start with the fun part - writing some Python code, but I’m going to keep it really simple. We'll build a simple Flask application that demonstrates why running a full web framework in Lambda makes sense. Instead of splitting everything into separate functions, we'll create a proper web application with multiple endpoints, error handling, and middleware.

Here's our starting point in `scripts/simple_server.py`

```python
from flask import Flask, jsonify, request
from mangum import Mangum

# Create Flask app
app = Flask(__name__)

@app.route("/hello")
def hello():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/echo", methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"reversed": data['message'][::-1]})

# Create Lambda handler
lambda_handler = Mangum(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
```

Notice a few key things about this code:

1. **It's Just Flask**: This is a standard Flask application. No Lambda-specific code, no special frameworks. If you know Flask, you know how to modify this.
2. **Multiple Endpoints**: We have several routes demonstrating different HTTP methods and URL patterns. In traditional Lambda, each of these would be a separate function.
3. **Error Handling**: Global error handling works just like in any Flask app. No need to handle errors differently for Lambda.

## **Containerizing for Lambda**

Let's look at Lambda's container requirements - they're straightforward once we break them down. The key is using the right base image and adapting our application to work with Lambda's runtime interface.

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

A few things to notice:

1. We're using AWS's official Lambda Python base image. There are ways do use your own base image, and your python package manager of choice, but starting with this base  and `pip install` is easiest.
2. The `${LAMBDA_TASK_ROOT}` is a special directory where Lambda expects to find your code
3. We're introducing a new file: `simple_entrypoint.sh`

## No Special Lambda Knowledge Required

The beauty of everything covered so far is that it's just a container running a flask app. I can work with it locally with docker run, put it in kubenetes or run it one of the [1000 places you can run containers](https://www.pulumi.com/blog/cursed-container-iceberg/). Lambda has some odd requirements about function calling that get in the way of this, but `simple_entrypoint.sh` saves the day:

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

This means locally, you don't need to know about lambdas at all if you supply `RUN_MODE=local`:

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

The beauty of this setup is that once it works locally, it'll work the same way in AWS. In the next section, we'll use Pulumi to deploy our container to AWS and set up all the necessary infrastructure.

## **Infrastructure as Code with Pulumi**

Now comes the really fun part - getting our containerized Flask app into AWS. While you could click around in the AWS console, we're going to do this properly with infrastructure as code. Pulumi lets us use real Python to define our AWS resources, which means we get type checking, proper IDE support, and all the other benefits of writing actual code.

Here's our infrastructure code:

```python
import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx
import json

# First, create an API Gateway
api_gateway = aws.apigatewayv2.Api("flask-api",
    name="Flask Lambda API",
    protocol_type="HTTP",
    route_selection_expression="$request.method $request.path"
)

# Create IAM role for Lambda
lambda_role = aws.iam.Role("flask-lambda-role",
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
lambda_role_policy = aws.iam.RolePolicyAttachment("lambda-role-policy",
    role=lambda_role.name,
    policy_arn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
)

# Create ECR repository for our container
repository = aws.ecr.Repository("flask-app-repo",
    name="flask-app-repo",
    force_delete=True,  # Makes cleanup easier for testing
    image_scanning_configuration=aws.ecr.RepositoryImageScanningConfigurationArgs(
        scan_on_push=True,
    )
)

# Build and push the Docker image to ECR
image = awsx.ecr.Image("flask-app-image",
    repository_url=repository.repository_url,
    path=".",  # Path to your Dockerfile
    platform="linux/amd64"  # Important for M1/M2 Mac users
)

# Create the Lambda function
lambda_function = aws.lambda_.Function("flask-app",
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
stage = aws.apigatewayv2.Stage("api-stage",
    api_id=api_gateway.id,
    name="$default",
    auto_deploy=True
)

# Connect API Gateway to Lambda
integration = aws.apigatewayv2.Integration("lambda-integration",
    api_id=api_gateway.id,
    integration_type="AWS_PROXY",
    integration_uri=lambda_function.arn,
    integration_method="POST",
    payload_format_version="2.0"
)

# Create catch-all route
route = aws.apigatewayv2.Route("catch-all-route",
    api_id=api_gateway.id,
    route_key="ANY /{proxy+}",
    target=integration.id.apply(lambda id: f"integrations/{id}")
)

# Allow API Gateway to invoke Lambda
lambda_permission = aws.lambda_.Permission("api-lambda-permission",
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
3. **Container Registry**: We create an ECR repository and use Pulumi's `awsx` package to automatically build and push our Docker image.
4. **Lambda Function**: We create the Lambda function using our container image. Notice how we set memory and timeout - these are important for a web application.
5. **Integration**: We connect API Gateway to Lambda using the AWS\_PROXY integration type. `ANY /{proxy+}` means we route everything through with the full path.

Want to add a custom domain? Here's how:

```python
# Create a certificate
certificate = aws.acm.Certificate("api-cert",
    domain_name="api.yourdomain.com",
    validation_method="DNS"
)

# Create domain name in API Gateway
domain_name = aws.apigatewayv2.DomainName("api-domain",
    domain_name="api.yourdomain.com",
    domain_name_configuration=aws.apigatewayv2.DomainNameDomainNameConfigurationArgs(
        certificate_arn=certificate.arn,
        endpoint_type="REGIONAL",
        security_policy="TLS_1_2"
    )
)

# Map the domain to our API stage
domain_mapping = aws.apigatewayv2.ApiMapping("api-mapping",
    api_id=api_gateway.id,
    domain_name=domain_name.id,
    stage=stage.id
)
```

Setup some Route53 records and cname a domain name appropratelly and you'll have a container backed by a custom domain name.

## Why I love this approach

The really cool thing about using Pulumi and lambdas is that it makes complex infrastructure changes safe and repeatable.

- Want to increase the Lambda memory? Change one number and run `pulumi up`.
- You get [complete AWS Lambda and API Gateway management](/registry/packages/aws/) for your low-traffic REST APIs
- And [Infrastructure testing capabilities](/docs/iac/concepts/testing/) mean you can validate your serverless configuration before deployment

You can find code for article in the [service status monitor repo](https://github.com/adamgordonbell/service-status-monitor) from my [python devops article](https://www.pulumi.com/blog/python-for-devops/). A larger version with rolling updates is coming soon.

{{< notes type="info" >}}

## **Alternative Approaches**

There are other ways to run containers that scale to zero. [Google Cloud Run](https://www.pulumi.com/registry/packages/gcp/api-docs/cloudrun/service/) offers similar functionality on GCP, and [AWS App Runner](https://www.pulumi.com/blog/deploy-applications-with-aws-app-runner/) is another AWS service that can do this. Both have similar pricing models—very cheap for low-volume services.

The beauty of the container approach is that switching between these services is straightforward. Since we're just running a standard container with a REST endpoint, there's nothing AWS-specific in our application code. If you need to move to a different platform later, you can take your container with you.

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

Is this approach right for every application? No. But for those Python web applications where you want to minimize operational overhead and costs, it's hard to beat. The combination of familiar development with serverless operations gives you the best of both worlds.

I'd love to hear about your experiences with monolithic serverless applications. What hosting solutions have you tried? What challenges have you encountered?
