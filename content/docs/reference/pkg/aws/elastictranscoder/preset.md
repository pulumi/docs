
---
title: "Preset"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides an Elastic Transcoder preset resource.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const bar = new aws.elastictranscoder.Preset("bar", {
    audio: {
        audioPackingMode: "SingleTrack",
        bitRate: "96",
        channels: "2",
        codec: "AAC",
        sampleRate: "44100",
    },
    audioCodecOptions: {
        profile: "AAC-LC",
    },
    container: "mp4",
    description: "Sample Preset",
    thumbnails: {
        format: "png",
        interval: "120",
        maxHeight: "auto",
        maxWidth: "auto",
        paddingPolicy: "Pad",
        sizingPolicy: "Fit",
    },
    video: {
        bitRate: "1600",
        codec: "H.264",
        displayAspectRatio: "16:9",
        fixedGop: "false",
        frameRate: "auto",
        keyframesMaxDist: "240",
        maxFrameRate: "60",
        maxHeight: "auto",
        maxWidth: "auto",
        paddingPolicy: "Pad",
        sizingPolicy: "Fit",
    },
    videoCodecOptions: {
        ColorSpaceConversionMode: "None",
        InterlacedMode: "Progressive",
        Level: "2.2",
        MaxReferenceFrames: 3,
        Profile: "main",
    },
    videoWatermarks: [{
        horizontalAlign: "Right",
        horizontalOffset: "10px",
        id: "Test",
        maxHeight: "20%",
        maxWidth: "20%",
        opacity: "55.5",
        sizingPolicy: "ShrinkToFit",
        target: "Content",
        verticalAlign: "Bottom",
        verticalOffset: "10px",
    }],
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastictranscoder_preset.html.markdown.



## Create a Preset Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elastictranscoder/#Preset">Preset</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elastictranscoder/#PresetArgs">PresetArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Preset</span><span class="p">(resource_name, opts=None, </span>audio=None<span class="p">, </span>audio_codec_options=None<span class="p">, </span>container=None<span class="p">, </span>description=None<span class="p">, </span>name=None<span class="p">, </span>thumbnails=None<span class="p">, </span>type=None<span class="p">, </span>video=None<span class="p">, </span>video_codec_options=None<span class="p">, </span>video_watermarks=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewPreset<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PresetArgs">PresetArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#Preset">Preset</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.Preset.html">Preset</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PresetArgs.html">PresetArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Preset resource with the given unique name, arguments, and options.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Audio</td>
            <td class="align-top">
                
                <code><a href="#presetaudio">Pulumi.<wbr>Aws.<wbr>Elastictranscoder.<wbr>Preset<wbr>Audio<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Audio parameters object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Audio<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#presetaudiocodecoptions">Pulumi.<wbr>Aws.<wbr>Elastictranscoder.<wbr>Preset<wbr>Audio<wbr>Codec<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Codec options for the audio parameters (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Container</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A description of the preset (maximum 255 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the preset. (maximum 40 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnails</td>
            <td class="align-top">
                
                <code><a href="#presetthumbnails">Pulumi.<wbr>Aws.<wbr>Elastictranscoder.<wbr>Preset<wbr>Thumbnails<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Thumbnail parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video</td>
            <td class="align-top">
                
                <code><a href="#presetvideo">Pulumi.<wbr>Aws.<wbr>Elastictranscoder.<wbr>Preset<wbr>Video<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Video parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video<wbr>Watermarks</td>
            <td class="align-top">
                
                <code><a href="#presetvideowatermark">List&lt;Pulumi.<wbr>Aws.<wbr>Elastictranscoder.<wbr>Preset<wbr>Video<wbr>Watermark<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Watermark parameters for the video parameters (documented below)
* `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Audio</td>
            <td class="align-top">
                
                <code><a href="#presetaudio">*Preset<wbr>Audio</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Audio parameters object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Audio<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#presetaudiocodecoptions">*Preset<wbr>Audio<wbr>Codec<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Codec options for the audio parameters (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Container</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A description of the preset (maximum 255 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the preset. (maximum 40 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnails</td>
            <td class="align-top">
                
                <code><a href="#presetthumbnails">*Preset<wbr>Thumbnails</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Thumbnail parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video</td>
            <td class="align-top">
                
                <code><a href="#presetvideo">*Preset<wbr>Video</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Video parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video<wbr>Watermarks</td>
            <td class="align-top">
                
                <code><a href="#presetvideowatermark">[]Preset<wbr>Video<wbr>Watermark</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Watermark parameters for the video parameters (documented below)
* `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">audio</td>
            <td class="align-top">
                
                <code><a href="#presetaudio">elastictranscoder.<wbr>Preset<wbr>Audio?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Audio parameters object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">audio<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#presetaudiocodecoptions">elastictranscoder.<wbr>Preset<wbr>Audio<wbr>Codec<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Codec options for the audio parameters (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">container</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A description of the preset (maximum 255 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the preset. (maximum 40 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnails</td>
            <td class="align-top">
                
                <code><a href="#presetthumbnails">elastictranscoder.<wbr>Preset<wbr>Thumbnails?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Thumbnail parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video</td>
            <td class="align-top">
                
                <code><a href="#presetvideo">elastictranscoder.<wbr>Preset<wbr>Video?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Video parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video<wbr>Watermarks</td>
            <td class="align-top">
                
                <code><a href="#presetvideowatermark">elastictranscoder.<wbr>Preset<wbr>Video<wbr>Watermark[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Watermark parameters for the video parameters (documented below)
* `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">audio</td>
            <td class="align-top">
                
                <code><a href="#presetaudio">Dict[Preset<wbr>Audio]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Audio parameters object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">audio_<wbr>codec_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#presetaudiocodecoptions">Dict[Preset<wbr>Audio<wbr>Codec<wbr>Options]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Codec options for the audio parameters (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">container</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A description of the preset (maximum 255 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the preset. (maximum 40 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnails</td>
            <td class="align-top">
                
                <code><a href="#presetthumbnails">Dict[Preset<wbr>Thumbnails]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Thumbnail parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video</td>
            <td class="align-top">
                
                <code><a href="#presetvideo">Dict[Preset<wbr>Video]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Video parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video_<wbr>codec_<wbr>options</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video_<wbr>watermarks</td>
            <td class="align-top">
                
                <code><a href="#presetvideowatermark">List[Preset<wbr>Video<wbr>Watermark]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Watermark parameters for the video parameters (documented below)
* `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Preset Output Properties

The following output properties are available:



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Audio</td>
            <td class="align-top">
                
                <code><a href="#presetaudio">Pulumi.<wbr>Aws.<wbr>Elastictranscoder.<wbr>Preset<wbr>Audio?</a></code>
            </td>
            <td class="align-top">{{% md %}} Audio parameters object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Audio<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#presetaudiocodecoptions">Pulumi.<wbr>Aws.<wbr>Elastictranscoder.<wbr>Preset<wbr>Audio<wbr>Codec<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} Codec options for the audio parameters (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Container</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A description of the preset (maximum 255 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the preset. (maximum 40 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnails</td>
            <td class="align-top">
                
                <code><a href="#presetthumbnails">Pulumi.<wbr>Aws.<wbr>Elastictranscoder.<wbr>Preset<wbr>Thumbnails?</a></code>
            </td>
            <td class="align-top">{{% md %}} Thumbnail parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video</td>
            <td class="align-top">
                
                <code><a href="#presetvideo">Pulumi.<wbr>Aws.<wbr>Elastictranscoder.<wbr>Preset<wbr>Video?</a></code>
            </td>
            <td class="align-top">{{% md %}} Video parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video<wbr>Watermarks</td>
            <td class="align-top">
                
                <code><a href="#presetvideowatermark">List&lt;Pulumi.<wbr>Aws.<wbr>Elastictranscoder.<wbr>Preset<wbr>Video<wbr>Watermark&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} Watermark parameters for the video parameters (documented below)
* `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Audio</td>
            <td class="align-top">
                
                <code><a href="#presetaudio">*Preset<wbr>Audio</a></code>
            </td>
            <td class="align-top">{{% md %}} Audio parameters object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Audio<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#presetaudiocodecoptions">*Preset<wbr>Audio<wbr>Codec<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} Codec options for the audio parameters (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Container</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} A description of the preset (maximum 255 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the preset. (maximum 40 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnails</td>
            <td class="align-top">
                
                <code><a href="#presetthumbnails">*Preset<wbr>Thumbnails</a></code>
            </td>
            <td class="align-top">{{% md %}} Thumbnail parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video</td>
            <td class="align-top">
                
                <code><a href="#presetvideo">*Preset<wbr>Video</a></code>
            </td>
            <td class="align-top">{{% md %}} Video parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video<wbr>Watermarks</td>
            <td class="align-top">
                
                <code><a href="#presetvideowatermark">[]Preset<wbr>Video<wbr>Watermark</a></code>
            </td>
            <td class="align-top">{{% md %}} Watermark parameters for the video parameters (documented below)
* `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">audio</td>
            <td class="align-top">
                
                <code><a href="#presetaudio">elastictranscoder.<wbr>Preset<wbr>Audio?</a></code>
            </td>
            <td class="align-top">{{% md %}} Audio parameters object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">audio<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#presetaudiocodecoptions">elastictranscoder.<wbr>Preset<wbr>Audio<wbr>Codec<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} Codec options for the audio parameters (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">container</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A description of the preset (maximum 255 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the preset. (maximum 40 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnails</td>
            <td class="align-top">
                
                <code><a href="#presetthumbnails">elastictranscoder.<wbr>Preset<wbr>Thumbnails?</a></code>
            </td>
            <td class="align-top">{{% md %}} Thumbnail parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video</td>
            <td class="align-top">
                
                <code><a href="#presetvideo">elastictranscoder.<wbr>Preset<wbr>Video?</a></code>
            </td>
            <td class="align-top">{{% md %}} Video parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video<wbr>Watermarks</td>
            <td class="align-top">
                
                <code><a href="#presetvideowatermark">elastictranscoder.<wbr>Preset<wbr>Video<wbr>Watermark[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} Watermark parameters for the video parameters (documented below)
* `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">audio</td>
            <td class="align-top">
                
                <code><a href="#presetaudio">Dict[Preset<wbr>Audio]</a></code>
            </td>
            <td class="align-top">{{% md %}} Audio parameters object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">audio_<wbr>codec_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#presetaudiocodecoptions">Dict[Preset<wbr>Audio<wbr>Codec<wbr>Options]</a></code>
            </td>
            <td class="align-top">{{% md %}} Codec options for the audio parameters (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">container</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A description of the preset (maximum 255 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the preset. (maximum 40 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnails</td>
            <td class="align-top">
                
                <code><a href="#presetthumbnails">Dict[Preset<wbr>Thumbnails]</a></code>
            </td>
            <td class="align-top">{{% md %}} Thumbnail parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video</td>
            <td class="align-top">
                
                <code><a href="#presetvideo">Dict[Preset<wbr>Video]</a></code>
            </td>
            <td class="align-top">{{% md %}} Video parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video_<wbr>codec_<wbr>options</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video_<wbr>watermarks</td>
            <td class="align-top">
                
                <code><a href="#presetvideowatermark">List[Preset<wbr>Video<wbr>Watermark]</a></code>
            </td>
            <td class="align-top">{{% md %}} Watermark parameters for the video parameters (documented below)
* `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Preset Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elastictranscoder/#PresetState">PresetState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elastictranscoder/#Preset">Preset</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>audio=None<span class="p">, </span>audio_codec_options=None<span class="p">, </span>container=None<span class="p">, </span>description=None<span class="p">, </span>name=None<span class="p">, </span>thumbnails=None<span class="p">, </span>type=None<span class="p">, </span>video=None<span class="p">, </span>video_codec_options=None<span class="p">, </span>video_watermarks=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetPreset<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PresetState">PresetState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#Preset">Preset</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.Preset.html">Preset</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PresetState.html">PresetState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Preset resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following state arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Audio</td>
            <td class="align-top">
                
                <code><a href="#presetaudio">Pulumi.<wbr>Aws.<wbr>Elastictranscoder.<wbr>Preset<wbr>Audio<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Audio parameters object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Audio<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#presetaudiocodecoptions">Pulumi.<wbr>Aws.<wbr>Elastictranscoder.<wbr>Preset<wbr>Audio<wbr>Codec<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Codec options for the audio parameters (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Container</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A description of the preset (maximum 255 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the preset. (maximum 40 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnails</td>
            <td class="align-top">
                
                <code><a href="#presetthumbnails">Pulumi.<wbr>Aws.<wbr>Elastictranscoder.<wbr>Preset<wbr>Thumbnails<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Thumbnail parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video</td>
            <td class="align-top">
                
                <code><a href="#presetvideo">Pulumi.<wbr>Aws.<wbr>Elastictranscoder.<wbr>Preset<wbr>Video<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Video parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video<wbr>Watermarks</td>
            <td class="align-top">
                
                <code><a href="#presetvideowatermark">List&lt;Pulumi.<wbr>Aws.<wbr>Elastictranscoder.<wbr>Preset<wbr>Video<wbr>Watermark<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Watermark parameters for the video parameters (documented below)
* `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Audio</td>
            <td class="align-top">
                
                <code><a href="#presetaudio">*Preset<wbr>Audio</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Audio parameters object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Audio<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#presetaudiocodecoptions">*Preset<wbr>Audio<wbr>Codec<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Codec options for the audio parameters (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Container</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A description of the preset (maximum 255 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the preset. (maximum 40 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Thumbnails</td>
            <td class="align-top">
                
                <code><a href="#presetthumbnails">*Preset<wbr>Thumbnails</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Thumbnail parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video</td>
            <td class="align-top">
                
                <code><a href="#presetvideo">*Preset<wbr>Video</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Video parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Video<wbr>Watermarks</td>
            <td class="align-top">
                
                <code><a href="#presetvideowatermark">[]Preset<wbr>Video<wbr>Watermark</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Watermark parameters for the video parameters (documented below)
* `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">audio</td>
            <td class="align-top">
                
                <code><a href="#presetaudio">elastictranscoder.<wbr>Preset<wbr>Audio?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Audio parameters object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">audio<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#presetaudiocodecoptions">elastictranscoder.<wbr>Preset<wbr>Audio<wbr>Codec<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Codec options for the audio parameters (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">container</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A description of the preset (maximum 255 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the preset. (maximum 40 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnails</td>
            <td class="align-top">
                
                <code><a href="#presetthumbnails">elastictranscoder.<wbr>Preset<wbr>Thumbnails?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Thumbnail parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video</td>
            <td class="align-top">
                
                <code><a href="#presetvideo">elastictranscoder.<wbr>Preset<wbr>Video?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Video parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video<wbr>Codec<wbr>Options</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video<wbr>Watermarks</td>
            <td class="align-top">
                
                <code><a href="#presetvideowatermark">elastictranscoder.<wbr>Preset<wbr>Video<wbr>Watermark[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Watermark parameters for the video parameters (documented below)
* `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">audio</td>
            <td class="align-top">
                
                <code><a href="#presetaudio">Dict[Preset<wbr>Audio]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Audio parameters object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">audio_<wbr>codec_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#presetaudiocodecoptions">Dict[Preset<wbr>Audio<wbr>Codec<wbr>Options]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Codec options for the audio parameters (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">container</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The container type for the output file. Valid values are `flac`, `flv`, `fmp4`, `gif`, `mp3`, `mp4`, `mpg`, `mxf`, `oga`, `ogg`, `ts`, and `webm`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A description of the preset (maximum 255 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the preset. (maximum 40 characters)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">thumbnails</td>
            <td class="align-top">
                
                <code><a href="#presetthumbnails">Dict[Preset<wbr>Thumbnails]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Thumbnail parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video</td>
            <td class="align-top">
                
                <code><a href="#presetvideo">Dict[Preset<wbr>Video]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Video parameters object (documented below)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video_<wbr>codec_<wbr>options</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">video_<wbr>watermarks</td>
            <td class="align-top">
                
                <code><a href="#presetvideowatermark">List[Preset<wbr>Video<wbr>Watermark]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Watermark parameters for the video parameters (documented below)
* `video_codec_options` (Optional, Forces new resource) Codec options for the video parameters
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### PresetAudio
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PresetAudio">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PresetAudio">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PresetAudioArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PresetAudioOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PresetAudioArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PresetAudio.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Audio<wbr>Packing<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The method of organizing audio channels and tracks. Use Audio:Channels to specify the number of channels in your output, and Audio:AudioPackingMode to specify the number of tracks and their relation to the channels. If you do not specify an Audio:AudioPackingMode, Elastic Transcoder uses SingleTrack.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bit<wbr>Rate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Channels</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of audio channels in the output file
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Codec</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The video codec for the output file. Valid values are `gif`, `H.264`, `mpeg2`, `vp8`, and `vp9`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sample<wbr>Rate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The sample rate of the audio stream in the output file, in hertz. Valid values are: `auto`, `22050`, `32000`, `44100`, `48000`, `96000`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Audio<wbr>Packing<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The method of organizing audio channels and tracks. Use Audio:Channels to specify the number of channels in your output, and Audio:AudioPackingMode to specify the number of tracks and their relation to the channels. If you do not specify an Audio:AudioPackingMode, Elastic Transcoder uses SingleTrack.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bit<wbr>Rate</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Channels</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of audio channels in the output file
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Codec</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The video codec for the output file. Valid values are `gif`, `H.264`, `mpeg2`, `vp8`, and `vp9`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sample<wbr>Rate</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The sample rate of the audio stream in the output file, in hertz. Valid values are: `auto`, `22050`, `32000`, `44100`, `48000`, `96000`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">audio<wbr>Packing<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The method of organizing audio channels and tracks. Use Audio:Channels to specify the number of channels in your output, and Audio:AudioPackingMode to specify the number of tracks and their relation to the channels. If you do not specify an Audio:AudioPackingMode, Elastic Transcoder uses SingleTrack.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bit<wbr>Rate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">channels</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of audio channels in the output file
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">codec</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The video codec for the output file. Valid values are `gif`, `H.264`, `mpeg2`, `vp8`, and `vp9`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sample<wbr>Rate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The sample rate of the audio stream in the output file, in hertz. Valid values are: `auto`, `22050`, `32000`, `44100`, `48000`, `96000`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">audio<wbr>Packing<wbr>Mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The method of organizing audio channels and tracks. Use Audio:Channels to specify the number of channels in your output, and Audio:AudioPackingMode to specify the number of tracks and their relation to the channels. If you do not specify an Audio:AudioPackingMode, Elastic Transcoder uses SingleTrack.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bit<wbr>Rate</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">channels</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of audio channels in the output file
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">codec</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The video codec for the output file. Valid values are `gif`, `H.264`, `mpeg2`, `vp8`, and `vp9`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sample<wbr>Rate</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The sample rate of the audio stream in the output file, in hertz. Valid values are: `auto`, `22050`, `32000`, `44100`, `48000`, `96000`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### PresetAudioCodecOptions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PresetAudioCodecOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PresetAudioCodecOptions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PresetAudioCodecOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PresetAudioCodecOptionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PresetAudioCodecOptionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PresetAudioCodecOptions.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bit<wbr>Depth</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bit depth of a sample is how many bits of information are included in the audio samples. Valid values are `16` and `24`. (FLAC/PCM Only)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bit<wbr>Order</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The order the bits of a PCM sample are stored in. The supported value is LittleEndian. (PCM Only)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Profile</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you specified AAC for Audio:Codec, choose the AAC profile for the output file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Signed</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether audio samples are represented with negative and positive numbers (signed) or only positive numbers (unsigned). The supported value is Signed. (PCM Only)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bit<wbr>Depth</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bit depth of a sample is how many bits of information are included in the audio samples. Valid values are `16` and `24`. (FLAC/PCM Only)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bit<wbr>Order</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The order the bits of a PCM sample are stored in. The supported value is LittleEndian. (PCM Only)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Profile</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you specified AAC for Audio:Codec, choose the AAC profile for the output file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Signed</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether audio samples are represented with negative and positive numbers (signed) or only positive numbers (unsigned). The supported value is Signed. (PCM Only)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bit<wbr>Depth</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bit depth of a sample is how many bits of information are included in the audio samples. Valid values are `16` and `24`. (FLAC/PCM Only)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bit<wbr>Order</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The order the bits of a PCM sample are stored in. The supported value is LittleEndian. (PCM Only)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">profile</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you specified AAC for Audio:Codec, choose the AAC profile for the output file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">signed</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether audio samples are represented with negative and positive numbers (signed) or only positive numbers (unsigned). The supported value is Signed. (PCM Only)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bit<wbr>Depth</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bit depth of a sample is how many bits of information are included in the audio samples. Valid values are `16` and `24`. (FLAC/PCM Only)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bit<wbr>Order</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The order the bits of a PCM sample are stored in. The supported value is LittleEndian. (PCM Only)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">profile</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you specified AAC for Audio:Codec, choose the AAC profile for the output file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">signed</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether audio samples are represented with negative and positive numbers (signed) or only positive numbers (unsigned). The supported value is Signed. (PCM Only)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### PresetThumbnails
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PresetThumbnails">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PresetThumbnails">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PresetThumbnailsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PresetThumbnailsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PresetThumbnailsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PresetThumbnails.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Aspect<wbr>Ratio</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The display aspect ratio of the video in the output file. Valid values are: `auto`, `1:1`, `4:3`, `3:2`, `16:9`. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values `max_width`, `max_height`, `sizing_policy`, `padding_policy`, and `display_aspect_ratio` instead of `resolution` and `aspect_ratio`.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The format of thumbnails, if any. Valid formats are jpg and png.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Interval</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The approximate number of seconds between thumbnails. The value must be an integer. The actual interval can vary by several seconds from one thumbnail to the next.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Height</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum height of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Width</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum width of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Padding<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for `max_width` and `max_height`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resolution</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The width and height of the video in the output file, in pixels. Valid values are `auto` and `widthxheight`. (see note for `aspect_ratio`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sizing<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Aspect<wbr>Ratio</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The display aspect ratio of the video in the output file. Valid values are: `auto`, `1:1`, `4:3`, `3:2`, `16:9`. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values `max_width`, `max_height`, `sizing_policy`, `padding_policy`, and `display_aspect_ratio` instead of `resolution` and `aspect_ratio`.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Format</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The format of thumbnails, if any. Valid formats are jpg and png.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Interval</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The approximate number of seconds between thumbnails. The value must be an integer. The actual interval can vary by several seconds from one thumbnail to the next.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Height</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum height of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Width</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum width of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Padding<wbr>Policy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for `max_width` and `max_height`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resolution</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The width and height of the video in the output file, in pixels. Valid values are `auto` and `widthxheight`. (see note for `aspect_ratio`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sizing<wbr>Policy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">aspect<wbr>Ratio</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The display aspect ratio of the video in the output file. Valid values are: `auto`, `1:1`, `4:3`, `3:2`, `16:9`. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values `max_width`, `max_height`, `sizing_policy`, `padding_policy`, and `display_aspect_ratio` instead of `resolution` and `aspect_ratio`.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The format of thumbnails, if any. Valid formats are jpg and png.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">interval</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The approximate number of seconds between thumbnails. The value must be an integer. The actual interval can vary by several seconds from one thumbnail to the next.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Height</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum height of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Width</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum width of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">padding<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for `max_width` and `max_height`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resolution</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The width and height of the video in the output file, in pixels. Valid values are `auto` and `widthxheight`. (see note for `aspect_ratio`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sizing<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">aspect<wbr>Ratio</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The display aspect ratio of the video in the output file. Valid values are: `auto`, `1:1`, `4:3`, `3:2`, `16:9`. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values `max_width`, `max_height`, `sizing_policy`, `padding_policy`, and `display_aspect_ratio` instead of `resolution` and `aspect_ratio`.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">format</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The format of thumbnails, if any. Valid formats are jpg and png.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">interval</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The approximate number of seconds between thumbnails. The value must be an integer. The actual interval can vary by several seconds from one thumbnail to the next.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Height</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum height of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Width</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum width of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">padding<wbr>Policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for `max_width` and `max_height`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resolution</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The width and height of the video in the output file, in pixels. Valid values are `auto` and `widthxheight`. (see note for `aspect_ratio`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sizing<wbr>Policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### PresetVideo
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PresetVideo">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PresetVideo">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PresetVideoArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PresetVideoOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PresetVideoArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PresetVideo.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Aspect<wbr>Ratio</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The display aspect ratio of the video in the output file. Valid values are: `auto`, `1:1`, `4:3`, `3:2`, `16:9`. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values `max_width`, `max_height`, `sizing_policy`, `padding_policy`, and `display_aspect_ratio` instead of `resolution` and `aspect_ratio`.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bit<wbr>Rate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Codec</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The video codec for the output file. Valid values are `gif`, `H.264`, `mpeg2`, `vp8`, and `vp9`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Display<wbr>Aspect<wbr>Ratio</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value that Elastic Transcoder adds to the metadata in the output file. If you set DisplayAspectRatio to auto, Elastic Transcoder chooses an aspect ratio that ensures square pixels. If you specify another option, Elastic Transcoder sets that value in the output file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Fixed<wbr>Gop</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to use a fixed value for Video:FixedGOP. Not applicable for containers of type gif. Valid values are true and false. Also known as, Fixed Number of Frames Between Keyframes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Frame<wbr>Rate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frames per second for the video stream in the output file. The following values are valid: `auto`, `10`, `15`, `23.97`, `24`, `25`, `29.97`, `30`, `50`, `60`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Keyframes<wbr>Max<wbr>Dist</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum number of frames between key frames. Not applicable for containers of type gif.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Frame<wbr>Rate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you specify auto for FrameRate, Elastic Transcoder uses the frame rate of the input video for the frame rate of the output video, up to the maximum frame rate. If you do not specify a MaxFrameRate, Elastic Transcoder will use a default of 30.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Height</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum height of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Width</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum width of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Padding<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for `max_width` and `max_height`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resolution</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The width and height of the video in the output file, in pixels. Valid values are `auto` and `widthxheight`. (see note for `aspect_ratio`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sizing<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Aspect<wbr>Ratio</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The display aspect ratio of the video in the output file. Valid values are: `auto`, `1:1`, `4:3`, `3:2`, `16:9`. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values `max_width`, `max_height`, `sizing_policy`, `padding_policy`, and `display_aspect_ratio` instead of `resolution` and `aspect_ratio`.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bit<wbr>Rate</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Codec</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The video codec for the output file. Valid values are `gif`, `H.264`, `mpeg2`, `vp8`, and `vp9`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Display<wbr>Aspect<wbr>Ratio</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value that Elastic Transcoder adds to the metadata in the output file. If you set DisplayAspectRatio to auto, Elastic Transcoder chooses an aspect ratio that ensures square pixels. If you specify another option, Elastic Transcoder sets that value in the output file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Fixed<wbr>Gop</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to use a fixed value for Video:FixedGOP. Not applicable for containers of type gif. Valid values are true and false. Also known as, Fixed Number of Frames Between Keyframes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Frame<wbr>Rate</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frames per second for the video stream in the output file. The following values are valid: `auto`, `10`, `15`, `23.97`, `24`, `25`, `29.97`, `30`, `50`, `60`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Keyframes<wbr>Max<wbr>Dist</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum number of frames between key frames. Not applicable for containers of type gif.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Frame<wbr>Rate</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you specify auto for FrameRate, Elastic Transcoder uses the frame rate of the input video for the frame rate of the output video, up to the maximum frame rate. If you do not specify a MaxFrameRate, Elastic Transcoder will use a default of 30.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Height</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum height of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Width</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum width of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Padding<wbr>Policy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for `max_width` and `max_height`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resolution</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The width and height of the video in the output file, in pixels. Valid values are `auto` and `widthxheight`. (see note for `aspect_ratio`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sizing<wbr>Policy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">aspect<wbr>Ratio</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The display aspect ratio of the video in the output file. Valid values are: `auto`, `1:1`, `4:3`, `3:2`, `16:9`. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values `max_width`, `max_height`, `sizing_policy`, `padding_policy`, and `display_aspect_ratio` instead of `resolution` and `aspect_ratio`.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bit<wbr>Rate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">codec</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The video codec for the output file. Valid values are `gif`, `H.264`, `mpeg2`, `vp8`, and `vp9`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">display<wbr>Aspect<wbr>Ratio</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value that Elastic Transcoder adds to the metadata in the output file. If you set DisplayAspectRatio to auto, Elastic Transcoder chooses an aspect ratio that ensures square pixels. If you specify another option, Elastic Transcoder sets that value in the output file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">fixed<wbr>Gop</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to use a fixed value for Video:FixedGOP. Not applicable for containers of type gif. Valid values are true and false. Also known as, Fixed Number of Frames Between Keyframes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">frame<wbr>Rate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frames per second for the video stream in the output file. The following values are valid: `auto`, `10`, `15`, `23.97`, `24`, `25`, `29.97`, `30`, `50`, `60`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">keyframes<wbr>Max<wbr>Dist</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum number of frames between key frames. Not applicable for containers of type gif.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Frame<wbr>Rate</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you specify auto for FrameRate, Elastic Transcoder uses the frame rate of the input video for the frame rate of the output video, up to the maximum frame rate. If you do not specify a MaxFrameRate, Elastic Transcoder will use a default of 30.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Height</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum height of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Width</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum width of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">padding<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for `max_width` and `max_height`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resolution</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The width and height of the video in the output file, in pixels. Valid values are `auto` and `widthxheight`. (see note for `aspect_ratio`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sizing<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">aspect<wbr>Ratio</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The display aspect ratio of the video in the output file. Valid values are: `auto`, `1:1`, `4:3`, `3:2`, `16:9`. (Note; to better control resolution and aspect ratio of output videos, we recommend that you use the values `max_width`, `max_height`, `sizing_policy`, `padding_policy`, and `display_aspect_ratio` instead of `resolution` and `aspect_ratio`.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bit<wbr>Rate</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The bit rate of the video stream in the output file, in kilobits/second. You can configure variable bit rate or constant bit rate encoding.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">codec</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The video codec for the output file. Valid values are `gif`, `H.264`, `mpeg2`, `vp8`, and `vp9`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">display<wbr>Aspect<wbr>Ratio</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value that Elastic Transcoder adds to the metadata in the output file. If you set DisplayAspectRatio to auto, Elastic Transcoder chooses an aspect ratio that ensures square pixels. If you specify another option, Elastic Transcoder sets that value in the output file.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">fixed<wbr>Gop</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to use a fixed value for Video:FixedGOP. Not applicable for containers of type gif. Valid values are true and false. Also known as, Fixed Number of Frames Between Keyframes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">frame<wbr>Rate</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frames per second for the video stream in the output file. The following values are valid: `auto`, `10`, `15`, `23.97`, `24`, `25`, `29.97`, `30`, `50`, `60`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">keyframes<wbr>Max<wbr>Dist</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum number of frames between key frames. Not applicable for containers of type gif.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Frame<wbr>Rate</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If you specify auto for FrameRate, Elastic Transcoder uses the frame rate of the input video for the frame rate of the output video, up to the maximum frame rate. If you do not specify a MaxFrameRate, Elastic Transcoder will use a default of 30.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Height</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum height of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Width</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum width of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">padding<wbr>Policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When you set PaddingPolicy to Pad, Elastic Transcoder might add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for `max_width` and `max_height`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resolution</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The width and height of the video in the output file, in pixels. Valid values are `auto` and `widthxheight`. (see note for `aspect_ratio`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sizing<wbr>Policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### PresetVideoWatermark
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PresetVideoWatermark">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PresetVideoWatermark">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PresetVideoWatermarkArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elastictranscoder?tab=doc#PresetVideoWatermarkOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PresetVideoWatermarkArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elastictranscoder.PresetVideoWatermark.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Horizontal<wbr>Align</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The horizontal position of the watermark unless you specify a nonzero value for `horzontal_offset`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Horizontal<wbr>Offset</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount by which you want the horizontal position of the watermark to be offset from the position specified by `horizontal_align`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique identifier for the settings for one watermark. The value of Id can be up to 40 characters long. You can specify settings for up to four watermarks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Height</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum height of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Width</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum width of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Opacity</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A percentage that indicates how much you want a watermark to obscure the video in the location where it appears.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sizing<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A value that determines how Elastic Transcoder interprets values that you specified for `video_watermarks.horizontal_offset`, `video_watermarks.vertical_offset`, `video_watermarks.max_width`, and `video_watermarks.max_height`. Valid values are `Content` and `Frame`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vertical<wbr>Align</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The vertical position of the watermark unless you specify a nonzero value for `vertical_align`. Valid values are `Top`, `Bottom`, `Center`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vertical<wbr>Offset</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount by which you want the vertical position of the watermark to be offset from the position specified by `vertical_align`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Horizontal<wbr>Align</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The horizontal position of the watermark unless you specify a nonzero value for `horzontal_offset`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Horizontal<wbr>Offset</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount by which you want the horizontal position of the watermark to be offset from the position specified by `horizontal_align`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique identifier for the settings for one watermark. The value of Id can be up to 40 characters long. You can specify settings for up to four watermarks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Height</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum height of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Width</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum width of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Opacity</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A percentage that indicates how much you want a watermark to obscure the video in the location where it appears.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sizing<wbr>Policy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A value that determines how Elastic Transcoder interprets values that you specified for `video_watermarks.horizontal_offset`, `video_watermarks.vertical_offset`, `video_watermarks.max_width`, and `video_watermarks.max_height`. Valid values are `Content` and `Frame`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vertical<wbr>Align</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The vertical position of the watermark unless you specify a nonzero value for `vertical_align`. Valid values are `Top`, `Bottom`, `Center`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vertical<wbr>Offset</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount by which you want the vertical position of the watermark to be offset from the position specified by `vertical_align`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">horizontal<wbr>Align</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The horizontal position of the watermark unless you specify a nonzero value for `horzontal_offset`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">horizontal<wbr>Offset</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount by which you want the horizontal position of the watermark to be offset from the position specified by `horizontal_align`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique identifier for the settings for one watermark. The value of Id can be up to 40 characters long. You can specify settings for up to four watermarks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Height</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum height of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Width</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum width of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">opacity</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A percentage that indicates how much you want a watermark to obscure the video in the location where it appears.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sizing<wbr>Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A value that determines how Elastic Transcoder interprets values that you specified for `video_watermarks.horizontal_offset`, `video_watermarks.vertical_offset`, `video_watermarks.max_width`, and `video_watermarks.max_height`. Valid values are `Content` and `Frame`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vertical<wbr>Align</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The vertical position of the watermark unless you specify a nonzero value for `vertical_align`. Valid values are `Top`, `Bottom`, `Center`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vertical<wbr>Offset</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount by which you want the vertical position of the watermark to be offset from the position specified by `vertical_align`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">horizontal<wbr>Align</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The horizontal position of the watermark unless you specify a nonzero value for `horzontal_offset`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">horizontal<wbr>Offset</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount by which you want the horizontal position of the watermark to be offset from the position specified by `horizontal_align`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique identifier for the settings for one watermark. The value of Id can be up to 40 characters long. You can specify settings for up to four watermarks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Height</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum height of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Width</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum width of the watermark.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">opacity</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A percentage that indicates how much you want a watermark to obscure the video in the location where it appears.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sizing<wbr>Policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A value that controls scaling of the watermark. Valid values are: `Fit`, `Stretch`, `ShrinkToFit`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A value that determines how Elastic Transcoder interprets values that you specified for `video_watermarks.horizontal_offset`, `video_watermarks.vertical_offset`, `video_watermarks.max_width`, and `video_watermarks.max_height`. Valid values are `Content` and `Frame`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vertical<wbr>Align</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The vertical position of the watermark unless you specify a nonzero value for `vertical_align`. Valid values are `Top`, `Bottom`, `Center`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vertical<wbr>Offset</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount by which you want the vertical position of the watermark to be offset from the position specified by `vertical_align`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







