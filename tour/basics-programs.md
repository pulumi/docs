---
title: Programs
---

<div style="float: right; padding: 8px; background-color: #ddd;">LANG</div>

To get code to the cloud, you write Pulumi programs.

Programs are written in your language of choice.  For a customized experience, please choose your language above.

> Pulumi currently supports JavaScript and TypeScript, using Node.js, and Python.  More languages are on their way!

Pulumi programs are just like usual programs, except for a few important points:

* You will run them using the `pulumi` CLI instead of invoking them directly
* They create cloud resources, like containers, functions, and load balancers, that Pulumi will provision
* The result is a plan of action that may be previewed before asking Pulumi to deploy changes

Those familiar with [infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_Code) will feel at home.
Don't worry if you're not -- you'll be an expert by the end of this tour.

The full power of your language is available -- loops and conditionals, classes and objects, functions, and so on.

Here is a very basic program that creates a single load-balanced container service:

```typescript
import {Service} from "@pulumi/cloud";
const redis = new Service("redis-cache", {
    image: "redis:alpine",
    ports: [{ port: 6379 }],
});
```

Don't worry if the specific nuances of resources and deployments don't add up yet.  Those are
[coming in a few sections](deployments.html).

<div class="tour-nav">
    <a class="tour-button enabled" href="basics-projects.html" title="Projects">◀</a>
    <span class="tour-index"><strong>4</strong>/9</span>
    <a class="tour-button enabled" href="basics-packages.html" title="Packages">▶</a>
</div>
