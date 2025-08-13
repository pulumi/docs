---
title: "Pulumi GitOps for Scalable Cloud Infrastructure"
date: "2025-09-01"
meta_desc: "Learn how Pulumi's Git-centric workflow enables GitOps with automated deployments, drift detection, and CI/CD integration."
authors: ["asaf-ashirov"]
tags: ["GitOps", "Infrastructure as Code", "CI/CD", "DevOps", "Automation", "Cloud Infrastructure", "Version Control", "Kubernetes"]
---

GitOps has emerged as the gold standard for managing cloud-native infrastructure, bringing the power of Git workflows to infrastructure automation. This comprehensive guide explores how Pulumi seamlessly integrates with GitOps principles to deliver automated, auditable, and scalable cloud infrastructure management.

<!--more-->

## Understanding GitOps in the Context of Cloud Infrastructure

GitOps extends DevOps best practices by using Git as the single source of truth for declarative infrastructure and applications. With GitOps, your Git repository becomes the control plane for your infrastructure, where:

- **Every change** is tracked through Git commits
- **Every deployment** is triggered by Git events
- **Every configuration** is version-controlled and auditable
- **Every rollback** is as simple as reverting a commit

## Pulumi's Native GitOps Architecture

Pulumi was designed from the ground up with GitOps principles in mind. Unlike traditional infrastructure tools that bolt on Git support as an afterthought, Pulumi's architecture naturally aligns with Git-centric workflows.

### Core GitOps Capabilities in Pulumi

1. **Declarative Infrastructure as Real Code**: Define infrastructure using TypeScript, Python, Go, C#, Java, or YAML
1. **Git-Native State Management**: Infrastructure state tracked alongside code
1. **Automated Drift Detection**: Continuous reconciliation between desired and actual state
1. **Policy as Code Integration**: Enforce governance through version-controlled policies
1. **Native CI/CD Support**: First-class integration with GitHub Actions, GitLab CI, Azure DevOps, and more

## Implementing GitOps with Pulumi: A Practical Example

Let's build a complete GitOps workflow for deploying a microservices application to Kubernetes across multiple environments.

### Project Structure

```
infrastructure/
├── .github/
│   └── workflows/
│       ├── preview.yml
│       ├── deploy.yml
│       └── drift-detection.yml
├── environments/
│   ├── dev/
│   │   ├── Pulumi.yaml
│   │   └── Pulumi.dev.yaml
│   ├── staging/
│   │   ├── Pulumi.yaml
│   │   └── Pulumi.staging.yaml
│   └── production/
│       ├── Pulumi.yaml
│       └── Pulumi.production.yaml
├── components/
│   ├── kubernetes-cluster/
│   ├── database/
│   └── monitoring/
├── policies/
│   ├── security.ts
│   ├── cost.ts
│   └── compliance.ts
└── index.ts
```

### Core Infrastructure Definition

```typescript
// index.ts - Main infrastructure definition
import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";
import * as aws from "@pulumi/aws";
import { KubernetesCluster } from "./components/kubernetes-cluster";
import { Database } from "./components/database";
import { Monitoring } from "./components/monitoring";

const config = new pulumi.Config();
const environment = config.require("environment");
const region = config.require("region");

// Create EKS cluster with GitOps-friendly configuration
const cluster = new KubernetesCluster(`${environment}-cluster`, {
    desiredCapacity: config.requireNumber("clusterSize"),
    instanceType: config.require("instanceType"),
    kubernetesVersion: config.require("kubernetesVersion"),
    enableGitOpsController: true,
    tags: {
        Environment: environment,
        ManagedBy: "Pulumi",
        GitRepo: "infrastructure",
    },
});

// Deploy Flux GitOps controller for continuous deployment
const fluxNamespace = new k8s.core.v1.Namespace("flux-system", {
    metadata: {
        name: "flux-system",
    },
}, { provider: cluster.provider });

const fluxDeployment = new k8s.yaml.ConfigGroup("flux", {
    files: ["https://github.com/fluxcd/flux2/releases/latest/download/install.yaml"],
}, { provider: cluster.provider, dependsOn: [fluxNamespace] });

// Configure Git repository for Flux
const gitRepository = new k8s.apiextensions.CustomResource("app-repo", {
    apiVersion: "source.toolkit.fluxcd.io/v1beta2",
    kind: "GitRepository",
    metadata: {
        name: "app-repo",
        namespace: "flux-system",
    },
    spec: {
        interval: "1m",
        ref: {
            branch: environment === "production" ? "main" : environment,
        },
        url: "https://github.com/your-org/app-manifests",
    },
}, { provider: cluster.provider, dependsOn: [fluxDeployment] });

// Create Kustomization for automatic app deployment
const appKustomization = new k8s.apiextensions.CustomResource("app-kustomization", {
    apiVersion: "kustomize.toolkit.fluxcd.io/v1beta2",
    kind: "Kustomization",
    metadata: {
        name: "apps",
        namespace: "flux-system",
    },
    spec: {
        interval: "5m",
        path: `./clusters/${environment}`,
        prune: true,
        sourceRef: {
            kind: "GitRepository",
            name: "app-repo",
        },
        validation: "server",
        postBuild: {
            substitute: {
                cluster_name: cluster.name,
                region: region,
            },
        },
    },
}, { provider: cluster.provider, dependsOn: [gitRepository] });

// Database with automated backups
const database = new Database(`${environment}-db`, {
    engine: "postgres",
    instanceClass: config.require("dbInstanceClass"),
    allocatedStorage: config.requireNumber("dbStorage"),
    backupRetentionPeriod: environment === "production" ? 30 : 7,
    multiAz: environment === "production",
    tags: {
        Environment: environment,
        GitOpsManaged: "true",
    },
});

// Monitoring and observability
const monitoring = new Monitoring(`${environment}-monitoring`, {
    cluster: cluster,
    enablePrometheus: true,
    enableGrafana: true,
    enableAlertManager: true,
    slackWebhook: config.getSecret("slackWebhook"),
});

// Export outputs for GitOps workflows
export const clusterEndpoint = cluster.endpoint;
export const kubeconfig = cluster.kubeconfig;
export const databaseEndpoint = database.endpoint;
export const monitoringDashboard = monitoring.grafanaUrl;
```

### GitHub Actions GitOps Workflow

```yaml
# .github/workflows/preview.yml - Preview changes on PR
name: Preview Infrastructure Changes

on:
  pull_request:
    branches: [main]
    paths:
      - 'infrastructure/**'

jobs:
  preview:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        environment: [dev, staging, production]

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: |
          cd infrastructure
          npm install

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-west-2

      - name: Pulumi Preview
        uses: pulumi/actions@v4
        with:
          command: preview
          stack-name: ${{ matrix.environment }}
          work-dir: infrastructure/environments/${{ matrix.environment }}
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}

      - name: Post preview as PR comment
        uses: actions/github-script@v6
        with:
          script: |
            const output = '${{ steps.preview.outputs.output }}';
            const summary = output.split('\n').slice(0, 50).join('\n');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `## Pulumi Preview for ${{ matrix.environment }}

              \`\`\`
              ${summary}
              \`\`\`

              [View full preview in workflow logs](${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }})`
            });
```

```yaml
# .github/workflows/deploy.yml - Deploy on merge to main
name: Deploy Infrastructure

on:
  push:
    branches: [main]
    paths:
      - 'infrastructure/**'

jobs:
  deploy-dev:
    runs-on: ubuntu-latest
    environment: dev

    steps:
      - uses: actions/checkout@v3

      - name: Deploy to Dev
        uses: pulumi/actions@v4
        with:
          command: up
          stack-name: dev
          work-dir: infrastructure/environments/dev
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}

  deploy-staging:
    needs: deploy-dev
    runs-on: ubuntu-latest
    environment: staging

    steps:
      - uses: actions/checkout@v3

      - name: Run integration tests
        run: |
          cd tests
          npm test

      - name: Deploy to Staging
        uses: pulumi/actions@v4
        with:
          command: up
          stack-name: staging
          work-dir: infrastructure/environments/staging
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}

  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment: production

    steps:
      - uses: actions/checkout@v3

      - name: Deploy to Production
        uses: pulumi/actions@v4
        with:
          command: up
          stack-name: production
          work-dir: infrastructure/environments/production
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

### Implementing Drift Detection

```yaml
# .github/workflows/drift-detection.yml
name: Drift Detection

on:
  schedule:
    - cron: '0 */4 * * *'  # Every 4 hours
  workflow_dispatch:

jobs:
  detect-drift:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        environment: [dev, staging, production]

    steps:
      - uses: actions/checkout@v3

      - name: Detect Infrastructure Drift
        uses: pulumi/actions@v4
        with:
          command: preview
          stack-name: ${{ matrix.environment }}
          work-dir: infrastructure/environments/${{ matrix.environment }}
          expect-no-changes: true
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}

      - name: Alert on Drift
        if: failure()
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "⚠️ Infrastructure drift detected in ${{ matrix.environment }}!",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Infrastructure Drift Alert*\nDrift detected in `${{ matrix.environment }}` environment.\n<${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}|View Details>"
                  }
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

## Advanced GitOps Patterns with Pulumi

### 1. Multi-Environment Promotion Pipeline

```typescript
// promotion-pipeline.ts
import * as pulumi from "@pulumi/pulumi";
import { Octokit } from "@octokit/rest";

export class PromotionPipeline extends pulumi.ComponentResource {
    constructor(name: string, args: PromotionPipelineArgs, opts?: pulumi.ComponentResourceOptions) {
        super("custom:gitops:PromotionPipeline", name, opts);

        const octokit = new Octokit({
            auth: args.githubToken,
        });

        // Automated promotion workflow
        this.createPromotionWorkflow = async (fromEnv: string, toEnv: string, version: string) => {
            // Create PR for promotion
            const { data: pr } = await octokit.pulls.create({
                owner: args.repoOwner,
                repo: args.repoName,
                title: `Promote ${version} from ${fromEnv} to ${toEnv}`,
                head: `promote-${version}-to-${toEnv}`,
                base: toEnv === "production" ? "main" : toEnv,
                body: `## Promotion Request

                **Version**: ${version}
                **From**: ${fromEnv}
                **To**: ${toEnv}

                ### Changes
                - Updated image tags to ${version}
                - Applied environment-specific configurations

                ### Checklist
                - [ ] Integration tests passed
                - [ ] Performance benchmarks met
                - [ ] Security scan completed
                - [ ] Documentation updated

                /cc @platform-team`,
            });

            // Add reviewers based on environment
            if (toEnv === "production") {
                await octokit.pulls.requestReviewers({
                    owner: args.repoOwner,
                    repo: args.repoName,
                    pull_number: pr.number,
                    reviewers: args.productionReviewers,
                });
            }

            return pr.html_url;
        };
    }
}

interface PromotionPipelineArgs {
    repoOwner: string;
    repoName: string;
    githubToken: pulumi.Output<string>;
    productionReviewers: string[];
}
```

### 2. Policy-as-Code Enforcement

```typescript
// policies/security.ts
import * as policy from "@pulumi/policy";

export const securityPolicies = new policy.PolicyPack("security-gitops", {
    policies: [
        {
            name: "encrypted-secrets",
            description: "Ensure all secrets are encrypted",
            enforcementLevel: "mandatory",
            validateResource: (args, reportViolation) => {
                if (args.type === "kubernetes:core/v1:Secret") {
                    if (!args.props.stringData && !args.props.data) {
                        reportViolation("Secrets must contain encrypted data");
                    }
                }
            },
        },
        {
            name: "container-image-scanning",
            description: "Ensure container images are from approved registries",
            enforcementLevel: "mandatory",
            validateResource: (args, reportViolation) => {
                if (args.type === "kubernetes:core/v1:Pod" ||
                    args.type === "kubernetes:apps/v1:Deployment") {
                    const containers = args.props.spec?.containers || [];
                    const approvedRegistries = [
                        "gcr.io/your-org",
                        "your-org.azurecr.io",
                        "123456789.dkr.ecr.us-west-2.amazonaws.com",
                    ];

                    for (const container of containers) {
                        const image = container.image || "";
                        const isApproved = approvedRegistries.some(registry =>
                            image.startsWith(registry)
                        );

                        if (!isApproved) {
                            reportViolation(
                                `Container image ${image} is not from an approved registry`
                            );
                        }
                    }
                }
            },
        },
        {
            name: "network-policies-required",
            description: "Ensure network policies are defined for each namespace",
            enforcementLevel: "advisory",
            validateStack: (args, reportViolation) => {
                const namespaces = args.resources.filter(r =>
                    r.type === "kubernetes:core/v1:Namespace"
                );
                const networkPolicies = args.resources.filter(r =>
                    r.type === "kubernetes:networking.k8s.io/v1:NetworkPolicy"
                );

                for (const ns of namespaces) {
                    const hasPolicy = networkPolicies.some(np =>
                        np.props.metadata?.namespace === ns.props.metadata?.name
                    );

                    if (!hasPolicy) {
                        reportViolation(
                            `Namespace ${ns.props.metadata?.name} lacks network policies`
                        );
                    }
                }
            },
        },
    ],
});
```

### 3. Automated Rollback on Failure

```typescript
// components/auto-rollback.ts
import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";

export class AutoRollback extends pulumi.ComponentResource {
    constructor(
        name: string,
        args: AutoRollbackArgs,
        opts?: pulumi.ComponentResourceOptions
    ) {
        super("custom:gitops:AutoRollback", name, opts);

        // Deploy Flagger for progressive delivery
        const flaggerNamespace = new k8s.core.v1.Namespace(`${name}-flagger`, {
            metadata: { name: "flagger-system" },
        }, { parent: this });

        const flagger = new k8s.helm.v3.Chart(`${name}-flagger`, {
            chart: "flagger",
            version: "1.35.0",
            fetchOpts: {
                repo: "https://flagger.app",
            },
            namespace: flaggerNamespace.metadata.name,
            values: {
                prometheus: {
                    install: false,  // Use existing Prometheus
                },
                meshProvider: args.meshProvider || "istio",
            },
        }, { parent: this });

        // Create Canary resource for progressive rollout
        const canary = new k8s.apiextensions.CustomResource(`${name}-canary`, {
            apiVersion: "flagger.app/v1beta1",
            kind: "Canary",
            metadata: {
                name: args.deploymentName,
                namespace: args.namespace,
            },
            spec: {
                targetRef: {
                    apiVersion: "apps/v1",
                    kind: "Deployment",
                    name: args.deploymentName,
                },
                progressDeadlineSeconds: 60,
                service: {
                    port: args.servicePort,
                    targetPort: args.targetPort,
                    gateways: args.gateways,
                    hosts: args.hosts,
                },
                analysis: {
                    interval: "30s",
                    threshold: 5,
                    maxWeight: 50,
                    stepWeight: 10,
                    metrics: [
                        {
                            name: "request-success-rate",
                            thresholdRange: {
                                min: 99,
                            },
                            interval: "1m",
                        },
                        {
                            name: "request-duration",
                            thresholdRange: {
                                max: 500,
                            },
                            interval: "1m",
                        },
                    ],
                    webhooks: [
                        {
                            name: "load-test",
                            url: args.loadTestWebhook,
                            timeout: "5s",
                            metadata: {
                                cmd: "hey -z 1m -q 10 -c 2 http://podinfo-canary:9898/",
                            },
                        },
                        {
                            name: "rollback-notification",
                            url: args.notificationWebhook,
                            metadata: {
                                severity: "error",
                                channel: args.slackChannel,
                            },
                        },
                    ],
                },
            },
        }, { parent: this, dependsOn: [flagger] });
    }
}

interface AutoRollbackArgs {
    deploymentName: string;
    namespace: string;
    servicePort: number;
    targetPort: number;
    gateways?: string[];
    hosts?: string[];
    meshProvider?: string;
    loadTestWebhook: string;
    notificationWebhook: string;
    slackChannel: string;
}
```

## Pulumi Deployments: GitOps-Native Infrastructure Delivery

Pulumi Deployments takes GitOps to the next level with a purpose-built deployment platform:

```typescript
// pulumi-deployments-config.ts
import { DeploymentSettings } from "@pulumi/pulumi/deployments";

export const deploymentSettings: DeploymentSettings = {
    organization: "your-org",
    project: "infrastructure",
    stack: "production",

    // Git integration
    gitSource: {
        repoURL: "https://github.com/your-org/infrastructure",
        branch: "main",
        repoDir: "infrastructure",
    },

    // Deployment triggers
    deployTriggers: {
        // Auto-deploy on git push
        gitPush: {
            branches: ["main"],
            paths: ["infrastructure/**"],
        },
        // Scheduled deployments
        schedule: {
            cron: "0 2 * * *",  // Daily at 2 AM
            timezone: "UTC",
        },
        // API triggers for external systems
        apiTriggers: true,
    },

    // Environment configuration
    environmentVariables: {
        ENVIRONMENT: "production",
        PULUMI_CONFIG_PASSPHRASE: "${{ secrets.PULUMI_CONFIG_PASSPHRASE }}",
    },

    // Review and approval settings
    reviewSettings: {
        required: true,
        reviewers: ["platform-team", "security-team"],
        commentRequired: true,
    },

    // Drift detection and remediation
    driftDetection: {
        enabled: true,
        schedule: "0 */6 * * *",  // Every 6 hours
        autoRemediate: false,  // Require manual approval for drift correction
        notificationChannels: ["slack", "email"],
    },

    // Deployment validation
    validation: {
        preDeploymentSteps: [
            {
                name: "security-scan",
                command: "snyk test",
            },
            {
                name: "policy-check",
                command: "pulumi policy validate",
            },
        ],
        postDeploymentSteps: [
            {
                name: "smoke-tests",
                command: "npm run test:smoke",
            },
            {
                name: "health-check",
                command: "kubectl wait --for=condition=ready pods --all",
            },
        ],
    },

    // Rollback configuration
    rollback: {
        onFailure: true,
        maxRollbackAttempts: 3,
        rollbackWindow: "30m",
    },
};
```

## Integrating with Popular CI/CD Platforms

### GitLab CI Integration

```yaml
# .gitlab-ci.yml
stages:
  - validate
  - preview
  - deploy
  - verify

variables:
  PULUMI_VERSION: "latest"

before_script:
  - curl -fsSL https://get.pulumi.com | sh
  - export PATH=$PATH:$HOME/.pulumi/bin
  - pulumi login

validate:policy:
  stage: validate
  script:
    - cd infrastructure
    - npm install
    - pulumi policy validate
  only:
    - merge_requests

preview:infrastructure:
  stage: preview
  script:
    - cd infrastructure
    - pulumi stack select $CI_COMMIT_REF_SLUG
    - pulumi preview --diff
  artifacts:
    reports:
      terraform: preview-report.json
  only:
    - merge_requests

deploy:infrastructure:
  stage: deploy
  script:
    - cd infrastructure
    - pulumi stack select $CI_ENVIRONMENT_NAME
    - pulumi up --yes
  environment:
    name: $CI_COMMIT_REF_NAME
    url: https://$CI_ENVIRONMENT_SLUG.example.com
  only:
    - main
    - production

verify:deployment:
  stage: verify
  script:
    - kubectl get pods --all-namespaces
    - curl -f https://$CI_ENVIRONMENT_URL/health
  dependencies:
    - deploy:infrastructure
```

### Azure DevOps Pipeline

```yaml
# azure-pipelines.yml
trigger:
  branches:
    include:
      - main
      - releases/*
  paths:
    include:
      - infrastructure/*

pool:
  vmImage: 'ubuntu-latest'

stages:
- stage: Preview
  condition: eq(variables['Build.Reason'], 'PullRequest')
  jobs:
  - job: PreviewChanges
    steps:
    - task: Pulumi@1
      inputs:
        command: 'preview'
        stack: '$(System.PullRequest.TargetBranch)'
        cwd: 'infrastructure'
      env:
        PULUMI_ACCESS_TOKEN: $(PULUMI_ACCESS_TOKEN)

- stage: Deploy
  condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
  jobs:
  - deployment: DeployInfrastructure
    environment: 'production'
    strategy:
      runOnce:
        deploy:
          steps:
          - task: Pulumi@1
            inputs:
              command: 'up'
              args: '--yes'
              stack: 'production'
              cwd: 'infrastructure'
            env:
              PULUMI_ACCESS_TOKEN: $(PULUMI_ACCESS_TOKEN)
```

## Best Practices for GitOps with Pulumi

### 1. Repository Structure

- Separate infrastructure code from application code
- Use environment-specific directories or branches
- Implement clear naming conventions
- Document deployment processes in README files

### 2. Secret Management

```typescript
// Use Pulumi's built-in secret management
const dbPassword = new pulumi.Config().requireSecret("dbPassword");

// Or integrate with external secret stores
const vaultSecret = vault.generic.getSecret({
    path: "secret/data/database",
});

// Never commit secrets to Git
const secret = new k8s.core.v1.Secret("app-secret", {
    metadata: { name: "app-secret" },
    stringData: {
        password: dbPassword,  // Automatically encrypted
    },
});
```

### 3. Change Management

- Require pull request reviews for all changes
- Use semantic versioning for infrastructure releases
- Implement staging environments for testing
- Document breaking changes clearly

### 4. Monitoring and Alerting

```typescript
// Set up alerts for GitOps workflows
const gitOpsAlert = new aws.cloudwatch.MetricAlarm("gitops-failure", {
    alarmName: "GitOps-Deployment-Failure",
    comparisonOperator: "GreaterThanThreshold",
    evaluationPeriods: 1,
    metricName: "DeploymentFailures",
    namespace: "GitOps",
    period: 300,
    statistic: "Sum",
    threshold: 0,
    alarmActions: [snsTopicArn],
});
```

## Common GitOps Patterns and Solutions

### Progressive Delivery

Implement blue-green and canary deployments:

```typescript
const blueGreenDeployment = new BlueGreenDeployment("app", {
    blue: {
        image: "app:v1.0",
        replicas: 3,
    },
    green: {
        image: "app:v1.1",
        replicas: 3,
    },
    trafficSplit: {
        blue: 90,
        green: 10,
    },
    autoPromote: {
        enabled: true,
        successRate: 99.5,
        latencyP99: 200,
    },
});
```

### Multi-Tenancy

Support multiple teams with isolated environments:

```typescript
interface TenantConfig {
    name: string;
    namespace: string;
    quotas: ResourceQuotas;
    admins: string[];
}

class MultiTenantCluster extends pulumi.ComponentResource {
    constructor(name: string, tenants: TenantConfig[]) {
        super("custom:gitops:MultiTenantCluster", name);

        for (const tenant of tenants) {
            // Create isolated namespace
            const namespace = new k8s.core.v1.Namespace(
                `${tenant.name}-namespace`,
                {
                    metadata: {
                        name: tenant.namespace,
                        labels: {
                            tenant: tenant.name,
                            "gitops-managed": "true",
                        },
                    },
                },
                { parent: this }
            );

            // Apply resource quotas
            const quota = new k8s.core.v1.ResourceQuota(
                `${tenant.name}-quota`,
                {
                    metadata: {
                        namespace: tenant.namespace,
                    },
                    spec: {
                        hard: tenant.quotas,
                    },
                },
                { parent: this }
            );

            // Configure RBAC
            const role = new k8s.rbac.v1.Role(
                `${tenant.name}-admin`,
                {
                    metadata: {
                        namespace: tenant.namespace,
                    },
                    rules: [{
                        apiGroups: ["*"],
                        resources: ["*"],
                        verbs: ["*"],
                    }],
                },
                { parent: this }
            );

            // Bind admins to role
            const roleBinding = new k8s.rbac.v1.RoleBinding(
                `${tenant.name}-admin-binding`,
                {
                    metadata: {
                        namespace: tenant.namespace,
                    },
                    subjects: tenant.admins.map(admin => ({
                        kind: "User",
                        name: admin,
                        apiGroup: "rbac.authorization.k8s.io",
                    })),
                    roleRef: {
                        kind: "Role",
                        name: role.metadata.name,
                        apiGroup: "rbac.authorization.k8s.io",
                    },
                },
                { parent: this }
            );
        }
    }
}
```

## Troubleshooting Common GitOps Issues

### Handling Drift

When drift is detected:

1. **Investigate the cause**: Check audit logs and recent changes
1. **Decide on resolution**: Accept drift or revert to desired state
1. **Update source of truth**: Ensure Git reflects the intended state
1. **Re-sync**: Trigger deployment to reconcile

### Debugging Failed Deployments

```bash
# Check Pulumi stack history
pulumi stack history

# View detailed logs
pulumi logs --since 1h

# Inspect specific resource
pulumi stack export | jq '.deployment.resources[] | select(.urn | contains("problematic-resource"))'

# Force refresh state
pulumi refresh --yes
```

## Conclusion

Pulumi's native integration with Git workflows makes it an ideal choice for implementing GitOps at scale. By combining infrastructure as real code with Git-centric deployment practices, teams can achieve:

- **Complete auditability** through Git history
- **Automated deployments** via CI/CD integration
- **Drift detection and correction** for consistency
- **Policy enforcement** through code review
- **Rapid rollbacks** via Git revert

Whether you're managing a single application or a complex multi-cloud infrastructure, Pulumi's GitOps capabilities provide the foundation for reliable, scalable, and auditable infrastructure delivery.

Ready to implement GitOps with Pulumi? [Start with our GitOps guide](https://www.pulumi.com/docs/iac/adopting-pulumi/cicd/) or explore [Pulumi Deployments](https://www.pulumi.com/docs/pulumi-cloud/deployments/) for a fully-managed GitOps experience.
