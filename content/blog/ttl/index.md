---
title: "Time-to-Live Stacks: Auto-Destroying Stacks"
allow_long_title: True
date: 2024-04-24T07:00:03-08:00
draft: false
meta_desc: Explore Pulumi Cloud's new Time-to-Live Stacks feature, designed to help teams manage infrastructure lifecycles and control cloud costs by automatically decommissioning stacks and resources.
meta_image: ttl.png
authors:
    - meagan-cojocar
tags:
    - features
    - infrastructure-lifecycle-management
---


In the dynamic landscape of cloud-based software development, platform teams face the continuous challenge of balancing the need for innovation with the imperative to control cloud costs and security. Pulumi Cloud's new __Time-to-Live (TTL) Stacks__ feature directly addresses this challenge by empowering teams to manage infrastructure lifecycles automatically, mitigating the risks associated with stale infrastructure and resource costs ballooning.

Creating temporary environments for development, testing, or staging is a common practice in the lifecycle of software development. These environments are crucial for running experiments, testing new features, and ensuring that everything works smoothly before going live. However, these environments often don't get decommissioned properly and linger, forgotten, consuming resources and adding unnecessary costs to your cloud bill.

Furthermore, managing these temporary stacks usually requires manual oversight, adding to the operational burden of your team. They need to track which environments are active, which are outdated, and manually shut them down to avoid security risks from idle and unmonitored resources. This process is not only time-consuming but also prone to human error, leading to either premature deletion of necessary resources or overlooked environments that pose security risks.

### Simplifying Stack Management with Time-to-Live Stacks

The Time-to-Live Stacks feature in Pulumi Cloud is designed to solve these pain points by allowing teams to set a predefined lifespan on any stack directly in Pulumi Cloud. After the specified time, these stacks are automatically destroyed, and using the optional "delete after destroy" setting, they are also removed from Pulumi Cloud entirely. This setting plays a pivotal role by not just destroying the resources but also cleaning up the stack itself after all resources have been terminated, ensuring that no residual artifacts are left behind. This maintains a clean state in the cloud environment and further reduces costs by reducing clutter. Time-to-Live Stacks are available today on the Enterprise and Business Critical editions of Pulumi Cloud.

### Key Benefits of TTL Stacks

- **Cost Control:** Automatically terminate stacks that are no longer needed, helping to avoid overspending on cloud resources that are not in active use.
- **Developer Enablement:** Provides developers the flexibility to quickly spin up and test application changes in sandbox environments without worrying about the cleanup.
- **Operational Efficiency:** Reduces the administrative burden of manually tracking and decommissioning temporary or outdated stacks, allowing teams to focus on more strategic tasks.
- **Enhanced Security:** Automatically removing unused or neglected stacks helps ensure compliance and reduces the potential attack surface, making your infrastructure safer.

## Getting Started with Time-to-Live Stacks

### Setting it up in the Pulumi Cloud Console

In order to set up Time-to-Live Stacks in the Pulumi Cloud console, follow these steps:

1. Ensure Deployments Settings are configured on the stack [see the docs](/docs/pulumi-cloud/deployments/reference)
2. Navigate to the `Stack > Settings > Schedules` page
3. Select "Time-to-Live"
4. (Optional) Turn on "Delete After Destroy" if applicable
5. Set the schedule using a cron expression
6. Save the Schedule

You will now see a schedule in the Schedules tab which highlights when the destroy will occur.

### Setting it up via the API

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

Refer to the [Pulumi Deployments REST API documentation](/docs/pulumi-cloud/deployments/api) for more details on how to use the REST API to manage Time-to-Live Stacks.

### Setting it up via the Pulumi Service Provider

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

## Wrapping it up

Time-to-Live Stacks has been one of the top requests from our Pulumi Cloud users, and we are thrilled to be making it available today. We look forward to further feedback on where Pulumi Cloud can best support your organizations' infrastructure lifecycle management needs.

Happy hacking!
