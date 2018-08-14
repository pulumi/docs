---
title: Module objectstorage
---

<a href="../index.html">@pulumi/openstack</a> &gt; objectstorage

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Container">class Container</a>
* <a href="#ContainerObject">class ContainerObject</a>
* <a href="#ContainerArgs">interface ContainerArgs</a>
* <a href="#ContainerObjectArgs">interface ContainerObjectArgs</a>
* <a href="#ContainerObjectState">interface ContainerObjectState</a>
* <a href="#ContainerState">interface ContainerState</a>

<a href="/objectstorage/container.ts">objectstorage/container.ts</a> <a href="/objectstorage/containerObject.ts">objectstorage/containerObject.ts</a> 


<h2 class="pdoc-module-header" id="Container">
<a class="pdoc-member-name" href="/objectstorage/container.ts#L9">class Container</a>
</h2>

Manages a V1 container resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L68">constructor</a>
</h3>

```typescript
new Container(name: string, args?: ContainerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Container resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="/objectstorage/container.ts#L28">property containerRead</a>
</h3>

```typescript
public containerRead: pulumi.Output<string | undefined>;
```


Sets an access control list (ACL) that grants
read access. This header can contain a comma-delimited list of users that
can read the container (allows the GET method for all objects in the
container). Changing this updates the access control list read access.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L33">property containerSyncKey</a>
</h3>

```typescript
public containerSyncKey: pulumi.Output<string | undefined>;
```


The secret key for container synchronization.
Changing this updates container synchronization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L38">property containerSyncTo</a>
</h3>

```typescript
public containerSyncTo: pulumi.Output<string | undefined>;
```


The destination for container synchronization.
Changing this updates container synchronization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L43">property containerWrite</a>
</h3>

```typescript
public containerWrite: pulumi.Output<string | undefined>;
```


Sets an ACL that grants write access.
Changing this updates the access control list write access.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L48">property contentType</a>
</h3>

```typescript
public contentType: pulumi.Output<string | undefined>;
```


The MIME type for the container. Changing this
updates the MIME type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L52">property forceDestroy</a>
</h3>

```typescript
public forceDestroy: pulumi.Output<boolean | undefined>;
```


A boolean that indicates all objects should be deleted from the container so that the container can be destroyed without error. These objects are not recoverable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L57">property metadata</a>
</h3>

```typescript
public metadata: pulumi.Output<{ ... } | undefined>;
```


Custom key/value pairs to associate with the container.
Changing this updates the existing container metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L62">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the container. Changing this creates a
new container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L68">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to create the container. If
omitted, the `region` argument of the provider is used. Changing this
creates a new container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ContainerObject">
<a class="pdoc-member-name" href="/objectstorage/containerObject.ts#L9">class ContainerObject</a>
</h2>

Manages a V1 container object resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L128">constructor</a>
</h3>

```typescript
new ContainerObject(name: string, args: ContainerObjectArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ContainerObject resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ContainerObjectState): ContainerObject
```


Get an existing ContainerObject resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L30">property containerName</a>
</h3>

```typescript
public containerName: pulumi.Output<string>;
```


A unique (within an account) name for the container.
The container name must be from 1 to 256 characters long and can start
with any character and contain any pattern. Character set must be UTF-8.
The container name cannot contain a slash (/) character because this
character delimits the container and object name. For example, the path
/v1/account/www/pages specifies the www container, not the www/pages container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L35">property content</a>
</h3>

```typescript
public content: pulumi.Output<string | undefined>;
```


A string representing the content of the object. Conflicts with
`source` and `copy_from`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L41">property contentDisposition</a>
</h3>

```typescript
public contentDisposition: pulumi.Output<string>;
```


A string which specifies the override behavior for
the browser. For example, this header might specify that the browser use a download
program to save this file rather than show the file, which is the default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L46">property contentEncoding</a>
</h3>

```typescript
public contentEncoding: pulumi.Output<string>;
```


A string representing the value of the Content-Encoding
metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L51">property contentLength</a>
</h3>

```typescript
public contentLength: pulumi.Output<number>;
```


If the operation succeeds, this value is zero (0) or the
length of informational or error text in the response body.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L55">property contentType</a>
</h3>

```typescript
public contentType: pulumi.Output<string>;
```


A string which sets the MIME type for the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L63">property copyFrom</a>
</h3>

```typescript
public copyFrom: pulumi.Output<string | undefined>;
```


A string representing the name of an object
used to create the new object by copying the `copy_from` object. The value is in form
{container}/{object}. You must UTF-8-encode and then URL-encode the names of the
container and object before you include them in the header. Conflicts with `source` and
`content`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L69">property date</a>
</h3>

```typescript
public date: pulumi.Output<string>;
```


The date and time the system responded to the request, using the preferred
format of RFC 7231 as shown in this example Thu, 16 Jun 2016 15:10:38 GMT. The
time is always in UTC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L75">property deleteAfter</a>
</h3>

```typescript
public deleteAfter: pulumi.Output<number | undefined>;
```


An integer representing the number of seconds after which the
system removes the object. Internally, the Object Storage system stores this value in
the X-Delete-At metadata item.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L80">property deleteAt</a>
</h3>

```typescript
public deleteAt: pulumi.Output<string>;
```


An string representing the date when the system removes the object.
For example, "2015-08-26" is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L86">property detectContentType</a>
</h3>

```typescript
public detectContentType: pulumi.Output<boolean | undefined>;
```


If set to true, Object Storage guesses the content
type based on the file extension and ignores the value sent in the Content-Type
header, if present.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L90">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


Used to trigger updates. The only meaningful value is ${md5(file("path/to/file"))}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L99">property lastModified</a>
</h3>

```typescript
public lastModified: pulumi.Output<string>;
```


The date and time when the object was last modified. The date and time
stamp format is ISO 8601:
CCYY-MM-DDThh:mm:ss±hh:mm
For example, 2015-08-27T09:49:58-05:00.
The ±hh:mm value, if included, is the time zone as an offset from UTC. In the previous
example, the offset value is -05:00.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L100">property metadata</a>
</h3>

```typescript
public metadata: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L104">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L112">property objectManifest</a>
</h3>

```typescript
public objectManifest: pulumi.Output<string>;
```


A string set to specify that this is a dynamic large
object manifest object. The value is the container and object name prefix of the
segment objects in the form container/prefix. You must UTF-8-encode and then
URL-encode the names of the container and prefix before you include them in this
header.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L118">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to create the container. If
omitted, the `region` argument of the provider is used. Changing this
creates a new container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L123">property source</a>
</h3>

```typescript
public source: pulumi.Output<string | undefined>;
```


A string representing the local path of a file which will be used
as the object's content. Conflicts with `source` and `copy_from`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L128">property transId</a>
</h3>

```typescript
public transId: pulumi.Output<string>;
```


A unique transaction ID for this request. Your service provider might
need this value if you report a problem.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ContainerArgs">
<a class="pdoc-member-name" href="/objectstorage/container.ts#L163">interface ContainerArgs</a>
</h2>

The set of arguments for constructing a Container resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L170">property containerRead</a>
</h3>

```typescript
containerRead?: pulumi.Input<string>;
```


Sets an access control list (ACL) that grants
read access. This header can contain a comma-delimited list of users that
can read the container (allows the GET method for all objects in the
container). Changing this updates the access control list read access.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L175">property containerSyncKey</a>
</h3>

```typescript
containerSyncKey?: pulumi.Input<string>;
```


The secret key for container synchronization.
Changing this updates container synchronization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L180">property containerSyncTo</a>
</h3>

```typescript
containerSyncTo?: pulumi.Input<string>;
```


The destination for container synchronization.
Changing this updates container synchronization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L185">property containerWrite</a>
</h3>

```typescript
containerWrite?: pulumi.Input<string>;
```


Sets an ACL that grants write access.
Changing this updates the access control list write access.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L190">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```


The MIME type for the container. Changing this
updates the MIME type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L194">property forceDestroy</a>
</h3>

```typescript
forceDestroy?: pulumi.Input<boolean>;
```


A boolean that indicates all objects should be deleted from the container so that the container can be destroyed without error. These objects are not recoverable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L199">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Custom key/value pairs to associate with the container.
Changing this updates the existing container metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L204">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the container. Changing this creates a
new container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L210">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the container. If
omitted, the `region` argument of the provider is used. Changing this
creates a new container.

<h2 class="pdoc-module-header" id="ContainerObjectArgs">
<a class="pdoc-member-name" href="/objectstorage/containerObject.ts#L306">interface ContainerObjectArgs</a>
</h2>

The set of arguments for constructing a ContainerObject resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L315">property containerName</a>
</h3>

```typescript
containerName: pulumi.Input<string>;
```


A unique (within an account) name for the container.
The container name must be from 1 to 256 characters long and can start
with any character and contain any pattern. Character set must be UTF-8.
The container name cannot contain a slash (/) character because this
character delimits the container and object name. For example, the path
/v1/account/www/pages specifies the www container, not the www/pages container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L320">property content</a>
</h3>

```typescript
content?: pulumi.Input<string>;
```


A string representing the content of the object. Conflicts with
`source` and `copy_from`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L326">property contentDisposition</a>
</h3>

```typescript
contentDisposition?: pulumi.Input<string>;
```


A string which specifies the override behavior for
the browser. For example, this header might specify that the browser use a download
program to save this file rather than show the file, which is the default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L331">property contentEncoding</a>
</h3>

```typescript
contentEncoding?: pulumi.Input<string>;
```


A string representing the value of the Content-Encoding
metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L335">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```


A string which sets the MIME type for the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L343">property copyFrom</a>
</h3>

```typescript
copyFrom?: pulumi.Input<string>;
```


A string representing the name of an object
used to create the new object by copying the `copy_from` object. The value is in form
{container}/{object}. You must UTF-8-encode and then URL-encode the names of the
container and object before you include them in the header. Conflicts with `source` and
`content`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L349">property deleteAfter</a>
</h3>

```typescript
deleteAfter?: pulumi.Input<number>;
```


An integer representing the number of seconds after which the
system removes the object. Internally, the Object Storage system stores this value in
the X-Delete-At metadata item.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L354">property deleteAt</a>
</h3>

```typescript
deleteAt?: pulumi.Input<string>;
```


An string representing the date when the system removes the object.
For example, "2015-08-26" is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L360">property detectContentType</a>
</h3>

```typescript
detectContentType?: pulumi.Input<boolean>;
```


If set to true, Object Storage guesses the content
type based on the file extension and ignores the value sent in the Content-Type
header, if present.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L364">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


Used to trigger updates. The only meaningful value is ${md5(file("path/to/file"))}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L365">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L369">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L377">property objectManifest</a>
</h3>

```typescript
objectManifest?: pulumi.Input<string>;
```


A string set to specify that this is a dynamic large
object manifest object. The value is the container and object name prefix of the
segment objects in the form container/prefix. You must UTF-8-encode and then
URL-encode the names of the container and prefix before you include them in this
header.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L383">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the container. If
omitted, the `region` argument of the provider is used. Changing this
creates a new container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L388">property source</a>
</h3>

```typescript
source?: pulumi.Input<string>;
```


A string representing the local path of a file which will be used
as the object's content. Conflicts with `source` and `copy_from`.

<h2 class="pdoc-module-header" id="ContainerObjectState">
<a class="pdoc-member-name" href="/objectstorage/containerObject.ts#L193">interface ContainerObjectState</a>
</h2>

Input properties used for looking up and filtering ContainerObject resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L202">property containerName</a>
</h3>

```typescript
containerName?: pulumi.Input<string>;
```


A unique (within an account) name for the container.
The container name must be from 1 to 256 characters long and can start
with any character and contain any pattern. Character set must be UTF-8.
The container name cannot contain a slash (/) character because this
character delimits the container and object name. For example, the path
/v1/account/www/pages specifies the www container, not the www/pages container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L207">property content</a>
</h3>

```typescript
content?: pulumi.Input<string>;
```


A string representing the content of the object. Conflicts with
`source` and `copy_from`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L213">property contentDisposition</a>
</h3>

```typescript
contentDisposition?: pulumi.Input<string>;
```


A string which specifies the override behavior for
the browser. For example, this header might specify that the browser use a download
program to save this file rather than show the file, which is the default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L218">property contentEncoding</a>
</h3>

```typescript
contentEncoding?: pulumi.Input<string>;
```


A string representing the value of the Content-Encoding
metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L223">property contentLength</a>
</h3>

```typescript
contentLength?: pulumi.Input<number>;
```


If the operation succeeds, this value is zero (0) or the
length of informational or error text in the response body.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L227">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```


A string which sets the MIME type for the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L235">property copyFrom</a>
</h3>

```typescript
copyFrom?: pulumi.Input<string>;
```


A string representing the name of an object
used to create the new object by copying the `copy_from` object. The value is in form
{container}/{object}. You must UTF-8-encode and then URL-encode the names of the
container and object before you include them in the header. Conflicts with `source` and
`content`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L241">property date</a>
</h3>

```typescript
date?: pulumi.Input<string>;
```


The date and time the system responded to the request, using the preferred
format of RFC 7231 as shown in this example Thu, 16 Jun 2016 15:10:38 GMT. The
time is always in UTC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L247">property deleteAfter</a>
</h3>

```typescript
deleteAfter?: pulumi.Input<number>;
```


An integer representing the number of seconds after which the
system removes the object. Internally, the Object Storage system stores this value in
the X-Delete-At metadata item.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L252">property deleteAt</a>
</h3>

```typescript
deleteAt?: pulumi.Input<string>;
```


An string representing the date when the system removes the object.
For example, "2015-08-26" is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L258">property detectContentType</a>
</h3>

```typescript
detectContentType?: pulumi.Input<boolean>;
```


If set to true, Object Storage guesses the content
type based on the file extension and ignores the value sent in the Content-Type
header, if present.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L262">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


Used to trigger updates. The only meaningful value is ${md5(file("path/to/file"))}.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L271">property lastModified</a>
</h3>

```typescript
lastModified?: pulumi.Input<string>;
```


The date and time when the object was last modified. The date and time
stamp format is ISO 8601:
CCYY-MM-DDThh:mm:ss±hh:mm
For example, 2015-08-27T09:49:58-05:00.
The ±hh:mm value, if included, is the time zone as an offset from UTC. In the previous
example, the offset value is -05:00.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L272">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L276">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L284">property objectManifest</a>
</h3>

```typescript
objectManifest?: pulumi.Input<string>;
```


A string set to specify that this is a dynamic large
object manifest object. The value is the container and object name prefix of the
segment objects in the form container/prefix. You must UTF-8-encode and then
URL-encode the names of the container and prefix before you include them in this
header.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L290">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the container. If
omitted, the `region` argument of the provider is used. Changing this
creates a new container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L295">property source</a>
</h3>

```typescript
source?: pulumi.Input<string>;
```


A string representing the local path of a file which will be used
as the object's content. Conflicts with `source` and `copy_from`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/containerObject.ts#L300">property transId</a>
</h3>

```typescript
transId?: pulumi.Input<string>;
```


A unique transaction ID for this request. Your service provider might
need this value if you report a problem.

<h2 class="pdoc-module-header" id="ContainerState">
<a class="pdoc-member-name" href="/objectstorage/container.ts#L110">interface ContainerState</a>
</h2>

Input properties used for looking up and filtering Container resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L117">property containerRead</a>
</h3>

```typescript
containerRead?: pulumi.Input<string>;
```


Sets an access control list (ACL) that grants
read access. This header can contain a comma-delimited list of users that
can read the container (allows the GET method for all objects in the
container). Changing this updates the access control list read access.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L122">property containerSyncKey</a>
</h3>

```typescript
containerSyncKey?: pulumi.Input<string>;
```


The secret key for container synchronization.
Changing this updates container synchronization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L127">property containerSyncTo</a>
</h3>

```typescript
containerSyncTo?: pulumi.Input<string>;
```


The destination for container synchronization.
Changing this updates container synchronization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L132">property containerWrite</a>
</h3>

```typescript
containerWrite?: pulumi.Input<string>;
```


Sets an ACL that grants write access.
Changing this updates the access control list write access.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L137">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```


The MIME type for the container. Changing this
updates the MIME type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L141">property forceDestroy</a>
</h3>

```typescript
forceDestroy?: pulumi.Input<boolean>;
```


A boolean that indicates all objects should be deleted from the container so that the container can be destroyed without error. These objects are not recoverable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L146">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Custom key/value pairs to associate with the container.
Changing this updates the existing container metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L151">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the container. Changing this creates a
new container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/objectstorage/container.ts#L157">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the container. If
omitted, the `region` argument of the provider is used. Changing this
creates a new container.

