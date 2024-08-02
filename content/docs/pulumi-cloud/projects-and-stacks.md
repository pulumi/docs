---
title_tag: "Pulumi Cloud: Project and Stack Management"
meta_desc: Learn how to manage projects and stacks in the Pulumi Cloud, including creating a project and managing stack permissions.
title: "Projects & stacks"
h1: "Projects & stacks"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumicloud:
    weight: 3
aliases:
- /docs/intro/console/project-and-stack-management/
- /docs/reference/service/roles-and-access-controls/
- /docs/console/collaboration/stack-permissions/
- /docs/intro/console/stack-permissions/
- /docs/intro/console/projects-and-stacks/
- /docs/intro/pulumi-service/projects-and-stacks/
- /docs/intro/pulumi-cloud/projects-and-stacks/
search:
  keywords:
    - delete a stack
    - deleting a stack
    - delete a stack in Pulumi cloud
---

Projects group stacks together and contain a Pulumi.yaml file.
Stacks are isolated, independently configurable instances of a Pulumi program.
Projects can have as many stacks as you need.

## Creating a Project

To create a project:

1. Navigate to **All stacks**.
1. Select **Create project**.
1. Select a cloud and a language and use the **Next** button.
1. Optionally, change your project name and project description.
1. Select **Create project**.
1. Follow the provided CLI command instructions.

## Stack Permissions

The Pulumi Cloud provides fine-grained access controls for stacks. Stack permissions are
based on the member's role within the organization and their team membership.
Additionally, any member who creates a stack is granted admin permissions on that stack.

Organization admins can control the stack default permissions at the organization level from **Settings** > **Access Management**.
There are four types of stack permissions: `None`, `Read`, `Write`, and `Admin`.
[Team permissions](/docs/pulumi-cloud/access-management/teams#team-permissions) will expand these default permissions.

Stack permissions allow users to perform the following actions:

| Action | None | Read | Write | Admin |
|--------|------|------|-------|-------|
| View update history | | ✅ | ✅ | ✅ |
| Decrypt secret configuration | | ✅ | ✅ | ✅ |
| Read stack resources | | ✅ | ✅ | ✅ |
| Preview stack changes | | ✅ | ✅ | ✅ |
| Update stack | | | ✅ | ✅ |
| Destroy stack (`pulumi destroy`) | |   | ✅ | ✅ |
| Export stack checkpoint | | ✅ | ✅ | ✅ |
| Import stack checkpoint |  | | ✅ | ✅ |
| Delete stack (`pulumi stack rm`) |   |   |   | ✅ |
| Transfer to another organization |   |   |   | ✅ |
| Search stack resources           |   |  ✅ |  ✅ | ✅ |

## Viewing Stacks

![Organization projects and stacks](/images/docs/reference/service/organization-stacks.png)

To view an organization's stacks:

1. Navigate to **All stacks**.
1. Optionally, adjust the grouping by selecting the **Group By** and **Sort By** controls.
1. To view a stack's details, select the stack's name.
1. To view a specific stack update, navigate to **Activity** and select it from the list.

## Stack Favorites

Stack favorites allow you to label specific stacks for quick and easy access. Stack favorites are displayed in the navigation and on your dashboard.

![""](/images/docs/reference/service/stacks-navigation-favorites-card.png)

### Favorite a Stack

1. Navigate to the stack.
1. Select the star icon next to the stack name.

### Stack README

To add a README to a stack:

1. Export a [Stack output](/learn/building-with-pulumi/stack-outputs) named `readme` that contains your templated Stack README markdown, commonly by reading a file, i.e. `Pulumi.README.md`.
2. Create a README template for the Stack.
3. Run `pulumi up` on that Stack.
4. Navigate to **All stacks** and then select the stack.
5. Navigate to **README**.

Examples for adding the Stack Output `readme` to a Pulumi program:

{{< chooser language "typescript,python,go,csharp,java" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import { readFileSync } from "fs";

const loggroup = new aws.cloudwatch.LogGroup("loggroup", {});
const dashboard = new aws.cloudwatch.Dashboard("dashboard", {
    dashboardName: "mydashboard",
    dashboardBody: JSON.stringify({
        widgets: [
            {
                type: "metric",
                x: 0,
                y: 0,
                width: 12,
                height: 6,
                properties: {
                    metrics: [[
                        "AWS/EC2",
                        "CPUUtilization",
                        "InstanceId",
                        "i-012345",
                    ]],
                    period: 300,
                    stat: "Average",
                    region: "us-east-1",
                    title: "EC2 Instance CPU",
                },
            },
            {
                type: "text",
                x: 0,
                y: 7,
                width: 3,
                height: 3,
                properties: {
                    markdown: "Hello world",
                },
            },
        ],
    }),
});
const database = new aws.rds.Cluster("database", {
    clusterIdentifier: "aurora-cluster-demo",
    engine: aws.rds.EngineType.AuroraPostgresql,
    availabilityZones: [
        "us-west-2a",
        "us-west-2b",
        "us-west-2c",
    ],
    databaseName: "mydb",
    masterUsername: "foo",
    masterPassword: "must_be_eight_characters",
    backupRetentionPeriod: 5,
    preferredBackupWindow: "07:00-09:00",
    skipFinalSnapshot: true,
});
const instance = new aws.rds.ClusterInstance("instance", {
    clusterIdentifier: database.clusterIdentifier,
    instanceClass: aws.rds.InstanceType.R5_Large,
    engine: "aurora-postgresql",
    engineVersion: "15.4",
    performanceInsightsEnabled: true,
});

export const dashboardName = dashboard.dashboardName;
export const cloudwatchLogGroup = loggroup.name;
export const instanceId = instance.id;
export const dbResourceId = instance.dbiResourceId;
export const readme = readFileSync("./Pulumi.readme.md").toString();
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import json
import pulumi_aws as aws

loggroup = aws.cloudwatch.LogGroup("loggroup")
dashboard = aws.cloudwatch.Dashboard("dashboard",
    dashboard_name="mydashboard",
    dashboard_body=json.dumps({
        "widgets": [
            {
                "type": "metric",
                "x": 0,
                "y": 0,
                "width": 12,
                "height": 6,
                "properties": {
                    "metrics": [[
                        "AWS/EC2",
                        "CPUUtilization",
                        "InstanceId",
                        "i-012345",
                    ]],
                    "period": 300,
                    "stat": "Average",
                    "region": "us-east-1",
                    "title": "EC2 Instance CPU",
                },
            },
            {
                "type": "text",
                "x": 0,
                "y": 7,
                "width": 3,
                "height": 3,
                "properties": {
                    "markdown": "Hello world",
                },
            },
        ],
    }))
database = aws.rds.Cluster("database",
    cluster_identifier="aurora-cluster-demo",
    engine=aws.rds.EngineType.AURORA_POSTGRESQL,
    availability_zones=[
        "us-west-2a",
        "us-west-2b",
        "us-west-2c",
    ],
    database_name="mydb",
    master_username="foo",
    master_password="must_be_eight_characters",
    backup_retention_period=5,
    preferred_backup_window="07:00-09:00",
    skip_final_snapshot=True)
instance = aws.rds.ClusterInstance("instance",
    cluster_identifier=database.cluster_identifier,
    instance_class=aws.rds.InstanceType.R5_LARGE,
    engine="aurora-postgresql",
    engine_version="15.4",
    performance_insights_enabled=True)

pulumi.export("dashboardName", dashboard.dashboard_name)
pulumi.export("cloudwatchLogGroup", loggroup.name)
pulumi.export("instanceId", instance.id)
pulumi.export("dbResourceId", instance.dbi_resource_id)
with open('./Pulumi.README.md') as f:
    pulumi.export('readme', f.read())
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"encoding/json"

	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/cloudwatch"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/rds"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
  pulumi.Run(func(ctx *pulumi.Context) error {
    loggroup, err := cloudwatch.NewLogGroup(ctx, "loggroup", nil)
    if err != nil {
      return err
    }
    dashboardJson, err := json.Marshal(map[string]interface{}{
      "widgets": []interface{}{
        map[string]interface{}{
          "type":   "metric",
          "x":      0,
          "y":      0,
          "width":  12,
          "height": 6,
          "properties": map[string]interface{}{
          "metrics": [][]string{
            []string{
              "AWS/EC2",
              "CPUUtilization",
              "InstanceId",
              "i-012345",
            },
          },
            "period": 300,
            "stat":   "Average",
            "region": "us-east-1",
            "title":  "EC2 Instance CPU",
          },
        },
        map[string]interface{}{
          "type":   "text",
          "x":      0,
          "y":      7,
          "width":  3,
          "height": 3,
          "properties": map[string]interface{}{
            "markdown": "Hello world",
          },
        },
      },
    })
    if err != nil {
      return err
    }
    json0 := string(dashboardJson)
    dashboard, err := cloudwatch.NewDashboard(ctx, "dashboard", &cloudwatch.DashboardArgs{
      DashboardName: pulumi.String("mydashboard"),
      DashboardBody: pulumi.String(json0),
    })
    if err != nil {
      return err
    }
    database, err := rds.NewCluster(ctx, "database", &rds.ClusterArgs{
      ClusterIdentifier: pulumi.String("aurora-cluster-demo"),
      Engine:            pulumi.String(rds.EngineTypeAuroraPostgresql),
      AvailabilityZones: pulumi.StringArray{
        pulumi.String("us-west-2a"),
        pulumi.String("us-west-2b"),
        pulumi.String("us-west-2c"),
      },
      DatabaseName:          pulumi.String("mydb"),
      MasterUsername:        pulumi.String("foo"),
      MasterPassword:        pulumi.String("must_be_eight_characters"),
      BackupRetentionPeriod: pulumi.Int(5),
      PreferredBackupWindow: pulumi.String("07:00-09:00"),
      SkipFinalSnapshot:     pulumi.Bool(true),
    })
    if err != nil {
      return err
    }
    instance, err := rds.NewClusterInstance(ctx, "instance", &rds.ClusterInstanceArgs{
      ClusterIdentifier:          database.ClusterIdentifier,
      InstanceClass:              pulumi.String(rds.InstanceType_R5_Large),
      Engine:                     pulumi.String("aurora-postgresql"),
      EngineVersion:              pulumi.String("15.4"),
      PerformanceInsightsEnabled: pulumi.Bool(true),
    })
    if err != nil {
      return err
    }

    readme, err := os.ReadFile("./Pulumi.README.md")
    if err != nil {
      return fmt.Errorf("failed to read readme: %w", err)
    }
    ctx.Export("dashboardName", dashboard.DashboardName)
    ctx.Export("cloudwatchLogGroup", loggroup.Name)
    ctx.Export("instanceId", instance.ID())
    ctx.Export("dbResourceId", instance.DbiResourceId)
    ctx.Export("readme", pulumi.String(string(readme)))
    return nil
  })
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Text.Json;
using Pulumi;
using Aws = Pulumi.Aws;
using System.IO;

return await Deployment.RunAsync(() => 
{
    var loggroup = new Aws.CloudWatch.LogGroup("loggroup");

    var dashboard = new Aws.CloudWatch.Dashboard("dashboard", new()
    {
        DashboardName = "mydashboard",
        DashboardBody = JsonSerializer.Serialize(new Dictionary<string, object?>
        {
            ["widgets"] = new[]
            {
                new Dictionary<string, object?>
                {
                    ["type"] = "metric",
                    ["x"] = 0,
                    ["y"] = 0,
                    ["width"] = 12,
                    ["height"] = 6,
                    ["properties"] = new Dictionary<string, object?>
                    {
                        ["metrics"] = new[]
                        {
                            new[]
                            {
                                "AWS/EC2",
                                "CPUUtilization",
                                "InstanceId",
                                "i-012345",
                            },
                        },
                        ["period"] = 300,
                        ["stat"] = "Average",
                        ["region"] = "us-east-1",
                        ["title"] = "EC2 Instance CPU",
                    },
                },
                new Dictionary<string, object?>
                {
                    ["type"] = "text",
                    ["x"] = 0,
                    ["y"] = 7,
                    ["width"] = 3,
                    ["height"] = 3,
                    ["properties"] = new Dictionary<string, object?>
                    {
                        ["markdown"] = "Hello world",
                    },
                },
            },
        }),
    });

    var database = new Aws.Rds.Cluster("database", new()
    {
        ClusterIdentifier = "aurora-cluster-demo",
        Engine = Aws.Rds.EngineType.AuroraPostgresql,
        AvailabilityZones = new[]
        {
            "us-west-2a",
            "us-west-2b",
            "us-west-2c",
        },
        DatabaseName = "mydb",
        MasterUsername = "foo",
        MasterPassword = "must_be_eight_characters",
        BackupRetentionPeriod = 5,
        PreferredBackupWindow = "07:00-09:00",
        SkipFinalSnapshot = true,
    });

    var instance = new Aws.Rds.ClusterInstance("instance", new()
    {
        ClusterIdentifier = database.ClusterIdentifier,
        InstanceClass = Aws.Rds.InstanceType.R5_Large,
        Engine = "aurora-postgresql",
        EngineVersion = "15.4",
        PerformanceInsightsEnabled = true,
    });

    var readme = Output.Create(File.ReadAllText("./Pulumi.README.md"));

    return new Dictionary<string, object?>
    {
        ["dashboardName"] = dashboard.DashboardName,
        ["cloudwatchLogGroup"] = loggroup.Name,
        ["instanceId"] = instance.Id,
        ["dbResourceId"] = instance.DbiResourceId,
        ["readme"] = readme
    };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.aws.cloudwatch.LogGroup;
import com.pulumi.aws.cloudwatch.Dashboard;
import com.pulumi.aws.cloudwatch.DashboardArgs;
import com.pulumi.aws.rds.Cluster;
import com.pulumi.aws.rds.ClusterArgs;
import com.pulumi.aws.rds.ClusterInstance;
import com.pulumi.aws.rds.ClusterInstanceArgs;
import static com.pulumi.codegen.internal.Serialization.*;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var loggroup = new LogGroup("loggroup");

        var dashboard = new Dashboard("dashboard", DashboardArgs.builder()
            .dashboardName("mydashboard")
            .dashboardBody(serializeJson(
                jsonObject(
                    jsonProperty("widgets", jsonArray(
                        jsonObject(
                            jsonProperty("type", "metric"),
                            jsonProperty("x", 0),
                            jsonProperty("y", 0),
                            jsonProperty("width", 12),
                            jsonProperty("height", 6),
                            jsonProperty("properties", jsonObject(
                                jsonProperty("metrics", jsonArray(jsonArray(
                                    "AWS/EC2", 
                                    "CPUUtilization", 
                                    "InstanceId", 
                                    "i-012345"
                                ))),
                                jsonProperty("period", 300),
                                jsonProperty("stat", "Average"),
                                jsonProperty("region", "us-east-1"),
                                jsonProperty("title", "EC2 Instance CPU")
                            ))
                        ), 
                        jsonObject(
                            jsonProperty("type", "text"),
                            jsonProperty("x", 0),
                            jsonProperty("y", 7),
                            jsonProperty("width", 3),
                            jsonProperty("height", 3),
                            jsonProperty("properties", jsonObject(
                                jsonProperty("markdown", "Hello world")
                            ))
                        )
                    ))
                )))
            .build());

        var database = new Cluster("database", ClusterArgs.builder()
            .clusterIdentifier("aurora-cluster-demo")
            .engine("aurora-postgresql")
            .availabilityZones(            
                "us-west-2a",
                "us-west-2b",
                "us-west-2c")
            .databaseName("mydb")
            .masterUsername("foo")
            .masterPassword("must_be_eight_characters")
            .backupRetentionPeriod(5)
            .preferredBackupWindow("07:00-09:00")
            .skipFinalSnapshot(true)
            .build());

        var instance = new ClusterInstance("instance", ClusterInstanceArgs.builder()
            .clusterIdentifier(database.clusterIdentifier())
            .instanceClass("db.r5.large")
            .engine("aurora-postgresql")
            .engineVersion("15.4")
            .performanceInsightsEnabled(true)
            .build());

        ctx.export("dashboardName", dashboard.dashboardName());
        ctx.export("cloudwatchLogGroup", loggroup.name());
        ctx.export("instanceId", instance.id());
        ctx.export("dbResourceId", instance.dbiResourceId());

        try {
            var readme = Files.readString(Paths.get("./Pulumi.README.md"));
            ctx.export("readme", Output.of(readme));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
```

{{% /choosable %}}

An example of a README file, `Pulumi.README.md`, the template Stack README file for the Pulumi Cloud.

```markdown
# Pulumi Cloud README
​
[Sign in to AWS to view stack resources!](https://top-secret-url.com)
​
## On Call Operations
​
### Monitor
​
1. [Cloudwatch Metrics](https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#dashboards:name=${outputs.dashboardName}): Monitor holistic metrics tracking overall service health
2. [RDS Performance Metrics](https://us-west-2.console.aws.amazon.com/rds/home?region=us-west-2#performance-insights-v20206:/resourceId/${outputs.dbResourceId}/resourceName/${outputs.instanceId}/presetKey/1h/presetUnit/hour/presetAmount/1): Monitor RDS performance (wait times, top queries)
3. [Cloudwatch Logs](https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#logStream:group=${outputs.cloudwatchLogGroup}): Search across service logs
```

Here is how it looks rendered in the [Pulumi Cloud UI](https://app.pulumi.com):

![Stack READMEs](/images/docs/reference/service/stack-readme.png)

### Stack Detailed View

To view a stack's details:

1. Navigate to **Stacks** and then a specific stack.
1. Navigate to **Activity**.
1. Review the stack's outputs, configuration values, and tags.

![Stack outputs and configuration](/images/docs/reference/service/stack-outputs-and-configuration.png)

You can see other details, such as who applied the update, when, and counts of added, updated, and unchanged resources. If your stack is integrated with a CI/CD pipeline, such as [GitHub Actions](/docs/using-pulumi/continuous-delivery/github-actions/), you also see useful links to data like your Git commit hash, mapped branch, and pull request ID.

#### Custom Stack Tags

Custom stack tags can help you group and filter your stacks.

To create a custom tag:

1. Navigate to **Stacks** and then a specific stack.
1. Select **New tag**.

To modify or delete a custom tag:

1. Navigate to **All stacks** and then a specific stack.
1. To modify a custom tag, use the pencil icon.
1. To delete a custom tag, use the trash can icon.

#### Stack Activity

To view stack activity:

1. Navigate to **Stacks** and then a specific stack.
1. Navigate to **Activity**.
1. Review insights and operations that were performed on your stack resources during the update.
1. Navigate to **Changes**, **Timeline**, or **Configuration** for more details.

The **Changes** section of activity lets you toggle between different log views:

* _Summary Log_ lists a summary of changes, counts of affected resources, and update duration
* _Diff Log_ displays a diff of the changes (created, updated, or deleted resources), your stack outputs, and the same counts and update duration shown in the Summary Log view.
* _Diagnostic Log_ displays warning messages or a description of the operations performed during the update (if any).

![Stack resource graph](/images/docs/reference/service/resource-changes.png)

The **Timeline** section provides a detailed timeline of changes to individual cloud resources. It also includes useful resource links and counts of affected resources.

![Stack resource graph timeline](/images/docs/reference/service/timeline.png)

The **Configuration** section displays the same configuration details found in the Stack view for your update.

#### Stack Resources

To view a stack's resources:

1. Navigate to **Stacks** and then a specific stack.
1. Navigate to **Resources**.
1. Select **List View** or **Graph View** to toggle between a list view and a graph view.
1. Selecting an individual resource from the list or graph view will provide more details.

The list view displays a list of all of the stack's resources, including their type, name,
status, and link to the associated cloud provider.

![Stack resource list](/images/docs/reference/service/stack-resource-list.png)

The graph view displays a graphical representation of the stack's resources and their
dependencies. Select an individual resource to view its list of properties and dependencies.

![Stack resource visualization](/images/docs/reference/service/stack-resource-visualization.png)

## Transferring Stacks

Stack admins can transfer individual stacks between personal accounts and organizations or between organizations. Organization admins can transfer stacks in bulk.

If transferring to an organization, the **Allow organization members to create stacks and transfer stacks to this organization**
setting must be turned on from the **Access Management** page in the organization's settings.

To transfer an individual stack:

1. Navigate to the stack, and then the stack's **Settings**.
1. Select **Transfer stack**.
1. Provide the personal account or organization name and select **Transfer**.

To transfer stacks in bulk:

1. Navigate to the **Stacks** page.
2. Select the three dot menu beside **Create project**.
3. Choose **Transfer stacks** from the dropdown.
4. Choose the **Transfer destination** from the dropdown.
5. Tick the stacks you'd like to transfer and select **Transfer stacks**.

## Deleting a Stack

Deleting a stack removes the stack entirely from the Pulumi Cloud, along with all of its update history.

To delete a stack:

1. Navigate to the **Stacks** page and then a specific stack.
1. Navigate to the stack's **Settings** and then **Options**.
1. If you have no resources in the stack use the **Delete stack** button, otherwise use the provided CLI commands.

## Restoring a Stack

{{% notes type="info" %}}
The ability to restore a deleted stack is limited to Enterprise and Business Critical Editions. {{% /notes %}}
Restoring a stack allows you to recover a previously deleted stack, either because it was accidentally deleted or because you want to restore its history. The last 25 stacks deleted in your organization can be restored by an organization admin. Stacks can only be restored if deleted within the last year.

To restore a stack:

1. Navigate to the **Stacks** page.
2. Select the three dot menu beside **Create project**.
3. Choose **Restore deleted stacks** from the dropdown.
4. Use the three dot menu on the stack you want to restore and select **Restore stack**.

## Related Blogs

* [Building New Pulumi Projects and Stacks From Templates](/blog/building-new-pulumi-projects-and-stacks-from-templates/)
