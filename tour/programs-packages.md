---
title: Packages
---

Pulumi programs use packages just like ordinary programs.

JavaScript and TypeScript programs use NPM, Python programs use PyPI, and Go programs simply use packages distributed
in the usual means.

Packages let you share and reuse your Pulumi creations with your team and/or the community.

Packages are also how we distribute the foundational cloud resource definitions for AWS, Azure, Google Cloud, and
Kubernetes, in addition to our frameworks that aggregate these resources into higher level abstractions.

These packages are installed as usual in your language:

{% include langchoose.html %}

<span class="language-prologue-javascript"></span>
```json
{
    "name": "ahoy-pulumi",
    "dependencies": {
        "@pulumi/aws": "^0.14.0"
    }
}
```

<span class="language-prologue-typescript"></span>
```json
{
    "name": "ahoy-pulumi",
    "dependencies": {
        "@pulumi/aws": "^0.14.0"
    }
}
```

<span class="language-prologue-python"></span>
```
pulumi_aws>=0.14.0
```

<span class="language-prologue-go"></span>
```go
import (
    "github.com/pulumi/pulumi-aws/sdk/go/aws"
)
```

And are imported as usual in your code:

```javascript
var aws = require("@pulumi/aws");
```

We will learn more about resources later on ([generally](./deployments-resources.html) and
[specifically](./cloud.html)).  For now, just remember that Pulumi doesn't need its own package manager -- we'll
just use the standard package manager for your language.

***

Many packages demand configuration to customize their behavior.  Let's see how to do that now.

<div class="tour-nav">
    <a class="tour-button enabled" href="programs-stacks.html" title="Stacks">◀</a>
    <span class="tour-index"><strong>3</strong>/9</span>
    <a class="tour-button enabled" href="programs-configuring.html" title="Configuring your stack">▶</a>
</div>
