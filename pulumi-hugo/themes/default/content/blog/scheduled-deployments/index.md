---
title: "Pulumi Launches Scheduled Deployments: Automate Recurring Workflows"
allow_long_title: True
date: 2024-04-24T07:00:02-08:00
draft: false
meta_desc: Pulumi introduces Scheduled Deployments to enhance cloud management, allowing for automated operations based on customizable schedules.
meta_image: scheduled-deployments.png
authors:
    - meagan-cojocar
    - levi-blackstone
tags:
    - features
    - infrastructure-lifecycle-management
---

We are excited to announce __Scheduled Deployments__ for Pulumi Cloud. This new feature, which builds upon the robust foundation of Pulumi Deployments, is designed to streamline cloud management by automating the deployment and deactivation of resources according to customizable schedules. Two new Pulumi features also announced today, [Drift Detection and Remediation](/blog/drift-detection) and [Time-to-Live Stacks](/blog/ttl), are built on top of the new Scheduled Deployments functionality. These three new features are available today on the Enterprise and Business Critical editions of Pulumi Cloud.

### Simplifying Cloud Operations Through Automation

Scheduled Deployments enable precise automation of cloud operations, allowing users to schedule any Pulumi operation—such as `pulumi up`, `pulumi refresh`, `pulumi destroy`, or `pulumi preview`—for any stack with Pulumi Deployments. This feature is not just about automating routine tasks; it’s about enhancing operational efficiency, reducing costs, and deploying resources exactly when needed.

#### Example Use Cases

- **Automating Deployments outside of Git:** Pulumi Deployments handles Git based Deployments well, but we have heard from customers there are times you want to intentionally diverge from Git triggered Deployments, such as wanting to deploy only at set times ahead of a large usage event or deploy only on non-peak traffic times.
- **Cost Optimization:** Automatically power down non-critical development or test stacks during off-hours to cut unnecessary cloud spend. These stacks can be reactivated on a schedule or on-demand, ensuring resources are available precisely when teams need them without incurring costs during idle times.
- **Product Launches:** Configure infrastructure to deploy right before a major release with `pulumi up`, ensuring that all resources are aligned and active precisely for the event, eliminating the need for last-minute manual updates.
- **Scheduled Processing:** Perfect for tasks that require computing resources at specific times, such as nightly batch processing or periodic machine learning model training. Schedule these operations to maximize resource utilization and shut down upon task completion to optimize costs.

### How Scheduled Deployments Work

Users can define schedules for any Pulumi operation, on any stack, using cron expressions, which provide the flexibility to specify exact times for operations. This granular control over deployment timing allows for effective management of infrastructure tasks, accommodating even the most complex scheduling needs. Pulumi Deployments Schedules can be set up using the Pulumi Cloud console, our [REST API](/docs/pulumi-cloud/deployments/api) or managed in source control using the [Pulumi Service Provider](/registry/packages/pulumiservice/api-docs/provider).

### Integration with Existing Features

Scheduled Deployments integrate seamlessly with existing Pulumi Deployments. The concurrency limits of Pulumi Deployments apply and if deployments on a stack are paused, the scheduled deployments will queue, waiting for the pause to lift before executing. This integration ensures that all scheduled activities respect the operational parameters set within Pulumi Cloud.

## Getting Started with Scheduled Deployments

### Setting it up in the Pulumi Cloud Console

We'll walk through how to get up and running with Scheduled Deployments in the Pulumi Cloud console, REST API and Pulumi Service Provider. For more details on how to implement and maximize the benefits of Scheduled Deployments, please visit [our documentation](/docs/pulumi-cloud/deployments/schedules).

Setting up Scheduled Deployments via the Pulumi Cloud console is straightforward:

![Create a Scheduled Deployment](create-schedule.png)

In order to set up Scheduled Deployments in the Pulumi Cloud console, follow these steps:

1. Ensure Deployments Settings are configured on the stack [see the docs](/docs/pulumi-cloud/deployments/reference)
2. Navigate to the `Stack > Settings > Schedules` page
3. Select "Raw operation"
4. Select from the drop-down the type of operation you would like to schedule
5. Set the schedule using a cron expression
6. Save the Schedule

![Populated Schedule in the UI](raw-schedule.png)

Now you have a Scheduled Deployment!

The `Stack > Settings > Schedules` page will show all of the schedules configured for your stack, including Drift, TTL or Raw Operation schedules.

![List of schedules](schedules.png)

### Setting it up in the API

For those who prefer to automate and script their infrastructure tasks, Time-to-Live schedules can be configured programmatically using simple HTTP requests.

- Create a schedule
- Get a schedule for a stack
- Update or delete a schedule
- Pause or resume a schedule
- List all schedules in the organization (includes Drift and Time-to-Live schedules)

Below is an example of creating a Schedule on a stack programmatically:

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{ "scheduleCron":"0 0 * * *", "request": { "operation": "update" } }' \
  https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/deployments/schedules
```

Refer to the [Pulumi Deployments REST API documentation](/docs/pulumi-cloud/deployments/api) for more details on how to use the REST API to manage Scheduled Deployments.

### Setting it up in the Pulumi Service Provider

# Pulumi Service Provider for Creating a Raw Schedule

The Pulumi Service provider allows you to set up a raw schedule for operations like updates or deployments based on a specific time or a recurring schedule inside of source control.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```ts
import * as pulumi from "@pulumi/pulumi";
import * as pulumiservice from "@pulumi/pulumiservice";

const organizationName = "my-org";
const projectName = "my-project";
const stackName = "prod-stack";

const rawSchedule = new pulumiservice.DeploymentSchedule("rawSchedule", {
    organization: organizationName,
    project: projectName,
    stack: stackName,
    scheduleCron: "0 0 * * *", // Run an update daily at midnight
    pulumiOperation: pulumiservice.PulumiOperation.update
});

export const scheduleId = rawSchedule.scheduleId;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_pulumiservice as pulumiservice

organization_name = "my-org"
project_name = "my-project"
stack_name = "prod-stack"

# Create a raw deployment schedule
raw_schedule = pulumiservice.DeploymentSchedule("rawSchedule",
    organization=organization_name,
    project=project_name,
    stack=stack_name,
    schedule_cron="0 0 * * *",  # Run an update daily at midnight
    pulumi_operation=pulumiservice.PulumiOperation.update)

pulumi.export('scheduleId', raw_schedule.schedule_id)

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
        rawSchedule, err := pulumiservice.NewDeploymentSchedule(ctx, "rawSchedule", &pulumiservice.DeploymentScheduleArgs{
            Organization: pulumi.String("my-org"),
            Project: pulumi.String("my-project"),
            Stack: pulumi.String("prod-stack"),
            ScheduleCron: pulumi.String("0 0 * * *"),  // Run an update daily at midnight
            PulumiOperation: pulumiservice.PulumiOperationUpdate,
        })
        if err != nil {
            return err
        }

        ctx.Export("scheduleId", rawSchedule.ScheduleID)
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
        var rawSchedule = new PulumiService.DeploymentSchedule("rawSchedule", new PulumiService.DeploymentScheduleArgs
        {
            Organization = "my-org",
            Project = "my-project",
            Stack = "prod-stack",
            ScheduleCron = "0 0 * * *",  // Run an update daily at midnight
            PulumiOperation = PulumiService.PulumiOperation.Update,
        });

        return new Dictionary<string, object?>
        {
            { "scheduleId", rawSchedule.ScheduleId }
        };
    });
}

```

{{% /choosable %}}

{{% choosable language java %}}

```java
import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.pulumiservice.DeploymentSchedule;
import com.pulumi.pulumiservice.DeploymentScheduleArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    private static to stack(Context ctx) {
        var rawSchedule = new DeploymentSchedule("rawSchedule", DeploymentScheduleArgs.builder()
            .organization("my-org")
            .project("my-project")
            .stack("prod-stack")
            .scheduleCron("0 0 * * *") // Run an update daily at midnight
            .pulumiOperation(com.pulumi.pulumiservice.PulumiOperation.update())
            .build());

        ctx.export("scheduleId", rawSchedule.name());
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: raw-schedule-setup
runtime: yaml
description: Setup of a raw schedule for automatic operations with Pulumi

resources:
  rawSchedule:
    type: pulumiservice:index:DeploymentSchedule
    properties:
      organization: my-org
      project: my-project
      stack: prod-stack
      scheduleCron: "0 0 * * *" # Run an update daily at midnight
      pulumiOperation: update

outputs:
  scheduleId: ${rawSchedule.scheduleId}

```

{{% /choosable %}}

{{< /chooser >}}

See the [Pulumi Service Provider documentation](/registry/packages/pulumiservice/api-docs/provider) for more details on how to manage Scheduled Deployments in source control.

## Wrapping it up

We are looking forward to unlocking this capability to enable an out of the box way to automate your reoccuring workflows.

Happy building!
