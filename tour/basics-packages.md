---
title: Packages
---

Pulumi programs use packages just like ordinary programs.

JavaScript and TypeScript programs use NPM, while Python programs use PyPI, for example.

Packages let you share and reuse your Pulumi creations with your team and/or the community.

Packages are also how we distribute the foundational cloud resource definitions for AWS, Azure, Google Cloud, and
Kubernetes, in addition to our frameworks that aggregate these resources into higher level abstractions.

These packages show up as normal dependencies in your package manifest:

```json
{
    "name": "ahoy-pulumi",
    "dependencies": {
        "@pulumi/aws": "^0.12.1"
    }
}
```

And are imported as usual in your code:

```javascript
var aws = require("@pulumi/aws");
```

We will learn more about resources later on ([generally](./deployments-resources.html) and
[specifically](./cloud.html)).  For now, just remember that Pulumi doesn't need its own package manager -- we'll
just use the standard package manager for your language.

<div class="tour-nav">
    <a class="tour-button enabled" href="basics-programs.html" title="Programs">◀</a>
    <span class="tour-index"><strong>5</strong>/9</span>
    <a class="tour-button enabled" href="basics-stacks.html" title="Stacks">▶</a>
</div>
