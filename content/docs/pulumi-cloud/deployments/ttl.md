---
title_tag: "Time-to-live stacks"
meta_desc: Set a time-to-live on a stack, automatically destroying it when the one time schedule is set for.
title: "Time-to-live stacks"
h1: "Time-to-live stacks"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Time-to-live stacks
    parent: pulumi-cloud-deployments
    weight: 80
    identifier: pulumi-cloud-deployments-ttl
---

Time-to-live (TTL) Stacks in enable the automated management of a stack's lifecycle by specifying a date and time after which the stack is automatically torn down. TTL stacks allow platform teams to control costs, improve security posture, and reduce operational overhead by ensuring temporary or ephemeral cloud resources (like development environments) are automatically de-provisioned.

## Setting a Time-to-Live on a Stack

### Pulumi Cloud UI

In order to set up Time-to-Live Stacks in the Pulumi Cloud console, follow these steps:

1. Ensure Deployments Settings are configured on the stack [see the docs](/docs/pulumi-cloud/deployments/reference)
2. Navigate to the Stack > Settings > Schedules
3. Select "Time-to-Live"
4. (Optional) Turn on "Delete After Destroy" if applicable
5. Set the schedule using a cron expression
6. Save the Schedule

You will now see a schedule in the Schedules tab which highlights when the destroy will occur.

### REST API

For those who prefer to automate and script their infrastructure tasks, Time-to-Live schedules can be configured programmatically using simple HTTP requests.

- Create a Time-to-Live schedule
- Get a Time-to-Live schedule for a stack
- Update or delete a Time-to-Live schedule
- Pause or resume a Time-to-Live schedule
- List all schedules in the organization (includes raw Pulumi operations and Drift schedules)

Below is an example of setting up Time-To-Live on a stack programmatically:

```bash
  curl -H "Accept: application/vnd.pulumi+json" \
       -H "Content-Type: application/json" \
       -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
       --request POST \
       --data '{"timestamp":"2024-12-31T23:59:59Z","deleteAfterDestroy":true}' \
       https://api.pulumi.com/api/stacks/{organization}/{project}/{stack}/deployments/ttl/schedules
```

Refer to the [Pulumi Deployments REST API documentation](/docs/pulumi-cloud/reference/deployments/) for more details on how to use the REST API to manage Time-to-Live Stacks.

### Pulumi Cloud Service provider

The Pulumi Service Provider allows you to set up and manage Time-to-Live Stacks in source control.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```ts
import * as pulumi from "@pulumi/pulumi";
import * as pulumiservice from "@pulumi/pulumiservice";

const organizationName = "my-org";
const projectName = "my-project";
const stackName = "temp-stack";

const ttlSchedule = new pulumiservice.TtlSchedule("ttlSchedule", {
  organization: organizationName,
  project: projectName,
  stack: stackName,
  timestamp: "2024-01-01T00:00:00Z" // Specify the ISO date/time for destruction
});

export const scheduleId = ttlSchedule.scheduleId;

```

{{% /choosable %}}

{{% choosable language python %}}

```py
import pulumi
import pulumi_pulumiservice as pulumiservice

organization_name = "my-org"
project_name = "my-project"
stack_name = "temp-stack"

# Create a TTL schedule for stack destruction
ttl_schedule = pulumiservice.TtlSchedule("ttlSchedule",
    organization=organization_name,
    project=project_name,
    stack=stack_name,
    timestamp="2024-01-01T00:00:00Z") # Specify the ISO date/time for destruction

pulumi.export('scheduleId', ttl_schedule.schedule_id)
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
        ttlSchedule, err := pulumiservice.NewTtlSchedule(ctx, "ttlSchedule", &pulumiservice.TtlScheduleArgs{
            Organization: pulumi.String("my-org"),
            Project: pulumi.String("my-project"),
            Stack: pulumi.String("temp-stack"),
            Timestamp: pulumi.String("2024-01-01T00:00:00Z"),  // Specify the ISO date/time for destruction
        })
        if err != nil {
            return err
        }

        ctx.Export("scheduleId", ttlSchedule.ScheduleId)
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
        var ttlSchedule = new PulumiService.TtlSchedule("ttlSchedule", new PulumiService.TtlScheduleArgs
        {
            Organization = "my-org",
            Project = "my-project",
            Stack = "temp-stack",
            Timestamp = "2024-01-01T00:00:00Z",  // Specify the ISO date/time for destruction
        });

        return new Dictionary<string, object?>
        {
            { "scheduleID", ttlSchedule.ScheduleId }
        };
    });
}

```

{{% /choosable %}}

{{% choosable language java %}}

```java
import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.pulumiservice.TtlSchedule;
import com.pulumi.pulumiservice.TtlScheduleArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    private static void stack(Context ctx) {
        var ttlSchedule = new TtlSchedule("ttlSchedule", TtlScheduleArgs.builder()
            .organization("my-org")
            .project("my-project")
            .stack("temp-stack")
            .timestamp("2024-01-01T00:00:00Z") // Specify the ISO date/time for destruction
            .build());

        ctx.export("scheduleID", ttlSchedule.scheduleId());
    }
}

```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: ttl-schedule-setup
runtime: yaml
description: Setup of TTL for automatic resource destruction with Pulumi

resources:
  ttlSchedule:
    type: pulumiservice:index:TtlSchedule
    properties:
      organization: my-org
      project: my-project
      stack: temp-stack
      timestamp: "2024-01-01T00:00:00Z" # Specify the ISO date/time for destruction

outputs:
  scheduleId: ${ttlSchedule.scheduleId}

```

{{% /choosable %}}

{{< /chooser >}}

See the [Pulumi Service Provider documentation](/registry/packages/pulumiservice/api-docs/provider) for more details on how to manage Time-to-Live Stacks in source control.
