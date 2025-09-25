---
title: "Day 2 Operations: Drift Detection and Remediation | IDP Workshop"
allow_long_title: true
meta_desc: "Implement automated drift detection for your IDP using Pulumi. Maintain infrastructure integrity with scheduled checks and real-time alerts."
meta_image: meta.png
date: 2025-09-25
series: idp-best-practices
authors:
    - engin-diri
tags:
    - idp
    - drift-detection
    - day-2-operations
    - infrastructure-as-code
    - pulumi-deployments
    - automation
    - platform-engineering
    - devops
    - remediation
social:
    twitter: |
        Day 2 Operations: Drift Detection and Remediation | IDP Workshop

        Learn how to maintain infrastructure integrity with automated drift detection:
        • Understand drift in cloud infrastructure
        • Set up automated detection schedules
        • Implement remediation workflows
        • Configure real-time notifications

        Read more: https://www.pulumi.com/blog/day-2-operations-drift-detection-and-remediation/

        #IDP #DriftDetection #PlatformEngineering #InfrastructureAsCode #DevOps
    linkedin: |
        **Day 2 Operations: Drift Detection and Remediation | IDP Workshop**

        In the fourth post of our IDP Best Practices series, we explore the critical day 2 operations that ensure your infrastructure stays aligned with your intended configuration long after initial deployment.

        **Key topics covered:**
        ✅ Understanding infrastructure drift and its real-world impact
        ✅ Prevention vs. Detection paradigm in platform strategy
        ✅ Implementing automated drift detection with Pulumi
        ✅ Setting up remediation workflows and schedules
        ✅ Configuring webhooks and notifications for drift events
        ✅ Best practices for maintaining infrastructure integrity

        **Why drift detection matters:**
        Even well-designed platforms with robust guardrails face infrastructure drift. Emergency hotfixes during incidents, manual console changes, or configuration changes outside your IaC workflow all create drift. You need to detect and remediate it quickly.

        **Access the free IDP Builder Workshop Series** for hands-on guidance, demo code, and recordings.

        Read the full guide: https://www.pulumi.com/blog/day-2-operations-drift-detection-and-remediation/

        #InternalDeveloperPlatform #DriftDetection #InfrastructureAsCode #PlatformEngineering #DevOps #CloudNative #Automation #Pulumi
---

Welcome to the fourth post in our **IDP Best Practices** series. In this workshop, we explore **drift detection and remediation**: the critical day 2 operations that ensure your infrastructure stays aligned with your intended configuration long after initial deployment.

Even well-designed platforms with robust guardrails face infrastructure drift. Emergency hotfixes during incidents, manual console changes, or configuration changes outside your IaC workflow all create drift. You need to detect and remediate it quickly.

<!--more-->

This post is part of our IDP Best Practices series:

* [How to Build an Internal Developer Platform: Strategy, Best Practices, and Self-Service Infrastructure](/blog/idp-strategy-planning-self-service-infrastructure-that-balances-developer-autonomy-with-operational-control)
* [Build Golden Paths with Infrastructure Components and Templates](/blog/golden-paths-infrastructure-components-and-templates)
* [Deployment Guardrails with Policy as Code](/blog/deployment-guardrails-policy-as-code)
* **Day 2 Operations: Drift Detection and Remediation** (you are here)
* Extend Your IDP for AI Applications: GPUs, Models, and Cost Controls
* Next-Gen IDPs: How to Modernize Legacy Infrastructure with Pulumi

## The Reality of Infrastructure Drift

Picture this scenario: It's Saturday afternoon. You're at a barbecue when you get an alert: your production application is down. You grab your laptop, but you're not on the corporate VPN. You can access the AWS console, but you can't reach the application to troubleshoot.

In desperation, you modify the security group in the console to allow access from anywhere (0.0.0.0/0) so you can diagnose the issue. You fix the problem, the burgers are ready, and you forget to revert that security change.

**Your infrastructure is now drifting from its intended state, and it will continue drifting until someone or something notices and fixes it.**

This represents drift in production environments. Day 2 operations prevent these issues from accumulating.

## Understanding the Prevention vs. Detection Paradigm

Before diving into drift detection, let's understand where it fits in your platform strategy:

### Prevention: The First Line of Defense

* **Code reviews**: Peer review of infrastructure changes
* **Automated testing**: Validation before deployment
* **Policy guardrails**: [CrossGuard policies](/docs/iac/packages-and-automation/crossguard) that block misconfigurations
* **Golden paths**: [Standardized components](/blog/golden-paths-infrastructure-components-and-templates) that encode best practices

These preventative measures catch issues that flow through your IaC pipeline.

### Detection and Remediation: The Safety Net

Drift detection functions as continuous verification. Prevention blocks most issues, while detection catches what slips through.

Detection and remediation covers:

* **Emergency changes** made during incidents
* **Console modifications** bypassing IaC workflows
* **External factors** like service limits or API changes
* **Accidental modifications** by team members

No matter how robust your preventative controls, you need detective controls to maintain infrastructure integrity.

## What Is Infrastructure Drift?

At its core, **drift occurs when your actual infrastructure state doesn't match your declared state in code.**

In Pulumi's architecture:

* **Desired state**: What your Pulumi program declares
* **Current state**: What Pulumi's [state file](/docs/iac/concepts/state-and-backends) tracks
* **Actual state**: What exists in your cloud provider(s)

The typical flow looks like this:

1. **Initial deployment**: Run `pulumi up` to deploy resources
2. **State recorded**: Pulumi saves the configuration to state
3. **Time passes**: Resources exist in the cloud
4. **Manual change**: Someone modifies a resource in the console
5. **Drift created**: Actual state ≠ Current state ≠ Desired state

## Pulumi's Drift Detection and Remediation Workflow

Pulumi provides a complete workflow for detecting and remediating drift:

### 1. Drift Detection with `pulumi refresh`

The [`pulumi refresh`](/docs/iac/cli/commands/pulumi_refresh) command queries your cloud provider(s) and compares actual resources against your state file:

```bash
# Run drift detection
pulumi refresh --preview-only

# This command:
# 1. Reads your current Pulumi state
# 2. Queries cloud providers for actual resource configurations
# 3. Identifies any differences
# 4. Reports what has drifted
```

The `--preview-only` flag shows you what's different without modifying the state file, allowing you to review changes before taking action.

### 2. State Reconciliation with `pulumi refresh`

Once you've reviewed the drift, you can update your state to match reality:

```bash
# Update state file to match cloud reality
pulumi refresh

# This command:
# 1. Detects drift (as above)
# 2. Updates state file to match actual cloud state
# 3. Prepares for remediation via pulumi up
```

### 3. Drift Remediation with `pulumi up`

After updating your state, [`pulumi up`](/docs/iac/cli/commands/pulumi_up) remediates by restoring your infrastructure to match your code:

```bash
# Remediate drift - restore to desired state
pulumi up

# This command:
# 1. Compares updated state with your Pulumi program
# 2. Identifies required changes
# 3. Applies changes to restore infrastructure
```

## Automating Drift Detection with Pulumi Deployments

Manual drift detection doesn't scale. [Pulumi Deployments](/docs/pulumi-cloud/deployments) enables automated, scheduled drift detection and remediation.

### Setting Up Automated Drift Detection

#### Step 1: Configure Deployment Settings

First, connect Pulumi to your source control using [Deployment Settings](/docs/pulumi-cloud/deployments/get-started):

Pulumi provides native integrations with:

* **GitHub**: Full app integration with [PR previews](/docs/pulumi-cloud/deployments/ci-cd-integration-assistant)
* **GitLab**: Merge request automation
* **Raw Git**: Direct repository access with credentials

#### Step 2: Create Drift Detection Schedules

Configure [automated drift detection](/docs/pulumi-cloud/deployments/drift) to run periodically:

```yaml
# Drift Detection Schedule
schedule:
  type: drift
  frequency: hourly  # or: "0 */2 * * *" for every 2 hours
  
  # Detection only - alerts but doesn't remediate
  auto_remediate: false
```

Or enable automatic remediation:

```yaml
# Drift Detection + Remediation Schedule
schedule:
  type: drift
  frequency: "0 */6 * * *"  # Every 6 hours
  
  # Automatically remediate detected drift
  auto_remediate: true
```

#### Step 3: Configure Webhooks for Notifications

Set up [notifications](/docs/pulumi-cloud/webhooks) when drift is detected or remediated:

```yaml
# Slack Webhook Configuration
webhooks:
  - type: slack
    name: drift-alerts
    url: https://hooks.slack.com/services/YOUR/WEBHOOK/URL
    triggers:
      - drift_detected
      - drift_remediated
      - drift_remediation_failed
```

Available webhook types:

* **Slack**: Direct integration with Slack channels
* **Microsoft Teams**: Teams channel notifications
* **Custom**: Generic webhooks for any system
* **Deployment triggers**: Trigger other Pulumi stacks

## Programmatic Drift Detection with Pulumi Service Provider

The [Pulumi Service Provider](/registry/packages/pulumiservice) enables you to manage drift detection as infrastructure:

### Creating Drift Schedules with Code

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as pulumiservice from "@pulumi/pulumiservice";

const driftSchedule = new pulumiservice.DriftSchedule("production-drift-detection", {
    organization: "my-org",
    project: "core-infrastructure",
    stack: "production",

    // Run every 4 hours
    scheduleCron: "0 */4 * * *",

    // Automatically fix any drift found
    autoRemediate: true,
});

export const scheduleId = driftSchedule.scheduleId;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_pulumiservice as pulumiservice

drift_schedule = pulumiservice.DriftSchedule("production-drift-detection",
    organization="my-org",
    project="core-infrastructure",
    stack="production",

    # Run every 4 hours
    schedule_cron="0 */4 * * *",

    # Automatically fix any drift found
    auto_remediate=True
)

pulumi.export('schedule_id', drift_schedule.schedule_id)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-pulumiservice/sdk/go/pulumiservice"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        driftSchedule, err := pulumiservice.NewDriftSchedule(ctx, "production-drift-detection", &pulumiservice.DriftScheduleArgs{
            Organization: pulumi.String("my-org"),
            Project: pulumi.String("core-infrastructure"),
            Stack: pulumi.String("production"),

            // Run every 4 hours
            ScheduleCron: pulumi.String("0 */4 * * *"),

            // Automatically fix any drift found
            AutoRemediate: pulumi.Bool(true),
        })
        if err != nil {
            return err
        }

        ctx.Export("scheduleId", driftSchedule.ScheduleId)
        return nil
    })
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using PulumiService = Pulumi.PulumiService;

class Program
{
    static Task<int> Main() => Deployment.RunAsync(() => {
        var driftSchedule = new PulumiService.DriftSchedule("production-drift-detection", new PulumiService.DriftScheduleArgs
        {
            Organization = "my-org",
            Project = "core-infrastructure",
            Stack = "production",

            // Run every 4 hours
            ScheduleCron = "0 */4 * * *",

            // Automatically fix any drift found
            AutoRemediate = true,
        });

        return new Dictionary<string, object?>
        {
            { "scheduleId", driftSchedule.ScheduleId }
        };
    });
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.pulumiservice.DriftSchedule;
import com.pulumi.pulumiservice.DriftScheduleArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    private static void stack(Context ctx) {
        var driftSchedule = new DriftSchedule("production-drift-detection", DriftScheduleArgs.builder()
            .organization("my-org")
            .project("core-infrastructure")
            .stack("production")

            // Run every 4 hours
            .scheduleCron("0 */4 * * *")

            // Automatically fix any drift found
            .autoRemediate(true)
            .build());

        ctx.export("scheduleId", driftSchedule.scheduleId());
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: drift-detection
runtime: yaml

resources:
  production-drift-detection:
    type: pulumiservice:index:DriftSchedule
    properties:
      organization: my-org
      project: core-infrastructure
      stack: production

      # Run every 4 hours
      scheduleCron: "0 */4 * * *"

      # Automatically fix any drift found
      autoRemediate: true

outputs:
  scheduleId: ${production-drift-detection.scheduleId}
```

{{% /choosable %}}

{{< /chooser >}}

## Advanced Drift Detection Patterns

### Multi-Stack Drift Detection

For platforms with multiple environments, set up drift detection across all stacks:

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as pulumiservice from "@pulumi/pulumiservice";

const environments = ["dev", "staging", "production"];

environments.forEach(env => {
    // More frequent checks for production
    const cronSchedule = env === "production"
        ? "0 * * * *"      // Every hour for production
        : "0 */6 * * *";   // Every 6 hours for others

    new pulumiservice.DriftSchedule(`${env}-drift-detection`, {
        organization: "my-org",
        project: "platform",
        stack: env,
        scheduleCron: cronSchedule,

        // Only auto-remediate non-production
        autoRemediate: env !== "production",
    });
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_pulumiservice as pulumiservice

environments = ["dev", "staging", "production"]

for env in environments:
    # More frequent checks for production
    cron_schedule = "0 * * * *" if env == "production" else "0 */6 * * *"

    pulumiservice.DriftSchedule(f"{env}-drift-detection",
        organization="my-org",
        project="platform",
        stack=env,
        schedule_cron=cron_schedule,

        # Only auto-remediate non-production
        auto_remediate=(env != "production")
    )
```

{{% /choosable %}}

{{< /chooser >}}

## Best Practices for Drift Detection

### 1. Start with Detection Only

Begin with detection-only schedules to understand your drift patterns:

```yaml
schedule:
  type: drift
  frequency: "0 */2 * * *"  # Every 2 hours
  auto_remediate: false     # Monitor only initially
```

### 2. Implement Gradual Remediation

Roll out auto-remediation gradually:

1. **Week 1-2**: Detection only, monitor patterns
2. **Week 3-4**: Auto-remediate development environments
3. **Week 5-6**: Auto-remediate staging
4. **Week 7+**: Consider auto-remediation for production

### 3. Use Protected Resources

Mark critical resources as [protected](/docs/iac/concepts/options/protect) to prevent accidental changes:

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
const database = new aws.rds.Instance("production-db", {
    // ... configuration
}, {
    protect: true  // Prevents deletion even during drift remediation
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
database = aws.rds.Instance("production-db",
    # ... configuration
    opts=pulumi.ResourceOptions(
        protect=True  # Prevents deletion even during drift remediation
    )
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
database, err := rds.NewInstance(ctx, "production-db", &rds.InstanceArgs{
    // ... configuration
}, pulumi.Protect(true))  // Prevents deletion even during drift remediation
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var database = new Aws.Rds.Instance("production-db", new InstanceArgs
{
    // ... configuration
}, new CustomResourceOptions
{
    Protect = true  // Prevents deletion even during drift remediation
});
```

{{% /choosable %}}

{{< /chooser >}}

### 4. Implement Drift Metrics

Track drift patterns to improve your platform:

```typescript
interface DriftMetrics {
    timestamp: Date;
    stack: string;
    resourcesChanged: number;
    changeTypes: string[];
    autoRemediated: boolean;
}

async function trackDriftMetrics(metrics: DriftMetrics) {
    // Send to your monitoring system
    await prometheus.recordDriftEvent(metrics);

    // Log for analysis
    console.log(`Drift detected: ${JSON.stringify(metrics)}`);

    // Alert if drift is frequent
    if (await isDriftFrequent(metrics.stack)) {
        await alertOpsTeam({
            message: `Frequent drift in ${metrics.stack}`,
            severity: "warning"
        });
    }
}
```

## Integrating with CI/CD Pipelines

### GitHub Actions Integration

Add drift detection to your [GitHub Actions workflows](/docs/iac/packages-and-automation/continuous-delivery/github-actions):

```yaml
name: Drift Detection

on:
  schedule:
    # Run every 4 hours
    - cron: '0 */4 * * *'
  workflow_dispatch: # Allow manual triggers

jobs:
  detect-drift:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Configure Pulumi
        uses: pulumi/actions@v5
        with:
          cloud-url: ${{ secrets.PULUMI_CLOUD_URL }}

      - name: Detect Drift
        run: |
          pulumi refresh --stack production --preview-only
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}

      - name: Notify on Drift
        if: failure()
        uses: actions/slack@v1
        with:
          webhook: ${{ secrets.SLACK_WEBHOOK }}
          message: "⚠️ Drift detected in production infrastructure"
```

### GitLab CI Integration

Configure drift detection in [GitLab CI](/docs/iac/packages-and-automation/continuous-delivery/gitlab-ci):

```yaml
drift-detection:
  stage: monitor
  image: pulumi/pulumi:latest

  script:
    - pulumi refresh --stack production --preview-only

  only:
    - schedules  # Run on schedule only

  variables:
    PULUMI_ACCESS_TOKEN: $PULUMI_ACCESS_TOKEN

  after_script:
    - |
      if [ "$CI_JOB_STATUS" == "failed" ]; then
        curl -X POST $SLACK_WEBHOOK \
          -H 'Content-Type: application/json' \
          -d '{"text":"⚠️ Drift detected in production"}'
      fi
```

## Handling Common Drift Scenarios

### Scenario 1: Emergency Hotfix

When an emergency change causes drift:

```bash
# 1. Acknowledge the drift
pulumi refresh --stack production

# 2. Review the changes
pulumi preview --stack production

# 3. Either incorporate or revert
# Option A: Accept the change
pulumi refresh --stack production --yes

# Option B: Revert to code
pulumi up --stack production --yes
```

### Scenario 2: Legitimate External Changes

Some changes might be legitimate (e.g., auto-scaling adjustments):

```typescript
// Mark resources that can change externally
const autoScalingGroup = new aws.autoscaling.Group("app-asg", {
    minSize: 2,
    maxSize: 10,
    // ... other config
}, {
    ignoreChanges: ["desiredCapacity"] // Ignore scaling changes
});
```

### Scenario 3: Configuration Drift

For configuration-only drift:

```python
# Use Pulumi's configuration system
config = pulumi.Config()
allowed_ips = config.get_object("allowed_ips") or ["10.0.0.0/8"]

security_group = aws.ec2.SecurityGroup("app-sg",
    ingress=[{
        "from_port": 443,
        "to_port": 443,
        "protocol": "tcp",
        "cidr_blocks": allowed_ips  # Managed via configuration
    }]
)
```

## The Value of Automated Drift Detection

Implementing automated drift detection delivers immediate value:

### 1. Security Compliance

* **Detect unauthorized changes** within minutes instead of weeks
* **Maintain compliance** with security policies automatically
* **Create audit trails** of all infrastructure changes

### 2. Operational Excellence

* **Reduce incidents** caused by configuration drift
* **Minimize MTTR** by quickly identifying unexpected changes
* **Improve change management** with complete visibility

### 3. Cost Optimization

* **Identify orphaned resources** created outside IaC
* **Detect oversized instances** from manual scaling
* **Prevent resource sprawl** from untracked changes

### 4. Team Productivity

* **Eliminate manual checks** with automation
* **Reduce debugging time** with clear drift reports
* **Build confidence** in infrastructure state

## Getting Started with Drift Detection

Ready to implement drift detection for your IDP? Here's your action plan:

### Quick Start Checklist

1. **Enable basic detection** (15 minutes)

   ```bash
   pulumi refresh --preview-only --stack production
   ```

2. **Set up scheduled detection** (30 minutes)
   * Configure [Pulumi Deployments](/docs/pulumi-cloud/deployments/get-started)
   * Create hourly detection schedule
   * Configure Slack notifications

3. **Monitor for one week** (ongoing)
   * Review drift patterns
   * Identify common causes
   * Document legitimate changes

4. **Implement remediation** (1-2 hours)
   * Start with non-production environments
   * Enable auto-remediation gradually
   * Monitor remediation success

5. **Optimize and scale** (ongoing)
   * Adjust schedules based on patterns
   * Implement custom workflows
   * Expand to all environments

## Conclusion: Day 2 Operations as a Competitive Advantage

Drift detection and remediation provide competitive advantages. Teams with robust day 2 operations can:

* **Move faster** with confidence in their infrastructure
* **Recover quickly** from incidents and changes
* **Maintain security** without slowing development
* **Scale operations** without scaling headcount

Automated drift detection reduces incidents, accelerates recovery, and improves team confidence.

## Next Steps

Resources for implementing drift detection:

### 📚 Documentation

**[Pulumi Deployments Drift Detection](/docs/pulumi-cloud/deployments/drift)
**[Pulumi Refresh Command](/docs/iac/cli/commands/pulumi_refresh)
**[Pulumi Service Provider](/registry/packages/pulumiservice)
**[Automation API Guide](/docs/using-pulumi/automation-api)

### 🎓 Workshops and Tutorials

**[Drift Detection Tutorial](/tutorials/drift-detection-and-remediation)

## Coming Next in the Series

In our next post, **"Extend Your IDP for AI Applications: GPUs, Models, and Cost Controls"**, we'll explore how to adapt your platform for AI workloads, including GPU orchestration, model deployment pipelines, and cost management strategies.

Until then, start small with drift detection: even a simple hourly check can prevent major incidents. Your future self (and your on-call team) will thank you.

---

**Ready to implement drift detection?** [Start your free Pulumi Cloud trial](https://app.pulumi.com/signup) and set up your first drift detection schedule in minutes. No credit card required.
