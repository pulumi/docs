---
title: Upgrading to Pulumi 3.0
meta_desc: This page provides instructions for upgrading to Pulumi 3.0
no_on_this_page: true
---

## Upgrading to Pulumi 3.0

Pulumi 3.0 is currently in beta. If you'd like to try the beta and provide feedback, it's simple to upgrade. First, [install the 3.0 CLI]({{< relref "/docs/get-started/install#installing-betas-and-previous-versions" >}}). Then, update each of your Pulumi programs to utilize the new SDK.

## CLI behavior changes in Pulumi 3.0

Previously, when using the `--stack` option on CLI commands, Pulumi would inconsistently set that stack as the current stack. In Pulumi 3.0, this behavior has now standardized and will *NOT* set the stack as the current stack. This affects the following commands:

* `pulumi cancel`
* `pulumi config refresh`
* `pulumi destroy`
* `pulumi import`
* `pulumi logs`
* `pulumi preview`
* `pulumi refresh`
* `pulumi stack *`
* `pulumi state`
* `pulumi up`
* `pulumi watch`

## Update Your Pulumi Programs

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language "javascript,typescript" %}}

### Update Dependencies

```bash
npm install @pulumi/pulumi@^3.0.0-beta
```

{{% /choosable %}}

{{% choosable language python %}}

### Update Dependencies

Modify your `requirements.txt` file to update the Pulumi SDK and related providers as below:

```
pulumi>=3.0.0b,<4.0.0
pulumi-aws>=4.0.0b,<5.0.0
```

Then run `pip install`:

```bash
pip install -r requirements.txt
```

{{% /choosable %}}
{{% choosable language go %}}

### Update Dependencies

In `go.mod`, you can depend on the Pulumi SDK and related providers as below:

```
require (
    github.com/pulumi/pulumi/sdk/v3 v3.0.0-beta.1
    github.com/pulumi/pulumi-aws/sdk/v4 v4.0.0-beta.1
)
```

Then run `go mod download`

### Go SDK removes Apply<TypeName>

In order to improve the performance of our Go SDK, we have removed:

* Apply<TypeName>
* Apply
* ApplyWithContext

We now suggest that you use:

* ApplyT
* ApplyTWithContext

```go
//before
containerDef := image.ImageName.ApplyString(func(name string) (string, error) {
    return name, nil
})

//after
containerDef := image.ImageName.ApplyT(func(name string) (string, error) {
    return name, nil
}).(pulumi.StringOutput)
```

When using ApplyT, remember to cast the result to the Output type

{{% /choosable %}}
{{% choosable language csharp %}}

### Update Dependencies

Update your package reference to the latest version of the SDK:

```csharp
<PackageReference Include="Pulumi" Version="3.0.*-*" />
```

{{% /choosable %}}

{{< /chooser >}}

## Automation API changes in Pulumi 3.0

The Pulumi 3.0 beta includes the final preview of the Automation API. That preview standardizes the namespace requirements for Automation API. You can update your
program to use the following namespaces

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language "javascript,typescript" %}}

```javascript
// before
import as automation from "@pulumi/pulumi/x/automation";

//after
import as automation from "@pulumi/pulumi/automation";
```

{{% /choosable %}}

{{% choosable language "python" %}}

```python
#before
from pulumi.x import automation as auto

#after
from pulumi import automation as auto
```

{{% /choosable %}}

{{% choosable language "go" %}}

```go
//before
import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v2/go/x/auto"
	"github.com/pulumi/pulumi/sdk/v2/go/x/auto/optdestroy"
	"github.com/pulumi/pulumi/sdk/v2/go/x/auto/optup"
)

//after
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/auto"
	"github.com/pulumi/pulumi/sdk/v3/go/auto/optdestroy"
	"github.com/pulumi/pulumi/sdk/v3/go/auto/optup"
)
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

```csharp
using System;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Threading.Tasks;
using Pulumi.Automation;
```

{{% /choosable %}}

{{< /chooser >}}

## When you should upgrade to Pulumi 3.0

Pulumi 3.0 is currently in beta and not recommended for existing production workloads. Once it is made generally available (GA), we will recommend switching to Pulumi 3.0 in the docs and in the CLI via the normal upgrade prompts.
`pulumi new` will continue to use the stable versions of the templates. You can use the `3.x` version of the templates, which will use the 3.0 SDK, by running `pulumi new https://github.com/pulumi/templates/tree/3.x`.
