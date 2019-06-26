---
title: Resources
expanded_url: /docs/tour/programs/
menu:
  tour:
    parent: programs
    weight: 4
---

Cloud resources are just objects you will allocate in your program:

{{< langchoose >}}

```javascript
var aws = require("@pulumi/aws");
const bucket = new aws.s3.Bucket("my-bucket");
```

```typescript
import * as aws from "@pulumi/aws";
let bucket = new aws.s3.Bucket("my-bucket");
```

```python
from pulumi_aws import s3
bucket = s3.Bucket('my-bucket')
```

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/go/aws/s3"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
    pulumi.Run(func (ctx *pulumi.Context) error {
        _, err := s3.NewBucket(ctx, "my-bucket", nil)
        return err
    })
}
```

This program allocates a single AWS S3 Bucket resource, whose name is `my-bucket`.  All resources have names which must
be unique amongst all other instances of those resources in a single program, to help Pulumi identify them.

Each resource class derives from
[a common `Resource` base class]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Resource" >}}) defined by the Pulumi SDK,
whose shape differs in each language.

More complex resource types require additional properties, as we'll soon see.  Resources often have two properties:

* `urn` is the Pulumi-allocated Unique Resource Name (URN) for your resource
* `id` is the cloud provider allocated unique identifier, usually just its name or ID

Although resources can be allocated by hand using the SDK directly, you will almost always create them using an
appropriate language package, such as the AWS, Azure, GCP, OpenStack, or Kubernetes packages.

A resource may be created with one of the following three properties:

* `parent` causes a newly allocated resource to become a child of another resource
* `dependsOn` can be used to list other resources that a resource is dependent upon, for creation/deletion
* `protect`, when `true`, asks Pulumi to reject attempts to delete the resource, such as a database

***

Resource properties are unique enough, especially their outputs, that we will now look deeper into them.

<div class="tour-nav">
    <a class="tour-button enabled" href="{{< relref "programs-configuring.md" >}}" title="Configuring your stack">◀</a>
    <span class="tour-index"><strong>5</strong>/8</span>
    <a class="tour-button enabled" href="{{< relref "programs-properties.md" >}}" title="Resource properties">▶</a>
</div>
