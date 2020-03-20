---
title: MySQL
meta_desc: This page provides an overview of the MySQL Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-mysql
    weight: 2
---

<img src="/logos/tech/mysql.png" align="right" class="h-16 px-8 pb-4">

The MySQL provider for Pulumi can be used to provision any of the resources available for MySQL.
The MySQL provider must be configured with credentials to deploy and update resources in MySQL.

See the [full API documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/mysql" >}}) for complete details of the available MySQL provider APIs.

## Setup

The MySQL provider supports several options for providing access to MySQL credentials.  See the [MySQL setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const mysql = require("@pulumi/mysql")

const myDb = new mysql.Database("my-database");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as mysql from "@pulumi/mysql";

const myDb = new mysql.Database("my-database");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_mysql as mysql

my_db = mysql.Database("my-database")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  mysql "github.com/pulumi/pulumi-mysql/sdk/go/mysql"
)

myDb, _ := mysql.NewDatabase(ctx, "my-database", &mysql.DatabaseArgs{})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Mysql;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            mydatabase = new Database("my-database", new DatabaseArgs{});
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/mysql`](https://www.npmjs.com/package/@pulumi/mysql)
* Python: [`pulumi-mysql`](https://pypi.org/project/pulumi-mysql/)
* Go: [`github.com/pulumi/pulumi-mysql/sdk/go/mysql`](https://github.com/pulumi/pulumi-mysql)
* .NET: [`Pulumi.Mysql`](https://www.nuget.org/packages/Pulumi.Mysql)

The MySQL provider is open source and available in the [pulumi/pulumi-mysql](https://github.com/pulumi/pulumi-mysql) repo.
