---
title: "Stack READMEs in the Pulumi Service"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2022-05-16T14:35:01-07:00

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
meta_desc: Starting today you can add a README to your Pulumi Service Stacks to store key links, CLI commands and documentation.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
    - evan-boyle
    - devon-grove
    - myles-haynes
    - casey-huang
    - meagan-cojocar

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - features

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
---

Starting today, users can create [Stack READMEs](https://www.pulumi.com/docs/intro/pulumi-service/projects-and-stacks/#stack-readme) in the [Pulumi Service](https://app.pulumi.com) that dynamically update based on [Stack Outputs](https://www.pulumi.com/learn/building-with-pulumi/stack-outputs).

Each Pulumi Stack you deploy manages a key set of cloud infrastructure for your organization. The Pulumi Console includes a variety of features for exposing key information about your stack for other users within your organization - configuration, outputs, resources under management, links to cloud providers, and a graph of all resources. However, it's often useful to allow the author of a Pulumi Stack to describe in their own words the key elements of a stack, so future viewers can quickly understand the components and cloud resources that are managed.

<!--more-->

A README is a text file that introduces and explains a project. A Pulumi Service Stack README can contain documentation and common links for the Stack. The key difference between a source control README, such as a GitHub README, and a Pulumi Service Stack README, is that it is dynamically populated with details from your stack outputs. It does this by interpolating output variables on the stack (`${outputs.instances[0].ARN}`) so that each stack can construct links to dashboards, shell commands, and other pieces of documentation. All of this content stays up to date as you stand up new stacks, rename resources, and refactor your infrastructure.

There are a lot of operational activities that happen around [Pulumi Stacks](https://www.pulumi.com/docs/intro/concepts/stack), but critical information is spread across many tools. We have heard from our users that it can be time consuming switching from different tools and web apps to manage their deployments- from their cloud Console, to the Pulumi Service User Interface (UI), to the CLI, and so on. By collecting resource outputs in the Pulumi Service UI, we are reducing this friction and keeping relevant Stack information in one place so that is kept up to date automatically.

README templates can reference Stack outputs and resource properties, for example `${outputs.vpc.ARN}`. To walk you through a tangible example, a user can deploy an RDS instance and then use a variable in their README template to link to their CloudWatch dashboard to keep an eye on operational metrics. This CloudWatch dashboard link will dynamically update when deployments happen. You can use the same README template across dev, testing and production and have the correct dashboard links for each Stack. Learn more in the [Stack READMEs documentation page](https://www.pulumi.com/docs/intro/pulumi-service/projects-and-stacks/#stack-readme).

The new experience lives in the Stack page, which can be navigated to through Projects and clicking on the specific Stack you want to view the README for. Let's take a look at this new feature!

![Stack READMEs in the Pulumi Console](stack-readme.gif)

The `Pulumi.README.md` file we added to the Stack 'Production' above is a template README for our Pulumi Service. In it we have links to our AWS authentication tool, our CloudWatch metrics, to our production deployment documentation, and so on. The common places that we navigate to and from when managing this Stack. Here is some of the Markdown for this README:

```markdown
# Pulumi Service README

[Sign in to AWS to view stack resources!](https://top-secret-url.com)
​
## On Call Operations
​
### Monitor
​
**Cloudwatch Metrics**
Monitor holistic metrics tracking overall service health
[Link](https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#dashboards:name=${outputs.dashboardName})

**RDS Performance Metrics**
Monitor RDS performance (wait times, top queries)
[Link](https://us-west-2.console.aws.amazon.com/rds/home?region=us-west-2#performance-insights-v20206:/resourceId/${database.databaseCluster.id}/resourceName/${outputs.rdsClusterWriterInstance})

**Cloudwatch Logs**
Search across service logs
[Link](https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#logStream:group=${outputs.cloudwatchLogGroup})
```

## How to add a Stack README to your Stack

In order to add a README to your Pulumi Stack, you will need to do the following:

### Step 1

Export a [Stack output](https://www.pulumi.com/learn/building-with-pulumi/stack-outputs) named `readme` that contains your templated Stack README markdown, commonly by reading a file, i.e. `Pulumi.README.md`.

{{< chooser language "typescript,python,go,csharp,java" / >}}

{{% choosable language typescript %}}

```typescript
import { readFileSync } from "fs";
export const strVar = "foo";
export const arrVar = ["fizz", "buzz"];
// add readme to stack outputs. must be named "readme".
export const readme = readFileSync("./Pulumi.README.md");
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
        this.Readme = System.IO.File.ReadAllText("./Pulumi.README.md");
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

### Step 2

Create a README template for the Stack. In this example, we will create a `Pulumi.README.md` file that looks as follows:

```markdown
# Stack README

Full markdown support! Substitute stack outputs dynamically so that links can depend on your infrastructure! Link to dashboards, logs, metrics, and more.

1. Reference a string stack output: ${outputs.strVar}
2. Reference an array stack output: ${outputs.arrVar[1]}
```

### Step 3

Run `pulumi up` on that Stack

### Step 4

Open the Pulumi Service UI, navigate to Projects and then the Stack you have updated. Once on the Stack page you will see the README tab with your README file.

Ta da! 🎉

We now have a README on the Stack.

Refer to the [Stack README documentation page](https://www.pulumi.com/docs/intro/pulumi-service/projects-and-stacks/#stack-readme) for more details on how to use this feature. As always, please feel free to submit feature requests and bug reports to the [Pulumi Service GitHub Repo](https://github.com/pulumi/service-requests). We love hearing feedback from users about ways we can improve your productivity when using Pulumi. We look forward to seeing how you make Stack READMEs fit your needs!
