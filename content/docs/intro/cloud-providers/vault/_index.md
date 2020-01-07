---
title: HashiCorp Vault
meta_desc: This page provides an overview of the HashiCorp Vault Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-vault
    weight: 5
---

<img src="/logos/tech/vault.png" align="right" class="h-16 px-8 pb-4">

The HashiCorp Vault provider for Pulumi can be used to provision any of the resources available in [Vault](https://www.vaultproject.io/).

See the [full API documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/vault" >}}) for complete details of the available Vault provider APIs.

## Setup

The Vault provider supports several options for interacting with HashiCorp Vault.  See the [Vault setup page]({{< relref "setup" >}}) for details.

## Example

{{< langchoose csharp >}}

```javascript
const vault = require("@pulumi/vault")

const be = new vault.AuthBackend("example", {
  type: "github"
});
```

```typescript
import * as vault from "@pulumi/vault";

const be = new vault.AuthBackend("example", {
  type: "github"
});
```

```python
import pulumi_vault as vault

be = vault.AuthBackend("example",
  type='github'
)
```

```go
import (
  vault "github.com/pulumi/pulumi-vault/sdk/go/vault"
)

be, _ := vault.NewAuthBackend(ctx, "example", &vault.AuthBackendArgs{
  Type: "github",
})
```

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Vault;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var be = new Vault.AuthBackend("example", new Vault.AuthBackendArgs
            {
                Type = "github",
            });
        });
}
```

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/vault`](https://www.npmjs.com/package/@pulumi/vault)
* Python: [`pulumi-vault`](https://pypi.org/project/pulumi-vault/)
* Go: [`github.com/pulumi/pulumi-vault/sdk/go/vault`](https://github.com/pulumi/pulumi-vault)
* .NET: [`Pulumi.Vault`](https://www.nuget.org/packages/Pulumi.Vault)

The HashiCorp Vault provider is open source and available in the [pulumi/pulumi-vault](https://github.com/pulumi/pulumi-vault) repo.
