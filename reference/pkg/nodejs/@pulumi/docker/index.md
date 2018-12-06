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

* <a href="#Container">class Container</a>
* <a href="#Image">class Image</a>
* <a href="#Network">class Network</a>
* <a href="#Provider">class Provider</a>
* <a href="#RemoteImage">class RemoteImage</a>
* <a href="#Volume">class Volume</a>
* <a href="#buildAndPushImage">function buildAndPushImage</a>
* <a href="#buildAndPushImageAsync">function buildAndPushImageAsync</a>
* <a href="#getEnv">function getEnv</a>
* <a href="#getEnvBoolean">function getEnvBoolean</a>
* <a href="#getEnvNumber">function getEnvNumber</a>
* <a href="#requireWithDefault">function requireWithDefault</a>
* <a href="#CacheFrom">interface CacheFrom</a>
* <a href="#ContainerArgs">interface ContainerArgs</a>
* <a href="#ContainerState">interface ContainerState</a>
* <a href="#DockerBuild">interface DockerBuild</a>
* <a href="#ImageArgs">interface ImageArgs</a>
* <a href="#ImageRegistry">interface ImageRegistry</a>
* <a href="#NetworkArgs">interface NetworkArgs</a>
* <a href="#NetworkState">interface NetworkState</a>
* <a href="#ProviderArgs">interface ProviderArgs</a>
* <a href="#Registry">interface Registry</a>
* <a href="#RemoteImageArgs">interface RemoteImageArgs</a>
* <a href="#RemoteImageState">interface RemoteImageState</a>
* <a href="#VolumeArgs">interface VolumeArgs</a>
* <a href="#VolumeState">interface VolumeState</a>

<a href="/container.ts">container.ts</a> <a href="/docker.ts">docker.ts</a> <a href="/image.ts">image.ts</a> <a href="/network.ts">network.ts</a> <a href="/provider.ts">provider.ts</a> <a href="/remoteImage.ts">remoteImage.ts</a> <a href="/utilities.ts">utilities.ts</a> <a href="/volume.ts">volume.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>

* <a href="config">config</a>

<h2 class="pdoc-module-header" id="Container">
<a class="pdoc-member-name" href="/container.ts#L10">class Container</a>
</h2>

Manages the lifecycle of a Docker container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L245">constructor</a>
</h3>

```typescript
new Container(name: string, args: ContainerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Container resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ContainerState): Container
```


Get an existing Container resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L26">property attach</a>
</h3>

```typescript
public attach: pulumi.Output<boolean | undefined>;
```


If true attach to the container after its creation and waits the end of his execution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L30">property bridge</a>
</h3>

```typescript
public bridge: pulumi.Output<string>;
```


The network bridge of the container as read from its NetworkSettings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L34">property capabilities</a>
</h3>

```typescript
public capabilities: pulumi.Output<{ ... } | undefined>;
```


See Capabilities below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L40">property command</a>
</h3>

```typescript
public command: pulumi.Output<string[] | undefined>;
```


The command to use to start the
container. For example, to run `/usr/bin/myprogram -f baz.conf` set the
command to be `["/usr/bin/myprogram", "-f", "baz.conf"]`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L44">property containerLogs</a>
</h3>

```typescript
public containerLogs: pulumi.Output<string>;
```


The logs of the container if its execution is done (`attach` must be disabled).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L48">property cpuSet</a>
</h3>

```typescript
public cpuSet: pulumi.Output<string | undefined>;
```


A comma-separated list or hyphen-separated range of CPUs a container can use, e.g. `0-1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L52">property cpuShares</a>
</h3>

```typescript
public cpuShares: pulumi.Output<number | undefined>;
```


CPU shares (relative weight) for the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L56">property destroyGraceSeconds</a>
</h3>

```typescript
public destroyGraceSeconds: pulumi.Output<number | undefined>;
```


If defined will attempt to stop the container before destroying. Container will be destroyed after `n` seconds or on successful stop.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L60">property devices</a>
</h3>

```typescript
public devices: pulumi.Output<{ ... }[] | undefined>;
```


See Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L64">property dns</a>
</h3>

```typescript
public dns: pulumi.Output<string[] | undefined>;
```


Set of DNS servers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L68">property dnsOpts</a>
</h3>

```typescript
public dnsOpts: pulumi.Output<string[] | undefined>;
```


Set of DNS options used by the DNS provider(s), see `resolv.conf` documentation for valid list of options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L72">property dnsSearches</a>
</h3>

```typescript
public dnsSearches: pulumi.Output<string[] | undefined>;
```


Set of DNS search domains that are used when bare unqualified hostnames are used inside of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L76">property domainname</a>
</h3>

```typescript
public domainname: pulumi.Output<string | undefined>;
```


Domain name of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L84">property entrypoints</a>
</h3>

```typescript
public entrypoints: pulumi.Output<string[] | undefined>;
```


The command to use as the
Entrypoint for the container. The Entrypoint allows you to configure a
container to run as an executable. For example, to run `/usr/bin/myprogram`
when starting a container, set the entrypoint to be
`["/usr/bin/myprogram"]`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L88">property envs</a>
</h3>

```typescript
public envs: pulumi.Output<string[] | undefined>;
```


Environment variables to set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L92">property exitCode</a>
</h3>

```typescript
public exitCode: pulumi.Output<number>;
```


The exit code of the container if its execution is done (`must_run` must be disabled).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L97">property gateway</a>
</h3>

```typescript
public gateway: pulumi.Output<string>;
```


*Deprecated:* Use `network_data` instead. The network gateway of the container as read from its
NetworkSettings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L101">property healthcheck</a>
</h3>

```typescript
public healthcheck: pulumi.Output<{ ... } | undefined>;
```


See Healthcheck below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L109">property hostname</a>
</h3>

```typescript
public hostname: pulumi.Output<string | undefined>;
```


Hostname of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L105">property hosts</a>
</h3>

```typescript
public hosts: pulumi.Output<{ ... }[] | undefined>;
```


Hostname to add.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L115">property image</a>
</h3>

```typescript
public image: pulumi.Output<string>;
```


The ID of the image to back this container.
The easiest way to get this value is to use the `docker_image` resource
as is shown in the example above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L119">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string>;
```


*Deprecated:* Use `network_data` instead. The IP address of the container's first network it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L124">property ipPrefixLength</a>
</h3>

```typescript
public ipPrefixLength: pulumi.Output<number>;
```


*Deprecated:* Use `network_data` instead. The IP prefix length of the container as read from its
NetworkSettings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L129">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


Key/value pairs to set as labels on the
container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L134">property links</a>
</h3>

```typescript
public links: pulumi.Output<string[] | undefined>;
```


Set of links for link based
connectivity between containers that are running on the same host.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L139">property logDriver</a>
</h3>

```typescript
public logDriver: pulumi.Output<string | undefined>;
```


The logging driver to use for the container.
Defaults to "json-file".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L144">property logOpts</a>
</h3>

```typescript
public logOpts: pulumi.Output<{ ... } | undefined>;
```


Key/value pairs to use as options for
the logging driver.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L148">property logs</a>
</h3>

```typescript
public logs: pulumi.Output<boolean | undefined>;
```


Save the container logs (`attach` must be enabled).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L153">property maxRetryCount</a>
</h3>

```typescript
public maxRetryCount: pulumi.Output<number | undefined>;
```


The maximum amount of times to an attempt
a restart when `restart` is set to "on-failure"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L157">property memory</a>
</h3>

```typescript
public memory: pulumi.Output<number | undefined>;
```


The memory limit for the container in MBs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L162">property memorySwap</a>
</h3>

```typescript
public memorySwap: pulumi.Output<number | undefined>;
```


The total memory limit (memory + swap) for the
container in MBs. This setting may compute to `-1` after `terraform apply` if the target host doesn't support memory swap, when that is the case docker will use a soft limitation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L168">property mustRun</a>
</h3>

```typescript
public mustRun: pulumi.Output<boolean | undefined>;
```


If true, then the Docker container will be
kept running. If false, then as long as the container exists, Terraform
assumes it is successful.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L169">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L173">property networkAliases</a>
</h3>

```typescript
public networkAliases: pulumi.Output<string[] | undefined>;
```


Network aliases of the container for user-defined networks only. *Deprecated:* use `networks_advanced` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L178">property networkDatas</a>
</h3>

```typescript
public networkDatas: pulumi.Output<{ ... }[]>;
```


(Map of a block) The IP addresses of the container on each
network. Key are the network names, values are the IP addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L182">property networkMode</a>
</h3>

```typescript
public networkMode: pulumi.Output<string | undefined>;
```


Network mode of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L187">property networks</a>
</h3>

```typescript
public networks: pulumi.Output<string[] | undefined>;
```


Id of the networks in which the
container is. *Deprecated:* use `networks_advanced` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L191">property networksAdvanced</a>
</h3>

```typescript
public networksAdvanced: pulumi.Output<{ ... }[] | undefined>;
```


See Networks Advanced below for details. If this block has priority to the deprecated `network_alias` and `network` properties.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L195">property pidMode</a>
</h3>

```typescript
public pidMode: pulumi.Output<string | undefined>;
```


The PID (Process) Namespace mode for the container. Either `container:<name|id>` or `host`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L199">property ports</a>
</h3>

```typescript
public ports: pulumi.Output<{ ... }[] | undefined>;
```


See Ports below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L203">property privileged</a>
</h3>

```typescript
public privileged: pulumi.Output<boolean | undefined>;
```


Run container in privileged mode.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L207">property publishAllPorts</a>
</h3>

```typescript
public publishAllPorts: pulumi.Output<boolean | undefined>;
```


Publish all ports of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L212">property restart</a>
</h3>

```typescript
public restart: pulumi.Output<string | undefined>;
```


The restart policy for the container. Must be
one of "no", "on-failure", "always", "unless-stopped".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L217">property rm</a>
</h3>

```typescript
public rm: pulumi.Output<boolean | undefined>;
```


If true, then the container will be automatically removed after his execution. Terraform
won't check this container after creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L222">property start</a>
</h3>

```typescript
public start: pulumi.Output<boolean | undefined>;
```


If true, then the Docker container will be
started after creation. If false, then the container is only created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L227">property ulimits</a>
</h3>

```typescript
public ulimits: pulumi.Output<{ ... }[] | undefined>;
```


See Ulimits below for
details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L231">property uploads</a>
</h3>

```typescript
public uploads: pulumi.Output<{ ... }[] | undefined>;
```


See File Upload below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L237">property user</a>
</h3>

```typescript
public user: pulumi.Output<string | undefined>;
```


User used for run the first process. Format is
`user` or `user:group` which user and group can be passed literraly or
by name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L241">property usernsMode</a>
</h3>

```typescript
public usernsMode: pulumi.Output<string | undefined>;
```


Sets the usernamespace mode for the container when usernamespace remapping option is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L245">property volumes</a>
</h3>

```typescript
public volumes: pulumi.Output<{ ... }[] | undefined>;
```


See Volumes below for details.

<h2 class="pdoc-module-header" id="Image">
<a class="pdoc-member-name" href="/image.ts#L78">class Image</a>
</h2>

A docker.Image resource represents a Docker image built locally which is published and made
available via a remote Docker registry.  This can be used to ensure that a Docker source
directory from a local deployment environment is built and pushed to a cloud-hosted Docker
registry as part of a Pulumi deployment, so that it can be referenced as an image input from
other cloud services that reference Docker images - including Kubernetes Pods, AWS ECS Tasks, and
Azure Container Instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/image.ts#L101">constructor</a>
</h3>

```typescript
new Image(name: string, args: ImageArgs, opts?: pulumi.ComponentResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/image.ts#L83">property baseImageName</a>
</h3>

```typescript
public baseImageName: pulumi.Output<string>;
```


The base image name that was built and pushed.  This does not include the id annotation, so
is not pinned to the specific build performed by this docker.Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/image.ts#L101">property digest</a>
</h3>

```typescript
public digest: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/image.ts#L94">property id</a>
</h3>

```typescript
public id: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/image.ts#L87">property imageName</a>
</h3>

```typescript
public imageName: pulumi.Output<string>;
```


The unique pinned image name on the remote repository.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/image.ts#L91">property registryServer</a>
</h3>

```typescript
public registryServer: pulumi.Output<string | undefined>;
```


The server the image is located at.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Network">
<a class="pdoc-member-name" href="/network.ts#L12">class Network</a>
</h2>

Manages a Docker Network. This can be used alongside
[docker\_container](https://www.terraform.io/docs/providers/docker/r/container.html)
to create virtual networks within the docker environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L78">constructor</a>
</h3>

```typescript
new Network(name: string, args?: NetworkArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Network resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkState): Network
```


Get an existing Network resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L29">property attachable</a>
</h3>

```typescript
public attachable: pulumi.Output<boolean | undefined>;
```


Enable manual container attachment to the network.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L34">property checkDuplicate</a>
</h3>

```typescript
public checkDuplicate: pulumi.Output<boolean | undefined>;
```


Requests daemon to check for networks
with same name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L39">property driver</a>
</h3>

```typescript
public driver: pulumi.Output<string>;
```


Name of the network driver to use. Defaults to
`bridge` driver.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L44">property ingress</a>
</h3>

```typescript
public ingress: pulumi.Output<boolean | undefined>;
```


Create swarm routing-mesh network.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L49">property internal</a>
</h3>

```typescript
public internal: pulumi.Output<boolean>;
```


Restrict external access to the network.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L54">property ipamConfigs</a>
</h3>

```typescript
public ipamConfigs: pulumi.Output<{ ... }[] | undefined>;
```


See IPAM config below for
details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L59">property ipamDriver</a>
</h3>

```typescript
public ipamDriver: pulumi.Output<string | undefined>;
```


Driver used by the custom IP scheme of the
network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L64">property ipv6</a>
</h3>

```typescript
public ipv6: pulumi.Output<boolean | undefined>;
```


Enable IPv6 networking.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L68">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


User-defined key/value metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L72">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Docker network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L77">property options</a>
</h3>

```typescript
public options: pulumi.Output<{ ... }>;
```


Network specific options to be used by
the drivers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L78">property scope</a>
</h3>

```typescript
public scope: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Provider">
<a class="pdoc-member-name" href="/provider.ts#L10">class Provider</a>
</h2>

The provider type for the docker package

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L10">constructor</a>
</h3>

```typescript
new Provider(name: string, args?: ProviderArgs, opts?: pulumi.ResourceOptions)
```


Create a Provider resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RemoteImage">
<a class="pdoc-member-name" href="/remoteImage.ts#L14">class RemoteImage</a>
</h2>

Pulls a Docker image to a given Docker host from a Docker Registry.

This resource will *not* pull new layers of the image automatically unless used in
conjunction with [`docker_registry_image`](https://www.terraform.io/docs/providers/docker/d/registry_image.html)
data source to update the `pull_triggers` field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/remoteImage.ts#L48">constructor</a>
</h3>

```typescript
new RemoteImage(name: string, args: RemoteImageArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RemoteImage resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/remoteImage.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RemoteImageState): RemoteImage
```


Get an existing RemoteImage resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/remoteImage.ts#L32">property keepLocally</a>
</h3>

```typescript
public keepLocally: pulumi.Output<boolean | undefined>;
```


If true, then the Docker image won't be
deleted on destroy operation. If this is false, it will delete the image from
the docker local storage on destroy operation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/remoteImage.ts#L33">property latest</a>
</h3>

```typescript
public latest: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/remoteImage.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Docker image, including any tags or SHA256 repo digests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/remoteImage.ts#L41">property pullTrigger</a>
</h3>

```typescript
public pullTrigger: pulumi.Output<string | undefined>;
```


**Deprecated**, use `pull_triggers` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/remoteImage.ts#L48">property pullTriggers</a>
</h3>

```typescript
public pullTriggers: pulumi.Output<string[] | undefined>;
```


List of values which cause an
image pull when changed. This is used to store the image digest from the
registry when using the `docker_registry_image` [data source](https://www.terraform.io/docs/providers/docker/d/registry_image.html)
to trigger an image update.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Volume">
<a class="pdoc-member-name" href="/volume.ts#L12">class Volume</a>
</h2>

Creates and destroys a volume in Docker. This can be used alongside
[docker\_container](https://www.terraform.io/docs/providers/docker/r/container.html)
to prepare volumes that can be shared across containers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/volume.ts#L42">constructor</a>
</h3>

```typescript
new Volume(name: string, args?: VolumeArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Volume resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/volume.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VolumeState): Volume
```


Get an existing Volume resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/volume.ts#L28">property driver</a>
</h3>

```typescript
public driver: pulumi.Output<string>;
```


Driver type for the volume (defaults to local).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/volume.ts#L32">property driverOpts</a>
</h3>

```typescript
public driverOpts: pulumi.Output<{ ... } | undefined>;
```


Options specific to the driver.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/volume.ts#L36">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


User-defined key/value metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/volume.ts#L37">property mountpoint</a>
</h3>

```typescript
public mountpoint: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/volume.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Docker volume (generated if not
provided).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="buildAndPushImage">
<a class="pdoc-member-name" href="/docker.ts#L117">function buildAndPushImage</a>
</h2>

```typescript
buildAndPushImage(imageName: string, pathOrBuild: string | DockerBuild, repositoryUrl: pulumi.Input<string>, logResource: pulumi.Resource, connectToRegistry: { ... }): pulumi.Output<string>
```

<h2 class="pdoc-module-header" id="buildAndPushImageAsync">
<a class="pdoc-member-name" href="/docker.ts#L137">function buildAndPushImageAsync</a>
</h2>

```typescript
buildAndPushImageAsync(baseImageName: string, pathOrBuild: string | DockerBuild, repositoryUrl: string, logResource: pulumi.Resource, connectToRegistry?: { ... }): Promise<string>
```

<h2 class="pdoc-module-header" id="getEnv">
<a class="pdoc-member-name" href="/utilities.ts#L7">function getEnv</a>
</h2>

```typescript
getEnv(vars: string[]): string | undefined
```

<h2 class="pdoc-module-header" id="getEnvBoolean">
<a class="pdoc-member-name" href="/utilities.ts#L17">function getEnvBoolean</a>
</h2>

```typescript
getEnvBoolean(vars: string[]): boolean | undefined
```

<h2 class="pdoc-module-header" id="getEnvNumber">
<a class="pdoc-member-name" href="/utilities.ts#L32">function getEnvNumber</a>
</h2>

```typescript
getEnvNumber(vars: string[]): number | undefined
```

<h2 class="pdoc-module-header" id="requireWithDefault">
<a class="pdoc-member-name" href="/utilities.ts#L43">function requireWithDefault</a>
</h2>

```typescript
requireWithDefault<T>(req: { ... }, def: T | undefined): T
```

<h2 class="pdoc-module-header" id="CacheFrom">
<a class="pdoc-member-name" href="/docker.ts#L33">interface CacheFrom</a>
</h2>

CacheFrom may be used to specify build stages to use for the Docker build cache. The final image
is always implicitly included.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/docker.ts#L39">property stages</a>
</h3>

```typescript
stages?: string[];
```


An optional list of build stages to use for caching. Each build stage in this list will be
built explicitly and pushed to the target repository. A given stage's image will be tagged as
"[stage-name]".

<h2 class="pdoc-module-header" id="ContainerArgs">
<a class="pdoc-member-name" href="/container.ts#L601">interface ContainerArgs</a>
</h2>

The set of arguments for constructing a Container resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L605">property attach</a>
</h3>

```typescript
attach?: pulumi.Input<boolean>;
```


If true attach to the container after its creation and waits the end of his execution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L609">property capabilities</a>
</h3>

```typescript
capabilities?: pulumi.Input<{ ... }>;
```


See Capabilities below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L615">property command</a>
</h3>

```typescript
command?: pulumi.Input<pulumi.Input<string>[]>;
```


The command to use to start the
container. For example, to run `/usr/bin/myprogram -f baz.conf` set the
command to be `["/usr/bin/myprogram", "-f", "baz.conf"]`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L619">property cpuSet</a>
</h3>

```typescript
cpuSet?: pulumi.Input<string>;
```


A comma-separated list or hyphen-separated range of CPUs a container can use, e.g. `0-1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L623">property cpuShares</a>
</h3>

```typescript
cpuShares?: pulumi.Input<number>;
```


CPU shares (relative weight) for the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L627">property destroyGraceSeconds</a>
</h3>

```typescript
destroyGraceSeconds?: pulumi.Input<number>;
```


If defined will attempt to stop the container before destroying. Container will be destroyed after `n` seconds or on successful stop.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L631">property devices</a>
</h3>

```typescript
devices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


See Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L635">property dns</a>
</h3>

```typescript
dns?: pulumi.Input<pulumi.Input<string>[]>;
```


Set of DNS servers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L639">property dnsOpts</a>
</h3>

```typescript
dnsOpts?: pulumi.Input<pulumi.Input<string>[]>;
```


Set of DNS options used by the DNS provider(s), see `resolv.conf` documentation for valid list of options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L643">property dnsSearches</a>
</h3>

```typescript
dnsSearches?: pulumi.Input<pulumi.Input<string>[]>;
```


Set of DNS search domains that are used when bare unqualified hostnames are used inside of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L647">property domainname</a>
</h3>

```typescript
domainname?: pulumi.Input<string>;
```


Domain name of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L655">property entrypoints</a>
</h3>

```typescript
entrypoints?: pulumi.Input<pulumi.Input<string>[]>;
```


The command to use as the
Entrypoint for the container. The Entrypoint allows you to configure a
container to run as an executable. For example, to run `/usr/bin/myprogram`
when starting a container, set the entrypoint to be
`["/usr/bin/myprogram"]`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L659">property envs</a>
</h3>

```typescript
envs?: pulumi.Input<pulumi.Input<string>[]>;
```


Environment variables to set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L663">property healthcheck</a>
</h3>

```typescript
healthcheck?: pulumi.Input<{ ... }>;
```


See Healthcheck below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L671">property hostname</a>
</h3>

```typescript
hostname?: pulumi.Input<string>;
```


Hostname of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L667">property hosts</a>
</h3>

```typescript
hosts?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Hostname to add.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L677">property image</a>
</h3>

```typescript
image: pulumi.Input<string>;
```


The ID of the image to back this container.
The easiest way to get this value is to use the `docker_image` resource
as is shown in the example above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L682">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


Key/value pairs to set as labels on the
container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L687">property links</a>
</h3>

```typescript
links?: pulumi.Input<pulumi.Input<string>[]>;
```


Set of links for link based
connectivity between containers that are running on the same host.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L692">property logDriver</a>
</h3>

```typescript
logDriver?: pulumi.Input<string>;
```


The logging driver to use for the container.
Defaults to "json-file".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L697">property logOpts</a>
</h3>

```typescript
logOpts?: pulumi.Input<{ ... }>;
```


Key/value pairs to use as options for
the logging driver.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L701">property logs</a>
</h3>

```typescript
logs?: pulumi.Input<boolean>;
```


Save the container logs (`attach` must be enabled).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L706">property maxRetryCount</a>
</h3>

```typescript
maxRetryCount?: pulumi.Input<number>;
```


The maximum amount of times to an attempt
a restart when `restart` is set to "on-failure"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L710">property memory</a>
</h3>

```typescript
memory?: pulumi.Input<number>;
```


The memory limit for the container in MBs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L715">property memorySwap</a>
</h3>

```typescript
memorySwap?: pulumi.Input<number>;
```


The total memory limit (memory + swap) for the
container in MBs. This setting may compute to `-1` after `terraform apply` if the target host doesn't support memory swap, when that is the case docker will use a soft limitation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L721">property mustRun</a>
</h3>

```typescript
mustRun?: pulumi.Input<boolean>;
```


If true, then the Docker container will be
kept running. If false, then as long as the container exists, Terraform
assumes it is successful.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L722">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L726">property networkAliases</a>
</h3>

```typescript
networkAliases?: pulumi.Input<pulumi.Input<string>[]>;
```


Network aliases of the container for user-defined networks only. *Deprecated:* use `networks_advanced` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L730">property networkMode</a>
</h3>

```typescript
networkMode?: pulumi.Input<string>;
```


Network mode of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L735">property networks</a>
</h3>

```typescript
networks?: pulumi.Input<pulumi.Input<string>[]>;
```


Id of the networks in which the
container is. *Deprecated:* use `networks_advanced` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L739">property networksAdvanced</a>
</h3>

```typescript
networksAdvanced?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


See Networks Advanced below for details. If this block has priority to the deprecated `network_alias` and `network` properties.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L743">property pidMode</a>
</h3>

```typescript
pidMode?: pulumi.Input<string>;
```


The PID (Process) Namespace mode for the container. Either `container:<name|id>` or `host`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L747">property ports</a>
</h3>

```typescript
ports?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


See Ports below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L751">property privileged</a>
</h3>

```typescript
privileged?: pulumi.Input<boolean>;
```


Run container in privileged mode.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L755">property publishAllPorts</a>
</h3>

```typescript
publishAllPorts?: pulumi.Input<boolean>;
```


Publish all ports of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L760">property restart</a>
</h3>

```typescript
restart?: pulumi.Input<string>;
```


The restart policy for the container. Must be
one of "no", "on-failure", "always", "unless-stopped".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L765">property rm</a>
</h3>

```typescript
rm?: pulumi.Input<boolean>;
```


If true, then the container will be automatically removed after his execution. Terraform
won't check this container after creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L770">property start</a>
</h3>

```typescript
start?: pulumi.Input<boolean>;
```


If true, then the Docker container will be
started after creation. If false, then the container is only created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L775">property ulimits</a>
</h3>

```typescript
ulimits?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


See Ulimits below for
details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L779">property uploads</a>
</h3>

```typescript
uploads?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


See File Upload below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L785">property user</a>
</h3>

```typescript
user?: pulumi.Input<string>;
```


User used for run the first process. Format is
`user` or `user:group` which user and group can be passed literraly or
by name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L789">property usernsMode</a>
</h3>

```typescript
usernsMode?: pulumi.Input<string>;
```


Sets the usernamespace mode for the container when usernamespace remapping option is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L793">property volumes</a>
</h3>

```typescript
volumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


See Volumes below for details.

<h2 class="pdoc-module-header" id="ContainerState">
<a class="pdoc-member-name" href="/container.ts#L372">interface ContainerState</a>
</h2>

Input properties used for looking up and filtering Container resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L376">property attach</a>
</h3>

```typescript
attach?: pulumi.Input<boolean>;
```


If true attach to the container after its creation and waits the end of his execution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L380">property bridge</a>
</h3>

```typescript
bridge?: pulumi.Input<string>;
```


The network bridge of the container as read from its NetworkSettings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L384">property capabilities</a>
</h3>

```typescript
capabilities?: pulumi.Input<{ ... }>;
```


See Capabilities below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L390">property command</a>
</h3>

```typescript
command?: pulumi.Input<pulumi.Input<string>[]>;
```


The command to use to start the
container. For example, to run `/usr/bin/myprogram -f baz.conf` set the
command to be `["/usr/bin/myprogram", "-f", "baz.conf"]`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L394">property containerLogs</a>
</h3>

```typescript
containerLogs?: pulumi.Input<string>;
```


The logs of the container if its execution is done (`attach` must be disabled).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L398">property cpuSet</a>
</h3>

```typescript
cpuSet?: pulumi.Input<string>;
```


A comma-separated list or hyphen-separated range of CPUs a container can use, e.g. `0-1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L402">property cpuShares</a>
</h3>

```typescript
cpuShares?: pulumi.Input<number>;
```


CPU shares (relative weight) for the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L406">property destroyGraceSeconds</a>
</h3>

```typescript
destroyGraceSeconds?: pulumi.Input<number>;
```


If defined will attempt to stop the container before destroying. Container will be destroyed after `n` seconds or on successful stop.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L410">property devices</a>
</h3>

```typescript
devices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


See Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L414">property dns</a>
</h3>

```typescript
dns?: pulumi.Input<pulumi.Input<string>[]>;
```


Set of DNS servers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L418">property dnsOpts</a>
</h3>

```typescript
dnsOpts?: pulumi.Input<pulumi.Input<string>[]>;
```


Set of DNS options used by the DNS provider(s), see `resolv.conf` documentation for valid list of options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L422">property dnsSearches</a>
</h3>

```typescript
dnsSearches?: pulumi.Input<pulumi.Input<string>[]>;
```


Set of DNS search domains that are used when bare unqualified hostnames are used inside of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L426">property domainname</a>
</h3>

```typescript
domainname?: pulumi.Input<string>;
```


Domain name of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L434">property entrypoints</a>
</h3>

```typescript
entrypoints?: pulumi.Input<pulumi.Input<string>[]>;
```


The command to use as the
Entrypoint for the container. The Entrypoint allows you to configure a
container to run as an executable. For example, to run `/usr/bin/myprogram`
when starting a container, set the entrypoint to be
`["/usr/bin/myprogram"]`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L438">property envs</a>
</h3>

```typescript
envs?: pulumi.Input<pulumi.Input<string>[]>;
```


Environment variables to set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L442">property exitCode</a>
</h3>

```typescript
exitCode?: pulumi.Input<number>;
```


The exit code of the container if its execution is done (`must_run` must be disabled).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L447">property gateway</a>
</h3>

```typescript
gateway?: pulumi.Input<string>;
```


*Deprecated:* Use `network_data` instead. The network gateway of the container as read from its
NetworkSettings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L451">property healthcheck</a>
</h3>

```typescript
healthcheck?: pulumi.Input<{ ... }>;
```


See Healthcheck below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L459">property hostname</a>
</h3>

```typescript
hostname?: pulumi.Input<string>;
```


Hostname of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L455">property hosts</a>
</h3>

```typescript
hosts?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Hostname to add.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L465">property image</a>
</h3>

```typescript
image?: pulumi.Input<string>;
```


The ID of the image to back this container.
The easiest way to get this value is to use the `docker_image` resource
as is shown in the example above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L469">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


*Deprecated:* Use `network_data` instead. The IP address of the container's first network it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L474">property ipPrefixLength</a>
</h3>

```typescript
ipPrefixLength?: pulumi.Input<number>;
```


*Deprecated:* Use `network_data` instead. The IP prefix length of the container as read from its
NetworkSettings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L479">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


Key/value pairs to set as labels on the
container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L484">property links</a>
</h3>

```typescript
links?: pulumi.Input<pulumi.Input<string>[]>;
```


Set of links for link based
connectivity between containers that are running on the same host.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L489">property logDriver</a>
</h3>

```typescript
logDriver?: pulumi.Input<string>;
```


The logging driver to use for the container.
Defaults to "json-file".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L494">property logOpts</a>
</h3>

```typescript
logOpts?: pulumi.Input<{ ... }>;
```


Key/value pairs to use as options for
the logging driver.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L498">property logs</a>
</h3>

```typescript
logs?: pulumi.Input<boolean>;
```


Save the container logs (`attach` must be enabled).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L503">property maxRetryCount</a>
</h3>

```typescript
maxRetryCount?: pulumi.Input<number>;
```


The maximum amount of times to an attempt
a restart when `restart` is set to "on-failure"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L507">property memory</a>
</h3>

```typescript
memory?: pulumi.Input<number>;
```


The memory limit for the container in MBs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L512">property memorySwap</a>
</h3>

```typescript
memorySwap?: pulumi.Input<number>;
```


The total memory limit (memory + swap) for the
container in MBs. This setting may compute to `-1` after `terraform apply` if the target host doesn't support memory swap, when that is the case docker will use a soft limitation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L518">property mustRun</a>
</h3>

```typescript
mustRun?: pulumi.Input<boolean>;
```


If true, then the Docker container will be
kept running. If false, then as long as the container exists, Terraform
assumes it is successful.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L519">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L523">property networkAliases</a>
</h3>

```typescript
networkAliases?: pulumi.Input<pulumi.Input<string>[]>;
```


Network aliases of the container for user-defined networks only. *Deprecated:* use `networks_advanced` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L528">property networkDatas</a>
</h3>

```typescript
networkDatas?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


(Map of a block) The IP addresses of the container on each
network. Key are the network names, values are the IP addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L532">property networkMode</a>
</h3>

```typescript
networkMode?: pulumi.Input<string>;
```


Network mode of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L537">property networks</a>
</h3>

```typescript
networks?: pulumi.Input<pulumi.Input<string>[]>;
```


Id of the networks in which the
container is. *Deprecated:* use `networks_advanced` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L541">property networksAdvanced</a>
</h3>

```typescript
networksAdvanced?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


See Networks Advanced below for details. If this block has priority to the deprecated `network_alias` and `network` properties.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L545">property pidMode</a>
</h3>

```typescript
pidMode?: pulumi.Input<string>;
```


The PID (Process) Namespace mode for the container. Either `container:<name|id>` or `host`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L549">property ports</a>
</h3>

```typescript
ports?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


See Ports below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L553">property privileged</a>
</h3>

```typescript
privileged?: pulumi.Input<boolean>;
```


Run container in privileged mode.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L557">property publishAllPorts</a>
</h3>

```typescript
publishAllPorts?: pulumi.Input<boolean>;
```


Publish all ports of the container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L562">property restart</a>
</h3>

```typescript
restart?: pulumi.Input<string>;
```


The restart policy for the container. Must be
one of "no", "on-failure", "always", "unless-stopped".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L567">property rm</a>
</h3>

```typescript
rm?: pulumi.Input<boolean>;
```


If true, then the container will be automatically removed after his execution. Terraform
won't check this container after creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L572">property start</a>
</h3>

```typescript
start?: pulumi.Input<boolean>;
```


If true, then the Docker container will be
started after creation. If false, then the container is only created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L577">property ulimits</a>
</h3>

```typescript
ulimits?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


See Ulimits below for
details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L581">property uploads</a>
</h3>

```typescript
uploads?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


See File Upload below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L587">property user</a>
</h3>

```typescript
user?: pulumi.Input<string>;
```


User used for run the first process. Format is
`user` or `user:group` which user and group can be passed literraly or
by name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L591">property usernsMode</a>
</h3>

```typescript
usernsMode?: pulumi.Input<string>;
```


Sets the usernamespace mode for the container when usernamespace remapping option is enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/container.ts#L595">property volumes</a>
</h3>

```typescript
volumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


See Volumes below for details.

<h2 class="pdoc-module-header" id="DockerBuild">
<a class="pdoc-member-name" href="/docker.ts#L45">interface DockerBuild</a>
</h2>

DockerBuild may be used to specify detailed instructions about how to build a container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/docker.ts#L64">property args</a>
</h3>

```typescript
args?: { ... };
```


An optional map of named build-time argument variables to set during the Docker build.  This
flag allows you to pass built-time variables that can be accessed like environment variables
inside the `RUN` instruction.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/docker.ts#L73">property cacheFrom</a>
</h3>

```typescript
cacheFrom?: boolean | CacheFrom;
```


An optional CacheFrom object with information about the build stages to use for the Docker
build cache. This parameter maps to the --cache-from argument to the Docker CLI. If this
parameter is `true`, only the final image will be pulled and passed to --cache-from; if it is
a CacheFrom object, the stages named therein will also be pulled and passed to --cache-from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/docker.ts#L53">property context</a>
</h3>

```typescript
context?: string;
```


context is a path to a directory to use for the Docker build context, usually the directory
in which the Dockerfile resides (although dockerfile may be used to choose a custom location
independent of this choice). If not specified, the context defaults to the current working
directory; if a relative path is used, it is relative to the current working directory that
Pulumi is evaluating.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/docker.ts#L58">property dockerfile</a>
</h3>

```typescript
dockerfile?: string;
```


dockerfile may be used to override the default Dockerfile name and/or location.  By default,
it is assumed to be a file named Dockerfile in the root of the build context.

<h2 class="pdoc-module-header" id="ImageArgs">
<a class="pdoc-member-name" href="/image.ts#L22">interface ImageArgs</a>
</h2>

Arguments for constructing an Image resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/image.ts#L35">property build</a>
</h3>

```typescript
build: pulumi.Input<string | docker.DockerBuild>;
```


The Docker build context, as a folder path or a detailed DockerBuild object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/image.ts#L31">property imageName</a>
</h3>

```typescript
imageName: pulumi.Input<string>;
```


The qualified image name that will be pushed to the remote registry.  Must be a supported
image name for the target registry user.  This name can include a tag at the end.  If
provided all pushed image resources will contain that tag as well.

Either [imageName] or [localImageName] can have a tag.  However, if both have a tag, then
those tags must match.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/image.ts#L44">property localImageName</a>
</h3>

```typescript
localImageName?: pulumi.Input<string>;
```


The docker image name to build locally before tagging with imageName.  If not provided, it
will be given the value of to [imageName].  This name can include a tag at the end.  If
provided all pushed image resources will contain that tag as well.

Either [imageName] or [localImageName] can have a tag.  However, if both have a tag, then
those tags must match.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/image.ts#L48">property registry</a>
</h3>

```typescript
registry?: pulumi.Input<ImageRegistry>;
```


Credentials for the docker registry to push to.

<h2 class="pdoc-module-header" id="ImageRegistry">
<a class="pdoc-member-name" href="/image.ts#L51">interface ImageRegistry</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/image.ts#L67">property password</a>
</h3>

```typescript
password: pulumi.Input<string>;
```


Password for login to the target Docker registry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/image.ts#L59">property server</a>
</h3>

```typescript
server: pulumi.Input<string>;
```


Docker registry server URL to push to.  Some common values include:
DockerHub: `docker.io` or `https://index.docker.io/v1`
Azure Container Registry: `<name>.azurecr.io`
AWS Elastic Container Registry: `<account>.dkr.ecr.us-east-2.amazonaws.com`
Google Container Registry: `<name>.gcr.io`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/image.ts#L63">property username</a>
</h3>

```typescript
username: pulumi.Input<string>;
```


Username for login to the target Docker registry.

<h2 class="pdoc-module-header" id="NetworkArgs">
<a class="pdoc-member-name" href="/network.ts#L186">interface NetworkArgs</a>
</h2>

The set of arguments for constructing a Network resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L191">property attachable</a>
</h3>

```typescript
attachable?: pulumi.Input<boolean>;
```


Enable manual container attachment to the network.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L196">property checkDuplicate</a>
</h3>

```typescript
checkDuplicate?: pulumi.Input<boolean>;
```


Requests daemon to check for networks
with same name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L201">property driver</a>
</h3>

```typescript
driver?: pulumi.Input<string>;
```


Name of the network driver to use. Defaults to
`bridge` driver.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L206">property ingress</a>
</h3>

```typescript
ingress?: pulumi.Input<boolean>;
```


Create swarm routing-mesh network.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L211">property internal</a>
</h3>

```typescript
internal?: pulumi.Input<boolean>;
```


Restrict external access to the network.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L216">property ipamConfigs</a>
</h3>

```typescript
ipamConfigs?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


See IPAM config below for
details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L221">property ipamDriver</a>
</h3>

```typescript
ipamDriver?: pulumi.Input<string>;
```


Driver used by the custom IP scheme of the
network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L226">property ipv6</a>
</h3>

```typescript
ipv6?: pulumi.Input<boolean>;
```


Enable IPv6 networking.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L230">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


User-defined key/value metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L234">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Docker network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L239">property options</a>
</h3>

```typescript
options?: pulumi.Input<{ ... }>;
```


Network specific options to be used by
the drivers.

<h2 class="pdoc-module-header" id="NetworkState">
<a class="pdoc-member-name" href="/network.ts#L126">interface NetworkState</a>
</h2>

Input properties used for looking up and filtering Network resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L131">property attachable</a>
</h3>

```typescript
attachable?: pulumi.Input<boolean>;
```


Enable manual container attachment to the network.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L136">property checkDuplicate</a>
</h3>

```typescript
checkDuplicate?: pulumi.Input<boolean>;
```


Requests daemon to check for networks
with same name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L141">property driver</a>
</h3>

```typescript
driver?: pulumi.Input<string>;
```


Name of the network driver to use. Defaults to
`bridge` driver.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L146">property ingress</a>
</h3>

```typescript
ingress?: pulumi.Input<boolean>;
```


Create swarm routing-mesh network.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L151">property internal</a>
</h3>

```typescript
internal?: pulumi.Input<boolean>;
```


Restrict external access to the network.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L156">property ipamConfigs</a>
</h3>

```typescript
ipamConfigs?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


See IPAM config below for
details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L161">property ipamDriver</a>
</h3>

```typescript
ipamDriver?: pulumi.Input<string>;
```


Driver used by the custom IP scheme of the
network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L166">property ipv6</a>
</h3>

```typescript
ipv6?: pulumi.Input<boolean>;
```


Enable IPv6 networking.
Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L170">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


User-defined key/value metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L174">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Docker network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L179">property options</a>
</h3>

```typescript
options?: pulumi.Input<{ ... }>;
```


Network specific options to be used by
the drivers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/network.ts#L180">property scope</a>
</h3>

```typescript
scope?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="ProviderArgs">
<a class="pdoc-member-name" href="/provider.ts#L36">interface ProviderArgs</a>
</h2>

The set of arguments for constructing a Provider resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L40">property caMaterial</a>
</h3>

```typescript
caMaterial?: pulumi.Input<string>;
```


PEM-encoded content of Docker host CA certificate

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L44">property certMaterial</a>
</h3>

```typescript
certMaterial?: pulumi.Input<string>;
```


PEM-encoded content of Docker client certificate

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L48">property certPath</a>
</h3>

```typescript
certPath?: pulumi.Input<string>;
```


Path to directory with Docker TLS config

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L52">property host</a>
</h3>

```typescript
host?: pulumi.Input<string>;
```


The Docker daemon address

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L56">property keyMaterial</a>
</h3>

```typescript
keyMaterial?: pulumi.Input<string>;
```


PEM-encoded content of Docker client private key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L57">property registryAuth</a>
</h3>

```typescript
registryAuth?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h2 class="pdoc-module-header" id="Registry">
<a class="pdoc-member-name" href="/docker.ts#L23">interface Registry</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/docker.ts#L26">property password</a>
</h3>

```typescript
password: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/docker.ts#L24">property registry</a>
</h3>

```typescript
registry: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/docker.ts#L25">property username</a>
</h3>

```typescript
username: string;
```

<h2 class="pdoc-module-header" id="RemoteImageArgs">
<a class="pdoc-member-name" href="/remoteImage.ts#L113">interface RemoteImageArgs</a>
</h2>

The set of arguments for constructing a RemoteImage resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/remoteImage.ts#L119">property keepLocally</a>
</h3>

```typescript
keepLocally?: pulumi.Input<boolean>;
```


If true, then the Docker image won't be
deleted on destroy operation. If this is false, it will delete the image from
the docker local storage on destroy operation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/remoteImage.ts#L123">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The name of the Docker image, including any tags or SHA256 repo digests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/remoteImage.ts#L127">property pullTrigger</a>
</h3>

```typescript
pullTrigger?: pulumi.Input<string>;
```


**Deprecated**, use `pull_triggers` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/remoteImage.ts#L134">property pullTriggers</a>
</h3>

```typescript
pullTriggers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of values which cause an
image pull when changed. This is used to store the image digest from the
registry when using the `docker_registry_image` [data source](https://www.terraform.io/docs/providers/docker/d/registry_image.html)
to trigger an image update.

<h2 class="pdoc-module-header" id="RemoteImageState">
<a class="pdoc-member-name" href="/remoteImage.ts#L85">interface RemoteImageState</a>
</h2>

Input properties used for looking up and filtering RemoteImage resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/remoteImage.ts#L91">property keepLocally</a>
</h3>

```typescript
keepLocally?: pulumi.Input<boolean>;
```


If true, then the Docker image won't be
deleted on destroy operation. If this is false, it will delete the image from
the docker local storage on destroy operation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/remoteImage.ts#L92">property latest</a>
</h3>

```typescript
latest?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/remoteImage.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Docker image, including any tags or SHA256 repo digests.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/remoteImage.ts#L100">property pullTrigger</a>
</h3>

```typescript
pullTrigger?: pulumi.Input<string>;
```


**Deprecated**, use `pull_triggers` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/remoteImage.ts#L107">property pullTriggers</a>
</h3>

```typescript
pullTriggers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of values which cause an
image pull when changed. This is used to store the image digest from the
registry when using the `docker_registry_image` [data source](https://www.terraform.io/docs/providers/docker/d/registry_image.html)
to trigger an image update.

<h2 class="pdoc-module-header" id="VolumeArgs">
<a class="pdoc-member-name" href="/volume.ts#L100">interface VolumeArgs</a>
</h2>

The set of arguments for constructing a Volume resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/volume.ts#L104">property driver</a>
</h3>

```typescript
driver?: pulumi.Input<string>;
```


Driver type for the volume (defaults to local).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/volume.ts#L108">property driverOpts</a>
</h3>

```typescript
driverOpts?: pulumi.Input<{ ... }>;
```


Options specific to the driver.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/volume.ts#L112">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


User-defined key/value metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/volume.ts#L117">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Docker volume (generated if not
provided).

<h2 class="pdoc-module-header" id="VolumeState">
<a class="pdoc-member-name" href="/volume.ts#L76">interface VolumeState</a>
</h2>

Input properties used for looking up and filtering Volume resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/volume.ts#L80">property driver</a>
</h3>

```typescript
driver?: pulumi.Input<string>;
```


Driver type for the volume (defaults to local).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/volume.ts#L84">property driverOpts</a>
</h3>

```typescript
driverOpts?: pulumi.Input<{ ... }>;
```


Options specific to the driver.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/volume.ts#L88">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


User-defined key/value metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/volume.ts#L89">property mountpoint</a>
</h3>

```typescript
mountpoint?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/volume.ts#L94">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Docker volume (generated if not
provided).

