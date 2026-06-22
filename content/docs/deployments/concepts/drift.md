---
title: "Drift detection and remediation"
title_tag: "Drift detection and remediation"
h1: "Drift detection and remediation"
meta_desc: Detect and remediate infrastructure drift on a schedule with Pulumi Cloud — the Drift tab, auto-remediation, and webhook notifications.
meta_image: /images/docs/meta-images/docs-meta.png
aliases:
- /docs/deployments/deployments/drift/
- /docs/pulumi-cloud/deployments/drift/
- /docs/platform/deployments/drift/
menu:
  deployments:
    name: Drift Detection
    parent: deployments-concepts
    weight: 40
    identifier: deployments-concepts-drift
---

This page covers the drift detection and remediation capabilities that Pulumi Cloud manages for you: scheduled drift runs, the Drift tab, automatic remediation, and notifications. For the conceptual foundation — the difference between desired, current, and actual state, how to choose between remediation and adoption, and the underlying CLI workflow — see [Detecting and reconciling drift](/docs/iac/operations/stack-management/drift/).

Drift is the gap between the actual state of your cloud resources and the state Pulumi has recorded for them. It most often comes from manual, out-of-band changes ("click-ops") or from changes a cloud resource makes over its own lifecycle. Pulumi Cloud detects drift by running a preview-only refresh against your stack, and it can remediate drift — re-applying your program so the cloud matches your desired state — automatically.

To use drift detection and remediation with Pulumi Deployments, you must first configure the [deployment settings](/docs/deployments/concepts/settings/) for your stack.

## Running drift detection from the CLI

Any preview of a refresh counts as a drift detection run in Pulumi Cloud. To run drift detection from the CLI, use `pulumi refresh --preview-only`, or `pulumi refresh`, which runs a preview (creating the drift run) before performing the actual refresh.

After your run completes, you can see it in the [Drift tab](#drift-tab) for your stack, alongside any scheduled runs.

For the full CLI workflow — detection, remediation, adoption, and `--expect-no-changes` for CI — see [Detecting and reconciling drift](/docs/iac/operations/stack-management/drift/).

## Pulumi Cloud UI

### Running via Click to Deploy

You can run a drift or remediate-drift run ad hoc from your stack using the **Click to Deploy** menu, which lists the operations available for the stack. Select **Detect drift** to run a preview-only refresh, or **Remediate drift** to reconcile any detected drift. Both runs appear in the Drift tab when they complete.

### Drift tab

The Drift tab on the stack page is where every drift run surfaces, no matter how the run started — from the CLI, from Click to Deploy, or on a schedule. When the stack is currently in a drifted state, a warning bell icon appears on the tab. If a run detects drift, its information card includes a diff summary of the changes.

### Configuring drift detection on a schedule

To set up drift detection and remediation in the Pulumi Cloud console, follow these steps:

<!-- markdownlint-disable ol-prefix -->
1. Ensure deployment settings are configured on the stack ([see the docs](/docs/deployments/concepts/settings/)).
2. Navigate to **Stack > Settings > Schedules**.
3. Select **Drift**.
4. (Optional) Turn on auto-remediation if applicable. With auto-remediation enabled, Pulumi Cloud runs `pulumi up --refresh` after a detection run finds drift, reconciling the cloud back to your program's desired state.
5. Set the schedule using a cron expression.
6. Save the schedule.
<!-- markdownlint-enable ol-prefix -->

### Configuring notifications for drift detection

You can route drift notifications to Slack, Microsoft Teams, and more using the Pulumi [Webhooks](/docs/deployments/concepts/webhooks/) integration.

1. Navigate to **Stack > Settings > Webhooks**.
1. Select your desired webhook format.
1. Give your webhook a display name, destination URL, and optional secret.
1. All events include drift events, but you can also filter the events down to drift events only.

### Summary of drift detection and remediation events

* Drift detected - A drift run detected drift.
* Drift detection succeeded - A drift run succeeded, regardless of whether it detected drift or not.
* Drift detection failed - A drift run failed to finish.
* Drift remediation succeeded - A drift remediation run succeeded.
* Drift remediation failed - A drift remediation run failed to finish.

### Setting it up via the REST API

For those who prefer to automate and script their infrastructure tasks, drift detection and remediation can be configured programmatically using HTTP requests. The available endpoints are:

* Create a drift schedule
* Get a drift schedule
* Update or delete a drift schedule
* Pause or resume a drift schedule
* List all schedules (includes raw Pulumi operations and time-to-live schedules)

Below is an example of setting up drift detection and remediation on a stack. See the [Pulumi Deployments REST API documentation](/docs/deployments/deployments/api) for more details on configuring drift detection and remediation programmatically.

**Create a drift detection and remediation schedule:**

```bash
curl -H "Accept: application/vnd.pulumi+json" \
     -H "Content-Type: application/json" \
     -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
     --request POST \
     --data '{"scheduleCron":"0 0 * * *","autoRemediate":true}' \
     https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/deployments/drift/schedules
```

### Setting it up via the Pulumi Service Provider

The Pulumi Service Provider allows you to set up automated drift detection and remediation in source control.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as pulumiservice from "@pulumi/pulumiservice";

const organizationName = "my-org";
const projectName = "my-project";
const stackName = "production";

// Creating a DriftSchedule for automatically running drift detection
const driftDetectionSchedule = new pulumiservice.DriftSchedule("driftDetectionSchedule", {
    organization: organizationName,
    project: projectName,
    stack: stackName,
    scheduleCron: "0 0 * * *", // Run drift detection daily at midnight
    autoRemediate: true, // Automatically remediate any drift detected
});

export const driftScheduleId = driftDetectionSchedule.scheduleId;

```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_pulumiservice as pulumiservice

organization_name = "my-org"
project_name = "my-project"
stack_name = "production"

# Create a drift detection schedule
drift_detection_schedule = pulumiservice.DriftSchedule("driftDetectionSchedule",
    organization=organization_name,
    project=project_name,
    stack=stack_name,
    schedule_cron="0 0 * * *",  # Run drift detection daily at midnight
    auto_remediate=True)  # Automatically remediate any drift detected

pulumi.export('driftScheduleId', drift_detection_schedule.schedule_id)

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
        driftDetectionSchedule, err := pulumiservice.NewDriftSchedule(ctx, "driftDetectionSchedule", &pulumiservice.DriftScheduleArgs{
            Organization: pulumi.String("my-org"),
            Project: pulumi.String("my-project"),
            Stack: pulumi.String("production"),
            ScheduleCron: pulumi.String("0 0 * * *"),  // Run drift detection daily at midnight
            AutoRemediate: pulumi.Bool(true),  // Automatically remediate any drift detected
        })
        if err != nil {
            return err
        }

        ctx.Export("driftScheduleId", driftDetectionSchedule.ScheduleId)
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
        var driftDetectionSchedule = new PulumiService.DriftSchedule("driftDetectionSchedule", new PulumiService.DriftScheduleArgs
        {
            Organization = "my-org",
            Project = "my-project",
            Stack = "production",
            ScheduleCron = "0 0 * * *",  // Run drift detection daily at midnight
            AutoRemediate = true,  // Automatically remediate any drift detected
        });

        return new Dictionary<string, object?>
        {
            { "driftScheduleId", driftDetectionSchedule.ScheduleId }
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
        var driftDetectionSchedule = new DriftSchedule("driftDetectionSchedule", DriftScheduleArgs.builder()
            .organization("my-org")
            .project("my-project")
            .stack("production")
            .scheduleCron("0 0 * * *") // Run drift detection daily at midnight
            .autoRemediate(true) // Automatically remediate any drift detected
            .build());

        ctx.export("driftScheduleId", driftDetectionSchedule.scheduleId());
    }
}

```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: drift-detection-setup
runtime: yaml
description: Setup of automated drift detection with Pulumi

resources:
  driftDetectionSchedule:
    type: pulumiservice:index:DriftSchedule
    properties:
      organization: my-org
      project: my-project
      stack: production
      scheduleCron: "0 0 * * *" # Run drift detection daily at midnight
      autoRemediate: true # Automatically remediate any drift detected

outputs:
  driftScheduleId: ${driftDetectionSchedule.scheduleId}

```

{{% /choosable %}}

{{< /chooser >}}

See the [Pulumi Service Provider documentation](/registry/packages/pulumiservice/api-docs/provider) for more details on managing drift detection and remediation in source control.

## See also

* [Detecting and reconciling drift](/docs/iac/operations/stack-management/drift/) - the conceptual foundation and the CLI workflow.
* [Schedules](/docs/deployments/concepts/schedules/) - schedule any Pulumi operation, not just drift.
* [Webhooks](/docs/deployments/concepts/webhooks/) - route drift events to Slack, Microsoft Teams, or any HTTP endpoint.
