---
title: Package @pulumi/cloud
---


Node.js:

```javascript
var cloud = require("@pulumi/cloud");
```

ES6 modules:

```typescript
import * as cloud from "@pulumi/cloud";
```

<h2 class="pdoc-module-header">Index</h2>

* <a href="#cron">function cron</a>
* <a href="#daily">function daily</a>
* <a href="#hourly">function hourly</a>
* <a href="#interval">function interval</a>
* <a href="#API">interface API</a>
* <a href="#APIConstructor">interface APIConstructor</a>
* <a href="#Bucket">interface Bucket</a>
* <a href="#BucketConstructor">interface BucketConstructor</a>
* <a href="#BucketFilter">interface BucketFilter</a>
* <a href="#BucketHandlerArgs">interface BucketHandlerArgs</a>
* <a href="#CacheFrom">interface CacheFrom</a>
* <a href="#Container">interface Container</a>
* <a href="#ContainerBuild">interface ContainerBuild</a>
* <a href="#ContainerPort">interface ContainerPort</a>
* <a href="#ContainerVolumeMount">interface ContainerVolumeMount</a>
* <a href="#Containers">interface Containers</a>
* <a href="#DailySchedule">interface DailySchedule</a>
* <a href="#Domain">interface Domain</a>
* <a href="#Endpoint">interface Endpoint</a>
* <a href="#Endpoints">interface Endpoints</a>
* <a href="#HostPathVolume">interface HostPathVolume</a>
* <a href="#HostPathVolumeConstructor">interface HostPathVolumeConstructor</a>
* <a href="#HostProperties">interface HostProperties</a>
* <a href="#HourlySchedule">interface HourlySchedule</a>
* <a href="#HttpDeployment">interface HttpDeployment</a>
* <a href="#IntervalRate">interface IntervalRate</a>
* <a href="#Request">interface Request</a>
* <a href="#Response">interface Response</a>
* <a href="#ServeStaticOptions">interface ServeStaticOptions</a>
* <a href="#Service">interface Service</a>
* <a href="#ServiceArguments">interface ServiceArguments</a>
* <a href="#ServiceConstructor">interface ServiceConstructor</a>
* <a href="#SharedVolume">interface SharedVolume</a>
* <a href="#SharedVolumeConstructor">interface SharedVolumeConstructor</a>
* <a href="#Stream">interface Stream</a>
* <a href="#Table">interface Table</a>
* <a href="#TableConstructor">interface TableConstructor</a>
* <a href="#Task">interface Task</a>
* <a href="#TaskConstructor">interface TaskConstructor</a>
* <a href="#TaskRunOptions">interface TaskRunOptions</a>
* <a href="#Topic">interface Topic</a>
* <a href="#TopicConstructor">interface TopicConstructor</a>
* <a href="#Volume">interface Volume</a>
* <a href="#Action">type Action</a>
* <a href="#BucketHandler">type BucketHandler</a>
* <a href="#ContainerProtocol">type ContainerProtocol</a>
* <a href="#HostOperatingSystem">type HostOperatingSystem</a>
* <a href="#HttpEndpoint">type HttpEndpoint</a>
* <a href="#PrimaryKeyType">type PrimaryKeyType</a>
* <a href="#RouteHandler">type RouteHandler</a>
* <a href="#VolumeKind">type VolumeKind</a>

<a href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts">api.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/api/bucket.ts">bucket.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts">service.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/api/table.ts">table.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer.ts">timer.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/api/topic.ts">topic.ts</a> 


<h2 class="pdoc-module-header" id="cron">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer.ts#L88">function cron</a>
</h2>

```typescript
cron(name: string, cronTab: string, handler: Action, opts?: pulumi.ResourceOptions): void
```


A cron timer, which fires on based on a specificied cron schedule.

<h2 class="pdoc-module-header" id="daily">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer.ts#L99">function daily</a>
</h2>

```typescript
daily(name: string, handler: Action, opts?: pulumi.ResourceOptions): void
```


A daily timer, firing each day, on the day (at UTC midnight).


```typescript
daily(name: string, schedule: DailySchedule, handler: Action, opts?: pulumi.ResourceOptions): void
```


A daily timer, firing at the specified UTC hour and minute each day.

<h2 class="pdoc-module-header" id="hourly">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer.ts#L120">function hourly</a>
</h2>

```typescript
hourly(name: string, handler: Action, opts?: pulumi.ResourceOptions): void
```


An hourly timer, firing each hour, on the hour.


```typescript
hourly(name: string, schedule: HourlySchedule, handler: Action, opts?: pulumi.ResourceOptions): void
```


An hourly timer, firing at the specified UTC minute each hour.

<h2 class="pdoc-module-header" id="interval">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer.ts#L75">function interval</a>
</h2>

```typescript
interval(name: string, options: IntervalRate, handler: Action, opts?: pulumi.ResourceOptions): void
```


An interval timer, which fires on a regular time interval.

<h2 class="pdoc-module-header" id="API">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L160">interface API</a>
</h2>

API publishes an internet-facing HTTP API, for serving web
applications or REST APIs.

```javascript
let api = new API("myapi")
api.get("/", (req, res) => res.json({hello: "world"}));
api.publish().url.then(url =>
  console.log(`Serving myapi at ${url}`)
);
```

Paths are `/` seperated.  A path can use `{param}` to capture zero-or-more
non-`/` characters and make the captured path segment available in
`req.params.param`, or `{param+}` to greedily capture all remaining
characters in the url path into `req.params.param`.

Paths and routing are defined statically, and cannot overlap. Code inside a
route handler can be used to provide dynamic decisions about sub-routing
within a static path.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L230">method all</a>
</h3>

```typescript
all(path: string, handlers: RouteHandler[]): void
```


Routes all HTTP methods on the given path to the provided handler(s).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L243">method attachCustomDomain</a>
</h3>

```typescript
attachCustomDomain(domain: Domain): void
```


Attach a custom domain to this API.

Provide a domain name you own, along with SSL certificates from a
certificate authority (e.g. LetsEncrypt).

Must be called prior to [publish]ing the API.

_Note_: It is strongly encouraged to store certificates in config
variables and not in source code.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L216">method delete</a>
</h3>

```typescript
delete(path: string, handlers: RouteHandler[]): void
```


Routes DELETE requests on the given path to the provided handler(s).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L195">method get</a>
</h3>

```typescript
get(path: string, handlers: RouteHandler[]): void
```


Routes GET requests on the given path to the provided handler(s).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L223">method options</a>
</h3>

```typescript
options(path: string, handlers: RouteHandler[]): void
```


Routes OPTIONS requests on the given path to the provided handler(s).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L209">method post</a>
</h3>

```typescript
post(path: string, handlers: RouteHandler[]): void
```


Routes POST requests on the given path to the provided handler(s).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L179">method proxy</a>
</h3>

```typescript
proxy(path: string, target: string | pulumi.Output<Endpoint>): void
```


proxy forwards an HTTP request to a target URL or Endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L253">method publish</a>
</h3>

```typescript
publish(): HttpDeployment
```


Publishes an API to be internet accessible.

This should be called after describing desired routes and domains.
Throws an error if called multiple times on the same endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L202">method put</a>
</h3>

```typescript
put(path: string, handlers: RouteHandler[]): void
```


Routes PUT requests on the given path to the provided handler(s).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L188">method route</a>
</h3>

```typescript
route(method: string, path: string, handlers: RouteHandler[]): void
```


Routes any requests with given HTTP method on the given path to the
provided handler(s).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L169">method static</a>
</h3>

```typescript
static(path: string, localPath: string, options?: ServeStaticOptions): void
```


static serves a file or directory from within the source folder at the requested path.

<h2 class="pdoc-module-header" id="APIConstructor">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L120">interface APIConstructor</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L120">constructor</a>
</h3>

```typescript
new APIConstructor(apiName: string)
```

<h2 class="pdoc-module-header" id="Bucket">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/bucket.ts#L67">interface Bucket</a>
</h2>

Bucket is a simple blob store.

Gets are read-after-write consistent for puts of new blobs, and eventually consistent for overwriting puts.

Blobs in a bucket are encrypted at rest by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/bucket.ts#L105">method delete</a>
</h3>

```typescript
delete(key: string): Promise<void>
```


Delete a blob from the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/bucket.ts#L91">method get</a>
</h3>

```typescript
get(key: string): Promise<Buffer>
```


Get a blob from the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/bucket.ts#L83">method onDelete</a>
</h3>

```typescript
onDelete(name: string, handler: BucketHandler, filter?: BucketFilter): void
```


Registers a handler to be notified when blobs are deleted from the bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/bucket.ts#L75">method onPut</a>
</h3>

```typescript
onPut(name: string, handler: BucketHandler, filter?: BucketFilter): void
```


Registers a handler to be notified when blobs are put into the bucket (created or updated).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/bucket.ts#L98">method put</a>
</h3>

```typescript
put(key: string, contents: Buffer): Promise<void>
```


Insert a blob into the bucket.

<h2 class="pdoc-module-header" id="BucketConstructor">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/bucket.ts#L48">interface BucketConstructor</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/bucket.ts#L48">constructor</a>
</h3>

```typescript
new BucketConstructor(name: string, opts?: pulumi.ResourceOptions)
```


Creates a new Bucket.

* `name` A unique name for the bucket.
* `opts` A bag of options that controls how this resource behaves.

<h2 class="pdoc-module-header" id="BucketFilter">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/bucket.ts#L43">interface BucketFilter</a>
</h2>

BucketFilter specifies filters to apply to an [onPut] or [onDelete] subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/bucket.ts#L44">property keyPrefix</a>
</h3>

```typescript
keyPrefix?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/bucket.ts#L45">property keySuffix</a>
</h3>

```typescript
keySuffix?: undefined | string;
```

<h2 class="pdoc-module-header" id="BucketHandlerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/bucket.ts#L20">interface BucketHandlerArgs</a>
</h2>

BucketHandlerArgs are the arguments passed to an [onPut] or [onDelete] handler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/bucket.ts#L32">property eventTime</a>
</h3>

```typescript
eventTime: string;
```


The time (in ISO-8601 format) when the [put] or [delete] was completed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/bucket.ts#L24">property key</a>
</h3>

```typescript
key: string;
```


The key that was updated or deleted by the operation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/bucket.ts#L28">property size</a>
</h3>

```typescript
size: number;
```


The size, in bytes, of the blob that was [put].

<h2 class="pdoc-module-header" id="CacheFrom">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L126">interface CacheFrom</a>
</h2>

CacheFrom may be used to specify build stages to use for the Docker build cache. The final image is always
implicitly included.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L131">property stages</a>
</h3>

```typescript
stages?: string[];
```


An optional list of build stages to use for caching. Each build stage in this list will be built explicitly and
pushed to the target repository. A given stage's image will be tagged as "[stage-name]".

<h2 class="pdoc-module-header" id="Container">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L41">interface Container</a>
</h2>

Container specifies the metadata for a component of a Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L53">property build</a>
</h3>

```typescript
build?: string | ContainerBuild;
```


Either a path to a folder in which a Docker build should be run to construct the image for this
Container, or a ContainerBuild object with more detailed build instructions.  If `image` is also specified, the
built container will be tagged with that name, but otherwise will get an auto-generated image name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L112">property command</a>
</h3>

```typescript
command?: pulumi.Input<string[]>;
```


The command line that is passed to the container. This parameter maps to
`Cmd` in the [Create a
container](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container)
section of the [Docker Remote
API](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/)
and the `COMMAND` parameter to [docker run](https://docs.docker.com/engine/reference/commandline/run/). For more
information about the Docker `CMD` parameter, go to
https://docs.docker.com/engine/reference/builder/#cmd.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L69">property cpu</a>
</h3>

```typescript
cpu?: pulumi.Input<number>;
```


Number of CPUs for the container to use. Maps to the Docker `--cpus` option - see
https://docs.docker.com/engine/reference/commandline/run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L119">property dockerLabels</a>
</h3>

```typescript
dockerLabels?: pulumi.Input<{ ... }>;
```


A key/value map of labels to add to the container. This parameter maps to Labels in the [Create a
container](https://docs.docker.com/engine/api/v1.27/#operation/ContainerCreate) section of the [Docker Remote
API](https://docs.docker.com/engine/api/v1.27/) and the --label option to [docker
run](https://docs.docker.com/engine/reference/run/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L64">property environment</a>
</h3>

```typescript
environment?: undefined | { ... };
```


Optional environment variables to set and make available to the container
as it is running.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L58">property function</a>
</h3>

```typescript
function?: undefined | { ... };
```


The function code to use as the implementation of the contaner.  If `function` is specified,
neither `image` nor `build` are legal.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L47">property image</a>
</h3>

```typescript
image?: undefined | string;
```


The image to use for the container.  If `image` is specified, but not `build`, the image will be
pulled from the Docker Hub.  If `image` *and* `build` are specified, the `image` controls the
resulting image tag for the build image that gets pushed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L77">property memory</a>
</h3>

```typescript
memory?: pulumi.Input<number>;
```


The maximum amount of memory the container will be allowed to use. Maps to the Docker
`--memory` option - see
https://docs.docker.com/engine/reference/commandline/run.

This should be supplied in MB. i.e. A value of 1024 would equal one gigabyte.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L87">property memoryReservation</a>
</h3>

```typescript
memoryReservation?: pulumi.Input<number>;
```


The amount of memory to reserve for the container, but the container will
be allowed to use more memory if it's available.  At least one of
`memory` and `memoryReservation` must be specified.  Maps to the Docker
`--memory-reservation` option - see
https://docs.docker.com/engine/reference/commandline/run.

This should be supplied in MB. i.e. A value of 1024 would equal one gigabyte.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L94">property ports</a>
</h3>

```typescript
ports?: ContainerPort[];
```


An array of ports to publish from the container.  Ports are exposed using the TCP protocol.  If the [external]
flag is true, the port will be exposed to the Internet even if the service is running in a private network.
Maps to the Docker `--publish` option - see
https://docs.docker.com/engine/reference/commandline/run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L101">property volumes</a>
</h3>

```typescript
volumes?: ContainerVolumeMount[];
```


An array of volume mounts, indicating a volume to mount and a path within
the container at which to moung the volume.  Maps to the Docker
`--volume` option - see
https://docs.docker.com/engine/reference/commandline/run.

<h2 class="pdoc-module-header" id="ContainerBuild">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L137">interface ContainerBuild</a>
</h2>

ContainerBuild may be used to specify detailed instructions about how to build a container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L154">property args</a>
</h3>

```typescript
args?: undefined | { ... };
```


An optional map of named build-time argument variables to set during the Docker build.  This flag allows you
to pass built-time variables that can be accessed like environment variables inside the `RUN` instruction.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L161">property cacheFrom</a>
</h3>

```typescript
cacheFrom?: boolean | CacheFrom;
```


An optional CacheFrom object with information about the build stages to use for the Docker build cache.
This parameter maps to the --cache-from argument to the Docker CLI. If this parameter is `true`, only the final
image will be pulled and passed to --cache-from; if it is a CacheFrom object, the stages named therein will
also be pulled and passed to --cache-from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L144">property context</a>
</h3>

```typescript
context?: undefined | string;
```


context is a path to a directory to use for the Docker build context, usually the directory in which the
Dockerfile resides (although dockerfile may be used to choose a custom location independent of this choice).
If not specified, the context defaults to the current working directory; if a relative path is used, it
is relative to the current working directory that Pulumi is evaluating.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L149">property dockerfile</a>
</h3>

```typescript
dockerfile?: undefined | string;
```


dockerfile may be used to override the default Dockerfile name and/or location.  By default, it is assumed
to be a file named Dockerfile in the root of the build context.

<h2 class="pdoc-module-header" id="ContainerPort">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L166">interface ContainerPort</a>
</h2>

ContainerPort represents the information about how to expose a container port on a [Service].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L178">property external</a>
</h3>

```typescript
external?: undefined | false | true;
```


Whether the port should be exposed externally.  Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L170">property port</a>
</h3>

```typescript
port: number;
```


The incoming port where the service exposes the endpoint.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L186">property protocol</a>
</h3>

```typescript
protocol?: ContainerProtocol;
```


The protocol to use for exposing the service:
* `tcp`: Expose TCP externaly and to the container.
* `udp`: Expose UDP externally and to the container.
* `http`: Expose HTTP externally and to the container.
* `https`: Expose HTTPS externally and HTTP to the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L174">property targetPort</a>
</h3>

```typescript
targetPort?: undefined | number;
```


The target port on the backing container.  Defaults to the value of [port].

<h2 class="pdoc-module-header" id="ContainerVolumeMount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L191">interface ContainerVolumeMount</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L192">property containerPath</a>
</h3>

```typescript
containerPath: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L193">property sourceVolume</a>
</h3>

```typescript
sourceVolume: Volume;
```

<h2 class="pdoc-module-header" id="Containers">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L20">interface Containers</a>
</h2>

A collection of Containers

<h2 class="pdoc-module-header" id="DailySchedule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer.ts#L46">interface DailySchedule</a>
</h2>

DailySchedule describes a time of day ([[hourUTC]] and [[minuteUTC]]) at which a daily timer should fire.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer.ts#L50">property hourUTC</a>
</h3>

```typescript
hourUTC?: undefined | number;
```


The hour, in UTC, that the timer should fire.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer.ts#L54">property minuteUTC</a>
</h3>

```typescript
minuteUTC?: undefined | number;
```


The minute, in UTC, that the timer should fire.

<h2 class="pdoc-module-header" id="Domain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L277">interface Domain</a>
</h2>

Domain includes the domain name and certificate data to enable hosting an
API on a custom domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L285">property certificateBody</a>
</h3>

```typescript
certificateBody: string;
```


An SSL/TLS certficicate issued for this domain (`cert.pem`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L294">property certificateChain</a>
</h3>

```typescript
certificateChain: string;
```


The certificate chain for the SSL/TLS certificate provided for this
domain (`chain.pem`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L289">property certificatePrivateKey</a>
</h3>

```typescript
certificatePrivateKey: string;
```


An SSL/TLS private key issued for thie domain (`privkey.pem`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L281">property domainName</a>
</h3>

```typescript
domainName: string;
```


The domain name to associate with the API.

<h2 class="pdoc-module-header" id="Endpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L274">interface Endpoint</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L275">property hostname</a>
</h3>

```typescript
hostname: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L276">property port</a>
</h3>

```typescript
port: number;
```

<h2 class="pdoc-module-header" id="Endpoints">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L279">interface Endpoints</a>
</h2>
<h2 class="pdoc-module-header" id="HostPathVolume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L231">interface HostPathVolume</a>
</h2>

A volume mounted from a path on the host machine.

_Note_: This is an emphemeral volume which will not persist across container restarts or
across different hosts.  This is not something that most containers will need, but it offers
a powerful escape hatch for some applications.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L199">property kind</a>
</h3>

```typescript
kind: VolumeKind;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L235">property path</a>
</h3>

```typescript
path: string;
```

<h2 class="pdoc-module-header" id="HostPathVolumeConstructor">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L238">interface HostPathVolumeConstructor</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L238">constructor</a>
</h3>

```typescript
new HostPathVolumeConstructor(path: string)
```


Construct a new Volume with the given unique name.

<h2 class="pdoc-module-header" id="HostProperties">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L29">interface HostProperties</a>
</h2>

HostProperties describes the kind of host where a service or task can run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L35">property os</a>
</h3>

```typescript
os?: HostOperatingSystem;
```


The operating system of the host.

Default is "linux".

<h2 class="pdoc-module-header" id="HourlySchedule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer.ts#L60">interface HourlySchedule</a>
</h2>

HourlySchedule describes a time of the hour ([[minuteUTC]]) at which an hourly timer should fire.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer.ts#L64">property minuteUTC</a>
</h3>

```typescript
minuteUTC?: undefined | number;
```


The minute, in UTC, that the timer should fire.

<h2 class="pdoc-module-header" id="HttpDeployment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L260">interface HttpDeployment</a>
</h2>

HttpDeployment represents an API that has been deployed and is
available at a URL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L270">property customDomainNames</a>
</h3>

```typescript
customDomainNames: pulumi.Output<string>[];
```


An optional list of custom domain names, each corresponding to a
previous call to attachCustomDomain on the API.  Each name
should be mapped using a DNS A record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L264">property url</a>
</h3>

```typescript
url: pulumi.Output<string>;
```


The URL at which the HttpDeployment is available to the Internet.

<h2 class="pdoc-module-header" id="IntervalRate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer.ts#L28">interface IntervalRate</a>
</h2>

IntervalRate describes the rate at which a timer will fire.

At least one of [[minutes]], [[hours]] or [[days]] must be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer.ts#L40">property days</a>
</h3>

```typescript
days?: undefined | number;
```


The number of days in the interval.  Must be a positive integer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer.ts#L36">property hours</a>
</h3>

```typescript
hours?: undefined | number;
```


The number of hours in the interval.  Must be a positive integer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer.ts#L32">property minutes</a>
</h3>

```typescript
minutes?: undefined | number;
```


The number of minutes in the interval.  Must be a positive integer.

<h2 class="pdoc-module-header" id="Request">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L21">interface Request</a>
</h2>

Request represents an API request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L58">property baseUrl</a>
</h3>

```typescript
baseUrl: string;
```


The base url on which this http request was served.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L25">property body</a>
</h3>

```typescript
body: Buffer;
```


The body of the HTTP request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L38">property headers</a>
</h3>

```typescript
headers: { ... };
```


The headers of the HTTP request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L62">property hostname</a>
</h3>

```typescript
hostname: string;
```


The hostname of the request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L29">property method</a>
</h3>

```typescript
method: string;
```


The method of the HTTP request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L34">property params</a>
</h3>

```typescript
params: { ... };
```


The path parameters of the HTTP request. Each `{param}` in the matched
route is available as a property of this oject.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L50">property path</a>
</h3>

```typescript
path: string;
```


The raw path from the HTTP request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L54">property protocol</a>
</h3>

```typescript
protocol: string;
```


The protocol of the request (e.g. HTTP/HTTPS).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L46">property query</a>
</h3>

```typescript
query: { ... };
```


The query parameters parsed from the query string of the request URL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L42">property rawHeaders</a>
</h3>

```typescript
rawHeaders: string[];
```


The headers of the HTTP request.

<h2 class="pdoc-module-header" id="Response">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L68">interface Response</a>
</h2>

Response represents the response to an API request.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L97">method end</a>
</h3>

```typescript
end(data?: string | Buffer, encoding?: undefined | string): void
```


Sends the HTTP response, optionally including data to write to the HTTP
response body.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L82">method getHeader</a>
</h3>

```typescript
getHeader(name: string): string
```


Gets the Headers for the Response

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L102">method json</a>
</h3>

```typescript
json(obj: any): void
```


JSON serializes an object, writes it to the HTTP response body, and sends
the HTTP response.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L107">method redirect</a>
</h3>

```typescript
redirect(url: string): void
```


Mark the response to redirect the client to the provided URL with
the optional status code, defaulting to 302.


```typescript
redirect(status: number, url: string): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L87">method setHeader</a>
</h3>

```typescript
setHeader(name: string, value: string): Response
```


Sets a header on the HTTP response and returns the `Response` for
chaining operations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L78">method status</a>
</h3>

```typescript
status(code: number): Response
```


Sets the HTTP response status code and returns a `Response` for chaining
operations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L92">method write</a>
</h3>

```typescript
write(data: string | Buffer, encoding?: undefined | string): Response
```


Writes a string to the HTTP response body and returns the `Response` for
chaining operations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L73">property locals</a>
</h3>

```typescript
locals: any;
```


Object containing local variables scoped to a single request. Useful for
exposing request-level information such as user settings.

<h2 class="pdoc-module-header" id="ServeStaticOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L126">interface ServeStaticOptions</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L131">property contentType</a>
</h3>

```typescript
contentType?: undefined | string;
```


The `content-type` to serve the file as.  Only valid when localPath points to a file.  If
localPath points to a directory, the content types for all files will be inferred.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L136">property index</a>
</h3>

```typescript
index?: boolean | string;
```


By default API.static will also serve 'index.html' in response to a request on a
directory. To disable this set false or to supply a new index pass a string.

<h2 class="pdoc-module-header" id="Service">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L290">interface Service</a>
</h2>

A persistent service running as part of the Pulumi Cloud application. A
collection of container specifications are provided to define the compute
that will run inside this service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L316">method getEndpoint</a>
</h3>

```typescript
getEndpoint(containerName?: undefined | string, containerPort?: undefined | number): Promise<Endpoint>
```


The exposed hostname and port for connecting to the given containerName
on the given containerPort.  If containerName is not provided, the first
container in the service is used.  If containerPort is not provided, the
first exposed port is used.

Only usable on the inside.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L306">property defaultEndpoint</a>
</h3>

```typescript
defaultEndpoint: pulumi.Output<Endpoint>;
```


The primary endpoint exposed by the service.  All endpoints (including this one)
can also be retrieved by using the 'Service.endpoints' property.  Note: this value
may not be present if the service does not actually expose any endpoints.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L299">property endpoints</a>
</h3>

```typescript
endpoints: pulumi.Output<Endpoints>;
```


The exposed hostname and port for connecting to the given containerName
on the given containerPort.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L291">property name</a>
</h3>

```typescript
name: string;
```

<h2 class="pdoc-module-header" id="ServiceArguments">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L252">interface ServiceArguments</a>
</h2>

The arguments to construct a Service object. These arguments may include container information, for simple
single-container scenarios, or you may specify that information using the containers property. If a single container
is specified in-line, it is implicitly given the name "default".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L53">property build</a>
</h3>

```typescript
build?: string | ContainerBuild;
```


Either a path to a folder in which a Docker build should be run to construct the image for this
Container, or a ContainerBuild object with more detailed build instructions.  If `image` is also specified, the
built container will be tagged with that name, but otherwise will get an auto-generated image name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L112">property command</a>
</h3>

```typescript
command?: pulumi.Input<string[]>;
```


The command line that is passed to the container. This parameter maps to
`Cmd` in the [Create a
container](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container)
section of the [Docker Remote
API](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/)
and the `COMMAND` parameter to [docker run](https://docs.docker.com/engine/reference/commandline/run/). For more
information about the Docker `CMD` parameter, go to
https://docs.docker.com/engine/reference/builder/#cmd.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L256">property containers</a>
</h3>

```typescript
containers?: Containers;
```


A collection of containers that will be deployed as part of this Service, if there are multiple.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L69">property cpu</a>
</h3>

```typescript
cpu?: pulumi.Input<number>;
```


Number of CPUs for the container to use. Maps to the Docker `--cpus` option - see
https://docs.docker.com/engine/reference/commandline/run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L119">property dockerLabels</a>
</h3>

```typescript
dockerLabels?: pulumi.Input<{ ... }>;
```


A key/value map of labels to add to the container. This parameter maps to Labels in the [Create a
container](https://docs.docker.com/engine/api/v1.27/#operation/ContainerCreate) section of the [Docker Remote
API](https://docs.docker.com/engine/api/v1.27/) and the --label option to [docker
run](https://docs.docker.com/engine/reference/run/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L64">property environment</a>
</h3>

```typescript
environment?: undefined | { ... };
```


Optional environment variables to set and make available to the container
as it is running.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L58">property function</a>
</h3>

```typescript
function?: undefined | { ... };
```


The function code to use as the implementation of the contaner.  If `function` is specified,
neither `image` nor `build` are legal.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L265">property host</a>
</h3>

```typescript
host?: HostProperties;
```


The properties of the host where this service can run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L47">property image</a>
</h3>

```typescript
image?: undefined | string;
```


The image to use for the container.  If `image` is specified, but not `build`, the image will be
pulled from the Docker Hub.  If `image` *and* `build` are specified, the `image` controls the
resulting image tag for the build image that gets pushed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L77">property memory</a>
</h3>

```typescript
memory?: pulumi.Input<number>;
```


The maximum amount of memory the container will be allowed to use. Maps to the Docker
`--memory` option - see
https://docs.docker.com/engine/reference/commandline/run.

This should be supplied in MB. i.e. A value of 1024 would equal one gigabyte.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L87">property memoryReservation</a>
</h3>

```typescript
memoryReservation?: pulumi.Input<number>;
```


The amount of memory to reserve for the container, but the container will
be allowed to use more memory if it's available.  At least one of
`memory` and `memoryReservation` must be specified.  Maps to the Docker
`--memory-reservation` option - see
https://docs.docker.com/engine/reference/commandline/run.

This should be supplied in MB. i.e. A value of 1024 would equal one gigabyte.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L94">property ports</a>
</h3>

```typescript
ports?: ContainerPort[];
```


An array of ports to publish from the container.  Ports are exposed using the TCP protocol.  If the [external]
flag is true, the port will be exposed to the Internet even if the service is running in a private network.
Maps to the Docker `--publish` option - see
https://docs.docker.com/engine/reference/commandline/run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L261">property replicas</a>
</h3>

```typescript
replicas?: undefined | number;
```


The number of copies of this Service's containers to deploy and maintain
as part of the running service.  Defaults to `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L101">property volumes</a>
</h3>

```typescript
volumes?: ContainerVolumeMount[];
```


An array of volume mounts, indicating a volume to mount and a path within
the container at which to moung the volume.  Maps to the Docker
`--volume` option - see
https://docs.docker.com/engine/reference/commandline/run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L271">property waitForSteadyState</a>
</h3>

```typescript
waitForSteadyState?: undefined | false | true;
```


Determines whether the service should wait to fully transition to a new steady state on creation and updates. If
set to false, the service may complete its deployment before it is fully ready to be used. Defaults to 'true'.

<h2 class="pdoc-module-header" id="ServiceConstructor">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L319">interface ServiceConstructor</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L319">constructor</a>
</h3>

```typescript
new ServiceConstructor(name: string, args: ServiceArguments, opts?: pulumi.ResourceOptions)
```


Construct a new Service, which is one or more managed replicas of a group of one or more Containers.

* `name` The unique name of the service.
* `opts` A bag of options that controls how this resource behaves.

<h2 class="pdoc-module-header" id="SharedVolume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L205">interface SharedVolume</a>
</h2>

A shared volume that can be mounted into one or more containers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L199">property kind</a>
</h3>

```typescript
kind: VolumeKind;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L209">property name</a>
</h3>

```typescript
name: string;
```

<h2 class="pdoc-module-header" id="SharedVolumeConstructor">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L212">interface SharedVolumeConstructor</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L212">constructor</a>
</h3>

```typescript
new SharedVolumeConstructor(name: string, opts?: pulumi.ResourceOptions)
```


Construct a new Volume with the given unique name.

* `name` The unique name of the volume.
* `opts` A bag of options that controls how this resource behaves.

<h2 class="pdoc-module-header" id="Stream">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/topic.ts#L62">interface Stream</a>
</h2>

A Stream<T> provides access to listen to an (infinite) stream of items coming
from a data source.  Unlike [[Topic]], a Stream provides only access to read
from the stream, not the ability to publish new items to the stream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/topic.ts#L75">method subscribe</a>
</h3>

```typescript
subscribe(name: string, handler: { ... }): void
```


Subscribe to items published to this stream.

Each subscription receives all items published to the stream. If a
subscription handler returns a failed promise, the subscription handler
may be retried some number of times.  If no retry is successful, the item
will be sent to the global error handler.  Note that as a result,
subscription handlers must ensure they can safely be retried.

<h2 class="pdoc-module-header" id="Table">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/table.ts#L57">interface Table</a>
</h2>

Table is a simple document store for persistent application backend storage.

```javascript
let table = new Table("my-table");
await table.insert({id: "kuibai", data: 42});
let item = await table.get({id: "kuibai"});
```

Tables support a single primary key with a user-defined name and type.  All
other document properties are schemaless.  If not specified, a primary key
named `id` with type `string` is used.

All queries provide a subset of properties to filter on, and only filters on
value equality are supported.  The `get`, `update` and `delete` operations
expect the query to contain only the value for the primary key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/table.ts#L101">method delete</a>
</h3>

```typescript
delete(query: Object): Promise<void>
```


Deletes a documents from the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/table.ts#L75">method get</a>
</h3>

```typescript
get(query: Object): Promise<any>
```


Get a document from the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/table.ts#L83">method insert</a>
</h3>

```typescript
insert(item: Object): Promise<void>
```


Insert a document into the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/table.ts#L92">method scan</a>
</h3>

```typescript
scan(): Promise<any[]>
```


Gets all documents from the table.


```typescript
scan(callback: { ... }): Promise<void>
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/table.ts#L111">method update</a>
</h3>

```typescript
update(query: Object, updates: Object): Promise<void>
```


Updates a documents in the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/table.ts#L61">property primaryKey</a>
</h3>

```typescript
primaryKey: pulumi.Output<string>;
```


The name of the primary key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/table.ts#L65">property primaryKeyType</a>
</h3>

```typescript
primaryKeyType: pulumi.Output<string>;
```


The type of the primary key.

<h2 class="pdoc-module-header" id="TableConstructor">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/table.ts#L23">interface TableConstructor</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/table.ts#L23">constructor</a>
</h3>

```typescript
new TableConstructor(name: string, primaryKey?: pulumi.Input<string>, primaryKeyType?: pulumi.Input<PrimaryKeyType>, opts?: pulumi.ResourceOptions)
```


Creates a new Table.

* `name` A unique name for the table.
* `primaryKey` An optional primary key name.
* `primaryKeyType` An optional primary key type.
* `opts` A bag of options that controls how this resource behaves.

<h2 class="pdoc-module-header" id="Task">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L350">interface Task</a>
</h2>

A Task represents a container which can be [run] dynamically whenever (and
as many times as) needed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L354">method run</a>
</h3>

```typescript
run(options?: TaskRunOptions): Promise<void>
```


Run the task, passing in additional task run options.

<h2 class="pdoc-module-header" id="TaskConstructor">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L357">interface TaskConstructor</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L357">constructor</a>
</h3>

```typescript
new TaskConstructor(name: string, container: Container, opts?: pulumi.ResourceOptions)
```


Construct a new Task, which is a Container that can be run many times as individual tasks.

* `name` The unique name of the task.
* `container` The container specification.
* `opts` A bag of options that controls how this resource behaves.

<h2 class="pdoc-module-header" id="TaskRunOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L335">interface TaskRunOptions</a>
</h2>

Arguments to use for initializing a single run of the Task

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L339">property environment</a>
</h3>

```typescript
environment?: Record<string, string>;
```


Optional environment variables to override those set in the container definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L343">property host</a>
</h3>

```typescript
host?: HostProperties;
```


The properties of the host where this task can run.

<h2 class="pdoc-module-header" id="Topic">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/topic.ts#L36">interface Topic</a>
</h2>

A Topic<T> is used to distribute work which will be run concurrently by any
susbcribed handlers.  Producers can [[publish]] to the topic, and consumers
can [[subscribe]] to be notified when new items are published.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/topic.ts#L52">method subscribe</a>
</h3>

```typescript
subscribe(name: string, handler: { ... }): void
```


Subscribe to items published to this topic.

Each subscription receives all items published to the topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/topic.ts#L42">property publish</a>
</h3>

```typescript
publish: { ... };
```


Publish an item to this Topic.

<h2 class="pdoc-module-header" id="TopicConstructor">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/topic.ts#L17">interface TopicConstructor</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/topic.ts#L17">constructor</a>
</h3>

```typescript
new TopicConstructor<T>(name: string, opts?: pulumi.ResourceOptions)
```


Allocate a new Topic with a given name.

* `name` The unique name of the Topic.
* `opts` A bag of options that controls how this resource behaves.

<h2 class="pdoc-module-header" id="Volume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L198">interface Volume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L199">property kind</a>
</h3>

```typescript
kind: VolumeKind;
```

<h2 class="pdoc-module-header" id="Action">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/timer.ts#L20">type Action</a>
</h2>

```typescript
type Action = { ... };
```


Action is a handler that performs an action in response to a timer firing.

<h2 class="pdoc-module-header" id="BucketHandler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/bucket.ts#L38">type BucketHandler</a>
</h2>

```typescript
type BucketHandler = { ... };
```


BucketHandler is the callback that handles an [onPut] or [onDelete] event.

<h2 class="pdoc-module-header" id="ContainerProtocol">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L189">type ContainerProtocol</a>
</h2>

```typescript
type ContainerProtocol = tcp | udp | http | https;
```

<h2 class="pdoc-module-header" id="HostOperatingSystem">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L24">type HostOperatingSystem</a>
</h2>

```typescript
type HostOperatingSystem = linux | windows;
```

<h2 class="pdoc-module-header" id="HttpEndpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L300">type HttpEndpoint</a>
</h2>

```typescript
type HttpEndpoint = API;
```

<h2 class="pdoc-module-header" id="PrimaryKeyType">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/table.ts#L21">type PrimaryKeyType</a>
</h2>

```typescript
type PrimaryKeyType = string | number | boolean;
```


The available types for primary keys. The default primary key type is
`string`.

<h2 class="pdoc-module-header" id="RouteHandler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/api.ts#L118">type RouteHandler</a>
</h2>

```typescript
type RouteHandler = { ... };
```


RouteHandler represents a handler for a route on an API.

Implementations should invoke methods on `res` to respond to the request, or
invoke `next` to pass control to the next available handler on the route for
further processing.

<h2 class="pdoc-module-header" id="VolumeKind">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/api/service.ts#L196">type VolumeKind</a>
</h2>

```typescript
type VolumeKind = SharedVolume | HostPathVolume;
```

