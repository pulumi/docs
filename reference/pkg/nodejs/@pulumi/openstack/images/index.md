---
title: Module images
---

<a href="../index.html">@pulumi/openstack</a> &gt; images

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Image">class Image</a>
* <a href="#getImage">function getImage</a>
* <a href="#GetImageArgs">interface GetImageArgs</a>
* <a href="#GetImageResult">interface GetImageResult</a>
* <a href="#ImageArgs">interface ImageArgs</a>
* <a href="#ImageState">interface ImageState</a>

<a href="/images/getImage.ts">images/getImage.ts</a> <a href="/images/image.ts">images/image.ts</a> 


<h2 class="pdoc-module-header" id="Image">
<a class="pdoc-member-name" href="/images/image.ts#L10">class Image</a>
</h2>

Manages a V2 Image resource within OpenStack Glance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L141">constructor</a>
</h3>

```typescript
new Image(name: string, args: ImageArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Image resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ImageState): Image
```


Get an existing Image resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/images/image.ts#L26">property checksum</a>
</h3>

```typescript
public checksum: pulumi.Output<string>;
```


The checksum of the data associated with the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L31">property containerFormat</a>
</h3>

```typescript
public containerFormat: pulumi.Output<string>;
```


The container format. Must be one of
"ami", "ari", "aki", "bare", "ovf".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L35">property createdAt</a>
</h3>

```typescript
public createdAt: pulumi.Output<string>;
```


The date the image was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L40">property diskFormat</a>
</h3>

```typescript
public diskFormat: pulumi.Output<string>;
```


The disk format. Must be one of
"ami", "ari", "aki", "vhd", "vmdk", "raw", "qcow2", "vdi", "iso".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L46">property file</a>
</h3>

```typescript
public file: pulumi.Output<string>;
```


the trailing path after the glance
endpoint that represent the location of the image
or the path to retrieve it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L52">property imageCachePath</a>
</h3>

```typescript
public imageCachePath: pulumi.Output<string | undefined>;
```


This is the directory where the images will
be downloaded. Images will be stored with a filename corresponding to
the url's md5 hash. Defaults to "$HOME/.terraform/image_cache"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L60">property imageSourceUrl</a>
</h3>

```typescript
public imageSourceUrl: pulumi.Output<string | undefined>;
```


This is the url of the raw image that will
be downloaded in the `image_cache_path` before being uploaded to Glance.
Glance is able to download image from internet but the `gophercloud` library
does not yet provide a way to do so.
Conflicts with `local_file_path`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L65">property localFilePath</a>
</h3>

```typescript
public localFilePath: pulumi.Output<string | undefined>;
```


This is the filepath of the raw image file
that will be uploaded to Glance. Conflicts with `image_source_url`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L71">property metadata</a>
</h3>

```typescript
public metadata: pulumi.Output<{ ... }>;
```


The metadata associated with the image.
Image metadata allow for meaningfully define the image properties
and tags. See http://docs.openstack.org/developer/glance/metadefs-concepts.html.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L76">property minDiskGb</a>
</h3>

```typescript
public minDiskGb: pulumi.Output<number | undefined>;
```


Amount of disk space (in GB) required to boot image.
Defaults to 0.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L81">property minRamMb</a>
</h3>

```typescript
public minRamMb: pulumi.Output<number | undefined>;
```


Amount of ram (in MB) required to boot image.
Defauts to 0.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L85">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L89">property owner</a>
</h3>

```typescript
public owner: pulumi.Output<string>;
```


The id of the openstack user who owns the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L95">property properties</a>
</h3>

```typescript
public properties: pulumi.Output<{ ... }>;
```


A map of key/value pairs to set freeform
information about an image. See the "Notes" section for further
information about properties.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L100">property protected</a>
</h3>

```typescript
public protected: pulumi.Output<boolean | undefined>;
```


If true, image will not be deletable.
Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L107">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Glance client.
A Glance client is needed to create an Image that can be used with
a compute instance. If omitted, the `region` argument of the provider
is used. Changing this creates a new Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L112">property schema</a>
</h3>

```typescript
public schema: pulumi.Output<string>;
```


The path to the JSON-schema that represent
the image or image

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L116">property sizeBytes</a>
</h3>

```typescript
public sizeBytes: pulumi.Output<number>;
```


The size in bytes of the data associated with the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L121">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```


The status of the image. It can be "queued", "active"
or "saving".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L126">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<string[] | undefined>;
```


The tags of the image. It must be a list of strings.
At this time, it is not possible to delete all tags of an image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L130">property updateAt</a>
</h3>

```typescript
public updateAt: pulumi.Output<string>;
```


The date the image was last updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L135">property verifyChecksum</a>
</h3>

```typescript
public verifyChecksum: pulumi.Output<boolean | undefined>;
```


If false, the checksum will not be verified
once the image is finished uploading. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L141">property visibility</a>
</h3>

```typescript
public visibility: pulumi.Output<string | undefined>;
```


The visibility of the image. Must be one of
"public", "private", "community", or "shared". The ability to set the
visibility depends upon the configuration of the OpenStack cloud.

<h2 class="pdoc-module-header" id="getImage">
<a class="pdoc-member-name" href="/images/getImage.ts#L10">function getImage</a>
</h2>

```typescript
getImage(args?: GetImageArgs, opts?: pulumi.InvokeOptions): Promise<GetImageResult>
```


Use this data source to get the ID of an available OpenStack image.

<h2 class="pdoc-module-header" id="GetImageArgs">
<a class="pdoc-member-name" href="/images/getImage.ts#L31">interface GetImageArgs</a>
</h2>

A collection of arguments for invoking getImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L36">property memberStatus</a>
</h3>

```typescript
memberStatus?: string;
```


The status of the image. Must be one of
"accepted", "pending", "rejected", or "all".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L41">property mostRecent</a>
</h3>

```typescript
mostRecent?: boolean;
```


If more than one result is returned, use the most
recent image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L45">property name</a>
</h3>

```typescript
name?: string;
```


The name of the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L49">property owner</a>
</h3>

```typescript
owner?: string;
```


The owner (UUID) of the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L54">property properties</a>
</h3>

```typescript
properties?: { ... };
```


a map of key/value pairs to match an image with.
All specified properties must be matched.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L61">property region</a>
</h3>

```typescript
region?: string;
```


The region in which to obtain the V2 Glance client.
A Glance client is needed to create an Image that can be used with
a compute instance. If omitted, the `region` argument of the provider
is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L65">property sizeMax</a>
</h3>

```typescript
sizeMax?: number;
```


The maximum size (in bytes) of the image to return.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L69">property sizeMin</a>
</h3>

```typescript
sizeMin?: number;
```


The minimum size (in bytes) of the image to return.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L73">property sortDirection</a>
</h3>

```typescript
sortDirection?: string;
```


Order the results in either `asc` or `desc`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L77">property sortKey</a>
</h3>

```typescript
sortKey?: string;
```


Sort images based on a certain key. Defaults to `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L81">property tag</a>
</h3>

```typescript
tag?: string;
```


Search for images with a specific tag.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L86">property visibility</a>
</h3>

```typescript
visibility?: string;
```


The visibility of the image. Must be one of
"public", "private", "community", or "shared". Defaults to "private".

<h2 class="pdoc-module-header" id="GetImageResult">
<a class="pdoc-member-name" href="/images/getImage.ts#L92">interface GetImageResult</a>
</h2>

A collection of values returned by getImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L96">property checksum</a>
</h3>

```typescript
checksum: string;
```


The checksum of the data associated with the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L97">property containerFormat</a>
</h3>

```typescript
containerFormat: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L98">property diskFormat</a>
</h3>

```typescript
diskFormat: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L103">property file</a>
</h3>

```typescript
file: string;
```


the trailing path after the glance endpoint that represent the
location of the image or the path to retrieve it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L136">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L109">property metadata</a>
</h3>

```typescript
metadata: { ... };
```


The metadata associated with the image.
Image metadata allow for meaningfully define the image properties
and tags. See http://docs.openstack.org/developer/glance/metadefs-concepts.html.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L113">property minDiskGb</a>
</h3>

```typescript
minDiskGb: number;
```


The minimum amount of disk space required to use the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L117">property minRamMb</a>
</h3>

```typescript
minRamMb: number;
```


The minimum amount of ram required to use the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L121">property protected</a>
</h3>

```typescript
protected: boolean;
```


Whether or not the image is protected.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L122">property region</a>
</h3>

```typescript
region: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L127">property schema</a>
</h3>

```typescript
schema: string;
```


The path to the JSON-schema that represent
the image or image

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L131">property sizeBytes</a>
</h3>

```typescript
sizeBytes: number;
```


The size of the image (in bytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/getImage.ts#L132">property updatedAt</a>
</h3>

```typescript
updatedAt: string;
```

<h2 class="pdoc-module-header" id="ImageArgs">
<a class="pdoc-member-name" href="/images/image.ts#L342">interface ImageArgs</a>
</h2>

The set of arguments for constructing a Image resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L347">property containerFormat</a>
</h3>

```typescript
containerFormat: pulumi.Input<string>;
```


The container format. Must be one of
"ami", "ari", "aki", "bare", "ovf".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L352">property diskFormat</a>
</h3>

```typescript
diskFormat: pulumi.Input<string>;
```


The disk format. Must be one of
"ami", "ari", "aki", "vhd", "vmdk", "raw", "qcow2", "vdi", "iso".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L358">property imageCachePath</a>
</h3>

```typescript
imageCachePath?: pulumi.Input<string>;
```


This is the directory where the images will
be downloaded. Images will be stored with a filename corresponding to
the url's md5 hash. Defaults to "$HOME/.terraform/image_cache"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L366">property imageSourceUrl</a>
</h3>

```typescript
imageSourceUrl?: pulumi.Input<string>;
```


This is the url of the raw image that will
be downloaded in the `image_cache_path` before being uploaded to Glance.
Glance is able to download image from internet but the `gophercloud` library
does not yet provide a way to do so.
Conflicts with `local_file_path`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L371">property localFilePath</a>
</h3>

```typescript
localFilePath?: pulumi.Input<string>;
```


This is the filepath of the raw image file
that will be uploaded to Glance. Conflicts with `image_source_url`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L376">property minDiskGb</a>
</h3>

```typescript
minDiskGb?: pulumi.Input<number>;
```


Amount of disk space (in GB) required to boot image.
Defaults to 0.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L381">property minRamMb</a>
</h3>

```typescript
minRamMb?: pulumi.Input<number>;
```


Amount of ram (in MB) required to boot image.
Defauts to 0.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L385">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L391">property properties</a>
</h3>

```typescript
properties?: pulumi.Input<{ ... }>;
```


A map of key/value pairs to set freeform
information about an image. See the "Notes" section for further
information about properties.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L396">property protected</a>
</h3>

```typescript
protected?: pulumi.Input<boolean>;
```


If true, image will not be deletable.
Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L403">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Glance client.
A Glance client is needed to create an Image that can be used with
a compute instance. If omitted, the `region` argument of the provider
is used. Changing this creates a new Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L408">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The tags of the image. It must be a list of strings.
At this time, it is not possible to delete all tags of an image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L413">property verifyChecksum</a>
</h3>

```typescript
verifyChecksum?: pulumi.Input<boolean>;
```


If false, the checksum will not be verified
once the image is finished uploading. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L419">property visibility</a>
</h3>

```typescript
visibility?: pulumi.Input<string>;
```


The visibility of the image. Must be one of
"public", "private", "community", or "shared". The ability to set the
visibility depends upon the configuration of the OpenStack cloud.

<h2 class="pdoc-module-header" id="ImageState">
<a class="pdoc-member-name" href="/images/image.ts#L217">interface ImageState</a>
</h2>

Input properties used for looking up and filtering Image resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L221">property checksum</a>
</h3>

```typescript
checksum?: pulumi.Input<string>;
```


The checksum of the data associated with the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L226">property containerFormat</a>
</h3>

```typescript
containerFormat?: pulumi.Input<string>;
```


The container format. Must be one of
"ami", "ari", "aki", "bare", "ovf".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L230">property createdAt</a>
</h3>

```typescript
createdAt?: pulumi.Input<string>;
```


The date the image was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L235">property diskFormat</a>
</h3>

```typescript
diskFormat?: pulumi.Input<string>;
```


The disk format. Must be one of
"ami", "ari", "aki", "vhd", "vmdk", "raw", "qcow2", "vdi", "iso".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L241">property file</a>
</h3>

```typescript
file?: pulumi.Input<string>;
```


the trailing path after the glance
endpoint that represent the location of the image
or the path to retrieve it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L247">property imageCachePath</a>
</h3>

```typescript
imageCachePath?: pulumi.Input<string>;
```


This is the directory where the images will
be downloaded. Images will be stored with a filename corresponding to
the url's md5 hash. Defaults to "$HOME/.terraform/image_cache"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L255">property imageSourceUrl</a>
</h3>

```typescript
imageSourceUrl?: pulumi.Input<string>;
```


This is the url of the raw image that will
be downloaded in the `image_cache_path` before being uploaded to Glance.
Glance is able to download image from internet but the `gophercloud` library
does not yet provide a way to do so.
Conflicts with `local_file_path`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L260">property localFilePath</a>
</h3>

```typescript
localFilePath?: pulumi.Input<string>;
```


This is the filepath of the raw image file
that will be uploaded to Glance. Conflicts with `image_source_url`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L266">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


The metadata associated with the image.
Image metadata allow for meaningfully define the image properties
and tags. See http://docs.openstack.org/developer/glance/metadefs-concepts.html.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L271">property minDiskGb</a>
</h3>

```typescript
minDiskGb?: pulumi.Input<number>;
```


Amount of disk space (in GB) required to boot image.
Defaults to 0.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L276">property minRamMb</a>
</h3>

```typescript
minRamMb?: pulumi.Input<number>;
```


Amount of ram (in MB) required to boot image.
Defauts to 0.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L280">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L284">property owner</a>
</h3>

```typescript
owner?: pulumi.Input<string>;
```


The id of the openstack user who owns the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L290">property properties</a>
</h3>

```typescript
properties?: pulumi.Input<{ ... }>;
```


A map of key/value pairs to set freeform
information about an image. See the "Notes" section for further
information about properties.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L295">property protected</a>
</h3>

```typescript
protected?: pulumi.Input<boolean>;
```


If true, image will not be deletable.
Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L302">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Glance client.
A Glance client is needed to create an Image that can be used with
a compute instance. If omitted, the `region` argument of the provider
is used. Changing this creates a new Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L307">property schema</a>
</h3>

```typescript
schema?: pulumi.Input<string>;
```


The path to the JSON-schema that represent
the image or image

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L311">property sizeBytes</a>
</h3>

```typescript
sizeBytes?: pulumi.Input<number>;
```


The size in bytes of the data associated with the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L316">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


The status of the image. It can be "queued", "active"
or "saving".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L321">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<pulumi.Input<string>[]>;
```


The tags of the image. It must be a list of strings.
At this time, it is not possible to delete all tags of an image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L325">property updateAt</a>
</h3>

```typescript
updateAt?: pulumi.Input<string>;
```


The date the image was last updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L330">property verifyChecksum</a>
</h3>

```typescript
verifyChecksum?: pulumi.Input<boolean>;
```


If false, the checksum will not be verified
once the image is finished uploading. Defaults to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/images/image.ts#L336">property visibility</a>
</h3>

```typescript
visibility?: pulumi.Input<string>;
```


The visibility of the image. Must be one of
"public", "private", "community", or "shared". The ability to set the
visibility depends upon the configuration of the OpenStack cloud.

