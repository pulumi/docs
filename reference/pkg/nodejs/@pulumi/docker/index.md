---
title: Package @pulumi/docker
---


Node.js:

```javascript
var docker = require("@pulumi/docker");
```

ES6 modules:

```typescript
import * as docker from "@pulumi/docker";
```

<h2 class="pdoc-module-header">Index</h2>

* <a href="#buildAndPushImage">function buildAndPushImage</a>
* <a href="#CacheFrom">interface CacheFrom</a>
* <a href="#DockerBuild">interface DockerBuild</a>
* <a href="#Registry">interface Registry</a>

<a href="/docker.ts">docker.ts</a> 


<h2 class="pdoc-module-header" id="buildAndPushImage">
<a class="pdoc-member-name" href="/docker.ts#L86">function buildAndPushImage</a>
</h2>

```typescript
buildAndPushImage(imageName: string, pathOrBuild: string | DockerBuild, repositoryUrl: pulumi.Input<string>, logResource: pulumi.Resource, connectToRegistry: { ... }): pulumi.Output<string>
```

<h2 class="pdoc-module-header" id="CacheFrom">
<a class="pdoc-member-name" href="/docker.ts#L41">interface CacheFrom</a>
</h2>

CacheFrom may be used to specify build stages to use for the Docker build cache. The final image
is always implicitly included.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/docker.ts#L47">property stages</a>
</h3>

```typescript
stages?: string[];
```


An optional list of build stages to use for caching. Each build stage in this list will be
built explicitly and pushed to the target repository. A given stage's image will be tagged as
"[stage-name]".

<h2 class="pdoc-module-header" id="DockerBuild">
<a class="pdoc-member-name" href="/docker.ts#L53">interface DockerBuild</a>
</h2>

DockerBuild may be used to specify detailed instructions about how to build a container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/docker.ts#L72">property args</a>
</h3>

```typescript
args?: undefined | { ... };
```


An optional map of named build-time argument variables to set during the Docker build.  This
flag allows you to pass built-time variables that can be accessed like environment variables
inside the `RUN` instruction.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/docker.ts#L81">property cacheFrom</a>
</h3>

```typescript
cacheFrom?: boolean | CacheFrom;
```


An optional CacheFrom object with information about the build stages to use for the Docker
build cache. This parameter maps to the --cache-from argument to the Docker CLI. If this
parameter is `true`, only the final image will be pulled and passed to --cache-from; if it is
a CacheFrom object, the stages named therein will also be pulled and passed to --cache-from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/docker.ts#L61">property context</a>
</h3>

```typescript
context?: undefined | string;
```


context is a path to a directory to use for the Docker build context, usually the directory
in which the Dockerfile resides (although dockerfile may be used to choose a custom location
independent of this choice). If not specified, the context defaults to the current working
directory; if a relative path is used, it is relative to the current working directory that
Pulumi is evaluating.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/docker.ts#L66">property dockerfile</a>
</h3>

```typescript
dockerfile?: undefined | string;
```


dockerfile may be used to override the default Dockerfile name and/or location.  By default,
it is assumed to be a file named Dockerfile in the root of the build context.

<h2 class="pdoc-module-header" id="Registry">
<a class="pdoc-member-name" href="/docker.ts#L26">interface Registry</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/docker.ts#L29">property password</a>
</h3>

```typescript
password: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/docker.ts#L27">property registry</a>
</h3>

```typescript
registry: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/docker.ts#L28">property username</a>
</h3>

```typescript
username: string;
```

