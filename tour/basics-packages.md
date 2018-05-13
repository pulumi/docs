---
title: Packages
---

Pulumi programs use packages just like ordinary programs.

JavaScript and TypeScript programs use NPM, while Python programs use PyPI, for example.

Packages are how we distribute cloud resource definitions for AWS, Azure, Google Cloud, and Kubernetes.  It's also
how we distribute frameworks that aggregate these resources into higher level abstractions.

These will show up as normal dependencies in your package manifest:

```json
{
    "name": "ahoy-pulumi",
    "dependencies": {
        "@pulumi/pulumi": "^0.12.1",
        "@pulumi/aws": "^0.12.1"
    }
}
```

And imported as usual in your code:

```javascript
var aws = require("@pulumi/aws");
```

We will learn more about resources later on ([generally](./deployments-resources.html) and
[specifically](./cloud.html)).  For now, just remember that Pulumi doesn't need its own package manager -- it
leverages those you already use for your existing code.

<div class="tour-nav">
    <a class="tour-button enabled" href="basics-programs.html" title="Programs">◀</a>
    <span class="tour-index"><strong>5</strong>/8</span>
    <a class="tour-button enabled" href="basics-stacks.html" title="Stacks">▶</a>
</div>
