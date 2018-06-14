---
title: Resources
---

Cloud resources are just objects you will allocate in your program:

```javascript
var aws = require("@pulumi/aws");
var bucket = new aws.s3.Bucket("photos");
```

This program allocates a single AWS S3 Bucket resource, whose name is `photos`.  All resources have names which must be
unique amongst all other instances of those resources in a single program, to help Pulumi identify them.

More complex resource types require additional properties, as will soon see.

Each resource class derives from a common `Resource` base class defined by the Pulumi SDK.

***

Resource properties are unique enough, especially their outputs, that we will now look deeper into them.

<div class="tour-nav">
    <a class="tour-button enabled" href="programs-configuring.html" title="Configuring your stack">◀</a>
    <span class="tour-index"><strong>5</strong>/9</span>
    <a class="tour-button enabled" href="programs-properties.html" title="Resource properties">▶</a>
</div>
