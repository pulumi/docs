---
title: Packages
---

Pulumi programs use packages just like ordinary programs.

JavaScript and TypeScript programs use NPM, Python programs use PyPI, and Go programs simply use packages distributed
in the usual means.

Packages let you share and reuse your Pulumi creations with your team and/or the community.

Packages are also how we distribute the foundational cloud resource definitions for AWS, Azure, Google Cloud, and
Kubernetes, in addition to our frameworks that aggregate these resources into higher level abstractions.

These packages are installed as any ordinary package would be:

{% include langchoose.html %}

<span class="language-prologue-javascript"></span>
```bash
$ npm install @pulumi/aws --save
```

<span class="language-prologue-typescript"></span>
```bash
$ npm install @pulumi/aws --save
```

<span class="language-prologue-python"></span>
```bash
$ pip install pulumi_aws
```

<span class="language-prologue-go"></span>
```bash
$ go get -u github.com/pulumi/pulumi-aws/sdk/go/aws/...
```

And are imported as usual in your code:

{% include langchoose.html %}

```javascript
var aws = require("@pulumi/aws");
```

```typescript
import * as aws from "@pulumi/aws";
```

```python
import pulumi_aws as aws
```

```go
import (
    "github.com/pulumi/pulumi-aws/sdk/go/aws"
)
```

As you can see, Pulumi doesn't need its own package manager.  Instead, you can share and reuse your creations
using all the existing tools and ecosystems for packages in your favorite language, including private packages.

***

Many packages demand configuration to customize their behavior.  Let's see how to do that now.

<div class="tour-nav">
    <a class="tour-button enabled" href="programs-stacks.html" title="Stacks">◀</a>
    <span class="tour-index"><strong>3</strong>/8</span>
    <a class="tour-button enabled" href="programs-configuring.html" title="Configuring your stack">▶</a>
</div>
