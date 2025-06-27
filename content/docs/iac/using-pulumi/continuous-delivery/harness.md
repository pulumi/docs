---
title_tag: "Using Harness | CI/CD"
meta_desc: This page details how to use Harness CI/CD to deploy infrastructure with Pulumi
           and manage Harness resources using the Pulumi Harness provider.
title: Harness
h1: Pulumi CI/CD & Harness
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Harness
        parent: iac-using-pulumi-cicd
        weight: 7
---

[Harness](https://www.harness.io/) is a modern software delivery platform that provides comprehensive CI/CD, feature flags, cloud cost management, and security testing capabilities. This page shows how to use Harness CI/CD to deploy infrastructure with Pulumi and how to manage Harness platform resources using the Pulumi Harness provider.

Pulumi doesn't require any particular arrangement of stacks or workflow to work in a continuous integration / continuous deployment system. The steps described here can be altered to fit into any existing deployment setup.

## Prerequisites

- An account on [https://app.pulumi.com](https://app.pulumi.com)
- The latest [Pulumi CLI](/docs/install/)
- A Harness account and access to Harness CI/CD
- A git repository connected to your Harness project
- [Pulumi Harness provider](/registry/packages/harness/) (optional, for managing Harness resources)

## Setting Up Harness CI/CD with Pulumi

### Authentication and Secrets Management

Authentication for both Pulumi and your cloud provider can be managed in several ways. We recommend using [Pulumi ESC (Environments, Secrets, and Configuration)](/docs/esc/) as your primary secrets management solution, as it provides centralized, secure configuration management that works seamlessly across different CI/CD platforms.

#### Option 1: Using Pulumi ESC (Recommended)

With Pulumi ESC, you can centralize all your secrets and configuration in one place:

1. **Create a Pulumi ESC environment** with your secrets:

```yaml
# esc-environment.yaml
values:
  pulumiConfig:
    pulumi:access-token:
      fn::secret: "your-pulumi-access-token"
  aws:
    AWS_ACCESS_KEY_ID:
      fn::secret: "your-aws-access-key"
    AWS_SECRET_ACCESS_KEY:
      fn::secret: "your-aws-secret-key"
    AWS_REGION: "us-east-1"
  environmentVariables:
    PULUMI_ACCESS_TOKEN: ${pulumiConfig.pulumi:access-token}
    AWS_ACCESS_KEY_ID: ${aws.AWS_ACCESS_KEY_ID}
    AWS_SECRET_ACCESS_KEY: ${aws.AWS_SECRET_ACCESS_KEY}
    AWS_REGION: ${aws.AWS_REGION}
```

1. **Configure your Harness pipeline** to use ESC:

```yaml
- step:
    type: Run
    name: Load Pulumi ESC Environment
    identifier: load_esc_env
    spec:
      shell: Bash
      command: |
        # Install and use ESC CLI to inject environment variables
        curl -fsSL https://get.pulumi.com/esc/install.sh | sh
        export PATH=$PATH:$HOME/.pulumi/bin
        # Open ESC environment and export variables
        eval "$(esc open your-org/your-environment --format shell)"

        # These variables are now available for subsequent steps
        echo "Environment loaded successfully"
    envVariables:
      PULUMI_ACCESS_TOKEN: <+secrets.getValue("PULUMI_ACCESS_TOKEN")>
```

#### Option 2: Using Harness Secrets

If you prefer to manage secrets directly in Harness, navigate to your project's **Secrets** section and add:

1. **`PULUMI_ACCESS_TOKEN`** - [Create a Pulumi access token](/docs/pulumi-cloud/accounts#access-tokens)
2. **Cloud provider credentials**:
   - AWS: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`
   - Azure: `ARM_CLIENT_ID`, `ARM_CLIENT_SECRET`, `ARM_TENANT_ID`, `ARM_SUBSCRIPTION_ID`
   - Google Cloud: `GOOGLE_CREDENTIALS`

### Pipeline Configuration

Create a `.harness/` directory in your repository with your pipeline configuration. Here's an example pipeline that runs `pulumi preview` on pull requests and `pulumi up` on commits to the main branch:

```yaml
pipeline:
  name: Pulumi Infrastructure
  identifier: pulumi_infrastructure
  projectIdentifier: your_project_id
  orgIdentifier: your_org_id
  tags: {}
  stages:
    - stage:
        name: Preview Infrastructure
        identifier: preview_infrastructure
        description: Preview infrastructure changes on pull requests
        type: CI
        spec:
          cloneCodebase: true
          platform:
            os: Linux
            arch: Amd64
          runtime:
            type: Cloud
            spec: {}
          execution:
            steps:
              - step:
                  type: Run
                  name: Install Dependencies
                  identifier: install_dependencies
                  spec:
                    shell: Bash
                    command: |
                      # Install Pulumi CLI
                      curl -fsSL https://get.pulumi.com | sh
                      export PATH=$PATH:$HOME/.pulumi/bin
                      # Install language-specific dependencies
                      case "<+pipeline.variables.language>" in
                        "typescript"|"javascript")
                          npm install
                          ;;
                        "python")
                          pip install -r requirements.txt
                          ;;
                        "go")
                          go mod download
                          ;;
                        "csharp")
                          dotnet restore
                          ;;
                      esac
              - step:
                  type: Run
                  name: Pulumi Preview
                  identifier: pulumi_preview
                  spec:
                    shell: Bash
                    command: |
                      export PATH=$PATH:$HOME/.pulumi/bin
                      cd <+pipeline.variables.workingDirectory>

                      # Login to Pulumi
                      pulumi login

                      # Select the stack
                      pulumi stack select <+pipeline.variables.stackName>
                      # Run preview
                      pulumi preview
                    envVariables:
                      PULUMI_ACCESS_TOKEN: <+secrets.getValue("PULUMI_ACCESS_TOKEN")>
                      AWS_ACCESS_KEY_ID: <+secrets.getValue("AWS_ACCESS_KEY_ID")>
                      AWS_SECRET_ACCESS_KEY: <+secrets.getValue("AWS_SECRET_ACCESS_KEY")>
                      AWS_REGION: <+secrets.getValue("AWS_REGION")>
        when:
          pipelineStatus: Success
          condition: <+trigger.event> == "PR"
    - stage:
        name: Deploy Infrastructure
        identifier: deploy_infrastructure
        description: Deploy infrastructure changes on main branch
        type: CI
        spec:
          cloneCodebase: true
          platform:
            os: Linux
            arch: Amd64
          runtime:
            type: Cloud
            spec: {}
          execution:
            steps:
              - step:
                  type: Run
                  name: Install Dependencies
                  identifier: install_dependencies_deploy
                  spec:
                    shell: Bash
                    command: |
                      # Install Pulumi CLI
                      curl -fsSL https://get.pulumi.com | sh
                      export PATH=$PATH:$HOME/.pulumi/bin
                      # Install language-specific dependencies
                      case "<+pipeline.variables.language>" in
                        "typescript"|"javascript")
                          npm install
                          ;;
                        "python")
                          pip install -r requirements.txt
                          ;;
                        "go")
                          go mod download
                          ;;
                        "csharp")
                          dotnet restore
                          ;;
                      esac
              - step:
                  type: HarnessApproval
                  name: Infrastructure Approval
                  identifier: infra_approval
                  spec:
                    message: Please review the infrastructure changes before deployment
                    includePipelineExecutionHistory: true
                    approvers:
                      userGroups:
                        - account.Infrastructure_Team
                  timeout: 1d
                  when:
                    stageStatus: Success
                    condition: <+pipeline.variables.requireApproval> == "true"
              - step:
                  type: Run
                  name: Pulumi Up
                  identifier: pulumi_up
                  spec:
                    shell: Bash
                    command: |
                      export PATH=$PATH:$HOME/.pulumi/bin
                      cd <+pipeline.variables.workingDirectory>
                      # Login to Pulumi
                      pulumi login

                      # Select the stack
                      pulumi stack select <+pipeline.variables.stackName>

                      # Deploy infrastructure
                      pulumi up --yes
                    envVariables:
                      PULUMI_ACCESS_TOKEN: <+secrets.getValue("PULUMI_ACCESS_TOKEN")>
                      AWS_ACCESS_KEY_ID: <+secrets.getValue("AWS_ACCESS_KEY_ID")>
                      AWS_SECRET_ACCESS_KEY: <+secrets.getValue("AWS_SECRET_ACCESS_KEY")>
                      AWS_REGION: <+secrets.getValue("AWS_REGION")>
        when:
          pipelineStatus: Success
          condition: <+trigger.sourceBranch> == "main"
  variables:
    - name: stackName
      type: String
      description: The Pulumi stack to deploy
      value: "dev"
    - name: workingDirectory
      type: String
      description: Directory containing Pulumi project
      value: "infra"
    - name: language
      type: String
      description: Programming language (typescript, python, go, csharp)
      value: "typescript"
    - name: requireApproval
      type: String
      description: Whether to require approval for deployments
      value: "true"
```

## Use Cases

### Use Case 1: Infrastructure as Code for Application Platforms

You can use Harness to deploy applications while leveraging Pulumi to manage the underlying infrastructure. This creates a powerful combination where:

1. **Pulumi manages infrastructure**: Virtual machines, networking, databases, and Kubernetes clusters
2. **Harness manages applications**: Deployments, feature flags, and application lifecycle
3. **Integration through stack outputs**: Pulumi stack outputs provide connection details to Harness deployments

Example workflow:

```bash
# Infrastructure pipeline (Pulumi)
pulumi up --stack production-infra

# Get infrastructure outputs
CLUSTER_ENDPOINT=$(pulumi stack output clusterEndpoint)
DATABASE_CONNECTION=$(pulumi stack output databaseConnectionString)

# Pass to application deployment (Harness)
harness deploy --cluster $CLUSTER_ENDPOINT --database $DATABASE_CONNECTION
```

### Use Case 2: Managing Harness Platform Configuration with Pulumi

Use the [Pulumi Harness provider](/registry/packages/harness/) to manage your Harness platform configuration as code:

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
import * as harness from "@pulumi/harness";

// Create a project
const project = new harness.platform.Project("myProject", {
    identifier: "my_project",
    name: "My Project",
    orgId: "default",
    color: "#0063F7",
    modules: ["CI", "CD", "CV"],
});

// Create an environment
const environment = new harness.platform.Environment("production", {
    identifier: "production",
    name: "Production",
    orgId: "default",
    projectId: project.identifier,
    tags: ["env:production"],
    type: "Production",
});

// Create a service
const service = new harness.platform.Service("webApp", {
    identifier: "web_app",
    name: "Web Application",
    orgId: "default",
    projectId: project.identifier,
});

// Create a connector for your cloud provider
const awsConnector = new harness.platform.ConnectorAwsSecret("awsConnector", {
    identifier: "aws_connector",
    name: "AWS Connector",
    orgId: "default",
    projectId: project.identifier,
    secretManagerRef: "account.harnessSecretManager",
    region: "us-east-1",
    delegateSelectors: ["harness-delegate"],
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_harness as harness

# Create a project
project = harness.platform.Project("my-project",
    identifier="my_project",
    name="My Project",
    org_id="default",
    color="#0063F7",
    modules=["CI", "CD", "CV"]
)

# Create an environment
environment = harness.platform.Environment("production",
    identifier="production",
    name="Production",
    org_id="default",
    project_id=project.identifier,
    tags=["env:production"],
    type="Production"
)

# Create a service
service = harness.platform.Service("web-app",
    identifier="web_app",
    name="Web Application",
    org_id="default",
    project_id=project.identifier
)

# Create a connector for your cloud provider
aws_connector = harness.platform.ConnectorAwsSecret("aws-connector",
    identifier="aws_connector",
    name="AWS Connector",
    org_id="default",
    project_id=project.identifier,
    secret_manager_ref="account.harnessSecretManager",
    region="us-east-1",
    delegate_selectors=["harness-delegate"]
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-harness/sdk/go/harness/platform"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create a project
        project, err := platform.NewProject(ctx, "myProject", &platform.ProjectArgs{
            Identifier: pulumi.String("my_project"),
            Name:       pulumi.String("My Project"),
            OrgId:      pulumi.String("default"),
            Color:      pulumi.String("#0063F7"),
            Modules:    pulumi.StringArray{pulumi.String("CI"), pulumi.String("CD"), pulumi.String("CV")},
        })
        if err != nil {
            return err
        }

        // Create an environment
        _, err = platform.NewEnvironment(ctx, "production", &platform.EnvironmentArgs{
            Identifier: pulumi.String("production"),
            Name:       pulumi.String("Production"),
            OrgId:      pulumi.String("default"),
            ProjectId:  project.Identifier,
            Tags:       pulumi.StringArray{pulumi.String("env:production")},
            Type:       pulumi.String("Production"),
        })
        if err != nil {
            return err
        }

        // Create a service
        _, err = platform.NewService(ctx, "webApp", &platform.ServiceArgs{
            Identifier: pulumi.String("web_app"),
            Name:       pulumi.String("Web Application"),
            OrgId:      pulumi.String("default"),
            ProjectId:  project.Identifier,
        })
        if err != nil {
            return err
        }

        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Harness.Platform;

class Program
{
    static Task<int> Main() => Deployment.RunAsync(() => {
        // Create a project
        var project = new Project("myProject", new ProjectArgs
        {
            Identifier = "my_project",
            Name = "My Project",
            OrgId = "default",
            Color = "#0063F7",
            Modules = new[] { "CI", "CD", "CV" }
        });

        // Create an environment
        var environment = new Environment("production", new EnvironmentArgs
        {
            Identifier = "production",
            Name = "Production",
            OrgId = "default",
            ProjectId = project.Identifier,
            Tags = new[] { "env:production" },
            Type = "Production"
        });

        // Create a service
        var service = new Service("webApp", new ServiceArgs
        {
            Identifier = "web_app",
            Name = "Web Application",
            OrgId = "default",
            ProjectId = project.Identifier
        });

        return new Dictionary<string, object?>
        {
            ["projectId"] = project.Identifier,
            ["environmentId"] = environment.Identifier,
            ["serviceId"] = service.Identifier
        };
    });
}
```

{{% /choosable %}}

{{< /chooser >}}

### Use Case 3: Internal Developer Platform (IDP) Integration

If you're using Harness as part of an Internal Developer Platform, Pulumi can be integrated to provision infrastructure that applications depend on. This is particularly valuable when:

1. **Self-service infrastructure**: Developers can trigger infrastructure provisioning through Harness workflows
2. **Template-driven deployments**: Use Pulumi templates that developers can customize through Harness parameters
3. **Environment standardization**: Ensure consistent infrastructure across different teams and projects

Example IDP integration:

```yaml
# Template pipeline for infrastructure provisioning
pipeline:
  name: IDP Infrastructure Template
  identifier: idp_infra_template
  templateInputs:
    - name: applicationName
      type: String
      description: Name of the application
    - name: environment
      type: String
      description: Target environment (dev/staging/prod)
      allowedValues:
        - dev
        - staging
        - prod
    - name: instanceSize
      type: String
      description: Instance size for the application
      allowedValues:
        - small
        - medium
        - large
  stages:
    - stage:
        name: Provision Infrastructure
        type: CI
        spec:
          execution:
            steps:
              - step:
                  name: Generate Infrastructure
                  type: Run
                  spec:
                    command: |
                      # Use Pulumi template with dynamic configuration
                      pulumi new aws-typescript --name <+pipeline.variables.applicationName>

                      # Configure based on template inputs
                      pulumi config set aws:region us-east-1
                      pulumi config set instanceSize <+pipeline.variables.instanceSize>
                      pulumi config set environment <+pipeline.variables.environment>

                      # Deploy infrastructure
                      pulumi up --yes
```

## Advanced Configuration

### Environment-Specific Infrastructure Management

Pulumi excels at managing different environments with varying infrastructure needs. You can structure your infrastructure to handle the unique requirements of development, staging, and production environments:

#### Development Environment

- **Smaller resource allocations**: Use smaller instance sizes and fewer replicas
- **Relaxed security**: Allow broader access for debugging and testing
- **Cost optimization**: Use spot instances or scaled-down services
- **Rapid iteration**: Enable features like auto-scaling and blue-green deployments

```typescript
const config = new pulumi.Config();
const environment = config.require("environment");

const instanceType = environment === "dev" ? "t3.micro" :
                    environment === "staging" ? "t3.small" : "t3.large";

const cluster = new aws.ecs.Cluster("app-cluster", {
    capacityProviders: environment === "dev" ? ["FARGATE_SPOT"] : ["FARGATE"],
});
```

#### Staging Environment

- **Production-like configuration**: Mirror production settings for accurate testing
- **Data isolation**: Use production-sized databases with test data
- **Security testing**: Enable security scanning and compliance checks
- **Performance testing**: Scale to handle load testing scenarios

#### Production Environment

- **High availability**: Multi-zone deployments with redundancy
- **Enhanced security**: Strict network policies and encryption
- **Monitoring and alerting**: Comprehensive observability stack
- **Backup and disaster recovery**: Automated backup procedures

### Approval Gates and Workflow Integration

Harness approval gates work particularly well with Pulumi workflows. You can implement different approval strategies:

#### Infrastructure Change Approvals

Use approval gates specifically for infrastructure changes that require review:

```yaml
- step:
    type: HarnessApproval
    name: Infrastructure Security Review
    identifier: security_review
    spec:
      message: "Infrastructure changes detected. Please review security implications."
      includePipelineExecutionHistory: true
      approvers:
        userGroups:
          - account.Security_Team
          - account.Infrastructure_Team
      approverInputs:
        - name: securityApproved
          type: String
          allowedValues:
            - approved
            - rejected
    timeout: 2d
    when:
      stageStatus: Success
      condition: <+pipeline.variables.hasInfraChanges> == "true"
```

#### Environment-Specific Approvals

Different environments can have different approval requirements:

```yaml
- step:
    type: HarnessApproval
    name: Production Deployment Approval
    identifier: prod_approval
    spec:
      message: "Production infrastructure deployment requires approval"
      approvers:
        userGroups:
          - account.Production_Approvers
        minimumCount: 2
    when:
      stageStatus: Success
      condition: <+pipeline.variables.environment> == "production"
```

#### Application Deployment Gates

Coordinate infrastructure and application deployments with sequential approval gates:

```yaml
stages:
  - stage:
      name: Infrastructure Deployment
      # Pulumi infrastructure deployment
  - stage:
      name: Infrastructure Validation
      type: Approval
      spec:
        approvers:
          userGroups:
            - account.Infrastructure_Team
  - stage:
      name: Application Deployment
      # Harness application deployment
      dependsOn:
        - Infrastructure Validation
```

### Multi-Stack Deployments

For complex environments with multiple stacks, you can configure your Harness pipeline to deploy multiple stacks in sequence:

```yaml
- step:
    type: Run
    name: Deploy Infrastructure Stack
    identifier: deploy_infra
    spec:
      shell: Bash
      command: |
        pulumi stack select infrastructure
        pulumi up --yes

- step:
    type: Run
    name: Deploy Application Stack
    identifier: deploy_app
    spec:
      shell: Bash
      command: |
        pulumi stack select application
        pulumi up --yes
    when:
      stageStatus: Success
```

## Best Practices

Following these best practices will help ensure reliable, secure, and maintainable infrastructure deployments with Harness and Pulumi:

- **Use Secrets Management**: Prefer Pulumi ESC for centralized secrets management, with Harness secrets as a secondary option for platform-specific needs.

- **Environment Configuration**: Use different Pulumi stacks and ESC environments for each deployment target (dev/staging/production).

- **Resource Tagging**: Tag your infrastructure resources with environment and ownership information for better cost management and organization.

- **Pipeline Validation**: Always run `pulumi preview` before `pulumi up` to review changes.

- **Approval Gates**: Implement appropriate approval gates based on environment criticality and change scope.

- **Rollback Strategy**: Implement proper rollback mechanisms using Pulumi's stack history:

   ```bash
   # Rollback to previous deployment
   pulumi stack history
   pulumi stack export --version <previous-version> > previous-state.json
   pulumi stack import previous-state.json
   ```

- **IDP Integration**: When using Harness as an IDP, provide templates and self-service capabilities that abstract infrastructure complexity from developers.

## Troubleshooting

When integrating Harness with Pulumi, you may encounter some common issues. Here are solutions to the most frequently encountered problems:

- **Authentication Failures**: Ensure all required secrets are properly configured in Harness or Pulumi ESC.
- **Stack Not Found**: Verify stack names and ensure stacks exist in Pulumi Cloud.
- **Resource Conflicts**: Use `pulumi refresh` to sync state with actual cloud resources.
- **Pipeline Timeouts**: Increase timeout values for long-running infrastructure deployments.

For additional troubleshooting, see our [CI/CD troubleshooting guide](/docs/iac/using-pulumi/continuous-delivery/troubleshooting-guide).

## Next Steps

- Explore the [Pulumi Harness provider documentation](/registry/packages/harness/)
- Learn about [Pulumi ESC](/docs/esc/) for advanced secrets and configuration management
- Check out [Pulumi Deployments](/docs/pulumi-cloud/deployments/) for additional CI/CD capabilities
- Review [Harness CI/CD documentation](https://docs.harness.io/category/zgffarnh1m-ci-category) for platform-specific features
- Explore [Harness IDP documentation](https://docs.harness.io/docs/internal-developer-portal) for internal developer platform capabilities
