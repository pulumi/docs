---
title: Pulumi Service Provider
title_tag: Manage Pulumi ESC resources using a Pulumi Program
h1: Manage Pulumi ESC resources using a Pulumi Program
meta_desc: Pulumi Service Provider allows you to create and manage ESC resources like
  environments, permissions and version tags using a Pulumi program.
menu:
  esc:
    identifier: esc-psp
    parent: esc-development
    weight: 2
search:
  keywords:
    - Environment
    - ESC
    - Service Provider
    - Infrastructure Code
---

Pulumi Service Provider empowers you to manage your entire infrastructure and application landscape through a unified approach. This means you can define [environments](/docs/esc/environments/), add [version tags](/docs/esc/environments/#tagging-versions), and even control access using familiar Infrastructure as Code (IaC) practices ensuring consistency and repeatability across your deployments.

Here's a list of ESC resources available through Pulumi Service Provider:

- **Environment**: Define new environments and create new revisions using the normal `pulumi up` command. Learn more [here](/registry/packages/pulumiservice/api-docs/environment/).
- **Environment Team Permission**: Control permissions to your environments. Combines with **Team** and **Environment** resources easily! Learn more [here](/registry/packages/pulumiservice/api-docs/teamenvironmentpermission/).
- **Environment Revision Tag**: Add tags to your environment revision for flexible environment import and version control. Learn more [here](/registry/packages/pulumiservice/api-docs/environmentversiontag/).
- **ESC Webhook**: Create webhooks to monitor or react to events on your environments. This can be configured for specific environments or at the organization level. Learn more [here](/docs/esc/webhooks).

If you haven't used Pulumi Service Provider before, see this [installation and configuration guide](https://www.pulumi.com/registry/packages/pulumiservice/installation-configuration/).

Pulumi Service Provider ESC capabilities are available for TypeScript/JavaScript, Go, Python, C#, Java, and YAML. Here are examples of creating environments in TypeScript/JavaScript, Go, and Python:

{{< chooser language "typescript,python,go" />}}

{{% choosable language typescript %}}

```typescript
import * as service from "@pulumi/pulumiservice";
import * as pulumi from "@pulumi/pulumi";

var environment = new service.Environment("testing-environment", {
  organization: "service-provider-test-org",
  name: "testing-environment-ts",
  yaml: new pulumi.asset.StringAsset(
    `values:
    myKey1: "myValue1"
    myNestedKey:
    myKey2: "myValue2"
    myNumber: 1`
  )
})
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_pulumiservice import Environment

environment = Environment(
    "testing-environment",
    organization="service-provider-test-org",
    name="testing-environment-py",
    yaml=pulumi.StringAsset("""
        values:
          myKey1: "myValue1"
          myNestedKey:
            myKey2: "myValue2"
            myNumber: 1
    """)
)
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
		_, err := pulumiservice.NewEnvironment(ctx, "testing-environment", &pulumiservice.EnvironmentArgs{
			Name:         pulumi.String("testing-environment-go"),
			Organization: pulumi.String("service-provider-test-org"),
			Yaml: pulumi.NewStringAsset(`
            values:
              myKey1: "myValue1"
              myNestedKey:
                myKey2: "myValue2"
                myNumber: 1`),
		})
		if err != nil {
			return err
		}
		return nil
	})
}
```

{{% /choosable %}}

For more examples of Pulumi Service Provider usage, check out the [examples folder](https://github.com/pulumi/pulumi-pulumiservice/tree/main/examples) in the Pulumi Service Provider GitHub repository. It is open source, and contributions are welcome!
