---
title: Linode
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-linode
    weight: 2

aliases: ["/docs/reference/clouds/linode/"]
---

<img src="/logos/tech/linode.svg" align="right" class="h-16 px-8 pb-4">

The Linode provider for Pulumi can be used to provision any of the cloud resources available in [Linode](https://www.linode.com).  
The Linode provider must be configured with credentials to deploy and update resources in Linode.

See the [full API documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/linode" >}}) for complete details of the available Linode provider APIs.

## Setup

The Linode provider supports several options for providing access to Linode credentials.  See [Linode setup page]({{< relref "/docs/intro/cloud-providers/linode/setup.md" >}}) for details.

## Example

{{< langchoose >}}

```javascript
const linode = require("@pulumi/linode")
const domain = new linode.Domain("my-domain", {
  domain: "foobar.example",
  soaEmail: "example@foobar.example",
  type: "master",
});
```

```typescript
import * as linode from "@pulumi/linode";
const domain = new linode.Domain("my-domain", {
  domain: "foobar.example",
  soaEmail: "example@foobar.example",
  type: "master",
});
```

```python
import pulumi_linode as linode
domain = linode.Domain("my-domain",
  domain='foobar.example',
  soa_email='example@foobar.example',
  type='master',
)
```

```go
import (
    linode "github.com/pulumi/pulumi-linode/sdk/go/linode"
)
domain, _ := linode.NewDomain(ctx, "test", &linode.DomainArgs{
  Domain: "foobar.example",
  SoaEmail: "example@foobar.example",
  Type: "master",
})
```

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/linode`](https://www.npmjs.com/package/@pulumi/linode)
* Python: [`pulumi-linode`](https://pypi.org/project/pulumi-linode/)
* Go: [`github.com/pulumi/pulumi-linode/sdk/go/linode`](https://github.com/pulumi/pulumi-linode)

The Linode provider is open source and available in the [pulumi/pulumi-linode](https://github.com/pulumi/pulumi-linode) repo.