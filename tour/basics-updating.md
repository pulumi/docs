---
title: Performing updates
---

After standing up program for the first time, it will be live and running in the cloud.

From there, we may wish to make incremental updates.  This includes adding new resources, changing existing ones, or
removing them altogether.

No matter what the nature of the changes, we simply make them to our program, and rerun `pulumi update`.  It will figure
out how to proceed by diffing the previous state with the new goal state, and then carry out a sequence of operations.

Remember, it will prompt us first, and we can explicitly run `pulumi preview` instead, if we'd like to be safe.

For instance, let's say we want to enable public read access to our S3 bucket, with a minor edit:

{% include langchoose.html %}

```javascript
var bucket = new aws.s3.Bucket("my-bucket", { acl: "public-read" });
```

```typescript
const bucket = new aws.s3.Bucket("my-bucket", { acl: "public-read" });
```

```python
from pulumi_aws import s3
buck = s3.Bucket('my-bucket', acl='public-read')
```

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/go/aws/s3"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
    pulumi.Run(func (ctx *pulumi.Context) error {
        _, err := s3.NewBucket(ctx, "my-bucket", &s3.BucketArgs{
            Acl: "public-read",
        })
        return err
    })
}
```

This time, `pulumi update` will make a smaller, more targeted change:

```bash
$ pulumi update
...
Updating stack 'ahoy-pulumi-dev'
Performing changes:

     Type                 Name                          Status      Info
 *   pulumi:pulumi:Stack  ahoy-pulumi-ahoy-pulumi-dev  done
 ~   └─ aws:s3:Bucket     my-bucket                     updated     changes: ~ acl

info: 1 change performed:
    ~ 1 resource updated
      1 resource unchanged
Update duration: 9.564362849s

Permalink: https://app.pulumi.com/broomllc/ahoy-pulumi-dev/updates/2
```

***

We're almost done with the first lesson.  Before wrapping up, however, let's destroy everything we just created.

<div class="tour-nav">
    <a class="tour-button enabled" href="basics-previewing.html" title="Previewing updates">◀</a>
    <span class="tour-index"><strong>7</strong>/8</span>
    <a class="tour-button enabled" href="basics-destroying.html" title="Destroying">▶</a>
</div>
