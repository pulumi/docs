---
title: Okta
meta_desc: This page provides an overview of the Okta Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-okta
    weight: 5
---

<img src="/logos/tech/okta.png" align="right" class="h-16 px-8 pb-4">

The Okta provider for Pulumi can be used to provision any of the resources available in [Okta](https://www.okta.com/).

See the [full API documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/okta" >}}) for complete details of the available Okta provider APIs.

## Setup

The Okta provider supports several options for interacting with Okta.  See the [Okta setup page]({{< relref "setup" >}}) for details.

## Example

{{< langchoose csharp >}}

```javascript
const okta = require("@pulumi/okta")

const user = new okta.user.User("example-user", {
    email: "test-user@mydomain.com",
    login: "test-user@mydomain.com",
    firstName: "random",
    lastName: "user",
})
```

```typescript
import * as okta from "@pulumi/okta";

const user = new okta.user.User("example-user", {
    email: "test-user@mydomain.com",
    login: "test-user@mydomain.com",
    firstName: "random",
    lastName: "user",
});
```

```python
import pulumi_okta as okta

user = okta.user.User("example-user",
email="test-user@mydomain.com",
login="test-user@mydomain.com",
first_name="random",
last_name="user",
)
```

```go
import (
  user "github.com/pulumi/pulumi-okta/sdk/go/okta/user"
)

user, _ := user.User(ctx, "example-user", &user.UserArgs{
    FirstName: "random",
    LastName: "user",
    Email: "test-user@mydomain.com",
    Login: "test-user@mydomain.com"
})
```

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Okta.User;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var user = new User.User("example-user", new User.UserArgs{
                FirstName = "random",
                LastName = "user",
                Login = "test-user@mydomain.com",
                Email = "test-user@mydomain.com",
            });
        });
}
```

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/okta`](https://www.npmjs.com/package/@pulumi/okta)
* Python: [`pulumi-okta`](https://pypi.org/project/pulumi-okta/)
* Go: [`github.com/pulumi/pulumi-okta/sdk/go/okta`](https://github.com/pulumi/pulumi-okta)
* .NET: [`Pulumi.Okta`](https://www.nuget.org/packages/Pulumi.Okta)

The Okta provider is open source and available in the [pulumi/pulumi-okta](https://github.com/pulumi/pulumi-okta) repo.
