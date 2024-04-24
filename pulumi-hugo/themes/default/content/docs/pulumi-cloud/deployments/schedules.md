---
title: "Schedules"
title_tag: "Schedules"
h1: "Schedules"
meta_desc: Schedule any Pulumi operation to occur at any time.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumicloud:
    parent: deployments
    weight: 4
---

Scheduled Deployments in Pulumi Cloud introduce a robust capability to automate cloud operations, enabling more control over when and how infrastructure updates are applied. This feature is ideal for teams looking to enhance operational efficiency by automating routine tasks and ensuring that changes are made during optimal times, such as off-peak hours or predetermined maintenance windows.

Users can easily define schedules for any stack with Pulumi Deployments configured, using cron expressions to specify exact times for operations. This granular level of control allows for precise management of infrastructure tasks, accommodating complex scheduling needs. Scheduled Deployments build upon the existing infrastructure provided by Pulumi Deployments, enhancing it with the flexibility to manage deployment timing extensively. This means Pulumi Deployments concurrency limits apply to scheduled deployments and pausing deployments on a stack will queue scheduled deployments as well.

## Pulumi Cloud UI

In order to set up a deployment schedule in the Pulumi Cloud console, follow these steps:

<!-- markdownlint-disable ol-prefix -->
1. Ensure Deployments Settings are configured on the stack [see the docs](/docs/pulumi-cloud/deployments/reference)
2. Navigate to the Stack > Settings > Schedules

![Schedule](../schedule.png)

3. Select "Drift"
4. (Optional) Turn on auto-remediation if applicable
5. Set the schedule using a cron expression
6. Save the Schedule
<!-- markdownlint-enable ol-prefix -->
![Populated Schedule in the UI](../raw-schedule.png)

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

### Pulumi Cloud Service provider

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
