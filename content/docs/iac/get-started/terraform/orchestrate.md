---
title_tag: Orchestrate Together | Pulumi for Terraform Users
title: Orchestrate Together
h1: "Orchestrate Together"
meta_desc: Learn advanced patterns for orchestrating Terraform and Pulumi deployments together in production environments.
weight: 8
menu:
    iac:
        name: Orchestrate Together
        parent: terraform-get-started
        weight: 8

aliases:
- /docs/iac/get-started/terraform/orchestrate/
---

## Deployment orchestration

In production environments, you'll often need to deploy both Terraform and Pulumi stacks together.
This section covers patterns for orchestrating deployments, managing dependencies, and sharing configuration.

## CI/CD pipeline integration

### GitHub Actions example

Let's consider the example from the [Referencing Terraform State](/docs/iac/get-started/terraform/reference-state/) step earlier. The configuration below shows a complete GitHub Actions workflow that deploys both the Terraform-managed ECS/ECR backend and the Pulumi-managed application stacks that depend on the backend infrastructure:

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

## Shared configuration with Pulumi ESC

[Pulumi ESC](/docs/esc/) is a powerful tool to share configuration between multiple environments and disparate tools. In brief, you can setup up a Pulumi ESC environment with configuration and secrets, and share that within both your Pulumi and Terraform environments.

You can run the `terraform` CLI app with environment variables provided by Pulumi ESC, or generate a var file that can be passed to Terraform.

To learn more, read this in-depth article showing how to [integrate Terraform and Pulumi ESC](/docs/esc/integrations/infrastructure/terraform/).

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

Some best practice tips to keep your two systems orchestrated:

1. **State management**: Use remote state for both Terraform and Pulumi
2. **Environment isolation**: Keep production and dev/test/staging environments completely separated
3. **Dependency documentation**: Clearly document dependencies between stacks
4. **Testing**: Test the output of both tools using integration tests
5. **Rollback strategy**: Have rollback procedures for both tools
6. **Monitoring**: Use common logging and metrics endpoints to monitor both Terraform and Pulumi deployments
7. **Security**: Use a single tool to manage secrets across both tools
8. **Version control**: Tag releases that include both Terraform and Pulumi changes to create a unified release

{{< get-started-stepper >}}
