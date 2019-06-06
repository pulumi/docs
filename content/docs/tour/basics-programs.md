---
title: Programs
aliases: ["basics-programs.html"]
menu:
  tour:
    parent: tour
    weight: 1
---

To get code to the cloud, you write Pulumi programs in your language of choice.

> Pulumi currently supports JavaScript and TypeScript (using Node.js), Python, and Go.
> More languages are on their way!

Pulumi programs are just like normal programs, except for a few important details:

* You run them using the `pulumi` CLI instead of invoking them directly
* They describe cloud resources, like containers, functions, and databases, that Pulumi will provision
* The result is a plan that may be previewed before asking Pulumi to take action

The full power of your language is available, including loops, conditionals, classes, functions, and packages.

Programs express their desired state by creating [resource objects]({{< relref "programs-resources.md" >}}) in code.  This
communicates to Pulumi what cloud resources will be required by the program.  Here is a simple example that uses an
[AWS S3 bucket](https://aws.amazon.com/s3/):

{{< langchoose >}}

```javascript
var aws = require("@pulumi/aws");
const bucket = new aws.s3.Bucket("my-bucket");
```

```typescript
import * as aws from "@pulumi/aws";
const bucket = new aws.s3.Bucket("my-bucket");
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

The `Bucket` object allocated above is called a [resource]({{< relref "programs-resources.md" >}}), and it describes your program's
cloud requirements so that Pulumi can create and manage them.  This is immutable infrastructure as code.

***

Next up, let's create a project to house our program.  From there, we can start deploying it!

<div class="tour-nav">
    <a class="tour-button enabled" href="{{< relref "./" >}}" title="A Tour of Pulumi">◀</a>
    <span class="tour-index"><strong>2</strong>/8</span>
    <a class="tour-button enabled" href="{{< relref "basics-projects.md" >}}" title="Creating a project">▶</a>
</div>
