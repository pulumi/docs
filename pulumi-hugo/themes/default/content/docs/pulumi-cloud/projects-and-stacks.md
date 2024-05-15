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
import { readFileSync } from "fs";
export const strVar = "foo";
export const arrVar = ["fizz", "buzz"];
// add readme to stack outputs. must be named "readme".
export const readme = readFileSync("./Pulumi.README.md").toString();
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
pulumi.export('strVar', 'foo')
pulumi.export('arrVar', ['fizz', 'buzz'])
# open template readme and read contents into stack output
with open('./Pulumi.README.md') as f:
    pulumi.export('readme', f.read())
```

{{% /choosable %}}

{{% choosable language go %}}

```go
func main() {
  pulumi.Run(func(ctx *pulumi.Context) error {
    strVar := "foo"
    arrVar := []string{"fizz", "buzz"}
    readmeBytes, err := ioutil.ReadFile("./Pulumi.README.md")
    if err != nil {
      return fmt.Errorf("failed to read readme: %w", err)
    }
    ctx.Export("strVar", pulumi.String(strVar))
    ctx.Export("arrVar", pulumi.ToStringArray(arrVar))
    ctx.Export("readme", pulumi.String(string(readmeBytes)))
    return nil
  })
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
class MyStack : Stack
{
    public MyStack()
    {
        this.StrVar = "foo";
        this.ArrVar = new string[] { "fizz", "buzz" };
        this.Readme = Output.Create(System.IO.File.ReadAllText("./Pulumi.README.md"));
    }
    [Output]
    public Output<string> StrVar { get; set; }
    [Output]
    public Output<string[]> ArrVar { get; set; }
    [Output]
    public Output<string> Readme { get; set; }
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package stackreadme;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var strVar = "foo";
            var arrVar = new String[]{ "fizz", "buzz" };
            try {
                var readme = Files.readString(Paths.get("./Pulumi.README.md"));
                ctx.export("strVar", Output.of(strVar));
                ctx.export("arrVar", Output.of(arrVar));
                ctx.export("readme", Output.of(readme));
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });
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
2. [RDS Performance Metrics](https://us-west-2.console.aws.amazon.com/rds/home?region=us-west-2#performance-insights-v20206:/resourceId/${database.databaseCluster.id}/resourceName/${outputs.rdsClusterWriterInstance}): Monitor RDS performance (wait times, top queries)
3. [Cloudwatch Logs](https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#logStream:group=${outputs.cloudwatchLogGroup}): Search across service logs
```

Here is how it looks rendered in the [Pulumi Cloud UI](https://app.pulumi.com):

![Stack READMEs](/images/docs/reference/service/stack-readme.png)

### Stack Detailed View

To view a stack's details:

1. Navigate to **All stacks** and then a specific stack.
1. Navigate to **Activity**.
1. Review the stack's outputs, configuration values, and tags.

![Stack outputs and configuration](/images/docs/reference/service/stack-outputs-and-configuration.png)

You can see other details, such as who applied the update, when, and counts of added, updated, and unchanged resources. If your stack is integrated with a CI/CD pipeline, such as [GitHub Actions](/docs/using-pulumi/continuous-delivery/github-actions/), you also see useful links to data like your Git commit hash, mapped branch, and pull request ID.

#### Custom Stack Tags

Custom stack tags can help you group and filter your stacks.

To create a custom tag:

1. Navigate to **All stacks** and then a specific stack.
1. Select **New tag**.

To modify or delete a custom tag:

1. Navigate to **All stacks** and then a specific stack.
1. To modify a custom tag, use the pencil icon.
1. To delete a custom tag, use the trash can icon.

#### Stack Activity

To view stack activity:

1. Navigate to **All stacks** and then a specific stack.
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

1. Navigate to **All stacks** and then a specific stack.
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
