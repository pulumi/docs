---
title: New Relic
meta_desc: This page provides an overview of the New Relic Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-newrelic
    weight: 2
---

<img src="/logos/tech/newrelic.svg" align="right" class="h-16 px-8 pb-4">

The New Relic provider for Pulumi can be used to provision any of the cloud resources available in [New Relic](https://newrelic.com/).
The New Relic provider must be configured with credentials to deploy and update resources in New Relic.

See the [full API documentation]({{< relref "/docs/reference/pkg/newrelic" >}}) for complete details of the available New Relic provider APIs.

## Setup

The New Relic provider supports several options for providing access to New Relic credentials.  See the [New Relic setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const newrelic = require("@pulumi/newrelic")

const policy = new newrelic.AlertPolicy("my-policy");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as newrelic from "@pulumi/newrelic";

const policu = new newrelic.AlertPolicy("my-policy");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_newrelic as newrelic

policy = newrelic.AlertPolicy("my-policy")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  newrelic "github.com/pulumi/pulumi-newrelic/sdk/go/newrelic"
)

policy, _ := newrelic.NewAlertPolicy(ctx, "my-policy"
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Newrelic;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var policy = new AlertPolicy("my-policy");
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/newrelic`](https://www.npmjs.com/package/@pulumi/newrelic)
* Python: [`pulumi-newrelic`](https://pypi.org/project/pulumi-newrelic/)
* Go: [`github.com/pulumi/pulumi-newrelic/sdk/go/newrelic`](https://github.com/pulumi/pulumi-newrelic)
* .NET: [`Pulumi.Newrelic`](https://www.nuget.org/packages/Pulumi.Newrelic)

The New Relic provider is open source and available in the [pulumi/pulumi-newrelic](https://github.com/pulumi/pulumi-newrelic) repo.
