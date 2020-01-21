---
title: RabbitMQ
meta_desc: This page provides an overview of the RabbitMQ Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-rabbitmq
    weight: 5
---

<img src="/logos/tech/rabbitmq.svg" align="right" class="h-16 px-8 pb-4">

The RabbitMQ provider for Pulumi can be used to provision any of the resources available for RabbitMQ.
The RabbitMQ provider must be configured with credentials to deploy and update resources in Fastly.

See the [full API documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/rabbitmq" >}}) for complete details of the available RabbitMQ provider APIs.

## Setup

The RabbitMQ provider supports several options for providing access to RabbitMQ credentials.  See the [RabbitMQ setup page]({{< relref "setup" >}}) for details.

## Example

{{< langchoose csharp >}}

```javascript
const rabbitmq = require("@pulumi/rabbitmq")

const user = new rabbitmq.User("user", {
  password: "MyPassword1234!"
});
```

```typescript
import * as rabbitmq from "@pulumi/rabbitmq";

const user = new rabbitmq.User("user", {
  password: "MyPassword1234!"
});
```

```python
import pulumi_rabbitmq as rabbitmq

user = rabbitmq.User("user",
  password="MyPassword1234!"
)
```

```go
import (
  rabbitmq "github.com/pulumi/pulumi-rabbitmq/sdk/go/rabbitmq"
)

user, _ := rabbitmq.NewUser(ctx, "user", &rabbitmq.UserArgs{
  Password: "MyPassword1234!"
})
```

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Rabbitmq;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var user = new User("user", new UserArgs
            {
                Password = "MyPassword1234!"
            });
        });
}
```

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/rabbitmq`](https://www.npmjs.com/package/@pulumi/rabbitmq)
* Python: [`pulumi-rabbitmq`](https://pypi.org/project/pulumi-rabbitmq/)
* Go: [`github.com/pulumi/pulumi-rabbitmq/sdk/go/rabbitmq`](https://github.com/pulumi/pulumi-rabbitmq)
* .NET: [`Pulumi.Rabbitmq`](https://www.nuget.org/packages/Pulumi.Rabbitmq)

The RabbitMQ provider is open source and available in the [pulumi/pulumi-rabbitmq](https://github.com/pulumi/pulumi-rabbitmq) repo.
