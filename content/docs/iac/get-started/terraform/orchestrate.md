---
title_tag: Orchestrate Together | Pulumi for Terraform Users
title: Orchestrate Together
h1: "Orchestrate Together"
meta_desc: Learn advanced patterns for orchestrating Terraform and Pulumi deployments together in production environments.
weight: 7
menu:
    iac:
        name: Orchestrate Together
        parent: terraform-get-started
        weight: 7

aliases:
- /docs/iac/get-started/terraform/orchestrate/
---

## Deployment orchestration

In production environments, you'll often need to deploy both Terraform and Pulumi stacks together.
This section covers patterns for orchestrating deployments, managing dependencies, and sharing configuration.

## CI/CD pipeline integration

### GitHub Actions example

Here's a complete GitHub Actions workflow that deploys both Terraform and Pulumi stacks:

```yaml
# .github/workflows/deploy.yml
name: Deploy Infrastructure

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  AWS_REGION: us-west-2

jobs:
  deploy-terraform:
    runs-on: ubuntu-latest
    outputs:
      ecs-cluster-name: ${{ steps.tf-output.outputs.ecs_cluster_name }}
      ecr-repository-url: ${{ steps.tf-output.outputs.ecr_repository_url }}
      vpc-id: ${{ steps.tf-output.outputs.vpc_id }}
      private-subnet-ids: ${{ steps.tf-output.outputs.private_subnet_ids }}
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@v4
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: ${{ env.AWS_REGION }}
    
    - name: Setup Terraform
      uses: hashicorp/setup-terraform@v3
      with:
        terraform_version: 1.5.0
        terraform_wrapper: false
    
    - name: Terraform Init
      run: terraform init
      working-directory: ./terraform
    
    - name: Terraform Plan
      run: terraform plan
      working-directory: ./terraform
    
    - name: Terraform Apply
      if: github.ref == 'refs/heads/main'
      run: terraform apply -auto-approve
      working-directory: ./terraform
    
    - name: Get Terraform outputs
      id: tf-output
      run: |
        echo "ecs_cluster_name=$(terraform output -raw ecs_cluster_name)" >> $GITHUB_OUTPUT
        echo "ecr_repository_url=$(terraform output -raw ecr_repository_url)" >> $GITHUB_OUTPUT
        echo "vpc_id=$(terraform output -raw vpc_id)" >> $GITHUB_OUTPUT
        echo "private_subnet_ids=$(terraform output -json private_subnet_ids)" >> $GITHUB_OUTPUT
      working-directory: ./terraform

  deploy-pulumi:
    runs-on: ubuntu-latest
    needs: deploy-terraform
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@v4
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: ${{ env.AWS_REGION }}
    
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '18'
    
    - name: Install dependencies
      run: npm install
      working-directory: ./pulumi
    
    - name: Install Pulumi CLI
      uses: pulumi/actions@v4
    
    - name: Deploy Pulumi stack
      uses: pulumi/actions@v4
      with:
        command: up
        stack-name: production
        work-dir: ./pulumi
      env:
        PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
        
    - name: Get Pulumi outputs
      id: pulumi-output
      run: |
        echo "app_url=$(pulumi stack output appUrl)" >> $GITHUB_OUTPUT
        echo "service_name=$(pulumi stack output serviceName)" >> $GITHUB_OUTPUT
      working-directory: ./pulumi
      env:
        PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}

  test-deployment:
    runs-on: ubuntu-latest
    needs: [deploy-terraform, deploy-pulumi]
    
    steps:
    - name: Test application
      run: |
        curl -f ${{ needs.deploy-pulumi.outputs.app_url }} || exit 1
        echo "Application is responding successfully"
```

### Terraform workflow dependencies

Use Terraform's `depends_on` and data sources to manage dependencies:

```hcl
# terraform/main.tf
resource "aws_ecs_cluster" "app" {
  name = "app-cluster"
}

resource "aws_ecr_repository" "app" {
  name = "my-app"
}

# Export outputs for Pulumi
output "ecs_cluster_name" {
  value = aws_ecs_cluster.app.name
}

output "ecr_repository_url" {
  value = aws_ecr_repository.app.repository_url
}

output "vpc_id" {
  value = aws_vpc.main.id
}

output "private_subnet_ids" {
  value = aws_subnet.private[*].id
}
```

### Pulumi stack configuration

Configure your Pulumi stack to reference Terraform state:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

```typescript
// pulumi/index.ts
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as terraform from "@pulumi/terraform";

// Get configuration
const config = new pulumi.Config();
const environment = pulumi.getStack();

// Reference Terraform state
const tfState = new terraform.state.S3Reference("infrastructure", {
    bucket: config.require("terraform-state-bucket"),
    key: `${environment}/terraform.tfstate`,
    region: config.require("aws-region"),
});

// Get infrastructure details from Terraform
const clusterName = tfState.getOutput("ecs_cluster_name");
const repositoryUrl = tfState.getOutput("ecr_repository_url");
const vpcId = tfState.getOutput("vpc_id");
const subnetIds = tfState.getOutput("private_subnet_ids");

// Create application load balancer
const albSg = new aws.ec2.SecurityGroup("alb-sg", {
    name: `${environment}-alb-sg`,
    description: "Security group for ALB",
    vpcId: vpcId,
    ingress: [
        {
            fromPort: 80,
            toPort: 80,
            protocol: "tcp",
            cidrBlocks: ["0.0.0.0/0"],
        },
        {
            fromPort: 443,
            toPort: 443,
            protocol: "tcp",
            cidrBlocks: ["0.0.0.0/0"],
        },
    ],
    egress: [
        {
            fromPort: 0,
            toPort: 0,
            protocol: "-1",
            cidrBlocks: ["0.0.0.0/0"],
        },
    ],
});

const alb = new aws.lb.LoadBalancer("app-alb", {
    name: `${environment}-alb`,
    internal: false,
    loadBalancerType: "application",
    securityGroups: [albSg.id],
    subnets: subnetIds,
    enableDeletionProtection: environment === "production",
});

// Create ECS service
const taskRole = new aws.iam.Role("task-role", {
    assumeRolePolicy: JSON.stringify({
        Version: "2012-10-17",
        Statement: [
            {
                Action: "sts:AssumeRole",
                Effect: "Allow",
                Principal: {
                    Service: "ecs-tasks.amazonaws.com",
                },
            },
        ],
    }),
});

const taskDefinition = new aws.ecs.TaskDefinition("app-task", {
    family: `${environment}-app`,
    networkMode: "awsvpc",
    requiresCompatibilities: ["FARGATE"],
    cpu: "256",
    memory: "512",
    executionRoleArn: taskRole.arn,
    taskRoleArn: taskRole.arn,
    containerDefinitions: pulumi.interpolate`[
        {
            "name": "app",
            "image": "${repositoryUrl}:latest",
            "essential": true,
            "portMappings": [
                {
                    "containerPort": 80,
                    "protocol": "tcp"
                }
            ],
            "environment": [
                {
                    "name": "ENVIRONMENT",
                    "value": "${environment}"
                }
            ],
            "logConfiguration": {
                "logDriver": "awslogs",
                "options": {
                    "awslogs-group": "/ecs/${environment}-app",
                    "awslogs-region": "${config.require("aws-region")}",
                    "awslogs-stream-prefix": "ecs"
                }
            }
        }
    ]`,
});

const service = new aws.ecs.Service("app-service", {
    name: `${environment}-app-service`,
    cluster: clusterName,
    taskDefinition: taskDefinition.arn,
    desiredCount: environment === "production" ? 3 : 1,
    launchType: "FARGATE",
    networkConfiguration: {
        subnets: subnetIds,
        securityGroups: [albSg.id],
        assignPublicIp: true,
    },
    loadBalancers: [
        {
            targetGroupArn: targetGroup.arn,
            containerName: "app",
            containerPort: 80,
        },
    ],
    dependsOn: [listener],
});

// Export outputs
export const appUrl = pulumi.interpolate`http://${alb.dnsName}`;
export const serviceName = service.name;
export const clusterName = clusterName;
```

{{% /choosable %}}

{{% choosable language "python" %}}

```python
# pulumi/__main__.py
import pulumi
import pulumi_aws as aws
import pulumi_terraform as terraform

# Get configuration
config = pulumi.Config()
environment = pulumi.get_stack()

# Reference Terraform state
tf_state = terraform.state.S3Reference("infrastructure",
    bucket=config.require("terraform-state-bucket"),
    key=f"{environment}/terraform.tfstate",
    region=config.require("aws-region")
)

# Get infrastructure details from Terraform
cluster_name = tf_state.get_output("ecs_cluster_name")
repository_url = tf_state.get_output("ecr_repository_url")
vpc_id = tf_state.get_output("vpc_id")
subnet_ids = tf_state.get_output("private_subnet_ids")

# Create application load balancer
alb_sg = aws.ec2.SecurityGroup("alb-sg",
    name=f"{environment}-alb-sg",
    description="Security group for ALB",
    vpc_id=vpc_id,
    ingress=[
        {
            "from_port": 80,
            "to_port": 80,
            "protocol": "tcp",
            "cidr_blocks": ["0.0.0.0/0"],
        },
        {
            "from_port": 443,
            "to_port": 443,
            "protocol": "tcp",
            "cidr_blocks": ["0.0.0.0/0"],
        },
    ],
    egress=[
        {
            "from_port": 0,
            "to_port": 0,
            "protocol": "-1",
            "cidr_blocks": ["0.0.0.0/0"],
        }
    ]
)

alb = aws.lb.LoadBalancer("app-alb",
    name=f"{environment}-alb",
    internal=False,
    load_balancer_type="application",
    security_groups=[alb_sg.id],
    subnets=subnet_ids,
    enable_deletion_protection=environment == "production"
)

# Create ECS service
task_role = aws.iam.Role("task-role",
    assume_role_policy="""{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": "sts:AssumeRole",
                "Effect": "Allow",
                "Principal": {
                    "Service": "ecs-tasks.amazonaws.com"
                }
            }
        ]
    }"""
)

task_definition = aws.ecs.TaskDefinition("app-task",
    family=f"{environment}-app",
    network_mode="awsvpc",
    requires_compatibilities=["FARGATE"],
    cpu="256",
    memory="512",
    execution_role_arn=task_role.arn,
    task_role_arn=task_role.arn,
    container_definitions=pulumi.Output.format("""[
        {{
            "name": "app",
            "image": "{0}:latest",
            "essential": true,
            "portMappings": [
                {{
                    "containerPort": 80,
                    "protocol": "tcp"
                }}
            ],
            "environment": [
                {{
                    "name": "ENVIRONMENT",
                    "value": "{1}"
                }}
            ],
            "logConfiguration": {{
                "logDriver": "awslogs",
                "options": {{
                    "awslogs-group": "/ecs/{1}-app",
                    "awslogs-region": "{2}",
                    "awslogs-stream-prefix": "ecs"
                }}
            }}
        }}
    ]""", repository_url, environment, config.require("aws-region"))
)

service = aws.ecs.Service("app-service",
    name=f"{environment}-app-service",
    cluster=cluster_name,
    task_definition=task_definition.arn,
    desired_count=3 if environment == "production" else 1,
    launch_type="FARGATE",
    network_configuration={
        "subnets": subnet_ids,
        "security_groups": [alb_sg.id],
        "assign_public_ip": True,
    },
    load_balancers=[
        {
            "target_group_arn": target_group.arn,
            "container_name": "app",
            "container_port": 80,
        }
    ],
    opts=pulumi.ResourceOptions(depends_on=[listener])
)

# Export outputs
pulumi.export("appUrl", pulumi.Output.format("http://{0}", alb.dns_name))
pulumi.export("serviceName", service.name)
pulumi.export("clusterName", cluster_name)
```

{{% /choosable %}}

{{% choosable language "go" %}}

```go
// pulumi/main.go
package main

import (
	"fmt"

	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ecs"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/lb"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/iam"
	"github.com/pulumi/pulumi-terraform/sdk/v5/go/terraform/state"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Get configuration
		cfg := config.New(ctx, "")
		environment := ctx.Stack()

		// Reference Terraform state
		tfState, err := state.NewS3Reference(ctx, "infrastructure", &state.S3ReferenceArgs{
			Bucket: pulumi.String(cfg.Require("terraform-state-bucket")),
			Key:    pulumi.String(fmt.Sprintf("%s/terraform.tfstate", environment)),
			Region: pulumi.String(cfg.Require("aws-region")),
		})
		if err != nil {
			return err
		}

		// Get infrastructure details from Terraform
		clusterName := tfState.GetOutput(pulumi.String("ecs_cluster_name"))
		repositoryUrl := tfState.GetOutput(pulumi.String("ecr_repository_url"))
		vpcId := tfState.GetOutput(pulumi.String("vpc_id"))
		subnetIds := tfState.GetOutput(pulumi.String("private_subnet_ids"))

		// Create application load balancer
		albSg, err := ec2.NewSecurityGroup(ctx, "alb-sg", &ec2.SecurityGroupArgs{
			Name:        pulumi.String(fmt.Sprintf("%s-alb-sg", environment)),
			Description: pulumi.String("Security group for ALB"),
			VpcId:       vpcId,
			Ingress: ec2.SecurityGroupIngressArray{
				&ec2.SecurityGroupIngressArgs{
					FromPort:   pulumi.Int(80),
					ToPort:     pulumi.Int(80),
					Protocol:   pulumi.String("tcp"),
					CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
				},
				&ec2.SecurityGroupIngressArgs{
					FromPort:   pulumi.Int(443),
					ToPort:     pulumi.Int(443),
					Protocol:   pulumi.String("tcp"),
					CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
				},
			},
			Egress: ec2.SecurityGroupEgressArray{
				&ec2.SecurityGroupEgressArgs{
					FromPort:   pulumi.Int(0),
					ToPort:     pulumi.Int(0),
					Protocol:   pulumi.String("-1"),
					CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
				},
			},
		})
		if err != nil {
			return err
		}

		alb, err := lb.NewLoadBalancer(ctx, "app-alb", &lb.LoadBalancerArgs{
			Name:           pulumi.String(fmt.Sprintf("%s-alb", environment)),
			Internal:       pulumi.Bool(false),
			LoadBalancerType: pulumi.String("application"),
			SecurityGroups: pulumi.StringArray{albSg.ID()},
			Subnets:        subnetIds,
			EnableDeletionProtection: pulumi.Bool(environment == "production"),
		})
		if err != nil {
			return err
		}

		// Create ECS service
		taskRole, err := iam.NewRole(ctx, "task-role", &iam.RoleArgs{
			AssumeRolePolicy: pulumi.String(`{
				"Version": "2012-10-17",
				"Statement": [
					{
						"Action": "sts:AssumeRole",
						"Effect": "Allow",
						"Principal": {
							"Service": "ecs-tasks.amazonaws.com"
						}
					}
				]
			}`),
		})
		if err != nil {
			return err
		}

		desiredCount := 1
		if environment == "production" {
			desiredCount = 3
		}

		containerDefinitions := pulumi.Sprintf(`[
			{
				"name": "app",
				"image": "%s:latest",
				"essential": true,
				"portMappings": [
					{
						"containerPort": 80,
						"protocol": "tcp"
					}
				],
				"environment": [
					{
						"name": "ENVIRONMENT",
						"value": "%s"
					}
				],
				"logConfiguration": {
					"logDriver": "awslogs",
					"options": {
						"awslogs-group": "/ecs/%s-app",
						"awslogs-region": "%s",
						"awslogs-stream-prefix": "ecs"
					}
				}
			}
		]`, repositoryUrl, environment, environment, cfg.Require("aws-region"))

		taskDefinition, err := ecs.NewTaskDefinition(ctx, "app-task", &ecs.TaskDefinitionArgs{
			Family:                  pulumi.String(fmt.Sprintf("%s-app", environment)),
			NetworkMode:             pulumi.String("awsvpc"),
			RequiresCompatibilities: pulumi.StringArray{pulumi.String("FARGATE")},
			Cpu:                     pulumi.String("256"),
			Memory:                  pulumi.String("512"),
			ExecutionRoleArn:        taskRole.Arn,
			TaskRoleArn:             taskRole.Arn,
			ContainerDefinitions:    containerDefinitions,
		})
		if err != nil {
			return err
		}

		service, err := ecs.NewService(ctx, "app-service", &ecs.ServiceArgs{
			Name:            pulumi.String(fmt.Sprintf("%s-app-service", environment)),
			Cluster:         clusterName,
			TaskDefinition:  taskDefinition.Arn,
			DesiredCount:    pulumi.Int(desiredCount),
			LaunchType:      pulumi.String("FARGATE"),
			NetworkConfiguration: &ecs.ServiceNetworkConfigurationArgs{
				Subnets:          subnetIds,
				SecurityGroups:   pulumi.StringArray{albSg.ID()},
				AssignPublicIp:   pulumi.Bool(true),
			},
		})
		if err != nil {
			return err
		}

		// Export outputs
		ctx.Export("appUrl", pulumi.Sprintf("http://%s", alb.DnsName))
		ctx.Export("serviceName", service.Name)
		ctx.Export("clusterName", clusterName)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language "yaml" %}}

```yaml
# pulumi/Pulumi.yaml
name: app-deployment
runtime: yaml
description: Application deployment using Terraform infrastructure

config:
  terraform-state-bucket:
    type: string
    description: S3 bucket for Terraform state
  aws-region:
    type: string
    default: us-west-2

variables:
  environment: ${pulumi.stack}

resources:
  # Reference Terraform state
  infrastructure:
    type: terraform:state:S3Reference
    properties:
      bucket: ${terraform-state-bucket}
      key: ${environment}/terraform.tfstate
      region: ${aws-region}

  # Create application load balancer
  alb-sg:
    type: aws:ec2:SecurityGroup
    properties:
      name: ${environment}-alb-sg
      description: Security group for ALB
      vpcId: ${infrastructure.outputs.vpc_id}
      ingress:
        - fromPort: 80
          toPort: 80
          protocol: tcp
          cidrBlocks: ["0.0.0.0/0"]
        - fromPort: 443
          toPort: 443
          protocol: tcp
          cidrBlocks: ["0.0.0.0/0"]
      egress:
        - fromPort: 0
          toPort: 0
          protocol: "-1"
          cidrBlocks: ["0.0.0.0/0"]

  app-alb:
    type: aws:lb:LoadBalancer
    properties:
      name: ${environment}-alb
      internal: false
      loadBalancerType: application
      securityGroups: [${alb-sg.id}]
      subnets: ${infrastructure.outputs.private_subnet_ids}
      enableDeletionProtection: ${environment == "production"}

  # Create ECS service
  task-role:
    type: aws:iam:Role
    properties:
      assumeRolePolicy: |
        {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": "sts:AssumeRole",
              "Effect": "Allow",
              "Principal": {
                "Service": "ecs-tasks.amazonaws.com"
              }
            }
          ]
        }

  app-task:
    type: aws:ecs:TaskDefinition
    properties:
      family: ${environment}-app
      networkMode: awsvpc
      requiresCompatibilities: [FARGATE]
      cpu: "256"
      memory: "512"
      executionRoleArn: ${task-role.arn}
      taskRoleArn: ${task-role.arn}
      containerDefinitions: |
        [
          {
            "name": "app",
            "image": "${infrastructure.outputs.ecr_repository_url}:latest",
            "essential": true,
            "portMappings": [
              {
                "containerPort": 80,
                "protocol": "tcp"
              }
            ],
            "environment": [
              {
                "name": "ENVIRONMENT",
                "value": "${environment}"
              }
            ],
            "logConfiguration": {
              "logDriver": "awslogs",
              "options": {
                "awslogs-group": "/ecs/${environment}-app",
                "awslogs-region": "${aws-region}",
                "awslogs-stream-prefix": "ecs"
              }
            }
          }
        ]

  app-service:
    type: aws:ecs:Service
    properties:
      name: ${environment}-app-service
      cluster: ${infrastructure.outputs.ecs_cluster_name}
      taskDefinition: ${app-task.arn}
      desiredCount: ${environment == "production" ? 3 : 1}
      launchType: FARGATE
      networkConfiguration:
        subnets: ${infrastructure.outputs.private_subnet_ids}
        securityGroups: [${alb-sg.id}]
        assignPublicIp: true

outputs:
  appUrl: http://${app-alb.dnsName}
  serviceName: ${app-service.name}
  clusterName: ${infrastructure.outputs.ecs_cluster_name}
```

{{% /choosable %}}

## Shared configuration with Pulumi ESC

Use [Pulumi ESC](/docs/esc/) to share configuration between Terraform and Pulumi:

```yaml
# environments/production.yaml
values:
  aws:
    region: us-west-2
    accountId: "123456789012"
  
  terraform:
    stateBucket: myorg-terraform-state
    stateKey: production/terraform.tfstate
  
  app:
    name: my-app
    environment: production
    desiredCount: 3
    
  # AWS credentials from OIDC
  aws:
    login:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: arn:aws:iam::123456789012:role/PulumiRole
          sessionName: pulumi-session
    
  # Export environment variables
  environmentVariables:
    AWS_REGION: ${aws.region}
    AWS_DEFAULT_REGION: ${aws.region}
    TERRAFORM_STATE_BUCKET: ${terraform.stateBucket}
    TERRAFORM_STATE_KEY: ${terraform.stateKey}
```

Reference the environment in your Pulumi stack:

```yaml
# Pulumi.production.yaml
environment:
  - production

config:
  aws:region: ${aws.region}
  terraform-state-bucket: ${terraform.stateBucket}
  terraform-state-key: ${terraform.stateKey}
```

And in your Terraform configuration:

```hcl
# terraform/backend.tf
terraform {
  backend "s3" {
    bucket = "myorg-terraform-state"
    key    = "production/terraform.tfstate"
    region = "us-west-2"
  }
}
```

## Dependency management strategies

### Sequential deployment

Deploy stacks in sequence when there are hard dependencies:

```bash
#!/bin/bash
# deploy.sh

set -e

echo "Deploying Terraform infrastructure..."
cd terraform
terraform init
terraform plan
terraform apply -auto-approve
cd ..

echo "Deploying Pulumi application..."
cd pulumi
pulumi up --yes
cd ..

echo "Deployment complete!"
```

### Parallel deployment

Deploy independent stacks in parallel for faster deployments:

```bash
#!/bin/bash
# parallel-deploy.sh

set -e

# Deploy independent infrastructure in parallel
(
  echo "Deploying Terraform networking..."
  cd terraform/networking
  terraform init
  terraform apply -auto-approve
) &

(
  echo "Deploying Terraform security..."
  cd terraform/security
  terraform init
  terraform apply -auto-approve
) &

# Wait for parallel deployments
wait

# Deploy dependent application stack
echo "Deploying Pulumi application..."
cd pulumi
pulumi up --yes

echo "Deployment complete!"
```

### Blue-green deployment

Implement blue-green deployments across both tools:

```yaml
# .github/workflows/blue-green.yml
name: Blue-Green Deployment

on:
  push:
    branches: [main]

jobs:
  deploy-green:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Deploy green environment
      run: |
        # Deploy Terraform infrastructure for green
        cd terraform
        terraform workspace select green || terraform workspace new green
        terraform apply -auto-approve
        
        # Deploy Pulumi application to green
        cd ../pulumi
        pulumi stack select green || pulumi stack init green
        pulumi up --yes
    
    - name: Test green environment
      run: |
        # Health check green environment
        GREEN_URL=$(cd pulumi && pulumi stack output appUrl)
        curl -f $GREEN_URL/health || exit 1
    
    - name: Switch traffic to green
      run: |
        # Update load balancer to point to green
        cd terraform/traffic
        terraform apply -auto-approve -var="active_environment=green"
    
    - name: Cleanup blue environment
      run: |
        # Destroy blue environment after successful switch
        cd pulumi
        pulumi stack select blue
        pulumi destroy --yes
        
        cd ../terraform
        terraform workspace select blue
        terraform destroy -auto-approve
```

## Monitoring and observability

### Unified logging

Configure both Terraform and Pulumi to send logs to the same destination:

```yaml
# terraform/logging.tf
resource "aws_cloudwatch_log_group" "terraform_logs" {
  name              = "/terraform/${var.environment}"
  retention_in_days = 30
}

resource "aws_cloudwatch_log_stream" "terraform_stream" {
  name           = "terraform-operations"
  log_group_name = aws_cloudwatch_log_group.terraform_logs.name
}
```

{{% choosable language "typescript" %}}

```typescript
// pulumi/monitoring.ts
import * as aws from "@pulumi/aws";

// Create log group for Pulumi operations
const pulumiLogGroup = new aws.cloudwatch.LogGroup("pulumi-logs", {
    name: `/pulumi/${pulumi.getStack()}`,
    retentionInDays: 30,
});

// Create log stream
const pulumiLogStream = new aws.cloudwatch.LogStream("pulumi-stream", {
    name: "pulumi-operations",
    logGroupName: pulumiLogGroup.name,
});
```

{{% /choosable %}}

### Shared metrics

Use the same metrics namespace for both tools:

```yaml
# terraform/metrics.tf
resource "aws_cloudwatch_metric_alarm" "terraform_errors" {
  alarm_name          = "terraform-errors-${var.environment}"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "2"
  metric_name         = "ErrorCount"
  namespace           = "InfrastructureDeployment"
  period              = "300"
  statistic           = "Sum"
  threshold           = "1"
  alarm_description   = "This metric monitors Terraform errors"
  alarm_actions       = [aws_sns_topic.alerts.arn]

  dimensions = {
    Tool = "Terraform"
    Environment = var.environment
  }
}
```

{{% choosable language "typescript" %}}

```typescript
// pulumi/metrics.ts
const pulumiErrorAlarm = new aws.cloudwatch.MetricAlarm("pulumi-errors", {
    alarmName: `pulumi-errors-${environment}`,
    comparisonOperator: "GreaterThanThreshold",
    evaluationPeriods: 2,
    metricName: "ErrorCount",
    namespace: "InfrastructureDeployment",
    period: 300,
    statistic: "Sum",
    threshold: 1,
    alarmDescription: "This metric monitors Pulumi errors",
    alarmActions: [alertsTopic.arn],
    dimensions: {
        Tool: "Pulumi",
        Environment: environment,
    },
});
```

{{% /choosable %}}

## Best practices

1. **State management**: Use remote state for both Terraform and Pulumi
2. **Environment isolation**: Keep environments completely separated
3. **Dependency documentation**: Clearly document dependencies between stacks
4. **Testing**: Test both tools' outputs in integration tests
5. **Rollback strategy**: Have rollback procedures for both tools
6. **Monitoring**: Monitor both Terraform and Pulumi deployments
7. **Security**: Use consistent security practices across both tools
8. **Version control**: Tag releases that include both Terraform and Pulumi changes

{{< get-started-stepper >}}