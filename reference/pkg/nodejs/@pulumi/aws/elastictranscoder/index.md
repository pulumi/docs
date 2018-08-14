---
title: Module elastictranscoder
---

<a href="../index.html">@pulumi/aws</a> &gt; elastictranscoder

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Pipeline">class Pipeline</a>
* <a href="#Preset">class Preset</a>
* <a href="#PipelineArgs">interface PipelineArgs</a>
* <a href="#PipelineState">interface PipelineState</a>
* <a href="#PresetArgs">interface PresetArgs</a>
* <a href="#PresetState">interface PresetState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts">elastictranscoder/pipeline.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts">elastictranscoder/preset.ts</a> 


<h2 class="pdoc-module-header" id="Pipeline">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L9">class Pipeline</a>
</h2>

Provides an Elastic Transcoder pipeline resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L62">constructor</a>
</h3>

```typescript
new Pipeline(name: string, args: PipelineArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Pipeline resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PipelineState): Pipeline
```


Get an existing Pipeline resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L22">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L26">property awsKmsKeyArn</a>
</h3>

```typescript
public awsKmsKeyArn: pulumi.Output<string | undefined>;
```


The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L30">property contentConfig</a>
</h3>

```typescript
public contentConfig: pulumi.Output<{ ... }>;
```


The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L34">property contentConfigPermissions</a>
</h3>

```typescript
public contentConfigPermissions: pulumi.Output<{ ... }[] | undefined>;
```


The permissions for the `content_config` object. (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L38">property inputBucket</a>
</h3>

```typescript
public inputBucket: pulumi.Output<string>;
```


The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the pipeline. Maximum 40 characters

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L46">property notifications</a>
</h3>

```typescript
public notifications: pulumi.Output<{ ... } | undefined>;
```


The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L50">property outputBucket</a>
</h3>

```typescript
public outputBucket: pulumi.Output<string>;
```


The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L54">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L58">property thumbnailConfig</a>
</h3>

```typescript
public thumbnailConfig: pulumi.Output<{ ... }>;
```


The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L62">property thumbnailConfigPermissions</a>
</h3>

```typescript
public thumbnailConfigPermissions: pulumi.Output<{ ... }[] | undefined>;
```


The permissions for the `thumbnail_config` object. (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Preset">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L9">class Preset</a>
</h2>

Provides an Elastic Transcoder preset resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L57">constructor</a>
</h3>

```typescript
new Preset(name: string, args: PresetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Preset resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PresetState): Preset
```


Get an existing Preset resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L22">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L26">property audio</a>
</h3>

```typescript
public audio: pulumi.Output<{ ... } | undefined>;
```


Audio parameters object (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L30">property audioCodecOptions</a>
</h3>

```typescript
public audioCodecOptions: pulumi.Output<{ ... } | undefined>;
```


Codec options for the audio parameters (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L34">property container</a>
</h3>

```typescript
public container: pulumi.Output<string>;
```


The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L38">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the preset (maximum 255 characters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the preset. (maximum 40 characters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L46">property thumbnails</a>
</h3>

```typescript
public thumbnails: pulumi.Output<{ ... } | undefined>;
```


Thumbnail parameters object (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L47">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L51">property video</a>
</h3>

```typescript
public video: pulumi.Output<{ ... } | undefined>;
```


Video parameters object (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L52">property videoCodecOptions</a>
</h3>

```typescript
public videoCodecOptions: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L57">property videoWatermarks</a>
</h3>

```typescript
public videoWatermarks: pulumi.Output<{ ... }[] | undefined>;
```


Watermark parameters for the video parameters (documented below)
* `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters

<h2 class="pdoc-module-header" id="PipelineArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L161">interface PipelineArgs</a>
</h2>

The set of arguments for constructing a Pipeline resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L165">property awsKmsKeyArn</a>
</h3>

```typescript
awsKmsKeyArn?: pulumi.Input<string>;
```


The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L169">property contentConfig</a>
</h3>

```typescript
contentConfig?: pulumi.Input<{ ... }>;
```


The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L173">property contentConfigPermissions</a>
</h3>

```typescript
contentConfigPermissions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The permissions for the `content_config` object. (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L177">property inputBucket</a>
</h3>

```typescript
inputBucket: pulumi.Input<string>;
```


The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L181">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the pipeline. Maximum 40 characters

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L185">property notifications</a>
</h3>

```typescript
notifications?: pulumi.Input<{ ... }>;
```


The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L189">property outputBucket</a>
</h3>

```typescript
outputBucket?: pulumi.Input<string>;
```


The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L193">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L197">property thumbnailConfig</a>
</h3>

```typescript
thumbnailConfig?: pulumi.Input<{ ... }>;
```


The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L201">property thumbnailConfigPermissions</a>
</h3>

```typescript
thumbnailConfigPermissions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The permissions for the `thumbnail_config` object. (documented below)

<h2 class="pdoc-module-header" id="PipelineState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L114">interface PipelineState</a>
</h2>

Input properties used for looking up and filtering Pipeline resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L115">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L119">property awsKmsKeyArn</a>
</h3>

```typescript
awsKmsKeyArn?: pulumi.Input<string>;
```


The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L123">property contentConfig</a>
</h3>

```typescript
contentConfig?: pulumi.Input<{ ... }>;
```


The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L127">property contentConfigPermissions</a>
</h3>

```typescript
contentConfigPermissions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The permissions for the `content_config` object. (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L131">property inputBucket</a>
</h3>

```typescript
inputBucket?: pulumi.Input<string>;
```


The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L135">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the pipeline. Maximum 40 characters

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L139">property notifications</a>
</h3>

```typescript
notifications?: pulumi.Input<{ ... }>;
```


The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L143">property outputBucket</a>
</h3>

```typescript
outputBucket?: pulumi.Input<string>;
```


The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L147">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L151">property thumbnailConfig</a>
</h3>

```typescript
thumbnailConfig?: pulumi.Input<{ ... }>;
```


The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/pipeline.ts#L155">property thumbnailConfigPermissions</a>
</h3>

```typescript
thumbnailConfigPermissions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The permissions for the `thumbnail_config` object. (documented below)

<h2 class="pdoc-module-header" id="PresetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L148">interface PresetArgs</a>
</h2>

The set of arguments for constructing a Preset resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L152">property audio</a>
</h3>

```typescript
audio?: pulumi.Input<{ ... }>;
```


Audio parameters object (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L156">property audioCodecOptions</a>
</h3>

```typescript
audioCodecOptions?: pulumi.Input<{ ... }>;
```


Codec options for the audio parameters (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L160">property container</a>
</h3>

```typescript
container: pulumi.Input<string>;
```


The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L164">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the preset (maximum 255 characters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L168">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the preset. (maximum 40 characters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L172">property thumbnails</a>
</h3>

```typescript
thumbnails?: pulumi.Input<{ ... }>;
```


Thumbnail parameters object (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L173">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L177">property video</a>
</h3>

```typescript
video?: pulumi.Input<{ ... }>;
```


Video parameters object (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L178">property videoCodecOptions</a>
</h3>

```typescript
videoCodecOptions?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L183">property videoWatermarks</a>
</h3>

```typescript
videoWatermarks?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Watermark parameters for the video parameters (documented below)
* `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters

<h2 class="pdoc-module-header" id="PresetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L106">interface PresetState</a>
</h2>

Input properties used for looking up and filtering Preset resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L107">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L111">property audio</a>
</h3>

```typescript
audio?: pulumi.Input<{ ... }>;
```


Audio parameters object (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L115">property audioCodecOptions</a>
</h3>

```typescript
audioCodecOptions?: pulumi.Input<{ ... }>;
```


Codec options for the audio parameters (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L119">property container</a>
</h3>

```typescript
container?: pulumi.Input<string>;
```


The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L123">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the preset (maximum 255 characters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L127">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the preset. (maximum 40 characters)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L131">property thumbnails</a>
</h3>

```typescript
thumbnails?: pulumi.Input<{ ... }>;
```


Thumbnail parameters object (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L132">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L136">property video</a>
</h3>

```typescript
video?: pulumi.Input<{ ... }>;
```


Video parameters object (documented below)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L137">property videoCodecOptions</a>
</h3>

```typescript
videoCodecOptions?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elastictranscoder/preset.ts#L142">property videoWatermarks</a>
</h3>

```typescript
videoWatermarks?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Watermark parameters for the video parameters (documented below)
* `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters

