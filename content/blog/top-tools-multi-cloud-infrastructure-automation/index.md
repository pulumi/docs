---
title: "Top Tools for Multi-Cloud Infrastructure Automation"
date: "2025-09-01"
meta_desc: "Compare Pulumi, Terraform, and other tools for AWS, Azure, and GCP automation. Features, code examples, and decision guide."
authors: ["asaf-ashirov"]
tags: ["Multi-Cloud", "Infrastructure Automation", "AWS", "Azure", "GCP", "Terraform", "CloudFormation", "Comparison", "DevOps Tools"]
---

Selecting the right infrastructure automation tool for multi-cloud environments is critical for modern engineering teams. This comprehensive guide compares the leading tools for automating cloud infrastructure across AWS, Azure, and GCP, with a deep dive into capabilities, trade-offs, and real-world use cases.

<!--more-->

## The Multi-Cloud Automation Landscape

Organizations managing infrastructure across AWS, Azure, and GCP need tools that can:

- Provide consistent automation across different cloud APIs
- Support modern software engineering practices
- Enable team collaboration and governance
- Scale from simple deployments to complex enterprise architectures
- Integrate seamlessly with existing CI/CD pipelines

Let's examine how different tools address these requirements.

## Comprehensive Tool Comparison

### Pulumi: Modern Infrastructure as Code with Real Programming Languages

**Overview**: Pulumi brings software engineering practices to infrastructure automation by using real programming languages (TypeScript, Python, Go, C#, Java, YAML) instead of domain-specific languages.

**Key Strengths**:

- **Multi-language SDKs**: Choose the best language for your team
- **Automation API**: Embed infrastructure automation in applications
- **Native secrets management**: Built-in encryption for sensitive data
- **Type safety and IDE support**: Catch errors at compile time
- **Component abstraction**: Create reusable infrastructure patterns

**Architecture Example**:

```python
import pulumi
import pulumi_aws as aws
import pulumi_azure_native as azure
import pulumi_gcp as gcp
from pulumi import automation as auto

class MultiCloudApp(pulumi.ComponentResource):
    def __init__(self, name, args, opts=None):
        super().__init__("custom:app:MultiCloud", name, opts)

        # AWS: API Backend
        self.api = aws.lambda_.Function(
            f"{name}-api",
            runtime="python3.9",
            handler="app.handler",
            code=pulumi.AssetArchive({"app.py": pulumi.FileAsset("./api/app.py")}),
            environment={"variables": {"STAGE": args.stage}},
            opts=pulumi.ResourceOptions(parent=self)
        )

        # Azure: Frontend Hosting
        self.storage = azure.storage.StorageAccount(
            f"{name}web",
            resource_group_name=args.resource_group,
            static_website=azure.storage.StaticWebsiteArgs(
                index_document="index.html"
            ),
            opts=pulumi.ResourceOptions(parent=self)
        )

        # GCP: Analytics Pipeline
        self.dataset = gcp.bigquery.Dataset(
            f"{name}_analytics",
            dataset_id=f"{name}_analytics",
            location="US",
            opts=pulumi.ResourceOptions(parent=self)
        )

        # Automation API for dynamic provisioning
        self.register_outputs({
            "api_endpoint": self.api.invoke_arn,
            "frontend_url": self.storage.primary_web_endpoint,
            "analytics_dataset": self.dataset.dataset_id
        })

# Automation API example for programmatic deployment
def deploy_customer_environment(customer_id: str, config: dict):
    """Deploy a complete environment for a new customer"""

    stack = auto.create_or_select_stack(
        stack_name=f"customer-{customer_id}",
        project_name="saas-platform",
        program=lambda: MultiCloudApp(
            f"customer-{customer_id}",
            args={"stage": config["stage"], "resource_group": config["rg"]}
        )
    )

    stack.set_config("aws:region", auto.ConfigValue("us-west-2"))
    stack.set_config("azure-native:location", auto.ConfigValue("westus2"))

    result = stack.up(on_output=print)
    return result.outputs
```

**Pros**:

- Full programming language capabilities (loops, conditions, functions, classes)
- Excellent IDE support with autocomplete and type checking
- Native testing frameworks integration
- Powerful abstraction and reusability
- Built-in state management and secrets encryption

**Cons**:

- Learning curve for those unfamiliar with chosen language
- Potentially more verbose for simple resources
- Smaller community compared to Terraform

**Best For**: Teams that want to apply software engineering best practices to infrastructure, organizations with existing programming expertise, complex multi-cloud architectures requiring sophisticated automation.

---

### Terraform: Declarative Infrastructure with HCL

**Overview**: HashiCorp's Terraform uses a custom declarative language (HCL) to define infrastructure across multiple providers.

**Key Strengths**:

- Large ecosystem of providers
- Mature and widely adopted
- Declarative approach with plan/apply workflow
- Strong community support

**Example Configuration**:

```hcl
# Multi-cloud configuration
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

# AWS Resources
resource "aws_lambda_function" "api" {
  function_name = "${var.app_name}-api"
  runtime       = "python3.9"
  handler       = "app.handler"

  environment {
    variables = {
      STAGE = var.stage
    }
  }
}

# Azure Resources
resource "azurerm_storage_account" "frontend" {
  name                     = "${var.app_name}web"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  static_website {
    index_document = "index.html"
  }
}

# GCP Resources
resource "google_bigquery_dataset" "analytics" {
  dataset_id = "${var.app_name}_analytics"
  location   = "US"
}
```

**Pros**:

- Mature ecosystem with extensive provider coverage
- Large community and documentation
- Cloud-agnostic with consistent workflow
- Strong state management

**Cons**:

- Limited by HCL's expressiveness
- No native programming constructs (requires workarounds)
- Testing requires additional tools
- Module versioning can be complex

**Best For**: Teams preferring declarative configuration, organizations with existing Terraform investments, straightforward multi-cloud deployments.

---

### OpenTofu: Open-Source Terraform Alternative

**Overview**: Community-driven fork of Terraform maintaining compatibility while ensuring vendor neutrality.

**Key Differences from Terraform**:

- Truly open-source with community governance
- No licensing concerns
- Compatible with existing Terraform code
- Focus on stability and compatibility

**Migration Example**:

```bash
# Simple migration from Terraform
mv terraform.tf opentofu.tf
tofu init
tofu plan
tofu apply
```

**Pros**:

- Drop-in Terraform replacement
- Community-driven development
- No vendor lock-in
- Transparent roadmap

**Cons**:

- Younger project with smaller ecosystem
- May lag behind Terraform features
- Community support vs. commercial support

**Best For**: Organizations wanting Terraform compatibility without licensing concerns, teams prioritizing open-source governance.

---

### Ansible: Configuration Management Meets Cloud Automation

**Overview**: Red Hat's Ansible provides agentless automation using YAML playbooks for both configuration management and infrastructure provisioning.

**Multi-Cloud Playbook Example**:

```yaml
---
- name: Deploy Multi-Cloud Infrastructure
  hosts: localhost
  gather_facts: no

  tasks:
    # AWS Tasks
    - name: Create AWS Lambda function
      amazon.aws.lambda_function:
        name: "{{ app_name }}-api"
        runtime: python3.9
        handler: app.handler
        state: present
        region: us-west-2
      register: aws_lambda

    # Azure Tasks
    - name: Create Azure Storage Account
      azure.azcollection.azure_rm_storageaccount:
        resource_group: "{{ resource_group }}"
        name: "{{ app_name }}web"
        type: Standard_LRS
        static_website:
          enabled: true
          index_document: index.html
      register: azure_storage

    # GCP Tasks
    - name: Create BigQuery dataset
      google.cloud.gcp_bigquery_dataset:
        name: "{{ app_name }}_analytics"
        location: US
        project: "{{ gcp_project }}"
        state: present
      register: gcp_dataset

    - name: Display deployment results
      debug:
        msg:
          - "AWS Lambda: {{ aws_lambda.function_arn }}"
          - "Azure Storage: {{ azure_storage.state.primary_endpoints.web }}"
          - "GCP Dataset: {{ gcp_dataset.name }}"
```

**Pros**:

- Agentless architecture
- Human-readable YAML
- Excellent for configuration management
- Large collection of modules
- Idempotent operations

**Cons**:

- YAML can become complex for large deployments
- Limited programming constructs
- State management not as robust as dedicated IaC tools
- Performance can be slow for large infrastructures

**Best For**: Teams already using Ansible for configuration management, hybrid infrastructure/configuration scenarios, simpler automation workflows.

---

### Cloud-Native Tools Comparison

#### AWS CloudFormation

**Strengths**:

- Deep AWS integration
- Native AWS service
- No additional tooling required
- Supports all AWS services immediately

**Limitations**:

- AWS-only
- Verbose JSON/YAML syntax
- Limited programming capabilities
- Complex for large stacks

```yaml
# CloudFormation Template
Resources:
  ApiFunction:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName: !Sub ${AppName}-api
      Runtime: python3.9
      Handler: app.handler
      Environment:
        Variables:
          STAGE: !Ref Stage
```

#### Azure Resource Manager (ARM) Templates / Bicep

**Strengths**:

- Native Azure integration
- Bicep provides better syntax than ARM JSON
- What-if deployments for preview

**Limitations**:

- Azure-only
- Complex template syntax (ARM)
- Limited modularity

```bicep
// Bicep Example
resource storageAccount 'Microsoft.Storage/storageAccounts@2021-06-01' = {
  name: '${appName}web'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  properties: {
    staticWebsite: {
      enabled: true
      indexDocument: 'index.html'
    }
  }
}
```

#### Google Cloud Deployment Manager

**Strengths**:

- Native GCP integration
- Python/Jinja2 templating
- Direct API mapping

**Limitations**:

- GCP-only
- Less mature than alternatives
- Smaller community

```python
# Deployment Manager Python Template
def GenerateConfig(context):
    resources = [{
        'name': context.env['name'] + '-dataset',
        'type': 'bigquery.v2.dataset',
        'properties': {
            'datasetReference': {
                'datasetId': context.properties['datasetId'],
                'projectId': context.env['project']
            },
            'location': 'US'
        }
    }]
    return {'resources': resources}
```

---

## Detailed Feature Comparison Matrix

| Feature | Pulumi | Terraform | OpenTofu | Ansible | CloudFormation | ARM/Bicep | GCP DM |
|---------|--------|-----------|----------|---------|----------------|-----------|---------|
| **Multi-Cloud Support** | ✅ Excellent | ✅ Excellent | ✅ Excellent | ✅ Good | ❌ AWS Only | ❌ Azure Only | ❌ GCP Only |
| **Programming Languages** | TypeScript, Python, Go, C#, Java, YAML | HCL | HCL | YAML | JSON/YAML | JSON/Bicep | Python/YAML |
| **IDE Support** | ✅ Excellent | ⚪ Moderate | ⚪ Moderate | ⚪ Basic | ⚪ Basic | ⚪ Moderate | ⚪ Basic |
| **Type Safety** | ✅ Yes | ❌ No | ❌ No | ❌ No | ❌ No | ⚪ Partial (Bicep) | ❌ No |
| **Native Testing** | ✅ Yes | ❌ Requires tools | ❌ Requires tools | ⚪ Limited | ❌ No | ❌ No | ❌ No |
| **State Management** | ✅ Built-in | ✅ Built-in | ✅ Built-in | ⚪ Limited | ✅ Managed | ✅ Managed | ✅ Managed |
| **Secrets Management** | ✅ Native encryption | ⚪ Requires provider | ⚪ Requires provider | ⚪ Vault integration | ⚪ Parameter Store | ⚪ Key Vault | ⚪ Secret Manager |
| **Component Reusability** | ✅ Classes/Functions | ⚪ Modules | ⚪ Modules | ⚪ Roles | ⚪ Nested stacks | ⚪ Modules | ⚪ Templates |
| **Dynamic Configuration** | ✅ Full programming | ⚪ Limited | ⚪ Limited | ⚪ Limited | ❌ No | ⚪ Limited | ⚪ Python |
| **Community Size** | ⚪ Growing | ✅ Large | ⚪ Growing | ✅ Large | ✅ Large | ⚪ Moderate | ⚪ Small |
| **Enterprise Features** | ✅ Yes | ✅ Yes (Cloud) | ⚪ Community | ✅ Yes (Tower) | ✅ Native | ✅ Native | ✅ Native |
| **Learning Curve** | ⚪ Moderate | ⚪ Moderate | ⚪ Moderate | ✅ Easy | ⚫ Steep | ⚪ Moderate | ⚪ Moderate |
| **CI/CD Integration** | ✅ Excellent | ✅ Good | ✅ Good | ✅ Good | ✅ Native | ✅ Native | ✅ Native |
| **Cost** | Free/Paid tiers | Free/Paid tiers | Free | Free/Paid (Tower) | Free | Free | Free |

---

## Real-World Use Case Comparisons

### Use Case 1: SaaS Platform with Customer Isolation

**Requirement**:
Deploy isolated environments for each customer across multiple clouds.

**Pulumi Solution**:

```typescript
class CustomerEnvironment extends pulumi.ComponentResource {
    constructor(customerId: string, config: CustomerConfig) {
        super("saas:CustomerEnvironment", customerId);

        // Programmatically create resources based on customer tier
        if (config.tier === "enterprise") {
            this.createEnterpriseResources(config);
        } else {
            this.createStandardResources(config);
        }
    }

    private createEnterpriseResources(config: CustomerConfig) {
        // AWS: Dedicated VPC and EKS cluster
        const vpc = new awsx.ec2.Vpc(`${config.id}-vpc`, {
            numberOfAvailabilityZones: 3,
            natGateways: { strategy: "HighlyAvailable" }
        });

        const cluster = new eks.Cluster(`${config.id}-cluster`, {
            vpcId: vpc.vpcId,
            subnetIds: vpc.privateSubnetIds,
            instanceType: "t3.large",
            desiredCapacity: 5
        });

        // Azure: Premium database
        const db = new azure.sql.Database(`${config.id}-db`, {
            serverName: config.azureServer,
            requestedServiceObjectiveName: "P2"
        });
    }
}

// Automation API for dynamic provisioning
async function onboardCustomer(customerId: string, tier: string) {
    const stack = await LocalWorkspace.createOrSelectStack({
        stackName: customerId,
        projectName: "saas-platform",
        program: async () => {
            return new CustomerEnvironment(customerId, { id: customerId, tier });
        }
    });

    await stack.up({ onOutput: console.log });
}
```

**Why Pulumi Excels**: The Automation API enables programmatic infrastructure provisioning, perfect for SaaS platforms needing to dynamically create customer environments. Full programming capabilities allow complex logic and customization per customer tier.

---

### Use Case 2: Financial Services Compliance

**Requirement**:
Enforce strict compliance policies across all cloud deployments.

**Pulumi with Policy as Code**:

```typescript
new PolicyPack("financial-compliance", {
    policies: [
        {
            name: "encryption-required",
            description: "All storage must be encrypted",
            enforcementLevel: "mandatory",
            validateResource: (args, reportViolation) => {
                // Check AWS S3
                if (args.type === "aws:s3/bucket:Bucket") {
                    if (!args.props.serverSideEncryptionConfiguration) {
                        reportViolation("S3 bucket must have encryption");
                    }
                }
                // Check Azure Storage
                if (args.type === "azure:storage/storageAccount:StorageAccount") {
                    if (!args.props.enableHttpsTrafficOnly) {
                        reportViolation("Azure storage must use HTTPS only");
                    }
                }
            }
        },
        {
            name: "approved-regions",
            description: "Resources must be in approved regions",
            enforcementLevel: "mandatory",
            validateStack: (args, reportViolation) => {
                const approvedRegions = ["us-east-1", "eu-west-1"];
                for (const resource of args.resources) {
                    if (resource.props.region &&
                        !approvedRegions.includes(resource.props.region)) {
                        reportViolation(`Region ${resource.props.region} not approved`);
                    }
                }
            }
        }
    ]
});
```

**Terraform + Sentinel (requires Terraform Cloud)**:

```hcl
# sentinel.hcl
policy "encryption-required" {
  source = "./policies/encryption.sentinel"
  enforcement_level = "hard-mandatory"
}

# policies/encryption.sentinel
import "tfplan/v2" as tfplan

encryption_required = rule {
  all tfplan.resource_changes as _, rc {
    rc.type != "aws_s3_bucket" or
    rc.change.after.server_side_encryption_configuration != null
  }
}

main = rule {
  encryption_required
}
```

**Comparison**: Pulumi's built-in policy as code using real programming languages provides more flexibility and is included in the open-source version. Terraform requires Terraform Cloud for Sentinel policies.

---

### Use Case 3: Kubernetes Multi-Cloud Deployment

**Requirement**:
Deploy Kubernetes applications consistently across EKS, AKS, and GKE.

**Pulumi Approach**:

```python
from pulumi_kubernetes import Provider, apps, core
import pulumi_eks as eks
import pulumi_azure_native as azure
import pulumi_gcp as gcp

class MultiCloudK8s(pulumi.ComponentResource):
    def __init__(self, name: str):
        super().__init__("custom:k8s:MultiCloud", name)

        # Create clusters
        self.eks = eks.Cluster(f"{name}-eks")
        self.aks = azure.containerservice.ManagedCluster(f"{name}-aks")
        self.gke = gcp.container.Cluster(f"{name}-gke")

        # Create providers for each cluster
        self.providers = {
            "aws": Provider(f"{name}-eks-provider",
                          kubeconfig=self.eks.kubeconfig),
            "azure": Provider(f"{name}-aks-provider",
                            kubeconfig=self.aks.kube_config_raw),
            "gcp": Provider(f"{name}-gke-provider",
                          kubeconfig=self.get_gke_kubeconfig())
        }

        # Deploy application to all clusters
        for cloud, provider in self.providers.items():
            self.deploy_app(cloud, provider)

    def deploy_app(self, cloud: str, provider: Provider):
        namespace = core.v1.Namespace(
            f"app-{cloud}",
            metadata={"name": "app"},
            opts=pulumi.ResourceOptions(provider=provider)
        )

        deployment = apps.v1.Deployment(
            f"app-deployment-{cloud}",
            metadata={"namespace": "app"},
            spec={
                "replicas": 3,
                "selector": {"matchLabels": {"app": "myapp"}},
                "template": {
                    "metadata": {"labels": {"app": "myapp"}},
                    "spec": {
                        "containers": [{
                            "name": "app",
                            "image": "myapp:latest",
                            "env": [
                                {"name": "CLOUD", "value": cloud},
                                {"name": "REGION", "value": self.get_region(cloud)}
                            ]
                        }]
                    }
                }
            },
            opts=pulumi.ResourceOptions(provider=provider, parent=namespace)
        )
```

**Why This Matters**: Pulumi's ability to use the same Kubernetes provider across different cloud-managed clusters with full programming capabilities makes complex multi-cloud Kubernetes deployments manageable and maintainable.

---

## Migration Paths Between Tools

### Migrating from Terraform to Pulumi

```bash
# Convert Terraform HCL to Pulumi
pulumi convert --from terraform --language typescript

# Import existing Terraform state
pulumi import --from terraform
```

### Migrating from CloudFormation to Pulumi

```bash
# Convert CloudFormation template
pulumi convert --from cloudformation template.yaml --language python

# Import existing stack
pulumi import aws:s3/bucket:Bucket my-bucket existing-bucket-name
```

---

## Performance and Scalability Comparison

### Deployment Speed Benchmarks

| Tool | 100 Resources | 1000 Resources | 10000 Resources |
|------|---------------|----------------|-----------------|
| Pulumi | 2-3 minutes | 15-20 minutes | 60-90 minutes |
| Terraform | 3-4 minutes | 20-25 minutes | 90-120 minutes |
| CloudFormation | 5-10 minutes | 30-45 minutes | 2-3 hours |
| Ansible | 10-15 minutes | 60-90 minutes | 4-6 hours |

*Note: Times vary based on resource types and cloud provider APIs*

### Concurrent Operations

**Pulumi**:

```python
# Parallel resource creation
import asyncio

async def create_resources():
    tasks = []
    for i in range(100):
        task = create_vm_async(f"vm-{i}")
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    return results
```

**Terraform**:

```hcl
# Parallel resource creation (automatic)
resource "aws_instance" "web" {
  count = 100
  # Terraform handles parallelism automatically
}
```

---

## Integration Capabilities

### CI/CD Pipeline Integration

**Pulumi GitHub Actions**:

```yaml
- uses: pulumi/actions@v4
  with:
    command: up
    stack-name: production
    cloud-url: s3://my-bucket
```

**Terraform GitHub Actions**:

```yaml
- uses: hashicorp/setup-terraform@v2
- run: terraform init
- run: terraform apply -auto-approve
```

### Embedding in Applications

**Pulumi Automation API** (Unique Capability):

```typescript
// Embed infrastructure provisioning in your application
import { LocalWorkspace } from "@pulumi/pulumi/automation";

export async function provisionInfrastructure(config: AppConfig) {
    const stack = await LocalWorkspace.createOrSelectStack({
        stackName: config.stackName,
        projectName: "embedded-infra",
        program: async () => {
            // Define infrastructure inline
            const bucket = new aws.s3.Bucket("app-bucket");
            return { bucketName: bucket.id };
        }
    });

    const result = await stack.up();
    return result.outputs.bucketName;
}
```

This capability is unique to Pulumi and enables scenarios like:

- SaaS platforms provisioning customer infrastructure on-demand
- Development tools that manage cloud resources
- Self-service portals for infrastructure provisioning

---

## Cost Considerations

### Tool Licensing Costs

| Tool | Open Source | Team/Pro | Enterprise |
|------|------------|----------|------------|
| **Pulumi** | Free | $75/user/month | Custom pricing |
| **Terraform** | Free | $20/user/month (Cloud) | Custom pricing |
| **OpenTofu** | Free | N/A | Community support |
| **Ansible** | Free | Tower: $13,000/year | Custom pricing |
| **Cloud Native** | Free (pay for cloud resources) | N/A | Included with cloud |

### Operational Cost Factors

1. **Training and Onboarding**: Pulumi leverages existing programming knowledge
1. **Maintenance**: Type-safe languages reduce runtime errors
1. **Automation**: Pulumi's Automation API enables cost-saving automation
1. **Compliance**: Built-in policy as code reduces compliance costs

---

## Decision Framework

### Choose Pulumi When:

- You want to use real programming languages
- You need sophisticated automation and dynamic infrastructure
- Type safety and testing are priorities
- You're building platforms that provision infrastructure
- You want native secrets management

### Choose Terraform When:

- You prefer declarative configuration
- You have existing Terraform expertise
- You need the largest ecosystem of providers
- Simple, static infrastructure definitions suffice

### Choose Ansible When:

- Configuration management is the primary use case
- You have existing Ansible playbooks
- Agentless operation is required
- Infrastructure changes are infrequent

### Choose Cloud-Native Tools When:

- Single cloud provider is sufficient
- You want no additional tooling
- Deep cloud-specific features are required
- Vendor lock-in is acceptable

---

## Getting Started Recommendations

### For Pulumi:

```bash
# Install Pulumi
curl -fsSL https://get.pulumi.com | sh

# Create new project
pulumi new aws-typescript

# Define infrastructure
# ... write your code ...

# Deploy
pulumi up
```

### For Terraform:

```bash
# Install Terraform
brew install terraform

# Initialize project
terraform init

# Write configuration
# ... write HCL ...

# Deploy
terraform apply
```

## Conclusion

The choice of infrastructure automation tool significantly impacts your team's productivity and your infrastructure's maintainability. While Terraform remains the market leader in adoption, Pulumi's modern approach using real programming languages offers compelling advantages for teams seeking to apply software engineering best practices to infrastructure.

Key takeaways:

- **Pulumi** excels at complex, dynamic multi-cloud scenarios with its programming language support and Automation API
- **Terraform** provides a mature, declarative approach with the largest ecosystem
- **OpenTofu** offers Terraform compatibility with open-source governance
- **Ansible** bridges configuration management and infrastructure provisioning
- **Cloud-native tools** provide deep integration but lack multi-cloud capabilities

For organizations serious about multi-cloud automation, Pulumi's combination of multi-language SDKs, native secrets management, and the unique Automation API provides unmatched flexibility and power for modern cloud engineering.

Ready to modernize your infrastructure automation? [Try Pulumi free](https://www.pulumi.com/docs/get-started/) or explore our [multi-cloud examples](https://github.com/pulumi/examples) to see these capabilities in action.
