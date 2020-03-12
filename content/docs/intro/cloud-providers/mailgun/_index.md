---
title: Mailgun
meta_desc: This page provides an overview of the Mailgun Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-mailgun
    weight: 2
---

<img src="/logos/tech/mailgun.png" align="right" class="h-16 px-8 pb-4">

The Mailgun provider for Pulumi can be used to provision any of the cloud resources available in [Mailgun](https://www.mailgun.com/).
The Mailgun provider must be configured with credentials to deploy and update resources in Mailgun.

See the [full API documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/mailgun" >}}) for complete details of the available Mailgun provider APIs.

## Setup

The Mailgun provider supports several options for providing access to Mailgun credentials.  See the [Mailgun setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const mailgun = require("@pulumi/mailgun")

const route = new mailgun.Route("test-route", {
    priority: 0,
    description: "Inbound route",
    expression: "match_recipient('.*@example.com')",
    actions: [
        "forward('http://example.com/api/v1/foos/')",
        "stop()"
    ]
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as mailgun from "@pulumi/mailgun";

const route = new mailgun.Route("test-route", {
    priority: 0,
    description: "Inbound route",
    expression: "match_recipient('.*@example.com')",
    actions: [
        "forward('http://example.com/api/v1/foos/')",
        "stop()"
    ]
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_mailgun as mailgun

route = mailgun.Route("test-route",
  priority=0,
  description="Inbound route",
  expression="match_recipient('.*@example.com')",
  actions=[
    "forward('http://example.com/api/v1/foos/')",
    "stop()"
])
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  mailgun "github.com/pulumi/pulumi-mailgun/sdk/go/mailgun"
)

route, _ := mailgun.NewRoute(ctx, "test-route", &mailgun.RouteArgs{
  Priority: 0,
  Description: "Inbound route",
  Expression: "match_recipient('.*@example.com')",
  Actions: [
    "forward('http://example.com/api/v1/foos/')",
    "stop()"
]})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Mailgun;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var route = new Route("test-route", new RouteArgs
            {
                Priority = 0,
                Description = "Inbound route",
                Expression = "match_recipient('.*@example.com')",
                Actions = [
                    "forward('http://example.com/api/v1/foos/')",
                    "stop()"
                ],
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/mailgun`](https://www.npmjs.com/package/@pulumi/mailgun)
* Python: [`pulumi-mailgun`](https://pypi.org/project/pulumi-mailgun/)
* Go: [`github.com/pulumi/pulumi-mailgun/sdk/go/mailgun`](https://github.com/pulumi/pulumi-mailgun)
* .NET: [`Pulumi.Mailgun`](https://www.nuget.org/packages/Pulumi.Mailgun)

The Mailgun provider is open source and available in the [pulumi/pulumi-mailgun](https://github.com/pulumi/pulumi-mailgun) repo.
